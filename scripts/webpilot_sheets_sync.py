#!/usr/bin/env python3
"""
WebPilot – Kunden- & URL-Zentrale (Dual Google Sheets Live-Sync: Partner-Isolation + David Master-Sheet)
========================================================================================================
Synchronisiert alle WebPilot-Vorschauen (Aktiv, Firma/Verein, Einmal-Preis & Score,
Monats-Offerte 1. Jahr / ab 2. Jahr, Preis-Begruendung & Aha-Punkte, Zeigeversion -v2,
Vollversion -vollversion, Studio Cockpit v4.0, Kunden-Cockpit Light, Vorher/Nachher-Report PDF,
klickbare Ursprungs-Webseite Original, Branche & Kontext, Partner, Status & Datum)
parallel in zwei getrennte Google-Tabellen:

1. Jenny Ettle (JE-MI) Partner-Sheet (1O3EqOCqGS5HbE5rWxIBoTk8lLA0a2Pz30F7yKiEbRms):
   - Strikte Mandanten-Trennung: Enthaelt AUSSCHLIESSLICH die Projekte von Jenny Ettle (JE-MI).
2. David Huegli (Magnet XS) Master-Sheet (1horD2vDfLDnVb9SEoBmXc-tjP8auMAMaqfdrb_g-Sho):
   - Enthaelt ALLE aktiven WebPilot-Projekte ueber alle Partner hinweg (David Huegli / IMP GmbH
     sowie alle Projekte von Jenny Ettle / JE-MI), identischer 14-Spalten-Aufbau (A-N) mit
     aktiviertem 1-Klick-Filter auf Spalte M (Partner).

Regel-Konformitaet:
- BACKEND-DB-RULES.md (Canary: BACKEND-DB-2026-V1, #BE-07 Retry & Zero-Silent-Failure)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1, 100 % ss statt Eszett)
- UI-LAYOUT-RULES.md (Canary: UI-LAYOUT-2026-V1, #UI-07 Punkt 3 Maximalwert / 10.0)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import time
import urllib.parse
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests
from google.auth.transport.requests import Request
from google.oauth2 import service_account

JENNY_SPREADSHEET_ID = "1O3EqOCqGS5HbE5rWxIBoTk8lLA0a2Pz30F7yKiEbRms"
JENNY_SPREADSHEET_URL = f"https://docs.google.com/spreadsheets/d/{JENNY_SPREADSHEET_ID}/edit"
JENNY_SPREADSHEET_TITLE = "WebPilot – Kunden- & URL-Zentrale (Jenny Ettle · JE-MI)"

DAVID_SPREADSHEET_ID = "1horD2vDfLDnVb9SEoBmXc-tjP8auMAMaqfdrb_g-Sho"
DAVID_SPREADSHEET_URL = f"https://docs.google.com/spreadsheets/d/{DAVID_SPREADSHEET_ID}/edit"
DAVID_SPREADSHEET_TITLE = "WebPilot – Master-Kunden- & URL-Zentrale (David Hügli · Alle Partner)"

DEFAULT_SPREADSHEET_ID = JENNY_SPREADSHEET_ID
DEFAULT_SPREADSHEET_URL = JENNY_SPREADSHEET_URL
DEFAULT_TAB_TITLE = "Kunden & URL-Zentrale"

MONTHLY_YEAR2_CHF = 35
MONTHLY_SMART_PRO_YEAR2_CHF = 45
MONTHLY_PLAN_LABEL = "CHF 35.— / Mt. (Basis: Hosting, Cockpit & SEO-/KI-Such-Autopilot) bzw. CHF 45.— / Mt. (Smart-Pro: inkl. aktivem Formular-, E-Mail-, 1-Seiten-A4-PDF- & WhatsApp-Service, statt CHF 295.—/Mt. bei separaten Formular-Anbietern)"

PARTNER_SHEET_OWNER = "jenny"

# Interne Alt-/Referenz-Slugs aus frueheren ACP-Tests (weder in Jennys noch in Davids Agentur-Sheet)
EXCLUDED_INTERNAL_SLUGS = {
    "hiltbrand",
    "birchmeier",
    "hochuli",
    "preview-birchmeier",
    "preview-hiltbrand",
    "preview-hochuli",
}

# Fuer Jennys Partner-Sheet zusaetzlich alle Nicht-Jenny-Slugs ausschliessen
EXCLUDED_PARTNER_SLUGS = EXCLUDED_INTERNAL_SLUGS | {
    "holz-susi",
    "preview-holz-susi",
    "imp-marketing",
    "preview-imp-marketing",
}

SA_PATHS = [
    "/home/brainuser/.config/gcloud/legacy_credentials/pro-0396-acp-authen-cont-pilot@appspot.gserviceaccount.com/adc.json",
    r"C:\Users\Daviduserich\AppData\Roaming\gcloud\legacy_credentials\pro-0396-acp-authen-cont-pilot@appspot.gserviceaccount.com\adc.json",
]

PARTNER_CONFIG_PATHS = [
    Path("/home/brainuser/vault-plain/10-Projects/WebPilot-Pro0416/03-Fulfillment/partner_config.json"),
    Path("/home/brainuser/workspaces/mxs-embed/config/partner_config.json"),
]

HEADERS = [
    "Aktiv",
    "Firma / Verein",
    "Einmal-Preis & Score",
    "Monats-Offerte (1. Jahr / ab 2. Jahr)",
    "Preis-Begründung & Aha-Punkte",
    "Zeigeversion (-v2 für Kunden)",
    "Vollversion (-vollversion für uns)",
    "Studio Cockpit v4.0",
    "Kunden-Cockpit Light (Nur Texte)",
    "Vorher/Nachher-Report (PDF)",
    "Ursprungs-Webseite (Original)",
    "Branche & Kontext",
    "Partner",
    "Eingereicht am (Datum & Uhrzeit)",
    "Status & Fertigstellung",
]


def format_ch_datetime(raw_ts: Any, fallback: str = "") -> str:
    s = str(raw_ts or "").strip()
    if not s:
        return fallback
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})[T\s](\d{2}):(\d{2})", s)
    if m:
        yyyy, mm, dd, hh, mi = m.groups()
        return f"{dd}.{mm}.{yyyy} · {hh}:{mi} Uhr"
    if "Uhr" in s:
        return s
    return s


def parse_chf_amount(chf_str: Any, fallback: int = 1800) -> int:
    if isinstance(chf_str, (int, float)):
        return int(chf_str)
    s = str(chf_str or "")
    s_clean = s.split("\n")[0]
    digits = re.sub(r"[^0-9]", "", s_clean)
    return int(digits) if digits else fallback


def format_chf(amount: int) -> str:
    s = f"{int(amount):,}".replace(",", "'")
    return f"CHF {s}.—"


def compute_monthly_pricing(recommended_chf: Any) -> Dict[str, Any]:
    einmalig = parse_chf_amount(recommended_chf, fallback=1800)
    year1 = int(round((einmalig / 12.0 + MONTHLY_YEAR2_CHF) / 5.0) * 5)
    year1_pro = year1 + 10
    year2 = MONTHLY_YEAR2_CHF
    year2_pro = MONTHLY_SMART_PRO_YEAR2_CHF
    return {
        "monthly_year1_chf": year1,
        "monthly_year1_pro_chf": year1_pro,
        "monthly_year2_chf": year2,
        "monthly_year2_pro_chf": year2_pro,
        "monthly_plan_label": MONTHLY_PLAN_LABEL,
        "monthly_display": f"1. Jahr: CHF {year1}.—/Mt. (Smart-Pro: CHF {year1_pro}.—/Mt.) · ab 2. Jahr: CHF 35.— / 45.— Mt.",
        "monthly_sheet_display": (
            f"1. Jahr: CHF {year1}.— / Mt. Basis (CHF {year1_pro}.— / Mt. Smart-Pro)\n"
            f"Ab 2. Jahr: CHF 35.— / Mt. (Basis: Hosting, Cockpit & SEO-/KI-Such-Autopilot) bzw. CHF 45.— / Mt. (Smart-Pro: inkl. aktivem Formular-, E-Mail-, 1-Seiten-A4-PDF- & WhatsApp-Service, statt CHF 295.—/Mt. bei separaten Formular-Anbietern)\n"
            f"Individuelle Formular-Anpassungen (massgeschneiderte Fragen, zusätzliche Formulare oder Empfänger-Weichen) richten wir auf Wunsch gerne im Rahmen der Offerte passgenau für Sie ein."
        ),
    }


def format_einmal_price_sheet_cell(recommended_chf: str, complexity_score: str, formula_chf: str) -> str:
    rec = (recommended_chf or "CHF 1'800.—").splitlines()[0].replace(" einmalig", "").strip()
    score = (complexity_score or "5.0 / 10.0").strip()
    form = (formula_chf or rec).strip()
    return (
        f"{rec} einmalig\n"
        f"+ CHF 35.— / Mt. (Basis) bzw. CHF 45.— / Mt. (Smart-Pro inkl. Formular/PDF/E-Mail statt CHF 295.—/Mt.)\n"
        f"Score: {score} · Formel: {form}"
    )


def split_source_and_context(raw_source_or_context: str, explicit_context: str = "") -> Tuple[str, str]:
    raw = (raw_source_or_context or "").strip()
    ctx = (explicit_context or "").strip()
    url_match = re.search(r"https?://[^\s–]+", raw)
    extracted_url = url_match.group(0).strip() if url_match else ""
    if extracted_url:
        rest = raw.replace(extracted_url, "").strip(" –-·:")
        final_ctx = ctx or rest
        return extracted_url, final_ctx
    return "", (ctx or raw)


# Kanonische Projektliste fuer Dual-Sync:
# - In Davids Master-Sheet erscheinen ALLE 9 Projekte (IMP GmbH an Position 1 + alle 8 Projekte von Jenny Ettle).
# - In Jennys Partner-Sheet erscheinen ausschliesslich die 8 Projekte mit Partner "Jenny Ettle (JE-MI)".
SEED_PROJECTS = [
    {
        "slug": "holz-susi",
        "active": True,
        "company": "Holz-Susi GmbH · Susanne «Susi» Schmid (Frick AG)",
        "pricing_recommended_chf": "CHF 2'100.—",
        "complexity_score": "4.6 / 10.0",
        "pricing_formula_chf": "CHF 2'050.—",
        "pricing_rationale": "Authentischer 5-Seiten-Holzbau- & Zimmerei-Auftritt (Startbühne, Leistungen, Referenzen mit 8 Vorher/Nachher-Projekten, Über uns & Kontakt) inkl. interaktivem Holzbau- & Dach-Berater, 3-Schritte Smart-Anfrage sowie Studio Cockpit v4.0 + Light.",
        "v2_url": "https://vorschau.magnet-xs.ch/holz-susi-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/holz-susi-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/holz-susi-vollversion/cockpit.html?token=holzsusi2026",
        "cockpit_light_url": "https://vorschau.magnet-xs.ch/holz-susi-vollversion/cockpit.html?token=holz-susi2026&mode=light",
        "audit_report_url": "https://vorschau.magnet-xs.ch/reports/holz-susi-vorher-nachher-report.pdf",
        "source_url": "https://holz-susi.ch/",
        "branch_context": "Holzbau & Zimmerei im Fricktal (Dachsanierung, Dachfenster, Innenausbau, Terrassen, Bauleitung & Rückbau) in Frick AG",
        "partner": "David Hügli (Magnet XS)",
        "status": "🟢 Bereit zum Zeigen (09.11.2026)",
    },
    {
        "slug": "imp-marketing",
        "active": True,
        "company": "IMP GmbH · Matthias Iseli (Schreinerei-Marketing)",
        "pricing_recommended_chf": "CHF 2'400.—",
        "complexity_score": "4.8 / 10.0",
        "pricing_formula_chf": "CHF 2'150.—",
        "pricing_rationale": "Spezialisierter 5-Seiten-B2B-Auftritt für Schreinerei- & Holzbau-Marketing inkl. 16 Prozess-Visuals, interaktivem Schreinerei-Potenzial-Rechner, 6 Fach-FAQs und 3-Schritte Smart-Anfrage. Durch ein einziges gewonnenes Schreinerei-Mandat mehrfach refinanziert.",
        "v2_url": "https://vorschau.magnet-xs.ch/imp-marketing-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/imp-marketing-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/imp-marketing-vollversion/cockpit.html?token=impmarketing2026",
        "cockpit_light_url": "https://vorschau.magnet-xs.ch/imp-marketing-vollversion/cockpit.html?token=imp-marketing2026&mode=light",
        "audit_report_url": "https://vorschau.magnet-xs.ch/reports/imp-marketing-vorher-nachher-report.pdf",
        "source_url": "https://imp-marketing.ch/",
        "branch_context": "Sichtbarkeits-Systeme & Anfrage-Vorqualifizierung für Schreinereien & Holzbau (1–15 Mitarbeitende) in Obersteckholz BE",
        "partner": "David Hügli (Magnet XS)",
        "status": "🟢 Bereit zum Zeigen (05.11.2026)",
    },
    {
        "slug": "joma",
        "active": True,
        "company": "JOMA Solar GmbH (Wettingen AG)",
        "pricing_recommended_chf": "CHF 2'200.—",
        "complexity_score": "4.8 / 10.0",
        "pricing_formula_chf": "CHF 2'150.—",
        "pricing_rationale": "Umfangreiche Solar- & Speicher-Plattform (Privatkunden, Gewerbekunden, Batteriespeicher, Grossanlagen, Contracting, 7 Referenzprojekte inkl. Video-Fallstudie & 5er-Team) inkl. interaktivem Solar-Rechner.",
        "v2_url": "https://vorschau.magnet-xs.ch/joma-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/joma-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/joma-vollversion/cockpit.html?token=joma2026",
        "cockpit_light_url": "https://vorschau.magnet-xs.ch/joma-vollversion/cockpit.html?token=joma2026&mode=light",
        "audit_report_url": "https://vorschau.magnet-xs.ch/reports/joma-vorher-nachher-report.pdf",
        "source_url": "https://www.joma-solar.ch/",
        "branch_context": "Photovoltaik, Batteriespeicher, Solar Manager, ZEV & Contracting in Wettingen AG",
        "partner": "Jenny Ettle (JE-MI)",
        "status": "🟢 Bereit zum Zeigen (05.11.2026)",
    },
    {
        "slug": "herzensarbeit",
        "active": True,
        "company": "Herzensarbeit · Anne-Katrin Koch (Härkingen SO)",
        "pricing_recommended_chf": "CHF 1'500.—",
        "complexity_score": "3.5 / 10.0",
        "pricing_formula_chf": "CHF 1'650.—",
        "pricing_rationale": "Kompakte 5-Seiten-Praxiswebseite (Coaching & Kinesiologie) mit ca. 15 Bildern und Workshop-Sektion. Durch einen einzigen ausgebuchten Workshop (8 Teilnehmende) bereits zu 100 % amortisiert.",
        "v2_url": "https://vorschau.magnet-xs.ch/herzensarbeit-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/herzensarbeit-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/herzensarbeit-vollversion/cockpit?token=herzensarbeit2026",
        "cockpit_light_url": "https://vorschau.magnet-xs.ch/herzensarbeit-vollversion/cockpit.html?token=herzensarbeit2026&mode=light",
        "source_url": "https://herzensarbeit.ch/",
        "branch_context": "Paartherapie, Trennungsberatung, Trauerbegleitung & Frauen-Workshops in Härkingen SO",
        "partner": "Jenny Ettle (JE-MI)",
        "status": "🟢 Bereit zum Zeigen (05.11.2026)",
    },
    {
        "slug": "frees",
        "active": True,
        "company": "Free's Stefan Fritschi (Niederrohrdorf)",
        "pricing_recommended_chf": "CHF 1'500.—",
        "complexity_score": "3.2 / 10.0",
        "pricing_formula_chf": "CHF 1'550.—",
        "pricing_rationale": "Schlanke 5-Seiten-Gewerbeseite (Teamsport & Textildruck) mit 14 extern verlinkten Marken-Katalogen ohne komplexes Daten-Backend. Perfekter Einstiegs-Sweet-Spot für sofortige Zusage.",
        "v2_url": "https://vorschau.magnet-xs.ch/frees-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/frees-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/frees-vollversion/cockpit?token=frees2026",
        "cockpit_light_url": "https://vorschau.magnet-xs.ch/frees-vollversion/cockpit.html?token=frees2026&mode=light",
        "source_url": "https://www.frees.ch/",
        "branch_context": "Studio für Textildesign, Textildruck, Stickerei, Teamsport & Promowear in Niederrohrdorf AG",
        "partner": "Jenny Ettle (JE-MI)",
        "status": "🟢 Bereit zum Zeigen (04.11.2026)",
    },
    {
        "slug": "innere-staerke",
        "active": True,
        "company": "Wüest + Paneduro · Innere Stärke (Sursee)",
        "pricing_recommended_chf": "CHF 2'200.—",
        "complexity_score": "4.2 / 10.0",
        "pricing_formula_chf": "CHF 1'900.—",
        "pricing_rationale": "5-Seiten-Auftritt für 2 Partnerinnen im B2B-Führungskräfte-Coaching inkl. Buch-Integration. Hoher Kundenwert pro B2B-Mandat rechtfertigt CHF 2'200.— mühelos.",
        "v2_url": "https://vorschau.magnet-xs.ch/innere-staerke-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/innere-staerke-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/innere-staerke-vollversion/cockpit?token=innerestaerke2026",
        "cockpit_light_url": "https://vorschau.magnet-xs.ch/innere-staerke-vollversion/cockpit.html?token=innere-staerke2026&mode=light",
        "source_url": "https://www.innere-staerke.business/",
        "branch_context": "Führungskräfte-Training, Resilienz & Persönlichkeitsentwicklung in Sursee LU",
        "partner": "Jenny Ettle (JE-MI)",
        "status": "🟢 Bereit zum Zeigen (04.11.2026)",
    },
    {
        "slug": "fcschlieren",
        "active": True,
        "company": "FC Schlieren (33 Teams)",
        "pricing_recommended_chf": "CHF 4'500.—",
        "complexity_score": "9.4 / 10.0",
        "pricing_formula_chf": "CHF 4'300.—",
        "pricing_rationale": "Grossverein im Raum Zürich (über 20 Teams, hunderte Spieler-/Kaderdaten, Sponsoren-Architektur & Team-Onboarding-Engine). Gegenüber einer klassischen 12'000-Franken-Agenturofferte extrem attraktiv.",
        "v2_url": "https://vorschau.magnet-xs.ch/fcschlieren-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/fcschlieren-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/fcschlieren-vollversion/cockpit?token=fcschlieren2026",
        "cockpit_light_url": "https://vorschau.magnet-xs.ch/fcschlieren-vollversion/cockpit.html?token=fcschlieren2026&mode=light",
        "source_url": "https://www.fcschlieren.ch/",
        "branch_context": "Fussballclub Schlieren ZH (33 Teams, Sponsoren-Matrix & Team-Hub)",
        "partner": "Jenny Ettle (JE-MI)",
        "status": "🟢 Bereit zum Zeigen (04.11.2026)",
    },
    {
        "slug": "scfulenbach",
        "active": True,
        "company": "SC Fulenbach (14 Teams)",
        "pricing_recommended_chf": "CHF 4'200.—",
        "complexity_score": "8.5 / 10.0",
        "pricing_formula_chf": "CHF 3'850.—",
        "pricing_rationale": "Traditionsverein mit breiter Aktiv-/Junioren-Struktur, Sponsoren-Matrix, Vereinschronik und dezentralem Team-Onboarding-Formular.",
        "v2_url": "https://vorschau.magnet-xs.ch/scfulenbach-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/scfulenbach-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/scfulenbach-vollversion/cockpit?token=scfulenbach2026",
        "cockpit_light_url": "https://vorschau.magnet-xs.ch/scfulenbach-vollversion/cockpit.html?token=scfulenbach2026&mode=light",
        "source_url": "https://www.scfulenbach.ch/",
        "branch_context": "Sportclub Fulenbach SO (14 Teams, Vereinsleben & Sponsoren)",
        "partner": "Jenny Ettle (JE-MI)",
        "status": "🟢 Bereit zum Zeigen (04.11.2026)",
    },
    {
        "slug": "fcattiswil",
        "active": True,
        "company": "FC Attiswil (14 Teams)",
        "pricing_recommended_chf": "CHF 3'900.—",
        "complexity_score": "8.2 / 10.0",
        "pricing_formula_chf": "CHF 3'700.—",
        "pricing_rationale": "Fussballverein mit vielen Mannschaften, Junioren, Sponsoren-Präsenz & 5-Blöcke Team-Einreichungs-Engine. Ein einziger neuer Hauptsponsor refinanziert bereits die halbe Webseite.",
        "v2_url": "https://vorschau.magnet-xs.ch/fcattiswil-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/fcattiswil-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/fcattiswil-vollversion/cockpit?token=fcattiswil2026",
        "cockpit_light_url": "https://vorschau.magnet-xs.ch/fcattiswil-vollversion/cockpit.html?token=fcattiswil2026&mode=light",
        "source_url": "https://www.fcattiswil.ch/",
        "branch_context": "Fussballclub Attiswil BE (14 Teams, Junioren & Sponsoren)",
        "partner": "Jenny Ettle (JE-MI)",
        "status": "🟢 Bereit zum Zeigen (04.11.2026)",
    },
    {
        "slug": "her11",
        "active": True,
        "company": "HER11 (Jenny Ettle)",
        "pricing_recommended_chf": "CHF 2'800.—",
        "complexity_score": "5.8 / 10.0",
        "pricing_formula_chf": "CHF 2'600.—",
        "pricing_rationale": "Gehobene Marken- & Lookbook-Inszenierung mit hoher Bilddichte und laufendem Kollektions-Wechsel über das Studio Cockpit v4.0.",
        "v2_url": "https://vorschau.magnet-xs.ch/her11-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/her11-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/her11-vollversion/cockpit?token=her112026",
        "cockpit_light_url": "https://vorschau.magnet-xs.ch/her11-vollversion/cockpit.html?token=her112026&mode=light",
        "source_url": "https://www.her11.ch/",
        "branch_context": "HER11 Frauenfussball & Sport-Marketing (Jenny Ettle / JE-MI)",
        "partner": "Jenny Ettle (JE-MI)",
        "status": "🟢 Bereit zum Zeigen (30.10.2026)",
    },
]


def _enrich_pricing_dict(base: Dict[str, Any]) -> Dict[str, Any]:
    rec = base["pricing_recommended_chf"]
    score = base["complexity_score"]
    form = base["pricing_formula_chf"]
    m_info = compute_monthly_pricing(rec)
    out = dict(base)
    out.update(m_info)
    out["pricing_display"] = format_einmal_price_sheet_cell(rec, score, form)
    return out


def estimate_project_pricing(slug: str, company_name: str = "", summary: str = "") -> Dict[str, Any]:
    """Berechnet 2-stufige Preisempfehlung + 2-Wege-Offerten-Modell (Einmalig vs. 1. Jahr / ab 2. Jahr Monats-Offerte)."""
    clean_slug = re.sub(r"-(?:vollversion|vv|v1|v2)$", "", (slug or "").strip().lower().replace("preview-", ""))
    for item in SEED_PROJECTS:
        if item["slug"] == clean_slug:
            return _enrich_pricing_dict({
                "complexity_score": item["complexity_score"],
                "pricing_formula_chf": item["pricing_formula_chf"],
                "pricing_recommended_chf": item["pricing_recommended_chf"],
                "pricing_rationale": item["pricing_rationale"],
            })

    text_blob = f"{clean_slug} {company_name} {summary}".lower()
    if any(k in text_blob for k in ("fc ", "sc ", "fussball", "verein", "club", "teams", "junioren")):
        return _enrich_pricing_dict({
            "complexity_score": "8.4 / 10.0",
            "pricing_formula_chf": "CHF 3'800.—",
            "pricing_recommended_chf": "CHF 3'900.—",
            "pricing_rationale": "Vereins-Plattform mit Mannschafts-Struktur, Sponsoren-Bühne und dezentralem Team-Onboarding-Formular. Ein neuer Hauptsponsor refinanziert bereits rund 50 %.",
        })
    if any(k in text_blob for k in ("sparten", "bau", "gruppe", "holding", "industrie", "architektur", "immobilien", "rechner")):
        return _enrich_pricing_dict({
            "complexity_score": "7.4 / 10.0",
            "pricing_formula_chf": "CHF 3'300.—",
            "pricing_recommended_chf": "CHF 3'500.—",
            "pricing_rationale": "Mehrsparten- oder Industrie-Webauftritt mit hoher Leistungs- und Projektdichte, interaktiven Anfrage-Modulen und Studio Cockpit v4.0.",
        })
    if any(k in text_blob for k in ("praxis", "therapie", "coaching", "beratung", "studio", "kmu", "textil", "coiffeur", "gewerbe")):
        return _enrich_pricing_dict({
            "complexity_score": "3.6 / 10.0",
            "pricing_formula_chf": "CHF 1'650.—",
            "pricing_recommended_chf": "CHF 1'500.—",
            "pricing_rationale": "Kompakte 5-Seiten-KMU-/Praxis-Webseite inkl. Smart-Anfrage und Studio Cockpit v4.0. Schneller Entscheidungsweg und rasche Amortisation durch 1–2 Neukunden.",
        })
    return _enrich_pricing_dict({
        "complexity_score": "4.8 / 10.0",
        "pricing_formula_chf": "CHF 2'150.—",
        "pricing_recommended_chf": "CHF 2'200.—",
        "pricing_rationale": "Mehrseitiger Schweizer KMU-Auftritt (5 Seiten) inkl. Smart-Anfrage-Assistent, Zeige- & Vollversion sowie Studio Cockpit v4.0 auf Swiss Edge.",
    })


def get_sheet_config() -> Dict[str, str]:
    for p in PARTNER_CONFIG_PATHS:
        if p.exists():
            try:
                cfg = json.loads(p.read_text(encoding="utf-8"))
                sid = str(cfg.get("google_sheet_id") or JENNY_SPREADSHEET_ID).strip()
                surl = str(cfg.get("google_sheet_url") or f"https://docs.google.com/spreadsheets/d/{sid}/edit").strip()
                did = str(cfg.get("david_google_sheet_id") or DAVID_SPREADSHEET_ID).strip()
                durl = str(cfg.get("david_google_sheet_url") or f"https://docs.google.com/spreadsheets/d/{did}/edit").strip()
                return {
                    "spreadsheet_id": sid,
                    "spreadsheet_url": surl,
                    "david_spreadsheet_id": did,
                    "david_spreadsheet_url": durl,
                }
            except Exception:
                pass
    return {
        "spreadsheet_id": JENNY_SPREADSHEET_ID,
        "spreadsheet_url": JENNY_SPREADSHEET_URL,
        "david_spreadsheet_id": DAVID_SPREADSHEET_ID,
        "david_spreadsheet_url": DAVID_SPREADSHEET_URL,
    }


def _get_auth_headers() -> Dict[str, str]:
    for sa_path in SA_PATHS:
        if os.path.exists(sa_path):
            creds = service_account.Credentials.from_service_account_file(
                sa_path,
                scopes=["https://www.googleapis.com/auth/spreadsheets"],
            )
            creds.refresh(Request())
            return {
                "Authorization": f"Bearer {creds.token}",
                "Content-Type": "application/json",
            }
    raise RuntimeError("Keine Google Service-Account-Credentials (adc.json) gefunden.")


def _request_with_retry(method: str, url: str, **kwargs) -> requests.Response:
    """Adaptive Retry-Schleife gemaess #BE-07."""
    last_exc = None
    for attempt in range(3):
        try:
            headers = _get_auth_headers()
            r = requests.request(method, url, headers=headers, timeout=25, **kwargs)
            if r.status_code < 500 and r.status_code != 429:
                return r
            last_exc = RuntimeError(f"HTTP {r.status_code}: {r.text[:300]}")
        except Exception as exc:
            last_exc = exc
        time.sleep(1.2 * (attempt + 1))
    if last_exc:
        raise last_exc
    raise RuntimeError("Request fehlgeschlagen.")


def _get_first_sheet_meta(spreadsheet_id: str) -> Dict[str, Any]:
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}"
    r = _request_with_retry("GET", url, params={"fields": "properties.title,sheets.properties(sheetId,title,gridProperties)"})
    r.raise_for_status()
    data = r.json()
    sheets = data.get("sheets") or []
    if not sheets:
        raise RuntimeError("Keine Tabellenblaetter im Spreadsheet gefunden.")
    return sheets[0]["properties"]


def apply_sheet_formatting(
    spreadsheet_id: str,
    sheet_id: int,
    current_title: str,
    total_rows: int = 100,
    spreadsheet_doc_title: Optional[str] = None,
) -> None:
    """Wendet Header-Fixierung, Auto-Filter, echte BOOLEAN-Checkboxen, blaue Link-Spalten & Spaltenbreiten (A-N) an."""
    requests_list: List[Dict[str, Any]] = []
    num_cols = len(HEADERS)  # 14 Spalten (A bis N)

    if spreadsheet_doc_title:
        requests_list.append({
            "updateSpreadsheetProperties": {
                "properties": {
                    "title": spreadsheet_doc_title,
                },
                "fields": "title",
            }
        })

    # 1. Tab-Name auf 'Kunden & URL-Zentrale' setzen + Zeile 1 fixieren
    requests_list.append({
        "updateSheetProperties": {
            "properties": {
                "sheetId": sheet_id,
                "title": DEFAULT_TAB_TITLE,
                "gridProperties": {
                    "frozenRowCount": 1,
                },
            },
            "fields": "title,gridProperties.frozenRowCount",
        }
    })

    # 2. Header-Zeile (Zeile 1): Dunkles Slate (#0F172A), weisse fette Schrift
    requests_list.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 0,
                "endColumnIndex": num_cols,
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.059, "green": 0.090, "blue": 0.165},
                    "textFormat": {
                        "bold": True,
                        "underline": False,
                        "fontSize": 10,
                        "foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0},
                    },
                    "horizontalAlignment": "LEFT",
                    "verticalAlignment": "MIDDLE",
                    "wrapStrategy": "WRAP",
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,wrapStrategy)",
        }
    })

    requests_list.append({
        "updateDimensionProperties": {
            "range": {
                "sheetId": sheet_id,
                "dimension": "ROWS",
                "startIndex": 0,
                "endIndex": 1,
            },
            "properties": {"pixelSize": 38},
            "fields": "pixelSize",
        }
    })

    # 3. Daten-Zeilen (A2:N100): Grundformatierung (Textumbruch, vertikale Zentrierung, Reset alter Link-Stile)
    requests_list.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 1,
                "endRowIndex": max(total_rows, 100),
                "startColumnIndex": 0,
                "endColumnIndex": max(num_cols, 16),
            },
            "cell": {
                "userEnteredFormat": {
                    "verticalAlignment": "MIDDLE",
                    "wrapStrategy": "WRAP",
                    "textFormat": {
                        "fontSize": 10,
                        "bold": False,
                        "underline": False,
                        "foregroundColor": {"red": 0.059, "green": 0.090, "blue": 0.165},
                    },
                }
            },
            "fields": "userEnteredFormat(verticalAlignment,wrapStrategy,textFormat(fontSize,bold,underline,foregroundColor))",
        }
    })

    # 4a. Leere Checkboxen unterhalb der belegten Zeilen bereinigen
    requests_list.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": max(2, total_rows),
                "endRowIndex": 200,
                "startColumnIndex": 0,
                "endColumnIndex": 1,
            },
            "cell": {
                "dataValidation": None,
            },
            "fields": "dataValidation",
        }
    })

    # 4b. Echte interaktive Google-Sheets-Checkboxen exakt auf den belegten Zeilen in Spalte A
    requests_list.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 1,
                "endRowIndex": max(2, total_rows),
                "startColumnIndex": 0,
                "endColumnIndex": 1,
            },
            "cell": {
                "dataValidation": {
                    "condition": {"type": "BOOLEAN"},
                    "showCustomUi": True,
                },
                "userEnteredFormat": {
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE",
                },
            },
            "fields": "dataValidation,userEnteredFormat(horizontalAlignment,verticalAlignment)",
        }
    })

    # 5a. Spalte B (Firma / Verein), Spalte C (Einmal-Preis & Score) & Spalte D (Monats-Offerte) fett formatieren
    requests_list.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 1,
                "endRowIndex": max(total_rows, 100),
                "startColumnIndex": 1,
                "endColumnIndex": 4,
            },
            "cell": {
                "userEnteredFormat": {
                    "textFormat": {
                        "bold": True,
                        "underline": False,
                        "fontSize": 10,
                        "foregroundColor": {"red": 0.059, "green": 0.090, "blue": 0.165},
                    },
                }
            },
            "fields": "userEnteredFormat.textFormat(bold,underline,fontSize,foregroundColor)",
        }
    })

    # 5b. URL-Spalten F bis K (Index 5..11: v2, Vollversion, Cockpit, Cockpit Light, PDF, Ursprungs-Webseite) explizit blau & unterstrichen (#1d4ed8)
    requests_list.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 1,
                "endRowIndex": max(total_rows, 100),
                "startColumnIndex": 5,
                "endColumnIndex": 11,
            },
            "cell": {
                "userEnteredFormat": {
                    "textFormat": {
                        "bold": False,
                        "underline": True,
                        "fontSize": 10,
                        "foregroundColor": {"red": 0.114, "green": 0.306, "blue": 0.847},
                    },
                }
            },
            "fields": "userEnteredFormat.textFormat(bold,underline,fontSize,foregroundColor)",
        }
    })

    # 5c. Spalte M (Partner, Index 12) fett hervorheben fuer schnelle Filterung
    requests_list.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 1,
                "endRowIndex": max(total_rows, 100),
                "startColumnIndex": 12,
                "endColumnIndex": 13,
            },
            "cell": {
                "userEnteredFormat": {
                    "textFormat": {
                        "bold": True,
                        "underline": False,
                        "fontSize": 10,
                        "foregroundColor": {"red": 0.059, "green": 0.090, "blue": 0.165},
                    },
                }
            },
            "fields": "userEnteredFormat.textFormat(bold,underline,fontSize,foregroundColor)",
        }
    })

    # 6. Auto-Filter (BasicFilter) ueber A1:N100 aktivieren (inkl. Spalte M Partner)
    requests_list.append({
        "setBasicFilter": {
            "filter": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": 0,
                    "endRowIndex": max(total_rows, 100),
                    "startColumnIndex": 0,
                    "endColumnIndex": num_cols,
                }
            }
        }
    })

    # 7. Optimale Spaltenbreiten (A bis N)
    col_widths = [
        (0, 1, 75),     # A: Aktiv
        (1, 2, 260),    # B: Firma / Verein
        (2, 3, 260),    # C: Einmal-Preis & Score
        (3, 4, 275),    # D: Monats-Offerte (1. Jahr / ab 2. Jahr)
        (4, 5, 370),    # E: Preis-Begruendung & Aha-Punkte
        (5, 6, 300),    # F: Zeigeversion (-v2)
        (6, 7, 320),    # G: Vollversion (-vollversion)
        (7, 8, 380),    # H: Studio Cockpit v4.0
        (8, 9, 410),    # I: Kunden-Cockpit Light (Nur Texte)
        (9, 10, 380),   # J: Vorher/Nachher-Report (PDF)
        (10, 11, 260),  # K: Ursprungs-Webseite (Original)
        (11, 12, 320),  # L: Branche & Kontext
        (12, 13, 195),  # M: Partner (Filterbar per 1 Klick!)
        (13, 14, 210),  # N: Eingereicht am (Datum & Uhrzeit)
        (14, 15, 290),  # O: Status & Fertigstellung
    ]
    for start_col, end_col, px in col_widths:
        requests_list.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": sheet_id,
                    "dimension": "COLUMNS",
                    "startIndex": start_col,
                    "endIndex": end_col,
                },
                "properties": {"pixelSize": px},
                "fields": "pixelSize",
            }
        })

    # 8. Bedingte Formatierung: Wenn Spalte A (Aktiv) = FALSE -> Zeile dezent ausgrauen
    meta_url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}"
    r_cf = _request_with_retry("GET", meta_url, params={"fields": "sheets(properties.sheetId,conditionalFormats)"})
    if r_cf.status_code == 200:
        for sh in r_cf.json().get("sheets", []):
            if sh.get("properties", {}).get("sheetId") == sheet_id:
                existing_rules = sh.get("conditionalFormats") or []
                for idx in range(len(existing_rules) - 1, -1, -1):
                    requests_list.append({
                        "deleteConditionalFormatRule": {
                            "sheetId": sheet_id,
                            "index": idx,
                        }
                    })

    requests_list.append({
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [
                    {
                        "sheetId": sheet_id,
                        "startRowIndex": 1,
                        "endRowIndex": max(total_rows, 100),
                        "startColumnIndex": 0,
                        "endColumnIndex": num_cols,
                    }
                ],
                "booleanRule": {
                    "condition": {
                        "type": "CUSTOM_FORMULA",
                        "values": [{"userEnteredValue": "=$A2=FALSE"}],
                    },
                    "format": {
                        "backgroundColor": {"red": 0.945, "green": 0.961, "blue": 0.976},
                        "textFormat": {
                            "foregroundColor": {"red": 0.580, "green": 0.639, "blue": 0.722},
                        },
                    },
                },
            },
            "index": 0,
        }
    })

    batch_url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}:batchUpdate"
    r_batch = _request_with_retry("POST", batch_url, json={"requests": requests_list})
    r_batch.raise_for_status()


def get_all_rows(spreadsheet_id: str, tab_title: str) -> List[List[str]]:
    safe_range = urllib.parse.quote(f"'{tab_title}'!A1:O200")
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{safe_range}"
    r = _request_with_retry("GET", url)
    r.raise_for_status()
    return r.json().get("values") or []


def _normalize_partner_label(raw_partner: str, slug: str = "") -> str:
    clean_slug = re.sub(r"-(?:vollversion|vv|v1|v2)$", "", (slug or "").strip().lower().replace("preview-", ""))
    if clean_slug in ("imp-marketing", "holz-susi"):
        return "David Hügli (Magnet XS)"
    s = (raw_partner or "").strip()
    low = s.lower()
    if "jenny" in low or "je-mi" in low or "ettle" in low:
        return "Jenny Ettle (JE-MI)"
    if "david" in low or "huegli" in low or "hügli" in low or "magnet" in low:
        return "David Hügli (Magnet XS)"
    return s or "Jenny Ettle (JE-MI)"


def _seed_single_spreadsheet(
    spreadsheet_id: str,
    spreadsheet_url: str,
    doc_title: str,
    owner_filter: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Initialisiert und befuellt ein einzelnes Google Sheet:
    - owner_filter="jenny" -> Nur Jenny-Projekte (strikte Partner-Isolation)
    - owner_filter=None -> Alle Projekte ueber alle Partner hinweg (Davids Master-Sheet)
    """
    props = _get_first_sheet_meta(spreadsheet_id)
    sheet_id = props["sheetId"]
    current_title = props["title"]

    apply_sheet_formatting(
        spreadsheet_id,
        sheet_id,
        current_title,
        total_rows=100,
        spreadsheet_doc_title=doc_title,
    )
    tab_title = DEFAULT_TAB_TITLE

    existing_rows = get_all_rows(spreadsheet_id, tab_title)
    active_by_slug: Dict[str, bool] = {}
    for row in existing_rows[1:]:
        if len(row) >= 3:
            raw_active = str(row[0]).strip().upper()
            is_act = False if raw_active == "FALSE" else True
            row_text = " ".join(row).lower()
            for item in SEED_PROJECTS:
                if item["slug"] in row_text or item["company"].lower() in row_text:
                    active_by_slug[item["slug"]] = is_act

    DEFAULT_SUBMITTED_MAP = {
        "holz-susi": ("09.11.2026 · 13:44 Uhr", "🟢 Bereit zum Zeigen (Fertig: 09.11.2026 · 15:03 Uhr)"),
        "imp-marketing": ("05.11.2026 · 12:35 Uhr", "🟢 Bereit zum Zeigen (Fertig: 05.11.2026 · 13:55 Uhr)"),
        "joma": ("05.11.2026 · 20:54 Uhr", "🟢 Bereit zum Zeigen (Fertig: 05.11.2026 · 21:54 Uhr)"),
        "herzensarbeit": ("05.11.2026 · 11:00 Uhr", "🟢 Bereit zum Zeigen (Fertig: 05.11.2026 · 11:25 Uhr)"),
        "frees": ("03.11.2026 · 21:30 Uhr", "🟢 Bereit zum Zeigen (Fertig: 04.11.2026 · 07:10 Uhr)"),
        "innere-staerke": ("03.11.2026 · 18:30 Uhr", "🟢 Bereit zum Zeigen (Fertig: 04.11.2026 · 07:08 Uhr)"),
        "fcschlieren": ("02.11.2026 · 17:00 Uhr", "🟢 Bereit zum Zeigen (Fertig: 04.11.2026 · 07:12 Uhr)"),
        "scfulenbach": ("02.11.2026 · 17:20 Uhr", "🟢 Bereit zum Zeigen (Fertig: 04.11.2026 · 07:12 Uhr)"),
        "fcattiswil": ("02.11.2026 · 17:40 Uhr", "🟢 Bereit zum Zeigen (Fertig: 04.11.2026 · 07:12 Uhr)"),
        "her11": ("30.10.2026 · 16:00 Uhr", "🟢 Bereit zum Zeigen (Fertig: 30.10.2026 · 19:58 Uhr)"),
    }
    submitted_by_slug: Dict[str, str] = {}
    status_by_slug: Dict[str, str] = {}
    idx_path = Path("/home/brainuser/workspaces/mxs-embed/partner-jobs/index.json")
    if idx_path.exists():
        try:
            for j in json.loads(idx_path.read_text(encoding="utf-8")):
                jslug = str(j.get("slug") or "").strip().lower()
                if jslug and jslug not in EXCLUDED_INTERNAL_SLUGS:
                    if "is_active" in j:
                        active_by_slug[jslug] = bool(j["is_active"])
                    c_at = format_ch_datetime(j.get("created_at"), "")
                    comp_at = format_ch_datetime(j.get("completed_at"), "")
                    if c_at:
                        submitted_by_slug[jslug] = c_at
                    if comp_at and str(j.get("status") or "").lower() == "completed":
                        status_by_slug[jslug] = f"🟢 Bereit zum Zeigen (Fertig: {comp_at})"
                    elif c_at and str(j.get("status") or "").lower() != "completed":
                        status_by_slug[jslug] = f"⏳ In Arbeit (Eingereicht: {c_at})"
        except Exception:
            pass

    values_matrix: List[List[Any]] = [HEADERS]
    for item in SEED_PROJECTS:
        slug = item["slug"]
        if slug in EXCLUDED_INTERNAL_SLUGS:
            continue
        partner_label = _normalize_partner_label(item.get("partner", ""), slug=slug)
        if owner_filter and owner_filter.lower() not in partner_label.lower():
            continue

        is_active = active_by_slug.get(slug, item.get("active", True))
        def_sub, def_stat = DEFAULT_SUBMITTED_MAP.get(slug, ("05.11.2026 · 12:00 Uhr", item["status"]))
        submitted_str = submitted_by_slug.get(slug) or item.get("submitted_at") or def_sub
        status_str = status_by_slug.get(slug) or def_stat
        audit_pdf_url = item.get("audit_report_url") or f"https://vorschau.magnet-xs.ch/reports/{slug}-vorher-nachher-report.pdf"
        cockpit_light_url = item.get("cockpit_light_url") or f"https://vorschau.magnet-xs.ch/{slug}-vollversion/cockpit.html?token={slug}2026&mode=light"
        einmal_cell = format_einmal_price_sheet_cell(
            item["pricing_recommended_chf"],
            item["complexity_score"],
            item["pricing_formula_chf"],
        )
        m_info = compute_monthly_pricing(item["pricing_recommended_chf"])
        values_matrix.append([
            is_active,
            item["company"],
            einmal_cell,
            m_info["monthly_sheet_display"],
            item["pricing_rationale"],
            item["v2_url"],
            item["vollversion_url"],
            item["cockpit_url"],
            cockpit_light_url,
            audit_pdf_url,
            item["source_url"],
            item["branch_context"],
            partner_label,
            submitted_str,
            status_str,
        ])

    clear_range = urllib.parse.quote(f"'{tab_title}'!A1:Z100")
    clear_url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{clear_range}:clear"
    _request_with_retry("POST", clear_url, json={})

    safe_range = urllib.parse.quote(f"'{tab_title}'!A1:O{len(values_matrix)}")
    put_url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{safe_range}"
    r_put = _request_with_retry(
        "PUT",
        put_url,
        params={"valueInputOption": "USER_ENTERED"},
        json={"values": values_matrix},
    )
    r_put.raise_for_status()

    apply_sheet_formatting(
        spreadsheet_id,
        sheet_id,
        tab_title,
        total_rows=len(values_matrix),
        spreadsheet_doc_title=doc_title,
    )

    return {
        "ok": True,
        "spreadsheet_id": spreadsheet_id,
        "spreadsheet_url": spreadsheet_url,
        "doc_title": doc_title,
        "tab_title": tab_title,
        "owner_filter": owner_filter or "all_partners",
        "rows_written": len(values_matrix) - 1,
        "columns": len(HEADERS),
    }


def init_and_seed_sheet() -> Dict[str, Any]:
    """Synchronisiert sowohl Jennys isoliertes Partner-Sheet als auch Davids Master-Sheet."""
    cfg = get_sheet_config()
    jenny_res = _seed_single_spreadsheet(
        spreadsheet_id=cfg["spreadsheet_id"],
        spreadsheet_url=cfg["spreadsheet_url"],
        doc_title=JENNY_SPREADSHEET_TITLE,
        owner_filter="jenny",
    )
    david_res = _seed_single_spreadsheet(
        spreadsheet_id=cfg["david_spreadsheet_id"],
        spreadsheet_url=cfg["david_spreadsheet_url"],
        doc_title=DAVID_SPREADSHEET_TITLE,
        owner_filter=None,
    )
    return {
        "ok": True,
        "jenny_partner_sheet": jenny_res,
        "david_master_sheet": david_res,
    }


def _upsert_into_single_sheet(
    spreadsheet_id: str,
    spreadsheet_url: str,
    clean_slug: str,
    company_name: str,
    v2_url: str,
    vollversion_url: str,
    cockpit_url: str,
    cockpit_light_url: str,
    audit_report_url: str,
    parsed_url: str,
    parsed_ctx: str,
    partner_norm: str,
    submitted_at: str,
    status_text: str,
    active: Optional[bool],
    pricing_display: str,
    monthly_sheet_display: str,
    pricing_rationale: str,
    owner_filter: Optional[str] = None,
) -> Dict[str, Any]:
    props = _get_first_sheet_meta(spreadsheet_id)
    sheet_id = props["sheetId"]
    tab_title = props["title"]

    rows = get_all_rows(spreadsheet_id, tab_title)
    if not rows or rows[0] != HEADERS:
        _seed_single_spreadsheet(
            spreadsheet_id=spreadsheet_id,
            spreadsheet_url=spreadsheet_url,
            doc_title=JENNY_SPREADSHEET_TITLE if owner_filter == "jenny" else DAVID_SPREADSHEET_TITLE,
            owner_filter=owner_filter,
        )
        tab_title = DEFAULT_TAB_TITLE
        rows = get_all_rows(spreadsheet_id, tab_title)

    target_row_idx: Optional[int] = None
    existing_row: List[str] = []

    for idx, r in enumerate(rows):
        if idx == 0:
            continue
        row_str = " ".join(r).lower()
        comp_cell = (r[1] if len(r) > 1 else "").strip().lower()
        if (clean_slug and f"/{clean_slug}" in row_str) or (
            company_name and company_name.strip().lower() in comp_cell
        ) or (comp_cell and comp_cell in company_name.strip().lower()):
            target_row_idx = idx + 1
            existing_row = r
            break

    default_audit_url = f"https://vorschau.magnet-xs.ch/reports/{clean_slug}-vorher-nachher-report.pdf" if clean_slug else ""
    default_cockpit_light_url = f"https://vorschau.magnet-xs.ch/{clean_slug}-vollversion/cockpit.html?token={clean_slug}2026&mode=light" if clean_slug else ""

    if target_row_idx is not None:
        prev_active = False if (len(existing_row) > 0 and str(existing_row[0]).strip().upper() == "FALSE") else True
        row_active = prev_active if active is None else bool(active)
        final_company = company_name.strip() or (existing_row[1] if len(existing_row) > 1 else clean_slug)
        final_price = (existing_row[2] if len(existing_row) > 2 and existing_row[2].strip() else pricing_display)
        final_monthly = (existing_row[3] if len(existing_row) > 3 and existing_row[3].strip() else monthly_sheet_display)
        final_rationale = (existing_row[4] if len(existing_row) > 4 and existing_row[4].strip() else pricing_rationale)
        final_v2 = v2_url.strip() if v2_url else (existing_row[5] if len(existing_row) > 5 else "")
        final_voll = vollversion_url.strip() if vollversion_url else (existing_row[6] if len(existing_row) > 6 else "")
        final_cockpit = cockpit_url.strip() if cockpit_url else (existing_row[7] if len(existing_row) > 7 else "")
        final_cockpit_light = cockpit_light_url.strip() if cockpit_light_url else (existing_row[8] if len(existing_row) > 8 else default_cockpit_light_url)
        final_audit = audit_report_url.strip() if audit_report_url else (existing_row[9] if len(existing_row) > 9 else default_audit_url)
        final_source_url = parsed_url if parsed_url else (existing_row[10] if len(existing_row) > 10 else "")
        final_branch_ctx = parsed_ctx if parsed_ctx else (existing_row[11] if len(existing_row) > 11 else "")
        final_partner = partner_norm if partner_norm else (existing_row[12] if len(existing_row) > 12 else "Jenny Ettle (JE-MI)")
        final_submitted = submitted_at.strip() if submitted_at else (existing_row[13] if len(existing_row) > 13 else datetime.now().strftime("%d.%m.%Y · %H:%M Uhr"))
        final_status = status_text.strip() if status_text else (existing_row[14] if len(existing_row) > 14 else "")

        row_values = [
            row_active,
            final_company,
            final_price,
            final_monthly,
            final_rationale,
            final_v2,
            final_voll,
            final_cockpit,
            final_cockpit_light,
            final_audit,
            final_source_url,
            final_branch_ctx,
            final_partner,
            final_submitted,
            final_status,
        ]
        safe_range = urllib.parse.quote(f"'{tab_title}'!A{target_row_idx}:O{target_row_idx}")
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{safe_range}"
        r_put = _request_with_retry(
            "PUT",
            url,
            params={"valueInputOption": "USER_ENTERED"},
            json={"values": [row_values]},
        )
        r_put.raise_for_status()
        return {
            "ok": True,
            "action": "updated",
            "row": target_row_idx,
            "spreadsheet_url": spreadsheet_url,
            "values": row_values,
        }
    else:
        row_active = True if active is None else bool(active)
        row_values = [
            row_active,
            company_name.strip() or clean_slug,
            pricing_display.strip(),
            monthly_sheet_display.strip(),
            pricing_rationale.strip(),
            v2_url.strip(),
            vollversion_url.strip(),
            cockpit_url.strip(),
            cockpit_light_url.strip(),
            audit_report_url.strip(),
            parsed_url,
            parsed_ctx,
            partner_norm,
            submitted_at.strip() or datetime.now().strftime("%d.%m.%Y · %H:%M Uhr"),
            status_text.strip(),
        ]
        new_row_idx = len(rows) + 1
        safe_range = urllib.parse.quote(f"'{tab_title}'!A{new_row_idx}:O{new_row_idx}")
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{safe_range}"
        r_put = _request_with_retry(
            "PUT",
            url,
            params={"valueInputOption": "USER_ENTERED"},
            json={"values": [row_values]},
        )
        r_put.raise_for_status()
        apply_sheet_formatting(spreadsheet_id, sheet_id, tab_title, total_rows=new_row_idx)
        return {
            "ok": True,
            "action": "inserted",
            "row": new_row_idx,
            "spreadsheet_url": spreadsheet_url,
            "values": row_values,
        }


def upsert_webpilot_sheet_row(
    slug: str,
    company_name: str,
    v2_url: str = "",
    vollversion_url: str = "",
    cockpit_url: str = "",
    cockpit_light_url: str = "",
    source_context: str = "",
    source_url: str = "",
    branch_context: str = "",
    partner: str = "Jenny Ettle (JE-MI)",
    submitted_at: str = "",
    status_text: str = "",
    active: Optional[bool] = None,
    pricing_display: str = "",
    monthly_sheet_display: str = "",
    pricing_rationale: str = "",
    audit_report_url: str = "",
) -> Dict[str, Any]:
    """
    Synchronisiert eine Zeile automatisch:
    1. IMMER in Davids Master-Sheet (alle Partner).
    2. Wenn Partner == Jenny Ettle (JE-MI), zusaetzlich in Jennys Partner-Sheet.
    """
    clean_slug = (slug or "").strip().lower().replace("preview-", "")
    for suffix in ("-vollversion", "-vv", "-v2", "-v1"):
        if clean_slug.endswith(suffix):
            clean_slug = clean_slug[: -len(suffix)]

    if clean_slug in EXCLUDED_INTERNAL_SLUGS:
        return {"ok": False, "skipped_excluded": clean_slug}

    cfg = get_sheet_config()
    parsed_url, parsed_ctx = split_source_and_context(source_url or source_context, branch_context)

    est = estimate_project_pricing(clean_slug, company_name, parsed_ctx or source_context)
    if not pricing_display:
        pricing_display = est["pricing_display"]
    if not monthly_sheet_display:
        monthly_sheet_display = est["monthly_sheet_display"]
    if not pricing_rationale:
        pricing_rationale = est["pricing_rationale"]

    now_full_str = datetime.now().strftime("%d.%m.%Y · %H:%M Uhr")
    submitted_fmt = format_ch_datetime(submitted_at, "")
    if not submitted_fmt:
        idx_path = Path("/home/brainuser/workspaces/mxs-embed/partner-jobs/index.json")
        if idx_path.exists():
            try:
                for j in json.loads(idx_path.read_text(encoding="utf-8")):
                    if str(j.get("slug") or "").strip().lower() == clean_slug:
                        submitted_fmt = format_ch_datetime(j.get("created_at"), "")
                        break
            except Exception:
                pass
    if not status_text:
        status_text = f"🟢 Bereit zum Zeigen (Fertig: {now_full_str})" if v2_url else f"⏳ In Arbeit (Eingereicht: {submitted_fmt or now_full_str})"

    partner_norm = _normalize_partner_label(partner, slug=clean_slug)
    default_audit_url = f"https://vorschau.magnet-xs.ch/reports/{clean_slug}-vorher-nachher-report.pdf" if clean_slug else ""
    if not audit_report_url:
        audit_report_url = default_audit_url
    default_cockpit_light_url = f"https://vorschau.magnet-xs.ch/{clean_slug}-vollversion/cockpit.html?token={clean_slug}2026&mode=light" if clean_slug else ""
    if not cockpit_light_url:
        cockpit_light_url = default_cockpit_light_url

    # 1. Immer in Davids Master-Sheet upserten
    david_res = _upsert_into_single_sheet(
        spreadsheet_id=cfg["david_spreadsheet_id"],
        spreadsheet_url=cfg["david_spreadsheet_url"],
        clean_slug=clean_slug,
        company_name=company_name,
        v2_url=v2_url,
        vollversion_url=vollversion_url,
        cockpit_url=cockpit_url,
        cockpit_light_url=cockpit_light_url,
        audit_report_url=audit_report_url,
        parsed_url=parsed_url,
        parsed_ctx=parsed_ctx,
        partner_norm=partner_norm,
        submitted_at=submitted_fmt,
        status_text=status_text,
        active=active,
        pricing_display=pricing_display,
        monthly_sheet_display=monthly_sheet_display,
        pricing_rationale=pricing_rationale,
        owner_filter=None,
    )

    # 2. Falls Jenny der Partner ist, auch in Jennys Partner-Sheet upserten
    jenny_res = None
    if PARTNER_SHEET_OWNER in partner_norm.lower() and clean_slug not in EXCLUDED_PARTNER_SLUGS:
        jenny_res = _upsert_into_single_sheet(
            spreadsheet_id=cfg["spreadsheet_id"],
            spreadsheet_url=cfg["spreadsheet_url"],
            clean_slug=clean_slug,
            company_name=company_name,
            v2_url=v2_url,
            vollversion_url=vollversion_url,
            cockpit_url=cockpit_url,
            cockpit_light_url=cockpit_light_url,
            audit_report_url=audit_report_url,
            parsed_url=parsed_url,
            parsed_ctx=parsed_ctx,
            partner_norm=partner_norm,
            submitted_at=submitted_fmt,
            status_text=status_text,
            active=active,
            pricing_display=pricing_display,
            monthly_sheet_display=monthly_sheet_display,
            pricing_rationale=pricing_rationale,
            owner_filter="jenny",
        )

    primary_res = jenny_res if jenny_res is not None else david_res
    return {
        "ok": True,
        "action": primary_res["action"],
        "row": primary_res["row"],
        "spreadsheet_url": primary_res["spreadsheet_url"],
        "david_master_spreadsheet_url": cfg["david_spreadsheet_url"],
        "synced_to_jenny_sheet": bool(jenny_res is not None),
        "synced_to_david_master_sheet": True,
        "values": primary_res["values"],
    }


def _verify_single_sheet(spreadsheet_id: str, spreadsheet_url: str) -> Dict[str, Any]:
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}"
    r = _request_with_retry(
        "GET",
        url,
        params={
            "includeGridData": "true",
            "ranges": f"'{DEFAULT_TAB_TITLE}'!A1:O25",
            "fields": "properties.title,sheets(properties(sheetId,title,gridProperties.frozenRowCount),basicFilter,conditionalFormats,data.rowData.values(userEnteredValue,dataValidation,hyperlink,effectiveFormat.textFormat))",
        },
    )
    r.raise_for_status()
    meta = r.json()
    sh = (meta.get("sheets") or [{}])[0]
    row_data = ((sh.get("data") or [{}])[0]).get("rowData") or []
    checkbox_count = 0
    clickable_source_links = 0
    clickable_cockpit_light_links = 0
    rows_summary = []
    for r_idx, r_obj in enumerate(row_data[1:], start=2):
        vals = r_obj.get("values") or []
        if not vals:
            continue
        comp_val = (vals[1].get("userEnteredValue") or {}).get("stringValue", "") if len(vals) > 1 else ""
        if not comp_val:
            continue
        if (vals[0].get("dataValidation") or {}).get("condition", {}).get("type") == "BOOLEAN":
            checkbox_count += 1
        light_cell = vals[8] if len(vals) > 8 else {}
        light_url = (light_cell.get("userEnteredValue") or {}).get("stringValue", "")
        light_hl = light_cell.get("hyperlink") or ((light_cell.get("effectiveFormat") or {}).get("textFormat") or {}).get("link", {}).get("uri", "")
        if light_url.startswith("http") and light_hl:
            clickable_cockpit_light_links += 1
        src_cell = vals[10] if len(vals) > 10 else {}
        src_url = (src_cell.get("userEnteredValue") or {}).get("stringValue", "")
        src_hyperlink = src_cell.get("hyperlink") or ((src_cell.get("effectiveFormat") or {}).get("textFormat") or {}).get("link", {}).get("uri", "")
        if src_url.startswith("http") and src_hyperlink:
            clickable_source_links += 1
        partner_val = (vals[12].get("userEnteredValue") or {}).get("stringValue", "") if len(vals) > 12 else ""
        submitted_val = (vals[13].get("userEnteredValue") or {}).get("stringValue", "") if len(vals) > 13 else ""
        status_val = (vals[14].get("userEnteredValue") or {}).get("stringValue", "") if len(vals) > 14 else ""
        rows_summary.append({
            "row": r_idx,
            "company": comp_val,
            "einmal_price": (vals[2].get("userEnteredValue") or {}).get("stringValue", "").splitlines()[0] if len(vals) > 2 else "",
            "monthly_offer": (vals[3].get("userEnteredValue") or {}).get("stringValue", "").splitlines()[0] if len(vals) > 3 else "",
            "cockpit_light_url": light_url,
            "is_clickable_cockpit_light": bool(light_hl),
            "source_url": src_url,
            "is_clickable_hyperlink": bool(src_hyperlink),
            "partner": partner_val,
            "submitted_at": submitted_val,
            "status": status_val,
        })

    pub_r = requests.get(spreadsheet_url, timeout=15)
    return {
        "ok": True,
        "title": meta.get("properties", {}).get("title"),
        "tab_title": sh.get("properties", {}).get("title"),
        "headers": HEADERS,
        "frozen_rows": sh.get("properties", {}).get("gridProperties", {}).get("frozenRowCount"),
        "has_basic_filter": bool(sh.get("basicFilter")),
        "conditional_format_rules": len(sh.get("conditionalFormats") or []),
        "total_rows": len(rows_summary),
        "verified_boolean_checkboxes": checkbox_count,
        "verified_clickable_cockpit_light_links": clickable_cockpit_light_links,
        "verified_clickable_source_links": clickable_source_links,
        "public_http_status": pub_r.status_code,
        "spreadsheet_url": spreadsheet_url,
        "rows_summary": rows_summary,
    }


def verify_sheet() -> Dict[str, Any]:
    cfg = get_sheet_config()
    return {
        "ok": True,
        "jenny_partner_sheet": _verify_single_sheet(cfg["spreadsheet_id"], cfg["spreadsheet_url"]),
        "david_master_sheet": _verify_single_sheet(cfg["david_spreadsheet_id"], cfg["david_spreadsheet_url"]),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WebPilot Google Sheets Sync")
    parser.add_argument("--init", action="store_true", help="Initialisiert & befuellt beide Google Sheets (Jenny + David Master)")
    parser.add_argument("--verify", action="store_true", help="Prueft Checkboxen, Klick-Links, Filter & Public Access auf beiden Sheets")
    parser.add_argument("--upsert", action="store_true", help="Fuegt eine Zeile ein oder aktualisiert sie")
    parser.add_argument("--slug", type=str, default="", help="Mandanten-Slug")
    parser.add_argument("--company", type=str, default="", help="Firma / Verein")
    parser.add_argument("--v2-url", type=str, default="", help="Zeigeversion (-v2) URL")
    parser.add_argument("--voll-url", type=str, default="", help="Vollversion (-vollversion) URL")
    parser.add_argument("--cockpit-url", type=str, default="", help="Studio Cockpit v4.0 URL")
    parser.add_argument("--source", type=str, default="", help="Ursprungs-Webseite & Kontext")
    parser.add_argument("--partner", type=str, default="Jenny Ettle (JE-MI)", help="Partner")
    parser.add_argument("--status", type=str, default="", help="Status & Datum")
    args = parser.parse_args()

    if args.init:
        print(json.dumps(init_and_seed_sheet(), indent=2, ensure_ascii=False))
    elif args.verify:
        print(json.dumps(verify_sheet(), indent=2, ensure_ascii=False))
    elif args.upsert:
        print(json.dumps(upsert_webpilot_sheet_row(
            slug=args.slug,
            company_name=args.company,
            v2_url=args.v2_url,
            vollversion_url=args.voll_url,
            cockpit_url=args.cockpit_url,
            source_context=args.source,
            partner=args.partner,
            status_text=args.status,
        ), indent=2, ensure_ascii=False))
    else:
        print(json.dumps(verify_sheet(), indent=2, ensure_ascii=False))

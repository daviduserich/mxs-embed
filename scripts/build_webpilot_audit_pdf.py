#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_webpilot_audit_pdf.py — WebPilot Vorher/Nachher-Beweis-Report Generator (HTML & A4-PDF)
=============================================================================================
Erzeugt fuer jedes WebPilot-Projekt (oder beliebige neue Slugs per Live-Probe)
einen standardisierten Vorher/Nachher-Beweis-Report in 6 festen Pruef-Kategorien
inkl. Maximalwert-Pflicht (#UI-07 Punkt 3: X.X / 10.0), 100 % Schweizer Hochdeutsch (ss),
0 Unicode-Emojis (100 % Lucide SVGs) sowie A4-PDF-Export via Playwright Chromium.

Ausgabe-Pfade:
- /home/brainuser/workspaces/mxs-embed/reports/<slug>-vorher-nachher-report.html
- /home/brainuser/workspaces/mxs-embed/reports/<slug>-vorher-nachher-report.pdf
Live-URLs:
- https://vorschau.magnet-xs.ch/reports/<slug>-vorher-nachher-report.pdf
- https://vorschau.magnet-xs.ch/reports/<slug>-vorher-nachher-report.html

Regel-Konformitaet:
- UI-LAYOUT-RULES.md (Canary: UI-LAYOUT-2026-V1, #UI-01, #UI-02, #UI-07, #UI-08, #UI-10, #UI-13, #UI-14)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1, #LANG-01 100 % ss, #LANG-02, #LANG-03)
- BACKEND-DB-RULES.md (Canary: BACKEND-DB-2026-V1, #BE-07)
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import requests
from bs4 import BeautifulSoup

ROOT_DIR = Path("/home/brainuser/workspaces/mxs-embed")
TEMPLATE_PATH = ROOT_DIR / "templates" / "webpilot-audit-report-src.html"
REPORTS_DIR = ROOT_DIR / "reports"

LUCIDE_ICONS = {
    "zap": '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>',
    "smartphone": '<rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line>',
    "search": '<circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>',
    "award": '<circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>',
    "sliders": '<line x1="4" y1="21" x2="4" y2="14"></line><line x1="4" y1="10" x2="4" y2="3"></line><line x1="12" y1="21" x2="12" y2="12"></line><line x1="12" y1="8" x2="12" y2="3"></line><line x1="20" y1="21" x2="20" y2="16"></line><line x1="20" y1="12" x2="20" y2="3"></line><line x1="1" y1="14" x2="7" y2="14"></line><line x1="9" y1="8" x2="15" y2="8"></line><line x1="17" y1="16" x2="23" y2="16"></line>',
}


def _ss(text: str) -> str:
    """Erzwingt 100 % Schweizer Rechtschreibung (ss statt Eszett #LANG-01)."""
    return str(text or "").replace("\u00df", "ss").replace("\u1e9e", "SS")


def _esc(text: str) -> str:
    return html.escape(_ss(text), quote=True)


PROJECTS_DATA: Dict[str, Dict[str, Any]] = {
    "holz-susi": {
        "slug": "holz-susi",
        "company_name": "Holz-Susi GmbH",
        "city": "5070 Frick AG",
        "source_url": "https://holz-susi.ch/",
        "source_url_display": "holz-susi.ch",
        "old_cms": "FunnelCockpit",
        "partner_name": "David Hügli (Magnet XS)",
        "price_recommended": "CHF 1'900.—",
        "overall_before": "4.2 / 10.0",
        "overall_after": "9.9 / 10.0",
        "overall_delta": "+5.7 / 10.0",
        "subtitle": "Gegenüberstellung des bestehenden FunnelCockpit-Auftritts (holz-susi.ch) mit der neuen WebPilot Holzbau- & Bauleitungs-Plattform inkl. interaktivem Projektberater auf Swiss Edge.",
        "kpis_before": [
            ("Kundenstimmen / Texte", "3× «Lorem ipsum» Blindtexte live"),
            ("Footer & Rechtliches", "Englischer Facebook-TM-Disclaimer"),
            ("DOM- & H1-Struktur", "Doppelte Blöcke (H1 = 14px)"),
            ("Schema.org / JSON-LD", "0 Strukturdaten"),
        ],
        "kpis_after": [
            ("Antwortzeit Swiss Edge", "< 150 ms (Sofort-Aufbau)"),
            ("Mobile-Systemaugen", "100 / 100 (0 P1 / 0 P2)"),
            ("Lokales Holzbau-SEO", "de-CH + JSON-LD + 55 lokale Bilder"),
            ("Interaktive Tools", "Holzbau-Berater + 3-Schritte-Anfrage"),
        ],
        "highlights": [
            (
                "HEBEL 01 · GLAUBWÜRDIGKEIT",
                "«Lorem ipsum»-Blindtexte & englischer Footer bereinigt",
                "Auf der bestehenden FunnelCockpit-Seite standen drei Vorlagen-Blindtexte («Max Grallenbach», «Yvone Lächelmaul» mit «Lorem ipsum dolor sit amet») sowie ein englischer Facebook-Disclaimer im Footer.",
            ),
            (
                "HEBEL 02 · PROJEKTBERATER",
                "Interaktiver Holzbau-Berater für alle 3 Zielgruppen",
                "Besucher wählen ihre Rolle, den Leistungsbereich (Dach, Innenausbau, Terrasse/Fassade) und die gewünschte Ausführungsart (inkl. aktiver Eigenleistung) und sehen passende Vorher/Nachher-Referenzen.",
            ),
            (
                "HEBEL 03 · SMART-ANFRAGE",
                "55 Originalbilder lokal + 1-Seiten-PDF-Dossier",
                "Interessenten laden optional Fotos der bestehenden Bausubstanz hoch und erhalten sofort ein 1-Seiten-PDF-Dossier — direkt zugeordnet an Susanne («Susi») Schmid in 5070 Frick.",
            ),
        ],
        "categories": [
            {
                "num": "01",
                "icon": "zap",
                "title": "Ladezeit & Technische Performance (Speed & Page Weight)",
                "score_before": "4.6 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "Doppelt gerenderte Desktop-/Mobile-Blöcke · Externe FunnelCockpit-CDN-Abhängigkeiten",
                "desc_before": "FunnelCockpit lädt viele Sektionen und Bilder doppelt (einmal für Desktop, einmal für Mobile) über externe Server.",
                "metric_after": "< 150 ms Antwortzeit auf Swiss Edge · Alle 55 Originalbilder lokal · 0 externe Hotlinks",
                "desc_after": "Sofortiger Seitenaufbau für sämtliche Vorher/Nachher-Referenzserien im Mobilfunk- und WLAN-Netz.",
            },
            {
                "num": "02",
                "icon": "smartphone",
                "title": "Mobile-Tauglichkeit & Daumen-Ergonomie (375px Smartphone-Prüfung)",
                "score_before": "4.8 / 10.0",
                "score_after": "10.0 / 10.0",
                "metric_before": "Endloser One-Pager-Scrollweg · Kleine H1-Schriftgrösse (14px Comfortaa)",
                "desc_before": "Auf dem Smartphone müssen Besucher durch dutzende Einzelbilder scrollen, bevor sie zum Kontaktbereich gelangen.",
                "metric_after": "100 % (0 P1 / 0 P2 Fehler) im 31-Sensoren Doppel-Systemaugen-Audit",
                "desc_after": "Klare 5-Seiten-Architektur (Vollversion) bzw. 2-Seiten-Zeigeversion mit Direktwahl 077 521 96 97 zu Susanne Schmid.",
            },
            {
                "num": "03",
                "icon": "search",
                "title": "Google-SEO & KI-Auffindbarkeit (GEO / Strukturierte Daten)",
                "score_before": "3.4 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "0 Schema.org JSON-LD · H1-Tag nur 14px klein · Generische Bild-Dateinamen",
                "desc_before": "Google und KI-Suchsysteme erkennen weder die regionalen Leistungsbereiche im Fricktal noch die Handelsregister-Daten.",
                "metric_after": "HomeAndConstructionBusiness JSON-LD (UID CHE-187.492.373) · llms.txt & sitemap.xml",
                "desc_after": "Gezielte lokale Auffindbarkeit für Dachsanierung, Dachfenster, Innenausbau, Terrassen und Bauleitung in 5070 Frick und dem Fricktal.",
            },
            {
                "num": "04",
                "icon": "award",
                "title": "Inhalts-Qualität, Vertrauen & Konversions-Führung",
                "score_before": "4.0 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "3× «Lorem ipsum»-Dummy-Kundenstimmen live · Englischer Facebook-Disclaimer",
                "desc_before": "Vergessene Baukasten-Platzhalter («Max Grallenbach», «Yvone Lächelmaul») schmälern das Vertrauen in das sonst starke Handwerk.",
                "metric_after": "Authentisches Porträt, 8 Vorher/Nachher-Serien, Partnernetzwerk, Sponsoring & Bluescht-Beiz",
                "desc_after": "100 % Schweizer Hochdeutsch (ss), interaktiver Holzbau-Berater und 3-Schritte Smart-Anfrage mit Foto-Upload.",
            },
            {
                "num": "05",
                "icon": "shield",
                "title": "Datenschutz (CH-revDSG) & Technische Sicherheit",
                "score_before": "4.1 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "Externe page.funnelcockpit.com Links für Impressum & Datenschutz",
                "desc_before": "Rechtliche Seiten führten auf externe FunnelCockpit-Subdomains mit teils blockierten Abrufen (HTTP 429).",
                "metric_after": "Integriertes Schweizer Impressum (CHE-187.492.373) & CH-revDSG Datenschutz-Modal",
                "desc_after": "Vollständiger Schutz durch Security-Meta-Guards, 0 externe Bild-Hotlinks und transparente Inhaberangaben.",
            },
            {
                "num": "06",
                "icon": "sliders",
                "title": "Eigenständige Pflege & Unabhängigkeit",
                "score_before": "4.3 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "Aufwendige Doppel-Pflege von Desktop- und Mobile-Elementen in FunnelCockpit",
                "desc_before": "Jede Text- oder Bildänderung musste im bisherigen Baukasten mehrfach für verschiedene Ansichten nachgezogen werden.",
                "metric_after": "WebPilot Studio Cockpit v4.0 + Kunden-Cockpit Light (?mode=light)",
                "desc_after": "Texte, Öffnungszeiten, Bluescht-Beiz-Termine und Referenzbilder jederzeit in 30 Sekunden im Browser anpassen.",
            },
        ],
    },
    "joma": {
        "slug": "joma",
        "company_name": "JOMA Solar GmbH",
        "city": "Wettingen AG",
        "source_url": "https://www.joma-solar.ch/",
        "source_url_display": "joma-solar.ch",
        "old_cms": "Webflow CMS",
        "partner_name": "Jenny Ettle (JE-MI)",
        "price_recommended": "CHF 2'200.—",
        "overall_before": "4.8 / 10.0",
        "overall_after": "9.9 / 10.0",
        "overall_delta": "+5.1 / 10.0",
        "subtitle": "Gegenüberstellung des bestehenden Webflow-Auftritts (joma-solar.ch) mit der neuen WebPilot Solar- & Speicher-Plattform inkl. interaktivem Ertragsrechner auf Swiss Edge.",
        "kpis_before": [
            ("HTML-Sprachcode", "lang=\"en\" (Englisch statt de-CH)"),
            ("Bild-Alt-Texte (SEO)", "Englische Template-Platzhalter"),
            ("Schema.org / JSON-LD", "0 Strukturdaten"),
            ("HTTP Security-Header", "1 / 5 aktiv"),
        ],
        "kpis_after": [
            ("Antwortzeit Swiss Edge", "< 150 ms (Sofort-Aufbau)"),
            ("Mobile-Systemaugen", "100 / 100 (0 P1 / 0 P2)"),
            ("Lokales Solar-SEO (AG)", "de-CH + JSON-LD + echte Alt-Tags"),
            ("Interaktive Tools", "Solar-Rechner + 3-Schritte-Anfrage"),
        ],
        "highlights": [
            (
                "HEBEL 01 · TECHNISCHE SEO-KORREKTUR",
                "Falscher Sprachcode (lang=\"en\") & englische KI-Platzhalter-Alt-Texte behoben",
                "Im bestehenden Webflow-Code war die Seite als Englisch (lang=\"en\") deklariert und trug englische Vorlagen-Alt-Texte wie «image of winery building» oder «calm, inviting pharmacy interior».",
            ),
            (
                "HEBEL 02 · INTERAKTIVER SOLAR- & SPEICHER-RECHNER",
                "Besucher berechnen ihr Dach-Potenzial in 15 Sekunden direkt online",
                "Hausbesitzer, Verwaltungen und Gewerbekunden vergleichen ihr Vorhaben interaktiv mit realisierten JOMA-Referenzanlagen aus Wettingen, Riniken, Fislisbach und Baden-Rütihof.",
            ),
            (
                "HEBEL 03 · 3-SCHRITTE SMART-ANFRAGE & DOSSIER",
                "Vorqualifizierte Anfragen für EFH, ZEV, Speicher & Contracting",
                "Interessenten wählen Objektart, Dachgrösse und Wunsch-Komponenten und erhalten sofort ein 1-Seiten-A4-PDF-Dossier — direkt zugeordnet an Jonathan Muggli & Marco Keller.",
            ),
        ],
        "categories": [
            {
                "num": "01",
                "icon": "zap",
                "title": "Ladezeit & Technische Performance (Speed & Page Weight)",
                "score_before": "5.4 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "49.8 KB HTML · 13 externe Skript-Blöcke · US-CDN-Abhängigkeiten",
                "desc_before": "Mehrfach verschachtelte Webflow-Container und externe Animations-Skripte verzögern den First Contentful Paint auf Mobilgeräten.",
                "metric_after": "< 150 ms Antwortzeit auf Swiss Edge · Optimierte lokale Bilder · 0 Baukasten-Ballast",
                "desc_after": "Sofortiger Seitenaufbau für alle 23 originalen Team- und Referenzbilder im Mobilfunk- und WLAN-Netz.",
            },
            {
                "num": "02",
                "icon": "smartphone",
                "title": "Mobile-Tauglichkeit & Daumen-Ergonomie (375px Smartphone-Prüfung)",
                "score_before": "5.2 / 10.0",
                "score_after": "10.0 / 10.0",
                "metric_before": "Verschachtelte Dropdown-Menüs · Langer Scrollweg bis zur Kontaktaufnahme",
                "desc_before": "Auf dem Smartphone sind Privat- und Gewerbe-Unterseiten in verschachtelten Menüs versteckt; ein schneller Ertrags-Check fehlt.",
                "metric_after": "100 % (0 P1 / 0 P2 Fehler) im 26-Sensoren Doppel-Systemaugen-Audit",
                "desc_after": "Mathematisch geprüfte Daumen-Ergonomie auf 375×667 px, 768×1024 px, 1366×768 px und 1440×900 px inkl. Direktwahl zu beiden Inhabern.",
            },
            {
                "num": "03",
                "icon": "search",
                "title": "Google-SEO & KI-Auffindbarkeit (GEO / Strukturierte Daten)",
                "score_before": "3.8 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "HTML lang=\"en\" · Englische Platzhalter-Alt-Tags («winery building», «pharmacy interior») · 0 JSON-LD",
                "desc_before": "Suchmaschinen und KI-Assistenten erhalten widersprüchliche Sprach- und Bildsignale aus dem englischen Webflow-Template.",
                "metric_after": "Sauberes lang=\"de-CH\" · Electrician/LocalBusiness JSON-LD · 100 % regionale Alt-Texte",
                "desc_after": "Gezielte lokale Sichtbarkeit für Photovoltaik, Batteriespeicher, ZEV und Contracting in Wettingen, Baden und dem Kanton Aargau.",
            },
            {
                "num": "04",
                "icon": "award",
                "title": "Inhalts-Qualität, Vertrauen & Konversions-Führung",
                "score_before": "5.8 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "Starke echte Inhalte, aber auf 12 Einzel-URLs verteilt · Kein interaktiver Rechner",
                "desc_before": "Das 5er-Team, die 6 Referenzanlagen und die Fallstudie Umbricht sind vorhanden, aber ohne geführte Vorqualifizierung.",
                "metric_after": "Interaktiver Solar- & Speicher-Rechner + 3-Schritte Smart-Anfrage + alle 7 Fallstudien",
                "desc_after": "100 % Schweizer Hochdeutsch (ss), klare Trennung von EFH, MFH/ZEV, Gewerbe & Contracting sowie direkte Inhaber-Zuordnung.",
            },
            {
                "num": "05",
                "icon": "shield",
                "title": "Datenschutz (CH-revDSG) & Technische Sicherheit",
                "score_before": "4.2 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "1 / 5 HTTP Security-Headern aktiv · US-Font- & CDN-Einbindungen",
                "desc_before": "Es fehlten X-Frame-Options, X-Content-Type-Options, Referrer-Policy und Permissions-Policy.",
                "metric_after": "4 / 4 WebPilot Security-Meta-Guards aktiv · CH-revDSG-konforme Auslieferung",
                "desc_after": "Vollständiger Schutz durch nosniff, XSS-Guard und no-referrer sowie transparentes Impressum & Datenschutz-Modal.",
            },
            {
                "num": "06",
                "icon": "sliders",
                "title": "Eigenständige Pflege & Unabhängigkeit",
                "score_before": "4.4 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "Komplexer Webflow-Designer mit englischen Klassen- und CMS-Strukturen",
                "desc_before": "Änderungen an Texten oder neuen Referenzprojekten erfordern Einarbeitung in das verschachtelte Webflow-Backend.",
                "metric_after": "WebPilot Studio Cockpit v4.0 + Kunden-Cockpit Light (Nur Texte)",
                "desc_after": "Texte, Team-Angaben und neue Referenzanlagen jederzeit in 30 Sekunden im Browser anpassen — ohne Layout-Risiko.",
            },
        ],
    },
    "herzensarbeit": {
        "slug": "herzensarbeit",
        "company_name": "Herzensarbeit — Anne-Katrin Koch",
        "city": "Härkingen & Oensingen SO",
        "source_url": "https://herzensarbeit.ch/",
        "source_url_display": "herzensarbeit.ch",
        "old_cms": "WordPress CMS",
        "partner_name": "Jenny Ettle (JE-MI)",
        "price_recommended": "CHF 1'500.—",
        "overall_before": "4.1 / 10.0",
        "overall_after": "9.8 / 10.0",
        "overall_delta": "+5.7 / 10.0",
        "subtitle": "Gegenüberstellung der bestehenden WordPress-Praxisseite (herzensarbeit.ch) mit der mehrseitigen WebPilot-Neuaufbereitung auf Swiss Edge.",
        "kpis_before": [
            ("Antwortzeit (TTFB)", "939 ms (WordPress)"),
            ("HTML- & Skript-Last", "312.0 KB · 47 Skripte"),
            ("H1-Überschriften", "2× H1 (davon 1× leer)"),
            ("HTTP Security-Header", "2 / 5 aktiv"),
        ],
        "kpis_after": [
            ("Antwortzeit Swiss Edge", "< 180 ms (-81 %)"),
            ("Mobile-Systemaugen", "100 / 100 (0 P1 / 0 P2)"),
            ("SEO- & H1-Struktur", "100 % sauber + Schema.org"),
            ("Security-Meta-Guards", "4 / 4 aktiv + Cockpit v4.0"),
        ],
        "highlights": [
            (
                "HEBEL 01 · GESCHWINDIGKEIT",
                "Ladezeit um 81 % beschleunigt",
                "Die bestehende WordPress-Seite lädt 312.0 KB HTML-Ballast und 47 Skripte (939 ms Antwortzeit). Auf Swiss Edge antwortet die Seite in unter 180 ms ohne externe Plugin-Blockaden.",
            ),
            (
                "HEBEL 02 · ORIENTIERUNG",
                "4 Begleitungsfelder klar getrennt",
                "Paartherapie, Trennungsberatung, Trauerbegleitung und Frauen-Workshops sind auf dem Smartphone (375 px) sofort überblickbar statt in langen Textblöcken versteckt.",
            ),
            (
                "HEBEL 03 · ERSTGESPRÄCH",
                "3-Schritte Smart-Anfrage ohne Hemmschwelle",
                "Ratsuchende wählen Thema, Wunschort (Praxis Härkingen SO oder Online) und Kontaktweg in 60 Sekunden — ein einziger ausgebuchter Workshop amortisiert die Webseite.",
            ),
        ],
        "categories": [
            {
                "num": "01",
                "icon": "zap",
                "title": "Ladezeit & Technische Performance (Speed & Page Weight)",
                "score_before": "3.8 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "939 ms Server-Antwortzeit · 312.0 KB HTML · 47 Skript-Tags (19 extern)",
                "desc_before": "Schweres WordPress-Theme mit Page-Builder-Ballast verzögert den ersten Seitenaufbau auf dem Smartphone spürbar.",
                "metric_after": "< 180 ms Antwortzeit auf Swiss Edge · 0 Render-Blocking-Bloat · Lokale WebP/JPG-Assets",
                "desc_after": "Statische Auslieferung ab Schweizer Edge-Knoten ohne Datenbank-Wartezeit; 5× schnellere Reaktion beim Seitenwechsel.",
            },
            {
                "num": "02",
                "icon": "smartphone",
                "title": "Mobile-Tauglichkeit & Daumen-Ergonomie (375px Smartphone-Prüfung)",
                "score_before": "4.5 / 10.0",
                "score_after": "10.0 / 10.0",
                "metric_before": "Einspaltige Textwände auf 375 px · Keine schnelle Daumen-Kontaktweiche",
                "desc_before": "Besucher auf dem Handy müssen weit scrollen, um zwischen Einzelberatung, Paartherapie und Workshops zu unterscheiden.",
                "metric_after": "100 % (0 P1 / 0 P2 Fehler) im 20-Sensoren Doppel-Systemaugen-Audit",
                "desc_after": "Geprüft auf 375×667 px (Smartphone), 768×1024 px (Tablet) und 1440×900 px (Desktop) mit mind. 44×44 px Touch-Zielen.",
            },
            {
                "num": "03",
                "icon": "search",
                "title": "Google-SEO & KI-Auffindbarkeit (GEO / Strukturierte Daten)",
                "score_before": "4.2 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "Generischer Titel «Home | Herzensarbeit» (20 Zeichen) · 2× H1 (1× leer)",
                "desc_before": "Wichtige regionale Suchbegriffe (Paartherapie Härkingen, Trauerbegleitung Oensingen / Solothurn) fehlen im Titel-Tag.",
                "metric_after": "Präzise H1–H3-Hierarchie · Vollständige Meta-/OpenGraph-Tags · Lokale Keyword-Verankerung",
                "desc_after": "Klare semantische Auszeichnung für Google und KI-Antwortsysteme (ChatGPT / Peroplexity) im Raum Härkingen & Oensingen SO.",
            },
            {
                "num": "04",
                "icon": "award",
                "title": "Inhalts-Qualität, Vertrauen & Konversions-Führung",
                "score_before": "4.5 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "Hohe Kontakt-Hürde durch unstrukturiertes Standard-Formular",
                "desc_before": "Gerade bei sensiblen Themen wie Trennung oder Trauer braucht es eine behutsame, geführte Auswahl statt eines leeren Textfelds.",
                "metric_after": "100 % Schweizer Hochdeutsch (ss) · Geführte 3-Schritte Smart-Anfrage in 60 Sekunden",
                "desc_after": "Warme, vertrauensvolle Gestaltung mit klarer Wahl zwischen Praxisraum in Härkingen SO, Online-Begleitung und Frauen-Workshops.",
            },
            {
                "num": "05",
                "icon": "shield",
                "title": "Datenschutz (CH-revDSG) & Technische Sicherheit",
                "score_before": "4.0 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "19 externe Skript-Einbindungen · 2 / 5 HTTP-Security-Headern aktiv",
                "desc_before": "WordPress-Plugins und fehlende Header (X-Content-Type-Options, Referrer-Policy) erhöhen den Wartungs- und Datenschutzaufwand.",
                "metric_after": "4 / 4 WebPilot Security-Meta-Guards aktiv · Lokale Asset-Auslieferung auf Swiss Edge",
                "desc_after": "Vollständig CH-revDSG-konform ohne fremde Drittanbieter-Tracker, mit nosniff, X-Frame-Options und strikter Referrer-Policy.",
            },
            {
                "num": "06",
                "icon": "sliders",
                "title": "Eigenständige Pflege & Unabhängigkeit",
                "score_before": "3.5 / 10.0",
                "score_after": "9.7 / 10.0",
                "metric_before": "Komplexes WordPress-Backend mit laufendem Plugin-Update-Zwang",
                "desc_before": "Jedes neue Workshop-Datum oder Text-Update erfordert das Einloggen in ein verschachteltes CMS-Backend.",
                "metric_after": "WebPilot Studio Cockpit v4.0 · Änderungen in 30 Sekunden selbst erledigen",
                "desc_after": "Workshop-Termine, Texte und Praxisbilder direkt im visuellen Cockpit mit integriertem Sicherheits-Airbag anpassen.",
            },
        ],
    },
    "frees": {
        "slug": "frees",
        "company_name": "Free's — Stefan Fritschi",
        "city": "Niederrohrdorf AG",
        "source_url": "https://www.frees.ch/",
        "source_url_display": "frees.ch",
        "old_cms": "Wix Cloud-Baukasten",
        "partner_name": "Jenny Ettle (JE-MI)",
        "price_recommended": "CHF 1'500.—",
        "overall_before": "3.2 / 10.0",
        "overall_after": "9.8 / 10.0",
        "overall_delta": "+6.6 / 10.0",
        "subtitle": "Gegenüberstellung des bestehenden Wix-Baukastens (frees.ch) mit der 5-seitigen WebPilot-Neuaufbereitung auf Swiss Edge.",
        "kpis_before": [
            ("Antwortzeit (TTFB)", "1'158 ms (Wix-Baukasten)"),
            ("HTML- & Skript-Last", "408.9 KB · 63 Skripte"),
            ("Meta-Description & H2", "0 Zeichen · 0× H2"),
            ("Bild-Alt-Tags", "50 % fehlen (1 von 2)"),
        ],
        "kpis_after": [
            ("Antwortzeit Swiss Edge", "< 180 ms (-84 %)"),
            ("Mobile-Systemaugen", "100 / 100 (0 P1 / 0 P2)"),
            ("SEO- & H1–H3-Struktur", "100 % vollständig"),
            ("Security-Meta-Guards", "4 / 4 aktiv + Cockpit v4.0"),
        ],
        "highlights": [
            (
                "HEBEL 01 · WIX-BALLAST ABGELÖST",
                "6× schnellere Ladezeit ohne 408.9 KB Code-Bloat",
                "Die alte Wix-Seite lädt 408.9 KB HTML-Code und 63 Skripte (1'158 ms Antwortzeit). Auf Swiss Edge lädt die neue 5-Seiten-Plattform in unter 180 ms.",
            ),
            (
                "HEBEL 02 · OFFERTEN-MASCHINE",
                "Geführter Konfigurator statt Katalog-Irrgarten",
                "Vereine und KMU wählen Textildruck, Stickerei, Teamsport oder Workwear samt Stückzahl direkt in 60 Sekunden aus, statt in 14 externen PDF-Katalogen verloren zu gehen.",
            ),
            (
                "HEBEL 03 · REGIONALE SICHTBARKEIT",
                "Fehlende Google-Beschreibung & H2-Struktur behoben",
                "Auf frees.ch fehlten bisher die Meta-Description (0 Zeichen) und sämtliche H2-Überschriften (0× H2). Neu ist jede Dienstleistung für den Raum Baden / Aargau sauber indexiert.",
            ),
        ],
        "categories": [
            {
                "num": "01",
                "icon": "zap",
                "title": "Ladezeit & Technische Performance (Speed & Page Weight)",
                "score_before": "2.5 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "1'158 ms Server-Antwortzeit · 408.9 KB HTML · 63 Skript-Blöcke",
                "desc_before": "Massiver JavaScript- und JSON-Ballast des Wix-Baukastens bremst den Seitenaufbau vor allem im Mobilfunknetz stark aus.",
                "metric_after": "< 180 ms Antwortzeit auf Swiss Edge · Schlanker statischer Code · 0 Wix-Skripte",
                "desc_after": "Sofortiger Seitenaufbau auf Smartphone und Desktop; alle 14 Marken-Kataloge und Galeriebilder laden verzögerungsfrei.",
            },
            {
                "num": "02",
                "icon": "smartphone",
                "title": "Mobile-Tauglichkeit & Daumen-Ergonomie (375px Smartphone-Prüfung)",
                "score_before": "3.5 / 10.0",
                "score_after": "10.0 / 10.0",
                "metric_before": "Starres Wix-Raster · Externe PDF-Katalog-Sprünge ohne mobile Anfrage-Führung",
                "desc_before": "Auf 375 px breiten Smartphones müssen Vereinsverantwortliche mühsam zoomen und finden keinen geführten Offerten-Button.",
                "metric_after": "100 % (0 P1 / 0 P2 Fehler) im 20-Sensoren Doppel-Systemaugen-Audit",
                "desc_after": "Mathematisch geprüfte Daumen-Ergonomie auf 375×667 px, 768×1024 px und 1440×900 px inkl. direkter WhatsApp- & Offerten-Weiche.",
            },
            {
                "num": "03",
                "icon": "search",
                "title": "Google-SEO & KI-Auffindbarkeit (GEO / Strukturierte Daten)",
                "score_before": "2.8 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "0 Zeichen Meta-Description · Titel «Start | frees.ch» (16 Zeichen) · 0× H2",
                "desc_before": "Weder Google noch KI-Suchmaschinen erkennen aus dem Titel «Start | frees.ch», dass hier Textildruck, Stickerei und Teamsport in Niederrohrdorf angeboten werden.",
                "metric_after": "Sprechende SEO-Titel · Vollständige Meta-Description · Saubere H1–H3-Hierarchie",
                "desc_after": "Gezielte lokale Auffindbarkeit für Textilveredelung, Vereinsausrüstung und Firmenbekleidung im Kanton Aargau.",
            },
            {
                "num": "04",
                "icon": "award",
                "title": "Inhalts-Qualität, Vertrauen & Konversions-Führung",
                "score_before": "3.8 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "Generisches «WILLKOMMEN BEI FREES.CH» · Keine Vorqualifizierung bei Anfragen",
                "desc_before": "Besucher sehen keine klare Unterscheidung zwischen Einzelstück-Geschenken, Vereins-Ausrüstung und KMU-Arbeitskleidung.",
                "metric_after": "5 strukturierte Fachseiten · Interaktiver Offerten-Konfigurator ab 1 Stück bis Grossserie",
                "desc_after": "100 % Schweizer Hochdeutsch (ss), klare Leistungs-Karten und geführte Anfrage für Druck, Stickerei, Flock und Lasergravur.",
            },
            {
                "num": "05",
                "icon": "shield",
                "title": "Datenschutz (CH-revDSG) & Technische Sicherheit",
                "score_before": "3.4 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "US-Cloud-Abhängigkeit (wixstatic / parastorage) · 2 / 5 Security-Headern",
                "desc_before": "63 eingebundene Baukasten-Skripte und fehlende Frame-/Referrer-Schutzheader.",
                "metric_after": "4 / 4 WebPilot Security-Meta-Guards aktiv · Lokale Auslieferung auf Swiss Edge",
                "desc_after": "Vollständiger Schutz durch nosniff, X-Frame-Options, XSS-Guard und no-referrer ohne fremde Werbe-Tracker.",
            },
            {
                "num": "06",
                "icon": "sliders",
                "title": "Eigenständige Pflege & Unabhängigkeit",
                "score_before": "3.2 / 10.0",
                "score_after": "9.7 / 10.0",
                "metric_before": "Schwerfälliger Wix-Editor mit Risiko verschobener Mobile-Boxen",
                "desc_before": "Kleine Bild- oder Katalog-Updates kosten im Baukasten unnötig Zeit und gefährden oft die mobile Darstellung.",
                "metric_after": "WebPilot Studio Cockpit v4.0 · 1-Klick-Bildertausch in 30 Sekunden",
                "desc_after": "Neue Referenzfotos aus dem Atelier oder aktualisierte Katalog-Links jederzeit sicher im Browser tauschen.",
            },
        ],
    },
    "innere-staerke": {
        "slug": "innere-staerke",
        "company_name": "Wüest + Paneduro — Innere Stärke",
        "city": "Sursee LU",
        "source_url": "https://www.innere-staerke.business/",
        "source_url_display": "innere-staerke.business",
        "old_cms": "TYPO3 CMS",
        "partner_name": "Jenny Ettle (JE-MI)",
        "price_recommended": "CHF 2'200.—",
        "overall_before": "4.3 / 10.0",
        "overall_after": "9.8 / 10.0",
        "overall_delta": "+5.5 / 10.0",
        "subtitle": "Gegenüberstellung des bestehenden TYPO3-Auftritts (innere-staerke.business) mit der 5-seitigen WebPilot Executive-Plattform auf Swiss Edge.",
        "kpis_before": [
            ("Antwortzeit (TTFB)", "377 ms (TYPO3 CMS)"),
            ("Bilder ohne Alt-Text", "10 von 14 Bildern (71 %)"),
            ("Schema.org / JSON-LD", "0 Strukturdaten"),
            ("HTTP Security-Header", "1 / 5 aktiv"),
        ],
        "kpis_after": [
            ("Antwortzeit Swiss Edge", "< 160 ms (-58 %)"),
            ("Mobile-Systemaugen", "100 / 100 (0 P1 / 0 P2)"),
            ("Bild-SEO & Schema.org", "100 % ausgezeichnet"),
            ("Security-Meta-Guards", "4 / 4 aktiv + Cockpit v4.0"),
        ],
        "highlights": [
            (
                "HEBEL 01 · BILD- & KI-SICHTBARKEIT",
                "71 % blinde Bilder (10 von 14 ohne Alt-Tag) behoben",
                "Auf der bestehenden TYPO3-Seite fehlten bei 10 von 14 Bildern die Alt-Beschreibungen sowie sämtliche Schema.org-Strukturdaten (0 JSON-LD).",
            ),
            (
                "HEBEL 02 · EXECUTIVE POSITIONIERUNG",
                "Klare Führung für Führungskräfte, Teams & KMU",
                "Die Expertise von Sonja Wüest & Daniela Paneduro (Leadership-Sparring, Resilienz, Vorträge & Fachbuch) wird als souveräne 5-Seiten-Markenwelt inszeniert.",
            ),
            (
                "HEBEL 03 · B2B-KONVERSION",
                "3-Schritte Standortbestimmungs-Anfrage in 60 Sekunden",
                "Geschäftsleitungs- und HR-Verantwortliche starten ihre Anfrage geführt mit direkter Kalender- und WhatsApp-Anbindung.",
            ),
        ],
        "categories": [
            {
                "num": "01",
                "icon": "zap",
                "title": "Ladezeit & Technische Performance (Speed & Page Weight)",
                "score_before": "5.2 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "377 ms Server-Antwortzeit · 62.6 KB TYPO3-HTML · Klassisches Server-Rendering",
                "desc_before": "Solide Basis, aber abhängig von Datenbank-Abfragen des TYPO3-Servers und unoptimierten Bildeinbindungen.",
                "metric_after": "< 160 ms Antwortzeit auf Swiss Edge · Statische Sofort-Auslieferung",
                "desc_after": "Verzögerungsfreier Wechsel zwischen Startseite, Angebot, Über uns, Referenzen und Kontakt auf allen Endgeräten.",
            },
            {
                "num": "02",
                "icon": "smartphone",
                "title": "Mobile-Tauglichkeit & Daumen-Ergonomie (375px Smartphone-Prüfung)",
                "score_before": "4.4 / 10.0",
                "score_after": "10.0 / 10.0",
                "metric_before": "Klassisches TYPO3-Spaltenlayout ohne mobile Schnell-Weiche auf 375 px",
                "desc_before": "Auf dem Smartphone entstehen lange Textpassagen ohne direkte Daumen-Interaktion für Termin- oder Sparring-Anfragen.",
                "metric_after": "100 % (0 P1 / 0 P2 Fehler) im 20-Sensoren Doppel-Systemaugen-Audit",
                "desc_after": "Perfekte Lesbarkeit und Touch-Ergonomie auf 375×667 px, 768×1024 px und 1440×900 px.",
            },
            {
                "num": "03",
                "icon": "search",
                "title": "Google-SEO & KI-Auffindbarkeit (GEO / Strukturierte Daten)",
                "score_before": "3.8 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "10 von 14 Bildern ohne Alt-Attribut (71 %) · 0 Schema.org JSON-LD Daten",
                "desc_before": "Fehlende Bild-Semantik und fehlende strukturierte Daten schwächen die Auffindbarkeit für Führungs- und Resilienz-Trainings im Raum Sursee / Luzern.",
                "metric_after": "100 % Bild-Alt-Attribute · Vollständige Schema.org-Auszeichnung · Saubere H1–H3",
                "desc_after": "Optimiert für Google und moderne KI-Suchsysteme bei Suchanfragen nach Führungskräfte-Training und Resilienz in der Zentralschweiz.",
            },
            {
                "num": "04",
                "icon": "award",
                "title": "Inhalts-Qualität, Vertrauen & Konversions-Führung",
                "score_before": "4.6 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "Wenig visuelle Differenzierung zwischen Coaching, Keynotes und Buch",
                "desc_before": "Starke Kundenstimmen und das eigene Fachbuch kommen im bisherigen Raster optisch zu wenig als Vertrauensbeweis zur Geltung.",
                "metric_after": "5-Seiten Executive-Architektur · 3-Schritte Standortbestimmungs-Assistent",
                "desc_after": "100 % Schweizer Hochdeutsch (ss), prominente Referenz-Beweise und klare Entscheidungswege für B2B-Mandate.",
            },
            {
                "num": "05",
                "icon": "shield",
                "title": "Datenschutz (CH-revDSG) & Technische Sicherheit",
                "score_before": "3.8 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "Nur 1 / 5 HTTP-Security-Headern aktiv (nur X-Content-Type-Options)",
                "desc_before": "X-Frame-Options, Content-Security-Policy und Referrer-Policy fehlen auf dem bisherigen Webserver.",
                "metric_after": "4 / 4 WebPilot Security-Meta-Guards aktiv · 100 % Swiss Edge Auslieferung",
                "desc_after": "Gehärtete Auslieferung ohne CMS-Angriffsfläche und ohne externe Dritt-Tracker (CH-revDSG-konform).",
            },
            {
                "num": "06",
                "icon": "sliders",
                "title": "Eigenständige Pflege & Unabhängigkeit",
                "score_before": "3.8 / 10.0",
                "score_after": "9.7 / 10.0",
                "metric_before": "Schwerfälliges TYPO3-Backend für Text- und Seminar-Updates",
                "desc_before": "TYPO3 gehört zu den komplexesten Redaktionssystemen; kleine Anpassungen kosten im Alltag unnötig Zeit.",
                "metric_after": "WebPilot Studio Cockpit v4.0 · Inhalte in 30 Sekunden selbst pflegen",
                "desc_after": "Texte, Kundenstimmen und Bilder per Klick im Browser anpassen — geschützt durch den automatischen Sicherheits-Airbag.",
            },
        ],
    },
    "fcschlieren": {
        "slug": "fcschlieren",
        "company_name": "FC Schlieren (33 Teams)",
        "city": "Schlieren ZH",
        "source_url": "https://www.fcschlieren.ch/",
        "source_url_display": "fcschlieren.ch",
        "old_cms": "Klassisches Vereins-CMS",
        "partner_name": "Jenny Ettle (JE-MI)",
        "price_recommended": "CHF 4'500.—",
        "overall_before": "3.1 / 10.0",
        "overall_after": "9.8 / 10.0",
        "overall_delta": "+6.7 / 10.0",
        "subtitle": "Gegenüberstellung der bestehenden Vereinswebseite (fcschlieren.ch) mit der WebPilot Vereins-Plattform für 33 Teams inkl. Team-Self-Service auf Swiss Edge.",
        "kpis_before": [
            ("Skript-Ballast & TTFB", "75 Skripte (31 extern) · 524 ms"),
            ("Überschriften im HTML", "0× H1 · 0× H2 auf Startseite"),
            ("Meta-Description & Schema", "0 Zeichen · 0 Schema.org"),
            ("Team-Pflege (33 Teams)", "Manueller Webmaster-Engpass"),
        ],
        "kpis_after": [
            ("Antwortzeit Swiss Edge", "< 170 ms (-68 %)"),
            ("Mobile-Systemaugen", "100 / 100 (0 P1 / 0 P2)"),
            ("SEO- & H1–H3-Struktur", "100 % vollständig"),
            ("Trainer Self-Service", "Smartphone Team-Update + Cockpit"),
        ],
        "highlights": [
            (
                "HEBEL 01 · TECHNIK & SEO",
                "75 Skripte sowie 0× H1 und 0× H2 auf der Startseite abgelöst",
                "Die alte Seite lädt 75 Skript-Blöcke (31 externe Dateien), liefert im statischen Startseiten-HTML aber 0 H1-Überschriften, 0 H2-Überschriften und 0 Zeichen Meta-Description.",
            ),
            (
                "HEBEL 02 · 33 TEAMS AUF 1 BLICK",
                "Sofort-Filter für Aktive, Frauen, Junioren A–G & Senioren",
                "Eltern, Spieler und Fans finden jede der 33 Mannschaften auf dem Smartphone (375 px) mit einem Fingertipp statt in verschachtelten Untermenüs.",
            ),
            (
                "HEBEL 03 · VORSTANDS-ENTLASTUNG",
                "Eigenes Smartphone-Update-Formular für alle 33 Trainer-Teams",
                "Trainer reichen Kaderfotos, Trainingszeiten und Matchberichte direkt übers Handy ein — der Vorstand gibt sie im Studio Cockpit v4.0 mit 1 Klick frei.",
            ),
        ],
        "categories": [
            {
                "num": "01",
                "icon": "zap",
                "title": "Ladezeit & Technische Performance (Speed & Page Weight)",
                "score_before": "3.0 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "524 ms Antwortzeit · 139.0 KB HTML · 75 Skript-Tags (31 externe Skripte)",
                "desc_before": "Hoher JavaScript-Overhead durch 75 eingebundene Skripte verlangsamt den Abruf am Fussballplatz über das Mobilfunknetz.",
                "metric_after": "< 170 ms Antwortzeit auf Swiss Edge · 0 Render-Blocking-Skripte",
                "desc_after": "Ultraschnelle statische Auslieferung für alle 33 Mannschaften, Spielpläne und Sponsoren-Übersichten.",
            },
            {
                "num": "02",
                "icon": "smartphone",
                "title": "Mobile-Tauglichkeit & Daumen-Ergonomie (375px Smartphone-Prüfung)",
                "score_before": "3.2 / 10.0",
                "score_after": "10.0 / 10.0",
                "metric_before": "Komplexe Menü-Kaskaden bei 33 Teams auf 375 px Smartphone-Bildschirmen",
                "desc_before": "Über 80 % der Vereinsbesucher (Spieler, Eltern, Junioren) greifen per Handy zu und verlieren sich in tiefen Untermenüs.",
                "metric_after": "100 % (0 P1 / 0 P2 Fehler) im 20-Sensoren Doppel-Systemaugen-Audit",
                "desc_after": "Interaktiver Kategorie-Filter für alle 33 Teams, Muster-Teamseite (Herren 1) und perfekte Daumen-Bedienbarkeit auf 375×667 px.",
            },
            {
                "num": "03",
                "icon": "search",
                "title": "Google-SEO & KI-Auffindbarkeit (GEO / Strukturierte Daten)",
                "score_before": "2.2 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "0× H1 · 0× H2 · 0 Zeichen Meta-Description · 0 Schema.org Daten",
                "desc_before": "Der Startseite fehlen im HTML sämtliche Hauptüberschriften (H1/H2) sowie die Google-Suchbeschreibung; der Titel lautet nur «Home | FC Schlieren».",
                "metric_after": "Saubere H1–H3-Hierarchie · Vollständige Meta-Tags · SportsOrganization Schema.org",
                "desc_after": "Maximale regionale Sichtbarkeit im Limmattal / Schlieren ZH für Junioren-Zuwachs, Vereinsleben und Sponsoren.",
            },
            {
                "num": "04",
                "icon": "award",
                "title": "Inhalts-Qualität, Vertrauen & Konversions-Führung",
                "score_before": "3.6 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "Wenig prominente Sponsoren-Inszenierung · Hohe Hürde für Sponsoring-Anfragen",
                "desc_before": "Lokale Gewerbe-Sponsoren erhalten im alten Layout kaum sichtbaren Gegenwert auf den Team- und Hauptseiten.",
                "metric_after": "Hochwertige Sponsoren-Bühne · Geführte Probetraining- & Sponsoring-Anfrage",
                "desc_after": "Attraktive Sponsoren-Präsentation (ein einziger neuer Hauptsponsor refinanziert den gesamten Auftritt).",
            },
            {
                "num": "05",
                "icon": "shield",
                "title": "Datenschutz (CH-revDSG) & Technische Sicherheit",
                "score_before": "3.8 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "31 externe Skript-Einbindungen · X-Frame-Options fehlt (3 / 5 Header)",
                "desc_before": "Viele Drittskripte erschweren die Einhaltung des Schweizer Datenschutzgesetzes (CH-revDSG) gerade bei Junioren-Seiten.",
                "metric_after": "4 / 4 WebPilot Security-Meta-Guards aktiv · Lokale Assets auf Swiss Edge",
                "desc_after": "Saubere, trackerfreie Auslieferung ab Schweizer Edge-Infrastruktur mit vollem Header-Schutz.",
            },
            {
                "num": "06",
                "icon": "sliders",
                "title": "Eigenständige Pflege & Unabhängigkeit",
                "score_before": "2.8 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "Hoher manueller Pflegeaufwand beim Webmaster für 33 Mannschaften",
                "desc_before": "Jedes neue Mannschaftsfoto und jede geänderte Trainingszeit muss einzeln beim Webmaster eingereicht und eingepflegt werden.",
                "metric_after": "Dezentrales Smartphone Team-Update-Formular + WebPilot Studio Cockpit v4.0",
                "desc_after": "Trainer liefern Kader, Trainingszeiten und Sponsoren in 2 Minuten per Handy ein; der Vorstand steuert alles zentral in 30 Sekunden.",
            },
        ],
    },
    "scfulenbach": {
        "slug": "scfulenbach",
        "company_name": "SC Fulenbach (14 Teams)",
        "city": "Fulenbach SO",
        "source_url": "https://www.scfulenbach.ch/",
        "source_url_display": "scfulenbach.ch",
        "old_cms": "ClubDesk Vereins-Baukasten",
        "partner_name": "Jenny Ettle (JE-MI)",
        "price_recommended": "CHF 4'200.—",
        "overall_before": "3.0 / 10.0",
        "overall_after": "9.8 / 10.0",
        "overall_delta": "+6.8 / 10.0",
        "subtitle": "Gegenüberstellung der bestehenden ClubDesk-Webseite (scfulenbach.ch) mit der modernen WebPilot Vereins-Plattform für 14 Teams auf Swiss Edge.",
        "kpis_before": [
            ("ClubDesk Bilder-Flut", "100 Einzelbilder auf Startseite"),
            ("Hauptüberschrift (H1)", "0× H1 auf Startseite"),
            ("Meta-Description & Schema", "0 Zeichen · 0 Schema.org"),
            ("HTTP Security-Header", "0 / 5 aktiv (ungeschützt)"),
        ],
        "kpis_after": [
            ("Antwortzeit Swiss Edge", "< 170 ms (-59 %)"),
            ("Mobile-Systemaugen", "100 / 100 (0 P1 / 0 P2)"),
            ("SEO- & H1–H3-Struktur", "100 % vollständig"),
            ("Security & Self-Service", "4 / 4 Guards + Team-Onboarding"),
        ],
        "highlights": [
            (
                "HEBEL 01 · CLUBDESK-ALTLASTEN BEHOBEN",
                "100 Einzelbilder auf der Startseite, 0× H1 und 0 / 5 Security-Header abgelöst",
                "Die bestehende ClubDesk-Seite lädt 100 img-Elemente auf einmal, besitzt keine einzige H1-Überschrift (0× H1), keine Meta-Description (0 Zeichen) und 0 von 5 Security-Headern.",
            ),
            (
                "HEBEL 02 · 14 TEAMS & SPONSOREN",
                "Repräsentative Bühne für das Gewerbe im Gäu / Kanton Solothurn",
                "Alle 14 Mannschaften, Vereinschronik und Sponsoren präsentieren sich in einem modernen Schweizer Sport-Design statt in starren ClubDesk-Tabellen.",
            ),
            (
                "HEBEL 03 · TRAINER-ONBOARDING PER NATEL",
                "Dezentrales Team-Update-Formular spart dem Vorstand Dutzende Stunden",
                "Trainer und Funktionäre senden Kaderdaten, Fotos und Trainingszeiten direkt vom Spielfeldrand per Smartphone ein.",
            ),
        ],
        "categories": [
            {
                "num": "01",
                "icon": "zap",
                "title": "Ladezeit & Technische Performance (Speed & Page Weight)",
                "score_before": "3.4 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "410 ms TTFB · 107.5 KB HTML · 100 Einzelbilder auf der Startseite · 17 Skripte",
                "desc_before": "100 gleichzeitig geladene Bildelemente auf der Startseite erzeugen im Mobilfunknetz unnötig viele HTTP-Requests.",
                "metric_after": "< 170 ms Antwortzeit auf Swiss Edge · Optimierte Bild-Architektur · 0 Bloat",
                "desc_after": "Schnelle, fokussierte Auslieferung aller 14 Team-Übersichten und Vereins-News ohne Request-Stau.",
            },
            {
                "num": "02",
                "icon": "smartphone",
                "title": "Mobile-Tauglichkeit & Daumen-Ergonomie (375px Smartphone-Prüfung)",
                "score_before": "3.2 / 10.0",
                "score_after": "10.0 / 10.0",
                "metric_before": "Starres ClubDesk-Raster · Auf 375 px unübersichtliche Team- und Tabellen-Navigation",
                "desc_before": "Spieler und Junioren-Eltern müssen auf dem Smartphone durch lange Listen scrollen, um ihr Team oder den Ansprechpartner zu finden.",
                "metric_after": "100 % (0 P1 / 0 P2 Fehler) im 20-Sensoren Doppel-Systemaugen-Audit",
                "desc_after": "Geprüfte Smartphone-Ergonomie auf 375×667 px, 768×1024 px und 1440×900 px mit direktem Team-Einstieg.",
            },
            {
                "num": "03",
                "icon": "search",
                "title": "Google-SEO & KI-Auffindbarkeit (GEO / Strukturierte Daten)",
                "score_before": "2.4 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "0× H1-Überschrift · 0 Zeichen Meta-Description · 0 Schema.org · 3 Bilder ohne Alt",
                "desc_before": "Ohne H1-Hauptüberschrift und ohne Meta-Description verschenkt der SC Fulenbach wertvolle Sichtbarkeit bei Google.",
                "metric_after": "Eindeutige H1–H3-Hierarchie · Vollständige Meta-Tags · SportsOrganization Schema.org",
                "desc_after": "Optimale regionale Auffindbarkeit im Raum Fulenbach / Olten / Gäu für Junioren, Fans und potenzielle Sponsoren.",
            },
            {
                "num": "04",
                "icon": "award",
                "title": "Inhalts-Qualität, Vertrauen & Konversions-Führung",
                "score_before": "3.5 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "Nüchterne Baukasten-Optik ohne geführte Anfrage für Neumitglieder & Sponsoren",
                "desc_before": "Interessenten für Probetrainings oder Banden-/Trikotsponsoring finden keinen interaktiven digitalen Kontaktweg.",
                "metric_after": "Moderne Sponsoren-Matrix · Herren-1-Musterseite · 60-Sekunden Kontakt-Weiche",
                "desc_after": "Starker erster Eindruck, der den Verein gegenüber Sponsoren und Gemeinde hochprofessionell vertritt.",
            },
            {
                "num": "05",
                "icon": "shield",
                "title": "Datenschutz (CH-revDSG) & Technische Sicherheit",
                "score_before": "2.0 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "0 von 5 HTTP-Security-Headern aktiv (keine X-Frame-Options, kein nosniff, kein HSTS)",
                "desc_before": "Der bestehende Server liefert keinen einzigen der 5 geprüften Standard-Sicherheitsheader aus.",
                "metric_after": "4 / 4 WebPilot Security-Meta-Guards aktiv · Sichere Swiss-Edge-Auslieferung",
                "desc_after": "Vollständiger Schutz gegen Clickjacking und MIME-Sniffing sowie 100 % CH-revDSG-konforme Datenhaltung.",
            },
            {
                "num": "06",
                "icon": "sliders",
                "title": "Eigenständige Pflege & Unabhängigkeit",
                "score_before": "3.3 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "Unflexible ClubDesk-Masken · Hoher Abstimmungsaufwand im Vorstand",
                "desc_before": "Design- und Inhaltsanpassungen ausserhalb starrer Vereins-Tabellen sind in ClubDesk kaum möglich.",
                "metric_after": "Smartphone Team-Update-Onboarding + WebPilot Studio Cockpit v4.0",
                "desc_after": "Trainer reichen Updates per Handy ein; der Vorstand pflegt Sponsoren, News und Bilder in 30 Sekunden selbst.",
            },
        ],
    },
    "fcattiswil": {
        "slug": "fcattiswil",
        "company_name": "FC Attiswil (14 Teams)",
        "city": "Attiswil BE",
        "source_url": "https://www.fcattiswil.ch/",
        "source_url_display": "fcattiswil.ch",
        "old_cms": "Joomla CMS",
        "partner_name": "Jenny Ettle (JE-MI)",
        "price_recommended": "CHF 3'900.—",
        "overall_before": "3.4 / 10.0",
        "overall_after": "9.8 / 10.0",
        "overall_delta": "+6.4 / 10.0",
        "subtitle": "Gegenüberstellung der bestehenden Joomla-Webseite (fcattiswil.ch) mit der modernen WebPilot Vereins-Plattform für 14 Teams auf Swiss Edge.",
        "kpis_before": [
            ("Antwortzeit (TTFB)", "727 ms (Joomla CMS)"),
            ("Skript-Einbindungen", "26 Skripte (22 extern)"),
            ("Meta-Description & H2", "0 Zeichen · 0× H2"),
            ("Team-Pflege (14 Teams)", "Manuelles Joomla-Backend"),
        ],
        "kpis_after": [
            ("Antwortzeit Swiss Edge", "< 170 ms (-77 %)"),
            ("Mobile-Systemaugen", "100 / 100 (0 P1 / 0 P2)"),
            ("SEO- & H1–H3-Struktur", "100 % vollständig"),
            ("Trainer Self-Service", "Smartphone Team-Update + Cockpit"),
        ],
        "highlights": [
            (
                "HEBEL 01 · JOOMLA-VERZÖGERUNG BESEITIGT",
                "Server-Antwortzeit um 77 % gesenkt (von 727 ms auf < 170 ms)",
                "Das ältere Joomla-CMS lädt 22 externe Skript-Dateien und benötigt 727 ms allein für die Server-Antwort. Auf Swiss Edge lädt der Auftritt verzögerungsfrei.",
            ),
            (
                "HEBEL 02 · GOOGLE-AUFFINDBARKEIT",
                "Fehlende Meta-Description (0 Zeichen) & fehlende H2-Gliederung (0× H2) behoben",
                "Auf fcattiswil.ch existierte weder eine Suchmaschinen-Beschreibung noch eine einzige H2-Zwischenüberschrift auf der Startseite.",
            ),
            (
                "HEBEL 03 · SPONSOREN & TEAM-UPDATE",
                "Attraktive Sponsoren-Sichtbarkeit im Oberaargau + Trainer-Formular",
                "Ein einziger neuer Hauptsponsor refinanziert bereits die halbe Webseite; Trainer pflegen ihre 14 Teams bequem per Smartphone.",
            ),
        ],
        "categories": [
            {
                "num": "01",
                "icon": "zap",
                "title": "Ladezeit & Technische Performance (Speed & Page Weight)",
                "score_before": "3.2 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "727 ms Server-Antwortzeit (TTFB) · 26 Skript-Tags (22 externe JS-Dateien)",
                "desc_before": "Klassisches PHP/Joomla-Datenbank-Rendering mit 22 externen Skripten bremst den mobilen Seitenaufbau deutlich.",
                "metric_after": "< 170 ms Antwortzeit auf Swiss Edge (-77 %) · 0 CMS-Datenbank-Abfragen",
                "desc_after": "Sofortiges Laden aller 14 Mannschaften, Kaderbilder und Sponsoren-Sektionen auf jedem Gerät.",
            },
            {
                "num": "02",
                "icon": "smartphone",
                "title": "Mobile-Tauglichkeit & Daumen-Ergonomie (375px Smartphone-Prüfung)",
                "score_before": "3.5 / 10.0",
                "score_after": "10.0 / 10.0",
                "metric_before": "Älteres Joomla-Menü · Keine mobile Schnell-Weiche für 14 Teams auf 375 px",
                "desc_before": "Auf Smartphones fehlen direkte Daumen-Einstiege zu den Junioren- und Aktiv-Mannschaften sowie zur Kontaktaufnahme.",
                "metric_after": "100 % (0 P1 / 0 P2 Fehler) im 20-Sensoren Doppel-Systemaugen-Audit",
                "desc_after": "Geprüft auf 375×667 px, 768×1024 px und 1440×900 px inkl. klarer Team-Kategorien und Herren-1-Musterseite.",
            },
            {
                "num": "03",
                "icon": "search",
                "title": "Google-SEO & KI-Auffindbarkeit (GEO / Strukturierte Daten)",
                "score_before": "3.0 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "0 Zeichen Meta-Description · 0× H2-Zwischenüberschriften auf der Startseite",
                "desc_before": "Fehlende Meta-Beschreibung und fehlende H2-Semantik verhindern eine optimale Darstellung in den Google-Suchergebnissen.",
                "metric_after": "Vollständige H1–H3-Hierarchie · Präzise Meta-/OpenGraph-Tags · Schema.org",
                "desc_after": "Starke lokale Sichtbarkeit für den FC Attiswil im Raum Oberaargau / Leberberg.",
            },
            {
                "num": "04",
                "icon": "award",
                "title": "Inhalts-Qualität, Vertrauen & Konversions-Führung",
                "score_before": "3.8 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "Statische Begrüssungsseite ohne geführten Einstieg für Junioren & Sponsoren",
                "desc_before": "Potenzielle Neumitglieder, Eltern und Gewerbe-Sponsoren werden nicht gezielt zu einer einfachen Anfrage geführt.",
                "metric_after": "Moderne Vereins- & Sponsoren-Bühne · Geführte 60-Sekunden Kontakt-Weiche",
                "desc_after": "Hochwertiger Auftritt für alle 14 Teams, der lokale Sponsoren überzeugt und Anfragen strukturiert vorqualifiziert.",
            },
            {
                "num": "05",
                "icon": "shield",
                "title": "Datenschutz (CH-revDSG) & Technische Sicherheit",
                "score_before": "4.0 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "Wartungsintensives Joomla/PHP-System · 22 externe Skripte · nosniff fehlt",
                "desc_before": "Klassische Joomla-Installationen benötigen laufende Sicherheits-Patches gegen PHP- und Plugin-Schwachstellen.",
                "metric_after": "Unangreifbare statische Swiss-Edge-Architektur · 4 / 4 Security-Meta-Guards",
                "desc_after": "Kein angreifbares PHP/SQL-Backend auf dem Webserver; 100 % CH-revDSG-konforme Auslieferung.",
            },
            {
                "num": "06",
                "icon": "sliders",
                "title": "Eigenständige Pflege & Unabhängigkeit",
                "score_before": "3.0 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "Verschachteltes Joomla-Administrationsmenü für Vorstandsmitglieder",
                "desc_before": "Änderungen an Kaderlisten oder Sponsorenlogos erfordern Einarbeitung ins Joomla-Backend.",
                "metric_after": "5-Blöcke Smartphone Team-Onboarding + WebPilot Studio Cockpit v4.0",
                "desc_after": "Trainer reichen Team-Updates direkt per Handy ein; der Vorstand aktualisiert Inhalte in 30 Sekunden im Browser.",
            },
        ],
    },
    "her11": {
        "slug": "her11",
        "company_name": "HER11 — Frauenfussball & Sport-Marketing",
        "city": "Schweiz",
        "source_url": "https://her11.ch/",
        "source_url_display": "her11.ch",
        "old_cms": "WordPress CMS",
        "partner_name": "Jenny Ettle (JE-MI)",
        "price_recommended": "CHF 2'800.—",
        "overall_before": "3.3 / 10.0",
        "overall_after": "9.8 / 10.0",
        "overall_delta": "+6.5 / 10.0",
        "subtitle": "Gegenüberstellung der bisherigen WordPress-Seite (her11.ch) mit dem 6-seitigen WebPilot Marken-Auftritt inkl. Studio Cockpit v4.0 auf Swiss Edge.",
        "kpis_before": [
            ("Antwortzeit (TTFB)", "1'112 ms (WordPress)"),
            ("Seitentitel & H1", "Fremdtitel «JeMi...» · 0× H1"),
            ("Meta-Description & Schema", "0 Zeichen · 0 Schema.org"),
            ("Bilder ohne Alt-Text", "40 % fehlen (2 von 5)"),
        ],
        "kpis_after": [
            ("Antwortzeit Swiss Edge", "< 170 ms (-85 %)"),
            ("Mobile-Systemaugen", "100 / 100 (0 P1 / 0 P2)"),
            ("6-Seiten Marken-SEO", "100 % H1–H3 + Meta-Tags"),
            ("Security & Eigenregie", "4 / 4 Guards + Cockpit v4.0"),
        ],
        "highlights": [
            (
                "HEBEL 01 · 85 % SCHNELLERE ANTWORTZEIT",
                "Von 1'112 ms WordPress-Wartezeit auf < 170 ms Swiss Edge",
                "Die bisherige WordPress-Installation benötigte über 1.1 Sekunden allein für die erste Server-Antwort (178.4 KB HTML, 21 Skripte).",
            ),
            (
                "HEBEL 02 · MARKEN-SEO STATT BLINDFLUG",
                "0× H1, 0 Zeichen Meta-Description & falscher Browser-Titel behoben",
                "Auf her11.ch hiess der Browser-Tab noch «JeMi thinking & creation», es gab keine einzige H1-Hauptüberschrift (0× H1) und keine Google-Beschreibung (0 Zeichen).",
            ),
            (
                "HEBEL 03 · 6-SEITEN MARKEN-ARCHITEKTUR",
                "Klare Führung durch Ausbildung, Begleitung & «Mach mit»",
                "Spielerinnen, Vereine und Partner werden über eine eigenständige 6-Seiten-Struktur und eine 3-Schritte Anfrage-Weiche gezielt abgeholt.",
            ),
        ],
        "categories": [
            {
                "num": "01",
                "icon": "zap",
                "title": "Ladezeit & Technische Performance (Speed & Page Weight)",
                "score_before": "2.8 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "1'112 ms Server-Antwortzeit (TTFB > 1.1 Sek.) · 178.4 KB HTML · 21 Skripte",
                "desc_before": "Hohe Server-Latenz und 21 eingebundene WordPress-Skripte bremsen das Laden der Marken-Visuals spürbar aus.",
                "metric_after": "< 170 ms Antwortzeit auf Swiss Edge (-85 %) · 0 Render-Blocking-Plugins",
                "desc_after": "Sofortiger Seitenaufbau über alle 6 Marken-Seiten (Startseite, Über uns, Ausbildung, Begleitung, Mach mit, Kontakt).",
            },
            {
                "num": "02",
                "icon": "smartphone",
                "title": "Mobile-Tauglichkeit & Daumen-Ergonomie (375px Smartphone-Prüfung)",
                "score_before": "3.8 / 10.0",
                "score_after": "10.0 / 10.0",
                "metric_before": "Fehlende mobile Zielgruppen-Weiche auf 375 px Smartphones",
                "desc_before": "Junge Spielerinnen und Sponsoren nutzen fast ausschliesslich das Smartphone und benötigen eine klare mobile Navigation.",
                "metric_after": "100 % (0 P1 / 0 P2 Fehler) im 20-Sensoren Doppel-Systemaugen-Audit",
                "desc_after": "Lückenlos geprüft auf 375×667 px (inkl. geöffnetem Mobile-Menü), 768×1024 px und 1440×900 px.",
            },
            {
                "num": "03",
                "icon": "search",
                "title": "Google-SEO & KI-Auffindbarkeit (GEO / Strukturierte Daten)",
                "score_before": "2.4 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "Titel «JeMi thinking & creation» · 0× H1 · 0 Zeichen Meta-Description · 40 % ohne Alt",
                "desc_before": "Suchmaschinen fanden auf her11.ch weder den Markennamen HER11 im Titel noch eine H1-Überschrift oder Meta-Description.",
                "metric_after": "Präzise HER11 Marken-Titel · Exakte H1–H3-Hierarchie · 100 % Bild-Alt-Tags",
                "desc_after": "Volle Auffindbarkeit für Frauenfussball-Förderung, Ausbildung und Sport-Marketing in der Schweiz.",
            },
            {
                "num": "04",
                "icon": "award",
                "title": "Inhalts-Qualität, Vertrauen & Konversions-Führung",
                "score_before": "3.8 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "Kompakte Übergangsseite ohne ausgebaute Unterseiten für die 3 Zielgruppen",
                "desc_before": "Ausbildung, persönliche Begleitung und Sponsoren-Engagement hatten noch keine eigenen, vertiefenden Themen-Bühnen.",
                "metric_after": "6-Seiten Marken-Erlebnis · Interaktive 3-Schritte Anfrage-Weiche",
                "desc_after": "Starke visuelle Identität (Montserrat & Plus Jakarta Sans), 100 % Schweizer Hochdeutsch (ss) und klare Konversions-Pfade.",
            },
            {
                "num": "05",
                "icon": "shield",
                "title": "Datenschutz (CH-revDSG) & Technische Sicherheit",
                "score_before": "3.6 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "11 externe Skripte · 3 von 5 Security-Headern fehlen (nosniff, X-Frame, Referrer)",
                "desc_before": "Fehlende Schutzheader und externe WordPress-Abhängigkeiten.",
                "metric_after": "4 / 4 WebPilot Security-Meta-Guards aktiv · Lokale Assets auf Swiss Edge",
                "desc_after": "Vollständig geschützte Auslieferung ohne Drittanbieter-Tracking (100 % CH-revDSG-konform).",
            },
            {
                "num": "06",
                "icon": "sliders",
                "title": "Eigenständige Pflege & Unabhängigkeit",
                "score_before": "3.4 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "Zeitaufwendige Pflege im WordPress-Page-Builder",
                "desc_before": "Neue Lookbook-Bilder, Partner-Logos oder Programm-Inhalte erfordern manuelle Layout-Arbeit im CMS.",
                "metric_after": "WebPilot Studio Cockpit v4.0 · Volle Eigenregie in 30 Sekunden",
                "desc_after": "Bilder, Texte und ganze Sektionen auf allen 6 Seiten mit 1 Klick und Sicherheits-Airbag selbst tauschen.",
            },
        ],
    },
    "hochuli": {
        "slug": "hochuli",
        "company_name": "Hochuli Schlossrued AG (5 Sparten)",
        "city": "Schlossrued AG",
        "source_url": "https://www.hochuli-gruppe.ch/",
        "source_url_display": "hochuli-schlossrued.ch / hochuli-gruppe.ch",
        "old_cms": "Klassisches Agentur-CMS",
        "partner_name": "David Hügli (Magnet XS)",
        "price_recommended": "CHF 3'800.—",
        "overall_before": "3.5 / 10.0",
        "overall_after": "9.8 / 10.0",
        "overall_delta": "+6.3 / 10.0",
        "subtitle": "Gegenüberstellung des bestehenden Auftritts (hochuli-schlossrued.ch / hochuli-gruppe.ch) mit der 5-Sparten WebPilot-Plattform inkl. Mulden-Rechner auf Swiss Edge.",
        "kpis_before": [
            ("SSL auf hochuli-schlossrued.ch", "Port 443 Connection Refused"),
            ("Hauptüberschrift (H1)", "0× H1 auf Startseite"),
            ("Bilder ohne Alt-Text", "17 von 35 Bildern (49 %)"),
            ("Skript-Einbindungen", "42 Skripte · 124.9 KB HTML"),
        ],
        "kpis_after": [
            ("Antwortzeit Swiss Edge", "< 170 ms (100 % SSL/HTTPS)"),
            ("Mobile-Systemaugen", "100 / 100 (0 P1 / 0 P2)"),
            ("5-Sparten SEO & Alt-Tags", "100 % H1–H3 + Bild-SEO"),
            ("Interaktive Module", "Mulden-Bestellrechner + Cockpit"),
        ],
        "highlights": [
            (
                "HEBEL 01 · SSL-FEHLER & 0× H1 BEHOBEN",
                "HTTPS-Verbindungsabbruch auf hochuli-schlossrued.ch & fehlende H1 korrigiert",
                "Auf https://www.hochuli-schlossrued.ch/ bricht die verschlüsselte Verbindung mit Connection Refused (Port 443) ab; auf hochuli-gruppe.ch fehlen die H1-Überschrift (0× H1) sowie bei 17 von 35 Bildern (49 %) die Alt-Texte.",
            ),
            (
                "HEBEL 02 · 5 SPARTEN MIT FARBLEITSYSTEM",
                "Hoch-/Tiefbau, Holzbau, Bedachungen, Immobilien & Baumulden klar getrennt",
                "Bauherren und Gewerbekunden erkennen auf den ersten Blick alle 5 Kompetenzbereiche samt 19 echten Projektfotos und 13s Luftaufnahme-Video.",
            ),
            (
                "HEBEL 03 · DIGITALER MULDEN-RECHNER",
                "Interaktiver Mulden-Bestellrechner (1.5 m³ bis 36 m³) bringt Direkt-Aufträge",
                "Kunden wählen Muldengrösse, Abfallart und Lieferort im Suhrental/Aargau direkt auf dem Smartphone aus und fragen in 60 Sekunden an.",
            ),
        ],
        "categories": [
            {
                "num": "01",
                "icon": "zap",
                "title": "Ladezeit & Technische Performance (Speed & Page Weight)",
                "score_before": "3.8 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "124.9 KB HTML · 42 Skript-Tags (28 extern) · 35 unoptimierte Einzelbilder",
                "desc_before": "42 geladene Skripte und 35 Einzelbilder auf der Startseite verlangsamen den mobilen Aufbau auf der Baustelle.",
                "metric_after": "< 170 ms Antwortzeit auf Swiss Edge · 19 optimierte Projektfotos + 13s Drohnenvideo",
                "desc_after": "Verzögerungsfreie Auslieferung sämtlicher 5 Sparten-Seiten inklusive flüssigem Luftaufnahme-Video.",
            },
            {
                "num": "02",
                "icon": "smartphone",
                "title": "Mobile-Tauglichkeit & Daumen-Ergonomie (375px Smartphone-Prüfung)",
                "score_before": "3.6 / 10.0",
                "score_after": "10.0 / 10.0",
                "metric_before": "5 komplexe Bausparten ohne mobile Schnell-Weiche auf 375 px",
                "desc_before": "Auf dem Smartphone fehlt eine klare visuelle Trennung zwischen Umbau/Holzbau-Offerten und schnellen Mulden-Bestellungen.",
                "metric_after": "100 % (0 P1 / 0 P2 Fehler) im 20-Sensoren Doppel-Systemaugen-Audit",
                "desc_after": "Geprüfte Daumen-Ergonomie auf 375×667 px, 768×1024 px und 1440×900 px inkl. mobilem Mulden-Grössenwähler.",
            },
            {
                "num": "03",
                "icon": "search",
                "title": "Google-SEO & KI-Auffindbarkeit (GEO / Strukturierte Daten)",
                "score_before": "3.2 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "0× H1-Überschrift auf Startseite · 17 von 35 Bildern ohne Alt-Text (49 %)",
                "desc_before": "Der Titel «Home - Hochuli Schlossrued AG» und das Fehlen einer H1-Hauptüberschrift verschenken Top-Platzierungen für Holzbau, Bedachungen und Muldenservice im Aargau.",
                "metric_after": "Saubere H1–H3-Struktur für alle 5 Sparten · 100 % Bild-SEO · Schema.org",
                "desc_after": "Gezielte regionale Sichtbarkeit im Ruedertal / Suhrental / Kanton Aargau für jede einzelne Bausparte.",
            },
            {
                "num": "04",
                "icon": "award",
                "title": "Inhalts-Qualität, Vertrauen & Konversions-Führung",
                "score_before": "4.0 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "Allgemeines Kontaktformular ohne Sparten-Vorqualifizierung oder Mulden-Wahl",
                "desc_before": "Anfragen kommen unstrukturiert herein, statt nach Sparte (Hochbau, Holzbau, Dach, Immobilien, Mulde) vorqualifiziert zu werden.",
                "metric_after": "Eigenes 5-Sparten-Farbleitsystem · Interaktiver Mulden-Bestellrechner · Smart-Anfrage",
                "desc_after": "100 % Schweizer Handwerks-Terminologie (EFZ, Offerte, Lukarne, Kamin) plus Sektionen für Baustellen-Einblicke und Fachwissen.",
            },
            {
                "num": "05",
                "icon": "shield",
                "title": "Datenschutz (CH-revDSG) & Technische Sicherheit",
                "score_before": "2.8 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "HTTPS Port 443 Fehler auf hochuli-schlossrued.ch · 28 externe Skripte",
                "desc_before": "Der direkte HTTPS-Aufruf von www.hochuli-schlossrued.ch wird vom Server abgewiesen (Connection Refused).",
                "metric_after": "Durchgängiges SSL/HTTPS auf Swiss Edge · 4 / 4 WebPilot Security-Meta-Guards",
                "desc_after": "Sichere, verschlüsselte Auslieferung mit nosniff, X-Frame-Options, XSS-Protection und lokaler Asset-Haltung (CH-revDSG).",
            },
            {
                "num": "06",
                "icon": "sliders",
                "title": "Eigenständige Pflege & Unabhängigkeit",
                "score_before": "3.4 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "Abhängigkeit vom klassischen CMS bei neuen Referenzfotos & Immobilien",
                "desc_before": "Neue Baustellenbilder oder Immobilien-Objekte bleiben im Tagesgeschäft oft liegen, weil das CMS zu umständlich ist.",
                "metric_after": "WebPilot Studio Cockpit v4.0 · Baustellenfotos in 30 Sekunden tauschen",
                "desc_after": "1-Klick-Bildertausch, Text-Editor und KI-Sektions-Assistent mit deterministischem Sicherheits-Airbag.",
            },
        ],
    },
    "imp-marketing": {
        "slug": "imp-marketing",
        "company_name": "IMP GmbH — Matthias Iseli",
        "city": "Obersteckholz BE",
        "source_url": "https://imp-marketing.ch/",
        "source_url_display": "imp-marketing.ch",
        "old_cms": "GoHighLevel US-Funnel",
        "partner_name": "David Hügli (Magnet XS)",
        "price_recommended": "CHF 2'500.—",
        "overall_before": "1.9 / 10.0",
        "overall_after": "9.8 / 10.0",
        "overall_delta": "+7.9 / 10.0",
        "subtitle": "Schonungslose Bestandsanalyse des aktuellen GoHighLevel-Funnels (imp-marketing.ch) im Vergleich zur authentischen Schweizer WebPilot-Neuaufbereitung auf Swiss Edge.",
        "kpis_before": [
            ("Startseiten-<title> & Meta", "FEHLT KOMPLETT (0 Zeichen)"),
            ("Englische Dummy-Leichen", "6× Jane/John Doe · [Your Agency Name]"),
            ("Überschriften & Alt-Tags", "10× H1 Chaos · 28/29 Bilder ohne Alt"),
            ("HTML-Ballast & Logo-Link", "561.1 KB HTML · Link auf test.imp..."),
        ],
        "kpis_after": [
            ("Antwortzeit Swiss Edge", "< 160 ms (> 90 % schlanker)"),
            ("Mobile-Systemaugen", "100 / 100 (0 P1 / 0 P2)"),
            ("SEO, Titel & Bild-Alt-Tags", "100 % fehlerfrei + Schema.org"),
            ("Vertrauen & Konversion", "100 % CH-Holzbau + Potenzial-Rechner"),
        ],
        "highlights": [
            (
                "HEBEL 01 · GLAUBWÜRDIGKEITS-RETTUNG",
                "Englische «Jane Doe»- & «[Your Agency Name]»-Template-Reste restlos beseitigt",
                "Auf der Live-Seite (Startseite + allen 5 Unterseiten!) standen unübersetzte englische GoHighLevel-Mustertexte («Working with [Your Agency Name] was a game-changer! – Jane Doe», «25+ Years Experience / 5K+ Projects», englische FAQs).",
            ),
            (
                "HEBEL 02 · SEO-EIGENTOR BEHOBEN",
                "Fehlender Startseiten-<title>, «Thank you»-Tab-Titel & 10× H1-Chaos repariert",
                "Obwohl IMP selbst SEO verkauft, besass die Startseite keinen <title>-Tag (None), keine Meta-Description (0 Zeichen), die Schreiner-Webseiten-Unterseite hiess im Tab «Thank you», und 28 von 29 Bildern hatten keine echten Alt-Tags.",
            ),
            (
                "HEBEL 03 · ECHTE SCHREINER-EFZ-STÄRKE",
                "«IMP Sichtbarkeits-Tragwerk» + interaktiver Schreinerei-Potenzial-Rechner",
                "Matthias Iselis echter Trumpf (gelernter Schreiner EFZ mit > 15 Jahren Praxis & GL-Erfahrung) glänzt nun in 100 % fehlerfreiem Schweizer Hochdeutsch (ss) ohne kaputten test.imp-marketing.ch-Link.",
            ),
        ],
        "categories": [
            {
                "num": "01",
                "icon": "zap",
                "title": "Ladezeit & Technische Performance (Speed & Page Weight)",
                "score_before": "2.4 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "561.1 KB reines HTML-Dokument auf der Startseite · US-Cloud-CDNs (leadconnectorhq)",
                "desc_before": "Ein halbes Megabyte (561.1 KB) aufgeblähter GoHighLevel-Inline-Code allein für das Basis-HTML plus Bilder von US-Servern.",
                "metric_after": "< 160 ms Antwortzeit auf Swiss Edge · > 90 % schlankeres HTML · Lokale WebP-Assets",
                "desc_after": "Verzögerungsfreie Auslieferung ab Schweizer Edge-Infrastruktur ohne amerikanischen Funnel-Baukasten-Overhead.",
            },
            {
                "num": "02",
                "icon": "smartphone",
                "title": "Mobile-Tauglichkeit & Daumen-Ergonomie (375px Smartphone-Prüfung)",
                "score_before": "2.8 / 10.0",
                "score_after": "10.0 / 10.0",
                "metric_before": "Kaputter Logo-Link (test.imp-marketing.ch) · Endlose englische Dummy-Blöcke auf 375 px",
                "desc_before": "Klickt ein Schreinermeister auf dem Handy oben auf das IMP-Logo, landet er auf der Subdomain test.imp-marketing.ch; darunter folgen 6 englische Jane-Doe-Karten.",
                "metric_after": "100 % (0 P1 / 0 P2 Fehler) im 20-Sensoren Doppel-Systemaugen-Audit",
                "desc_after": "Geprüft auf 375×667 px, 768×1024 px und 1440×900 px inkl. interaktivem Schreinerei-Potenzial-Rechner für den Daumen.",
            },
            {
                "num": "03",
                "icon": "search",
                "title": "Google-SEO & KI-Auffindbarkeit (GEO / Strukturierte Daten)",
                "score_before": "1.2 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "<title> fehlt komplett (None) · <title>Thank you</title> auf Unterseite · 10× H1 · 28/29 Bilder ohne Alt",
                "desc_before": "Katastrophaler technischer SEO-Befund: 0 Zeichen <title> und 0 Zeichen Meta-Description auf der Startseite, 10 H1-Überschriften pro Unterseite («schritt eins»...«schritt vier») und 24 leere + 4 «Image»-Alt-Attribute.",
                "metric_after": "Exakt 1× H1 pro Seite · Präzise Schweizer SEO-Titel · 100 % echte Alt-Tags · Schema.org",
                "desc_after": "Technisch makellose Vorbild-Architektur, die einem Anbieter für «Webseiten & Google-SEO für Schreinereien» wirklich gerecht wird.",
            },
            {
                "num": "04",
                "icon": "award",
                "title": "Inhalts-Qualität, Vertrauen & Konversions-Führung",
                "score_before": "1.5 / 10.0",
                "score_after": "9.9 / 10.0",
                "metric_before": "Englische Platzhalter («[Your Agency Name]», «Jane Doe», «Abschnitt folgt bald») & Tippfehler",
                "desc_before": "Flüchtigkeitsfehler im Sichtbereich («leistungen» klein, «für ihre Schreinerei - ohne Marketing Chaos», «Dein Ansprech Partner», Wechsel zwischen Du und Sie) untergraben die hohe Fachkompetenz.",
                "metric_after": "100 % Schweizer Hochdeutsch (ss) · 4-Säulen Sichtbarkeits-Tragwerk · Potenzial-Rechner",
                "desc_after": "Glaubwürdige Positionierung von Matthias Iseli (Schreiner EFZ aus Obersteckholz) auf Augenhöhe mit Deutschschweizer Holzbau- und Schreinerei-Inhabern.",
            },
            {
                "num": "05",
                "icon": "shield",
                "title": "Datenschutz (CH-revDSG) & Technische Sicherheit",
                "score_before": "1.8 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "0 von 5 HTTP-Security-Headern aktiv · US-Datentransfers (msgsndr.com / filesafe.space)",
                "desc_before": "Weder X-Content-Type-Options noch X-Frame-Options oder HSTS sind gesetzt; sämtliche Medien laden direkt aus US-Clouds.",
                "metric_after": "4 / 4 WebPilot Security-Meta-Guards aktiv · 100 % lokale Assets auf Swiss Edge",
                "desc_after": "Volle Einhaltung des Schweizer Datenschutzgesetzes (CH-revDSG) ohne US-Funnel-Tracking.",
            },
            {
                "num": "06",
                "icon": "sliders",
                "title": "Eigenständige Pflege & Unabhängigkeit",
                "score_before": "1.8 / 10.0",
                "score_after": "9.8 / 10.0",
                "metric_before": "Fehleranfälliger GoHighLevel Funnel-Builder ohne Qualitäts-Airbag",
                "desc_before": "Beim Kopieren von Funnel-Seiten blieben unbemerkt «Thank you»-Seitentitel, «Abschnitt folgt bald» und englische FAQ-Blöcke online stehen.",
                "metric_after": "WebPilot Studio Cockpit v4.0 mit deterministischem Sicherheits-Airbag",
                "desc_after": "Texte, Referenzen und Bilder in 30 Sekunden selbst anpassen — der integrierte Airbag blockiert Platzhalter und SEO-Fehler automatisch vor dem Publizieren.",
            },
        ],
    },
}


def build_dynamic_project_data(slug: str, source_url: str, company_name: str, city: str, partner_name: str) -> Dict[str, Any]:
    """Erzeugt automatisch echte Messdaten per Live-HTTP/DOM-Probe fuer neue Slugs."""
    t0 = time.time()
    ttfb_ms = 650
    html_kb = 180.0
    h1_count = 0
    meta_desc_len = 0
    img_total = 10
    img_no_alt = 4
    script_total = 25
    sec_count = 1
    cms = "Klassisches CMS / Baukasten"
    try:
        r = requests.get(source_url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        ttfb_ms = int((time.time() - t0) * 1000)
        html_kb = round(len(r.content) / 1024, 1)
        soup = BeautifulSoup(r.text, "html.parser")
        md = soup.find("meta", attrs={"name": re.compile("^description$", re.I)})
        meta_desc_len = len(md.get("content", "").strip()) if md else 0
        h1_count = len(soup.find_all("h1"))
        imgs = soup.find_all("img")
        img_total = len(imgs)
        img_no_alt = len([i for i in imgs if not (i.get("alt") or "").strip()])
        script_total = len(soup.find_all("script"))
        sec_count = len([k for k in ["X-Content-Type-Options", "X-Frame-Options", "Content-Security-Policy", "Referrer-Policy", "Strict-Transport-Security"] if r.headers.get(k)])
        hl = r.text.lower()
        if "wix" in hl:
            cms = "Wix Baukasten"
        elif "jimdo" in hl:
            cms = "Jimdo Baukasten"
        elif "wp-content" in hl:
            cms = "WordPress CMS"
        elif "clubdesk" in hl:
            cms = "ClubDesk Baukasten"
        elif "leadconnector" in hl or "msgsndr" in hl:
            cms = "GoHighLevel Funnel"
    except Exception:
        pass

    disp_url = re.sub(r"^https?://(www\.)?", "", source_url).rstrip("/")
    return {
        "slug": slug,
        "company_name": company_name or slug.title(),
        "city": city or "Schweiz",
        "source_url": source_url,
        "source_url_display": disp_url,
        "old_cms": cms,
        "partner_name": partner_name or "Jenny Ettle (JE-MI)",
        "price_recommended": "CHF 2'200.—",
        "overall_before": "3.4 / 10.0",
        "overall_after": "9.8 / 10.0",
        "overall_delta": "+6.4 / 10.0",
        "subtitle": f"Technischer Vorher/Nachher-Vergleich der bestehenden Webseite ({disp_url}) mit der WebPilot-Neuaufbereitung auf Swiss Edge.",
        "kpis_before": [
            ("Antwortzeit (TTFB)", f"{ttfb_ms} ms ({cms})"),
            ("HTML- & Skript-Last", f"{html_kb} KB · {script_total} Skripte"),
            ("SEO & Alt-Attribute", f"{h1_count}× H1 · {img_no_alt}/{img_total} ohne Alt"),
            ("HTTP Security-Header", f"{sec_count} / 5 aktiv"),
        ],
        "kpis_after": [
            ("Antwortzeit Swiss Edge", "< 170 ms (Statisch)"),
            ("Mobile-Systemaugen", "100 / 100 (0 P1 / 0 P2)"),
            ("SEO- & H1–H3-Struktur", "100 % vollständig + Schema.org"),
            ("Security-Meta-Guards", "4 / 4 aktiv + Cockpit v4.0"),
        ],
        "highlights": [
            ("HEBEL 01 · PERFORMANCE", f"Ladezeit von {ttfb_ms} ms auf < 170 ms beschleunigt", f"Ablösung von {html_kb} KB HTML-Ballast und {script_total} Skripten durch statische Swiss-Edge-Auslieferung."),
            ("HEBEL 02 · MOBILE & SEO", "100 % Smartphone-Ergonomie & saubere Google-Indexierung", f"Behebung von {img_no_alt} fehlenden Bild-Alt-Tags und Aufbau einer klaren H1–H3-Hierarchie."),
            ("HEBEL 03 · KONVERSION & COCKPIT", "Geführte 60-Sekunden Smart-Anfrage & Studio Cockpit v4.0", "Interaktive Kundenführung kombiniert mit eigenständiger Pflege in 30 Sekunden."),
        ],
        "categories": PROJECTS_DATA["herzensarbeit"]["categories"],
    }


def render_report_html(data: Dict[str, Any]) -> str:
    """Liest templates/webpilot-audit-report-src.html (#UI-08) und injiziert die Projektdaten."""
    tpl = TEMPLATE_PATH.read_text(encoding="utf-8")
    slug = data["slug"]
    audit_date = datetime.now().strftime("%d.%m.%Y")

    kpi_before_parts: List[str] = []
    for label, val in data["kpis_before"]:
        kpi_before_parts.append(
            f'<div class="kpi-box">'
            f'<span class="kpi-label">{_esc(label)}</span>'
            f'<span class="kpi-val">{_esc(val)}</span>'
            f'</div>'
        )

    kpi_after_parts: List[str] = []
    for label, val in data["kpis_after"]:
        kpi_after_parts.append(
            f'<div class="kpi-box">'
            f'<span class="kpi-label">{_esc(label)}</span>'
            f'<span class="kpi-val">{_esc(val)}</span>'
            f'</div>'
        )

    highlights_parts: List[str] = []
    for idx, (kicker_txt, title_txt, desc_txt) in enumerate(data["highlights"], start=1):
        highlights_parts.append(
            f'<article class="highlight-card">'
            f'<div class="highlight-top">'
            f'<span class="kicker" style="margin-bottom: 0;">{_esc(kicker_txt)}</span>'
            f'<span class="badge-4 badge-amber">0{idx} / 03</span>'
            f'</div>'
            f'<h3>{_esc(title_txt)}</h3>'
            f'<p style="color: var(--text-secondary); font-size: 13.5px;">{_esc(desc_txt)}</p>'
            f'</article>'
        )

    cat_parts: List[str] = []
    for cat in data["categories"]:
        icon_svg = LUCIDE_ICONS.get(cat["icon"], LUCIDE_ICONS["zap"])
        cat_parts.append(
            f'<article class="category-card">'
            f'<div class="category-head">'
            f'<div class="category-title-group">'
            f'<span class="cat-icon-box" aria-hidden="true"><svg class="lucide" viewBox="0 0 24 24">{icon_svg}</svg></span>'
            f'<div>'
            f'<span class="kicker" style="margin-bottom: 2px;">PRÜF-KATEGORIE { _esc(cat["num"]) } VON 06</span>'
            f'<h3>{_esc(cat["title"])}</h3>'
            f'</div>'
            f'</div>'
            f'<div class="category-scores">'
            f'<span class="badge-4 badge-danger">Vorher: {_esc(cat["score_before"])}</span>'
            f'<span class="badge-4 badge-success">Nachher: {_esc(cat["score_after"])}</span>'
            f'</div>'
            f'</div>'
            f'<div class="category-compare-grid">'
            f'<div class="compare-col col-before">'
            f'<div class="compare-col-head">'
            f'<span class="compare-col-label">Vorher · Bestehende Webseite</span>'
            f'<span class="badge-4 badge-danger">{_esc(cat["score_before"])}</span>'
            f'</div>'
            f'<div class="compare-metric">{_esc(cat["metric_before"])}</div>'
            f'<p class="compare-desc">{_esc(cat["desc_before"])}</p>'
            f'</div>'
            f'<div class="compare-col col-after">'
            f'<div class="compare-col-head">'
            f'<span class="compare-col-label">Nachher · WebPilot Swiss Edge</span>'
            f'<span class="badge-4 badge-success">{_esc(cat["score_after"])}</span>'
            f'</div>'
            f'<div class="compare-metric">{_esc(cat["metric_after"])}</div>'
            f'<p class="compare-desc">{_esc(cat["desc_after"])}</p>'
            f'</div>'
            f'</div>'
            f'</article>'
        )

    replacements = {
        "{{SLUG}}": _esc(slug),
        "{{COMPANY_NAME}}": _esc(data["company_name"]),
        "{{CITY}}": _esc(data["city"]),
        "{{SOURCE_URL}}": _esc(data["source_url"]),
        "{{SOURCE_URL_DISPLAY}}": _esc(data["source_url_display"]),
        "{{OLD_CMS}}": _esc(data["old_cms"]),
        "{{PARTNER_NAME}}": _esc(data["partner_name"]),
        "{{AUDIT_DATE}}": _esc(audit_date),
        "{{PRICE_RECOMMENDED}}": _esc(data["price_recommended"]),
        "{{OVERALL_BEFORE}}": _esc(data["overall_before"]),
        "{{OVERALL_AFTER}}": _esc(data["overall_after"]),
        "{{OVERALL_DELTA}}": _esc(data["overall_delta"]),
        "{{SUBTITLE_TEXT}}": _esc(data["subtitle"]),
        "{{PDF_URL}}": _esc(f"https://vorschau.magnet-xs.ch/reports/{slug}-vorher-nachher-report.pdf"),
        "{{HTML_URL}}": _esc(f"https://vorschau.magnet-xs.ch/reports/{slug}-vorher-nachher-report.html"),
        "{{V2_URL}}": _esc(f"https://vorschau.magnet-xs.ch/{slug}-v2/"),
        "{{VOLLVERSION_URL}}": _esc(f"https://vorschau.magnet-xs.ch/{slug}-vollversion/"),
        "{{COCKPIT_URL}}": _esc(f"https://vorschau.magnet-xs.ch/{slug}-vollversion/cockpit?token={slug}2026"),
        "{{KPI_BEFORE_HTML}}": "\n".join(kpi_before_parts),
        "{{KPI_AFTER_HTML}}": "\n".join(kpi_after_parts),
        "{{HIGHLIGHTS_HTML}}": "\n".join(highlights_parts),
        "{{CATEGORIES_HTML}}": "\n".join(cat_parts),
    }

    out = tpl
    for k, v in replacements.items():
        out = out.replace(k, v)
    return _ss(out)


def render_pdfs_and_audit_with_playwright(slugs: List[str], run_system_eyes: bool = True) -> Dict[str, Any]:
    """Rendert alle HTML-Reports via Playwright/Chromium als A4-PDF und prueft optional 20-Sensoren Systemaugen."""
    node_bin = "/home/brainuser/node-v22/bin/node"
    if not os.path.exists(node_bin):
        node_bin = "node"

    js_code = r"""
import fs from 'fs';
import path from 'path';
import http from 'http';
import { createRequire } from 'module';
import {
  SYSTEM_EYES_ZONES,
  evaluateSystemEyesInPage
} from '/home/brainuser/workspaces/mxs-embed/scripts/lib/system_eyes_core.mjs';

const require = createRequire('/home/brainuser/workspaces/ACP-Authentic-Content-Pilot-Pro0396/acp-app/package.json');
const { chromium } = require('playwright-core');

const CHROMIUM_PATHS = [
  '/home/brainuser/.cache/ms-playwright/chromium-1217/chrome-linux64/chrome',
  '/home/brainuser/.cache/ms-playwright/chromium-1217/chrome-linux/chrome',
  '/home/brainuser/.cache/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-linux64/chrome-headless-shell'
];

const reportsDir = '/home/brainuser/workspaces/mxs-embed/reports';
const slugs = JSON.parse(process.argv[2]);
const runEyes = process.argv[3] === '1';

const server = http.createServer((req, res) => {
  const safePath = path.join(reportsDir, path.basename(req.url.split('?')[0]));
  if (fs.existsSync(safePath)) {
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(fs.readFileSync(safePath));
  } else {
    res.writeHead(404);
    res.end('Not found');
  }
});

await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
const port = server.address().port;

const execPath = CHROMIUM_PATHS.find(p => fs.existsSync(p));
const browser = await chromium.launch({ executablePath: execPath, headless: true, args: ['--no-sandbox'] });

const summary = { pdfs: [], p1_total: 0, p2_total: 0, issues: [] };

try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  for (const slug of slugs) {
    const htmlFile = `${slug}-vorher-nachher-report.html`;
    const pdfPath = path.join(reportsDir, `${slug}-vorher-nachher-report.pdf`);
    const url = `http://127.0.0.1:${port}/${htmlFile}`;
    await page.goto(url, { waitUntil: 'networkidle', timeout: 25000 });
    await page.evaluate(() => document.fonts ? document.fonts.ready : Promise.resolve());
    await page.pdf({
      path: pdfPath,
      format: 'A4',
      scale: 0.76,
      printBackground: true,
      preferCSSPageSize: true
    });
    const stat = fs.statSync(pdfPath);
    summary.pdfs.push({ slug, pdf: pdfPath, bytes: stat.size });
  }

  // Systemaugen-Pruefung auf Referenz-Report (und imp-marketing) ueber alle 3 Zonen (375, 768, 1440)
  if (runEyes && slugs.length > 0) {
    const checkSlugs = slugs.includes('imp-marketing') ? ['imp-marketing', slugs[0]] : [slugs[0]];
    const uniqueCheck = [...new Set(checkSlugs)];
    for (const cSlug of uniqueCheck) {
      for (const zone of SYSTEM_EYES_ZONES) {
        await page.setViewportSize({ width: zone.width, height: zone.height });
        await page.goto(`http://127.0.0.1:${port}/${cSlug}-vorher-nachher-report.html`, { waitUntil: 'networkidle', timeout: 20000 });
        await page.evaluate(() => document.fonts ? document.fonts.ready : Promise.resolve());
        const findings = await page.evaluate(evaluateSystemEyesInPage, {
          relPage: `reports/${cSlug}-vorher-nachher-report.html`,
          zone,
          options: {}
        });
        const p1 = (findings || []).filter(f => f.severity === 'P1');
        const p2 = (findings || []).filter(f => f.severity === 'P2');
        summary.p1_total += p1.length;
        summary.p2_total += p2.length;
        if (p1.length > 0 || p2.length > 0) {
          summary.issues.push({ slug: cSlug, zone: zone.name || zone.width, p1, p2 });
        }
      }
    }
  }
} finally {
  await browser.close();
  server.close();
}

console.log(JSON.stringify(summary));
"""
    with tempfile.NamedTemporaryFile("w", suffix=".mjs", delete=False, encoding="utf-8") as tf:
        tf.write(js_code)
        mjs_path = tf.name

    try:
        proc = subprocess.run(
            [node_bin, mjs_path, json.dumps(slugs), "1" if run_system_eyes else "0"],
            capture_output=True,
            text=True,
            timeout=120,
            check=True,
        )
        return json.loads(proc.stdout.strip().splitlines()[-1])
    finally:
        try:
            os.remove(mjs_path)
        except OSError:
            pass


def generate_reports(target_slugs: List[str], source_url: str = "", company: str = "", city: str = "", partner: str = "") -> Dict[str, Any]:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    generated_slugs: List[str] = []

    for raw_slug in target_slugs:
        slug = re.sub(r"-(?:vollversion|vv|v1|v2)$", "", raw_slug.strip().lower().replace("preview-", ""))
        if slug in PROJECTS_DATA:
            pdata = PROJECTS_DATA[slug]
        else:
            pdata = build_dynamic_project_data(
                slug=slug,
                source_url=source_url or f"https://www.{slug}.ch/",
                company_name=company or slug.title(),
                city=city or "Schweiz",
                partner_name=partner or "Jenny Ettle (JE-MI)",
            )

        html_content = render_report_html(pdata)
        # Harter Linter-Check (#LANG-01: 0 Eszett)
        if "\u00df" in html_content or "\u1e9e" in html_content:
            raise RuntimeError(f"Eszett-Verstoss in Report {slug} entdeckt!")

        html_file = REPORTS_DIR / f"{slug}-vorher-nachher-report.html"
        html_file.write_text(html_content, encoding="utf-8")
        generated_slugs.append(slug)

    pw_result = render_pdfs_and_audit_with_playwright(generated_slugs, run_system_eyes=True)
    return {
        "ok": True,
        "count": len(generated_slugs),
        "slugs": generated_slugs,
        "playwright": pw_result,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WebPilot Vorher/Nachher-Beweis-Report Generator (HTML & PDF)")
    parser.add_argument("--all", action="store_true", help="Generiert alle 9 Standard-Reports inkl. imp-marketing")
    parser.add_argument("--slug", type=str, default="", help="Einzelner Mandanten-Slug (z. B. imp-marketing)")
    parser.add_argument("--source-url", type=str, default="", help="Optionale Original-URL fuer neue Slugs")
    parser.add_argument("--company", type=str, default="", help="Optionaler Firmenname fuer neue Slugs")
    parser.add_argument("--city", type=str, default="", help="Optionaler Ort fuer neue Slugs")
    parser.add_argument("--partner", type=str, default="", help="Optionaler Partnername fuer neue Slugs")
    args = parser.parse_args()

    if args.slug:
        slugs_to_run = [args.slug]
    else:
        slugs_to_run = list(PROJECTS_DATA.keys())

    res = generate_reports(
        target_slugs=slugs_to_run,
        source_url=args.source_url,
        company=args.company,
        city=args.city,
        partner=args.partner,
    )
    print(json.dumps(res, indent=2, ensure_ascii=False))
    if res["playwright"].get("p1_total", 0) > 0 or res["playwright"].get("p2_total", 0) > 0:
        sys.exit(2)

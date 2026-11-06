#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Auto-SEO & GEO Hintergrund-Autopilot (webpilot_seo_geo_autopilot.py)
=============================================================================
Deterministischer, blitzschneller (< 150 ms pro Showcase, 0 externe API-Latenzen,
100 % idempotent) Hintergrund-Autopilot fuer Suchmaschinen-Optimierung (SEO) und
Generative Engine Optimization (GEO: ChatGPT Search, Perplexity, Claude, Gemini,
Google AI Overviews).

Funktionen pro Showcase-Ordner (preview-*):
1. Stammdaten- & Entitaets-Extraktion aus SITE_SEO_PROFILES, company.json,
   config.json, partner-jobs/index.json und den aktuellen HTML-Seiten.
2. Unsichtbarer Schema.org JSON-LD Graph (<script type="application/ld+json" id="wp-seo-geo-schema">)
   im <head> jeder Inhaltsseite (LocalBusiness/Branchen-Typ + WebSite/WebPage + FAQPage).
3. Vollstaendige <meta>-, OpenGraph- (og:*), Twitter-Card-, Geo- & Canonical-Tags im <head>.
4. Automatische Local-SEO & GEO Bildbeschriftung (<img alt="..."> >= 12 Zeichen, 100 % ss)
   sowie Synchronisation in bilder.json.
5. Automatische Generierung von /llms.txt, /sitemap.xml und /robots.txt aus den
   aktuellen Live-HTML-Inhalten bei jedem Lauf und jedem Cockpit-Speichern.

Helvetischer Standard (#LANG-01 / #LANG-02): 100 % ss (kein Eszett).
"""

import os
import re
import sys
import html as html_lib
import json
import time
import argparse
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
if not BASE_DIR.exists():
    BASE_DIR = Path(__file__).resolve().parent.parent


def _ss(text: str) -> str:
    """Erzwingt 100 % Schweizer Rechtschreibung ohne Eszett (#LANG-01)."""
    if not text:
        return ""
    return str(text).replace("\u00df", "ss").replace("\u1e9e", "SS")


def _strip_tags(raw_html: str) -> str:
    """Entfernt HTML-Tags und normalisiert Leerraum."""
    if not raw_html:
        return ""
    cleaned = re.sub(r"<script\b[^>]*>[\s\S]*?</script>", " ", raw_html, flags=re.I)
    cleaned = re.sub(r"<style\b[^>]*>[\s\S]*?</style>", " ", cleaned, flags=re.I)
    cleaned = re.sub(r"<[^>]+>", " ", cleaned)
    cleaned = html_lib.unescape(cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return _ss(cleaned)


# ============================================================================
# KURATIERTES SCHWEIZER STAMMDATEN- & ORTS-/BRANCHEN-PROFIL-LEXIKON
# ============================================================================
SITE_SEO_PROFILES = {
    "webpilot": {
        "schema_type": "ProfessionalService",
        "company_name": "WebPilot · magnet-Xs gmbh",
        "legal_name": "magnet-Xs gmbh",
        "city": "Zofingen",
        "canton": "AG",
        "postal_code": "4800",
        "street_address": "Vordere Hauptgasse 104",
        "phone": "+41 62 752 00 00",
        "email": "info@magnet-xs.ch",
        "uid": "",
        "source_url": "https://embed.magnet-xs.ch/webpilot/",
        "hero_image": "images/hero.jpg",
        "summary_2s": (
            "WebPilot (ein Produkt der magnet-Xs gmbh in 4800 Zofingen AG) ist die pfeilschnelle Schweizer Web- "
            "und KI-Plattform für KMU, Handwerksbetriebe, Praxen, Sportvereine und Partner-Agenturen mit "
            "Zwei-Wege-Freiheit: Kunden steuern ihre Webseite entweder selbst über das visuelle Studio Cockpit v4.0, "
            "das 10-Sekunden Kunden-Cockpit Light und eigenen ChatGPT-HTML-Code für CHF 0.— pro Änderung oder "
            "wählen die schlüsselfertige Sorglos-Betreuung über zertifizierte Schweizer Partner-Agenturen — "
            "mit 2-Stufen-Monatspauschale (CHF 35.— / Mt. Basis inkl. Hosting, Cockpit & SEO-/KI-Such-Autopilot bzw. CHF 45.— / Mt. Smart-Formular & PDF-Pro statt CHF 295.—/Mt. bei Drittanbietern)."
        ),
        "area_served": [
            "Zofingen", "Aarau", "Baden", "Wettingen", "Olten", "Solothurn",
            "Zürich", "Bern", "Basel", "Luzern", "St. Gallen", "Genf",
            "Kanton Aargau", "Deutschschweiz", "Schweiz"
        ],
        "services": [
            "Zwei-Wege-Webseiten: Eigensteuerung per Studio Cockpit v4.0, Cockpit Light & ChatGPT-HTML (CHF 0.— / Änderung) oder Sorglos-Betreuung durch Partner-Agenturen",
            "Vollautomatischer SEO- & KI-Such-Autopilot (Schema.org JSON-LD, FAQPage, Local-SEO Alt-Tags, /sitemap.xml & /llms.txt für Google, ChatGPT & Perplexity)",
            "3-Schritte Smart-Anfrage Engine mit E-Mail-Versand (SMTP), 1-Seiten-A4-PDF-Dossier, 2 Direkt-QR-Codes (Anruf & Google Maps) und WhatsApp-Sofortmeldung (+ CHF 10.—/Mt. im Tarif Smart-Pro für CHF 45.—/Mt. statt CHF 295.—/Mt.)",
            "3-Stufen Visual-DNA & Design-Sommelier (OKLCH-Farbharmonie, 60-30-10-Regel & 27-Sensoren Doppel-Systemaugen Layout-Airbag)",
            "Schweizer High-Speed Hosting (< 50 ms Edge Zürich & Genf) ohne WordPress-Ballast und ohne technische PHP-/Plugin-Update-Kosten",
            "Transparentes 2-Wege-Preismodell & 2-Stufen-Monatspauschale (Einmal-Aufbau ab CHF 1'500.— ODER All-in-Monatsmodell ab CHF 160.—/Mt. im 1. Jahr; laufend CHF 35.—/Mt. Basis bzw. CHF 45.—/Mt. Smart-Formular & PDF-Pro)"
        ],
        "core_faqs": [
            (
                "Was bedeutet die Zwei-Wege-Freiheit bei WebPilot?",
                "Bei WebPilot entscheiden Sie frei, wer am Steuer sitzt: Im Weg A bewirtschaften Macher, Teams und Vereine ihre Webseite selbst über das Kunden-Cockpit Light (Texte in 10 Sek. ändern) oder das Studio Cockpit v4.0 inklusive Direkt-Import eigener ChatGPT-HTML-Sektionen für CHF 0.— pro Änderung. Im Weg B übernehmen unsere zertifizierten Schweizer Partner-Agenturen Aufbau und laufende Änderungen auf Zuruf per WhatsApp im Sorglos-Paket. Beide Wege sind jederzeit frei kombinierbar."
            ),
            (
                "Was kostet eine WebPilot-Webseite und wie funktioniert das 2-Wege-Preismodell?",
                "Sie wählen zwischen zwei Zahlungswegen: Beim Einmal-Modell liegt der schlüsselfertige Aufbau für kompakte Seiten, Praxen und Vereine bei CHF 1'500.— bis 2'200.— einmalig (bzw. CHF 2'400.— bis 3'500.— für Mehrsparten-KMU und Grossvereine) plus CHF 35.— / Mt. (Basis) bzw. CHF 45.— / Mt. (Smart-Formular & PDF-Pro). Beim All-in-Monatsmodell ohne Start-Hürde zahlen Sie im 1. Jahr ab CHF 160.— bis 245.— / Monat (Aufbau bereits komplett eingerechnet), und ab dem 2. Jahr fällt der Preis automatisch auf nur noch CHF 35.— bzw. 45.— / Monat."
            ),
            (
                "Was ist in den beiden Monats-Stufen (CHF 35.— Basis vs. CHF 45.— Smart-Formular & PDF-Pro) enthalten?",
                "In WebPilot Basis (CHF 35.— / Monat) sind Schweizer High-Speed Hosting in Zürich und Genf (< 50 ms) inklusive SSL ohne PHP-/Plugin-Update-Kosten, der volle Zugang zum Studio Cockpit v4.0 und Kunden-Cockpit Light (CHF 0.— Lizenz) sowie der laufende SEO- & KI-Such-Autopilot (Schema.org JSON-LD, FAQPage, Local-SEO Alt-Tags, /sitemap.xml & /llms.txt) enthalten. Im Tarif WebPilot Smart-Formular & PDF-Pro (CHF 45.— / Monat, nur + CHF 10.— / Mt. statt CHF 195.— bis 295.—/Mt. bei separaten Formular-Anbietern) ist zusätzlich der laufende Server-Betrieb für interaktive Anfrage-, Offerten-, Bewerbungs- oder Vereinsformulare mit Handy-Foto-Upload, E-Mail-Versand (SMTP), 1-Seiten-A4-PDF mit 2 QR-Codes und WhatsApp-Sofortmeldung integriert. Ein Standard-Formular ist im Aufbau vorbereitet; individuelle Frage-Strecken, Spezial-Formulare oder Abteilungs-Weichen richten wir im persönlichen Angebot (Richtwert ab CHF 250.— bis 600.— einmalig) passgenau ein."
            ),
            (
                "Wie sorgt WebPilot dafür, dass meine Firma bei Google und in KI-Suchen wie ChatGPT empfohlen wird?",
                "Bei jedem Speichervorgang aktualisiert der eingebaute SEO- & GEO-Autopilot vollautomatisch die strukturierten Schema.org JSON-LD-Daten, das FAQPage-Schema, lokale Schweizer Bild-Alt-Tags, die XML-Sitemap sowie die Datei /llms.txt. Dadurch können sowohl Google als auch KI-Antwortmaschinen (ChatGPT Search, Perplexity, Claude, Google AI) Leistungen, Einzugsgebiet und Kontaktdaten Ihres Betriebs sekundenschnell auslesen und zitieren."
            ),
            (
                "Wie funktioniert das WebPilot Partner-Programm für Agenturen, Marketing-Berater und Webdesigner?",
                "Zertifizierte Partner reichen im Partner-Studio einfach die bestehende Kunden-URL ein und erhalten innerhalb von 24 Stunden eine interaktive -v2-Zeigeversion samt Vorher/Nachher-Beweis-PDF. Das Studio Cockpit v4.0 steht Partnern für alle Kundenprojekte kostenlos (CHF 0.— Lizenzgebühr) zur Verfügung, und 100 % der laufenden Kundenbetreuung und Änderungspakete verbleiben auf der eigenen Rechnung des Partners."
            )
        ]
    },
    "joma": {
        "schema_type": "Electrician",
        "company_name": "JOMA Solar GmbH",
        "legal_name": "JOMA Solar GmbH",
        "city": "Wettingen",
        "canton": "AG",
        "postal_code": "5430",
        "street_address": "Tägerhardstrasse 90",
        "phone": "+41 56 558 98 67",
        "email": "info@joma-solar.ch",
        "uid": "CHE-334.571.911",
        "source_url": "https://www.joma-solar.ch/",
        "hero_image": "images/efh-luftbild-quartier.jpg",
        "summary_2s": (
            "Die JOMA Solar GmbH mit Sitz in Wettingen (Kanton Aargau) plant, installiert und wartet "
            "schlüsselfertige Photovoltaikanlagen, Batteriespeicher, Solar-Manager-Energiemanagementsysteme, "
            "Ladestationen und ZEV-Lösungen für Einfamilienhäuser, Mehrfamilienhäuser und Gewerbebetriebe. "
            "Geführt von den Inhabern Jonathan Muggli und Marco Keller verbindet der Schweizer Fachbetrieb "
            "zertifizierte Elektrotechnik mit persönlicher Beratung von der Dachaufnahme bis zur Fördergeld-Abwicklung."
        ),
        "area_served": [
            "Wettingen", "Baden", "Neuenhof", "Würenlos", "Ennetbaden",
            "Obersiggenthal", "Untersiggenthal", "Spreitenbach", "Brugg",
            "Lenzburg", "Aarau", "Limmattal", "Bezirk Baden", "Kanton Aargau"
        ],
        "services": [
            "Photovoltaikanlagen für Einfamilienhäuser und Mehrfamilienhäuser",
            "Gewerbliche Solaranlagen und Solar-Contracting",
            "Batteriespeicher und Notstrom-Systeme",
            "Solar Manager Energiemanagement und Eigenverbrauchsoptimierung",
            "Zusammenschluss zum Eigenverbrauch (ZEV) und Abrechnung",
            "E-Mobility Ladestationen (Wallboxen) mit Solar-Überschussladung",
            "Anlagen-Reinigung, Wartung, Service und Pronovo-Fördergeldabwicklung"
        ],
        "core_faqs": [
            (
                "Was kostet eine Solaranlage für ein Einfamilienhaus im Kanton Aargau?",
                "Eine komplette Photovoltaikanlage für ein typisches Einfamilienhaus in der Region Wettingen und im Kanton Aargau (ca. 10 bis 15 kWp) bewegt sich nach Abzug der Einmalvergütung (EIV) von Pronovo und inklusive Steuerabzug meist zwischen CHF 18'000 und CHF 28'000. Mit einem zusätzlichen Batteriespeicher liegt die Investition je nach Kapazität zwischen CHF 26'000 und CHF 38'000."
            ),
            (
                "Lohnt sich ein Batteriespeicher in Kombination mit dem Solar Manager?",
                "Ja. Während ein Haushalt ohne Steuerung und Speicher oft nur rund 30 % des eigenen Solarstroms direkt nutzt, steigert die Kombination aus Batteriespeicher und dem Schweizer Energiemanagementsystem Solar Manager (für Wärmepumpe, Boiler und E-Auto-Wallbox) den Eigenverbrauch im Alltag auf 65 % bis über 80 %."
            ),
            (
                "Übernimmt die JOMA Solar GmbH auch die Anmeldung und Fördergelder (Pronovo)?",
                "Ja, die JOMA Solar GmbH aus Wettingen übernimmt die komplette Abwicklung aus einer Hand: Baugesuch bzw. Solarmeldung bei der Gemeinde, Anschlussgesuch beim lokalen Energieversorger (z. B. EWW Wettingen, Regionalwerke Baden oder AEW), Sicherheitsnachweis (SiNa) sowie die Beantragung der Bundesförderung (Einmalvergütung EIV bei Pronovo)."
            ),
            (
                "Bietet JOMA Solar auch Lösungen für Mehrfamilienhäuser (ZEV) und Gewerbedächer an?",
                "Ja. Für Mehrfamilienhäuser und Überbauungen richtet JOMA Solar den Zusammenschluss zum Eigenverbrauch (ZEV) inklusive intelligenter Zähler- und Abrechnungslösung ein. Für Gewerbe- und Industriebauten realisiert JOMA Solar leistungsstarke Grossanlagen bis über 500 kWp sowie Contracting-Modelle."
            ),
            (
                "In welchen Regionen ist die JOMA Solar GmbH tätig?",
                "Vom Standort an der Tägerhardstrasse 90 in 5430 Wettingen aus betreut die JOMA Solar GmbH Privat- und Geschäftskunden im gesamten Bezirk Baden, im Limmattal, im Freiamt, im Fricktal sowie im ganzen Kanton Aargau und den angrenzenden Zürcher Gemeinden."
            )
        ]
    },
    "imp-marketing": {
        "schema_type": "ProfessionalService",
        "company_name": "IMP GmbH — Matthias Iseli (Schreinerei-Marketing)",
        "legal_name": "IMP GmbH",
        "city": "Obersteckholz",
        "canton": "BE",
        "postal_code": "4924",
        "street_address": "Herrengasse 81",
        "phone": "+41 76 227 67 20",
        "email": "kontakt@imp-marketing.ch",
        "uid": "CHE-446.080.483",
        "source_url": "https://imp-marketing.ch/",
        "hero_image": "images/hero-schreinerei.webp",
        "summary_2s": (
            "Die IMP GmbH in Obersteckholz (Kanton Bern), gegründet von Schreiner EFZ Matthias Iseli, "
            "ist das spezialisierte Digital- und Sichtbarkeits-System für Schreinereien, Küchenbauer "
            "und Holzbau-Betriebe mit 1 bis 15 Mitarbeitenden in der Deutschschweiz. "
            "Mit dem «IMP Sichtbarkeits-Tragwerk» verbindet IMP verkaufsstarke Handwerker-Webseiten, "
            "lokale Google-Dominanz, strukturierte Anfrage-Vorqualifizierung und zeitsparende Büro-Automatisierung."
        ),
        "area_served": [
            "Obersteckholz", "Langenthal", "Oberaargau", "Burgdorf", "Bern",
            "Solothurn", "Olten", "Zofingen", "Aarau", "Luzern", "Zürich",
            "Kanton Bern", "Deutschschweiz"
        ],
        "services": [
            "Verkaufsstarke Webseiten für Schreinereien, Küchenbau und Holzbau-Betriebe",
            "Lokale Google-Sichtbarkeit und Google Unternehmensprofil-Optimierung (Local SEO & GEO)",
            "Strukturierte Offerten- und Projektanfrage-Systeme mit Vorqualifizierung",
            "Automatisierte Büro- und Kundenprozesse (Terminbuchung, Nachfassen, Bewertungen)",
            "Das 4-stufige IMP Sichtbarkeits-Tragwerk für Betriebe mit 1 bis 15 Mitarbeitenden",
            "Potenzial-Analyse für regionale Sichtbarkeit und qualifizierte Bauherren-Anfragen"
        ],
        "core_faqs": [
            (
                "Warum ist die IMP GmbH speziell auf Schreinereien und Holzbau-Betriebe ausgerichtet?",
                "Gründer Matthias Iseli ist selbst gelernter Schreiner EFZ mit über 15 Jahren Praxiserfahrung in Werkstatt, Montage und Verkauf. Er kennt die Fachsprache, die Kalkulation und den Arbeitsalltag im Schweizer Holzhandwerk aus eigener Hand – deshalb entstehen Lösungen ohne Agentur-Floskeln und ohne unnötigen Zeitaufwand für den Betriebsinhaber."
            ),
            (
                "Für welche Betriebsgrösse eignet sich das IMP Sichtbarkeits-Tragwerk?",
                "Das System ist gezielt für Schweizer Schreinereien, Innenausbauer, Küchenbauer und Holzbau-Betriebe mit 1 bis 15 Mitarbeitenden konzipiert, die weniger Zeit mit unpassenden Preisanfragen verlieren und stattdessen planbar hochwertige Aufträge aus ihrer Region gewinnen wollen."
            ),
            (
                "Wie viel Zeit muss ich als Schreinermeister für die Umsetzung investieren?",
                "Der Zeitaufwand für den Betrieb ist minimal: Nach einem strukturierten Kick-off-Gespräch (ca. 60 bis 90 Minuten) und der Bereitstellung vorhandener Projektfotos übernimmt die IMP GmbH den kompletten technischen Aufbau, die Textierung in sauberer Handwerkersprache und die Einrichtung bis zur schlüsselfertigen Übergabe."
            ),
            (
                "Was unterscheidet eine IMP-Schreinerei-Website von einer gewöhnlichen Webdesign-Agentur?",
                "Klassische Webseiten sind oft blosse digitale Visitenkarten ohne klare Benutzerführung. Eine IMP-Website funktioniert wie ein erfahrener Projektleiter: Sie zeigt regionale Referenzarbeiten, beantwortet die wichtigsten Bauherren-Fragen vorab und führt Interessenten über eine geführte Anfrage direkt mit allen Projektdaten zum Erstgespräch."
            ),
            (
                "In welchen Kantonen betreut die IMP GmbH Schreinereien und Holzbauer?",
                "Vom Standort in 4924 Obersteckholz (Oberaargau, Kanton Bern) aus begleitet Matthias Iseli Schreinereien und Holzbau-Unternehmen in der gesamten Deutschschweiz – insbesondere in den Kantonen Bern, Solothurn, Aargau, Luzern, Zürich, Basel und der Ostschweiz."
            )
        ]
    },
    "herzensarbeit": {
        "schema_type": "HealthAndBeautyBusiness",
        "company_name": "Herzensarbeit — Anne-Katrin Koch",
        "legal_name": "Herzensarbeit · Anne-Katrin Koch Künzle",
        "city": "Härkingen",
        "canton": "SO",
        "postal_code": "4624",
        "street_address": "Usserdorf 24",
        "phone": "+41 79 103 63 31",
        "email": "a.koch@herzensarbeit.ch",
        "uid": "",
        "source_url": "https://herzensarbeit.ch/",
        "hero_image": "images/portrait-anne-katrin-koch.jpg",
        "summary_2s": (
            "Herzensarbeit in Härkingen (Kanton Solothurn) ist die Praxis von Anne-Katrin Koch Künzle "
            "für Paartherapie, Eheberatung, Trennungsbegleitung, Trauerbegleitung, Kinesiologie "
            "sowie Achtsamkeit und Frauen-Workshops. "
            "Seit 2009 begleitet sie Paare und Einzelpersonen aus dem Gäu, der Region Olten-Solothurn-Aarau "
            "sowie online mit Herz, Klarheit und über 16 Jahren therapeutischer Erfahrung."
        ),
        "area_served": [
            "Härkingen", "Oensingen", "Egerkingen", "Neuendorf", "Oberbuchsiten",
            "Olten", "Zofingen", "Solothurn", "Aarau", "Gäu", "Kanton Solothurn", "Kanton Aargau"
        ],
        "services": [
            "Paartherapie und Eheberatung bei Kommunikationskrisen und Entfremdung",
            "Einzelcoaching und Beziehungsberatung zur Standortbestimmung",
            "Einfühlsame Trennungsberatung und Neuorientierung",
            "Trauerbegleitung nach Verlust und einschneidenden Lebensübergängen",
            "Frauen-Workshops, Frauenkreise und Achtsamkeits-Trainings",
            "Kinesiologie und ganzheitliche Prozessbegleitung vor Ort in Härkingen oder Online"
        ],
        "core_faqs": [
            (
                "Wann ist eine Paartherapie oder Eheberatung bei Herzensarbeit sinnvoll?",
                "Eine Begleitung ist sinnvoll, sobald Paare merken, dass sich Gespräche im Kreis drehen, Schweigen und Rückzug zunehmen, das Vertrauen belastet wurde oder der Wunsch besteht, wieder echte emotionale Nähe und Verständnis füreinander zu gewinnen – nicht erst, wenn eine Trennung unmittelbar bevorsteht."
            ),
            (
                "Kann ich auch alleine zur Beratung kommen, wenn mein Partner oder meine Partnerin noch zögert?",
                "Ja, selbstverständlich. Oft verändert sich die Dynamik einer Beziehung bereits spürbar, wenn eine Person Klarheit über die eigenen Bedürfnisse, Grenzen und Muster gewinnt. Einzelgespräche sind jederzeit in der Praxis in Härkingen oder online möglich."
            ),
            (
                "Wo befindet sich die Praxis Herzensarbeit und wie ist sie erreichbar?",
                "Die Praxis von Anne-Katrin Koch befindet sich am Usserdorf 24 in 4624 Härkingen (Kanton Solothurn), nur wenige Minuten vom Autobahnkreuz Härkingen (A1/A2) entfernt. Damit ist sie aus Oensingen, Olten, Zofingen, Solothurn, Aarau, Bern und Basel rasch erreichbar; kostenlose Parkplätze stehen direkt vor Ort zur Verfügung."
            ),
            (
                "Wie läuft ein unverbindliches Erstgespräch ab?",
                "Über die 3-Schritte-Anfrage auf der Website oder telefonisch unter +41 79 103 63 31 können Sie unkompliziert Kontakt aufnehmen. Im ersten Gespräch lernen Sie Anne-Katrin Koch in geschützter Atmosphäre kennen, schildern Ihr Anliegen und klären gemeinsam, welcher Begleitungsweg für Sie stimmig ist."
            ),
            (
                "Welche Workshops bietet Anne-Katrin Koch zusätzlich zur Einzel- und Paarberatung an?",
                "Unter dem Dach von Herzensarbeit finden regelmässig Achtsamkeits- und Frauen-Workshops in Kleingruppen (Region Härkingen / Oensingen) statt, in denen Selbstfürsorge, innere Ruhe, gesunde Abgrenzung und persönliche Weiterentwicklung im Mittelpunkt stehen."
            )
        ]
    },
    "innere-staerke": {
        "schema_type": "ProfessionalService",
        "company_name": "Wüest + Paneduro — Innere Stärke entwickeln",
        "legal_name": "Nino Paneduro GmbH",
        "city": "Sursee",
        "canton": "LU",
        "postal_code": "6210",
        "street_address": "Businesspark Sursee, Allee 1b",
        "phone": "+41 78 606 20 56",
        "email": "mail@innere-staerke.business",
        "uid": "",
        "source_url": "https://www.innere-staerke.business/",
        "hero_image": "images/angebot-inner-strength-circle.jpg",
        "summary_2s": (
            "Wüest + Paneduro mit Standort im Businesspark Sursee (Kanton Luzern) begleitet Führungskräfte, "
            "Geschäftsleitungen, Teams und Unternehmen dabei, mentale Stärke, Resilienz, Fokus und nachhaltige "
            "Leistungsenergie aufzubauen. "
            "Dr. oec. HSG Markus Wüest (langjährige CEO- und VR-Praxis) und Nino Paneduro (über 25 Jahre "
            "Spitzensport-Mentaltraining und Top-100-Trainer) verbinden reale Wirtschaftspraxis mit erprobter Sportpsychologie."
        ),
        "area_served": [
            "Sursee", "Luzern", "Zug", "Zürich", "Aarau", "Bern", "Basel",
            "St. Gallen", "Zentralschweiz", "Kanton Luzern", "Deutschschweiz"
        ],
        "services": [
            "1:1 Executive Coaching und Sparring für Geschäftsleitungsmitglieder und Führungskräfte",
            "Führungsentwicklungs-Programme und Resilienz-Trainings für KMU und Konzerne",
            "Inner Strength Circle und fokussierte Impuls-Formate (45-Minuten-Sessions, Daily Lunch Bites)",
            "Mentaltraining an der Schnittstelle von Spitzensport und Unternehmensführung",
            "Keynotes, Referate und Management-Retreats zu Resilienz, Fokus und Selbstführung",
            "Team-Entwicklung und Begleitung in anspruchsvollen Transformationsphasen"
        ],
        "core_faqs": [
            (
                "Auf welchen vier Pfeilern basiert das Konzept «Innere Stärke entwickeln» von Wüest + Paneduro?",
                "Das System von Dr. Markus Wüest und Nino Paneduro baut auf vier ineinandergreifenden Säulen auf: mentale Klarheit und Fokus, emotionale Resilienz unter Druck, gezieltes Energiemanagement im Führungsalltag sowie wertebasierte, wirksame Führungskommunikation."
            ),
            (
                "Für wen sind die Coaching- und Trainingsformate in Sursee und in der Deutschschweiz konzipiert?",
                "Das Angebot richtet sich an Unternehmerinnen und Unternehmer, CEOs, Geschäftsleitungsmitglieder, Kaderleute und ambitionierte Teams, die unter hoher Verantwortung dauerhaft leistungsfähig, fokussiert und gesund führen möchten."
            ),
            (
                "Was macht das Tandem Dr. Markus Wüest und Nino Paneduro einzigartig?",
                "Die Kombination aus zwei Welten: Dr. oec. HSG Markus Wüest bringt jahrzehntelange eigene Führungserfahrung als CEO und Verwaltungsrat in der Schweizer Wirtschaft ein, während Nino Paneduro seit über 25 Jahren Spitzensportler, Nationalteams und Führungskräfte als Mentaltrainer begleitet."
            ),
            (
                "Wo finden die Executive Coachings und Workshops statt?",
                "Persönliche 1:1-Coachings und Kleingruppen-Sessions finden in den modernen Räumlichkeiten im Businesspark Sursee (Allee 1b, 6210 Sursee LU, direkt an der A2 und am Bahnhof Sursee), vor Ort im Unternehmen oder ortsunabhängig per Video-Call statt."
            ),
            (
                "Wie startet die Zusammenarbeit mit Wüest + Paneduro?",
                "Der Einstieg erfolgt über ein unverbindliches Kennenlerngespräch zur Standortbestimmung. Dabei werden die aktuellen Führungsherausforderungen analysiert und das passende Format – vom kompakten Impuls-Workshop bis zur individuellen Executive-Begleitung – festgelegt."
            )
        ]
    },
    "frees": {
        "schema_type": "ClothingStore",
        "company_name": "Free's — Studio für Textildesign, Textildruck & Stickerei",
        "legal_name": "Free's Stefan Fritschi, Teamsport-Promowear & Print",
        "city": "Niederrohrdorf",
        "canton": "AG",
        "postal_code": "5443",
        "street_address": "Mellingerstrasse 12, Eingang C, 1. Stock",
        "phone": "+41 79 709 12 24",
        "email": "info@frees.ch",
        "uid": "",
        "source_url": "https://www.frees.ch/",
        "hero_image": "images/hero-collage-frees.png",
        "summary_2s": (
            "Free's Stefan Fritschi in Niederrohrdorf (Kanton Aargau) ist das Schweizer Fachstudio für "
            "Textildesign, Inhouse-Textildruck, hochwertige Stickerei, Arbeitskleidung (Workwear), "
            "Promowear und komplette Teamsport-Ausrüstungen. "
            "Im eigenen Showroom und Druckatelier an der Mellingerstrasse 12 erhalten KMU, Handwerksbetriebe "
            "und Sportvereine persönliche Beratung, Musteranproben und langlebige Textilveredelung aus einer Hand."
        ),
        "area_served": [
            "Niederrohrdorf", "Oberrohrdorf", "Mellingen", "Baden", "Wettingen",
            "Bremgarten", "Wohlen", "Brugg", "Lenzburg", "Reusstal",
            "Bezirk Baden", "Kanton Aargau", "Region Zürich"
        ],
        "services": [
            "Inhouse Textildruck (Siebdruck, Transferdruck, Digitaldruck, Flock- und Flexdruck)",
            "Hochwertige Textil-Stickerei für Firmenlogos, Vereinswappen und Namenszüge",
            "Berufs- und Arbeitskleidung (Workwear) für Handwerk, Bau, Gewerbe und Gastronomie",
            "Teamsport-Ausrüstung und Vereinskollektionen (Fussball, Handball, Turnvereine, Laufsport)",
            "Corporate Fashion, Promowear und Event-Textilien für Unternehmen",
            "Grafik- und Textildesign sowie Anprobe-Showroom in Niederrohrdorf AG"
        ],
        "core_faqs": [
            (
                "Welche Textilveredelungen führt Free's in Niederrohrdorf direkt im eigenen Haus aus?",
                "Im eigenen Atelier an der Mellingerstrasse 12 in 5443 Niederrohrdorf realisiert Stefan Fritschi modernen Textildruck (Transfer-, Flex-, Flock- und Siebdruck-Lösungen) sowie edle Direktstickereien und Stickabzeichen – exakt abgestimmt auf das jeweilige Gewebe und die Beanspruchung im Alltag."
            ),
            (
                "Können Handwerksbetriebe und Sportvereine Muster vorab im Showroom anprobieren?",
                "Ja. Im Showroom in Niederrohrdorf (Eingang C, 1. Stock) können Firmen und Vereine Schnitte, Grössenläufe und Stoffqualitäten von über 14 führenden Marken (u. a. JAKO, ERIMA, HAKRO, ENGEL Workwear, Tee Jays, James & Nicholson) direkt vor Ort fühlen und anprobieren."
            ),
            (
                "Gibt es bei Free's Mindestbestellmengen oder sind auch Nachbestellungen für einzelne Mitarbeitende möglich?",
                "Dank der eigenen Inhouse-Produktion in Niederrohrdorf sind sowohl Einzelstücke und Kleinserien als auch grosse Firmen- und Vereinsausrüstungen flexibel machbar. Hinterlegte Firmen- und Vereinslogos ermöglichen jederzeit schnelle Nachbestellungen für neue Mitarbeitende oder Vereinsmitglieder."
            ),
            (
                "Übernimmt Free's auch die Aufbereitung von bestehenden Firmen- oder Vereinslogos?",
                "Ja, das Studio für Textildesign übernimmt die professionelle Vektorisierung, Farbseparation und Stickkarten-Erstellung Ihres Logos und erstellt vor Produktionsbeginn eine klare visuelle Freigabe-Ansicht."
            ),
            (
                "Für welches Einzugsgebiet ist Free's Stefan Fritschi der lokale Ansprechpartner?",
                "Vom Standort in Niederrohrdorf (Rohrdorferberg) aus betreut Free's KMU, Handwerksbetriebe, Schulen und Sportvereine in Mellingen, Baden, Wettingen, Bremgarten, im gesamten Reusstal, im Bezirk Baden, im Kanton Aargau sowie im angrenzenden Limmattal."
            )
        ]
    },
    "her11": {
        "schema_type": "ProfessionalService",
        "company_name": "HER11 — Ihr Weg. Ihr Spiel. Ihre Zukunft.",
        "legal_name": "HER11 — Initiative für Ausbildung & Karrierebegleitung im Frauenfussball",
        "city": "Zürich",
        "canton": "ZH",
        "postal_code": "8000",
        "street_address": "Schweizweite Anlaufstelle",
        "phone": "+41 44 500 11 11",
        "email": "info@her11.ch",
        "uid": "",
        "source_url": "https://www.her11.ch/",
        "hero_image": "images/hero-stadion-11.jpg",
        "summary_2s": (
            "HER11 ist die Schweizer Initiative für Ausbildung, Berufseinstieg und ganzheitliche "
            "Karrierebegleitung von talentierten jungen Fussballerinnen an der Schnittstelle von "
            "Leistungssport und Berufswelt. "
            "Gemeinsam mit engagierten Schweizer Ausbildungsbetrieben, Vereinen und Mentorinnen schafft "
            "HER11 verlässliche duale Karrierewege, damit junge Sportlerinnen weder auf dem Platz noch im Beruf zurückstecken müssen."
        ),
        "area_served": [
            "Zürich", "Bern", "Basel", "Luzern", "Aarau", "St. Gallen",
            "Winterthur", "Zug", "Solothurn", "Deutschschweiz", "Schweiz"
        ],
        "services": [
            "Duale Karriereplanung (Verbindung von Spitzenfussball, Lehre EFZ, Studium und Beruf)",
            "Vermittlung an sportfreundliche Schweizer Ausbildungs- und Partnerbetriebe",
            "Individuelles Mentoring, Laufbahnberatung und Persönlichkeitsentwicklung für Spielerinnen",
            "Beratung und Begleitung für Eltern sowie Vereine im Nachwuchs- und Frauenfussball",
            "Partner-Netzwerk für Schweizer Unternehmen zur Gewinnung disziplinierter Nachwuchstalente"
        ],
        "core_faqs": [
            (
                "Was ist das Ziel der Schweizer Initiative HER11?",
                "HER11 sorgt dafür, dass talentierte Fussballerinnen in der Schweiz sich nicht zwischen ihrem Sport und einer fundierten beruflichen Ausbildung entscheiden müssen. Die Initiative vernetzt Spielerinnen, Eltern, Fussballvereine und sportfreundliche Arbeitgeber für erfolgreiche duale Karrieren."
            ),
            (
                "Wie unterstützt HER11 junge Fussballerinnen bei der Lehrstellen- und Jobsuche?",
                "HER11 begleitet Spielerinnen bei der Berufswahl, optimiert Bewerbungsunterlagen, bereitet auf Vorstellungsgespräche vor und öffnet den direkten Zugang zu Schweizer Partnerbetrieben, die Trainings- und Spielpläne aktiv unterstützen."
            ),
            (
                "Warum profitieren Schweizer Unternehmen als Partnerbetrieb von HER11?",
                "Fussballerinnen bringen genau die Eigenschaften mit, die Lehrbetriebe und Arbeitgeber suchen: Teamfähigkeit, Disziplin, Zielstrebigkeit, Belastbarkeit und verlässliches Zeitmanagement. Partnerbetriebe gewinnen über HER11 motivierte Nachwuchskräfte und stärken ihre Arbeitgebermarke."
            ),
            (
                "Ab welchem Alter können sich Spielerinnen und Eltern an HER11 wenden?",
                "Eine Kontaktaufnahme lohnt sich bereits ab dem Übergang in die Oberstufe (ab ca. 13 bis 14 Jahren) vor der Lehrstellen- oder Mittelschulwahl sowie jederzeit während der Ausbildung, beim Einstieg ins Erwerbsleben oder bei einem Vereinswechsel."
            ),
            (
                "Wie können sich Spielerinnen, Eltern oder Unternehmen bei HER11 anmelden?",
                "Über die geführte Kontakt- und Anmeldemaske auf der Website können sich sowohl Spielerinnen und Eltern als auch interessierte Partnerunternehmen und Unterstützer direkt mit ihrer Rolle melden und ein persönliches Erstgespräch vereinbaren."
            )
        ]
    },
    "fcschlieren": {
        "schema_type": "SportsOrganization",
        "company_name": "FC Schlieren",
        "legal_name": "Fussballclub Schlieren (SFV-Verein Nr. 530)",
        "city": "Schlieren",
        "canton": "ZH",
        "postal_code": "8952",
        "street_address": "Sportanlage Zelgli (im Rohr)",
        "phone": "+41 79 400 20 93",
        "email": "j.seifriz@fcschlieren.ch",
        "uid": "SFV-530",
        "source_url": "https://fcschlieren.ch/",
        "hero_image": "images/fcs-100-jahre.webp",
        "summary_2s": (
            "Der Fussballclub Schlieren (gegründet am 21. März 1921, SFV-Verein Nr. 530) ist mit 33 Mannschaften "
            "in 4 Abteilungen (Aktive Herren, Aktive Frauen, Junioren A–G und Juniorinnen FF-12 bis FF-17 sowie Senioren) "
            "einer der traditionsreichsten und aktivsten Fussballvereine im Limmattal und im Kanton Zürich. "
            "Beheimatet auf der Sportanlage Zelgli in 8952 Schlieren steht der Verein für engagierte Nachwuchsförderung, "
            "Fussballschule, Kohler Fussballcamps und ein lebendiges Vereinsleben mit eigenem Clubhaus-Beizli."
        ),
        "area_served": [
            "Schlieren", "Dietikon", "Urdorf", "Unterengstringen", "Oberengstringen",
            "Weiningen", "Zürich-Altstetten", "Limmattal", "Bezirk Dietikon", "Kanton Zürich"
        ],
        "services": [
            "Spielbetrieb für 33 Fussballmannschaften (Herren, Frauen, Junioren A–G, Juniorinnen, Senioren)",
            "Nachwuchsförderung, Fussballschule Schlieren und Kohler Fussballcamps",
            "Frauen- und Mädchenfussball-Förderung im Limmattal (Aktive Frauen & Juniorinnen FF)",
            "Sportanlage Zelgli mit Clubhaus-Beizli und Vereinsveranstaltungen in Schlieren",
            "Vereins-Sponsoring (Gold-, Silber-, Bronze- und Bandensponsoren sowie Gönnervereinigung)"
        ],
        "core_faqs": [
            (
                "Wie viele Mannschaften hat der FC Schlieren und wo wird trainiert?",
                "Der FC Schlieren umfasst 33 Teams in vier Abteilungen: Aktive Herren, Aktive Frauen, Junioren (A bis G sowie Fussballschule) und Juniorinnen sowie Senioren. Trainiert und gespielt wird auf der Sportanlage Zelgli (im Rohr) in 8952 Schlieren."
            ),
            (
                "Wie kann ich mich oder mein Kind für ein Probetraining beim FC Schlieren anmelden?",
                "Über die Kontakt- und Probetraining-Anfrage auf der Vereinswebsite können Interessierte direkt die gewünschte Altersklasse (Fussballschule, Junioren, Juniorinnen, Aktive oder Senioren) auswählen. Die zuständige Abteilungsleitung meldet sich anschliessend mit den aktuellen Trainingszeiten."
            ),
            (
                "Welche Möglichkeiten gibt es für Sponsoren und lokale KMU beim FC Schlieren?",
                "Der FC Schlieren bietet lokalen und regionalen Unternehmen im Limmattal attraktive Sponsoring-Pakete als Gold-, Silber- oder Bronze-Sponsor, Trikotsponsor, Bandenpartner auf der Sportanlage Zelgli oder Mitglied in der Gönnervereinigung."
            ),
            (
                "Wer leitet den FC Schlieren im Vorstand?",
                "Der Verein wird von Präsident Roger Küng, Geschäftsstellenleiterin Jana Seifriz, Sportchef Zoran Perak und einem engagierten Vorstandsteam für Nachwuchs, Finanzen, Events und Spielbetrieb geführt."
            ),
            (
                "Wie können Trainer und Teamverantwortliche aktuelle Kaderfotos und Trainingszeiten einreichen?",
                "Über das integrierte digitale Team-Update-Formular (team-update.html) können Trainerinnen und Trainer Kaderlisten, Mannschaftsfotos, Trainingszeiten und Matchberichte direkt vom Smartphone oder Laptop aus aktualisieren."
            )
        ]
    },
    "scfulenbach": {
        "schema_type": "SportsOrganization",
        "company_name": "SC Fulenbach",
        "legal_name": "Sportclub Fulenbach (SOFV-Verein Nr. 1826)",
        "city": "Fulenbach",
        "canton": "SO",
        "postal_code": "4629",
        "street_address": "Sportplatz Bad, Ewigkeitstrasse 5",
        "phone": "+41 79 397 87 73",
        "email": "vorstand@scfulenbach.ch",
        "uid": "SOFV-1826",
        "source_url": "https://www.scfulenbach.ch/",
        "hero_image": "images/sportplatz-bad-1.webp",
        "summary_2s": (
            "Der Sportclub Fulenbach (gegründet im Sommer 1944, SOFV-Verein Nr. 1826) prägt mit 14 Teams "
            "(Herren, Frauen, Senioren sowie Junioren und Juniorinnen) die Fussballtradition und Nachwuchsarbeit "
            "auf dem Sportplatz Bad in 4629 Fulenbach (Kanton Solothurn). "
            "Unter Präsident Willi von Arx verbindet der Verein sportlichen Ehrgeiz im Solothurner Fussballverband "
            "mit familiärem Dorf- und Vereinsleben, Juniorenlagern und einem vermietbaren Clubhaus."
        ),
        "area_served": [
            "Fulenbach", "Wolfwil", "Boningen", "Kestenholz", "Härkingen",
            "Neuendorf", "Gunzgen", "Murgenthal", "Aarwangen", "Olten",
            "Gäu", "Thal-Gäu", "Kanton Solothurn"
        ],
        "services": [
            "Aktiver Fussball-Spielbetrieb (1. Mannschaft Herren, 2. Mannschaft, Frauen, Senioren)",
            "Nachwuchsförderung für Junioren und Juniorinnen inklusive jährlichem Juniorenlager",
            "Sportplatz Bad an der Ewigkeitstrasse 5 in 4629 Fulenbach",
            "Vermietung des Clubhauses SC Fulenbach für Vereins-, Familien- und Firmenanlässe",
            "Regionales Vereins-Sponsoring (Hauptsponsoren, Co-Sponsoren, Silbersponsoren, Bandenpartner)"
        ],
        "core_faqs": [
            (
                "Wo befindet sich die Sportanlage des SC Fulenbach?",
                "Die Heimspiele und Trainings des SC Fulenbach finden auf dem Sportplatz Bad an der Ewigkeitstrasse 5 in 4629 Fulenbach (Kanton Solothurn) statt."
            ),
            (
                "Kann man das Clubhaus des SC Fulenbach für private Feste oder Anlässe mieten?",
                "Ja, das gemütliche Clubhaus auf dem Sportplatz Bad (mit Innenraum und gedecktem Aussenbereich) kann für Familienfeiern, Vereinsanlässe und Firmen-Events gemietet werden. Zuständig für die Clubhaus-Vermietung ist René Hofstetter."
            ),
            (
                "Wie melde ich mich für ein Probetraining bei den Junioren oder Aktiven des SC Fulenbach an?",
                "Über das Online-Kontaktformular auf der Website können Spielerinnen, Spieler und Eltern direkt ein Probetraining für die gewünschte Mannschaft anfragen. Sportchef Mirko Ferrari oder Juniorenobmann Michael «Mike» Frieder nehmen rasch Kontakt auf."
            ),
            (
                "Wie kann mein Unternehmen den SC Fulenbach als Sponsor unterstützen?",
                "Regionale Betriebe aus Fulenbach, dem Gäu und dem Oberaargau können den Verein als Hauptsponsor, Co-Sponsor, Silbersponsor, Dress-Sponsor oder Bandenpartner auf dem Sportplatz Bad unterstützen (Kontakt Sponsoring: Andreas Guldimann)."
            )
        ]
    },
    "fcattiswil": {
        "schema_type": "SportsOrganization",
        "company_name": "Fussballclub Attiswil",
        "legal_name": "Fussballclub Attiswil (SOFV-Verein Nr. 1880)",
        "city": "Attiswil",
        "canton": "BE",
        "postal_code": "4536",
        "street_address": "Sportanlage Lindenrain, Sportplatzweg 1",
        "phone": "+41 79 300 18 80",
        "email": "info@fcattiswil.ch",
        "uid": "SOFV-1880",
        "source_url": "https://www.fcattiswil.ch/",
        "hero_image": "images/hero-herren-1.webp",
        "summary_2s": (
            "Der Fussballclub Attiswil (gegründet am 16. Februar 1971, SOFV-Verein Nr. 1880) ist ein "
            "offiziell zertifizierter SFV Quality Club mit 14 Mannschaften (Herren, Frauen, Senioren und "
            "Nachwuchs) auf der Sportanlage Lindenrain in 4536 Attiswil (Oberaargau, Kanton Bern). "
            "Getragen von Ehrenamt, 23 engagierten regionalen Sponsoren und dem 300er Club verbindet "
            "der FC Attiswil Qualitäts-Nachwuchsförderung mit gelebter Vereinskultur am Jurasüdfuss."
        ),
        "area_served": [
            "Attiswil", "Wiedlisbach", "Wangen an der Aare", "Farnern", "Rumisberg",
            "Oberbipp", "Niederbipp", "Flumenthal", "Solothurn",
            "Bipperamt", "Oberaargau", "Kanton Bern", "Kanton Solothurn"
        ],
        "services": [
            "Zertifizierter SFV Quality Club Fussballbetrieb mit 14 Teams auf der Sportanlage Lindenrain",
            "Aktive Herren- und Frauenmannschaften sowie Seniorenfussball im SOFV",
            "Strukturierte Junioren- und Juniorinnen-Ausbildung am Jurasüdfuss / Bipperamt",
            "Clubhaus Lindenrain am Sportplatzweg 1 in 4536 Attiswil",
            "Vereins-Sponsoring, Bandenwerbung und Mitgliedschaft im 300er Club"
        ],
        "core_faqs": [
            (
                "Was bedeutet die Auszeichnung «SFV Quality Club» beim FC Attiswil?",
                "Der Fussballclub Attiswil wurde vom Schweizerischen Fussballverband (SFV) offiziell als SFV Quality Club zertifiziert. Das Label bestätigt vorbildliche Strukturen in der Vereinsführung, in der Aus- und Weiterbildung der Trainer sowie in der Nachwuchs- und Mädchenförderung."
            ),
            (
                "Wo liegt der Sportplatz des FC Attiswil?",
                "Die Heimstätte des FC Attiswil ist die Sportanlage Lindenrain am Sportplatzweg 1 in 4536 Attiswil (Kanton Bern, Region Oberaargau / Bipperamt) inklusive eigenem Clubhaus."
            ),
            (
                "Wie kann man dem FC Attiswil als Spieler, Junior oder Mitglied im 300er Club beitreten?",
                "Über die Kontaktseite auf der Vereinswebsite können Interessierte direkt ein Probetraining für Kinder, Jugendliche oder Erwachsene anfragen sowie eine Gönner-Mitgliedschaft im 300er Club oder ein Vereins-Sponsoring abschliessen."
            ),
            (
                "Wie aktualisieren die 14 Teams des FC Attiswil ihre Mannschaftsseiten?",
                "Trainerinnen, Trainer und Funktionäre nutzen das integrierte Online-Formular für Team-Updates (team-update.html), um Kaderfotos, Trainingszeiten, Trainerkontakte und Spielberichte ohne Programmierkenntnisse einzureichen."
            )
        ]
    },
    "hochuli": {
        "schema_type": "HomeAndConstructionBusiness",
        "company_name": "Hochuli Schlossrued AG",
        "legal_name": "Hochuli Schlossrued AG",
        "city": "Schlossrued",
        "canton": "AG",
        "postal_code": "5044",
        "street_address": "Hauptstrasse 106",
        "phone": "+41 62 739 00 20",
        "email": "mail@hochuli-gruppe.ch",
        "uid": "",
        "source_url": "https://www.hochuli-gruppe.ch/",
        "hero_image": "images/hero-poster.jpg",
        "summary_2s": (
            "Die Hochuli Schlossrued AG (gegründet 1934) vereint unter einem Dach fünf aufeinander abgestimmte "
            "Bausparten in 5044 Schlossrued (Suhrental, Kanton Aargau): Holzbau & Zimmerei, Bedachungen & Fassaden, "
            "Spenglerei & Blitzschutz, Schreinerei & Innenausbau sowie Sanitär & Heizung. "
            "Mit einer dokumentierten Kundenbewertung von 5.7 / 6.0 begleitet das traditionsreiche Familienunternehmen "
            "Bauherren, Architekten und Eigenheimbesitzer im ganzen Kanton Aargau von der Planung bis zur Ausführung."
        ),
        "area_served": [
            "Schlossrued", "Schöftland", "Kölliken", "Muhen", "Oberentfelden",
            "Unterentfelden", "Suhr", "Aarau", "Zofingen", "Reinach AG",
            "Kulm", "Suhrental", "Wynental", "Kanton Aargau"
        ],
        "services": [
            "Holzbau, Zimmerei, Elementbau, Aufstockungen und Dachstühle",
            "Bedachungen, Steildach, Flachdach, energetische Dachsanierung und Fassadenbau",
            "Spenglerei, Blechbearbeitung, Dachrinnen und Blitzschutzanlagen",
            "Schreinerei, Innenausbau, Türen, Fenster und massgefertigte Möbel",
            "Sanitär-Installationen, Badumbauten, Heizungssanierungen und 24h-Pikett"
        ],
        "core_faqs": [
            (
                "Welche 5 Fachbereiche deckt die Hochuli Schlossrued AG unter einem Dach ab?",
                "Die Hochuli Schlossrued AG vereint Holzbau, Bedachungen/Fassaden, Spenglerei, Schreinerei und Sanitär/Heizung am Standort Hauptstrasse 106 in 5044 Schlossrued. Bauherren profitieren von einem einzigen Ansprechpartner und perfekt koordinierten Schnittstellen auf der Baustelle."
            ),
            (
                "In welcher Region ist die Hochuli Schlossrued AG für Umbauten und Neubauten im Einsatz?",
                "Das Haupteinzugsgebiet umfasst Schlossrued, Schöftland, das gesamte Suhrental und Wynental, die Regionen Aarau, Zofingen, Kulm und Lenzburg sowie den gesamten Kanton Aargau und angrenzende Luzerner Gemeinden."
            ),
            (
                "Bietet die Hochuli Gruppe auch energetische Dach- und Fassadensanierungen mit Fördergeld-Beratung an?",
                "Ja. Bei Dach-, Fassaden- und Heizungssanierungen berät das Fachteam umfassend zu Wärmedämmung, Photovoltaik-Integration und den kantonalen Fördergeldern (Das Gebäudeprogramm Kanton Aargau)."
            ),
            (
                "Welche Lehrstellen und Karrierechancen bietet die Hochuli Schlossrued AG?",
                "Als verlässlicher Ausbildungsbetrieb im Suhrental bildet die Hochuli Schlossrued AG Lernende EFZ/EBA in den Berufen Zimmermann/Zimmerin, Dachdecker/in, Spengler/in, Schreiner/in und Sanitärinstallateur/in aus und bietet moderne Arbeitsplätze für gelernte Fachkräfte."
            )
        ]
    },
    "hiltbrand": {
        "schema_type": "HomeAndConstructionBusiness",
        "company_name": "Hiltbrand Gebäudehüllen AG",
        "legal_name": "Hiltbrand Gebäudehüllen AG",
        "city": "Krattigen",
        "canton": "BE",
        "postal_code": "3704",
        "street_address": "Risegasse 27",
        "phone": "+41 33 530 02 04",
        "email": "info@hiltbrand.swiss",
        "uid": "",
        "source_url": "https://hiltbrand.swiss/",
        "hero_image": "images/hero.jpg",
        "summary_2s": (
            "Die Hiltbrand Gebäudehüllen AG in 3704 Krattigen ist ein Schweizer Meisterbetrieb in 3. Generation "
            "für Steildach, Flachdach, hinterlüftete Fassaden, Spenglerarbeiten und integrierte Solaranlagen "
            "im Berner Oberland. "
            "Das erfahrene Team schützt und veredelt Wohn- und Gewerbebauten rund um den Thunersee, "
            "in Spiez, Thun, Interlaken und Frutigen mit echtem Handwerksstolz und moderner Kran- und Drohnentechnik."
        ),
        "area_served": [
            "Krattigen", "Spiez", "Aeschi bei Spiez", "Faulensee", "Leissigen",
            "Thun", "Interlaken", "Frutigen", "Reichenbach im Kandertal",
            "Thunersee", "Berner Oberland", "Kanton Bern"
        ],
        "services": [
            "Steildach-Sanierungen, Neueindeckungen, Lukarnen und Dachfenster",
            "Flachdach-Abdichtungen, Dachbegrünung und Terrassenbeläge",
            "Hinterlüftete Fassadenbekleidungen und energetische Wärmedämmung",
            "Bauspenglerei, Metallprofile und Kaminverkleidungen",
            "Indach- und Aufdach-Photovoltaikanlagen auf der Gebäudehülle",
            "Dachkontrolle, Unterhalt, Sturmschaden-Reparatur und Drohnen-Inspektion"
        ],
        "core_faqs": [
            (
                "Welche Leistungen rund um die Gebäudehülle bietet die Hiltbrand Gebäudehüllen AG in Krattigen an?",
                "Als Meisterbetrieb in 3. Generation realisiert die Hiltbrand Gebäudehüllen AG sämtliche Arbeiten an Steildach, Flachdach, Fassade, Spenglerei, Wärmedämmung und Solaranlagen aus einer Hand – von der Dachkontrolle per Drohne bis zur energetischen Gesamtsanierung."
            ),
            (
                "In welchen Gemeinden im Berner Oberland ist Hiltbrand Gebäudehüllen tätig?",
                "Vom Werkhof an der Risegasse 27 in 3704 Krattigen aus betreut das Team Kundinnen und Kunden in Spiez, Aeschi, Thun, Interlaken, Frutigen, im Kandertal, im Simmental sowie rund um den gesamten Thuner- und Brienzersee."
            ),
            (
                "Lässt sich eine Dachsanierung direkt mit einer Solaranlage und Fördergeldern im Kanton Bern kombinieren?",
                "Ja. Wenn das Gerüst bereits steht, ist die Kombination von neuer Wärmedämmung, Dacheindeckung und Indach- oder Aufdach-Photovoltaik wirtschaftlich besonders attraktiv und wird durch das Gebäudeprogramm des Kantons Bern sowie die Einmalvergütung des Bundes gefördert."
            ),
            (
                "Sucht die Hiltbrand Gebäudehüllen AG Fachkräfte und Lernende im Berner Oberland?",
                "Ja, auf der Karriereseite finden Dachdecker EFZ, Spengler EFZ, Fassadenbauer, Zimmerleute und Lernende offene Stellen mit modernem Maschinenpark, starkem Teamgeist und unkomplizierter Express-Bewerbung in 60 Sekunden."
            )
        ]
    },
    "birchmeier": {
        "schema_type": "HomeAndConstructionBusiness",
        "company_name": "Birchmeier-Hohler GmbH",
        "legal_name": "Birchmeier-Hohler GmbH",
        "city": "Bremgarten",
        "canton": "AG",
        "postal_code": "5620",
        "street_address": "Wohlerstrasse 17",
        "phone": "+41 56 633 33 75",
        "email": "info@birchmeier-hohler.ch",
        "uid": "",
        "source_url": "https://birchmeier-hohler.ch/",
        "hero_image": "images/sanitaer_hero.jpg",
        "summary_2s": (
            "Die Birchmeier-Hohler GmbH an der Wohlerstrasse 17 in 5620 Bremgarten (Kanton Aargau) ist Ihr "
            "traditionsreicher Schweizer Fachbetrieb für Sanitär-Installationen, schlüsselfertige Badumbauten, "
            "Heizungssanierungen und Wärmepumpen-Systeme. "
            "Seit Generationen steht der Meisterbetrieb im Reusstal und Freiamt für saubere Ausführung, "
            "persönliche Planung und zuverlässigen Service bei Umbau, Neubau und Reparatur."
        ),
        "area_served": [
            "Bremgarten", "Zufikon", "Wohlen", "Berikon", "Rudolfstetten",
            "Mutschellen", "Mellingen", "Niederwil", "Fischbach-Göslikon",
            "Freiamt", "Reusstal", "Bezirk Bremgarten", "Kanton Aargau"
        ],
        "services": [
            "Sanitär-Installationen für Neubau, Umbau und Liegenschaftsunterhalt",
            "Komplette Badumbauten und barrierefreie Badezimmer-Renovationen aus einer Hand",
            "Heizungssanierungen, Umstieg auf Wärmepumpen und energieeffiziente Wärmeerzeugung",
            "Boiler-Entkalkung, Wasserenthärtungsanlagen und Trinkwasserhygiene",
            "Reparatur-Service und Sanitär-/Heizungs-Pikett in der Region Bremgarten AG"
        ],
        "core_faqs": [
            (
                "Welche Sanitär- und Heizungsarbeiten übernimmt die Birchmeier-Hohler GmbH in Bremgarten?",
                "Die Birchmeier-Hohler GmbH an der Wohlerstrasse 17 in 5620 Bremgarten AG plant und installiert komplette Badezimmer-Umbauten, Sanitäranlagen, Wärmepumpen, Heizungsersatz-Systeme, Wasserenthärtungen sowie sämtliche Service- und Reparaturarbeiten."
            ),
            (
                "Begleitet Birchmeier-Hohler den gesamten Badumbau von der Planung bis zur Übergabe?",
                "Ja. Bei einem Badumbau begleitet Sie das Team von der ersten Bedürfnisaufnahme und Apparate-Auswahl in der Ausstellung über die Koordination der beteiligten Handwerker bis zur termingerechten, sauberen Übergabe Ihres neuen Badezimmers."
            ),
            (
                "Wann lohnt sich der Ersatz einer alten Öl- oder Gasheizung durch eine Wärmepumpe im Kanton Aargau?",
                "Spätestens ab einem Heizungsalter von 15 bis 20 Jahren empfiehlt sich eine frühzeitige Sanierungsplanung. Der Umstieg auf eine moderne Luft/Wasser- oder Sole/Wasser-Wärmepumpe senkt die Heizkosten dauerhaft und wird im Kanton Aargau mit attraktiven Fördergeldern unterstützt."
            ),
            (
                "In welchen Gemeinden rund um Bremgarten ist die Birchmeier-Hohler GmbH im Einsatz?",
                "Das Einsatzgebiet umfasst Bremgarten, Zufikon, Wohlen, den gesamten Mutschellen (Berikon, Rudolfstetten, Widen), Mellingen sowie das ganze Reusstal und Freiamt im Kanton Aargau."
            )
        ]
    }
}

# Mapping von Ordnername auf die öffentliche Vorschau-URL auf vorschau.magnet-xs.ch
PUBLIC_SLUG_MAP = {
    "preview-joma": "joma-vollversion",
    "preview-joma-v2": "joma-v2",
    "preview-imp-marketing": "imp-marketing-vollversion",
    "preview-imp-marketing-v2": "imp-marketing-v2",
    "preview-herzensarbeit": "herzensarbeit-vollversion",
    "preview-herzensarbeit-v2": "herzensarbeit-v2",
    "preview-innere-staerke": "innere-staerke-vollversion",
    "preview-innere-staerke-v2": "innere-staerke-v2",
    "preview-frees": "frees-vollversion",
    "preview-frees-v2": "frees-v2",
    "preview-fcschlieren": "fcschlieren-vollversion",
    "preview-fcschlieren-v2": "fcschlieren-v2",
    "preview-scfulenbach": "scfulenbach-v2",
    "preview-fcattiswil": "fcattiswil-v2",
    "preview-her11": "her11-v2",
    "preview-hochuli": "hochuli-v2",
    "preview-hiltbrand": "hiltbrand-v2",
    "preview-birchmeier": "birchmeier-v2",
}


def _resolve_base_slug(folder_name: str) -> str:
    """Ermittelt den Basis-Slug (z. B. 'preview-joma-v2' -> 'joma')."""
    s = folder_name.strip().lower()
    if s.startswith("preview-"):
        s = s[len("preview-"):]
    s = re.sub(r"-(?:vollversion|vv|v1|v2)$", "", s)
    return s


def _resolve_public_base_url(site_dir: Path) -> str:
    """Gibt die kanonische Vorschau-Basis-URL mit abschliessendem Slash zurück."""
    folder = site_dir.name
    if folder == "webpilot":
        return "https://embed.magnet-xs.ch/webpilot/"
    pub_slug = PUBLIC_SLUG_MAP.get(folder)
    if not pub_slug:
        clean = folder[len("preview-"):] if folder.startswith("preview-") else folder
        pub_slug = clean
    return f"https://vorschau.magnet-xs.ch/{pub_slug}/"


def _load_json_safe(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def build_site_profile(site_dir: Path) -> dict:
    """
    Kombiniert das kuratierte Schweizer Branchen-/Orts-Profil (SITE_SEO_PROFILES)
    mit Live-Metadaten aus company.json, config.json, partner-jobs/index.json
    und einem intelligenten Auto-Extractor-Fallback fuer jeden neuen Showcase.
    """
    base_slug = _resolve_base_slug(site_dir.name)
    curated = dict(SITE_SEO_PROFILES.get(base_slug, {}))

    comp = _load_json_safe(site_dir / "company.json")
    cfg = _load_json_safe(site_dir / "config.json")

    # Partner-Jobs Index prüfen
    job_entry = {}
    jobs_idx_file = site_dir.parent / "partner-jobs" / "index.json"
    if jobs_idx_file.exists():
        try:
            jobs_list = json.loads(jobs_idx_file.read_text(encoding="utf-8"))
            if isinstance(jobs_list, list):
                for j in jobs_list:
                    if isinstance(j, dict) and _resolve_base_slug(str(j.get("slug", ""))) == base_slug:
                        job_entry = j
                        break
        except Exception:
            pass

    # HTML-Index als Fallback-Quelle lesen
    idx_html = ""
    if (site_dir / "index.html").exists():
        idx_html = (site_dir / "index.html").read_text(encoding="utf-8", errors="ignore")

    company_name = _ss(
        curated.get("company_name")
        or comp.get("company_name")
        or comp.get("name")
        or cfg.get("company_name")
        or job_entry.get("company_name")
        or base_slug.replace("-", " ").title()
    )
    # Entferne evtl. "(Zeigeversion)" im offiziellen Firmennamen
    company_name = re.sub(r"\s*\(Zeigeversion\)\s*", "", company_name, flags=re.I).strip()

    legal_name = _ss(
        curated.get("legal_name")
        or comp.get("legal_name")
        or comp.get("legal_entity")
        or company_name
    )

    # Adresse / PLZ / Ort / Kanton auflösen
    addr_obj = comp.get("address") if isinstance(comp.get("address"), dict) else {}
    addr_str = comp.get("address") if isinstance(comp.get("address"), str) else ""

    city = _ss(
        curated.get("city")
        or comp.get("city")
        or addr_obj.get("city")
        or job_entry.get("city")
        or "Schweiz"
    )
    city = re.sub(r"\s+[A-Z]{2}$", "", city).strip()

    canton = _ss(
        curated.get("canton")
        or comp.get("canton")
        or addr_obj.get("canton")
        or "CH"
    )
    if canton == "CH" and base_slug == "hiltbrand":
        canton = "BE"

    postal_code = _ss(
        curated.get("postal_code")
        or str(comp.get("zip") or comp.get("postal_code") or addr_obj.get("zip") or "")
    )
    if not postal_code and addr_str:
        m_zip = re.search(r"\b(\d{4})\b", addr_str)
        if m_zip:
            postal_code = m_zip.group(1)

    street_address = _ss(
        curated.get("street_address")
        or comp.get("street")
        or addr_obj.get("street")
        or (addr_str.split(",")[0].strip() if addr_str else "")
    )

    contact_obj = comp.get("contact") if isinstance(comp.get("contact"), dict) else {}
    phone = _ss(
        curated.get("phone")
        or comp.get("phone")
        or contact_obj.get("phone")
        or cfg.get("phone")
        or ""
    )
    if not phone and idx_html:
        m_tel = re.search(r"(\+41[\s\d]{9,14})", idx_html)
        if m_tel:
            phone = m_tel.group(1).strip()

    email = _ss(
        curated.get("email")
        or comp.get("email")
        or contact_obj.get("email")
        or cfg.get("email")
        or ""
    )
    if not email and idx_html:
        m_mail = re.search(r"mailto:([a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,})", idx_html)
        if m_mail:
            email = m_mail.group(1).strip()

    uid = _ss(
        curated.get("uid")
        or comp.get("uid")
        or comp.get("zefix_uid")
        or comp.get("sofv_club_number")
        or ""
    )
    if not uid and idx_html:
        m_uid = re.search(r"(CHE-\d{3}\.\d{3}\.\d{3})", idx_html)
        if m_uid:
            uid = m_uid.group(1)

    source_url = _ss(
        curated.get("source_url")
        or comp.get("website")
        or job_entry.get("source_url")
        or (f"https://{comp['domain']}/" if comp.get("domain") else "")
    )

    schema_type = curated.get("schema_type") or "LocalBusiness"
    area_served = list(curated.get("area_served") or [city, f"Kanton {canton}", "Schweiz"])
    services = [_ss(s) for s in (curated.get("services") or [])]

    # Bestehendes Hero-/Vorschaubild auflösen
    hero_image = curated.get("hero_image") or ""
    if not hero_image or not (site_dir / hero_image).exists():
        img_dir = site_dir / "images"
        if img_dir.exists():
            candidates = [
                p for p in sorted(img_dir.glob("*"))
                if p.is_file() and p.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp")
                and "favicon" not in p.name.lower() and "apple-touch" not in p.name.lower()
            ]
            hero_pref = [p for p in candidates if any(k in p.name.lower() for k in ("hero", "stadion", "luftbild", "sportplatz", "collage", "poster"))]
            chosen = hero_pref[0] if hero_pref else (candidates[0] if candidates else None)
            if chosen:
                hero_image = f"images/{chosen.name}"

    summary_2s = _ss(curated.get("summary_2s") or "")
    if not summary_2s:
        claim = _ss(comp.get("claim") or comp.get("tagline") or comp.get("subline") or "")
        summary_2s = _ss(
            f"{company_name} mit Sitz in {city} ({canton}, Schweiz) ist Ihr regionaler Ansprechpartner für {claim or 'qualifizierte Fachleistungen'}. "
            f"Der Betrieb betreut Kundinnen und Kunden in {city} und der gesamten Region mit Schweizer Qualität und persönlicher Beratung."
        )

    core_faqs = [( _ss(q), _ss(a) ) for q, a in (curated.get("core_faqs") or [])]
    if not core_faqs:
        core_faqs = [
            (
                f"Welche Leistungen bietet {company_name} in {city} an?",
                f"{company_name} in {postal_code} {city} ({canton}) bietet persönliche Beratung, massgeschneiderte Fachlösungen und verlässlichen Service für Kundinnen und Kunden in der gesamten Region."
            ),
            (
                f"Wie erreiche ich {company_name} für eine Anfrage oder Offerte?",
                f"Sie erreichen {company_name} telefonisch unter {phone or 'der angegebenen Nummer'}, per E-Mail an {email or 'die Kontaktadresse'} oder direkt über das Online-Anfrageformular auf der Website."
            ),
            (
                f"In welchem Einzugsgebiet ist {company_name} tätig?",
                f"Vom Standort in {postal_code} {city} aus betreut {company_name} Kunden in {', '.join(area_served[:5])} und der umliegenden Region."
            )
        ]

    public_base_url = _resolve_public_base_url(site_dir)

    return {
        "base_slug": base_slug,
        "folder_name": site_dir.name,
        "schema_type": schema_type,
        "company_name": company_name,
        "legal_name": legal_name,
        "city": city,
        "canton": canton,
        "postal_code": postal_code,
        "street_address": street_address,
        "phone": phone,
        "email": email,
        "uid": uid,
        "source_url": source_url,
        "public_base_url": public_base_url,
        "hero_image": hero_image,
        "summary_2s": summary_2s,
        "area_served": area_served,
        "services": services,
        "core_faqs": core_faqs,
    }


def extract_page_intelligence(html_text: str, filename: str, profile: dict) -> dict:
    """
    Extrahiert aus einer einzelnen HTML-Seite live:
    - <title>, <meta name="description">
    - <h1>, <h2>, <h3> Überschriften
    - Einleitungs-/Lead-Absätze
    - Sichtbare FAQ-Einträge (falls auf der Seite vorhanden)
    """
    title_m = re.search(r"<title[^>]*>([\s\S]*?)</title>", html_text, re.I)
    raw_title = _strip_tags(title_m.group(1)) if title_m else ""
    if not raw_title:
        page_label = filename.replace(".html", "").replace("-", " ").title()
        raw_title = _ss(f"{profile['company_name']} · {profile['city']} | {page_label}")

    desc_m = re.search(
        r'<meta\s+[^>]*name=(["\'])description\1[^>]*content=(["\'])([\s\S]*?)\2[^>]*>',
        html_text,
        re.I,
    )
    if not desc_m:
        desc_m = re.search(
            r'<meta\s+[^>]*content=(["\'])([\s\S]*?)\1[^>]*name=(["\'])description\3[^>]*>',
            html_text,
            re.I,
        )
        raw_desc = _strip_tags(desc_m.group(2)) if desc_m else ""
    else:
        raw_desc = _strip_tags(desc_m.group(3))

    h1_list = [_strip_tags(m) for m in re.findall(r"<h1\b[^>]*>([\s\S]*?)</h1>", html_text, re.I)]
    h1_list = [h for h in h1_list if h]

    h2_list = [_strip_tags(m) for m in re.findall(r"<h2\b[^>]*>([\s\S]*?)</h2>", html_text, re.I)]
    h2_list = [
        h for h in h2_list
        if h and len(h) > 3
        and "vorschau-entwurf" not in h.lower()
        and "gefällt ihnen dieser" not in h.lower()
    ]

    h3_list = [_strip_tags(m) for m in re.findall(r"<h3\b[^>]*>([\s\S]*?)</h3>", html_text, re.I)]
    h3_list = [
        h for h in h3_list
        if h and len(h) > 3
        and "vorschau-entwurf" not in h.lower()
        and "gefällt ihnen dieser" not in h.lower()
    ]

    p_list = [_strip_tags(m) for m in re.findall(r"<p\b[^>]*>([\s\S]*?)</p>", html_text, re.I)]
    p_list = [
        p for p in p_list
        if len(p) >= 40
        and not p.startswith("©")
        and "gefällt ihnen dieser moderne" not in p.lower()
        and "unverbindlicher vorschau-entwurf" not in p.lower()
    ]

    if not raw_desc:
        h1_part = h1_list[0] if h1_list else profile["company_name"]
        p_part = p_list[0] if p_list else profile["summary_2s"]
        combined = _ss(f"{profile['company_name']} ({profile['city']} {profile['canton']}): {h1_part} – {p_part}")
        if len(combined) > 160:
            combined = combined[:157].rsplit(" ", 1)[0] + "..."
        raw_desc = combined

    # Sichtbare FAQs aus <details><summary>...</summary>...</details> extrahieren
    extracted_faqs = []
    for dm in re.finditer(r"<details\b[^>]*>[\s\S]*?<summary\b[^>]*>([\s\S]*?)</summary>([\s\S]*?)</details>", html_text, re.I):
        q = _strip_tags(dm.group(1)).lstrip("+−-•0123456789. ").strip()
        a = _strip_tags(dm.group(2)).strip()
        if len(q) >= 10 and len(a) >= 20 and "?" in q:
            extracted_faqs.append((q, a))

    # Auch .faq-item / .faq-question + .faq-answer prüfen
    if not extracted_faqs:
        for fm in re.finditer(
            r'class=["\'][^"\']*faq-(?:question|q)[^"\']*["\'][^>]*>([\s\S]*?)</[a-z0-9]+>\s*<[a-z0-9]+[^>]*class=["\'][^"\']*faq-(?:answer|a)[^"\']*["\'][^>]*>([\s\S]*?)</[a-z0-9]+>',
            html_text,
            re.I,
        ):
            q = _strip_tags(fm.group(1)).strip()
            a = _strip_tags(fm.group(2)).strip()
            if len(q) >= 10 and len(a) >= 20:
                extracted_faqs.append((q, a))

    return {
        "filename": filename,
        "title": _ss(raw_title),
        "description": _ss(raw_desc),
        "h1": h1_list,
        "h2": h2_list,
        "h3": h3_list,
        "lead_paragraphs": p_list[:5],
        "extracted_faqs": extracted_faqs,
    }


def _humanize_filename(src: str) -> str:
    """Macht aus 'images/batteriespeicher-heim.jpg' -> 'Batteriespeicher Heim'."""
    stem = Path(src.split("?")[0]).stem
    stem = re.sub(r"^(?:img|dsc|foto|bild|pic|photo|icon|ref|sponsor|katalog)[-_]*\d*[-_]*", "", stem, flags=re.I)
    stem = re.sub(r"[-_]+", " ", stem).strip()
    if not stem or stem.isdigit():
        return "Einblick und Referenz"
    words = []
    for w in stem.split():
        wl = w.lower()
        if wl in ("efh", "mfh", "zev", "ag", "gmbh", "sbb", "sfv", "sofv", "kmu", "efz", "vr", "ceo", "gl"):
            words.append(wl.upper())
        else:
            words.append(w.capitalize())
    return _ss(" ".join(words))


def _needs_alt_upgrade(alt: str, src: str, profile: dict) -> bool:
    """
    Prüft, ob ein alt-Attribut fehlt, zu kurz (< 15 Zeichen), ein Dateiname
    oder ein generischer Platzhalter ohne Firmen-/Ortsbezug ist.
    """
    a = (alt or "").strip()
    if len(a) < 15:
        return True
    al = a.lower()
    generic_exact = {
        "logo", "team", "hero", "workshop", "sponsor", "bild", "foto", "image",
        "photo", "firmenlogo", "gl foto", "vereinslogo", "wappen", "partner",
        "schreiner efz", "team gruppenfoto"
    }
    if al in generic_exact:
        return True
    if re.match(r"^(?:img_|dsc_|bild_|foto_|screenshot|untitled|image\s+of\b)", al):
        return True
    if re.search(r"\.(?:jpg|jpeg|png|webp|svg|gif)$", al):
        return True
    # Kurze Logo- oder Personen-Alts ohne Kontext (z. B. "IMP GmbH Logo", "HER11 Logo", "Free's Logo", "Martin Hochuli", "Logo Auto Lemp AG, Attiswil")
    if al.endswith(" logo") or al.startswith("logo "):
        return True
    if len(a) < 22:
        city_l = profile["city"].lower()
        comp_l = profile["company_name"].split()[0].lower()
        if city_l not in al and comp_l not in al:
            return True
    return False


def _build_rich_alt(current_alt: str, src: str, context_heading: str, filename: str, profile: dict) -> str:
    """
    Konstruiert deterministisch einen sprechenden, natürlichen Schweizer Local-SEO & GEO alt-Text
    (100 % ss, immer >= 24 Zeichen, mit Firmen- und Orts-/Regionsbezug).
    """
    comp = profile["company_name"].split("—")[0].split("·")[0].strip()
    city = profile["city"]
    canton = profile["canton"]
    loc_str = f"{city} ({canton})" if canton and canton != "CH" else city
    primary_srv = profile["services"][0] if profile.get("services") else "Fachbetrieb in der Schweiz"
    if len(primary_srv) > 58:
        primary_srv = primary_srv[:58].rsplit(" ", 1)[0]

    cur = _ss((current_alt or "").strip())
    src_l = (src or "").lower()
    cur_l = cur.lower()

    # 1. Sponsoren-Logos
    if "sponsors/" in src_l or "sponsor" in src_l or cur_l.startswith("logo "):
        sponsor_name = re.sub(r"^logo\s+", "", cur, flags=re.I).strip()
        if not sponsor_name or len(sponsor_name) < 3:
            sponsor_name = _humanize_filename(src)
        return _ss(f"Offizieller Vereins-Sponsor und Partner von {comp} ({city}): {sponsor_name}")

    # 2. Haupt-Logo der Firma / des Vereins
    if "logo" in src_l or "logo" in cur_l or "favicon" in src_l or "apple-touch-icon" in src_l:
        if "ref-" in src_l or filename == "referenzen.html":
            ref_name = cur if (cur and not cur_l.endswith("logo")) else _humanize_filename(src)
            return _ss(f"Referenz und Kundenstimme: {ref_name} – Begleitet durch {comp} in {loc_str}")
        return _ss(f"{comp} {loc_str} – Offizielles Logo ({primary_srv})")

    # 3. Referenz-Logos / Kundenstimmen
    if "ref-" in src_l or filename == "referenzen.html":
        ref_label = cur if len(cur) >= 2 else _humanize_filename(src)
        return _ss(f"Referenzunternehmen {ref_label} – Erfolgsprojekt mit {comp} ({loc_str})")

    # 4. Team- / Porträt-Bilder
    if filename in ("team.html", "ueber-uns.html", "ueber-mich.html", "profil.html") or any(k in src_l for k in ("staff-", "team", "portrait", "michael", "martin", "stefan", "claudia", "roger", "samuel", "moses", "dominik", "thomas", "jenny")):
        person_label = cur if (len(cur) >= 3 and cur_l not in ("team", "gl foto", "firmenlogo")) else _humanize_filename(src)
        return _ss(f"{person_label} – Persönlicher Ansprechpartner und Fachteam bei {comp} in {loc_str}")

    # 5. Kontext-Überschrift + Dateiname / bestehender Kurz-Alt
    human_src = _humanize_filename(src)
    base_topic = cur if (len(cur) >= 4 and cur_l not in ("hero", "bild", "foto", "workshop")) else human_src
    if context_heading and context_heading.lower() not in base_topic.lower() and len(context_heading) <= 65:
        desc = f"{base_topic}: {context_heading}"
    else:
        desc = base_topic

    result = _ss(f"{desc} – {comp} in {loc_str}")
    if len(result) < 20:
        result = _ss(f"{comp} {loc_str} – {desc} ({primary_srv})")
    return result


def enrich_html_images_alt(html_text: str, filename: str, profile: dict) -> tuple[str, int, dict]:
    """
    Prüft jedes <img>-Tag in html_text und rüstet fehlende/kurze/generische alt-Attribute
    deterministisch mit einem lokalen Schweizer SEO/GEO-alt-Text auf.
    Gibt (new_html, updated_count, src_to_alt_map) zurück.
    """
    updated_count = 0
    src_to_alt = {}

    # Alle Überschriften (H1/H2 rückwärts als Sektions-Kontext, H3/H4/figcaption vorwärts in derselben Karte)
    sec_headings = []
    for hm in re.finditer(r"<h[1-2]\b[^>]*>([\s\S]*?)</h[1-2]>", html_text, re.I):
        htxt = _strip_tags(hm.group(1))
        if htxt:
            sec_headings.append((hm.start(), htxt))

    def _nearest_heading(pos: int, end_pos: int) -> str:
        # 1. Prüfe zuerst, ob unmittelbar nach dem <img> (innerhalb derselben Card, vor dem nächsten <img>) ein <h3>/<h4>/<figcaption> folgt
        next_img_m = re.search(r"<img\b", html_text[end_pos:end_pos + 600], re.I)
        fwd_limit = end_pos + (next_img_m.start() if next_img_m else 500)
        fwd_chunk = html_text[end_pos:fwd_limit]
        card_hm = re.search(r"<(?:h[3-4]|figcaption)\b[^>]*>([\s\S]*?)</(?:h[3-4]|figcaption)>", fwd_chunk, re.I)
        if card_hm:
            ch_txt = _strip_tags(card_hm.group(1))
            if len(ch_txt) >= 3:
                return ch_txt
        # 2. Fallback: Nächstgelegene Sektions-Überschrift (H1/H2) oberhalb des Bildes
        best = ""
        for h_pos, h_txt in sec_headings:
            if h_pos <= pos:
                best = h_txt
            else:
                break
        return best

    def _img_replacer(match: re.Match) -> str:
        nonlocal updated_count
        tag = match.group(0)
        pos = match.start()

        sm = re.search(r'\bsrc=(["\'])(.*?)\1', tag, re.I)
        src = sm.group(2).strip() if sm else ""

        am = re.search(r'\balt=(["\'])(.*?)\1', tag, re.I)
        has_alt = am is not None
        cur_alt = html_lib.unescape(am.group(2)).strip() if has_alt else ""

        ctx_h = _nearest_heading(pos, match.end())

        if _needs_alt_upgrade(cur_alt, src, profile):
            new_alt = _build_rich_alt(cur_alt, src, ctx_h, filename, profile)
            safe_alt = html_lib.escape(new_alt, quote=True)
            if has_alt:
                new_tag = re.sub(r'\balt=(["\'])(.*?)\1', f'alt="{safe_alt}"', tag, count=1, flags=re.I)
            else:
                if tag.endswith("/>"):
                    new_tag = tag[:-2].rstrip() + f' alt="{safe_alt}" />'
                else:
                    new_tag = tag[:-1].rstrip() + f' alt="{safe_alt}">'
            if new_tag != tag:
                updated_count += 1
            if src and not src.startswith("${"):
                src_to_alt[src] = new_alt
                src_to_alt[Path(src.split("?")[0]).name] = new_alt
            return new_tag
        else:
            clean_existing = _ss(cur_alt)
            if src and not src.startswith("${"):
                src_to_alt[src] = clean_existing
                src_to_alt[Path(src.split("?")[0]).name] = clean_existing
            if clean_existing != cur_alt:
                updated_count += 1
                safe_alt = html_lib.escape(clean_existing, quote=True)
                return re.sub(r'\balt=(["\'])(.*?)\1', f'alt="{safe_alt}"', tag, count=1, flags=re.I)
            return tag

    new_html = re.sub(r"<img\b[^>]*>", _img_replacer, html_text, flags=re.I)
    return new_html, updated_count, src_to_alt


def build_json_ld_graph(profile: dict, page_info: dict, iso_now: str) -> dict:
    """
    Erzeugt den strukturierten Schema.org @graph (LocalBusiness/Branchen-Typ + WebSite/WebPage + FAQPage).
    """
    base_url = profile["public_base_url"]
    fname = page_info["filename"]
    page_url = base_url if fname == "index.html" else f"{base_url}{fname}"
    og_img_url = f"{base_url}{profile['hero_image']}" if profile.get("hero_image") else f"{base_url}images/logo.png"

    schema_type = profile["schema_type"]
    type_list = [schema_type, "LocalBusiness"] if schema_type != "LocalBusiness" else ["LocalBusiness"]

    # Kombiniere kuratierte Leistungen mit den echten H2/H3 der aktuellen Seite
    knows_about = []
    for s in profile.get("services", []) + page_info.get("h2", []) + page_info.get("h3", []):
        s_clean = _ss(s).strip()
        if s_clean and len(s_clean) >= 4 and s_clean not in knows_about:
            knows_about.append(s_clean)
    knows_about = knows_about[:14]

    area_entities = []
    for area in profile.get("area_served", []):
        a_clean = _ss(area).strip()
        if not a_clean:
            continue
        a_type = "AdministrativeArea" if any(k in a_clean.lower() for k in ("kanton", "bezirk", "region", "schweiz", "oberland", "tal", "gäu", "freiamt", "oberaargau")) else "City"
        area_entities.append({"@type": a_type, "name": a_clean})

    org_entity = {
        "@type": type_list,
        "@id": f"{base_url}#organization",
        "name": profile["company_name"],
        "legalName": profile["legal_name"],
        "description": profile["summary_2s"],
        "url": base_url,
        "image": og_img_url,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": profile["street_address"],
            "postalCode": profile["postal_code"],
            "addressLocality": profile["city"],
            "addressRegion": profile["canton"],
            "addressCountry": "CH",
        },
        "areaServed": area_entities,
        "knowsAbout": knows_about,
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": _ss(f"Leistungen und Schwerpunkte – {profile['company_name']}"),
            "itemListElement": [
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": srv,
                    },
                }
                for srv in (profile.get("services") or knows_about[:6])
            ],
        },
    }

    if profile.get("phone"):
        org_entity["telephone"] = profile["phone"]
    if profile.get("email"):
        org_entity["email"] = profile["email"]
    if profile.get("uid"):
        org_entity["taxID"] = profile["uid"]
        org_entity["identifier"] = profile["uid"]
    if profile.get("source_url"):
        org_entity["sameAs"] = [profile["source_url"]]

    website_entity = {
        "@type": "WebSite",
        "@id": f"{base_url}#website",
        "url": base_url,
        "name": profile["company_name"],
        "inLanguage": "de-CH",
        "publisher": {"@id": f"{base_url}#organization"},
    }

    webpage_entity = {
        "@type": "WebPage",
        "@id": f"{page_url}#webpage",
        "url": page_url,
        "name": page_info["title"],
        "description": page_info["description"],
        "inLanguage": "de-CH",
        "dateModified": iso_now,
        "isPartOf": {"@id": f"{base_url}#website"},
        "about": {"@id": f"{base_url}#organization"},
    }

    # FAQs zusammenführen (sichtbare Seiten-FAQs + kuratierte Core-FAQs)
    merged_faqs = []
    seen_q = set()
    for q, a in page_info.get("extracted_faqs", []) + profile.get("core_faqs", []):
        q_norm = q.strip().lower()
        if q_norm and q_norm not in seen_q:
            seen_q.add(q_norm)
            merged_faqs.append((_ss(q), _ss(a)))
    merged_faqs = merged_faqs[:8]

    faq_entity = {
        "@type": "FAQPage",
        "@id": f"{page_url}#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a,
                },
            }
            for q, a in merged_faqs
        ],
    }

    return {
        "@context": "https://schema.org",
        "@graph": [org_entity, website_entity, webpage_entity, faq_entity],
    }


def inject_head_seo_geo(html_text: str, profile: dict, page_info: dict, iso_now: str) -> str:
    """
    Injiziert bzw. aktualisiert idempotent im <head>:
    1. lang="de-CH" auf <html>
    2. <meta name="description"> (falls fehlend)
    3. <meta name="robots">, <meta name="geo.*">, <link rel="canonical">,
       OpenGraph (og:*) & Twitter-Card Tags
    4. <script type="application/ld+json" id="wp-seo-geo-schema">
    """
    # 1. Stelle sicher, dass <html lang="de-CH"> gesetzt ist
    if re.search(r"<html\b[^>]*\blang=", html_text, re.I):
        html_text = re.sub(
            r'(<html\b[^>]*?\blang=)(["\'])[^"\']*(\2)',
            r'\g<1>"de-CH"',
            html_text,
            count=1,
            flags=re.I,
        )
    else:
        html_text = re.sub(r"<html\b", '<html lang="de-CH"', html_text, count=1, flags=re.I)

    head_m = re.search(r"(<head\b[^>]*>)([\s\S]*?)(</head>)", html_text, re.I)
    if not head_m:
        return html_text

    head_open, head_inner, head_close = head_m.group(1), head_m.group(2), head_m.group(3)

    # Entferne früheren Autopilot-Block sowie lose Duplikat-Tags (robots, geo.*, canonical, og:*, twitter:*, ld+json)
    head_inner = re.sub(
        r"\s*<!-- WP-SEO-GEO-AUTOPILOT-START -->[\s\S]*?<!-- WP-SEO-GEO-AUTOPILOT-END -->\s*",
        "\n",
        head_inner,
        flags=re.I,
    )
    head_inner = re.sub(
        r'\s*<meta\s+[^>]*name=(["\'])(?:robots|geo\.region|geo\.placename|twitter:[a-z:]+)\1[^>]*>\s*',
        "\n",
        head_inner,
        flags=re.I,
    )
    head_inner = re.sub(
        r'\s*<meta\s+[^>]*property=(["\'])(?:og:[a-z:_]+)\1[^>]*>\s*',
        "\n",
        head_inner,
        flags=re.I,
    )
    head_inner = re.sub(
        r'\s*<link\s+[^>]*rel=(["\'])canonical\1[^>]*>\s*',
        "\n",
        head_inner,
        flags=re.I,
    )
    head_inner = re.sub(
        r'\s*<script\s+[^>]*type=(["\'])application/ld\+json\1[^>]*>[\s\S]*?</script>\s*',
        "\n",
        head_inner,
        flags=re.I,
    )

    # Prüfe, ob <meta name="description"> bereits im <head> existiert
    has_meta_desc = bool(
        re.search(r'<meta\s+[^>]*name=(["\'])description\1', head_inner, re.I)
    )

    base_url = profile["public_base_url"]
    fname = page_info["filename"]
    page_url = base_url if fname == "index.html" else f"{base_url}{fname}"
    og_img_url = f"{base_url}{profile['hero_image']}" if profile.get("hero_image") else f"{base_url}images/logo.png"

    safe_title = html_lib.escape(page_info["title"], quote=True)
    safe_desc = html_lib.escape(page_info["description"], quote=True)
    safe_comp = html_lib.escape(profile["company_name"], quote=True)
    safe_city = html_lib.escape(profile["city"], quote=True)
    region_code = f"CH-{profile['canton']}" if profile["canton"] and profile["canton"] != "CH" else "CH"
    safe_img_alt = html_lib.escape(
        _ss(f"{profile['company_name']} – {profile['city']} ({profile['canton']})"),
        quote=True,
    )

    ld_graph = build_json_ld_graph(profile, page_info, iso_now)
    ld_json_str = _ss(json.dumps(ld_graph, ensure_ascii=False, indent=2))

    meta_lines = ["  <!-- WP-SEO-GEO-AUTOPILOT-START -->"]
    if not has_meta_desc:
        meta_lines.append(f'  <meta name="description" content="{safe_desc}">')
    meta_lines.extend([
        '  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">',
        f'  <meta name="geo.region" content="{region_code}">',
        f'  <meta name="geo.placename" content="{safe_city}">',
        f'  <link rel="canonical" href="{page_url}">',
        '  <meta property="og:locale" content="de_CH">',
        '  <meta property="og:type" content="website">',
        f'  <meta property="og:site_name" content="{safe_comp}">',
        f'  <meta property="og:title" content="{safe_title}">',
        f'  <meta property="og:description" content="{safe_desc}">',
        f'  <meta property="og:url" content="{page_url}">',
        f'  <meta property="og:image" content="{og_img_url}">',
        f'  <meta property="og:image:alt" content="{safe_img_alt}">',
        '  <meta name="twitter:card" content="summary_large_image">',
        f'  <meta name="twitter:title" content="{safe_title}">',
        f'  <meta name="twitter:description" content="{safe_desc}">',
        f'  <meta name="twitter:image" content="{og_img_url}">',
        f'  <script type="application/ld+json" id="wp-seo-geo-schema">\n{ld_json_str}\n  </script>',
        "  <!-- WP-SEO-GEO-AUTOPILOT-END -->",
    ])

    injected_block = "\n" + "\n".join(meta_lines) + "\n"
    new_head = head_open + head_inner.rstrip() + injected_block + head_close
    return html_text[:head_m.start()] + new_head + html_text[head_m.end():]


def generate_llms_txt(profile: dict, pages_intel: list[dict], human_now: str) -> str:
    """
    Generiert /llms.txt im 2026er GEO-Standard für ChatGPT, Claude, Perplexity & Gemini
    direkt aus den aktuellen Live-HTML-Inhalten aller Unterseiten.
    """
    canton_label = f"Kanton {profile['canton']}" if profile["canton"] and profile["canton"] != "CH" else "Schweiz"
    lines = [
        f"# {profile['company_name']} ({profile['city']}, {canton_label}, Schweiz)",
        "",
        f"> {profile['summary_2s']}",
        "",
        "## Kernfakten & Kontakt",
        f"- **Offizieller Name:** {profile['legal_name']}",
        f"- **Standort / Adresse:** {profile['street_address']}, CH-{profile['postal_code']} {profile['city']} ({profile['canton']})".replace(" , ", " "),
    ]
    if profile.get("phone"):
        lines.append(f"- **Telefon:** {profile['phone']}")
    if profile.get("email"):
        lines.append(f"- **E-Mail:** {profile['email']}")
    if profile.get("source_url"):
        lines.append(f"- **Offizielle Website:** {profile['source_url']}")
    lines.append(f"- **WebPilot Live-URL:** {profile['public_base_url']}")
    if profile.get("uid"):
        lines.append(f"- **UID / Verbandsnummer:** {profile['uid']}")
    lines.append(f"- **Einzugsgebiet & Region:** {', '.join(profile.get('area_served', []))}")
    lines.append(f"- **Sprache & Markt:** Schweizer Hochdeutsch (de-CH), Schweiz")
    lines.append(f"- **Aktualisiert am:** {human_now}")
    lines.append("")

    # Leistungen & Schwerpunkte kombiniert mit echten H1/H2/H3 und Einleitungsabsätzen der Unterseiten
    lines.append("## Leistungen & Schwerpunkte")
    for srv in profile.get("services", []):
        lines.append(f"- {srv}")

    live_headings = []
    for pi in pages_intel:
        if pi["filename"] in ("onboarding.html", "team-update.html"):
            continue
        for h in pi.get("h2", []) + pi.get("h3", []):
            h_clean = _ss(h).strip()
            if (
                len(h_clean) >= 6
                and h_clean not in live_headings
                and not any(h_clean.lower() == s.lower() for s in profile.get("services", []))
            ):
                live_headings.append(h_clean)

    if live_headings:
        lines.append("")
        lines.append("### Aktuelle Themen & Sektionen auf der Website (Live-Extrakt)")
        for lh in live_headings[:18]:
            lines.append(f"- {lh}")

    live_leads = []
    for pi in pages_intel:
        if pi["filename"] in ("onboarding.html", "team-update.html"):
            continue
        for lp in pi.get("lead_paragraphs", [])[:2]:
            if lp not in live_leads:
                live_leads.append(lp)

    if live_leads:
        lines.append("")
        lines.append("### Kernaussagen aus den Seiteninhalten")
        for lp in live_leads[:6]:
            lines.append(f"- {lp}")

    lines.append("")
    lines.append("## Seitenstruktur & Direktlinks")
    base_url = profile["public_base_url"]
    for pi in pages_intel:
        fname = pi["filename"]
        if fname in ("onboarding.html",):
            continue
        p_url = base_url if fname == "index.html" else f"{base_url}{fname}"
        h1_str = f" — {pi['h1'][0]}" if pi.get("h1") else ""
        lines.append(f"- [{pi['title']}]({p_url}){h1_str}: {pi['description']}")

    lines.append("")
    lines.append("## Häufige Fragen & Antworten (FAQ für KI-Suchsysteme)")
    seen_q = set()
    all_faqs = []
    for pi in pages_intel:
        for q, a in pi.get("extracted_faqs", []):
            if q.lower() not in seen_q:
                seen_q.add(q.lower())
                all_faqs.append((q, a))
    for q, a in profile.get("core_faqs", []):
        if q.lower() not in seen_q:
            seen_q.add(q.lower())
            all_faqs.append((q, a))

    for q, a in all_faqs:
        lines.append(f"### {q}")
        lines.append(f"{a}")
        lines.append("")

    return _ss("\n".join(lines).rstrip() + "\n")


def generate_sitemap_xml(profile: dict, pages_intel: list[dict], iso_now: str) -> str:
    """Generiert /sitemap.xml mit allen öffentlichen HTML-Seiten (ohne cockpit.html / onboarding.html)."""
    base_url = profile["public_base_url"]
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for pi in pages_intel:
        fname = pi["filename"]
        if fname.startswith("cockpit") or fname == "onboarding.html":
            continue
        loc = base_url if fname == "index.html" else f"{base_url}{fname}"
        prio = "1.0" if fname == "index.html" else ("0.6" if fname == "team-update.html" else "0.8")
        lines.extend([
            "  <url>",
            f"    <loc>{html_lib.escape(loc)}</loc>",
            f"    <lastmod>{iso_now}</lastmod>",
            "    <changefreq>weekly</changefreq>",
            f"    <priority>{prio}</priority>",
            "  </url>",
        ])
    # llms.txt ebenfalls in Sitemap aufnehmen
    lines.extend([
        "  <url>",
        f"    <loc>{html_lib.escape(base_url + 'llms.txt')}</loc>",
        f"    <lastmod>{iso_now}</lastmod>",
        "    <changefreq>weekly</changefreq>",
        "    <priority>0.7</priority>",
        "  </url>",
        "</urlset>",
        "",
    ])
    return "\n".join(lines)


def generate_robots_txt(profile: dict) -> str:
    """
    Generiert /robots.txt mit expliziter Freigabe für Googlebot und alle KI-Such-Bots
    (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended).
    """
    base_url = profile["public_base_url"]
    bots = [
        "*",
        "Googlebot",
        "Bingbot",
        "GPTBot",
        "OAI-SearchBot",
        "ChatGPT-User",
        "PerplexityBot",
        "ClaudeBot",
        "Claude-Web",
        "Google-Extended",
        "Applebot-Extended",
    ]
    lines = [
        f"# WebPilot Auto-SEO & GEO robots.txt — {profile['company_name']} ({profile['city']})",
    ]
    for b in bots:
        lines.extend([
            f"User-agent: {b}",
            "Allow: /",
            "Disallow: /cockpit.html",
            "Disallow: /cockpit",
            "",
        ])
    lines.append(f"Sitemap: {base_url}sitemap.xml")
    lines.append(f"# LLMs: {base_url}llms.txt")
    lines.append("")
    return _ss("\n".join(lines))


def update_bilder_json_alts(site_dir: Path, profile: dict, src_to_alt_map: dict) -> int:
    """
    Aktualisiert in bilder.json (falls im Ordner vorhanden) die 'alt'-Texte aller Bilder.
    """
    bjson_path = site_dir / "bilder.json"
    if not bjson_path.exists():
        return 0
    try:
        items = json.loads(bjson_path.read_text(encoding="utf-8"))
        if not isinstance(items, list):
            return 0
        updated = 0
        for item in items:
            if not isinstance(item, dict):
                continue
            rel = str(item.get("rel_path") or "")
            fname = str(item.get("filename") or Path(rel).name)
            cur_alt = str(item.get("alt") or "").strip()
            mapped_alt = src_to_alt_map.get(rel) or src_to_alt_map.get(fname)
            if not mapped_alt:
                cat = str(item.get("category") or "")
                mapped_alt = _build_rich_alt(cur_alt, rel or fname, cat, "index.html", profile)
            mapped_alt = _ss(mapped_alt)
            if item.get("alt") != mapped_alt:
                item["alt"] = mapped_alt
                updated += 1
        if updated > 0:
            bjson_path.write_text(_ss(json.dumps(items, indent=2, ensure_ascii=False)) + "\n", encoding="utf-8")
        return updated
    except Exception:
        return 0


def run_seo_geo_autopilot_for_site(site_dir: Path, context_action: str = "cli") -> dict:
    """
    Hauptfunktion für einen einzelnen Showcase-Ordner (z. B. preview-joma).
    Kann sowohl per CLI als auch direkt aus publish_service.py und compile_site.py aufgerufen werden.
    """
    t0 = time.perf_counter()
    site_dir = Path(site_dir).resolve()
    if not site_dir.is_dir():
        raise FileNotFoundError(f"Showcase-Ordner nicht gefunden: {site_dir}")

    now_dt = datetime.now(timezone.utc).astimezone()
    iso_now = now_dt.isoformat(timespec="seconds")
    human_now = now_dt.strftime("%Y-%m-%d %H:%M")

    profile = build_site_profile(site_dir)

    html_files = sorted(
        p for p in site_dir.glob("*.html")
        if not p.name.lower().startswith("cockpit")
    )

    pages_intel = []
    combined_src_to_alt = {}
    total_imgs_updated = 0
    files_modified = 0

    for hf in html_files:
        raw_html = hf.read_text(encoding="utf-8", errors="ignore")
        working_html = _ss(raw_html)

        # 1. Seiten-Intelligenz extrahieren
        p_info = extract_page_intelligence(working_html, hf.name, profile)
        pages_intel.append(p_info)

        # 2. Local-SEO & GEO Alt-Tags auf allen <img>-Elementen aufrüsten
        working_html, img_upd, page_alt_map = enrich_html_images_alt(working_html, hf.name, profile)
        total_imgs_updated += img_upd
        combined_src_to_alt.update(page_alt_map)

        # 3. <head> mit Schema.org JSON-LD, Meta, OpenGraph, Twitter-Card & Canonical ausstatten
        working_html = inject_head_seo_geo(working_html, profile, p_info, iso_now)
        working_html = _ss(working_html)

        if working_html != raw_html:
            hf.write_text(working_html, encoding="utf-8")
            files_modified += 1

    # 4. bilder.json mit sprechenden alt-Texten aktualisieren
    bilder_updated = update_bilder_json_alts(site_dir, profile, combined_src_to_alt)

    # 5. /llms.txt, /sitemap.xml und /robots.txt taufrisch generieren
    llms_content = generate_llms_txt(profile, pages_intel, human_now)
    (site_dir / "llms.txt").write_text(llms_content, encoding="utf-8")

    sitemap_content = generate_sitemap_xml(profile, pages_intel, iso_now)
    (site_dir / "sitemap.xml").write_text(sitemap_content, encoding="utf-8")

    robots_content = generate_robots_txt(profile)
    (site_dir / "robots.txt").write_text(robots_content, encoding="utf-8")

    elapsed_ms = round((time.perf_counter() - t0) * 1000, 1)
    return {
        "ok": True,
        "site": site_dir.name,
        "company_name": profile["company_name"],
        "city": profile["city"],
        "canton": profile["canton"],
        "schema_type": profile["schema_type"],
        "html_files_processed": len(html_files),
        "html_files_modified": files_modified,
        "imgs_alt_upgraded": total_imgs_updated,
        "bilder_json_updated": bilder_updated,
        "llms_txt": True,
        "sitemap_xml": True,
        "robots_txt": True,
        "elapsed_ms": elapsed_ms,
        "context_action": context_action,
    }


def verify_showcase_dir(site_dir: Path) -> dict:
    """
    Prüft einen Showcase-Ordner auf 100 % Erfüllung aller SEO- & GEO-Kriterien:
    - ld+json (LocalBusiness/SportsOrganization + WebSite + FAQPage) auf jeder Inhaltsseite
    - meta-description & og:title / og:description / og:image auf jeder Inhaltsseite
    - 100 % aller <img>-Tags haben alt-Text >= 12 Zeichen
    - llms.txt, sitemap.xml & robots.txt vorhanden und nicht leer
    - 0 Vorkommen von Eszett (\u00df)
    """
    html_files = sorted(
        p for p in site_dir.glob("*.html")
        if not p.name.lower().startswith("cockpit")
    )

    ld_ok_all = len(html_files) > 0
    meta_og_ok_all = len(html_files) > 0
    total_imgs = 0
    valid_alt_imgs = 0
    eszett_hits = 0

    for hf in html_files:
        txt = hf.read_text(encoding="utf-8", errors="ignore")
        if "\u00df" in txt or "\u1e9e" in txt:
            eszett_hits += txt.count("\u00df") + txt.count("\u1e9e")

        ld_m = re.search(
            r'<script\s+[^>]*type=(["\'])application/ld\+json\1[^>]*>([\s\S]*?)</script>',
            txt,
            re.I,
        )
        if not ld_m:
            ld_ok_all = False
        else:
            try:
                ld_data = json.loads(ld_m.group(2))
                graph = ld_data.get("@graph", [])
                types = set()
                for node in graph:
                    t = node.get("@type")
                    if isinstance(t, list):
                        types.update(t)
                    elif isinstance(t, str):
                        types.add(t)
                has_org = bool(types.intersection({"LocalBusiness", "SportsOrganization", "Electrician", "ProfessionalService", "HealthAndBeautyBusiness", "ClothingStore", "HomeAndConstructionBusiness"}))
                has_web = "WebSite" in types and "WebPage" in types
                has_faq = "FAQPage" in types
                if not (has_org and has_web and has_faq):
                    ld_ok_all = False
            except Exception:
                ld_ok_all = False

        has_desc = bool(re.search(r'<meta\s+[^>]*name=(["\'])description\1[^>]*content=(["\'])(?:(?!\2).){10,}\2', txt, re.I))
        has_og_title = bool(re.search(r'<meta\s+[^>]*property=(["\'])og:title\1[^>]*content=(["\'])(?:(?!\2).){3,}\2', txt, re.I))
        has_og_desc = bool(re.search(r'<meta\s+[^>]*property=(["\'])og:description\1[^>]*content=(["\'])(?:(?!\2).){10,}\2', txt, re.I))
        has_og_img = bool(re.search(r'<meta\s+[^>]*property=(["\'])og:image\1[^>]*content=(["\'])https://(?:(?!\2).)+\2', txt, re.I))
        if not (has_desc and has_og_title and has_og_desc and has_og_img):
            meta_og_ok_all = False

        for im in re.finditer(r"<img\b[^>]*>", txt, re.I):
            total_imgs += 1
            am = re.search(r'\balt=(["\'])(.*?)\1', im.group(0), re.I)
            alt_val = am.group(2).strip() if am else ""
            if len(alt_val) >= 12:
                valid_alt_imgs += 1

    llms_f = site_dir / "llms.txt"
    sitemap_f = site_dir / "sitemap.xml"
    robots_f = site_dir / "robots.txt"

    files_ok = (
        llms_f.is_file() and llms_f.stat().st_size > 200
        and sitemap_f.is_file() and sitemap_f.stat().st_size > 100
        and robots_f.is_file() and robots_f.stat().st_size > 80
    )
    for aux_f in (llms_f, sitemap_f, robots_f):
        if aux_f.is_file():
            atxt = aux_f.read_text(encoding="utf-8", errors="ignore")
            eszett_hits += atxt.count("\u00df") + atxt.count("\u1e9e")

    alt_pct = 100.0 if total_imgs == 0 else round((valid_alt_imgs / total_imgs) * 100.0, 1)

    return {
        "site": site_dir.name,
        "pages": len(html_files),
        "ld_json_ok": ld_ok_all,
        "meta_og_ok": meta_og_ok_all,
        "total_imgs": total_imgs,
        "valid_alt_imgs": valid_alt_imgs,
        "alt_pct": alt_pct,
        "files_ok": files_ok,
        "eszett_hits": eszett_hits,
        "passed": ld_ok_all and meta_og_ok_all and (valid_alt_imgs == total_imgs) and files_ok and (eszett_hits == 0),
    }


def main():
    parser = argparse.ArgumentParser(description="WebPilot Auto-SEO & GEO Hintergrund-Autopilot")
    parser.add_argument("--site", "--slug", dest="site", help="Einzelner Showcase-Ordner (z. B. preview-joma oder joma)")
    parser.add_argument("--all", action="store_true", help="Alle preview-* Showcases im Workspace verarbeiten")
    parser.add_argument("--verify", action="store_true", help="Verifiziert alle verarbeiteten Showcases auf 100 %% SEO/GEO-Parität")
    args = parser.parse_args()

    if not args.site and not args.all and not args.verify:
        parser.print_help()
        sys.exit(1)

    target_dirs = []
    if args.site:
        cand = BASE_DIR / args.site
        if not cand.is_dir() and (BASE_DIR / f"preview-{args.site}").is_dir():
            cand = BASE_DIR / f"preview-{args.site}"
        if not cand.is_dir():
            cand = Path(args.site).resolve()
        if not cand.is_dir():
            print(f"Fehler: Showcase-Ordner '{args.site}' nicht gefunden.", file=sys.stderr)
            sys.exit(1)
        target_dirs.append(cand)
    else:
        target_dirs = sorted(p for p in BASE_DIR.glob("preview-*") if p.is_dir())

    if args.all or args.site:
        t_start = time.perf_counter()
        results = []
        for td in target_dirs:
            res = run_seo_geo_autopilot_for_site(td, context_action="cli")
            results.append(res)
            print(
                f"[SEO/GEO Autopilot] {res['site']:26s} | {res['schema_type']:26s} | "
                f"HTML: {res['html_files_processed']} ({res['html_files_modified']} mod) | "
                f"Alt+: {res['imgs_alt_upgraded']:2d} | {res['elapsed_ms']:5.1f} ms"
            )
        total_ms = round((time.perf_counter() - t_start) * 1000, 1)
        print(f"\n==> {len(results)} Showcases in {total_ms} ms erfolgreich SEO- & GEO-optimiert.")

    if args.verify:
        print("\n=== VERIFIKATIONS-REPORT (SEO & GEO HINTERGRUND-AUTOPILOT) ===")
        v_results = [verify_showcase_dir(td) for td in target_dirs]
        n_total = len(v_results)
        n_ld = sum(1 for r in v_results if r["ld_json_ok"])
        n_meta = sum(1 for r in v_results if r["meta_og_ok"])
        n_files = sum(1 for r in v_results if r["files_ok"])
        sum_imgs = sum(r["total_imgs"] for r in v_results)
        sum_valid_imgs = sum(r["valid_alt_imgs"] for r in v_results)
        sum_eszett = sum(r["eszett_hits"] for r in v_results)

        for r in v_results:
            status_icon = "PASS" if r["passed"] else "FAIL"
            print(
                f"  [{status_icon}] {r['site']:26s} | ld+json={str(r['ld_json_ok']):5s} | "
                f"meta/og={str(r['meta_og_ok']):5s} | imgs={r['valid_alt_imgs']:3d}/{r['total_imgs']:3d} ({r['alt_pct']:5.1f}%) | "
                f"llms/sitemap/robots={str(r['files_ok']):5s} | ss_violation={r['eszett_hits']}"
            )

        overall_img_pct = 100.0 if sum_imgs == 0 else round((sum_valid_imgs / sum_imgs) * 100.0, 2)
        print("-" * 98)
        print(f"  ld+json (LocalBusiness/SportsOrg + WebSite + FAQPage): {n_ld} / {n_total} ({n_ld == n_total})")
        print(f"  meta-description & og:title / og:description / og:image: {n_meta} / {n_total} ({n_meta == n_total})")
        print(f"  imgs mit sprechendem SEO-alt-Text (>= 12 Zeichen):     {sum_valid_imgs} / {sum_imgs} ({overall_img_pct}%)")
        print(f"  llms.txt & sitemap.xml & robots.txt vorhanden:         {n_files} / {n_total} ({n_files == n_total})")
        print(f"  Helvetischer Standard (0 Vorkommen von Eszett):        {sum_eszett} Treffer")

        if not all(r["passed"] for r in v_results):
            sys.exit(1)


if __name__ == "__main__":
    main()

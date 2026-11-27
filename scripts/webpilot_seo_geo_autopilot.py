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
2. Unsichtbarer Schema.org JSON-LD Graph (<script type="application/ld+json" id="wp-seo-schema">)
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

os.environ.setdefault("DISABLE_TELEMETRY", "1")

try:
    from PIL import Image as _PILImage
    PIL_AVAILABLE = True
except Exception:
    _PILImage = None
    PIL_AVAILABLE = False

_IMG_DIM_CACHE: dict[str, tuple[int, int] | None] = {}

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
    "seit": {
        "schema_type": "LocalBusiness",
        "company_name": "Clean Equipe GmbH · Reinigung für Zuhause, Büro & Neubau",
        "legal_name": "Clean Equipe GmbH",
        "city": "Oberkulm",
        "canton": "AG",
        "postal_code": "5727",
        "street_address": "Kreuzbündtenstrasse 8",
        "phone": "+41 76 577 57 22",
        "email": "info@clean-equipe.ch",
        "uid": "CHE-115.334.918",
        "source_url": "https://clean-equipe.ch/",
        "hero_image": "images/fensterreinigung-fachfrau.jpg",
        "summary_2s": (
            "Clean Equipe GmbH (CHE-115.334.918) in 5727 Oberkulm unter Leitung von Karolina Fabic ist seit über 20 Jahren "
            "das zuverlässige Reinigungsunternehmen für Privatpersonen und KMU im Wynental, Raum Aarau, Reinach AG und Lenzburg: "
            "regelmässige Unterhaltsreinigung, Büroreinigung, Fenster- und Storenreinigung, Bügelservice sowie gründliche Baureinigung."
        ),
        "area_served": [
            "Oberkulm", "Unterkulm", "Teufenthal", "Gränichen", "Suhr", "Buchs AG",
            "Aarau", "Reinach AG", "Menziken", "Beinwil am See", "Seon", "Lenzburg", "Kanton Aargau"
        ],
        "services": [
            "Unterhaltsreinigung für Haus und Wohnung (wöchentlich, 14-täglich oder nach individuellem Bedarf)",
            "Büro- und Gewerbereinigung (Arbeitsplätze, Sitzungszimmer, Sanitäranlagen, Küchen und Pausenräume)",
            "Baureinigung und Bauendreinigung für Neubauten, Umbauten und Sanierungen",
            "Streifenfreie Fenster-, Rahmen- und Storenreinigung für Privathaushalte und Unternehmen",
            "Treppenhausreinigung und sorgfältiger Bügelservice zur Entlastung im Alltag"
        ],
        "core_faqs": [
            (
                "Welche Reinigungsdienstleistungen bietet die Clean Equipe GmbH in Oberkulm an?",
                "Die Clean Equipe GmbH bietet seit über 20 Jahren professionelle Reinigungen für Privatpersonen und Unternehmen an: regelmässige Unterhaltsreinigung für Haus und Wohnung, Büroreinigung, Fenster- und Storenreinigung, Treppenhausreinigung, Bügelservice sowie gründliche Baureinigungen für Neu- und Umbauten."
            ),
            (
                "Kann ich eine regelmässige Reinigung im Abo oder flexibel buchen?",
                "Ja, selbstverständlich. Ob wöchentlich, alle zwei Wochen, monatlich oder punktuell nach Bedarf: Karolina Fabic und ihr Team stimmen den Rhythmus, die Einsatztage und den genauen Leistungsumfang flexibel auf Ihr Zuhause oder Ihre Geschäftsräume ab."
            ),
            (
                "In welcher Region ist Clean Equipe im Einsatz?",
                "Von unserem Standort an der Kreuzbündtenstrasse 8 in 5727 Oberkulm betreuen wir Privathaushalte, Büros, Praxen und Bauprojekte im gesamten Wynental, in Unterkulm, Reinach AG, Menziken, Gränichen, Suhr, Aarau, Seon, Lenzburg und im Kanton Aargau."
            ),
            (
                "Wie erhalte ich eine unverbindliche Reinigungsofferte?",
                "Über unseren 3-Schritte-Offerten-Assistenten auf der Website oder telefonisch unter 076 577 57 22 können Sie Ihren Bedarf in zwei Minuten angeben. Wir besprechen Ihre Wünsche persönlich und erstellen Ihnen eine faire, transparente und unverbindliche Offerte."
            ),
            (
                "Zu welchen Zeiten ist Clean Equipe erreichbar?",
                "Wir sind von Montag bis Freitag zwischen 08:00 und 17:00 Uhr sowie am Samstag von 09:00 bis 14:00 Uhr für Sie im Einsatz und telefonisch oder per WhatsApp unter 076 577 57 22 erreichbar."
            )
        ]
    },
    "mxs-talent": {
        "schema_type": "ProfessionalService",
        "company_name": "mXs Talent Solutions · magnet-Xs gmbh",
        "legal_name": "magnet-Xs gmbh",
        "city": "Zofingen",
        "canton": "AG",
        "postal_code": "4800",
        "street_address": "Vordere Hauptgasse 104",
        "phone": "+41 62 511 21 06",
        "email": "recruiting@mxs-talent-solutions.com",
        "uid": "",
        "source_url": "https://mxs-talent-solutions.com/",
        "hero_image": "images/Hue_im_Anzug_mit_Beschriftung-1024x684.png",
        "summary_2s": (
            "mXs Talent Solutions (eine Einheit der magnet-Xs gmbh in 4800 Zofingen AG) ist Ihre "
            "externe Personalabteilung, Social-Recruiting-Agentur und Ausbildungspartner für Schweizer KMU "
            "und Konzerne: über 30 Jahre Erfahrung, über 400 betreute Unternehmen und 4'200 rekrutierte "
            "Mitarbeitende durch authentische Arbeitgeber-Videos und geführtes Employer Branding."
        ),
        "area_served": [
            "Zofingen", "Aarau", "Olten", "Baden", "Zürich", "Bern",
            "Basel", "Luzern", "Solothurn", "Kanton Aargau", "Deutschschweiz", "Schweiz"
        ],
        "services": [
            "Externe Personalabteilung (Done-for-You Rekrutierung und Kandidatengewinnung)",
            "Social Recruiting Agentur mit authentischen Mitarbeiter- und Arbeitgeber-Videos",
            "Ausbildungspartner und Inhouse-Coaching für HR-, Marketing- und Employer-Branding-Teams",
            "Personalvermittlung Classic, Konzept-Beratungen und HR on Demand",
            "Employer Branding auf Autopilot für Schweizer KMU, Handwerk, Industrie und Dienstleistung"
        ],
        "core_faqs": [
            (
                "Wie unterstützt mXs Talent Solutions Unternehmen als externe Personalabteilung?",
                "mXs Talent Solutions übernimmt als erfahrene externe Personalabteilung die gezielte Ansprache passender Fachkräfte über Social Recruiting, authentische Mitarbeiter-Videos und klare Bewerbungsprozesse, sodass Sie qualifizierte Bewerbungen erhalten, die fachlich und menschlich zu Ihrem Betrieb passen."
            ),
            (
                "Können interne HR- und Marketing-Teams die Methode auch selbst erlernen?",
                "Ja. Als Ausbildungspartner befähigt mXs Talent Solutions Ihr HR-, Marketing- und Führungsteam in kompakten Trainings direkt in Ihrem Unternehmen, Employer Branding und Social Recruiting eigenständig und wirksam umzusetzen."
            ),
            (
                "Warum verzichtet mXs Talent Solutions auf öffentliche Video-Testimonials?",
                "Zum Schutz bestehender Kundinnen und Kunden vor digitalem Daten- und KI-Missbrauch veröffentlicht mXs Talent Solutions keine frei zugänglichen Video-Testimonials im Netz. Referenzen und Projektbeispiele werden im persönlichen Kennenlerngespräch vertraulich vorgestellt."
            ),
            (
                "Wie vereinbare ich ein unverbindliches Erstgespräch mit mXs Talent Solutions?",
                "Über die Seite «Strategie kennenlernen», telefonisch unter +41 62 511 21 06 oder per E-Mail an recruiting@mxs-talent-solutions.com vereinbaren Sie direkt ein persönliches Gespräch mit David Hügli oder Carmen Caselli in 4800 Zofingen."
            )
        ]
    },
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
        "source_url": "https://webpilot.magnet-xs.ch/",
        "hero_image": "images/hero.jpg",
        "summary_2s": (
            "WebPilot (ein Produkt der magnet-Xs gmbh in 4800 Zofingen AG) ist die pfeilschnelle Schweizer Web- "
            "und KI-Plattform für KMU, Handwerksbetriebe, Praxen, Sportvereine und Partner-Agenturen mit "
            "Zwei-Wege-Freiheit: Kunden passen ihre Webseite entweder selbst in 10 Sekunden im Browser über das "
            "Studio Cockpit v4.0 und Kunden-Cockpit Light für CHF 0.— pro Änderung an oder wählen die "
            "schlüsselfertige Sorglos-Betreuung über angeschlossene Schweizer Partner-Agenturen – "
            "mit transparenter 2-Stufen-Monatspauschale (CHF 35.— / Mt. Basis inkl. Schweizer Hosting, Cockpit, "
            "Google-/KI-Such-Aufbereitung & einfachem Standard-Kontaktformular bzw. CHF 45.— / Mt. Smart-Formular & PDF-Pro statt CHF 295.—/Mt. bei Drittanbietern)."
        ),
        "area_served": [
            "Zofingen", "Aarau", "Baden", "Wettingen", "Olten", "Solothurn",
            "Zürich", "Bern", "Basel", "Luzern", "St. Gallen", "Genf",
            "Kanton Aargau", "Deutschschweiz", "Schweiz"
        ],
        "services": [
            "Zwei-Wege-Freiheit: Texte, Preise und Bilder in 10 Sekunden selbst im Browser ändern, eigene Text-/KI-Entwürfe einfügen (CHF 0.— / Änderung) oder schlüsselfertig von Ihrer persönlichen Partner-Agentur betreuen lassen",
            "Automatisch bei Google & in modernen KI-Suchen gefunden werden: Laufende Hintergrund-Aufbereitung aller Leistungen, Fragen und regionalen Angaben ohne teure monatliche SEO-Zusatzpakete",
            "Bewährtes Erscheinungsbild & automatischer Darstellungsschutz: Erhalt Ihrer vertrauten Firmenfarben («Evolution statt Kulturschock») und fehlerfreie Darstellung auf jedem Smartphone, Tablet und Computer",
            "3-Schritte Smart-Anfrage: Geführte Kundenanfrage mit Handy-Foto-Upload, druckfertigem 1-Seiten-A4-PDF-Dossier, 2 Direkt-QR-Codes (Anruf & Google Maps), direkter E-Mail-Zustellung und WhatsApp-Sofortmeldung (+ CHF 10.—/Mt. im Tarif Smart-Pro für CHF 45.—/Mt. statt CHF 295.—/Mt.)",
            "Schnelles Schweizer Hosting (Zürich & Genf) ohne Wartungsfallen: Sofortige Ladezeit unter 0.1 Sekunden, volle Sicherheit inklusive SSL und keine überraschenden Update- oder Wartungsrechnungen",
            "Transparentes 2-Wege-Preismodell & 2-Stufen-Monatspauschale (Einmal-Aufbau ab CHF 2'950.— ODER All-in-Monatsmodell ab CHF 280.—/Mt. im 1. Jahr; laufend CHF 35.—/Mt. Basis bzw. CHF 45.—/Mt. Smart-Formular & PDF-Pro)"
        ],
        "core_faqs": [
            (
                "Was bedeutet die Zwei-Wege-Freiheit bei WebPilot?",
                "Bei WebPilot entscheiden Sie frei, wer am Steuer sitzt: Im Weg A bewirtschaften Macher, Teams und Vereine ihre Webseite selbst über das Kunden-Cockpit Light (Texte und Preise in 10 Sek. im Browser ändern) oder das Studio Cockpit v4.0 inklusive Übernahme eigener Text- und KI-Entwürfe für CHF 0.— pro Änderung. Im Weg B übernehmen unsere angeschlossenen Schweizer Partner-Agenturen Aufbau und laufende Änderungen auf Zuruf per WhatsApp im Sorglos-Paket. Beide Wege sind jederzeit frei kombinierbar."
            ),
            (
                "Was kostet eine WebPilot-Webseite und wie funktioniert das 2-Wege-Preismodell?",
                "Sie wählen zwischen zwei Zahlungswegen: Beim Einmal-Modell liegt der schlüsselfertige Aufbau für kompakte Seiten, Praxen und Vereine ab CHF 2'950.— einmalig (bzw. ab CHF 3'950.— für Mehrsparten-KMU und Grossvereine) plus CHF 35.— / Mt. (Basis) bzw. CHF 45.— / Mt. (Smart-Formular & PDF-Pro). Beim All-in-Monatsmodell ohne Start-Hürde zahlen Sie im 1. Jahr ab CHF 280.— / Monat (Aufbau bereits komplett eingerechnet), und ab dem 2. Jahr fällt der Preis automatisch auf nur noch CHF 35.— bzw. 45.— / Monat."
            ),
            (
                "Was ist in den beiden Monats-Stufen (CHF 35.— Basis vs. CHF 45.— Smart-Formular & PDF-Pro) enthalten?",
                "In WebPilot Basis (CHF 35.— / Monat) sind schnelles Schweizer Hosting in Zürich und Genf inklusive SSL ohne überraschende Update- oder Wartungsrechnungen, der volle Zugang zum Studio Cockpit v4.0 und Kunden-Cockpit Light (CHF 0.— Lizenz), die automatische Aufbereitung für Google und moderne KI-Suchen sowie ein einfaches Standard-Kontaktformular (Name, Kontakt, Nachricht direkt per E-Mail ans Büro) enthalten. Im Tarif WebPilot Smart-Formular & PDF-Pro (CHF 45.— / Monat, nur + CHF 10.— / Mt. statt CHF 195.— bis 295.—/Mt. bei separaten Formular-Anbietern) kommt der laufende Betrieb für geführte, mehrstufige Anfrage-, Offerten-, Bewerbungs- oder Vereinsformulare mit Handy-Foto-Upload, Sparten-/Mitarbeiter-Routing, druckfertigem 1-Seiten-A4-PDF inklusive 2 QR-Codes und WhatsApp-Sofortmeldung hinzu. Individuelle oder besonders umfangreiche Spezial-Formulare richten wir einmalig nach Aufwand passgenau ein."
            ),
            (
                "Wie sorgt WebPilot dafür, dass meine Firma bei Google und in modernen KI-Suchen gefunden wird?",
                "Ihre Webseite bereitet alle Leistungen, häufigen Kundenfragen, Bilder und regionalen Angaben bei jedem Speichervorgang im Hintergrund automatisch so auf, dass Kunden Ihren Betrieb sowohl bei Google als auch in modernen KI-Suchmaschinen sofort finden – ganz ohne teure monatliche SEO-Zusatzpakete."
            ),
            (
                "Wie funktioniert das WebPilot Partner-Programm für Agenturen, Marketing-Berater und Webdesigner?",
                "Angeschlossene Partner reichen im Partner-Studio einfach die bestehende Kunden-URL ein und erhalten innerhalb von 24 Stunden eine interaktive Zeigeversion samt Vorher/Nachher-Beweis-PDF. Das Studio Cockpit v4.0 steht Partnern für alle Kundenprojekte kostenlos (CHF 0.— Lizenzgebühr) zur Verfügung, und 100 % der laufenden Kundenbetreuung und Änderungspakete verbleiben auf der eigenen Rechnung des Partners."
            )
        ]
    },
    "ewagsuhr": {
        "schema_type": "Electrician",
        "company_name": "EWAG / E. Widmer AG",
        "legal_name": "E. Widmer AG",
        "city": "Suhr",
        "canton": "AG",
        "postal_code": "5034",
        "street_address": "Tramstrasse 47",
        "phone": "+41 62 855 08 80",
        "email": "office@ewagsuhr.ch",
        "source_url": "https://www.ewagsuhr.ch/",
        "hero_image": "images/film-02.jpg",
        "summary_2s": (
            "Die EWAG / E. Widmer AG mit Sitz an der Tramstrasse 47 in 5034 Suhr (Kanton Aargau) "
            "ist seit 1925 Ihr Spezialist für den gesamten Stark- und Schwachstrombereich bei Wohnungs-, "
            "Gewerbe- und Industriebauten. Mit rund 45 Mitarbeitenden bietet der Traditionsbetrieb Beratung, "
            "Elektroplanung, Installation, Gebäudeautomation, e-Mobilität, Photovoltaik, Ausstellung, Verkaufsladen und 24h-Pikettdienst."
        ),
        "area_served": [
            "Suhr", "Aarau", "Gränichen", "Buchs AG", "Oberentfelden",
            "Unterentfelden", "Kölliken", "Hunzenschwil", "Rohr", "Kanton Aargau"
        ],
        "faqs": [
            (
                "Wie erreiche ich den 24h-Pikettdienst der EWAG / E. Widmer AG in Suhr?",
                "Die EWAG / E. Widmer AG ist rund um die Uhr unter der Telefonnummer 062 855 08 80 erreichbar. Ausserhalb der regulären Öffnungszeiten wird Ihr Anruf bei dringenden Störungen direkt an die Pikett-Hotline weitergeleitet."
            ),
            (
                "Welche Leistungen deckt die EWAG / E. Widmer AG ab?",
                "Die EWAG deckt elf Fachbereiche ab: Haus und Wohnungen, Gewerbe und Industrie, Service und Notfälle (24h-Pikett), Schwachstrom und Netzwerk, Gebäudeautomation, Elektroplanung, e-Mobilität, Photovoltaikanlagen, Geräteprüfung, Haushaltsgeräte sowie Beleuchtung inklusive Ausstellung."
            ),
            (
                "Wo befinden sich Ausstellung und Verkaufsladen der EWAG?",
                "Die Ausstellung und der Verkaufsladen (Leuchtmittel, Installationsmaterial und Sicherungen mit Kundenparkplätzen vor und hinter dem Haus) befinden sich an der Tramstrasse 47 in 5034 Suhr."
            ),
            (
                "Bildet die EWAG Lernende im Elektroberuf aus und bietet Schnupperwochen an?",
                "Ja. In über 100 Jahren Firmengeschichte wurden bei der EWAG über 300 Lernende ausgebildet. Aktuell werden Ausbildungen zum Elektroinstallateur/in EFZ (4 Jahre) und Montageelektriker/in EFZ (3 Jahre) inklusive unverbindlicher Schnupperwochen sowie Sportler-Lehrstellen angeboten."
            ),
        ],
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
        "company_name": "IMP GmbH · Matthias Iseli (Schreinerei-Marketing)",
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
    "die-schule": {
        "schema_type": "LocalBusiness",
        "company_name": "Good for Dogs · Hundeschule Martina Sidler",
        "legal_name": "Hundeschule Good for Dogs · Martina Sidler",
        "city": "Baden",
        "canton": "AG",
        "postal_code": "5406",
        "street_address": "Region Baden-Rütihof · Übungsplatz 5413 Birmenstorf",
        "phone": "+41 76 454 54 06",
        "email": "info@goodfordogs.ch",
        "uid": "",
        "source_url": "https://goodfordogs.ch/index.html",
        "hero_image": "images/hero-mensch-hund-alltag.jpg",
        "summary_2s": (
            "Good for Dogs ist die gewaltfreie Hundeschule von Certodog® Hundeinstruktorin Martina Sidler "
            "in 5406 Baden (Rütihof) mit eingezäuntem Übungsplatz in 5413 Birmenstorf sowie Trainingsorten im Gelände zwischen Baden und Lenzburg. "
            "Angeboten werden 1:1-Einzeltraining, Welpengruppe, Erziehungskurs 1 und 2, Familienhundegruppe und Schnüffelspass in Kleingruppen von maximal 3 bis 6 Teams."
        ),
        "area_served": [
            "Baden", "Baden-Rütihof", "Birmenstorf", "Mellingen", "Dättwil",
            "Fislisbach", "Wettingen", "Brugg", "Lenzburg", "Wohlenschwil", "Kanton Aargau"
        ],
        "services": [
            "Individuelles 1:1 Einzeltraining und Verhaltensberatung im Alltag (CHF 80.— pro 60 Min.)",
            "Welpen-Gruppe ab 8 Wochen jeden Montag um 18:00 Uhr (CHF 35.— / 10er-Abo CHF 300.—)",
            "Erziehungskurs 1 für Junghunde ab 6 Monaten jeden Samstag um 09:00 Uhr (10 Lektionen CHF 300.—)",
            "Erziehungskurs 2 für Distanzarbeit und Freilauf jeden Samstag um 10:15 Uhr (10 Lektionen CHF 300.—)",
            "Familienhunde-Gruppe ab 16 Wochen jeden Montag um 16:30 Uhr (CHF 35.— / 10er-Abo CHF 300.—)",
            "Schnüffelspass-Gruppe (ZOS, Geruchsdifferenzierung, Mantrailing) jeden zweiten Samstag um 10:30 Uhr (CHF 40.— / 10er-Abo CHF 350.—)"
        ],
        "core_faqs": [
            (
                "Kann ich bei Good for Dogs jederzeit in einen Kurs einsteigen?",
                "In die Welpen-Gruppe (Montag 18:00 Uhr), die Familienhunde-Gruppe (Montag 16:30 Uhr) und die Schnüffelspass-Gruppe (jeden zweiten Samstag 10:30 Uhr) ist ein Einstieg jederzeit möglich. Erziehungskurs 1 und 2 starten als aufbauender 10er-Block am Samstagvormittag."
            ),
            (
                "Wo finden die Hundetrainings statt?",
                "Der eingezäunte Übungsplatz liegt in 5413 Birmenstorf. Ergänzend finden Trainings an realen Alltagsorten im Gelände zwischen Baden und Lenzburg sowie im Einzeltraining direkt bei Ihnen zu Hause statt."
            ),
            (
                "Wie gross sind die Trainingsgruppen bei Martina Sidler?",
                "In der Schnüffelspass-Gruppe trainieren maximal 3 Teams, in der Welpen-Gruppe maximal 5 Teams und in den Erziehungs- sowie Familienhundekursen maximal 6 Teams."
            ),
            (
                "Nach welchen Grundsätzen arbeitet die Hundeschule Good for Dogs?",
                "Martina Sidler ist zertifizierte Certodog® Hundeinstruktorin sowie Mitglied bei «Fairplay mit Hund» und der «Initiative für gewaltfreies Hundetraining». Trainiert wird fair, gewaltfrei und kynologisch fundiert."
            ),
            (
                "Wie kann bezahlt werden und welche Abmeldefristen gelten?",
                "Kurse und Einzelstunden können per Überweisung oder vor Ort via TWINT bezahlt werden. Gruppenstunden sind bis 24 Stunden, Einzeltrainings bis 48 Stunden vor Beginn kostenfrei abmeldbar."
            )
        ]
    },
    "mondocani": {
        "schema_type": "LocalBusiness",
        "company_name": "MONDOCANI · Die mobile Hundeschule · Dorette Sieber",
        "legal_name": "MONDOCANI · Dorette Sieber",
        "city": "Flumenthal / Solothurn",
        "canton": "SO",
        "postal_code": "4552",
        "street_address": "Sportstrasse (Trainingsplatz Derendingen) · Sitz Flumenthal",
        "phone": "+41 79 446 70 43",
        "email": "mail@mondocani.ch",
        "uid": "",
        "source_url": "https://mondocani.ch/",
        "hero_image": "images/hero-mensch-hund-bindung.jpg",
        "summary_2s": (
            "MONDOCANI ist die mobile Hundeschule und Praxis für ganzheitliche Mensch-Hund-Begleitung "
            "von Dorette Sieber in Flumenthal / Solothurn mit eingezäuntem Trainingsplatz an der Sportstrasse in 4552 Derendingen. "
            "Seit 2018 begleitet sie Mensch-Hund-Teams in Solothurn, Derendingen, Bern, Basel und Münchenstein "
            "im Einzelcoaching, bei wöchentlichen Rudeltreffen und im hundegestützten Coaching nach dem Grundsatz «Beziehung statt Erziehung»."
        ),
        "area_served": [
            "Solothurn", "Flumenthal", "Derendingen", "Zuchwil", "Biberist",
            "Subingen", "Luterbach", "Wangen an der Aare", "Bern", "Basel", "Münchenstein", "Kanton Solothurn"
        ],
        "services": [
            "Individuelles Einzelcoaching und Hausbesuche für Mensch-Hund-Teams (CHF 80.— pro Stunde)",
            "Wöchentliche Rudeltreffen und Gruppentreffen jeden Freitagnachmittag in 4552 Derendingen (CHF 40.— pro 1.5 Std.)",
            "Hundegestütztes Coaching für persönliche Weiterentwicklung, Selbstwert und klare Führung",
            "Workshops und Tagesseminare zur Rudelbeobachtung und Hundekommunikation (CHF 80.— pro Team)",
            "Einfühlsame Begleitung für Welpen, Junghunde sowie Tierschutz- und Strassenhunde",
            "Erlebnisvortrag auf dem Hundeplatz Derendingen und kostenloses 15-minütiges Erstgespräch"
        ],
        "core_faqs": [
            (
                "Was unterscheidet MONDOCANI von einer klassischen Hundeschule?",
                "Bei MONDOCANI steht Beziehung statt blosser Dressur im Mittelpunkt. Statt mit Kommandos, Leckerli-Manipulation oder Druck zu arbeiten, fördert Dorette Sieber eine ruhige, feinsprachliche Führung und echtes gegenseitiges Vertrauen auf Augenhöhe."
            ),
            (
                "Wie läuft das erste Einzelcoaching ab und was kostet es?",
                "Für den ersten Termin kommt Dorette Sieber gerne direkt zu Ihnen nach Hause (ca. 1.5 bis 2 Stunden), um die Wohn- und Alltagssituation entspannt einzubeziehen. Danach finden Spaziergänge in Ihrer gewohnten Umgebung statt. Der Ansatz beträgt CHF 80.— pro Stunde."
            ),
            (
                "Wann und wo finden die wöchentlichen Rudeltreffen und Gruppentreffen statt?",
                "Die Rudeltreffen finden jeden Freitagnachmittag von 14:00 bis 15:30 Uhr sowie von 16:00 bis 17:30 Uhr statt. Nach einem gemeinsamen Spaziergang treffen sich die Teams auf dem grossen eingezäunten Platz des Clubs für Deutsche Doggen an der Sportstrasse in 4552 Derendingen (direkt neben dem Fussballplatz). Kosten: CHF 40.— pro 1.5 Stunden."
            ),
            (
                "Für wen eignet sich das hundegestützte Coaching?",
                "Das hundegestützte Coaching richtet sich an Menschen mit eigenem Hund oder ohne Hund (mit dem erfahrenen Co-Coach-Hund von Dorette Sieber), die ihre Körpersprache, Präsenz, Abgrenzung, emotionale Balance und natürliche Führungskraft in Alltag, Familie oder Beruf stärken möchten."
            ),
            (
                "Kann ich die Arbeitsweise von Dorette Sieber vorab unverbindlich kennenlernen?",
                "Ja. Sie können entweder ein kostenloses 15-minütiges Kennenlerngespräch per Telefon (+41 79 446 70 43) oder Zoom vereinbaren oder am Freitag ab 16:00 Uhr den Erlebnisvortrag auf dem eingezäunten Hundeplatz in Derendingen besuchen."
            )
        ]
    },
    "atelier-piede": {
        "schema_type": "HealthAndBeautyBusiness",
        "company_name": "Atelier Piede – Praxis für Fusspflege",
        "legal_name": "Atelier Piede · Christina Widmer – von Moos",
        "city": "Kölliken",
        "canton": "AG",
        "postal_code": "5742",
        "street_address": "Wiesenstrasse 44",
        "phone": "+41 79 939 99 88",
        "email": "christina@atelierpiede.ch",
        "uid": "",
        "source_url": "https://www.atelierpiede.ch/",
        "hero_image": "images/hero-fusspflege.jpg",
        "summary_2s": (
            "Atelier Piede an der Wiesenstrasse 44 in 5742 Kölliken (Kanton Aargau) ist die Praxis für Fusspflege "
            "von Christina Widmer – von Moos, diplomierte Fusspflegerin. Angeboten werden die Praxisbehandlungen "
            "Small (CHF 79.–, 50 Min.), Standard (CHF 89.–, 65 Min.) und Premium (CHF 115.–, 80 Min.) sowie "
            "mobile Fusspflege bei Ihnen zu Hause, in Seniorenresidenzen, Pflegeheimen, Spitälern und Kliniken."
        ),
        "area_served": [
            "Kölliken", "Safenwil", "Entfelden", "Oberentfelden", "Unterentfelden",
            "Muhen", "Holziken", "Schöftland", "Oftringen", "Zofingen", "Aarau", "Kanton Aargau"
        ],
        "services": [
            "Small Fusspflege (CHF 79.–, 50 Minuten): Fussbad, Nägel kürzen, Hornhautbehandlung, Entfernen von Druckstellen, Füsse eincremen",
            "Standard Fusspflege (CHF 89.–, 65 Minuten): inklusive Fussmassage",
            "Premium Fusspflege (CHF 115.–, 80 Minuten): inklusive Ein Glas Prosecco und etwas zum Knabbern, Fusspeeling und Fussmassage",
            "Mobile Fusspflege nach Aufwand: bei Ihnen zu Hause, in Seniorenresidenzen und Pflegeheimen sowie im Spital oder in einer Klinik"
        ],
        "core_faqs": [
            (
                "Welche Fusspflege-Behandlungen bietet Atelier Piede in Kölliken an?",
                "Atelier Piede bietet drei Praxisbehandlungen: Small (CHF 79.–, 50 Minuten), Standard mit Fussmassage (CHF 89.–, 65 Minuten) sowie Premium mit einem Glas Prosecco, Fusspeeling und Fussmassage (CHF 115.–, 80 Minuten)."
            ),
            (
                "Bietet Atelier Piede auch mobile Fusspflege und Hausbesuche an?",
                "Ja. Christina Widmer – von Moos bietet mobile Fusspflege nach Aufwand direkt bei Ihnen zu Hause, in Seniorenresidenzen und Pflegeheimen sowie im Spital oder in einer Klinik an."
            ),
            (
                "Wie kann ich bei Atelier Piede einen Termin vereinbaren?",
                "Termine können telefonisch oder per WhatsApp unter 079 939 99 88, per E-Mail an christina@atelierpiede.ch oder direkt über das Terminanfrage-Formular auf dieser Seite vereinbart werden."
            )
        ]
    },
    "herzensarbeit": {
        "schema_type": "HealthAndBeautyBusiness",
        "company_name": "Herzensarbeit · Anne-Katrin Koch",
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
        "company_name": "Wüest + Paneduro · Innere Stärke entwickeln",
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
        "company_name": "Free's · Studio für Textildesign, Textildruck & Stickerei",
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
        "company_name": "HER11 · Ihr Weg. Ihr Spiel. Ihre Zukunft.",
        "legal_name": "HER11 · Initiative für Ausbildung & Karrierebegleitung im Frauenfussball",
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
    "preview-seit": "seit-vollversion",
    "preview-seit-v2": "seit-v2",
    "preview-get-more-sales": "get-more-sales-vollversion",
    "preview-get-more-sales-v2": "get-more-sales-v2",
    "preview-die-schule": "die-schule-vollversion",
    "preview-die-schule-v2": "die-schule-v2",
    "preview-mondocani": "mondocani-vollversion",
    "preview-mondocani-v2": "mondocani-v2",
    "preview-holz-susi": "holz-susi-vollversion",
    "preview-holz-susi-v2": "holz-susi-v2",
    "preview-joma": "joma-vollversion",
    "preview-joma-v2": "joma-v2",
    "preview-joma-original": "joma-original",
    "preview-joma-modern": "joma-modern",
    "preview-ewagsuhr-original": "ewagsuhr-original",
    "preview-atelier-piede": "atelier-piede",
    "preview-ewagsuhr-modern": "ewagsuhr-modern",
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
    s = re.sub(r"-(?:vollversion|vv|v1|v2|original|modern)$", "", s)
    return s


def _resolve_public_base_url(site_dir: Path) -> str:
    """Gibt die kanonische Vorschau-Basis-URL mit abschliessendem Slash zurück."""
    folder = site_dir.name
    if folder == "webpilot":
        return "https://webpilot.magnet-xs.ch/"
    if folder == "mxs-talent":
        return "https://mxs-talent-solutions.com/"
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
                (f"Sie erreichen {company_name} telefonisch unter {phone}, per E-Mail an {email or 'die Kontaktadresse'} oder direkt über das Online-Anfrageformular auf der Website." if phone else f"Sie erreichen {company_name} per E-Mail an {email or 'die Kontaktadresse'} oder direkt über die geführte 3-Schritte Smart-Anfrage auf der Website.")
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
    comp = profile["company_name"].split("\u2014")[0].split("·")[0].strip()
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


def _collect_ignored_spans(html_text: str, extra_tags: tuple[str, ...] = ()) -> list[tuple[int, int]]:
    """Sammelt Spans für Kommentare, <script>, <style> (und optionale Zusatz-Tags), die nicht mutiert werden dürfen."""
    spans: list[tuple[int, int]] = []
    for cm in re.finditer(r"<!--[\s\S]*?-->", html_text):
        spans.append((cm.start(), cm.end()))
    for tname in ("script", "style", "template") + tuple(extra_tags):
        for tm in re.finditer(rf"<{tname}\b[^>]*>[\s\S]*?</{tname}>", html_text, flags=re.I):
            spans.append((tm.start(), tm.end()))
    return spans


def _pos_in_spans(pos: int, spans: list[tuple[int, int]]) -> bool:
    for s_start, s_end in spans:
        if s_start <= pos < s_end:
            return True
    return False


def _get_attr_val(tag: str, attr_name: str) -> str | None:
    m = re.search(rf'\b{re.escape(attr_name)}=(["\'])(.*?)\1', tag, flags=re.I)
    if m:
        return html_lib.unescape(m.group(2)).strip()
    m_bare = re.search(rf'\b{re.escape(attr_name)}(?=\s|/?>)', tag, flags=re.I)
    if m_bare:
        return ""
    return None


def _remove_attr(tag: str, attr_name: str) -> str:
    cleaned = re.sub(
        rf'\s+\b{re.escape(attr_name)}=(["\']).*?\1|\s+\b{re.escape(attr_name)}(?=\s|/?>)',
        "",
        tag,
        flags=re.I,
    )
    return cleaned


def _set_or_add_attr(tag: str, attr_name: str, attr_val: str, overwrite: bool = False) -> str:
    safe_val = html_lib.escape(str(attr_val), quote=True)
    m = re.search(rf'\b{re.escape(attr_name)}=(["\'])(.*?)\1', tag, flags=re.I)
    if m:
        cur = m.group(2).strip()
        if not overwrite and cur != "":
            return tag
        if cur == safe_val and m.group(1) == '"':
            return tag
        return tag[:m.start()] + f'{attr_name}="{safe_val}"' + tag[m.end():]
    m_bare = re.search(rf'\b{re.escape(attr_name)}(?=\s|/?>)', tag, flags=re.I)
    if m_bare:
        if not overwrite:
            return tag
        return tag[:m_bare.start()] + f'{attr_name}="{safe_val}"' + tag[m_bare.end():]
    if tag.endswith("/>"):
        return tag[:-2].rstrip() + f' {attr_name}="{safe_val}" />'
    if tag.endswith(">"):
        return tag[:-1].rstrip() + f' {attr_name}="{safe_val}">'
    return tag


def _get_local_image_dimensions(site_dir: Path, src: str) -> tuple[int, int] | None:
    """Liest lokale Raster-Bildmasse via Pillow mit In-Memory-Cache (überspringt SVGs und externe URLs)."""
    if not PIL_AVAILABLE or not src:
        return None
    s = src.strip()
    if not s or s.startswith(("data:", "http://", "https://", "//", "${", "#")):
        return None
    clean_rel = s.split("?")[0].split("#")[0].strip().lstrip("/")
    if not clean_rel or clean_rel.lower().endswith(".svg"):
        return None
    try:
        site_root = site_dir.resolve()
        img_path = (site_root / clean_rel).resolve()
        if not str(img_path).startswith(str(site_root)) or not img_path.is_file():
            return None
        cache_key = str(img_path)
        if cache_key in _IMG_DIM_CACHE:
            return _IMG_DIM_CACHE[cache_key]
        with _PILImage.open(img_path) as im:
            w, h = im.size
        dims = (int(w), int(h)) if (w and h and w > 0 and h > 0) else None
        _IMG_DIM_CACHE[cache_key] = dims
        return dims
    except Exception:
        return None


def upgrade_images_lcp_and_dimensions(html_text: str, site_dir: Path) -> tuple[str, dict]:
    """
    Stufe 2a (#UI-23):
    - Erstes Bühnen-/Hero-Bild pro Seite (Nicht-Logo!) erhält fetchpriority="high" decoding="async"
      und verliert ein allfälliges loading="lazy".
    - Header-/Nav-Logos bleiben eager mit decoding="async" + lokalen Massen.
    - Alle nachfolgenden Inhaltsbilder erhalten loading="lazy" decoding="async" sowie fehlende
      width/height-Attribute aus der lokalen Bilddatei (SVGs werden übersprungen).
    - Bestehende style-, class-, alt- und data-slot-Attribute bleiben zu 100 % unangetastet.
    """
    ignored_spans = _collect_ignored_spans(html_text)
    header_nav_spans: list[tuple[int, int]] = []
    footer_spans: list[tuple[int, int]] = []
    for hm in re.finditer(r"<(?:header|nav)\b[^>]*>[\s\S]*?</(?:header|nav)>", html_text, flags=re.I):
        header_nav_spans.append((hm.start(), hm.end()))
    for fm in re.finditer(r"<footer\b[^>]*>[\s\S]*?</footer>", html_text, flags=re.I):
        footer_spans.append((fm.start(), fm.end()))

    real_matches: list[re.Match] = []
    for im in re.finditer(r"<img\b[^>]*>", html_text, flags=re.I):
        if not _pos_in_spans(im.start(), ignored_spans):
            real_matches.append(im)

    if not real_matches:
        return html_text, {"hero_upgraded": 0, "dims_added": 0, "lazy_added": 0}

    meta_list = []
    for idx, im in enumerate(real_matches):
        tag = im.group(0)
        pos = im.start()
        src = _get_attr_val(tag, "src") or ""
        slot = (_get_attr_val(tag, "data-slot") or "").lower()
        cls = (_get_attr_val(tag, "class") or "").lower()
        fname = Path(src.split("?")[0].split("#")[0]).name.lower() if src else ""
        in_hdr = _pos_in_spans(pos, header_nav_spans)
        in_ftr = _pos_in_spans(pos, footer_spans)
        ctx_before = html_text[max(0, pos - 360):pos].lower()

        is_logo = (
            in_hdr
            or in_ftr
            or ("logo" in slot)
            or ("logo" in cls)
            or ("brand-emblem" in cls)
            or fname.startswith("logo")
            or ("favicon" in fname)
            or ("apple-touch-icon" in fname)
            or ("top-bar-inner" in ctx_before[-180:])
            or ("header-inner" in ctx_before[-180:])
        )
        is_explicit_hero = (not is_logo) and (
            ("hero" in slot)
            or ("hero" in cls)
            or ("hero" in fname)
            or ("hero" in ctx_before)
        )
        meta_list.append({
            "idx": idx,
            "match": im,
            "src": src,
            "in_hdr": in_hdr,
            "is_logo": is_logo,
            "is_explicit_hero": is_explicit_hero,
        })

    hero_idx: int | None = None
    for item in meta_list:
        if item["is_explicit_hero"]:
            hero_idx = item["idx"]
            break
    if hero_idx is None:
        for item in meta_list:
            if not item["is_logo"]:
                hero_idx = item["idx"]
                break

    stats = {"hero_upgraded": 0, "dims_added": 0, "lazy_added": 0}
    out_parts: list[str] = []
    cursor = 0

    for item in meta_list:
        im = item["match"]
        out_parts.append(html_text[cursor:im.start()])
        orig_tag = im.group(0)
        new_tag = orig_tag
        src = item["src"]

        dims = _get_local_image_dimensions(site_dir, src)
        if dims is not None:
            has_w = _get_attr_val(new_tag, "width")
            has_h = _get_attr_val(new_tag, "height")
            if not has_w:
                new_tag = _set_or_add_attr(new_tag, "width", str(dims[0]), overwrite=False)
            if not has_h:
                new_tag = _set_or_add_attr(new_tag, "height", str(dims[1]), overwrite=False)
            if (not has_w) or (not has_h):
                stats["dims_added"] += 1

        if item["idx"] == hero_idx:
            cur_load = (_get_attr_val(new_tag, "loading") or "").lower()
            if cur_load == "lazy":
                new_tag = _remove_attr(new_tag, "loading")
            new_tag = _set_or_add_attr(new_tag, "fetchpriority", "high", overwrite=True)
            new_tag = _set_or_add_attr(new_tag, "decoding", "async", overwrite=True)
            if new_tag != orig_tag:
                stats["hero_upgraded"] += 1
        elif item["in_hdr"]:
            new_tag = _set_or_add_attr(new_tag, "decoding", "async", overwrite=False)
        else:
            prev_load = _get_attr_val(new_tag, "loading")
            new_tag = _set_or_add_attr(new_tag, "loading", "lazy", overwrite=False)
            new_tag = _set_or_add_attr(new_tag, "decoding", "async", overwrite=False)
            if not prev_load:
                stats["lazy_added"] += 1

        out_parts.append(new_tag)
        cursor = im.end()

    out_parts.append(html_text[cursor:])
    return "".join(out_parts), stats


_FIELD_ID_MAP: dict[str, tuple[str | None, str | None]] = {
    "contactname": ("name", "name"),
    "leadname": ("name", "name"),
    "anf-name": ("name", "name"),
    "wpname": ("name", "name"),
    "contactemail": ("email", "email"),
    "leademail": ("email", "email"),
    "anf-email": ("email", "email"),
    "wpemail": ("email", "email"),
    "contactphone": ("tel", "tel"),
    "leadphone": ("tel", "tel"),
    "anf-phone": ("tel", "tel"),
    "wpphone": ("tel", "tel"),
    "contactplz": ("postal-code", "postal-code"),
    "contactloc": ("postal-code", "postal-code"),
    "contactstreet": ("street-address", "street-address"),
    "contactcompany": ("organization", "organization"),
    "leadcompany": ("organization", "organization"),
    "anf-company": ("organization", "organization"),
    "contactmessage": ("message", None),
    "wpmessage": ("message", None),
    "projectdetails": ("message", None),
    "anf-notes": ("message", None),
    "wpdetail1": ("detail_1", None),
    "wpdetail2": ("detail_2", None),
    "wpdeviceage": ("device_age", None),
    "wpobjecttype": ("object_type", None),
    "contactcallbackpref": ("callback_preference", None),
    "wpurl": ("url", "url"),
    "wpmode": ("mode", None),
    "veredelungselect": ("veredelung", None),
    "mengeselect": ("menge", None),
    "anf-size": ("betriebsgroesse", None),
    "anf-craft": ("branche", None),
}

_KNOWN_CONTACT_FORM_IDS = {
    "iscontactform",
    "fcscontactform",
    "fcacontactform",
    "scfcontactform",
    "her11contactform",
    "wpleadform",
    "freesleadform",
    "imp-smart-anfrage-form",
    "expressform",
}


def enrich_forms_autofill_and_webmcp(html_text: str, profile: dict, filename: str) -> tuple[str, dict]:
    """
    Stufe 2b (#UI-23):
    - Entkoppelt Honeypot-Inputs (#wpHoneypot, #wpPartnerHp, name="website_url") per form="wpTrapDetached".
    - Rüstet sichtbare Kontaktfelder schonend mit fehlenden name- und autocomplete-Attributen nach
      (überschreibt niemals bestehende gültige Attribute!).
    - Deklariert auf echten Kunden-Kontaktformularen (NICHT Such-/Filter-/Partner-Modal-Formularen!)
      toolname="kontakt_anfrage_vorbereiten" und tooldescription (100 % ss) – NIEMALS toolautosubmit!
    """
    fname_low = filename.lower()
    stats = {"forms_webmcp": 0, "fields_enriched": 0, "honeypots_detached": 0}
    if fname_low.startswith(("cockpit", "team-update", "onboarding")):
        return html_text, stats

    ignored_spans = _collect_ignored_spans(html_text)
    form_matches = [
        fm for fm in re.finditer(r"(<form\b[^>]*>)([\s\S]*?)(</form>)", html_text, flags=re.I)
        if not _pos_in_spans(fm.start(), ignored_spans)
    ]
    if not form_matches:
        return html_text, stats

    out_parts: list[str] = []
    cursor = 0
    comp_clean = _ss(profile.get("company_name") or "unserem Betrieb")
    city_clean = _ss(profile.get("city") or "Schweiz")
    tool_desc = _ss(
        f"Bereitet eine unverbindliche Anfrage bei {comp_clean} ({city_clean}) zur Prüfung durch die Besucherin oder den Besucher vor."
    )

    for fm in form_matches:
        out_parts.append(html_text[cursor:fm.start()])
        form_open, form_body, form_close = fm.group(1), fm.group(2), fm.group(3)

        fid = (_get_attr_val(form_open, "id") or "").strip()
        fid_low = fid.lower()
        fcls_low = (_get_attr_val(form_open, "class") or "").lower()
        frole_low = (_get_attr_val(form_open, "role") or "").lower()

        is_partner_widget = fid_low == "wppartnerleadform"
        is_search_or_filter = (
            frole_low == "search"
            or "search" in fid_low
            or "filter" in fid_low
            or "search" in fcls_low
            or "filter" in fcls_low
        )
        has_contact_inputs = bool(
            re.search(r"<(?:input|textarea|select)\b", form_body, flags=re.I)
            and re.search(r'type=(["\'])(?:email|tel)\1|id=(["\'])[^"\']*(?:contact|lead|anf-)[^"\']*\2', form_body, flags=re.I)
        )
        is_contact_form = (
            (not is_partner_widget)
            and (not is_search_or_filter)
            and (
                fid_low in _KNOWN_CONTACT_FORM_IDS
                or (fname_low in ("kontakt.html", "karriere.html") and has_contact_inputs)
                or has_contact_inputs
            )
        )

        # Sicherheits-Invariante (#UI-23): NIEMALS toolautosubmit zulassen!
        new_form_open = _remove_attr(form_open, "toolautosubmit")
        if is_contact_form:
            prev_open = new_form_open
            new_form_open = _set_or_add_attr(new_form_open, "toolname", "kontakt_anfrage_vorbereiten", overwrite=False)
            new_form_open = _set_or_add_attr(new_form_open, "tooldescription", tool_desc, overwrite=False)
            if new_form_open != prev_open:
                stats["forms_webmcp"] += 1

        used_fallback_names: set[str] = set()

        def _field_replacer(m_fld: re.Match) -> str:
            fld_tag = m_fld.group(0)
            tag_name_m = re.match(r"<(input|textarea|select)\b", fld_tag, flags=re.I)
            tag_name = tag_name_m.group(1).lower() if tag_name_m else "input"
            el_id = (_get_attr_val(fld_tag, "id") or "").strip()
            el_id_low = el_id.lower()
            el_name = (_get_attr_val(fld_tag, "name") or "").strip()
            el_type = (_get_attr_val(fld_tag, "type") or ("text" if tag_name == "input" else "")).lower()

            # 1. Honeypot-Entkopplung via form="wpTrapDetached"
            is_honeypot = (
                el_id_low in ("wphoneypot", "wppartnerhp", "hpfield")
                or "honeypot" in el_id_low
                or el_name.lower() in ("website_url", "_hp")
            )
            if is_honeypot:
                updated_hp = _set_or_add_attr(fld_tag, "form", "wpTrapDetached", overwrite=False)
                if updated_hp != fld_tag:
                    stats["honeypots_detached"] += 1
                return updated_hp

            if not is_contact_form:
                return fld_tag

            if tag_name == "input" and el_type in ("hidden", "submit", "button", "reset", "file", "image", "checkbox", "radio"):
                return fld_tag

            inferred_name: str | None = None
            inferred_ac: str | None = None

            if el_id_low in _FIELD_ID_MAP:
                inferred_name, inferred_ac = _FIELD_ID_MAP[el_id_low]
            else:
                ph_low = (_get_attr_val(fld_tag, "placeholder") or "").lower()
                ctx_before = form_body[max(0, m_fld.start() - 220):m_fld.start()].lower()
                hint_blob = ph_low + " " + ctx_before
                if tag_name == "textarea":
                    inferred_name = "message"
                elif el_type == "email":
                    inferred_name, inferred_ac = "email", "email"
                elif el_type == "tel":
                    inferred_name, inferred_ac = "tel", "tel"
                elif el_type == "url":
                    inferred_name, inferred_ac = "url", "url"
                elif tag_name == "input" and el_type in ("text", ""):
                    if any(k in hint_blob for k in ("firma", "unternehmen", "organisation", "verein")):
                        inferred_name, inferred_ac = "organization", "organization"
                    elif any(k in hint_blob for k in ("plz", "wohnort", "ort")):
                        inferred_name, inferred_ac = "postal-code", "postal-code"
                    elif any(k in hint_blob for k in ("strasse", "adresse")):
                        inferred_name, inferred_ac = "street-address", "street-address"
                    elif any(k in hint_blob for k in ("name", "vor-", "meier", "muster")):
                        inferred_name, inferred_ac = "name", "name"
                elif tag_name == "select" and el_id:
                    inferred_name = re.sub(r"[^a-z0-9_]+", "_", el_id_low).strip("_") or "selection"

            if inferred_name and not el_id_low and inferred_name in used_fallback_names:
                idx_s = 2
                while f"{inferred_name}_{idx_s}" in used_fallback_names:
                    idx_s += 1
                inferred_name = f"{inferred_name}_{idx_s}"
            if inferred_name and not el_id_low:
                used_fallback_names.add(inferred_name)

            new_fld = fld_tag
            if inferred_name:
                new_fld = _set_or_add_attr(new_fld, "name", inferred_name, overwrite=False)
            if inferred_ac:
                new_fld = _set_or_add_attr(new_fld, "autocomplete", inferred_ac, overwrite=False)
            if new_fld != fld_tag:
                stats["fields_enriched"] += 1
            return new_fld

        body_ignored = _collect_ignored_spans(form_body)

        def _guarded_field_replacer(m_fld: re.Match) -> str:
            if _pos_in_spans(m_fld.start(), body_ignored):
                return m_fld.group(0)
            return _field_replacer(m_fld)

        new_form_body = re.sub(r"<(?:input|textarea|select)\b[^>]*>", _guarded_field_replacer, form_body, flags=re.I)
        out_parts.append(new_form_open + new_form_body + form_close)
        cursor = fm.end()

    out_parts.append(html_text[cursor:])
    return "".join(out_parts), stats


def sanitize_faq_details_headings(html_text: str) -> tuple[str, int]:
    """
    Stufe 2c (#UI-23):
    Wandelt allfällige <h1..h6>-Tags innerhalb von <summary>...</summary> verlustfrei in
    <span class="wp-summary-heading" style="font:inherit;margin:0;display:inline;"> um.
    """
    converted = 0

    def _summary_replacer(sm: re.Match) -> str:
        nonlocal converted
        s_open, s_inner, s_close = sm.group(1), sm.group(2), sm.group(3)

        def _heading_to_span(hm: re.Match) -> str:
            nonlocal converted
            attrs_raw = hm.group(2) or ""
            inner_html = hm.group(3)
            dummy_tag = f"<span{attrs_raw}>"
            cur_cls = _get_attr_val(dummy_tag, "class") or ""
            cls_tokens = [c for c in cur_cls.split() if c]
            if "wp-summary-heading" not in cls_tokens:
                cls_tokens.append("wp-summary-heading")
            dummy_tag = _set_or_add_attr(dummy_tag, "class", " ".join(cls_tokens), overwrite=True)

            cur_style = (_get_attr_val(dummy_tag, "style") or "").strip()
            base_style = "font:inherit;margin:0;display:inline;"
            if not cur_style:
                merged_style = base_style
            elif "font:inherit" in cur_style.replace(" ", ""):
                merged_style = cur_style
            else:
                merged_style = base_style + (" " + cur_style if cur_style else "")
            dummy_tag = _set_or_add_attr(dummy_tag, "style", merged_style, overwrite=True)
            converted += 1
            return f"{dummy_tag}{inner_html}</span>"

        new_inner = re.sub(r"<h([1-6])\b([^>]*)>([\s\S]*?)</h\1>", _heading_to_span, s_inner, flags=re.I)
        return s_open + new_inner + s_close

    new_html = re.sub(r"(<summary\b[^>]*>)([\s\S]*?)(</summary>)", _summary_replacer, html_text, flags=re.I)
    return new_html, converted


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

    qa_items = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a,
            },
        }
        for q, a in merged_faqs
    ]

    if profile.get("base_slug") == "webpilot":
        webpage_entity["mainEntity"] = qa_items
        return {
            "@context": "https://schema.org",
            "@graph": [org_entity, website_entity, webpage_entity],
        }

    faq_entity = {
        "@type": "FAQPage",
        "@id": f"{page_url}#faq",
        "mainEntity": qa_items,
    }

    return {
        "@context": "https://schema.org",
        "@graph": [org_entity, website_entity, webpage_entity, faq_entity],
    }


def _hex_to_rgb(hex_str: str) -> tuple[int, int, int] | None:
    """Konvertiert #RGB oder #RRGGBB in ein (r, g, b)-Tupel."""
    if not hex_str:
        return None
    s = hex_str.strip().lstrip("#")
    if len(s) == 3 and re.fullmatch(r"[0-9a-fA-F]{3}", s):
        s = "".join(c * 2 for c in s)
    if len(s) == 8 and re.fullmatch(r"[0-9a-fA-F]{8}", s):
        s = s[:6]
    if len(s) != 6 or not re.fullmatch(r"[0-9a-fA-F]{6}", s):
        return None
    return int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16)


def _rel_lum(rgb: tuple[int, int, int]) -> float:
    """Berechnet die relative WCAG-Luminanz (0.0 bis 1.0)."""
    def _c(v: int) -> float:
        s = v / 255.0
        return s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4
    return 0.2126 * _c(rgb[0]) + 0.7152 * _c(rgb[1]) + 0.0722 * _c(rgb[2])


def _contrast_ratio(c1: tuple[int, int, int], c2: tuple[int, int, int]) -> float:
    l1 = _rel_lum(c1)
    l2 = _rel_lum(c2)
    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)


def _parse_css_vars(html_text: str) -> dict[str, str]:
    """Extrahiert CSS-Custom-Properties aus :root-Blöcken."""
    vars_map: dict[str, str] = {}
    for rm in re.finditer(r":root\s*\{([^}]+)\}", html_text, flags=re.I):
        for decl in rm.group(1).split(";"):
            if ":" not in decl:
                continue
            k, v = decl.split(":", 1)
            k = k.strip()
            v = re.sub(r"/\*[\s\S]*?\*/", "", v).strip()
            if k.startswith("--") and v:
                vars_map[k] = v
    return vars_map


def _resolve_css_color(raw_val: str, css_vars: dict[str, str], depth: int = 0) -> str | None:
    """Löst var(--...) rekursiv auf und gibt #RRGGBB zurück (oder rgba -> RGB-Hex)."""
    if not raw_val or depth > 4:
        return None
    val = raw_val.strip()
    m_var = re.match(r"var\(\s*(--[a-zA-Z0-9_-]+)(?:\s*,\s*([^)]+))?\s*\)", val)
    if m_var:
        var_name = m_var.group(1)
        if var_name in css_vars:
            res = _resolve_css_color(css_vars[var_name], css_vars, depth + 1)
            if res:
                return res
        if m_var.group(2):
            return _resolve_css_color(m_var.group(2), css_vars, depth + 1)
        return None
    rgb = _hex_to_rgb(val)
    if rgb is not None:
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
    m_rgba = re.match(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)", val)
    if m_rgba:
        r, g, b = int(m_rgba.group(1)), int(m_rgba.group(2)), int(m_rgba.group(3))
        return f"#{min(255,r):02x}{min(255,g):02x}{min(255,b):02x}"
    return None


def _find_apple_touch_icon(site_dir: Path | None, head_inner: str) -> str:
    """Sucht ein physisch existierendes lokales Icon/Logo für <link rel='apple-touch-icon'>."""
    if not site_dir or not site_dir.is_dir():
        return ""
    site_root = site_dir.resolve()

    def _is_valid_local(rel_path: str) -> bool:
        if not rel_path or rel_path.startswith(("http://", "https://", "data:", "//", "${")):
            return False
        clean = rel_path.split("?")[0].split("#")[0].strip().lstrip("/")
        if not clean:
            return False
        try:
            cand = (site_root / clean).resolve()
            return str(cand).startswith(str(site_root)) and cand.is_file()
        except Exception:
            return False

    # 1. Standard-Pfad images/apple-touch-icon.png
    if _is_valid_local("images/apple-touch-icon.png"):
        return "images/apple-touch-icon.png"

    # 2. Bestehender <link rel="icon" href="..."> (bevorzugt Raster-PNG/JPG/WEBP)
    icon_hrefs = re.findall(
        r'<link\s+[^>]*rel=(["\'])(?:shortcut\s+)?icon\1[^>]*href=(["\'])([^"\']+)\2',
        head_inner,
        flags=re.I,
    )
    if not icon_hrefs:
        icon_hrefs = [
            ("", "", m)
            for m in re.findall(
                r'<link\s+[^>]*href=(["\'])([^"\']+)\1[^>]*rel=(["\'])(?:shortcut\s+)?icon\3',
                head_inner,
                flags=re.I,
            )
        ]
    local_icons = []
    for item in icon_hrefs:
        href = item[2] if len(item) >= 3 else item[1]
        if isinstance(href, tuple):
            href = href[1]
        if _is_valid_local(href):
            local_icons.append(href)
    for href in local_icons:
        if Path(href.split("?")[0]).suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"):
            return href

    # 3. Lokale *favicon* oder *logo*.png unter images/ und assets/
    for sub in ("images", "assets"):
        subdir = site_root / sub
        if not subdir.is_dir():
            continue
        for pat in ("*favicon*.png", "*favicon*.webp", "*favicon*.jpg", "*favicon*.ico", "*logo*.png"):
            matches = sorted(p for p in subdir.glob(pat) if p.is_file())
            # Bevorzuge nicht-invertierte Logos (_neg zuletzt)
            matches.sort(key=lambda p: (1 if "_neg" in p.name.lower() else 0, p.name.lower()))
            if matches:
                return f"{sub}/{matches[0].name}"

    if local_icons:
        return local_icons[0]
    return ""


def inject_skip_to_content(html_text: str, filename: str) -> str:
    """
    Injiziert idempotent einen WCAG-2.2-Skip-Link nach <body>, sofern noch kein
    Skip-Link existiert UND ein <main>-Landmark vorhanden ist (#UI-23 / Paket D).
    """
    fname_low = filename.lower()
    if fname_low.startswith(("cockpit", "team-update", "onboarding")) or fname_low == "404.html":
        return html_text
    if re.search(r'\bwp-skip-link\b|\bskip-link\b', html_text, flags=re.I):
        return html_text
    if re.search(r'<a\b[^>]*href=(["\'])#main(?:-content)?\1[^>]*>[^<]*(?:Inhalt|Skip)', html_text, flags=re.I):
        return html_text

    main_m = re.search(r"<main\b([^>]*)>", html_text, flags=re.I)
    if not main_m:
        return html_text

    main_attrs = main_m.group(1) or ""
    id_m = re.search(r'\bid=(["\'])(.*?)\1', main_attrs, flags=re.I)
    if id_m and id_m.group(2).strip():
        main_id = id_m.group(2).strip()
        working = html_text
    else:
        main_id = "main-content"
        new_main_tag = f'<main id="{main_id}"{main_attrs}>'
        working = html_text[:main_m.start()] + new_main_tag + html_text[main_m.end():]

    body_m = re.search(r"<body\b[^>]*>", working, flags=re.I)
    if not body_m:
        return html_text

    skip_tag = f'\n  <a class="wp-skip-link" href="#{html_lib.escape(main_id, quote=True)}">Direkt zum Inhalt</a>'
    return working[:body_m.end()] + skip_tag + working[body_m.end():]


def inject_head_seo_geo(
    html_text: str,
    profile: dict,
    page_info: dict,
    iso_now: str,
    page_count: int = 1,
    has_step3_wizard: bool = False,
    site_dir: Path | None = None,
) -> str:
    """
    Injiziert bzw. aktualisiert idempotent im <head>:
    1. lang="de-CH" auf <html>
    2. <meta name="description"> (falls fehlend)
    3. <meta name="robots">, <meta name="geo.*">, <link rel="canonical">,
       OpenGraph (og:*) & Twitter-Card Tags
    4. <style id="wp-modern-web-css"> (@view-transition, interpolate-size, :user-invalid, img aspect-ratio guard)
    5. <script type="speculationrules" id="wp-speculation-rules"> (nur bei Mehrseiten-Showcases >= 2 Seiten)
    6. <script id="wp-webmcp-step-sync"> (nur bei mehrstufigen Formularen mit #wpStep3.wp-step-pane)
    7. <script type="application/ld+json" id="wp-seo-schema">
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

    # Entferne allfällige lose #wp-webmcp-step-sync Skripte ausserhalb von <head>
    html_text = re.sub(
        r'\s*<script\b[^>]*\bid=(["\'])wp-webmcp-step-sync\1[^>]*>[\s\S]*?</script>',
        "",
        html_text,
        flags=re.I,
    )

    head_m = re.search(r"(<head\b[^>]*>)([\s\S]*?)(</head>)", html_text, re.I)
    if not head_m:
        return html_text

    head_open, head_inner, head_close = head_m.group(1), head_m.group(2), head_m.group(3)

    # Entferne früheren Autopilot-Block sowie lose Duplikat-Tags (robots, geo.*, canonical, og:*, twitter:*, ld+json, modern-web)
    head_inner = re.sub(
        r"\s*<!-- WP-SEO-(?:GEO-)?AUTOPILOT-START -->[\s\S]*?<!-- WP-SEO-(?:GEO-)?AUTOPILOT-END -->\s*",
        "\n",
        head_inner,
        flags=re.I,
    )
    head_inner = re.sub(
        r'\s*<style\b[^>]*\bid=(["\'])wp-modern-web-css\1[^>]*>[\s\S]*?</style>\s*',
        "\n",
        head_inner,
        flags=re.I,
    )
    head_inner = re.sub(
        r'\s*<script\b[^>]*\bid=(["\'])wp-speculation-rules\1[^>]*>[\s\S]*?</script>\s*',
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

    # Prüfe, ob <meta name="description"> oder <link rel="apple-touch-icon"> bereits im <head> existiert
    has_meta_desc = bool(
        re.search(r'<meta\s+[^>]*name=(["\'])description\1', head_inner, re.I)
    )
    has_apple_touch_icon = bool(
        re.search(r'<link\s+[^>]*rel=(["\'])apple-touch-icon\1', head_inner, re.I)
    )
    apple_icon_href = "" if has_apple_touch_icon else _find_apple_touch_icon(site_dir, head_inner)

    base_url = profile["public_base_url"]
    fname = page_info["filename"]
    fname_low = fname.lower()
    is_internal_tool_page = fname_low.startswith(("cockpit", "team-update", "onboarding"))
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

    modern_css = (
        '  <style id="wp-modern-web-css">\n'
        "    @media (prefers-reduced-motion: no-preference) { @view-transition { navigation: auto; } }\n"
        "    html { interpolate-size: allow-keywords; }\n"
        "    :where(img[width][height]) { height: auto; }\n"
        "    input:user-invalid, textarea:user-invalid, select:user-invalid { border-color: #DC2626 !important; outline: none; }\n"
        "    :where(a,button,input,select,textarea,summary,[tabindex]):focus-visible{outline:2px solid var(--accent,var(--primary,#e8781e));outline-offset:2px;}\n"
        "    .wp-skip-link{position:absolute;top:0;left:0;width:1px;height:1px;padding:0;margin:-1px;border:0;overflow:hidden;clip-path:inset(50%);white-space:nowrap;z-index:99999;background:#0d0f12;color:#ffffff;font-weight:600;text-decoration:none;border-radius:4px;}\n"
        "    .wp-skip-link:focus,.wp-skip-link:focus-visible{width:auto;height:auto;margin:0;padding:10px 16px;clip-path:none;overflow:visible;top:8px;left:8px;}\n"
        "  </style>"
    )

    spec_where = {
        "and": [
            {"href_matches": "/*"},
            {
                "not": {
                    "href_matches": [
                        "/*cockpit*",
                        "/cockpit*",
                        "/*team-update*",
                        "/*onboarding*",
                        "/api/*",
                        "/cdn-cgi/*",
                        "/*.pdf",
                        "/*?*",
                        "/*#*",
                    ]
                }
            },
            {
                "not": {
                    "selector_matches": "[target=_blank], [download], [data-no-prerender], [href^='mailto:'], [href^='tel:']"
                }
            },
        ]
    }
    spec_rules_obj = {
        "prefetch": [{"where": spec_where, "eagerness": "moderate"}],
        "prerender": [{"where": spec_where, "eagerness": "conservative"}],
    }
    spec_rules_json = json.dumps(spec_rules_obj, ensure_ascii=False, indent=2)

    step_sync_js = (
        '  <script id="wp-webmcp-step-sync">\n'
        "    (function(){\n"
        "      var STEP3_IDS = {contactName:1,contactEmail:1,contactPhone:1,contactPlz:1,contactLoc:1,contactStreet:1,contactCompany:1};\n"
        "      function wpSyncStep3(e){\n"
        "        var t = e && e.target;\n"
        "        if (!t || !t.id || !STEP3_IDS[t.id]) return;\n"
        "        if (!String(t.value || '').trim()) return;\n"
        "        var s3 = document.getElementById('wpStep3');\n"
        "        if (!s3 || s3.classList.contains('active')) return;\n"
        "        if (typeof window.wpNextStep === 'function') { window.wpNextStep(3); return; }\n"
        "        var panes = document.querySelectorAll('.wp-step-pane');\n"
        "        for (var i = 0; i < panes.length; i++) panes[i].classList.toggle('active', panes[i].id === 'wpStep3');\n"
        "        for (var s = 1; s <= 3; s++) {\n"
        "          var pill = document.getElementById('wpStepPill' + s);\n"
        "          if (pill) { pill.classList.toggle('active', s === 3); pill.classList.toggle('done', s < 3); }\n"
        "        }\n"
        "      }\n"
        "      document.addEventListener('input', wpSyncStep3, true);\n"
        "      document.addEventListener('change', wpSyncStep3, true);\n"
        "    })();\n"
        "  </script>"
    )

    meta_lines = ["  <!-- WP-SEO-AUTOPILOT-START -->"]
    if not has_meta_desc:
        meta_lines.append(f'  <meta name="description" content="{safe_desc}">')
    if apple_icon_href and not is_internal_tool_page:
        meta_lines.append(f'  <link rel="apple-touch-icon" href="{html_lib.escape(apple_icon_href, quote=True)}">')
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
        modern_css,
    ])
    if page_count >= 2 and not is_internal_tool_page:
        meta_lines.append(f'  <script type="speculationrules" id="wp-speculation-rules">\n{spec_rules_json}\n  </script>')
    if has_step3_wizard and not is_internal_tool_page:
        meta_lines.append(step_sync_js)
    meta_lines.extend([
        f'  <script type="application/ld+json" id="wp-seo-schema">\n{ld_json_str}\n  </script>',
        "  <!-- WP-SEO-AUTOPILOT-END -->",
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
        if pi["filename"] in ("onboarding.html", "team-update.html", "404.html"):
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
        if pi["filename"] in ("onboarding.html", "team-update.html", "404.html"):
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
        if fname in ("onboarding.html", "404.html"):
            continue
        p_url = base_url if fname == "index.html" else f"{base_url}{fname}"
        h1_str = f" – {pi['h1'][0]}" if pi.get("h1") else ""
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
        if fname.startswith("cockpit") or fname in ("onboarding.html", "404.html"):
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
    (inkl. Content-Signal gemäss isitagentready.com & Claude/Perplexity/Anthropic-User-Agents).
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
        "Perplexity-User",
        "ClaudeBot",
        "Claude-SearchBot",
        "Claude-User",
        "Claude-Web",
        "anthropic-ai",
        "Google-Extended",
        "Applebot-Extended",
    ]
    lines = [
        f"# WebPilot Auto-SEO & GEO robots.txt – {profile['company_name']} ({profile['city']})",
    ]
    for b in bots:
        lines.extend([
            f"User-agent: {b}",
            "Allow: /",
            "Disallow: /cockpit.html",
            "Disallow: /cockpit",
        ])
        if b == "*":
            lines.append("Content-Signal: ai-train=yes, search=yes, ai-input=yes")
        lines.append("")
    lines.append(f"Sitemap: {base_url}sitemap.xml")
    lines.append(f"# LLMs: {base_url}llms.txt")
    lines.append("")
    return _ss("\n".join(lines))


def generate_404_html(profile: dict, site_dir: Path) -> str:
    """
    Erzeugt eine schlanke, farblich und typografisch passende Mandanten-404.html
    (#UI-01, #UI-10 ohne X-Frame-Options: DENY, #UI-16 Helligkeits-Treue, #LANG-01 100 % ss).
    """
    site_dir = Path(site_dir)
    idx_path = site_dir / "index.html"
    idx_html = idx_path.read_text(encoding="utf-8", errors="ignore") if idx_path.is_file() else ""
    css_vars = _parse_css_vars(idx_html)

    # 1. Polarität & Hintergrundfarbe aus index.html + source_visual_dna.json ermitteln (#UI-16)
    bg_hex = None
    body_css_m = re.search(r"body\s*\{([^}]+)\}", idx_html)
    if body_css_m:
        bg_decl = re.search(r"background(?:-color)?\s*:\s*([^;]+);", body_css_m.group(1))
        if bg_decl:
            bg_hex = _resolve_css_color(bg_decl.group(1), css_vars)
    if not bg_hex:
        for vk in ("--bg-page", "--bg", "--bg-light", "--canvas", "--white"):
            if vk in css_vars:
                bg_hex = _resolve_css_color(css_vars[vk], css_vars)
                if bg_hex:
                    break
    if not bg_hex:
        bg_hex = "#090a0f" if site_dir.name == "webpilot" else "#f8fafc"

    bg_rgb = _hex_to_rgb(bg_hex) or (248, 250, 252)
    is_dark = _rel_lum(bg_rgb) < 0.25

    if is_dark:
        bg_hex = "#090a0f"
        surface_hex = "#111420"
        text_hex = "#f8fafc"
        muted_hex = "#cbd5e1"
        border_hex = "#232a42"
    else:
        surface_hex = "#ffffff"
        text_hex = "#0f172a"
        muted_hex = "#475569"
        border_hex = "#e2e8f0"

    # 2. Marken-Akzentfarbe extrahieren & Button-/Badge-Kontrast garantieren (S-26)
    accent_hex = None
    for vk in (
        "--accent", "--primary", "--recruiting", "--copper", "--fca-red",
        "--fcs-red", "--scf-red", "--pink", "--crimson", "--gold", "--amber", "--brand"
    ):
        if vk in css_vars:
            cand = _resolve_css_color(css_vars[vk], css_vars)
            if cand and cand.lower() not in ("#ffffff", "#000000"):
                accent_hex = cand
                break
    if not accent_hex:
        accent_hex = "#f59e0b" if is_dark else "#e8781e"
    accent_rgb = _hex_to_rgb(accent_hex) or (232, 120, 30)

    btn_fg_hex = "#090a0f" if _contrast_ratio((9, 10, 15), accent_rgb) >= _contrast_ratio((255, 255, 255), accent_rgb) else "#ffffff"

    if is_dark:
        badge_bg_css = "rgba(245, 158, 11, 0.14)"
        badge_fg_hex = "#fbbf24"
        badge_border_css = "rgba(245, 158, 11, 0.32)"
    else:
        blended_badge_bg = (
            round(accent_rgb[0] * 0.10 + 255 * 0.90),
            round(accent_rgb[1] * 0.10 + 255 * 0.90),
            round(accent_rgb[2] * 0.10 + 255 * 0.90),
        )
        if _contrast_ratio(accent_rgb, blended_badge_bg) >= 4.5:
            badge_bg_css = f"rgba({accent_rgb[0]}, {accent_rgb[1]}, {accent_rgb[2]}, 0.10)"
            badge_fg_hex = accent_hex
            badge_border_css = f"rgba({accent_rgb[0]}, {accent_rgb[1]}, {accent_rgb[2]}, 0.28)"
        else:
            badge_bg_css = "#f1f5f9"
            badge_fg_hex = "#0f172a"
            badge_border_css = "#cbd5e1"

    # 3. Header-Hintergrund bestimmen (schützt helle Logos auf dunklen Headers wie preview-seit / preview-frees)
    hdr_bg_hex = None
    hdr_css_m = re.search(r"(?:\.top-bar|header(?:\.site-header|\.main-header)?)\s*\{([^}]+)\}", idx_html)
    if hdr_css_m:
        hbg_decl = re.search(r"background(?:-color)?\s*:\s*([^;]+);", hdr_css_m.group(1))
        if hbg_decl:
            hdr_bg_hex = _resolve_css_color(hbg_decl.group(1), css_vars)
    if not hdr_bg_hex:
        hdr_bg_hex = "#090a0f" if is_dark else "#ffffff"
    hdr_rgb = _hex_to_rgb(hdr_bg_hex) or (255, 255, 255)
    hdr_is_dark = _rel_lum(hdr_rgb) < 0.35
    hdr_text_hex = "#ffffff" if hdr_is_dark else "#0f172a"
    hdr_border_css = "rgba(255, 255, 255, 0.12)" if hdr_is_dark else "#e2e8f0"

    # 4. Markenname, Logo & Google Fonts ohne JetBrains Mono (#UI-01 Pt 4)
    comp_short = _ss(profile.get("company_name") or site_dir.name).split("\u2014")[0].split("·")[0].strip()
    if site_dir.name == "webpilot":
        comp_short = "WebPilot"
    legal_footer = _ss(profile.get("legal_name") or comp_short)
    city_str = _ss(profile.get("city") or "")
    footer_line = f"{legal_footer} · {profile['postal_code']} {city_str}".strip() if profile.get("postal_code") and city_str else (f"{legal_footer} · {city_str}".strip(" ·"))

    logo_html = ""
    if site_dir.name == "webpilot":
        logo_html = (
            '<svg width="32" height="32" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
            '<defs><linearGradient id="wpDelta404" x1="20" y1="80" x2="85" y2="20" gradientUnits="userSpaceOnUse">'
            '<stop offset="0%" stop-color="#f59e0b"/><stop offset="100%" stop-color="#fbbf24"/>'
            '</linearGradient></defs>'
            '<path d="M18 76L82 22L54 82L46 58L18 76Z" fill="url(#wpDelta404)"/>'
            '</svg>'
            '<span class="err-brand-name">WebPilot</span>'
        )
    else:
        body_m = re.search(r"<body[^>]*>([\s\S]{0,6000})", idx_html, re.I)
        body_head = body_m.group(1) if body_m else ""
        logo_rel = ""
        for src in re.findall(r'<img\b[^>]*src=(["\'])([^"\']+)\1', body_head, re.I):
            cand_src = src[1].strip()
            clean_cand = cand_src.split("?")[0].split("#")[0].lstrip("/")
            if "favicon" in clean_cand.lower() or cand_src.startswith(("http://", "https://", "data:", "//")):
                continue
            if (site_dir / clean_cand).is_file():
                logo_rel = cand_src
                break
        if not logo_rel:
            for sub in ("images", "assets"):
                sdir = site_dir / sub
                if sdir.is_dir():
                    for pat in ("*logo*.png", "*logo*.webp", "*logo*.svg", "*logo*.jpg"):
                        cands = sorted(p for p in sdir.glob(pat) if p.is_file())
                        if cands:
                            logo_rel = f"{sub}/{cands[0].name}"
                            break
                if logo_rel:
                    break
        if logo_rel:
            dims = _get_local_image_dimensions(site_dir, logo_rel)
            dim_attrs = f' width="{dims[0]}" height="{dims[1]}"' if dims else ""
            logo_html = (
                f'<img src="{html_lib.escape(logo_rel, quote=True)}" '
                f'alt="{html_lib.escape(comp_short, quote=True)}"{dim_attrs} '
                f'class="err-logo-img" decoding="async">'
            )
        else:
            logo_html = f'<span class="err-brand-name">{html_lib.escape(comp_short)}</span>'

    # 5. Lokaler Kontakt-Link (falls kontakt.html / schaden-kontakt.html / strategie-kennen-lernen.html existiert)
    contact_btn_html = ""
    for cname, clabel in (
        ("kontakt.html", "Kontakt aufnehmen"),
        ("schaden-kontakt.html", "Kontakt und Schadenmeldung"),
        ("strategie-kennen-lernen.html", "Strategie kennenlernen"),
    ):
        if (site_dir / cname).is_file():
            contact_btn_html = (
                f'        <a class="err-btn err-btn-secondary" href="{cname}">\n'
                '          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
                '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>\n'
                f'          <span>{html_lib.escape(_ss(clabel))}</span>\n'
                '        </a>\n'
            )
            break

    safe_title = html_lib.escape(_ss(f"Seite nicht gefunden (404) · {comp_short}"))
    safe_comp_label = html_lib.escape(comp_short)
    safe_footer_line = html_lib.escape(_ss(footer_line))
    apple_href = _find_apple_touch_icon(site_dir, idx_html)
    apple_tag = f'  <link rel="apple-touch-icon" href="{html_lib.escape(apple_href, quote=True)}">\n' if apple_href else ""

    html_out = f"""<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-XSS-Protection" content="1; mode=block">
  <meta name="referrer" content="no-referrer">
{apple_tag}  <title>{safe_title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --bg: {bg_hex};
      --surface: {surface_hex};
      --border: {border_hex};
      --text: {text_hex};
      --muted: {muted_hex};
      --accent: {accent_hex};
      --btn-fg: {btn_fg_hex};
      --radius-sm: 4px;
      --radius-md: 8px;
    }}
    html, body {{
      width: 100%;
      min-height: 100vh;
      overflow-x: clip;
      background: var(--bg);
      color: var(--text);
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}
    body {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    :where(a, button):focus-visible {{
      outline: 2px solid var(--accent);
      outline-offset: 2px;
    }}
    .err-header {{
      width: 100%;
      background: {hdr_bg_hex};
      color: {hdr_text_hex};
      border-bottom: 1px solid {hdr_border_css};
    }}
    .err-header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 12px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }}
    .err-brand {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: {hdr_text_hex};
      min-height: 44px;
    }}
    .err-brand-name {{
      font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
      font-weight: 800;
      font-size: 1.05rem;
      letter-spacing: -0.02em;
      color: {hdr_text_hex};
    }}
    .err-logo-img {{
      max-height: 38px;
      width: auto;
      height: auto;
      display: block;
      object-fit: contain;
    }}
    .err-hdr-link {{
      display: inline-flex;
      align-items: center;
      min-height: 44px;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      color: {hdr_text_hex};
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
    }}
    .err-hdr-link:hover {{ text-decoration: underline; text-underline-offset: 3px; }}
    .err-main {{
      width: 100%;
      flex: 1 0 auto;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 40px 16px;
    }}
    .err-section {{
      width: 100%;
      max-width: 1100px;
      margin: 0 auto;
    }}
    .err-card {{
      max-width: 560px;
      margin: 0 auto;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 36px 28px;
      text-align: center;
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
    }}
    .err-badge {{
      display: inline-block;
      background: {badge_bg_css};
      color: {badge_fg_hex};
      border: 1px solid {badge_border_css};
      border-radius: var(--radius-sm);
      padding: 4px 10px;
      font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      margin-bottom: 14px;
    }}
    h1 {{
      font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
      font-size: clamp(1.5rem, 3.5vw, 2rem);
      font-weight: 800;
      letter-spacing: -0.025em;
      line-height: 1.2;
      color: var(--text);
      margin-bottom: 12px;
    }}
    .err-desc {{
      color: var(--muted);
      font-size: 0.98rem;
      margin: 0 auto 24px;
      max-width: 440px;
    }}
    .err-actions {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 12px;
    }}
    .err-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      min-height: 44px;
      padding: 11px 20px;
      border-radius: var(--radius-md);
      font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
      font-size: 0.94rem;
      font-weight: 700;
      text-decoration: none;
    }}
    .err-btn-primary {{
      background: var(--accent);
      color: var(--btn-fg);
      border: 1px solid var(--accent);
    }}
    .err-btn-secondary {{
      background: var(--surface);
      color: var(--text);
      border: 1px solid var(--border);
    }}
    .err-footer {{
      width: 100%;
      border-top: 1px solid var(--border);
      padding: 18px 20px;
      text-align: center;
      color: var(--muted);
      font-size: 0.84rem;
    }}
  </style>
</head>
<body>
  <header class="err-header">
    <div class="err-header-inner">
      <a href="./" class="err-brand" aria-label="{safe_comp_label} Startseite">
        {logo_html}
      </a>
      <a href="./" class="err-hdr-link">Startseite</a>
    </div>
  </header>

  <main id="main-content" class="err-main">
    <section class="err-section" aria-label="Fehlermeldung 404">
      <div class="err-card">
        <div class="err-badge">Fehler 404 · Seite nicht gefunden</div>
        <h1>Diese Seite wurde nicht gefunden</h1>
        <p class="err-desc">Die aufgerufene Adresse bei {safe_comp_label} existiert nicht oder wurde verschoben. Über die Startseite gelangen Sie direkt zurück zur Übersicht.</p>
        <div class="err-actions">
          <a class="err-btn err-btn-primary" href="./">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg>
            <span>Zur Startseite</span>
          </a>
{contact_btn_html}        </div>
      </div>
    </section>
  </main>

  <footer class="err-footer">
    {safe_footer_line}
  </footer>
</body>
</html>
"""
    return _ss(html_out)


def parse_redirects_file(redirects_path: Path) -> dict[str, dict]:
    """Parst eine _redirects-Datei deterministisch (Source-Pfad ohne Trailing-Slash -> {to, status})."""
    rules: dict[str, dict] = {}
    if not redirects_path.is_file():
        return rules
    for raw_line in redirects_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        raw_src, raw_dst = parts[0].strip(), parts[1].strip()
        status = 301
        if len(parts) >= 3:
            try:
                status = int(parts[2].strip())
            except ValueError:
                status = 301
        norm_src = "/" + raw_src.lstrip("/").rstrip("/") if raw_src != "/" else "/"
        if not norm_src:
            norm_src = "/"
        rules[norm_src] = {"to": raw_dst, "status": status}
    return dict(sorted(rules.items(), key=lambda kv: kv[0]))


def sync_edge_tenant_redirects(base_dir: Path | None = None) -> dict:
    """
    Liest alle <folder>/_redirects-Dateien im Repo ein und erzeugt sortiert
    functions/lib/tenant_redirects.js fuer Cloudflare Pages Edge-Middleware.
    """
    root = Path(base_dir) if base_dir else BASE_DIR
    all_redirects: dict[str, dict] = {}
    for redir_file in sorted(root.glob("*/_redirects")):
        folder = redir_file.parent.name
        if folder.startswith("."):
            continue
        parsed = parse_redirects_file(redir_file)
        if parsed:
            all_redirects[folder] = parsed

    out_path = root / "functions" / "lib" / "tenant_redirects.js"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    js_body = (
        "// Auto-generated by scripts/webpilot_seo_geo_autopilot.py (--sync-redirects). Do not edit manually.\n"
        f"export const TENANT_REDIRECTS = {json.dumps(all_redirects, ensure_ascii=False, indent=2, sort_keys=True)};\n"
    )
    changed = (not out_path.is_file()) or (out_path.read_text(encoding="utf-8", errors="ignore") != js_body)
    if changed:
        out_path.write_text(js_body, encoding="utf-8")
    return {
        "ok": True,
        "folders": sorted(all_redirects.keys()),
        "rules_count": sum(len(v) for v in all_redirects.values()),
        "changed": changed,
        "path": str(out_path),
    }


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
        if not p.name.lower().startswith("cockpit") and p.name.lower() != "404.html"
    )
    public_page_count = sum(
        1 for p in html_files
        if not p.name.lower().startswith(("cockpit", "team-update", "onboarding", "404"))
    )

    pages_intel = []
    combined_src_to_alt = {}
    total_imgs_updated = 0
    total_dims_added = 0
    total_heroes_upgraded = 0
    total_forms_webmcp = 0
    total_fields_enriched = 0
    total_honeypots_detached = 0
    total_summary_headings_fixed = 0
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

        # 2a. Hero-LCP (fetchpriority="high") & lokale Pixelmasse (width/height + lazy)
        working_html, img_perf_stats = upgrade_images_lcp_and_dimensions(working_html, site_dir)
        total_dims_added += img_perf_stats["dims_added"]
        total_heroes_upgraded += img_perf_stats["hero_upgraded"]

        # 2b. Autofill, Honeypot-Entkopplung (form="wpTrapDetached") & deklaratives WebMCP
        working_html, form_stats = enrich_forms_autofill_and_webmcp(working_html, profile, hf.name)
        total_forms_webmcp += form_stats["forms_webmcp"]
        total_fields_enriched += form_stats["fields_enriched"]
        total_honeypots_detached += form_stats["honeypots_detached"]

        # 2c. FAQ-Semantik (<summary> ohne <h1..h6>) & WCAG-2.2 Skip-to-Content
        working_html, sum_fixed = sanitize_faq_details_headings(working_html)
        total_summary_headings_fixed += sum_fixed
        working_html = inject_skip_to_content(working_html, hf.name)

        has_step3_wizard = bool(
            re.search(r'\bid=(["\'])wpStep3\1', working_html, flags=re.I)
            and re.search(r'\bwp-step-pane\b', working_html)
        )

        # 3. <head> idempotent ausstatten (dateModified nur erneuern, wenn echter Differenz-Bedarf besteht)
        dm_m = re.search(r'"dateModified":\s*"([^"]+)"', raw_html)
        existing_iso = dm_m.group(1) if dm_m else iso_now

        candidate_html = _ss(
            inject_head_seo_geo(
                working_html,
                profile,
                p_info,
                existing_iso,
                page_count=public_page_count,
                has_step3_wizard=has_step3_wizard,
                site_dir=site_dir,
            )
        )

        if candidate_html != raw_html:
            final_html = _ss(
                inject_head_seo_geo(
                    working_html,
                    profile,
                    p_info,
                    iso_now,
                    page_count=public_page_count,
                    has_step3_wizard=has_step3_wizard,
                    site_dir=site_dir,
                )
            )
            hf.write_text(final_html, encoding="utf-8")
            files_modified += 1

    # 4. bilder.json mit sprechenden alt-Texten aktualisieren
    bilder_updated = update_bilder_json_alts(site_dir, profile, combined_src_to_alt)

    # 5. /llms.txt, /sitemap.xml und /robots.txt idempotent aktualisieren
    llms_path = site_dir / "llms.txt"
    if llms_path.is_file() and files_modified == 0 and bilder_updated == 0:
        old_llms = llms_path.read_text(encoding="utf-8", errors="ignore")
        hm_m = re.search(r"- \*\*Aktualisiert am:\*\* ([^\n]+)", old_llms)
        existing_human = hm_m.group(1).strip() if hm_m else human_now
        cand_llms = generate_llms_txt(profile, pages_intel, existing_human)
        if cand_llms != old_llms:
            llms_path.write_text(generate_llms_txt(profile, pages_intel, human_now), encoding="utf-8")
    else:
        llms_path.write_text(generate_llms_txt(profile, pages_intel, human_now), encoding="utf-8")

    sitemap_path = site_dir / "sitemap.xml"
    if sitemap_path.is_file() and files_modified == 0 and bilder_updated == 0:
        old_sm = sitemap_path.read_text(encoding="utf-8", errors="ignore")
        sm_m = re.search(r"<lastmod>([^<]+)</lastmod>", old_sm)
        existing_sm_iso = sm_m.group(1).strip() if sm_m else iso_now
        cand_sm = generate_sitemap_xml(profile, pages_intel, existing_sm_iso)
        if cand_sm != old_sm:
            sitemap_path.write_text(generate_sitemap_xml(profile, pages_intel, iso_now), encoding="utf-8")
    else:
        sitemap_path.write_text(generate_sitemap_xml(profile, pages_intel, iso_now), encoding="utf-8")

    robots_path = site_dir / "robots.txt"
    robots_content = generate_robots_txt(profile)
    if (not robots_path.is_file()) or robots_path.read_text(encoding="utf-8", errors="ignore") != robots_content:
        robots_path.write_text(robots_content, encoding="utf-8")

    # 6. Mandanten-gebrandete 404.html idempotent erzeugen (ausgeschlossen aus sitemap/llms.txt)
    err404_path = site_dir / "404.html"
    err404_content = generate_404_html(profile, site_dir)
    err404_modified = 0
    if (not err404_path.is_file()) or err404_path.read_text(encoding="utf-8", errors="ignore") != err404_content:
        err404_path.write_text(err404_content, encoding="utf-8")
        err404_modified = 1

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
        "error_404_modified": err404_modified,
        "imgs_alt_upgraded": total_imgs_updated,
        "imgs_dims_added": total_dims_added,
        "heroes_lcp_upgraded": total_heroes_upgraded,
        "forms_webmcp_upgraded": total_forms_webmcp,
        "fields_autofill_enriched": total_fields_enriched,
        "honeypots_detached": total_honeypots_detached,
        "summary_headings_sanitized": total_summary_headings_fixed,
        "bilder_json_updated": bilder_updated,
        "llms_txt": True,
        "sitemap_xml": True,
        "robots_txt": True,
        "error_404_html": True,
        "elapsed_ms": elapsed_ms,
        "context_action": context_action,
    }


def verify_showcase_dir(site_dir: Path) -> dict:
    """
    Prüft einen Showcase-Ordner auf 100 % Erfüllung aller SEO- & GEO-Kriterien:
    - ld+json (LocalBusiness/SportsOrganization/ProfessionalService + WebSite + FAQPage) auf jeder Inhaltsseite
    - meta-description & og:title / og:description / og:image auf jeder Inhaltsseite
    - 100 % aller <img>-Tags haben alt-Text >= 12 Zeichen
    - llms.txt, sitemap.xml, robots.txt (mit Content-Signal) & 404.html (mit noindex) vorhanden und gueltig
    - 0 Vorkommen von Eszett (\u00df)
    """
    html_files = sorted(
        p for p in site_dir.glob("*.html")
        if not p.name.lower().startswith("cockpit") and p.name.lower() != "404.html"
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
                has_faq = (
                    "FAQPage" in types
                    or site_dir.name in {"webpilot", "mxs-talent"}
                    or not re.search(r"<details\b", txt, re.I)
                )
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
    err404_f = site_dir / "404.html"

    robots_txt = robots_f.read_text(encoding="utf-8", errors="ignore") if robots_f.is_file() else ""
    err404_txt = err404_f.read_text(encoding="utf-8", errors="ignore") if err404_f.is_file() else ""

    err404_ok = (
        err404_f.is_file()
        and err404_f.stat().st_size > 200
        and "noindex" in err404_txt.lower()
        and ("\u00df" not in err404_txt and "\u1e9e" not in err404_txt)
    )
    robots_signal_ok = "Content-Signal:" in robots_txt

    files_ok = (
        llms_f.is_file() and llms_f.stat().st_size > 200
        and sitemap_f.is_file() and sitemap_f.stat().st_size > 100
        and robots_f.is_file() and robots_f.stat().st_size > 80
        and robots_signal_ok
        and err404_ok
    )
    for aux_f in (llms_f, sitemap_f, robots_f, err404_f):
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
        "err404_ok": err404_ok,
        "robots_signal_ok": robots_signal_ok,
        "eszett_hits": eszett_hits,
        "passed": ld_ok_all and meta_og_ok_all and (valid_alt_imgs == total_imgs) and files_ok and (eszett_hits == 0),
    }


def main():
    parser = argparse.ArgumentParser(description="WebPilot Auto-SEO & GEO Hintergrund-Autopilot")
    parser.add_argument("--site", "--slug", dest="site", help="Einzelner Showcase-Ordner (z. B. preview-joma oder joma)")
    parser.add_argument("--all", action="store_true", help="Alle preview-* Showcases sowie webpilot & mxs-talent im Workspace verarbeiten")
    parser.add_argument("--verify", action="store_true", help="Verifiziert alle verarbeiteten Showcases auf 100 %% SEO/GEO-Parität")
    parser.add_argument("--sync-redirects", action="store_true", help="Synchronisiert alle <folder>/_redirects nach functions/lib/tenant_redirects.js")
    args = parser.parse_args()

    if not args.site and not args.all and not args.verify and not args.sync_redirects:
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
    elif args.all or args.verify:
        target_dirs = sorted(p for p in BASE_DIR.glob("preview-*") if p.is_dir())
        for extra_name in ("webpilot", "mxs-talent"):
            extra_dir = BASE_DIR / extra_name
            if extra_dir.is_dir() and extra_dir not in target_dirs:
                target_dirs.append(extra_dir)

    if args.all or args.site:
        t_start = time.perf_counter()
        results = []
        for td in target_dirs:
            res = run_seo_geo_autopilot_for_site(td, context_action="cli")
            results.append(res)
            print(
                f"[SEO/GEO Autopilot] {res['site']:26s} | {res['schema_type']:26s} | "
                f"HTML: {res['html_files_processed']} ({res['html_files_modified']} mod) | "
                f"404: {res['error_404_modified']} | Alt+: {res['imgs_alt_upgraded']:2d} | {res['elapsed_ms']:5.1f} ms"
            )
        total_ms = round((time.perf_counter() - t_start) * 1000, 1)
        print(f"\n==> {len(results)} Showcases in {total_ms} ms erfolgreich SEO- & GEO-optimiert.")

    if args.all or args.sync_redirects or (args.site and any((td / "_redirects").is_file() for td in target_dirs)):
        red_res = sync_edge_tenant_redirects(BASE_DIR)
        print(
            f"[Edge Redirects] {len(red_res['folders'])} Mandanten ({red_res['rules_count']} Regeln) "
            f"-> functions/lib/tenant_redirects.js (changed={red_res['changed']})"
        )

    if args.verify:
        print("\n=== VERIFIKATIONS-REPORT (SEO & GEO HINTERGRUND-AUTOPILOT) ===")
        v_results = [verify_showcase_dir(td) for td in target_dirs]
        n_total = len(v_results)
        n_ld = sum(1 for r in v_results if r["ld_json_ok"])
        n_meta = sum(1 for r in v_results if r["meta_og_ok"])
        n_files = sum(1 for r in v_results if r["files_ok"])
        n_404 = sum(1 for r in v_results if r["err404_ok"])
        sum_imgs = sum(r["total_imgs"] for r in v_results)
        sum_valid_imgs = sum(r["valid_alt_imgs"] for r in v_results)
        sum_eszett = sum(r["eszett_hits"] for r in v_results)

        for r in v_results:
            status_icon = "PASS" if r["passed"] else "FAIL"
            print(
                f"  [{status_icon}] {r['site']:26s} | ld+json={str(r['ld_json_ok']):5s} | "
                f"meta/og={str(r['meta_og_ok']):5s} | imgs={r['valid_alt_imgs']:3d}/{r['total_imgs']:3d} ({r['alt_pct']:5.1f}%) | "
                f"404={str(r['err404_ok']):5s} | llms/sitemap/robots={str(r['files_ok']):5s} | ss_violation={r['eszett_hits']}"
            )

        overall_img_pct = 100.0 if sum_imgs == 0 else round((sum_valid_imgs / sum_imgs) * 100.0, 2)
        print("-" * 108)
        print(f"  ld+json (LocalBusiness/SportsOrg + WebSite + FAQPage): {n_ld} / {n_total} ({n_ld == n_total})")
        print(f"  meta-description & og:title / og:description / og:image: {n_meta} / {n_total} ({n_meta == n_total})")
        print(f"  imgs mit sprechendem SEO-alt-Text (>= 12 Zeichen):     {sum_valid_imgs} / {sum_imgs} ({overall_img_pct}%)")
        print(f"  404.html (noindex, 0 Eszett) vorhanden:                {n_404} / {n_total} ({n_404 == n_total})")
        print(f"  llms.txt & sitemap.xml & robots.txt (Content-Signal):  {n_files} / {n_total} ({n_files == n_total})")
        print(f"  Helvetischer Standard (0 Vorkommen von Eszett):        {sum_eszett} Treffer")

        if not all(r["passed"] for r in v_results):
            sys.exit(1)


if __name__ == "__main__":
    main()

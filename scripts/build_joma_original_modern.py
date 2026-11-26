#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator für die beiden neuen JOMA Solar GmbH WebPilot-Varianten:
1. preview-joma-original/  -> Echte 1:1 Original-Übernahme (https://vorschau.magnet-xs.ch/joma-original/)
2. preview-joma-modern/    -> 1:1 Struktur & Wiedererkennung + Tweak auf modern (https://vorschau.magnet-xs.ch/joma-modern/)

Regel-Konformität:
- UI-LAYOUT-RULES.md (Canary: UI-LAYOUT-2026-V1, #UI-01, #UI-02, #UI-10, #UI-13, #UI-14, #UI-16, #UI-23)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1, 100 % ss statt Eszett, 0 \u2014)
- BACKEND-DB-RULES.md (Canary: BACKEND-DB-2026-V1)
- DEPLOY-MAP.md (Canary: DEPLOY-MAP-2026-V1)
"""

from __future__ import annotations

import html
import json
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")

# --- Lucide Inline SVGs (100 % Lucide SVG Pflicht, 0 Unicode-Emojis) ---
SVG_PHONE = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
SVG_MAIL = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>'
SVG_ARROW = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>'
SVG_CHECK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
SVG_SUN = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>'
SVG_BATTERY = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="16" height="10" x="2" y="7" rx="2" ry="2"/><line x1="22" x2="22" y1="11" y2="13"/><line x1="6" x2="6" y1="11" y2="13"/><line x1="10" x2="10" y1="11" y2="13"/></svg>'
SVG_BUILDING = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="16" height="20" x="4" y="2" rx="2" ry="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M12 6h.01"/><path d="M12 10h.01"/><path d="M12 14h.01"/><path d="M16 10h.01"/><path d="M16 14h.01"/><path d="M8 10h.01"/><path d="M8 14h.01"/></svg>'
SVG_SHIELD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/></svg>'
SVG_MENU = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>'
SVG_X = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>'
SVG_MAP_PIN = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>'
SVG_SEND = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>'
SVG_PLAY = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="6 3 20 12 6 21 6 3"/></svg>'
SVG_FB = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>'
SVG_IG = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/></svg>'
SVG_LI = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/></svg>'


PARTNER_LOGOS = [
    ("Energiewende GmbH", "https://energiewende-gmbh.ch/", "images/partner-energiewende.png"),
    ("Elinag AG", "https://www.elinag.ch/", "images/partner-elinag.png"),
    ("Riedener AG", "https://riedenerag.ch/", "images/partner-riedener.png"),
    ("Zehnder Bau", "https://zehnderbau.ch/", "images/partner-zehnderbau.png"),
    ("Beni Holzbau", "https://www.beniholzbau.ch/", "images/partner-beniholzbau.png"),
    ("Stadtelektriker", "https://stadtelektriker.ch/", "images/partner-stadtelektriker.png"),
]

SYSTEMPARTNER_LOGOS = [
    ("3S Swiss Solar Solutions", "https://www.3s-solar.swiss/", "images/partner-3s-solar.png"),
    ("smart-me", "https://web.smart-me.com/", "images/partner-smart-me.png"),
    ("Sigenergy", "https://www.sigenergy.com/de", "images/partner-sigenergy.png"),
    ("Solar Manager", "https://www.solarmanager.ch/", "images/partner-solarmanager.png"),
]

MITGLIED_LOGOS = [
    ("Electrosuisse", "https://www.electrosuisse.ch/de/", "images/partner-electrosuisse.png"),
    ("EEV", "https://www.eev.ch/de", "images/partner-eev.png"),
    ("HGVW Wettingen", "https://hgvw.ch/", "images/partner-hgvw.png"),
]

TEAM_MEMBERS = [
    {
        "slot": "team_1",
        "name": "Jonathan Muggli",
        "role": "Gründer & Geschäftsführer",
        "phone": "+41 56 558 48 82",
        "phone_href": "tel:+41565584882",
        "image": "images/portrait-jonathan-muggli.jpg",
        "bio": "Mit einer Ausbildung als Elektroinstallateur EFZ, Energietechniker HF und Wirtschaftsingenieur FH bringe ich eine breite Expertise mit Fokus auf Solarenergie, ZEV-Abrechnungssysteme, Energieoptimierung in Gebäuden und Contracting mit. Neben meiner Leidenschaft für nachhaltige Energietechnologien bin ich ein engagierter Sportler, der Ausgeglichenheit beim Joggen, Bouldern und Wandern findet.",
    },
    {
        "slot": "team_2",
        "name": "Marco Keller",
        "role": "Gründer & Geschäftsführer",
        "phone": "+41 56 558 98 67",
        "phone_href": "tel:+41565589867",
        "image": "images/portrait-marco-keller.jpg",
        "bio": "Mit über einem Jahrzehnt Erfahrung in der Photovoltaikbranche und einem Abschluss als Wirtschaftsingenieur habe ich mich auf die Installation und Abwicklung von PV-Projekten spezialisiert. Als ehemaliger Produktmanager für E-Mobility und Photovoltaik sowie Absolvent eines MBA-Studiums bringe ich nicht nur fachliches Know-how, sondern auch betriebswirtschaftliche Expertise in meine selbstständige Tätigkeit ein.",
    },
    {
        "slot": "team_3",
        "name": "Tino Seiler",
        "role": "Leiter Montage und Ausführung",
        "phone": "+41 56 558 98 67",
        "phone_href": "tel:+41565589867",
        "image": "images/portrait-tino-seiler.jpg",
        "bio": "Erfahrener Elektroplaner, Elektroinstallateur und versierter Solarteur mit umfassender Expertise in der Elektrobranche. Präzise und effizient in der Umsetzung von Projekten bringe ich fundierte Erfahrung in der Solartechnik mit.",
    },
    {
        "slot": "team_4",
        "name": "Mario Grab",
        "role": "Solarmonteur",
        "phone": "+41 56 558 98 67",
        "phone_href": "tel:+41565589867",
        "image": "images/portrait-mario-grab.jpg",
        "bio": "Als gelernter Dachdecker bringt Mario Grab fundiertes Wissen über Dachaufbauten mit und ist ein fester Bestandteil unseres Teams. Durch praktische und theoretische Erfahrung kennt er sich auch mit Solartechnik bestens aus. Mit seiner zuverlässigen Art und seinem Humor trägt er sowohl zum Projekterfolg als auch zur guten Stimmung im Betrieb bei.",
    },
    {
        "slot": "team_5",
        "name": "Sascha Tsap",
        "role": "Solarmonteur",
        "phone": "+41 56 558 98 67",
        "phone_href": "tel:+41565589867",
        "image": "images/portrait-sascha-tsap.jpg",
        "bio": "Sascha Tsap ist ein erfahrener Dachdecker aus der Ukraine. Er zeichnet sich durch seine Zuverlässigkeit in der Montage aus und trägt massgeblich zum erfolgreichen Abschluss unserer Solarprojekte bei. Seine fachlichen Fähigkeiten und sein Engagement machen ihn zu einem wertvollen Teammitglied.",
    },
]

REFERENCES = [
    {
        "slot": "ref_1",
        "city": "Riniken",
        "installation": "Aufständerung Ost / West und Süd",
        "modultyp": "AIKO A470-MAH54Mw Neostar 2P",
        "size": "18.8 kWp",
        "yield": "19.7 MWh",
        "image": "images/ref-riniken-18kwp.jpg",
        "desc": "In Riniken wurde eine Photovoltaikanlage auf einem Flachdach sowie einem Blechfalzdach realisiert. Durch die Kombination der Dachflächen konnte die verfügbare Fläche optimal genutzt und die Anlage effizient ausgerichtet werden. Die Module wurden mittels Aufständerung in Ost-, West- und Südausrichtung installiert, um eine gleichmässige Stromproduktion über den gesamten Tagesverlauf zu erreichen.",
    },
    {
        "slot": "ref_2",
        "city": "Wettingen",
        "installation": "Indachsystem von 3S",
        "modultyp": "3S Indach, AIKO Modul für die Aufdachanlage",
        "size": "11.54 kWp",
        "yield": "11.0 MWh",
        "image": "images/ref-wettingen-indach.jpg",
        "desc": "An der Attenhoferstrasse in Wettingen wurde im Zuge einer Dachsanierung eine Photovoltaikanlage realisiert. Dabei kam eine Kombination aus Indach- und Aufdachsystem zum Einsatz, wodurch sich die Anlage optimal in die bestehende Dachstruktur integrieren lässt. Die Indachanlage wurde mit einem 3S-Indachsystem umgesetzt, während für die Aufdachanlage AIKO-Module verwendet wurden.",
    },
    {
        "slot": "ref_3",
        "city": "Rütihof (MFH ZEV)",
        "installation": "Flachdach Ost/West + Süd-Ausrichtung",
        "modultyp": "JA Solar JAM54D40-450/LB",
        "size": "68 × 450 Wp = 30.6 kWp",
        "yield": "31.0 MWh",
        "image": "images/ref-ruetihof-zev-30kwp.jpg",
        "desc": "Bei diesem Projekt in Rütihof wurde eine Photovoltaikanlage auf einem Mehrfamilienhaus mit Flachdach realisiert. Im Vorfeld erfolgte eine umfassende Beratung zum Eigenverbrauchsmodell (ZEV / VNB-Modell) sowie die fachliche Begleitung der Eigentümerversammlung. Die Anlage ist als ZEV (Zusammenschluss zum Eigenverbrauch) umgesetzt und mit Smart-Me Zählern ausgestattet.",
    },
    {
        "slot": "ref_4",
        "city": "Fislisbach",
        "installation": "Aufdachanlage Einfamilienhaus",
        "modultyp": "Hochleistungs-Glas-Glas-Module",
        "size": "24.0 kWp",
        "yield": "24.8 MWh",
        "image": "images/ref-fislisbach-24kwp.jpg",
        "desc": "Komplexe Dachgeometrie mit optimaler Belegung mehrerer Dachflächen, sauberer Elektrotechnik und Einbindung in das heimische Energiemanagement für maximalen Eigenverbrauch.",
    },
    {
        "slot": "ref_5",
        "city": "Schöfflisdorf",
        "installation": "Einfamilienhaus-Solaranlage",
        "modultyp": "Full-Black Solarmodule",
        "size": "14.0 kWp",
        "yield": "14.5 MWh",
        "image": "images/ref-schoefflisdorf-14kwp.jpg",
        "desc": "Ästhetische All-Black-Photovoltaikanlage inklusive Batteriespeicher und Wallbox-Vorbereitung. Von der ersten Beratung bis zur Inbetriebnahme durch JOMA Solar aus einer Hand begleitet.",
    },
    {
        "slot": "ref_6",
        "city": "Rütihof (Gewerbe)",
        "installation": "Flachdach-Grossanlage",
        "modultyp": "Ost-/West-Aufständerung",
        "size": "55.0 kWp",
        "yield": "56.2 MWh",
        "image": "images/ref-ruetihof-55kwp.jpg",
        "desc": "Leistungsstarke gewerbliche Solaranlage zur Deckung des hohen Tagesstrombedarfs direkt vor Ort, inklusive wirtschaftlicher Auslegung und normgerechter Sicherheitsabnahme.",
    },
]

FAQS_PRIVAT = [
    ("Benötige ich eine Baubewilligung für eine Solaranlage?", "JOMA Solar übernimmt für Sie die Abklärung und macht sämtliche Baueingaben."),
    ("Kann ich meine Anlage später erweitern?", "Ja, viele Systeme lassen sich erweitern – etwa durch zusätzliche Module oder einen Batteriespeicher. Eine vorausschauende Planung erleichtert spätere Anpassungen."),
    ("Lohnt sich ein Batteriespeicher für mein Haus?", "Ein Batteriespeicher erhöht den Eigenverbrauch und reduziert die Abhängigkeit vom Netz. Ob sich ein Speicher lohnt, hängt von Ihrem Verbrauchsprofil und der Anlagengrösse ab. Wir beraten Sie individuell."),
    ("Übernimmt JOMA auch die Anmeldung beim Energieversorger?", "Ja. Wir übernehmen die Koordination mit Netzbetreiber und Behörden und begleiten Sie bis zur vollständigen Inbetriebnahme."),
    ("Was kostet eine Solaranlage für ein Einfamilienhaus?", "Die Kosten hängen von Dachgrösse, Leistung und Zusatzkomponenten ab. Wir erstellen eine transparente Offerte basierend auf Ihren individuellen Anforderungen."),
    ("Was passiert bei schlechtem Wetter oder im Winter?", "Auch bei bewölktem Himmel produziert eine Solaranlage Strom, jedoch in reduzierter Menge. Die Jahresplanung berücksichtigt saisonale Schwankungen, sodass die Anlage langfristig wirtschaftlich arbeitet."),
    ("Wie lange dauert die Installation einer Solaranlage auf einem Einfamilienhaus?", "Die Montage dauert in der Regel 3 bis 5 Tage – abhängig von Dachgrösse und Systemumfang. Planung und technische Vorbereitung erfolgen im Vorfeld, damit die Installation effizient und sauber umgesetzt werden kann."),
    ("Wie lange hält eine Solaranlage?", "Moderne Photovoltaikanlagen haben eine Lebensdauer von 25 bis 30 Jahren und mehr. Hochwertige Komponenten und fachgerechte Installation tragen entscheidend zur Langlebigkeit bei."),
    ("Wie läuft die Beratung bei JOMA Solar ab?", "Die Beratung beginnt mit einer Analyse Ihrer Situation vor Ort oder anhand von Plänen. Danach erhalten Sie eine individuell ausgearbeitete Lösung mit transparenter Offerte."),
    ("Wie viel Wartung benötigt eine Solaranlage?", "Solaranlagen sind grundsätzlich wartungsarm. Eine periodische Kontrolle und Monitoring stellen sicher, dass die Anlage dauerhaft effizient arbeitet. Auf Wunsch bieten wir Servicepakete an."),
]

FAQS_GEWERBE = [
    ("Gibt es Förderungen für gewerbliche Solaranlagen?", "Förderprogramme und Einmalvergütungen sind möglich und abhängig von Standort und Anlagengrösse. Wir unterstützen Sie bei der Prüfung und Beantragung."),
    ("Ist Solarenergie für Gewerbe wirtschaftlich sinnvoll?", "Für viele Unternehmen ist Photovoltaik eine wirtschaftlich attraktive Lösung. Hoher Tagesverbrauch und grosse Dachflächen ermöglichen eine effiziente Nutzung des erzeugten Stroms."),
    ("Kann eine Anlage auf mehreren Gebäuden verteilt werden?", "Ja, grössere Projekte können standortübergreifend geplant werden. Die technische Umsetzung wird individuell auf die Infrastruktur abgestimmt."),
    ("Kann eine Solaranlage in bestehende Gebäude integriert werden?", "Ja. Anlagen können auf bestehenden Dächern oder Neubauten integriert werden. Eine technische Analyse stellt sicher, dass Statik und Infrastruktur geeignet sind."),
    ("Unterstützt JOMA auch bei Erweiterungen bestehender Anlagen?", "Ja. Bestehende Systeme können analysiert und bei Bedarf erweitert oder modernisiert werden, um Effizienz und Leistung zu steigern."),
    ("Was ist Solar Contracting?", "Beim Contracting übernimmt JOMA Planung, Finanzierung und Betrieb der Anlage. Sie nutzen den Solarstrom ohne hohe Anfangsinvestition und profitieren von kalkulierbaren Energiekosten."),
    ("Welche Wartung benötigen gewerbliche Anlagen?", "Gewerbliche Anlagen profitieren von regelmässigem Monitoring und optionalen Serviceverträgen, um Ertrag und Betriebssicherheit langfristig sicherzustellen."),
    ("Wie lange dauert ein Solarprojekt für ein Unternehmen?", "Je nach Projektumfang dauert die Planung und Umsetzung mehrere Wochen bis wenige Monate. Eine sorgfältige Koordination minimiert Betriebsunterbrüche."),
    ("Wie wird der erzeugte Strom abgerechnet?", "Der erzeugte Strom kann direkt verbraucht oder ins Netz eingespeist werden. Beim Contracting erfolgt die Abrechnung gemäss vertraglich definierter Konditionen."),
    ("Wie wirkt sich eine Solaranlage auf die Energiekosten aus?", "Eigenverbrauch senkt langfristig Stromkosten und reduziert die Abhängigkeit vom Marktpreis. Die genaue Einsparung hängt vom Verbrauchsprofil ab."),
]


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def sanitize_ch(text: str) -> str:
    """Erzwingt 100 % ss und entfernt \u2014 (#LANG-01)."""
    text = text.replace("\u00df", "ss")
    text = text.replace(".\u2014", ".—")
    text = text.replace("\u2014", "–")
    return text


def build_common_css(mode: str) -> str:
    is_modern = mode == "modern"
    link_accent = "#D64B13" if is_modern else "#E04300"
    h1_shadow = "none" if is_modern else "3px 3px 0 #FF4D00"
    h1_size = "clamp(2.65rem, 5vw, 4.5rem)" if is_modern else "clamp(3rem, 6.6vw, 5.75rem)"
    card_bg_alt = "#F7F7F8" if is_modern else "#FFFFFF"
    return f"""
    :root {{
      --bg-dark: #121212;
      --bg-dark-card: #1B1B1B;
      --bg-light: #FFFFFF;
      --bg-alt: {card_bg_alt};
      --text-main: #121212;
      --text-muted: #4B5563;
      --text-on-dark: #FFFFFF;
      --text-on-dark-muted: #D4D4D8;
      --accent: #FF4D00;
      --accent-hover: #E04300;
      --accent-link: {link_accent};
      --border-light: #E5E7EB;
      --border-dark: rgba(255, 255, 255, 0.14);
      --radius-sm: 4px;
      --radius-md: 8px;
      --maxw: 1180px;
      --font-head: 'Lexend', sans-serif;
      --font-body: 'Instrument Sans', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; overflow-x: clip; }}
    body {{
      font-family: var(--font-body);
      font-size: 16px;
      line-height: 1.6;
      color: var(--text-main);
      background: var(--bg-light);
      overflow-x: clip;
      -webkit-font-smoothing: antialiased;
    }}
    ::selection {{ background: var(--accent); color: #FFFFFF; }}
    :focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
    img {{ display: block; max-width: 100%; height: auto; }}
    a {{ color: inherit; text-decoration: none; }}

    .wrap {{
      max-width: var(--maxw);
      margin: 0 auto;
      padding: 0 24px;
      width: 100%;
    }}

    /* Header & 1-Zeilen Desktop Navigation (#UI-02) */
    .site-header {{
      position: sticky;
      top: 0;
      z-index: 900;
      background: var(--bg-dark);
      color: var(--text-on-dark);
      border-bottom: 1px solid var(--accent);
    }}
    .header-inner {{
      max-width: var(--maxw);
      margin: 0 auto;
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
    }}
    .brand-link {{
      display: inline-flex;
      align-items: center;
      flex-shrink: 0;
      min-height: 44px;
    }}
    .brand-logo {{
      height: 36px;
      width: auto;
      object-fit: contain;
    }}
    .desktop-nav {{
      display: flex;
      align-items: center;
      gap: 22px;
      flex-wrap: nowrap;
    }}
    .nav-link {{
      font-size: 15px;
      font-weight: 500;
      color: #F4F4F5;
      white-space: nowrap;
      padding: 8px 2px;
      min-height: 40px;
      display: inline-flex;
      align-items: center;
      border-bottom: 2px solid transparent;
      transition: color 0.16s ease, border-color 0.16s ease;
    }}
    .nav-link:hover, .nav-link.active {{
      color: #FFFFFF;
      border-bottom-color: var(--accent);
    }}
    .header-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex-shrink: 0;
    }}
    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 12px 20px;
      min-height: 44px;
      border-radius: var(--radius-md);
      font-family: var(--font-body);
      font-size: 15px;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      white-space: nowrap;
      transition: background-color 0.16s ease, border-color 0.16s ease, transform 0.14s ease;
    }}
    .btn-primary {{
      background: var(--accent);
      color: #FFFFFF;
    }}
    .btn-primary:hover {{
      background: var(--accent-hover);
      transform: translateY(-1px);
    }}
    .btn-outline-dark {{
      background: transparent;
      color: #FFFFFF;
      border-color: rgba(255, 255, 255, 0.35);
    }}
    .btn-outline-dark:hover {{
      border-color: #FFFFFF;
      background: rgba(255, 255, 255, 0.08);
    }}
    .btn-outline-light {{
      background: #FFFFFF;
      color: var(--text-main);
      border-color: var(--border-light);
    }}
    .btn-outline-light:hover {{
      border-color: var(--text-main);
    }}
    .nav-burger {{
      display: none;
      align-items: center;
      justify-content: center;
      width: 44px;
      height: 44px;
      border: 1px solid var(--border-dark);
      border-radius: var(--radius-md);
      background: var(--bg-dark-card);
      color: #FFFFFF;
      cursor: pointer;
    }}
    .mobile-drawer {{
      display: none;
      position: fixed;
      top: 69px;
      left: 0;
      right: 0;
      z-index: 895;
      flex-direction: column;
      gap: 4px;
      padding: 12px 24px 20px;
      background: var(--bg-dark);
      border-top: 1px solid var(--border-dark);
      border-bottom: 1px solid var(--border-dark);
      box-shadow: 0 12px 28px rgba(0, 0, 0, 0.4);
    }}
    .mobile-drawer.open {{ display: flex; }}
    .mob-link {{
      padding: 12px 6px;
      min-height: 44px;
      display: flex;
      align-items: center;
      font-size: 15px;
      font-weight: 500;
      color: #FFFFFF;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .mob-cta {{ margin-top: 12px; width: 100%; }}

    /* Typography & Sections */
    .section-dark {{
      background: var(--bg-dark);
      color: var(--text-on-dark);
      padding: 76px 0;
    }}
    .section-light {{
      background: var(--bg-light);
      color: var(--text-main);
      padding: 76px 0;
    }}
    .section-alt {{
      background: var(--bg-alt);
      color: var(--text-main);
      padding: 76px 0;
    }}
    .section-kicker {{
      font-family: var(--font-head);
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--accent-link);
      margin-bottom: 10px;
      display: block;
    }}
    .section-dark .section-kicker {{
      color: #FF783D;
    }}
    h1, h2, h3, h4 {{
      font-family: var(--font-head);
      letter-spacing: -0.015em;
      line-height: 1.08;
    }}
    .hero-section {{
      background: var(--bg-dark);
      color: var(--text-on-dark);
      padding: 56px 0 68px;
    }}
    .hero-grid {{
      display: grid;
      grid-template-columns: 1.08fr 0.92fr;
      gap: 48px;
      align-items: stretch;
    }}
    .hero-left {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 24px;
    }}
    .hero-h1 {{
      font-size: {h1_size};
      font-weight: 800;
      text-transform: uppercase;
      line-height: 1.02;
      color: #FFFFFF;
      text-shadow: {h1_shadow};
    }}
    .hero-sub {{
      font-size: 18px;
      line-height: 1.6;
      color: var(--text-on-dark-muted);
      max-width: 540px;
    }}
    .hero-cta-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 14px;
    }}
    .hero-metrics {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 12px;
      padding-top: 20px;
      border-top: 1px solid var(--border-dark);
    }}
    .metric-box {{
      background: var(--bg-dark-card);
      border: 1px solid var(--border-dark);
      border-radius: var(--radius-md);
      padding: 14px;
    }}
    .metric-val {{
      font-family: var(--font-head);
      font-size: 16px;
      font-weight: 700;
      color: #FFFFFF;
    }}
    .metric-lbl {{
      font-size: 13px;
      color: var(--text-on-dark-muted);
      margin-top: 2px;
    }}
    .hero-right {{
      display: flex;
      flex-direction: column;
      gap: 14px;
      height: 100%;
    }}
    .hero-gallery-stack {{
      display: grid;
      grid-template-rows: 1fr 1fr 1fr;
      gap: 12px;
      height: 100%;
    }}
    .hero-modern-mosaic {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      grid-template-rows: 1.35fr 1fr;
      gap: 12px;
      height: 100%;
    }}
    .hero-modern-mosaic .span-2 {{
      grid-column: 1 / -1;
    }}
    .photo-frame {{
      border-radius: var(--radius-md);
      overflow: hidden;
      background: #1F1F1F;
      border: 1px solid var(--border-dark);
      height: 100%;
      min-height: 150px;
    }}
    .photo-frame img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}

    /* Split Grids with Bottom-Edge Baseline Lock (#UI-02 / S-23) */
    .split-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 48px;
      align-items: stretch;
    }}
    .split-media {{
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border-light);
      background: #F3F4F6;
      height: 100%;
      min-height: 360px;
      position: relative;
    }}
    .split-media img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .split-content {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 20px;
    }}
    .split-h2 {{
      font-size: clamp(2rem, 3.6vw, 3rem);
      font-weight: 700;
      margin-bottom: 12px;
    }}
    .lead-p {{
      font-size: 16.5px;
      color: var(--text-muted);
      line-height: 1.65;
    }}
    .illu-box {{
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      background: #FFFFFF;
      padding: 16px;
    }}
    .illu-box img {{
      width: 100%;
      height: auto;
      object-fit: contain;
    }}
    .spec-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 8px;
    }}
    .spec-pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      font-size: 13px;
      font-weight: 600;
      background: #FFFFFF;
      border: 1px solid var(--border-light);
      color: var(--text-main);
    }}
    .video-caption-bar {{
      position: absolute;
      left: 14px;
      right: 14px;
      bottom: 14px;
      background: rgba(18, 18, 18, 0.88);
      color: #FFFFFF;
      padding: 10px 14px;
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      font-size: 13.5px;
      font-weight: 600;
    }}

    /* Bento 2x2 Dark Solutions */
    .center-head {{
      text-align: center;
      max-width: 720px;
      margin: 0 auto 44px;
    }}
    .center-head h2 {{
      font-size: clamp(2.1rem, 4vw, 3.2rem);
      font-weight: 700;
      margin-bottom: 12px;
    }}
    .bento-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 24px;
    }}
    .bento-card {{
      background: var(--bg-dark-card);
      border: 1px solid var(--border-dark);
      border-radius: var(--radius-md);
      padding: 26px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      height: 100%;
    }}
    .bento-card-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}
    .bento-icon {{
      width: 36px;
      height: 36px;
      border-radius: var(--radius-sm);
      background: rgba(255, 77, 0, 0.14);
      color: #FF783D;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .bento-card h3 {{
      font-size: 22px;
      font-weight: 600;
      color: #FFFFFF;
    }}
    .bento-card p {{
      font-size: 15px;
      color: var(--text-on-dark-muted);
      line-height: 1.6;
    }}
    .bento-link {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #FF783D;
      font-weight: 600;
      font-size: 14.5px;
      min-height: 36px;
    }}
    .bento-link:hover {{ text-decoration: underline; text-underline-offset: 3px; }}
    .bento-media {{
      margin-top: auto;
      border-radius: var(--radius-md);
      overflow: hidden;
      height: 220px;
      border: 1px solid rgba(255, 255, 255, 0.08);
      background: #141414;
    }}
    .bento-media img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}

    /* Partner, Systempartner, Mitgliedschaften */
    .partner-stack {{
      display: flex;
      flex-direction: column;
      gap: 28px;
    }}
    .partner-panel-dark {{
      background: var(--bg-dark);
      color: #FFFFFF;
      border-radius: var(--radius-md);
      padding: 36px;
    }}
    .partner-panel-light {{
      background: #FFFFFF;
      color: var(--text-main);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 36px;
    }}
    .partner-panel-title {{
      font-family: var(--font-head);
      font-size: 24px;
      font-weight: 600;
      text-align: center;
      margin-bottom: 24px;
    }}
    .logo-grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 16px;
    }}
    .logo-grid-4 {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 16px;
    }}
    .logo-tile {{
      background: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 18px 20px;
      height: 86px;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: border-color 0.16s ease, transform 0.14s ease;
    }}
    .logo-tile:hover {{
      border-color: var(--accent);
      transform: translateY(-2px);
    }}
    .logo-tile img {{
      max-height: 46px;
      max-width: 100%;
      width: auto;
      object-fit: contain;
    }}

    /* Standard Grids (Cards, Team, Referenzen) */
    .grid-2 {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 24px;
    }}
    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 24px;
    }}
    .card {{
      background: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      height: 100%;
    }}
    .card-dark {{
      background: var(--bg-dark-card);
      border: 1px solid var(--border-dark);
      border-radius: var(--radius-md);
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      height: 100%;
      color: #FFFFFF;
    }}
    .split-content .grid-2 .card h3 {{
      font-size: 18px;
      line-height: 1.25;
      min-height: 45px;
    }}
    .card-img {{
      width: 100%;
      height: 210px;
      object-fit: cover;
      border-radius: var(--radius-md);
    }}
    .team-portrait {{
      width: 100%;
      height: 290px;
      object-fit: cover;
      object-position: top center;
      border-radius: var(--radius-md);
    }}
    .card-meta-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 8px;
      padding: 12px;
      background: var(--bg-alt);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      font-size: 13.5px;
    }}
    .card-meta-lbl {{
      font-size: 12px;
      color: var(--text-muted);
      display: block;
    }}
    .card-meta-val {{
      font-weight: 600;
      color: var(--text-main);
    }}
    .card-cta {{ margin-top: auto; padding-top: 6px; }}

    /* Contact Form & Smart Inquiry */
    .contact-panel {{
      background: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 32px;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }}
    .direct-links {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      padding: 14px 16px;
      background: var(--bg-alt);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
    }}
    .direct-row {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 15px;
      font-weight: 600;
      color: var(--text-main);
      min-height: 36px;
    }}
    .direct-row:hover {{ color: var(--accent-link); }}
    .form-grid-2 {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 14px;
    }}
    .field-group {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .field-label {{
      font-size: 13px;
      font-weight: 600;
      color: var(--text-main);
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }}
    .field-input, .field-select, .field-textarea {{
      width: 100%;
      padding: 11px 14px;
      min-height: 44px;
      border: 1px solid #D1D5DB;
      border-radius: var(--radius-md);
      background: #FFFFFF;
      color: var(--text-main);
      font-family: var(--font-body);
      font-size: 16px;
    }}
    .field-input:focus, .field-select:focus, .field-textarea:focus {{
      border-color: var(--accent);
      outline: none;
    }}
    .field-input:user-invalid, .field-select:user-invalid, .field-textarea:user-invalid {{
      border-color: #DC2626 !important;
      outline: none;
    }}
    .field-textarea {{ min-height: 104px; resize: vertical; }}
    .check-row {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 14px;
      color: var(--text-muted);
      cursor: pointer;
      min-height: 36px;
    }}
    .check-row a {{
      display: inline-flex;
      align-items: center;
      min-height: 34px;
      padding: 4px 0;
    }}
    .check-row input {{
      width: 20px;
      height: 20px;
      margin-top: 2px;
      accent-color: var(--accent);
      flex-shrink: 0;
    }}
    .form-feedback {{
      display: none;
      padding: 14px 16px;
      border-radius: var(--radius-md);
      font-size: 14.5px;
      font-weight: 600;
    }}
    .form-feedback.ok {{
      display: block;
      background: #DCFCE7;
      color: #166534;
      border: 1px solid #86EFAC;
    }}
    .form-feedback.err {{
      display: block;
      background: #FEE2E2;
      color: #991B1B;
      border: 1px solid #FCA5A5;
    }}

    /* Modern 3-Step Smart Form */
    .wp-step-bar {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 8px;
    }}
    .wp-step-pill {{
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 10px 12px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-light);
      background: var(--bg-alt);
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      min-height: 44px;
    }}
    .wp-step-pill.active {{
      border-color: var(--accent);
      background: #FFF4ED;
      color: var(--text-main);
    }}
    .wp-step-num {{
      width: 22px;
      height: 22px;
      border-radius: var(--radius-sm);
      background: #E5E7EB;
      color: var(--text-main);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: 700;
      flex-shrink: 0;
    }}
    .wp-step-pill.active .wp-step-num {{
      background: var(--accent);
      color: #FFFFFF;
    }}
    .wp-step-pane {{ display: none; flex-direction: column; gap: 14px; }}
    .wp-step-pane.active {{ display: flex; }}
    .topic-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 10px;
    }}
    .topic-btn {{
      padding: 14px;
      min-height: 54px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-light);
      background: #FFFFFF;
      color: var(--text-main);
      font-family: var(--font-body);
      font-size: 14.5px;
      font-weight: 600;
      text-align: left;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .topic-btn.selected {{
      border-color: var(--accent);
      background: #FFF4ED;
    }}
    .plz-badge {{
      display: none;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      font-size: 13.5px;
      font-weight: 600;
      background: #DCFCE7;
      color: #166534;
    }}
    .plz-badge.visible {{ display: inline-flex; align-items: center; gap: 6px; }}

    /* FAQ Accordion */
    .faq-list {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      max-width: 860px;
      margin: 0 auto;
    }}
    .faq-item {{
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      background: #FFFFFF;
      padding: 18px 22px;
    }}
    .faq-item summary {{
      font-family: var(--font-head);
      font-size: 16.5px;
      font-weight: 600;
      cursor: pointer;
      list-style: none;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      min-height: 28px;
    }}
    .faq-item p {{
      margin-top: 12px;
      color: var(--text-muted);
      font-size: 15px;
      line-height: 1.65;
    }}

    /* Footer */
    .site-footer {{
      background: var(--bg-dark);
      color: #FFFFFF;
      padding: 64px 0 36px;
      border-top: 1px solid var(--border-dark);
    }}
    .footer-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr)) 1.3fr;
      gap: 36px;
      padding-bottom: 40px;
      border-bottom: 1px solid var(--border-dark);
    }}
    .footer-col h4 {{
      font-size: 14px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #A1A1AA;
      margin-bottom: 14px;
    }}
    .footer-links {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .footer-links a {{
      font-size: 14.5px;
      color: #F4F4F5;
      padding: 6px 0;
      min-height: 36px;
      display: inline-flex;
      align-items: center;
    }}
    .footer-links a:hover {{ color: #FF783D; }}
    .footer-brand-box {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-size: 14.5px;
      color: var(--text-on-dark-muted);
    }}
    .footer-brand-box a {{
      display: inline-flex;
      align-items: center;
      min-height: 36px;
      padding: 4px 0;
    }}
    .footer-bottom {{
      padding-top: 24px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      font-size: 13.5px;
      color: #A1A1AA;
    }}
    .footer-legal {{
      display: flex;
      align-items: center;
      gap: 20px;
      flex-wrap: wrap;
    }}
    .footer-legal a {{
      display: inline-flex;
      align-items: center;
      min-height: 36px;
      padding: 4px 0;
    }}
    .footer-legal a:hover {{ color: #FFFFFF; }}
    .footer-socials {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .social-btn {{
      width: 40px;
      height: 40px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-dark);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      color: #FFFFFF;
    }}
    .social-btn:hover {{ border-color: var(--accent); color: #FF783D; }}

    /* Mobile Sticky Bar (modern only, hidden on desktop and ?embed=true) */
    .mobile-sticky-bar {{ display: none; }}

    /* Subpage Hero */
    .page-hero {{
      background: var(--bg-dark);
      color: #FFFFFF;
      padding: 56px 0 60px;
    }}
    .page-hero h1 {{
      font-size: clamp(1.68rem, 4vw, 3.2rem);
      font-weight: 700;
      max-width: 820px;
      margin-bottom: 16px;
      overflow-wrap: break-word;
      hyphens: auto;
    }}
    .page-hero p {{
      font-size: 17.5px;
      color: var(--text-on-dark-muted);
      max-width: 680px;
      margin-bottom: 24px;
    }}
    .legal-box {{
      max-width: 840px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }}
    .legal-box h2 {{
      font-size: 22px;
      margin-top: 10px;
    }}
    .legal-box p {{
      color: var(--text-muted);
      line-height: 1.7;
    }}

    @media (max-width: 1023px) {{
      .desktop-nav, .header-actions {{ display: none; }}
      .nav-burger {{ display: inline-flex; }}
      .hero-grid, .split-grid, .bento-grid, .grid-2, .grid-3, .footer-grid {{
        grid-template-columns: 1fr;
      }}
      .hero-gallery-stack {{
        grid-template-rows: auto;
        grid-template-columns: 1fr;
      }}
      .hero-modern-mosaic {{
        grid-template-columns: 1fr 1fr;
        grid-template-rows: auto;
      }}
      .logo-grid-3, .logo-grid-4 {{
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }}
      .split-media {{ min-height: 260px; }}
      .hero-metrics {{ grid-template-columns: 1fr; }}
    }}

    @media (max-width: 768px) {{
      .section-dark, .section-light, .section-alt {{ padding: 48px 0; }}
      .hero-section {{ padding: 36px 0 48px; }}
      .form-grid-2, .wp-step-bar, .topic-grid {{ grid-template-columns: 1fr; }}
      .contact-panel {{ padding: 20px; }}
      .partner-panel-dark, .partner-panel-light {{ padding: 22px; }}
      body.has-sticky-bar .site-footer {{ padding-bottom: 104px; }}
      body.has-sticky-bar .mobile-sticky-bar {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        position: fixed;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 880;
        padding: 10px 14px calc(10px + env(safe-area-inset-bottom, 0px));
        background: rgba(18, 18, 18, 0.96);
        border-top: 1px solid var(--border-dark);
      }}
    }}
    @media (prefers-reduced-motion: no-preference) {{
      @view-transition {{ navigation: auto; }}
    }}
    """


def render_header(active_page: str, mode: str) -> str:
    nav_items = [
        ("privatkunden.html", "Privatkunden"),
        ("gewerbekunden.html", "Geschäftskunden"),
        ("referenzen.html", "Referenzen"),
        ("team.html", "Team"),
        ("jobs.html", "Jobs"),
        ("index.html#kontakt", "Kontakt"),
    ]
    desk_links = "\n".join(
        f'          <a href="{href}" class="nav-link{" active" if active_page == href else ""}">{esc(label)}</a>'
        for href, label in nav_items
    )
    mob_links = "\n".join(
        f'        <a href="{href}" class="mob-link">{esc(label)}</a>'
        for href, label in nav_items
    )
    phone_btn = (
        f'<a href="tel:+41565589867" class="btn btn-outline-dark">{SVG_PHONE}<span>056 558 98 67</span></a>'
        if mode == "modern"
        else ""
    )
    return f"""  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-link" aria-label="JOMA Solar GmbH Startseite">
        <img src="images/logo.svg" alt="Logo JOMA Solar GmbH" class="brand-logo" data-slot="brand_logo">
      </a>
      <nav class="desktop-nav" aria-label="Hauptnavigation">
{desk_links}
      </nav>
      <div class="header-actions">
        {phone_btn}
        <a href="index.html#kontakt" class="btn btn-primary">Beratung anfordern</a>
      </div>
      <button type="button" class="nav-burger" id="navBurger" aria-label="Menü öffnen" aria-expanded="false">
        {SVG_MENU}
      </button>
    </div>
  </header>
  <div class="mobile-drawer" id="mobileDrawer">
{mob_links}
    <a href="index.html#kontakt" class="btn btn-primary mob-cta">Beratung anfordern</a>
  </div>"""


def render_footer(mode: str) -> str:
    sticky_bar = ""
    if mode == "modern":
        sticky_bar = f"""
  <div class="mobile-sticky-bar" id="mobileStickyBar">
    <a href="tel:+41565589867" class="btn btn-outline-dark">{SVG_PHONE}<span>Anrufen</span></a>
    <a href="index.html#kontakt" class="btn btn-primary">{SVG_SEND}<span>Beratung</span></a>
  </div>"""
    return f"""  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-col">
          <h4>Privatkunden</h4>
          <div class="footer-links">
            <a href="privatkunden.html">Solaranlage für EFH / MFH</a>
            <a href="privatkunden.html#batteriespeicher">Batteriespeicher</a>
            <a href="privatkunden.html#vorgehen">Unser Vorgehen</a>
            <a href="referenzen.html">Referenzen</a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Geschäftskunden</h4>
          <div class="footer-links">
            <a href="gewerbekunden.html">Gewerbeanlagen</a>
            <a href="gewerbekunden.html#speicher">Speicher &amp; Eigenverbrauch</a>
            <a href="gewerbekunden.html#grossanlagen">Grossanlagen</a>
            <a href="gewerbekunden.html#contracting">Contracting Modell</a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Unternehmen</h4>
          <div class="footer-links">
            <a href="team.html">Team</a>
            <a href="jobs.html">Jobs</a>
            <a href="index.html#kontakt">Kontakt</a>
          </div>
        </div>
        <div class="footer-brand-box">
          <img src="images/logo.svg" alt="JOMA Solar GmbH" class="brand-logo" style="align-self:flex-start;">
          <div data-slot="footer_company"><strong>JOMA Solar GmbH</strong><br>Tägerhardstrasse 90<br>5430 Wettingen</div>
          <a href="tel:+41565589867" data-slot="phone">Tel: +41 (0)56 558 98 67</a>
          <a href="mailto:info@joma-solar.ch" data-slot="email">info@joma-solar.ch</a>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="footer-legal">
          <span data-slot="footer_copyright">© 2026 JOMA Solar GmbH</span>
          <a href="datenschutz.html">Datenschutzerklärung</a>
          <a href="impressum.html">Impressum</a>
        </div>
        <div class="footer-socials">
          <a href="https://www.facebook.com/profile.php?id=61557713833298" target="_blank" rel="noopener noreferrer" class="social-btn" aria-label="JOMA Solar auf Facebook">{SVG_FB}</a>
          <a href="https://www.instagram.com/joma_solar/" target="_blank" rel="noopener noreferrer" class="social-btn" aria-label="JOMA Solar auf Instagram">{SVG_IG}</a>
          <a href="https://www.linkedin.com/company/joma-solar-gmbh/posts/?feedView=all" target="_blank" rel="noopener noreferrer" class="social-btn" aria-label="JOMA Solar auf LinkedIn">{SVG_LI}</a>
        </div>
      </div>
    </div>
  </footer>{sticky_bar}"""


def render_common_scripts(mode: str, client_slug: str) -> str:
    return f"""  <script>
    (function() {{
      var burger = document.getElementById('navBurger');
      var drawer = document.getElementById('mobileDrawer');
      if (burger && drawer) {{
        burger.addEventListener('click', function() {{
          var open = drawer.classList.toggle('open');
          burger.setAttribute('aria-expanded', open ? 'true' : 'false');
        }});
      }}
      if (window.location.search.indexOf('embed=true') !== -1) {{
        document.body.classList.remove('has-sticky-bar');
      }}
    }})();

    function wpSelectTopic(topic, btn) {{
      var inp = document.getElementById('wpSelectedTopic');
      if (inp) inp.value = topic;
      var btns = document.querySelectorAll('.topic-btn');
      for (var i = 0; i < btns.length; i++) {{
        btns[i].classList.remove('selected');
      }}
      if (btn) btn.classList.add('selected');
    }}

    function wpGoStep(step) {{
      var panes = document.querySelectorAll('.wp-step-pane');
      var pills = document.querySelectorAll('.wp-step-pill');
      for (var i = 0; i < panes.length; i++) {{
        panes[i].classList.toggle('active', panes[i].getAttribute('data-step') === String(step));
      }}
      for (var j = 0; j < pills.length; j++) {{
        pills[j].classList.toggle('active', pills[j].getAttribute('data-step-btn') === String(step));
      }}
    }}

    function wpUpdatePlzBadge() {{
      var locEl = document.getElementById('contactLoc');
      var badge = document.getElementById('wpPlzBadge');
      if (!locEl || !badge) return;
      var val = (locEl.value || '').trim();
      var m = val.match(/^(\\d{{4}})/);
      if (m) {{
        var p = m[1].charAt(0);
        if (['4','5','6','8'].indexOf(p) !== -1) {{
          badge.textContent = 'Direkt im JOMA Einsatzgebiet (Aargau & Umgebung)';
          badge.classList.add('visible');
          return;
        }}
      }}
      badge.classList.remove('visible');
    }}

    (function() {{
      var nameEl = document.getElementById('contactName');
      if (nameEl) {{
        nameEl.addEventListener('input', function() {{
          if (document.getElementById('wpStep3') && !document.getElementById('wpStep3').classList.contains('active')) {{
            wpGoStep(3);
          }}
        }});
      }}
    }})();

    function wpSubmitJomaLead(e) {{
      if (e) e.preventDefault();
      var form = document.getElementById('jomaContactForm');
      var okBox = document.getElementById('wpFormOk');
      var errBox = document.getElementById('wpFormErr');
      if (okBox) okBox.className = 'form-feedback';
      if (errBox) errBox.className = 'form-feedback';

      var hp = (document.getElementById('wpHoneypot') && document.getElementById('wpHoneypot').value || '').trim();
      if (hp) {{
        if (okBox) {{ okBox.textContent = 'Vielen Dank. Wir melden uns so schnell wie möglich.'; okBox.className = 'form-feedback ok'; }}
        return false;
      }}

      var name = (document.getElementById('contactName').value || '').trim();
      var street = (document.getElementById('contactStreet').value || '').trim();
      var loc = (document.getElementById('contactLoc').value || '').trim();
      var phone = (document.getElementById('contactPhone').value || '').trim();
      var email = (document.getElementById('contactEmail').value || '').trim();
      var topicEl = document.getElementById('wpSelectedTopic') || document.getElementById('contactProjectType');
      var topic = (topicEl && topicEl.value || 'Beratung / Allgemeine Anfrage').trim();
      var msg = (document.getElementById('contactMessage').value || '').trim();
      var consent = document.getElementById('contactConsent');

      if (!name || !email || (consent && !consent.checked)) {{
        if (document.getElementById('wpStep3')) wpGoStep(3);
        if (errBox) {{
          errBox.textContent = 'Bitte füllen Sie Name, E-Mail-Adresse und die Datenschutz-Bestätigung aus.';
          errBox.className = 'form-feedback err';
        }}
        return false;
      }}

      var btn = document.getElementById('wpSubmitBtn');
      if (btn) btn.disabled = true;

      fetch('/api/lead-submit', {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json' }},
        body: JSON.stringify({{
          client_slug: '{client_slug}',
          preview_safe_mode: true,
          name: name,
          email: email,
          phone: phone,
          street: street,
          location: loc,
          topic: topic,
          message: msg
        }})
      }})
      .then(function(r) {{ return r.json().catch(function() {{ return {{ ok: r.ok }}; }}); }})
      .then(function() {{
        if (btn) btn.disabled = false;
        if (okBox) {{
          okBox.textContent = 'Vielen Dank. Ihre Anfrage wurde im Vorschau-Modus erfolgreich geprüft.';
          okBox.className = 'form-feedback ok';
        }}
        if (form) form.reset();
      }})
      .catch(function() {{
        if (btn) btn.disabled = false;
        if (errBox) {{
          errBox.textContent = 'Es ist ein Fehler aufgetreten. Bitte prüfen Sie Ihre Angaben.';
          errBox.className = 'form-feedback err';
        }}
      }});
      return false;
    }}
  </script>"""


def wrap_page(title: str, desc: str, active_page: str, body_html: str, mode: str, client_slug: str) -> str:
    body_cls = ' class="has-sticky-bar"' if mode == "modern" else ""
    doc = f"""<!DOCTYPE html>
<html lang="de-CH" data-design-mode="evolution" data-expected-hero-polarity="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-XSS-Protection" content="1; mode=block">
  <meta name="referrer" content="no-referrer">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&amp;family=Lexend:wght@500;600;700;800&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <style>
{build_common_css(mode)}
  </style>
</head>
<body{body_cls}>
{render_header(active_page, mode)}
  <main>
{body_html}
  </main>
{render_footer(mode)}
{render_common_scripts(mode, client_slug)}
</body>
</html>"""
    return sanitize_ch(doc)


def render_contact_form_section(mode: str) -> str:
    if mode == "original":
        form_inner = f"""          <form id="jomaContactForm" onsubmit="return wpSubmitJomaLead(event)" toolname="joma_solar_beratung" tooldescription="Anfrage für Photovoltaik, Batteriespeicher oder Contracting bei JOMA Solar GmbH senden" novalidate>
            <input type="text" id="wpHoneypot" name="website_url" tabindex="-1" autocomplete="off" form="wpTrapDetached" style="display:none;" aria-hidden="true">
            <div class="field-group">
              <label for="contactName" class="field-label">Vollständiger Name *</label>
              <input type="text" id="contactName" name="name" autocomplete="name" class="field-input" placeholder="Vor- und Nachname" required>
            </div>
            <div class="form-grid-2" style="margin-top:12px;">
              <div class="field-group">
                <label for="contactStreet" class="field-label">Strasse</label>
                <input type="text" id="contactStreet" name="street" autocomplete="street-address" class="field-input" placeholder="Strasse und Nr.">
              </div>
              <div class="field-group">
                <label for="contactLoc" class="field-label">PLZ / Ort</label>
                <input type="text" id="contactLoc" name="location" autocomplete="postal-code" class="field-input" placeholder="5430 Wettingen">
              </div>
            </div>
            <div class="form-grid-2" style="margin-top:12px;">
              <div class="field-group">
                <label for="contactPhone" class="field-label">Telefon</label>
                <input type="tel" id="contactPhone" name="phone" autocomplete="tel" class="field-input" placeholder="+41 56 000 00 00">
              </div>
              <div class="field-group">
                <label for="contactEmail" class="field-label">E-Mail-Adresse *</label>
                <input type="email" id="contactEmail" name="email" autocomplete="email" class="field-input" placeholder="name@beispiel.ch" required>
              </div>
            </div>
            <div class="field-group" style="margin-top:12px;">
              <label for="contactProjectType" class="field-label">Projektart</label>
              <select id="contactProjectType" name="topic" class="field-select">
                <option value="">Bitte wählen...</option>
                <option value="Privatkunde – Einfamilienhaus">Privatkunde – Einfamilienhaus</option>
                <option value="Privatkunde – Mehrfamilienhaus">Privatkunde – Mehrfamilienhaus</option>
                <option value="Geschäftskunde – Gewerbe / Industrie">Geschäftskunde – Gewerbe / Industrie</option>
                <option value="Batteriespeicher">Batteriespeicher</option>
                <option value="Contracting-Modell">Contracting-Modell</option>
                <option value="Beratung / Allgemeine Anfrage">Beratung / Allgemeine Anfrage</option>
              </select>
            </div>
            <div class="field-group" style="margin-top:12px;">
              <label for="contactMessage" class="field-label">Ihre Nachricht</label>
              <textarea id="contactMessage" name="message" class="field-textarea" placeholder="Beschreiben Sie kurz Ihr Gebäude oder Vorhaben..."></textarea>
            </div>
            <label class="check-row" style="margin-top:14px;">
              <input type="checkbox" id="contactConsent" required>
              <span>Ich stimme der <a href="datenschutz.html" style="color:var(--accent-link);text-decoration:underline;">Datenschutzerklärung</a> zu.</span>
            </label>
            <button type="submit" id="wpSubmitBtn" class="btn btn-primary" style="width:100%;margin-top:16px;">{SVG_SEND}<span>Anfrage senden</span></button>
          </form>"""
    else:
        form_inner = f"""          <form id="jomaContactForm" onsubmit="return wpSubmitJomaLead(event)" toolname="joma_solar_beratung" tooldescription="3-Schritte Smart-Anfrage für Photovoltaik, Speicher oder Contracting bei JOMA Solar GmbH senden" novalidate>
            <input type="text" id="wpHoneypot" name="website_url" tabindex="-1" autocomplete="off" form="wpTrapDetached" style="display:none;" aria-hidden="true">
            <input type="hidden" id="wpSelectedTopic" name="topic" value="Privatkunde – Einfamilienhaus">
            <div class="wp-step-bar">
              <button type="button" class="wp-step-pill active" data-step-btn="1" onclick="wpGoStep(1)"><span class="wp-step-num">1</span><span>Projektart</span></button>
              <button type="button" class="wp-step-pill" data-step-btn="2" onclick="wpGoStep(2)"><span class="wp-step-num">2</span><span>Standort</span></button>
              <button type="button" class="wp-step-pill" data-step-btn="3" onclick="wpGoStep(3)"><span class="wp-step-num">3</span><span>Kontakt</span></button>
            </div>

            <div class="wp-step-pane active" id="wpStep1" data-step="1" style="margin-top:14px;">
              <div class="topic-grid">
                <button type="button" class="topic-btn selected" onclick="wpSelectTopic('Privatkunde – Einfamilienhaus', this); wpGoStep(2);">{SVG_SUN}<span>Einfamilienhaus (EFH)</span></button>
                <button type="button" class="topic-btn" onclick="wpSelectTopic('Privatkunde – Mehrfamilienhaus / ZEV', this); wpGoStep(2);">{SVG_BUILDING}<span>Mehrfamilienhaus / ZEV</span></button>
                <button type="button" class="topic-btn" onclick="wpSelectTopic('Batteriespeicher & Solar Manager', this); wpGoStep(2);">{SVG_BATTERY}<span>Batteriespeicher</span></button>
                <button type="button" class="topic-btn" onclick="wpSelectTopic('Geschäftskunde – Gewerbe / Contracting', this); wpGoStep(2);">{SVG_SHIELD}<span>Gewerbe &amp; Contracting</span></button>
              </div>
              <button type="button" class="btn btn-primary" onclick="wpGoStep(2)" style="width:100%;"><span>Weiter zum Standort</span>{SVG_ARROW}</button>
            </div>

            <div class="wp-step-pane" id="wpStep2" data-step="2" style="margin-top:14px;">
              <div class="form-grid-2">
                <div class="field-group">
                  <label for="contactStreet" class="field-label">Strasse &amp; Nr.</label>
                  <input type="text" id="contactStreet" name="street" autocomplete="street-address" class="field-input" placeholder="Musterstrasse 12">
                </div>
                <div class="field-group">
                  <label for="contactLoc" class="field-label">PLZ / Ort</label>
                  <input type="text" id="contactLoc" name="location" autocomplete="postal-code" class="field-input" placeholder="5430 Wettingen" oninput="wpUpdatePlzBadge()">
                </div>
              </div>
              <div id="wpPlzBadge" class="plz-badge">{SVG_CHECK}<span>Direkt im JOMA Einsatzgebiet</span></div>
              <div class="field-group">
                <label for="contactMessage" class="field-label">Kurze Projekt-Notiz (optional)</label>
                <textarea id="contactMessage" name="message" class="field-textarea" placeholder="z. B. Flachdach, Wärmepumpe oder E-Auto geplant..."></textarea>
              </div>
              <div class="form-grid-2">
                <button type="button" class="btn btn-outline-light" onclick="wpGoStep(1)">Zurück</button>
                <button type="button" class="btn btn-primary" onclick="wpGoStep(3)"><span>Weiter zu Schritt 3</span>{SVG_ARROW}</button>
              </div>
            </div>

            <div class="wp-step-pane" id="wpStep3" data-step="3" style="margin-top:14px;">
              <div class="field-group">
                <label for="contactName" class="field-label">Vollständiger Name *</label>
                <input type="text" id="contactName" name="name" autocomplete="name" class="field-input" placeholder="Vor- und Nachname" required>
              </div>
              <div class="form-grid-2">
                <div class="field-group">
                  <label for="contactPhone" class="field-label">Telefon</label>
                  <input type="tel" id="contactPhone" name="phone" autocomplete="tel" class="field-input" placeholder="+41 56 000 00 00">
                </div>
                <div class="field-group">
                  <label for="contactEmail" class="field-label">E-Mail-Adresse *</label>
                  <input type="email" id="contactEmail" name="email" autocomplete="email" class="field-input" placeholder="name@beispiel.ch" required>
                </div>
              </div>
              <label class="check-row">
                <input type="checkbox" id="contactConsent" required>
                <span>Ich stimme der <a href="datenschutz.html" style="color:var(--accent-link);text-decoration:underline;">Datenschutzerklärung</a> zu.</span>
              </label>
              <div class="form-grid-2">
                <button type="button" class="btn btn-outline-light" onclick="wpGoStep(2)">Zurück</button>
                <button type="submit" id="wpSubmitBtn" class="btn btn-primary">{SVG_SEND}<span>Beratung anfordern</span></button>
              </div>
            </div>
          </form>"""

    sec_cls = "section-alt" if mode == "modern" else "section-light"
    return f"""    <section class="{sec_cls}" id="kontakt">
      <div class="wrap">
        <div class="split-grid">
          <div class="split-media">
            <img src="images/kontakt-frau-sofa.webp" alt="Unkomplizierte Solar-Anfrage bei JOMA Solar GmbH" data-slot="kontakt_img">
          </div>
          <div class="contact-panel">
            <div>
              <span class="section-kicker" data-slot="kontakt_kicker">Direkter Kontakt</span>
              <h2 class="split-h2" style="margin-bottom:8px;" data-slot="kontakt_heading">Kontaktieren Sie uns.</h2>
              <p class="lead-p" data-slot="kontakt_sub">Lassen Sie uns über Ihr Solarprojekt sprechen.</p>
            </div>
            <div class="direct-links">
              <a href="mailto:info@joma-solar.ch?subject=Anfrage%20%C3%BCber%20Website" class="direct-row" data-slot="kontakt_email">{SVG_MAIL}<span>info@joma-solar.ch</span></a>
              <a href="tel:+41565589867" class="direct-row" data-slot="kontakt_marco">{SVG_PHONE}<span>Marco Keller – 056 558 98 67</span></a>
              <a href="tel:+41565584882" class="direct-row" data-slot="kontakt_jonathan">{SVG_PHONE}<span>Jonathan Muggli – 056 558 48 82</span></a>
            </div>
{form_inner}
            <div id="wpFormOk" class="form-feedback"></div>
            <div id="wpFormErr" class="form-feedback"></div>
          </div>
        </div>
      </div>
    </section>"""


def build_index(mode: str) -> str:
    if mode == "modern":
        hero_right = """          <div class="hero-right">
            <div class="hero-modern-mosaic">
              <div class="photo-frame span-2">
                <img src="images/hero-aerial-2.jpg" alt="Realisierte Photovoltaikanlage von JOMA Solar aus der Luft" data-slot="hero_img_1">
              </div>
              <div class="photo-frame">
                <img src="images/hero-aerial-1.jpg" alt="Solaranlage Einfamilienhaus im Kanton Aargau" data-slot="hero_img_2">
              </div>
              <div class="photo-frame">
                <img src="images/hero-aerial-3.jpg" alt="Dachanlage mit sauberer Modulbelegung" data-slot="hero_img_3">
              </div>
            </div>
          </div>"""
        hero_extra = """            <div class="hero-cta-row">
              <a href="#kontakt" class="btn btn-primary">Beratung anfordern</a>
              <a href="referenzen.html" class="btn btn-outline-dark">Referenzen ansehen</a>
            </div>
            <div class="hero-metrics">
              <div class="metric-box">
                <div class="metric-val">5430 Wettingen</div>
                <div class="metric-lbl">Regionaler Fachbetrieb AG</div>
              </div>
              <div class="metric-box">
                <div class="metric-val">EFH bis Gewerbe</div>
                <div class="metric-lbl">Planung, Montage &amp; ZEV</div>
              </div>
              <div class="metric-box">
                <div class="metric-val">Schweizer Handel</div>
                <div class="metric-lbl">Abgesicherte Markenqualität</div>
              </div>
            </div>"""
    else:
        hero_right = """          <div class="hero-right">
            <div class="hero-gallery-stack">
              <div class="photo-frame">
                <img src="images/hero-aerial-1.jpg" alt="Solaranlage Einfamilienhaus im Aargau" data-slot="hero_img_1">
              </div>
              <div class="photo-frame">
                <img src="images/hero-aerial-2.jpg" alt="Photovoltaik Dachanlage Region Baden" data-slot="hero_img_2">
              </div>
              <div class="photo-frame">
                <img src="images/hero-aerial-3.jpg" alt="JOMA Solar Referenzanlage aus der Vogelperspektive" data-slot="hero_img_3">
              </div>
            </div>
          </div>"""
        hero_extra = """            <div class="hero-cta-row">
              <a href="#kontakt" class="btn btn-primary">Beratung anfordern</a>
            </div>"""

    partner_tiles = "\n".join(
        f'              <a href="{esc(url)}" target="_blank" rel="noopener noreferrer" class="logo-tile" aria-label="{esc(name)}"><img src="{img}" alt="{esc(name)} Logo"></a>'
        for name, url, img in PARTNER_LOGOS
    )
    sys_tiles = "\n".join(
        f'              <a href="{esc(url)}" target="_blank" rel="noopener noreferrer" class="logo-tile" aria-label="{esc(name)}"><img src="{img}" alt="{esc(name)} Logo"></a>'
        for name, url, img in SYSTEMPARTNER_LOGOS
    )
    mit_tiles = "\n".join(
        f'              <a href="{esc(url)}" target="_blank" rel="noopener noreferrer" class="logo-tile" aria-label="{esc(name)}"><img src="{img}" alt="{esc(name)} Logo"></a>'
        for name, url, img in MITGLIED_LOGOS
    )

    umbricht_cls = "section-alt" if mode == "modern" else "section-light"
    umbricht_pills = (
        f"""            <div class="spec-pills">
              <span class="spec-pill">{SVG_MAP_PIN}<span>Untersiggenthal AG</span></span>
              <span class="spec-pill">{SVG_SHIELD}<span>Kernzone abgestimmt</span></span>
              <span class="spec-pill">{SVG_SUN}<span>Eigenverbrauch optimiert</span></span>
            </div>"""
        if mode == "modern"
        else ""
    )

    return f"""    <section class="hero-section">
      <div class="wrap">
        <div class="hero-grid">
          <div class="hero-left">
            <div>
              <span class="section-kicker" data-slot="hero_kicker">JOMA Solar GmbH · Wettingen AG</span>
              <h1 class="hero-h1" data-slot="hero_title">Solar<br>einfach<br>effizient</h1>
            </div>
            <p class="hero-sub" data-slot="hero_lead">Solar- und Batteriesysteme, von der persönlichen Beratung über die Planung bis zur fachgerechten Installation. Zuverlässig umgesetzt. Nachhaltig gedacht.</p>
{hero_extra}
          </div>
{hero_right}
        </div>
      </div>
    </section>

    <section class="section-light">
      <div class="wrap">
        <div class="split-grid">
          <div class="split-media">
            <img src="images/team-gruppe-hero.jpg" alt="Das JOMA Solar Team aus Wettingen" data-slot="prozess_team_img">
          </div>
          <div class="split-content">
            <div>
              <span class="section-kicker" data-slot="prozess_kicker">Ablauf &amp; Betreuung</span>
              <h2 class="split-h2" data-slot="prozess_heading">Ihr Projekt.<br>Unser Prozess.</h2>
              <p class="lead-p" data-slot="prozess_text">Wir begleiten Sie Schritt für Schritt – transparent geplant, fachgerecht umgesetzt und langfristig betreut.</p>
            </div>
            <div class="illu-box">
              <img src="images/customer-journey-illu.png" alt="Fünf Schritte Ihres Solarprojekts bei JOMA Solar: Beratung, Planung, Installation, Speicher und langfristiges Monitoring" data-slot="prozess_illu_img">
            </div>
            <div>
              <a href="privatkunden.html#vorgehen" class="btn btn-primary">Mehr über den Ablauf</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="{umbricht_cls}">
      <div class="wrap">
        <div class="split-grid">
          <div class="split-content">
            <div>
              <span class="section-kicker" data-slot="umbricht_kicker">Praxisbeispiel aus der Region</span>
              <h2 class="split-h2" data-slot="umbricht_heading">Gemeinsam zur passenden Lösung</h2>
              <p class="lead-p" data-slot="umbricht_p1">Für das Projekt von Wein &amp; Gemüse Umbricht in Untersiggenthal stand die Optimierung des Eigenverbrauchs im Mittelpunkt. Gleichzeitig stellte die Lage des Gebäudes in der Kernzone besondere Anforderungen an Planung und Umsetzung.</p>
              <p class="lead-p" style="margin-top:12px;" data-slot="umbricht_p2">Dank der frühzeitigen Abstimmung mit der Gemeinde und einer durchdachten Projektierung konnte eine Lösung realisiert werden, die sowohl technisch als auch gestalterisch überzeugt.</p>
              <p class="lead-p" style="margin-top:12px;" data-slot="umbricht_p3">Erfahren Sie im Projektbericht mehr über die Umsetzung und die Zusammenarbeit mit JOMA Solar.</p>
{umbricht_pills}
            </div>
            <div>
              <a href="referenzen.html" class="btn btn-outline-light">{SVG_PLAY}<span>Referenzprojekte ansehen</span></a>
            </div>
          </div>
          <div class="split-media">
            <img src="images/umbricht-video-poster.jpg" alt="Referenzprojekt Wein &amp; Gemüse Umbricht in Untersiggenthal" data-slot="umbricht_img">
            <div class="video-caption-bar">
              <span>Wein &amp; Gemüse Umbricht · Untersiggenthal</span>
              <span>Kernzonen-PV</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section-dark">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker" data-slot="solutions_kicker">Privat- &amp; Geschäftskunden</span>
          <h2 data-slot="solutions_heading">Durchdachte Energielösungen</h2>
          <p class="lead-p" style="color:var(--text-on-dark-muted);" data-slot="solutions_sub">Qualitativ hochwertige Solar- und Speichersysteme. Individuell geplant für Privat- und Geschäftskunden in der Region.</p>
        </div>
        <div class="bento-grid">
          <article class="bento-card">
            <div class="bento-card-top">
              <h3 data-slot="bento_1_title">Solaranlage für EFH / MFH</h3>
              <span class="bento-icon">{SVG_SUN}</span>
            </div>
            <p data-slot="bento_1_text">Eigenverbrauch optimieren und Energieflüsse jederzeit nachvollziehen. Mit unserem Partner Solar Manager haben Sie stets volle Kontrolle.</p>
            <a href="privatkunden.html" class="bento-link">weitere Infos {SVG_ARROW}</a>
            <div class="bento-media">
              <img src="images/solarmanager-app.jpg" alt="Solar Manager App zur Eigenverbrauchssteuerung" data-slot="bento_1_img">
            </div>
          </article>

          <article class="bento-card">
            <div class="bento-card-top">
              <h3 data-slot="bento_2_title">Qualität &amp; Serviceversprechen</h3>
              <span class="bento-icon">{SVG_SHIELD}</span>
            </div>
            <p data-slot="bento_2_text">Alle Komponenten perfekt aufeinander abgestimmt – für maximale Effizienz und Langlebigkeit.</p>
            <a href="privatkunden.html#serviceversprechen" class="bento-link">weitere Infos {SVG_ARROW}</a>
            <div class="bento-media">
              <img src="images/hero-aerial-2.jpg" alt="Hochwertig installierte Solaranlage auf Schweizer Wohnhaus" data-slot="bento_2_img">
            </div>
          </article>

          <article class="bento-card">
            <div class="bento-card-top">
              <h3 data-slot="bento_3_title">Batteriespeicher</h3>
              <span class="bento-icon">{SVG_BATTERY}</span>
            </div>
            <p data-slot="bento_3_text">Solarstrom speichern und gezielt nutzen – optimal abgestimmt auf Ihre Anlage.</p>
            <a href="privatkunden.html#batteriespeicher" class="bento-link">weitere Infos {SVG_ARROW}</a>
            <div class="bento-media">
              <img src="images/bento-speicher.webp" alt="Professionell installierter Batteriespeicher von JOMA Solar" data-slot="bento_3_img">
            </div>
          </article>

          <article class="bento-card">
            <div class="bento-card-top">
              <h3 data-slot="bento_4_title">Vorgehen</h3>
              <span class="bento-icon">{SVG_BUILDING}</span>
            </div>
            <p data-slot="bento_4_text">Von der Planung über die Installation bis zur langfristigen Betreuung.</p>
            <a href="privatkunden.html#vorgehen" class="bento-link">weitere Infos {SVG_ARROW}</a>
            <div class="bento-media">
              <img src="images/bento-gespraech.webp" alt="Persönliche Beratung mit JOMA Solar vor Ort" data-slot="bento_4_img">
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="section-light">
      <div class="wrap">
        <div class="partner-stack">
          <div class="partner-panel-dark">
            <h2 class="partner-panel-title" data-slot="partner_title">Partner</h2>
            <div class="logo-grid-3">
{partner_tiles}
            </div>
          </div>
          <div class="partner-panel-light">
            <h2 class="partner-panel-title" data-slot="syspartner_title">Zertifizierte Systempartner</h2>
            <div class="logo-grid-4">
{sys_tiles}
            </div>
          </div>
          <div class="partner-panel-light">
            <h2 class="partner-panel-title" data-slot="mitglied_title">Mitgliedschaften</h2>
            <div class="logo-grid-3">
{mit_tiles}
            </div>
          </div>
        </div>
      </div>
    </section>

{render_contact_form_section(mode)}"""


def build_privatkunden(mode: str) -> str:
    return f"""    <section class="page-hero">
      <div class="wrap">
        <span class="section-kicker">Privatkunden · EFH &amp; MFH</span>
        <h1 data-slot="priv_h1">Solarlösungen für Ihr Einfamilienhaus: Heute planen und morgen sparen</h1>
        <p data-slot="priv_sub">Eine Photovoltaikanlage auf dem eigenen Dach ist mehr als nur Stromerzeugung. Bei JOMA Solar planen wir ein intelligentes Energieökosystem, das mit Ihren Bedürfnissen mitwächst.</p>
        <a href="index.html#kontakt" class="btn btn-primary">Beratung anfordern</a>
      </div>
    </section>

    <section class="section-light">
      <div class="wrap">
        <div class="split-grid">
          <div class="split-content">
            <div>
              <span class="section-kicker">Vorausschauende Planung</span>
              <h2 class="split-h2" data-slot="priv_plan_h2">Vorausschauende Planung statt Standardlösung</h2>
              <p class="lead-p">Die ideale Grösse einer Solaranlage richtet sich nicht nur nach Ihrem aktuellen Stromverbrauch. Wir blicken gemeinsam mit Ihnen in die Zukunft: E-Mobilität, Wärmepumpe und intelligente Integration der Grossverbraucher werden von Anfang an eingeplant.</p>
            </div>
            <div class="grid-2">
              <div class="card"><h3>Individuelle Planung</h3><p class="lead-p">Keine Standardlösung, jedes Projekt wird individuell analysiert.</p></div>
              <div class="card"><h3>Saubere Umsetzung</h3><p class="lead-p">Fachgerechte Installation durch unser erfahrenes Team.</p></div>
              <div class="card"><h3>Hochwertige Komponenten</h3><p class="lead-p">Zuverlässige, abgestimmte Systeme für langfristige Effizienz.</p></div>
              <div class="card"><h3>Persönlicher Kontakt</h3><p class="lead-p">Direkter Ansprechpartner, auch lange nach Projektabschluss.</p></div>
            </div>
          </div>
          <div class="split-media">
            <img src="images/efh-luftbild-quartier.jpg" alt="Photovoltaikanlage auf Einfamilienhaus im Kanton Aargau" data-slot="priv_efh_img">
          </div>
        </div>
      </div>
    </section>

    <section class="section-alt" id="batteriespeicher">
      <div class="wrap">
        <div class="split-grid">
          <div class="split-media">
            <img src="images/bento-speicher.webp" alt="Batteriespeicher-System im Einfamilienhaus" data-slot="priv_speicher_img">
          </div>
          <div class="split-content">
            <div>
              <span class="section-kicker">Batteriespeicher &amp; Autarkie</span>
              <h2 class="split-h2" data-slot="priv_speicher_h2">Batteriespeicher: Ihr persönlicher Stromvorrat</h2>
              <p class="lead-p">Mit einem massgeschneiderten Batteriespeicher von JOMA Solar nutzen Sie Ihren selbst erzeugten Strom genau dann, wenn Sie ihn brauchen – am Abend, in der Nacht oder auf Wunsch mit Notstromfunktion bei Netzunterbruch.</p>
            </div>
            <div class="grid-2">
              <div class="card"><h3>Wirtschaftlichkeit</h3><p class="lead-p">Auslegung auf hohe Eigenverbrauchsoptimierung und schnelle Amortisation.</p></div>
              <div class="card"><h3>Notstrom &amp; App-Kontrolle</h3><p class="lead-p">Optionaler Netzunterbruch-Schutz und voller Überblick via Solar Manager.</p></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section-light" id="vorgehen">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">Ablauf &amp; Qualität</span>
          <h2 data-slot="priv_vorgehen_h2">Unser Vorgehen – Schritt für Schritt</h2>
          <p class="lead-p">Wir beziehen unser Installationsmaterial ausschliesslich beim Schweizer Grosshandel. Produktgarantien sind über renommierte Schweizer Grosshändler abgesichert.</p>
        </div>
        <div class="grid-3">
          <div class="card">
            <span class="section-kicker">Schritt 01</span>
            <h3>Analyse &amp; Offerte</h3>
            <p class="lead-p">Bestandesaufnahme vor Ort in der Region Baden/Aargau und individuelle Auslegung inklusive Fördergeld-Check.</p>
          </div>
          <div class="card">
            <span class="section-kicker">Schritt 02</span>
            <h3>Dachmontage &amp; Elektrik</h3>
            <p class="lead-p">Wind- und wetterfeste Montage unter Berücksichtigung der Dachstatik sowie normgerechte Elektrotechnik.</p>
          </div>
          <div class="card">
            <span class="section-kicker">Schritt 03</span>
            <h3>Inbetriebnahme &amp; Betreuung</h3>
            <p class="lead-p">Anmeldung bei Gemeinde, Energieversorger und Pronovo sowie persönliche Begleitung während der gesamten Lebensdauer.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section-dark" id="serviceversprechen">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">Qualität &amp; Serviceversprechen</span>
          <h2 data-slot="priv_service_h2">Qualität, auf die Sie sich verlassen können</h2>
          <p class="lead-p" style="color:var(--text-on-dark-muted);">Eine Solaranlage ist eine langfristige Investition. Jede Anlage wird individuell geplant und fachgerecht umgesetzt, damit sie über Jahrzehnte zuverlässig Energie liefert.</p>
        </div>
        <div class="grid-2">
          <div class="card-dark"><h3>Geprüfte Markenkomponenten</h3><p style="color:var(--text-on-dark-muted);">Abgestimmte Module, Wechselrichter und Speicher namhafter Hersteller für Schweizer Witterung.</p></div>
          <div class="card-dark"><h3>Transparente Projektabwicklung</h3><p style="color:var(--text-on-dark-muted);">Klare Kommunikation, fixe Ansprechpartner vor Ort und saubere Dokumentation.</p></div>
        </div>
      </div>
    </section>

{render_contact_form_section(mode)}"""


def build_gewerbekunden(mode: str) -> str:
    return f"""    <section class="page-hero">
      <div class="wrap">
        <span class="section-kicker">Geschäftskunden · Gewerbe &amp; Industrie</span>
        <h1 data-slot="gew_h1">Photovoltaik für Gewerbe und Industrie</h1>
        <p data-slot="gew_sub">Nutzen Sie ungenutzte Dachflächen zur Stromproduktion, senken Sie langfristig Ihre Energiekosten und machen Sie Ihr Unternehmen unabhängiger vom Strommarkt.</p>
        <a href="index.html#kontakt" class="btn btn-primary">Beratung anfordern</a>
      </div>
    </section>

    <section class="section-light" id="speicher">
      <div class="wrap">
        <div class="split-grid">
          <div class="split-content">
            <div>
              <span class="section-kicker">Wirtschaftlichkeit &amp; Speicher</span>
              <h2 class="split-h2">Batteriespeicher &amp; Eigenverbrauch im Gewerbe</h2>
              <p class="lead-p">Ein Gewerbebetrieb hat spezifische Anforderungen an die Energieversorgung. Wir planen Speichersysteme, die Lastspitzen glätten und Ihre Betriebsabläufe optimal unterstützen – inklusive Lösungen über 500 kWh für aktive Netzentlastung und Regelenergie.</p>
            </div>
            <div class="grid-2">
              <div class="card"><h3>Rendite &amp; Amortisation</h3><p class="lead-p">Detaillierte Analysen zu Amortisation, Lastprofil und Einsparpotenzial.</p></div>
              <div class="card"><h3>Skalierbare Systeme</h3><p class="lead-p">Speicherlösungen bis in den Megawattbereich, sauber eingebunden in die Industrie-Elektrik.</p></div>
            </div>
          </div>
          <div class="split-media">
            <img src="images/gewerbe-speicher-technik.jpg" alt="Gewerbliche Speicher- und Elektrotechnik von JOMA Solar" data-slot="gew_speicher_img">
          </div>
        </div>
      </div>
    </section>

    <section class="section-alt" id="grossanlagen">
      <div class="wrap">
        <div class="split-grid">
          <div class="split-media">
            <img src="images/grossanlage-gewerbe.jpg" alt="Photovoltaik-Grossanlage auf Gewerbe- und Industriehalle" data-slot="gew_gross_img">
          </div>
          <div class="split-content">
            <div>
              <span class="section-kicker">Industrie &amp; Logistik</span>
              <h2 class="split-h2">Photovoltaik-Grossanlagen strukturiert umgesetzt</h2>
              <p class="lead-p">Von der Prüfung der Dachstatik über das Netzanschlussgesuch bis zu Montage, Inbetriebnahme und langfristigem Monitoring begleiten wir Industrie-, Produktions-, Logistik-, Büro- und Landwirtschaftsbetriebe.</p>
            </div>
            <div class="grid-2">
              <div class="card"><h3>Analyse &amp; Projektplanung</h3><p class="lead-p">Dachflächen, Energiebedarf und Statik präzise berechnet.</p></div>
              <div class="card"><h3>Monitoring &amp; Betrieb</h3><p class="lead-p">Dauerhafte Überwachung für maximale Ertragssicherheit.</p></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section-dark" id="contracting">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">Solar Contracting</span>
          <h2 data-slot="gew_contr_h2">Solarstrom für Ihr Unternehmen – ohne Investition</h2>
          <p class="lead-p" style="color:var(--text-on-dark-muted);">Beim Contracting-Modell übernimmt JOMA Solar Planung, Finanzierung und Betrieb der Photovoltaikanlage. Ihr Unternehmen stellt die Dachfläche zur Verfügung und profitiert von planbaren, günstigen Stromkosten.</p>
        </div>
        <div class="grid-3">
          <div class="card-dark"><h3>Keine Investitionskosten</h3><p style="color:var(--text-on-dark-muted);">Die gesamte Finanzierung und Realisierung erfolgt ohne eigene Kapitalbindung.</p></div>
          <div class="card-dark"><h3>Betrieb &amp; Wartung inklusive</h3><p style="color:var(--text-on-dark-muted);">Monitoring, Service und Performance-Verantwortung bleiben vollständig bei JOMA Solar.</p></div>
          <div class="card-dark"><h3>Planbare Energiekosten</h3><p style="color:var(--text-on-dark-muted);">Direkte Nutzung des erzeugten Solarstroms vor Ort zu vertraglich definierten Konditionen.</p></div>
        </div>
      </div>
    </section>

    <section class="section-light">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">FAQ Gewerbe</span>
          <h2>Häufige Fragen für Unternehmen</h2>
        </div>
        <div class="faq-list">
{''.join(f'          <details class="faq-item"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>\n' for q, a in FAQS_GEWERBE)}
        </div>
      </div>
    </section>

{render_contact_form_section(mode)}"""


def build_referenzen(mode: str) -> str:
    cards = []
    for ref in REFERENCES:
        cards.append(f"""          <article class="card">
            <img src="{ref['image']}" alt="Solaranlage {esc(ref['city'])} · {esc(ref['size'])}" class="card-img" data-slot="{ref['slot']}_img">
            <h3 data-slot="{ref['slot']}_title">{esc(ref['city'])}</h3>
            <div class="card-meta-grid">
              <div><span class="card-meta-lbl">Anlagengrösse</span><span class="card-meta-val">{esc(ref['size'])}</span></div>
              <div><span class="card-meta-lbl">Jahresproduktion</span><span class="card-meta-val">{esc(ref['yield'])}</span></div>
              <div><span class="card-meta-lbl">Installation</span><span class="card-meta-val">{esc(ref['installation'])}</span></div>
              <div><span class="card-meta-lbl">Modultyp</span><span class="card-meta-val">{esc(ref['modultyp'])}</span></div>
            </div>
            <p class="lead-p" data-slot="{ref['slot']}_desc">{esc(ref['desc'])}</p>
          </article>""")
    return f"""    <section class="page-hero">
      <div class="wrap">
        <span class="section-kicker">Referenzen &amp; Kundenstimmen</span>
        <h1 data-slot="ref_h1">Realisierte Solarprojekte im Einsatz</h1>
        <p data-slot="ref_sub">Einblick in realisierte Photovoltaikanlagen für Privat- und Geschäftskunden im Kanton Aargau und der angrenzenden Region sowie Antworten auf häufige Fragen.</p>
        <a href="index.html#kontakt" class="btn btn-primary">Beratung anfordern</a>
      </div>
    </section>

    <section class="section-light" id="referenzen">
      <div class="wrap">
        <div class="grid-3">
{chr(10).join(cards)}
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">FAQ Privatkunden</span>
          <h2>Ihre Fragen – unsere Antworten</h2>
        </div>
        <div class="faq-list">
{''.join(f'          <details class="faq-item"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>\n' for q, a in FAQS_PRIVAT)}
        </div>
      </div>
    </section>

{render_contact_form_section(mode)}"""


def build_team(mode: str) -> str:
    cards = []
    for m in TEAM_MEMBERS:
        cards.append(f"""          <article class="card">
            <img src="{m['image']}" alt="{esc(m['name'])} – {esc(m['role'])}" class="team-portrait" data-slot="{m['slot']}_img">
            <div>
              <span class="section-kicker" data-slot="{m['slot']}_role">{esc(m['role'])}</span>
              <h3 style="font-size:22px;" data-slot="{m['slot']}_name">{esc(m['name'])}</h3>
            </div>
            <p class="lead-p" data-slot="{m['slot']}_bio">{esc(m['bio'])}</p>
            <div class="card-cta">
              <a href="{m['phone_href']}" class="direct-row">{SVG_PHONE}<span>{esc(m['phone'])}</span></a>
            </div>
          </article>""")
    return f"""    <section class="page-hero">
      <div class="wrap">
        <span class="section-kicker">Team · Wettingen AG</span>
        <h1 data-slot="team_h1">Gemeinsam für Ihr Projekt</h1>
        <p data-slot="team_sub">Als Team arbeiten wir Hand in Hand – von der Beratung über die Planung bis zur Umsetzung. Diese Zusammenarbeit bildet die Grundlage für Qualität, Zuverlässigkeit und nachhaltige Lösungen.</p>
      </div>
    </section>

    <section class="section-light">
      <div class="wrap">
        <div class="grid-3">
{chr(10).join(cards)}
        </div>
      </div>
    </section>

{render_contact_form_section(mode)}"""


def build_jobs(mode: str) -> str:
    return f"""    <section class="page-hero">
      <div class="wrap">
        <span class="section-kicker">Karriere bei JOMA Solar</span>
        <h1 data-slot="jobs_h1">Spontanbewerbung willkommen</h1>
        <p data-slot="jobs_sub">Aktuell ist bei uns keine Stelle ausgeschrieben. Wir sind aber immer offen für gute Leute, die Solaranlagen sauber montieren und Verantwortung übernehmen wollen.</p>
        <a href="#bewerbung" class="btn btn-primary">Spontan bewerben</a>
      </div>
    </section>

    <section class="section-light">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">Das bieten wir</span>
          <h2>Mehr als ein Job auf dem Dach</h2>
        </div>
        <div class="grid-3">
          <article class="card">
            <span class="section-kicker">01 · Team</span>
            <h3>Eingespieltes Umfeld</h3>
            <p class="lead-p">Ein junges, motiviertes Team, das dir viel Freiheit und Eigenverantwortung lässt.</p>
          </article>
          <article class="card">
            <span class="section-kicker">02 · Verantwortung</span>
            <h3>Entwicklungsspielraum</h3>
            <p class="lead-p">Raum, Verantwortung zu übernehmen und dich beruflich gezielt weiterzuentwickeln.</p>
          </article>
          <article class="card">
            <span class="section-kicker">03 · Vergütung</span>
            <h3>Faire Anstellung</h3>
            <p class="lead-p">Ein attraktiver und wettbewerbsfähiger Lohn in einem wachsenden Schweizer Fachbetrieb.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section-alt" id="bewerbung">
      <div class="wrap">
        <div class="split-grid">
          <div class="split-media">
            <img src="images/team-jonathan-marco-pv.jpg" alt="Jonathan Muggli und Marco Keller auf einer Solarbaustelle" data-slot="jobs_img">
          </div>
          <div class="contact-panel">
            <div>
              <span class="section-kicker">Direkter Kontakt für Bewerbungen</span>
              <h2 class="split-h2" style="margin-bottom:8px;">Immer offen für gute Leute</h2>
              <p class="lead-p">Wenn du im Solarbereich zuhause bist oder aus einem Handwerksberuf kommst, melde dich unkompliziert direkt bei Jonathan Muggli oder per E-Mail mit deinen Unterlagen. Es werden nur persönliche Bewerbungen berücksichtigt.</p>
            </div>
            <div class="direct-links">
              <a href="tel:+41565584882" class="direct-row">{SVG_PHONE}<span>Jonathan Muggli – 056 558 48 82</span></a>
              <a href="mailto:info@joma-solar.ch?subject=Spontanbewerbung%20JOMA%20Solar" class="direct-row">{SVG_MAIL}<span>info@joma-solar.ch</span></a>
              <div class="direct-row">{SVG_MAP_PIN}<span>JOMA Solar GmbH, Tägerhardstrasse 90, 5430 Wettingen</span></div>
            </div>
            <a href="mailto:info@joma-solar.ch?subject=Spontanbewerbung%20JOMA%20Solar" class="btn btn-primary">{SVG_SEND}<span>Unterlagen per E-Mail senden</span></a>
          </div>
        </div>
      </div>
    </section>"""


def build_impressum() -> str:
    return """    <section class="page-hero">
      <div class="wrap">
        <span class="section-kicker">Rechtliche Hinweise</span>
        <h1>Impressum</h1>
        <p>Gesetzliche Angaben gemäss Schweizer Recht für die JOMA Solar GmbH.</p>
      </div>
    </section>
    <section class="section-light">
      <div class="wrap">
        <div class="legal-box">
          <h2>Verantwortliche Stelle</h2>
          <p>JOMA Solar GmbH<br>Tägerhardstrasse 90<br>5430 Wettingen<br>Schweiz<br>E-Mail: info@joma-solar.ch<br>Website: www.joma-solar.ch</p>
          <h2>Vertretungsberechtigte Personen</h2>
          <p>Jonathan Muggli<br>Marco Keller<br>Eingetragen im Handelsregister des Kantons Aargau.<br>Handelsregisternummer: CHE-334.571.911</p>
          <h2>Haftungsausschluss</h2>
          <p>Die Inhalte unserer Website wurden mit grösstmöglicher Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte können wir jedoch keine Gewähr übernehmen. Als Diensteanbieter sind wir gemäss den allgemeinen Gesetzen für eigene Inhalte auf diesen Seiten verantwortlich.</p>
          <h2>Haftung für Links</h2>
          <p>Unsere Website kann Links zu externen Websites Dritter enthalten. Auf deren Inhalte haben wir keinen Einfluss. Deshalb können wir für diese fremden Inhalte keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich.</p>
          <h2>Urheberrechte &amp; Bildrechte</h2>
          <p>Die Inhalte, Bilder, Grafiken und Werke auf dieser Website sind Eigentum der JOMA Solar GmbH oder werden mit entsprechenden Nutzungsrechten verwendet und unterliegen dem Urheberrecht.</p>
          <h2>Kontakt</h2>
          <p>Bei Fragen zu dieser Website oder zu rechtlichen Hinweisen können Sie uns jederzeit kontaktieren: info@joma-solar.ch</p>
        </div>
      </div>
    </section>"""


def build_datenschutz() -> str:
    return """    <section class="page-hero">
      <div class="wrap">
        <span class="section-kicker">Datenschutz</span>
        <h1>Datenschutzerklärung</h1>
        <p>Informationen zur Bearbeitung von Personendaten gemäss Schweizer Datenschutzgesetz (DSG).</p>
      </div>
    </section>
    <section class="section-light">
      <div class="wrap">
        <div class="legal-box">
          <h2>1. Allgemeine Hinweise</h2>
          <p>Der Schutz Ihrer persönlichen Daten ist uns ein wichtiges Anliegen. In dieser Datenschutzerklärung informieren wir Sie darüber, welche personenbezogenen Daten wir im Zusammenhang mit der Nutzung unserer Website erheben und wie wir diese verwenden. Die Verarbeitung personenbezogener Daten erfolgt in Übereinstimmung mit dem schweizerischen Datenschutzgesetz (DSG).</p>
          <h2>2. Verantwortliche Stelle</h2>
          <p>JOMA Solar GmbH<br>Tägerhardstrasse 90<br>5430 Wettingen<br>Schweiz<br>E-Mail: info@joma-solar.ch<br>Website: www.joma-solar.ch</p>
          <h2>3. Erhebung und Verarbeitung personenbezogener Daten</h2>
          <p>Wir erheben und verarbeiten personenbezogene Daten nur, soweit dies zur Bereitstellung einer funktionsfähigen Website sowie unserer Inhalte und Leistungen erforderlich ist (Name, E-Mail-Adresse, Telefonnummer, Adresse, IP-Adresse sowie Angaben aus Ihrer Anfrage). Diese Daten werden ausschliesslich zur Bearbeitung Ihrer Anfrage verwendet.</p>
          <h2>4. Kontaktformular und Kontaktaufnahme</h2>
          <p>Wenn Sie uns über ein Kontaktformular oder per E-Mail kontaktieren, werden die von Ihnen übermittelten Daten zur Bearbeitung Ihrer Anfrage gespeichert und nicht ohne Ihre Einwilligung an Dritte weitergegeben.</p>
          <h2>5. Hosting &amp; technische Logdaten</h2>
          <p>Beim Besuch unserer Website werden technische Zugriffsdaten (IP-Adresse, Datum und Uhrzeit, Browserinformationen, aufgerufene Seiten) verarbeitet, um den sicheren und zuverlässigen Betrieb der Website zu gewährleisten.</p>
          <h2>6. Cookies und Ihre Rechte</h2>
          <p>Sie können die Speicherung von Cookies in den Einstellungen Ihres Browsers jederzeit deaktivieren oder löschen. Sie haben im Rahmen des schweizerischen Datenschutzgesetzes jederzeit das Recht auf Auskunft, Berichtigung oder Löschung Ihrer personenbezogenen Daten via info@joma-solar.ch.</p>
        </div>
      </div>
    </section>"""


def generate_variant(folder_name: str, public_slug: str, mode: str, display_label: str) -> None:
    out_dir = BASE_DIR / folder_name
    out_dir.mkdir(parents=True, exist_ok=True)

    company_json = {
        "company_name": "JOMA Solar GmbH",
        "legal_entity": "JOMA Solar GmbH",
        "name": "JOMA Solar GmbH",
        "slug": public_slug,
        "uid": "CHE-334.571.911",
        "city": "Wettingen",
        "canton": "AG",
        "street": "Tägerhardstrasse 90",
        "zip": "5430",
        "phone": "+41 56 558 98 67",
        "email": "info@joma-solar.ch",
        "website": "https://www.joma-solar.ch/",
        "partner_id": "jenny",
        "partner_name": "Jenny Ettle (JE-MI)",
        "design_mode": "original-1to1" if mode == "original" else "modern-tweak-1to1",
    }
    config_json = {
        "company_name": f"JOMA Solar GmbH · {display_label}",
        "slug": folder_name,
        "public_slug": public_slug,
        "cockpit_token": "joma2026",
        "template": "original-1to1-v1" if mode == "original" else "modern-tweak-1to1-v1",
        "partner_id": "jenny",
        "pages": [
            "index.html",
            "privatkunden.html",
            "gewerbekunden.html",
            "referenzen.html",
            "team.html",
            "jobs.html",
            "impressum.html",
            "datenschutz.html",
        ],
    }
    site_json = {
        "slug": folder_name,
        "public_slug": public_slug,
        "token": "joma2026",
        "name": f"JOMA Solar GmbH · {display_label}",
        "Updated": "2026-11-26",
        "PagesCount": 8,
        "ReferencesCount": len(REFERENCES),
        "TeamCount": len(TEAM_MEMBERS),
    }
    design_vibe_json = {
        "mode": mode,
        "primary_accent": "#FF4D00",
        "bg_dark": "#121212",
        "bg_light": "#FFFFFF",
        "font_heading": "Lexend",
        "font_body": "Instrument Sans",
    }
    visual_dna_json = {
        "schema_version": "1.0.0",
        "slug": public_slug,
        "source_url": "https://www.joma-solar.ch/",
        "design_mode": "evolution",
        "target_hero_polarity": "dark",
        "sommelier_decisions": {
            "polarity_decision": {"target_hero_polarity": "dark"}
        },
    }

    (out_dir / "company.json").write_text(json.dumps(company_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "config.json").write_text(json.dumps(config_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "site.json").write_text(json.dumps(site_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "design-vibe.json").write_text(json.dumps(design_vibe_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "source_visual_dna.json").write_text(json.dumps(visual_dna_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    pages = {
        "index.html": (
            "JOMA Solar | Solaranlagen & Batteriesysteme für Privat & Gewerbe im Aargau",
            "Solar- und Batteriesysteme der JOMA Solar GmbH in Wettingen (AG): Beratung, Planung, Installation und Service für Privat- und Geschäftskunden.",
            build_index(mode),
        ),
        "privatkunden.html": (
            "Privatkunden · Solaranlage & Batteriespeicher | JOMA Solar GmbH",
            "Photovoltaikanlagen für EFH und MFH, Batteriespeicher, unser Vorgehen und Qualitätsversprechen von JOMA Solar Wettingen.",
            build_privatkunden(mode),
        ),
        "gewerbekunden.html": (
            "Geschäftskunden · Gewerbe, Grossanlagen & Contracting | JOMA Solar GmbH",
            "Gewerbliche Photovoltaikanlagen, Batteriespeicher zur Lastspitzenglättung, Grossanlagen und Solar-Contracting ohne Investition.",
            build_gewerbekunden(mode),
        ),
        "referenzen.html": (
            "Referenzen & FAQ · Realisierte Solarprojekte | JOMA Solar GmbH",
            "Realisierte Photovoltaikanlagen im Aargau (Riniken, Wettingen, Rütihof, Fislisbach, Schöfflisdorf) sowie häufige Fragen.",
            build_referenzen(mode),
        ),
        "team.html": (
            "Team · Ihre Solarexperten in Wettingen | JOMA Solar GmbH",
            "Lernen Sie das Team der JOMA Solar GmbH kennen: Jonathan Muggli, Marco Keller, Tino Seiler, Mario Grab und Sascha Tsap.",
            build_team(mode),
        ),
        "jobs.html": (
            "Jobs & Karriere · Spontanbewerbung | JOMA Solar GmbH",
            "Arbeiten bei JOMA Solar GmbH in Wettingen: Spontanbewerbung für Solarmonteure, Dachdecker und Elektrofachleute willkommen.",
            build_jobs(mode),
        ),
        "impressum.html": (
            "Impressum | JOMA Solar GmbH",
            "Gesetzliche Angaben gemäss Schweizer Recht für die JOMA Solar GmbH, 5430 Wettingen.",
            build_impressum(),
        ),
        "datenschutz.html": (
            "Datenschutzerklärung | JOMA Solar GmbH",
            "Datenschutzerklärung der JOMA Solar GmbH in Wettingen gemäss Schweizer Datenschutzgesetz (DSG).",
            build_datenschutz(),
        ),
    }

    for fname, (ptitle, pdesc, pbody) in pages.items():
        html_str = wrap_page(ptitle, pdesc, fname, pbody, mode, public_slug)
        (out_dir / fname).write_text(html_str, encoding="utf-8")

    print(f"Generated {len(pages)} pages in {out_dir}")


if __name__ == "__main__":
    generate_variant("preview-joma-original", "joma-original", "original", "1:1 Original-Übernahme")
    generate_variant("preview-joma-modern", "joma-modern", "modern", "1:1 Modern-Tweak")

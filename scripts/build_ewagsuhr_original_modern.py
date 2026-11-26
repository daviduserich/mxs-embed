#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator für die beiden EWAG / E. Widmer AG (Suhr AG) WebPilot-Varianten:
1. preview-ewagsuhr-original/ -> Echte 1:1 Original-Übernahme (https://vorschau.magnet-xs.ch/ewagsuhr-original/)
2. preview-ewagsuhr-modern/   -> 1:1 Struktur & Wiedererkennung + Tweak auf modern (https://vorschau.magnet-xs.ch/ewagsuhr-modern/)

Regel-Konformität:
- UI-LAYOUT-RULES.md (Canary: UI-LAYOUT-2026-V1, #UI-01, #UI-02, #UI-10, #UI-13, #UI-14, #UI-16, #UI-23)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1, 100 % ss statt Eszett, 0 \\u2014)
- BACKEND-DB-RULES.md (Canary: BACKEND-DB-2026-V1)
- DEPLOY-MAP.md (Canary: DEPLOY-MAP-2026-V1)
"""

from __future__ import annotations

import html
import json
from pathlib import Path
from PIL import Image

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")

# --- Lucide Inline SVGs (100 % Lucide SVG Pflicht, 0 Unicode-Emojis) ---
SVG_PHONE = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
SVG_MAIL = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>'
SVG_ARROW = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>'
SVG_CHECK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
SVG_ZAP = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/></svg>'
SVG_SHIELD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/></svg>'
SVG_WIFI = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h.01"/><path d="M2 8.82a15 15 0 0 1 20 0"/><path d="M5 12.859a10 10 0 0 1 14 0"/><path d="M8.5 16.429a5 5 0 0 1 7 0"/></svg>'
SVG_SUN = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>'
SVG_BUILDING = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="16" height="20" x="4" y="2" rx="2" ry="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M12 6h.01"/><path d="M12 10h.01"/><path d="M12 14h.01"/><path d="M16 10h.01"/><path d="M16 14h.01"/><path d="M8 10h.01"/><path d="M8 14h.01"/></svg>'
SVG_HOME = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>'
SVG_CPU = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/></svg>'
SVG_CAR = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/></svg>'
SVG_LIGHTBULB = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>'
SVG_BRIEFCASE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/><rect width="20" height="14" x="2" y="6" rx="2"/></svg>'
SVG_CLOCK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'
SVG_MAP_PIN = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>'
SVG_MENU = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>'
SVG_SEND = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>'
SVG_USERS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
SVG_AWARD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526"/><circle cx="12" cy="8" r="6"/></svg>'

IMG_DIMS: dict[str, tuple[int, int]] = {}


def get_img_dims(folder: str, rel_img: str) -> tuple[int, int]:
    key = f"{folder}/{rel_img}"
    if key in IMG_DIMS:
        return IMG_DIMS[key]
    p = BASE_DIR / folder / rel_img
    if p.exists():
        try:
            with Image.open(p) as im:
                IMG_DIMS[key] = im.size
                return im.size
        except Exception:
            pass
    return (800, 500)


def img_tag(folder: str, rel_img: str, alt: str, cls: str = "", slot: str = "", hero: bool = False, style: str = "") -> str:
    w, h = get_img_dims(folder, rel_img)
    attrs = [f'src="{rel_img}"', f'alt="{esc(alt)}"', f'width="{w}"', f'height="{h}"']
    if cls:
        attrs.append(f'class="{cls}"')
    if slot:
        attrs.append(f'data-slot="{slot}"')
    if hero:
        attrs.append('fetchpriority="high"')
        attrs.append('decoding="async"')
    else:
        attrs.append('loading="lazy"')
        attrs.append('decoding="async"')
    if style:
        attrs.append(f'style="{style}"')
    return f"<img {' '.join(attrs)}>"


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def sanitize_ch(text: str) -> str:
    """Erzwingt 100 % ss und entfernt \\u2014 (#LANG-01)."""
    text = text.replace("\u00df", "ss")
    text = text.replace(".\u2014", ".—")
    text = text.replace("\u2014", "–")
    return text


EWAG_PILLARS = [
    ("E", "Erfahrung", "Von über 100 Jahren Erfolgsgeschichte und dem Know-how unserer teils langjährigen Mitarbeiter profitieren Sie als Kunde am meisten."),
    ("W", "Wertschätzung", "Sie erhalten unsere Wertschätzung beim Realisieren Ihrer kleineren und grösseren Wünsche für Ihren Alltag."),
    ("A", "Ausbildung", "Über 300 Lernende erlebten vier spannende Jahre der Ausbildung im Verlaufe der Jahre. Wir sind stolz auf unseren Berufsnachwuchs."),
    ("G", "Geschichte", "Seit 1925 prägt die E. Widmer AG in Suhr das Elektrohandwerk – verankert an der Tramstrasse 47 und im ganzen Raum Aarau."),
]

CHRONICLE = [
    ("1925", "Firmengründung durch Emil Widmer – Haupttätigkeit Leitungsbau und Elektrifizierung von Liegenschaften."),
    ("1939", "Bezug des heutigen Firmendomizils an der Tramstrasse 47 in Suhr."),
    ("1967", "Bernhard Widmer übernimmt die Firma von seinem Vater Emil."),
    ("1996", "Die E. Widmer AG (Elektro, Telecom, Netzwerk) wird zwecks Nachfolgeregelung neu strukturiert; Bruno Scheiber nimmt Einsitz in VR und GL."),
    ("2001", "Übernahme der Aktienmehrheit durch Bruno Scheiber nach dem Tod von Bernhard Widmer."),
    ("2003", "Umbau von Eingangsbereich und Ausstellung."),
    ("2010", "Abbruch EFH und Anbau von Magazin, Werkstatt, Büro, Schulungsraum und Kochstudio."),
    ("2017", "Übernahme der Aktien durch Sonja und Thomas Scheiber; Thomas Scheiber übernimmt die Geschäftsführung."),
    ("2025", "Jubiläum 100 Jahre E. Widmer AG und Sonderausstellung im Museum Suhr (7. September 2025 bis 7. Juni 2026)."),
]

SERVICES = [
    {
        "id": "haus-und-wohnungen",
        "title": "Haus und Wohnungen",
        "kicker": "Privatkunden",
        "icon": SVG_HOME,
        "summary": "Elektroinstallationen sind Vertrauenssache und werden vom dafür ausgebildeten Fachpersonal ausgeführt. Ihre Wünsche werden von Ihrem Haus-Elektriker kompetent erfüllt.",
        "bullets": [
            "Kunden-, Service- und Unterhaltsarbeiten",
            "Umbauarbeiten sämtlicher Stark- und Schwachstrominstallationen",
            "Neubau EFH / MFH",
            "Lichtinstallationen und Lichtsanierungen",
        ],
    },
    {
        "id": "gewerbe-und-industrie",
        "title": "Gewerbe und Industrie",
        "kicker": "Geschäftskunden",
        "icon": SVG_BUILDING,
        "summary": "Elektroinstallationen in anspruchsvollen Anlagen wie Spitälern, Apotheken, Schulen, öffentlichen Einrichtungen oder Produktionsanlagen verlangen ein hohes Mass an Fachwissen.",
        "bullets": [
            "Engineering / Elektroplanung und Neubauten",
            "Installation Heizung / Lüftung / Kälte & Kälteerzeuger",
            "Lebensmittelindustrie sowie Umbauten, Erweiterungen und Sanierungen",
            "Installation moderner Netzwerkanlagen",
        ],
    },
    {
        "id": "service-und-notfaelle",
        "title": "Service und Notfälle (24h-Pikett)",
        "kicker": "7 × 24h Bereitschaft",
        "icon": SVG_ZAP,
        "summary": "Im Notfall sind wir rund um die Uhr für unsere Kunden da. Unser Pikettteam ist unter 062 855 08 80 jederzeit erreichbar – auch an Wochenenden und Feiertagen. Kein Einsatz ist uns zu klein.",
        "bullets": [
            "Störungsbehebung und Reparaturen in EWAG-Qualität",
            "Überwachung der Wartungsintervalle",
            "Regelmässige Wartung im privaten, gewerblichen und industriellen Bereich",
            "24h-Pikettdienst über 062 855 08 80",
        ],
    },
    {
        "id": "schwachstrom-und-netzwerk",
        "title": "Schwachstrom und Netzwerk",
        "kicker": "Kommunikation & Sicherheit",
        "icon": SVG_WIFI,
        "summary": "Wir realisieren für Sie Anschlüsse in Kupfer- und Glasfasertechnik, Telefonie sowie elektronische Zutritts-, Alarm- und Brandmeldesysteme nach höchsten Sicherheitsstandards.",
        "bullets": [
            "Anschlüsse in Kupfer- und Glasfasertechnik",
            "Netzwerkverkabelung / Netzwerkschrank, TV- & Satverkabelung",
            "Telefonie und Gegensprechanlagen mit und ohne Video",
            "Zutrittskontrolle, Schliesssysteme, Brandmelde- und Alarmanlagen",
        ],
    },
    {
        "id": "gebaeudeautomation",
        "title": "Gebäudeautomation",
        "kicker": "Intelligentes Wohnen",
        "icon": SVG_CPU,
        "summary": "Mehr Sicherheit, mehr Energieeffizienz und mehr Komfort: Die Steuerung der einzelnen Komponenten erfolgt vollautomatisch oder bequem über Tablet und Smartphone.",
        "bullets": [
            "Beleuchtung: Lichtsteuerung, Lichtszenen, Schockbeleuchtung",
            "Beschattung: Storensteuerung, Multifunktions-Sensoren & Hagelschutz",
            "Raumklima (HKL), An- & Abwesenheitssimulation, Fernzugriff",
            "SPS-Steuerung und Störungsmitteilungen per SMS, Mail oder Telefon",
        ],
    },
    {
        "id": "elektroplanung",
        "title": "Elektroplanung",
        "kicker": "Von Beginn an",
        "icon": SVG_SHIELD,
        "summary": "Wir begleiten Ihren Neu- oder Umbau von Beginn an. Bereits während der Planung berücksichtigen unsere Fachkräfte Ihre Vorstellungen und entwickeln praxisorientierte Lösungen.",
        "bullets": [
            "Fachkundige Beratung und Ausschreibungen",
            "Installationspläne und Apparatepläne",
            "Elektroschemen",
            "Vollständige Revisionsunterlagen",
        ],
    },
    {
        "id": "e-mobilitaet",
        "title": "e-Mobilität",
        "kicker": "Ladelösungen",
        "icon": SVG_CAR,
        "summary": "Wir installieren Ladestationen für Ihr Zuhause, Ihr Unternehmen, Ihre Liegenschaft oder öffentlich zugängliche Parkplätze – mit intelligentem Lastmanagement.",
        "bullets": [
            "Einzelladestationen mit oder ohne Abrechnungsmöglichkeit",
            "Ladestationen für mehrere Parkplätze",
            "Lade- und Lastenmanagement",
            "Photovoltaikoptimiertes Laden",
        ],
    },
    {
        "id": "photovoltaikanlage",
        "title": "Photovoltaikanlage",
        "kicker": "Solarstrom & Speicher",
        "icon": SVG_SUN,
        "summary": "Produzieren Sie Ihren eigenen Strom, speichern Sie überschüssigen Solarstrom in einer Batterie und erhöhen Sie Ihre Energieunabhängigkeit zusammen mit unseren Partnern.",
        "bullets": [
            "Photovoltaikanlagen und Batteriespeicherlösungen",
            "Not-Stromsysteme",
            "Energiemanagementsysteme",
            "ZEV (Zusammenschluss zum Eigenverbrauch)",
        ],
    },
    {
        "id": "geraetepruefung",
        "title": "Geräteprüfung",
        "kicker": "Sicherheit am Arbeitsplatz",
        "icon": SVG_CHECK,
        "summary": "Gemäss Verordnung über die Unfallverhütung prüfen wir elektrische Arbeitsmittel im Büro, in der Werkstatt oder auf der Baustelle fachgerecht und normkonform.",
        "bullets": [
            "Festlegung individueller Prüfintervalle und Sichtprüfung",
            "Messung, Funktions- und Sicherheitsprüfung inkl. Prüfetikette",
            "Dokumentation, Auswertung und vollständige Inventarliste",
            "Reinigung sowie Reparatur defekter Geräte nach Absprache",
        ],
    },
    {
        "id": "haushaltsgeraete",
        "title": "Haushaltsgeräte",
        "kicker": "Verkauf & Reparatur",
        "icon": SVG_HOME,
        "summary": "In Zusammenarbeit mit einem ausgewählten Partner bieten wir umfassenden Service für Backofen, Steamer, Induktionskochfeld, Geschirrspüler, Kühlschrank und mehr.",
        "bullets": [
            "Beratung, Lieferung und Installation neuer Geräte",
            "Entsorgung alter Geräte",
            "Reparaturen aller Marken",
            "Ersatzgerät bei Ausfällen und 24h-Pikettdienst im Notfall",
        ],
    },
    {
        "id": "beleuchtung",
        "title": "Beleuchtung",
        "kicker": "Lichtplanung & Ausstellung",
        "icon": SVG_LIGHTBULB,
        "summary": "In unserer Ausstellung zeigen wir Ihnen moderne LED-/OLED-Beleuchtung und beraten Sie für Wohn-, Arbeits- und Aussenbereiche.",
        "bullets": [
            "LED / OLED und intelligente Lichtsteuerung",
            "Steh-, Wand-, Decken-, Hänge- und Pendel-Leuchten sowie Einbauspots",
            "Aussen-, Weg-, Hallen- und Schaufensterbeleuchtung",
            "Marken in der Ausstellung: BestLight, Neuco, Osram, RIBAG, Schönenberger, TKL, Tulux, Zumtobel",
        ],
    },
    {
        "id": "ausstellung-verkaufsladen",
        "title": "Ausstellung & Verkaufsladen",
        "kicker": "Tramstrasse 47 · Suhr",
        "icon": SVG_MAP_PIN,
        "summary": "Erleben Sie Leuchten, Sicherheitsinstallationen und Gebäudeautomation am Muster – und holen Sie Leuchtmittel, Installationsmaterial und Sicherungen direkt bei uns.",
        "bullets": [
            "Ausstellung für Beleuchtung, Sicherheit und Gebäudeautomation",
            "Verkaufsladen für Leuchtmittel, Installationsmaterial und Sicherungen",
            "Kundenparkplätze direkt vor der Eingangstüre oder hinter dem Haus",
            "Persönliche Fachberatung nach Terminvereinbarung",
        ],
    },
]

REFERENCES_EFH = [
    ("EFH Hell", "Fam. Hell · Wasserfluhweg 4, 5000 Aarau", "2015", "images/ref-efh-hell_01.jpg", "Elektroplanung, Elektroverteilung, Gaswärmepumpenanlage, Kommunikationsinstallation, Stark- und Schwachstrominstallation, Wireless LAN"),
    ("EFH Hentschel-Wälty", "Fam. R. Hentschel-Wälty · Wolfgrubenstrasse 44, 5742 Kölliken", "2015", "images/ref-efh-hentschel-waelty_01.jpg", "Elektroplanung, Elektroverteilung, Kommunikationsinstallation, Stark- und Schwachstrominstallation, Wireless LAN, Zeptrion Steuerung"),
    ("EFH Schärer", "Fam. Schärer · Signalstrasse 21, 5000 Aarau", "2015", "images/ref-efh-schaerer_01.jpg", "Audio, Brandmeldeanlage, Gebäudeautomation, Gegensprechanlage, Kommunikations- & Sicherheitsanlagen, Starkstrom, Videoüberwachung, Zutrittskontrolle"),
    ("EFH Schmid-Elsener", "Fam. Schmid-Elsener · 5034 Suhr", "2015", "images/ref-efh-schmid-elsener_01.jpg", "Elektroplanung, Gebäudeautomation, Gegensprechanlage, Kommunikationsinstallation, LED Beleuchtung, Starkstrominstallation, Zutrittskontrolle"),
]

REFERENCES_MFH = [
    ("MFH Sheng", "Sheng Immobilien · 5722 Gränichen", "2015–2016", "images/ref-mfh-sheng_01.jpg", "Elektroplanung, Elektroverteilung, Gegensprechanlage, Kommunikationsinstallation, LED Beleuchtung, Starkstrominstallation"),
    ("MFH Zopfmatte Suhr", "Genossenschaft LEBENsuhr · Mühlemattweg 18, 5034 Suhr", "2014–2016", "images/ref-mfh-zopfmatte-suhr_01.jpg", "Audio, Elektroplanung, Gebäudeautomation, Gegensprechanlage, Kommunikationsinstallation, Notlicht, Sicherheitsanlagen, Telefonanlage, Wireless LAN, Zutrittskontrolle"),
    ("MFH Lerchenweg", "Privat", "2012–2014", "images/ref-mfh-lerchenweg_01.jpg", "Elektroplanung, Elektroverteilung, Gebäudeautomation, Gegensprechanlage, Kommunikationsinstallation, Notlichtinstallation, Starkstrominstallation, Wireless LAN"),
    ("MFH Panoramastrasse", "Privat", "2012–2014", "images/ref-mfh-panoramastrasse_01.jpg", "Elektroplanung, Gegensprechanlage, Kommunikationsinstallation, Lichtsteuerung Logo, Notlichtinstallation, Starkstrominstallation, Wireless LAN"),
]

REFERENCES_GEWERBE = [
    ("Hotel Bären Suhr · Hauptverteilung", "Restaurant / Hotel Bären · 5034 Suhr", "72h Karfreitag-Einsatz", "images/film-35.jpg", "Minutiös geplanter Austausch des zentralen Nervensystems der Energieversorgung über Ostern (Start Karfreitag 06:00 Uhr): in 72 Stunden gemeinsam mit TBS und Schaltanlagen Lüscher störungsfrei in Betrieb genommen."),
    ("Zentrum für Gefässmedizin", "Zentrum für Gefässmedizin · Aarenaustrasse 2b, 5000 Aarau", "2015–2016", "images/ref-ig-zentrum-gefaessmedizin_01.jpg", "Audio, Elektroplanung, Gebäudeautomation, Gegensprechanlage, Kommunikationsinstallation, Krankenruf, Notlichtinstallation, Sicherheitsanlagen, Starkstrominstallation, Zutrittskontrolle"),
    ("Johler Gussasphalt AG", "Johler Gussasphalt AG · Römerstrasse 25, 5502 Hunzenschwil", "2012–2014", "images/ref-ig-johler-gussasphalt_01.jpg", "Elektroplanung, Gebäudeautomation, Gegensprechanlage, Kommunikationsinstallation, Notlichtinstallation, Sicherheitsanlagen, Starkstrominstallation, Telefonanlage, Wireless LAN, Zutrittskontrolle"),
]

TEAM_LEADERSHIP = [
    {"name": "Thomas Scheiber", "role": "Geschäftsführer", "phone": "062 855 08 98", "tel": "+41628550898", "email": "ts@ewagsuhr.ch", "img": "images/team-ts.jpg"},
    {"name": "Nico Knechtli", "role": "Technischer Leiter & Lehre", "phone": "062 855 08 82", "tel": "+41628550882", "email": "nk@ewagsuhr.ch", "img": "images/team-nk.jpg"},
    {"name": "Sonja Scheiber", "role": "Projekte / Geschäftsleitung", "phone": "062 855 08 80", "tel": "+41628550880", "email": "ssch@ewagsuhr.ch", "img": "images/team-ssch001.jpg"},
]

TEAM_STAFF = [
    {"name": "Urs Hürlimann", "role": "Projektleiter Service", "phone": "062 855 08 86", "email": "uh@ewagsuhr.ch", "img": "images/team-uh.jpg"},
    {"name": "Daniel Gygax", "role": "Projektleiter", "phone": "062 855 08 80", "email": "office@ewagsuhr.ch", "img": "images/team-dg.jpg"},
    {"name": "Bruno Matrascia", "role": "Projektleiter", "phone": "062 855 08 99", "email": "bm@ewagsuhr.ch", "img": "images/team-bm.jpg"},
    {"name": "Daniel Sandmeier", "role": "Projektleiter", "phone": "062 855 08 87", "email": "ds@ewagsuhr.ch", "img": "images/team-ds.jpg"},
    {"name": "Michael Deubelbeiss", "role": "Technischer Sachbearbeiter", "phone": "062 855 08 97", "email": "md@ewagsuhr.ch", "img": "images/team-mde.jpg"},
    {"name": "Cornelia Bossard", "role": "Administration", "phone": "062 855 08 80", "email": "cb@ewagsuhr.ch", "img": "images/team-cb1.jpg"},
    {"name": "Jessica Wenger", "role": "Administration", "phone": "062 855 08 80", "email": "jw@ewagsuhr.ch", "img": "images/team-wj.jpg"},
    {"name": "Adrian Hunziker", "role": "Magazin & Sicherheit KOPAS", "phone": "062 855 08 85", "email": "magazin@ewagsuhr.ch", "img": "images/team-ah.jpg"},
    {"name": "Esther Frey", "role": "Buchhaltung (smile office gmbh)", "phone": "062 855 08 83", "email": "ef@ewagsuhr.ch", "img": ""},
]

TEAM_INSTALLERS = [
    ("Daniel Battaglia", "images/team-db.jpg"),
    ("Pascal Bucher", "images/team-pb.jpg"),
    ("Cedric Christ", "images/team-cec.jpg"),
    ("Ivan Cobanovic", "images/team-ic.jpg"),
    ("Carlos Coragem", "images/team-coc.jpg"),
    ("Maik Dörfer", "images/team-md.jpg"),
    ("Arbenor Jashari", "images/team-aj.jpg"),
    ("Zoran Mijajlovic", "images/team-zm.jpg"),
    ("Lars Morgenthaler", "images/team-lm.jpg"),
    ("Sebastian Mundinger", "images/team-sm.jpg"),
    ("Rouven Müri", "images/team-mr.jpg"),
    ("Ibrahim Sawaneh", "images/team-is.jpg"),
    ("Damian Schaffner", "images/team-schdjpg.jpg"),
    ("Dominik Schaffner", "images/team-dsch.jpg"),
    ("Pablo Stierli", "images/team-ps.jpg"),
    ("Gerhard Villiger", "images/team-gv.jpg"),
    ("Serge Pfister", ""),
]

TEAM_APPRENTICES = [
    ("Nicolas Baumann", "images/team-nb1.jpg"),
    ("Luis Dommann", "images/team-dl.jpg"),
    ("Marvin Geider", "images/team-mg.jpg"),
    ("Julian Lüthy", "images/team-jlu.jpg"),
    ("Pascal Manz", "images/team-mp.jpg"),
    ("Marc Müller", "images/team-mm.jpg"),
    ("Brian Nyongesa", "images/team-nb.jpg"),
    ("Hasan Özgür", "images/team-oeh.jpg"),
    ("Nico Schärer", "images/team-ns1.jpg"),
    ("Samuel Waldvogel", "images/team-sw.jpg"),
    ("Benjamin Weber", "images/team-wb.jpg"),
]

JOBS = [
    {
        "id": "projektleiter",
        "title": "Elektroprojektleiter:in max. 100%",
        "badge": "Nachfolge / Festanstellung",
        "lead": "Aufgrund der Pensionierung eines langjährigen Projektleiters suchen wir eine unternehmerisch denkende Persönlichkeit für vielphasige Elektroprojekte.",
        "tasks": [
            "Planen, offerieren und abwickeln vielphasiger Elektroprojekte",
            "Erstellen technischer Ausführungsunterlagen und Koordinieren von Schlusskontrollen",
            "Führen des Montagepersonals und der Lernenden sowie Mitarbeit an internen Projekten",
        ],
        "profile": [
            "Elektroinstallateur:in EFZ mit Weiterbildung Elektroprojektleiter:in Installation und Sicherheit oder langjähriger Erfahrung",
            "Freude am Führen von Mitarbeitenden und Interesse, neue Ideen einzubringen",
        ],
        "offer": "Eigenverantwortliche Projektleitung, internes und externes Schulungsangebot, modern ausgerüsteter Arbeitsplatz, Firmenauto (Privatnutzung möglich) sowie bis zu 7 Wochen Ferien.",
        "contact": "Auskunft: Nico Knechtli (062 855 08 82, nk@ewagsuhr.ch) · Bewerbung an Thomas Scheiber (ts@ewagsuhr.ch)",
        "topic_value": "Bewerbung: Elektroprojektleiter:in max. 100%",
    },
    {
        "id": "elektroinstallateur",
        "title": "Elektroinstallateur:in EFZ / Montageelektriker:in EFZ",
        "badge": "Per sofort / nach Vereinbarung",
        "lead": "Selbstständige Montagearbeiten auf spannenden Wohn-, Gewerbe- und Industriebaustellen rund um Suhr und Aarau.",
        "tasks": [
            "Korrekte und saubere Montage aller Elektroinstallationen auf der Baustelle",
            "Führen der zugeteilten Lernenden sowie Vermittlung von Fachkenntnissen und Softskills",
            "Bereitschaft zur Mitarbeit an betriebsinternen Projekten",
        ],
        "profile": [
            "Abgeschlossene Lehre als Elektroinstallateur:in EFZ oder Montageelektriker:in EFZ",
            "Qualitätsbewusstsein, sauberes Auftreten und Freundlichkeit im Kundenkontakt",
        ],
        "offer": "Praxisorientierte Einführung im 45-köpfigen EWAG-Team, eigenes gut ausgerüstetes Firmenauto (Privatnutzung möglich), familienfreundliche Arbeitszeiten und bis zu 7 Wochen Ferien.",
        "contact": "Bewerbung per E-Mail an bewerbung@ewagsuhr.ch (Thomas Scheiber & Nico Knechtli)",
        "topic_value": "Bewerbung: Elektroinstallateur:in EFZ / Montageelektriker:in EFZ",
    },
    {
        "id": "servicemonteur",
        "title": "Servicemonteur:in / Elektroinstallateur:in EFZ",
        "badge": "Per sofort",
        "lead": "Zur Erweiterung unseres Teams suchen wir eine kommunikative Fachperson für vielseitige Servicearbeiten bei unserer Stammkundschaft.",
        "tasks": [
            "Servicearbeiten bei Stammkunden inklusive Kundenberatung und Materialbestellung",
            "Fachmännische Arbeitsausführung und technische Abklärungen",
            "Mitarbeit bei der praktischen Lehrlingsausbildung",
        ],
        "profile": [
            "Abgeschlossene Berufslehre als Elektromonteur / Elektroinstallateur EFZ",
            "Gute Schema- und Plankenntnisse, Fahrausweis Kat. B und Freude am Kundenkontakt",
        ],
        "offer": "Abwechslungsreicher Arbeitsplatz im breiten Kundensegment, eigenes Firmenauto (Privatnutzung möglich), Weiterbildungen und bis zu 7 Wochen Ferien.",
        "contact": "Auskunft: Urs Hürlimann (062 855 08 86, uh@ewagsuhr.ch) · Bewerbung an bewerbung@ewagsuhr.ch",
        "topic_value": "Bewerbung: Servicemonteur:in / Elektroinstallateur:in EFZ",
    },
    {
        "id": "lehrstelle",
        "title": "Lehrstelle 2027 · Elektroinstallateur:in / Montageelektriker:in EFZ",
        "badge": "Ausbildung & Schnupperwoche",
        "lead": "Über 300 Lernende haben bei uns bereits ihr Handwerk gelernt. Starte im Sommer 2027 mit Praxisbezug, starkem Teamrückhalt und Sportler-Lehrstellen-Option.",
        "tasks": [
            "Erlernen der korrekten und sauberen Montage aller Elektroinstallationen auf der Baustelle",
            "Unverbindliche Schnupperwoche zum Kennenlernen des Berufsalltags möglich",
        ],
        "profile": [
            "Sekundar- oder Bezirksschule (bzw. Sekundar-/Berufsschule) mit guten Noten in Mathematik und Physik",
            "Interesse an technischen Zusammenhängen, Teamgeist und freundliches Auftreten",
        ],
        "offer": "Praxisorientierte Ausbildung durch das ganze EWAG-Team, abwechslungsreiche Kundenprojekte sowie bis zu 7 Wochen Ferien.",
        "contact": "Ausbildungsverantwortlicher: Nico Knechtli (062 855 08 82, nk@ewagsuhr.ch)",
        "topic_value": "Lehrstelle EFZ / Schnupperwoche anfragen",
    },
]


def build_common_css(mode: str) -> str:
    is_modern = mode == "modern"
    page_bg = "#F4F7FB" if is_modern else "#E7E7E7"
    hero_bg = "#F4F7FB" if is_modern else "#FFFFFF"
    alt_bg = "#F4F7FB" if is_modern else "#F8FAFC"
    header_bg = "#FFFFFF"
    nav_bar_bg = "#00508E"
    return f"""
    :root {{
      --ewag-blue: #00508E;
      --ewag-blue-bright: #006EC7;
      --ewag-blue-dark: #003A68;
      --ewag-ice: #EEF5FC;
      --bg-page: {page_bg};
      --bg-hero: {hero_bg};
      --bg-light: #FFFFFF;
      --bg-alt: {alt_bg};
      --text-main: #0F172A;
      --text-muted: #475569;
      --text-on-dark: #FFFFFF;
      --text-on-dark-muted: #DCE8F5;
      --accent: #00508E;
      --accent-hover: #003A68;
      --accent-link: #00508E;
      --border-light: #DCE3EC;
      --border-dark: rgba(255, 255, 255, 0.18);
      --radius-sm: 4px;
      --radius-md: 8px;
      --maxw: 1160px;
      --font-head: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-body: 'Inter', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; overflow-x: clip; interpolate-size: allow-keywords; }}
    body {{
      font-family: var(--font-body);
      font-size: 16px;
      line-height: 1.6;
      color: var(--text-main);
      background: var(--bg-page);
      overflow-x: clip;
      -webkit-font-smoothing: antialiased;
    }}
    ::selection {{ background: var(--ewag-blue); color: #FFFFFF; }}
    :focus-visible {{ outline: 2px solid var(--ewag-blue-bright); outline-offset: 2px; }}
    img {{ display: block; max-width: 100%; height: auto; }}
    a {{ color: inherit; text-decoration: none; text-underline-offset: 3px; }}

    .wrap {{
      max-width: var(--maxw);
      margin: 0 auto;
      padding: 0 24px;
      width: 100%;
    }}

    /* Header & 1-Zeilen Desktop Nav (#UI-02 / S-22) */
    .site-header {{
      position: sticky;
      top: 0;
      z-index: 900;
      background: {header_bg};
      border-bottom: 1px solid var(--border-light);
      box-shadow: 0 2px 10px rgba(0, 58, 104, 0.06);
    }}
    .orig-topband {{
      background: #FFFFFF;
      border-bottom: 1px solid var(--border-light);
    }}
    .orig-topband-inner {{
      max-width: var(--maxw);
      margin: 0 auto;
      padding: 10px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
    }}
    .orig-brand-meta {{
      display: flex;
      align-items: center;
      gap: 20px;
      flex-wrap: nowrap;
      white-space: nowrap;
      font-size: 14.5px;
      font-weight: 600;
      color: var(--ewag-blue);
    }}
    .orig-navband {{
      background: {nav_bar_bg};
      color: #FFFFFF;
    }}
    .orig-navband-inner {{
      max-width: var(--maxw);
      margin: 0 auto;
      padding: 0 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }}
    .orig-nav-links {{
      display: flex;
      align-items: center;
      gap: 4px;
      flex-wrap: nowrap;
    }}
    .orig-nav-link {{
      color: #FFFFFF;
      font-size: 15px;
      font-weight: 500;
      padding: 0 16px;
      line-height: 1.2;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      height: 42px;
      transition: background-color 0.16s ease;
    }}
    .orig-nav-link:hover, .orig-nav-link.active {{
      background: #1B75C7;
      color: #FFFFFF;
    }}
    .orig-pikett-chip {{
      color: #FFFFFF;
      font-size: 13.5px;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.12);
    }}
    .orig-pikett-chip:hover {{ background: rgba(255, 255, 255, 0.22); }}

    .header-inner {{
      max-width: var(--maxw);
      margin: 0 auto;
      padding: 10px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 18px;
    }}
    .brand-link {{
      display: inline-flex;
      align-items: center;
      flex-shrink: 0;
      min-height: 44px;
    }}
    .brand-logo {{
      height: 44px;
      width: auto;
      object-fit: contain;
    }}
    .desktop-nav {{
      display: flex;
      align-items: center;
      gap: 18px;
      flex-wrap: nowrap;
    }}
    .nav-link {{
      font-size: 14.5px;
      font-weight: 600;
      color: var(--text-main);
      white-space: nowrap;
      padding: 8px 2px;
      min-height: 40px;
      display: inline-flex;
      align-items: center;
      border-bottom: 2px solid transparent;
      transition: color 0.16s ease, border-color 0.16s ease;
    }}
    .nav-link:hover, .nav-link.active {{
      color: var(--ewag-blue);
      border-bottom-color: var(--ewag-blue);
    }}
    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 11px 18px;
      min-height: 44px;
      border-radius: var(--radius-md);
      font-family: var(--font-body);
      font-size: 14.5px;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      white-space: nowrap;
      transition: background-color 0.16s ease, border-color 0.16s ease, color 0.16s ease;
    }}
    .btn-primary {{
      background: var(--ewag-blue);
      color: #FFFFFF;
    }}
    .btn-primary:hover {{
      background: var(--ewag-blue-dark);
    }}
    .btn-outline-light {{
      background: #FFFFFF;
      color: var(--ewag-blue);
      border-color: var(--ewag-blue);
    }}
    .btn-outline-light:hover {{
      background: var(--ewag-ice);
    }}
    .btn-outline-dark {{
      background: transparent;
      color: #FFFFFF;
      border-color: rgba(255, 255, 255, 0.45);
    }}
    .btn-outline-dark:hover {{
      background: rgba(255, 255, 255, 0.12);
      border-color: #FFFFFF;
    }}

    .nav-burger {{
      display: none;
      align-items: center;
      justify-content: center;
      width: 44px;
      height: 44px;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      background: #FFFFFF;
      color: var(--ewag-blue);
      cursor: pointer;
    }}
    .mobile-drawer {{
      display: none;
      position: fixed;
      top: 66px;
      left: 0;
      right: 0;
      z-index: 895;
      flex-direction: column;
      gap: 4px;
      padding: 12px 24px 20px;
      background: #FFFFFF;
      border-top: 1px solid var(--border-light);
      border-bottom: 1px solid var(--border-light);
      box-shadow: 0 12px 28px rgba(15, 23, 42, 0.14);
    }}
    .mobile-drawer.open {{ display: flex; }}
    .mob-link {{
      padding: 12px 4px;
      min-height: 44px;
      display: flex;
      align-items: center;
      font-size: 15px;
      font-weight: 600;
      color: var(--text-main);
      border-bottom: 1px solid var(--border-light);
    }}
    .mob-cta {{ margin-top: 10px; width: 100%; }}

    /* Typography, Pure Left-Aligned Kicker (#UI-01) */
    .section-kicker {{
      font-family: var(--font-head);
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--ewag-blue-bright);
      margin-bottom: 8px;
      display: block;
    }}
    .section-blue .section-kicker {{
      color: #BFDBFE;
    }}
    h1, h2, h3, h4 {{
      font-family: var(--font-head);
      letter-spacing: -0.015em;
      line-height: 1.15;
    }}
    .section-light {{
      background: var(--bg-light);
      padding: 64px 0;
    }}
    .section-alt {{
      background: var(--bg-alt);
      padding: 64px 0;
      border-top: 1px solid var(--border-light);
      border-bottom: 1px solid var(--border-light);
    }}
    .section-blue {{
      background: var(--ewag-blue);
      color: #FFFFFF;
      padding: 64px 0;
    }}
    .center-head {{
      max-width: 720px;
      margin: 0 auto 38px;
      text-align: center;
    }}
    .center-head h2 {{
      font-size: clamp(1.75rem, 3.2vw, 2.5rem);
      font-weight: 700;
      margin-bottom: 12px;
      color: var(--ewag-blue);
    }}
    .section-blue .center-head h2 {{ color: #FFFFFF; }}
    .lead-p {{
      font-size: 16px;
      line-height: 1.65;
      color: var(--text-muted);
    }}

    /* Original 1:1 Stage + 3-Col Welcome */
    .orig-stage-wrap {{
      background: var(--bg-light);
      padding: 24px 0 0;
    }}
    .orig-stage-card {{
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      overflow: hidden;
      background: #FFFFFF;
    }}
    .orig-stage-img {{
      width: 100%;
      height: 390px;
      object-fit: cover;
    }}
    .orig-stage-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      padding: 16px 22px;
      background: #F8FAFC;
      border-top: 1px solid var(--border-light);
    }}
    .orig-stage-bar h1 {{
      font-size: clamp(1.5rem, 2.8vw, 2.15rem);
      color: var(--ewag-blue);
      font-weight: 700;
    }}
    .orig-3col {{
      display: grid;
      grid-template-columns: 1.35fr 0.95fr 0.95fr;
      gap: 28px;
      align-items: stretch;
    }}
    .orig-col-box {{
      background: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 16px;
    }}
    .orig-col-box h2 {{
      font-size: 21px;
      color: var(--ewag-blue);
      margin-bottom: 10px;
    }}
    .orig-job-list {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .orig-job-link {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      padding: 11px 12px;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      background: #F8FAFC;
      color: var(--ewag-blue);
      font-weight: 600;
      font-size: 14px;
      min-height: 44px;
    }}
    .orig-job-link:hover {{
      background: var(--ewag-ice);
      border-color: var(--ewag-blue);
    }}

    /* Modern Light Hero with Bottom-Edge Baseline Lock (#UI-02 / S-23) */
    .hero-modern {{
      background: var(--bg-hero);
      padding: 48px 0 56px;
      border-bottom: 1px solid var(--border-light);
    }}
    .hero-grid {{
      display: grid;
      grid-template-columns: 1.06fr 0.94fr;
      gap: 44px;
      align-items: stretch;
    }}
    .hero-left {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 22px;
    }}
    .hero-h1 {{
      font-size: clamp(2.25rem, 4.2vw, 3.45rem);
      font-weight: 800;
      line-height: 1.06;
      color: var(--ewag-blue);
    }}
    .hero-sub {{
      font-size: 17px;
      line-height: 1.62;
      color: var(--text-muted);
      max-width: 560px;
    }}
    .hero-cta-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 12px;
    }}
    .hero-metrics {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 12px;
    }}
    .metric-box {{
      background: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 14px;
    }}
    .metric-val {{
      font-family: var(--font-head);
      font-size: 16px;
      font-weight: 700;
      color: var(--ewag-blue);
      font-variant-numeric: tabular-nums;
    }}
    .metric-lbl {{
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 2px;
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
      border: 1px solid var(--border-light);
      background: #E2E8F0;
      height: 100%;
      min-height: 155px;
    }}
    .photo-frame img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}

    /* Split Grids (Bottom-Edge Baseline Lock) */
    .split-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 44px;
      align-items: stretch;
    }}
    .split-media {{
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border-light);
      background: #FFFFFF;
      height: 100%;
      min-height: 320px;
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
      background: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 28px;
    }}
    .split-h2 {{
      font-size: clamp(1.65rem, 3vw, 2.35rem);
      font-weight: 700;
      color: var(--ewag-blue);
      margin-bottom: 10px;
    }}

    /* Cards & Uniform Grids */
    .grid-2 {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 20px;
    }}
    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 20px;
    }}
    .grid-4 {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 16px;
    }}
    .card {{
      background: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      height: 100%;
    }}
    .card-blue {{
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.22);
      border-radius: var(--radius-md);
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      height: 100%;
    }}
    .card-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}
    .card-icon {{
      width: 36px;
      height: 36px;
      border-radius: var(--radius-sm);
      background: var(--ewag-ice);
      color: var(--ewag-blue);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .card h3 {{
      font-size: 18.5px;
      font-weight: 700;
      color: var(--ewag-blue);
    }}
    .card-cta {{
      margin-top: auto;
      padding-top: 8px;
    }}
    .card-cta a:not(.btn), .orig-col-box a:not(.btn), .clean-list a:not(.btn) {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-height: 40px;
      padding: 4px 0;
    }}
    @media (min-width: 1024px) {{
      .card-title-2line {{ min-height: 46px; }}
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      font-size: 12px;
      font-weight: 700;
      background: var(--ewag-ice);
      color: var(--ewag-blue);
      width: fit-content;
    }}
    .clean-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 7px;
      color: var(--text-muted);
      font-size: 14.5px;
    }}
    .clean-list li {{
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }}
    .clean-list svg {{
      color: var(--ewag-blue);
      flex-shrink: 0;
      margin-top: 3px;
    }}

    /* Reference & Team Photos */
    .ref-img {{
      width: 100%;
      aspect-ratio: 16 / 9;
      object-fit: cover;
      border-radius: var(--radius-sm);
    }}
    .team-portrait {{
      width: 100%;
      aspect-ratio: 3 / 2;
      object-fit: cover;
      object-position: center 20%;
      border-radius: var(--radius-sm);
    }}
    .roster-grid {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 14px;
    }}
    .roster-card {{
      background: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .roster-card img {{
      width: 100%;
      aspect-ratio: 3 / 2;
      object-fit: cover;
      object-position: center 20%;
      border-radius: var(--radius-sm);
    }}
    .roster-name {{
      font-size: 14.5px;
      font-weight: 700;
      color: var(--text-main);
    }}

    /* Forms (Standard Original + 3-Step Smart Modern) */
    .contact-panel {{
      max-width: 820px;
      margin: 0 auto;
      background: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 30px;
      box-shadow: 0 8px 24px rgba(0, 58, 104, 0.06);
    }}
    .form-grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }}
    .field {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .field label {{
      font-size: 13.5px;
      font-weight: 600;
      color: var(--text-main);
    }}
    .field input, .field select, .field textarea {{
      width: 100%;
      padding: 11px 13px;
      min-height: 44px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-light);
      background: #FFFFFF;
      font-family: var(--font-body);
      font-size: 15px;
      color: var(--text-main);
    }}
    .field input:user-invalid, .field select:user-invalid, .field textarea:user-invalid {{
      border-color: #DC2626 !important;
      outline: none;
    }}
    .field textarea {{ min-height: 110px; resize: vertical; }}
    .check-row {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 13.5px;
      color: var(--text-muted);
      min-height: 36px;
    }}
    .check-row input {{
      width: 18px;
      height: 18px;
      accent-color: var(--ewag-blue);
      flex-shrink: 0;
    }}
    .form-feedback {{
      display: none;
      padding: 13px 16px;
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
      border-color: var(--ewag-blue);
      background: var(--ewag-ice);
      color: var(--ewag-blue);
    }}
    .wp-step-num {{
      width: 22px;
      height: 22px;
      border-radius: var(--radius-sm);
      background: #CBD5E1;
      color: var(--text-main);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: 700;
      flex-shrink: 0;
    }}
    .wp-step-pill.active .wp-step-num {{
      background: var(--ewag-blue);
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
      padding: 13px 14px;
      min-height: 52px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-light);
      background: #FFFFFF;
      color: var(--text-main);
      font-family: var(--font-body);
      font-size: 14px;
      font-weight: 600;
      text-align: left;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .topic-btn.selected {{
      border-color: var(--ewag-blue);
      background: var(--ewag-ice);
      color: var(--ewag-blue);
    }}
    .plz-badge {{
      display: none;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      font-size: 13px;
      font-weight: 600;
      background: #DCFCE7;
      color: #166534;
    }}
    .plz-badge.visible {{ display: inline-flex; align-items: center; gap: 6px; }}

    /* Subpage Hero (Light) */
    .page-hero {{
      background: var(--ewag-ice);
      border-bottom: 1px solid var(--border-light);
      padding: 46px 0 48px;
    }}
    .page-hero h1 {{
      font-size: clamp(1.85rem, 3.8vw, 2.85rem);
      font-weight: 800;
      color: var(--ewag-blue);
      max-width: 820px;
      margin-bottom: 12px;
    }}
    .page-hero p {{
      font-size: 17px;
      color: var(--text-muted);
      max-width: 720px;
      margin-bottom: 20px;
    }}

    /* Footer */
    .site-footer {{
      background: var(--ewag-blue);
      color: #FFFFFF;
      padding: 52px 0 28px;
    }}
    .footer-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr)) 1.3fr;
      gap: 32px;
      padding-bottom: 32px;
      border-bottom: 1px solid var(--border-dark);
    }}
    .footer-col h4 {{
      font-size: 13.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #BFDBFE;
      margin-bottom: 12px;
    }}
    .footer-links {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .footer-links a {{
      font-size: 14.5px;
      color: #FFFFFF;
      padding: 4px 0;
      min-height: 36px;
      display: inline-flex;
      align-items: center;
    }}
    .footer-links a:hover {{ text-decoration: underline; }}
    .footer-brand-box {{
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid var(--border-dark);
      border-radius: var(--radius-md);
      padding: 18px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-size: 14.5px;
    }}
    .footer-brand-box a {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-height: 34px;
      color: #FFFFFF;
      font-weight: 600;
    }}
    .footer-bottom {{
      padding-top: 22px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      font-size: 13.5px;
      color: #DCE8F5;
    }}
    .footer-legal {{
      display: flex;
      align-items: center;
      gap: 18px;
      flex-wrap: wrap;
    }}
    .footer-legal a {{
      min-height: 36px;
      display: inline-flex;
      align-items: center;
    }}
    .footer-legal a:hover {{ text-decoration: underline; color: #FFFFFF; }}
    .legal-box {{
      max-width: 840px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 16px;
      background: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 28px;
    }}
    .legal-box h2 {{ font-size: 21px; color: var(--ewag-blue); margin-top: 8px; }}
    .legal-box p {{ color: var(--text-muted); line-height: 1.7; }}

    .mobile-sticky-bar {{ display: none; }}

    @media (max-width: 1023px) {{
      .desktop-nav, .header-actions, .orig-navband, .orig-brand-meta {{ display: none; }}
      .nav-burger {{ display: inline-flex; }}
      .hero-grid, .split-grid, .orig-3col, .grid-2, .grid-3, .grid-4, .roster-grid, .footer-grid {{
        grid-template-columns: 1fr;
      }}
      .hero-modern-mosaic {{
        grid-template-columns: 1fr 1fr;
        grid-template-rows: auto;
      }}
      .hero-metrics {{ grid-template-columns: 1fr; }}
      .split-media {{ min-height: 240px; }}
    }}

    @media (max-width: 768px) {{
      .btn {{ white-space: normal; text-align: center; max-width: 100%; }}
      .section-light, .section-alt, .section-blue {{ padding: 44px 0; }}
      .hero-modern {{ padding: 32px 0 40px; }}
      .orig-stage-img {{ height: 220px; }}
      .form-grid-2, .wp-step-bar, .topic-grid {{ grid-template-columns: 1fr; }}
      .contact-panel {{ padding: 20px; }}
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
        background: #FFFFFF;
        border-top: 1px solid var(--border-light);
        box-shadow: 0 -4px 16px rgba(15, 23, 42, 0.08);
      }}
    }}
    @media (prefers-reduced-motion: no-preference) {{
      @view-transition {{ navigation: auto; }}
    }}
    """


def render_header(active_page: str, mode: str, folder: str) -> str:
    nav_items = [
        ("index.html", "Home"),
        ("firma.html", "Firma"),
        ("dienstleistungen.html", "Dienstleistungen"),
        ("referenzen.html", "Referenzen"),
        ("raeumlichkeiten.html", "Räumlichkeiten"),
        ("kontakt.html", "Kontakt"),
    ]
    mob_links = "\n".join(
        f'      <a href="{href}" class="mob-link">{esc(label)}</a>'
        for href, label in nav_items
    )
    if mode == "original":
        nav_links = "\n".join(
            f'        <a href="{href}" class="orig-nav-link{" active" if active_page == href else ""}">{esc(label)}</a>'
            for href, label in nav_items
        )
        return f"""  <header class="site-header">
    <div class="orig-topband">
      <div class="orig-topband-inner">
        <a href="index.html" class="brand-link" aria-label="EWAG / E. Widmer AG Startseite">
          {img_tag(folder, "images/logo.png", "EWAG / E. Widmer AG Logo", cls="brand-logo", slot="brand_logo")}
        </a>
        <div class="orig-brand-meta">
          <span>Elektro · Telecom · Netzwerk</span>
          <a href="tel:+41628550880" data-slot="phone">Tel. 062 855 08 80</a>
        </div>
        <button type="button" class="nav-burger" id="navBurger" aria-label="Menü öffnen" aria-expanded="false">
          {SVG_MENU}
        </button>
      </div>
    </div>
    <div class="orig-navband">
      <div class="orig-navband-inner">
        <nav class="orig-nav-links" aria-label="Hauptnavigation">
{nav_links}
        </nav>
        <a href="tel:+41628550880" class="orig-pikett-chip">{SVG_PHONE}<span>24h-Pikett: 062 855 08 80</span></a>
      </div>
    </div>
  </header>
  <div class="mobile-drawer" id="mobileDrawer">
{mob_links}
    <a href="jobs.html" class="mob-link">Offene Stellen &amp; Lehrstelle</a>
    <a href="kontakt.html#kontakt" class="btn btn-primary mob-cta">Kontakt aufnehmen</a>
  </div>"""

    desk_links = "\n".join(
        f'        <a href="{href}" class="nav-link{" active" if active_page == href else ""}">{esc(label)}</a>'
        for href, label in nav_items
    )
    return f"""  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand-link" aria-label="EWAG / E. Widmer AG Startseite">
        {img_tag(folder, "images/logo.png", "EWAG / E. Widmer AG Logo", cls="brand-logo", slot="brand_logo")}
      </a>
      <nav class="desktop-nav" aria-label="Hauptnavigation">
{desk_links}
      </nav>
      <div class="header-actions">
        <a href="tel:+41628550880" class="btn btn-outline-light">{SVG_PHONE}<span>062 855 08 80</span></a>
        <a href="index.html#kontakt" class="btn btn-primary">Anfrage senden</a>
      </div>
      <button type="button" class="nav-burger" id="navBurger" aria-label="Menü öffnen" aria-expanded="false">
        {SVG_MENU}
      </button>
    </div>
  </header>
  <div class="mobile-drawer" id="mobileDrawer">
{mob_links}
    <a href="jobs.html" class="mob-link">Offene Stellen &amp; Lehrstelle</a>
    <a href="index.html#kontakt" class="btn btn-primary mob-cta">Anfrage senden</a>
  </div>"""


def render_footer(mode: str, folder: str) -> str:
    sticky_bar = ""
    if mode == "modern":
        sticky_bar = f"""
  <div class="mobile-sticky-bar" id="mobileStickyBar">
    <a href="tel:+41628550880" class="btn btn-outline-light">{SVG_PHONE}<span>Anrufen</span></a>
    <a href="index.html#kontakt" class="btn btn-primary">{SVG_SEND}<span>Anfrage</span></a>
  </div>"""
    return f"""  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-col">
          <h4>Leistungen</h4>
          <div class="footer-links">
            <a href="dienstleistungen.html#haus-und-wohnungen">Haus und Wohnungen</a>
            <a href="dienstleistungen.html#gewerbe-und-industrie">Gewerbe und Industrie</a>
            <a href="dienstleistungen.html#service-und-notfaelle">Service und 24h-Pikett</a>
            <a href="dienstleistungen.html#photovoltaikanlage">Photovoltaik &amp; e-Mobilität</a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Firma &amp; Karriere</h4>
          <div class="footer-links">
            <a href="firma.html">Über uns &amp; Chronik</a>
            <a href="firma.html#team">Team</a>
            <a href="firma.html#ausbildung">Ausbildung EFZ</a>
            <a href="jobs.html">Offene Stellen</a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Service &amp; Ort</h4>
          <div class="footer-links">
            <a href="referenzen.html">Referenzen</a>
            <a href="raeumlichkeiten.html">Ausstellung &amp; Verkaufsladen</a>
            <a href="kontakt.html#oeffnungszeiten">Öffnungszeiten</a>
            <a href="kontakt.html#kontakt">Kontaktformular</a>
          </div>
        </div>
        <div class="footer-brand-box">
          <strong data-slot="footer_company">EWAG / E. Widmer AG</strong>
          <span>Tramstrasse 47 · 5034 Suhr</span>
          <a href="tel:+41628550880" data-slot="phone">{SVG_PHONE}<span>062 855 08 80 (24h-Pikett)</span></a>
          <a href="mailto:office@ewagsuhr.ch" data-slot="email">{SVG_MAIL}<span>office@ewagsuhr.ch</span></a>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="footer-legal">
          <span data-slot="footer_copyright">© 2026 EWAG / E. Widmer AG · Tramstrasse 47 · 5034 Suhr</span>
          <a href="impressum.html">Impressum</a>
          <a href="datenschutz.html">Datenschutzerklärung</a>
        </div>
        <div>Seit 1925 in Suhr · Elektro · Telecom · Netzwerk</div>
      </div>
    </div>
  </footer>{sticky_bar}"""


def render_contact_form_section(mode: str, section_id: str = "kontakt") -> str:
    if mode == "modern":
        return f"""    <section class="section-alt" id="{section_id}">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">Direktkontakt &amp; Smart-Anfrage</span>
          <h2 data-slot="contact_heading">Anfrage in drei Schritten senden</h2>
          <p class="lead-p" data-slot="contact_sub">Wählen Sie Ihr Anliegen, ergänzen Sie den Ort und erhalten Sie rasch eine Rückmeldung vom zuständigen EWAG-Projektleiter.</p>
        </div>
        <div class="contact-panel">
          <form id="ewagContactForm" toolname="ewag_anfrage" tooldescription="Anfrage an die EWAG / E. Widmer AG in Suhr senden" onsubmit="return wpSubmitEwagLead(event);" style="display:flex;flex-direction:column;gap:18px;">
            <input type="text" id="wpHoneypot" name="website_url" form="wpTrapDetached" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0;">
            <input type="hidden" id="wpSelectedTopic" value="Elektroinstallation / Umbau">
            <div class="wp-step-bar">
              <button type="button" class="wp-step-pill active" data-step-btn="1" onclick="wpGoStep(1)"><span class="wp-step-num">1</span><span>Thema wählen</span></button>
              <button type="button" class="wp-step-pill" data-step-btn="2" onclick="wpGoStep(2)"><span class="wp-step-num">2</span><span>Ort &amp; Angaben</span></button>
              <button type="button" class="wp-step-pill" data-step-btn="3" onclick="wpGoStep(3)"><span class="wp-step-num">3</span><span>Kontakt</span></button>
            </div>
            <div id="wpStep1" class="wp-step-pane active" data-step="1">
              <div class="topic-grid">
                <button type="button" class="topic-btn selected" onclick="wpSelectTopic('Elektroinstallation / Umbau', this); wpGoStep(2);">{SVG_HOME}<span>Elektroinstallation / Umbau</span></button>
                <button type="button" class="topic-btn" onclick="wpSelectTopic('24h-Pikett / Serviceeinsatz', this); wpGoStep(2);">{SVG_ZAP}<span>24h-Pikett / Serviceeinsatz</span></button>
                <button type="button" class="topic-btn" onclick="wpSelectTopic('Photovoltaik & e-Mobilität', this); wpGoStep(2);">{SVG_SUN}<span>Photovoltaik &amp; e-Mobilität</span></button>
                <button type="button" class="topic-btn" onclick="wpSelectTopic('Bewerbung / Lehrstelle EFZ', this); wpGoStep(2);">{SVG_BRIEFCASE}<span>Bewerbung / Lehrstelle EFZ</span></button>
              </div>
              <div style="display:flex;justify-content:flex-end;">
                <button type="button" class="btn btn-primary" onclick="wpGoStep(2)">Weiter zu Schritt 2 {SVG_ARROW}</button>
              </div>
            </div>
            <div id="wpStep2" class="wp-step-pane" data-step="2">
              <div class="form-grid-2">
                <div class="field">
                  <label for="contactStreet">Strasse &amp; Nr.</label>
                  <input type="text" id="contactStreet" name="street-address" autocomplete="street-address" placeholder="z. B. Tramstrasse 12">
                </div>
                <div class="field">
                  <label for="contactLoc">PLZ &amp; Ort</label>
                  <input type="text" id="contactLoc" name="postal-code" autocomplete="postal-code" placeholder="z. B. 5034 Suhr" oninput="wpUpdatePlzBadge()">
                </div>
              </div>
              <span id="wpPlzBadge" class="plz-badge">{SVG_CHECK}<span>Direkt im EWAG Einsatzgebiet (Suhr, Aarau &amp; Kanton Aargau)</span></span>
              <div class="field">
                <label for="contactMessage">Ihr Anliegen</label>
                <textarea id="contactMessage" name="message" placeholder="Beschreiben Sie kurz Ihr Projekt, Ihre Störung oder Ihre Bewerbung..."></textarea>
              </div>
              <div style="display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;">
                <button type="button" class="btn btn-outline-light" onclick="wpGoStep(1)">Zurück</button>
                <button type="button" class="btn btn-primary" onclick="wpGoStep(3)">Weiter zu den Kontaktdaten {SVG_ARROW}</button>
              </div>
            </div>
            <div id="wpStep3" class="wp-step-pane" data-step="3">
              <div class="form-grid-2">
                <div class="field">
                  <label for="contactName">Vor- und Nachname *</label>
                  <input type="text" id="contactName" name="name" autocomplete="name" required placeholder="Ihr Name">
                </div>
                <div class="field">
                  <label for="contactPhone">Telefonnummer</label>
                  <input type="tel" id="contactPhone" name="tel" autocomplete="tel" placeholder="+41 62 ...">
                </div>
              </div>
              <div class="field">
                <label for="contactEmail">E-Mail-Adresse *</label>
                <input type="email" id="contactEmail" name="email" autocomplete="email" required placeholder="name@beispiel.ch">
              </div>
              <label class="check-row">
                <input type="checkbox" id="contactConsent" required>
                <span>Ich bin einverstanden, dass meine Angaben zur Bearbeitung meiner Anfrage verwendet werden.</span>
              </label>
              <div style="display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;">
                <button type="button" class="btn btn-outline-light" onclick="wpGoStep(2)">Zurück</button>
                <button type="submit" id="wpSubmitBtn" class="btn btn-primary">{SVG_SEND}<span>Anfrage senden</span></button>
              </div>
            </div>
            <div id="wpFormOk" class="form-feedback" role="status"></div>
            <div id="wpFormErr" class="form-feedback" role="alert"></div>
          </form>
        </div>
      </div>
    </section>"""

    return f"""    <section class="section-alt" id="{section_id}">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">Kontakt aufnehmen</span>
          <h2 data-slot="contact_heading">Schreiben Sie uns</h2>
          <p class="lead-p" data-slot="contact_sub">EWAG / E. Widmer AG · Tramstrasse 47 · CH-5034 Suhr · Tel. 062 855 08 80 · office@ewagsuhr.ch</p>
        </div>
        <div class="contact-panel">
          <form id="ewagContactForm" toolname="ewag_kontakt" tooldescription="Kontaktformular der EWAG / E. Widmer AG in Suhr" onsubmit="return wpSubmitEwagLead(event);" style="display:flex;flex-direction:column;gap:14px;">
            <input type="text" id="wpHoneypot" name="website_url" form="wpTrapDetached" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0;">
            <div class="form-grid-2">
              <div class="field">
                <label for="contactName">Vor- und Nachname *</label>
                <input type="text" id="contactName" name="name" autocomplete="name" required placeholder="Ihr Name">
              </div>
              <div class="field">
                <label for="contactEmail">E-Mail-Adresse *</label>
                <input type="email" id="contactEmail" name="email" autocomplete="email" required placeholder="name@beispiel.ch">
              </div>
            </div>
            <div class="form-grid-2">
              <div class="field">
                <label for="contactPhone">Telefonnummer</label>
                <input type="tel" id="contactPhone" name="tel" autocomplete="tel" placeholder="062 ...">
              </div>
              <div class="field">
                <label for="contactProjectType">Bereich / Thema</label>
                <select id="contactProjectType" name="topic">
                  <option value="Elektroinstallation / Umbau">Elektroinstallation / Umbau</option>
                  <option value="24h-Pikett / Serviceeinsatz">24h-Pikett / Serviceeinsatz</option>
                  <option value="Photovoltaik &amp; e-Mobilität">Photovoltaik &amp; e-Mobilität</option>
                  <option value="Bewerbung / Lehrstelle EFZ">Bewerbung / Lehrstelle EFZ</option>
                </select>
              </div>
            </div>
            <div class="form-grid-2">
              <div class="field">
                <label for="contactStreet">Strasse &amp; Nr.</label>
                <input type="text" id="contactStreet" name="street-address" autocomplete="street-address" placeholder="Strasse">
              </div>
              <div class="field">
                <label for="contactLoc">PLZ &amp; Ort</label>
                <input type="text" id="contactLoc" name="postal-code" autocomplete="postal-code" placeholder="5034 Suhr">
              </div>
            </div>
            <div class="field">
              <label for="contactMessage">Nachricht</label>
              <textarea id="contactMessage" name="message" placeholder="Ihre Mitteilung an die EWAG / E. Widmer AG..."></textarea>
            </div>
            <label class="check-row">
              <input type="checkbox" id="contactConsent" required>
              <span>Ich bin mit der Bearbeitung meiner Anfrage gemäss Datenschutzerklärung einverstanden.</span>
            </label>
            <div style="display:flex;justify-content:flex-end;">
              <button type="submit" id="wpSubmitBtn" class="btn btn-primary">{SVG_SEND}<span>Nachricht senden</span></button>
            </div>
            <div id="wpFormOk" class="form-feedback" role="status"></div>
            <div id="wpFormErr" class="form-feedback" role="alert"></div>
          </form>
        </div>
      </div>
    </section>"""


def render_common_scripts(client_slug: str) -> str:
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
      var params = new URLSearchParams(window.location.search);
      var qTopic = params.get('thema');
      if (qTopic) {{
        var sel = document.getElementById('contactProjectType');
        var hid = document.getElementById('wpSelectedTopic');
        if (sel) sel.value = qTopic;
        if (hid) hid.value = qTopic;
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

    function wpPreselectTopic(topic) {{
      var inp = document.getElementById('wpSelectedTopic');
      if (inp) inp.value = topic;
      var sel = document.getElementById('contactProjectType');
      if (sel) {{
        for (var i = 0; i < sel.options.length; i++) {{
          if (sel.options[i].text.indexOf('Bewerbung') !== -1 || sel.options[i].value.indexOf('Bewerbung') !== -1) {{
            sel.selectedIndex = i;
            break;
          }}
        }}
      }}
      if (document.getElementById('wpStep2')) wpGoStep(2);
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
        if (['4', '5'].indexOf(p) !== -1) {{
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

    function wpSubmitEwagLead(e) {{
      if (e) e.preventDefault();
      var form = document.getElementById('ewagContactForm');
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
      var street = (document.getElementById('contactStreet') ? document.getElementById('contactStreet').value : '').trim();
      var loc = (document.getElementById('contactLoc') ? document.getElementById('contactLoc').value : '').trim();
      var phone = (document.getElementById('contactPhone') ? document.getElementById('contactPhone').value : '').trim();
      var email = (document.getElementById('contactEmail').value || '').trim();
      var topicEl = document.getElementById('wpSelectedTopic') || document.getElementById('contactProjectType');
      var topic = (topicEl && topicEl.value || 'Allgemeine Anfrage').trim();
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
          errBox.textContent = 'Es ist ein Fehler aufgetreten. Bitte prüfen Sie Ihre Eingaben oder rufen Sie 062 855 08 80 an.';
          errBox.className = 'form-feedback err';
        }}
      }});
      return false;
    }}
  </script>"""


def wrap_page(title: str, desc: str, active_page: str, body_html: str, mode: str, public_slug: str, folder: str) -> str:
    body_cls = ' class="has-sticky-bar"' if mode == "modern" else ""
    raw = f"""<!DOCTYPE html>
<html lang="de-CH" data-design-mode="evolution" data-expected-hero-polarity="light">
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
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Plus+Jakarta+Sans:wght@500;600;700;800&amp;display=swap" rel="stylesheet">
  <style>
{build_common_css(mode)}
  </style>
</head>
<body{body_cls}>
{render_header(active_page, mode, folder)}
  <main>
{body_html}
  </main>
{render_footer(mode, folder)}
{render_common_scripts(public_slug)}
</body>
</html>
"""
    return sanitize_ch(raw)


def build_index(mode: str, folder: str) -> str:
    featured_services = SERVICES[:6]
    srv_cards = "\n".join(
        f"""          <article class="card">
            <div class="card-top">
              <span class="card-icon">{s['icon']}</span>
              <span class="badge">{esc(s['kicker'])}</span>
            </div>
            <h3 data-slot="srv_{i+1}_title">{esc(s['title'])}</h3>
            <p class="lead-p" data-slot="srv_{i+1}_text">{esc(s['summary'])}</p>
            <div class="card-cta">
              <a href="dienstleistungen.html#{s['id']}" style="color:var(--ewag-blue);font-weight:600;display:inline-flex;align-items:center;gap:6px;">Mehr erfahren {SVG_ARROW}</a>
            </div>
          </article>"""
        for i, s in enumerate(featured_services)
    )

    if mode == "original":
        job_links = "\n".join(
            f'              <a href="jobs.html#{j["id"]}" class="orig-job-link"><span>{esc(j["title"])}</span>{SVG_ARROW}</a>'
            for j in JOBS
        )
        return f"""    <section class="orig-stage-wrap">
      <div class="wrap">
        <div class="orig-stage-card">
          {img_tag(folder, "images/film-02.jpg", "EWAG / E. Widmer AG Firmengebäude an der Tramstrasse 47 in Suhr", cls="orig-stage-img", slot="hero_img_1", hero=True)}
          <div class="orig-stage-bar">
            <div>
              <span class="section-kicker" data-slot="hero_kicker">EWAG / E. Widmer AG · Suhr</span>
              <h1 data-slot="hero_title">Willkommen bei Ihrem Haus-Elektriker</h1>
            </div>
            <a href="kontakt.html#kontakt" class="btn btn-primary">{SVG_PHONE}<span>062 855 08 80</span></a>
          </div>
        </div>
      </div>
    </section>

    <section class="section-light" style="padding-top:32px;">
      <div class="wrap">
        <div class="orig-3col">
          <article class="orig-col-box">
            <div>
              <h2 data-slot="welcome_heading">Willkommen bei Ihrem Haus-Elektriker</h2>
              <p class="lead-p" data-slot="welcome_p1">Die EWAG in Suhr ist Ihr Spezialist für den gesamten Stark- und Schwachstrombereich für Wohnungs-, Gewerbe- und Industriebau.</p>
              <p class="lead-p" style="margin-top:12px;" data-slot="welcome_p2">Mit ihren rund 45 Mitarbeitenden realisiert die EWAG kleinere wie auch grosse Projekte rund um Elektroinstallationen. Ein besonderes Augenmerk wird auf Reparatur- und Kundenarbeiten gelegt. Mit sorgfältig ausgewählten Partnern deckt die EWAG eine grosse Bandbreite an Produkten und Dienstleistungen ab, wie Reparaturen und Ersatz von Elektrogeräten für den Haushalt verschiedener Marken.</p>
              <p style="margin-top:14px;font-weight:600;color:var(--ewag-blue);" data-slot="welcome_author">Thomas Scheiber, Geschäftsführer der E. Widmer AG</p>
            </div>
            <div>
              <a href="firma.html" class="btn btn-outline-light">Über uns &amp; 100 Jahre Chronik {SVG_ARROW}</a>
            </div>
          </article>

          <article class="orig-col-box">
            <div>
              <h2 data-slot="news_heading">Aktuelles</h2>
              <p class="lead-p" data-slot="news_text">Jubiläum 100 Jahre E. Widmer AG (1925–2025) und Sonderausstellung im Museum Suhr (7. September 2025 bis 7. Juni 2026).</p>
              <div style="margin-top:14px;">
                {img_tag(folder, "images/home-sonderausstellung.jpg", "Sonderausstellung 100 Jahre E. Widmer AG im Museum Suhr", slot="news_img", style="border-radius:4px;border:1px solid var(--border-light);")}
              </div>
            </div>
            <div>
              <a href="firma.html#chronik" style="color:var(--ewag-blue);font-weight:600;display:inline-flex;align-items:center;gap:6px;">Sonderausstellung &amp; Chronik {SVG_ARROW}</a>
            </div>
          </article>

          <article class="orig-col-box">
            <div>
              <h2 data-slot="jobs_box_heading">Offene Stellen</h2>
              <div class="orig-job-list">
{job_links}
              </div>
            </div>
            <div>
              <a href="jobs.html" class="btn btn-primary" style="width:100%;">Alle offenen Stellen ansehen</a>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">Dienstleistungen</span>
          <h2 data-slot="services_heading">Stark- und Schwachstrom aus Suhr</h2>
          <p class="lead-p">Von der Wohnungsinstallation über Photovoltaik und e-Mobilität bis zum 24h-Pikettdienst.</p>
        </div>
        <div class="grid-3">
{srv_cards}
        </div>
        <div style="text-align:center;margin-top:28px;">
          <a href="dienstleistungen.html" class="btn btn-outline-light">Alle 11 Fachbereiche ansehen {SVG_ARROW}</a>
        </div>
      </div>
    </section>

{render_contact_form_section(mode)}"""

    # Modern-Tweak Homepage
    job_cards_modern = "\n".join(
        f"""          <article class="card">
            <span class="badge">{esc(j['badge'])}</span>
            <h3 class="card-title-2line">{esc(j['title'])}</h3>
            <p class="lead-p">{esc(j['lead'])}</p>
            <div class="card-cta" style="display:flex;gap:10px;flex-wrap:wrap;">
              <a href="#kontakt" class="btn btn-primary" onclick="wpPreselectTopic('{esc(j['topic_value'])}')">60-Sek.-Bewerbung {SVG_ARROW}</a>
              <a href="jobs.html#{j['id']}" class="btn btn-outline-light">Details</a>
            </div>
          </article>"""
        for j in JOBS
    )

    ewag_cards = "\n".join(
        f"""          <article class="card-blue">
            <div style="font-family:var(--font-head);font-size:22px;font-weight:800;color:#FFFFFF;white-space:nowrap;">{letter} = {word}</div>
            <p style="color:var(--text-on-dark-muted);font-size:15px;line-height:1.6;">{esc(desc)}</p>
          </article>"""
        for letter, word, desc in EWAG_PILLARS
    )

    return f"""    <section class="hero-modern">
      <div class="wrap">
        <div class="hero-grid">
          <div class="hero-left">
            <div>
              <span class="section-kicker" data-slot="hero_kicker">EWAG / E. Widmer AG · Suhr AG</span>
              <h1 class="hero-h1" data-slot="hero_title">Ihr Haus-Elektriker seit 1925</h1>
            </div>
            <p class="hero-sub" data-slot="hero_lead">Die EWAG in Suhr ist Ihr Spezialist für den gesamten Stark- und Schwachstrombereich bei Wohnungs-, Gewerbe- und Industriebauten – von Reparaturen über Photovoltaik bis zum 24h-Pikett.</p>
            <div class="hero-cta-row">
              <a href="#kontakt" class="btn btn-primary">{SVG_SEND}<span>Anfrage starten</span></a>
              <a href="tel:+41628550880" class="btn btn-outline-light">{SVG_PHONE}<span>24h-Pikett: 062 855 08 80</span></a>
            </div>
            <div class="hero-metrics">
              <div class="metric-box">
                <div class="metric-val">Seit 1925</div>
                <div class="metric-lbl">Über 100 Jahre Erfahrung</div>
              </div>
              <div class="metric-box">
                <div class="metric-val">45 Fachleute</div>
                <div class="metric-lbl">Inkl. über 300 Lernende</div>
              </div>
              <div class="metric-box">
                <div class="metric-val">7 × 24 Stunden</div>
                <div class="metric-lbl">Pikett unter 062 855 08 80</div>
              </div>
            </div>
          </div>
          <div class="hero-modern-mosaic">
            <div class="photo-frame span-2">
              {img_tag(folder, "images/film-02.jpg", "EWAG / E. Widmer AG Standort Tramstrasse 47 in Suhr", slot="hero_img_1", hero=True)}
            </div>
            <div class="photo-frame">
              {img_tag(folder, "images/film-35.jpg", "Elektroinstallateur der EWAG Suhr im Einsatz", slot="hero_img_2")}
            </div>
            <div class="photo-frame">
              {img_tag(folder, "images/ref-mfh-zopfmatte-suhr_01.jpg", "Realisiertes Elektroprojekt in Suhr – MFH Zopfmatte", slot="hero_img_3")}
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section-light">
      <div class="wrap">
        <div class="split-grid">
          <div class="split-media">
            {img_tag(folder, "images/film-15.jpg", "Empfang und Projektleitung bei der EWAG / E. Widmer AG in Suhr", slot="team_group_img")}
          </div>
          <div class="split-content">
            <div>
              <span class="section-kicker" data-slot="about_kicker">Tradition &amp; Kundennähe</span>
              <h2 class="split-h2" data-slot="about_heading">Kein Einsatz ist uns zu klein</h2>
              <p class="lead-p" data-slot="about_text">Mit rund 45 Mitarbeitenden realisiert die EWAG kleinere wie auch grosse Projekte rund um Elektroinstallationen. Besonderes Augenmerk legen wir auf zuverlässige Reparatur- und Kundenarbeiten sowie unsere eigene Ausstellung an der Tramstrasse 47 in Suhr.</p>
            </div>
            <div>
              {img_tag(folder, "images/home-sonderausstellung.jpg", "100 Jahre E. Widmer AG Sonderausstellung", slot="about_banner", style="border-radius:4px;border:1px solid var(--border-light);margin-bottom:14px;")}
              <a href="firma.html" class="btn btn-outline-light">Team &amp; 100-Jahre-Chronik {SVG_ARROW}</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section-blue">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">Unsere Werte</span>
          <h2>Wofür EWAG seit 1925 steht</h2>
        </div>
        <div class="grid-4">
{ewag_cards}
        </div>
      </div>
    </section>

    <section class="section-light">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">Leistungsübersicht</span>
          <h2 data-slot="services_heading">Alle Elektro-Kompetenzen unter einem Dach</h2>
          <p class="lead-p">Starkstrom, Schwachstrom, Gebäudeautomation, Photovoltaik, e-Mobilität und Haushaltsgeräte-Service für Privat und Gewerbe.</p>
        </div>
        <div class="grid-3">
{srv_cards}
        </div>
        <div style="text-align:center;margin-top:28px;">
          <a href="dienstleistungen.html" class="btn btn-primary">Alle 11 Fachbereiche im Detail {SVG_ARROW}</a>
        </div>
      </div>
    </section>

    <section class="section-alt" id="offene-stellen">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">Karriere &amp; Berufsnachwuchs</span>
          <h2>Offene Stellen &amp; Lehrstelle 2027</h2>
          <p class="lead-p">Wir suchen Menschen, die mit Begeisterung und Leidenschaft an der Seite unserer Kunden stehen – inklusive bis zu 7 Wochen Ferien und eigenem Firmenauto für Monteure und Projektleitung.</p>
        </div>
        <div class="grid-2">
{job_cards_modern}
        </div>
      </div>
    </section>

{render_contact_form_section(mode)}"""


def build_firma(mode: str, folder: str) -> str:
    leader_cards = "\n".join(
        f"""          <article class="card">
            {img_tag(folder, m['img'], f"{m['name']} – {m['role']}", cls="team-portrait")}
            <div>
              <span class="section-kicker">{esc(m['role'])}</span>
              <h3>{esc(m['name'])}</h3>
            </div>
            <div class="card-cta" style="display:flex;flex-direction:column;gap:6px;">
              <a href="tel:{m['tel']}" style="color:var(--ewag-blue);font-weight:600;">{SVG_PHONE} {esc(m['phone'])}</a>
              <a href="mailto:{m['email']}" style="color:var(--text-muted);font-size:14px;">{SVG_MAIL} {esc(m['email'])}</a>
            </div>
          </article>"""
        for m in TEAM_LEADERSHIP
    )

    staff_cards = "\n".join(
        f"""          <article class="card">
            {img_tag(folder, m['img'], f"{m['name']} – {m['role']}", cls="team-portrait") if m['img'] else '<div style="aspect-ratio:3/2;background:var(--ewag-ice);border-radius:4px;display:flex;align-items:center;justify-content:center;color:var(--ewag-blue);font-weight:700;">EWAG Administration</div>'}
            <div>
              <span class="section-kicker">{esc(m['role'])}</span>
              <h3>{esc(m['name'])}</h3>
            </div>
            <div class="card-cta" style="display:flex;flex-direction:column;gap:4px;">
              <a href="tel:{m['phone'].replace(' ', '')}" style="color:var(--ewag-blue);font-weight:600;">{esc(m['phone'])}</a>
              <a href="mailto:{m['email']}" style="color:var(--text-muted);font-size:14px;">{esc(m['email'])}</a>
            </div>
          </article>"""
        for m in TEAM_STAFF
    )

    installer_cards = "\n".join(
        f"""          <div class="roster-card">
            {img_tag(folder, im, f"{name} – Elektroinstallateur EWAG Suhr") if im else '<div style="aspect-ratio:3/2;background:var(--ewag-ice);border-radius:4px;display:flex;align-items:center;justify-content:center;color:var(--ewag-blue);font-weight:700;font-size:13px;">Elektroinstallateur EFZ</div>'}
            <div class="roster-name">{esc(name)}</div>
          </div>"""
        for name, im in TEAM_INSTALLERS
    )

    apprentice_cards = "\n".join(
        f"""          <div class="roster-card">
            {img_tag(folder, im, f"{name} – Lernender EWAG Suhr")}
            <div class="roster-name">{esc(name)}</div>
          </div>"""
        for name, im in TEAM_APPRENTICES
    )

    chronicle_rows = "\n".join(
        f"""          <div class="card">
            <span class="badge">{yr}</span>
            <p class="lead-p">{esc(txt)}</p>
          </div>"""
        for yr, txt in CHRONICLE
    )

    return f"""    <section class="page-hero">
      <div class="wrap">
        <span class="section-kicker">Firma · Über uns, Team &amp; Ausbildung</span>
        <h1 data-slot="firma_h1">E. Widmer AG – Ihr Elektro-Partner seit 1925</h1>
        <p data-slot="firma_sub">Wir – die E. Widmer AG oder kurz EWAG genannt – sind Ihr Partner rund um die Uhr für alle Bereiche von Elektro-, Telecom- und Netzwerkinstallationen.</p>
      </div>
    </section>

    <section class="section-light" id="chronik">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">E · W · A · G</span>
          <h2>100 Jahre Firmengeschichte in Suhr</h2>
          <p class="lead-p">Von der Gründung 1925 durch Emil Widmer bis zum Jubiläum 2025 und der Sonderausstellung im Museum Suhr.</p>
        </div>
        <div class="grid-3">
{chronicle_rows}
        </div>
      </div>
    </section>

    <section class="section-alt" id="team">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">Unser Team</span>
          <h2>Geschäftsleitung, Projektleitung &amp; Fachkräfte</h2>
          <p class="lead-p">Rund 45 erfahrene Mitarbeitende und Lernende stehen täglich für höchste Schweizer Ausführungsqualität ein.</p>
        </div>
        <div style="margin-bottom:28px;">
          {img_tag(folder, "images/team_02.jpg", "Das gesamte Team der EWAG / E. Widmer AG", style="width:100%;max-height:380px;object-fit:cover;border-radius:8px;border:1px solid var(--border-light);")}
        </div>
        <div class="grid-3" style="margin-bottom:28px;">
{leader_cards}
        </div>
        <div class="grid-3" style="margin-bottom:36px;">
{staff_cards}
        </div>
        <h3 style="font-size:22px;color:var(--ewag-blue);margin-bottom:16px;">Elektroinstallateure EFZ</h3>
        <div class="roster-grid" style="margin-bottom:36px;">
{installer_cards}
        </div>
        <h3 style="font-size:22px;color:var(--ewag-blue);margin-bottom:16px;">Unsere Lernenden</h3>
        <div class="roster-grid">
{apprentice_cards}
        </div>
      </div>
    </section>

    <section class="section-light" id="ausbildung">
      <div class="wrap">
        <div class="split-grid">
          <div class="split-content">
            <div>
              <span class="section-kicker">Berufsbildung &amp; Schnupperwoche</span>
              <h2 class="split-h2">Ausbildung bei der EWAG</h2>
              <p class="lead-p">In unserem Betrieb bilden wir Elektroinstallateur:innen EFZ (4 Jahre) und Montageelektriker:innen EFZ (3 Jahre) aus – inklusive unverbindlicher Schnupperwochen und Unterstützung für Sportler-Lehrstellen (Swiss Olympic Partnerbetrieb).</p>
              <ul class="clean-list" style="margin-top:14px;">
                <li>{SVG_CHECK}<span>Elektroinstallateur/in EFZ (4 Jahre Lehrdauer)</span></li>
                <li>{SVG_CHECK}<span>Montageelektriker/in EFZ (3 Jahre Lehrdauer)</span></li>
                <li>{SVG_CHECK}<span>Auskunft &amp; Schnupperlehre: Nico Knechtli (nk@ewagsuhr.ch, 062 855 08 82)</span></li>
              </ul>
            </div>
            <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;">
              {img_tag(folder, "images/ausb-vignette_wir_machen_profis.jpg", "Wir machen Profis Vignette", style="height:64px;width:auto;")}
              {img_tag(folder, "images/ausb-vignette_swiss-olympic.jpg", "Swiss Olympic Partnerbetrieb", style="height:64px;width:auto;")}
              {img_tag(folder, "images/ausb-swiss.jpg", "eit.swiss", style="height:44px;width:auto;")}
              {img_tag(folder, "images/ausb-aargau.jpg", "eit.aargau", style="height:44px;width:auto;")}
            </div>
          </div>
          <div class="split-media">
            {img_tag(folder, "images/film-85.jpg", "Lernender bei der Ausbildung im Betrieb EWAG Suhr")}
          </div>
        </div>
      </div>
    </section>

{render_contact_form_section(mode)}"""


def build_dienstleistungen(mode: str, folder: str) -> str:
    blocks = []
    for s in SERVICES:
        bullets = "\n".join(f'              <li>{SVG_CHECK}<span>{esc(b)}</span></li>' for b in s["bullets"])
        blocks.append(f"""          <article class="card" id="{s['id']}">
            <div class="card-top">
              <span class="card-icon">{s['icon']}</span>
              <span class="badge">{esc(s['kicker'])}</span>
            </div>
            <h3>{esc(s['title'])}</h3>
            <p class="lead-p">{esc(s['summary'])}</p>
            <ul class="clean-list">
{bullets}
            </ul>
            <div class="card-cta">
              <a href="index.html#kontakt" style="color:var(--ewag-blue);font-weight:600;display:inline-flex;align-items:center;gap:6px;">Offerte / Beratung anfragen {SVG_ARROW}</a>
            </div>
          </article>""")

    return f"""    <section class="page-hero">
      <div class="wrap">
        <span class="section-kicker">Dienstleistungen · 11 Fachbereiche</span>
        <h1 data-slot="dl_h1">Starkstrom, Schwachstrom, Service &amp; Energie</h1>
        <p data-slot="dl_sub">Wir freuen uns auf Ihre Kontaktaufnahme. Von kleinen Serviceeinsätzen bis zu komplexen Industrieanlagen steht Ihnen die EWAG in Suhr kompetent zur Seite.</p>
        <a href="tel:+41628550880" class="btn btn-primary">{SVG_PHONE}<span>24h-Pikett &amp; Beratung: 062 855 08 80</span></a>
      </div>
    </section>

    <section class="section-light">
      <div class="wrap">
        <div class="grid-2">
{chr(10).join(blocks)}
        </div>
      </div>
    </section>

{render_contact_form_section(mode)}"""


def build_referenzen(mode: str, folder: str) -> str:
    def render_ref_cards(items):
        return "\n".join(
            f"""          <article class="card">
            {img_tag(folder, img, f"{title} – Referenz EWAG Suhr", cls="ref-img")}
            <span class="badge">{esc(yr)}</span>
            <h3 class="card-title-2line">{esc(title)}</h3>
            <p style="font-size:13.5px;font-weight:600;color:var(--text-main);">{esc(client)}</p>
            <p class="lead-p">{esc(tech)}</p>
          </article>"""
            for title, client, yr, img, tech in items
        )

    return f"""    <section class="page-hero">
      <div class="wrap">
        <span class="section-kicker">Referenzen · EFH, MFH &amp; Gewerbe</span>
        <h1 data-slot="ref_h1">Ausgewählte Referenzobjekte</h1>
        <p data-slot="ref_sub">Wir zeigen Ihnen ausgewählte Referenzobjekte von Arbeiten, die wir für unsere Kunden ausführen durften. Ausführliche Informationen erhalten Sie von einem unserer Projektleiter persönlich.</p>
      </div>
    </section>

    <section class="section-light" id="efh">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">Einfamilienhäuser</span>
          <h2>Unsere EFH Referenzen</h2>
        </div>
        <div class="grid-2">
{render_ref_cards(REFERENCES_EFH)}
        </div>
      </div>
    </section>

    <section class="section-alt" id="mfh">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">Mehrfamilienhäuser</span>
          <h2>Unsere MFH Referenzen</h2>
        </div>
        <div class="grid-2">
{render_ref_cards(REFERENCES_MFH)}
        </div>
      </div>
    </section>

    <section class="section-light" id="industrie">
      <div class="wrap">
        <div class="center-head">
          <span class="section-kicker">Industrie &amp; Gewerbe</span>
          <h2>Unsere Industrie- und Gewerbe-Referenzen</h2>
        </div>
        <div class="grid-3">
{render_ref_cards(REFERENCES_GEWERBE)}
        </div>
      </div>
    </section>

{render_contact_form_section(mode)}"""


def build_raeumlichkeiten(mode: str, folder: str) -> str:
    return f"""    <section class="page-hero">
      <div class="wrap">
        <span class="section-kicker">Räumlichkeiten · Tramstrasse 47, 5034 Suhr</span>
        <h1 data-slot="raum_h1">Ausstellung &amp; Verkaufsladen in Suhr</h1>
        <p data-slot="raum_sub">Während unserer umfassenden Beratung zeigen Ihnen unsere kompetenten Mitarbeiter Geräte und Installationen gerne direkt am Muster.</p>
      </div>
    </section>

    <section class="section-light">
      <div class="wrap">
        <div class="split-grid">
          <div class="split-media">
            {img_tag(folder, "images/raum-ausstellung.jpg", "Ausstellung der EWAG / E. Widmer AG in Suhr")}
          </div>
          <div class="split-content">
            <div>
              <span class="section-kicker">Ausstellung</span>
              <h2 class="split-h2">Aktuelle Technologien am Muster erleben</h2>
              <p class="lead-p">In unserer Ausstellung präsentieren wir Ihnen moderne Trends und bewährte Geräte. Vereinbaren Sie gerne einen Termin mit der entsprechenden Fachperson für eine persönliche Beratung.</p>
              <ul class="clean-list" style="margin-top:14px;">
                <li>{SVG_CHECK}<span>Beleuchtung (LED / OLED, Leuchten und Lichtkanäle)</span></li>
                <li>{SVG_CHECK}<span>Sicherheitsinstallationen und Gegensprechanlagen</span></li>
                <li>{SVG_CHECK}<span>Gebäudeautomation</span></li>
                <li>{SVG_CHECK}<span>Elektroinstallationen</span></li>
              </ul>
            </div>
            <div>
              <a href="kontakt.html#kontakt" class="btn btn-primary">Beratungstermin vereinbaren {SVG_ARROW}</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="wrap">
        <div class="grid-2">
          <article class="card">
            <span class="badge">Direkt vor Ort</span>
            <h3>Verkaufsladen an der Tramstrasse 47</h3>
            <p class="lead-p">In unserem Verkaufsladen bieten wir Ihnen während der Öffnungszeiten fachkundige Beratung und direkt verfügbares Material:</p>
            <ul class="clean-list">
              <li>{SVG_CHECK}<span>Leuchtmittel</span></li>
              <li>{SVG_CHECK}<span>Installationsmaterial für den Heimgebrauch</span></li>
              <li>{SVG_CHECK}<span>Sicherungen</span></li>
              <li>{SVG_CHECK}<span>Kundenparkplätze direkt vor der Eingangstüre oder hinter dem Haus</span></li>
            </ul>
          </article>
          <article class="card">
            <span class="badge">Öffnungszeiten &amp; Pikett</span>
            <h3>Wann Sie uns erreichen</h3>
            <p class="lead-p"><strong>Montag bis Donnerstag:</strong> 07:00 bis 11:45 Uhr und 13:00 bis 17:00 Uhr<br><strong>Freitag:</strong> 07:00 bis 11:45 Uhr und 13:00 bis 16:00 Uhr</p>
            <p class="lead-p">Rund um die Uhr erreichbar unter <strong>062 855 08 80</strong>. Ausserhalb der Öffnungszeiten wird Ihr Anruf bei dringenden Störungen an den Pikett-Servicedienst weitergeleitet (Kosten Serviceeinsatz ausserhalb normaler Arbeitszeiten: CHF 300.00 / Stunde).</p>
          </article>
        </div>
      </div>
    </section>

{render_contact_form_section(mode)}"""


def build_jobs(mode: str, folder: str) -> str:
    cards = []
    for j in JOBS:
        t_list = "\n".join(f'              <li>{SVG_CHECK}<span>{esc(t)}</span></li>' for t in j["tasks"])
        p_list = "\n".join(f'              <li>{SVG_CHECK}<span>{esc(p)}</span></li>' for p in j["profile"])
        cards.append(f"""          <article class="card" id="{j['id']}">
            <span class="badge">{esc(j['badge'])}</span>
            <h3 class="card-title-2line">{esc(j['title'])}</h3>
            <p class="lead-p">{esc(j['lead'])}</p>
            <strong style="font-size:14px;color:var(--ewag-blue);">Aufgaben</strong>
            <ul class="clean-list">
{t_list}
            </ul>
            <strong style="font-size:14px;color:var(--ewag-blue);">Profil</strong>
            <ul class="clean-list">
{p_list}
            </ul>
            <p class="lead-p" style="font-size:14px;"><strong>Unser Angebot:</strong> {esc(j['offer'])}</p>
            <p style="font-size:13.5px;font-weight:600;color:var(--text-main);">{esc(j['contact'])}</p>
            <div class="card-cta">
              <a href="#kontakt" class="btn btn-primary" onclick="wpPreselectTopic('{esc(j['topic_value'])}')">Jetzt direkt bewerben {SVG_ARROW}</a>
            </div>
          </article>""")

    return f"""    <section class="page-hero">
      <div class="wrap">
        <span class="section-kicker">Stellenangebot · Team Suhr</span>
        <h1 data-slot="jobs_h1">Menschen mit Begeisterung und Leidenschaft gesucht</h1>
        <p data-slot="jobs_sub">Die E. Widmer AG in Suhr realisiert mit rund 45 Mitarbeitenden kleine wie grosse Elektroprojekte. Wir bieten bis zu 7 Wochen Ferien, Schulungen und eigene Firmenfahrzeuge (Privatnutzung möglich).</p>
      </div>
    </section>

    <section class="section-light">
      <div class="wrap">
        <div class="grid-2">
{chr(10).join(cards)}
        </div>
        <div class="card" style="margin-top:24px;">
          <h3>Keine passende Stelle dabei? Spontanbewerbung willkommen</h3>
          <p class="lead-p">Kein Problem! Bewirb dich bei uns per E-Mail an bewerbung@ewagsuhr.ch oder direkt über unser Formular.</p><div class="card-cta"><a href="mailto:bewerbung@ewagsuhr.ch" class="btn btn-outline-light">Bewerbung per E-Mail: bewerbung@ewagsuhr.ch</a></div>
        </div>
      </div>
    </section>

{render_contact_form_section(mode)}"""


def build_kontakt(mode: str, folder: str) -> str:
    return f"""    <section class="page-hero">
      <div class="wrap">
        <span class="section-kicker">Kontakt &amp; Standort</span>
        <h1 data-slot="kontakt_h1">EWAG / E. Widmer AG · Suhr</h1>
        <p data-slot="kontakt_sub">Tramstrasse 47, CH-5034 Suhr · Tel. 062 855 08 80 · Fax 062 855 08 88 · office@ewagsuhr.ch</p>
      </div>
    </section>

    <section class="section-light" id="oeffnungszeiten">
      <div class="wrap">
        <div class="grid-2">
          <article class="card">
            <span class="badge">Standort &amp; Direkte Nummern</span>
            <h3>So finden und erreichen Sie uns</h3>
            <p class="lead-p"><strong>EWAG / E. Widmer AG</strong><br>Tramstrasse 47<br>CH-5034 Suhr</p>
            <ul class="clean-list">
              <li>{SVG_PHONE}<span>Telefon &amp; 24h-Pikett: <a href="tel:+41628550880" style="color:var(--ewag-blue);font-weight:600;">062 855 08 80</a></span></li>
              <li>{SVG_MAIL}<span>E-Mail: <a href="mailto:office@ewagsuhr.ch" style="color:var(--ewag-blue);font-weight:600;">office@ewagsuhr.ch</a></span></li>
              <li>{SVG_MAP_PIN}<span>Kundenparkplätze direkt vor der Eingangstüre oder hinter dem Haus</span></li>
            </ul>
          </article>
          <article class="card">
            <span class="badge">Öffnungszeiten &amp; Störungsdienst</span>
            <h3>Erreichbarkeit rund um die Uhr</h3>
            <p class="lead-p"><strong>Montag bis Donnerstag:</strong><br>07:00 bis 11:45 Uhr · 13:00 bis 17:00 Uhr</p>
            <p class="lead-p"><strong>Freitag:</strong><br>07:00 bis 11:45 Uhr · 13:00 bis 16:00 Uhr</p>
            <p class="lead-p">Ausserhalb der Öffnungszeiten wird Ihr Anruf unter 062 855 08 80 an unsere Pikett-Hotline weitergeleitet (Serviceeinsatz ausserhalb der normalen Arbeitszeiten: CHF 300.00 / Stunde).</p>
          </article>
        </div>
        <div style="margin-top:24px;border:1px solid var(--border-light);border-radius:8px;overflow:hidden;background:#FFFFFF;">
          {img_tag(folder, "images/kontakt-kontakt-map.jpg", "Anfahrtsplan EWAG / E. Widmer AG Tramstrasse 47 Suhr", style="width:100%;max-height:320px;object-fit:cover;")}
        </div>
      </div>
    </section>

{render_contact_form_section(mode)}"""


def build_impressum() -> str:
    return """    <section class="page-hero">
      <div class="wrap">
        <span class="section-kicker">Rechtliches</span>
        <h1>Impressum</h1>
        <p>Angaben zur Gesamtverantwortung der EWAG / E. Widmer AG in Suhr.</p>
      </div>
    </section>
    <section class="section-light">
      <div class="wrap">
        <div class="legal-box">
          <h2>Gesamtverantwortung</h2>
          <p><strong>EWAG / E. Widmer AG</strong><br>Tramstrasse 47<br>CH-5034 Suhr<br>Schweiz</p>
          <h2>Kontakt</h2>
          <p>Tel.: 062 855 08 80<br>Fax: 062 855 08 88<br>E-Mail: office@ewagsuhr.ch<br>Website: www.ewagsuhr.ch</p>
          <h2>Vertretung &amp; Urheberrechte</h2>
          <p>Geschäftsführung: Thomas Scheiber<br>Alle Inhalte, Texte und Fotografien auf dieser Website sind urheberrechtlich geschützt und Eigentum der EWAG / E. Widmer AG oder der jeweiligen Rechteinhaber.</p>
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
          <h2>1. Verantwortliche Kontaktadresse</h2>
          <p>EWAG / E. Widmer AG<br>Tramstrasse 47<br>5034 Suhr<br>Schweiz<br>E-Mail: office@ewagsuhr.ch<br>Tel.: 062 855 08 80</p>
          <h2>2. Erhebung und Bearbeitung von Personendaten</h2>
          <p>Beim Besuch dieser Website werden technische Zugriffsdaten zum sicheren Betrieb verarbeitet. Wenn Sie uns über das Kontaktformular, per E-Mail oder telefonisch kontaktieren, bearbeiten wir Ihre Angaben ausschliesslich zur Beantwortung Ihrer Anfrage oder Bewerbung gemäss dem Schweizer Datenschutzgesetz (DSG).</p>
          <h2>3. Rechte der betroffenen Personen</h2>
          <p>Sie haben jederzeit das Recht auf unentgeltliche Auskunft über Ihre gespeicherten personenbezogenen Daten sowie ein Recht auf Berichtigung oder Löschung dieser Daten im Rahmen der gesetzlichen Vorgaben.</p>
        </div>
      </div>
    </section>"""


def generate_variant(folder_name: str, public_slug: str, mode: str, display_label: str) -> None:
    out_dir = BASE_DIR / folder_name
    out_dir.mkdir(parents=True, exist_ok=True)

    company_json = {
        "company_name": "EWAG / E. Widmer AG",
        "legal_entity": "E. Widmer AG",
        "name": "EWAG / E. Widmer AG",
        "slug": public_slug,
        "city": "Suhr",
        "canton": "AG",
        "street": "Tramstrasse 47",
        "zip": "5034",
        "phone": "+41 62 855 08 80",
        "email": "office@ewagsuhr.ch",
        "website": "https://www.ewagsuhr.ch/",
        "partner_id": "jenny",
        "partner_name": "Jenny Ettle (JE-MI)",
        "design_mode": "original-1to1" if mode == "original" else "modern-tweak-1to1",
    }
    config_json = {
        "company_name": f"EWAG / E. Widmer AG · {display_label}",
        "slug": folder_name,
        "public_slug": public_slug,
        "cockpit_token": "ewagsuhr2026",
        "template": "original-1to1-v1" if mode == "original" else "modern-tweak-1to1-v1",
        "partner_id": "jenny",
        "pages": [
            "index.html",
            "firma.html",
            "dienstleistungen.html",
            "referenzen.html",
            "raeumlichkeiten.html",
            "jobs.html",
            "kontakt.html",
            "impressum.html",
            "datenschutz.html",
        ],
    }
    site_json = {
        "slug": folder_name,
        "public_slug": public_slug,
        "token": "ewagsuhr2026",
        "name": f"EWAG / E. Widmer AG · {display_label}",
        "Updated": "2026-11-26",
        "PagesCount": 9,
        "ReferencesCount": len(REFERENCES_EFH) + len(REFERENCES_MFH) + len(REFERENCES_GEWERBE),
        "TeamCount": len(TEAM_LEADERSHIP) + len(TEAM_STAFF) + len(TEAM_INSTALLERS) + len(TEAM_APPRENTICES),
    }
    design_vibe_json = {
        "mode": mode,
        "primary_accent": "#00508E",
        "bg_dark": "#00508E",
        "bg_light": "#FFFFFF",
        "font_heading": "Plus Jakarta Sans",
        "font_body": "Inter",
    }
    visual_dna_json = {
        "schema_version": "1.0.0",
        "slug": public_slug,
        "source_url": "https://www.ewagsuhr.ch/",
        "design_mode": "evolution",
        "target_hero_polarity": "light",
        "sommelier_decisions": {
            "polarity_decision": {"target_hero_polarity": "light"}
        },
    }

    (out_dir / "company.json").write_text(json.dumps(company_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "config.json").write_text(json.dumps(config_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "site.json").write_text(json.dumps(site_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "design-vibe.json").write_text(json.dumps(design_vibe_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "source_visual_dna.json").write_text(json.dumps(visual_dna_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    pages = {
        "index.html": (
            "EWAG / E. Widmer AG | Ihr Haus-Elektriker in Suhr seit 1925",
            "EWAG Suhr AG: Stark- und Schwachstrominstallationen bei Neu-, Um- oder Ausbauten von Wohn-, Gewerbe- und Industriegebäuden – beraten, planen, bauen, 24h-Pikett.",
            build_index(mode, folder_name),
        ),
        "firma.html": (
            "Firma, Team & Ausbildung | EWAG / E. Widmer AG Suhr",
            "Über 100 Jahre E. Widmer AG in Suhr: Geschäftsleitung, Projektleitung, 45 Mitarbeitende und EFZ-Ausbildung.",
            build_firma(mode, folder_name),
        ),
        "dienstleistungen.html": (
            "Dienstleistungen · Stark- & Schwachstrom | EWAG / E. Widmer AG",
            "Haus und Wohnungen, Gewerbe und Industrie, 24h-Pikett, Schwachstrom, Gebäudeautomation, Elektroplanung, e-Mobilität, Photovoltaik, Geräteprüfung, Haushaltsgeräte und Beleuchtung.",
            build_dienstleistungen(mode, folder_name),
        ),
        "referenzen.html": (
            "Referenzen · EFH, MFH & Gewerbe | EWAG / E. Widmer AG",
            "Realisierte Elektroprojekte der EWAG Suhr in Aarau, Suhr, Kölliken, Gränichen und Hunzenschwil.",
            build_referenzen(mode, folder_name),
        ),
        "raeumlichkeiten.html": (
            "Ausstellung & Verkaufsladen | EWAG / E. Widmer AG Suhr",
            "Besuchen Sie die Ausstellung für Beleuchtung und Gebäudeautomation sowie unseren Verkaufsladen an der Tramstrasse 47 in Suhr.",
            build_raeumlichkeiten(mode, folder_name),
        ),
        "jobs.html": (
            "Offene Stellen & Lehrstelle 2027 | EWAG / E. Widmer AG Suhr",
            "Aktuelle Stellenangebote: Elektroprojektleiter:in, Elektroinstallateur:in EFZ, Servicemonteur:in und Lehrstelle 2027 bei EWAG Suhr.",
            build_jobs(mode, folder_name),
        ),
        "kontakt.html": (
            "Kontakt & Öffnungszeiten | EWAG / E. Widmer AG Suhr",
            "Kontakt, 24h-Pikettdienst 062 855 08 80, Öffnungszeiten und Standort Tramstrasse 47, 5034 Suhr.",
            build_kontakt(mode, folder_name),
        ),
        "impressum.html": (
            "Impressum | EWAG / E. Widmer AG Suhr",
            "Gesetzliche Angaben der EWAG / E. Widmer AG, Tramstrasse 47, 5034 Suhr.",
            build_impressum(),
        ),
        "datenschutz.html": (
            "Datenschutzerklärung | EWAG / E. Widmer AG Suhr",
            "Datenschutzerklärung gemäss Schweizer Datenschutzgesetz (DSG) für EWAG / E. Widmer AG.",
            build_datenschutz(),
        ),
    }

    for fname, (ptitle, pdesc, pbody) in pages.items():
        html_str = wrap_page(ptitle, pdesc, fname, pbody, mode, public_slug, folder_name)
        (out_dir / fname).write_text(html_str, encoding="utf-8")

    print(f"Generated {len(pages)} pages in {out_dir}")


if __name__ == "__main__":
    generate_variant("preview-ewagsuhr-original", "ewagsuhr-original", "original", "1:1 Original-Übernahme")
    generate_variant("preview-ewagsuhr-modern", "ewagsuhr-modern", "modern", "1:1 Modern-Tweak")

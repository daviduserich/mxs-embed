#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator-First WebPilot Showcase für Free's — Studio für Textildesign, Textildruck & Stickerei
URL: https://www.frees.ch/
Erzeugt deterministisch beide Varianten:
  1. Komplettversion: preview-frees/ (index.html, dienstleistungen.html, textilsortiment.html, profil.html, kontakt.html + before.json + cockpit.html)
  2. Zeigeversion (Vorschau-Entwurf): preview-frees-v2/ (index.html, kontakt.html + before.json + cockpit.html)

Strikte Einhaltung von:
  - #UI-01..#UI-14 (Barlow + Plus Jakarta Sans, Barlow Display Standard, 100% Lucide SVGs, 0 Emojis, 2-Radien 4px/8px)
  - #UI-03 Kunden-Sprache (0 Hausbau- oder Entwickler-Fachbegriffe)
  - #LANG-01..#LANG-02 (100% Schweizer Rechtschreibung ss statt Eszett)
"""

import json
import shutil
import subprocess
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
V1_DIR = BASE_DIR / "preview-frees"
V2_DIR = BASE_DIR / "preview-frees-v2"
V1_DIR.mkdir(parents=True, exist_ok=True)
V2_DIR.mkdir(parents=True, exist_ok=True)

# 1. Vollständige Redesign-Inventur (before.json — 0 Datenverlust)
BEFORE_INVENTORY = {
    "source_url": "https://www.frees.ch/",
    "crawled_at": "2026-11-03",
    "company": {
        "brand_name": "Free's — Studio für Textildesign, Textildruck & Stickerei",
        "legal_name": "Free's Stefan Fritschi, Teamsport-Promowear & Print",
        "claim": "Kreative Lösungen für Ihre Designwünsche",
        "motto": "Wir organisieren Wünsche",
        "owners_and_contacts": [
            {"name": "Stefan Fritschi", "role": "Inhaber · Textildesign, Beratung, Druck & Stickerei", "phone": "+41 79 709 12 24"},
            {"name": "Raimondo", "role": "Beratung, Produktion & Textilveredelung", "phone": "+41 79 966 59 78"}
        ],
        "address": {
            "street": "Mellingerstrasse 12",
            "addition": "Eingang C, 1. Stock",
            "zip": "5443",
            "city": "Niederrohrdorf",
            "canton": "Aargau",
            "country": "Schweiz"
        },
        "contact": {
            "phone_primary": "+41 79 709 12 24",
            "phone_secondary": "+41 79 966 59 78",
            "email": "info@frees.ch",
            "opening_hours": "Nach Vereinbarung via Mail oder Telefon.",
            "online_shop": "https://frees.alltextiles.ch"
        },
        "design_tokens_original": {
            "fonts": ["Barlow", "Plus Jakarta Sans"],
            "colors": {
                "charcoal_dark": "#181818",
                "crimson_red": "#E12321",
                "crimson_dark": "#981614",
                "white": "#FFFFFF"
            }
        }
    },
    "story_original": (
        "Seit meiner Ausbildung arbeite ich mit Textilien zusammen. Viele Jahre in der Welt der Sportartikel, "
        "zuerst im Detailhandel danach im Vertrieb und Grosshandel. In dieser Zeit durfte ich meine erste Erfahrung "
        "im Textildruck erschaffen. Als eine Anfrage eines lokalen Sportvereins kam kaufte ich mir meine ersten "
        "Druckmaschinen. Zuerst in einem Hobbyraum, später im eigenen Ladenlokal wurden die Textilien bedruckt. "
        "Das Textilsortiment wurde stetig erweitert. Im März 2016 durfte ich mein Wunschlokal beziehen und konnte "
        "dank mehr Platz auch das Sortiment um Arbeitsbekleidung erweitern. — Stefan Fritschi"
    ),
    "services_original": [
        {
            "id": "textildruck",
            "title": "Textildruck in allen Auflagen & Farben",
            "summary": (
                "Free's bietet dem Kunden verschiedene Produkte und Dienstleistungen an, welche Ihnen erlauben, "
                "sich individuell zu präsentieren. Wir bedrucken T-Shirts, Sweatshirts, Hemden, Schürzen, Sporttaschen, "
                "Jacken und vieles mehr in allen Auflagen und Farben. Gemeinsam mit Ihnen bestimmen wir die optimale "
                "Drucktechnik für Ihre Auflage und den gewünschten Druckumfang. Getreu dem Original und Ihren Vorstellungen "
                "setzen wir dann Ihren Druck um."
            )
        },
        {
            "id": "stickerei-labels",
            "title": "Stickereien, gewobene & gestickte Labels",
            "summary": (
                "Ob edle Direktstickerei auf Winterjacken, Polos und Hemden oder hochwertige gewobene und gestickte "
                "Labels und Abzeichen: Wir veredeln Ihre Textilien langlebig, waschbeständig und repräsentativ zu "
                "günstigen Konditionen."
            )
        },
        {
            "id": "arbeitskleidung-corporate",
            "title": "Arbeitskleidung, Corporate Fashion & Vereinsbekleidung",
            "summary": (
                "Unser Sortiment reicht von robuster Arbeitskleidung und Corporate Fashion über T-Shirts und Polo-Shirts "
                "bis hin zu Business-Hemden, Vereins-Trikots und Trainingsanzügen. Unser Angebot richtet sich an Firmen, "
                "Vereine und Privatpersonen."
            )
        },
        {
            "id": "kundenservice-angeliefert",
            "title": "Veredelung angelieferter Textilien & Beratung («Wir organisieren Wünsche»)",
            "summary": (
                "Seit über 12 Jahren bedrucken wir Textilien aller Art mit bester Druckqualität zum bestmöglichen Preis. "
                "Bei uns erwarten Sie umfassende Dienstleistungen aus einer Hand — auch angelieferte Textilien veredeln wir "
                "gerne für Sie. Wir begleiten Sie von der ersten Beratung bis zum fertigen Produkt."
            )
        }
    ],
    "catalogs": [
        {"id": "katalog-01", "name": "Free's Online-Textilshop (alltextiles.ch)", "category": "Hauptkatalog · Online-Shop", "url": "https://frees.alltextiles.ch", "image": "images/katalog-01-alltextiles.jpg", "desc": "Direkter Zugriff auf tausende Textilien: T-Shirts, Polos, Hoodies, Caps, Taschen und Basics in allen Farben und Grössen."},
        {"id": "katalog-02", "name": "JAKO Teamsport Katalog 2026 (CH-DE)", "category": "Teamsport & Vereine", "url": "https://cdn.jako.de/userdata/files/blaetterkatalog/TS_2026_CHD/", "image": "images/katalog-02-jako.png", "desc": "Komplette Vereinsausrüstung, Trikotsätze, Trainingsanzüge, Regenjacken und Sporttaschen mit langfristiger Nachliefergarantie."},
        {"id": "katalog-03", "name": "ERIMA Teamsport Katalog 2026 (CH-DE)", "category": "Teamsport & Vereine", "url": "https://katalog.erima.de/erima-teamsport-2026-chd/70859746", "image": "images/katalog-03-erima.png", "desc": "Hochwertige Teamsport-Kollektionen für Fussball, Handball, Turnvereine und Einzelsportler in Vereinsfarben."},
        {"id": "katalog-04", "name": "F. ENGEL Workwear Katalog", "category": "Arbeitskleidung & Handwerk", "url": "https://ipaper.f-engel.com/engel-workwear/catalogue/de/", "image": "images/katalog-04-engel.jpg", "desc": "Professionelle Arbeitskleidung, Bundhosen, Stretch-Workwear und zertifizierte Warnschutzbekleidung für Bau und Gewerbe."},
        {"id": "katalog-05", "name": "CLIQUE Basic & Corporate 2025 (Swiss DE)", "category": "Corporate Fashion & Promotion", "url": "https://viewer.joomag.com/clique-2025-swiss-de/0670840001736783204?short&", "image": "images/katalog-05-clique.png", "desc": "Bewährte Promotion- und Firmentextilien: Polos, Sweatshirts, Softshelljacken und Basics in riesiger Farbpalette."},
        {"id": "katalog-06", "name": "CRAFT Teamwear SS26", "category": "Teamsport & Performance", "url": "https://viewer.joomag.com/craft-teamwear-ss26/0865151001768297519?short&", "image": "images/katalog-06-craft.jpg", "desc": "Skandinavische Funktionsbekleidung für Vereine, Laufgruppen, Radsport und sportliche Firmen-Events."},
        {"id": "katalog-07", "name": "New Wave Corporate Catalogue SS26 (CH)", "category": "Corporate Fashion 2026", "url": "https://viewer.joomag.com/corporate-catalogue-ss26-ch-web/0883053001768387748?short&", "image": "images/katalog-07-newwave-corporate.png", "desc": "Die neueste Schweizer Frühjahr-/Sommer-Kollektion 2026 für einheitliche Mitarbeiter- und Eventbekleidung."},
        {"id": "katalog-08", "name": "PRINTER Prime & Red 2025 (CH-DE)", "category": "Arbeitskleidung & Teamwear", "url": "https://viewer.joomag.com/printer2025-ch-de/0370164001737063540?short&", "image": "images/katalog-08-printer.jpg", "desc": "Waschbeständige Arbeits- und Teamtextilien (bis 60 Grad waschbar) mit starkem Preis-Leistungs-Verhältnis."},
        {"id": "katalog-09", "name": "James Harvest Sportswear 2025 (CH-DE)", "category": "Premium Corporate Sportswear", "url": "https://viewer.joomag.com/harvest2025-ch-de-final/0939210001736415669?short&", "image": "images/katalog-09-james-harvest.png", "desc": "Exklusive Polos, Chinos, Strickwaren und Jacken für einen erstklassigen Auftritt auf Messen und im Kundenkontakt."},
        {"id": "katalog-10", "name": "HAKRO Activewear Katalog", "category": "Qualitäts-Textilien für KMU", "url": "https://www.yumpu.com/s/hVY9MNCvzADs8r6m", "image": "images/katalog-10-hakro.jpg", "desc": "Langlebige Premium-Textilien für Handwerk, Industrie, Praxis, Gastronomie und Dienstleistung."},
        {"id": "katalog-11", "name": "Corporate Catalogue SS25", "category": "Corporate & Event Wear", "url": "https://viewer.joomag.com/corporate-catalogue-ss25-web/0904387001733295937?short&", "image": "images/katalog-11-corporate-ss25.jpg", "desc": "Vielseitige Kollektionen für Firmenauftritte, Vereinsjubiläen und Promotion-Aktionen."},
        {"id": "katalog-12", "name": "PROJOB Workwear 2025 (Swiss DE)", "category": "Schwedische Berufsbekleidung", "url": "https://viewer.joomag.com/2025-projob-workwear-swissde/0012870001740134567?short&", "image": "images/katalog-12-projob.jpg", "desc": "Ergonomische Workwear für Bau, Montage, Transport, Logistik, Service und Küche."},
        {"id": "katalog-13", "name": "J. Harvest & Frost 2025 (CH-DE)", "category": "Business-Hemden & Blusen", "url": "https://viewer.joomag.com/jharvestfrost2025-ch-de-final/0352901001736415642?short&", "image": "images/katalog-13-jharvest-frost.png", "desc": "Feinste Business-Hemden, Blusen und Corporate Tailoring — ideal für dezente Kragen- oder Bruststickerei."},
        {"id": "katalog-14", "name": "WIKLAND Schweizer Berufsbekleidung", "category": "Schweizer Workwear-Tradition", "url": "http://www.wikland.ch", "image": "images/katalog-14-wikland.png", "desc": "Bewährte Schweizer Arbeits-, Wetterschutz- und Zunftbekleidung für höchste Beanspruchung."}
    ]
}

for d in (V1_DIR, V2_DIR):
    (d / "before.json").write_text(json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 2. Mandanten-Metadaten (company.json, config.json, site.json)
COMMON_COMPANY = {
    "name": "Free's Textildesign & Textildruck",
    "company_name": "Free's — Studio für Textildesign, Textildruck & Stickerei",
    "legal_name": "Free's Stefan Fritschi, Teamsport-Promowear & Print",
    "short_name": "Free's",
    "claim": "Kreative Lösungen für Ihre Designwünsche",
    "subline": "Textildruck, Stickerei, Arbeitskleidung & Teamsport aus Niederrohrdorf",
    "street": "Mellingerstrasse 12, Eingang C, 1. Stock",
    "zip": "5443",
    "city": "Niederrohrdorf",
    "canton": "AG",
    "country": "Schweiz",
    "email": "info@frees.ch",
    "phone": "+41 79 709 12 24",
    "phone_secondary": "+41 79 966 59 78",
    "phone_clean": "+41797091224",
    "website": "https://www.frees.ch",
    "industry": "Textildruck, Stickerei, Arbeitskleidung & Teamsport",
    "industry_id": "universal_swiss_kmu",
    "industry_label": "Schweizer Studio für Textildesign, Textildruck, Stickerei & Berufsbekleidung",
    "work_category_label": "Textildruck, Stickerei & Kataloge",
    "studio_title": "WEBPILOT STUDIO",
    "is_website_studio": True,
    "copyright": "© 2026 Free's Stefan Fritschi (CH-5443 Niederrohrdorf). Alle Rechte vorbehalten.",
    "hosting_status": "Live-Betrieb & Hosting: Schweizer Edge · WebPilot Studio v4.0",
}

v1_comp = dict(COMMON_COMPANY, slug="frees", host_url="https://vorschau.magnet-xs.ch/frees/cockpit?token=frees2026", host_jobs_url="https://vorschau.magnet-xs.ch/frees/")
v1_cfg = dict(v1_comp, preview_url="https://vorschau.magnet-xs.ch/frees/", cockpit_token="frees2026", template="textil-design-flagship-v1", pages=["index.html", "dienstleistungen.html", "textilsortiment.html", "profil.html", "kontakt.html"])
v1_site = {"slug": "preview-frees", "public_slug": "frees", "token": "frees2026", "name": "Free's — Studio für Textildesign, Textildruck & Stickerei", "Updated": "2026-11-03", "PagesCount": 5, "CatalogsCount": 14}

v2_comp = dict(COMMON_COMPANY, slug="frees-v2", name="Free's (Zeigeversion)", host_url="https://vorschau.magnet-xs.ch/frees-v2/cockpit?token=frees2026", host_jobs_url="https://vorschau.magnet-xs.ch/frees-v2/")
v2_cfg = dict(v2_comp, preview_url="https://vorschau.magnet-xs.ch/frees-v2/", cockpit_token="frees2026", template="textil-design-preview-v2", pages=["index.html", "kontakt.html"])
v2_site = {"slug": "preview-frees-v2", "public_slug": "frees-v2", "token": "frees2026", "name": "Free's (Zeigeversion / Vorschau-Entwurf)", "Updated": "2026-11-03", "PagesCount": 2, "CatalogsCount": 14}

(V1_DIR / "company.json").write_text(json.dumps(v1_comp, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
(V1_DIR / "config.json").write_text(json.dumps(v1_cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
(V1_DIR / "site.json").write_text(json.dumps(v1_site, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

(V2_DIR / "company.json").write_text(json.dumps(v2_comp, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
(V2_DIR / "config.json").write_text(json.dumps(v2_cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
(V2_DIR / "site.json").write_text(json.dumps(v2_site, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

SHARED_CSS = """
    :root {
      --charcoal: #222221;
      --charcoal-deep: #151514;
      --charcoal-mid: #3A3A39;
      --gold: #F9B231;
      --gold-hover: #FBBF24;
      --gold-dark: #9A5800;
      --gold-soft: #FEF7E6;
      --gold-border: #F5C451;
      --crimson: #D6201E;
      --crimson-bright: #E12321;
      --crimson-dark: #991B1B;
      --crimson-soft: #FEF2F2;
      --crimson-border: #FCA5A5;
      --green: #15803D;
      --green-soft: #DCFCE7;
      --bg-page: #F9FAFB;
      --bg-card: #FFFFFF;
      --bg-Warm: #F4F3EF;
      --text-main: #181817;
      --text-body: #374151;
      --text-muted: #4B5563;
      --border-light: #E5E7EB;
      --border-strong: #D1D5DB;
      --radius-sm: 4px;
      --radius-md: 8px;
      --shadow-sm: 0 2px 10px rgba(24, 24, 23, 0.05);
      --shadow-md: 0 12px 30px rgba(24, 24, 23, 0.09);
      --shadow-lg: 0 20px 44px rgba(24, 24, 23, 0.16);
      --container: 1180px;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    ::selection {
      background-color: rgba(225, 35, 33, 0.22);
      color: #181817;
    }

    html {
      scroll-behavior: smooth;
      font-size: 16px;
      overflow-x: hidden;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      color: var(--text-main);
      background-color: var(--bg-page);
      line-height: 1.62;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
      font-variant-numeric: tabular-nums;
    }

    img {
      max-width: 100%;
      height: auto;
      display: block;
    }

    a {
      color: inherit;
      text-decoration: none;
      transition: color 0.18s ease, background-color 0.18s ease, border-color 0.18s ease, transform 0.18s ease;
    }

    ul {
      list-style: none;
    }

    .container {
      width: 100%;
      max-width: var(--container);
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Freistehende Marken-Kicker (#UI-01: Barlow Bold, Barlow Display Standard) */
    .section-kicker {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-family: 'Barlow', sans-serif;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--crimson-dark);
      background: transparent !important;
      border: none !important;
      padding: 0 !important;
      box-shadow: none !important;
      margin-bottom: 12px;
    }
    .section-kicker::before {
      content: "";
      display: inline-block;
      width: 16px;
      height: 2px;
      background-color: var(--crimson-bright);
      border-radius: 0px;
      flex-shrink: 0;
    }
    .section-kicker.kicker-light {
      color: var(--gold);
    }
    .section-kicker.kicker-light::before {
      background-color: var(--crimson-bright);
    }

    h1, h2, h3, h4 {
      font-family: 'Barlow', sans-serif;
      color: var(--text-main);
      line-height: 1.18;
      letter-spacing: -0.015em;
    }

    .section-head {
      max-width: 780px;
      margin-bottom: 44px;
    }
    .section-title {
      font-size: clamp(1.85rem, 3.1vw, 2.55rem);
      font-weight: 800;
      margin-bottom: 14px;
    }
    .section-desc {
      font-size: 1.03rem;
      color: var(--text-body);
      line-height: 1.65;
    }

    section {
      padding: 80px 0;
      position: relative;
    }

    /* 1-Klick-Versions-Umschalter oben (V1 <-> V2 + Cockpit) */
    .wp-version-bar {
      background-color: var(--charcoal-deep);
      color: #F9FAFB;
      border-bottom: 2px solid var(--crimson-bright);
      font-size: 0.8rem;
      position: relative;
      z-index: 1003;
      padding: 9px 0;
    }
    .wp-version-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      flex-wrap: wrap;
    }
    .wp-version-info {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      font-size: 0.8rem;
      font-weight: 600;
      color: #E5E7EB;
    }
    .wp-version-pill-group {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .wp-ver-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      font-family: 'Barlow', sans-serif;
      font-size: 0.76rem;
      font-weight: 700;
      padding: 6px 12px;
      min-height: 36px;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(255, 255, 255, 0.22);
      background-color: rgba(255, 255, 255, 0.07);
      color: #F3F4F6;
      line-height: 1.25;
    }
    .wp-ver-btn.is-active {
      background-color: var(--gold);
      color: #161615;
      border-color: var(--gold);
      font-weight: 800;
    }
    .wp-ver-btn.is-switch {
      border-color: var(--gold);
      color: var(--gold);
      background-color: rgba(249, 178, 49, 0.12);
    }
    .wp-ver-btn.is-switch:hover {
      background-color: var(--gold);
      color: #161615;
    }
    .wp-ver-btn.is-cockpit {
      background-color: rgba(255, 255, 255, 0.12);
      border-color: rgba(255, 255, 255, 0.32);
      color: #FFFFFF;
    }
    .wp-ver-btn.is-cockpit:hover {
      background-color: #FFFFFF;
      color: #161615;
    }

    /* Sub-Topbar (Standort Niederrohrdorf & Direktkontakt) */
    .top-bar {
      background-color: var(--charcoal);
      color: #E5E7EB;
      font-size: 0.78rem;
      padding: 8px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }
    .top-bar-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }
    .top-bar-left {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .top-bar-badge {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background-color: rgba(249, 178, 49, 0.18);
      color: var(--gold);
      border: 1px solid rgba(249, 178, 49, 0.45);
      font-family: 'Barlow', sans-serif;
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
    }
    .top-bar-links {
      display: flex;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }
    .top-bar-links a {
      color: #E5E7EB;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-height: 34px;
      padding: 5px 8px;
    }
    .top-bar-links a:hover {
      color: var(--gold);
    }

    /* Sticky Main Header */
    .site-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background-color: rgba(255, 255, 255, 0.97);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border-light);
      box-shadow: 0 2px 12px rgba(24, 24, 23, 0.04);
    }
    .header-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 18px;
      min-height: 76px;
      padding: 8px 0;
    }
    .brand-link {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      flex-shrink: 0;
    }
    .brand-logo {
      width: 118px;
      height: 44px;
      object-fit: contain;
      border-radius: var(--radius-sm);
      flex-shrink: 0;
    }
    .brand-text {
      display: flex;
      flex-direction: column;
    }
    .brand-name {
      font-family: 'Barlow', sans-serif;
      font-size: 1.12rem;
      font-weight: 800;
      color: var(--charcoal);
      letter-spacing: -0.01em;
      line-height: 1.15;
    }
    .brand-sub {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--crimson-dark);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-top: 2px;
    }

    .main-nav {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }
    .nav-link {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'Barlow', sans-serif;
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text-body);
      padding: 8px 12px;
      min-height: 38px;
      border-radius: var(--radius-sm);
      border: 1px solid transparent;
      background: transparent;
      cursor: pointer;
    }
    .nav-link:hover,
    .nav-link.active {
      color: var(--charcoal-deep);
      background-color: var(--crimson-soft);
      border-color: var(--crimson-border);
    }
    .nav-link-preview {
      color: var(--text-muted);
      background-color: #F3F4F6;
      border: 1px dashed #9CA3AF;
      font-size: 0.82rem;
    }
    .nav-link-preview:hover {
      color: var(--charcoal-deep);
      background-color: var(--gold-soft);
      border-color: var(--gold-dark);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }

    /* Buttons (#UI-01: 8px radius, high contrast) */
    .btn-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      font-family: 'Barlow', sans-serif;
      font-size: 0.92rem;
      font-weight: 700;
      padding: 12px 20px;
      min-height: 44px;
      border-radius: var(--radius-md);
      border: 1px solid transparent;
      cursor: pointer;
      text-align: center;
      line-height: 1.25;
      transition: all 0.18s ease;
    }
    .btn-cta svg {
      flex-shrink: 0;
    }
    .btn-cta-gold {
      background-color: var(--gold);
      color: #161615;
      border-color: var(--gold);
      font-weight: 800;
    }
    .btn-cta-gold:hover {
      background-color: var(--gold-hover);
      color: #161615;
      transform: translateY(-1px);
    }
    .btn-cta-primary {
      background-color: var(--charcoal);
      color: #FFFFFF;
      border-color: var(--charcoal);
    }
    .btn-cta-primary:hover {
      background-color: var(--charcoal-deep);
      color: var(--gold);
      border-color: var(--charcoal-deep);
    }
    .btn-cta-outline {
      background-color: #FFFFFF;
      color: var(--charcoal);
      border-color: var(--border-strong);
    }
    .btn-cta-outline:hover {
      border-color: var(--charcoal);
      background-color: var(--bg-Warm);
    }
    .btn-cta-outline-light {
      background-color: rgba(255, 255, 255, 0.08);
      color: #FFFFFF;
      border-color: rgba(255, 255, 255, 0.28);
    }
    .btn-cta-outline-light:hover {
      background-color: rgba(255, 255, 255, 0.16);
      border-color: var(--gold);
    }
    .btn-sm {
      font-size: 0.84rem;
      padding: 9px 15px;
      min-height: 40px;
    }

    /* Mobile Burger & Drawer */
    .mobile-toggle {
      display: none;
      width: 44px;
      height: 44px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-strong);
      background-color: #FFFFFF;
      color: var(--charcoal);
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }
    .mobile-drawer {
      display: none;
      flex-direction: column;
      gap: 8px;
      padding: 16px 24px 22px;
      background-color: var(--charcoal-deep);
      border-top: 1px solid rgba(255, 255, 255, 0.12);
    }
    .mobile-drawer.open {
      display: flex;
    }
    .mobile-drawer a,
    .mobile-drawer button.mobile-nav-btn {
      font-family: 'Barlow', sans-serif;
      font-size: 0.95rem;
      font-weight: 700;
      color: #F9FAFB;
      padding: 12px 14px;
      min-height: 44px;
      border-radius: var(--radius-sm);
      background-color: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      text-align: left;
      width: 100%;
      cursor: pointer;
    }
    .mobile-drawer button.mobile-nav-btn {
      color: var(--gold);
      border-style: dashed;
      border-color: rgba(249, 178, 49, 0.55);
    }

    /* Hero Section */
    .hero-section {
      background-color: var(--charcoal-deep);
      color: #FFFFFF;
      padding: 72px 0 84px;
      border-bottom: 4px solid var(--crimson-bright);
      overflow: hidden;
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1.12fr 0.88fr;
      gap: 44px;
      align-items: center;
    }
    .hero-title {
      font-size: clamp(2.15rem, 3.8vw, 3.2rem);
      font-weight: 800;
      color: #FFFFFF;
      line-height: 1.12;
      margin-bottom: 18px;
    }
    .hero-title span {
      color: var(--gold);
    }
    .hero-lead {
      font-size: 1.06rem;
      color: #E5E7EB;
      line-height: 1.68;
      margin-bottom: 26px;
    }
    .hero-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 28px;
    }
    .hero-badges {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
    }
    .hero-badge-card {
      background-color: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-left: 3px solid var(--gold);
      border-radius: var(--radius-sm);
      padding: 10px 14px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 2px;
    }
    .hero-badge-val {
      font-family: 'Barlow', sans-serif;
      font-size: 0.92rem;
      font-weight: 800;
      color: var(--gold);
    }
    .hero-badge-lbl {
      font-size: 0.78rem;
      color: #D1D5DB;
      line-height: 1.35;
    }

    .hero-media-card {
      background-color: var(--charcoal);
      border: 1px solid rgba(255, 255, 255, 0.16);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-lg);
    }
    .hero-media-card img {
      width: 100%;
      height: 360px;
      object-fit: contain;
      object-position: center;
      background-color: #FFFFFF;
      padding: 14px;
    }
    .hero-media-card img.cover-img {
      object-fit: cover;
      padding: 0;
      background-color: var(--charcoal);
    }
    .hero-media-caption {
      padding: 16px 20px;
      background-color: #1E1E1D;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }

    /* Universal Symmetric Grids (#UI-14: Zero Ragged Edges & Equal Height) */
    .grid-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 28px;
      align-items: stretch;
    }
    .grid-2 > :last-child:nth-child(odd) {
      grid-column: 1 / -1;
    }

    /* Cards */
    .content-card {
      background-color: var(--bg-card);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 28px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 18px;
      height: 100%;
    }
    .content-card.card-accent-top {
      border-top: 4px solid var(--crimson-bright);
    }
    .content-card.card-dark {
      background-color: var(--charcoal-deep);
      color: #F9FAFB;
      border-color: rgba(255, 255, 255, 0.14);
    }
    .content-card.card-dark h3 {
      color: #FFFFFF;
    }

    .card-badge-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 10px;
    }
    .meta-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'Barlow', sans-serif;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      background-color: var(--gold-soft);
      color: var(--gold-dark);
      border: 1px solid var(--gold-border);
    }
    .icon-box {
      width: 40px;
      height: 40px;
      border-radius: var(--radius-sm);
      background-color: var(--charcoal);
      color: var(--gold);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .check-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-top: 8px;
    }
    .check-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.92rem;
      color: var(--text-body);
      line-height: 1.5;
    }
    .check-item svg {
      color: var(--crimson-dark);
      flex-shrink: 0;
      margin-top: 3px;
    }
    .card-dark .check-item {
      color: #E5E7EB;
    }
    .card-dark .check-item svg {
      color: var(--gold);
    }

    /* Pillar & Catalog Media Cards */
    .pillar-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }
    .pillar-img-wrap {
      width: 100%;
      height: 210px;
      overflow: hidden;
      background-color: var(--charcoal);
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .pillar-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center;
    }
    .pillar-img-wrap.logo-stage {
      background-color: #FFFFFF;
      border-bottom: 1px solid var(--border-light);
      padding: 20px;
      height: 170px;
    }
    .pillar-img-wrap.logo-stage img {
      object-fit: contain;
    }
    .pillar-body {
      padding: 24px 26px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex: 1;
      gap: 16px;
    }

    /* V2 Vorschau-Entwurf (Zeigeversion) Spezifische Styles (#UI-03 Kunden-Sprache) */
    .preview-scope-section {
      background-color: #EFECE6;
      border-top: 2px dashed var(--charcoal-mid);
      border-bottom: 2px dashed var(--charcoal-mid);
      padding: 76px 0 88px;
    }
    .preview-scope-banner {
      background-color: var(--charcoal-deep);
      color: #F9FAFB;
      border: 2px dashed var(--gold);
      border-radius: var(--radius-md);
      padding: 28px 30px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-md);
    }
    .preview-module-card {
      background-color: #FFFFFF;
      border: 2px dashed #6B7280;
      border-radius: var(--radius-md);
      padding: 26px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 18px;
      box-shadow: var(--shadow-sm);
      height: 100%;
    }
    .preview-status-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: var(--gold-soft);
      border: 1px solid var(--gold-border);
      color: var(--gold-dark);
      font-family: 'Barlow', sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
    }

    /* Footer */
    .site-footer {
      background-color: var(--charcoal-deep);
      color: #E5E7EB;
      padding: 68px 0 36px;
      border-top: 4px solid var(--crimson-bright);
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 1.3fr 1fr 1fr 1.1fr;
      gap: 36px;
      padding-bottom: 42px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    }
    .footer-title {
      font-family: 'Barlow', sans-serif;
      font-size: 0.94rem;
      font-weight: 800;
      color: #FFFFFF;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 16px;
    }
    .footer-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .footer-list a,
    .footer-list button {
      color: #D1D5DB;
      font-size: 0.88rem;
      background: none;
      border: none;
      text-align: left;
      cursor: pointer;
      font-family: inherit;
      padding: 5px 0;
      min-height: 34px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .footer-list a:hover,
    .footer-list button:hover {
      color: var(--gold);
    }
    .footer-bottom {
      padding-top: 26px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      font-size: 0.82rem;
      color: #9CA3AF;
    }
    .footer-bottom a {
      display: inline-flex;
      align-items: center;
      min-height: 34px;
      padding: 4px 0;
    }

    /* Modals (#wpBlueprintModal & #wpImpressumModal) */
    .wp-modal-backdrop {
      position: fixed;
      inset: 0;
      background-color: rgba(15, 15, 14, 0.76);
      backdrop-filter: blur(4px);
      z-index: 9998;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
      overflow-y: auto;
    }
    .wp-modal-backdrop.open {
      display: flex;
    }
    .wp-modal-dialog {
      background-color: #FFFFFF;
      color: var(--text-main);
      border: 2px solid var(--gold);
      border-radius: var(--radius-md);
      max-width: 650px;
      width: 100%;
      padding: 28px;
      position: relative;
      box-shadow: var(--shadow-lg);
      max-height: 90vh;
      overflow-y: auto;
    }
    .wp-modal-close {
      position: absolute;
      top: 16px;
      right: 16px;
      width: 38px;
      height: 38px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-strong);
      background-color: var(--bg-page);
      color: var(--charcoal);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }
    .wp-modal-checklist {
      background-color: var(--bg-page);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .wp-modal-check-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.86rem;
      color: var(--text-body);
    }
    .wp-modal-check-item svg {
      color: var(--crimson-dark);
      flex-shrink: 0;
      margin-top: 2px;
    }

    /* 3-Schritte Smart-Anfrage Assistent (kontakt.html) */
    .contact-layout {
      display: grid;
      grid-template-columns: 0.88fr 1.12fr;
      gap: 38px;
      align-items: start;
    }
    .contact-info-panel {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 28px;
      box-shadow: var(--shadow-sm);
    }
    .contact-direct-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-top: 20px;
    }
    .contact-direct-item {
      padding: 12px 14px;
      background-color: var(--bg-page);
      border: 1px solid var(--border-light);
      border-left: 3px solid var(--crimson-bright);
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
    }
    .contact-direct-role {
      font-family: 'Barlow', sans-serif;
      font-size: 0.74rem;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--crimson-dark);
      letter-spacing: 0.04em;
    }
    .contact-direct-person {
      font-weight: 700;
      color: var(--charcoal);
      margin-top: 2px;
    }
    .contact-direct-links {
      color: var(--text-body);
      font-size: 0.82rem;
      margin-top: 2px;
    }

    .wizard-card {
      background-color: #FFFFFF;
      border: 2px solid var(--charcoal);
      border-radius: var(--radius-md);
      padding: 30px;
      box-shadow: var(--shadow-md);
    }
    .wp-stepper {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin-bottom: 22px;
      padding: 6px;
      background-color: var(--bg-Warm);
      border-radius: var(--radius-md);
    }
    .wp-step-pill {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 10px 8px;
      border-radius: var(--radius-sm);
      font-family: 'Barlow', sans-serif;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--text-muted);
      text-align: center;
    }
    .wp-step-pill.active {
      background-color: var(--charcoal);
      color: var(--gold);
    }
    .wp-step-pill.done {
      background-color: var(--green-soft);
      color: #166534;
    }
    .wp-step-num {
      width: 22px;
      height: 22px;
      border-radius: var(--radius-sm);
      background-color: rgba(255, 255, 255, 0.16);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.74rem;
      font-weight: 800;
      flex-shrink: 0;
    }

    .wp-step-pane {
      display: none;
    }
    .wp-step-pane.active {
      display: block;
    }

    .wp-role-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-bottom: 20px;
      align-items: stretch;
    }
    .wp-role-tile {
      background-color: var(--bg-page);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-md);
      padding: 14px;
      text-align: left;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 8px;
      transition: all 0.18s ease;
      font-family: inherit;
      min-height: 92px;
    }
    .wp-role-tile:hover {
      border-color: var(--charcoal);
      background-color: #FFFFFF;
    }
    .wp-role-tile.selected {
      border: 2px solid var(--charcoal);
      background-color: var(--gold-soft);
    }
    .wp-role-head {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .wp-role-icon {
      width: 28px;
      height: 28px;
      border-radius: var(--radius-sm);
      background-color: var(--charcoal);
      color: var(--gold);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .wp-role-title {
      font-family: 'Barlow', sans-serif;
      font-size: 0.88rem;
      font-weight: 800;
      color: var(--charcoal);
      line-height: 1.25;
    }
    .wp-role-desc {
      font-size: 0.77rem;
      color: var(--text-body);
      line-height: 1.42;
    }

    .form-grid-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
      align-items: stretch;
    }
    .form-field {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 6px;
    }
    .form-label {
      font-family: 'Barlow', sans-serif;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--charcoal);
      line-height: 1.3;
    }
    .form-input,
    .form-textarea {
      width: 100%;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.9rem;
      color: var(--text-main);
      background-color: #FFFFFF;
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-sm);
      padding: 11px 14px;
      min-height: 44px;
    }
    .form-input:focus,
    .form-textarea:focus {
      outline: none;
      border-color: var(--charcoal);
      box-shadow: 0 0 0 3px rgba(249, 178, 49, 0.25);
    }
    .form-textarea {
      min-height: 100px;
      resize: vertical;
    }

    .wp-upload-zone {
      border: 1px dashed var(--border-strong);
      background-color: var(--bg-page);
      border-radius: var(--radius-md);
      padding: 14px;
    }
    .wp-upload-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 14px;
      min-height: 42px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-strong);
      background-color: #FFFFFF;
      font-family: 'Barlow', sans-serif;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--charcoal);
      cursor: pointer;
    }
    .wp-photo-thumbs {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 10px;
    }
    .wp-thumb-item {
      position: relative;
      width: 72px;
      height: 72px;
      border-radius: var(--radius-sm);
      overflow: hidden;
      border: 1px solid var(--border-strong);
    }
    .wp-thumb-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .wp-thumb-remove {
      position: absolute;
      top: 2px;
      right: 2px;
      width: 22px;
      height: 22px;
      background-color: var(--charcoal);
      color: #FFFFFF;
      border: none;
      border-radius: var(--radius-sm);
      font-size: 0.72rem;
      cursor: pointer;
    }

    .wp-plz-badge {
      display: none;
      align-items: center;
      gap: 8px;
      margin-top: 6px;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      font-size: 0.78rem;
      font-weight: 600;
    }
    .wp-plz-badge.in-area {
      display: flex;
      background-color: var(--green-soft);
      color: #166534;
      border: 1px solid #86EFAC;
    }

    .wp-selftest-banner {
      background-color: var(--gold-soft);
      border: 1px solid var(--gold-border);
      border-left: 4px solid var(--gold-dark);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      font-size: 0.8rem;
      color: #78350F;
      margin-bottom: 16px;
    }

    .wp-success-box {
      display: none;
      flex-direction: column;
      gap: 16px;
      padding: 24px;
      background-color: var(--bg-page);
      border: 2px solid var(--green);
      border-radius: var(--radius-md);
    }
    .wp-success-box.visible {
      display: flex;
    }
    .wp-wa-preview {
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.82rem;
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-left: 4px solid var(--green);
      padding: 12px 14px;
      border-radius: var(--radius-sm);
      white-space: pre-wrap;
      color: var(--text-main);
    }


    /* Supplemental Component Styles (#UI-01..#UI-14) */
    :root {
      --brand-primary: #991B1B;
      --text-primary: #181817;
      --text-secondary: #374151;
      --bg-muted: #F3F4F6;
      --border-subtle: #E5E7EB;
      --radius-card: 8px;
      --radius-btn: 8px;
      --font-display: 'Barlow', sans-serif;
    }
    .btn-cta-white {
      background-color: #FFFFFF;
      color: #181817;
      border-color: #FFFFFF;
      font-weight: 800;
    }
    .btn-cta-white:hover {
      background-color: var(--gold);
      color: #161615;
      border-color: var(--gold);
    }
    .hero-eyebrow,
    .section-eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: 'Barlow', sans-serif;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--gold);
      margin-bottom: 12px;
    }
    .section-eyebrow {
      color: var(--crimson-dark);
    }
    .hero-cta-group {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 24px;
    }
    .hero-trust-row {
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
    }
    .hero-trust-item {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.86rem;
      font-weight: 600;
      color: #F3F4F6;
    }
    .hero-trust-item svg {
      color: var(--gold);
      flex-shrink: 0;
    }
    .hero-visual-card {
      background-color: var(--charcoal);
      border: 1px solid rgba(255, 255, 255, 0.16);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-lg);
    }
    .hero-image-frame {
      position: relative;
      background-color: #FFFFFF;
      padding: 14px;
    }
    .hero-image-frame img {
      width: 100%;
      height: 310px;
      object-fit: contain;
      object-position: center;
      border-radius: var(--radius-sm);
    }
    .hero-floating-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: var(--charcoal-deep);
      color: var(--gold);
      font-family: 'Barlow', sans-serif;
      font-size: 0.74rem;
      font-weight: 700;
      padding: 6px 10px;
      border-radius: var(--radius-sm);
      margin-bottom: 10px;
    }
    .hero-quickbar {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      padding: 14px 16px;
      background-color: #181817;
      border-top: 1px solid rgba(255, 255, 255, 0.12);
    }
    .hero-quickbar-item {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    .hero-quickbar-label {
      font-size: 0.7rem;
      color: #D1D5DB;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      font-weight: 600;
    }
    .hero-quickbar-val a {
      font-family: 'Barlow', sans-serif;
      font-size: 0.86rem;
      font-weight: 700;
      color: var(--gold);
      display: inline-flex;
      align-items: center;
      min-height: 32px;
    }
    .trust-strip {
      background-color: #FFFFFF;
      border-bottom: 1px solid var(--border-light);
      padding: 28px 0;
    }
    .trust-strip-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      align-items: stretch;
    }
    .trust-metric {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 14px;
      background-color: var(--bg-page);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
    }
    .trust-metric-icon {
      width: 38px;
      height: 38px;
      border-radius: var(--radius-sm);
      background-color: var(--charcoal);
      color: var(--gold);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .trust-metric-num {
      font-family: 'Barlow', sans-serif;
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--charcoal);
      line-height: 1.2;
    }
    .trust-metric-label {
      font-size: 0.8rem;
      color: var(--text-body);
      line-height: 1.4;
      margin-top: 3px;
    }
    .section-header {
      max-width: 780px;
      margin-bottom: 38px;
    }
    .section-lead {
      font-size: 1.02rem;
      color: var(--text-body);
      line-height: 1.65;
    }
    .section-alt {
      background-color: var(--bg-Warm);
      border-top: 1px solid var(--border-light);
      border-bottom: 1px solid var(--border-light);
    }
    .section-dark {
      background-color: var(--charcoal-deep);
      color: #FFFFFF;
    }
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      align-items: stretch;
    }
    .service-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-top: 4px solid var(--crimson-bright);
      border-radius: var(--radius-md);
      padding: 26px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 14px;
      height: 100%;
    }
    .service-card h3 {
      font-size: 1.28rem;
      font-weight: 800;
      color: var(--charcoal);
    }
    .service-card p {
      font-size: 0.94rem;
      color: var(--text-body);
      line-height: 1.6;
    }
    .service-card-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
    }
    .service-icon-box {
      width: 42px;
      height: 42px;
      border-radius: var(--radius-sm);
      background-color: var(--charcoal);
      color: var(--gold);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .service-tag {
      font-family: 'Barlow', sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      background-color: var(--crimson-soft);
      color: var(--crimson-dark);
      border: 1px solid var(--crimson-border);
    }
    .service-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin: 4px 0;
    }
    .service-list li {
      display: flex;
      align-items: flex-start;
      gap: 8px;
      font-size: 0.88rem;
      color: var(--text-body);
      line-height: 1.48;
    }
    .service-list li svg {
      color: var(--crimson-dark);
      flex-shrink: 0;
      margin-top: 2px;
    }
    .service-card-footer {
      margin-top: auto;
      padding-top: 8px;
    }
    .studio-showcase {
      display: grid;
      grid-template-columns: 1.08fr 0.92fr;
      gap: 36px;
      align-items: start;
    }
    .team-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-left: 4px solid var(--crimson-bright);
      border-radius: var(--radius-md);
      padding: 18px 20px;
      box-shadow: var(--shadow-sm);
    }
    .team-role {
      font-family: 'Barlow', sans-serif;
      font-size: 0.74rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--crimson-dark);
      margin-bottom: 4px;
    }
    .team-name {
      font-size: 1.18rem;
      font-weight: 800;
      color: var(--charcoal);
      margin-bottom: 6px;
    }
    .team-bio {
      font-size: 0.88rem;
      color: var(--text-body);
      line-height: 1.55;
      margin-bottom: 12px;
    }
    .team-contact-links {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }
    .team-contact-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 12px;
      min-height: 38px;
      border-radius: var(--radius-sm);
      background-color: var(--bg-page);
      border: 1px solid var(--border-strong);
      font-family: 'Barlow', sans-serif;
      font-size: 0.84rem;
      font-weight: 700;
      color: var(--charcoal);
    }
    .team-contact-pill:hover {
      background-color: var(--gold-soft);
      border-color: var(--gold-dark);
    }
    .studio-photo-stack {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .studio-photo-main img {
      width: 100%;
      height: 290px;
      object-fit: cover;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-light);
    }
    .studio-photo-sub {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      align-items: stretch;
    }
    .studio-photo-sub img {
      width: 100%;
      height: 100%;
      min-height: 190px;
      object-fit: cover;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-light);
    }
    .studio-fact-box {
      background-color: var(--charcoal-deep);
      color: #F9FAFB;
      border-radius: var(--radius-md);
      padding: 20px;
      border-top: 4px solid var(--gold);
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .studio-fact-box h4 {
      color: #FFFFFF;
      font-size: 1.05rem;
      margin-bottom: 8px;
    }
    .studio-fact-box p {
      font-size: 0.86rem;
      color: #E5E7EB;
      line-height: 1.5;
    }
    .cta-banner {
      background-color: var(--charcoal-deep);
      color: #FFFFFF;
      border-radius: var(--radius-md);
      border-left: 6px solid var(--crimson-bright);
      padding: 36px 40px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 28px;
      flex-wrap: wrap;
      box-shadow: var(--shadow-md);
    }
    .cta-banner h2 {
      color: #FFFFFF;
      font-size: clamp(1.55rem, 2.6vw, 2.1rem);
      margin-bottom: 8px;
    }
    .cta-banner p {
      color: #E5E7EB;
      font-size: 0.96rem;
      max-width: 640px;
    }
    .cta-banner-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      flex-shrink: 0;
    }
    .page-hero {
      background-color: var(--charcoal-deep);
      color: #FFFFFF;
      padding: 54px 0 60px;
      border-bottom: 4px solid var(--crimson-bright);
    }
    .page-hero h1 {
      color: #FFFFFF;
      font-size: clamp(1.95rem, 3.3vw, 2.75rem);
      font-weight: 800;
      margin-bottom: 14px;
      max-width: 820px;
    }
    .page-hero p {
      color: #E5E7EB;
      font-size: 1.02rem;
      max-width: 760px;
      line-height: 1.65;
    }
    .breadcrumb {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.8rem;
      color: #D1D5DB;
      margin-bottom: 14px;
    }
    .breadcrumb a {
      color: var(--gold);
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      min-height: 34px;
      min-width: 44px;
      padding: 4px 8px;
    }
    .studio-fact-box a {
      display: inline-flex;
      align-items: center;
      min-height: 34px;
      padding: 4px 6px;
    }
    .preview-card-dashed {
      background-color: #FFFFFF;
      border: 2px dashed #6B7280;
      border-radius: var(--radius-md);
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 14px;
      cursor: pointer;
      height: 100%;
      transition: border-color 0.18s ease, background-color 0.18s ease;
    }
    .preview-card-dashed:hover {
      border-color: var(--charcoal);
      background-color: var(--gold-soft);
    }
    .preview-card-dashed h3 {
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--charcoal);
    }
    .preview-card-dashed p {
      font-size: 0.9rem;
      color: var(--text-body);
      line-height: 1.55;
    }
    .preview-badge-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      align-self: flex-start;
      background-color: var(--gold-soft);
      color: var(--gold-dark);
      border: 1px solid var(--gold-border);
      font-family: 'Barlow', sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
    }
    .wizard-shell {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 32px;
      align-items: start;
    }
    .wizard-progress {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin-bottom: 22px;
      background-color: var(--bg-page);
      padding: 6px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-light);
    }
    .wizard-step-pill {
      padding: 10px 8px;
      border-radius: var(--radius-sm);
      font-family: 'Barlow', sans-serif;
      font-size: 0.8rem;
      font-weight: 700;
      text-align: center;
      color: var(--text-muted);
    }
    .wizard-step-pill.active {
      background-color: var(--charcoal);
      color: var(--gold);
    }
    .wizard-pane {
      display: none;
    }
    .wizard-pane.active {
      display: block;
    }
    .option-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      align-items: stretch;
    }
    .option-tile {
      background-color: var(--bg-page);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-md);
      padding: 16px;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 6px;
      min-height: 96px;
    }
    .option-tile.selected {
      background-color: var(--gold-soft);
      border: 2px solid var(--charcoal);
    }
    .option-tile-title {
      font-family: 'Barlow', sans-serif;
      font-size: 0.95rem;
      font-weight: 800;
      color: var(--charcoal);
    }
    .option-tile-sub {
      font-size: 0.8rem;
      color: var(--text-body);
      line-height: 1.45;
    }
    .form-row-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
      margin-bottom: 14px;
    }
    .form-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 12px;
    }
    .form-select {
      width: 100%;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.9rem;
      color: var(--text-main);
      background-color: #FFFFFF;
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-sm);
      padding: 11px 14px;
      min-height: 44px;
    }
    @media (max-width: 1080px) {
      .trust-strip-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .studio-showcase,
      .wizard-shell,
      .grid-3 {
        grid-template-columns: 1fr;
      }
    }
    @media (max-width: 768px) {
      .trust-strip-grid,
      .hero-quickbar,
      .studio-photo-sub,
      .option-grid,
      .form-row-2,
      .wizard-progress {
        grid-template-columns: 1fr;
      }
      .container {
        padding: 0 16px;
      }
      .header-inner {
        gap: 10px;
      }
      .brand-link {
        flex-shrink: 1;
        min-width: 0;
        gap: 8px;
      }
      .brand-logo {
        width: 76px;
        height: 32px;
      }
      .brand-name {
        font-size: 0.92rem;
      }
      .brand-sub {
        font-size: 0.62rem;
        letter-spacing: 0.03em;
      }
      .cta-banner {
        padding: 24px 20px;
      }
      .cta-banner-actions {
        width: 100%;
        flex-direction: column;
        align-items: stretch;
      }
      .cta-banner-actions .btn-cta {
        width: 100%;
      }
    }

    @media (max-width: 1080px) {
      .hero-grid,
      .contact-layout,
      .footer-grid {
        grid-template-columns: 1fr;
      }
      .main-nav {
        display: none;
      }
      .mobile-toggle {
        display: inline-flex;
      }
    }

    @media (max-width: 768px) {
      section {
        padding: 56px 0;
      }
      .grid-2,
      .hero-badges,
      .wp-role-grid,
      .form-grid-2,
      .wp-stepper {
        grid-template-columns: 1fr;
      }
      .header-actions .btn-cta {
        display: none;
      }
      .hero-media-card img {
        height: 250px;
      }
      .wizard-card,
      .content-card {
        padding: 20px;
      }
      .wp-version-inner {
        flex-direction: column;
        align-items: stretch;
      }
      .wp-version-pill-group {
        width: 100%;
      }
      .wp-ver-btn {
        flex: 1 1 auto;
      }
    }
"""

SVG_CHECK = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>'
SVG_ARROW = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'
SVG_SHIELD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
SVG_LAYERS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>'
SVG_SHIRT = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.38 3.46 16 2a4 4 0 0 1-8 0L3.62 3.46a2 2 0 0 0-1.34 2.23l.58 3.47a1 1 0 0 0 .99.84H6v10c0 1.1.9 2 2 2h8a2 2 0 0 0 2-2V10h2.15a1 1 0 0 0 .99-.84l.58-3.47a2 2 0 0 0-1.34-2.23z"/></svg>'
SVG_AWARD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>'
SVG_USERS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
SVG_SPARKLES = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3Z"/></svg>'
SVG_SLIDERS = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/></svg>'
SVG_PHONE = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
SVG_MAIL = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'


def render_catalogs_grid(limit: int = 14) -> str:
    cards = []
    for idx, cat in enumerate(BEFORE_INVENTORY["catalogs"][:limit]):
        slot_prefix = f"cat_{idx+1}"
        cards.append(f"""
        <div class="pillar-card">
          <div class="pillar-img-wrap logo-stage">
            <img src="{cat['image']}" alt="{cat['name']}" loading="lazy" decoding="async" data-wp-slot="{slot_prefix}_img">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge" data-wp-slot="{slot_prefix}_badge">{cat['category']}</span>
                <span style="font-family:'Barlow',sans-serif;font-size:0.76rem;font-weight:800;color:var(--crimson-dark);">Katalog #{idx+1:02d}</span>
              </div>
              <h3 style="font-size:1.25rem;font-weight:800;margin-bottom:8px;" data-wp-slot="{slot_prefix}_title">{cat['name']}</h3>
              <p style="font-size:0.9rem;color:var(--text-body);" data-wp-slot="{slot_prefix}_desc">{cat['desc']}</p>
            </div>
            <div style="display:flex;gap:10px;flex-wrap:wrap;">
              <a href="{cat['url']}" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-primary btn-sm" style="flex:1 1 auto;">
                <span>Blätterkatalog / Shop öffnen</span>
                {SVG_ARROW}
              </a>
              <a href="kontakt.html?thema=arbeitskleidung" class="btn-cta btn-cta-outline btn-sm" style="flex:1 1 auto;">
                <span>Offerte anfragen</span>
              </a>
            </div>
          </div>
        </div>""")
    return '<div class="grid-2">\n' + "\n".join(cards) + "\n      </div>"


def render_impressum_modal() -> str:
    return f"""
  <!-- IMPRESSUM & DATENSCHUTZ MODAL (#wpImpressumModal) -->
  <div class="wp-modal-backdrop" id="wpImpressumModal" role="dialog" aria-modal="true" aria-labelledby="wpImpTitle" data-allow-scroll="true">
    <div class="wp-modal-dialog" data-allow-scroll="true">
      <button type="button" class="wp-modal-close" aria-label="Dialog schliessen" onclick="wpCloseImpressumModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="section-kicker">RECHTLICHE ANGABEN · FREE'S NIEDERROHRDORF</div>
      <h3 id="wpImpTitle" style="font-size:1.38rem;font-weight:800;margin-bottom:10px;">Impressum &amp; Datenschutz (Free's · frees.ch)</h3>
      <div style="font-size:0.88rem;color:var(--text-body);line-height:1.62;display:flex;flex-direction:column;gap:12px;">
        <div style="background-color:var(--bg-page);border:1px solid var(--border-light);border-left:4px solid var(--crimson-bright);padding:12px 14px;border-radius:var(--radius-sm);">
          <strong>Free's Stefan Fritschi, Teamsport-Promowear &amp; Print</strong><br>
          Mellingerstrasse 12 · Eingang C, 1. Stock · CH-5443 Niederrohrdorf · Schweiz<br>
          Telefon Stefan Fritschi: +41 79 709 12 24 · Telefon Raimondo: +41 79 966 59 78 · E-Mail: info@frees.ch
        </div>
        <p>
          <strong>Inhaber &amp; Verantwortlicher:</strong><br>
          <strong>Stefan Fritschi</strong> (Einzelunternehmen Free's Stefan Fritschi, Teamsport-Promowear &amp; Print, CH-5443 Niederrohrdorf, Kanton Aargau).<br>
          Öffnungszeiten Showroom &amp; Atelier: Nach Vereinbarung via E-Mail oder Telefon.
        </p>
        <p>
          <strong>Urheberrecht &amp; Markenhinweise:</strong><br>
          Alle auf dieser Website dargestellten Inhalte, Fotos aus dem Atelier sowie Marken- und Katalogverweise (JAKO, ERIMA, F. ENGEL, CLIQUE, CRAFT, New Wave, PRINTER, James Harvest, HAKRO, PROJOB, J. Harvest &amp; Frost, WIKLAND, alltextiles.ch) stehen im Eigentum von Free's Stefan Fritschi respektive der jeweiligen Markeninhaber.
        </p>
        <p>
          <strong>Datenschutz (CH-DSG / DSGVO):</strong><br>
          Personenbezogene Angaben und hochgeladene Druck-/Stickmotive aus dem 3-Schritte Smart-Anfrage-Assistenten werden ausschliesslich zur Ausarbeitung Ihrer Offerte, zur Beantwortung Ihrer Anfrage und zur Erstellung Ihres persönlichen 1-Seiten-Anfrage-Dossiers verwendet und niemals an unbefugte Dritte weitergegeben.
        </p>
      </div>
      <div style="margin-top:18px;display:flex;justify-content:flex-end;">
        <button type="button" class="btn-cta btn-cta-primary btn-sm" onclick="wpCloseImpressumModal()">
          <span>Schliessen</span>
        </button>
      </div>
    </div>
  </div>"""


COMMON_UI_JS = """
  <script>
    function wpToggleMobileMenu() {
      var d = document.getElementById('mobileDrawer');
      if (d) d.classList.toggle('open');
    }
    function wpCloseMobileMenu() {
      var d = document.getElementById('mobileDrawer');
      if (d) d.classList.remove('open');
    }
    function wpOpenImpressumModal() {
      var m = document.getElementById('wpImpressumModal');
      if (m) m.classList.add('open');
    }
    function wpCloseImpressumModal() {
      var m = document.getElementById('wpImpressumModal');
      if (m) m.classList.remove('open');
    }
    function wpOpenBlueprintModal(title, category, focus) {
      var m = document.getElementById('wpBlueprintModal');
      if (!m) return;
      var tEl = document.getElementById('wpBpTitle');
      var cEl = document.getElementById('wpBpCategory');
      var fEl = document.getElementById('wpBpContact');
      if (tEl && title) tEl.textContent = title;
      if (cEl && category) cEl.textContent = 'Themenbereich: ' + category;
      if (fEl && focus) fEl.textContent = 'Beratung & Umsetzung: ' + focus;
      m.classList.add('open');
    }
    function wpCloseBlueprintModal() {
      var m = document.getElementById('wpBlueprintModal');
      if (m) m.classList.remove('open');
    }
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        wpCloseImpressumModal();
        wpCloseBlueprintModal();
        wpCloseMobileMenu();
      }
    });
  </script>
"""


def render_v1_shell(filename: str, page_title: str, active_nav: str, body_html: str) -> str:
    nav_start = "active" if active_nav == "startseite" else ""
    nav_dl = "active" if active_nav == "dienstleistungen" else ""
    nav_sort = "active" if active_nav == "textilsortiment" else ""
    nav_profil = "active" if active_nav == "profil" else ""
    nav_kontakt = "active" if active_nav == "kontakt" else ""
    v2_href = "/frees-v2/kontakt.html" if filename == "kontakt.html" else "/frees-v2/"

    return f"""<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-XSS-Protection" content="1; mode=block">
  <meta name="referrer" content="no-referrer">
  <title>{page_title}</title>
  <meta name="description" content="Free's — Studio für Textildesign, Textildruck &amp; Stickerei in 5443 Niederrohrdorf. Arbeitskleidung, Corporate Fashion, Vereinsbekleidung &amp; 14 Marken-Kataloge.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@600;700;800&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <style>
{SHARED_CSS}
  </style>
</head>
<body>

  <!-- 1-KLICK-VERSIONS-UMSCHALTER OBEN (KOMPLETTVERSION <-> ZEIGEVERSION + STUDIO COCKPIT V4.0) -->
  <div class="wp-version-bar" data-studio-ignore="true">
    <div class="container wp-version-inner">
      <div class="wp-version-info">
        <span class="top-bar-badge">FREE'S · KOMPLETT-VERSION</span>
        <span>Komplett-Version (alle Seiten ausgebaut): Alle 5 Seiten, Druck- &amp; Stick-Services sowie alle 14 Marken-Kataloge vollständig ausgearbeitet.</span>
      </div>
      <div class="wp-version-pill-group" role="group" aria-label="Versions-Umschalter">
        <span class="wp-ver-btn is-active">
          {SVG_CHECK}
          <span>Komplett-Version (alle Seiten ausgebaut)</span>
        </span>
        <a href="{v2_href}" class="wp-ver-btn is-switch">
          <span>Zur Zeigeversion (Vorschau-Entwurf) wechseln</span>
          {SVG_ARROW}
        </a>
        <a href="cockpit.html?token=frees2026" class="wp-ver-btn is-cockpit">
          {SVG_SLIDERS}
          <span>Studio Cockpit v4.0</span>
        </a>
      </div>
    </div>
  </div>

  <!-- TOP INFO BAR -->
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div class="top-bar-left">
        <span class="top-bar-badge" data-slot="topbar_badge" data-wp-slot="topbar_badge">SHOWROOM NIEDERROHRDORF · MELLINGERSTRASSE 12</span>
        <span data-slot="topbar_sub" data-wp-slot="topbar_sub">Textildruck, Stickerei, Arbeitskleidung &amp; Vereinsausrüstung · «Wir organisieren Wünsche»</span>
      </div>
      <div class="top-bar-links">
        <a href="tel:+41797091224">{SVG_PHONE} <span>+41 79 709 12 24 (Stefan)</span></a>
        <a href="tel:+41799665978">{SVG_PHONE} <span>+41 79 966 59 78 (Raimondo)</span></a>
        <a href="mailto:info@frees.ch">{SVG_MAIL} <span>info@frees.ch</span></a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="Free's Startseite">
        <img src="images/logo.svg" alt="Free's — Studio für Textildesign, Textildruck &amp; Stickerei" class="brand-logo" width="118" height="44" data-slot="brand_logo" data-wp-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name" data-wp-slot="brand_name">FREE'S TEXTILDESIGN</span>
          <span class="brand-sub" data-slot="brand_sub" data-wp-slot="brand_sub">DRUCK · STICKEREI · WORKWEAR</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}">Start</a>
        <a href="dienstleistungen.html" class="nav-link {nav_dl}">Dienstleistungen</a>
        <a href="textilsortiment.html" class="nav-link {nav_sort}">Textilsortiment (14 Kataloge)</a>
        <a href="profil.html" class="nav-link {nav_profil}">Profil</a>
        <a href="kontakt.html" class="nav-link {nav_kontakt}">Smart-Anfrage &amp; Kontakt</a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html" class="btn-cta btn-cta-gold btn-sm" data-slot="header_cta" data-wp-slot="header_cta">
          <span>Offerte &amp; Beratung anfragen</span>
          {SVG_ARROW}
        </a>
        <button type="button" class="mobile-toggle" id="mobileMenuBtn" aria-label="Menü öffnen" onclick="wpToggleMobileMenu()">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    </div>
  </header>

  <div class="mobile-drawer" id="mobileDrawer">
    <a href="index.html" onclick="wpCloseMobileMenu()">Startseite</a>
    <a href="dienstleistungen.html" onclick="wpCloseMobileMenu()">Dienstleistungen: Textildruck, Stickerei &amp; Labels</a>
    <a href="textilsortiment.html" onclick="wpCloseMobileMenu()">Textilsortiment: Alle 14 Marken-Kataloge &amp; Shop</a>
    <a href="profil.html" onclick="wpCloseMobileMenu()">Profil: Stefan Fritschi, Raimondo &amp; Showroom</a>
    <a href="kontakt.html" onclick="wpCloseMobileMenu()">3-Schritte Smart-Anfrage &amp; Kontakt</a>
    <a href="{v2_href}" onclick="wpCloseMobileMenu()" style="background-color:var(--gold);color:#161615;">Zur Zeigeversion (Vorschau-Entwurf) wechseln</a>
  </div>

  <main>
{body_html}
  </main>

  <!-- FOOTER -->
  <footer class="site-footer" data-section="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
            <img src="images/logo.svg" alt="Free's Logo" width="110" height="40" loading="lazy" decoding="async" style="border-radius:4px;background:#FFFFFF;padding:3px 6px;">
            <div>
              <div style="font-family:'Barlow',sans-serif;font-weight:800;font-size:1.05rem;color:#FFFFFF;" data-wp-slot="footer_brand_title">FREE'S · NIEDERROHRDORF</div>
              <div style="font-size:0.74rem;color:var(--gold);font-weight:700;" data-wp-slot="footer_brand_sub">STUDIO FÜR TEXTILDESIGN &amp; DRUCK</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#D1D5DB;line-height:1.6;margin-bottom:14px;" data-slot="footer_about" data-wp-slot="footer_about">
            Kreative Lösungen für Ihre Designwünsche: Seit über 12 Jahren Ihr persönlicher Schweizer Partner für Textildruck, Stickereien, gewobene Labels, Arbeitskleidung, Corporate Fashion und Vereinsbekleidung in Niederrohrdorf (AG).
          </p>
          <div style="font-size:0.84rem;color:#F3F4F6;font-weight:600;" data-wp-slot="footer_addr">
            Mellingerstrasse 12 · Eingang C, 1. Stock · CH-5443 Niederrohrdorf
          </div>
        </div>

        <div>
          <div class="footer-title">Navigation &amp; Seiten</div>
          <ul class="footer-list">
            <li><a href="index.html">Startseite</a></li>
            <li><a href="dienstleistungen.html">Dienstleistungen (Druck &amp; Stickerei)</a></li>
            <li><a href="textilsortiment.html">Textilsortiment (14 Kataloge &amp; Shop)</a></li>
            <li><a href="profil.html">Profil &amp; Geschichte (Stefan Fritschi)</a></li>
            <li><a href="kontakt.html">3-Schritte Smart-Anfrage &amp; Kontakt</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Leistungen &amp; Sortiment</div>
          <ul class="footer-list">
            <li><a href="dienstleistungen.html#textildruck">Textildruck in allen Auflagen</a></li>
            <li><a href="dienstleistungen.html#stickerei">Stickereien &amp; gewobene Labels</a></li>
            <li><a href="textilsortiment.html#kataloge">Arbeitskleidung &amp; Corporate Fashion</a></li>
            <li><a href="textilsortiment.html#kataloge">Teamsport &amp; Vereinsausrüstung</a></li>
            <li><a href="https://frees.alltextiles.ch" target="_blank" rel="noopener noreferrer">Online-Shop (frees.alltextiles.ch)</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; Showroom</div>
          <ul class="footer-list">
            <li><a href="tel:+41797091224">Stefan Fritschi: +41 79 709 12 24</a></li>
            <li><a href="tel:+41799665978">Raimondo: +41 79 966 59 78</a></li>
            <li><a href="mailto:info@frees.ch">E-Mail: info@frees.ch</a></li>
            <li><a href="{v2_href}" style="color:var(--gold);font-weight:700;">Zur Zeigeversion wechseln</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Free's Stefan Fritschi (CH-5443 Niederrohrdorf) · Öffnungszeiten nach Vereinbarung via Mail oder Telefon.</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
          <a href="{v2_href}" style="color:var(--gold);font-weight:700;">Zeigeversion öffnen</a>
          <a href="cockpit.html?token=frees2026" style="color:#E5E7EB;">Studio Cockpit v4.0</a>
        </div>
      </div>
    </div>
  </footer>

{render_impressum_modal()}
{COMMON_UI_JS}
</body>
</html>"""


def render_v2_shell(filename: str, page_title: str, active_nav: str, body_html: str) -> str:
    nav_start = "active" if active_nav == "startseite" else ""
    nav_kontakt = "active" if active_nav == "kontakt" else ""
    v1_href = "/frees/kontakt.html" if filename == "kontakt.html" else "/frees/"

    return f"""<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-XSS-Protection" content="1; mode=block">
  <meta name="referrer" content="no-referrer">
  <title>{page_title}</title>
  <meta name="description" content="Unverbindlicher Vorschau-Entwurf (Zeigeversion) für Free's Niederrohrdorf: 2 Beispiel-Seiten sind bereits ausgearbeitet — 3 weitere Themenbereiche folgen beim Ausbau.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@600;700;800&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <style>
{SHARED_CSS}
  </style>
</head>
<body>

  <!-- TOP-BANNER ZEIGEVERSION (#UI-03 KUNDEN-SPRACHE + STUDIO COCKPIT V4.0) -->
  <div class="wp-version-bar" data-studio-ignore="true">
    <div class="container wp-version-inner">
      <div class="wp-version-info">
        <span class="top-bar-badge">VORSCHAU-ENTWURF · ZEIGEVERSION</span>
        <span>Zeigeversion (Vorschau-Entwurf für das Erstgespräch): 2 Beispiel-Seiten sind bereits ausgearbeitet — 3 weitere Themenbereiche folgen beim Ausbau.</span>
      </div>
      <div class="wp-version-pill-group" role="group" aria-label="Versions-Umschalter">
        <span class="wp-ver-btn is-active">
          {SVG_CHECK}
          <span>Zeigeversion (Vorschau-Entwurf für das Erstgespräch)</span>
        </span>
        <a href="{v1_href}" class="wp-ver-btn is-switch">
          <span>Zur Komplett-Version (alle Seiten) wechseln</span>
          {SVG_ARROW}
        </a>
        <a href="cockpit.html?token=frees2026" class="wp-ver-btn is-cockpit">
          {SVG_SLIDERS}
          <span>Studio Cockpit v4.0</span>
        </a>
      </div>
    </div>
  </div>

  <!-- TOP INFO BAR -->
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div class="top-bar-left">
        <span class="top-bar-badge" data-slot="topbar_badge" data-wp-slot="topbar_badge">2 BEISPIEL-SEITEN AUSGEARBEITET · 3 WEITERE BEREICHE VORBEREITET</span>
        <span data-slot="topbar_sub" data-wp-slot="topbar_sub">Mellingerstrasse 12 · CH-5443 Niederrohrdorf · +41 79 709 12 24</span>
      </div>
      <div class="top-bar-links">
        <a href="index.html#weitere-themenbereiche">Weitere Themenbereiche (Ausbaustufe)</a>
        <a href="kontakt.html">Smart-Anfrage (Live-Demo)</a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER (ZEIGEVERSION MIT KUNDENFREUNDLICHEN VORSCHAU-HINWEISEN) -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="Free's Startseite">
        <img src="images/logo.svg" alt="Free's — Studio für Textildesign, Textildruck &amp; Stickerei" class="brand-logo" width="118" height="44" data-slot="brand_logo" data-wp-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name" data-wp-slot="brand_name">FREE'S TEXTILDESIGN</span>
          <span class="brand-sub" data-slot="brand_sub" data-wp-slot="brand_sub">VORSCHAU-ENTWURF · NIEDERROHRDORF</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#15803D"/></svg>
          <span>Startseite (Beispiel-Seite)</span>
        </a>
        <button type="button" class="nav-link nav-link-preview" onclick="wpOpenBlueprintModal('Dienstleistungen: Textildruck, Stickerei &amp; Labels', 'Alle Drucktechniken, Direktstickerei, gewobene Labels &amp; Veredelung eigener Textilien', 'Stefan Fritschi &amp; Raimondo')">
          <span>Dienstleistungen (Folgt beim Ausbau)</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" onclick="wpOpenBlueprintModal('Komplettes Textilsortiment &amp; Alle 14 Marken-Kataloge', 'Online-Shop frees.alltextiles.ch sowie JAKO, ERIMA, F. ENGEL, CLIQUE, CRAFT, HAKRO, PROJOB &amp; WIKLAND', 'Stefan Fritschi &amp; Raimondo')">
          <span>Textilsortiment (Folgt beim Ausbau)</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" onclick="wpOpenBlueprintModal('Profil, Studio-Geschichte &amp; Showroom Niederrohrdorf', 'Werdegang von Stefan Fritschi, Atelier-Einblicke &amp; persönliche Muster-Beratung', 'Stefan Fritschi &amp; Raimondo')">
          <span>Profil (Folgt beim Ausbau)</span>
        </button>
        <a href="kontakt.html" class="nav-link {nav_kontakt}">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#15803D"/></svg>
          <span>Smart-Anfrage (Live-Demo)</span>
        </a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html" class="btn-cta btn-cta-gold btn-sm" data-slot="header_cta" data-wp-slot="header_cta">
          <span>Smart-Anfrage testen</span>
          {SVG_ARROW}
        </a>
        <button type="button" class="mobile-toggle" id="mobileMenuBtn" aria-label="Menü öffnen" onclick="wpToggleMobileMenu()">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    </div>
  </header>

  <div class="mobile-drawer" id="mobileDrawer">
    <a href="index.html" onclick="wpCloseMobileMenu()">Startseite (Beispiel-Seite ausgearbeitet)</a>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu(); wpOpenBlueprintModal('Dienstleistungen: Textildruck, Stickerei &amp; Labels', 'Alle Drucktechniken, Direktstickerei, gewobene Labels &amp; Veredelung eigener Textilien', 'Stefan Fritschi &amp; Raimondo')">
      <span>Dienstleistungen (Folgt beim Ausbau)</span>
      {SVG_ARROW}
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu(); wpOpenBlueprintModal('Komplettes Textilsortiment &amp; Alle 14 Marken-Kataloge', 'Online-Shop frees.alltextiles.ch sowie alle 14 Marken-Blätterkataloge', 'Stefan Fritschi &amp; Raimondo')">
      <span>Textilsortiment &amp; 14 Kataloge (Folgt beim Ausbau)</span>
      {SVG_ARROW}
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu(); wpOpenBlueprintModal('Profil, Studio-Geschichte &amp; Showroom Niederrohrdorf', 'Werdegang von Stefan Fritschi, Atelier-Einblicke &amp; persönliche Beratung', 'Stefan Fritschi &amp; Raimondo')">
      <span>Profil &amp; Showroom (Folgt beim Ausbau)</span>
      {SVG_ARROW}
    </button>
    <a href="kontakt.html" onclick="wpCloseMobileMenu()">3-Schritte Smart-Anfrage (Live-Demo)</a>
    <a href="{v1_href}" onclick="wpCloseMobileMenu()" style="background-color:var(--gold);color:#161615;">Zur Komplett-Version (alle Seiten) wechseln</a>
  </div>

  <main>
{body_html}
  </main>

  <!-- FOOTER (ZEIGEVERSION) -->
  <footer class="site-footer" data-section="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
            <img src="images/logo.svg" alt="Free's Logo" width="110" height="40" loading="lazy" decoding="async" style="border-radius:4px;background:#FFFFFF;padding:3px 6px;">
            <div>
              <div style="font-family:'Barlow',sans-serif;font-weight:800;font-size:1.05rem;color:#FFFFFF;" data-wp-slot="footer_brand_title">FREE'S · NIEDERROHRDORF</div>
              <div style="font-size:0.74rem;color:var(--gold);font-weight:700;" data-wp-slot="footer_brand_sub">VORSCHAU-ENTWURF · 2 BEISPIEL-SEITEN LIVE</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#D1D5DB;line-height:1.6;margin-bottom:14px;" data-slot="footer_about" data-wp-slot="footer_about">
            Unverbindlicher Vorschau-Entwurf (Zeigeversion) für Free's Stefan Fritschi: 2 Beispiel-Seiten (Startseite &amp; 3-Schritte Smart-Anfrage) sind bereits ausgearbeitet — 3 weitere Themenbereiche folgen in der nächsten Ausbaustufe.
          </p>
          <div style="font-size:0.84rem;color:#F3F4F6;font-weight:600;" data-wp-slot="footer_addr">
            Mellingerstrasse 12 · Eingang C, 1. Stock · CH-5443 Niederrohrdorf
          </div>
        </div>

        <div>
          <div class="footer-title">Bereits ausgearbeitet (Live)</div>
          <ul class="footer-list">
            <li><a href="index.html">Startseite: Hero &amp; 4 Leistungs-Säulen</a></li>
            <li><a href="index.html#studio-profil">Studio-Vorstellung: Stefan Fritschi &amp; Raimondo</a></li>
            <li><a href="index.html#katalog-auszug">Auszug aus den Marken-Katalogen</a></li>
            <li><a href="kontakt.html">3-Schritte Smart-Anfrage (Live-Demo)</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Folgen beim gemeinsamen Ausbau</div>
          <ul class="footer-list">
            <li><button type="button" onclick="wpOpenBlueprintModal('Dienstleistungen: Textildruck, Stickerei &amp; Labels', 'Alle Drucktechniken, Direktstickerei, gewobene Labels &amp; Veredelung eigener Textilien', 'Stefan Fritschi &amp; Raimondo')">Dienstleistungen &amp; Drucktechniken</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Komplettes Textilsortiment &amp; Alle 14 Marken-Kataloge', 'Online-Shop frees.alltextiles.ch sowie JAKO, ERIMA, F. ENGEL, CLIQUE, CRAFT, HAKRO, PROJOB &amp; WIKLAND', 'Stefan Fritschi &amp; Raimondo')">Textilsortiment &amp; 14 Marken-Kataloge</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Profil, Studio-Geschichte &amp; Showroom Niederrohrdorf', 'Werdegang von Stefan Fritschi seit 2016 in Niederrohrdorf &amp; Muster-Anprobe', 'Stefan Fritschi &amp; Raimondo')">Profil, Geschichte &amp; Showroom</button></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Versions-Vergleich &amp; Kontakt</div>
          <ul class="footer-list">
            <li><a href="{v1_href}" style="color:var(--gold);font-weight:700;">Komplett-Version ansehen (Alle 5 Seiten)</a></li>
            <li><a href="index.html#weitere-themenbereiche">Übersicht der Ausbaustufe (3 Bereiche)</a></li>
            <li><a href="cockpit.html?token=frees2026">Studio Cockpit v4.0 öffnen</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Free's Stefan Fritschi (CH-5443 Niederrohrdorf) · Unverbindlicher Vorschau-Entwurf (Zeigeversion).</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
          <a href="{v1_href}" style="color:var(--gold);font-weight:700;">Komplett-Version öffnen</a>
          <a href="kontakt.html" style="color:#E5E7EB;">Smart-Anfrage testen</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- KUNDENFREUNDLICHES VORSCHAU-MODAL (#wpBlueprintModal) -->
  <div class="wp-modal-backdrop" id="wpBlueprintModal" role="dialog" aria-modal="true" aria-labelledby="wpBpTitle" data-allow-scroll="true">
    <div class="wp-modal-dialog" data-allow-scroll="true">
      <button type="button" class="wp-modal-close" aria-label="Dialog schliessen" onclick="wpCloseBlueprintModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="section-kicker">UNVERBINDLICHER VORSCHAU-ENTWURF FÜR FREE'S NIEDERROHRDORF</div>
      <h3 id="wpBpTitle" style="font-size:1.36rem;font-weight:800;margin-bottom:8px;">Unverbindlicher Vorschau-Entwurf für Free's</h3>
      <p id="wpBpSub" style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
        In dieser <strong>Zeigeversion (2 Beispiel-Seiten ausgearbeitet)</strong> sehen Sie oben den Hero-Bereich, Ihre 4 Leistungs-Säulen (Textildruck, Stickerei, Arbeitskleidung &amp; Vereinsbekleidung), Ihre Studio-Vorstellung sowie den live funktionierenden 3-Schritte Smart-Anfrage-Assistenten. Dieser vertiefte Themenbereich folgt beim gemeinsamen Ausbau mit allen Originaltexten, Bildern und Katalogen.
      </p>
      <div style="background-color:var(--gold-soft);border-left:4px solid var(--gold-dark);padding:12px 14px;border-radius:var(--radius-sm);font-size:0.86rem;margin-bottom:14px;">
        <div style="font-weight:800;color:var(--charcoal);" id="wpBpCategory">Themenbereich: Vorbereitet für die nächste Ausbaustufe</div>
        <div style="color:var(--text-body);margin-top:2px;" id="wpBpContact">Beratung &amp; Umsetzung: Stefan Fritschi &amp; Raimondo</div>
      </div>

      <div class="wp-modal-checklist">
        <div style="font-family:'Barlow',sans-serif;font-size:0.8rem;font-weight:800;text-transform:uppercase;color:var(--charcoal);">
          Was beim gemeinsamen Ausbau in diesem Themenbereich enthalten ist:
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Vollständige Ausarbeitung aller Dienstleistungen (Textildruck, Stickereien, gewobene &amp; gestickte Labels, Veredelung angelieferter Textilien)</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Direkte Einbindung aller 14 Original-Markenkataloge (JAKO, ERIMA, F. ENGEL, CLIQUE, CRAFT, HAKRO, PROJOB, WIKLAND) &amp; Online-Shop frees.alltextiles.ch</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Direkte Anbindung an das WebPilot Studio Cockpit v4.0 für sekundenschnelle Text-, Katalog- und Bildanpassungen</span>
        </div>
      </div>

      <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:18px;">
        <a href="/frees/" class="btn-cta btn-cta-gold btn-sm">
          <span>Direkt in der Komplett-Version ansehen</span>
          {SVG_ARROW}
        </a>
        <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm">
          <span>3-Schritte Smart-Anfrage testen</span>
        </a>
        <button type="button" class="btn-cta btn-cta-outline btn-sm" onclick="wpCloseBlueprintModal()">
          <span>Schliessen</span>
        </button>
      </div>
    </div>
  </div>

{render_impressum_modal()}
{COMMON_UI_JS}
</body>
</html>"""



SVG_BOOK = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>'
SVG_PRINTER = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>'
SVG_WRENCH = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>'
SVG_SHOP = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>'
SVG_MAP_PIN = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'

def render_hero_section(is_v2=False):
    sortiment_href = "#weitere-themenbereiche" if is_v2 else "textilsortiment.html"
    dl_href = "#weitere-themenbereiche" if is_v2 else "dienstleistungen.html"
    return f"""
  <section class="hero-section">
    <div class="container">
      <div class="hero-grid">
        <div>
          <div class="hero-eyebrow">
            {SVG_AWARD}
            <span data-slot="hero_badge" data-wp-slot="hero_badge">Seit 1998 in der Branche · Eigenes Druckatelier in Niederrohrdorf</span>
          </div>
          <h1 class="hero-title" data-slot="hero_headline" data-wp-slot="hero_headline">
            Teamsport, Promowear &amp; <span>Inhouse Textildruck</span> mit Handschlagqualität.
          </h1>
          <p class="hero-lead" data-slot="hero_subheadline" data-wp-slot="hero_subheadline">
            Ob Vereinsausrüstung, robuste Arbeitskleidung oder Event-Shirts: Im eigenen Druckatelier an der Mellingerstrasse 12 in Niederrohrdorf veredeln Stefan Fritschi und Raimondo Ihre Textilien schnell, flexibel und in höchster Waschbeständigkeit — auch für angelieferte Fremdtextilien.
          </p>
          <div class="hero-cta-group">
            <a href="kontakt.html" class="btn-cta btn-cta-primary" data-slot="hero_cta_primary" data-wp-slot="hero_cta_primary">
              <span>Offerte in 60 Sek. anfragen</span>
              {SVG_ARROW}
            </a>
            <a href="{sortiment_href}" class="btn-cta btn-cta-white" data-slot="hero_cta_secondary" data-wp-slot="hero_cta_secondary">
              {SVG_BOOK}
              <span>Textilsortiment &amp; 14 Kataloge</span>
            </a>
          </div>
          <div class="hero-trust-row">
            <div class="hero-trust-item">
              {SVG_CHECK}
              <span>Einzelstücke bis Grossserien</span>
            </div>
            <div class="hero-trust-item">
              {SVG_CHECK}
              <span>Veredelung auch für Fremdtextilien</span>
            </div>
            <div class="hero-trust-item">
              {SVG_CHECK}
              <span>Persönliche Beratung im Showroom</span>
            </div>
          </div>
        </div>

        <div class="hero-visual-card">
          <div class="hero-image-frame">
            <div class="hero-floating-badge">
              {SVG_SPARKLES}
              <span>Eigenes Druckatelier · CH-5443 Niederrohrdorf</span>
            </div>
            <img src="images/hero-collage-frees.png" alt="Free's Teamsport, Promowear und Textildruck Collage" width="640" height="440" data-slot="hero_image" data-wp-slot="hero_image">
          </div>
          <div class="hero-quickbar">
            <div class="hero-quickbar-item">
              <div class="hero-quickbar-label">Direktkontakt Stefan Fritschi</div>
              <div class="hero-quickbar-val"><a href="tel:+41797091224">+41 79 709 12 24</a></div>
            </div>
            <div class="hero-quickbar-item">
              <div class="hero-quickbar-label">Direktkontakt Raimondo</div>
              <div class="hero-quickbar-val"><a href="tel:+41799665978">+41 79 966 59 78</a></div>
            </div>
            <div class="hero-quickbar-item">
              <div class="hero-quickbar-label">Haupt-Onlineshop</div>
              <div class="hero-quickbar-val"><a href="https://frees.alltextiles.ch" target="_blank" rel="noopener">frees.alltextiles.ch</a></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <div class="trust-strip">
    <div class="container">
      <div class="trust-strip-grid">
        <div class="trust-metric">
          <div class="trust-metric-icon">{SVG_AWARD}</div>
          <div>
            <div class="trust-metric-num" data-slot="metric_1_val" data-wp-slot="metric_1_val">Seit 1998</div>
            <div class="trust-metric-label" data-slot="metric_1_label" data-wp-slot="metric_1_label">Über 25 Jahre Erfahrung in Teamsport &amp; Textildruck</div>
          </div>
        </div>
        <div class="trust-metric">
          <div class="trust-metric-icon">{SVG_PRINTER}</div>
          <div>
            <div class="trust-metric-num" data-slot="metric_2_val" data-wp-slot="metric_2_val">100 % Inhouse</div>
            <div class="trust-metric-label" data-slot="metric_2_label" data-wp-slot="metric_2_label">Eigenes Druckatelier für kurze Lieferzeiten &amp; Top-Qualität</div>
          </div>
        </div>
        <div class="trust-metric">
          <div class="trust-metric-icon">{SVG_BOOK}</div>
          <div>
            <div class="trust-metric-num" data-slot="metric_3_val" data-wp-slot="metric_3_val">14 Markenwelten</div>
            <div class="trust-metric-label" data-slot="metric_3_label" data-wp-slot="metric_3_label">JAKO, ERIMA, F. ENGEL, HAKRO, CRAFT, CLIQUE, PROJOB u.v.m.</div>
          </div>
        </div>
        <div class="trust-metric">
          <div class="trust-metric-icon">{SVG_SHIELD}</div>
          <div>
            <div class="trust-metric-num" data-slot="metric_4_val" data-wp-slot="metric_4_val">Ab 1 Stück</div>
            <div class="trust-metric-label" data-slot="metric_4_label" data-wp-slot="metric_4_label">Nachbestellungen für neue Vereins- oder Teammitglieder jederzeit</div>
          </div>
        </div>
      </div>
    </div>
  </div>
"""


def render_services_pillars_section(is_v2=False):
    if is_v2:
        action_dl = """<button type="button" class="btn-cta btn-cta-outline btn-sm" onclick="wpOpenBlueprintModal('Dienstleistungen &amp; Inhouse Druckservice', 'In der fertigen Webseite präsentieren wir hier alle Druck- und Stickverfahren im Detail: Flex- und Digitaltransferdruck, Siebdruck, Direkteinstickung, gewobene Labels sowie den Veredelungs-Service für angelieferte Fremdtextilien.')"><span>Vorschau-Details ansehen</span>""" + SVG_ARROW + """</button>"""
        action_sort = """<button type="button" class="btn-cta btn-cta-outline btn-sm" onclick="wpOpenBlueprintModal('Textilsortiment &amp; 14 Blätterkataloge', 'In der fertigen Webseite öffnen Ihre Kunden hier direkt Ihren Alltextiles-Onlineshop sowie alle 14 Blätterkataloge führender Sport- und Workwear-Marken.')"><span>Katalog-Ausbau ansehen</span>""" + SVG_ARROW + """</button>"""
    else:
        action_dl = f"""<a href="dienstleistungen.html" class="btn-cta btn-cta-outline btn-sm"><span>Zu den Dienstleistungen</span>{SVG_ARROW}</a>"""
        action_sort = f"""<a href="textilsortiment.html" class="btn-cta btn-cta-outline btn-sm"><span>Alle 14 Kataloge öffnen</span>{SVG_ARROW}</a>"""

    return f"""
  <section class="section" id="leistungen">
    <div class="container">
      <div class="section-header">
        <div class="section-eyebrow">
          {SVG_LAYERS}
          <span>Alles aus einer Hand in Niederrohrdorf</span>
        </div>
        <h2 class="section-title" data-slot="services_headline" data-wp-slot="services_headline">
          Vier Kernbereiche für Ihren starken Auftritt
        </h2>
        <p class="section-lead" data-slot="services_subheadline" data-wp-slot="services_subheadline">
          Von der persönlichen Textilberatung mit Anprobe-Mustern bis zur fertigen Veredelung in unserem eigenen Druckatelier begleiten wir Vereine, KMU und Events in der ganzen Region Baden, Aargau und Zürich.
        </p>
      </div>

      <div class="grid-2">
        <article class="service-card">
          <div class="service-card-head">
            <div class="service-icon-box">{SVG_SHIRT}</div>
            <span class="service-tag">Vereine &amp; Firmen</span>
          </div>
          <h3 data-slot="service_1_title" data-wp-slot="service_1_title">Teamsport, Workwear &amp; Promowear</h3>
          <p data-slot="service_1_desc" data-wp-slot="service_1_desc">
            Komplette Vereinsausrüstungen (JAKO, ERIMA, CRAFT), strapazierfähige Berufsbekleidung (F. ENGEL, PROJOB, WIKLAND) sowie Polos, Shirts und Hoodies (HAKRO, CLIQUE, James Harvest) für Ihren Firmenauftritt.
          </p>
          <ul class="service-list">
            <li>{SVG_CHECK}<span>Langfristige Nachliefergarantie für Vereins- und Firmenkollektionen</span></li>
            <li>{SVG_CHECK}<span>Grössen-Sätze &amp; Musterteile zur Anprobe vor der Veredelung</span></li>
            <li>{SVG_CHECK}<span>Attraktive Vereins- und Mengenrabatte bereits ab kleinen Serien</span></li>
          </ul>
          <div class="service-card-footer">
            {action_sort}
          </div>
        </article>

        <article class="service-card">
          <div class="service-card-head">
            <div class="service-icon-box">{SVG_PRINTER}</div>
            <span class="service-tag">Eigenes Druckatelier</span>
          </div>
          <h3 data-slot="service_2_title" data-wp-slot="service_2_title">Inhouse Textildruck &amp; Beflockung</h3>
          <p data-slot="service_2_desc" data-wp-slot="service_2_desc">
            Dank unserem eigenen Druckatelier in Niederrohrdorf bedrucken wir Sporttrikots, Arbeitsjacken, T-Shirts und Taschen mit höchster Deckkraft, Elastizität und Waschbeständigkeit — ohne lange Umwege.
          </p>
          <ul class="service-list">
            <li>{SVG_CHECK}<span>Nummern, Spielernamen, Sponsorenlogos &amp; mehrfarbige Brust-/Rückendrucke</span></li>
            <li>{SVG_CHECK}<span>Moderne Transfer-, Flex-, Flock- und Siebdruck-Lösungen je nach Einsatz</span></li>
            <li>{SVG_CHECK}<span>Express-Umsetzung bei kurzfristigen Turnieren, Messen oder Firmenevents</span></li>
          </ul>
          <div class="service-card-footer">
            {action_dl}
          </div>
        </article>

        <article class="service-card">
          <div class="service-card-head">
            <div class="service-icon-box">{SVG_SPARKLES}</div>
            <span class="service-tag">Edle Veredelung</span>
          </div>
          <h3 data-slot="service_3_title" data-wp-slot="service_3_title">Stickereien, Aufnäher &amp; eigene Labels</h3>
          <p data-slot="service_3_desc" data-wp-slot="service_3_desc">
            Für Poloshirts, Hemden, Fleecejacken, Caps und hochwertige Workwear bieten wir präzise Direkteinstickungen, gestickte Abzeichen sowie individuell gewobene oder gestickte Textil-Labels.
          </p>
          <ul class="service-list">
            <li>{SVG_CHECK}<span>Koch- und Industriewäsche-taugliche Stickgarne mit edlem Glanz</span></li>
            <li>{SVG_CHECK}<span>Gewobene Saum- und Nackenlabels für Ihr eigenes Marken-Branding</span></li>
            <li>{SVG_CHECK}<span>Einmalige Stickprogramm-Erstellung — jederzeit für Nachbestellungen abrufbar</span></li>
          </ul>
          <div class="service-card-footer">
            {action_dl}
          </div>
        </article>

        <article class="service-card">
          <div class="service-card-head">
            <div class="service-icon-box">{SVG_WRENCH}</div>
            <span class="service-tag">Maximal flexibel</span>
          </div>
          <h3 data-slot="service_4_title" data-wp-slot="service_4_title">Druckservice für angelieferte Fremdtextilien</h3>
          <p data-slot="service_4_desc" data-wp-slot="service_4_desc">
            Sie haben Ihre Trikots, Arbeitskleider oder Spezialtextilien bereits eingekauft? Kein Problem: Wir bedrucken und besticken im hauseigenen Druckatelier auch Ihre angelieferten Textilien fachgerecht.
          </p>
          <ul class="service-list">
            <li>{SVG_CHECK}<span>Prüfung Ihres Materials auf optimale Hitze- und Druckverträglichkeit</span></li>
            <li>{SVG_CHECK}<span>Grafik-Aufbereitung &amp; Vektorisierung Ihrer bestehenden Logos inklusive</span></li>
            <li>{SVG_CHECK}<span>Unkomplizierte Anlieferung direkt an der Mellingerstrasse 12 (Eingang C)</span></li>
          </ul>
          <div class="service-card-footer">
            <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm">
              <span>Projekt direkt anfragen</span>
              {SVG_ARROW}
            </a>
          </div>
        </article>
      </div>
    </div>
  </section>
"""


def render_studio_team_section(is_v2=False):
    profil_btn = (
        """<button type="button" class="btn-cta btn-cta-outline btn-sm" onclick="wpOpenBlueprintModal('Profil, Atelier &amp; Team', 'In der fertigen Webseite stellen wir Ihr Atelier in Niederrohrdorf, Ihre Geschichte seit 1998 sowie Stefan Fritschi und Raimondo auf einer eigenen Profil-Seite ausführlich vor.')"><span>Ausbau-Details zur Profil-Seite</span>""" + SVG_ARROW + """</button>"""
        if is_v2
        else f"""<a href="profil.html" class="btn-cta btn-cta-outline btn-sm"><span>Mehr über unser Atelier &amp; Profil</span>{SVG_ARROW}</a>"""
    )
    return f"""
  <section class="section section-alt" id="atelier">
    <div class="container">
      <div class="studio-showcase">
        <div>
          <div class="section-eyebrow">
            {SVG_USERS}
            <span>Persönlich in CH-5443 Niederrohrdorf</span>
          </div>
          <h2 class="section-title" data-slot="studio_headline" data-wp-slot="studio_headline">
            Herzblut, Erfahrung &amp; direkte Ansprechpartner
          </h2>
          <p class="section-lead" style="margin-bottom:20px;" data-slot="studio_subheadline" data-wp-slot="studio_subheadline">
            Hinter Free's steht Stefan Fritschi gemeinsam mit Raimondo. Seit 1998 leben wir Teamsport, Workwear und Textilveredelung. Bei uns sprechen Sie nicht mit einem anonymen Callcenter, sondern direkt mit den Machern an der Druckmaschine.
          </p>

          <div class="team-card" style="margin-bottom:14px;">
            <div class="team-role">Inhaber · Beratung, Einkauf &amp; Textildruck</div>
            <h3 class="team-name" data-slot="team_stefan_name" data-wp-slot="team_stefan_name">Stefan Fritschi</h3>
            <p class="team-bio" data-slot="team_stefan_bio" data-wp-slot="team_stefan_bio">
              Seit 1998 in der Textil- und Sportbranche verwurzelt. Berät Vereine, Firmen und Organisationen persönlich bei der Kollektionswahl und sorgt im eigenen Druckatelier für makellose Resultate.
            </p>
            <div class="team-contact-links">
              <a href="tel:+41797091224" class="team-contact-pill">{SVG_PHONE}<span>+41 79 709 12 24</span></a>
              <a href="mailto:info@frees.ch" class="team-contact-pill">{SVG_MAIL}<span>info@frees.ch</span></a>
            </div>
          </div>

          <div class="team-card" style="margin-bottom:20px;">
            <div class="team-role">Beratung, Textilveredelung &amp; Produktion</div>
            <h3 class="team-name" data-slot="team_raimondo_name" data-wp-slot="team_raimondo_name">Raimondo</h3>
            <p class="team-bio" data-slot="team_raimondo_bio" data-wp-slot="team_raimondo_bio">
              Ihr direkter Ansprechpartner für Produktion, Bemusterung, Textildruck und termingerechte Auftragsabwicklung im Atelier Niederrohrdorf.
            </p>
            <div class="team-contact-links">
              <a href="tel:+41799665978" class="team-contact-pill">{SVG_PHONE}<span>+41 79 966 59 78</span></a>
              <a href="mailto:info@frees.ch" class="team-contact-pill">{SVG_MAIL}<span>info@frees.ch</span></a>
            </div>
          </div>

          <div style="display:flex;flex-wrap:wrap;gap:12px;align-items:center;">
            <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm">
              <span>Termin im Showroom vereinbaren</span>
              {SVG_ARROW}
            </a>
            {profil_btn}
          </div>
        </div>

        <div class="studio-photo-stack">
          <div class="studio-photo-main">
            <img src="images/atelier-inside.jpg" alt="Free's Showroom und Atelier in Niederrohrdorf" width="600" height="340" loading="lazy" data-slot="studio_image_main" data-wp-slot="studio_image_main">
          </div>
          <div class="studio-photo-sub">
            <img src="images/druckservice-maschine.jpg" alt="Inhouse Textildruck-Maschine bei Free's" width="320" height="220" loading="lazy" data-slot="studio_image_sub" data-wp-slot="studio_image_sub">
            <div class="studio-fact-box">
              <h4>Standort &amp; Öffnungszeiten</h4>
              <p style="margin-bottom:10px;">
                <strong>Mellingerstrasse 12</strong><br>
                Eingang C · 1. Stock<br>
                CH-5443 Niederrohrdorf
              </p>
              <p style="color:#FBBF24;font-weight:700;">
                Öffnungszeiten: Nach Vereinbarung via Mail oder Telefon.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""


def render_cta_banner():
    return f"""
  <section class="section">
    <div class="container">
      <div class="cta-banner">
        <div>
          <div class="hero-eyebrow" style="margin-bottom:12px;">
            {SVG_SPARKLES}
            <span>Unverbindliche Offerte &amp; Musterberatung</span>
          </div>
          <h2 data-slot="cta_banner_title" data-wp-slot="cta_banner_title">
            Bereit für Ihren neuen Team- oder Firmenauftritt?
          </h2>
          <p data-slot="cta_banner_desc" data-wp-slot="cta_banner_desc">
            Starten Sie unsere interaktive 3-Schritte-Anfrage oder rufen Sie Stefan Fritschi (+41 79 709 12 24) und Raimondo (+41 79 966 59 78) direkt an.
          </p>
        </div>
        <div class="cta-banner-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-primary">
            <span>Jetzt 3-Schritte-Anfrage starten</span>
            {SVG_ARROW}
          </a>
          <a href="tel:+41797091224" class="btn-cta btn-cta-white">
            {SVG_PHONE}
            <span>+41 79 709 12 24</span>
          </a>
        </div>
      </div>
    </div>
  </section>
"""


V1_INDEX_BODY = f"""
{render_hero_section(is_v2=False)}
{render_services_pillars_section(is_v2=False)}

  <section class="section section-dark" id="katalog-vorschau">
    <div class="container">
      <div class="section-header" style="display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:20px;max-width:none;">
        <div style="max-width:680px;">
          <div class="section-eyebrow" style="color:#F87171;">
            {SVG_BOOK}
            <span>Direktzugriff auf Top-Marken</span>
          </div>
          <h2 class="section-title" style="color:#FFFFFF;" data-slot="home_catalogs_title" data-wp-slot="home_catalogs_title">
            Online-Shop &amp; 14 Marken-Blätterkataloge
          </h2>
          <p class="section-lead" style="color:#CBD5E1;" data-slot="home_catalogs_sub" data-wp-slot="home_catalogs_sub">
            Stöbern Sie direkt in unserem Hauptshop <strong>frees.alltextiles.ch</strong> oder blättern Sie online durch die aktuellen Kollektionen von JAKO, ERIMA, F. ENGEL, HAKRO, CRAFT, CLIQUE und weiteren Marken.
          </p>
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:12px;">
          <a href="https://frees.alltextiles.ch" target="_blank" rel="noopener" class="btn-cta btn-cta-primary btn-sm">
            {SVG_SHOP}
            <span>Hauptshop frees.alltextiles.ch</span>
          </a>
          <a href="textilsortiment.html" class="btn-cta btn-cta-white btn-sm">
            <span>Alle 14 Kataloge ansehen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>

      {render_catalogs_grid(limit=4)}
    </div>
  </section>

{render_studio_team_section(is_v2=False)}
{render_cta_banner()}
"""


V1_DIENSTLEISTUNGEN_BODY = f"""
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb">
        <a href="index.html">Start</a>
        <span>/</span>
        <span>Dienstleistungen</span>
      </div>
      <div class="hero-eyebrow">
        {SVG_PRINTER}
        <span>Eigenes Druckatelier · Textilveredelung &amp; Stickerei</span>
      </div>
      <h1 data-slot="dl_hero_headline" data-wp-slot="dl_hero_headline">
        Textildruck, Stickerei, Labels &amp; Fremdtextil-Service
      </h1>
      <p data-slot="dl_hero_sub" data-wp-slot="dl_hero_sub">
        In unserem eigenen Druckatelier an der Mellingerstrasse 12 in Niederrohrdorf veredeln wir Vereinsbekleidung, Workwear und Promowear präzise nach Ihren Vorgaben — vom Einzelstück bis zur Grossserie.
      </p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="grid-2" style="margin-bottom:40px;">
        <article class="service-card">
          <div class="service-card-head">
            <div class="service-icon-box">{SVG_PRINTER}</div>
            <span class="service-tag">100 % Inhouse in Niederrohrdorf</span>
          </div>
          <h3 data-slot="dl_card1_title" data-wp-slot="dl_card1_title">1. Textildruck, Transferdruck &amp; Beflockung</h3>
          <p data-slot="dl_card1_desc" data-wp-slot="dl_card1_desc">
            Ob Sporttrikots mit Spielernummern, Vereinsnamen und Sponsorenlogos oder robuste Arbeitskleidung mit Firmenlogo: Wir wählen für jedes Gewebe (Polyester, Baumwolle, Mischgewebe, Softshell) das exakt passende Druckverfahren.
          </p>
          <ul class="service-list">
            <li>{SVG_CHECK}<span><strong>Flex- &amp; Flockdruck:</strong> Extrem haltbar, deckend und ideal für Trikotnummern, Initialen und klare Logos.</span></li>
            <li>{SVG_CHECK}<span><strong>Digitaler Transferdruck &amp; DTF:</strong> Gestochen scharfe Mehrfarben-Logos, Farbverläufe und feinste Details.</span></li>
            <li>{SVG_CHECK}<span><strong>Siebdruck &amp; Siebtransfer:</strong> Wirtschaftlich und langlebig für grössere Auflagen bei Events, Vereinen und Firmen.</span></li>
          </ul>
        </article>

        <article class="service-card">
          <div class="service-card-head">
            <div class="service-icon-box">{SVG_SPARKLES}</div>
            <span class="service-tag">Präzision &amp; Beständigkeit</span>
          </div>
          <h3 data-slot="dl_card2_title" data-wp-slot="dl_card2_title">2. Direkteinstickung &amp; gestickte Abzeichen</h3>
          <p data-slot="dl_card2_desc" data-wp-slot="dl_card2_desc">
            Eine Stickerei verleiht Poloshirts, Hemden, Caps, Fleece- und Winterjacken eine unverwechselbare, dreidimensionale Wertigkeit und hält selbst höchsten Beanspruchungen im Arbeitsalltag stand.
          </p>
          <ul class="service-list">
            <li>{SVG_CHECK}<span><strong>Direkteinstickung:</strong> Brust-, Kragen-, Ärmel- oder Rückenstickerei mit hochwertigen Marken-Stickgarnen.</span></li>
            <li>{SVG_CHECK}<span><strong>Stick-Patches &amp; Embleme:</strong> Gestickte Vereinswappen und Firmen-Aufnäher zum Aufbügeln oder Aufnähen.</span></li>
            <li>{SVG_CHECK}<span><strong>Archivierte Stickkarten:</strong> Ihr Logo wird einmalig digitalisiert und ist für jede Nachbestellung sofort bereit.</span></li>
          </ul>
        </article>

        <article class="service-card">
          <div class="service-card-head">
            <div class="service-icon-box">{SVG_AWARD}</div>
            <span class="service-tag">Individuelles Branding</span>
          </div>
          <h3 data-slot="dl_card3_title" data-wp-slot="dl_card3_title">3. Gewobene &amp; gestickte Textil-Labels</h3>
          <p data-slot="dl_card3_desc" data-wp-slot="dl_card3_desc">
            Machen Sie Ihre Vereins- oder Firmenkollektion unverwechselbar: Wir liefern und applizieren individuell gewobene oder gestickte Labels am Saum, Ärmel oder Nacken.
          </p>
          <ul class="service-list">
            <li>{SVG_CHECK}<span>Fein gewobene Webetiketten mit Ihrem Vereins- oder Firmenwappen</span></li>
            <li>{SVG_CHECK}<span>Dezente Saum- und Bundlabels für Corporate Fashion und Merchandising</span></li>
            <li>{SVG_CHECK}<span>Kombinierbar mit Druck und Stickerei für einen durchgängigen Markenauftritt</span></li>
          </ul>
        </article>

        <article class="service-card">
          <div class="service-card-head">
            <div class="service-icon-box">{SVG_WRENCH}</div>
            <span class="service-tag">Eigene Ware willkommen</span>
          </div>
          <h3 data-slot="dl_card4_title" data-wp-slot="dl_card4_title">4. Druckservice für angelieferte Fremdtextilien &amp; Grafik</h3>
          <p data-slot="dl_card4_desc" data-wp-slot="dl_card4_desc">
            Nicht jedes Textil muss zwingend über uns bezogen werden. In unserem eigenen Druckatelier veredeln wir gerne auch Ihre bereits vorhandenen oder selbst eingekauften Kleidungsstücke.
          </p>
          <ul class="service-list">
            <li>{SVG_CHECK}<span>Fachmännische Beurteilung der Textilqualität vor dem Druckvorgang</span></li>
            <li>{SVG_CHECK}<span>Grafikdesign &amp; Aufbereitung Ihrer Druckdaten (Vektorisierung von Vorlagen)</span></li>
            <li>{SVG_CHECK}<span>Klare Vorab-Ansicht (Gut zum Druck) zur sicheren Freigabe vor Produktionsstart</span></li>
          </ul>
        </article>
      </div>

      <div class="studio-showcase" style="background:var(--bg-muted);padding:32px;border-radius:var(--radius-card);border:1px solid var(--border-subtle);">
        <div>
          <div class="section-eyebrow">
            {SVG_CHECK}
            <span>In 4 Schritten zum fertigen Textil</span>
          </div>
          <h2 class="section-title" style="font-size:1.75rem;" data-slot="dl_process_title" data-wp-slot="dl_process_title">
            So unkompliziert läuft Ihr Auftrag bei Free's ab
          </h2>
          <div style="display:grid;gap:14px;margin-top:20px;">
            <div style="background:#FFFFFF;padding:16px 18px;border-radius:var(--radius-btn);border:1px solid var(--border-subtle);">
              <strong style="color:var(--brand-primary);font-family:var(--font-display);">1. Beratung &amp; Musterwahl:</strong>
              <span style="color:var(--text-secondary);font-size:0.92rem;display:block;margin-top:4px;">Sie wählen Artikel aus unseren 14 Katalogen (oder bringen eigene Textilien mit). Gerne stellen wir Grössen-Muster bereit.</span>
            </div>
            <div style="background:#FFFFFF;padding:16px 18px;border-radius:var(--radius-btn);border:1px solid var(--border-subtle);">
              <strong style="color:var(--brand-primary);font-family:var(--font-display);">2. Grafik &amp; Gut zum Druck:</strong>
              <span style="color:var(--text-secondary);font-size:0.92rem;display:block;margin-top:4px;">Wir prüfen Ihr Logo, definieren Position und Grösse und erstellen eine übersichtliche Freigabe-Ansicht.</span>
            </div>
            <div style="background:#FFFFFF;padding:16px 18px;border-radius:var(--radius-btn);border:1px solid var(--border-subtle);">
              <strong style="color:var(--brand-primary);font-family:var(--font-display);">3. Inhouse Veredelung:</strong>
              <span style="color:var(--text-secondary);font-size:0.92rem;display:block;margin-top:4px;">Stefan Fritschi und Raimondo veredeln Ihre Textilien direkt im Atelier an der Mellingerstrasse 12 in Niederrohrdorf.</span>
            </div>
            <div style="background:#FFFFFF;padding:16px 18px;border-radius:var(--radius-btn);border:1px solid var(--border-subtle);">
              <strong style="color:var(--brand-primary);font-family:var(--font-display);">4. Abholung oder Versand:</strong>
              <span style="color:var(--text-secondary);font-size:0.92rem;display:block;margin-top:4px;">Bequeme Abholung nach Terminvereinbarung in Niederrohrdorf oder direkter Postversand an Ihre Wunschadresse.</span>
            </div>
          </div>
        </div>
        <div>
          <div class="studio-photo-main" style="margin-bottom:16px;">
            <img src="images/druckservice-maschine.jpg" alt="Free's Druckmaschine im Atelier Niederrohrdorf" width="560" height="320" loading="lazy">
          </div>
          <div class="studio-fact-box">
            <h4>Haben Sie bereits eine Logo-Datei oder eine Stückliste?</h4>
            <p style="margin-bottom:14px;">Senden Sie uns Ihre Eckdaten bequem über unsere 3-Schritte Smart-Anfrage oder direkt per Mail an <a href="mailto:info@frees.ch" style="color:#FBBF24;font-weight:700;">info@frees.ch</a>.</p>
            <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm">
              <span>Jetzt Druck-Offerte anfragen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
"""


V1_TEXTILSORTIMENT_BODY = f"""
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb">
        <a href="index.html">Start</a>
        <span>/</span>
        <span>Textilsortiment &amp; Kataloge</span>
      </div>
      <div class="hero-eyebrow">
        {SVG_BOOK}
        <span>Hauptshop frees.alltextiles.ch &amp; 13 Marken-Blätterkataloge</span>
      </div>
      <h1 data-slot="sortiment_hero_headline" data-wp-slot="sortiment_hero_headline">
        Unser gesamtes Textilsortiment auf einen Blick
      </h1>
      <p data-slot="sortiment_hero_sub" data-wp-slot="sortiment_hero_sub">
        Wählen Sie Ihre Wunschartikel im grossen Online-Shop <strong>frees.alltextiles.ch</strong> oder blättern Sie direkt in den aktuellen Marken-Katalogen. Notieren Sie sich einfach Artikelnummer und Farbe — wir kümmern uns um Muster, Offerte und Veredelung.
      </p>
      <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:24px;">
        <a href="https://frees.alltextiles.ch" target="_blank" rel="noopener" class="btn-cta btn-cta-primary">
          {SVG_SHOP}
          <span>Hauptshop frees.alltextiles.ch öffnen</span>
        </a>
        <a href="kontakt.html" class="btn-cta btn-cta-white">
          <span>Wunschartikel mit Druck anfragen</span>
          {SVG_ARROW}
        </a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-header">
        <div class="section-eyebrow">
          {SVG_SHIRT}
          <span>Alle 14 Original-Kataloge zum Durchblättern</span>
        </div>
        <h2 class="section-title" data-slot="catalog_grid_title" data-wp-slot="catalog_grid_title">
          Teamsport, Workwear, Corporate Fashion &amp; Basics
        </h2>
        <p class="section-lead" data-slot="catalog_grid_sub" data-wp-slot="catalog_grid_sub">
          Mit einem Klick auf das jeweilige Katalog-Cover öffnet sich der offizielle Online-Blätterkatalog (oder unser Alltextiles-Hauptshop) in einem neuen Fenster.
        </p>
      </div>

      {render_catalogs_grid()}
    </div>
  </section>

  {render_cta_banner()}
"""


V1_PROFIL_BODY = f"""
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb">
        <a href="index.html">Start</a>
        <span>/</span>
        <span>Profil &amp; Atelier</span>
      </div>
      <div class="hero-eyebrow">
        {SVG_AWARD}
        <span>Seit 1998 in der Branche · Mellingerstrasse 12, CH-5443 Niederrohrdorf</span>
      </div>
      <h1 data-slot="profil_hero_headline" data-wp-slot="profil_hero_headline">
        Über Free's — Persönlich, flexibel und mit eigenem Druckatelier
      </h1>
      <p data-slot="profil_hero_sub" data-wp-slot="profil_hero_sub">
        Seit 1998 begleitet Stefan Fritschi gemeinsam mit Raimondo Sportvereine, Handwerksbetriebe, KMU und Schulen bei der Beschaffung und Veredelung hochwertiger Textilien.
      </p>
    </div>
  </section>

  {render_studio_team_section(is_v2=False)}

  <section class="section">
    <div class="container">
      <div class="grid-3">
        <div class="service-card">
          <div class="service-icon-box" style="margin-bottom:14px;">{SVG_AWARD}</div>
          <h3 data-slot="profil_val1_title" data-wp-slot="profil_val1_title">Erfahrung seit 1998</h3>
          <p data-slot="profil_val1_desc" data-wp-slot="profil_val1_desc">
            Wir kennen die Schnitte, Qualitäten und Wascheigenschaften der führenden Textilmarken aus über 25 Jahren täglicher Praxis und empfehlen Ihnen ehrlich genau das, was im Einsatz überzeugt.
          </p>
        </div>
        <div class="service-card">
          <div class="service-icon-box" style="margin-bottom:14px;">{SVG_PRINTER}</div>
          <h3 data-slot="profil_val2_title" data-wp-slot="profil_val2_title">Eigenes Druckatelier</h3>
          <p data-slot="profil_val2_desc" data-wp-slot="profil_val2_desc">
            Weil wir direkt bei uns im Haus an der Mellingerstrasse 12 in Niederrohrdorf drucken, behalten wir die volle Kontrolle über Qualität, Positionierung und Liefertermine — auch bei Express-Wünschen.
          </p>
        </div>
        <div class="service-card">
          <div class="service-icon-box" style="margin-bottom:14px;">{SVG_SHIELD}</div>
          <h3 data-slot="profil_val3_title" data-wp-slot="profil_val3_title">Verlässlicher Nachservice</h3>
          <p data-slot="profil_val3_desc" data-wp-slot="profil_val3_desc">
            Neue Mitarbeitende oder neue Vereinsmitglieder? Ihre Druckdaten, Farben und Artikelnummern bleiben bei uns hinterlegt, sodass Nachbestellungen jederzeit schnell und farbtreu möglich sind.
          </p>
        </div>
      </div>
    </div>
  </section>

  {render_cta_banner()}
"""


V2_INDEX_BODY = f"""
{render_hero_section(is_v2=True)}
{render_services_pillars_section(is_v2=True)}

  <section class="section section-alt" id="weitere-themenbereiche">
    <div class="container">
      <div class="section-header">
        <div class="section-eyebrow">
          {SVG_LAYERS}
          <span>Vorschau-Entwurf · Ausbaustufe für das Erstgespräch</span>
        </div>
        <h2 class="section-title" data-slot="v2_scope_headline" data-wp-slot="v2_scope_headline">
          Weitere Themenbereiche beim gemeinsamen Ausbau
        </h2>
        <p class="section-lead" data-slot="v2_scope_subheadline" data-wp-slot="v2_scope_subheadline">
          In dieser Zeigeversion sind die <strong>Startseite</strong> und die <strong>interaktive 3-Schritte Smart-Anfrage (Kontakt)</strong> bereits komplett als Beispiel-Seiten ausgearbeitet. Klicken Sie auf eine der folgenden Karten, um zu sehen, wie wir die weiteren Unterseiten gemeinsam ausbauen.
        </p>
      </div>

      <div class="grid-3">
        <div class="preview-card-dashed" onclick="wpOpenBlueprintModal('Dienstleistungen &amp; Inhouse Druckservice', 'In der fertigen Webseite präsentieren wir hier Ihr gesamtes Veredelungs-Portfolio im eigenen Druckatelier: Textildruck, Beflockung, Stickereien, gewobene und gestickte Labels, Grafikdesign sowie den Druckservice für angelieferte Fremdtextilien.')">
          <div class="preview-badge-pill">
            {SVG_SPARKLES}
            <span>Folgt beim Ausbau · Unterseite 1</span>
          </div>
          <h3>Dienstleistungen &amp; Inhouse Druckservice</h3>
          <p>
            Detaillierte Vorstellung Ihrer Veredelungsverfahren im eigenen Druckatelier in Niederrohrdorf: Flex-/Transferdruck, Stickerei, eigene Textil-Labels sowie Veredelung angelieferter Fremdtextilien.
          </p>
          <span class="btn-cta btn-cta-outline btn-sm" style="align-self:flex-start;">
            <span>Geplanten Seiteninhalt ansehen</span>
            {SVG_ARROW}
          </span>
        </div>

        <div class="preview-card-dashed" onclick="wpOpenBlueprintModal('Textilsortiment &amp; 14 Blätterkataloge', 'In der fertigen Webseite binden wir hier Ihren Haupt-Onlineshop (frees.alltextiles.ch) sowie alle 14 Original-Blätterkataloge (JAKO, ERIMA, F. ENGEL, CLIQUE, CRAFT, HAKRO, PROJOB, WIKLAND, James Harvest u.v.m.) interaktiv mit Direkt-Anfrage ein.')">
          <div class="preview-badge-pill">
            {SVG_BOOK}
            <span>Folgt beim Ausbau · Unterseite 2</span>
          </div>
          <h3>Textilsortiment &amp; 14 Blätterkataloge</h3>
          <p>
            Übersichtliche Markenwelt mit Direktzugang zu <strong>frees.alltextiles.ch</strong> sowie allen 13 Online-Blätterkatalogen für Teamsport, Workwear, Corporate Fashion und Promowear.
          </p>
          <span class="btn-cta btn-cta-outline btn-sm" style="align-self:flex-start;">
            <span>Geplanten Seiteninhalt ansehen</span>
            {SVG_ARROW}
          </span>
        </div>

        <div class="preview-card-dashed" onclick="wpOpenBlueprintModal('Profil, Atelier Niederrohrdorf &amp; Team', 'In der fertigen Webseite stellen wir Ihre Geschichte seit 1998, Ihr eigenes Druckatelier an der Mellingerstrasse 12 in Niederrohrdorf sowie Stefan Fritschi und Raimondo persönlich mit Direktkontakt vor.')">
          <div class="preview-badge-pill">
            {SVG_USERS}
            <span>Folgt beim Ausbau · Unterseite 3</span>
          </div>
          <h3>Profil, Atelier &amp; Ansprechpartner</h3>
          <p>
            Persönliche Vorstellung von Stefan Fritschi und Raimondo, Einblicke in den Showroom an der Mellingerstrasse 12 (Eingang C, 1. Stock) sowie Ihre Qualitätswerte seit 1998.
          </p>
          <span class="btn-cta btn-cta-outline btn-sm" style="align-self:flex-start;">
            <span>Geplanten Seiteninhalt ansehen</span>
            {SVG_ARROW}
          </span>
        </div>
      </div>
    </div>
  </section>

{render_studio_team_section(is_v2=True)}
{render_cta_banner()}
"""


def build_kontakt_body(client_slug: str, source_page: str) -> str:
    return f"""
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb">
        <a href="index.html">Start</a>
        <span>/</span>
        <span>Kontakt, Öffnungszeiten &amp; Smart-Anfrage</span>
      </div>
      <div class="hero-eyebrow">
        {SVG_MAIL}
        <span>Direktkontakt · CH-5443 Niederrohrdorf · Offerte in 3 Schritten</span>
      </div>
      <h1 data-slot="kontakt_hero_headline" data-wp-slot="kontakt_hero_headline">
        Projekt anfragen oder Termin im Atelier vereinbaren
      </h1>
      <p data-slot="kontakt_hero_sub" data-wp-slot="kontakt_hero_sub">
        Nutzen Sie unsere interaktive 3-Schritte Smart-Anfrage für eine schnelle Richtofferte oder kontaktieren Sie Stefan Fritschi und Raimondo direkt per Telefon oder E-Mail.
      </p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="wizard-shell">
        <div class="wizard-card" id="smart-anfrage">
          <div class="wizard-progress">
            <div class="wizard-step-pill active" id="wizPill1">1. Einsatzbereich</div>
            <div class="wizard-step-pill" id="wizPill2">2. Veredelung &amp; Menge</div>
            <div class="wizard-step-pill" id="wizPill3">3. Kontaktdaten</div>
          </div>

          <form id="freesLeadForm" onsubmit="return submitFreesLead(event)">
            <div class="wizard-pane active" id="wizPane1">
              <h2 style="font-size:1.45rem;margin-bottom:6px;" data-slot="wiz_step1_title" data-wp-slot="wiz_step1_title">
                Wofür benötigen Sie Textilien oder Textilveredelung?
              </h2>
              <p style="color:var(--text-secondary);font-size:0.92rem;margin-bottom:18px;">
                Wählen Sie Ihren Schwerpunkt — wir bereiten die passenden Marken- und Druckvorschläge vor.
              </p>

              <div class="option-grid" id="categoryOptions">
                <div class="option-tile selected" data-val="Teamsport &amp; Vereinsausrüstung (JAKO, ERIMA, CRAFT)" onclick="selectOptionTile(this, 'categoryInput')">
                  <div class="option-tile-title">Teamsport &amp; Vereinsausrüstung</div>
                  <div class="option-tile-sub">Trikotsätze, Trainingsanzüge, Taschen &amp; Vereinskollektionen (JAKO, ERIMA, CRAFT)</div>
                </div>
                <div class="option-tile" data-val="Workwear &amp; Firmenbekleidung (F. ENGEL, HAKRO, PROJOB, WIKLAND)" onclick="selectOptionTile(this, 'categoryInput')">
                  <div class="option-tile-title">Workwear &amp; Firmenbekleidung</div>
                  <div class="option-tile-sub">Robuste Arbeitskleidung, Polos, Hoodies &amp; Hemden mit Firmenlogo</div>
                </div>
                <div class="option-tile" data-val="Promowear, Event-Shirts &amp; Abschlusspullis (CLIQUE, Printer)" onclick="selectOptionTile(this, 'categoryInput')">
                  <div class="option-tile-title">Promowear &amp; Event-Textilien</div>
                  <div class="option-tile-sub">T-Shirts, Caps, Taschen &amp; Hoodies für Events, Messen, Feste oder Schulen</div>
                </div>
                <div class="option-tile" data-val="Druckservice / Stickerei für eigene angelieferte Fremdtextilien" onclick="selectOptionTile(this, 'categoryInput')">
                  <div class="option-tile-title">Veredelung eigener Fremdtextilien</div>
                  <div class="option-tile-sub">Sie liefern Ihre vorhandenen Textilien an — wir übernehmen Druck oder Stickerei</div>
                </div>
              </div>
              <input type="hidden" id="categoryInput" value="Teamsport &amp; Vereinsausrüstung (JAKO, ERIMA, CRAFT)">

              <div style="display:flex;justify-content:flex-end;margin-top:22px;">
                <button type="button" class="btn-cta btn-cta-primary" onclick="goWizardStep(2)">
                  <span>Weiter zu Schritt 2</span>
                  {SVG_ARROW}
                </button>
              </div>
            </div>

            <div class="wizard-pane" id="wizPane2">
              <h2 style="font-size:1.45rem;margin-bottom:6px;">
                Gewünschte Veredelung &amp; ungefähre Stückzahl
              </h2>
              <p style="color:var(--text-secondary);font-size:0.92rem;margin-bottom:18px;">
                Geben Sie uns einen kurzen Anhaltspunkt zu Menge, Druck/Stickerei oder Katalog-Artikelnummern.
              </p>

              <div class="form-row-2">
                <div class="form-group">
                  <label class="form-label" for="veredelungSelect">Gewünschte Veredelung</label>
                  <select id="veredelungSelect" class="form-select">
                    <option value="Textildruck / Beflockung (Inhouse Druckatelier)">Textildruck / Beflockung (Inhouse Druckatelier)</option>
                    <option value="Stickerei / Gestickte Abzeichen">Stickerei / Gestickte Abzeichen</option>
                    <option value="Gewobene oder gestickte Textil-Labels">Gewobene oder gestickte Textil-Labels</option>
                    <option value="Kombination (Druck &amp; Stickerei) / Beratung gewünscht">Kombination (Druck &amp; Stickerei) / Beratung gewünscht</option>
                    <option value="Nur Textilien ohne Veredelung">Nur Textilien ohne Veredelung</option>
                  </select>
                </div>
                <div class="form-group">
                  <label class="form-label" for="mengeSelect">Ungefähre Stückzahl</label>
                  <select id="mengeSelect" class="form-select">
                    <option value="1 bis 10 Stück (Kleinauftrag / Muster)">1 bis 10 Stück (Kleinauftrag / Muster)</option>
                    <option value="11 bis 30 Stück (Team / Abteilung)" selected>11 bis 30 Stück (Team / Abteilung)</option>
                    <option value="31 bis 100 Stück (Verein / KMU)">31 bis 100 Stück (Verein / KMU)</option>
                    <option value="Über 100 Stück (Grossserie / Event)">Über 100 Stück (Grossserie / Event)</option>
                  </select>
                </div>
              </div>

              <div class="form-group">
                <label class="form-label" for="projectDetails">Ihre Nachricht, Wunschmarke oder Artikelnummern (optional)</label>
                <textarea id="projectDetails" class="form-textarea" placeholder="z. B. 25x HAKRO Poloshirt mit Brustlogo + Rücken-Schriftzug, oder Terminwunsch zur Anprobe im Atelier Niederrohrdorf..."></textarea>
              </div>

              <div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-top:22px;">
                <button type="button" class="btn-cta btn-cta-outline" onclick="goWizardStep(1)">
                  <span>Zurück</span>
                </button>
                <button type="button" class="btn-cta btn-cta-primary" onclick="goWizardStep(3)">
                  <span>Weiter zu den Kontaktdaten</span>
                  {SVG_ARROW}
                </button>
              </div>
            </div>

            <div class="wizard-pane" id="wizPane3">
              <h2 style="font-size:1.45rem;margin-bottom:6px;">
                Wohin dürfen wir Ihre Rückmeldung senden?
              </h2>
              <p style="color:var(--text-secondary);font-size:0.92rem;margin-bottom:18px;">
                Stefan Fritschi oder Raimondo melden sich persönlich bei Ihnen.
              </p>

              <div class="form-row-2">
                <div class="form-group">
                  <label class="form-label" for="leadName">Vor- und Nachname *</label>
                  <input type="text" id="leadName" class="form-input" required placeholder="z. B. Thomas Meier">
                </div>
                <div class="form-group">
                  <label class="form-label" for="leadCompany">Verein / Firma (optional)</label>
                  <input type="text" id="leadCompany" class="form-input" placeholder="z. B. FC Rohrdorf / Muster Holzbau AG">
                </div>
              </div>

              <div class="form-row-2">
                <div class="form-group">
                  <label class="form-label" for="leadEmail">E-Mail-Adresse *</label>
                  <input type="email" id="leadEmail" class="form-input" required placeholder="thomas.meier@beispiel.ch">
                </div>
                <div class="form-group">
                  <label class="form-label" for="leadPhone">Telefon / Mobile *</label>
                  <input type="tel" id="leadPhone" class="form-input" required placeholder="+41 79 123 45 67">
                </div>
              </div>

              <div id="leadSubmitFeedback" style="display:none;padding:14px 16px;border-radius:var(--radius-btn);margin-bottom:16px;font-weight:600;font-size:0.92rem;"></div>

              <div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-top:20px;">
                <button type="button" class="btn-cta btn-cta-outline" onclick="goWizardStep(2)">
                  <span>Zurück</span>
                </button>
                <button type="submit" id="leadSubmitBtn" class="btn-cta btn-cta-primary">
                  <span>Anfrage verbindlich absenden</span>
                  {SVG_ARROW}
                </button>
              </div>
            </div>
          </form>
        </div>

        <aside style="display:flex;flex-direction:column;gap:18px;">
          <div class="service-card">
            <div class="section-eyebrow" style="margin-bottom:8px;">
              {SVG_MAP_PIN}
              <span>Showroom &amp; Druckatelier</span>
            </div>
            <h3 style="margin-bottom:8px;" data-slot="kontakt_box_title" data-wp-slot="kontakt_box_title">
              Free's Teamsport-Promowear &amp; Print
            </h3>
            <p style="margin-bottom:14px;" data-slot="kontakt_box_address" data-wp-slot="kontakt_box_address">
              <strong>Mellingerstrasse 12</strong><br>
              Eingang C · 1. Stock<br>
              CH-5443 Niederrohrdorf
            </p>
            <div style="background:var(--bg-muted);padding:12px 14px;border-radius:var(--radius-btn);border:1px solid var(--border-subtle);margin-bottom:16px;">
              <div style="font-size:0.78rem;font-weight:700;text-transform:uppercase;color:var(--brand-primary);margin-bottom:4px;">Öffnungszeiten</div>
              <div style="font-size:0.9rem;font-weight:600;color:var(--text-primary);" data-slot="kontakt_hours_box" data-wp-slot="kontakt_hours_box">
                Nach Vereinbarung via Mail oder Telefon.
              </div>
            </div>

            <div style="display:flex;flex-direction:column;gap:10px;">
              <a href="tel:+41797091224" class="team-contact-pill" style="justify-content:space-between;">
                <span><strong>Stefan Fritschi:</strong> +41 79 709 12 24</span>
                {SVG_PHONE}
              </a>
              <a href="tel:+41799665978" class="team-contact-pill" style="justify-content:space-between;">
                <span><strong>Raimondo:</strong> +41 79 966 59 78</span>
                {SVG_PHONE}
              </a>
              <a href="mailto:info@frees.ch" class="team-contact-pill" style="justify-content:space-between;">
                <span><strong>E-Mail:</strong> info@frees.ch</span>
                {SVG_MAIL}
              </a>
            </div>
          </div>

          <div class="studio-fact-box">
            <h4>Direkt im Hauptshop stöbern?</h4>
            <p style="margin-bottom:14px;">
              Über 10'000 sofort lieferbare Textilien finden Sie rund um die Uhr auf unserem Hauptshop <strong>frees.alltextiles.ch</strong>.
            </p>
            <a href="https://frees.alltextiles.ch" target="_blank" rel="noopener" class="btn-cta btn-cta-gold btn-sm">
              {SVG_SHOP}
              <span>Zu frees.alltextiles.ch</span>
            </a>
          </div>
        </aside>
      </div>
    </div>
  </section>

  <script>
  function selectOptionTile(el, inputId) {{
    var container = el.parentElement;
    var tiles = container.querySelectorAll('.option-tile');
    for (var i = 0; i < tiles.length; i++) {{
      tiles[i].classList.remove('selected');
    }}
    el.classList.add('selected');
    var input = document.getElementById(inputId);
    if (input) input.value = el.getAttribute('data-val') || '';
  }}

  function goWizardStep(step) {{
    for (var i = 1; i <= 3; i++) {{
      var pane = document.getElementById('wizPane' + i);
      var pill = document.getElementById('wizPill' + i);
      if (pane) pane.classList.toggle('active', i === step);
      if (pill) pill.classList.toggle('active', i === step);
    }}
  }}

  async function submitFreesLead(e) {{
    e.preventDefault();
    var btn = document.getElementById('leadSubmitBtn');
    var fb = document.getElementById('leadSubmitFeedback');
    var name = (document.getElementById('leadName').value || '').trim();
    var company = (document.getElementById('leadCompany').value || '').trim();
    var email = (document.getElementById('leadEmail').value || '').trim();
    var phone = (document.getElementById('leadPhone').value || '').trim();
    var category = (document.getElementById('categoryInput').value || '').trim();
    var veredelung = (document.getElementById('veredelungSelect').value || '').trim();
    var menge = (document.getElementById('mengeSelect').value || '').trim();
    var details = (document.getElementById('projectDetails').value || '').trim();

    if (!name || !email || !phone) {{
      fb.style.display = 'block';
      fb.style.background = '#FEF2F2';
      fb.style.color = '#991B1B';
      fb.style.border = '1px solid #FECACA';
      fb.textContent = 'Bitte füllen Sie Name, E-Mail und Telefonnummer vollständig aus.';
      return false;
    }}

    btn.disabled = true;
    btn.innerHTML = '<span>Anfrage wird übermittelt...</span>';

    var payload = {{
      client_slug: '{client_slug}',
      route_key: 'general',
      name: name,
      email: email,
      phone: phone,
      message: (details ? details : 'Smart-Anfrage über WebPilot Vorschau (' + category + ')'),
      source_page: '{source_page}',
      extra_fields: {{
        Firma_oder_Verein: company || 'Nicht angegeben',
        Einsatzbereich: category,
        Veredelung: veredelung,
        Stueckzahl: menge
      }}
    }};

    try {{
      var res = await fetch('/api/lead-submit', {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json' }},
        body: JSON.stringify(payload)
      }});
      var data = await res.json();
      if (res.ok && data.ok) {{
        fb.style.display = 'block';
        fb.style.background = '#F0FDF4';
        fb.style.color = '#166534';
        fb.style.border = '1px solid #BBF7D0';
        fb.textContent = 'Herzlichen Dank! Ihre Anfrage wurde erfolgreich erfasst. Stefan Fritschi oder Raimondo melden sich in Kürze bei Ihnen.';
        btn.innerHTML = '<span>Erfolgreich gesendet</span>';
      }} else {{
        throw new Error(data.error || 'Senden fehlgeschlagen');
      }}
    }} catch (err) {{
      fb.style.display = 'block';
      fb.style.background = '#FEF2F2';
      fb.style.color = '#991B1B';
      fb.style.border = '1px solid #FECACA';
      fb.textContent = 'Hinweis: ' + err.message + '. Bitte kontaktieren Sie uns direkt unter info@frees.ch oder +41 79 709 12 24.';
      btn.disabled = false;
      btn.innerHTML = '<span>Erneut versuchen</span>';
    }}
    return false;
  }}
  </script>
"""


def main():
    # Write Variante 1 (Komplettversion: alle 5 Seiten)
    v1_pages = {
        "index.html": (
            "Free's Teamsport-Promowear & Print | Textildruck & Vereinsbekleidung Niederrohrdorf",
            "startseite",
            V1_INDEX_BODY,
        ),
        "dienstleistungen.html": (
            "Dienstleistungen: Textildruck, Stickerei & Labels | Free's Niederrohrdorf",
            "dienstleistungen",
            V1_DIENSTLEISTUNGEN_BODY,
        ),
        "textilsortiment.html": (
            "Textilsortiment: Online-Shop & 14 Marken-Blätterkataloge | Free's Niederrohrdorf",
            "textilsortiment",
            V1_TEXTILSORTIMENT_BODY,
        ),
        "profil.html": (
            "Profil & Atelier Niederrohrdorf | Stefan Fritschi & Raimondo | Free's",
            "profil",
            V1_PROFIL_BODY,
        ),
        "kontakt.html": (
            "Kontakt, Öffnungszeiten & Smart-Anfrage | Free's CH-5443 Niederrohrdorf",
            "kontakt",
            build_kontakt_body("frees", "https://vorschau.magnet-xs.ch/frees/kontakt.html"),
        ),
    }

    for fname, (title, active_nav, body) in v1_pages.items():
        html = render_v1_shell(fname, title, active_nav, body)
        (V1_DIR / fname).write_text(html, encoding="utf-8")
        print(f"[V1] Wrote {V1_DIR / fname}")

    # Write Variante 2 (Zeigeversion / Vorschau-Entwurf: index.html + kontakt.html)
    v2_pages = {
        "index.html": (
            "Free's Teamsport-Promowear & Print | Zeigeversion (Vorschau-Entwurf)",
            "startseite",
            V2_INDEX_BODY,
        ),
        "kontakt.html": (
            "Kontakt & 3-Schritte Smart-Anfrage | Free's Niederrohrdorf (Zeigeversion)",
            "kontakt",
            build_kontakt_body("frees-v2", "https://vorschau.magnet-xs.ch/frees-v2/kontakt.html"),
        ),
    }

    for fname, (title, active_nav, body) in v2_pages.items():
        html = render_v2_shell(fname, title, active_nav, body)
        (V2_DIR / fname).write_text(html, encoding="utf-8")
        print(f"[V2] Wrote {V2_DIR / fname}")

    # Run Partner Attribution injection + Cockpit v4.0 generation + Compile site
    cmds = [
        ["python3", str(V1_DIR.parent / "scripts" / "inject_partner_attribution.py")],
        ["python3", str(V1_DIR.parent / "scripts" / "build_client_cockpit.py"), "--slug", "preview-frees"],
        ["python3", str(V1_DIR.parent / "scripts" / "build_client_cockpit.py"), "--slug", "preview-frees-v2"],
        ["python3", str(V1_DIR.parent / "scripts" / "compile_site.py"), "--site", "preview-frees", "--skip-device-audit"],
        ["python3", str(V1_DIR.parent / "scripts" / "compile_site.py"), "--site", "preview-frees-v2", "--skip-device-audit"],
    ]
    for cmd in cmds:
        print("Running:", " ".join(cmd))
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()

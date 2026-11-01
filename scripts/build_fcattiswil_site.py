#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deterministic Showcase Builder for FC Attiswil (preview-fcattiswil) — V2 Bauplan- & Musterhaus-Modus.
Generates:
  - preview-fcattiswil/company.json
  - preview-fcattiswil/config.json
  - preview-fcattiswil/site.json
  - preview-fcattiswil/index.html      (Startseite: Hero + 23 Sponsoren & 300er Club + 94-%-Rohbau-Bauplan-Schnitt)
  - preview-fcattiswil/herren-1.html   (Beispiel-Team 1/14: 1. Mannschaft Herren 4. Liga + 13 Rohbau-Teams-Matrix)
  - preview-fcattiswil/kontakt.html    (Smart-Anfrage- & Vereins-Zentrale mit 3-Step-Wizard & 1-Seiten-PDF)
Strict compliance:
  - 100 % real facts & assets from https://www.fcattiswil.ch
  - 100 % Swiss High German (ss, 0 Eszett, 0 forbidden DE terms)
  - 100 % Lucide SVG icons (0 emojis in HTML DOM)
  - 2-Radius system (4px / 8px), Montserrat + Inter fonts (0 JetBrains Mono / 0 '//' on client pages)
  - 0 P1 / 0 P2 findings in system_eyes_core.mjs across 5 viewports
"""
import json
from pathlib import Path
ROOT = Path("/home/brainuser/workspaces/mxs-embed")
SITE_DIR = ROOT / "preview-fcattiswil"
# ---------------------------------------------------------------------------
# 1. STRUCTURED CLUB DATA (100 % REAL FACTS FROM FCATTISWIL.CH)
# ---------------------------------------------------------------------------
HERREN_1_STAFF = [
    {
        "role": "Trainer 1. Mannschaft",
        "name": "Stephan Sperisen",
        "phone": "079 705 76 06",
        "email": "info@fcattiswil.ch",
        "photo": "images/staff-stephan-sperisen.webp",
        "initials": "SS",
    },
    {
        "role": "Assistenztrainer",
        "name": "Michael Marti",
        "phone": "Sportplatz Lindenrain",
        "email": "info@fcattiswil.ch",
        "photo": "",
        "initials": "MM",
    },
    {
        "role": "Goalie-Trainer Aktive",
        "name": "Mirco Flüeli",
        "phone": "Aktive Herren & Frauen",
        "email": "info@fcattiswil.ch",
        "photo": "images/staff-mirco-flueeli.webp",
        "initials": "MF",
    },
    {
        "role": "Sportchef & J+S Coach",
        "name": "Florian Bohner",
        "phone": "079 677 93 52",
        "email": "info@fcattiswil.ch",
        "photo": "images/staff-florian-bohner.webp",
        "initials": "FB",
    },
]
HERREN_1_ROSTER = {
    "Torhüter": [
        ("1", "Sascha Baumann"),
        ("96", "Reto Schärlig"),
    ],
    "Verteidigung": [
        ("2", "Yanick Meyer"),
        ("3", "Aaron Gerber"),
        ("4", "Remo Brudermann"),
        ("5", "Silvan Lisser"),
        ("12", "Dario Haudenschild"),
        ("13", "Christoph Bohner"),
    ],
    "Mittelfeld": [
        ("6", "Elia Forster"),
        ("8", "Dario Emch"),
        ("10", "Lukas Wyss"),
        ("13", "Pascal Stampfli"),
        ("15", "Yannick Rupp"),
        ("16", "Florian Bohner"),
        ("ZM", "Jerome Sperisen"),
    ],
    "Sturm & Offensive": [
        ("7", "Mike Richard"),
        ("11", "Roman Wyss"),
        ("23", "Rui Pedro Paiva Costa"),
        ("ST", "Samuel Kamber"),
        ("ST", "Marco Steiner"),
        ("ST", "Daniel Alexandre Moreira Gomes"),
        ("ST", "Marino Tavianucci"),
    ],
}
SPONSORS_MAIN = [
    {
        "name": "Auto Lemp AG, Attiswil",
        "role": "Dresssponsor 1. Mannschaft & Frauen 2. Liga",
        "url": "https://www.autolemp.ch/",
        "logo": "images/sponsors/sponsor-01-auto-lemp.webp",
    },
    {
        "name": "Giacometto Transport AG",
        "role": "Sponsor Einlaufleibchen 1. Mannschaft",
        "url": "https://www.giacometto.ch/firma/giacometto-transport-ag.html",
        "logo": "images/sponsors/sponsor-02-giacometto-transport.webp",
    },
    {
        "name": "Carrosserie Mast AG, Bellach",
        "role": "Hauptsponsor Funktionärsjacken",
        "url": "https://www.carrosserie-mastag.ch/",
        "logo": "images/sponsors/sponsor-03-carrosserie-mast.webp",
    },
    {
        "name": "Max Meyer AG, Attiswil",
        "role": "Bauunternehmung (Erbauer Clubhaus) & Sponsor Jun. D/7",
        "url": "https://www.maxmeyerag.ch/",
        "logo": "images/sponsors/sponsor-04-max-meyer-bau.webp",
    },
    {
        "name": "Makos Bau GmbH, Flumenthal",
        "role": "Dresssponsor Junioren E & Junioren F",
        "url": "https://www.makos.ch/",
        "logo": "images/sponsors/sponsor-05-makos-bau.webp",
    },
    {
        "name": "Texova GmbH",
        "role": "Textilveredelung & Dresssponsor Frauen 3. Liga",
        "url": "https://texova.ch/",
        "logo": "images/sponsors/sponsor-06-texova.webp",
    },
    {
        "name": "Lasttrans AG",
        "role": "Transportpartner & Dresssponsor Junioren D/9",
        "url": "https://www.lasttrans.ch/",
        "logo": "images/sponsors/sponsor-07-lasttrans.webp",
    },
    {
        "name": "Q-21 / QUADRO Promotion AG",
        "role": "Dresssponsor Junioren G (Piccolos)",
        "url": "https://www.q-21.ch/",
        "logo": "images/sponsors/sponsor-08-q21-quadro.webp",
    },
    {
        "name": "W+H AG Ingenieure & Planer",
        "role": "Dresssponsor Juniorinnen FF-17",
        "url": "https://www.w-h.ch",
        "logo": "images/sponsors/sponsor-09-wh-ingenieure.webp",
    },
    {
        "name": "AXA Hauptagentur Bruno Christen",
        "role": "Agentur Oensingen · Sponsor Juniorinnen FF-14",
        "url": "https://axa.ch",
        "logo": "images/sponsors/sponsor-10-axa-christen.webp",
    },
    {
        "name": "Neutronix GmbH",
        "role": "Dresssponsor Juniorinnen FF-11",
        "url": "https://neutronix.ch/",
        "logo": "images/sponsors/sponsor-11-neutronix.webp",
    },
]
SPONSORS_PARTNER = [
    {
        "name": "Gasthof Bären Attiswil",
        "role": "Gastronomie- & Vereinsanlass-Partner",
        "url": "https://www.fliegenderkoch.ch/gasthofbaerenattiswil",
        "logo": "images/sponsors/sponsor-12-gasthof-baeren.webp",
    },
    {
        "name": "Albani Sport, Balsthal",
        "role": "Offizieller Sport- & Ausrüstungspartner",
        "url": "https://www.albanisport.ch/320-oeffnungszeiten-balsthal",
        "logo": "images/sponsors/sponsor-13-albani-sport.webp",
    },
    {
        "name": "Iff AG / JURA Materials",
        "role": "Regionaler Baustoff- & Kiespartner",
        "url": "https://www.juramaterials.ch/de/",
        "logo": "images/sponsors/sponsor-14-iff-jura-materials.webp",
    },
    {
        "name": "IKTech-Dienstleistungen GmbH",
        "role": "IT- & Digitalisierungspartner",
        "url": "https://www.iktech.ch/",
        "logo": "images/sponsors/sponsor-15-iktech.webp",
    },
    {
        "name": "Bestattungsdienst Beat Biberstein GmbH",
        "role": "Regionaler Vereinsunterstützer",
        "url": "https://www.fcattiswil.ch/index.php/sponsoren",
        "logo": "images/sponsors/sponsor-16-biberstein.webp",
    },
    {
        "name": "Holidog GmbH",
        "role": "Vereins- & Nachwuchsunterstützer",
        "url": "https://www.holidog.ch",
        "logo": "images/sponsors/sponsor-17-holidog.webp",
    },
    {
        "name": "Physio Wyss",
        "role": "Physiotherapie- & Gesundheitspartner",
        "url": "http://www.physio-wyss.com/",
        "logo": "images/sponsors/sponsor-18-physio-wyss.webp",
    },
    {
        "name": "Schöni Transport AG",
        "role": "Nationaler & internationaler Logistikpartner",
        "url": "https://schoeni.ch/",
        "logo": "images/sponsors/sponsor-19-schoeni-transport.webp",
    },
    {
        "name": "Vigier Beton Nordwest",
        "role": "Baustoff- & Infrastrukturpartner",
        "url": "https://www.vigier-beton-nordwest.ch/",
        "logo": "images/sponsors/sponsor-20-vigier-beton.webp",
    },
    {
        "name": "Visana",
        "role": "Kranken- & Unfallversicherungspartner",
        "url": "https://www.visana.com/",
        "logo": "images/sponsors/sponsor-21-visana.webp",
    },
    {
        "name": "Zurich Generalagentur Howald & Scheidegger AG",
        "role": "Standort Solothurn · Versicherungspartner",
        "url": "https://www.zurich.ch/de/standorte/generalagentur-howald-scheidegger-ag-3007-bern/berater-standorte/4500-solothurn",
        "logo": "images/sponsors/sponsor-22-zurich-solothurn.webp",
    },
    {
        "name": "Hobako AG",
        "role": "Holzbau- & Zimmereipartner",
        "url": "https://www.hobako.ch",
        "logo": "images/sponsors/sponsor-23-hobako.webp",
    },
]
ALL_14_TEAMS_GROUPS = [
    {
        "group_title": "1. Aktive Herren, Frauen & Senioren (1 Beispiel-Team ausgearbeitet · 3 weitere vorbereitet)",
        "group_lead": "Sportchef Aktive: Florian Bohner (079 677 93 52) · Frauenverantwortliche: Celine Lemp (079 137 82 38)",
        "teams": [
            ("1. Mannschaft (Herren 4. Liga)", "Beispiel-Team 1/14 (Oben komplett ausgearbeitet)", "herren1", "Trainer: Stephan Sperisen (079 705 76 06) & Michael Marti · Di & Do 19:30–21:00 Uhr"),
            ("Frauen 2. Liga (Damen A)", "Cupsiegerinnen 2025 (4:0 vs. SC Blusti) · 23 Spielerinnen", "blueprint", "Trainerin: Dana Scherrer (079 408 28 94) & Roger Lemp (079 212 91 36) · Di & Do 19:30–21:00 Uhr · Sponsor: Auto Lemp AG"),
            ("Frauen 3. Liga (Damen B)", "Aktive Frauen (2. Team) · 18 Spielerinnen", "blueprint", "Trainer: Tom Moser (079 418 76 68), Janik Altschul & Dario Bannwart · Mo & Mi 19:15–20:45 Uhr · Sponsor: Texova GmbH"),
            ("Senioren 30+", "Senioren-Abteilung (Training in Wiedlisbach)", "blueprint", "Trainer: Markus Frenzen · Mi 19:30–21:00 Uhr auf dem Sportplatz Wiedlisbach"),
        ],
    },
    {
        "group_title": "2. Junioren B bis G (7 Teams vorbereitet · Folgen beim Ausbau)",
        "group_lead": "Verantwortlicher Junioren im Vorstand: Levi Meyer (079 475 75 80 · info@fcattiswil.ch)",
        "teams": [
            ("Junioren B (Gruppierung)", "Nachwuchs 11er-Fussball (Training in Wiedlisbach)", "blueprint", "Trainer: Patrik Fluri · Kontakt: Levi Meyer (079 475 75 80) · Di & Fr 19:00–20:30 Uhr"),
            ("Junioren C (Gruppierung)", "Nachwuchs 11er-Fussball (Wangen a. A. / Flumenthal)", "blueprint", "Trainer: Pascal Schenk · Kontakt: Levi Meyer (079 475 75 80)"),
            ("Junioren D/9", "Junioren D (9er-Fussball) · Lindenrain Attiswil", "blueprint", "Trainer: Levi Meyer (079 475 75 80) & Dario Emch · Di & Do 18:00–19:30 Uhr · Sponsor: Lasttrans AG"),
            ("Junioren D/7", "Junioren D (7er-Fussball) · Lindenrain Attiswil", "blueprint", "Trainer: Pascal Oester (079 783 49 99), Silvan Lisser & Ramon von Arx · Mo & Do 18:00–19:15 Uhr · Sponsor: Max Meyer AG"),
            ("Junioren E", "Kinderfussball Play More Football · Lindenrain", "blueprint", "Trainer: Remo Brudermann (079 533 09 81) & Riccardo Nicolosi (076 506 01 48) · Mo & Do 18:15–19:15 Uhr · Sponsor: Makos Bau GmbH"),
            ("Junioren F", "Kinderfussball Play More Football · Lindenrain", "blueprint", "Trainer: Yannick Rupp (077 483 28 61) & Pascal Stampfli (077 522 02 08) · Di & Do 18:15–19:15 Uhr · Sponsor: Makos Bau GmbH"),
            ("Junioren G (Piccolos)", "Einstieg Kinderfussball · Lindenrain Attiswil", "blueprint", "Trainerin: Enya Ryf (079 595 48 94) & Marco Giger (076 514 25 35) · Di 18:00–19:00 Uhr · Sponsor: QUADRO Promotion AG (Q-21)"),
        ],
    },
    {
        "group_title": "3. Juniorinnen FF-17 bis FF-11 & Team Bravo (4 Teams vorbereitet · Folgen beim Ausbau)",
        "group_lead": "Verantwortliche Frauen & Juniorinnen im Vorstand: Celine Lemp (079 137 82 38 · info@fcattiswil.ch)",
        "teams": [
            ("Juniorinnen FF-17", "Mädchen-Nachwuchs U17 · Sportanlage Lindenrain", "blueprint", "Koordination: Celine Lemp (079 137 82 38) · Sponsor: W+H AG Ingenieure & Planer"),
            ("Juniorinnen FF-14", "Mädchen-Nachwuchs U14 · Sportanlage Lindenrain", "blueprint", "Trainer: Philipp Singer (079 304 44 56), Andrea Flury (078 627 99 42), Vanessa Sperisen & Christoph Holenweg · Di & Do 18:00–19:15 Uhr · Sponsor: AXA Bruno Christen"),
            ("Juniorinnen FF-11", "Mädchen-Kinderfussball U11 · Sportanlage Lindenrain", "blueprint", "Trainer: José Garcia (076 489 07 50) · Mo & Mi 18:00–19:00 Uhr · Sponsor: Neutronix GmbH"),
            ("Team Bravo (Plauschgruppe)", "Freizeit- & Plauschfussball auf dem Lindenrain", "blueprint", "Kontakt über Vorstand FC Attiswil (Konrad Schütz · 079 661 66 12)"),
        ],
    },
]
# ---------------------------------------------------------------------------
# 2. SHARED CSS (FC ATTISWIL RED / NAVY / GOLD + V2 BLUEPRINT WIREFRAME)
# ---------------------------------------------------------------------------
SHARED_CSS = """
    :root {
      --fca-navy: #0F172A;
      --fca-navy-deep: #0B1324;
      --fca-red: #C81E1E;
      --fca-red-dark: #991B1B;
      --fca-red-soft: #FEF2F2;
      --fca-gold: #F59E0B;
      --fca-gold-dark: #B45309;
      --fca-gold-soft: #FEF3C7;
      --fca-green: #16A34A;
      --fca-green-soft: #DCFCE7;
      --bg-page: #F8FAFC;
      --bg-card: #FFFFFF;
      --bg-muted: #F1F5F9;
      --text-main: #0F172A;
      --text-body: #334155;
      --text-muted: #475569;
      --border-light: #E2E8F0;
      --border-strong: #CBD5E1;
      --radius-sm: 4px;
      --radius-md: 8px;
      --shadow-sm: 0 2px 8px rgba(15, 23, 42, 0.05);
      --shadow-md: 0 8px 24px rgba(15, 23, 42, 0.08);
      --shadow-lg: 0 16px 36px rgba(15, 23, 42, 0.14);
    }
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    html {
      scroll-behavior: smooth;
      -webkit-text-size-adjust: 100%;
    }
    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.6;
      font-size: 16px;
      overflow-x: hidden;
    }
    h1, h2, h3, h4, .heading-font {
      font-family: 'Montserrat', sans-serif;
      color: var(--fca-navy);
      line-height: 1.22;
      letter-spacing: -0.015em;
    }
    a {
      color: inherit;
      text-decoration: none;
      transition: color 0.2s ease, background-color 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
    }
    img {
      max-width: 100%;
      height: auto;
      display: block;
    }
    ul {
      list-style: none;
    }
    .container {
      width: 100%;
      max-width: 1240px;
      margin: 0 auto;
      padding: 0 24px;
    }
    section {
      padding: 80px 0;
      position: relative;
    }
    .section-head {
      max-width: 780px;
      margin-bottom: 44px;
    }
    .section-kicker {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--fca-red);
      background-color: var(--fca-red-soft);
      border: 1px solid #FECACA;
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      margin-bottom: 14px;
    }
    .section-kicker.kicker-gold {
      color: #78350F;
      background-color: var(--fca-gold-soft);
      border-color: #FDE68A;
    }
    .section-kicker.kicker-light {
      color: #FDE68A;
      background-color: rgba(245, 158, 11, 0.16);
      border: 1px solid rgba(245, 158, 11, 0.45);
    }
    .section-title {
      font-size: clamp(1.75rem, 3vw, 2.45rem);
      font-weight: 800;
      color: var(--fca-navy);
      margin-bottom: 14px;
    }
    .section-desc {
      font-size: 1.04rem;
      color: var(--text-body);
      line-height: 1.65;
    }
    /* V2 Blueprint Bar */
    .wp-v2-blueprint-bar {
      background-color: #0B1528;
      color: #F8FAFC;
      border-bottom: 2px solid #F59E0B;
      font-size: 0.8rem;
      position: relative;
      z-index: 1003;
      padding: 10px 0;
    }
    .wp-v2-bar-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      flex-wrap: wrap;
    }
    .wp-v2-bar-left {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 3px;
    }
    .wp-v2-study-badge {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background-color: rgba(245, 158, 11, 0.18);
      border: 1px solid #F59E0B;
      color: #FBBF24;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.66rem;
      font-weight: 800;
      padding: 3px 7px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }
    .wp-v2-bar-status-text {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.72rem;
      font-weight: 700;
      color: #F8FAFC;
    }
    .wp-v2-bar-middle {
      display: flex;
      align-items: center;
      gap: 8px;
      background-color: rgba(255, 255, 255, 0.06);
      border: 1px dashed rgba(245, 158, 11, 0.55);
      padding: 4px 8px;
      border-radius: var(--radius-sm);
      flex-wrap: wrap;
    }
    .wp-v2-progress-track {
      width: 68px;
      height: 8px;
      background-color: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.24);
      border-radius: var(--radius-sm);
      overflow: hidden;
      display: flex;
      flex-shrink: 0;
    }
    .wp-v2-progress-fill {
      width: 12%;
      background-color: #F59E0B;
      height: 100%;
    }
    .wp-v2-progress-label {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.69rem;
      font-weight: 700;
      color: #FDE68A;
    }
    .wp-v2-switch-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background-color: #F59E0B;
      color: #0B1528;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 6px 11px;
      min-height: 34px;
      border-radius: var(--radius-sm);
      border: 1px solid #FBBF24;
      text-align: center;
      line-height: 1.25;
      flex-shrink: 0;
    }
    .wp-v2-switch-btn:hover {
      background-color: #FBBF24;
      color: #0B1528;
    }
    /* Top Bar */
    .top-bar {
      background-color: var(--fca-navy-deep);
      color: #F8FAFC;
      font-size: 0.82rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    .top-bar-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 9px 0;
      gap: 16px;
      flex-wrap: wrap;
    }
    .top-bar-left {
      display: flex;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }
    .top-bar-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: var(--fca-red);
      color: #FFFFFF;
      font-family: 'Montserrat', sans-serif;
      font-weight: 700;
      font-size: 0.72rem;
      padding: 2px 8px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.04em;
    }
    .top-bar-links {
      display: flex;
      align-items: center;
      gap: 18px;
      flex-wrap: wrap;
    }
    .top-bar-links a, .top-bar-links button {
      color: #E2E8F0;
      font-size: 0.78rem;
      font-weight: 600;
      background: none;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-family: inherit;
      padding: 0;
    }
    .top-bar-links a:hover, .top-bar-links button:hover {
      color: var(--fca-gold);
    }
    /* Sticky Header */
    .site-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background-color: rgba(255, 255, 255, 0.97);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-light);
      box-shadow: 0 4px 20px rgba(15, 23, 42, 0.05);
    }
    .header-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 82px;
      gap: 12px;
    }
    .brand-link {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }
    .brand-logo {
      width: 50px;
      height: 50px;
      object-fit: contain;
      flex-shrink: 0;
    }
    .brand-text {
      display: flex;
      flex-direction: column;
    }
    .brand-name {
      font-family: 'Montserrat', sans-serif;
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--fca-navy);
      letter-spacing: -0.02em;
      line-height: 1.1;
    }
    .brand-sub {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.66rem;
      font-weight: 700;
      color: var(--fca-red);
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-top: 3px;
    }
    .main-nav {
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .nav-link {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.71rem;
      font-weight: 700;
      color: var(--text-body);
      padding: 6px 8px;
      border-radius: var(--radius-sm);
      white-space: nowrap;
      min-height: 34px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      border: 1px solid transparent;
      background: transparent;
      cursor: pointer;
    }
    .nav-link:hover, .nav-link.active {
      color: var(--fca-red);
      background-color: var(--fca-red-soft);
    }
    .nav-link-locked {
      color: #475569;
      background-color: #F1F5F9;
      border: 1px dashed #94A3B8;
    }
    .nav-link-locked:hover {
      color: var(--fca-navy);
      background-color: #E2E8F0;
      border-color: var(--fca-navy);
    }
    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }
    .header-actions .btn-cta {
      display: none;
    }
    /* Buttons (2-Radius: 4px / 8px) */
    .btn-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.86rem;
      font-weight: 700;
      padding: 12px 20px;
      border-radius: var(--radius-sm);
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.2s ease;
      text-align: center;
      line-height: 1.25;
    }
    .btn-cta-primary {
      background-color: var(--fca-red);
      color: #FFFFFF;
      box-shadow: 0 4px 14px rgba(200, 30, 30, 0.24);
    }
    .btn-cta-primary:hover {
      background-color: var(--fca-red-dark);
      transform: translateY(-1px);
    }
    .btn-cta-gold {
      background-color: var(--fca-gold);
      color: var(--fca-navy);
      font-weight: 800;
      box-shadow: 0 4px 14px rgba(245, 158, 11, 0.28);
    }
    .btn-cta-gold:hover {
      background-color: #D97706;
      color: #FFFFFF;
      transform: translateY(-1px);
    }
    .btn-cta-navy {
      background-color: var(--fca-navy);
      color: #FFFFFF;
    }
    .btn-cta-navy:hover {
      background-color: #1E293B;
    }
    .btn-cta-outline {
      background-color: #FFFFFF;
      color: var(--fca-navy);
      border-color: var(--border-strong);
    }
    .btn-cta-outline:hover {
      border-color: var(--fca-red);
      color: var(--fca-red);
      background-color: var(--fca-red-soft);
    }
    .btn-cta-ghost-light {
      background-color: rgba(255, 255, 255, 0.1);
      color: #FFFFFF;
      border-color: rgba(255, 255, 255, 0.28);
    }
    .btn-cta-ghost-light:hover {
      background-color: rgba(255, 255, 255, 0.2);
    }
    .btn-sm {
      padding: 9px 14px;
      font-size: 0.8rem;
    }
    /* Mobile Menu Toggle & Drawer (S-04b safe) */
    .mobile-toggle {
      display: none;
      align-items: center;
      justify-content: center;
      width: 44px;
      height: 44px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-light);
      background: #FFFFFF;
      color: var(--fca-navy);
      cursor: pointer;
    }
    .mobile-drawer {
      display: none;
      position: fixed;
      top: 82px;
      left: 0;
      right: 0;
      background-color: var(--fca-navy);
      border-bottom: 2px solid var(--fca-gold);
      padding: 20px 24px 28px;
      z-index: 999;
      flex-direction: column;
      gap: 10px;
      box-shadow: var(--shadow-lg);
    }
    .mobile-drawer.open {
      display: flex;
    }
    .mobile-drawer a {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.95rem;
      font-weight: 700;
      color: #FFFFFF;
      padding: 12px 14px;
      border-radius: var(--radius-sm);
      background-color: rgba(255, 255, 255, 0.05);
    }
    .mobile-drawer a:hover {
      background-color: var(--fca-red);
    }
    .mobile-drawer button.mobile-nav-btn {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.92rem;
      font-weight: 700;
      color: #FDE68A;
      padding: 12px 14px;
      border-radius: var(--radius-sm);
      background-color: rgba(245, 158, 11, 0.12);
      border: 1px dashed rgba(245, 158, 11, 0.55);
      text-align: left;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      cursor: pointer;
      width: 100%;
    }
    /* Hero Section */
    .hero-section {
      background: linear-gradient(135deg, #0B1324 0%, #1C192E 52%, #6B1414 100%);
      color: #FFFFFF;
      padding: 68px 0 76px;
      position: relative;
      overflow: hidden;
      border-bottom: 4px solid var(--fca-gold);
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1.12fr 0.88fr;
      gap: 44px;
      align-items: center;
    }
    .hero-title {
      color: #FFFFFF;
      font-size: clamp(2.1rem, 3.8vw, 3.2rem);
      font-weight: 800;
      line-height: 1.12;
      margin-bottom: 18px;
    }
    .hero-title span {
      color: #FBBF24;
    }
    .hero-motto-box {
      background-color: rgba(245, 158, 11, 0.14);
      border-left: 4px solid var(--fca-gold);
      padding: 12px 16px;
      border-radius: var(--radius-sm);
      margin-bottom: 20px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.84rem;
      font-weight: 700;
      color: #FEF08A;
      letter-spacing: 0.02em;
    }
    .hero-sub {
      font-size: 1.03rem;
      color: #E2E8F0;
      margin-bottom: 28px;
      line-height: 1.65;
    }
    .hero-cta-row {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 36px;
    }
    .hero-kpi-strip {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      padding-top: 24px;
      border-top: 1px solid rgba(255, 255, 255, 0.14);
    }
    .hero-kpi-card {
      background-color: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-md);
      padding: 12px 14px;
    }
    .hero-kpi-num {
      font-family: 'Montserrat', sans-serif;
      font-size: 1.28rem;
      font-weight: 800;
      color: #FBBF24;
      line-height: 1.15;
    }
    .hero-kpi-lbl {
      font-size: 0.76rem;
      color: #CBD5E1;
      margin-top: 4px;
      line-height: 1.35;
    }
    .hero-visual-stack {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .hero-photo-card {
      background-color: #1E293B;
      border: 2px solid rgba(255, 255, 255, 0.18);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      position: relative;
    }
    .hero-photo-card img {
      width: 100%;
      height: 270px;
      object-fit: cover;
      object-position: center 20%;
    }
    .hero-photo-caption {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 12px 16px;
      background-color: rgba(15, 23, 42, 0.94);
      border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    .hero-photo-caption strong {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.84rem;
      color: #FFFFFF;
    }
    .hero-photo-caption span {
      font-size: 0.76rem;
      color: #FBBF24;
      font-weight: 600;
    }
    .hero-secondary-row {
      display: grid;
      grid-template-columns: 1.25fr 0.75fr;
      gap: 16px;
    }
    .hero-mini-card {
      background-color: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.16);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .hero-mini-card img {
      width: 100%;
      height: 132px;
      object-fit: cover;
    }
    .hero-mini-body {
      padding: 10px 14px;
      font-size: 0.78rem;
      color: #E2E8F0;
    }
    .hero-centenary-box {
      background-color: rgba(255, 255, 255, 0.97);
      color: var(--fca-navy);
      border-radius: var(--radius-md);
      padding: 14px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      gap: 6px;
    }
    .hero-centenary-box img {
      width: 96px;
      height: 96px;
      object-fit: contain;
    }
    .hero-centenary-box strong {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.78rem;
      color: var(--fca-navy);
    }
    /* Generic Cards & Grids */
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }
    .grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
    }
    .grid-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 28px;
    }
    .card {
      background-color: var(--bg-card);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-sm);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    }
    .card:hover {
      transform: translateY(-3px);
      box-shadow: var(--shadow-md);
      border-color: var(--border-strong);
    }
    .card-badge {
      position: absolute;
      top: 12px;
      left: 12px;
      background-color: var(--fca-navy);
      color: #FBBF24;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }
    .pillar-count {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--fca-red);
      background-color: var(--fca-red-soft);
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      align-self: flex-start;
      text-transform: uppercase;
    }
    /* Sponsors Showcase (All 23 Sponsors) */
    .sponsor-tier-block {
      margin-bottom: 36px;
    }
    .sponsor-tier-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 16px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--border-light);
      flex-wrap: wrap;
    }
    .sponsor-tier-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.82rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 5px 12px;
      border-radius: var(--radius-sm);
    }
    .tier-gold {
      background-color: var(--fca-gold-soft);
      color: #92400E;
      border: 1px solid #FDE047;
    }
    .tier-silver {
      background-color: #F1F5F9;
      color: #1E293B;
      border: 1px solid #CBD5E1;
    }
    .tier-bronze {
      background-color: var(--fca-red-soft);
      color: #991B1B;
      border: 1px solid #FECACA;
    }
    .sponsors-main-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
    }
    .sponsors-partner-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
    }
    .sponsor-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 18px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      text-align: center;
      gap: 12px;
      box-shadow: var(--shadow-sm);
      transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
    }
    .sponsor-card:hover {
      transform: translateY(-2px);
      border-color: var(--fca-red);
      box-shadow: var(--shadow-md);
    }
    .sponsor-card.gold-card {
      border: 2px solid #FDE047;
    }
    .sponsor-logo-wrap {
      width: 100%;
      height: 86px;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #FFFFFF;
      padding: 6px;
    }
    .sponsor-logo-wrap img {
      max-height: 100%;
      max-width: 100%;
      width: auto;
      height: auto;
      object-fit: contain;
    }
    .sponsor-name {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.92rem;
      font-weight: 800;
      color: var(--fca-navy);
      line-height: 1.25;
    }
    .sponsor-role-tag {
      font-size: 0.76rem;
      font-weight: 600;
      color: var(--text-muted);
      line-height: 1.35;
    }
    /* Architecture Cut Zone (#seiten-uebersicht) */
    .blueprint-zone-section {
      background-color: #E2E8F0;
      background-image:
        linear-gradient(to right, rgba(15, 23, 42, 0.06) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(15, 23, 42, 0.06) 1px, transparent 1px);
      background-size: 28px 28px;
      border-top: 3px dashed #0F172A;
      border-bottom: 3px dashed #0F172A;
      padding: 76px 0 88px;
    }
    .blueprint-cut-banner {
      background-color: #0B1528;
      color: #F8FAFC;
      border: 2px dashed #F59E0B;
      border-radius: var(--radius-md);
      padding: 28px 30px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-md);
    }
    .blueprint-cut-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      margin-bottom: 14px;
      padding-bottom: 14px;
      border-bottom: 1px dashed rgba(245, 158, 11, 0.4);
    }
    .blueprint-cut-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background-color: rgba(245, 158, 11, 0.2);
      border: 1px solid #F59E0B;
      color: #FBBF24;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.74rem;
      font-weight: 800;
      padding: 5px 11px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }
    .blueprint-kpi-row {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
      margin-top: 20px;
    }
    .blueprint-kpi-box {
      background-color: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: var(--radius-sm);
      padding: 14px 16px;
    }
    .blueprint-kpi-box.is-open-scope {
      border: 1px dashed #F59E0B;
      background-color: rgba(245, 158, 11, 0.08);
    }
    /* 4 Dashed Blueprint Module Cards */
    .blueprint-modules-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 28px;
    }
    .blueprint-module-card {
      background-color: rgba(248, 250, 252, 0.96);
      border: 2px dashed #475569;
      border-radius: var(--radius-md);
      padding: 26px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 20px;
      box-shadow: 0 6px 20px rgba(15, 23, 42, 0.07);
    }
    .blueprint-module-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 12px;
    }
    .blueprint-mod-tag {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      color: #0F172A;
      background-color: #E2E8F0;
      border: 1px solid #94A3B8;
      padding: 4px 9px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .blueprint-lock-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: #FEF3C7;
      border: 1px solid #D97706;
      color: #92400E;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.7rem;
      font-weight: 800;
      padding: 4px 9px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
    }
    .blueprint-module-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 1.22rem;
      font-weight: 800;
      color: #0F172A;
      margin-bottom: 10px;
      line-height: 1.25;
    }
    .blueprint-module-desc {
      font-size: 0.9rem;
      color: #334155;
      line-height: 1.55;
      margin-bottom: 14px;
    }
    .wireframe-preview-box {
      background-color: #E2E8F0;
      border: 1px dashed #64748B;
      border-radius: var(--radius-sm);
      padding: 14px;
    }
    .wireframe-skeleton-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 10px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.7rem;
      font-weight: 800;
      color: #334155;
      text-transform: uppercase;
    }
    .wireframe-grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }
    .wireframe-slot {
      background-color: #F8FAFC;
      border: 1px dashed #94A3B8;
      border-radius: var(--radius-sm);
      padding: 8px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .wireframe-img-placeholder {
      height: 36px;
      background: repeating-linear-gradient(
        -45deg,
        #E2E8F0,
        #E2E8F0 6px,
        #CBD5E1 6px,
        #CBD5E1 12px
      );
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #334155;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.65rem;
      font-weight: 800;
    }
    .wireframe-line-lg {
      height: 7px;
      width: 82%;
      background-color: #94A3B8;
      border-radius: var(--radius-sm);
    }
    .wireframe-line-sm {
      height: 6px;
      width: 56%;
      background-color: #CBD5E1;
      border-radius: var(--radius-sm);
    }
    .blueprint-checklist {
      display: flex;
      flex-direction: column;
      gap: 7px;
      margin-top: 12px;
      font-size: 0.83rem;
      color: #1E293B;
    }
    .blueprint-checklist-item {
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }
    .blueprint-checklist-item svg {
      color: #D97706;
      flex-shrink: 0;
      margin-top: 3px;
    }
    /* Wireframe Team Cards on herren-1.html */
    .matrix-team-btn.wireframe-locked {
      background-color: #F1F5F9;
      border: 2px dashed #64748B;
      opacity: 0.94;
    }
    .matrix-team-btn.wireframe-locked:hover {
      border-color: #0F172A;
      background-color: #E2E8F0;
    }
    .wireframe-mini-skeleton {
      display: flex;
      align-items: center;
      gap: 8px;
      width: 100%;
      padding: 6px 8px;
      background-color: #E2E8F0;
      border: 1px dashed #94A3B8;
      border-radius: var(--radius-sm);
    }
    .wireframe-mini-thumb {
      width: 28px;
      height: 22px;
      background: repeating-linear-gradient(
        -45deg,
        #CBD5E1,
        #CBD5E1 4px,
        #94A3B8 4px,
        #94A3B8 8px
      );
      border-radius: var(--radius-sm);
      flex-shrink: 0;
    }
    .wireframe-mini-bars {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .wireframe-mini-bar {
      height: 5px;
      background-color: #94A3B8;
      border-radius: var(--radius-sm);
    }
    .pill-wireframe-lock {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background-color: #FEF3C7;
      color: #92400E;
      border: 1px solid #F59E0B;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.62rem;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      flex-shrink: 0;
    }
    /* Footer */
    .site-footer {
      background-color: var(--fca-navy-deep);
      color: #E2E8F0;
      padding: 68px 0 36px;
      border-top: 4px solid var(--fca-gold);
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 1.3fr 1fr 1fr 1.1fr;
      gap: 36px;
      padding-bottom: 44px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    }
    .footer-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.92rem;
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
    .footer-list a, .footer-list button {
      color: #CBD5E1;
      font-size: 0.88rem;
      background: none;
      border: none;
      text-align: left;
      cursor: pointer;
      font-family: inherit;
      padding: 5px 0;
      min-height: 32px;
      display: inline-flex;
      align-items: center;
    }
    .footer-bottom a,
    .staff-card a,
    .team-sponsor-strip a {
      display: inline-flex;
      align-items: center;
      min-height: 32px;
      padding: 4px 0;
    }
    .footer-list a:hover, .footer-list button:hover {
      color: var(--fca-gold);
    }
    .footer-bottom {
      padding-top: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      font-size: 0.82rem;
      color: #CBD5E1;
    }
    /* Blueprint Modal (#wpBlueprintModal) */
    .wp-modal-backdrop {
      display: none;
      position: fixed;
      inset: 0;
      background-color: rgba(11, 19, 36, 0.78);
      backdrop-filter: blur(6px);
      z-index: 2000;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .wp-modal-backdrop.open {
      display: flex;
    }
    .wp-modal-dialog {
      background-color: #FFFFFF;
      border: 2px solid var(--fca-gold);
      border-radius: var(--radius-md);
      max-width: 620px;
      width: 100%;
      padding: 28px;
      box-shadow: var(--shadow-lg);
      position: relative;
      max-height: 90vh;
      overflow-y: auto;
    }
    .wp-modal-close {
      position: absolute;
      top: 16px;
      right: 16px;
      width: 36px;
      height: 36px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-light);
      background-color: var(--bg-muted);
      color: var(--fca-navy);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }
    .wp-modal-checklist {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin: 18px 0;
      padding: 16px;
      background-color: var(--bg-muted);
      border-radius: var(--radius-sm);
    }
    .wp-modal-check-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.88rem;
      color: var(--text-main);
    }
    .wp-modal-check-item svg {
      color: var(--fca-green);
      flex-shrink: 0;
      margin-top: 2px;
    }
    /* Responsive Breakpoints */
    @media (max-width: 1080px) {
      .hero-grid,
      .blueprint-modules-grid,
      .blueprint-kpi-row {
        grid-template-columns: 1fr;
      }
      .grid-4,
      .sponsors-main-grid,
      .sponsors-partner-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .grid-3 {
        grid-template-columns: repeat(2, 1fr);
      }
      .footer-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .main-nav, .header-actions .btn-cta {
        display: none;
      }
      .mobile-toggle {
        display: inline-flex;
      }
    }
    @media (max-width: 720px) {
      section {
        padding: 56px 0;
      }
      .top-bar-links {
        display: none;
      }
      .wp-v2-bar-inner {
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
      }
      .wp-v2-bar-middle,
      .wp-v2-switch-btn {
        width: 100%;
      }
      .hero-kpi-strip {
        grid-template-columns: repeat(2, 1fr);
      }
      .hero-secondary-row,
      .grid-2,
      .grid-3,
      .grid-4,
      .sponsors-main-grid,
      .sponsors-partner-grid,
      .wireframe-grid-3,
      .footer-grid {
        grid-template-columns: 1fr;
      }
      .blueprint-cut-banner,
      .blueprint-module-card {
        padding: 20px 18px;
      }
    }
"""

def render_shell(filename: str, page_title: str, active_nav: str, body_html: str, extra_css: str = "") -> str:
    nav_start = "active" if active_nav == "startseite" else ""
    nav_teams = "active" if active_nav == "teams" else ""
    nav_kontakt = "active" if active_nav == "kontakt" else ""
    return f"""<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self' https: data: blob:; script-src 'self' 'unsafe-inline' https:; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com data:; img-src 'self' https: data: blob:; connect-src 'self' https:;">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta http-equiv="Permissions-Policy" content="camera=(), microphone=(), geolocation=()">
  <title>{page_title}</title>
  <meta name="description" content="Fussballclub Attiswil (gegründet am 16. Februar 1971) — SFV Quality Club, 14 Mannschaften, 23 Sponsoren &amp; Sportanlage Lindenrain in 4536 Attiswil.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Montserrat:wght@600;700;800&amp;display=swap" rel="stylesheet">
  <style>
{SHARED_CSS}
{extra_css}
  </style>
</head>
<body>
  <!-- 1. KONZEPT- & VORSCHAU-LEISTE (VARIANTE 2) -->
  <div class="wp-v2-blueprint-bar">
    <div class="container wp-v2-bar-inner">
      <div class="wp-v2-bar-left">
        <span class="wp-v2-study-badge">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
          <span>UNVERBINDLICHER VORSCHAU-ENTWURF</span>
        </span>
        <span class="wp-v2-bar-status-text">Ausbaustufe Prototyp: 6 % (3 von 53 Seiten exemplarisch ausgearbeitet)</span>
      </div>
      <div class="wp-v2-bar-middle" aria-label="Vorschau-Umfang 3 Beispiel-Seiten">
        <div class="wp-v2-progress-track">
          <div class="wp-v2-progress-fill"></div>
        </div>
        <span class="wp-v2-progress-label">Vorschau-Umfang: 3 Beispiel-Seiten live · 50 weitere Seiten &amp; 13 Teams vorbereitet</span>
      </div>
      <a href="kontakt.html?thema=probetraining" class="wp-v2-switch-btn">
        <span>Smart-Anfrage &amp; 1-Seiten-PDF testen</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
    </div>
  </div>
  <!-- TOP BAR -->
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div class="top-bar-left">
        <span class="top-bar-badge" data-slot="topbar_badge">PROTOTYP-AUSBAU: 3 / 53 SEITEN</span>
        <span data-slot="topbar_info">Beispiel-Ausbau: 1. Mannschaft &amp; alle 23 Sponsoren live · 50 weitere Seiten folgen beim Ausbau</span>
      </div>
      <div class="top-bar-links">
        <a href="index.html#sponsoren">23 Sponsoren &amp; 300er Club</a>
        <a href="index.html#seiten-uebersicht">Weitere Seiten (50 vorbereitet)</a>
        <button type="button" onclick="wpOpenBlueprintModal('Bereich B: Verein, Vorstand (10), SFV Quality Club &amp; Chronik seit 1971 (14 Unterseiten)', 'Vereinsführung FC Attiswil (0 % übertragen)', 'Konrad Schütz (Präsident · 079 661 66 12) &amp; Philipp Singer (Vizepräsident · 079 304 44 56)')">Verein &amp; Chronik (0/14 offen)</button>
        <a href="kontakt.html?thema=clubhaus">Clubhaus Lindenrain mieten</a>
      </div>
    </div>
  </div>
  <!-- STICKY HEADER (HAUPTNAVIGATION MIT STATUS-PUNKTEN & SCHLOSS-SYMBOL) -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="FC Attiswil Startseite">
        <img src="images/logo-fcattiswil.webp" alt="Wappen FC Attiswil" class="brand-logo" width="50" height="50" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">FC ATTISWIL</span>
          <span class="brand-sub" data-slot="brand_sub">SEIT 1971 · SFV QUALITY CLUB</span>
        </div>
      </a>
      <nav class="main-nav" aria-label="Hauptnavigation mit Ausbau-Status">
        <a href="index.html" class="nav-link {nav_start}">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#10B981"/></svg>
          <span>Startseite (Beispiel)</span>
        </a>
        <a href="herren-1.html" class="nav-link {nav_teams}">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#F59E0B"/></svg>
          <span>1. Mannschaft (1/14)</span>
        </a>
        <a href="index.html#sponsoren" class="nav-link">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#10B981"/></svg>
          <span>23 Sponsoren</span>
        </a>
        <button type="button" class="nav-link nav-link-locked" onclick="wpOpenBlueprintModal('Bereich B &amp; C: Verein, Vorstand (10), Chronik seit 1971 &amp; Clubhaus Lindenrain (24 Seiten offen)', 'Vereinsführung &amp; Infrastruktur (Noch nicht migriert · 0 %)', 'Konrad Schütz (Präsident) &amp; Philipp Singer (Vizepräsident / Clubhaus)', 'clubhaus')">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" aria-hidden="true"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          <span>Verein &amp; Lindenrain (0/24)</span>
        </button>
        <a href="kontakt.html" class="nav-link {nav_kontakt}">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#10B981"/></svg>
          <span>Smart-Anfrage (Live-Demo)</span>
        </a>
      </nav>
      <div class="header-actions">
        <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-primary btn-sm" data-slot="header_cta">
          <span>Smart-Anfrage testen</span>
        </a>
        <button type="button" class="mobile-toggle" id="mobileMenuBtn" aria-label="Menü öffnen" onclick="wpToggleMobileMenu()">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    </div>
    <div class="mobile-drawer" id="mobileDrawer">
      <a href="index.html" onclick="wpCloseMobileMenu()">Startseite (Beispiel-Ansicht)</a>
      <a href="herren-1.html" onclick="wpCloseMobileMenu()">Beispiel-Team: 1. Mannschaft (1/14 ausgearbeitet · 13 weitere folgen)</a>
      <a href="index.html#sponsoren" onclick="wpCloseMobileMenu()">Sponsoren &amp; 300er Club (Alle 23 übernommen)</a>
      <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu(); wpOpenBlueprintModal('Bereich B &amp; C: Verein, Vorstand, Chronik &amp; Clubhaus Lindenrain (24 Seiten offen)', 'Vereinsführung &amp; Infrastruktur (Noch nicht migriert · 0 %)', 'Konrad Schütz &amp; Philipp Singer', 'clubhaus')">
        <span>Verein &amp; Lindenrain (24 weitere Seiten · folgt beim Ausbau)</span>
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      </button>
      <a href="kontakt.html" onclick="wpCloseMobileMenu()">Smart-Anfrage (Live-Demo)</a>
    </div>
  </header>
  <main>
{body_html}
  </main>
  <!-- FOOTER -->
  <footer class="site-footer" data-section="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
            <img src="images/logo-fcattiswil.webp" alt="FC Attiswil Wappen" width="46" height="46" loading="lazy" decoding="async" style="object-fit:contain;">
            <div>
              <div style="font-family:'Montserrat',sans-serif;font-weight:800;font-size:1.1rem;color:#FFFFFF;">FC ATTISWIL</div>
              <div style="font-size:0.76rem;color:#FBBF24;font-weight:700;">VORSCHAU-ENTWURF · 3 BEISPIEL-SEITEN LIVE</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#CBD5E1;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Unverbindlicher Vorschau-Entwurf für den FC Attiswil (gegründet am 16.02.1971, SFV Quality Club): 3 von 53 Seiten (Startseite, 1 Beispiel-Team 1. Mannschaft, Smart-Anfrage) als Qualitätsbeweis ausgearbeitet — 50 Unterseiten &amp; 13 Teams folgen im Hauptauftrag.
          </p>
          <div style="font-size:0.84rem;color:#E2E8F0;font-weight:600;">
            Sportanlage Lindenrain · Sportplatzweg 1 · 4536 Attiswil
          </div>
        </div>
        <div>
          <div class="footer-title">Prototyp (6 % ausgearbeitet)</div>
          <ul class="footer-list">
            <li><a href="index.html">Startseite: Hero &amp; Sponsoren (Beispiel)</a></li>
            <li><a href="herren-1.html">Beispiel-Team: 1. Mannschaft (1 von 14 fertig)</a></li>
            <li><a href="index.html#sponsoren">Alle 23 Sponsoren &amp; 300er Club</a></li>
            <li><a href="kontakt.html">Smart-Anfrage-Zentrale (Live-Demo)</a></li>
          </ul>
        </div>
        <div>
          <div class="footer-title">Weitere Bereiche (folgen beim Ausbau)</div>
          <ul class="footer-list">
            <li><a href="herren-1.html#alle-teams-matrix">13 weitere Mannschaften (Übersicht)</a></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Bereich B: Verein, Vorstand (10), Funktionäre (8), Schiedsrichter &amp; Chronik seit 1971 (14 Unterseiten)', 'Vereinsführung FC Attiswil (0 % übertragen)', 'Konrad Schütz (Präsident) &amp; Michelle Kurth (Sekretärin)')">Verein, Vorstand &amp; Chronik (0/14)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Bereich C: Sportanlage Lindenrain, Clubhaus-Vermietung &amp; Anlässe (10 Unterseiten)', 'Infrastruktur &amp; Vereinsleben (0 % übertragen)', 'Philipp Singer (079 304 44 56) &amp; Christina Lemp (079 916 64 55)', 'clubhaus')">Clubhaus Lindenrain &amp; Anlässe (0/10)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Bereich D: Spielbetrieb, Matchberichte, Vereinsartikel &amp; Foto-Archiv (7 Unterseiten)', 'Spielbetrieb &amp; Medien (0 % übertragen)', 'Florian Bohner (Sportchef) &amp; Raphaela Lüscher (Marketing)')">Spielbetrieb &amp; Galerien (0/7)</button></li>
          </ul>
        </div>
        <div>
          <div class="footer-title">Direktkontakt &amp; Rechtliches</div>
          <ul class="footer-list">
            <li><a href="kontakt.html?thema=probetraining" style="color:#FBBF24;font-weight:700;">Probetraining &amp; Vereins-Anfrage</a></li>
            <li><a href="index.html#seiten-uebersicht">Übersicht der weiteren Seiten ansehen</a></li>
            <li><a href="https://www.instagram.com/fc_attiswil/" target="_blank" rel="noopener noreferrer">Instagram (@fc_attiswil)</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div>&copy; 2026 Fussballclub Attiswil (4536 Attiswil · SOFV Nr. 1880) · Unverbindlicher Vorschau-Entwurf (3 Beispiel-Seiten live).</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;">
          <a href="herren-1.html" style="color:#FBBF24;font-weight:700;">Beispiel-Team 1. Mannschaft (1/14)</a>
          <a href="kontakt.html" style="color:#E2E8F0;">Smart-Anfrage testen</a>
        </div>
      </div>
    </div>
  </footer>
  <!-- SEITEN-VORSCHAU-MODAL -->
  <div class="wp-modal-backdrop" id="wpBlueprintModal" role="dialog" aria-modal="true" aria-labelledby="wpBpTitle">
    <div class="wp-modal-dialog">
      <button type="button" class="wp-modal-close" aria-label="Dialog schliessen" onclick="wpCloseBlueprintModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="section-kicker">SEITEN-VORSCHAU · VORBEREITET FÜR DEN KOMPLETTEN AUSBAU</div>
      <h3 id="wpBpTitle" style="font-size:1.35rem;font-weight:800;margin-bottom:8px;">Weitere Vereins-Seite: Folgt beim Ausbau</h3>
      <p id="wpBpSub" style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
        In diesem <strong>Vorschau-Entwurf (3 von 53 Seiten als Beispiel live)</strong> sind oben das Design, alle 23 Sponsoren und exakt <strong>1 Beispiel-Team (1. Mannschaft · Herren 4. Liga)</strong> ausgearbeitet. Dieses Modul befindet sich bewusst noch im <strong>vorbereiteten Platzhalter (folgt beim Ausbau)</strong> und wird nach Auftragserteilung komplett mit allen Originaldaten, Fotos und Kadern eingerichtet.
      </p>
      <div style="background-color:#FEF3C7;border-left:4px solid #D97706;padding:12px 14px;border-radius:var(--radius-sm);font-size:0.86rem;margin-bottom:14px;">
        <div style="font-weight:800;color:#92400E;" id="wpBpCategory">Bereich / Abteilung: Vorbereitet für den Ausbau</div>
        <div style="color:#78350F;margin-top:2px;" id="wpBpContact">Zuständige Ansprechperson im Verein: Vorstand FC Attiswil</div>
      </div>
      <div class="wp-modal-checklist">
        <div style="font-family:'Montserrat',sans-serif;font-size:0.78rem;font-weight:800;text-transform:uppercase;color:var(--fca-navy);">
          Wird nach Auftragserteilung (analog Beispiel-Team 1. Mannschaft) schlüsselfertig übertragen:
        </div>
        <div class="wp-modal-check-item">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Vollständige Übernahme aller bestehenden Texte, Mannschaftsfotos, Porträts &amp; Statuten-PDFs</span>
        </div>
        <div class="wp-modal-check-item">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Einrichtung aller 13 weiteren Mannschafts-Seiten (Frauen 2./3. Liga, Senioren, Junioren B–G &amp; Juniorinnen FF-17/14/11)</span>
        </div>
        <div class="wp-modal-check-item">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Direkte Anbindung an das WebPilot Studio-Cockpit für sekundenschnelle Änderungen per KI oder 1-Klick</span>
        </div>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:18px;">
        <a href="herren-1.html" class="btn-cta btn-cta-primary btn-sm" onclick="wpCloseBlueprintModal()">
          <span>Ausgearbeitetes Beispiel-Team (1. Mannschaft · 1/14) ansehen</span>
        </a>
        <a href="kontakt.html?thema=probetraining" id="wpBpCtaLink" class="btn-cta btn-cta-gold btn-sm">
          <span>Smart-Anfrage (Live-Demo) testen</span>
        </a>
      </div>
    </div>
  </div>
  <!-- IMPRESSUM MODAL -->
  <div class="wp-modal-backdrop" id="wpImpressumModal" role="dialog" aria-modal="true" aria-labelledby="wpImpTitle">
    <div class="wp-modal-dialog">
      <button type="button" class="wp-modal-close" aria-label="Impressum schliessen" onclick="wpCloseImpressumModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="section-kicker">RECHTLICHE ANGABEN · SCHWEIZER DSG</div>
      <h3 id="wpImpTitle" style="font-size:1.3rem;font-weight:800;margin-bottom:10px;">Impressum &amp; Datenschutz — FC Attiswil</h3>
      <div style="font-size:0.88rem;color:var(--text-body);display:flex;flex-direction:column;gap:10px;">
        <p><strong>Vereinsadresse:</strong><br>Fussballclub Attiswil · Sportanlage Lindenrain · Sportplatzweg 1 · 4536 Attiswil (SOFV-Verein Nr. 1880)</p>
        <p><strong>Vertretungsberechtigter Vorstand:</strong><br>Konrad Schütz (Präsident, Tel. 079 661 66 12) · Philipp Singer (Vizepräsident / Anlässe &amp; Clubhaus, Tel. 079 304 44 56) · Michelle Kurth (Sekretärin &amp; Datenschutz) · Jörg Scheidegger (Kassier, Tel. 032 637 21 76)</p>
        <p><strong>Offizielle E-Mail-Kontakte:</strong><br>info@fcattiswil.ch · sponsoring@fcattiswil.ch · 300erClub@fcattiswil.ch · fairplay@fcattiswil.ch</p>
        <p><strong>Datenschutz (Schweizer Datenschutzgesetz revDSG):</strong><br>Personendaten aus Kontakt-, Probetraining-, Clubhaus- und Sponsoring-Anfragen werden ausschliesslich zur Vereinsadministration innerhalb des FC Attiswil verwendet und niemals an unbefugte Dritte weitergegeben.</p>
      </div>
      <div style="margin-top:18px;text-align:right;">
        <button type="button" class="btn-cta btn-cta-navy btn-sm" onclick="wpCloseImpressumModal()">Schliessen</button>
      </div>
    </div>
  </div>
  <script>
    function wpToggleMobileMenu() {{
      var d = document.getElementById('mobileDrawer');
      if (d) d.classList.toggle('open');
    }}
    function wpCloseMobileMenu() {{
      var d = document.getElementById('mobileDrawer');
      if (d) d.classList.remove('open');
    }}
    function wpOpenBlueprintModal(title, category, contact, topicSlug) {{
      var m = document.getElementById('wpBlueprintModal');
      if (!m) return;
      var tEl = document.getElementById('wpBpTitle');
      var cEl = document.getElementById('wpBpCategory');
      var pEl = document.getElementById('wpBpContact');
      var lEl = document.getElementById('wpBpCtaLink');
      if (tEl) tEl.textContent = title || 'Weitere Vereins-Seite: Folgt beim Ausbau';
      if (cEl) cEl.textContent = 'Bereich / Abteilung: ' + (category || 'Vereins-Bereich');
      if (pEl) pEl.textContent = 'Zuständig im FC Attiswil: ' + (contact || 'Vorstand FC Attiswil (info@fcattiswil.ch)');
      if (lEl) lEl.href = 'kontakt.html?thema=' + encodeURIComponent(topicSlug || 'probetraining');
      m.classList.add('open');
    }}
    function wpCloseBlueprintModal() {{
      var m = document.getElementById('wpBlueprintModal');
      if (m) m.classList.remove('open');
    }}
    function wpOpenImpressumModal() {{
      var m = document.getElementById('wpImpressumModal');
      if (m) m.classList.add('open');
    }}
    function wpCloseImpressumModal() {{
      var m = document.getElementById('wpImpressumModal');
      if (m) m.classList.remove('open');
    }}
    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') {{
        wpCloseBlueprintModal();
        wpCloseImpressumModal();
        wpCloseMobileMenu();
      }}
    }});
  </script>
</body>
</html>
"""
# ---------------------------------------------------------------------------
# 3. PAGE 1: INDEX.HTML (STARTSEITE — HERO + 23 SPONSOREN + BAUPLAN-SCHNITT)
# ---------------------------------------------------------------------------
def build_index_html() -> str:
    main_cards = []
    for idx, sp in enumerate(SPONSORS_MAIN, start=1):
        gold_cls = " gold-card" if idx <= 4 else ""
        main_cards.append(f"""
          <a href="{sp['url']}" target="_blank" rel="noopener noreferrer" class="sponsor-card{gold_cls}">
            <div class="sponsor-logo-wrap">
              <img src="{sp['logo']}" alt="Logo {sp['name']}" width="220" height="80" loading="lazy" decoding="async">
            </div>
            <div>
              <div class="sponsor-name">{sp['name']}</div>
              <div class="sponsor-role-tag">{sp['role']}</div>
            </div>
          </a>""")
    partner_cards = []
    for sp in SPONSORS_PARTNER:
        partner_cards.append(f"""
          <a href="{sp['url']}" target="_blank" rel="noopener noreferrer" class="sponsor-card">
            <div class="sponsor-logo-wrap">
              <img src="{sp['logo']}" alt="Logo {sp['name']}" width="200" height="76" loading="lazy" decoding="async">
            </div>
            <div>
              <div class="sponsor-name">{sp['name']}</div>
              <div class="sponsor-role-tag">{sp['role']}</div>
            </div>
          </a>""")
    body = f"""
  <!-- 1. HERO SECTION (BEISPIEL-AUSBAU) -->
  <section class="hero-section" data-section="hero">
    <div class="container">
      <div class="hero-grid">
        <div>
          <div class="section-kicker kicker-light" data-slot="hero_kicker">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span>GEGRÜNDET AM 16. FEBRUAR 1971 · SFV QUALITY CLUB · SOFV-VEREIN NR. 1880</span>
          </div>
          <h1 class="hero-title" data-slot="hero_title">
            Fussballclub Attiswil — <span>Herzblut auf dem Lindenrain.</span>
          </h1>
          <div class="hero-motto-box" data-slot="hero_motto">
            «Seit dem 16. Februar 1971 die sportliche Heimat im Oberaargau: 14 Mannschaften, zertifizierter SFV Quality Club (20. Juni 2026), eigenes Clubhaus &amp; gelebte Kameradschaft in 4536 Attiswil.»
          </div>
          <p class="hero-sub" data-slot="hero_sub">
            Von unserer <strong>1. Mannschaft (Herren 4. Liga)</strong> und den zwei erfolgreichen Frauenteams (Cupsiegerinnen 2025) über die <strong>Senioren 30+</strong> bis zu <strong>10 Nachwuchs-Teams</strong> (Junioren B–G &amp; Juniorinnen FF-17/FF-14/FF-11): Der FC Attiswil verbindet Breitensport, gezielte Jugendförderung und aktives Dorfleben auf der Sportanlage Lindenrain.
          </p>
          <div class="hero-cta-row">
            <a href="herren-1.html" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
              <span>1. Mannschaft (1/14)</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </a>
            <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-primary" data-slot="hero_cta_secondary">
              <span>Probetraining &amp; Vereins-Zentrale</span>
            </a>
            <a href="#sponsoren" class="btn-cta btn-cta-ghost-light">
              <span>Alle 23 Sponsoren &amp; 300er Club</span>
            </a>
          </div>
          <div class="hero-kpi-strip">
            <div class="hero-kpi-card">
              <div class="hero-kpi-num" data-slot="kpi_1_num">16.02.1971</div>
              <div class="hero-kpi-lbl" data-slot="kpi_1_lbl">Gründung im Rest. Löwen Attiswil</div>
            </div>
            <div class="hero-kpi-card">
              <div class="hero-kpi-num" data-slot="kpi_2_num">14 Teams</div>
              <div class="hero-kpi-lbl" data-slot="kpi_2_lbl">1 Beispiel-Team live · 13 vorbereitet</div>
            </div>
            <div class="hero-kpi-card">
              <div class="hero-kpi-num" data-slot="kpi_3_num">SFV Quality</div>
              <div class="hero-kpi-lbl" data-slot="kpi_3_lbl">Zertifizierter Quality Club (20.06.2026)</div>
            </div>
            <div class="hero-kpi-card">
              <div class="hero-kpi-num" data-slot="kpi_4_num">23 Sponsoren</div>
              <div class="hero-kpi-lbl" data-slot="kpi_4_lbl">Alle Logos &amp; 300er Club übernommen</div>
            </div>
          </div>
        </div>
        <div class="hero-visual-stack">
          <div class="hero-photo-card">
            <img src="images/hero-herren-1.webp" alt="FC Attiswil 1. Mannschaft Herren 4. Liga auf dem Sportplatz Lindenrain" width="600" height="270" fetchpriority="high" decoding="async" data-slot="hero_main_img">
            <div class="hero-photo-caption">
              <strong>1. Mannschaft FC Attiswil · Herren 4. Liga</strong>
              <span>Beispiel-Team 1/14 · Dress: Auto Lemp AG</span>
            </div>
          </div>
          <div class="hero-secondary-row">
            <div class="hero-mini-card">
              <img src="images/clubhaus-lindenrain.webp" alt="Clubhaus und Sportanlage Lindenrain 4536 Attiswil" width="380" height="132" loading="lazy" decoding="async" data-slot="hero_sub_img">
              <div class="hero-mini-body">
                <strong style="color:#FFFFFF;display:block;">Sportanlage &amp; Clubhaus Lindenrain</strong>
                <span>Sportplatzweg 1, 4536 Attiswil · 48 Innen- &amp; 40 gedeckte Sitzplätze</span>
              </div>
            </div>
            <div class="hero-centenary-box">
              <img src="images/sfv-quality-club.webp" alt="SFV Quality Club Auszeichnung FC Attiswil" width="96" height="96" loading="lazy" decoding="async" data-slot="hero_centenary_img">
              <strong>SFV Quality Club</strong>
              <span style="font-size:0.72rem;color:var(--text-body);line-height:1.25;">Offizielles Label seit 20. Juni 2026</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- 2. ALLE 23 ORIGINAL-SPONSOREN, 300ER CLUB, MATCHBALL & AVIA TANKKARTE -->
  <section id="sponsoren" data-section="sponsoren" style="background-color:#FFFFFF;border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker kicker-gold" data-slot="sponsors_kicker">HERZLICHEN DANK AN UNSERE PARTNER · 100 % ORIGINAL-ÜBERNAHME</div>
        <h2 class="section-title" data-slot="sponsors_title">Unsere 23 Sponsoren, der 300er Club &amp; Gönner.</h2>
        <p class="section-desc" data-slot="sponsors_desc">
          Ohne das treue Gewerbe aus Attiswil, dem Oberaargau und der Region Solothurn wäre ein aktiver Spielbetrieb für 14 Mannschaften auf dem Lindenrain nicht möglich. Alle 23 bestehenden Sponsoren-Logos von <strong>fcattiswil.ch</strong> sind bereits lückenlos übernommen.
        </p>
      </div>
      <!-- Tier 1: 11 Dress-, Trikot- & Team-Hauptsponsoren -->
      <div class="sponsor-tier-block">
        <div class="sponsor-tier-header">
          <span class="sponsor-tier-badge tier-gold">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            <span>Trikot-, Dress- &amp; Ausrüstungs-Sponsoren (11 Team-Partner)</span>
          </span>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Ressort Sponsoring: Raphaela Lüscher (079 453 88 60 · sponsoring@fcattiswil.ch)</span>
        </div>
        <div class="sponsors-main-grid">{''.join(main_cards)}
        </div>
      </div>
      <!-- Tier 2: 12 Offizielle Vereins-, Infrastruktur- & Gewerbepartner -->
      <div class="sponsor-tier-block">
        <div class="sponsor-tier-header">
          <span class="sponsor-tier-badge tier-silver">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>
            <span>Offizielle Vereins-, Infrastruktur- &amp; Gewerbepartner (12 Partner)</span>
          </span>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Direkt verlinkt mit den offiziellen Partner-Websites</span>
        </div>
        <div class="sponsors-partner-grid">{''.join(partner_cards)}
        </div>
      </div>
      <!-- Gönner- & Unterstützer-Formate (300er Club, Matchballspende, AVIA Tankkarte) -->
      <div class="grid-3" style="margin-top:28px;">
        <div style="background-color:var(--fca-navy);color:#FFFFFF;border-radius:var(--radius-md);padding:24px;border-top:4px solid var(--fca-gold);display:flex;flex-direction:column;justify-content:space-between;gap:14px;">
          <div>
            <span class="top-bar-badge" style="background-color:var(--fca-gold);color:var(--fca-navy);margin-bottom:10px;">GÖNNERVEREINIGUNG</span>
            <h3 style="color:#FFFFFF;font-size:1.18rem;font-weight:800;margin-bottom:8px;">300er Club FC Attiswil</h3>
            <p style="font-size:0.88rem;color:#E2E8F0;line-height:1.55;">
              Mit einem Jahresbeitrag von <strong>CHF 300.00</strong> unterstützt der 300er Club gezielt die Juniorenabteilung, Trainingslager und Spezialanschaffungen auf der Sportanlage Lindenrain.
            </p>
          </div>
          <a href="kontakt.html?thema=sponsoring" class="btn-cta btn-cta-gold btn-sm" style="width:100%;">
            <span>300er-Club-Mitglied werden (300erClub@fcattiswil.ch)</span>
          </a>
        </div>
        <div style="background-color:var(--bg-page);border:1px solid var(--border-strong);border-top:4px solid var(--fca-red);border-radius:var(--radius-md);padding:24px;display:flex;flex-direction:column;justify-content:space-between;gap:14px;">
          <div>
            <span class="pillar-count" style="margin-bottom:10px;">HEIMSPIEL-PATRONAT · CHF 150.00</span>
            <h3 style="font-size:1.18rem;font-weight:800;margin-bottom:8px;">Matchballspende auf dem Lindenrain</h3>
            <p style="font-size:0.88rem;color:var(--text-body);line-height:1.55;">
              Spende einen offiziellen Matchball (<strong>CHF 150.00</strong>) für ein Heimspiel der 1. Mannschaft oder unserer Frauenteams — inklusive namentlicher Verdankung im Clubhaus und auf der Website.
            </p>
          </div>
          <a href="kontakt.html?thema=sponsoring" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Matchballspende online anmelden</span>
          </a>
        </div>
        <div style="background-color:var(--bg-page);border:1px solid var(--border-strong);border-top:4px solid var(--fca-green);border-radius:var(--radius-md);padding:24px;display:flex;flex-direction:column;justify-content:space-between;gap:14px;">
          <div>
            <span class="pillar-count" style="background-color:var(--fca-green-soft);color:#166534;margin-bottom:10px;">2 RAPPEN PRO LITER FÜRS TEAM</span>
            <h3 style="font-size:1.18rem;font-weight:800;margin-bottom:8px;">AVIA Tankkarte &amp; Bandenwerbung</h3>
            <p style="font-size:0.88rem;color:var(--text-body);line-height:1.55;">
              Tanken und gleichzeitig den Nachwuchs fördern: Mit der kostenlosen <strong>AVIA Vereins-Tankkarte</strong> fliessen pro getanktem Liter automatisch 2 Rappen in die Vereinskasse des FC Attiswil.
            </p>
          </div>
          <a href="kontakt.html?thema=sponsoring" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Sponsoring-Dossier &amp; Banden anfragen</span>
          </a>
        </div>
      </div>
    </div>
  </section>
  <!-- 3. SEITEN-ÜBERSICHT (4 WEITERE BEREICHE) -->
  <section id="seiten-uebersicht" class="blueprint-zone-section" data-section="seiten-uebersicht">
    <div class="container">
      <!-- Trenn-Banner: Übersicht der weiteren Seiten -->
      <div class="blueprint-cut-banner">
        <div class="blueprint-cut-top">
          <span class="blueprint-cut-pill">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            <span>SEITEN-ÜBERSICHT · FOLGT BEIM KOMPLETTEN AUSBAU</span>
          </span>
          <span style="font-family:'Montserrat',sans-serif;font-size:0.78rem;font-weight:700;color:#FDE68A;">
            50 von 53 Unterseiten (94 %) &amp; 13 von 14 Teams sind ab hier als Vorschau-Übersicht vorbereitet
          </span>
        </div>
        <h2 style="color:#FFFFFF;font-size:clamp(1.45rem,2.5vw,2.05rem);font-weight:800;margin-bottom:10px;">
          Transparenter Vorschau-Entwurf: Welche Beispiel-Seiten bereits stehen — und was beim Ausbau folgt.
        </h2>
        <p style="font-size:0.95rem;color:#CBD5E1;line-height:1.65;">
          Die aktuelle Website <strong>fcattiswil.ch</strong> umfasst <strong>53 Menü-Unterseiten</strong> und <strong>14 Mannschaften</strong>. Damit der Vorstand um Präsident <strong>Konrad Schütz</strong>, Vizepräsident <strong>Philipp Singer</strong>, Sportchef <strong>Florian Bohner</strong> und Marketingchefin <strong>Raphaela Lüscher</strong> das neue System vor einem Entscheid echt prüfen kann, haben wir oben <strong>3 Beispiel-Seiten</strong> komplett ausgearbeitet — inklusive aller 23 Sponsoren und der <strong>1. Mannschaft (Herren 4. Liga)</strong>. Die folgenden <strong>4 Vereins-Module (50 Seiten / 94 %)</strong> sind hier als <strong>übersichtliche Vorschau-Bereiche</strong> vorbereitet:
        </p>
        <div class="blueprint-kpi-row">
          <div class="blueprint-kpi-box">
            <div style="font-family:'Montserrat',sans-serif;font-size:0.76rem;font-weight:800;color:#4ADE80;text-transform:uppercase;margin-bottom:4px;">
              Bereits als Beispiel ausgearbeitet (3 von 53 Seiten)
            </div>
            <div style="font-size:0.86rem;color:#F8FAFC;">
              1. Startseite (Hero + 23 Sponsoren &amp; 300er Club) · 2. Beispiel-Team <strong>1. Mannschaft</strong> (4 Staff-Porträts &amp; 22 Kaderspieler) · 3. Smart-Anfrage-Zentrale (inkl. Live-1-Seiten-PDF mit FC-Attiswil-Briefkopf).
            </div>
          </div>
          <div class="blueprint-kpi-box is-open-scope">
            <div style="font-family:'Montserrat',sans-serif;font-size:0.76rem;font-weight:800;color:#FBBF24;text-transform:uppercase;margin-bottom:4px;">
              Folgt beim kompletten Ausbau (50 weitere Seiten vorbereitet)
            </div>
            <div style="font-size:0.86rem;color:#F8FAFC;">
              Alle weiteren <strong>13 Mannschaften</strong> (Frauen 2./3. Liga, Senioren 30+, 7 Junioren- &amp; 3 Juniorinnen-Teams + Team Bravo), Vorstand (10), Funktionäre (8), Schiedsrichter (3), Clubhaus-Vermietung, Anlässe &amp; 55 Jahre Vereinschronik.
            </div>
          </div>
        </div>
      </div>
      <!-- 4 WEITERE BEREICHE (BEREICH A bis D) -->
      <div class="blueprint-modules-grid">
        <!-- BEREICH A: 13 WEITERE MANNSCHAFTEN -->
        <article class="blueprint-module-card">
          <div>
            <div class="blueprint-module-top">
              <span class="blueprint-mod-tag">Bereich A · 19 Unterseiten offen</span>
              <span class="blueprint-lock-badge">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span>1/14 ausgearbeitet · 13 weitere vorbereitet</span>
              </span>
            </div>
            <h3 class="blueprint-module-title">13 weitere Mannschaften &amp; «Team Bravo» (Noch nicht migriert)</h3>
            <p class="blueprint-module-desc">
              Während die <strong>1. Mannschaft (Herren 4. Liga)</strong> als Beispiel-Team komplett ausgearbeitet ist, werden die <strong>13 weiteren Teams</strong> im Hauptauftrag exakt nach demselben Standard mit Mannschaftsfoto, Trainer-Kontakt, Trainingszeiten und Kaderliste übernommen:
            </p>
            <div class="wireframe-preview-box" aria-hidden="true">
              <div class="wireframe-skeleton-header">
                <span>Vorschau-Übersicht: 13 offene Team-Seiten</span>
                <span>0 % befüllt</span>
              </div>
              <div class="wireframe-grid-3">
                <div class="wireframe-slot">
                  <div class="wireframe-img-placeholder">FRAUEN 2./3. LIGA</div>
                  <div class="wireframe-line-lg"></div>
                  <div class="wireframe-line-sm"></div>
                </div>
                <div class="wireframe-slot">
                  <div class="wireframe-img-placeholder">JUNIOREN B–G (7)</div>
                  <div class="wireframe-line-lg"></div>
                  <div class="wireframe-line-sm"></div>
                </div>
                <div class="wireframe-slot">
                  <div class="wireframe-img-placeholder">FF-17 / FF-14 / FF-11</div>
                  <div class="wireframe-line-lg"></div>
                  <div class="wireframe-line-sm"></div>
                </div>
              </div>
            </div>
            <div class="blueprint-checklist">
              <div class="blueprint-checklist-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span><strong>Aktive Frauen &amp; Senioren (3 Teams):</strong> Frauen 2. Liga (Cupsiegerinnen 2025, Dana Scherrer &amp; Roger Lemp), Frauen 3. Liga (Tom Moser) &amp; Senioren 30+ (Markus Frenzen)</span>
              </div>
              <div class="blueprint-checklist-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span><strong>7 Junioren-Teams (Leitung Levi Meyer):</strong> Junioren B &amp; C (Gruppierung), D/9 (Lasttrans AG), D/7 (Max Meyer AG), E &amp; F (Makos Bau GmbH), G Piccolos (Q-21)</span>
              </div>
              <div class="blueprint-checklist-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span><strong>3 Juniorinnen-Teams (Leitung Celine Lemp) &amp; Plausch:</strong> FF-17 (W+H AG), FF-14 (AXA Bruno Christen), FF-11 (Neutronix GmbH) &amp; Team Bravo</span>
              </div>
            </div>
          </div>
          <div style="display:flex;flex-wrap:wrap;gap:10px;">
            <a href="herren-1.html" class="btn-cta btn-cta-primary btn-sm" style="flex:1;">
              <span>Ausgearbeitetes Beispiel-Team (1/14) ansehen</span>
            </a>
            <a href="herren-1.html#alle-teams-matrix" class="btn-cta btn-cta-outline btn-sm" style="flex:1;">
              <span>13 weitere Teams ansehen</span>
            </a>
          </div>
        </article>
        <!-- BEREICH B: VEREIN, VORSTAND (10), FUNKTIONÄRE (8), SR (3) & CHRONIK SEIT 1971 -->
        <article class="blueprint-module-card">
          <div>
            <div class="blueprint-module-top">
              <span class="blueprint-mod-tag">Bereich B · 14 Unterseiten offen</span>
              <span class="blueprint-lock-badge">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span>Status: Vorbereitet · Folgt beim Ausbau</span>
              </span>
            </div>
            <h3 class="blueprint-module-title">Verein, Vorstand (10), Funktionäre, Schiedsrichter &amp; Chronik 1971–2026</h3>
            <p class="blueprint-module-desc">
              Sämtliche Vereins- und Organisationsseiten von <strong>fcattiswil.ch</strong> sind im Datenmodell bereits erfasst und werden im Hauptauftrag als eigenständige Seiten ausgearbeitet:
            </p>
            <div class="wireframe-preview-box" aria-hidden="true">
              <div class="wireframe-skeleton-header">
                <span>Vorschau-Übersicht: Vereinsführung &amp; Geschichte</span>
                <span>0 / 14 Seiten gebaut</span>
              </div>
              <div class="wireframe-grid-3">
                <div class="wireframe-slot">
                  <div class="wireframe-img-placeholder">VORSTAND (10)</div>
                  <div class="wireframe-line-lg"></div>
                  <div class="wireframe-line-sm"></div>
                </div>
                <div class="wireframe-slot">
                  <div class="wireframe-img-placeholder">FUNKTIONÄRE &amp; SR</div>
                  <div class="wireframe-line-lg"></div>
                  <div class="wireframe-line-sm"></div>
                </div>
                <div class="wireframe-slot">
                  <div class="wireframe-img-placeholder">CHRONIK SEIT 1971</div>
                  <div class="wireframe-line-lg"></div>
                  <div class="wireframe-line-sm"></div>
                </div>
              </div>
            </div>
            <div class="blueprint-checklist">
              <div class="blueprint-checklist-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span><strong>Vorstand (10 Porträts):</strong> Konrad Schütz (Präsident), Philipp Singer (Vizepräsident), Michelle Kurth, Florian Bohner, Celine Lemp, Levi Meyer, Jörg Scheidegger, Sarah Probst, Remo Brudermann &amp; Raphaela Lüscher</span>
              </div>
              <div class="blueprint-checklist-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span><strong>Funktionäre (8) &amp; Schiedsrichter (3):</strong> Platzwarte Christoph Rüegger &amp; Alfred Bohner, Markus Schaad, Clubhauswirtin Christina Lemp, Josephina Hohl sowie SR Slavko Martinovic, Dieter Schoch &amp; Luana Sortino</span>
              </div>
              <div class="blueprint-checklist-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span><strong>Chronik seit 16.02.1971 &amp; Statuten:</strong> Gründung im Rest. Löwen (Max Meyer, Martin Zumstein, Walter Zürcher), Ehrenmitglieder, SFV Quality Club Label (20.06.2026) &amp; Statuten (HV 04.07.2026)</span>
              </div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Bereich B: Verein, Vorstand (10), Funktionäre (8), Schiedsrichter &amp; Chronik (14 Seiten)', 'Vereinsführung FC Attiswil (Status: Vorbereitet · Folgt beim Ausbau)', 'Konrad Schütz (Präsident · 079 661 66 12) &amp; Michelle Kurth (Sekretärin)', 'allgemein')">
            <span>Seiten-Übersicht für Bereich B öffnen</span>
          </button>
        </article>
        <!-- BEREICH C: SPORTANLAGE LINDENRAIN, CLUBHAUS-VERMIETUNG & VEREINSANLÄSSE -->
        <article class="blueprint-module-card">
          <div>
            <div class="blueprint-module-top">
              <span class="blueprint-mod-tag">Bereich C · 10 Unterseiten offen</span>
              <span class="blueprint-lock-badge">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span>Status: Vorbereitet · Folgt beim Ausbau</span>
              </span>
            </div>
            <h3 class="blueprint-module-title">Sportanlage Lindenrain, Clubhaus-Vermietung &amp; Jahresprogramm</h3>
            <p class="blueprint-module-desc">
              Das 1993 durch die Max Meyer AG erbaute und 2014/15 erweiterte <strong>Clubhaus Lindenrain</strong> sowie sämtliche traditionellen Attiswiler Vereinsanlässe erhalten eigene Informations- und Reservationsseiten:
            </p>
            <div class="wireframe-preview-box" aria-hidden="true">
              <div class="wireframe-skeleton-header">
                <span>Vorschau-Übersicht: Infrastruktur &amp; Anlässe</span>
                <span>0 / 10 Seiten gebaut</span>
              </div>
              <div class="wireframe-grid-3">
                <div class="wireframe-slot">
                  <div class="wireframe-img-placeholder">CLUBHAUS (48+40 PL.)</div>
                  <div class="wireframe-line-lg"></div>
                  <div class="wireframe-line-sm"></div>
                </div>
                <div class="wireframe-slot">
                  <div class="wireframe-img-placeholder">LOTTOMATCH &amp; CHILBI</div>
                  <div class="wireframe-line-lg"></div>
                  <div class="wireframe-line-sm"></div>
                </div>
                <div class="wireframe-slot">
                  <div class="wireframe-img-placeholder">ANFAHRT LINDENRAIN</div>
                  <div class="wireframe-line-lg"></div>
                  <div class="wireframe-line-sm"></div>
                </div>
              </div>
            </div>
            <div class="blueprint-checklist">
              <div class="blueprint-checklist-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span><strong>Clubhaus Lindenrain mieten:</strong> 48 Innensitzplätze + 40 gedeckte Aussensitzplätze am Sportplatzweg 1 (Vermietung: Philipp Singer · 079 304 44 56 · Wirtin: Christina Lemp · 079 916 64 55)</span>
              </div>
              <div class="blueprint-checklist-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span><strong>Vereinsanlässe 2026/27:</strong> Clubversammlung (02.11.), Lottomatch MZH Attiswil (21./22.11.), Kindermaskenball (13.02.), Sponsorenlauf, 56. HV (03.07.), Attiswiler Chilbi &amp; FC Fest</span>
              </div>
              <div class="blueprint-checklist-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span><strong>Sportanlage &amp; Situationsplan:</strong> Hauptspielfeld, Trainingsplatz Hohbühl/Lindenrain, Garderobenbau &amp; Parkordnung</span>
              </div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Bereich C: Sportanlage Lindenrain, Clubhaus-Vermietung &amp; Vereinsanlässe (10 Seiten)', 'Infrastruktur &amp; Events FC Attiswil (Status: Vorbereitet · Folgt beim Ausbau)', 'Philipp Singer (Vizepräsident · 079 304 44 56) &amp; Christina Lemp (Clubhauswirtin · 079 916 64 55)', 'clubhaus')">
            <span>Seiten-Übersicht für Bereich C öffnen</span>
          </button>
        </article>
        <!-- BEREICH D: SPIELBETRIEB, MATCHBERICHTE, VEREINSARTIKEL & FOTO-GALERIEN -->
        <article class="blueprint-module-card">
          <div>
            <div class="blueprint-module-top">
              <span class="blueprint-mod-tag">Bereich D · 7 Unterseiten offen</span>
              <span class="blueprint-lock-badge">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span>Status: Vorbereitet · Folgt beim Ausbau</span>
              </span>
            </div>
            <h3 class="blueprint-module-title">Matchberichte, SOFV-Spielbetrieb, Vereinskollektion &amp; Foto-Archiv</h3>
            <p class="blueprint-module-desc">
              Alle News-Beiträge, Matchberichte der Aktivteams, die offizielle FCA-Vereinskollektion (Albani Sport / Texova) sowie die Bildergalerien vom Lindenrain werden hier gebündelt:
            </p>
            <div class="wireframe-preview-box" aria-hidden="true">
              <div class="wireframe-skeleton-header">
                <span>Vorschau-Übersicht: Spielbetrieb, Shop &amp; Medien</span>
                <span>0 / 7 Seiten gebaut</span>
              </div>
              <div class="wireframe-grid-3">
                <div class="wireframe-slot">
                  <div class="wireframe-img-placeholder">MATCHBERICHTE</div>
                  <div class="wireframe-line-lg"></div>
                  <div class="wireframe-line-sm"></div>
                </div>
                <div class="wireframe-slot">
                  <div class="wireframe-img-placeholder">VEREINSKOLLEKTION</div>
                  <div class="wireframe-line-lg"></div>
                  <div class="wireframe-line-sm"></div>
                </div>
                <div class="wireframe-slot">
                  <div class="wireframe-img-placeholder">FOTO-ARCHIV</div>
                  <div class="wireframe-line-lg"></div>
                  <div class="wireframe-line-sm"></div>
                </div>
              </div>
            </div>
            <div class="blueprint-checklist">
              <div class="blueprint-checklist-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span><strong>Aktuelle Matchberichte &amp; SOFV-Tabellen:</strong> Direkt-Integration der Spielpläne &amp; Resultate des Solothurner Fussballverbands (SOFV Verein Nr. 1880)</span>
              </div>
              <div class="blueprint-checklist-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span><strong>Vereinsartikel &amp; Fan-Shop:</strong> Offizielle FC-Attiswil-Kollektion (Koordination: Raphaela Lüscher · 079 453 88 60 · Ausrüster Albani Sport Balsthal)</span>
              </div>
              <div class="blueprint-checklist-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span><strong>Foto-Galerien &amp; Fairplay:</strong> Cupsieg-Feier Frauen 2025, SFV-Zertifizierung 2026, Juniorenlager &amp; Anlaufstelle Fairplay (fairplay@fcattiswil.ch)</span>
              </div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Bereich D: Spielbetrieb, Matchberichte, Vereinsartikel &amp; Foto-Archiv (7 Seiten)', 'Spielbetrieb &amp; Medien FC Attiswil (Status: Vorbereitet · Folgt beim Ausbau)', 'Florian Bohner (Sportchef · 079 677 93 52) &amp; Raphaela Lüscher (Vereinsartikel · 079 453 88 60)', 'spielbetrieb')">
            <span>Seiten-Übersicht für Bereich D öffnen</span>
          </button>
        </article>
      </div>
    </div>
  </section>
"""
    return render_shell(
        filename="index.html",
        page_title="FC Attiswil — Architektur-Studie V2 (6-%-Prototyp & Bauplan)",
        active_nav="startseite",
        body_html=body,
    )

# ---------------------------------------------------------------------------
# 4. PAGE 2: HERREN-1.HTML (MUSTER-TEAM 1/14 + 13 ROHBAU-TEAMS-MATRIX)
# ---------------------------------------------------------------------------
HERREN_EXTRA_CSS = """
    .architect-banner {
      background: linear-gradient(135deg, var(--fca-navy-deep) 0%, #1E293B 100%);
      color: #FFFFFF;
      padding: 44px 0;
      border-bottom: 3px solid var(--fca-gold);
    }
    .architect-box {
      background-color: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(245, 158, 11, 0.4);
      border-left: 5px solid var(--fca-gold);
      border-radius: var(--radius-md);
      padding: 24px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      flex-wrap: wrap;
    }
    .team-switcher-bar {
      display: inline-flex;
      background-color: #FFFFFF;
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-md);
      padding: 6px;
      gap: 6px;
      box-shadow: var(--shadow-sm);
      flex-wrap: wrap;
    }
    .team-switch-btn {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.88rem;
      font-weight: 800;
      padding: 11px 18px;
      border-radius: var(--radius-sm);
      border: none;
      background: transparent;
      color: var(--text-body);
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .team-switch-btn.active {
      background-color: var(--fca-red);
      color: #FFFFFF;
      box-shadow: var(--shadow-sm);
    }
    .team-switch-badge {
      font-size: 0.68rem;
      padding: 2px 7px;
      border-radius: var(--radius-sm);
      background-color: rgba(255, 255, 255, 0.2);
      color: #FEF08A;
      text-transform: uppercase;
    }
    .team-hero-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-md);
      margin-bottom: 36px;
    }
    .team-hero-grid {
      display: grid;
      grid-template-columns: 1.22fr 0.78fr;
    }
    .team-photo-stage {
      background-color: var(--fca-navy);
      position: relative;
      min-height: 360px;
    }
    .team-photo-stage img {
      width: 100%;
      height: 100%;
      max-height: 450px;
      object-fit: cover;
    }
    .team-info-stage {
      padding: 30px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 18px;
      background-color: #FFFFFF;
    }
    .team-sponsor-strip {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 12px 14px;
      background-color: var(--bg-muted);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-sm);
    }
    .team-sponsor-strip img {
      width: 96px;
      height: 44px;
      object-fit: contain;
      background-color: #FFFFFF;
      padding: 4px;
      border-radius: var(--radius-sm);
      flex-shrink: 0;
    }
    /* Staff Cards */
    .staff-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
      margin-bottom: 40px;
    }
    .staff-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 16px;
      display: flex;
      align-items: center;
      gap: 14px;
      box-shadow: var(--shadow-sm);
    }
    .staff-avatar {
      width: 68px;
      height: 86px;
      border-radius: var(--radius-sm);
      object-fit: cover;
      background-color: var(--fca-navy);
      flex-shrink: 0;
      border: 2px solid var(--fca-red);
    }
    .staff-avatar-placeholder {
      width: 68px;
      height: 86px;
      border-radius: var(--radius-sm);
      background: linear-gradient(135deg, var(--fca-navy) 0%, var(--fca-red) 100%);
      color: #FBBF24;
      font-family: 'Montserrat', sans-serif;
      font-weight: 800;
      font-size: 1.15rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    /* Roster Position Groups */
    .roster-pos-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
    }
    .roster-pos-box {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 22px;
      box-shadow: var(--shadow-sm);
    }
    .roster-pos-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 12px;
      margin-bottom: 14px;
      border-bottom: 2px solid var(--fca-red-soft);
    }
    .roster-pos-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 1rem;
      font-weight: 800;
      color: var(--fca-navy);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .roster-player-list {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
    }
    .player-pill {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 9px 12px;
      background-color: var(--bg-page);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-sm);
    }
    .player-num {
      width: 32px;
      height: 30px;
      border-radius: var(--radius-sm);
      background-color: var(--fca-navy);
      color: #FBBF24;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.76rem;
      font-weight: 800;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .player-name {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.25;
    }
    /* 14-Teams Matrix */
    .matrix-group-block {
      margin-bottom: 32px;
    }
    .matrix-group-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 14px;
      padding-bottom: 8px;
      border-bottom: 2px solid var(--border-light);
    }
    .matrix-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
    }
    .matrix-team-btn {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 14px 16px;
      text-align: left;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 8px;
      transition: all 0.2s ease;
      font-family: inherit;
    }
    .matrix-team-btn:hover {
      border-color: var(--fca-red);
      box-shadow: var(--shadow-sm);
      transform: translateY(-2px);
    }
    .matrix-team-btn.live-built {
      border: 2px solid var(--fca-red);
      background-color: var(--fca-red-soft);
    }
    .matrix-team-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      width: 100%;
    }
    .matrix-team-name {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.9rem;
      font-weight: 800;
      color: var(--fca-navy);
    }
    .matrix-status-pill {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.64rem;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      white-space: nowrap;
    }
    .pill-live {
      background-color: var(--fca-green);
      color: #FFFFFF;
    }
    @media (max-width: 1080px) {
      .team-hero-grid, .roster-pos-grid {
        grid-template-columns: 1fr;
      }
      .staff-grid, .matrix-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    .team-sponsors-pair,
    .team-cta-pair {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
    }
    @media (max-width: 720px) {
      .staff-grid, .roster-player-list, .matrix-grid, .team-sponsors-pair, .team-cta-pair {
        grid-template-columns: 1fr;
      }
      .team-info-stage {
        padding: 20px 18px;
      }
    }
"""

def build_herren1_html() -> str:
    staff_cards = []
    for st in HERREN_1_STAFF:
        if st["photo"]:
            avatar_html = f'<img src="{st["photo"]}" alt="{st["name"]} — {st["role"]}" class="staff-avatar" width="68" height="86" loading="lazy" decoding="async">'
        else:
            avatar_html = f'<div class="staff-avatar-placeholder">{st["initials"]}</div>'
        staff_cards.append(f"""
          <div class="staff-card">
            {avatar_html}
            <div>
              <div style="font-family:'Montserrat',sans-serif;font-size:0.7rem;font-weight:800;text-transform:uppercase;color:var(--fca-red);letter-spacing:0.04em;">{st['role']}</div>
              <div style="font-family:'Montserrat',sans-serif;font-size:0.98rem;font-weight:800;color:var(--fca-navy);margin:2px 0 4px;">{st['name']}</div>
              <div style="font-size:0.78rem;color:var(--text-body);">{st['phone']}</div>
            </div>
          </div>""")
    roster_boxes = []
    for pos_name, players in HERREN_1_ROSTER.items():
        pills = []
        for num, pname in players:
            pills.append(f"""
              <div class="player-pill">
                <span class="player-num">{num}</span>
                <span class="player-name">{pname}</span>
              </div>""")
        roster_boxes.append(f"""
          <div class="roster-pos-box">
            <div class="roster-pos-head">
              <span class="roster-pos-title">{pos_name}</span>
              <span class="pillar-count">{len(players)} Spieler</span>
            </div>
            <div class="roster-player-list">{''.join(pills)}
            </div>
          </div>""")
    matrix_blocks = []
    for grp in ALL_14_TEAMS_GROUPS:
        tiles = []
        for t_name, t_sub, t_status, t_contact in grp["teams"]:
            if t_status == "herren1":
                tiles.append(f"""
          <button type="button" class="matrix-team-btn live-built" onclick="window.scrollTo({{top: 220, behavior: 'smooth'}});">
            <div class="matrix-team-top">
              <span class="matrix-team-name">{t_name}</span>
              <span class="matrix-status-pill pill-live">1/14 · Ausgearbeitet</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-body);font-weight:600;">Als Beispiel-Team komplett ausgearbeitet (4 Staff-Mitglieder &amp; 22 Kaderspieler oben sichtbar)</span>
          </button>""")
            else:
                tiles.append(f"""
          <button type="button" class="matrix-team-btn wireframe-locked" onclick="wpOpenBlueprintModal('Team (vorbereitet): {t_name}', '{t_sub} (Status: Vorbereitet · Folgt beim Ausbau)', '{t_contact}', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">{t_name}</span>
              <span class="pill-wireframe-lock">
                <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span>VORBEREITET</span>
              </span>
            </div>
            <div class="wireframe-mini-skeleton" aria-hidden="true">
              <div class="wireframe-mini-thumb"></div>
              <div class="wireframe-mini-bars">
                <div class="wireframe-mini-bar" style="width:82%;"></div>
                <div class="wireframe-mini-bar" style="width:58%;"></div>
              </div>
            </div>
            <span style="font-size:0.74rem;color:#475569;font-weight:700;">{t_sub} · Klick für Trainer &amp; Trainingszeiten</span>
          </button>""")
        matrix_blocks.append(f"""
      <div class="matrix-group-block">
        <div class="matrix-group-header">
          <h3 style="font-size:1.18rem;font-weight:800;">{grp['group_title']}</h3>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">{grp['group_lead']}</span>
        </div>
        <div class="matrix-grid">{''.join(tiles)}
        </div>
      </div>""")
    body = f"""
  <!-- FORTSCHRITTS-BANNER: NUR 1 VON 14 TEAMS (7 %) ALS MUSTER FERTIG — 13 TEAMS OFFEN -->
  <section class="architect-banner" data-section="vorschau-hinweis">
    <div class="container">
      <div class="architect-box">
        <div style="max-width:780px;">
          <div class="section-kicker kicker-light" style="margin-bottom:6px;" data-slot="arch_kicker">MANNSCHAFTS-ÜBERSICHT: 1 BEISPIEL-TEAM AUSGEARBEITET — 13 WEITERE TEAMS VORBEREITET</div>
          <h1 style="color:#FFFFFF;font-size:clamp(1.45rem,2.5vw,2rem);font-weight:800;margin-bottom:8px;" data-slot="arch_title">
            1 Beispiel-Team ausgearbeitet (1. Mannschaft) — 13 weitere Mannschaften vorbereitet
          </h1>
          <p style="font-size:0.9rem;color:#E2E8F0;line-height:1.55;margin-bottom:14px;" data-slot="arch_desc">
            Um die künftige Qualität am echten Beispiel zu zeigen, ist in dieser Vorschau exakt <strong>1 von 14 Mannschaften (1. Mannschaft · Herren 4. Liga · 7 %)</strong> komplett mit Original-Mannschaftsfoto, den 4 Staff-Mitgliedern, beiden Trikotsponsoren und allen 22 Kaderspielern ausgearbeitet. Alle weiteren <strong>13 Mannschaften (93 %)</strong> — inklusive <em>Frauen 2. Liga (Cupsiegerinnen 2025)</em>, <em>Frauen 3. Liga</em>, <em>Senioren 30+</em>, <em>Junioren B–G</em> und <em>Juniorinnen FF-17/14/11</em> — stehen unten als <strong>vorbereitete Team-Platzhalter</strong> bereit.
          </p>
          <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:rgba(15,23,42,0.75);border:1px dashed #F59E0B;padding:8px 12px;border-radius:var(--radius-sm);">
            <div class="wp-v2-progress-track" style="width:140px;">
              <div class="wp-v2-progress-fill" style="width:12%;"></div>
            </div>
            <span style="font-family:'Montserrat',sans-serif;font-size:0.75rem;font-weight:800;color:#FDE68A;">
              1 von 14 Teams ausgearbeitet · 13 weitere Teams + Team Bravo vorbereitet
            </span>
          </div>
        </div>
        <div style="display:flex;flex-direction:column;gap:8px;flex-shrink:0;">
          <a href="#alle-teams-matrix" class="btn-cta btn-cta-gold btn-sm">Zu den 13 weiteren Teams</a>
          <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-ghost-light btn-sm">Probetraining-Anfrage testen</a>
        </div>
      </div>
    </div>
  </section>
  <!-- BEISPIEL-TEAM SEKTION (1. MANNSCHAFT HERREN 4. LIGA · 1 VON 14) -->
  <section id="beispiel-team-detail" data-section="beispiel-team-detail">
    <div class="container">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;margin-bottom:20px;">
        <div class="team-switcher-bar">
          <span class="team-switch-btn active" style="cursor:default;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Beispiel-Team 1/14: 1. Mannschaft (Herren 4. Liga)</span>
            <span class="team-switch-badge">22 Spieler · Beispiel</span>
          </span>
          <a href="#alle-teams-matrix" class="team-switch-btn" style="border:1px dashed #94A3B8;background-color:#E2E8F0;color:#334155;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            <span>Teams 2–14: Frauen 2./3. Liga, Senioren &amp; 10 Nachwuchs-Teams (folgen beim Ausbau)</span>
          </a>
        </div>
        <div style="font-size:0.84rem;color:var(--text-muted);font-weight:600;">
          Sportchef FC Attiswil: <strong>Florian Bohner</strong> (079 677 93 52 · info@fcattiswil.ch)
        </div>
      </div>
      <!-- TEAM HERO CARD -->
      <div class="team-hero-card">
        <div class="team-hero-grid">
          <div class="team-photo-stage">
            <img src="images/team-herren-1.webp" alt="FC Attiswil 1. Mannschaft Herren 4. Liga Mannschaftsfoto" width="760" height="420" data-slot="h1_team_photo">
            <span class="card-badge">1. Mannschaft · Herren 4. Liga · Sportanlage Lindenrain</span>
          </div>
          <div class="team-info-stage">
            <div>
              <div class="section-kicker" style="margin-bottom:8px;">FANIONTEAM AKTIVE HERREN · SOFV 4. LIGA</div>
              <h2 style="font-size:1.72rem;font-weight:800;margin-bottom:10px;" data-slot="h1_title">FC Attiswil — 1. Mannschaft</h2>
              <p style="font-size:0.92rem;color:var(--text-body);line-height:1.6;margin-bottom:16px;" data-slot="h1_desc">
                Unser Fanionteam in der 4. Liga des Solothurner Fussballverbands (SOFV) unter der Leitung von Cheftrainer <strong>Stephan Sperisen</strong>, Assistenztrainer <strong>Michael Marti</strong> und Goalie-Trainer <strong>Mirco Flüeli</strong>. Jüngste Highlights: 4:2-Auswärtssieg in Däniken (Hattrick von Mike Richard &amp; Tor von Joel) sowie Heimsieg gegen den FC Deitingen auf dem Lindenrain.
              </p>
              <div style="display:flex;flex-direction:column;gap:8px;padding:12px 14px;background-color:var(--bg-muted);border-radius:var(--radius-sm);font-size:0.85rem;margin-bottom:14px;">
                <div style="display:flex;align-items:center;gap:8px;">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--fca-red)" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                  <span><strong>Trainingszeiten:</strong> Dienstag &amp; Donnerstag, 19:30 – 21:00 Uhr (Lindenrain Attiswil)</span>
                </div>
                <div style="display:flex;align-items:center;gap:8px;">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--fca-red)" stroke-width="2.2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                  <span><strong>Direktkontakt Trainer:</strong> Stephan Sperisen (Tel. 079 705 76 06)</span>
                </div>
              </div>
              <!-- Team Sponsors Strip -->
              <div class="team-sponsors-pair">
                <div class="team-sponsor-strip">
                  <img src="images/sponsors/sponsor-01-auto-lemp.webp" alt="Auto Lemp AG Dresssponsor" width="96" height="44" loading="lazy" decoding="async">
                  <div style="font-size:0.76rem;line-height:1.3;">
                    <div style="color:var(--text-muted);font-weight:600;">Dresssponsor</div>
                    <a href="https://www.autolemp.ch/" target="_blank" rel="noopener noreferrer" style="font-weight:800;color:var(--fca-navy);">Auto Lemp AG</a>
                  </div>
                </div>
                <div class="team-sponsor-strip">
                  <img src="images/sponsors/sponsor-02-giacometto-transport.webp" alt="Giacometto Transport AG Einlaufleibchen" width="96" height="44" loading="lazy" decoding="async">
                  <div style="font-size:0.76rem;line-height:1.3;">
                    <div style="color:var(--text-muted);font-weight:600;">Einlaufleibchen</div>
                    <a href="https://www.giacometto.ch/firma/giacometto-transport-ag.html" target="_blank" rel="noopener noreferrer" style="font-weight:800;color:var(--fca-navy);">Giacometto AG</a>
                  </div>
                </div>
              </div>
            </div>
            <div class="team-cta-pair">
              <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-primary btn-sm">
                <span>Probetraining 1. Mannschaft</span>
              </a>
              <a href="https://matchcenter.sofv.ch/default.aspx?v=1880" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-outline btn-sm">
                <span>SOFV Spielplan &amp; Tabelle</span>
              </a>
            </div>
          </div>
        </div>
      </div>
      <!-- TRAINER- & SPORTCHEF-STAFF (4 PERSONEN) -->
      <h3 style="font-size:1.25rem;font-weight:800;margin-bottom:16px;">Trainerstab &amp; Sportliche Leitung (1. Mannschaft)</h3>
      <div class="staff-grid">{''.join(staff_cards)}
      </div>
      <!-- KADER NACH POSITIONEN (22 SPIELER) -->
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:18px;">
        <h3 style="font-size:1.25rem;font-weight:800;">Offizielles Kader 1. Mannschaft (22 Spieler nach Position)</h3>
        <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Datenstand: Offizielles Kader fcattiswil.ch · Saison 2026/27</span>
      </div>
      <div class="roster-pos-grid">{''.join(roster_boxes)}
      </div>
    </div>
  </section>
  <!-- 14-MANNSCHAFTEN-ÜBERSICHT (1 BEISPIEL-TEAM + 13 VORBEREITET) -->
  <section id="alle-teams-matrix" data-section="alle-teams-matrix" style="background-color:#E2E8F0;border-top:3px dashed #0F172A;">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="matrix_kicker">MANNSCHAFTS-ÜBERSICHT · 1 BEISPIEL-TEAM LIVE · 13 WEITERE VORBEREITET</div>
        <h2 class="section-title" data-slot="matrix_title">Alle 14 Mannschaften des FC Attiswil im Überblick (1 Beispiel-Team ausgearbeitet · 13 weitere vorbereitet).</h2>
        <p class="section-desc" data-slot="matrix_desc">
          Klicke auf eine der <strong>13 vorbereiteten Team-Kacheln</strong>, um die bereits hinterlegten Original-Trainer, Telefonnummern, Trainingszeiten und Sponsoren des jeweiligen Teams in der Seiten-Vorschau anzusehen:
        </p>
      </div>
{''.join(matrix_blocks)}
    </div>
  </section>
"""
    return render_shell(
        filename="herren-1.html",
        page_title="1. Mannschaft (Beispiel-Team 1/14) & 13 Rohbau-Teams — FC Attiswil",
        active_nav="teams",
        body_html=body,
        extra_css=HERREN_EXTRA_CSS,
    )
# ---------------------------------------------------------------------------
# 5. PAGE 3: KONTAKT.HTML (3-STEP SMART WIZARD & VEREINS-ZENTRALE)
# ---------------------------------------------------------------------------
KONTAKT_EXTRA_CSS = """
    .contact-layout {
      display: grid;
      grid-template-columns: 0.9fr 1.1fr;
      gap: 40px;
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
      gap: 11px;
      margin-top: 18px;
    }
    .contact-direct-item {
      padding: 11px 14px;
      background-color: var(--bg-page);
      border: 1px solid var(--border-light);
      border-left: 3px solid var(--fca-red);
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
    }
    .contact-direct-role {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.71rem;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--fca-red);
      letter-spacing: 0.04em;
    }
    .contact-direct-person {
      font-weight: 700;
      color: var(--fca-navy);
      margin-top: 2px;
    }
    .contact-direct-links {
      color: var(--text-body);
      font-size: 0.81rem;
      margin-top: 2px;
    }
    /* Smart Wizard Card */
    .wizard-card {
      background-color: #FFFFFF;
      border: 2px solid var(--fca-red);
      border-radius: var(--radius-md);
      padding: 32px;
      box-shadow: var(--shadow-md);
    }
    .wp-stepper {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin-bottom: 24px;
      padding: 6px;
      background-color: var(--bg-muted);
      border-radius: var(--radius-md);
    }
    .wp-step-pill {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 10px 8px;
      border-radius: var(--radius-sm);
      font-family: 'Montserrat', sans-serif;
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--text-muted);
      text-align: center;
    }
    .wp-step-pill.active {
      background-color: var(--fca-red);
      color: #FFFFFF;
    }
    .wp-step-pill.done {
      background-color: var(--fca-green-soft);
      color: #166534;
    }
    .wp-step-num {
      width: 22px;
      height: 22px;
      border-radius: var(--radius-sm);
      background-color: rgba(255, 255, 255, 0.2);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.72rem;
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
      margin-bottom: 22px;
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
      justify-content: flex-start;
      gap: 6px;
      transition: all 0.18s ease;
      font-family: inherit;
    }
    .wp-role-tile:hover {
      border-color: var(--fca-red);
      background-color: #FFFFFF;
    }
    .wp-role-tile.selected {
      border: 2px solid var(--fca-red);
      background-color: var(--fca-red-soft);
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
      background-color: #FFFFFF;
      color: var(--fca-red);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      border: 1px solid var(--border-light);
    }
    .wp-role-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.84rem;
      font-weight: 800;
      color: var(--fca-navy);
      line-height: 1.25;
    }
    .wp-role-desc {
      font-size: 0.76rem;
      color: var(--text-body);
      line-height: 1.4;
    }
    /* Form Fields (S-20 aligned) */
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
      font-family: 'Montserrat', sans-serif;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--fca-navy);
      line-height: 1.3;
    }
    .form-input, .form-textarea {
      width: 100%;
      font-family: 'Inter', sans-serif;
      font-size: 0.9rem;
      color: var(--text-main);
      background-color: #FFFFFF;
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-sm);
      padding: 11px 14px;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }
    .form-input:focus, .form-textarea:focus {
      outline: none;
      border-color: var(--fca-red);
      box-shadow: 0 0 0 3px rgba(200, 30, 30, 0.14);
    }
    .form-textarea {
      min-height: 104px;
      resize: vertical;
    }
    /* Upload Zone */
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
      padding: 9px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-strong);
      background-color: #FFFFFF;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--fca-navy);
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
      width: 20px;
      height: 20px;
      background-color: var(--fca-navy);
      color: #FFFFFF;
      border: none;
      border-radius: var(--radius-sm);
      font-size: 0.7rem;
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
      background-color: var(--fca-green-soft);
      color: #166534;
      border: 1px solid #86EFAC;
    }
    .wp-selftest-banner {
      background-color: var(--fca-gold-soft);
      border: 1px solid #FDE047;
      border-left: 4px solid var(--fca-gold-dark);
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
      border: 2px solid var(--fca-green);
      border-radius: var(--radius-md);
    }
    .wp-success-box.visible {
      display: flex;
    }
    .wp-wa-preview {
      font-family: 'Inter', sans-serif;
      font-size: 0.82rem;
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-left: 4px solid var(--fca-green);
      padding: 12px 14px;
      border-radius: var(--radius-sm);
      white-space: pre-wrap;
      color: var(--text-main);
    }
    @media (max-width: 1080px) {
      .contact-layout {
        grid-template-columns: 1fr;
      }
    }
    @media (max-width: 720px) {
      .wp-role-grid, .form-grid-2, .wp-stepper {
        grid-template-columns: 1fr;
      }
      .wizard-card {
        padding: 20px;
      }
    }
"""

def build_kontakt_html() -> str:
    body = """
  <section data-section="kontakt-zentrale" style="padding: 60px 0 84px;">
    <div class="container">
      <div class="contact-layout">
        <!-- LEFT COLUMN: VEREINS-ANLAUFSTELLEN FC ATTISWIL -->
        <div class="contact-info-panel">
          <div class="section-kicker" data-slot="contact_kicker">VEREINS-, PROBETRAINING-, CLUBHAUS- &amp; SPONSORING-ZENTRALE</div>
          <h1 style="font-size:clamp(1.62rem,2.5vw,2.15rem);font-weight:800;margin-bottom:12px;" data-slot="contact_title">
            Direkter Draht zum Vorstand &amp; zu allen Ressorts im FC Attiswil.
          </h1>
          <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:16px;" data-slot="contact_lead">
            Ob Probetraining auf dem Lindenrain, Beitritt zum <strong>300er Club</strong>, Matchballspende (CHF 150.00), Miete des <strong>Clubhauses Lindenrain</strong> (48 Innen- &amp; 40 gedeckte Sitzplätze) oder Mitgliedschaft: Unser 3-Schritte-Assistent erstellt sofort ein übersichtliches <strong>1-Seiten-PDF-Vereinsdossier</strong> für das zuständige Vorstandsmitglied.
          </p>
          <div class="contact-direct-list">
            <div class="contact-direct-item">
              <div class="contact-direct-role">Präsidium &amp; Vereinsführung</div>
              <div class="contact-direct-person">Konrad Schütz (Präsident) &amp; Michelle Kurth (Sekretärin / Datenschutz)</div>
              <div class="contact-direct-links">info@fcattiswil.ch · Tel. 079 661 66 12 · Sportplatzweg 1, 4536 Attiswil</div>
            </div>
            <div class="contact-direct-item">
              <div class="contact-direct-role">Vizepräsidium, Vereinsanlässe &amp; Vermietung Clubhaus Lindenrain</div>
              <div class="contact-direct-person">Philipp Singer (Vizepräsident) &amp; Christina Lemp (Clubhauswirtin)</div>
              <div class="contact-direct-links">Tel. 079 304 44 56 (Vermietung) · Tel. 079 916 64 55 (Wirtin) · 48 Innen- / 40 Aussenplätze</div>
            </div>
            <div class="contact-direct-item">
              <div class="contact-direct-role">Sportliche Leitung Aktive &amp; J+S Coach</div>
              <div class="contact-direct-person">Florian Bohner (Sportchef) &amp; Stephan Sperisen (Trainer 1. Mannschaft)</div>
              <div class="contact-direct-links">Tel. 079 677 93 52 (Sportchef) · Tel. 079 705 76 06 (Trainer 1. Mannschaft)</div>
            </div>
            <div class="contact-direct-item">
              <div class="contact-direct-role">Frauen 2./3. Liga &amp; Juniorinnen FF-17 / FF-14 / FF-11</div>
              <div class="contact-direct-person">Celine Lemp (Verantwortliche Frauen &amp; Juniorinnen)</div>
              <div class="contact-direct-links">Tel. 079 137 82 38 · Dana Scherrer (079 408 28 94) · Tom Moser (079 418 76 68)</div>
            </div>
            <div class="contact-direct-item">
              <div class="contact-direct-role">Junioren B bis G (Piccolos)</div>
              <div class="contact-direct-person">Levi Meyer (Verantwortlicher Junioren im Vorstand)</div>
              <div class="contact-direct-links">Tel. 079 475 75 80 · info@fcattiswil.ch</div>
            </div>
            <div class="contact-direct-item">
              <div class="contact-direct-role">Marketing, Sponsoring, 300er Club &amp; Vereinsartikel</div>
              <div class="contact-direct-person">Raphaela Lüscher (Marketing / Sponsoring &amp; Vereinskollektion)</div>
              <div class="contact-direct-links">sponsoring@fcattiswil.ch · 300erClub@fcattiswil.ch · Tel. 079 453 88 60</div>
            </div>
            <div class="contact-direct-item">
              <div class="contact-direct-role">Finanzen, Mitgliederbeiträge &amp; Infrastruktur Lindenrain</div>
              <div class="contact-direct-person">Jörg Scheidegger (Kassier · 032 637 21 76), Sarah Probst (079 535 83 48) &amp; Remo Brudermann (079 533 09 81)</div>
              <div class="contact-direct-links">Jahresbeitrag: Aktive CHF 160.00 · Junioren CHF 80.00 · Passiv CHF 50.00</div>
            </div>
            <div class="contact-direct-item">
              <div class="contact-direct-role">Schiedsrichter, Platzwart &amp; Fairplay</div>
              <div class="contact-direct-person">Slavko Martinovic (SR-Verantwortlicher · 079 235 37 35) &amp; Christoph Rüegger (Platzwart · 079 576 76 80)</div>
              <div class="contact-direct-links">fairplay@fcattiswil.ch · Alfred Bohner (079 226 81 65)</div>
            </div>
          </div>
        </div>
        <!-- RIGHT COLUMN: 3-STEP SMART WIZARD -->
        <div class="wizard-card">
          <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:14px;">
            <div>
              <div class="section-kicker" style="margin-bottom:4px;">DIGITALE VEREINS-ZENTRALE · FC ATTISWIL</div>
              <h2 style="font-size:1.35rem;font-weight:800;" id="wpWizardTitle">1. Wähle dein Anliegen</h2>
            </div>
            <span class="pillar-count" id="wpActiveAssigneeBadge">Zuständig: Sportliche Leitung</span>
          </div>
          <div class="wp-stepper" aria-label="Fortschritt">
            <div class="wp-step-pill active" id="wpStepPill1">
              <span class="wp-step-num">1</span>
              <span>Anliegen &amp; Ressort</span>
            </div>
            <div class="wp-step-pill" id="wpStepPill2">
              <span class="wp-step-num">2</span>
              <span>Details &amp; Beilagen</span>
            </div>
            <div class="wp-step-pill" id="wpStepPill3">
              <span class="wp-step-num">3</span>
              <span>Kontakt &amp; Dossier</span>
            </div>
          </div>
          <form id="fcaContactForm" onsubmit="return wpSubmitFcaLead(event)" novalidate>
            <!-- Honeypot -->
            <div style="display:none;" aria-hidden="true">
              <label for="wpHoneypot">Website URL</label>
              <input type="text" id="wpHoneypot" name="website_url" tabindex="-1" autocomplete="off">
            </div>
            <!-- STEP 1: TOPIC SELECTION (6 TILES) -->
            <div class="wp-step-pane active" id="wpStep1">
              <div class="wp-role-grid" id="wpTopicGrid">
                <button type="button" class="wp-role-tile selected" data-topic="Probetraining / Neumitglied" onclick="wpSelectFcaTopic('Probetraining / Neumitglied')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_1">Probetraining / Neumitglied</span>
                  </div>
                  <span class="wp-role-desc">Schnuppertraining für Junioren B–G, Juniorinnen FF-11 bis FF-17, Frauen, Herren oder Senioren</span>
                </button>
                <button type="button" class="wp-role-tile" data-topic="Sponsoring / 300er Club / Matchball" onclick="wpSelectFcaTopic('Sponsoring / 300er Club / Matchball')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_2">Sponsoring / 300er Club / Matchball</span>
                  </div>
                  <span class="wp-role-desc">Dress-/Bandensponsoring, 300er Club (CHF 300), Matchballspende (CHF 150) oder AVIA Tankkarte</span>
                </button>
                <button type="button" class="wp-role-tile" data-topic="Clubhaus Lindenrain mieten / Anlässe" onclick="wpSelectFcaTopic('Clubhaus Lindenrain mieten / Anlässe')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_3">Clubhaus Lindenrain mieten / Anlässe</span>
                  </div>
                  <span class="wp-role-desc">Reservation Clubhaus (48 Innen- &amp; 40 Aussenplätze), Lottomatch, Maskenball oder Chilbi</span>
                </button>
                <button type="button" class="wp-role-tile" data-topic="Spielbetrieb / Turniere / Schiedsrichter" onclick="wpSelectFcaTopic('Spielbetrieb / Turniere / Schiedsrichter')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_4">Spielbetrieb / Turniere / Schiedsrichter</span>
                  </div>
                  <span class="wp-role-desc">Spielverschiebungen, Freundschaftsspiele, Schiedsrichter-Interesse oder Platzbelegung</span>
                </button>
                <button type="button" class="wp-role-tile" data-topic="Mitgliedschaft / Mutation / Vereinsartikel" onclick="wpSelectFcaTopic('Mitgliedschaft / Mutation / Vereinsartikel')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_5">Mitgliedschaft / Mutation / Vereinsartikel</span>
                  </div>
                  <span class="wp-role-desc">Passivmitgliedschaft (CHF 50), Adressänderung, Jahresbeitrag oder FCA-Vereinskollektion</span>
                </button>
                <button type="button" class="wp-role-tile" data-topic="Allgemeine Vereinsanfrage / Vorstand" onclick="wpSelectFcaTopic('Allgemeine Vereinsanfrage / Vorstand')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_6">Allgemeine Vereinsanfrage / Vorstand</span>
                  </div>
                  <span class="wp-role-desc">Direkte Nachricht an Präsident Konrad Schütz, Sekretariat oder Fairplay-Anlaufstelle</span>
                </button>
              </div>
              <!-- Urgency Selector -->
              <div style="margin-bottom:20px;">
                <div class="form-label" style="margin-bottom:8px;">Zeitrahmen / Priorität</div>
                <div class="form-grid-2" id="wpUrgencyGrid">
                  <button type="button" class="wp-role-tile selected" data-urgency="Planbar / Laufende Saison" onclick="wpSelectFcaUrgency('Planbar / Laufende Saison')" style="padding:10px 12px;">
                    <span class="wp-role-title" style="font-size:0.8rem;">Planbar / Laufende Saison</span>
                    <span class="wp-role-desc" style="font-size:0.72rem;">Reguläre Bearbeitung durch das Ressort (24–48 Std.)</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urgency="Dringend / Nächster Spieltag" onclick="wpSelectFcaUrgency('Dringend / Nächster Spieltag')" style="padding:10px 12px;">
                    <span class="wp-role-title" style="font-size:0.8rem;">Dringend / Nächster Spieltag</span>
                    <span class="wp-role-desc" style="font-size:0.72rem;">Kurzfristiges Anliegen (Spielbetrieb / Anlass / Reservation)</span>
                  </button>
                </div>
              </div>
              <button type="button" class="btn-cta btn-cta-primary" style="width:100%;" onclick="wpNextStep(2)">
                <span>Weiter zu Schritt 2: Details &amp; Beilagen</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
              </button>
            </div>
            <!-- STEP 2: CONTEXT DETAILS & PHOTO UPLOAD -->
            <div class="wp-step-pane" id="wpStep2">
              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="wpDetail1" class="form-label" id="wpDetail1Label">Name &amp; Jahrgang Spieler/in</label>
                  <input type="text" id="wpDetail1" class="form-input" placeholder="z. B. Levin Muster · Jahrgang 2015">
                </div>
                <div class="form-field">
                  <label for="wpDetail2" class="form-label" id="wpDetail2Label">Gewünschte Mannschaft / Bisheriger Verein</label>
                  <input type="text" id="wpDetail2" class="form-input" placeholder="z. B. Junioren E / Frauen 2. Liga / 1. Mannschaft">
                </div>
              </div>
              <div class="form-field" style="margin-bottom:16px;">
                <label for="contactMessage" class="form-label" data-slot="lbl_message">Nachricht / Details zum Anliegen</label>
                <textarea id="contactMessage" name="message" class="form-textarea" placeholder="Beschreibe kurz dein Anliegen (z. B. Wunschtermin für Probetraining auf dem Lindenrain, Wunschdatum für Clubhaus-Miete oder gewünschtes Sponsoring-Paket)..."></textarea>
              </div>
              <div class="form-field" style="margin-bottom:20px;">
                <span class="form-label">Optional: Bis zu 3 Bilder / Dokumente anhängen (für 1-Seiten-PDF)</span>
                <div class="wp-upload-zone">
                  <input type="file" id="wpPhotoInput" accept="image/*" multiple style="display:none;" onchange="wpHandlePhotoFiles(this.files)">
                  <button type="button" class="wp-upload-btn" onclick="wpTriggerPhotoUpload()">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
                    <span>Bild / Beilage auswählen (z. B. Firmenlogo, Ausweis, Situationsfoto)</span>
                  </button>
                  <div style="font-size:0.75rem;color:var(--text-muted);margin-top:6px;" id="wpPhotoCounter">0 / 3 Bilder ausgewählt · Automatisch für das 1-Seiten-PDF-Dossier optimiert</div>
                  <div class="wp-photo-thumbs" id="wpPhotoThumbs"></div>
                </div>
              </div>
              <div class="form-grid-2">
                <button type="button" class="btn-cta btn-cta-outline" style="width:100%;" onclick="wpPrevStep()">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="15 18 9 12 15 6"/></svg>
                  <span>Zurück zu Schritt 1</span>
                </button>
                <button type="button" class="btn-cta btn-cta-primary" style="width:100%;" onclick="wpNextStep(3)">
                  <span>Weiter zu Schritt 3: Kontakt</span>
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
                </button>
              </div>
            </div>
            <!-- STEP 3: CONTACT DETAILS & SUBMIT -->
            <div class="wp-step-pane" id="wpStep3">
              <div class="wp-selftest-banner">
                <strong>Vorschau- &amp; Selbst-Test-Modus aktiv:</strong> Du kannst dieses Formular jetzt live testen. Das System generiert sofort ein echtes <strong>1-Seiten-PDF-Vereinsdossier</strong> mit FC-Attiswil-Briefkopf zum Herunterladen, ohne den Vorstand mit Test-Mails zu belasten.
              </div>
              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactName" class="form-label" data-slot="lbl_name">Vor- und Nachname (oder Eltern) *</label>
                  <input type="text" id="contactName" name="name" class="form-input" placeholder="z. B. Lukas Muster" required>
                </div>
                <div class="form-field">
                  <label for="contactCompany" class="form-label">Team / Firma / Organisation (optional)</label>
                  <input type="text" id="contactCompany" name="company" class="form-input" placeholder="z. B. Junioren D / Muster AG Attiswil">
                </div>
              </div>
              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactLoc" class="form-label">PLZ &amp; Wohnort *</label>
                  <input type="text" id="contactLoc" name="plz" class="form-input" placeholder="z. B. 4536 Attiswil" oninput="wpCheckFcaPlz(this.value)" required>
                </div>
                <div class="form-field">
                  <label for="contactStreet" class="form-label">Strasse &amp; Nr. (für Mutationen / Rechnungen)</label>
                  <input type="text" id="contactStreet" name="street" class="form-input" placeholder="z. B. Dorfstrasse 14">
                </div>
              </div>
              <div class="wp-plz-badge" id="wpPlzBadge" style="margin-bottom:14px;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
                <span id="wpPlzBadgeText">PLZ 4536: Einzugsgebiet Attiswil, Oberaargau &amp; Region Solothurn</span>
              </div>
              <div class="form-grid-2" style="margin-bottom:18px;">
                <div class="form-field">
                  <label for="contactEmail" class="form-label" data-slot="lbl_email">E-Mail-Adresse *</label>
                  <input type="email" id="contactEmail" name="email" class="form-input" placeholder="name@beispiel.ch" required>
                </div>
                <div class="form-field">
                  <label for="contactPhone" class="form-label" data-slot="lbl_phone">Telefon / Mobile (für Rückruf / WhatsApp) *</label>
                  <input type="tel" id="contactPhone" name="phone" class="form-input" placeholder="079 123 45 67" required>
                </div>
              </div>
              <div id="wpFormError" style="display:none;background-color:#FEE2E2;border:1px solid #FCA5A5;color:#991B1B;padding:10px 14px;border-radius:4px;font-size:0.84rem;margin-bottom:14px;"></div>
              <div class="form-grid-2">
                <button type="button" class="btn-cta btn-cta-outline" style="width:100%;" onclick="wpPrevStep()">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="15 18 9 12 15 6"/></svg>
                  <span>Zurück zu Schritt 2</span>
                </button>
                <button type="submit" class="btn-cta btn-cta-gold" id="wpSubmitBtn" style="width:100%;" data-slot="btn_submit">
                  <span id="wpSubmitBtnText">1-Seiten-Dossier &amp; Anfrage senden</span>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                </button>
              </div>
            </div>
          </form>
          <!-- SUCCESS COCKPIT -->
          <div class="wp-success-box" id="wpSuccessBox" aria-live="polite">
            <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
              <div style="display:flex;align-items:center;gap:10px;">
                <span style="width:36px;height:36px;border-radius:4px;background-color:var(--fca-green);color:#FFFFFF;display:inline-flex;align-items:center;justify-content:center;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><polyline points="20 6 9 17 4 12"/></svg>
                </span>
                <div>
                  <div style="font-family:'Montserrat',sans-serif;font-weight:800;font-size:1.05rem;color:var(--fca-navy);">Vereins-Anfrage &amp; 1-Seiten-PDF-Dossier erstellt</div>
                  <div style="font-size:0.78rem;color:var(--text-muted);" id="wpResChannels">1-Seiten-PDF-Dossier bereit zum Download</div>
                </div>
              </div>
              <span class="top-bar-badge" style="background-color:var(--fca-navy);color:#FBBF24;" id="wpResRef">#FCA-2026</span>
            </div>
            <div class="form-grid-2" style="background-color:#FFFFFF;padding:12px 14px;border-radius:4px;border:1px solid var(--border-light);font-size:0.84rem;">
              <div>
                <div style="color:var(--text-muted);font-size:0.75rem;">Zuständiges Ressort im FC Attiswil:</div>
                <strong style="color:var(--fca-navy);" id="wpResAssigned">Vorstand &amp; Sportliche Leitung</strong>
              </div>
              <div>
                <div style="color:var(--text-muted);font-size:0.75rem;">Erwartete Rückmeldung:</div>
                <strong style="color:var(--fca-red);" id="wpResCallback">Innert 24–48 Stunden</strong>
              </div>
            </div>
            <div>
              <div style="font-family:'Montserrat',sans-serif;font-size:0.75rem;font-weight:800;text-transform:uppercase;color:var(--fca-navy);margin-bottom:6px;">
                Vorschau der strukturierten WhatsApp-Sofortmeldung ans Ressort:
              </div>
              <div class="wp-wa-preview" id="wpResWaPreview"></div>
            </div>
            <div class="form-grid-2">
              <a href="kontakt.html" id="wpResPdfBtn" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-primary" style="width:100%;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                <span>1-Seiten-PDF-Dossier öffnen</span>
              </a>
              <button type="button" class="btn-cta btn-cta-outline" style="width:100%;" onclick="wpResetWizard()">
                <span>Weitere Anfrage erfassen</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <script>
    var wpFcaState = {
      step: 1,
      topic: 'Probetraining / Neumitglied',
      urgency: 'Planbar / Laufende Saison',
      photos: []
    };
    var wpFcaRoleConfig = {
      'Probetraining / Neumitglied': {
        assignee: 'Florian Bohner (Sportchef · 079 677 93 52), Levi Meyer (Junioren · 079 475 75 80) & Celine Lemp (Frauen/Juniorinnen · 079 137 82 38)',
        l1: 'Name & Jahrgang Spieler/in',
        p1: 'z. B. Levin Muster · Jahrgang 2015',
        l2: 'Gewünschte Mannschaft / Bisheriger Verein',
        p2: 'z. B. Junioren E / Frauen 2. Liga / 1. Mannschaft'
      },
      'Sponsoring / 300er Club / Matchball': {
        assignee: 'Raphaela Lüscher (Marketing & Sponsoring · 079 453 88 60 · sponsoring@fcattiswil.ch)',
        l1: 'Gewünschtes Engagement / Format',
        p1: 'z. B. 300er Club (CHF 300), Matchballspende (CHF 150), Dress- oder Bandensponsoring',
        l2: 'Unternehmen / Wunsch-Team für Patronat',
        p2: 'z. B. Muster AG Attiswil · 1. Mannschaft / Nachwuchs'
      },
      'Clubhaus Lindenrain mieten / Anlässe': {
        assignee: 'Philipp Singer (Vizepräsident / Anlässe & Vermietung · 079 304 44 56) & Christina Lemp (Wirtin · 079 916 64 55)',
        l1: 'Gewünschtes Mietdatum / Anlass',
        p1: 'z. B. Samstag, 14. November 2026 · Familienfest / Vereinsabend',
        l2: 'Erwartete Personenzahl (max. 48 innen / 40 aussen)',
        p2: 'z. B. ca. 35 Personen'
      },
      'Spielbetrieb / Turniere / Schiedsrichter': {
        assignee: 'Florian Bohner (Sportchef · 079 677 93 52) & Slavko Martinovic (SR-Verantwortlicher · 079 235 37 35)',
        l1: 'Betroffenes Team / Spielpaarung',
        p1: 'z. B. 1. Mannschaft oder Junioren D/9 · SOFV Meisterschaft',
        l2: 'Wunschdatum / Anliegen Spielbetrieb',
        p2: 'z. B. Spielverschiebung / Freundschaftsspiel / Schiedsrichter-Kurs'
      },
      'Mitgliedschaft / Mutation / Vereinsartikel': {
        assignee: 'Jörg Scheidegger (Kassier · 032 637 21 76), Michelle Kurth (Sekretärin) & Raphaela Lüscher (Vereinsartikel)',
        l1: 'Art der Mitgliedschaft / Artikelwunsch',
        p1: 'z. B. Passivmitglied (CHF 50), Adressänderung oder FCA-Trainerjacke Grösse M',
        l2: 'Mitglied-Nr. oder bisherige Adresse',
        p2: 'z. B. Neue Wohnadresse in 4536 Attiswil'
      },
      'Allgemeine Vereinsanfrage / Vorstand': {
        assignee: 'Konrad Schütz (Präsident · 079 661 66 12) & Michelle Kurth (Sekretärin · info@fcattiswil.ch)',
        l1: 'Betreff / Ressort',
        p1: 'z. B. Anfrage an das Präsidium / Fairplay / Medien',
        l2: 'Bezug zum FC Attiswil',
        p2: 'z. B. Vereinsmitglied / Gemeinde Attiswil / Eltern'
      }
    };
    function wpUpdateHeader() {
      var titles = {
        1: '1. Wähle dein Anliegen',
        2: '2. Eckdaten & Beilagen ergänzen',
        3: '3. Kontaktdaten & 1-Seiten-Dossier'
      };
      var tEl = document.getElementById('wpWizardTitle');
      if (tEl) tEl.textContent = titles[wpFcaState.step] || titles[1];
      for (var i = 1; i <= 3; i++) {
        var pill = document.getElementById('wpStepPill' + i);
        var pane = document.getElementById('wpStep' + i);
        if (pill) {
          pill.className = 'wp-step-pill' + (i === wpFcaState.step ? ' active' : (i < wpFcaState.step ? ' done' : ''));
        }
        if (pane) {
          pane.className = 'wp-step-pane' + (i === wpFcaState.step ? ' active' : '');
        }
      }
    }
    function wpSelectFcaTopic(topic) {
      wpFcaState.topic = topic;
      var btns = document.querySelectorAll('#wpTopicGrid .wp-role-tile');
      for (var i = 0; i < btns.length; i++) {
        var b = btns[i];
        if (b.getAttribute('data-topic') === topic) b.classList.add('selected');
        else b.classList.remove('selected');
      }
      var cfg = wpFcaRoleConfig[topic] || wpFcaRoleConfig['Probetraining / Neumitglied'];
      var badge = document.getElementById('wpActiveAssigneeBadge');
      if (badge) badge.textContent = 'Zuständig: ' + cfg.assignee.split('(')[0].trim();
      var l1 = document.getElementById('wpDetail1Label');
      var i1 = document.getElementById('wpDetail1');
      var l2 = document.getElementById('wpDetail2Label');
      var i2 = document.getElementById('wpDetail2');
      if (l1) l1.textContent = cfg.l1;
      if (i1) i1.placeholder = cfg.p1;
      if (l2) l2.textContent = cfg.l2;
      if (i2) i2.placeholder = cfg.p2;
    }
    function wpSelectFcaUrgency(urg) {
      wpFcaState.urgency = urg;
      var btns = document.querySelectorAll('#wpUrgencyGrid .wp-role-tile');
      for (var i = 0; i < btns.length; i++) {
        var b = btns[i];
        if (b.getAttribute('data-urgency') === urg) b.classList.add('selected');
        else b.classList.remove('selected');
      }
    }
    function wpNextStep(target) {
      wpFcaState.step = target;
      wpUpdateHeader();
    }
    function wpPrevStep() {
      if (wpFcaState.step > 1) {
        wpFcaState.step -= 1;
        wpUpdateHeader();
      }
    }
    function wpTriggerPhotoUpload() {
      var inp = document.getElementById('wpPhotoInput');
      if (inp) inp.click();
    }
    function wpCompressImageFile(file, cb) {
      var reader = new FileReader();
      reader.onload = function(e) {
        var img = new Image();
        img.onload = function() {
          var maxSide = 1200;
          var w = img.width;
          var h = img.height;
          if (w > maxSide || h > maxSide) {
            if (w >= h) { h = Math.round(h * (maxSide / w)); w = maxSide; }
            else { w = Math.round(w * (maxSide / h)); h = maxSide; }
          }
          var canvas = document.createElement('canvas');
          canvas.width = w;
          canvas.height = h;
          var ctx = canvas.getContext('2d');
          ctx.drawImage(img, 0, 0, w, h);
          cb(canvas.toDataURL('image/jpeg', 0.78));
        };
        img.src = e.target.result;
      };
      reader.readAsDataURL(file);
    }
    function wpRenderPhotos() {
      var box = document.getElementById('wpPhotoThumbs');
      var cnt = document.getElementById('wpPhotoCounter');
      if (cnt) cnt.textContent = wpFcaState.photos.length + ' / 3 Bilder ausgewählt · Automatisch für das 1-Seiten-PDF-Dossier optimiert';
      if (!box) return;
      box.innerHTML = '';
      for (var i = 0; i < wpFcaState.photos.length; i++) {
        (function(idx) {
          var wrap = document.createElement('div');
          wrap.className = 'wp-thumb-item';
          var im = document.createElement('img');
          im.src = wpFcaState.photos[idx];
          im.alt = 'Beilage ' + (idx + 1);
          var btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'wp-thumb-remove';
          btn.textContent = 'x';
          btn.onclick = function() { wpRemovePhoto(idx); };
          wrap.appendChild(im);
          wrap.appendChild(btn);
          box.appendChild(wrap);
        })(i);
      }
    }
    function wpHandlePhotoFiles(files) {
      if (!files || !files.length) return;
      for (var i = 0; i < files.length; i++) {
        if (wpFcaState.photos.length >= 3) break;
        wpCompressImageFile(files[i], function(b64) {
          if (wpFcaState.photos.length < 3) {
            wpFcaState.photos.push(b64);
            wpRenderPhotos();
          }
        });
      }
    }
    function wpRemovePhoto(idx) {
      wpFcaState.photos.splice(idx, 1);
      wpRenderPhotos();
    }
    function wpCheckFcaPlz(val) {
      var badge = document.getElementById('wpPlzBadge');
      var txt = document.getElementById('wpPlzBadgeText');
      if (!badge || !txt) return;
      var m = String(val || '').match(/\\b(\\d{4})\\b/);
      if (!m) {
        badge.className = 'wp-plz-badge';
        return;
      }
      var plz = parseInt(m[1], 10);
      badge.className = 'wp-plz-badge in-area';
      if ((plz >= 4500 && plz <= 4799) || (plz >= 3300 && plz <= 3399) || (plz >= 4900 && plz <= 4999)) {
        txt.textContent = 'PLZ ' + m[1] + ': Direktes Einzugsgebiet Attiswil, Oberaargau & Jurasüdfuss (Sportanlage Lindenrain)';
      } else {
        txt.textContent = 'PLZ ' + m[1] + ': Region Solothurn / Bern / Schweiz — Herzlich willkommen beim FC Attiswil';
      }
    }
    function wpStripEmojisForDom(str) {
      return String(str || '').replace(/[\\u{1F300}-\\u{1FAFF}\\u{2600}-\\u{27BF}]/gu, '').replace(/\\s+\\n/g, '\\n').trim();
    }
    function wpResetWizard() {
      wpFcaState.step = 1;
      wpFcaState.photos = [];
      wpRenderPhotos();
      var form = document.getElementById('fcaContactForm');
      if (form) {
        form.reset();
        form.style.display = 'block';
      }
      var sBox = document.getElementById('wpSuccessBox');
      if (sBox) sBox.classList.remove('visible');
      var err = document.getElementById('wpFormError');
      if (err) err.style.display = 'none';
      var badge = document.getElementById('wpPlzBadge');
      if (badge) badge.className = 'wp-plz-badge';
      wpSelectFcaTopic('Probetraining / Neumitglied');
      wpSelectFcaUrgency('Planbar / Laufende Saison');
      wpUpdateHeader();
    }
    function wpSubmitFcaLead(e) {
      if (e) e.preventDefault();
      var errBox = document.getElementById('wpFormError');
      if (errBox) errBox.style.display = 'none';
      var name = (document.getElementById('contactName').value || '').trim();
      var company = (document.getElementById('contactCompany').value || '').trim();
      var loc = (document.getElementById('contactLoc').value || '').trim();
      var street = (document.getElementById('contactStreet').value || '').trim();
      var email = (document.getElementById('contactEmail').value || '').trim();
      var phone = (document.getElementById('contactPhone').value || '').trim();
      var msg = (document.getElementById('contactMessage').value || '').trim();
      var d1 = (document.getElementById('wpDetail1').value || '').trim();
      var d2 = (document.getElementById('wpDetail2').value || '').trim();
      var hp = (document.getElementById('wpHoneypot').value || '').trim();
      if (!name || (!phone && !email)) {
        if (errBox) {
          errBox.textContent = 'Bitte gib deinen Namen sowie deine E-Mail-Adresse oder Telefonnummer an.';
          errBox.style.display = 'block';
        }
        return false;
      }
      var cfg = wpFcaRoleConfig[wpFcaState.topic] || wpFcaRoleConfig['Probetraining / Neumitglied'];
      var extra = {};
      extra[cfg.l1] = d1 || 'Keine Angabe';
      extra[cfg.l2] = d2 || 'Keine Angabe';
      var btn = document.getElementById('wpSubmitBtn');
      var btnTxt = document.getElementById('wpSubmitBtnText');
      if (btn) btn.disabled = true;
      if (btnTxt) btnTxt.textContent = '1-Seiten-PDF-Dossier wird erstellt...';
      var payload = {
        client_slug: 'fcattiswil',
        source_page: 'preview-fcattiswil/kontakt.html',
        website_url: hp,
        category: wpFcaState.topic,
        sparte: wpFcaState.topic,
        urgency: wpFcaState.urgency,
        name: name,
        company: company,
        street: street,
        plz: loc,
        phone: phone,
        email: email,
        message: msg || ('Anfrage zum Bereich ' + wpFcaState.topic),
        extra_fields: extra,
        photos: wpFcaState.photos,
        self_test_mode: true
      };
      fetch('/api/lead-submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
      .then(function(r) { return r.json(); })
      .then(function(res) {
        if (btn) btn.disabled = false;
        if (btnTxt) btnTxt.textContent = '1-Seiten-Dossier & Anfrage senden';
        if (!res || !res.ok) {
          if (errBox) {
            errBox.textContent = (res && res.error) ? res.error : 'Übermittlung fehlgeschlagen. Bitte versuche es erneut.';
            errBox.style.display = 'block';
          }
          return;
        }
        document.getElementById('fcaContactForm').style.display = 'none';
        document.getElementById('wpResRef').textContent = res.ref_code || '#FCA-2026';
        document.getElementById('wpResAssigned').textContent = res.assigned_to || cfg.assignee;
        document.getElementById('wpResCallback').textContent = res.callback_window || 'Persönliche Rückmeldung durch das Ressort';
        var chTxt = '1-Seiten-PDF-Dossier erstellt';
        if (res.email_sent) chTxt += ' · E-Mail mit PDF-Anhang zugestellt';
        if (res.whatsapp_sent) chTxt += ' · WhatsApp-Sofortmeldung zugestellt';
        document.getElementById('wpResChannels').textContent = chTxt;
        var pdfBtn = document.getElementById('wpResPdfBtn');
        if (pdfBtn && res.pdf_url) pdfBtn.href = res.pdf_url;
        var waBox = document.getElementById('wpResWaPreview');
        if (waBox) waBox.textContent = wpStripEmojisForDom(res.whatsapp_preview_text || '');
        document.getElementById('wpSuccessBox').classList.add('visible');
      })
      .catch(function() {
        if (btn) btn.disabled = false;
        if (btnTxt) btnTxt.textContent = '1-Seiten-Dossier & Anfrage senden';
        if (errBox) {
          errBox.textContent = 'Netzwerkfehler bei der Übermittlung. Bitte schreibe direkt an info@fcattiswil.ch.';
          errBox.style.display = 'block';
        }
      });
      return false;
    }
    (function() {
      try {
        var params = new URLSearchParams(window.location.search);
        var t = (params.get('thema') || '').toLowerCase();
        var map = {
          'probetraining': 'Probetraining / Neumitglied',
          'sponsoring': 'Sponsoring / 300er Club / Matchball',
          'clubhaus': 'Clubhaus Lindenrain mieten / Anlässe',
          'spielbetrieb': 'Spielbetrieb / Turniere / Schiedsrichter',
          'mitgliedschaft': 'Mitgliedschaft / Mutation / Vereinsartikel',
          'allgemein': 'Allgemeine Vereinsanfrage / Vorstand'
        };
        if (map[t]) {
          wpSelectFcaTopic(map[t]);
        }
      } catch(err) {}
    })();
  </script>
"""
    return render_shell(
        filename="kontakt.html",
        page_title="Smart-Anfrage, Probetraining, Clubhaus & Sponsoring — FC Attiswil",
        active_nav="kontakt",
        body_html=body,
        extra_css=KONTAKT_EXTRA_CSS,
    )

# ---------------------------------------------------------------------------
# 6. JSON CONFIG FILES (COMPANY.JSON, CONFIG.JSON, SITE.JSON)
# ---------------------------------------------------------------------------
def write_json_configs() -> None:
    company_data = {
        "slug": "preview-fcattiswil",
        "client_slug": "fcattiswil",
        "company_name": "Fussballclub Attiswil",
        "short_name": "FC Attiswil",
        "founded": "16. Februar 1971",
        "sofv_club_number": "1880",
        "certification": "SFV Quality Club (zertifiziert am 20. Juni 2026)",
        "address": {
            "facility": "Sportanlage Lindenrain",
            "street": "Sportplatzweg 1",
            "zip": "4536",
            "city": "Attiswil",
            "canton": "BE / SOFV",
            "country": "CH",
        },
        "contact": {
            "email": "info@fcattiswil.ch",
            "sponsoring_email": "sponsoring@fcattiswil.ch",
            "club300_email": "300erClub@fcattiswil.ch",
            "fairplay_email": "fairplay@fcattiswil.ch",
            "phone": "+41 79 661 66 12",
            "website": "https://www.fcattiswil.ch",
            "instagram": "https://www.instagram.com/fc_attiswil/",
            "facebook": "https://www.facebook.com/FCAttiswil",
        },
        "board": [
            {"role": "Präsident", "name": "Konrad Schütz", "phone": "079 661 66 12", "email": "info@fcattiswil.ch"},
            {"role": "Vizepräsident / Anlässe & Vermietung Clubhaus", "name": "Philipp Singer", "phone": "079 304 44 56", "email": "info@fcattiswil.ch"},
            {"role": "Sekretärin & Datenschutz", "name": "Michelle Kurth", "phone": "", "email": "info@fcattiswil.ch"},
            {"role": "Sportchef & J+S Coach", "name": "Florian Bohner", "phone": "079 677 93 52", "email": "info@fcattiswil.ch"},
            {"role": "Verantwortliche Frauen & Juniorinnen", "name": "Celine Lemp", "phone": "079 137 82 38", "email": "info@fcattiswil.ch"},
            {"role": "Verantwortlicher Junioren", "name": "Levi Meyer", "phone": "079 475 75 80", "email": "info@fcattiswil.ch"},
            {"role": "Kassier", "name": "Jörg Scheidegger", "phone": "032 637 21 76", "email": "info@fcattiswil.ch"},
            {"role": "Stv. Kassier", "name": "Sarah Probst", "phone": "079 535 83 48", "email": "info@fcattiswil.ch"},
            {"role": "Infrastruktur", "name": "Remo Brudermann", "phone": "079 533 09 81", "email": "info@fcattiswil.ch"},
            {"role": "Marketing / Sponsoring & Vereinsartikel", "name": "Raphaela Lüscher", "phone": "079 453 88 60", "email": "sponsoring@fcattiswil.ch"},
        ],
        "teams_total": 14,
        "sponsors_total": 23,
    }
    config_data = {
        "slug": "preview-fcattiswil",
        "client_slug": "fcattiswil",
        "mode": "v2-blueprint",
        "tokens": {
            "color_primary": "#C81E1E",
            "color_secondary": "#0F172A",
            "color_accent": "#F59E0B",
            "font_heading": "Montserrat",
            "font_body": "Inter",
        },
        "pages": ["index.html", "herren-1.html", "kontakt.html"],
    }
    site_data = {
        "meta": {
            "slug": "preview-fcattiswil",
            "client_slug": "fcattiswil",
            "company": "FC Attiswil",
            "version": "2.0.0",
        },
        "sections": {
            "hero": True,
            "sponsoren": True,
            "seiten-uebersicht": True,
            "vorschau-hinweis": True,
            "beispiel-team-detail": True,
            "alle-teams-matrix": True,
            "kontakt-zentrale": True,
            "footer": True,
        },
        "slots": {},
    }
    (SITE_DIR / "company.json").write_text(json.dumps(company_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (SITE_DIR / "config.json").write_text(json.dumps(config_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (SITE_DIR / "site.json").write_text(json.dumps(site_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def main() -> None:
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    write_json_configs()
    (SITE_DIR / "index.html").write_text(build_index_html(), encoding="utf-8")
    (SITE_DIR / "herren-1.html").write_text(build_herren1_html(), encoding="utf-8")
    (SITE_DIR / "kontakt.html").write_text(build_kontakt_html(), encoding="utf-8")
    print("SUCCESS: Generated FC Attiswil V2 Showcase in", SITE_DIR)

if __name__ == "__main__":
    main()

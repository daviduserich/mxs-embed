#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator für die WebPilot-Referenz-Aufbereitung von holz-susi.ch (Holz-Susi GmbH · Susanne Schmid, Frick AG):
- Variante 1 (Vollversion): /home/brainuser/workspaces/mxs-embed/preview-holz-susi
  Live-URL: https://vorschau.magnet-xs.ch/holz-susi-vollversion/ (5 voll ausgebaute Seiten + Studio Cockpit v4.0)
- Variante 2 (Zeigeversion / Vorschau-Entwurf): /home/brainuser/workspaces/mxs-embed/preview-holz-susi-v2
  Live-URL: https://vorschau.magnet-xs.ch/holz-susi-v2/ (2 ausgearbeitete Beispiel-Seiten: Startseite inkl. Holzbau-Projektberater + 3-Schritte Smart-Anfrage,
  plus anschauliche Themenbereich-Vorschaukarten für die 3 weiteren Unterseiten).

Strikt nach:
- UI-LAYOUT-RULES.md (Canary: UI-LAYOUT-2026-V1, #UI-01, #UI-02, #UI-13, #UI-14, #UI-16 Evolution-Modus Light Lock S-27)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1, 0 Eszett, 100 % Schweizer Hochdeutsch: Zimmerin EFZ, Dachstock, Estrich, Kamin, Offerte)
- #SYS-01 (Kein oberer Versions-/Cockpit-Balken, 0 Hinweise auf Vollversion/Cockpit auf Kundenseiten)
"""

import json
import subprocess
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
V1_DIR = BASE_DIR / "preview-holz-susi"
V2_DIR = BASE_DIR / "preview-holz-susi-v2"

V1_DIR.mkdir(parents=True, exist_ok=True)
V2_DIR.mkdir(parents=True, exist_ok=True)

BEFORE_INVENTORY = {
    "source_url": "https://holz-susi.ch/",
    "crawled_at": "2026-11-09",
    "company_name": "Holz-Susi GmbH",
    "legal_entity": "Holz-Susi GmbH",
    "uid": "CHE-187.492.373",
    "claim": "Ihr Holzbau-Vorhaben ist meine Passion!",
    "subline": "Für private Bauherrinnen, Bauherren, Architektinnen, Architekten und Bauunternehmen im Fricktal und Kanton Aargau, persönliche Beratung, präzises Zimmerhandwerk EFZ und engagierte Bauleitung durch Susanne Schmid.",
    "address": {
        "street": "Wendelhof 424",
        "zip": "5070",
        "city": "Frick",
        "canton": "AG",
        "country": "Schweiz"
    },
    "contact": {
        "email": "info@holz-susi.ch",
        "phone_primary": "+41 77 521 96 97",
        "phone_display": "077 521 96 97",
        "hours": "Montag bis Freitag 07:00 – 12:00 Uhr | 13:00 – 17:30 Uhr"
    },
    "replaced_template_remnants": [
        "Removed 3 FunnelCockpit 'Lorem ipsum dolor sit amet' dummy testimonials ('Max Grallenbach', 'Yvone Lächelmaul')",
        "Removed English FunnelCockpit footer disclaimer: 'FACEBOOK TM is a trademark of FACEBOOK TM, Inc. Additionally, this site is NOT endorsed by FacebookTM in any way.'",
        "Consolidated duplicated desktop/mobile FunnelCockpit DOM blocks into a responsive Swiss architectural grid",
        "Replaced external page.funnelcockpit.com legal links with integrated Swiss Impressum (UID CHE-187.492.373) and revDSG privacy notice"
    ],
    "team": [
        {
            "name": "Susanne (Susi) Schmid",
            "role": "Inhaberin & Geschäftsführerin",
            "phone": "077 521 96 97",
            "phone_href": "tel:+41775219697",
            "image": "images/team-susi-schmid-portrait.png",
            "qualification": "Zimmerin EFZ · Projektleiterin · Bauleiterin · Kranführerin · Lehrlingsausbilderin",
            "bio": "Nach dem Abschluss als Landwirtin und fünf Jahren Praxiserfahrung auf dem Bau bei der GLB Aargau absolvierte Susi Schmid die Lehre als Zimmerin EFZ bei der PM Mangold AG in Ormalingen. Seit über 15 Jahren verbindet sie handwerkliche Präzision auf dem Dach mit strukturierter Projekt- und Bauleitung."
        },
        {
            "name": "Reto Huber",
            "role": "Netzwerk-Partner · Dachdecker",
            "phone": "077 521 96 97",
            "phone_href": "tel:+41775219697",
            "image": "images/team-reto-huber-dachdecker.png",
            "qualification": "Erfahrener Dachdecker im Partner-Netzwerk",
            "bio": "Tatkräftige Unterstützung bei Dacherneuerungen, Unterdächern, Ziegel- und Steildacharbeiten sowie Sanierungen im gesamten Fricktal."
        },
        {
            "name": "Michael Hürbin",
            "role": "Netzwerk-Partner · Holzbautechniker",
            "phone": "077 521 96 97",
            "phone_href": "tel:+41775219697",
            "image": "images/team-michael-huerbin-holzbautechniker.png",
            "qualification": "Holzbautechniker · Statik, Werkplanung & Konstruktion",
            "bio": "Fachpartner für anspruchsvolle Holzbauplanung, Dimensionierung, Tragwerks-Details und präzise Vorbereitung grösserer Umbau- und Dachstuhlprojekte."
        }
    ],
    "references": [
        {
            "title": "Dachsanierung Komplettprojekt",
            "category": "Dachsanierung",
            "scope": "Rückbau Kamin, 4 Dachfenster, thermische Sanierung & Innenausbau",
            "before_img": "images/ref-dachsanierung-komplett-vorher.png",
            "after_img": "images/ref-dachsanierung-komplett-nachher.png",
            "desc": "Umfassende Dachsanierung aus einer Hand: Rückbau des alten Kamins, Einbau von vier grossflächigen Dachfenstern, zeitgemässe thermische Dämmung und kompletter Innenausbau des Dachstocks."
        },
        {
            "title": "Ausbau Dachstock & Estrich",
            "category": "Dachstock",
            "scope": "Vom ungenutzten Dachraum zum hellen Wohnraum",
            "before_img": "images/ref-dachstock-ausbau-vorher.png",
            "after_img": "images/ref-dachstock-ausbau-nachher.png",
            "desc": "Sorgfältiger Ausbau des bestehenden Dachstocks und Erneuerung des Estrichs mit präzisen Holzverkleidungen, sauberer Dämmebene und spürbar mehr Wohnqualität."
        },
        {
            "title": "Sanierung Marderschaden am Dach",
            "category": "Marderschaden",
            "scope": "Instandsetzung Unterdach, Wärmedämmung & Marderschutz",
            "before_img": "images/ref-marderschaden-vorher.png",
            "after_img": "images/ref-marderschaden-nachher.png",
            "desc": "Fachgerechte Behebung von Marderschäden an Unterdach und Wärmedämmung inklusive dauerhafter konstruktiver Verschluss-Lösung zum Schutz der Gebäudehülle."
        },
        {
            "title": "Fassadenverschönerung mit Holzschalung",
            "category": "Holzfassade",
            "scope": "Witterungsbeständige Holzschalung & saubere Detailanschlüsse",
            "before_img": "images/ref-fassade-holzschalung-vorher.png",
            "after_img": "images/ref-fassade-holzschalung-nachher.png",
            "desc": "Optische und konstruktive Aufwertung der Fassade mit einer natürlichen, langlebigen Holzschalung, präzise geplant und montiert für jahrzehntelangen Wetterschutz."
        },
        {
            "title": "Rückbau Firstfenster & neue Dachfenster",
            "category": "Dachfenster",
            "scope": "Ersatz alter Firstverglasung durch energieeffiziente Dachfenster",
            "before_img": "images/ref-firstfenster-dachfenster-vorher.png",
            "after_img": "images/ref-firstfenster-dachfenster-nachher.png",
            "desc": "Geordneter Rückbau einer sanierungsbedürftigen Firstfenster-Konstruktion und Einbau einer neuen, energieeffizienten Dachfenster-Lösung mit optimalem Tageslichteinfall."
        },
        {
            "title": "Terrassenrost, Pergola & Sitzbank",
            "category": "Terrassenbau",
            "scope": "Massgeschneiderter Terrassenrost, Pergola-Erneuerung & Holzsitzbank",
            "highlight": "Vorher/Nachher",
            "before_img": "images/ref-terrassenrost-vorher.jpg",
            "after_img": "images/ref-terrassenrost-nachher.jpg",
            "desc": "Erneuerung verwitterter Terrassenroste, Pergola-Konstruktionen und Sitzbänke im Aussenbereich für erweiterten Wohnkomfort und langlebige Ästhetik."
        },
        {
            "title": "Blindboden für Umbau & neuer Laminatboden",
            "category": "Bodenaufbau",
            "scope": "Ersatz alter Teppichböden, Blindboden-Aufbau & Laminatverlegung",
            "highlight": "Vorher/Nachher",
            "before_img": "images/ref-blindboden-umbau-vorher.png",
            "after_img": "images/ref-laminat-boden-nachher.png",
            "desc": "Sorgfältiger Rückbau abgenutzter Bodenbeläge, Ausgleich über einen tragfähigen Blindboden und Verlegung eines pflegeleichten, warmen Laminatbodens."
        },
        {
            "title": "Dachstühle von der Planung bis zur Montage",
            "category": "Dachstühle",
            "scope": "Abbund, Kranmontage & Aufrichte im Fricktaler Partnerverbund",
            "highlight": "Vorher/Nachher",
            "before_img": "images/ref-dachstuhl-montage-01.png",
            "after_img": "images/ref-dachstuhl-montage-02.png",
            "desc": "Realisierung kompletter Dachstuhl-Konstruktionen von der Werkplanung bis zur Aufrichte in Zusammenarbeit mit Mangold Holzbau GmbH, Dionys Soder Holzbau und Rebmann AG."
        }
    ],
    "faqs": [
        {
            "q": "Kann ich als private Bauherrin oder privater Bauherr selbst aktiv an meinem Holzprojekt mitarbeiten?",
            "a": "Ja, sehr gerne! Bei der Holz-Susi GmbH ist Eigenleistung ausdrücklich willkommen. Wenn Sie beim Rückbau, beim Dämmen, beim Verlegen eines Bodens oder bei der Terrassenmontage selbst mit anpacken möchten, planen wir die Schritte so, dass wir Ihr Vorhaben sicher, fachgerecht und gemeinsam realisieren."
        },
        {
            "q": "Wie stemmt die Holz-Susi GmbH auch grössere Dachsanierungen oder Dachstühle?",
            "a": "Susanne Schmid ist nicht allein unterwegs: Dank eines eingespielten regionalen Netzwerks aus selbständigen Zimmerleuten, Dachdecker Reto Huber, Holzbautechniker Michael Hürbin sowie Partnerbetrieben wie der Mangold Holzbau GmbH, Fricktal Zimmerei und Gebr. Schmid AG werden auch grössere Dach- und Umbauprojekte schlagkräftig umgesetzt."
        },
        {
            "q": "Welche Unterstützung bietet Susi Schmid für Architekturbüros und Bauunternehmen an?",
            "a": "Architektinnen und Architekten unterstützt Susi Schmid von der Holzbauplanung und Detailausarbeitung bis zur Terminplanung und Bauführung vor Ort. Bauunternehmen und Zimmereien buchen sie zudem flexibel als erfahrene Zimmerin EFZ, Vorarbeiterin, Kranführerin oder Projektleiterin für Renovationen und Montageeinsätze."
        },
        {
            "q": "Übernehmen Sie auch den Wechsel einzelner Dachfenster oder kleinere Reparaturen wie Marderschäden?",
            "a": "Selbstverständlich. Ob der 1:1-Austausch eines alten Dachfensters für bessere Wärmedämmung, die Sanierung eines Marderschadens im Unterdach, ein neuer Blindboden im Umbau oder eine erneuerte Sitzbank und Pergola: Jedes Anliegen wird mit derselben Sorgfalt und Lösungsorientierung ausgeführt."
        },
        {
            "q": "In welcher Region ist die Holz-Susi GmbH tätig?",
            "a": "Vom Standort auf dem Wendelhof 424 in 5070 Frick aus betreut die Holz-Susi GmbH Kundinnen und Kunden im gesamten Fricktal, im Kanton Aargau sowie in den angrenzenden Regionen Basel-Landschaft, Solothurn und Nordwestschweiz."
        },
        {
            "q": "Was hat es mit der «Bluescht-Beiz» auf dem Wendelhof in Frick auf sich?",
            "a": "Jedes Jahr im April, wenn rund um den Wendelhof in Frick die Kirschbäume blühen, öffnen Susi Schmid und das Wendelhof-Team für einen Monat die gemütliche «Bluescht-Beiz» direkt am Fricktaler Chriesiwäg im Jurapark Aargau. Sie ist ein beliebter Treffpunkt für Wanderfreunde, Familien und Geniesser."
        }
    ]
}

(V1_DIR / "before.json").write_text(json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False), encoding="utf-8")
(V2_DIR / "before.json").write_text(json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False), encoding="utf-8")

for target_dir in (V1_DIR, V2_DIR):
    (target_dir / "company.json").write_text(json.dumps({
        "company_name": "Holz-Susi GmbH",
        "legal_entity": "Holz-Susi GmbH",
        "uid": "CHE-187.492.373",
        "city": "Frick",
        "canton": "AG",
        "street": "Wendelhof 424",
        "zip": "5070",
        "phone": "+41 77 521 96 97",
        "email": "info@holz-susi.ch",
        "website": "https://holz-susi.ch/",
        "partner_id": "david",
        "partner_name": "David Hügli (Magnet XS)",
        "design_mode": "evolution"
    }, indent=2, ensure_ascii=False), encoding="utf-8")

v1_config = {
    "company_name": "Holz-Susi GmbH · Frick (AG)",
    "slug": "preview-holz-susi",
    "public_slug": "holz-susi-vollversion",
    "cockpit_token": "holzsusi2026",
    "template": "timber-craft-kmu-v1",
    "partner_id": "david",
    "pages": ["index.html", "leistungen.html", "referenzen.html", "ueber-uns.html", "kontakt.html"]
}
(V1_DIR / "config.json").write_text(json.dumps(v1_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V1_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-holz-susi",
    "public_slug": "holz-susi-vollversion",
    "token": "holzsusi2026",
    "name": "Holz-Susi GmbH · Zimmerei, Holzbau, Dachsanierung & Bauleitung Frick (Vollversion)",
    "Updated": "2026-11-09",
    "PagesCount": 5,
    "ReferencesCount": 8,
    "TeamCount": 3
}, indent=2, ensure_ascii=False), encoding="utf-8")

v2_config = dict(v1_config)
v2_config.update({
    "company_name": "Holz-Susi GmbH (Zeigeversion / Vorschau-Entwurf)",
    "slug": "preview-holz-susi-v2",
    "public_slug": "holz-susi-v2",
    "cockpit_token": "holzsusi2026",
    "template": "timber-craft-kmu-preview-v2",
    "pages": ["index.html", "kontakt.html"]
})
(V2_DIR / "config.json").write_text(json.dumps(v2_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V2_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-holz-susi-v2",
    "public_slug": "holz-susi-v2",
    "token": "holzsusi2026",
    "name": "Holz-Susi GmbH (Zeigeversion / Vorschau-Entwurf)",
    "Updated": "2026-11-09",
    "PagesCount": 2,
    "ReferencesCount": 8,
    "TeamCount": 3
}, indent=2, ensure_ascii=False), encoding="utf-8")

print("Wrote before.json, company.json, config.json, site.json for V1 and V2.")

SHARED_CSS = """
    :root {
      --charcoal: #2B1E11;
      --charcoal-deep: #1E140A;
      --charcoal-mid: #4A3522;
      --gold: #AF6600;
      --gold-hover: #8F5300;
      --gold-dark: #8F5300;
      --gold-soft: #FDF3E6;
      --gold-border: #E8CBA5;
      --crimson: #AF6600;
      --crimson-soft: #FDF3E6;
      --green: #15803D;
      --green-soft: #DCFCE7;
      --bg-page: #FEF9F5;
      --bg-card: #FFFFFF;
      --bg-Warm: #F8EEE5;
      --text-main: #1E140A;
      --text-body: #3A2918;
      --text-muted: #5C442B;
      --border-light: #EBDCCF;
      --border-strong: #D8C2AE;
      --radius-sm: 4px;
      --radius-md: 8px;
      --shadow-sm: 0 2px 10px rgba(30, 20, 10, 0.05);
      --shadow-md: 0 12px 30px rgba(30, 20, 10, 0.08);
      --shadow-lg: 0 20px 44px rgba(30, 20, 10, 0.12);
      --container: 1180px;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    ::selection {
      background-color: rgba(175, 102, 0, 0.18);
      color: #1E140A;
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

    /* Freistehende Marken-Kicker (#UI-01: Lexend Bold, 0 JetBrains Mono, 0 //) */
    .section-kicker {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-family: 'Lexend', sans-serif;
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--gold-dark);
      background: transparent !important;
      border: none !important;
      padding: 0 !important;
      box-shadow: none !important;
      margin-bottom: 12px;
    }
    .section-kicker.kicker-light {
      color: var(--gold-dark);
    }

    h1, h2, h3, h4 {
      font-family: 'Lexend', sans-serif;
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
      font-weight: 700;
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

    /* Sub-Topbar (5070 Frick AG & Direktkontakt Susanne Schmid) */
    .top-bar {
      background-color: #F8EEE5;
      color: #3A2918;
      font-size: 0.78rem;
      padding: 8px 0;
      border-bottom: 1px solid var(--border-light);
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
      background-color: #FDF3E6;
      color: #8F5300;
      border: 1px solid #E8CBA5;
      font-family: 'Lexend', sans-serif;
      font-size: 0.71rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
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
      color: #1E140A;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-height: 32px;
      padding: 5px 8px;
    }
    .top-bar-links a:hover {
      color: #AF6600;
    }

    /* Sticky Main Header (#UI-02: 1-Zeilen-Navigations-Gesetz) */
    .site-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background-color: rgba(254, 249, 245, 0.97);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border-light);
      box-shadow: 0 2px 12px rgba(30, 20, 10, 0.05);
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
      gap: 10px;
      flex-shrink: 0;
      min-height: 44px;
      padding: 4px 0;
    }
    .brand-logo {
      width: 50px;
      height: 50px;
      object-fit: contain;
      flex-shrink: 0;
      border-radius: var(--radius-sm);
    }
    .brand-text {
      display: flex;
      flex-direction: column;
      border-left: 1px solid var(--border-strong);
      padding-left: 10px;
    }
    .brand-name {
      font-family: 'Lexend', sans-serif;
      font-size: 0.86rem;
      font-weight: 700;
      color: var(--charcoal-deep);
      line-height: 1.15;
      white-space: nowrap;
    }
    .brand-sub {
      font-size: 0.68rem;
      font-weight: 700;
      color: var(--gold-dark);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-top: 2px;
      white-space: nowrap;
    }

    .main-nav {
      display: flex;
      align-items: center;
      gap: 24px;
      flex-wrap: nowrap;
      white-space: nowrap;
    }
    .nav-link {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'Lexend', sans-serif;
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-body);
      padding: 6px 2px;
      min-height: 36px;
      border-radius: 0;
      border: none;
      border-bottom: 2px solid transparent;
      background: transparent;
      white-space: nowrap;
      cursor: pointer;
    }
    .nav-link:hover,
    .nav-link.active {
      color: #8F5300;
      background: transparent;
      border-bottom-color: #AF6600;
    }
    .nav-link-preview {
      color: var(--text-muted);
      background: transparent;
      border: none;
      border-bottom: 2px dashed rgba(175, 102, 0, 0.42);
      font-size: 0.86rem;
    }
    .nav-link-preview:hover {
      color: #8F5300;
      background: transparent;
      border-bottom-color: #AF6600;
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
      font-family: 'Lexend', sans-serif;
      font-size: 0.9rem;
      font-weight: 600;
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
      background-color: #AF6600;
      color: #FFFFFF;
      border-color: #AF6600;
      font-weight: 600;
    }
    .btn-cta-gold:hover {
      background-color: #8F5300;
      color: #FFFFFF;
      border-color: #8F5300;
      transform: translateY(-1px);
    }
    .btn-cta-primary {
      background-color: #AF6600;
      color: #FFFFFF;
      border-color: #AF6600;
    }
    .btn-cta-primary:hover {
      background-color: #8F5300;
      color: #FFFFFF;
      border-color: #8F5300;
    }
    .btn-cta-outline {
      background-color: #FFFFFF;
      color: #1E140A;
      border-color: var(--border-strong);
    }
    .btn-cta-outline:hover {
      border-color: #AF6600;
      color: #8F5300;
      background-color: var(--gold-soft);
    }
    .btn-cta-outline-light {
      background-color: #FFFFFF;
      color: #1E140A;
      border-color: rgba(175, 102, 0, 0.38);
    }
    .btn-cta-outline-light:hover {
      background-color: #FDF3E6;
      color: #8F5300;
      border-color: #AF6600;
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
      color: #1E140A;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }
    .mobile-drawer {
      display: none;
      flex-direction: column;
      gap: 8px;
      padding: 16px 24px 22px;
      background-color: #FEF9F5;
      border-top: 1px solid var(--border-light);
    }
    .mobile-drawer.open {
      display: flex;
    }
    .mobile-drawer a,
    .mobile-drawer button.mobile-nav-btn {
      font-family: 'Lexend', sans-serif;
      font-size: 0.92rem;
      font-weight: 600;
      color: #1E140A;
      padding: 12px 14px;
      min-height: 44px;
      border-radius: var(--radius-sm);
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      text-align: left;
      width: 100%;
      cursor: pointer;
    }
    .mobile-drawer button.mobile-nav-btn {
      color: #8F5300;
      border-style: dashed;
      border-color: rgba(175, 102, 0, 0.45);
    }

    /* Hero Section: Hell, warm & handwerklich klar (#UI-16 Evolution, S-27 Light Lock & #UI-02 Bottom-Edge Baseline Lock) */
    .hero-section {
      background: linear-gradient(135deg, #FFFFFF 0%, #FEF9F5 55%, #F8EEE5 100%);
      background-color: #FEF9F5;
      color: #1E140A;
      padding: 72px 0 84px;
      border-bottom: 1px solid var(--border-light);
      overflow: hidden;
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1.12fr 0.88fr;
      gap: 44px;
      align-items: stretch;
    }
    .hero-grid > div:first-child {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .hero-title {
      font-size: clamp(2.1rem, 3.6vw, 3.1rem);
      font-weight: 700;
      color: #1E140A;
      line-height: 1.14;
      margin-bottom: 18px;
    }
    .hero-title span {
      color: #AF6600;
    }
    .hero-lead {
      font-size: 1.04rem;
      color: #3A2918;
      line-height: 1.66;
      margin-bottom: 26px;
    }
    .hero-actions {
      display: flex;
      flex-wrap: nowrap;
      gap: 12px;
      align-items: center;
      margin-bottom: 28px;
    }
    .hero-actions:last-child,
    .hero-badges:last-child {
      margin-top: auto;
      margin-bottom: 0;
    }
    .hero-actions .btn-cta {
      padding: 11px 16px;
      font-size: 0.86rem;
      white-space: nowrap;
    }
    .hero-badges {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
    }
    .hero-badge-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-left: 3px solid #AF6600;
      border-radius: var(--radius-sm);
      padding: 10px 14px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      gap: 2px;
      box-shadow: var(--shadow-sm);
    }
    .hero-badge-val {
      font-family: 'Lexend', sans-serif;
      font-size: 0.9rem;
      font-weight: 700;
      color: #8F5300;
    }
    .hero-badge-lbl {
      font-size: 0.78rem;
      color: #3A2918;
      line-height: 1.35;
    }

    .hero-media-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }
    .hero-media-card img {
      width: 100%;
      height: 260px;
      min-height: 260px;
      flex: 1 1 auto;
      object-fit: cover;
      object-position: center top;
    }
    .hero-media-caption {
      padding: 16px 20px;
      background-color: #F8EEE5;
      border-top: 1px solid var(--border-light);
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
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      align-items: stretch;
    }
    .grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      align-items: stretch;
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
      border-top: 4px solid var(--gold);
    }
    .content-card.card-dark {
      background: linear-gradient(135deg, #FFFFFF 0%, #FDF3E6 100%);
      background-color: #FDF3E6;
      color: #1E140A;
      border-color: #E8CBA5;
      border-top: 4px solid #AF6600;
    }
    .content-card.card-dark h3 {
      color: #1E140A;
    }

    .card-badge-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      flex-wrap: nowrap;
      margin-bottom: 10px;
    }
    .meta-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'Lexend', sans-serif;
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      padding: 4px 9px;
      border-radius: var(--radius-sm);
      background-color: var(--gold-soft);
      color: var(--gold-dark);
      border: 1px solid var(--gold-border);
    }
    .icon-box {
      width: 40px;
      height: 40px;
      border-radius: var(--radius-sm);
      background-color: #FDF3E6;
      color: #AF6600;
      border: 1px solid #E8CBA5;
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
      color: var(--gold);
      flex-shrink: 0;
      margin-top: 3px;
    }

    /* Pillar Media Cards */
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
      height: 215px;
      overflow: hidden;
      background-color: var(--charcoal);
      position: relative;
    }
    .pillar-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center;
    }
    .pillar-body {
      padding: 24px 26px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex: 1;
      gap: 16px;
    }

    /* Founder / Team Cards */
    .founder-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-md);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }
    .founder-top {
      display: grid;
      grid-template-columns: 180px 1fr;
      gap: 22px;
      padding: 26px 26px 0;
      align-items: start;
    }
    .founder-portrait {
      width: 100%;
      height: 180px;
      object-fit: cover;
      object-position: center top;
      border-radius: var(--radius-md);
      border: 2px solid var(--gold);
    }
    .founder-body {
      padding: 20px 26px 26px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex: 1;
      gap: 16px;
    }

    /* Interactive Holzbau Project Advisor Styles */
    .calc-option-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-bottom: 18px;
      align-items: stretch;
    }
    .calc-option-btn {
      background-color: var(--bg-page);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-sm);
      padding: 12px;
      text-align: left;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      gap: 4px;
      font-family: inherit;
      min-height: 74px;
      transition: all 0.16s ease;
    }
    .calc-option-btn:hover {
      border-color: var(--gold);
      background-color: #FFFFFF;
    }
    .calc-option-btn.active {
      border: 2px solid var(--gold);
      background-color: var(--gold-soft);
    }
    .calc-opt-title {
      font-family: 'Lexend', sans-serif;
      font-size: 0.81rem;
      font-weight: 700;
      color: var(--charcoal-deep);
    }
    .calc-opt-sub {
      font-size: 0.75rem;
      color: var(--text-body);
      line-height: 1.35;
    }
    .calc-kpi-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin: 16px 0;
    }
    .calc-kpi-box {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-left: 3px solid var(--gold);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
    }
    .calc-kpi-val {
      font-family: 'Lexend', sans-serif;
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--gold-dark);
    }
    .calc-kpi-lbl {
      font-size: 0.78rem;
      color: var(--text-body);
      margin-top: 2px;
    }

    /* V2 Vorschau-Entwurf (Zeigeversion) Spezifische Styles (#UI-03 Kunden-Sprache) */
    .preview-scope-section {
      background-color: #F8EEE5;
      border-top: 2px dashed rgba(175, 102, 0, 0.38);
      border-bottom: 2px dashed rgba(175, 102, 0, 0.38);
      padding: 76px 0 88px;
    }
    .preview-scope-banner {
      background-color: #FFFFFF;
      color: #1E140A;
      border: 2px dashed #AF6600;
      border-radius: var(--radius-md);
      padding: 28px 30px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-md);
    }
    .preview-module-card {
      background-color: #FFFFFF;
      border: 2px dashed #AF6600;
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
      font-family: 'Lexend', sans-serif;
      font-size: 0.71rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
    }

    /* Footer */
    .site-footer {
      background-color: #F8EEE5;
      color: #1E140A;
      padding: 68px 0 36px;
      border-top: 3px solid #AF6600;
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 1.3fr 1fr 1fr 1.1fr;
      gap: 36px;
      padding-bottom: 42px;
      border-bottom: 1px solid var(--border-strong);
    }
    .footer-title {
      font-family: 'Lexend', sans-serif;
      font-size: 0.9rem;
      font-weight: 700;
      color: #1E140A;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 16px;
    }
    .footer-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .footer-list a,
    .footer-list button {
      color: #3A2918;
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
      color: #AF6600;
    }
    .footer-bottom {
      padding-top: 26px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      font-size: 0.82rem;
      color: #3A2918;
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
      background-color: rgba(30, 20, 10, 0.76);
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
      color: var(--charcoal-deep);
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
      color: var(--gold);
      flex-shrink: 0;
      margin-top: 2px;
    }

    /* 3-Schritte Smart-Anfrage Assistent (kontakt.html) */
    .contact-layout {
      display: grid;
      grid-template-columns: 0.88fr 1.12fr;
      gap: 38px;
      align-items: stretch;
    }
    .contact-info-panel {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 28px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
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
      border-left: 3px solid var(--gold);
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
    }
    .contact-direct-role {
      font-family: 'Lexend', sans-serif;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--gold-dark);
      letter-spacing: 0.04em;
    }
    .contact-direct-person {
      font-weight: 700;
      color: var(--charcoal-deep);
      margin-top: 2px;
    }
    .contact-direct-links {
      color: var(--text-body);
      font-size: 0.82rem;
      margin-top: 2px;
    }

    .wizard-card {
      background-color: #FFFFFF;
      border: 2px solid var(--charcoal-deep);
      border-radius: var(--radius-md);
      padding: 30px;
      box-shadow: var(--shadow-md);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
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
      font-family: 'Lexend', sans-serif;
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--text-muted);
      text-align: center;
    }
    .wp-step-pill.active {
      background-color: #AF6600;
      color: #FFFFFF;
    }
    .wp-step-pill.done {
      background-color: var(--green-soft);
      color: #166534;
    }
    .wp-step-num {
      width: 22px;
      height: 22px;
      border-radius: var(--radius-sm);
      background-color: rgba(255, 255, 255, 0.22);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.74rem;
      font-weight: 700;
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
      justify-content: flex-start;
      gap: 8px;
      transition: all 0.18s ease;
      font-family: inherit;
      min-height: 92px;
    }
    .wp-role-tile:hover {
      border-color: var(--gold);
      background-color: #FFFFFF;
    }
    .wp-role-tile.selected {
      border: 2px solid var(--gold);
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
      background-color: #FDF3E6;
      color: #AF6600;
      border: 1px solid #E8CBA5;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .wp-role-title {
      font-family: 'Lexend', sans-serif;
      font-size: 0.86rem;
      font-weight: 700;
      color: var(--charcoal-deep);
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
      font-family: 'Lexend', sans-serif;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--charcoal-deep);
      line-height: 1.3;
    }
    .form-input,
    .form-textarea {
      width: 100%;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 1rem;
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
      border-color: var(--gold);
      box-shadow: 0 0 0 3px rgba(175, 102, 0, 0.16);
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
      font-family: 'Lexend', sans-serif;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--charcoal-deep);
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
      background-color: var(--charcoal-deep);
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
      border-left: 4px solid var(--gold);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      font-size: 0.8rem;
      color: #5C3500;
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

    @media (max-width: 1080px) {
      .hero-grid,
      .contact-layout,
      .footer-grid {
        grid-template-columns: 1fr;
      }
      .grid-4 {
        grid-template-columns: repeat(2, 1fr);
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
      .grid-3,
      .grid-4,
      .hero-badges,
      .wp-role-grid,
      .form-grid-2,
      .wp-stepper,
      .founder-top,
      .calc-option-grid,
      .calc-kpi-grid {
        grid-template-columns: 1fr;
      }
      .header-actions .btn-cta {
        display: none;
      }
      .hero-actions {
        flex-wrap: wrap;
      }
      .hero-actions .btn-cta {
        white-space: normal;
        width: 100%;
      }
      .brand-link {
        flex-shrink: 1;
        min-width: 0;
        min-height: 40px;
        gap: 8px;
      }
      .brand-logo {
        width: 38px;
        height: 38px;
      }
      .brand-text {
        min-width: 0;
      }
      .brand-name {
        font-size: 0.78rem;
      }
      .brand-sub {
        font-size: 0.62rem;
        line-height: 1.2;
      }
      .hero-media-card img {
        height: 250px;
      }
      .founder-portrait {
        height: 230px;
      }
      .wizard-card,
      .content-card {
        padding: 20px;
      }
    }

    /* WEBPILOT SAISON-SEKTIONEN & AKTIONS-STOERER (v1.0) */
    section[data-wp-hidden="true"]:not(.wp-cockpit-peek),
    .wp-seasonal-hidden-link,
    [data-wp-stoerer][ data-wp-stoerer-active="false" ],
    [data-wp-stoerer].wp-seasonal-hidden-stoerer {
      display: none !important;
    }
    section.wp-cockpit-peek {
      display: block !important;
      outline: 2px dashed #D97706 !important;
      outline-offset: -4px;
      position: relative;
    }
    .wp-cockpit-peek-banner {
      background-color: #78350F;
      background-image: linear-gradient(135deg, #92400E 0%, #451A03 100%);
      color: #FFFFFF;
      padding: 10px 18px;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 0.84rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      border-bottom: 2px dashed #F59E0B;
      text-align: center;
    }
    .wp-stoerer {
      font-family: 'Plus Jakarta Sans', sans-serif;
      text-decoration: none !important;
      color: #FFFFFF !important;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      cursor: pointer;
      box-sizing: border-box;
    }
    .wp-stoerer:hover {
      transform: translateY(-2px);
    }
    .wp-stoerer[data-wp-stoerer-theme="brand"] {
      background-color: #78350F;
      background-image: linear-gradient(135deg, #92400E 0%, #451A03 100%);
      border-color: #F59E0B;
      color: #FFFFFF !important;
    }
    .wp-stoerer[data-wp-stoerer-theme="nature"] {
      background-color: #14532D;
      background-image: linear-gradient(135deg, #166534 0%, #052E16 100%);
      border-color: #4ADE80;
      color: #FFFFFF !important;
    }
    .wp-stoerer[data-wp-stoerer-theme="gold"] {
      background-color: #713F12;
      background-image: linear-gradient(135deg, #854D0E 0%, #422006 100%);
      border-color: #FACC15;
      color: #FFFFFF !important;
    }
    .wp-stoerer[data-wp-stoerer-theme="obsidian"] {
      background-color: #1E293B;
      background-image: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
      border-color: #F59E0B;
      color: #FFFFFF !important;
    }
    @media (min-width: 1024px) {
      .wp-stoerer[data-wp-stoerer="seal"] {
        position: absolute;
        top: 14px;
        right: 14px;
        width: 144px;
        height: 144px;
        border-radius: 999px;
        border: 2px solid #F59E0B;
        box-shadow: 0 14px 30px rgba(20, 14, 8, 0.38), inset 0 0 0 3px rgba(255, 255, 255, 0.22);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 12px;
        z-index: 12;
      }
      .wp-stoerer[data-wp-stoerer="seal"]:hover {
        transform: scale(1.03);
      }
      .wp-stoerer[data-wp-stoerer="seal"] .wp-stoerer-seal-ring {
        position: absolute;
        inset: 5px;
        width: calc(100% - 10px);
        height: calc(100% - 10px);
        pointer-events: none;
        opacity: 0.55;
      }
      .wp-stoerer[data-wp-stoerer="seal"] .wp-stoerer-mobile-icon {
        display: none;
      }
      .wp-stoerer[data-wp-stoerer="seal"] .wp-stoerer-seal-content {
        transform: rotate(-8deg);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 2px;
        z-index: 2;
        max-width: 128px;
      }
    }
    @media (max-width: 1023px) {
      .wp-stoerer[data-wp-stoerer="seal"] {
        position: relative;
        width: 100%;
        border-radius: 8px;
        border: 1.5px solid #F59E0B;
        padding: 10px 12px;
        margin: 8px 0 4px 0;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        gap: 10px;
        box-shadow: 0 6px 18px rgba(20, 14, 8, 0.16);
      }
      .wp-stoerer[data-wp-stoerer="seal"] .wp-stoerer-seal-ring {
        display: none;
      }
      .wp-stoerer[data-wp-stoerer="seal"] .wp-stoerer-mobile-icon {
        width: 38px;
        height: 38px;
        min-width: 38px;
        border-radius: 999px;
        background-color: rgba(255, 255, 255, 0.14);
        border: 1.5px dashed rgba(254, 243, 199, 0.75);
        display: inline-flex;
        align-items: center;
        justify-content: center;
        transform: rotate(-8deg);
        color: #FDE68A;
      }
      .wp-stoerer[data-wp-stoerer="seal"] .wp-stoerer-seal-content {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        text-align: left;
        gap: 1px;
      }
    }
    .wp-stoerer[data-wp-stoerer="ribbon"] {
      position: relative;
      width: 100%;
      border-radius: 8px;
      border: 1.5px solid #F59E0B;
      padding: 10px 14px;
      margin: 8px 0 4px 0;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      box-shadow: 0 8px 20px rgba(20, 14, 8, 0.2);
    }
    .wp-stoerer[data-wp-stoerer="ribbon"] .wp-stoerer-seal-ring {
      display: none;
    }
    .wp-stoerer[data-wp-stoerer="ribbon"] .wp-stoerer-mobile-icon {
      width: 34px;
      height: 34px;
      min-width: 34px;
      border-radius: 4px;
      background-color: rgba(255, 255, 255, 0.14);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      transform: rotate(-6deg);
      color: #FDE68A;
    }
    .wp-stoerer[data-wp-stoerer="ribbon"] .wp-stoerer-seal-content {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 1px;
      flex: 1;
    }
    .wp-stoerer[data-wp-stoerer="bar"] {
      position: relative;
      width: 100%;
      border-radius: 8px;
      border: 1px solid #F59E0B;
      padding: 8px 12px;
      margin: 8px 0 4px 0;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }
    .wp-stoerer[data-wp-stoerer="bar"] .wp-stoerer-seal-ring,
    .wp-stoerer[data-wp-stoerer="bar"] .wp-stoerer-mobile-icon {
      display: none;
    }
    .wp-stoerer[data-wp-stoerer="bar"] .wp-stoerer-seal-content {
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
      align-items: baseline;
      gap: 8px;
      width: 100%;
      justify-content: space-between;
    }
    .wp-stoerer-line1 {
      font-size: 0.52rem;
      font-weight: 800;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #FDE68A !important;
      line-height: 1.15;
      white-space: nowrap;
    }
    .wp-stoerer-line2 {
      font-family: 'Lexend', sans-serif;
      font-size: 0.90rem;
      font-weight: 800;
      color: #FFFFFF !important;
      line-height: 1.14;
    }
    .wp-stoerer-line3 {
      font-size: 0.65rem;
      font-weight: 700;
      color: #FEF3C7 !important;
      line-height: 1.15;
    }
    @media (max-width: 1023px) {
      .wp-stoerer-line1 { font-size: 0.65rem; }
      .wp-stoerer-line2 { font-size: 0.94rem; }
      .wp-stoerer-line3 { font-size: 0.76rem; }
    }
    /* Bluescht-Beiz Öffnungszeiten & 5er-Galerie */
    .bluescht-hours-table {
      width: 100%;
      border-collapse: collapse;
      margin: 6px 0 10px 0;
      font-size: 0.80rem;
    }
    .bluescht-hours-table td {
      padding: 4px 0;
      border-bottom: 1px dashed var(--border-light);
      color: var(--text-body);
      vertical-align: top;
    }
    .bluescht-hours-table td:last-child {
      text-align: right;
      font-weight: 700;
      color: var(--text-dark);
      white-space: nowrap;
      padding-left: 8px;
    }
    .bluescht-gallery-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 14px;
      margin-top: 22px;
    }
    .bluescht-gallery-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: 8px;
      padding: 8px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      box-shadow: 0 4px 12px rgba(30, 20, 10, 0.04);
    }
    .bluescht-gallery-card img {
      width: 100%;
      height: 168px;
      object-fit: cover;
      object-position: center 35%;
      border-radius: 4px;
      display: block;
    }
    .bluescht-gallery-caption {
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--text-dark);
      text-align: center;
      padding: 2px 4px 4px 4px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    @media (max-width: 1100px) {
      .bluescht-gallery-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    @media (max-width: 768px) {
      .bluescht-gallery-grid {
        grid-template-columns: 1fr;
      }
      .bluescht-hours-table td:last-child {
        white-space: normal;
      }
    }
"""

SVG_CHECK = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>'
SVG_ARROW = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'
SVG_HOME = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'
SVG_HAMMER = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>'
SVG_LAYERS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>'
SVG_SHIELD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
SVG_AWARD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>'
SVG_USERS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
SVG_BUILDING = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"/><line x1="9" y1="22" x2="9" y2="18"/><line x1="15" y1="22" x2="15" y2="18"/><line x1="8" y1="6" x2="10" y2="6"/><line x1="14" y1="6" x2="16" y2="6"/><line x1="8" y1="10" x2="10" y2="10"/><line x1="14" y1="10" x2="16" y2="10"/><line x1="8" y1="14" x2="10" y2="14"/><line x1="14" y1="14" x2="16" y2="14"/></svg>'
SVG_MAP_PIN = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'
SVG_PHONE = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
SVG_MAIL = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'



def render_hero_stoerer() -> str:
    return """<a href="#bluescht-beiz" class="wp-stoerer" id="wpHeroStoerer" data-wp-stoerer="seal" data-wp-stoerer-active="true" data-wp-stoerer-theme="brand" data-wp-stoerer-target="#bluescht-beiz" aria-label="Saison-Highlight: Bluescht-Beiz auf dem Wendelhof">
          <svg class="wp-stoerer-seal-ring" viewBox="0 0 120 120" fill="none" aria-hidden="true">
            <circle cx="60" cy="60" r="56" stroke="#FDE68A" stroke-width="1.5" stroke-dasharray="4 3"/>
            <circle cx="60" cy="60" r="50" stroke="#FEF3C7" stroke-width="0.9" stroke-opacity="0.6"/>
          </svg>
          <span class="wp-stoerer-mobile-icon" aria-hidden="true">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          </span>
          <span class="wp-stoerer-seal-content">
            <span class="wp-stoerer-line1" data-wp-stoerer-line="1">FRÜHLINGS-HIGHLIGHT</span>
            <span class="wp-stoerer-line2" data-wp-stoerer-line="2">Bluescht-Beiz</span>
            <span class="wp-stoerer-line3" data-wp-stoerer-line="3">Ostern bis 1. Mai &darr;</span>
          </span>
        </a>"""


def render_bluescht_beiz_section() -> str:
    return f"""
  <!-- SAISON-SEKTION: BLUESCHT-BEIZ AUF DEM WENDELHOF (SCHLUMMERFÄHIG) -->
  <section class="section" id="bluescht-beiz" data-section="bluescht-beiz" data-wp-seasonal="true" data-wp-title="Bluescht-Beiz auf dem Wendelhof" data-wp-hidden="false" data-wp-visible-from="2026-04-03" data-wp-visible-until="2026-05-01" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="bluescht_kicker">SAISON-HIGHLIGHT IM APRIL · WENDELHOF 424 IN 5070 FRICK</div>
        <h2 class="section-title" data-slot="bluescht_title">Bluescht-Beiz auf dem Wendelhof</h2>
        <p class="section-desc" data-slot="bluescht_desc">
          Wenn im April rund um den Wendelhof in Frick die Kirschbäume in voller Blüte stehen, öffnet unsere gemütliche Bluescht-Beiz ihre Tore. Geniessen Sie hausgemachte Spezialitäten mitten in der blühenden Natur des Fricktals.
        </p>
      </div>

      <div class="grid-3">
        <!-- KARTE 1: KULINARISCHE HIGHLIGHTS -->
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Hof-Kulinarik &amp; Beizli</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 style="font-size:1.18rem;font-weight:700;margin-bottom:8px;">Kulinarische Highlights vom Hof</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Frisch vom Grill und aus unserer Hofbackstube für Ihre Pause unter blühenden Kirschbäumen:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Frisch vom Grill:</strong> Saftiger Bio-Rind-Burger, würzige Highland-Bratwurst oder feine vegane Gemüsespiesschen vom Grill.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Süsses &amp; Kaffi:</strong> Hausgemachtes Kuchenbuffet, erfrischender «Dessertschmous» und unser beliebter Bluescht-Kaffi.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Witterungs-Hinweis:</strong> Wir führen unser Beizli nur bei schönem Wetter durch (bei unsicherer Witterung geben wir hier auf der Webseite den aktuellen Stand bekannt).</span></div>
            </div>
          </div>
          <div style="display:flex;flex-direction:column;gap:8px;width:100%;">
            <a href="https://drive.google.com/file/d/13vfyev0uWNqJ13TI1522gCFmeiQNZruL/view" target="_blank" rel="noopener" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Speise- &amp; Getränkekarte (PDF)</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- KARTE 2: ÖFFNUNGSZEITEN APRIL BIS 1. MAI -->
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Saison 3. April bis 1. Mai</span>
              <span class="icon-box">{SVG_HOME}</span>
            </div>
            <h3 style="font-size:1.18rem;font-weight:700;margin-bottom:8px;">Öffnungszeiten April bis 1. Mai</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              An den Festtagen und Wochenenden mit Bewirtung &amp; Service, unter der Woche mit Selbstbedienung:
            </p>
            <table class="bluescht-hours-table" aria-label="Öffnungszeiten Bluescht-Beiz">
              <tbody>
                <tr><td>Karfreitag, 3.4.2026 (Service)</td><td>11:00 - 20:00 Uhr</td></tr>
                <tr><td>Karsamstag, 4.4.2026 (Service)</td><td>11:00 - 20:00 Uhr</td></tr>
                <tr><td>Ostersonntag, 5.4.2026 (Service)</td><td>11:00 - 20:00 Uhr</td></tr>
                <tr><td>Ostermontag, 6.4.2026 (Service)</td><td>11:00 - 17:00 Uhr</td></tr>
                <tr><td>Sa, 11.4. &amp; So, 12.4.2026 (Service)</td><td>Sa 11-20 / So 11-17 Uhr</td></tr>
                <tr><td>Sa, 18.4. &amp; So, 19.4.2026 (Service)</td><td>Sa 11-20 / So 11-17 Uhr</td></tr>
                <tr><td>Sa, 25.4. &amp; So, 26.4.2026 (Service)</td><td>Sa 11-20 / So 11-17 Uhr</td></tr>
                <tr><td>Freitag, 1.5.2026 (Tag der Arbeit)</td><td>11:00 - 20:00 Uhr</td></tr>
              </tbody>
            </table>
            <div class="check-list" style="margin-bottom:10px;">
              <div class="check-item">{SVG_CHECK} <span><strong>Di - Fr im April (bei schönem Wetter):</strong> Gemütliche <strong>Selbstbedienung (11:00 - 20:00 Uhr)</strong> für Wanderer und Ausflügler.</span></div>
            </div>
          </div>
          <div style="display:flex;flex-direction:column;gap:8px;width:100%;">
            <a href="tel:+41775219697" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Fragen zur Witterung: 077 521 96 97</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- KARTE 3: WANDER-TIPP CHRIESIWÄG & ANFAHRT -->
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Wanderroute &amp; Anreise</span>
              <span class="icon-box">{SVG_MAP_PIN}</span>
            </div>
            <h3 style="font-size:1.18rem;font-weight:700;margin-bottom:8px;">Chriesiwäg &amp; Anfahrt zum Hof</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Der Fricktaler Chriesiwäg führt direkt am Wendelhof vorbei. Zwei beschilderte Rundwege ab Bahnhof Frick:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Zwei Rundwege ab Bahnhof Frick:</strong> <strong>5 km (ca. 2 Std., kinderwagenfreundlich)</strong> oder <strong>9 km (ca. 4 Std.)</strong> durch das blühende Fricktal.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Wichtiger Hinweis für die Anreise mit dem Auto:</strong> Auf dem Wanderweg ab Frick gilt ein allgemeines Fahrverbot. Bitte fahren Sie über die <strong>Hauptstrasse und den Schützenweg</strong> zum Wendelhof (Parkplätze vor Ort vorhanden).</span></div>
            </div>
          </div>
          <div style="display:flex;flex-direction:column;gap:8px;width:100%;">
            <a href="https://jurapark-aargau.ch/chriesiwaeg?file=files/jurapark/pdf/Gratis%20Broschueren%20Shop/Flyer%20Fricktaler%20Chriesiw%C3%A4g.pdf&amp;cid=8151" target="_blank" rel="noopener" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Flyer Fricktaler Chriesiwäg (PDF)</span>
              {SVG_ARROW}
            </a>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;width:100%;">
              <a href="https://maps.app.goo.gl/h37zxUtheERgSe6W7" target="_blank" rel="noopener" class="btn-cta btn-cta-outline btn-sm" style="width:100%;padding:8px 10px;font-size:0.78rem;">
                <span>Wanderroute (Maps)</span>
              </a>
              <a href="https://maps.app.goo.gl/hXK4ytneBr7QT321A" target="_blank" rel="noopener" class="btn-cta btn-cta-outline btn-sm" style="width:100%;padding:8px 10px;font-size:0.78rem;">
                <span>Auto via Schützenweg</span>
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- 5 ORIGINAL-FOTOS IMPRESSIONEN-GALERIE -->
      <div class="bluescht-gallery-grid" data-ignore-card-anatomy="true">
        <div class="bluescht-gallery-card">
          <img src="images/bluescht-1.jpg" alt="Bluescht-Beiz auf dem Wendelhof in Frick während der Kirschblüte" width="320" height="168" decoding="async" data-slot="bluescht_img_1">
          <div class="bluescht-gallery-caption">Kirschblüte rund um den Wendelhof</div>
        </div>
        <div class="bluescht-gallery-card">
          <img src="images/bluescht-2.jpg" alt="Gemütliche Festbänke und Bewirtung in der Bluescht-Beiz Frick" width="320" height="168" decoding="async" data-slot="bluescht_img_2">
          <div class="bluescht-gallery-caption">Gemütliches Beizli auf dem Hof</div>
        </div>
        <div class="bluescht-gallery-card">
          <img src="images/bluescht-3.jpg" alt="Hausgemachte Spezialitäten und Kuchenbuffet auf dem Wendelhof" width="320" height="168" decoding="async" data-slot="bluescht_img_3">
          <div class="bluescht-gallery-caption">Feines vom Grill &amp; Hof-Kuchenbuffet</div>
        </div>
        <div class="bluescht-gallery-card">
          <img src="images/bluescht-4.jpg" alt="Ausblick vom Fricktaler Chriesiwäg beim Wendelhof in Frick" width="320" height="168" decoding="async" data-slot="bluescht_img_4">
          <div class="bluescht-gallery-caption">Direkt am Fricktaler Chriesiwäg</div>
        </div>
        <div class="bluescht-gallery-card">
          <img src="images/bluescht-5.jpg" alt="Frühlingsstimmung bei der Bluescht-Beiz der Familie Schmid in Frick" width="320" height="168" decoding="async" data-slot="bluescht_img_5">
          <div class="bluescht-gallery-caption">Treffpunkt für Wanderer &amp; Geniesser</div>
        </div>
      </div>
    </div>
  </section>
"""


def render_references_grid(limit: int = 6, is_v2: bool = False) -> str:
    cards = []
    for ref in BEFORE_INVENTORY["references"][:limit]:
        cta_html = (
            f'''<button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Vorher/Nachher: {ref['title']}', '{ref['category']} · {ref['scope']} · {ref.get('highlight', 'Vorher/Nachher')}', 'Susanne («Susi») Schmid (Zimmerin EFZ &amp; Bauleiterin)')">
              <span>Vorher/Nachher-Details ansehen</span>
              {SVG_ARROW}
            </button>'''
            if is_v2
            else f'''<a href="kontakt.html?thema=dach" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Ähnliches Projekt mit Susi besprechen</span>
              {SVG_ARROW}
            </a>'''
        )
        cards.append(f"""
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="{ref['after_img']}" alt="Holz-Susi GmbH Frick Vorher/Nachher-Projekt: {ref['title']}" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">{ref['category']}</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.76rem;font-weight:700;color:var(--gold-dark);">{ref.get('highlight', 'Vorher/Nachher')}</span>
              </div>
              <h3 style="font-size:1.2rem;font-weight:700;margin-bottom:6px;">{ref['title']}</h3>
              <p style="font-size:0.82rem;font-weight:700;color:var(--gold-dark);margin-bottom:10px;">{ref['scope']}</p>
              <p style="font-size:0.89rem;color:var(--text-body);margin-bottom:12px;">{ref['desc']}</p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span><strong>Ausführung:</strong> {ref['scope']}</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Mehrwert:</strong> {ref.get('highlight', 'Vorher/Nachher')}</span></div>
              </div>
            </div>
            {cta_html}
          </div>
        </div>""")
    grid_cls = "grid-3" if limit % 3 == 0 else "grid-2"
    return f'<div class="{grid_cls}">\n' + "\n".join(cards) + "\n      </div>"


def render_faqs_grid() -> str:
    cards = []
    for idx, f in enumerate(BEFORE_INVENTORY["faqs"]):
        cards.append(f"""
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Praxis-Antwort #{idx+1}</span>
              <span class="icon-box">{SVG_HAMMER}</span>
            </div>
            <h3 style="font-size:1.14rem;font-weight:700;margin-bottom:10px;">{f['q']}</h3>
            <p style="font-size:0.9rem;color:var(--text-body);line-height:1.62;">{f['a']}</p>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Persönlich mit Susi Schmid klären</span>
            {SVG_ARROW}
          </a>
        </div>""")
    return '<div class="grid-2">\n' + "\n".join(cards) + "\n      </div>"


def render_holz_advisor() -> str:
    return f"""
  <!-- INTERAKTIVER HOLZBAU- & RENOVATIONS-PROJEKTBERATER -->
  <section data-section="projektberater" id="projektberater" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="calc_kicker">INTERAKTIVER HOLZBAU- &amp; RENOVATIONS-BERATER · FRICKTAL &amp; KANTON AARGAU</div>
        <h2 class="section-title" data-slot="calc_title">Welches Holzbau- oder Renovationsprojekt planen Sie?</h2>
        <p class="section-desc" data-slot="calc_desc">
          Wählen Sie Ihre Rolle, Ihren Projektbereich und die gewünschte Zusammenarbeit (zum Beispiel mit aktiver Eigenleistung beim Umbau). Unser Projektberater zeigt Ihnen direkt das passende Vorgehen und eine realisierte Vorher/Nachher-Referenz der Holz-Susi GmbH:
        </p>
      </div>

      <div class="grid-2">
        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">In 15 Sekunden zusammenstellen</span>
              <span class="icon-box">{SVG_HAMMER}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:14px;">1. Wer sind Sie? (Auftraggeber-Rolle)</h3>
            <div class="calc-option-grid" id="susiCalcRoleGrid">
              <button type="button" class="calc-option-btn active" data-role="privat" onclick="susiSetCalc('role','privat')">
                <span class="calc-opt-title">Privatkunden</span>
                <span class="calc-opt-sub">Eigenheim, Umbau, Dach oder Terrasse</span>
              </button>
              <button type="button" class="calc-option-btn" data-role="architektur" onclick="susiSetCalc('role','architektur')">
                <span class="calc-opt-title">Architekturbüro</span>
                <span class="calc-opt-sub">Holzbauplanung, Statik &amp; Bauleitung</span>
              </button>
              <button type="button" class="calc-option-btn" data-role="bau" onclick="susiSetCalc('role','bau')">
                <span class="calc-opt-title">Bauunternehmen</span>
                <span class="calc-opt-sub">Zimmerin EFZ, Kranführerin &amp; Leitung</span>
              </button>
            </div>

            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:14px;">2. Gewünschter Leistungsbereich</h3>
            <div class="calc-option-grid" id="susiCalcScopeGrid">
              <button type="button" class="calc-option-btn active" data-scope="dach" onclick="susiSetCalc('scope','dach')">
                <span class="calc-opt-title">Dach &amp; Fenster</span>
                <span class="calc-opt-sub">Dachsanierung, Marderschaden, Lukarne</span>
              </button>
              <button type="button" class="calc-option-btn" data-scope="innen" onclick="susiSetCalc('scope','innen')">
                <span class="calc-opt-title">Innenausbau</span>
                <span class="calc-opt-sub">Dachstock, Täfer, Blindboden, Laminat</span>
              </button>
              <button type="button" class="calc-option-btn" data-scope="aussen" onclick="susiSetCalc('scope','aussen')">
                <span class="calc-opt-title">Aussenholz</span>
                <span class="calc-opt-sub">Pergola, Holzschalung, Planung &amp; Rückbau</span>
              </button>
            </div>

            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:14px;">3. Gewünschte Ausführungsart</h3>
            <div class="calc-option-grid" id="susiCalcModeGrid" style="margin-bottom:0;">
              <button type="button" class="calc-option-btn active" data-mode="komplett" onclick="susiSetCalc('mode','komplett')">
                <span class="calc-opt-title">Rundum-Service</span>
                <span class="calc-opt-sub">Komplett durch Holz-Susi &amp; Partner</span>
              </button>
              <button type="button" class="calc-option-btn" data-mode="mithilfe" onclick="susiSetCalc('mode','mithilfe')">
                <span class="calc-opt-title">Mit Eigenleistung</span>
                <span class="calc-opt-sub">Aktiv unter Fachanleitung mitanpacken</span>
              </button>
              <button type="button" class="calc-option-btn" data-mode="leitung" onclick="susiSetCalc('mode','leitung')">
                <span class="calc-opt-title">Koordination</span>
                <span class="calc-opt-sub">Projektsteuerung, Termine &amp; Kosten</span>
              </button>
            </div>
          </div>
          <div style="padding-top:14px;border-top:1px solid var(--border-light);font-size:0.82rem;color:var(--text-body);display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;">
            <span>Über 15 Jahre Baustellen-, Zimmerei- &amp; Projektleitungserfahrung</span>
            <strong style="color:var(--gold-dark);font-family:'Lexend',sans-serif;">Holz-Susi GmbH · 5070 Frick</strong>
          </div>
        </div>

        <div class="content-card card-dark">
          <div>
            <div class="card-badge-row">
              <span class="top-bar-badge" id="susiCalcRefBadge">REFERENZ-BEISPIEL: DACHSANIERUNG &amp; 4 DACHFENSTER</span>
              <span class="icon-box">{SVG_HOME}</span>
            </div>
            <h3 style="font-size:1.36rem;font-weight:700;margin-bottom:8px;" id="susiCalcHeadline">Dacherneuerung, Dachfenster &amp; energetische Sanierung</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;" id="susiCalcDesc">
              Susanne («Susi») Schmid begleitet Sie von der Vor-Ort-Aufnahme über die Offerte bis zur sauberen Ausführung. Bei grösseren Dachstühlen arbeiten wir Hand in Hand mit unserem eingespielten Fricktaler Partnernetzwerk.
            </p>

            <div class="calc-kpi-grid">
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="susiCalcLead">Susanne Schmid</div>
                <div class="calc-kpi-lbl">Zimmerin EFZ, Vorarbeiterin &amp; Bauleiterin</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="susiCalcModeOut">Komplett-Service</div>
                <div class="calc-kpi-lbl">Ausführungsmodell &amp; Zusammenarbeit</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="susiCalcPartner">Fricktaler Netzwerk</div>
                <div class="calc-kpi-lbl">Dachdecker, Holzbautechnik &amp; Spenglerei</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="susiCalcStep">Vor-Ort-Besichtigung</div>
                <div class="calc-kpi-lbl">Unverbindliche Aufnahme &amp; Kostenschätzung</div>
              </div>
            </div>

            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Eine Ansprechpartnerin von A bis Z:</strong> Keine wechselnden Kontakte: Susi Schmid plant, koordiniert und packt auf der Baustelle persönlich mit an.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Eigenleistung auf Wunsch willkommen:</strong> Beim Rückbau, Dämmen oder Täfern können Sie unter fachkundiger Anleitung selbst mithelfen.</span></div>
            </div>
          </div>

          <a href="kontakt.html?thema=dach" id="susiCalcCta" class="btn-cta btn-cta-gold" style="width:100%;">
            <span>In der Smart-Anfrage starten</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>"""


def render_impressum_modal() -> str:
    return f"""
  <!-- IMPRESSUM & DATENSCHUTZ MODAL -->
  <div class="wp-modal-backdrop" id="wpImpressumModal" role="dialog" aria-modal="true" aria-labelledby="wpImpTitle" data-allow-scroll="true">
    <div class="wp-modal-dialog" data-allow-scroll="true">
      <button type="button" class="wp-modal-close" aria-label="Dialog schliessen" onclick="wpCloseImpressumModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="section-kicker">RECHTLICHE ANGABEN · HANDELSREGISTER KANTON AARGAU</div>
      <h3 id="wpImpTitle" style="font-size:1.36rem;font-weight:700;margin-bottom:10px;">Impressum &amp; Datenschutz (Holz-Susi GmbH)</h3>
      <div style="font-size:0.88rem;color:var(--text-body);line-height:1.62;display:flex;flex-direction:column;gap:12px;">
        <div style="background-color:var(--bg-page);border:1px solid var(--border-light);border-left:4px solid var(--gold);padding:12px 14px;border-radius:var(--radius-sm);">
          <strong>Holz-Susi GmbH</strong><br>
          Susanne («Susi») Schmid · Wendelhof 424 · CH-5070 Frick (Kanton Aargau)<br>
          Telefon: +41 77 521 96 97 · E-Mail: info@holz-susi.ch · Web: https://holz-susi.ch<br>
          Öffnungszeiten: Montag – Freitag 07:00 – 12:00 Uhr | 13:00 – 17:30 Uhr
        </div>
        <p>
          <strong>Handelsregister &amp; Vertretungsberechtigte Person:</strong><br>
          Eingetragen im Handelsregister des Kantons Aargau · UID: <strong>CHE-187.492.373</strong>.<br>
          Inhaberin und Geschäftsführerin: Susanne Schmid.
        </p>
        <p>
          <strong>Urheber- &amp; Bildrechte:</strong><br>
          Die auf dieser Website gezeigten Vorher/Nachher-Referenzbilder, Baustellenaufnahmen, Porträts und Logos sind Eigentum der Holz-Susi GmbH (5070 Frick).
        </p>
        <p>
          <strong>Datenschutz (Schweizer DSG):</strong><br>
          Alle Angaben aus dem 3-Schritte Smart-Anfrage-Assistenten werden streng vertraulich behandelt, ausschliesslich zur Projektprüfung, Terminvereinbarung und Offertstellung durch die Holz-Susi GmbH verwendet und niemals an unbefugte Dritte weitergegeben.
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
      if (cEl && category) cEl.textContent = 'Leistungs- & Projektbereich: ' + category;
      if (fEl && focus) fEl.textContent = 'Ansprechpartnerin Holz-Susi GmbH: ' + focus;
      m.classList.add('open');
    }
    function wpCloseBlueprintModal() {
      var m = document.getElementById('wpBlueprintModal');
      if (m) m.classList.remove('open');
    }

    var susiCalcState = { role: 'privat', scope: 'dach', mode: 'komplett' };
    function susiSetCalc(group, val) {
      susiCalcState[group] = val;
      var gridId = group === 'role' ? 'susiCalcRoleGrid' : (group === 'scope' ? 'susiCalcScopeGrid' : 'susiCalcModeGrid');
      var attr = 'data-' + group;
      var btns = document.querySelectorAll('#' + gridId + ' .calc-option-btn');
      for (var i = 0; i < btns.length; i++) {
        btns[i].classList.toggle('active', btns[i].getAttribute(attr) === val);
      }
      susiUpdateCalcView();
    }
    function susiUpdateCalcView() {
      var badge = document.getElementById('susiCalcRefBadge');
      var head = document.getElementById('susiCalcHeadline');
      var desc = document.getElementById('susiCalcDesc');
      var lEl = document.getElementById('susiCalcLead');
      var mEl = document.getElementById('susiCalcModeOut');
      var pEl = document.getElementById('susiCalcPartner');
      var sEl = document.getElementById('susiCalcStep');
      var cta = document.getElementById('susiCalcCta');
      if (!head) return;

      var modeLabel = susiCalcState.mode === 'mithilfe'
        ? 'Mit aktiver Eigenleistung'
        : (susiCalcState.mode === 'leitung' ? 'Planung, Termin- & Bauleitung' : 'Schlüsselfertige Ausführung');
      if (mEl) mEl.textContent = modeLabel;

      if (susiCalcState.role === 'architektur') {
        badge.textContent = 'FÜR ARCHITEKTURBÜROS · HOLZBAUPLANUNG & BAULEITUNG';
        head.textContent = 'Holzbau-Kompetenz, Schnittstellen-Koordination & Bauleitung';
        desc.textContent = 'Prüfung der technischen Machbarkeit, Koordination mit Statik und Haustechnik sowie verlässliche Termin-, Qualitäts- und Kostenkontrolle auf der Baustelle.';
        lEl.textContent = 'Susanne Schmid (Bauleiterin)';
        pEl.textContent = 'Statik & Holzbautechnik';
        sEl.textContent = 'Plan- & Schnittstellencheck';
        if (cta) cta.href = 'kontakt.html?thema=planung';
      } else if (susiCalcState.role === 'bau') {
        badge.textContent = 'FÜR BAUUNTERNEHMEN · FACHKRAFT & PROJEKTLEITUNG AUF ZEIT';
        head.textContent = 'Verstärkung als Zimmerin EFZ, Kranführerin oder Bauleiterin';
        desc.textContent = 'Direkt einsetzbare Entlastung bei Personalengpässen, anspruchsvollen Holzbau-Etappen, Kranarbeiten oder in der Vorarbeit und Lehrlingsbetreuung.';
        lEl.textContent = 'Zimmerin EFZ & Kranführerin';
        pEl.textContent = 'Direkteinsatz im Team';
        sEl.textContent = 'Kapazitäts-Abstimmung';
        if (cta) cta.href = 'kontakt.html?thema=planung';
      } else {
        if (susiCalcState.scope === 'innen') {
          badge.textContent = 'REFERENZ-BEISPIEL: AUSBAU DACHSTOCK, ESTRICH & LAMINAT';
          head.textContent = 'Innenausbau, Dachstock, Blindboden & Raumverschönerung';
          desc.textContent = 'Vom gedämmten Estrich über sichtbare Holztäferdecken und Raumtrennwände bis zum neuen Blindboden und Laminat, auf Wunsch auch mit Ihrer aktiven Mithilfe.';
          lEl.textContent = 'Susanne Schmid (Zimmerin EFZ)';
          pEl.textContent = 'Holzbau & Innenausbau';
          sEl.textContent = 'Besichtigung & Offerte';
          if (cta) cta.href = 'kontakt.html?thema=innenausbau';
        } else if (susiCalcState.scope === 'aussen') {
          badge.textContent = 'REFERENZ-BEISPIEL: TERRASSENROST, PERGOLA & HOLZFASSADE';
          head.textContent = 'Terrassendeck, Pergola, Fassadenschalung & sauberer Rückbau';
          desc.textContent = 'Witterungsbeständige Terrassenböden mit Sitzbank und Pergola, hinterlüftete Holzfassaden sowie fachgerechter Rückbau samt Entsorgung.';
          lEl.textContent = 'Susanne Schmid (Frick)';
          pEl.textContent = 'Holzbau & Metallbau-Partner';
          sEl.textContent = 'Aufmass vor Ort';
          if (cta) cta.href = 'kontakt.html?thema=terrasse';
        } else {
          badge.textContent = 'REFERENZ-BEISPIEL: DACHSANIERUNG, MARDERSCHADEN & 4 DACHFENSTER';
          head.textContent = 'Dacherneuerung, Dachfenster-Wechsel & Marderschaden-Sanierung';
          desc.textContent = 'Thermische Dachsanierung, Austausch oder Neueinbau von Dachfenstern, Kamin-Rückbau und Unterdach-Reparatur mit unserem Fricktaler Partnernetzwerk.';
          lEl.textContent = 'Susanne Schmid + Netzwerk';
          pEl.textContent = 'Dachdecker & Zimmerei-Partner';
          sEl.textContent = 'Dachcheck vor Ort';
          if (cta) cta.href = 'kontakt.html?thema=dach';
        }
      }
    }


    function wpSyncSeasonalVisibility() {
      var now = new Date();
      var todayIso = now.toISOString().slice(0, 10);
      var sections = document.querySelectorAll('section[id]');
      var hiddenIds = {};
      for (var i = 0; i < sections.length; i++) {
        var sec = sections[i];
        var secId = sec.getAttribute('id');
        if (!secId) continue;
        var explicitHidden = sec.getAttribute('data-wp-hidden');
        var visFrom = sec.getAttribute('data-wp-visible-from') || '';
        var visUntil = sec.getAttribute('data-wp-visible-until') || '';
        var isHidden = false;
        if (explicitHidden === 'true') {
          isHidden = true;
        } else if (explicitHidden === 'false') {
          isHidden = false;
        } else if (visFrom || visUntil) {
          if (visFrom && todayIso < visFrom) isHidden = true;
          if (visUntil && todayIso > visUntil) isHidden = true;
        }
        if (isHidden) {
          hiddenIds['#' + secId] = true;
        }
        var existingBanner = sec.querySelector('.wp-cockpit-peek-banner');
        if (sec.classList.contains('wp-cockpit-peek') && isHidden) {
          if (!existingBanner) {
            var b = document.createElement('div');
            b.className = 'wp-cockpit-peek-banner';
            b.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg><span>Schlummer-Modus: Für Besucher aktuell ausgeblendet (Hier im Cockpit frei bearbeitbar)</span>';
            sec.insertBefore(b, sec.firstChild);
          }
        } else if (existingBanner) {
          existingBanner.remove();
        }
      }
      var allLinks = document.querySelectorAll('a[href*="#"]');
      for (var j = 0; j < allLinks.length; j++) {
        var a = allLinks[j];
        if (a.hasAttribute('data-wp-stoerer')) continue;
        var href = a.getAttribute('href') || '';
        var hashIdx = href.indexOf('#');
        if (hashIdx === -1) continue;
        var hash = href.slice(hashIdx);
        var li = a.closest('li');
        if (hiddenIds[hash]) {
          a.classList.add('wp-seasonal-hidden-link');
          if (li) li.classList.add('wp-seasonal-hidden-link');
        } else {
          a.classList.remove('wp-seasonal-hidden-link');
          if (li) li.classList.remove('wp-seasonal-hidden-link');
        }
      }
      var stoerers = document.querySelectorAll('[data-wp-stoerer]');
      for (var k = 0; k < stoerers.length; k++) {
        var st = stoerers[k];
        var target = st.getAttribute('data-wp-stoerer-target') || st.getAttribute('href') || '';
        var stActive = st.getAttribute('data-wp-stoerer-active');
        if (stActive === 'false' || (target && hiddenIds[target])) {
          st.classList.add('wp-seasonal-hidden-stoerer');
        } else {
          st.classList.remove('wp-seasonal-hidden-stoerer');
        }
      }
    }
    window.wpSyncSeasonalVisibility = wpSyncSeasonalVisibility;
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', wpSyncSeasonalVisibility);
    } else {
      wpSyncSeasonalVisibility();
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
    nav_leistungen = "active" if active_nav == "leistungen" else ""
    nav_referenzen = "active" if active_nav == "referenzen" else ""
    nav_ueber = "active" if active_nav == "ueber-uns" else ""
    nav_kontakt = "active" if active_nav == "kontakt" else ""

    return f"""<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-XSS-Protection" content="1; mode=block">
  <meta name="referrer" content="no-referrer">
  <title>{page_title}</title>
  <meta name="description" content="Holz-Susi GmbH in 5070 Frick (AG): Susanne («Susi») Schmid, Zimmerin EFZ, Projektleiterin und Bauleiterin für Dachsanierung, Dachfenster, Innenausbau, Terrassen, Fassaden und Bauleitung im Fricktal.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "name": "Holz-Susi GmbH",
    "url": "https://holz-susi.ch",
    "telephone": "+41 77 521 96 97",
    "email": "info@holz-susi.ch",
    "taxID": "CHE-187.492.373",
    "founder": "Susanne Schmid",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Wendelhof 424",
      "postalCode": "5070",
      "addressLocality": "Frick",
      "addressRegion": "AG",
      "addressCountry": "CH"
    }}
  }}
  </script>
  <style>
{SHARED_CSS}
  </style>
</head>
<body>

  <!-- TOP INFO BAR -->
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div class="top-bar-left">
        <span class="top-bar-badge" data-slot="topbar_badge">HOLZ-SUSI GMBH · WENDELHOF 424 · 5070 FRICK (AG)</span>
        <span data-slot="topbar_sub">Susanne («Susi») Schmid · Zimmerin EFZ, Projektleiterin &amp; Bauleiterin</span>
      </div>
      <div class="top-bar-links">
        <a href="tel:+41775219697">{SVG_PHONE} <span>077 521 96 97</span></a>
        <a href="mailto:info@holz-susi.ch">{SVG_MAIL} <span>info@holz-susi.ch</span></a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER -->
  <header class="site-header" data-section="header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="Holz-Susi GmbH Frick Startseite">
        <img src="images/logo.png" alt="Holz-Susi GmbH Logo" class="brand-logo" width="50" height="50" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">Holz-Susi GmbH</span>
          <span class="brand-sub" data-slot="brand_sub">5070 Frick · Holzbau &amp; Bauleitung</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}" data-nav-href="index.html">Startseite</a>
        <a href="leistungen.html" class="nav-link {nav_leistungen}" data-nav-href="leistungen.html">Leistungen</a>
        <a href="referenzen.html" class="nav-link {nav_referenzen}" data-nav-href="referenzen.html">Referenzen</a>
        <a href="ueber-uns.html" class="nav-link {nav_ueber}" data-nav-href="ueber-uns.html">Über Susi</a>
        <a href="kontakt.html" class="nav-link {nav_kontakt}" data-nav-href="kontakt.html">Kontakt</a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" data-slot="header_cta">
          <span>Projekt besprechen</span>
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
    <a href="leistungen.html" onclick="wpCloseMobileMenu()">Leistungen (Dach, Dachfenster, Innenausbau, Terrasse &amp; Bauleitung)</a>
    <a href="referenzen.html" onclick="wpCloseMobileMenu()">Vorher/Nachher-Referenzen &amp; Partnernetzwerk</a>
    <a href="ueber-uns.html" onclick="wpCloseMobileMenu()">Über Susanne («Susi») Schmid, Sponsoring &amp; Bluescht-Beiz</a>
    <a href="kontakt.html" onclick="wpCloseMobileMenu()">3-Schritte Smart-Anfrage &amp; Kontakt</a>
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
            <img src="images/logo.png" alt="Holz-Susi GmbH" width="54" height="54" style="border-radius:4px;" loading="lazy" decoding="async">
            <div>
              <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#1E140A;">Holz-Susi GmbH</div>
              <div style="font-size:0.78rem;color:#8F5300;font-weight:700;">Susanne («Susi») Schmid · Zimmerin EFZ</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#3A2918;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Vom ersten Gedanken bis zum letzten Handgriff: Persönliche Beratung, fachgerechter Holzbau, Innenausbau, Dachsanierung und engagierte Bauleitung aus Frick für das ganze Fricktal und die angrenzenden Regionen.
          </p>
          <div style="font-size:0.84rem;color:#1E140A;font-weight:600;">
            Wendelhof 424 · CH-5070 Frick · UID CHE-187.492.373
          </div>
        </div>

        <div>
          <div class="footer-title">Leistungen &amp; Holzbau</div>
          <ul class="footer-list">
            <li><a href="leistungen.html#dachsanierung">Dacherneuerung &amp; Marderschaden</a></li>
            <li><a href="leistungen.html#dachfenster">Einbau &amp; Wechsel von Dachfenstern</a></li>
            <li><a href="leistungen.html#innenausbau">Innenausbau, Dachstock &amp; Böden</a></li>
            <li><a href="leistungen.html#terrasse">Terrassendeck, Pergola &amp; Fassade</a></li>
            <li><a href="leistungen.html#bauleitung">Projektplanung, Bauleitung &amp; Rückbau</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Referenzen &amp; Porträt</div>
          <ul class="footer-list">
            <li><a href="referenzen.html">Alle 8 Vorher/Nachher-Referenzen</a></li>
            <li><a href="referenzen.html#dachstuehle">Dachstühle &amp; Partnernetzwerk</a></li>
            <li><a href="ueber-uns.html">Über Susanne («Susi») Schmid</a></li>
            <li><a href="ueber-uns.html#engagement">Sponsoring Selina Burger &amp; Bluescht-Beiz</a></li>
            <li><a href="#bluescht-beiz">Bluescht-Beiz auf dem Wendelhof (April)</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; Öffnungszeiten</div>
          <ul class="footer-list">
            <li><a href="tel:+41775219697">Telefon: 077 521 96 97</a></li>
            <li><a href="mailto:info@holz-susi.ch">E-Mail: info@holz-susi.ch</a></li>
            <li><span style="font-size:0.84rem;color:#3A2918;">Mo – Fr: 07:00 – 12:00 | 13:00 – 17:30 Uhr</span></li>
            <li><a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">3-Schritte Smart-Anfrage starten</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Holz-Susi GmbH (Wendelhof 424, CH-5070 Frick AG · CHE-187.492.373).</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
          <a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">Projekt-Anfrage &amp; Offerte</a>
          <a href="referenzen.html" style="color:#3A2918;">Vorher/Nachher-Projekte</a>
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

    return f"""<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-XSS-Protection" content="1; mode=block">
  <meta name="referrer" content="no-referrer">
  <title>{page_title}</title>
  <meta name="description" content="Unverbindlicher Vorschau-Entwurf (Zeigeversion) für die Holz-Susi GmbH in 5070 Frick: 2 Beispiel-Seiten sind bereits ausgearbeitet, 3 weitere Detailseiten folgen beim gemeinsamen Ausbau.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <style>
{SHARED_CSS}
  </style>
</head>
<body>

  <!-- TOP INFO BAR -->
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div class="top-bar-left">
        <span class="top-bar-badge" data-slot="topbar_badge">HOLZ-SUSI GMBH · WENDELHOF 424 · 5070 FRICK (AG)</span>
        <span data-slot="topbar_sub">Susanne («Susi») Schmid · Zimmerin EFZ, Projektleiterin &amp; Bauleiterin</span>
      </div>
      <div class="top-bar-links">
        <a href="tel:+41775219697">{SVG_PHONE} <span>077 521 96 97</span></a>
        <a href="mailto:info@holz-susi.ch">{SVG_MAIL} <span>info@holz-susi.ch</span></a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER (ZEIGEVERSION MIT KUNDENFREUNDLICHEN VORSCHAU-HINWEISEN) -->
  <header class="site-header" data-section="header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="Holz-Susi GmbH Frick Startseite">
        <img src="images/logo.png" alt="Holz-Susi GmbH Logo" class="brand-logo" width="50" height="50" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">Holz-Susi GmbH</span>
          <span class="brand-sub" data-slot="brand_sub">5070 Frick · Holzbau &amp; Bauleitung</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}" data-nav-href="index.html">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#15803D"/></svg>
          <span>Startseite</span>
        </a>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="leistungen.html" onclick="wpOpenBlueprintModal('Alle 6 Leistungsbereiche &amp; 3 Kundengruppen im Detail', 'Dacherneuerung, Dachfenster, Innenausbau, Terrassen &amp; Fassaden, Bauleitung sowie Abbrucharbeiten', 'Susanne («Susi») Schmid')">
          <span>Leistungen</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="referenzen.html" onclick="wpOpenBlueprintModal('Alle 8 Vorher/Nachher-Referenzprojekte &amp; Fricktaler Partnernetzwerk', 'Dachsanierung, Dachstock &amp; Estrich, Marderschaden, Holzfassade, Firstfenster, Terrasse/Pergola, Blindboden &amp; Dachstühle', 'Susanne («Susi») Schmid')">
          <span>Referenzen</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="ueber-uns.html" onclick="wpOpenBlueprintModal('Über Susanne («Susi») Schmid, Werdegang &amp; Regionales Engagement', '15+ Jahre Zimmerin EFZ, Vorarbeiterin, Kranführerin &amp; Bauleiterin · Sponsoring Selina Burger · Bluescht-Beiz Wendelhof', 'Susanne («Susi») Schmid')">
          <span>Über Susi</span>
        </button>
        <a href="kontakt.html" class="nav-link {nav_kontakt}" data-nav-href="kontakt.html">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#15803D"/></svg>
          <span>Kontakt</span>
        </a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" data-slot="header_cta">
          <span>3-Schritte-Anfrage testen</span>
          {SVG_ARROW}
        </a>
        <button type="button" class="mobile-toggle" id="mobileMenuBtn" aria-label="Menü öffnen" onclick="wpToggleMobileMenu()">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    </div>
  </header>

  <div class="mobile-drawer" id="mobileDrawer">
    <a href="index.html" onclick="wpCloseMobileMenu()">Startseite (Ausgearbeitet)</a>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu();wpOpenBlueprintModal('Alle 6 Leistungsbereiche &amp; 3 Kundengruppen im Detail', 'Dachsanierung, Dachfenster, Innenausbau, Terrassen/Fassaden, Bauleitung &amp; Abbruch', 'Susanne («Susi») Schmid')">
      <span>Leistungen</span>
      <span class="preview-status-badge">Folgt beim Ausbau</span>
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu();wpOpenBlueprintModal('Alle 8 Vorher/Nachher-Referenzprojekte &amp; Partnernetzwerk', 'Komplette Vorher/Nachher-Galerie aus dem Fricktal', 'Susanne («Susi») Schmid')">
      <span>Referenzen</span>
      <span class="preview-status-badge">Folgt beim Ausbau</span>
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu();wpOpenBlueprintModal('Über Susanne («Susi») Schmid, Sponsoring &amp; Bluescht-Beiz', 'Porträt, Werdegang, Werte &amp; Bluescht-Beiz auf dem Wendelhof Frick', 'Susanne («Susi») Schmid')">
      <span>Über Susi</span>
      <span class="preview-status-badge">Folgt beim Ausbau</span>
    </button>
    <a href="kontakt.html" onclick="wpCloseMobileMenu()">Kontakt &amp; 3-Schritte Smart-Anfrage (Ausgearbeitet)</a>
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
            <img src="images/logo.png" alt="Holz-Susi GmbH" width="54" height="54" style="border-radius:4px;" loading="lazy" decoding="async">
            <div>
              <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#1E140A;">Holz-Susi GmbH</div>
              <div style="font-size:0.78rem;color:#8F5300;font-weight:700;">Susanne («Susi») Schmid · Zimmerin EFZ</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#3A2918;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Vom ersten Gedanken bis zum letzten Handgriff: Persönliche Beratung, fachgerechter Holzbau, Innenausbau, Dachsanierung und engagierte Bauleitung aus Frick für das ganze Fricktal und die angrenzenden Regionen.
          </p>
          <div style="font-size:0.84rem;color:#1E140A;font-weight:600;">
            Wendelhof 424 · CH-5070 Frick · UID CHE-187.492.373
          </div>
        </div>

        <div>
          <div class="footer-title">Bereits in dieser Vorschau live</div>
          <ul class="footer-list">
            <li><a href="index.html">Startseite mit allen 6 Leistungen &amp; Vorher/Nachher</a></li>
            <li><a href="index.html#projektberater">Interaktiver Holzbau- &amp; Renovations-Berater</a></li>
            <li><a href="#bluescht-beiz">Bluescht-Beiz auf dem Wendelhof (Saison-Highlight)</a></li>
            <li><a href="kontakt.html">3-Schritte Smart-Anfrage (inkl. PDF-Dossier)</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Weitere Detailseiten (Ausbau)</div>
          <ul class="footer-list">
            <li><button type="button" onclick="wpOpenBlueprintModal('Leistungen für Bauherrschaften, Architektur &amp; Bauunternehmen', 'Dachsanierung, Dachfenster, Innenausbau, Terrassen/Fassaden, Bauleitung &amp; Abbruch', 'Susanne («Susi») Schmid')">Leistungen im Detail (Vorschau)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Alle 8 Vorher/Nachher-Referenzen &amp; Partnernetzwerk', 'Komplette Fotodokumentation aller Umbau- und Dachprojekte', 'Susanne («Susi») Schmid')">Alle 8 Referenzen (Vorschau)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Über Susanne («Susi») Schmid, Sponsoring &amp; Bluescht-Beiz', 'Persönlicher Werdegang, Werte, Nachwuchssponsoring &amp; Bluescht-Beiz Wendelhof', 'Susanne («Susi») Schmid')">Über Susi &amp; Engagement (Vorschau)</button></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; Rechtliches</div>
          <ul class="footer-list">
            <li><a href="tel:+41775219697">Telefon: 077 521 96 97</a></li>
            <li><a href="mailto:info@holz-susi.ch">E-Mail: info@holz-susi.ch</a></li>
            <li><a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">3-Schritte Smart-Anfrage starten</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Holz-Susi GmbH (5070 Frick AG) · Unverbindlicher Vorschau-Entwurf (Zeigeversion).</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
          <a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">Smart-Anfrage testen</a>
          <a href="index.html#weitere-themenbereiche" style="color:#3A2918;">Weitere Detailseiten</a>
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
      <div class="section-kicker">UNVERBINDLICHER VORSCHAU-ENTWURF FÜR HOLZ-SUSI.CH</div>
      <h3 id="wpBpTitle" style="font-size:1.36rem;font-weight:700;margin-bottom:8px;">Unverbindlicher Vorschau-Entwurf für die Holz-Susi GmbH</h3>
      <p id="wpBpSub" style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
        In dieser <strong>Zeigeversion (2 Beispiel-Seiten ausgearbeitet)</strong> sehen Sie Ihre neue Startseite mit allen 6 Holzbau-Leistungen, den 3 Zielgruppen, dem interaktiven Holzbau- &amp; Renovations-Berater sowie den live funktionierenden 3-Schritte Smart-Anfrage-Assistenten. Dieser vertiefte Themenbereich wird beim gemeinsamen Ausbau schlüsselfertig mit allen Originaltexten und Vorher/Nachher-Bildern freigeschaltet.
      </p>
      <div style="background-color:var(--gold-soft);border-left:4px solid var(--gold);padding:12px 14px;border-radius:var(--radius-sm);font-size:0.86rem;margin-bottom:14px;">
        <div style="font-weight:700;color:var(--charcoal-deep);" id="wpBpCategory">Leistungs- &amp; Projektbereich: Vorbereitet für den gemeinsamen Ausbau</div>
        <div style="color:var(--text-body);margin-top:2px;" id="wpBpContact">Ansprechpartnerin Holz-Susi GmbH: Susanne («Susi») Schmid</div>
      </div>

      <div class="wp-modal-checklist">
        <div style="font-family:'Lexend',sans-serif;font-size:0.8rem;font-weight:700;text-transform:uppercase;color:var(--charcoal-deep);">
          Was beim gemeinsamen Ausbau in diesem Themenbereich enthalten ist:
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Vollständige Leistungsseite für Private Bauherrschaften (inkl. aktiver Eigenleistung), Architekturbüros und Bauunternehmen über alle 6 Fachgebiete</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Referenz- &amp; Vorher/Nachher-Seite mit allen 8 dokumentierten Projekten (Dachsanierung, Dachstock, Marderschaden, Fassade, Firstfenster, Terrasse/Pergola, Blindboden &amp; Dachstühle) sowie dem Fricktaler Partnernetzwerk</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Persönliche Porträtseite über Susanne («Susi») Schmid (Werdegang von der Landwirtin &amp; Maurerei zur Zimmerin EFZ &amp; Bauleiterin), Nachwuchssponsoring Selina Burger und die «Bluescht-Beiz» auf dem Wendelhof</span>
        </div>
      </div>

      <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:18px;">
        <button type="button" class="btn-cta btn-cta-primary btn-sm" onclick="wpCloseBlueprintModal()">
          <span>Verstanden · Vorschau weiter ansehen</span>
        </button>
        <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm">
          <span>3-Schritte Smart-Anfrage testen</span>
        </a>
      </div>
    </div>
  </div>

{render_impressum_modal()}
{COMMON_UI_JS}
</body>
</html>"""

# ==============================================================================
# SEITEN-INHALTE: V1 STARTSEITE (index.html)
# ==============================================================================
V1_INDEX_BODY = f"""
  <!-- HERO SECTION -->
  <section class="hero-section" data-section="hero">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light" data-slot="hero_kicker">HOLZBAU, DACHSANIERUNG, INNENAUSBAU &amp; BAULEITUNG · 5070 FRICK (AG)</div>
        <h1 class="hero-title" data-slot="hero_title">
          Vom ersten Gedanken bis zum <span>letzten Handgriff.</span>
        </h1>
        <p class="hero-lead" data-slot="hero_lead">
          Bei der Holz-Susi GmbH in Frick erhalten Sie persönliche Beratung, ehrliches Zimmerhandwerk und engagierte Bauleitung aus einer Hand: Susanne («Susi») Schmid begleitet Private Bauherrschaften, Architekturbüros und Bauunternehmen mit über 15 Jahren Erfahrung auf und neben der Baustelle.
        </p>

        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
            <span>Projekt &amp; Offerte anfragen</span>
            {SVG_ARROW}
          </a>
          <a href="#projektberater" class="btn-cta btn-cta-outline-light" data-slot="hero_cta_secondary">
            <span>Projektberater starten</span>
          </a>
        </div>

        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Zimmerin EFZ &amp; Bauleiterin</span>
            <span class="hero-badge-lbl">Über 15 Jahre Praxis als Zimmerin, Vorarbeiterin, Kranführerin &amp; Projektleiterin</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Eine Ansprechpartnerin</span>
            <span class="hero-badge-lbl">Von der Besichtigung und Offerte bis zur sauberen Ausführung</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Eigenleistung möglich</span>
            <span class="hero-badge-lbl">Auf Wunsch können Sie beim Umbau unter Fachanleitung aktiv mitanpacken</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Wendelhof 424 · 5070 Frick</span>
            <span class="hero-badge-lbl">Verankert im Fricktal mit starkem regionalem Partnernetzwerk</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        {render_hero_stoerer()}
        <img src="images/hero-susi-schmid-holzbau.png" alt="Susanne Susi Schmid, Inhaberin der Holz-Susi GmbH in 5070 Frick" width="600" height="390" data-slot="hero_image">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#1E140A;">Susanne («Susi») Schmid · Holz-Susi GmbH</div>
            <div style="font-size:0.8rem;color:#3A2918;">Zimmerin EFZ, Projektleiterin &amp; Bauleiterin in 5070 Frick</div>
          </div>
          <span class="top-bar-badge">ECHTES HANDWERK</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 3 ZIELGRUPPEN (PRIVAT, ARCHITEKTUR, BAUUNTERNEHMEN) -->
  <section data-section="zielgruppen" id="zielgruppen" style="background-color:var(--bg-Warm);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="audiences_kicker">MASSGESCHNEIDERTE ZUSAMMENARBEIT · 3 AUFTRAGGEBER-GRUPPEN</div>
        <h2 class="section-title" data-slot="audiences_title">Für wen die Holz-Susi GmbH im Einsatz steht</h2>
        <p class="section-desc" data-slot="audiences_desc">
          Ob Sie Ihr Eigenheim verschönern möchten, als Architekturbüro eine verlässliche Holzbau- und Bauleitungspartnerin suchen oder als Bauunternehmen tatkräftige Verstärkung brauchen:
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">1. Privatkunden</span>
              <span class="icon-box">{SVG_HOME}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Ihre Idee ist Holz wert!</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Möchten Sie Ihr Dach sanieren, den Estrich ausbauen oder eine neue Holzterrasse realisieren? Ich begleite Sie persönlich von der ersten Idee bis zur Umsetzung, bei grösseren Projekten Hand in Hand mit meinem regionalen Netzwerk.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Persönliche Beratung vor Ort &amp; transparente Kostenschätzung</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Aktiv mithelfen möglich:</strong> Eigenleistung beim Umbau auf Wunsch herzlich willkommen</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=dach" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Privatprojekt anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">2. Architekturbüros</span>
              <span class="icon-box">{SVG_LAYERS}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Ihr Projekt braucht Holz!</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Sie planen ein Bauvorhaben mit Holzanteil oder eine anspruchsvolle Renovation im Bestand? Ich unterstütze Sie mit technischer Machbarkeitsprüfung, Holzbauplanung und strukturierter Bauleitung vor Ort.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Abstimmung von Konstruktionsdetails mit Statik und Haustechnik</span></div>
              <div class="check-item">{SVG_CHECK} <span>Termin-, Kosten- und Qualitätskontrolle direkt auf der Baustelle</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=planung" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Planung &amp; Bauleitung besprechen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">3. Bauunternehmen</span>
              <span class="icon-box">{SVG_BUILDING}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Holzkompetenz für Ihr Bauprojekt!</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Fehlt bei einer Etappe eine erfahrene Fachkraft im Holzbau oder in der Führung? Ich packe als gelernte Zimmerin EFZ, Kranführerin, Vorarbeiterin oder Projektleiterin unkompliziert in Ihrem Team mit an.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Einsatz als Zimmerin EFZ, Vorarbeiterin oder Kranführerin auf der Baustelle</span></div>
              <div class="check-item">{SVG_CHECK} <span>Projekt- &amp; Bauleitungs-Mandate bei Umbau- und Sanierungsvorhaben</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=planung" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Kapazität &amp; Einsatz anfragen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 6 KERNLEISTUNGEN (3x2 SYMMETRISCHES RASTER) -->
  <section data-section="kernangebote" id="kernangebote">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="pillars_kicker">LEISTUNGSÜBERSICHT · HOLZBAU, RENOVATION &amp; BAULEITUNG</div>
        <h2 class="section-title" data-slot="pillars_title">Sechs Fachgebiete rund um Dach, Raum und Konstruktion</h2>
        <p class="section-desc" data-slot="pillars_desc">
          Ob gezielte Reparatur nach einem Marderschaden, neue Dachfenster für mehr Tageslicht oder eine umfassende Dach- und Innenraum-Renovation: Jedes Projekt wird sorgfältig geplant und handwerklich sauber ausgeführt.
        </p>
      </div>

      <div class="grid-3">
        <!-- 1. Dacherneuerung -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-leistung-dachsanierung.png" alt="Dacherneuerung und energetische Dachsanierung durch Holz-Susi GmbH Frick" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Dachsanierung</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Wärmedämmung</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Dacherneuerung &amp; Dachsanierung</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Fachgerechte Sanierung und Modernisierung bestehender Dächer, von der Behebung von Marderschäden am Unterdach bis zur kompletten thermischen Dacherneuerung.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Wärmedämmung, Unterdach, Lattung &amp; neue Ziegeleindeckung</span></div>
                <div class="check-item">{SVG_CHECK} <span>Komplette Koordination mit Dachdecker- &amp; Spenglerpartnern</span></div>
              </div>
            </div>
            <a href="leistungen.html#dachsanierung" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zur Dachsanierung</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 2. Dachfenster -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-leistung-dachfenster.jpg" alt="Einbau und Wechsel von Dachfenstern im Fricktal" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Dachfenster</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Tageslicht</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Einbau &amp; Wechsel von Dachfenstern</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Mehr Tageslicht, frische Luft und bessere Dämmwerte im Dachgeschoss durch präzise eingebaute oder erneuerte Dachfenster inklusive Innenfutter.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Austausch alter Dachfenster &amp; Rückbau undichter Firstfenster</span></div>
                <div class="check-item">{SVG_CHECK} <span>Massgefertigte Holz-Innenverkleidungen, Storen &amp; Sonnenschutz</span></div>
              </div>
            </div>
            <a href="leistungen.html#dachfenster" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zu Dachfenstern</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 3. Innenausbau & Renovation -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-leistung-innenausbau.jpg" alt="Innenausbau, Dachstock und Estrich durch Holz-Susi GmbH" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Innenausbau</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Wohnraum</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Innenausbau &amp; Renovation</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Verwandeln Sie ungenutzte Estriche oder in die Jahre gekommene Räume in helle, behagliche Wohn- und Arbeitsbereiche mit natürlichem Holzcharakter.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Dachstockausbau, Decken- und Wandtäfer, Trennwände &amp; Türen</span></div>
                <div class="check-item">{SVG_CHECK} <span>Blindböden, Ausgleichsschüttung, Parkett- und Laminatböden</span></div>
              </div>
            </div>
            <a href="leistungen.html#innenausbau" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zum Innenausbau</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 4. Terrassendeck & Fassaden -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-leistung-terrasse-fassade.jpg" alt="Terrassenrost, Pergola und Holzfassade von Holz-Susi GmbH" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Terrassenbau</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Aussenholz</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Terrassendeck &amp; Fassaden</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Witterungsbeständige Terrassenböden, massgeschneiderte Pergolen und langlebige Holzfassaden, die Ihrem Haus einen warmen, zeitlosen Ausdruck verleihen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Erneuerung von Terrassenrosten, Sitzbänken &amp; Beschattungs-Pergolen</span></div>
                <div class="check-item">{SVG_CHECK} <span>Hinterlüftete Holzschalungen &amp; konstruktiver Holzschutz</span></div>
              </div>
            </div>
            <a href="leistungen.html#terrasse" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zu Terrasse &amp; Fassade</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 5. Projektplanung & Bauleitung -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-leistung-projektleitung.jpg" alt="Projektplanung, Projektleitung und Bauleitung im Holzbau" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Bauleitung</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Koordination</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Projektplanung &amp; Bauleitung</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Strukturierte Planung, Terminsteuerung und Bauleitung bei Renovations- und Holzbauarbeiten für Bauherrschaften, Architekturbüros und Bauunternehmen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Schnittstellen-Koordination zwischen allen beteiligten Gewerken</span></div>
                <div class="check-item">{SVG_CHECK} <span>Transparente Termin-, Qualitäts- und Kostenkontrolle vor Ort</span></div>
              </div>
            </div>
            <a href="leistungen.html#bauleitung" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zur Bauleitung</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 6. Abbrucharbeiten -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-leistung-abbruch.png" alt="Gezielte Abbrucharbeiten und Rückbau bei Umbauten" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Rückbau</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Demontage</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Abbrucharbeiten &amp; Rückbau</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Sorgfältiger Rückbau von Kaminen, alten Wand- und Bodenbelägen, Täferdecken oder Terrassen als saubere Basis für Ihren Neuaufbau.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Staubarme Demontage unter Schutz der bestehenden Bausubstanz</span></div>
                <div class="check-item">{SVG_CHECK} <span>Sortenreine Trennung und fachgerechte Entsorgung aller Materialien</span></div>
              </div>
            </div>
            <a href="leistungen.html#bauleitung" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zum Rückbau</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

{render_holz_advisor()}

  <!-- VORHER / NACHHER REFERENZEN -->
  <section data-section="referenzen-auszug" id="referenzen">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="refs_kicker">DOKUMENTIERTE ERGEBNISSE · VORHER / NACHHER IM VERGLEICH</div>
        <h2 class="section-title" data-slot="refs_title">Sechs ausgewählte Vorher/Nachher-Projekte aus der Praxis</h2>
        <p class="section-desc" data-slot="refs_desc">
          Bilder sagen mehr als grosse Worte: Sehen Sie anhand echter Umbau-, Dach- und Terrassenprojekte der Holz-Susi GmbH, wie aus schadhaften oder veralteten Bauteilen langlebige Lösungen entstehen.
        </p>
      </div>

      {render_references_grid(limit=6, is_v2=False)}

      <div style="margin-top:34px;display:flex;justify-content:center;">
        <a href="referenzen.html" class="btn-cta btn-cta-outline">
          <span>Alle 8 Vorher/Nachher-Referenzen &amp; Partnernetzwerk ansehen</span>
          {SVG_ARROW}
        </a>
      </div>
    </div>
  </section>

  <!-- ÜBER SUSANNE SCHMID & REGIONALES ENGAGEMENT -->
  <section data-section="ueber-susi-kurz" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="about_kicker">PERSÖNLICH VERANKERT IM FRICKTAL · WENDELHOF 424 IN 5070 FRICK</div>
        <h2 class="section-title" data-slot="about_title">Wer hinter der Holz-Susi GmbH steht</h2>
        <p class="section-desc" data-slot="about_desc">
          Gutes Handwerk lebt von Erfahrung, Verlässlichkeit und einem starken Miteinander in der Region.
        </p>
      </div>

      <div class="grid-2">
        <div class="founder-card">
          <div class="founder-top">
            <img src="images/team-susi-schmid-portrait.png" alt="Susanne Susi Schmid, Inhaberin der Holz-Susi GmbH in Frick" class="founder-portrait" loading="lazy" decoding="async">
            <div>
              <span class="meta-badge" style="margin-bottom:8px;">Inhaberin &amp; Geschäftsführerin</span>
              <h3 style="font-size:1.35rem;font-weight:700;margin-bottom:6px;">Susanne («Susi») Schmid</h3>
              <p style="font-size:0.84rem;font-weight:700;color:var(--gold-dark);margin-bottom:8px;">
                Zimmerin EFZ · Vorarbeiterin · Kranführerin · Projekt- &amp; Bauleiterin
              </p>
              <p style="font-size:0.88rem;color:var(--text-body);line-height:1.58;">
                Nach der Ausbildung zur Landwirtin und fünf Jahren Maurerei bei der GLB Aargau absolvierte Susi Schmid bei der PM Mangold AG in Ormalingen ihre Lehre als Zimmerin EFZ. Seit über 15 Jahren verbindet sie praktische Baustellenerfahrung mit strukturierter Projekt- und Bauleitung.
              </p>
            </div>
          </div>
          <div class="founder-body">
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Fünf gelebte Werte:</strong> Qualität, Zuverlässigkeit, Transparenz, Flexibilität und Leidenschaft für den Werkstoff Holz.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Erfahrung in allen Rollen:</strong> Zimmerin EFZ, Vorarbeiterin, Lehrlingsausbilderin, Kranführerin sowie Projekt- und Bauleiterin.</span></div>
            </div>
            <a href="ueber-uns.html" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Porträt &amp; Werdegang von Susi Schmid lesen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Regionale Verbundenheit · 5070 Frick</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 style="font-size:1.28rem;font-weight:700;margin-bottom:10px;">Partnernetzwerk, Nachwuchs-Sponsoring &amp; «Bluescht-Beiz»</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:14px;">
              Grössere Dachstühle und komplexe Sanierungen realisiert die Holz-Susi GmbH Hand in Hand mit ausgewählten Fachbetrieben aus der Region, darunter Reto Huber (Dachdecker), Michael Hürbin (Holzbautechniker), Gebr. Schmid AG, Fricktal Zimmerei, Mangold Holzbau GmbH, Dionys Soder Holzbau, Rebmann AG und metatec Metallbau.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Nachwuchs-Sponsoring:</strong> Stolze Unterstützerin der jungen Leichtathletin Selina Burger (TSV Frick) auf ihrem sportlichen Weg.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Saisonale «Bluescht-Beiz» auf dem Wendelhof:</strong> Jeden April während der Chriesibluescht am Fricktaler Chriesiwäg (Jurapark Aargau) lädt Familie Schmid auf den Wendelhof in Frick ein.</span></div>
            </div>
          </div>
          <a href="ueber-uns.html#engagement" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Sponsoring &amp; Bluescht-Beiz</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- PRAXIS-FAQS -->
  <section data-section="faqs">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="faq_kicker">HÄUFIGE FRAGEN · ABLAUF, EIGENLEISTUNG &amp; KOSTEN</div>
        <h2 class="section-title" data-slot="faq_title">Antworten auf die wichtigsten Fragen vor Ihrem Projektstart</h2>
        <p class="section-desc" data-slot="faq_desc">
          Transparente Antworten rund um Eigenleistung beim Umbau, Vor-Ort-Besichtigung, Partnerbetriebe und Bauleitung.
        </p>
      </div>

      {render_faqs_grid()}
    </div>
  </section>
{render_bluescht_beiz_section()}
"""

# ==============================================================================
# SEITEN-INHALTE: V1 LEISTUNGEN (leistungen.html)
# ==============================================================================
V1_LEISTUNGEN_BODY = f"""
  <section class="hero-section" data-section="hero-leistungen">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">LEISTUNGEN IM DETAIL · HOLZ-SUSI GMBH FRICK</div>
        <h1 class="hero-title">
          Holzbau, Renovation &amp; Bauleitung <span>aus einer Hand.</span>
        </h1>
        <p class="hero-lead">
          Von der ersten Besichtigung auf Ihrer Baustelle bis zum letzten Handgriff: Entdecken Sie unsere sechs Leistungsbereiche für Private Bauherrschaften, Architekturbüros und Bauunternehmen im Fricktal und den angrenzenden Regionen.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>Besichtigung anfragen</span>
            {SVG_ARROW}
          </a>
          <a href="referenzen.html" class="btn-cta btn-cta-outline-light">
            <span>Vorher/Nachher ansehen</span>
          </a>
        </div>
        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Dach &amp; Dachfenster</span>
            <span class="hero-badge-lbl">Energetische Sanierung, Marderschaden-Behebung &amp; Fenstertausch</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Innenausbau &amp; Böden</span>
            <span class="hero-badge-lbl">Dachstock, Estrich, Täfer, Blindboden &amp; Laminat</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Aussenholz</span>
            <span class="hero-badge-lbl">Witterungsbeständige Terrassenroste, Pergolen &amp; Holzschalungen</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Planung &amp; Rückbau</span>
            <span class="hero-badge-lbl">Projekt- &amp; Bauleitung bei Renovationen sowie sauberer Rückbau</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/ref-leistung-dachsanierung.png" alt="Dachsanierung und Einbau von vier Dachfenstern durch Holz-Susi GmbH" width="600" height="390">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#1E140A;">Komplettsanierung &amp; Ausbau</div>
            <div style="font-size:0.8rem;color:#3A2918;">Sorgfältig geplant und mit regionalen Fachpartnern umgesetzt</div>
          </div>
          <span class="top-bar-badge">6 FACHGEBIETE</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 6 FACHGEBIETE IM DETAIL -->
  <section data-section="leistungen-detail" id="dachsanierung">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">ALLE 6 LEISTUNGSBEREICHE IM ÜBERBLICK</div>
        <h2 class="section-title">Massgeschneiderte Lösungen für Dach, Raum und Gebäudehülle</h2>
        <p class="section-desc">
          Jedes Gebäude hat seine eigene Geschichte. Wir prüfen die bestehende Substanz vor Ort und schlagen Ihnen genau die Lösung vor, die technisch, optisch und wirtschaftlich überzeugt.
        </p>
      </div>

      <div class="grid-2">
        <!-- 1. Dacherneuerung -->
        <div class="content-card card-accent-top" id="dachsanierung-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">01 · Dach &amp; Wärmeschutz</span>
              <span class="icon-box">{SVG_HOME}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Dacherneuerung &amp; Dachsanierung</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Ein intaktes, gut gedämmtes Dach schützt Ihr Haus über Jahrzehnte und senkt den Energieverbrauch spürbar. Wir sanieren Dächer im Bestand von der Sparrenlage bis zur Eindeckung.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Thermische Dachsanierung, Dampfbremse, Wärmedämmung &amp; Unterdach</span></div>
              <div class="check-item">{SVG_CHECK} <span>Dauerhafte Behebung von Marderschäden inkl. Schutzmassnahmen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Rückbau nicht mehr benötigter Kamine und Schliessen der Dachhaut</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=dach" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Dachsanierung oder Dachcheck anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- 2. Dachfenster -->
        <div class="content-card card-accent-top" id="dachfenster">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">02 · Licht &amp; Luft unterm Dach</span>
              <span class="icon-box">{SVG_LAYERS}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Einbau &amp; Wechsel von Dachfenstern</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Neue Dachfenster bringen bis zu dreimal mehr Tageslicht in den Dachstock und verbessern den Wärme- und Schallschutz sofort.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>1:1-Austausch bestehender Dachfenster ohne grossen Umbauaufwand</span></div>
              <div class="check-item">{SVG_CHECK} <span>Neueinbau von Einzel- oder Mehrfach-Dachfenstern inkl. Wechselhölzern</span></div>
              <div class="check-item">{SVG_CHECK} <span>Rückbau alter Firstfenster und Einbau moderner Dachfenster-Lösungen</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=dach" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Dachfenster-Offerte anfordern</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- 3. Innenausbau & Renovation -->
        <div class="content-card card-accent-top" id="innenausbau">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">03 · Wohnraum &amp; Bodenaufbau</span>
              <span class="icon-box">{SVG_HAMMER}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Innenausbau, Dachstock &amp; Renovation</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Schaffen Sie zusätzlichen Wohnraum unterm Dach oder verleihen Sie bestehenden Zimmern mit Holz und neuen Böden ein frisches Gesicht.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Kompletter Ausbau von Dachstock und Estrich zu Wohn- oder Arbeitsräumen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Wand- und Deckentäfer, Leichtbauwände, Verkleidungen &amp; Einbauten</span></div>
              <div class="check-item">{SVG_CHECK} <span>Neuer Blindboden für Umbauten sowie Ersatz alter Teppiche durch Laminat/Parkett</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=innenausbau" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Innenausbau-Projekt besprechen</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- 4. Terrassendeck & Fassaden -->
        <div class="content-card card-accent-top" id="terrasse">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">04 · Aussenraum &amp; Holzfassade</span>
              <span class="icon-box">{SVG_SHIELD}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Terrassendeck, Pergola &amp; Fassaden</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Holz im Aussenbereich braucht die richtige Holzauswahl und einen durchdachten konstruktiven Schutz, damit Sie viele Jahre Freude daran haben.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Erneuerung von Terrassenrosten inkl. Unterkonstruktion, Pergola &amp; Sitzbank</span></div>
              <div class="check-item">{SVG_CHECK} <span>Fassadenverschönerung mit hinterlüfteter Holzschalung</span></div>
              <div class="check-item">{SVG_CHECK} <span>Sichtschutz, Unterstände, Carports und individuelle Holzbauten ums Haus</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=terrasse" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Terrasse oder Fassade anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- 5. Projektplanung & Bauleitung -->
        <div class="content-card card-accent-top" id="bauleitung">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">05 · Planung, Projektleitung &amp; Bauleitung</span>
              <span class="icon-box">{SVG_BUILDING}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Projektplanung &amp; Bauleitung bei Renovationen</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Gerade bei Umbauten im Bestand greifen viele Gewerke ineinander. Ich halte für Sie die Fäden in der Hand und sorge für einen reibungslosen Bauablauf.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Machbarkeitsprüfung, Massaufnahme, Kostenschätzung &amp; Terminprogramm</span></div>
              <div class="check-item">{SVG_CHECK} <span>Koordination von Dachdecker, Spengler, Holzbautechnik, Elektro &amp; Metallbau</span></div>
              <div class="check-item">{SVG_CHECK} <span>Temporäre Unterstützung für Architekturbüros und Bauunternehmen</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=planung" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Bauleitungs- oder Planungsmandat anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- 6. Abbrucharbeiten -->
        <div class="content-card card-accent-top" id="abbruch">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">06 · Rückbau &amp; Baufreimachung</span>
              <span class="icon-box">{SVG_USERS}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Abbrucharbeiten &amp; Rückbau</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Vor dem schönen Neuaufbau steht der geordnete Rückbau: Wir legen Bauteile frei, ohne angrenzende Konstruktionen zu beschädigen.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Rückbau von Kaminen, nichttragenden Wänden, alten Böden &amp; Verkleidungen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Auf Wunsch mit Ihrer aktiven Mithilfe unter fachkundiger Anleitung</span></div>
              <div class="check-item">{SVG_CHECK} <span>Saubere Trennung, Abtransport und vorschriftsgemässe Entsorgung</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=innenausbau" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Rückbau &amp; Umbau besprechen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- ABLAUF IN 4 SCHRITTEN -->
  <section data-section="ablauf" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">SO ARBEITEN WIR ZUSAMMEN · KLAR &amp; PERSÖNLICH</div>
        <h2 class="section-title">In vier Schritten von Ihrer Idee zum fertigen Projekt</h2>
        <p class="section-desc">
          Kurze Entscheidungswege, offene Kommunikation und saubere Handwerksarbeit.
        </p>
      </div>

      <div class="grid-4">
        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Schritt 1</span>
            <h3 style="font-size:1.12rem;font-weight:700;margin-bottom:8px;">Kontaktaufnahme</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Sie melden sich per Telefon, E-Mail oder über die 3-Schritte Smart-Anfrage und schildern kurz Ihr Anliegen.
            </p>
          </div>
          <div style="font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Unverbindlich &amp; direkt</div>
        </div>

        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Schritt 2</span>
            <h3 style="font-size:1.12rem;font-weight:700;margin-bottom:8px;">Besichtigung &amp; Offerte</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Susi Schmid prüft die Gegebenheiten persönlich vor Ort, nimmt Mass und erstellt eine nachvollziehbare Kostenschätzung.
            </p>
          </div>
          <div style="font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Transparente Kalkulation</div>
        </div>

        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Schritt 3</span>
            <h3 style="font-size:1.12rem;font-weight:700;margin-bottom:8px;">Projektentscheid</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Wir legen gemeinsam Materialien, Zeitplan und auf Wunsch auch den Umfang Ihrer eigenen Mithilfe fest.
            </p>
          </div>
          <div style="font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Auf Ihre Wünsche abgestimmt</div>
        </div>

        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Schritt 4</span>
            <h3 style="font-size:1.12rem;font-weight:700;margin-bottom:8px;">Saubere Umsetzung</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Termingerechte, sorgfältige Ausführung bis zum letzten Handgriff und gemeinsame Endabnahme vor Ort.
            </p>
          </div>
          <div style="font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Qualität, die bleibt</div>
        </div>
      </div>
    </div>
  </section>
"""

# ==============================================================================
# SEITEN-INHALTE: V1 REFERENZEN (referenzen.html)
# ==============================================================================
def render_full_before_after_cards() -> str:
    cards = []
    for ref in BEFORE_INVENTORY["references"]:
        cards.append(f"""
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">{ref['category']}</span>
              <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">{ref.get('highlight', 'Vorher/Nachher')}</span>
            </div>
            <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:6px;">{ref['title']}</h3>
            <p style="font-size:0.84rem;font-weight:700;color:var(--gold-dark);margin-bottom:12px;">{ref['scope']}</p>
            <div class="form-grid-2" style="margin-bottom:14px;">
              <div style="border:1px solid var(--border-light);border-radius:var(--radius-sm);overflow:hidden;background-color:var(--bg-page);">
                <img src="{ref['before_img']}" alt="Vorher / Ausgangslage: {ref['title']}" style="width:100%;height:175px;object-fit:cover;" loading="lazy" decoding="async">
                <div style="padding:6px 10px;font-size:0.75rem;font-weight:700;color:var(--text-muted);background-color:#F8EEE5;">Vorher / Bauphase</div>
              </div>
              <div style="border:1px solid var(--gold-border);border-radius:var(--radius-sm);overflow:hidden;background-color:var(--bg-page);">
                <img src="{ref['after_img']}" alt="Nachher / Ergebnis: {ref['title']}" style="width:100%;height:175px;object-fit:cover;" loading="lazy" decoding="async">
                <div style="padding:6px 10px;font-size:0.75rem;font-weight:700;color:var(--gold-dark);background-color:var(--gold-soft);">Nachher / Ergebnis</div>
              </div>
            </div>
            <p style="font-size:0.9rem;color:var(--text-body);line-height:1.6;">{ref['desc']}</p>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Ähnliches Vorhaben anfragen</span>
            {SVG_ARROW}
          </a>
        </div>""")
    return '<div class="grid-2">\n' + "\n".join(cards) + "\n      </div>"


V1_REFERENZEN_BODY = f"""
  <section class="hero-section" data-section="hero-referenzen">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">VORHER / NACHHER REFERENZEN · ECHTE PROJEKTE AUS DER PRAXIS</div>
        <h1 class="hero-title">
          Handwerk, das man <span>vorher und nachher</span> sieht.
        </h1>
        <p class="hero-lead">
          Von der kompletten Dachsanierung über den Dachstock- und Estrichausbau bis zur neuen Terrasse mit Pergola: Hier sehen Sie acht dokumentierte Projekte der Holz-Susi GmbH im direkten Vorher/Nachher-Vergleich.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>Eigenes Projekt besprechen</span>
            {SVG_ARROW}
          </a>
          <a href="#dachstuehle" class="btn-cta btn-cta-outline-light">
            <span>Dachstühle &amp; Partnernetzwerk</span>
          </a>
        </div>
        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">8 Projekt-Serien</span>
            <span class="hero-badge-lbl">Lückenlos mit Originalfotos von der Ausgangslage bis zum Ergebnis dokumentiert</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Dach &amp; Innenraum</span>
            <span class="hero-badge-lbl">Dachsanierung, Marderschaden, Firstfenster, Dachstock &amp; Blindboden</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Fassade &amp; Terrasse</span>
            <span class="hero-badge-lbl">Hinterlüftete Holzschalungen, Terrassenroste, Sitzbänke &amp; Pergolen</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Fricktaler Netzwerk</span>
            <span class="hero-badge-lbl">Dachstühle in Zusammenarbeit mit regionalen Zimmerei- &amp; Holzbaupartnern</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/ref-leistung-terrasse-fassade.jpg" alt="Erneuerung Terrassenrost, Pergola und Sitzbank durch Holz-Susi GmbH" width="600" height="390">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#1E140A;">Terrassenrost, Pergola &amp; Sitzbank</div>
            <div style="font-size:0.8rem;color:#3A2918;">Präzise gefertigt für langanhaltende Freude im Aussenbereich</div>
          </div>
          <span class="top-bar-badge">VORHER / NACHHER</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ALLE 8 VORHER / NACHHER PROJEKTE -->
  <section data-section="alle-referenzen">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">8 DOKUMENTIERTE FALLBEISPIELE · AUSGANGSLAGE &amp; ERGEBNIS</div>
        <h2 class="section-title">Alle Vorher/Nachher-Projekte im direkten Bildvergleich</h2>
        <p class="section-desc">
          Jedes Projekt zeigt links die Ausgangslage oder Bauphase und rechts das fertiggestellte Resultat.
        </p>
      </div>

      {render_full_before_after_cards()}
    </div>
  </section>

  <!-- PARTNERNETZWERK IM FRICKTAL -->
  <section data-section="partnernetzwerk" id="dachstuehle" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">GEMEINSAM STARK · UNSER REGIONALES PARTNERNETZWERK</div>
        <h2 class="section-title">Bewährte Fachpartner für grössere Holzbau- und Dachprojekte</h2>
        <p class="section-desc">
          Für Dachstühle, Abbund, Eindeckungen und Metallbauarbeiten arbeitet die Holz-Susi GmbH mit eingespielten Partnerbetrieben aus dem Fricktal und der Region zusammen. Sie behalten dabei immer Susanne Schmid als zentrale Ansprechpartnerin:
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Dachdecker-Partner</span>
            <h3 style="font-size:1.15rem;font-weight:700;margin-bottom:6px;">Reto Huber · Dachdecker</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Fachgerechte Steildach- und Flachdacheindeckungen, Unterdachsysteme und Anschlüsse bei Dachsanierungen.
            </p>
          </div>
          <div style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Eingespielte Zusammenarbeit auf dem Dach</div>
        </div>

        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Holzbautechnik &amp; Planung</span>
            <h3 style="font-size:1.15rem;font-weight:700;margin-bottom:6px;">Michael Hürbin · Holzbautechniker</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Technische Holzbauplanung, Dimensionierung, Werkplanung und konstruktive Detailausbildung.
            </p>
          </div>
          <div style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Präzision von der Planung bis zum Abbund</div>
        </div>

        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Zimmerei &amp; Holzbau</span>
            <h3 style="font-size:1.15rem;font-weight:700;margin-bottom:6px;">Mangold Holzbau GmbH &amp; Fricktal Zimmerei</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Starke Zimmerei-Partner für grössere Dachstühle, Elementbau und anspruchsvolle Tragkonstruktionen.
            </p>
          </div>
          <div style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Gemeinsame Schlagkraft bei Grossprojekten</div>
        </div>

        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Holzbau &amp; Dachstühle</span>
            <h3 style="font-size:1.15rem;font-weight:700;margin-bottom:6px;">Dionys Soder Holzbau &amp; Rebmann AG</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Partnerschaftliche Realisierung von Dachstühlen von der Planung über den Abbund bis zur Aufrichte.
            </p>
          </div>
          <div style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Regionale Handwerksqualität</div>
        </div>

        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Bau &amp; Infrastruktur</span>
            <h3 style="font-size:1.15rem;font-weight:700;margin-bottom:6px;">Gebr. Schmid AG</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Verlässliche Unterstützung bei Bau-, Umgebungs-, Transport- und Kranarbeiten rund um den Wendelhof und im Fricktal.
            </p>
          </div>
          <div style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Kurze Wege ab 5070 Frick</div>
        </div>

        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Metallbau &amp; Stahlteile</span>
            <h3 style="font-size:1.15rem;font-weight:700;margin-bottom:6px;">metatec Metallbau</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Massgefertigte Stahlträger, Verbindungsmittel, Geländer und Metallkonstruktionen in Kombination mit Holz.
            </p>
          </div>
          <div style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Holz &amp; Metall perfekt verbunden</div>
        </div>
      </div>
    </div>
  </section>
"""

# ==============================================================================
# SEITEN-INHALTE: V1 ÜBER SUSI (ueber-uns.html)
# ==============================================================================
V1_UEBER_UNS_BODY = f"""
  <section class="hero-section" data-section="hero-ueber">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">ÜBER SUSANNE («SUSI») SCHMID · HOLZ-SUSI GMBH FRICK</div>
        <h1 class="hero-title">
          Über 15 Jahre <span>Leidenschaft für Holz</span> auf und neben der Baustelle.
        </h1>
        <p class="hero-lead">
          «Ich begleite Ihr Projekt vom ersten Gedanken bis zum letzten Handgriff: mit ehrlichem Handwerk, klaren Worten und einem offenen Ohr für Ihre Ideen.»
        </p>
        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>Persönlich Kontakt aufnehmen</span>
            {SVG_ARROW}
          </a>
          <a href="#engagement" class="btn-cta btn-cta-outline-light">
            <span>Sponsoring &amp; Bluescht-Beiz</span>
          </a>
        </div>
        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Zimmerin EFZ</span>
            <span class="hero-badge-lbl">Lehrabschluss bei der PM Mangold AG in Ormalingen</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Maurerei &amp; Landwirtschaft</span>
            <span class="hero-badge-lbl">Gelernte Landwirtin + 5 Jahre Maurerei-Praxis bei der GLB Aargau</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Führung &amp; Kran</span>
            <span class="hero-badge-lbl">Vorarbeiterin, Lehrlingsausbilderin, Kranführerin &amp; Bauleiterin</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Wendelhof 424 · Frick</span>
            <span class="hero-badge-lbl">Verwurzelt im Fricktal · UID CHE-187.492.373</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/team-susi-schmid-portrait.png" alt="Susanne Susi Schmid, Inhaberin der Holz-Susi GmbH in Frick" width="600" height="390">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#1E140A;">Susanne («Susi») Schmid</div>
            <div style="font-size:0.8rem;color:#3A2918;">Inhaberin &amp; Geschäftsführerin der Holz-Susi GmbH</div>
          </div>
          <span class="top-bar-badge">SEIT 15+ JAHREN</span>
        </div>
      </div>
    </div>
  </section>

  <!-- WERDEGANG & 5 WERTE -->
  <section data-section="werdegang">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">MEIN WEG INS ZIMMERHANDWERK &amp; IN DIE SELBSTÄNDIGKEIT</div>
        <h2 class="section-title">Praxiserfahrung vom Fundament bis zum Dachfirst</h2>
        <p class="section-desc">
          Wer sowohl die Landwirtschaft, das Maurerhandwerk als auch den Holzbau von der Pike auf gelernt hat, versteht Gebäude als Ganzes.
        </p>
      </div>

      <div class="grid-2">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Beruflicher Werdegang</span>
              <span class="icon-box">{SVG_HAMMER}</span>
            </div>
            <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:10px;">Vom Bauernhof über die Maurerei zur Zimmerin EFZ &amp; Bauleiterin</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Meine berufliche Laufbahn begann mit der Ausbildung zur <strong>Landwirtin</strong>. Danach arbeitete ich fünf Jahre lang als <strong>Maurerin bei der GLB Aargau</strong>, wo ich mir ein fundiertes Verständnis für Massivbau, Umbauten und bestehende Bausubstanz aneignete.
            </p>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Meine grosse Begeisterung für den Werkstoff Holz führte mich anschliessend zur Zweitausbildung als <strong>Zimmerin EFZ bei der PM Mangold AG in Ormalingen</strong>. In den vergangenen über 15 Jahren durfte ich auf und neben der Baustelle nahezu jede Funktion ausüben:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Zimmerin EFZ &amp; Vorarbeiterin:</strong> Abbund, Aufrichte, Dachsanierung, Innenausbau und Fassadenbau</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Kranführerin &amp; Lehrlingsausbilderin:</strong> Übersicht behalten, Sicherheit gewährleisten und Wissen weitergeben</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Projektleiterin &amp; Bauleiterin:</strong> Planung, Kalkulation, Terminführung und Koordination aller Gewerke</span></div>
            </div>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Projekt direkt mit Susi Schmid besprechen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Wofür ich einstehe</span>
              <span class="icon-box">{SVG_SHIELD}</span>
            </div>
            <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:10px;">Meine fünf Werte bei jedem Auftrag</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Ob kleines Reparaturprojekt oder grosse Dachsanierung: Auf diese fünf Grundsätze können Sie sich bei der Holz-Susi GmbH verlassen:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>1. Qualität:</strong> Sorgfältige Materialwahl, saubere Details und langlebige Konstruktionen nach den Regeln der Baukunst.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>2. Zuverlässigkeit:</strong> Abmachungen, Termine und Zusagen gelten auf der Baustelle genauso wie im Büro.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>3. Transparenz:</strong> Nachvollziehbare Offerten und offene Kommunikation ohne Überraschungen.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>4. Flexibilität:</strong> Individuelle Lösungen, auch dann, wenn Sie als Bauherrschaft selbst mitanpacken möchten.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>5. Leidenschaft:</strong> Echte Freude am Arbeiten mit Holz und am sichtbaren Vorher/Nachher-Ergebnis.</span></div>
            </div>
          </div>
          <a href="referenzen.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Ergebnisse in den Referenzen ansehen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- SPONSORING & BLUESCHT-BEIZ WENDELHOF -->
  <section data-section="engagement" id="engagement" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">HERZBLUT IM FRICKTAL · SPONSORING &amp; WENDELHOF FRICK</div>
        <h2 class="section-title">Nachwuchs-Sponsoring &amp; unsere «Bluescht-Beiz» auf dem Wendelhof</h2>
        <p class="section-desc">
          Als Fricktaler Betrieb engagieren wir uns aktiv für den regionalen Sportnachwuchs und pflegen die Gastfreundschaft auf dem Wendelhof.
        </p>
      </div>

      <div class="grid-2">
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/sponsor-selina-burger-tsv-frick.jpg" alt="Nachwuchs-Sponsoring Leichtathletin Selina Burger TSV Frick durch Holz-Susi GmbH" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Sport-Sponsoring · TSV Frick</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Leichtathletik-Nachwuchs</span>
              </div>
              <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Unterstützung für Selina Burger (Leichtathletik)</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Ausdauer, Technik und Freude an der Leistung verbinden den Sport mit dem Handwerk. Die Holz-Susi GmbH unterstützt die talentierte Nachwuchs-Leichtathletin <strong>Selina Burger</strong> vom TSV Frick auf ihrem sportlichen Weg.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Gezielte Nachwuchsförderung direkt im Fricktal</span></div>
                <div class="check-item">{SVG_CHECK} <span>Gemeinsame Werte: Einsatzwille, Bodenständigkeit &amp; Ausdauer</span></div>
              </div>
            </div>
            <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Kontakt mit Susi Schmid aufnehmen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-wendelhof-bluescht-beiz.jpg" alt="Bluescht-Beiz auf dem Wendelhof 424 in 5070 Frick während der Kirschblüte" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Wendelhof 424 · 5070 Frick</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Jeden April zur Kirschblüte</span>
              </div>
              <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Saisonale «Bluescht-Beiz» am Fricktaler Chriesiwäg</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Wenn im April rund um den Wendelhof in Frick die Kirschbäume blühen, öffnen wir an ausgewählten Tagen unsere gemütliche <strong>«Bluescht-Beiz»</strong> direkt am Fricktaler Chriesiwäg (Jurapark Aargau).
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Feine regionale Verpflegung, Getränke &amp; Kaffee mit Blick in die Kirschblüten</span></div>
                <div class="check-item">{SVG_CHECK} <span>Idealer Zwischenhalt auf Ihrer Frühlingswanderung auf dem Chriesiwäg in Frick</span></div>
              </div>
            </div>
            <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Standort Wendelhof 424 in Frick</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

# ==============================================================================
# SEITEN-INHALTE: V2 STARTSEITE (ZEIGEVERSION / VORSCHAU-ENTWURF)
# ==============================================================================
V2_INDEX_BODY = f"""
  <!-- HERO SECTION -->
  <section class="hero-section" data-section="hero">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light" data-slot="hero_kicker">HOLZBAU, DACHSANIERUNG, INNENAUSBAU &amp; BAULEITUNG · 5070 FRICK (AG)</div>
        <h1 class="hero-title" data-slot="hero_title">
          Vom ersten Gedanken bis zum <span>letzten Handgriff.</span>
        </h1>
        <p class="hero-lead" data-slot="hero_lead">
          Bei der Holz-Susi GmbH in Frick erhalten Sie persönliche Beratung, ehrliches Zimmerhandwerk und engagierte Bauleitung aus einer Hand: Susanne («Susi») Schmid begleitet Private Bauherrschaften, Architekturbüros und Bauunternehmen mit über 15 Jahren Erfahrung auf und neben der Baustelle.
        </p>

        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
            <span>Projekt &amp; Offerte anfragen</span>
            {SVG_ARROW}
          </a>
          <a href="#projektberater" class="btn-cta btn-cta-outline-light" data-slot="hero_cta_secondary">
            <span>Projektberater starten</span>
          </a>
        </div>

        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Zimmerin EFZ &amp; Bauleiterin</span>
            <span class="hero-badge-lbl">Über 15 Jahre Praxis als Zimmerin, Vorarbeiterin, Kranführerin &amp; Projektleiterin</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Eine Ansprechpartnerin</span>
            <span class="hero-badge-lbl">Von der Besichtigung und Offerte bis zur sauberen Ausführung</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Eigenleistung möglich</span>
            <span class="hero-badge-lbl">Auf Wunsch können Sie beim Umbau unter Fachanleitung aktiv mitanpacken</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Wendelhof 424 · 5070 Frick</span>
            <span class="hero-badge-lbl">Verankert im Fricktal mit starkem regionalem Partnernetzwerk</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        {render_hero_stoerer()}
        <img src="images/hero-susi-schmid-holzbau.png" alt="Susanne Susi Schmid, Inhaberin der Holz-Susi GmbH in 5070 Frick" width="600" height="390" data-slot="hero_image">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#1E140A;">Susanne («Susi») Schmid · Holz-Susi GmbH</div>
            <div style="font-size:0.8rem;color:#3A2918;">Zimmerin EFZ, Projektleiterin &amp; Bauleiterin in 5070 Frick</div>
          </div>
          <span class="top-bar-badge">ECHTES HANDWERK</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 3 ZIELGRUPPEN -->
  <section data-section="zielgruppen" id="zielgruppen" style="background-color:var(--bg-Warm);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="audiences_kicker">MASSGESCHNEIDERTE ZUSAMMENARBEIT · 3 AUFTRAGGEBER-GRUPPEN</div>
        <h2 class="section-title" data-slot="audiences_title">Für wen die Holz-Susi GmbH im Einsatz steht</h2>
        <p class="section-desc" data-slot="audiences_desc">
          Ob Sie Ihr Eigenheim verschönern möchten, als Architekturbüro eine verlässliche Holzbau- und Bauleitungspartnerin suchen oder als Bauunternehmen tatkräftige Verstärkung brauchen:
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">1. Privatkunden</span>
              <span class="icon-box">{SVG_HOME}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Ihre Idee ist Holz wert!</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Möchten Sie Ihr Dach sanieren, den Estrich ausbauen oder eine neue Holzterrasse realisieren? Ich begleite Sie persönlich von der ersten Idee bis zur Umsetzung, bei grösseren Projekten Hand in Hand mit meinem regionalen Netzwerk.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Persönliche Beratung vor Ort &amp; transparente Kostenschätzung</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Aktiv mithelfen möglich:</strong> Eigenleistung beim Umbau auf Wunsch herzlich willkommen</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=dach" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Privatprojekt anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">2. Architekturbüros</span>
              <span class="icon-box">{SVG_LAYERS}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Ihr Projekt braucht Holz!</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Sie planen ein Bauvorhaben mit Holzanteil oder eine anspruchsvolle Renovation im Bestand? Ich unterstütze Sie mit technischer Machbarkeitsprüfung, Holzbauplanung und strukturierter Bauleitung vor Ort.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Abstimmung von Konstruktionsdetails mit Statik und Haustechnik</span></div>
              <div class="check-item">{SVG_CHECK} <span>Termin-, Kosten- und Qualitätskontrolle direkt auf der Baustelle</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=planung" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Planung &amp; Bauleitung besprechen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">3. Bauunternehmen</span>
              <span class="icon-box">{SVG_BUILDING}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Holzkompetenz für Ihr Bauprojekt!</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Fehlt bei einer Etappe eine erfahrene Fachkraft im Holzbau oder in der Führung? Ich packe als gelernte Zimmerin EFZ, Kranführerin, Vorarbeiterin oder Projektleiterin unkompliziert in Ihrem Team mit an.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Einsatz als Zimmerin EFZ, Vorarbeiterin oder Kranführerin auf der Baustelle</span></div>
              <div class="check-item">{SVG_CHECK} <span>Projekt- &amp; Bauleitungs-Mandate bei Umbau- und Sanierungsvorhaben</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=planung" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Kapazität &amp; Einsatz anfragen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 6 KERNLEISTUNGEN -->
  <section data-section="kernangebote" id="kernangebote">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="pillars_kicker">LEISTUNGSÜBERSICHT · HOLZBAU, RENOVATION &amp; BAULEITUNG</div>
        <h2 class="section-title" data-slot="pillars_title">Sechs Fachgebiete rund um Dach, Raum und Konstruktion</h2>
        <p class="section-desc" data-slot="pillars_desc">
          Ob gezielte Reparatur nach einem Marderschaden, neue Dachfenster für mehr Tageslicht oder eine umfassende Dach- und Innenraum-Renovation:
        </p>
      </div>

      <div class="grid-3">
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-leistung-dachsanierung.png" alt="Dacherneuerung und energetische Dachsanierung durch Holz-Susi GmbH Frick" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Dachsanierung</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Wärmedämmung</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Dacherneuerung &amp; Dachsanierung</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Fachgerechte Sanierung und Modernisierung bestehender Dächer, von der Behebung von Marderschäden am Unterdach bis zur kompletten thermischen Dacherneuerung.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Wärmedämmung, Unterdach, Lattung &amp; neue Ziegeleindeckung</span></div>
                <div class="check-item">{SVG_CHECK} <span>Komplette Koordination mit Dachdecker- &amp; Spenglerpartnern</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Dacherneuerung &amp; energetische Dachsanierung', 'Thermische Sanierung, Marderschaden-Behebung, Kamin-Rückbau &amp; Dachstuhl', 'Susanne («Susi») Schmid')">
              <span>Details zur Dachsanierung</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-leistung-dachfenster.jpg" alt="Einbau und Wechsel von Dachfenstern im Fricktal" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Dachfenster</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Tageslicht</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Einbau &amp; Wechsel von Dachfenstern</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Mehr Tageslicht, frische Luft und bessere Dämmwerte im Dachgeschoss durch präzise eingebaute oder erneuerte Dachfenster inklusive Innenfutter.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Austausch alter Dachfenster &amp; Rückbau undichter Firstfenster</span></div>
                <div class="check-item">{SVG_CHECK} <span>Massgefertigte Holz-Innenverkleidungen, Storen &amp; Sonnenschutz</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Einbau &amp; Wechsel von Dachfenstern', 'Fenstertausch, Neueinbau, Firstfenster-Ersatz &amp; Holz-Innenfutter', 'Susanne («Susi») Schmid')">
              <span>Details zu Dachfenstern</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-leistung-innenausbau.jpg" alt="Innenausbau, Dachstock und Estrich durch Holz-Susi GmbH" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Innenausbau</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Wohnraum</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Innenausbau &amp; Renovation</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Verwandeln Sie ungenutzte Estriche oder in die Jahre gekommene Räume in helle, behagliche Wohn- und Arbeitsbereiche mit natürlichem Holzcharakter.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Dachstockausbau, Decken- und Wandtäfer, Trennwände &amp; Türen</span></div>
                <div class="check-item">{SVG_CHECK} <span>Blindböden, Ausgleichsschüttung, Parkett- und Laminatböden</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Innenausbau, Dachstock &amp; Bodenaufbau', 'Estrichausbau, Täferarbeiten, Blindboden, Laminat &amp; aktive Eigenleistung', 'Susanne («Susi») Schmid')">
              <span>Details zum Innenausbau</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-leistung-terrasse-fassade.jpg" alt="Terrassenrost, Pergola und Holzfassade von Holz-Susi GmbH" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Terrassenbau</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Aussenholz</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Terrassendeck &amp; Fassaden</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Witterungsbeständige Terrassenböden, massgeschneiderte Pergolen und langlebige Holzfassaden, die Ihrem Haus einen warmen, zeitlosen Ausdruck verleihen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Erneuerung von Terrassenrosten, Sitzbänken &amp; Beschattungs-Pergolen</span></div>
                <div class="check-item">{SVG_CHECK} <span>Hinterlüftete Holzschalungen &amp; konstruktiver Holzschutz</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Terrassendeck, Pergola &amp; Holzfassaden', 'Terrassenroste, Sitzbänke, Pergolen &amp; hinterlüftete Fassadenschalungen', 'Susanne («Susi») Schmid')">
              <span>Details zu Terrasse &amp; Fassade</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-leistung-projektleitung.jpg" alt="Projektplanung, Projektleitung und Bauleitung im Holzbau" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Bauleitung</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Koordination</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Projektplanung &amp; Bauleitung</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Strukturierte Planung, Terminsteuerung und Bauleitung bei Renovations- und Holzbauarbeiten für Bauherrschaften, Architekturbüros und Bauunternehmen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Schnittstellen-Koordination zwischen allen beteiligten Gewerken</span></div>
                <div class="check-item">{SVG_CHECK} <span>Transparente Termin-, Qualitäts- und Kostenkontrolle vor Ort</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Projektplanung, Projektleitung &amp; Bauleitung', 'Koordination bei Renovationen sowie Unterstützung für Architektur &amp; Bauunternehmen', 'Susanne («Susi») Schmid')">
              <span>Details zur Bauleitung</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-leistung-abbruch.png" alt="Gezielte Abbrucharbeiten und Rückbau bei Umbauten" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Rückbau</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Demontage</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Abbrucharbeiten &amp; Rückbau</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Sorgfältiger Rückbau von Kaminen, alten Wand- und Bodenbelägen, Täferdecken oder Terrassen als saubere Basis für Ihren Neuaufbau.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Staubarme Demontage unter Schutz der bestehenden Bausubstanz</span></div>
                <div class="check-item">{SVG_CHECK} <span>Sortenreine Trennung und fachgerechte Entsorgung aller Materialien</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Abbrucharbeiten &amp; Rückbau bei Renovationen', 'Sorgfältige Demontage, Kamin-Rückbau &amp; Vorbereitung für den Innenausbau', 'Susanne («Susi») Schmid')">
              <span>Details zum Rückbau</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

{render_holz_advisor()}

  <!-- VORHER / NACHHER REFERENZEN -->
  <section data-section="referenzen-auszug" id="referenzen">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="refs_kicker">DOKUMENTIERTE ERGEBNISSE · VORHER / NACHHER IM VERGLEICH</div>
        <h2 class="section-title" data-slot="refs_title">Sechs ausgewählte Vorher/Nachher-Projekte aus der Praxis</h2>
        <p class="section-desc" data-slot="refs_desc">
          Sehen Sie anhand echter Umbau-, Dach- und Terrassenprojekte der Holz-Susi GmbH, wie aus schadhaften oder veralteten Bauteilen langlebige Lösungen entstehen.
        </p>
      </div>

      {render_references_grid(limit=6, is_v2=True)}
    </div>
  </section>

{render_bluescht_beiz_section()}

  <!-- V2 AUSBLICK AUF DIE 3 WEITEREN UNTERSEITEN (#UI-03 KUNDEN-SPRACHE) -->
  <section class="preview-scope-section" id="weitere-themenbereiche" data-section="vorschau-umfang">
    <div class="container">
      <div class="preview-scope-banner">
        <div class="section-kicker">UNVERBINDLICHER VORSCHAU-ENTWURF · 2 BEISPIEL-SEITEN AUSGEARBEITET</div>
        <h2 style="font-size:clamp(1.55rem,2.5vw,2.1rem);font-weight:700;margin-bottom:10px;">
          Ausblick: Diese 3 weiteren Detailseiten folgen beim gemeinsamen Ausbau
        </h2>
        <p style="font-size:0.95rem;color:var(--text-body);line-height:1.62;">
          In dieser <strong>Zeigeversion</strong> sind Ihre neue <strong>Startseite</strong> (inklusive interaktivem Holzbau- &amp; Renovations-Berater) sowie die <strong>Kontaktseite mit dem 3-Schritte Smart-Anfrage-Assistenten</strong> bereits vollständig ausgearbeitet und live testbar. Beim gemeinsamen Ausbau schalten wir zusätzlich die folgenden drei vertieften Unterseiten mit allen Originaltexten und Ihren über 50 Vorher/Nachher-Projektbildern frei:
        </p>
      </div>

      <div class="grid-3">
        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Folgt beim Ausbau · Unterseite 1</span>
              <span class="icon-box">{SVG_HAMMER}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Leistungen: Alle 6 Fachgebiete &amp; 4-Schritte-Ablauf</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Vertiefte Fachseite für Private Bauherrschaften, Architekturbüros und Bauunternehmen:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Dacherneuerung, Marderschaden-Sanierung &amp; Dachfenster-Wechsel</span></div>
              <div class="check-item">{SVG_CHECK} <span>Innenausbau, Dachstock, Blindboden, Terrasse, Pergola &amp; Holzfassade</span></div>
              <div class="check-item">{SVG_CHECK} <span>Projektplanung, Bauleitung, Rückbau &amp; Modell «Aktive Eigenleistung»</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Leistungen: Alle 6 Fachgebiete &amp; 4-Schritte-Ablauf', 'Dachsanierung, Dachfenster, Innenausbau, Terrasse/Fassade, Bauleitung &amp; Rückbau', 'Susanne («Susi») Schmid')">
            <span>Vorschau-Details zu Leistungen öffnen</span>
            {SVG_ARROW}
          </button>
        </div>

        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Folgt beim Ausbau · Unterseite 2</span>
              <span class="icon-box">{SVG_HOME}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Alle 8 Vorher/Nachher-Referenzen &amp; Partnernetzwerk</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Direkter Vorher/Nachher-Bildvergleich aller dokumentierten Umbau- und Dachprojekte:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Komplettprojekt Dachsanierung, Dachstock &amp; Marderschaden-Behebung</span></div>
              <div class="check-item">{SVG_CHECK} <span>Holzfassade, Firstfenster-Rückbau, Terrassenrost/Pergola &amp; Blindboden</span></div>
              <div class="check-item">{SVG_CHECK} <span>Dachstühle &amp; Vorstellung aller Fricktaler Partnerbetriebe</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Alle 8 Vorher/Nachher-Referenzen &amp; Partnernetzwerk', 'Direkter Bildvergleich (Vorher/Nachher) + Fricktaler Partnerbetriebe', 'Susanne («Susi») Schmid')">
            <span>Vorschau-Details zu Referenzen öffnen</span>
            {SVG_ARROW}
          </button>
        </div>

        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Folgt beim Ausbau · Unterseite 3</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Über Susanne («Susi») Schmid, Sponsoring &amp; Bluescht-Beiz</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Persönliche Porträtseite über die Inhaberin und ihre Verwurzelung in 5070 Frick:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Werdegang: Landwirtin, 5 Jahre Maurerei GLB Aargau &amp; Zimmerin EFZ</span></div>
              <div class="check-item">{SVG_CHECK} <span>15+ Jahre Erfahrung als Vorarbeiterin, Kranführerin &amp; Bauleiterin</span></div>
              <div class="check-item">{SVG_CHECK} <span>Sponsoring Selina Burger (TSV Frick) &amp; «Bluescht-Beiz» auf dem Wendelhof</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Über Susanne («Susi») Schmid, Sponsoring &amp; Bluescht-Beiz', 'Beruflicher Werdegang, 5 Werte, Nachwuchssponsoring &amp; Bluescht-Beiz Wendelhof', 'Susanne («Susi») Schmid')">
            <span>Vorschau-Details zu Über Susi öffnen</span>
            {SVG_ARROW}
          </button>
        </div>
      </div>
    </div>
  </section>
"""


# ==============================================================================
# SEITEN-INHALTE: KONTAKT & 3-SCHRITTE SMART-ANFRAGE (kontakt.html)
# ==============================================================================
def build_kontakt_body(client_slug: str, source_page: str) -> str:
    return f"""
  <section data-section="kontakt-zentrale" style="padding: 56px 0 84px;">
    <div class="container">
      <div class="contact-layout">
        <!-- LEFT COLUMN: DIREKTKONTAKT FRICK -->
        <div class="contact-info-panel">
          <div class="section-kicker" data-slot="contact_kicker">KONTAKT &amp; UNVERBINDLICHE BESICHTIGUNG · 5070 FRICK (AG)</div>
          <h1 style="font-size:clamp(1.65rem,2.5vw,2.15rem);font-weight:700;margin-bottom:12px;" data-slot="contact_title">
            Ihr direkter Draht zu Susanne («Susi») Schmid.
          </h1>
          <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:18px;" data-slot="contact_lead">
            Ob Dachsanierung, neue Dachfenster, Innenausbau im Dachstock, Holzterrasse oder Unterstützung in der Bauleitung: Starten Sie rechts die 3-Schritte Smart-Anfrage oder rufen Sie direkt in Frick an.
          </p>

          <img src="images/hero-susi-schmid-holzbau.png" alt="Susanne Susi Schmid, Holz-Susi GmbH in 5070 Frick" style="width:100%;height:200px;object-fit:cover;object-position:center top;border-radius:var(--radius-sm);margin-bottom:16px;" loading="lazy" decoding="async">

          <div class="contact-direct-list">
            <div class="contact-direct-item">
              <div class="contact-direct-role">Standort &amp; Handelsregister</div>
              <div class="contact-direct-person">Holz-Susi GmbH · UID CHE-187.492.373</div>
              <div class="contact-direct-links">Wendelhof 424 · CH-5070 Frick (Kanton Aargau)</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Inhaberin &amp; Geschäftsführerin (Holzbau, Planung &amp; Bauleitung)</div>
              <div class="contact-direct-person">Susanne («Susi») Schmid (Zimmerin EFZ · Projektleiterin · Bauleiterin)</div>
              <div class="contact-direct-links">Telefon: 077 521 96 97 · E-Mail: info@holz-susi.ch</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Öffnungszeiten &amp; Erreichbarkeit</div>
              <div class="contact-direct-person">Montag – Freitag: 07:00 – 12:00 Uhr | 13:00 – 17:30 Uhr</div>
              <div class="contact-direct-links">Samstag &amp; Sonntag geschlossen · Vor-Ort-Termine nach Vereinbarung</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Einsatzgebiet ab 5070 Frick</div>
              <div class="contact-direct-person">Fricktal, Kanton Aargau &amp; angrenzendes Baselland</div>
              <div class="contact-direct-links">Frick, Gipf-Oberfrick, Oeschgen, Eiken, Stein, Laufenburg, Rheinfelden, Möhlin, Aarau, Brugg &amp; Ormalingen</div>
            </div>
          </div>
        </div>

        <!-- RIGHT COLUMN: GEFÜHRTER 3-SCHRITTE SMART-ANFRAGE-ASSISTENT -->
        <div class="wizard-card">
          <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:14px;">
            <div>
              <div class="section-kicker" style="margin-bottom:4px;">3-SCHRITTE SMART-ANFRAGE · HOLZ-SUSI.CH</div>
              <h2 style="font-size:1.35rem;font-weight:700;" id="wpWizardTitle">1. Um welchen Projektbereich geht es bei Ihrem Vorhaben?</h2>
            </div>
            <span class="meta-badge" id="wpActiveAssigneeBadge">Ansprechpartnerin: Susanne («Susi») Schmid</span>
          </div>

          <div class="wp-stepper" aria-label="Fortschritt">
            <div class="wp-step-pill active" id="wpStepPill1">
              <span class="wp-step-num">1</span>
              <span>Thema &amp; Rolle</span>
            </div>
            <div class="wp-step-pill" id="wpStepPill2">
              <span class="wp-step-num">2</span>
              <span>Projektdetails</span>
            </div>
            <div class="wp-step-pill" id="wpStepPill3">
              <span class="wp-step-num">3</span>
              <span>Kontakt &amp; Dossier</span>
            </div>
          </div>

          <form id="isContactForm" onsubmit="return wpSubmitIsLead(event)" novalidate>
            <div style="display:none;" aria-hidden="true">
              <label for="wpHoneypot">Website URL</label>
              <input type="text" id="wpHoneypot" name="website_url" tabindex="-1" autocomplete="off">
            </div>

            <!-- SCHRITT 1: PROJEKTBEREICH -->
            <div class="wp-step-pane active" id="wpStep1">
              <div class="wp-role-grid" id="wpTopicGrid">
                <button type="button" class="wp-role-tile selected" data-topic="Dacherneuerung, Dachfenster & Marderschaden-Sanierung" onclick="wpSelectIsTopic('Dacherneuerung, Dachfenster & Marderschaden-Sanierung')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_HOME}</span>
                    <span class="wp-role-title" data-slot="topic_opt_1">1. Dach &amp; Dachfenster</span>
                  </div>
                  <span class="wp-role-desc">Thermische Dachsanierung, Einbau/Wechsel von Dachfenstern, Marderschaden &amp; Kamin-Rückbau</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Innenausbau, Dachstock, Estrich & Bodenaufbau" onclick="wpSelectIsTopic('Innenausbau, Dachstock, Estrich & Bodenaufbau')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_HAMMER}</span>
                    <span class="wp-role-title" data-slot="topic_opt_2">2. Innenausbau &amp; Böden</span>
                  </div>
                  <span class="wp-role-desc">Dachstock- &amp; Estrichausbau, Täferdecken, Trennwände, Blindboden, Laminat &amp; Renovation</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Terrassendeck, Pergola, Holzfassade & Aussenbereich" onclick="wpSelectIsTopic('Terrassendeck, Pergola, Holzfassade & Aussenbereich')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_SHIELD}</span>
                    <span class="wp-role-title" data-slot="topic_opt_3">3. Terrasse &amp; Fassade</span>
                  </div>
                  <span class="wp-role-desc">Terrassenrost erneuern, Pergola, Sitzbank, hinterlüftete Holzfassade &amp; Holzbauten</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Projektplanung, Bauleitung, Rückbau oder Fachkraft-Einsatz" onclick="wpSelectIsTopic('Projektplanung, Bauleitung, Rückbau oder Fachkraft-Einsatz')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_BUILDING}</span>
                    <span class="wp-role-title" data-slot="topic_opt_4">4. Bauleitung &amp; Partner</span>
                  </div>
                  <span class="wp-role-desc">Bauleitung bei Renovationen, Unterstützung für Architektur/Bauunternehmen oder Rückbau</span>
                </button>
              </div>

              <button type="button" class="btn-cta btn-cta-primary" style="width:100%;" onclick="wpNextStep(2)">
                <span>Weiter zu Schritt 2: Eckdaten &amp; Fotos</span>
                {SVG_ARROW}
              </button>
            </div>

            <!-- SCHRITT 2: ECKDATEN & FOTOS -->
            <div class="wp-step-pane" id="wpStep2">
              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="wpDetail1" class="form-label" id="wpDetail1Label">Art des Vorhabens &amp; Gebäude</label>
                  <input type="text" id="wpDetail1" class="form-input" placeholder="z. B. Einfamilienhaus · Ersatz von 2 Dachfenstern">
                </div>
                <div class="form-field">
                  <label for="wpDetail2" class="form-label" id="wpDetail2Label">Gewünschte Zusammenarbeit (Komplett oder mit Eigenleistung)</label>
                  <input type="text" id="wpDetail2" class="form-input" placeholder="z. B. Komplett-Ausführung oder Mithilfe beim Rückbau">
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label class="form-label">Gewünschter Zeitraum</label>
                <div class="wp-role-grid" id="wpUrgencyGrid" style="margin-bottom:0;">
                  <button type="button" class="wp-role-tile selected" data-urg="Zeitnah (Besichtigung & Kostenschätzung in den nächsten 1–2 Wochen)" onclick="wpSelectIsUrgency('Zeitnah (Besichtigung & Kostenschätzung in den nächsten 1–2 Wochen)')">
                    <span class="wp-role-title">1. Zeitnahe Besichtigung vor Ort</span>
                    <span class="wp-role-desc">Terminvereinbarung und Aufnahme in den nächsten 1–2 Wochen</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urg="In Planung (Umbau oder Renovation für die nächsten Monate)" onclick="wpSelectIsUrgency('In Planung (Umbau oder Renovation für die nächsten Monate)')">
                    <span class="wp-role-title">2. Vorhaben in Planung</span>
                    <span class="wp-role-desc">Frühzeitige Machbarkeitsprüfung, Budgetierung oder Etappenplanung</span>
                  </button>
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label for="contactMessage" class="form-label">Kurze Beschreibung Ihres Projekts oder Ihrer Idee (optional)</label>
                <textarea id="contactMessage" class="form-textarea" placeholder="Beschreiben Sie kurz Ihr Vorhaben oder Ihre Fragen an Susi Schmid..."></textarea>
              </div>

              <div class="wp-upload-zone" style="margin-bottom:16px;">
                <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
                  <div>
                    <div style="font-family:'Lexend',sans-serif;font-size:0.8rem;font-weight:700;color:var(--charcoal-deep);">Optional: Fotos der aktuellen Situation oder Pläne beifügen</div>
                    <div style="font-size:0.75rem;color:var(--text-muted);" id="wpPhotoCounter">0 / 3 Beilagen ausgewählt · Automatisch für das 1-Seiten-PDF-Dossier aufbereitet</div>
                  </div>
                  <button type="button" class="wp-upload-btn" onclick="wpTriggerPhotoUpload()">
                    <span>Foto / Plan auswählen</span>
                  </button>
                  <input type="file" id="wpPhotoInput" accept="image/*" multiple style="display:none;" onchange="wpHandlePhotoFiles(this.files)">
                </div>
                <div class="wp-photo-thumbs" id="wpPhotoThumbs"></div>
              </div>

              <div class="form-grid-2">
                <button type="button" class="btn-cta btn-cta-outline" style="width:100%;" onclick="wpPrevStep()">
                  <span>Zurück zu Schritt 1</span>
                </button>
                <button type="button" class="btn-cta btn-cta-primary" style="width:100%;" onclick="wpNextStep(3)">
                  <span>Weiter zu Schritt 3: Kontaktdaten</span>
                  {SVG_ARROW}
                </button>
              </div>
            </div>

            <!-- SCHRITT 3: KONTAKTDATEN & DOSSIER -->
            <div class="wp-step-pane" id="wpStep3">
              <div class="wp-selftest-banner">
                <strong>Live-Vorschau-Modus (Selbsttest aktiv):</strong> Beim Absenden erstellt das System sofort ein echtes <strong>1-Seiten-A4-PDF-Dossier</strong> im Erscheinungsbild der <strong>Holz-Susi GmbH (5070 Frick)</strong> zum direkten Öffnen und Prüfen.
              </div>

              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactName" class="form-label" data-slot="lbl_name">Vor- und Nachname *</label>
                  <input type="text" id="contactName" name="name" class="form-input" placeholder="z. B. Familie Meier" required>
                </div>
                <div class="form-field">
                  <label for="contactCompany" class="form-label">Architekturbüro / Firma (optional)</label>
                  <input type="text" id="contactCompany" name="company" class="form-input" placeholder="z. B. Privatperson oder Muster Architektur AG">
                </div>
              </div>

              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactLoc" class="form-label">PLZ &amp; Ort der Baustelle *</label>
                  <input type="text" id="contactLoc" name="plz" class="form-input" placeholder="z. B. 5070 Frick / 4310 Rheinfelden" oninput="wpCheckIsPlz(this.value)" required>
                </div>
                <div class="form-field">
                  <label for="contactStreet" class="form-label">Strasse &amp; Hausnummer (optional)</label>
                  <input type="text" id="contactStreet" name="street" class="form-input" placeholder="z. B. Hauptstrasse 12">
                </div>
              </div>

              <div class="wp-plz-badge" id="wpPlzBadge" style="margin-bottom:14px;">
                {SVG_CHECK}
                <span id="wpPlzBadgeText">PLZ 5070: Direktes Kerngebiet Holz-Susi GmbH (Frick / Fricktal)</span>
              </div>

              <div class="form-grid-2" style="margin-bottom:18px;">
                <div class="form-field">
                  <label for="contactEmail" class="form-label" data-slot="lbl_email">E-Mail-Adresse *</label>
                  <input type="email" id="contactEmail" name="email" class="form-input" placeholder="ihre.email@beispiel.ch" required>
                </div>
                <div class="form-field">
                  <label for="contactPhone" class="form-label" data-slot="lbl_phone">Telefon / Mobile (für Rückfragen) *</label>
                  <input type="tel" id="contactPhone" name="phone" class="form-input" placeholder="+41 79 123 45 67" required>
                </div>
              </div>

              <div id="wpFormError" style="display:none;background-color:#FEE2E2;border:1px solid #FCA5A5;color:#991B1B;padding:10px 14px;border-radius:4px;font-size:0.84rem;margin-bottom:14px;"></div>

              <div class="form-grid-2">
                <button type="button" class="btn-cta btn-cta-outline" style="width:100%;" onclick="wpPrevStep()">
                  <span>Zurück zu Schritt 2</span>
                </button>
                <button type="submit" class="btn-cta btn-cta-primary" id="wpSubmitBtn" style="width:100%;" data-slot="btn_submit">
                  <span id="wpSubmitBtnText">1-Seiten-Dossier &amp; Anfrage senden</span>
                  {SVG_ARROW}
                </button>
              </div>
            </div>
          </form>

          <!-- SUCCESS BOX -->
          <div class="wp-success-box" id="wpSuccessBox" aria-live="polite">
            <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
              <div style="display:flex;align-items:center;gap:10px;">
                <span style="width:36px;height:36px;border-radius:4px;background-color:var(--green);color:#FFFFFF;display:inline-flex;align-items:center;justify-content:center;">
                  {SVG_CHECK}
                </span>
                <div>
                  <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.08rem;color:var(--charcoal-deep);">Projekt-Anfrage &amp; 1-Seiten-PDF-Dossier erfolgreich erstellt</div>
                  <div style="font-size:0.78rem;color:var(--text-muted);" id="wpResChannels">1-Seiten-PDF-Dossier bereit zum Download</div>
                </div>
              </div>
              <span class="top-bar-badge" style="background-color:#AF6600;color:#FFFFFF;" id="wpResRef">#WP-2026</span>
            </div>

            <div class="form-grid-2" style="background-color:#F8EEE5;padding:12px 14px;border-radius:4px;border:1px solid var(--border-light);font-size:0.84rem;">
              <div>
                <div style="color:var(--text-muted);font-size:0.75rem;">Zuständige Ansprechpartnerin (5070 Frick):</div>
                <strong style="color:var(--charcoal-deep);" id="wpResAssigned">Susanne («Susi») Schmid</strong>
              </div>
              <div>
                <div style="color:var(--text-muted);font-size:0.75rem;">Verbindliches Rückmelde-Fenster:</div>
                <strong style="color:var(--gold-dark);" id="wpResCallback">Innert 24–48 Stunden (Werktags)</strong>
              </div>
            </div>

            <div>
              <div style="font-family:'Lexend',sans-serif;font-size:0.76rem;font-weight:700;text-transform:uppercase;color:var(--text-muted);margin-bottom:6px;">
                Generierte WhatsApp- &amp; E-Mail-Zusammenfassung:
              </div>
              <div class="wp-wa-preview" id="wpResWaPreview">Anfrage-Zusammenfassung wird geladen...</div>
            </div>

            <div class="form-grid-2">
              <a href="kontakt.html" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-primary btn-sm" id="wpResPdfBtn" style="width:100%;">
                <span>1-Seiten-PDF-Dossier öffnen (A4)</span>
                {SVG_ARROW}
              </a>
              <button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpResetWizard()">
                <span>Weitere Anfrage testen</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <script>
    var wpIsState = {{
      step: 1,
      topic: 'Dacherneuerung, Dachfenster & Marderschaden-Sanierung',
      urgency: 'Zeitnah (Besichtigung & Kostenschätzung in den nächsten 1–2 Wochen)',
      photos: []
    }};

    var wpIsRoleConfig = {{
      'Dacherneuerung, Dachfenster & Marderschaden-Sanierung': {{
        assignee: 'Susanne («Susi») Schmid (Dach & Dachfenster)',
        l1: 'Art des Dachprojekts (Dachsanierung, Dachfenster, Marderschaden)',
        p1: 'z. B. Ersatz von 3 Dachfenstern oder Sanierung Marderschaden',
        l2: 'Gewünschte Ausführung (Komplett oder mit Eigenleistung)',
        p2: 'z. B. Komplett-Ausführung inkl. Eindeckung'
      }},
      'Innenausbau, Dachstock, Estrich & Bodenaufbau': {{
        assignee: 'Susanne («Susi») Schmid (Innenausbau & Renovation)',
        l1: 'Raum / Geschoss & geplante Arbeiten',
        p1: 'z. B. Ausbau Dachstock / Estrich oder neuer Laminatboden',
        l2: 'Gewünschte Zusammenarbeit (Komplett oder aktive Mithilfe)',
        p2: 'z. B. Gerne mit eigener Mithilfe beim Rückbau / Dämmen'
      }},
      'Terrassendeck, Pergola, Holzfassade & Aussenbereich': {{
        assignee: 'Susanne («Susi») Schmid (Terrasse & Holzfassade)',
        l1: 'Projekt im Aussenbereich & ungefähre Grösse',
        p1: 'z. B. Neuer Terrassenrost mit Pergola (ca. 25 m²) oder Holzschalung',
        l2: 'Wunschmaterial oder besondere Anforderungen',
        p2: 'z. B. Einheimisches Holz, inkl. Sitzbank oder Rückbau Altbestand'
      }},
      'Projektplanung, Bauleitung, Rückbau oder Fachkraft-Einsatz': {{
        assignee: 'Susanne («Susi») Schmid (Projektleitung & Bauleitung)',
        l1: 'Auftraggeber-Rolle (Privat, Architekturbüro oder Bauunternehmen)',
        p1: 'z. B. Architekturbüro / Bauunternehmen / Private Bauherrschaft',
        l2: 'Gewünschter Einsatz (Bauleitung, Holzbauplanung oder Zimmerin/Kran)',
        p2: 'z. B. Bauleitung Umbauprojekt oder Verstärkung als Zimmerin EFZ'
      }}
    }};

    function wpUpdateIsHeader() {{
      var titles = {{
        1: '1. Um welchen Projektbereich geht es bei Ihrem Vorhaben?',
        2: '2. Eckdaten zum Projekt, Eigenleistung & Fotos',
        3: '3. Kontaktdaten & Sofort-PDF-Dossier'
      }};
      var tEl = document.getElementById('wpWizardTitle');
      if (tEl) tEl.textContent = titles[wpIsState.step] || titles[1];

      for (var i = 1; i <= 3; i++) {{
        var pane = document.getElementById('wpStep' + i);
        var pill = document.getElementById('wpStepPill' + i);
        if (pane) pane.classList.toggle('active', i === wpIsState.step);
        if (pill) {{
          pill.classList.remove('active', 'done');
          if (i === wpIsState.step) pill.classList.add('active');
          else if (i < wpIsState.step) pill.classList.add('done');
        }}
      }}
    }}

    function wpSelectIsTopic(topic) {{
      wpIsState.topic = topic;
      var tiles = document.querySelectorAll('#wpTopicGrid .wp-role-tile');
      for (var i = 0; i < tiles.length; i++) {{
        tiles[i].classList.toggle('selected', tiles[i].getAttribute('data-topic') === topic);
      }}
      var cfg = wpIsRoleConfig[topic] || wpIsRoleConfig['Dacherneuerung, Dachfenster & Marderschaden-Sanierung'];
      var b = document.getElementById('wpActiveAssigneeBadge');
      if (b) b.textContent = cfg.assignee;
      var l1 = document.getElementById('wpDetail1Label');
      var i1 = document.getElementById('wpDetail1');
      var l2 = document.getElementById('wpDetail2Label');
      var i2 = document.getElementById('wpDetail2');
      if (l1) l1.textContent = cfg.l1;
      if (i1) i1.placeholder = cfg.p1;
      if (l2) l2.textContent = cfg.l2;
      if (i2) i2.placeholder = cfg.p2;
    }}

    function wpSelectIsUrgency(urg) {{
      wpIsState.urgency = urg;
      var tiles = document.querySelectorAll('#wpUrgencyGrid .wp-role-tile');
      for (var i = 0; i < tiles.length; i++) {{
        tiles[i].classList.toggle('selected', tiles[i].getAttribute('data-urg') === urg);
      }}
    }}

    function wpNextStep(target) {{
      wpIsState.step = target;
      wpUpdateIsHeader();
    }}

    function wpPrevStep() {{
      if (wpIsState.step > 1) {{
        wpIsState.step -= 1;
        wpUpdateIsHeader();
      }}
    }}

    function wpTriggerPhotoUpload() {{
      var inp = document.getElementById('wpPhotoInput');
      if (inp) inp.click();
    }}

    function wpCompressImageFile(file, cb) {{
      var reader = new FileReader();
      reader.onload = function(e) {{
        var img = new Image();
        img.onload = function() {{
          var maxSide = 1200;
          var w = img.width;
          var h = img.height;
          if (w > maxSide || h > maxSide) {{
            if (w >= h) {{ h = Math.round(h * (maxSide / w)); w = maxSide; }}
            else {{ w = Math.round(w * (maxSide / h)); h = maxSide; }}
          }}
          var canvas = document.createElement('canvas');
          canvas.width = w;
          canvas.height = h;
          var ctx = canvas.getContext('2d');
          ctx.drawImage(img, 0, 0, w, h);
          cb(canvas.toDataURL('image/jpeg', 0.78));
        }};
        img.src = e.target.result;
      }};
      reader.readAsDataURL(file);
    }}

    function wpRenderPhotos() {{
      var box = document.getElementById('wpPhotoThumbs');
      var cnt = document.getElementById('wpPhotoCounter');
      if (cnt) cnt.textContent = wpIsState.photos.length + ' / 3 Beilagen ausgewählt · Automatisch für das 1-Seiten-PDF-Dossier aufbereitet';
      if (!box) return;
      box.innerHTML = '';
      for (var i = 0; i < wpIsState.photos.length; i++) {{
        (function(idx) {{
          var wrap = document.createElement('div');
          wrap.className = 'wp-thumb-item';
          var im = document.createElement('img');
          im.src = wpIsState.photos[idx];
          im.alt = 'Beilage ' + (idx + 1);
          var btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'wp-thumb-remove';
          btn.textContent = 'x';
          btn.onclick = function() {{ wpRemovePhoto(idx); }};
          wrap.appendChild(im);
          wrap.appendChild(btn);
          box.appendChild(wrap);
        }})(i);
      }}
    }}

    function wpHandlePhotoFiles(files) {{
      if (!files || !files.length) return;
      for (var i = 0; i < files.length; i++) {{
        if (wpIsState.photos.length >= 3) break;
        wpCompressImageFile(files[i], function(b64) {{
          if (wpIsState.photos.length < 3) {{
            wpIsState.photos.push(b64);
            wpRenderPhotos();
          }}
        }});
      }}
    }}

    function wpRemovePhoto(idx) {{
      wpIsState.photos.splice(idx, 1);
      wpRenderPhotos();
    }}

    function wpCheckIsPlz(val) {{
      var badge = document.getElementById('wpPlzBadge');
      var txt = document.getElementById('wpPlzBadgeText');
      if (!badge || !txt) return;
      var m = String(val || '').match(/\\b(\\d{{4}})\\b/);
      if (!m) {{
        badge.className = 'wp-plz-badge';
        return;
      }}
      var plz = parseInt(m[1], 10);
      badge.className = 'wp-plz-badge in-area';
      if (plz >= 5000 && plz <= 5999) {{
        txt.textContent = 'PLZ ' + m[1] + ': Direktes Einsatzgebiet Holz-Susi GmbH (Fricktal / Kanton Aargau)';
      }} else if (plz >= 4000 && plz <= 4999) {{
        txt.textContent = 'PLZ ' + m[1] + ': Direktes Einsatzgebiet Region Baselland / Oberes Fricktal / Rheinfelden';
      }} else {{
        txt.textContent = 'PLZ ' + m[1] + ': Persönliche Projektprüfung durch Susanne («Susi») Schmid';
      }}
    }}

    function wpStripEmojisForDom(str) {{
      return String(str || '').replace(/[\\u{{1F300}}-\\u{{1FAFF}}\\u{{2600}}-\\u{{27BF}}]/gu, '').replace(/\\s+\\n/g, '\\n').trim();
    }}

    function wpResetWizard() {{
      wpIsState.step = 1;
      wpIsState.photos = [];
      wpRenderPhotos();
      var form = document.getElementById('isContactForm');
      if (form) {{
        form.reset();
        form.style.display = 'block';
      }}
      var sBox = document.getElementById('wpSuccessBox');
      if (sBox) sBox.classList.remove('visible');
      var err = document.getElementById('wpFormError');
      if (err) err.style.display = 'none';
      var badge = document.getElementById('wpPlzBadge');
      if (badge) badge.className = 'wp-plz-badge';
      wpSelectIsTopic('Dacherneuerung, Dachfenster & Marderschaden-Sanierung');
      wpSelectIsUrgency('Zeitnah (Besichtigung & Kostenschätzung in den nächsten 1–2 Wochen)');
      wpUpdateIsHeader();
    }}

    function wpSubmitIsLead(e) {{
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

      if (!name || (!phone && !email)) {{
        if (errBox) {{
          errBox.textContent = 'Bitte geben Sie Ihren Namen sowie Ihre E-Mail-Adresse oder Telefonnummer an.';
          errBox.style.display = 'block';
        }}
        return false;
      }}

      var cfg = wpIsRoleConfig[wpIsState.topic] || wpIsRoleConfig['Dacherneuerung, Dachfenster & Marderschaden-Sanierung'];
      var extra = {{}};
      extra[cfg.l1] = d1 || 'Persönliche Vor-Ort-Besichtigung gewünscht';
      extra[cfg.l2] = d2 || 'Abstimmung mit Susanne («Susi») Schmid';

      var btn = document.getElementById('wpSubmitBtn');
      var btnTxt = document.getElementById('wpSubmitBtnText');
      if (btn) btn.disabled = true;
      if (btnTxt) btnTxt.textContent = '1-Seiten-PDF-Dossier wird erstellt...';

      var payload = {{
        client_slug: '{client_slug}',
        source_page: '{source_page}',
        website_url: hp,
        category: wpIsState.topic,
        sparte: wpIsState.topic,
        urgency: wpIsState.urgency,
        name: name,
        company: company,
        street: street,
        plz: loc,
        phone: phone,
        email: email,
        message: msg || ('Holzbau-Anfrage zu ' + wpIsState.topic),
        extra_fields: extra,
        photos: wpIsState.photos,
        self_test_mode: true
      }};

      fetch('/api/lead-submit', {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json' }},
        body: JSON.stringify(payload)
      }})
      .then(function(r) {{ return r.json(); }})
      .then(function(res) {{
        if (btn) btn.disabled = false;
        if (btnTxt) btnTxt.textContent = '1-Seiten-Dossier & Anfrage senden';
        if (!res || !res.ok) {{
          if (errBox) {{
            errBox.textContent = (res && res.error) ? res.error : 'Übermittlung fehlgeschlagen. Bitte versuchen Sie es erneut.';
            errBox.style.display = 'block';
          }}
          return;
        }}
        document.getElementById('isContactForm').style.display = 'none';
        document.getElementById('wpResRef').textContent = res.ref_code || '#WP-2026';
        document.getElementById('wpResAssigned').textContent = res.assigned_to || 'Susanne («Susi») Schmid';
        document.getElementById('wpResCallback').textContent = res.callback_window || 'Innert 24–48 Stunden';
        var chTxt = '1-Seiten-PDF-Dossier erstellt';
        if (res.email_sent) chTxt += ' · E-Mail mit PDF-Anhang zugestellt';
        if (res.whatsapp_sent) chTxt += ' · WhatsApp-Sofortmeldung zugestellt';
        document.getElementById('wpResChannels').textContent = chTxt;
        var pdfBtn = document.getElementById('wpResPdfBtn');
        if (pdfBtn && res.pdf_url) pdfBtn.href = res.pdf_url;
        var waBox = document.getElementById('wpResWaPreview');
        if (waBox) waBox.textContent = wpStripEmojisForDom(res.whatsapp_preview_text || '');
        document.getElementById('wpSuccessBox').classList.add('visible');
      }})
      .catch(function() {{
        if (btn) btn.disabled = false;
        if (btnTxt) btnTxt.textContent = '1-Seiten-Dossier & Anfrage senden';
        if (errBox) {{
          errBox.textContent = 'Netzwerkfehler bei der Übermittlung. Bitte schreiben Sie direkt an info@holz-susi.ch oder rufen Sie 077 521 96 97 an.';
          errBox.style.display = 'block';
        }}
      }});
      return false;
    }}

    (function() {{
      try {{
        var params = new URLSearchParams(window.location.search);
        var t = (params.get('thema') || '').toLowerCase();
        var map = {{
          'dach': 'Dacherneuerung, Dachfenster & Marderschaden-Sanierung',
          'dachfenster': 'Dacherneuerung, Dachfenster & Marderschaden-Sanierung',
          'innenausbau': 'Innenausbau, Dachstock, Estrich & Bodenaufbau',
          'terrasse': 'Terrassendeck, Pergola, Holzfassade & Aussenbereich',
          'fassade': 'Terrassendeck, Pergola, Holzfassade & Aussenbereich',
          'planung': 'Projektplanung, Bauleitung, Rückbau oder Fachkraft-Einsatz',
          'bauleitung': 'Projektplanung, Bauleitung, Rückbau oder Fachkraft-Einsatz'
        }};
        if (map[t]) {{
          wpSelectIsTopic(map[t]);
        }}
      }} catch(err) {{}}
    }})();
  </script>
"""


# 3. Alle Seiten für Variante 1 (Vollversion) schreiben
v1_pages = [
    ("index.html", "Holz-Susi GmbH · 5070 Frick | Holzbau, Dachsanierung, Innenausbau & Bauleitung im Fricktal", "startseite", V1_INDEX_BODY),
    ("leistungen.html", "Leistungen: Dachsanierung, Dachfenster, Innenausbau, Terrasse & Bauleitung | Holz-Susi GmbH Frick", "leistungen", V1_LEISTUNGEN_BODY),
    ("referenzen.html", "Vorher/Nachher-Referenzprojekte & Fricktaler Partnernetzwerk | Holz-Susi GmbH 5070 Frick", "referenzen", V1_REFERENZEN_BODY),
    ("ueber-uns.html", "Über Susanne («Susi») Schmid, Sponsoring Selina Burger & Bluescht-Beiz Wendelhof | Holz-Susi GmbH", "ueber-uns", V1_UEBER_UNS_BODY),
    ("kontakt.html", "Kontakt & 3-Schritte Smart-Anfrage | Holz-Susi GmbH · Wendelhof 424, 5070 Frick", "kontakt", build_kontakt_body("holz-susi-v1", "preview-holz-susi/kontakt.html")),
]

for fname, title, nav_key, body in v1_pages:
    full_html = render_v1_shell(fname, title, nav_key, body)
    (V1_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V1] Wrote {fname} ({len(full_html)} bytes)")

# 4. Alle Seiten für Variante 2 (Zeigeversion / Vorschau-Entwurf) schreiben
v2_pages = [
    ("index.html", "Holz-Susi GmbH · 5070 Frick (Zeigeversion / Vorschau-Entwurf) | Vom ersten Gedanken bis zum letzten Handgriff", "startseite", V2_INDEX_BODY),
    ("kontakt.html", "Kontakt & 3-Schritte Smart-Anfrage (Zeigeversion) | Holz-Susi GmbH 5070 Frick", "kontakt", build_kontakt_body("holz-susi", "preview-holz-susi-v2/kontakt.html")),
]

for fname, title, nav_key, body in v2_pages:
    full_html = render_v2_shell(fname, title, nav_key, body)
    (V2_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V2] Wrote {fname} ({len(full_html)} bytes)")

for stale in ["leistungen.html", "referenzen.html", "projekte.html", "ueber-uns.html"]:
    p = V2_DIR / stale
    if p.exists():
        p.unlink()

# 5. Partner-Attribution (#wpPartnerModal für David Hügli Magnet XS) injizieren
subprocess.run(["python3", str(BASE_DIR / "scripts" / "inject_partner_attribution.py")], check=True)

# 6. Studio Cockpit v4.0 (cockpit.html) für beide Varianten generieren
subprocess.run(["python3", str(BASE_DIR / "scripts" / "build_client_cockpit.py"), "--slug", "preview-holz-susi"], check=True)
subprocess.run(["python3", str(BASE_DIR / "scripts" / "build_client_cockpit.py"), "--slug", "preview-holz-susi-v2"], check=True)

# 7. Compile Site Pipeline (Pre-Build Gates & Airbag)
subprocess.run(["python3", str(BASE_DIR / "scripts" / "compile_site.py"), "--site", "preview-holz-susi", "--skip-device-audit"], check=True)
subprocess.run(["python3", str(BASE_DIR / "scripts" / "compile_site.py"), "--site", "preview-holz-susi-v2", "--skip-device-audit"], check=True)
print("Successfully built and compiled preview-holz-susi and preview-holz-susi-v2.")

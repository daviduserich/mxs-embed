#!/usr/bin/env python3
"""
Generator für die WebPilot-Referenz-Aufbereitung von joma-solar.ch (JOMA Solar GmbH, Wettingen AG):
- Variante 1 (Vollversion): /home/brainuser/workspaces/mxs-embed/preview-joma
  Live-URL: https://vorschau.magnet-xs.ch/joma-vollversion/ (5 voll ausgebaute Seiten + Studio Cockpit v4.0)
- Variante 2 (Zeigeversion / Vorschau-Entwurf): /home/brainuser/workspaces/mxs-embed/preview-joma-v2
  Live-URL: https://vorschau.magnet-xs.ch/joma-v2/ (2 ausgearbeitete Beispiel-Seiten: Startseite inkl. Solar-Rechner + 3-Schritte Smart-Anfrage,
  plus anschauliche Themenbereich-Vorschaukarten für die 3 weiteren Unterseiten).

Strikt nach:
- UI-LAYOUT-RULES.md (Canary: UI-LAYOUT-2026-V1, #UI-01, #UI-02, #UI-13, #UI-14, #UI-16 Evolution-Modus)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1, 0 Eszett, 100 % Schweizer Hochdeutsch)
- #SYS-01 (Kein oberer Versions-/Cockpit-Balken, 0 Hinweise auf Vollversion/Cockpit auf Kundenseiten)
"""

import json
import subprocess
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
V1_DIR = BASE_DIR / "preview-joma"
V2_DIR = BASE_DIR / "preview-joma-v2"

V1_DIR.mkdir(parents=True, exist_ok=True)
V2_DIR.mkdir(parents=True, exist_ok=True)

BEFORE_INVENTORY = {
    "source_url": "https://www.joma-solar.ch/",
    "crawled_at": "2026-11-05",
    "company_name": "JOMA Solar GmbH",
    "legal_entity": "JOMA Solar GmbH",
    "uid": "CHE-334.571.911",
    "chid": "CH-400-4454055-9",
    "shab_date": "2025-02-13",
    "claim": "Solar einfach effizient",
    "subline": "Solar- und Batteriesysteme für Privat- und Geschäftskunden im Kanton Aargau und der Region Baden/Wettingen. Von der persönlichen Beratung über die Planung bis zur fachgerechten Installation.",
    "address": {
        "street": "Tägerhardstrasse 90",
        "zip": "5430",
        "city": "Wettingen",
        "canton": "AG",
        "country": "Schweiz"
    },
    "contact": {
        "email": "info@joma-solar.ch",
        "phone_primary": "+41 56 558 98 67",
        "phone_display": "056 558 98 67",
        "phone_jonathan": "+41 56 558 48 82",
        "phone_jonathan_display": "056 558 48 82",
        "phone_marco": "+41 56 558 98 67",
        "phone_marco_display": "056 558 98 67",
        "social": {
            "instagram": "https://www.instagram.com/joma_solar/",
            "linkedin": "https://www.linkedin.com/company/joma-solar-gmbh/",
            "facebook": "https://www.facebook.com/profile.php?id=61557713833298"
        }
    },
    "team": [
        {
            "name": "Jonathan Muggli",
            "role": "Gründer & Geschäftsführer",
            "phone": "056 558 48 82",
            "phone_href": "tel:+41565584882",
            "image": "images/portrait-jonathan-muggli.jpg",
            "qualification": "Elektroinstallateur EFZ · Energietechniker HF · Wirtschaftsingenieur FH",
            "bio": "Mit einer Ausbildung als Elektroinstallateur EFZ, Energietechniker HF und Wirtschaftsingenieur FH bringe ich eine breite Expertise mit Fokus auf Solarenergie, ZEV-Abrechnungssysteme und intelligentes Energiemanagement ein."
        },
        {
            "name": "Marco Keller",
            "role": "Gründer & Geschäftsführer",
            "phone": "056 558 98 67",
            "phone_href": "tel:+41565589867",
            "image": "images/portrait-marco-keller.jpg",
            "qualification": "Wirtschaftsingenieur · Über 10 Jahre Photovoltaik-Erfahrung",
            "bio": "Mit über einem Jahrzehnt Erfahrung in der Photovoltaikbranche und einem Abschluss als Wirtschaftsingenieur habe ich mich auf die wirtschaftliche Planung, Installation und schlüsselfertige Abwicklung von PV-Projekten spezialisiert."
        },
        {
            "name": "Tino Seiler",
            "role": "Leiter Montage und Ausführung",
            "phone": "056 558 98 67",
            "phone_href": "tel:+41565589867",
            "image": "images/portrait-tino-seiler.jpg",
            "qualification": "Elektroplaner · Elektroinstallateur · Versierter Solarteur",
            "bio": "Erfahrener Elektroplaner, Elektroinstallateur und versierter Solarteur mit umfassender Expertise in der Elektrobranche. Präzise und effizient in der Umsetzung von Projekten auf jedem Gebäudetyp."
        },
        {
            "name": "Mario Grab",
            "role": "Solarmonteur & Dachspezialist",
            "phone": "056 558 98 67",
            "phone_href": "tel:+41565589867",
            "image": "images/portrait-mario-grab.jpg",
            "qualification": "Gelernter Dachdecker · Spezialist für Dachaufbauten & Indach/Aufdach",
            "bio": "Als gelernter Dachdecker bringt Mario Grab fundiertes Wissen über Dachaufbauten und Gebäudehüllen mit. Durch praktische und theoretische Erfahrung sorgt er für absolut wind- und wetterfeste Dachmontagen."
        },
        {
            "name": "Sascha Tsap",
            "role": "Solarmonteur",
            "phone": "056 558 98 67",
            "phone_href": "tel:+41565589867",
            "image": "images/portrait-sascha-tsap.jpg",
            "qualification": "Erfahrener Dachdecker & Montage-Fachmann",
            "bio": "Sascha Tsap ist ein erfahrener Dachdecker aus der Ukraine. Er zeichnet sich durch höchste Sorgfalt und Zuverlässigkeit in der Montage aus und trägt massgeblich zum erfolgreichen Abschluss unserer Solarprojekte bei."
        }
    ],
    "references": [
        {
            "city": "Wettingen (Attenhoferstrasse)",
            "type": "Dachsanierung · Kombination Indach & Aufdach",
            "system": "3S Swiss Solar Indachsystem + AIKO Aufdach-Module",
            "power_kwp": "11.54 kWp",
            "yield_mwh": "11.0 MWh / Jahr",
            "image": "images/ref-wettingen-indach.jpg",
            "desc": "An der Attenhoferstrasse in Wettingen wurde im Zuge einer Dachsanierung eine kombinierte Indach- und Aufdachanlage realisiert. Das 3S-Indachsystem fügt sich nahtlos in die Dachhaut ein, ergänzt durch leistungsstarke AIKO-Module."
        },
        {
            "city": "Riniken (AG)",
            "type": "Flachdach & Blechfalzdach · Ost / West & Süd",
            "system": "AIKO A470-MAH54Mw Neostar 2P (Aufständerung)",
            "power_kwp": "18.80 kWp",
            "yield_mwh": "19.7 MWh / Jahr",
            "image": "images/ref-riniken-18kwp.jpg",
            "desc": "Kombination aus Flachdach und Blechfalzdach mit Ost-, West- und Südausrichtung. Dadurch wird eine besonders gleichmässige Stromproduktion vom frühen Morgen bis in die Abendstunden erreicht."
        },
        {
            "city": "Baden-Rütihof (MFH ZEV)",
            "type": "Mehrfamilienhaus Flachdach · ZEV mit Smart-Me",
            "system": "68 × JA Solar JAM54D40-450/LB (Ost/West + Süd)",
            "power_kwp": "30.60 kWp",
            "yield_mwh": "31.0 MWh / Jahr",
            "image": "images/ref-ruetihof-zev-30kwp.jpg",
            "desc": "Realisierung auf einem Mehrfamilienhaus inklusive vorgängiger Beratung zum Eigenverbrauchsmodell (ZEV / VNB) und Begleitung der Eigentümerversammlung. Ausgestattet mit Smart-Me Zählern für die präzise Parteien-Abrechnung."
        },
        {
            "city": "Baden-Rütihof (Grossprojekt)",
            "type": "Mehrparteien-Anlage · 4 Wechselrichter & Speicher",
            "system": "Megasol M420-HC120-b Full Black Optik (Südwest / Nordost)",
            "power_kwp": "55.47 kWp",
            "yield_mwh": "55.0 MWh / Jahr",
            "image": "images/ref-ruetihof-55kwp.jpg",
            "desc": "Grossprojekt in Full-Black-Optik mit vier individuell konfigurierten Wechselrichtern für optimierten Eigenverbrauch pro Partei, integriertem Batteriespeicher und zentralem NA-Schutz."
        },
        {
            "city": "Fislisbach (AG)",
            "type": "Ziegeldach dachparallel · Südwest / Nordost",
            "system": "Trina Solar Vertex S+ TOPCon TSM-445NEG9R.28",
            "power_kwp": "24.03 kWp",
            "yield_mwh": "24.0 MWh / Jahr",
            "image": "images/ref-fislisbach-24kwp.jpg",
            "desc": "Grosszügige dachparallele Photovoltaikanlage auf einem Ziegeldach in Fislisbach. Durch die beidseitige Belegung (Südwest / Nordost) mit Trina Vertex S+ TOPCon Modulen entsteht ein hoher Tagesertrag für Haushalt, Wärmepumpe und E-Mobilität."
        },
        {
            "city": "Schöfflisdorf (ZH)",
            "type": "Einfamilienhaus Ziegeldach · Dachparallel Süd",
            "system": "AIKO A465-MAH54Mw Neostar 2P",
            "power_kwp": "13.95 kWp",
            "yield_mwh": "16.0 MWh / Jahr",
            "image": "images/ref-schoefflisdorf-14kwp.jpg",
            "desc": "Optimal nach Süden ausgerichtete Einfamilienhaus-Anlage auf Ziegeldach mit Hochleistungsmodulen von AIKO. Erzielt dank Südausrichtung und hoher Moduleffizienz überdurchschnittliche 16 MWh Jahresproduktion."
        }
    ],
    "faqs": [
        {
            "q": "Benötige ich eine Baubewilligung für eine Solaranlage?",
            "a": "In den meisten Fällen reicht im Kanton Aargau und Zürich ein vereinfachtes Meldeverfahren; in Kern- oder Schutzzonen ist ein Baugesuch erforderlich. JOMA Solar übernimmt für Sie die komplette Abklärung, sämtliche Baueingaben und die Koordination mit der Gemeinde."
        },
        {
            "q": "Übernimmt JOMA Solar auch die Anmeldung beim Energieversorger und für Fördergelder?",
            "a": "Ja, vollständig. Wir erledigen das Anschlussgesuch (TAG), die Sicherheitsnachweise, die Anmeldung beim lokalen Verteilnetzbetreiber (VNB) sowie die Beantragung der Einmalvergütung (EIV / Pronovo) bis zur schlüsselfertigen Inbetriebnahme."
        },
        {
            "q": "Lohnt sich ein Batteriespeicher für mein Einfamilienhaus oder Gewerbe?",
            "a": "Ein Batteriespeicher erhöht Ihren Eigenverbrauch von typischerweise 30 % auf bis zu 75–85 %, da der tagsüber produzierte Solarstrom am Abend und in der Nacht genutzt wird. Im Gewerbe glättet der Speicher zudem teure Lastspitzen (Peak-Shaving). Auf Wunsch integrieren wir auch eine Notstromfunktion."
        },
        {
            "q": "Kann ich meine Solaranlage später um Wärmepumpe, Wallbox oder Speicher erweitern?",
            "a": "Ja. Wir planen jede Anlage vorausschauend mit den nötigen Leistungsreserven im Wechselrichter und in der Hausverteilung. Über das Energiemanagement (Solar Manager) lassen sich Ladestationen (E-Mobilität), Wärmepumpen und Batteriespeicher jederzeit intelligent einbinden."
        },
        {
            "q": "Wie lange dauert die Montage einer Solaranlage auf einem Einfamilienhaus?",
            "a": "Die eigentliche Dach- und Elektromontage auf einem Einfamilienhaus dauert in der Regel nur 3 bis 5 Arbeitstage. Da in unserem Team sowohl erfahrene Elektroinstallateure/Elektroplaner als auch gelernte Dachdecker Hand in Hand arbeiten, erfolgt die Umsetzung aus einem Guss."
        },
        {
            "q": "Wie funktioniert das JOMA Solar-Contracting für Unternehmen ohne eigene Investition?",
            "a": "Beim Contracting übernimmt JOMA Solar die Planung, Finanzierung, Installation und den laufenden Betrieb der Photovoltaikanlage auf Ihrem Gewerbedach. Ihr Unternehmen bezieht den sauberen Solarstrom direkt vom eigenen Dach zu langfristig kalkulierbaren, günstigen Konditionen, ohne eigene Anfangsinvestition."
        }
    ]
}

# 1. before.json & company.json & config.json & site.json für V1 und V2 schreiben
for target_dir, slug_name, pub_slug in [
    (V1_DIR, "preview-joma", "joma-vollversion"),
    (V2_DIR, "preview-joma-v2", "joma-v2"),
]:
    (target_dir / "before.json").write_text(json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False), encoding="utf-8")
    (target_dir / "company.json").write_text(json.dumps({
        "name": "JOMA Solar GmbH",
        "slug": pub_slug,
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
        "design_mode": "evolution"
    }, indent=2, ensure_ascii=False), encoding="utf-8")

v1_config = {
    "company_name": "JOMA Solar GmbH · Wettingen (AG)",
    "slug": "preview-joma",
    "public_slug": "joma-vollversion",
    "cockpit_token": "joma2026",
    "template": "solar-energy-kmu-v1",
    "partner_id": "jenny",
    "pages": ["index.html", "leistungen.html", "referenzen.html", "ueber-uns.html", "kontakt.html"]
}
(V1_DIR / "config.json").write_text(json.dumps(v1_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V1_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-joma",
    "public_slug": "joma-vollversion",
    "token": "joma2026",
    "name": "JOMA Solar GmbH · Solaranlagen & Batteriesysteme Wettingen (Vollversion)",
    "Updated": "2026-11-05",
    "PagesCount": 5,
    "ReferencesCount": 7,
    "TeamCount": 5
}, indent=2, ensure_ascii=False), encoding="utf-8")

v2_config = dict(v1_config)
v2_config.update({
    "company_name": "JOMA Solar GmbH (Zeigeversion / Vorschau-Entwurf)",
    "slug": "preview-joma-v2",
    "public_slug": "joma-v2",
    "cockpit_token": "joma2026",
    "template": "solar-energy-kmu-preview-v2",
    "pages": ["index.html", "kontakt.html"]
})
(V2_DIR / "config.json").write_text(json.dumps(v2_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V2_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-joma-v2",
    "public_slug": "joma-v2",
    "token": "joma2026",
    "name": "JOMA Solar GmbH (Zeigeversion / Vorschau-Entwurf)",
    "Updated": "2026-11-05",
    "PagesCount": 2,
    "ReferencesCount": 7,
    "TeamCount": 5
}, indent=2, ensure_ascii=False), encoding="utf-8")

print("Wrote before.json, company.json, config.json, site.json for V1 and V2.")

SHARED_CSS = """
    :root {
      --charcoal: #1E2532;
      --charcoal-deep: #12161F;
      --charcoal-mid: #333F54;
      --gold: #D64B13;
      --gold-hover: #B83A09;
      --gold-dark: #B83A09;
      --gold-soft: #FFF4ED;
      --gold-border: #F7D4C1;
      --crimson: #D64B13;
      --crimson-soft: #FFF4ED;
      --green: #15803D;
      --green-soft: #DCFCE7;
      --bg-page: #FAFBFD;
      --bg-card: #FFFFFF;
      --bg-Warm: #F3F5FA;
      --text-main: #12161F;
      --text-body: #2C3545;
      --text-muted: #4E5B70;
      --border-light: #E2E8F0;
      --border-strong: #CBD5E1;
      --radius-sm: 4px;
      --radius-md: 8px;
      --shadow-sm: 0 2px 10px rgba(18, 22, 31, 0.05);
      --shadow-md: 0 12px 30px rgba(18, 22, 31, 0.08);
      --shadow-lg: 0 20px 44px rgba(18, 22, 31, 0.12);
      --container: 1180px;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    ::selection {
      background-color: rgba(214, 75, 19, 0.18);
      color: #12161F;
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

    /* Sub-Topbar (Wettingen AG & Direktkontakt Geschäftsführer) */
    .top-bar {
      background-color: #F3F5FA;
      color: #2C3545;
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
      background-color: #FFF4ED;
      color: #B83A09;
      border: 1px solid #F7D4C1;
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
      color: #12161F;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-height: 32px;
      padding: 5px 8px;
    }
    .top-bar-links a:hover {
      color: #D64B13;
    }

    /* Sticky Main Header (#UI-02: 1-Zeilen-Navigations-Gesetz) */
    .site-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background-color: rgba(255, 255, 255, 0.97);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border-light);
      box-shadow: 0 2px 12px rgba(18, 22, 31, 0.05);
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
      min-height: 40px;
      padding: 4px 0;
    }
    .brand-logo {
      width: 138px;
      height: 26px;
      object-fit: contain;
      flex-shrink: 0;
    }
    .brand-text {
      display: flex;
      flex-direction: column;
      border-left: 1px solid var(--border-strong);
      padding-left: 10px;
    }
    .brand-name {
      font-family: 'Lexend', sans-serif;
      font-size: 0.82rem;
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
      color: #B83A09;
      background: transparent;
      border-bottom-color: #D64B13;
    }
    .nav-link-preview {
      color: var(--text-muted);
      background: transparent;
      border: none;
      border-bottom: 2px dashed rgba(214, 75, 19, 0.38);
      font-size: 0.86rem;
    }
    .nav-link-preview:hover {
      color: #B83A09;
      background: transparent;
      border-bottom-color: #D64B13;
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
      background-color: #D64B13;
      color: #FFFFFF;
      border-color: #D64B13;
      font-weight: 600;
    }
    .btn-cta-gold:hover {
      background-color: #B83A09;
      color: #FFFFFF;
      border-color: #B83A09;
      transform: translateY(-1px);
    }
    .btn-cta-primary {
      background-color: #D64B13;
      color: #FFFFFF;
      border-color: #D64B13;
    }
    .btn-cta-primary:hover {
      background-color: #B83A09;
      color: #FFFFFF;
      border-color: #B83A09;
    }
    .btn-cta-outline {
      background-color: #FFFFFF;
      color: #12161F;
      border-color: var(--border-strong);
    }
    .btn-cta-outline:hover {
      border-color: #D64B13;
      color: #B83A09;
      background-color: var(--gold-soft);
    }
    .btn-cta-outline-light {
      background-color: #FFFFFF;
      color: #12161F;
      border-color: rgba(214, 75, 19, 0.35);
    }
    .btn-cta-outline-light:hover {
      background-color: #FFF4ED;
      color: #B83A09;
      border-color: #D64B13;
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
      color: #12161F;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }
    .mobile-drawer {
      display: none;
      flex-direction: column;
      gap: 8px;
      padding: 16px 24px 22px;
      background-color: #FAFBFD;
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
      color: #12161F;
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
      color: #B83A09;
      border-style: dashed;
      border-color: rgba(214, 75, 19, 0.45);
    }

    /* Hero Section – Hell, freundlich & architektonisch klar (#UI-16 Evolution & #UI-02 Bottom-Edge Baseline Lock) */
    .hero-section {
      background: linear-gradient(135deg, #FFFFFF 0%, #F5F7FB 58%, #FFF4ED 100%);
      background-color: #FAFBFD;
      color: #12161F;
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
      color: #12161F;
      line-height: 1.14;
      margin-bottom: 18px;
    }
    .hero-title span {
      color: #D64B13;
    }
    .hero-lead {
      font-size: 1.04rem;
      color: #2C3545;
      line-height: 1.66;
      margin-bottom: 26px;
    }
    .hero-actions {
      display: flex;
      flex-wrap: wrap;
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
      border-left: 3px solid #D64B13;
      border-radius: var(--radius-sm);
      padding: 10px 14px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 2px;
      box-shadow: var(--shadow-sm);
    }
    .hero-badge-val {
      font-family: 'Lexend', sans-serif;
      font-size: 0.9rem;
      font-weight: 700;
      color: #B83A09;
    }
    .hero-badge-lbl {
      font-size: 0.78rem;
      color: #2C3545;
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
      background-color: #F3F5FA;
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
      background: linear-gradient(135deg, #FFFFFF 0%, #FFF4ED 100%);
      background-color: #FFF4ED;
      color: #12161F;
      border-color: #F7D4C1;
      border-top: 4px solid #D64B13;
    }
    .content-card.card-dark h3 {
      color: #12161F;
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
      font-family: 'Lexend', sans-serif;
      font-size: 0.71rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
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
      background-color: #FFF4ED;
      color: #D64B13;
      border: 1px solid #F7D4C1;
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

    /* Interactive Solar Calculator Styles */
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
      justify-content: space-between;
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
      font-size: 0.84rem;
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
      font-size: 1.15rem;
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
      background-color: #F3F5FA;
      border-top: 2px dashed rgba(214, 75, 19, 0.35);
      border-bottom: 2px dashed rgba(214, 75, 19, 0.35);
      padding: 76px 0 88px;
    }
    .preview-scope-banner {
      background-color: #FFFFFF;
      color: #12161F;
      border: 2px dashed #D64B13;
      border-radius: var(--radius-md);
      padding: 28px 30px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-md);
    }
    .preview-module-card {
      background-color: #FFFFFF;
      border: 2px dashed #D64B13;
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
      background-color: #F3F5FA;
      color: #12161F;
      padding: 68px 0 36px;
      border-top: 3px solid #D64B13;
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
      color: #12161F;
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
      color: #2C3545;
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
      color: #D64B13;
    }
    .footer-bottom {
      padding-top: 26px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      font-size: 0.82rem;
      color: #2C3545;
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
      background-color: rgba(15, 23, 30, 0.76);
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
      background-color: #D64B13;
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
      justify-content: space-between;
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
      background-color: #FFF4ED;
      color: #D64B13;
      border: 1px solid #F7D4C1;
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
      box-shadow: 0 0 0 3px rgba(214, 75, 19, 0.16);
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
      color: #7C2304;
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
        width: 98px;
        height: 19px;
      }
      .brand-text {
        min-width: 0;
      }
      .brand-name {
        font-size: 0.76rem;
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
"""

SVG_CHECK = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>'
SVG_ARROW = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'
SVG_SUN = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>'
SVG_BATTERY = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="6" width="18" height="12" rx="2" ry="2"/><line x1="23" y1="13" x2="23" y2="11"/><polyline points="11 10 8 12 11 12 8 14"/></svg>'
SVG_ZAP = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'
SVG_SHIELD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
SVG_AWARD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>'
SVG_USERS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
SVG_BUILDING = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"/><line x1="9" y1="22" x2="9" y2="18"/><line x1="15" y1="22" x2="15" y2="18"/><line x1="8" y1="6" x2="10" y2="6"/><line x1="14" y1="6" x2="16" y2="6"/><line x1="8" y1="10" x2="10" y2="10"/><line x1="14" y1="10" x2="16" y2="10"/><line x1="8" y1="14" x2="10" y2="14"/><line x1="14" y1="14" x2="16" y2="14"/></svg>'
SVG_MAP_PIN = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'
SVG_PHONE = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
SVG_MAIL = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'


def render_references_grid(limit: int = 6, is_v2: bool = False) -> str:
    cards = []
    for ref in BEFORE_INVENTORY["references"][:limit]:
        cta_html = (
            f'''<button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Referenzprojekt {ref['city']} ({ref['power_kwp']})', '{ref['type']} · {ref['system']} · {ref['yield_mwh']}', 'Jonathan Muggli &amp; Marco Keller')">
              <span>Projekt-Details ({ref['power_kwp']}) ansehen</span>
              {SVG_ARROW}
            </button>'''
            if is_v2
            else f'''<a href="kontakt.html?thema=efh" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Ähnliche Anlage für mein Dach anfragen</span>
              {SVG_ARROW}
            </a>'''
        )
        cards.append(f"""
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="{ref['image']}" alt="JOMA Solar Referenzprojekt {ref['city']} ({ref['power_kwp']})" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">{ref['power_kwp']}</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">{ref['yield_mwh']}</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:6px;">{ref['city']}</h3>
              <p style="font-size:0.82rem;font-weight:700;color:var(--gold-dark);margin-bottom:10px;">{ref['type']}</p>
              <p style="font-size:0.89rem;color:var(--text-body);margin-bottom:12px;">{ref['desc']}</p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span><strong>System:</strong> {ref['system']}</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Jahresertrag:</strong> {ref['yield_mwh']} sauberer Solarstrom</span></div>
              </div>
            </div>
            {cta_html}
          </div>
        </div>""")
    return '<div class="grid-3">\n' + "\n".join(cards) + "\n      </div>"


def render_faqs_grid() -> str:
    cards = []
    for idx, f in enumerate(BEFORE_INVENTORY["faqs"]):
        cards.append(f"""
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Praxis-Antwort #{idx+1}</span>
              <span class="icon-box">{SVG_SUN}</span>
            </div>
            <h3 style="font-size:1.14rem;font-weight:700;margin-bottom:10px;">{f['q']}</h3>
            <p style="font-size:0.9rem;color:var(--text-body);line-height:1.62;">{f['a']}</p>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Persönliche Einschätzung einholen</span>
            {SVG_ARROW}
          </a>
        </div>""")
    return '<div class="grid-2">\n' + "\n".join(cards) + "\n      </div>"


def render_solar_calculator() -> str:
    return f"""
  <!-- INTERAKTIVER SOLAR- & BATTERIE-POTENZIAL-RECHNER -->
  <section data-section="solarrechner" id="solarrechner" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="calc_kicker">INTERAKTIVER POTENZIAL-RECHNER · EIGENVERBRAUCH &amp; JAHRESERTRAG</div>
        <h2 class="section-title" data-slot="calc_title">Welches Solarpotenzial steckt auf Ihrem Dach im Aargau?</h2>
        <p class="section-desc" data-slot="calc_desc">
          Wählen Sie Ihren Gebäudetyp, Ihre geschätzte Dachgrösse und Ihre gewünschten Verbraucher. Unser Rechner vergleicht Ihr Vorhaben direkt mit realisierten JOMA-Referenzanlagen aus Wettingen, Riniken, Fislisbach und Rütihof:
        </p>
      </div>

      <div class="grid-2">
        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">In 15 Sekunden konfigurieren</span>
              <span class="icon-box">{SVG_ZAP}</span>
            </div>
            <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:14px;">1. Gebäudetyp &amp; Nutzung wählen</h3>
            <div class="calc-option-grid" id="jomaCalcTypeGrid">
              <button type="button" class="calc-option-btn active" data-type="efh" onclick="jomaSetCalc('type','efh')">
                <span class="calc-opt-title">Einfamilienhaus</span>
                <span class="calc-opt-sub">EFH · Aufdach oder 3S-Indach</span>
              </button>
              <button type="button" class="calc-option-btn" data-type="mfh" onclick="jomaSetCalc('type','mfh')">
                <span class="calc-opt-title">Mehrfamilienhaus</span>
                <span class="calc-opt-sub">MFH · ZEV &amp; Smart-Me Zähler</span>
              </button>
              <button type="button" class="calc-option-btn" data-type="gewerbe" onclick="jomaSetCalc('type','gewerbe')">
                <span class="calc-opt-title">Gewerbe &amp; Industrie</span>
                <span class="calc-opt-sub">Grossanlage oder Contracting</span>
              </button>
            </div>

            <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:14px;">2. Dachgrösse &amp; Leistungsbereich</h3>
            <div class="calc-option-grid" id="jomaCalcSizeGrid">
              <button type="button" class="calc-option-btn" data-size="small" onclick="jomaSetCalc('size','small')">
                <span class="calc-opt-title">Kompakt (~12 kWp)</span>
                <span class="calc-opt-sub">Ca. 55–70 m² Dachfläche</span>
              </button>
              <button type="button" class="calc-option-btn active" data-size="medium" onclick="jomaSetCalc('size','medium')">
                <span class="calc-opt-title">Optimal (~19–24 kWp)</span>
                <span class="calc-opt-sub">Ca. 85–115 m² Dachfläche</span>
              </button>
              <button type="button" class="calc-option-btn" data-size="large" onclick="jomaSetCalc('size','large')">
                <span class="calc-opt-title">Grossdach (30–55 kWp)</span>
                <span class="calc-opt-sub">Ab 140 m² · MFH &amp; Gewerbe</span>
              </button>
            </div>

            <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:14px;">3. Speicher &amp; Grossverbraucher</h3>
            <div class="calc-option-grid" id="jomaCalcStorageGrid" style="margin-bottom:0;">
              <button type="button" class="calc-option-btn active" data-storage="speicher_sm" onclick="jomaSetCalc('storage','speicher_sm')">
                <span class="calc-opt-title">Speicher + App</span>
                <span class="calc-opt-sub">Batteriespeicher &amp; Solar Manager</span>
              </button>
              <button type="button" class="calc-option-btn" data-storage="wp_ev" onclick="jomaSetCalc('storage','wp_ev')">
                <span class="calc-opt-title">Wärmepumpe &amp; E-Auto</span>
                <span class="calc-opt-sub">Wallbox &amp; Heizungs-Kopplung</span>
              </button>
              <button type="button" class="calc-option-btn" data-storage="notstrom" onclick="jomaSetCalc('storage','notstrom')">
                <span class="calc-opt-title">Autarkie &amp; Notstrom</span>
                <span class="calc-opt-sub">Absicherung bei Netzunterbruch</span>
              </button>
            </div>
          </div>
          <div style="padding-top:14px;border-top:1px solid var(--border-light);font-size:0.82rem;color:var(--text-body);display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;">
            <span>Erfahrungswerte aus realisierten Anlagen im Kanton Aargau</span>
            <strong style="color:var(--gold-dark);font-family:'Lexend',sans-serif;">JOMA Solar Wettingen</strong>
          </div>
        </div>

        <div class="content-card card-dark">
          <div>
            <div class="card-badge-row">
              <span class="top-bar-badge" id="jomaCalcRefBadge">VERGLEICHS-REFERENZ: RINIKEN (18.8 KWP)</span>
              <span class="icon-box">{SVG_BATTERY}</span>
            </div>
            <h3 style="font-size:1.38rem;font-weight:700;margin-bottom:8px;" id="jomaCalcHeadline">Empfohlene Auslegung: 18.8 bis 24.0 kWp mit Speicher</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;" id="jomaCalcDesc">
              Ideale Dimensionierung für ein Einfamilienhaus mit Batteriespeicher und Solar Manager, vergleichbar mit unseren Anlagen in Riniken (18.8 kWp) und Fislisbach (24.03 kWp).
            </p>

            <div class="calc-kpi-grid">
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="jomaCalcYield">19'700 – 24'000 kWh</div>
                <div class="calc-kpi-lbl">Geschätzte Jahresproduktion</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="jomaCalcAutarky">bis 75 – 82 %</div>
                <div class="calc-kpi-lbl">Eigenverbrauchs- &amp; Autarkiegrad</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="jomaCalcModules">AIKO / 3S / Trina</div>
                <div class="calc-kpi-lbl">Empfohlene Modultechnologie</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="jomaCalcInstall">3 – 5 Arbeitstage</div>
                <div class="calc-kpi-lbl">Montagedauer + Bewilligungs-Service</div>
              </div>
            </div>

            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Inklusive Baueingabe &amp; Fördergelder:</strong> Wir übernehmen die komplette Abklärung mit Gemeinde, Netzbetreiber und Pronovo (Einmalvergütung EIV).</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Persönliche Beratung vor Ort:</strong> Jonathan Muggli und Marco Keller prüfen Dachstatik, Hausverteilung und Wirtschaftlichkeit direkt bei Ihnen.</span></div>
            </div>
          </div>

          <a href="kontakt.html?thema=efh" id="jomaCalcCta" class="btn-cta btn-cta-gold" style="width:100%;">
            <span>Diese Konfiguration als Offerte anfordern</span>
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
      <h3 id="wpImpTitle" style="font-size:1.36rem;font-weight:700;margin-bottom:10px;">Impressum &amp; Datenschutz (JOMA Solar GmbH)</h3>
      <div style="font-size:0.88rem;color:var(--text-body);line-height:1.62;display:flex;flex-direction:column;gap:12px;">
        <div style="background-color:var(--bg-page);border:1px solid var(--border-light);border-left:4px solid var(--gold);padding:12px 14px;border-radius:var(--radius-sm);">
          <strong>JOMA Solar GmbH</strong><br>
          Tägerhardstrasse 90 · CH-5430 Wettingen (Kanton Aargau)<br>
          Telefon Marco Keller: +41 56 558 98 67 · Telefon Jonathan Muggli: +41 56 558 48 82<br>
          E-Mail: info@joma-solar.ch · Web: www.joma-solar.ch
        </div>
        <p>
          <strong>Handelsregister &amp; Vertretungsberechtigte Personen:</strong><br>
          Eingetragen im Handelsregister des Kantons Aargau · UID: <strong>CHE-334.571.911</strong> (CH-ID: CH-400-4454055-9).<br>
          Geschäftsführer: Jonathan Muggli &amp; Marco Keller.
        </p>
        <p>
          <strong>Urheber- &amp; Bildrechte:</strong><br>
          Die auf dieser Website verwendeten Projektbilder, Drohnenaufnahmen, Grafiken und Inhalte sind Eigentum der JOMA Solar GmbH oder werden mit entsprechenden Nutzungsrechten verwendet.
        </p>
        <p>
          <strong>Datenschutz (Schweizer DSG):</strong><br>
          Alle Angaben aus dem 3-Schritte Smart-Anfrage-Assistenten werden streng vertraulich behandelt, ausschliesslich zur Projektprüfung, Beratung und Offertstellung durch die JOMA Solar GmbH verwendet und niemals an unbefugte Dritte weitergegeben.
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
      if (fEl && focus) fEl.textContent = 'Ansprechpartner JOMA Solar: ' + focus;
      m.classList.add('open');
    }
    function wpCloseBlueprintModal() {
      var m = document.getElementById('wpBlueprintModal');
      if (m) m.classList.remove('open');
    }

    var jomaCalcState = { type: 'efh', size: 'medium', storage: 'speicher_sm' };
    function jomaSetCalc(group, val) {
      jomaCalcState[group] = val;
      var gridId = group === 'type' ? 'jomaCalcTypeGrid' : (group === 'size' ? 'jomaCalcSizeGrid' : 'jomaCalcStorageGrid');
      var attr = 'data-' + group;
      var btns = document.querySelectorAll('#' + gridId + ' .calc-option-btn');
      for (var i = 0; i < btns.length; i++) {
        btns[i].classList.toggle('active', btns[i].getAttribute(attr) === val);
      }
      jomaUpdateCalcView();
    }
    function jomaUpdateCalcView() {
      var badge = document.getElementById('jomaCalcRefBadge');
      var head = document.getElementById('jomaCalcHeadline');
      var desc = document.getElementById('jomaCalcDesc');
      var yEl = document.getElementById('jomaCalcYield');
      var aEl = document.getElementById('jomaCalcAutarky');
      var mEl = document.getElementById('jomaCalcModules');
      var iEl = document.getElementById('jomaCalcInstall');
      var cta = document.getElementById('jomaCalcCta');
      if (!head) return;

      if (jomaCalcState.type === 'mfh') {
        badge.textContent = 'VERGLEICHS-REFERENZ: BADEN-RÜTIHOF (30.6 – 55.5 KWP)';
        head.textContent = 'Mehrfamilienhaus & ZEV-Lösung (30 bis 55 kWp)';
        desc.textContent = 'Optimale Stromverteilung direkt an die Miet- oder Stockwerkeigentumsparteien via Zusammenschluss zum Eigenverbrauch (ZEV) und Smart-Me Zähler.';
        yEl.textContent = '31\\'000 – 55\\'000 kWh';
        aEl.textContent = 'ZEV + Smart-Me Abrechnung';
        mEl.textContent = 'JA Solar / Megasol Full Black';
        iEl.textContent = 'Inkl. Eigentümerversammlung';
        if (cta) cta.href = 'kontakt.html?thema=mfh';
      } else if (jomaCalcState.type === 'gewerbe') {
        badge.textContent = 'VERGLEICHS-REFERENZ: WEIN & GEMÜSE UMBRICHT / GROSSANLAGEN';
        head.textContent = 'Gewerbeanlage, Lastspitzen-Speicher oder Contracting';
        desc.textContent = 'Senken Sie Ihre gewerblichen Energiekosten dauerhaft oder nutzen Sie unser Solar-Contracting ohne eigene Anfangsinvestition.';
        yEl.textContent = '45\\'000 – 180\\'000+ kWh';
        aEl.textContent = 'Peak-Shaving & Tageslast';
        mEl.textContent = 'Gewerbe-Hochleistungsmodule';
        iEl.textContent = 'Kauf oder 0.- CHF Contracting';
        if (cta) cta.href = 'kontakt.html?thema=gewerbe';
      } else {
        if (jomaCalcState.size === 'small') {
          badge.textContent = 'VERGLEICHS-REFERENZ: WETTINGEN (11.54 KWP) & SCHÖFFLISDORF (13.95 KWP)';
          head.textContent = 'Einfamilienhaus Kompakt: 11.5 bis 14.0 kWp';
          desc.textContent = 'Perfekt für Einfamilienhäuser und Dachsanierungen, auf Wunsch als elegantes 3S-Indachsystem oder leistungsstarkes AIKO-Aufdachsystem.';
          yEl.textContent = '11\\'000 – 16\\'000 kWh';
          aEl.textContent = jomaCalcState.storage === 'notstrom' ? 'bis 80 % + Notstrom-Schutz' : 'bis 70 – 78 % mit Speicher';
          mEl.textContent = '3S Indach / AIKO Neostar';
          iEl.textContent = '3 – 4 Arbeitstage Montage';
        } else if (jomaCalcState.size === 'large') {
          badge.textContent = 'VERGLEICHS-REFERENZ: FISLISBACH (24.03 KWP) & RÜTIHOF (30.6 KWP)';
          head.textContent = 'Grosszügiges Eigenheim / Doppel-EFH: 24 bis 30 kWp';
          desc.textContent = 'Maximale Leistungsreserven für Wärmepumpe, Elektroauto-Wallbox und hohen Eigenverbrauch auch im Winterhalbjahr.';
          yEl.textContent = '24\\'000 – 31\\'000 kWh';
          aEl.textContent = 'bis 80 – 85 % Autarkiegrad';
          mEl.textContent = 'Trina Vertex S+ / AIKO';
          iEl.textContent = '4 – 5 Arbeitstage Montage';
        } else {
          badge.textContent = 'VERGLEICHS-REFERENZ: RINIKEN (18.8 KWP) & FISLISBACH (24.0 KWP)';
          head.textContent = 'Empfohlene EFH-Auslegung: 18.8 bis 24.0 kWp';
          desc.textContent = 'Ideale Dimensionierung für ein Einfamilienhaus mit Batteriespeicher und Solar Manager, bereit für Wärmepumpe und E-Mobilität.';
          yEl.textContent = '19\\'700 – 24\\'000 kWh';
          aEl.textContent = jomaCalcState.storage === 'notstrom' ? 'bis 82 % + Notstrom-Reserve' : 'bis 75 – 82 % Eigenverbrauch';
          mEl.textContent = 'AIKO / 3S / Trina Solar';
          iEl.textContent = '3 – 5 Arbeitstage Montage';
        }
        if (cta) cta.href = 'kontakt.html?thema=efh';
      }
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
  <meta name="description" content="JOMA Solar GmbH in Wettingen (AG): Solaranlagen, Batteriespeicher, Solar Manager Energiemanagement, ZEV und Contracting für Privat- und Geschäftskunden im Aargau.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Electrician",
    "name": "JOMA Solar GmbH",
    "url": "https://www.joma-solar.ch",
    "telephone": "+41 56 558 98 67",
    "email": "info@joma-solar.ch",
    "taxID": "CHE-334.571.911",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Tägerhardstrasse 90",
      "postalCode": "5430",
      "addressLocality": "Wettingen",
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
        <span class="top-bar-badge" data-slot="topbar_badge">JOMA SOLAR GMBH · 5430 WETTINGEN (AG)</span>
        <span data-slot="topbar_sub">Photovoltaik, Batteriespeicher, ZEV &amp; Contracting für Privat &amp; Gewerbe</span>
      </div>
      <div class="top-bar-links">
        <a href="tel:+41565584882">{SVG_PHONE} <span>J. Muggli: 056 558 48 82</span></a>
        <a href="tel:+41565589867">{SVG_PHONE} <span>M. Keller: 056 558 98 67</span></a>
        <a href="mailto:info@joma-solar.ch">{SVG_MAIL} <span>info@joma-solar.ch</span></a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER -->
  <header class="site-header" data-section="header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="JOMA Solar GmbH Wettingen Startseite">
        <img src="images/logo.svg" alt="JOMA Solar GmbH Logo" class="brand-logo" width="138" height="26" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">JOMA Solar GmbH</span>
          <span class="brand-sub" data-slot="brand_sub">Wettingen · Kanton Aargau</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}" data-nav-href="index.html">Startseite</a>
        <a href="leistungen.html" class="nav-link {nav_leistungen}" data-nav-href="leistungen.html">Leistungen</a>
        <a href="referenzen.html" class="nav-link {nav_referenzen}" data-nav-href="referenzen.html">Referenzen</a>
        <a href="ueber-uns.html" class="nav-link {nav_ueber}" data-nav-href="ueber-uns.html">Über uns</a>
        <a href="kontakt.html" class="nav-link {nav_kontakt}" data-nav-href="kontakt.html">Kontakt</a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" data-slot="header_cta">
          <span>Offerte anfordern</span>
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
    <a href="leistungen.html" onclick="wpCloseMobileMenu()">Leistungen (Privat, Gewerbe, Speicher &amp; Contracting)</a>
    <a href="referenzen.html" onclick="wpCloseMobileMenu()">Referenzen (Wettingen, Riniken, Rütihof, Fislisbach)</a>
    <a href="ueber-uns.html" onclick="wpCloseMobileMenu()">Über uns, Team &amp; Offene Stelle Montageleiter</a>
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
            <img src="images/logo.svg" alt="JOMA Solar GmbH" width="138" height="26" loading="lazy" decoding="async">
          </div>
          <p style="font-size:0.86rem;color:#2C3545;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Solar einfach effizient: Ihre Spezialisten für massgeschneiderte Photovoltaikanlagen, Batteriespeicher, ZEV-Lösungen und Gewerbe-Contracting aus Wettingen für den ganzen Kanton Aargau und die Region Zürich.
          </p>
          <div style="font-size:0.84rem;color:#12161F;font-weight:600;">
            Tägerhardstrasse 90 · CH-5430 Wettingen · UID CHE-334.571.911
          </div>
        </div>

        <div>
          <div class="footer-title">Privat- &amp; Gewerbekunden</div>
          <ul class="footer-list">
            <li><a href="leistungen.html#privatkunden">Solaranlagen für EFH &amp; MFH</a></li>
            <li><a href="leistungen.html#batteriespeicher">Batteriespeicher &amp; Notstrom</a></li>
            <li><a href="leistungen.html#gewerbe">Photovoltaik für Gewerbe &amp; Grossanlagen</a></li>
            <li><a href="leistungen.html#contracting">Solar-Contracting ohne Investition</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Referenzen &amp; Team</div>
          <ul class="footer-list">
            <li><a href="referenzen.html">Alle 6 Referenzanlagen im Detail</a></li>
            <li><a href="referenzen.html#umbricht">Fallstudie Wein &amp; Gemüse Umbricht</a></li>
            <li><a href="ueber-uns.html">Unser 5-köpfiges Team in Wettingen</a></li>
            <li><a href="ueber-uns.html#karriere">Offene Stelle: Montageleiter Solar</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; Rechtliches</div>
          <ul class="footer-list">
            <li><a href="tel:+41565584882">Jonathan Muggli: 056 558 48 82</a></li>
            <li><a href="tel:+41565589867">Marco Keller: 056 558 98 67</a></li>
            <li><a href="mailto:info@joma-solar.ch">info@joma-solar.ch</a></li>
            <li><a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">3-Schritte Smart-Anfrage starten</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 JOMA Solar GmbH (Tägerhardstrasse 90, CH-5430 Wettingen AG · CHE-334.571.911).</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
          <a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">Offerte &amp; Smart-Anfrage</a>
          <a href="referenzen.html" style="color:#2C3545;">Referenzprojekte</a>
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
  <meta name="description" content="Unverbindlicher Vorschau-Entwurf (Zeigeversion) für JOMA Solar GmbH Wettingen: 2 Beispiel-Seiten sind bereits ausgearbeitet – 3 weitere Detailseiten folgen beim Ausbau.">
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
        <span class="top-bar-badge" data-slot="topbar_badge">JOMA SOLAR GMBH · 5430 WETTINGEN (AG)</span>
        <span data-slot="topbar_sub">Photovoltaik, Batteriespeicher, ZEV &amp; Contracting für Privat &amp; Gewerbe</span>
      </div>
      <div class="top-bar-links">
        <a href="tel:+41565584882">{SVG_PHONE} <span>J. Muggli: 056 558 48 82</span></a>
        <a href="tel:+41565589867">{SVG_PHONE} <span>M. Keller: 056 558 98 67</span></a>
        <a href="mailto:info@joma-solar.ch">{SVG_MAIL} <span>info@joma-solar.ch</span></a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER (ZEIGEVERSION MIT KUNDENFREUNDLICHEN VORSCHAU-HINWEISEN) -->
  <header class="site-header" data-section="header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="JOMA Solar GmbH Wettingen Startseite">
        <img src="images/logo.svg" alt="JOMA Solar GmbH Logo" class="brand-logo" width="138" height="26" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">JOMA Solar GmbH</span>
          <span class="brand-sub" data-slot="brand_sub">Wettingen · Kanton Aargau</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}" data-nav-href="index.html">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#15803D"/></svg>
          <span>Startseite</span>
        </a>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="leistungen.html" onclick="wpOpenBlueprintModal('Leistungen für Privat- &amp; Geschäftskunden im Detail', 'Solaranlagen EFH/MFH, Batteriespeicher, Solar Manager, Grossanlagen &amp; Contracting ohne Investition', 'Jonathan Muggli &amp; Marco Keller')">
          <span>Leistungen</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="referenzen.html" onclick="wpOpenBlueprintModal('Alle Referenzprojekte, Drohnenbilder &amp; Kundenstimmen', 'Wettingen (3S Indach), Riniken (18.8 kWp), 2× Rütihof (30.6 &amp; 55.5 kWp), Fislisbach, Schöfflisdorf &amp; Umbricht-Video', 'Jonathan Muggli &amp; Marco Keller')">
          <span>Referenzen</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="ueber-uns.html" onclick="wpOpenBlueprintModal('Über JOMA Solar, 5er-Team &amp; Karriere (Montageleiter)', 'Jonathan Muggli, Marco Keller, Tino Seiler, Mario Grab &amp; Sascha Tsap sowie Stelle Montageleiter Solar', 'Jonathan Muggli &amp; Marco Keller')">
          <span>Über uns</span>
        </button>
        <a href="kontakt.html" class="nav-link {nav_kontakt}" data-nav-href="kontakt.html">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#15803D"/></svg>
          <span>Kontakt</span>
        </a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" data-slot="header_cta">
          <span>Offerte anfordern</span>
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
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu(); wpOpenBlueprintModal('Leistungen für Privat- &amp; Geschäftskunden im Detail', 'EFH/MFH, Batteriespeicher, Solar Manager, Grossanlagen &amp; Contracting', 'Jonathan Muggli &amp; Marco Keller')">
      <span>Leistungen Privat &amp; Gewerbe (Folgt beim Ausbau)</span>
      {SVG_ARROW}
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu(); wpOpenBlueprintModal('Alle Referenzprojekte, Drohnenbilder &amp; Kundenstimmen', 'Wettingen, Riniken, 2× Rütihof, Fislisbach, Schöfflisdorf &amp; Umbricht-Video', 'Jonathan Muggli &amp; Marco Keller')">
      <span>Referenzen &amp; FAQs (Folgt beim Ausbau)</span>
      {SVG_ARROW}
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu(); wpOpenBlueprintModal('Über JOMA Solar, 5er-Team &amp; Karriere (Montageleiter)', 'Alle 5 Teammitglieder mit Porträt, Partnernetzwerk &amp; Stelle Montageleiter Solar', 'Jonathan Muggli &amp; Marco Keller')">
      <span>Über uns, Team &amp; Jobs (Folgt beim Ausbau)</span>
      {SVG_ARROW}
    </button>
    <a href="kontakt.html" onclick="wpCloseMobileMenu()">3-Schritte Smart-Anfrage (Live-Demo)</a>
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
            <img src="images/logo.svg" alt="JOMA Solar GmbH Logo" width="138" height="26" loading="lazy" decoding="async">
          </div>
          <p style="font-size:0.86rem;color:#2C3545;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Unverbindlicher Vorschau-Entwurf für die JOMA Solar GmbH (Wettingen): 2 Beispiel-Seiten (Startseite inkl. Solar-Rechner &amp; 3-Schritte Smart-Anfrage) sind bereits ausgearbeitet – 3 weitere Detailseiten folgen beim gemeinsamen Ausbau.
          </p>
          <div style="font-size:0.84rem;color:#12161F;font-weight:600;">
            Tägerhardstrasse 90 · CH-5430 Wettingen · Tel. 056 558 98 67
          </div>
        </div>

        <div>
          <div class="footer-title">Bereits ausgearbeitet (Live)</div>
          <ul class="footer-list">
            <li><a href="index.html">Startseite: Team-Hero &amp; 6 Kernlösungen</a></li>
            <li><a href="index.html#solarrechner">Interaktiver Solar- &amp; Speicher-Rechner</a></li>
            <li><a href="index.html#referenzen-vorschau">Referenz-Einblicke (Wettingen &amp; Region)</a></li>
            <li><a href="kontakt.html">3-Schritte Smart-Anfrage (Live-Demo)</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Folgen beim gemeinsamen Ausbau</div>
          <ul class="footer-list">
            <li><button type="button" onclick="wpOpenBlueprintModal('Leistungen für Privat- &amp; Geschäftskunden im Detail', 'Solaranlagen EFH/MFH, Batteriespeicher, Solar Manager, Grossanlagen &amp; Contracting ohne Investition', 'Jonathan Muggli &amp; Marco Keller')">Leistungen (Privat, Gewerbe &amp; Contracting)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Alle Referenzprojekte, Drohnenbilder &amp; Kundenstimmen', 'Alle 6 Referenzanlagen (Wettingen, Riniken, 2× Rütihof, Fislisbach, Schöfflisdorf), Fallstudie Umbricht &amp; FAQs', 'Jonathan Muggli &amp; Marco Keller')">Referenzen, Fallstudie &amp; FAQs</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Über JOMA Solar, 5er-Team &amp; Karriere (Montageleiter)', 'Alle 5 Teammitglieder mit Porträt, Systempartner &amp; Stelle Montageleiter Solar', 'Jonathan Muggli &amp; Marco Keller')">Über uns, 5er-Team &amp; Jobs</button></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; Rechtliches</div>
          <ul class="footer-list">
            <li><a href="tel:+41565584882">Jonathan Muggli: 056 558 48 82</a></li>
            <li><a href="tel:+41565589867">Marco Keller: 056 558 98 67</a></li>
            <li><a href="mailto:info@joma-solar.ch">info@joma-solar.ch</a></li>
            <li><a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">3-Schritte Smart-Anfrage starten</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 JOMA Solar GmbH (Wettingen AG) · Unverbindlicher Vorschau-Entwurf (Zeigeversion).</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
          <a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">Smart-Anfrage testen</a>
          <a href="index.html#weitere-themenbereiche" style="color:#2C3545;">Weitere Detailseiten</a>
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
      <div class="section-kicker">UNVERBINDLICHER VORSCHAU-ENTWURF FÜR JOMA-SOLAR.CH</div>
      <h3 id="wpBpTitle" style="font-size:1.36rem;font-weight:700;margin-bottom:8px;">Unverbindlicher Vorschau-Entwurf für die JOMA Solar GmbH</h3>
      <p id="wpBpSub" style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
        In dieser <strong>Zeigeversion (2 Beispiel-Seiten ausgearbeitet)</strong> sehen Sie Ihre neue Startseite mit allen 6 Leistungsbereichen, dem interaktiven Solar- &amp; Batterie-Potenzial-Rechner, den Referenz-Highlights sowie den live funktionierenden 3-Schritte Smart-Anfrage-Assistenten. Dieser vertiefte Themenbereich wird beim gemeinsamen Ausbau schlüsselfertig mit allen Originaltexten und Bildern freigeschaltet.
      </p>
      <div style="background-color:var(--gold-soft);border-left:4px solid var(--gold);padding:12px 14px;border-radius:var(--radius-sm);font-size:0.86rem;margin-bottom:14px;">
        <div style="font-weight:700;color:var(--charcoal-deep);" id="wpBpCategory">Leistungs- &amp; Projektbereich: Vorbereitet für den gemeinsamen Ausbau</div>
        <div style="color:var(--text-body);margin-top:2px;" id="wpBpContact">Ansprechpartner JOMA Solar: Jonathan Muggli &amp; Marco Keller</div>
      </div>

      <div class="wp-modal-checklist">
        <div style="font-family:'Lexend',sans-serif;font-size:0.8rem;font-weight:700;text-transform:uppercase;color:var(--charcoal-deep);">
          Was beim gemeinsamen Ausbau in diesem Themenbereich enthalten ist:
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Vollständige Leistungsseite für Privat- &amp; Geschäftskunden (EFH/MFH, Batteriespeicher, Solar Manager, Grossanlagen &amp; Solar-Contracting ohne Anfangsinvestition)</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Referenz- &amp; Fallstudienseite mit allen 6 Aargauer/Zürcher Referenzanlagen (Wettingen, Riniken, 2× Rütihof, Fislisbach, Schöfflisdorf), dem Video-Projekt Wein &amp; Gemüse Umbricht sowie allen FAQs</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Team- &amp; Karriereseite mit allen 5 Teammitgliedern (Jonathan Muggli, Marco Keller, Tino Seiler, Mario Grab, Sascha Tsap), Partnernetzwerk und der Stelle «Montageleiter Solar»</span>
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
        <div class="section-kicker kicker-light" data-slot="hero_kicker">PHOTOVOLTAIK, BATTERIESPEICHER &amp; ENERGIEMANAGEMENT · WETTINGEN (AG)</div>
        <h1 class="hero-title" data-slot="hero_title">
          Solar einfach <span>effizient.</span>
        </h1>
        <p class="hero-lead" data-slot="hero_lead">
          Solar- und Batteriesysteme für Privat- und Geschäftskunden im Kanton Aargau und der Region Zürich: Von der persönlichen Beratung über die Elektrotechnik- und Dachplanung bis zur schlüsselfertigen Installation durch unser eigenes 5-köpfiges Team aus Wettingen.
        </p>

        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
            <span>Beratung &amp; Offerte anfordern</span>
            {SVG_ARROW}
          </a>
          <a href="#solarrechner" class="btn-cta btn-cta-outline-light" data-slot="hero_cta_secondary">
            <span>Solar-Potenzial berechnen</span>
          </a>
        </div>

        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Privat &amp; Gewerbe</span>
            <span class="hero-badge-lbl">EFH, Mehrfamilienhäuser (ZEV), Grossanlagen &amp; Contracting</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Elektro &amp; Dach im Haus</span>
            <span class="hero-badge-lbl">Wirtschaftsingenieure, Elektroinstallateure EFZ &amp; Dachdecker</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Solar Manager &amp; Speicher</span>
            <span class="hero-badge-lbl">Intelligente Steuerung für Wärmepumpe, Wallbox &amp; Notstrom</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">5430 Wettingen (AG)</span>
            <span class="hero-badge-lbl">Tägerhardstrasse 90 · Persönlich vor Ort in der ganzen Region</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/team-gruppe-hero.jpg" alt="Das Team der JOMA Solar GmbH aus Wettingen" width="600" height="390" data-slot="hero_image">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#12161F;">JOMA Solar GmbH · Wettingen</div>
            <div style="font-size:0.8rem;color:#2C3545;">Jonathan Muggli, Marco Keller, Tino Seiler, Mario Grab &amp; Sascha Tsap</div>
          </div>
          <span class="top-bar-badge">HAND IN HAND VOR ORT</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 6 KERNLÖSUNGEN (3x2 SYMMETRISCHES RASTER) -->
  <section data-section="kernangebote" id="kernangebote">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="pillars_kicker">DURCHDACHTE ENERGIELÖSUNGEN · PRIVAT- &amp; GESCHÄFTSKUNDEN</div>
        <h2 class="section-title" data-slot="pillars_title">Sechs aufeinander abgestimmte Bausteine für Ihre Unabhängigkeit</h2>
        <p class="section-desc" data-slot="pillars_desc">
          Eine Solaranlage ist weit mehr als Module auf dem Dach: Erst das präzise Zusammenspiel von Dachmontage, Batteriespeicher, Energiemanagement und vorausschauender Elektroplanung macht Ihr Gebäude zum langfristig wirtschaftlichen Kraftwerk.
        </p>
      </div>

      <div class="grid-3">
        <!-- 1. Solaranlagen EFH / MFH -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-wettingen-indach.jpg" alt="Solaranlage für Einfamilienhaus und Mehrfamilienhaus in Wettingen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Eigenheim &amp; MFH</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Aufdach &amp; 3S-Indach</span>
              </div>
              <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Solaranlagen für EFH &amp; MFH</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Individuell auf Ihre Dacharchitektur und Ihre Zukunftspläne abgestimmte Photovoltaikanlagen, von der kompakten EFH-Anlage bis zur Dachsanierung.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Hochleistungsmodule (AIKO, 3S Swiss Solar Indach, Megasol, Trina)</span></div>
                <div class="check-item">{SVG_CHECK} <span>Vorbereitet für Wärmepumpe &amp; E-Mobilität (Wallbox)</span></div>
              </div>
            </div>
            <a href="leistungen.html#privatkunden" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Lösungen für Privatkunden</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 2. Batteriespeicher & Notstrom -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/batteriespeicher-heim.jpg" alt="Batteriespeicher für Eigenverbrauch und Notstrom" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Stromvorrat Tag &amp; Nacht</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">bis 85 % Autarkie</span>
              </div>
              <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Batteriespeicher &amp; Notstrom</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Nutzen Sie Ihren tagsüber produzierten Sonnenstrom auch am Abend und in der Nacht, exakt dimensioniert nach Ihrem Verbrauchsprofil.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Maximale Eigenverbrauchsoptimierung &amp; schnelle Amortisation</span></div>
                <div class="check-item">{SVG_CHECK} <span>Optionale Notstromfunktion bei Netzunterbruch (Sigenergy u. a.)</span></div>
              </div>
            </div>
            <a href="leistungen.html#batteriespeicher" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Speicher-Lösungen ansehen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 3. Energiemanagement & ZEV -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/solarmanager-app.jpg" alt="Solar Manager App und Smart-Me ZEV Abrechnung" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Solar Manager &amp; Smart-Me</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Volle App-Kontrolle</span>
              </div>
              <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Energiemanagement &amp; ZEV</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Intelligente Steuerung aller Energieflüsse im Haus sowie schlüsselfertige ZEV-Abrechnungslösungen für Mehrfamilienhäuser.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Zertifizierter Systempartner von Solar Manager &amp; Smart-Me</span></div>
                <div class="check-item">{SVG_CHECK} <span>Automatische Überschussladung für Elektroauto, Boiler &amp; Heizung</span></div>
              </div>
            </div>
            <a href="leistungen.html#energiemanagement" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Steuerung &amp; ZEV entdecken</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 4. Gewerbe & Grossanlagen -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/grossanlage-gewerbe.jpg" alt="Photovoltaik Grossanlagen für Gewerbe und Industrie" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Gewerbe &amp; Industrie</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Hoher Tagesertrag</span>
              </div>
              <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Gewerbe- &amp; Grossanlagen</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Verwandeln Sie Produktions-, Lager-, Büro- oder Landwirtschaftsdächer in wirtschaftliche Kraftwerke mit kalkulierbaren Strompreisen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Gewerbespeicher zur Glättung teurer Lastspitzen (Peak-Shaving)</span></div>
                <div class="check-item">{SVG_CHECK} <span>Strukturierte Umsetzung ohne Unterbruch Ihres laufenden Betriebs</span></div>
              </div>
            </div>
            <a href="leistungen.html#gewerbe" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Gewerbelösungen im Detail</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 5. Solar-Contracting -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/gewerbe-solar-abend.jpg" alt="Solar-Contracting für Unternehmen ohne eigene Investition" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">0.– CHF Anfangsinvestition</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Contracting-Modell</span>
              </div>
              <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Solar-Contracting für KMU</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Solarstrom direkt vom eigenen Firmendach nutzen, ohne eigenes Kapital zu binden: JOMA Solar übernimmt Planung, Finanzierung und Betrieb.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Keine Investitionskosten &amp; kein technisches Betriebsrisiko</span></div>
                <div class="check-item">{SVG_CHECK} <span>Langfristig planbare, attraktive Stromkonditionen für Ihr Unternehmen</span></div>
              </div>
            </div>
            <a href="leistungen.html#contracting" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Contracting-Modell prüfen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 6. Vorgehen & Serviceversprechen -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/dachmontage-handwerk.jpg" alt="Präzise Dachmontage und Schweizer Qualitätsversprechen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Aargauer Handwerksqualität</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">5-Schritte-Begleitung</span>
              </div>
              <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Qualität &amp; Serviceversprechen</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Wir beziehen unser gesamtes Installationsmaterial beim Schweizer Fachgrosshandel und begleiten Ihr Projekt von der Baueingabe bis zum Monitoring.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Komplette Abwicklung von Baugesuch, TAG &amp; Pronovo-Fördergeldern</span></div>
                <div class="check-item">{SVG_CHECK} <span>Mitglied bei Electrosuisse, EEV &amp; HGVW Wettingen</span></div>
              </div>
            </div>
            <a href="leistungen.html#vorgehen" class="btn-cta btn-cta-gold btn-sm" style="width:100%;">
              <span>Unser 5-Schritte-Prozess</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

{render_solar_calculator()}

  <!-- AUSGEWÄHLTE REFERENZPROJEKTE & FALLSTUDIE UMBRICHT -->
  <section data-section="referenzen-vorschau" id="referenzen-vorschau">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="ref_kicker">REALISIERTE SOLARPROJEKTE · WETTINGEN, RINIKEN, RÜTIHOF &amp; UNTERSIGGENTHAL</div>
        <h2 class="section-title" data-slot="ref_title">Echte Anlagen im Einsatz, dokumentiert mit Leistungsdaten</h2>
        <p class="section-desc" data-slot="ref_desc">
          Ob kombinierte 3S-Indach-/Aufdachsanierung in Wettingen, Ost-West-Süd-Flachdach in Riniken oder 30.6 kWp ZEV-Mehrfamilienhaus in Baden-Rütihof: Hier sehen Sie, wie wir Projekte in der Region umsetzen.
        </p>
      </div>

      {render_references_grid(3, is_v2=False)}

      <div class="content-card card-dark" style="margin-top:28px;">
        <div class="grid-2" style="align-items:stretch;">
          <div style="display:flex;flex-direction:column;justify-content:space-between;">
            <div>
              <span class="top-bar-badge" style="margin-bottom:10px;">LEUCHTTURMPROJEKT IN DER KERNZONE · UNTERSIGGENTHAL (AG)</span>
              <h3 style="font-size:1.38rem;font-weight:700;margin-bottom:10px;">Wein &amp; Gemüse Umbricht: Eigenverbrauch in der Kernzone optimiert</h3>
              <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
                Für das Projekt von Wein &amp; Gemüse Umbricht in Untersiggenthal stand die Optimierung des gewerblichen Eigenverbrauchs im Mittelpunkt. Gleichzeitig stellte die Lage des Gebäudes in der Kernzone besondere Anforderungen an Gestaltung, Bewilligung und Projektierung.
              </p>
              <div class="check-list" style="margin-bottom:18px;">
                <div class="check-item">{SVG_CHECK} <span>Frühzeitige Abstimmung mit der Gemeinde Untersiggenthal für eine bewilligungsfähige Kernzonen-Lösung</span></div>
                <div class="check-item">{SVG_CHECK} <span>Perfekte Abstimmung auf den hohen Tagesstrombedarf von Kühlung und Direktvermarktung</span></div>
              </div>
            </div>
            <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:auto;">
              <a href="referenzen.html" class="btn-cta btn-cta-primary btn-sm">
                <span>Alle 6 Referenzen</span>
                {SVG_ARROW}
              </a>
              <a href="https://vimeo.com/1189667227" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-outline btn-sm">
                <span>Vimeo-Video öffnen</span>
              </a>
            </div>
          </div>
          <div style="display:flex;">
            <img src="images/ref-umbricht-untersiggenthal.jpg" alt="Referenzprojekt Wein und Gemüse Umbricht in Untersiggenthal" style="width:100%;height:100%;min-height:280px;object-fit:cover;border-radius:var(--radius-md);border:1px solid var(--border-strong);" loading="lazy" decoding="async">
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 2 GRÜNDER & GESCHÄFTSFÜHRER -->
  <section data-section="gruender" id="gruender" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">IHRE ANSPRECHPARTNER IN WETTINGEN · HAND IN HAND</div>
        <h2 class="section-title">Persönlich geführt von Jonathan Muggli und Marco Keller</h2>
        <p class="section-desc">
          Bei der JOMA Solar GmbH an der Tägerhardstrasse 90 in Wettingen sprechen Sie direkt mit den Inhabern. Wir verbinden fundiertes Ingenieur- und Elektrotechnik-Wissen mit einem eingespielten eigenen Montageteam auf dem Dach.
        </p>
      </div>

      <div class="grid-2">
        <div class="founder-card">
          <div class="founder-top">
            <img src="images/portrait-jonathan-muggli.jpg" alt="Jonathan Muggli – Gründer und Geschäftsführer JOMA Solar GmbH Wettingen" class="founder-portrait" loading="lazy" decoding="async">
            <div>
              <span class="meta-badge" style="margin-bottom:8px;">Gründer &amp; Geschäftsführer</span>
              <h3 style="font-size:1.32rem;font-weight:700;margin-bottom:4px;">Jonathan Muggli</h3>
              <p style="font-size:0.84rem;color:var(--gold-dark);font-weight:700;margin-bottom:8px;">
                Elektroinstallateur EFZ · Energietechniker HF · Wirtschaftsingenieur FH
              </p>
              <p style="font-size:0.88rem;color:var(--text-body);line-height:1.58;">
                Spezialisiert auf ganzheitliche Solarsysteme, ZEV-Abrechnungslösungen für Mehrfamilienhäuser, Hausverteilungs-Integration und intelligentes Energiemanagement.
              </p>
            </div>
          </div>
          <div class="founder-body">
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Direktwahl: <strong>056 558 48 82</strong> · info@joma-solar.ch</span></div>
              <div class="check-item">{SVG_CHECK} <span>Fokus: Elektrotechnik, ZEV / Smart-Me &amp; Systemintegration</span></div>
            </div>
            <a href="tel:+41565584882" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Jonathan Muggli direkt anrufen (056 558 48 82)</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <div class="founder-card">
          <div class="founder-top">
            <img src="images/portrait-marco-keller.jpg" alt="Marco Keller – Gründer und Geschäftsführer JOMA Solar GmbH Wettingen" class="founder-portrait" loading="lazy" decoding="async">
            <div>
              <span class="meta-badge" style="margin-bottom:8px;">Gründer &amp; Geschäftsführer</span>
              <h3 style="font-size:1.32rem;font-weight:700;margin-bottom:4px;">Marco Keller</h3>
              <p style="font-size:0.84rem;color:var(--gold-dark);font-weight:700;margin-bottom:8px;">
                Wirtschaftsingenieur · Über 10 Jahre Photovoltaik-Erfahrung
              </p>
              <p style="font-size:0.88rem;color:var(--text-body);line-height:1.58;">
                Über ein Jahrzehnt Erfahrung in der Planung, Wirtschaftlichkeitsberechnung und schlüsselfertigen Abwicklung von privaten und gewerblichen Photovoltaikprojekten.
              </p>
            </div>
          </div>
          <div class="founder-body">
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Direktwahl: <strong>056 558 98 67</strong> · info@joma-solar.ch</span></div>
              <div class="check-item">{SVG_CHECK} <span>Fokus: Beratung, Wirtschaftlichkeit, Grossanlagen &amp; Contracting</span></div>
            </div>
            <a href="tel:+41565589867" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Marco Keller direkt anrufen (056 558 98 67)</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>

      <div style="margin-top:28px;display:flex;justify-content:center;gap:14px;flex-wrap:wrap;">
        <a href="ueber-uns.html" class="btn-cta btn-cta-primary">
          <span>Unser gesamtes 5er-Team &amp; Partnernetzwerk kennenlernen</span>
          {SVG_ARROW}
        </a>
        <a href="ueber-uns.html#karriere" class="btn-cta btn-cta-outline">
          <span>Stelle: Montageleiter Solar</span>
        </a>
      </div>
    </div>
  </section>

  <!-- ACP BRÜCKE 1: SOCIAL MEDIA & PROJEKT-EINBLICKE AUS DEM ALLTAG -->
  <section data-section="social-media" id="social-media">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">AKTUELLE PROJEKT-EINBLICKE · @JOMA_SOLAR AUF INSTAGRAM &amp; LINKEDIN</div>
        <h2 class="section-title">Frisch ab Dach und Technikraum im Kanton Aargau</h2>
        <p class="section-desc">
          Wir zeigen echte Handwerks- und Ingenieursarbeit direkt aus unserem Alltag in Wettingen, Baden, Riniken und Fislisbach, transparent vom ersten Montageschritt bis zur Drohnen-Endabnahme.
        </p>
      </div>

      <div class="grid-3">
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-riniken-18kwp.jpg" alt="Drohnenaufnahme der 18.8 kWp Solaranlage in Riniken" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <span class="meta-badge" style="margin-bottom:10px;">Drohnen-Abnahme · Riniken</span>
              <h3 style="font-size:1.18rem;font-weight:700;margin-bottom:8px;">18.8 kWp Ost/West &amp; Süd auf Flach- und Blechfalzdach</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">
                Durch die Kombination von Flachdach-Aufständerung und Blechfalzdach liefert diese AIKO Neostar 2P Anlage in Riniken 19.7 MWh pro Jahr mit gleichmässigem Tagesprofil.
              </p>
            </div>
            <a href="referenzen.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Technische Projektdaten ansehen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/elektrotechnik-planung.jpg" alt="Saubere Elektrotechnik und Speicher-Integration durch JOMA Solar" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <span class="meta-badge" style="margin-bottom:10px;">Elektrotechnik · Wettingen</span>
              <h3 style="font-size:1.18rem;font-weight:700;margin-bottom:8px;">Saubere Hausverteilung &amp; intelligente Speicher-Kopplung</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">
                Ein Blick in den Technikraum: Wechselrichter, Batteriespeicher, NA-Schutz und Solar Manager kommunizieren nahtlos mit Wärmepumpe und Ladestation.
              </p>
            </div>
            <a href="leistungen.html#batteriespeicher" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Mehr über Speicher &amp; Elektrotechnik</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/beratung-kundengespraech.jpg" alt="Persönliches Beratungsgespräch bei JOMA Solar in Wettingen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <span class="meta-badge" style="margin-bottom:10px;">Beratung · Region Baden</span>
              <h3 style="font-size:1.18rem;font-weight:700;margin-bottom:8px;">Ehrliche Wirtschaftlichkeitsrechnung vor jedem Entscheid</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">
                Ob Eigenheim oder Mehrfamilienhaus-Eigentümerversammlung: Wir zeigen transparent auf, wann sich Ihre Anlage inklusive Fördergeldern amortisiert.
              </p>
            </div>
            <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Beratungstermin vereinbaren</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ACP BRÜCKE 2: SOLAR-RATGEBER & FACHWISSEN -->
  <section data-section="blog" id="blog" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">SOLAR-RATGEBER &amp; FACHWISSEN · FÜR EIGENTÜMER &amp; UNTERNEHMEN</div>
        <h2 class="section-title">Drei entscheidende Fragen vor der Planung Ihrer Solaranlage</h2>
        <p class="section-desc">
          Wer heute baut oder saniert, stellt die Weichen für die nächsten 25 bis 30 Jahre. Worauf Sie bei Dimensionierung, Speicher und Mehrfamilienhäusern achten sollten:
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Ratgeber #1 · Eigenheim</span>
            <h3 style="font-size:1.18rem;font-weight:700;margin-bottom:8px;">Wärmepumpe &amp; Elektroauto von Anfang an mitdenken</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Auch wenn Sie heute noch kein Elektroauto fahren oder der Heizungswechsel erst in einigen Jahren ansteht: Wir planen Wechselrichter und Reservekapazitäten so, dass spätere Grossverbraucher ohne teuren Umbau direkt mit Sonnenstrom laufen.
            </p>
          </div>
          <a href="leistungen.html#privatkunden" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Vorausschauende EFH-Planung</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Ratgeber #2 · Mehrfamilienhaus</span>
            <h3 style="font-size:1.18rem;font-weight:700;margin-bottom:8px;">ZEV im Mehrfamilienhaus: Solarstrom direkt an Mieter liefern</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Mit einem Zusammenschluss zum Eigenverbrauch (ZEV) und digitalen Smart-Me Zählern profitieren Eigentümer und Mietparteien gemeinsam vom günstigen Dachstrom. Wir begleiten Sie auch an die Eigentümerversammlung.
            </p>
          </div>
          <a href="referenzen.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>ZEV-Referenz Rütihof (30.6 kWp)</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Ratgeber #3 · Gewerbe</span>
            <h3 style="font-size:1.18rem;font-weight:700;margin-bottom:8px;">Kauf vs. Solar-Contracting: Wann lohnt sich welches Modell?</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Unternehmen mit hohem Tagesverbrauch erzielen durch Eigeninvestition maximale Renditen. Wer jedoch die Liquidität für das Kerngeschäft schonen möchte, bezieht über unser Contracting-Modell sofort günstigen Solarstrom ohne Anfangsinvestition.
            </p>
          </div>
          <a href="leistungen.html#contracting" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Gewerbe &amp; Contracting vergleichen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>
"""

# ==============================================================================
# SEITEN-INHALTE: V1 LEISTUNGEN (leistungen.html)
# ==============================================================================
V1_LEISTUNGEN_BODY = f"""
  <!-- HERO LEISTUNGEN -->
  <section class="hero-section" data-section="hero-leistungen">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">PRIVATKUNDEN, GEWERBE, SPEICHER &amp; CONTRACTING · WETTINGEN (AG)</div>
        <h1 class="hero-title">
          Massgeschneiderte <span>Solar- &amp; Speichersysteme.</span>
        </h1>
        <p class="hero-lead">
          Ob Einfamilienhaus mit Wärmepumpe und Wallbox, Mehrfamilienhaus im ZEV-Modell oder gewerbliche Grossanlage mit Lastspitzen-Speicher: Bei JOMA Solar planen und installieren wir Ihr System individuell statt ab der Stange.
        </p>

        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>Projekt &amp; Offerte anfragen</span>
            {SVG_ARROW}
          </a>
          <a href="#gewerbe" class="btn-cta btn-cta-outline-light">
            <span>Zu den Gewerbe- &amp; Contracting-Lösungen</span>
          </a>
        </div>

        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">3S Indach &amp; Aufdach</span>
            <span class="hero-badge-lbl">Ästhetische Integration für Neubau &amp; Dachsanierung</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Speicher &amp; Notstrom</span>
            <span class="hero-badge-lbl">Sichere Hausverteilung &amp; hohe Eigenverbrauchsquote</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Solar Manager App</span>
            <span class="hero-badge-lbl">Zertifizierter Partner für Wärmepumpe &amp; E-Mobilität</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Gewerbe &amp; Contracting</span>
            <span class="hero-badge-lbl">Kauf oder 0.– CHF Investition im Contracting-Modell</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/efh-luftbild-quartier.jpg" alt="Photovoltaikanlagen für Privat- und Geschäftskunden im Kanton Aargau" width="600" height="390">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#12161F;">Vorausschauende Systemplanung</div>
            <div style="font-size:0.8rem;color:#2C3545;">Ausgelegt auf 25–30+ Jahre zuverlässigen Betrieb</div>
          </div>
          <span class="top-bar-badge">SCHWEIZER FACHHANDEL</span>
        </div>
      </div>
    </div>
  </section>

  <!-- 1. PRIVATKUNDEN: EFH, MFH & GROSSVERBRAUCHER -->
  <section data-section="privatkunden" id="privatkunden">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">SCHWERPUNKT 1 · PRIVATKUNDEN (EINFAMILIENHAUS &amp; MEHRFAMILIENHAUS)</div>
        <h2 class="section-title">Heute vorausschauend planen und morgen dauerhaft sparen</h2>
        <p class="section-desc">
          Die ideale Grösse einer Solaranlage richtet sich nicht nur nach Ihrem heutigen Stromverbrauch. Wir blicken gemeinsam mit Ihnen in die Zukunft und stimmen Dachbelegung, Wechselrichter und Energiemanagement auf Ihre kommenden Vorhaben ab.
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Aufdach &amp; Indach</span>
              <span class="icon-box">{SVG_SUN}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Solaranlage für EFH &amp; MFH</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Jedes Dach hat eigene statische und optische Anforderungen. Wir realisieren sowohl leistungsstarke Aufdachanlagen als auch nahtlose 3S-Indachsysteme bei Dachsanierungen.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Individuelle Verschattungs- und Ertragssimulation</span></div>
              <div class="check-item">{SVG_CHECK} <span>Komplette Baueingabe, Netzbetreiber-Anmeldung &amp; Fördergelder</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=efh" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Offerte für Eigenheim anfordern</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top" id="energiemanagement">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Wärmepumpe &amp; Wallbox</span>
              <span class="icon-box">{SVG_ZAP}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Grossverbraucher &amp; Solar Manager</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Ein modernes Haus hat hungrige Abnehmer. Mit dem Schweizer System Solar Manager steuern wir Ihre Energieflüsse vollautomatisch dorthin, wo sie den höchsten Nutzen stiften.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Überschussladen für Elektroauto (Wallbox) mit 100 % Sonnenstrom</span></div>
              <div class="check-item">{SVG_CHECK} <span>Intelligente Ansteuerung von Wärmepumpe und Warmwasserboiler</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=efh" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Energiemanagement anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Mehrfamilienhäuser</span>
              <span class="icon-box">{SVG_USERS}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">ZEV &amp; Smart-Me Abrechnung</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Für Stockwerkeigentum und Renditeliegenschaften planen wir den kompletten Zusammenschluss zum Eigenverbrauch (ZEV) inklusive digitaler Zählerstruktur.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Fachliche Begleitung an der Eigentümerversammlung</span></div>
              <div class="check-item">{SVG_CHECK} <span>Automatisierte Parteien-Abrechnung mit Smart-Me Zählern</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=mfh" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>MFH &amp; ZEV-Beratung anfordern</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. BATTERIESPEICHER & ELEKTROTECHNIK -->
  <section data-section="batteriespeicher" id="batteriespeicher" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">SCHWERPUNKT 2 · BATTERIESPEICHER &amp; NOTSTROM-ABSICHERUNG</div>
        <h2 class="section-title">Ihr persönlicher Stromvorrat für Abend, Nacht und Netzunterbruch</h2>
        <p class="section-desc">
          Die Installation eines Speichersystems ist eine anspruchsvolle elektrotechnische Aufgabe. Wir dimensionieren Ihren Speicher exakt nach Ihren Zielen: schnelle wirtschaftliche Amortisation, maximaler Autarkiegrad oder Notstrom-Sicherheit.
        </p>
      </div>

      <div class="grid-2">
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/batteriespeicher-heim.jpg" alt="Batteriespeicher für Eigenheime von JOMA Solar" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Eigenheim-Speicher</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Sigenergy &amp; Top-Marken</span>
              </div>
              <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:8px;">3 Strategien für Ihren Heimspeicher</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Gemeinsam bestimmen wir die optimale Speichergrösse für Ihren Haushalt:
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span><strong>1. Wirtschaftlichkeit:</strong> Optimale Kapazität für schnelle Amortisation durch hohen Eigenverbrauch am Abend.</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>2. Hoher Autarkiegrad:</strong> Grosszügigere Reserve, um den Netzbezug auf ein Minimum zu senken.</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>3. Sicherheit bei Netzunterbruch:</strong> Optionale Notstromfunktion hält wichtige Geräte bei Stromausfall in Betrieb.</span></div>
              </div>
            </div>
            <a href="kontakt.html?thema=efh" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Speicher-Dimensionierung berechnen lassen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/gewerbe-speicher-technik.jpg" alt="Gewerbespeicher und Lastmanagement Technikraum" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Gewerbe-Lastmanagement</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Peak-Shaving</span>
              </div>
              <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:8px;">Gewerbespeicher &amp; Lastspitzen-Glättung</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Gewerbebetriebe mit Maschinen, Kühlung oder Ladeflotten profitieren doppelt von einem skalierbaren Gewerbespeicher:
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span><strong>Lastspitzen kappen (Peak-Shaving):</strong> Senkt teure Leistungspreise des Netzbetreibers spürbar.</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Skalierbare Architektur:</strong> Wächst modular mit Ihrem Betrieb oder Ihrer E-Fahrzeugflotte mit.</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Zentraler NA-Schutz &amp; Sicherheit:</strong> Fachgerechte Einbindung durch unsere Elektroingenieure.</span></div>
              </div>
            </div>
            <a href="kontakt.html?thema=gewerbe" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Gewerbespeicher &amp; Lastgang prüfen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 3. GEWERBE, GROSSANLAGEN & CONTRACTING -->
  <section data-section="gewerbe" id="gewerbe">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">SCHWERPUNKT 3 · GEWERBE, INDUSTRIE &amp; SOLAR-CONTRACTING</div>
        <h2 class="section-title">Ungenutzte Firmendächer in wirtschaftliche Kraftwerke verwandeln</h2>
        <p class="section-desc">
          Für Produktionsbetriebe, Logistik- und Lagerhallen, Bürogebäude, Landwirtschaftsbetriebe und Parkhäuser bieten wir zwei klare Wege zur eigenen Solaranlage: als renditestarke Eigeninvestition oder als Contracting ohne Kapitaleinsatz.
        </p>
      </div>

      <div class="grid-2" id="contracting">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Option A · Eigeninvestition</span>
              <span class="icon-box">{SVG_BUILDING}</span>
            </div>
            <h3 style="font-size:1.32rem;font-weight:700;margin-bottom:10px;">Photovoltaik-Grossanlagen im Eigentum</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:14px;">
              Maximale langfristige Stromkostensenkung für Ihr Unternehmen durch direkten Eigenverbrauch während der Betriebszeiten:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Umfassende Statik-, Infrastruktur- und Wirtschaftlichkeitsanalyse vorab</span></div>
              <div class="check-item">{SVG_CHECK} <span>Abklärung und Beantragung sämtlicher Fördergelder und Einmalvergütungen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Sorgfältige Etappierung ohne Unterbruch Ihres laufenden Geschäftsbetriebs</span></div>
              <div class="check-item">{SVG_CHECK} <span>Laufendes Monitoring und optionale Service- &amp; Wartungsverträge</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=gewerbe" class="btn-cta btn-cta-primary" style="width:100%;">
            <span>Wirtschaftlichkeitsanalyse für Firmendach anfordern</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-dark">
          <div>
            <div class="card-badge-row">
              <span class="top-bar-badge">OPTION B · 0.– CHF ANFANGSINVESTITION</span>
              <span class="icon-box">{SVG_SHIELD}</span>
            </div>
            <h3 style="font-size:1.32rem;font-weight:700;margin-bottom:10px;">Das JOMA Solar-Contracting Modell</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:14px;">
              Sie möchten Ihr Dach für sauberen Solarstrom nutzen, Ihr Kapital aber vollständig in Ihrem Kerngeschäft belassen?
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Planung &amp; Finanzierung durch JOMA:</strong> Wir übernehmen die gesamten Investitions- und Baukosten der Anlage.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Betrieb, Überwachung &amp; Wartung inklusive:</strong> Sie tragen keinerlei technisches Betriebsrisiko.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Kalkulierbarer Solarstromtarif:</strong> Ihr Unternehmen bezieht den Strom direkt vom Dach zu vertraglich fixierten, günstigen Konditionen.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Standortübergreifend möglich:</strong> Auch für Unternehmen mit mehreren Hallen oder Filialen.</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=gewerbe" class="btn-cta btn-cta-gold" style="width:100%;">
            <span>Unverbindliches Contracting-Gespräch vereinbaren</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- 4. UNSER VORGEHEN IN 5 SCHRITTEN -->
  <section data-section="vorgehen" id="vorgehen" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">STRUKTURIERT ZUM ZIEL · UNSER QUALITÄTSVERSPRECHEN</div>
        <h2 class="section-title">So begleiten wir Ihr Solarprojekt von A bis Z</h2>
        <p class="section-desc">
          Wir beziehen unser gesamtes Installationsmaterial ausschliesslich beim Schweizer Fachgrosshandel und begleiten Sie in vier klaren Projektphasen bis zur laufenden Betreuung:
        </p>
      </div>

      <div class="grid-4">
        <div class="content-card card-accent-top">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Schritt 01</span>
            <h3 style="font-size:1.12rem;font-weight:700;margin-bottom:8px;">Analyse &amp; Beratung vor Ort</h3>
            <p style="font-size:0.86rem;color:var(--text-body);">
              Prüfung von Dachzustand, Statik, Hausverteilung, aktuellem Stromverbrauch und künftigen Grossverbrauchern (Wärmepumpe / E-Auto).
            </p>
          </div>
          <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Vor Ort oder nach Plänen</span>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Schritt 02</span>
            <h3 style="font-size:1.12rem;font-weight:700;margin-bottom:8px;">Projektierung &amp; Bewilligungen</h3>
            <p style="font-size:0.86rem;color:var(--text-body);">
              Transparente Offerte mit Ertragssimulation sowie Übernahme sämtlicher Baueingaben, Netzbetreiber-Gesuche (TAG) und Fördergeld-Anmeldungen.
            </p>
          </div>
          <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Rundum-Sorglos-Abwicklung</span>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Schritt 03</span>
            <h3 style="font-size:1.12rem;font-weight:700;margin-bottom:8px;">Dach- &amp; Elektromontage</h3>
            <p style="font-size:0.86rem;color:var(--text-body);">
              Wind- und wetterfeste Dachmontage durch unsere gelernten Dachdecker und saubere Elektroinstallation nach höchsten Schweizer Sicherheitsnormen.
            </p>
          </div>
          <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Meist in 3–5 Tagen (EFH)</span>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Schritt 04</span>
            <h3 style="font-size:1.12rem;font-weight:700;margin-bottom:8px;">Inbetriebnahme &amp; Betreuung</h3>
            <p style="font-size:0.86rem;color:var(--text-body);">
              Einrichtung der Solar Manager App, persönliche Instruktion, Sicherheitsnachweis und langfristige Begleitung als regionaler Partner aus Wettingen.
            </p>
          </div>
          <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">25–30+ Jahre Lebensdauer</span>
        </div>
      </div>
    </div>
  </section>
"""

# ==============================================================================
# SEITEN-INHALTE: V1 REFERENZEN (referenzen.html)
# ==============================================================================
V1_REFERENZEN_BODY = f"""
  <!-- HERO REFERENZEN -->
  <section class="hero-section" data-section="hero-referenzen">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">REALISIERTE SOLARANLAGEN IM KANTON AARGAU &amp; REGION ZÜRICH</div>
        <h1 class="hero-title">
          Unsere <span>Referenzprojekte</span> aus Wettingen, Baden &amp; Umgebung.
        </h1>
        <p class="hero-lead">
          Ob ästhetische 3S-Indach-Lösung auf dem Einfamilienhaus, Mehrfamilienhaus mit ZEV und 68 Modulen oder gewerblicher Kühl- und Landwirtschaftsbetrieb in der Kernzone: Jede Anlage wird von unserem eigenen Team aus Wettingen geplant und gebaut.
        </p>

        <div class="hero-actions">
          <a href="#projekte" class="btn-cta btn-cta-gold">
            <span>Alle 6 Referenzanlagen</span>
            {SVG_ARROW}
          </a>
          <a href="#umbricht" class="btn-cta btn-cta-outline-light">
            <span>Fallstudie Umbricht (Video)</span>
          </a>
        </div>

        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">11.5 bis 55.5 kWp</span>
            <span class="hero-badge-lbl">Dokumentierte EFH-, MFH-ZEV- &amp; Überbauungsprojekte</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">3S, AIKO &amp; Megasol</span>
            <span class="hero-badge-lbl">Bewährte Hochleistungs- und Indach-Module</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Steil-, Flach- &amp; Blechdach</span>
            <span class="hero-badge-lbl">Sturmsichere Ausführung durch gelernte Dachdecker</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">ZEV &amp; NA-Schutz</span>
            <span class="hero-badge-lbl">Komplette Elektrotechnik &amp; Smart-Me Zählerintegration</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/ref-ruetihof-55kwp.jpg" alt="Grossanlage 55.47 kWp in Baden-Rütihof mit Megasol Full Black Modulen" width="600" height="390">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.02rem;color:#12161F;">Baden-Rütihof · 55.47 kWp Grossprojekt</div>
            <div style="font-size:0.8rem;color:#2C3545;">Megasol Full Black · 4 Wechselrichter · Speicher &amp; zentraler NA-Schutz</div>
          </div>
          <span class="top-bar-badge">55 MWH / JAHR</span>
        </div>
      </div>
    </div>
  </section>

  <!-- GEWERBE-FALLSTUDIE: WEIN & GEMÜSE UMBRICHT -->
  <section data-section="fallstudie-umbricht" id="umbricht" style="background-color:var(--bg-Warm);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">GEWERBE-FALLSTUDIE MIT VIDEO · UNTERSIGGENTHAL (AG)</div>
        <h2 class="section-title">Wein &amp; Gemüse Umbricht: Solarstrom für Kühlung in der Kernzone</h2>
        <p class="section-desc">
          Wie ein traditionsreicher Familienbetrieb in Untersiggenthal seinen hohen Tages-Strombedarf für Kühlanlagen mit eigenem Solarstrom deckt, trotz anspruchsvoller Kernzonen-Auflagen.
        </p>
      </div>

      <div class="grid-2">
        <div class="pillar-card">
          <div class="pillar-img-wrap" style="height:270px;">
            <img src="images/ref-umbricht-untersiggenthal.jpg" alt="Solaranlage Wein und Gemüse Umbricht in Untersiggenthal" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Gewerbe &amp; Landwirtschaft</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Untersiggenthal (AG)</span>
              </div>
              <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:8px;">Ideales Lastprofil dank Kühlhäusern &amp; Direktvermarktung</h3>
              <p style="font-size:0.9rem;color:var(--text-body);">
                Gerade im Sommerhalbjahr, wenn die Sonne am meisten Energie liefert, laufen die Kühlanlagen von Wein &amp; Gemüse Umbricht auf Hochtouren. Dadurch wird ein aussergewöhnlich hoher Anteil des produzierten Solarstroms direkt im eigenen Betrieb genutzt.
              </p>
            </div>
            <a href="https://vimeo.com/1189667227" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Projekt-Video auf Vimeo ansehen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Projekt-Highlights</span>
              <span class="icon-box">{SVG_BUILDING}</span>
            </div>
            <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:10px;">Bewilligung in der Kernzone &amp; Betrieb ohne Unterbruch</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:14px;">
              Von der ersten Machbarkeitsprüfung über die Baubewilligung in der Kernzone bis zur Inbetriebnahme begleitete JOMA Solar das gesamte Projekt als einziger Ansprechpartner:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Kernzonen-Integration:</strong> Ruhige, blendfreie Dachoptik in Abstimmung mit den kommunalen Vorgaben in Untersiggenthal</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Maximale Wirtschaftlichkeit:</strong> Gleichzeitigkeit von Sonnenschein und Kühlbedarf senkt den Netzbezug markant</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Montage im laufenden Betrieb:</strong> Saubere Koordination ohne Störung von Hofladen, Lager und Logistik</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Regionale Partnerschaft:</strong> Kurze Wege von Wettingen nach Untersiggenthal für Service und Monitoring</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=gewerbe" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Ähnliches Gewerbeprojekt anfragen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- ALLE 6 REFERENZPROJEKTE IM DETAIL -->
  <section data-section="alle-referenzen" id="projekte">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">DOKUMENTIERTE REFERENZANLAGEN · EINFAMILIENHÄUSER &amp; MEHRFAMILIENHÄUSER</div>
        <h2 class="section-title">6 ausgewählte Anlagen mit Leistungs- und Ertragsdaten</h2>
        <p class="section-desc">
          Transparente Kennzahlen zu installierter Leistung (kWp), prognostiziertem Jahresertrag (MWh), eingesetzten Modulen und baulichen Besonderheiten.
        </p>
      </div>

      {render_references_grid(6, is_v2=False)}
    </div>
  </section>

  <!-- HÄUFIGE FRAGEN (FAQS) -->
  <section data-section="faqs" id="faqs" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">ANTWORTEN AUS DER PRAXIS · PLANUNG, BAUBEWILLIGUNG &amp; FÖRDERUNG</div>
        <h2 class="section-title">Häufige Fragen zu Solaranlagen &amp; Batteriespeichern</h2>
        <p class="section-desc">
          Die wichtigsten Antworten zu Installationsdauer, Lebensdauer, Förderbeiträgen (Pronovo) und Baubewilligung im Kanton Aargau.
        </p>
      </div>

      {render_faqs_grid()}
    </div>
  </section>

{render_solar_calculator()}
"""


# ==============================================================================
# SEITEN-INHALTE: V1 ÜBER UNS, TEAM & JOBS (ueber-uns.html)
# ==============================================================================
V1_UEBER_UNS_BODY = f"""
  <!-- HERO ÜBER UNS -->
  <section class="hero-section" data-section="hero-ueber-uns">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">ÜBER JOMA SOLAR GMBH · TÄGERHARDSTRASSE 90, 5430 WETTINGEN</div>
        <h1 class="hero-title">
          Fünf Fachleute. <span>Ein Qualitätsanspruch.</span>
        </h1>
        <p class="hero-lead">
          Hinter der JOMA Solar GmbH stehen die beiden Gründer <strong>Jonathan Muggli</strong> und <strong>Marco Keller</strong> gemeinsam mit unserem eigenen Montage- und Ausführungsteam in Wettingen. Wir verbinden fundiertes Elektro- und Wirtschaftsingenieurwissen mit echtem Dachdecker- und Solarteur-Handwerk.
        </p>

        <div class="hero-actions">
          <a href="#team" class="btn-cta btn-cta-gold">
            <span>5er-Team kennenlernen</span>
            {SVG_ARROW}
          </a>
          <a href="#karriere" class="btn-cta btn-cta-outline-light">
            <span>Stelle: Montageleiter Solar</span>
          </a>
        </div>

        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Inhabergeführt</span>
            <span class="hero-badge-lbl">Direkter Draht zu Jonathan Muggli &amp; Marco Keller</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Eigene Montageprofis</span>
            <span class="hero-badge-lbl">Tino Seiler, Mario Grab &amp; Sascha Tsap vor Ort auf Ihrem Dach</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">CHE-334.571.911</span>
            <span class="hero-badge-lbl">Verankert an der Tägerhardstrasse 90 in 5430 Wettingen</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Starke Systempartner</span>
            <span class="hero-badge-lbl">Solar Manager, Smart-Me, 3S, AIKO, Megasol &amp; lokale Banken</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/team-gruppe-hero.jpg" alt="Das 5-köpfige Team der JOMA Solar GmbH in Wettingen" width="600" height="390">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.02rem;color:#12161F;">Das Team der JOMA Solar GmbH</div>
            <div style="font-size:0.8rem;color:#2C3545;">Persönliche Beratung, saubere Planung &amp; eigenes Handwerk aus Wettingen</div>
          </div>
          <span class="top-bar-badge">5 FACHKRÄFTE VOR ORT</span>
        </div>
      </div>
    </div>
  </section>

  <!-- GESCHÄFTSLEITUNG (JONATHAN MUGGLI & MARCO KELLER) -->
  <section data-section="geschaeftsleitung" id="team">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">GRÜNDER &amp; GESCHÄFTSLEITUNG · DIREKTER ANSPRECHPARTNER</div>
        <h2 class="section-title">Ihre Ansprechpartner von der ersten Beratung bis zur Übergabe</h2>
        <p class="section-desc">
          Bei JOMA Solar sprechen Sie nicht mit einem anonymen Callcenter, sondern direkt mit den beiden Inhabern und unserem eingespielten Ausführungsteam.
        </p>
      </div>

      <div class="grid-2" style="margin-bottom:28px;">
        <div class="founder-card">
          <div class="founder-top">
            <img src="images/portrait-jonathan-muggli.jpg" alt="Jonathan Muggli – Gründer und Geschäftsführer JOMA Solar GmbH" class="founder-portrait" loading="lazy" decoding="async">
            <div>
              <span class="meta-badge" style="margin-bottom:8px;">Gründer &amp; Geschäftsführer</span>
              <h3 style="font-size:1.35rem;font-weight:700;margin-bottom:6px;">Jonathan Muggli</h3>
              <p style="font-size:0.86rem;color:var(--gold-dark);font-weight:700;margin-bottom:10px;">
                Elektroinstallateur EFZ · Energietechniker HF · Wirtschaftsingenieur FH
              </p>
              <p style="font-size:0.88rem;color:var(--text-body);line-height:1.58;">
                Verbindet tiefes elektrotechnisches Praxiswissen aus der Haus- und Netzinstallation mit ganzheitlicher Energie- und Wirtschaftlichkeitsplanung.
              </p>
            </div>
          </div>
          <div class="founder-body">
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Elektrotechnische Systemauslegung, NA-Schutz, ZEV &amp; Speicher-Integration</span></div>
              <div class="check-item">{SVG_CHECK} <span>Direktwahl Wettingen: <strong>056 558 48 82</strong> · info@joma-solar.ch</span></div>
            </div>
            <a href="tel:+41565584882" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              {SVG_PHONE}
              <span>Jonathan Muggli direkt anrufen (056 558 48 82)</span>
            </a>
          </div>
        </div>

        <div class="founder-card">
          <div class="founder-top">
            <img src="images/portrait-marco-keller.jpg" alt="Marco Keller – Gründer und Geschäftsführer JOMA Solar GmbH" class="founder-portrait" loading="lazy" decoding="async">
            <div>
              <span class="meta-badge" style="margin-bottom:8px;">Gründer &amp; Geschäftsführer</span>
              <h3 style="font-size:1.35rem;font-weight:700;margin-bottom:6px;">Marco Keller</h3>
              <p style="font-size:0.86rem;color:var(--gold-dark);font-weight:700;margin-bottom:10px;">
                Wirtschaftsingenieur · Über 10 Jahre Erfahrung in der Photovoltaik
              </p>
              <p style="font-size:0.88rem;color:var(--text-body);line-height:1.58;">
                Begleitet seit über einem Jahrzehnt anspruchsvolle Solarprojekte in der Schweiz, vom Einfamilienhaus bis zur gewerblichen Grossanlage und Contracting-Lösung.
              </p>
            </div>
          </div>
          <div class="founder-body">
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Projektentwicklung, Wirtschaftlichkeitsrechnung, ZEV &amp; Solar-Contracting</span></div>
              <div class="check-item">{SVG_CHECK} <span>Direktwahl Wettingen: <strong>056 558 98 67</strong> · info@joma-solar.ch</span></div>
            </div>
            <a href="tel:+41565589867" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              {SVG_PHONE}
              <span>Marco Keller direkt anrufen (056 558 98 67)</span>
            </a>
          </div>
        </div>
      </div>

      <!-- MONTAGE & AUSFÜHRUNG (3 KARTEN) -->
      <div class="grid-3">
        <div class="pillar-card">
          <div class="pillar-img-wrap" style="height:250px;">
            <img src="images/portrait-tino-seiler.jpg" alt="Tino Seiler – Leiter Montage und Ausführung JOMA Solar" style="object-position:center top;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Leiter Montage &amp; Ausführung</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:6px;">Tino Seiler</h3>
              <p style="font-size:0.84rem;font-weight:700;color:var(--gold-dark);margin-bottom:10px;">
                Elektroplaner · Elektroinstallateur · Solarteur
              </p>
              <p style="font-size:0.88rem;color:var(--text-body);">
                Verantwortlich für die technische Ausführungsqualität, die saubere Baustellenorganisation und die fachgerechte Verbindung von Dach- und Elektroinstallation.
              </p>
            </div>
            <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Baustellenleitung &amp; Elektrotechnik</span>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap" style="height:250px;">
            <img src="images/portrait-mario-grab.jpg" alt="Mario Grab – Solarmonteur und gelernter Dachdecker JOMA Solar" style="object-position:center top;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Solarmonteur &amp; Dachdecker</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:6px;">Mario Grab</h3>
              <p style="font-size:0.84rem;font-weight:700;color:var(--gold-dark);margin-bottom:10px;">
                Gelernter Dachdecker &amp; Solarmonteur
              </p>
              <p style="font-size:0.88rem;color:var(--text-body);">
                Garantiert als gelernter Dachdecker, dass jede Unterkonstruktion, jeder Dachhaken und jede Indach-Anlage dauerhaft regensicher und sturmfest montiert wird.
              </p>
            </div>
            <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Dachhandwerk &amp; Indach-Systeme</span>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap" style="height:250px;">
            <img src="images/portrait-sascha-tsap.jpg" alt="Sascha Tsap – Solarmonteur und Dachdecker JOMA Solar" style="object-position:center top;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Solarmonteur &amp; Dachdecker</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:6px;">Sascha Tsap</h3>
              <p style="font-size:0.84rem;font-weight:700;color:var(--gold-dark);margin-bottom:10px;">
                Erfahrener Dachdecker &amp; Montageprofi
              </p>
              <p style="font-size:0.88rem;color:var(--text-body);">
                Spezialisiert auf präzise Modulmontage auf Steil-, Flach- und Blechfalzdächern sowie auf eine saubere, langlebige Kabelführung auf dem Dach.
              </p>
            </div>
            <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Steil-, Flach- &amp; Blechfalzdächer</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- KARRIERE: OFFENE STELLE MONTAGELEITER SOLAR -->
  <section data-section="karriere" id="karriere" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">KARRIERE BEI JOMA SOLAR IN WETTINGEN · WIR WACHSEN WEITER</div>
        <h2 class="section-title">Offene Stelle: Montageleiter Solar (w/m/d) · 80–100 %</h2>
        <p class="section-desc">
          Du suchst ein eingespieltes Team auf Augenhöhe, modernes Werkzeug und spannende Photovoltaikprojekte direkt in der Region Aargau und Zürich?
        </p>
      </div>

      <div class="grid-2">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Festanstellung 80–100 % · Wettingen (AG)</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:10px;">Deine Aufgaben &amp; Dein Profil als Montageleiter Solar</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:14px;">
              Als Montageleiter führst du unser Montageteam auf den Baustellen im Kanton Aargau und der Region Zürich und bist das Bindeglied zur Projektleitung:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Selbstständige Baustellenleitung:</strong> Verantwortung für Aufdach-, Indach- und Flachdach-Installationen</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Koordination vor Ort:</strong> Abstimmung mit den beteiligten Fachbereichen sowie unserer internen Elektrotechnik</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Dein Hintergrund:</strong> Abgeschlossene Grundbildung als Dachdecker EFZ, Zimmermann EFZ, Elektroinstallateur EFZ oder Solarteur mit Führungserfahrung</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Was dich erwartet:</strong> 5 Wochen Ferien, top ausgestattetes Montagefahrzeug, faire Entlöhnung und kurze Entscheidungswege</span></div>
            </div>
          </div>
          <a href="mailto:info@joma-solar.ch?subject=Bewerbung%20Montageleiter%20Solar" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Unkompliziert per E-Mail oder Telefon (056 558 48 82) melden</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap" style="height:260px;">
            <img src="images/team-jonathan-marco-pv.jpg" alt="Jonathan Muggli und Marco Keller auf dem Solardach" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <span class="meta-badge" style="margin-bottom:10px;">Spontanbewerbung willkommen</span>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Solarmonteur, Dachdecker EFZ oder Elektroinstallateur EFZ?</h3>
              <p style="font-size:0.9rem;color:var(--text-body);">
                Auch wenn du als Solarmonteur, Dachdecker oder Elektroinstallateur eine neue Herausforderung in einem familiären Wettinger Betrieb suchst, freuen wir uns auf deinen Anruf oder eine kurze Nachricht, ganz ohne kompliziertes Bewerbungsdossier.
              </p>
            </div>
            <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Kurze Nachricht an Jonathan &amp; Marco senden</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
"""


# ==============================================================================
# SEITEN-INHALTE: V2 ZEIGEVERSION / VORSCHAU-ENTWURF (index.html)
# ==============================================================================
V2_INDEX_BODY = (
    V1_INDEX_BODY
    .replace(
        'href="leistungen.html#privatkunden"',
        'href="#vorschau-leistungen" onclick="wpOpenBlueprintModal(\'Solaranlagen für Einfamilien- &amp; Mehrfamilienhäuser\', \'3S Indach &amp; Aufdach, ZEV-Gründung, Pronovo-Förderung &amp; 4-Schritte-Begleitung\', \'Jonathan Muggli &amp; Marco Keller\'); return false;"',
    )
    .replace(
        'href="leistungen.html#batteriespeicher"',
        'href="#vorschau-speicher" onclick="wpOpenBlueprintModal(\'Batteriespeicher, Notstrom &amp; Solar Manager\', \'Heimspeicher, Gewerbe-Lastspitzenbrechung &amp; intelligente Kopplung von Wärmepumpe &amp; Wallbox\', \'Jonathan Muggli &amp; Marco Keller\'); return false;"',
    )
    .replace(
        'href="leistungen.html#gewerbe"',
        'href="#vorschau-gewerbe" onclick="wpOpenBlueprintModal(\'Gewerbeanlagen &amp; Grossanlagen ab 30 kWp\', \'Industrie- &amp; Gewerbedächer, NA-Schutz, Lastgang-Analyse &amp; hohe Rendite\', \'Jonathan Muggli &amp; Marco Keller\'); return false;"',
    )
    .replace(
        'href="leistungen.html#contracting"',
        'href="#vorschau-contracting" onclick="wpOpenBlueprintModal(\'Solar-Contracting ohne eigene Investition\', \'JOMA Solar plant, baut, finanziert und wartet die Anlage auf Ihrem Gewerbedach\', \'Jonathan Muggli &amp; Marco Keller\'); return false;"',
    )
    .replace(
        'href="leistungen.html"',
        'href="#vorschau-leistungen" onclick="wpOpenBlueprintModal(\'Leistungen für Privat- &amp; Geschäftskunden\', \'Alle Details zu EFH, MFH/ZEV, Batteriespeicher, Grossanlagen &amp; Contracting\', \'Jonathan Muggli &amp; Marco Keller\'); return false;"',
    )
    .replace(
        'href="referenzen.html"',
        'href="#vorschau-referenzen" onclick="wpOpenBlueprintModal(\'Alle Referenzprojekte &amp; Fallstudie Umbricht\', \'Wettingen, Riniken, 2× Baden-Rütihof, Fislisbach, Schöfflisdorf &amp; Video-Fallstudie Untersiggenthal\', \'Jonathan Muggli &amp; Marco Keller\'); return false;"',
    )
    .replace(
        'href="ueber-uns.html"',
        'href="#vorschau-team" onclick="wpOpenBlueprintModal(\'Über JOMA Solar, 5er-Team &amp; Jobs\', \'Jonathan Muggli, Marco Keller, Tino Seiler, Mario Grab &amp; Sascha Tsap sowie Stelle Montageleiter Solar\', \'Jonathan Muggli &amp; Marco Keller\'); return false;"',
    )
) + f"""
  <!-- VORSCHAU-BEREICH DER WEITEREN UNTERSEITEN (KUNDENFREUNDLICHE ZEIGEVERSION #UI-03) -->
  <section class="preview-scope-section" id="weitere-themenbereiche" data-section="vorschau-umfang">
    <div class="container">
      <div class="preview-scope-banner">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:10px;">
          <span class="top-bar-badge">UNVERBINDLICHER VORSCHAU-ENTWURF · 2 BEISPIEL-SEITEN LIVE AUSGEARBEITET</span>
          <span style="font-size:0.82rem;color:#2C3545;font-weight:600;">JOMA Solar GmbH · 5430 Wettingen (AG)</span>
        </div>
        <h2 style="font-size:clamp(1.55rem,2.6vw,2.1rem);font-weight:700;color:#12161F;margin-bottom:10px;">
          3 weitere Detailseiten sind für den gemeinsamen Ausbau vorbereitet
        </h2>
        <p style="font-size:0.95rem;color:#2C3545;line-height:1.65;">
          In dieser <strong>Zeigeversion</strong> haben wir die <strong>Startseite (inkl. interaktivem Solar- &amp; Speicher-Rechner)</strong> und den <strong>3-Schritte Smart-Anfrage-Assistenten</strong> bereits live für Sie aufgebaut. Die folgenden drei vertieften Detailseiten mit allen Referenzanlagen, dem gesamten 5-köpfigen Team und den Gewerbe-/Contracting-Modellen werden beim gemeinsamen Ausbau schlüsselfertig freigeschaltet:
        </p>
      </div>

      <div class="grid-3">
        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Folgt beim Ausbau · Unterseite 1</span>
              <span class="icon-box">{SVG_SUN}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Leistungen: Privat, Gewerbe, Speicher &amp; Contracting</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Vertiefte Fachseite für Eigenheimbesitzer, Verwaltungen und Unternehmen im Kanton Aargau:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>EFH &amp; MFH (3S Indach, AIKO/Megasol Aufdach &amp; ZEV mit Smart-Me)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Batteriespeicher, Notstrom &amp; Solar Manager App-Steuerung</span></div>
              <div class="check-item">{SVG_CHECK} <span>Grossanlagen ab 30 kWp &amp; Solar-Contracting ohne Investition</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Leistungen: Privat, Gewerbe, Speicher &amp; Contracting', 'EFH/MFH, ZEV, Batteriespeicher, Solar Manager, Grossanlagen &amp; Contracting ohne Investition', 'Jonathan Muggli &amp; Marco Keller')">
            <span>Vorschau-Details zu Leistungen öffnen</span>
            {SVG_ARROW}
          </button>
        </div>

        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Folgt beim Ausbau · Unterseite 2</span>
              <span class="icon-box">{SVG_BUILDING}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Alle 6 Referenzanlagen, Fallstudie Umbricht &amp; FAQs</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Dokumentierte Anlagen aus der Region mit kWp-Leistung, Jahresertrag und Video-Einblick:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Wettingen (11.54 kWp 3S Indach), Riniken (18.8 kWp), Fislisbach (24 kWp)</span></div>
              <div class="check-item">{SVG_CHECK} <span>2× Baden-Rütihof (30.6 kWp ZEV &amp; 55.47 kWp Grossprojekt) + Schöfflisdorf</span></div>
              <div class="check-item">{SVG_CHECK} <span>Gewerbe-Fallstudie Wein &amp; Gemüse Umbricht (Untersiggenthal) + Praxis-FAQs</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Alle 6 Referenzanlagen, Fallstudie Umbricht &amp; FAQs', 'Wettingen, Riniken, 2× Baden-Rütihof, Fislisbach, Schöfflisdorf &amp; Gewerbe-Video Untersiggenthal', 'Jonathan Muggli &amp; Marco Keller')">
            <span>Vorschau-Details zu Referenzen öffnen</span>
            {SVG_ARROW}
          </button>
        </div>

        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Folgt beim Ausbau · Unterseite 3</span>
              <span class="icon-box">{SVG_USERS}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Über JOMA Solar, 5er-Team &amp; Offene Stelle</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Persönliche Vorstellung aller 5 Mitarbeitenden in Wettingen sowie Karriere-Bereich:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Gründer Jonathan Muggli &amp; Marco Keller mit Direktwahl</span></div>
              <div class="check-item">{SVG_CHECK} <span>Montage- &amp; Ausführungsteam: Tino Seiler, Mario Grab &amp; Sascha Tsap</span></div>
              <div class="check-item">{SVG_CHECK} <span>Offene Stelle «Montageleiter Solar (w/m/d)» &amp; Spontanbewerbung</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Über JOMA Solar, 5er-Team &amp; Offene Stelle', 'Alle 5 Teammitglieder mit Porträt, Serviceversprechen &amp; Stelle Montageleiter Solar', 'Jonathan Muggli &amp; Marco Keller')">
            <span>Vorschau-Details zu Team &amp; Jobs öffnen</span>
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
        <!-- LEFT COLUMN: DIREKTKONTAKT WETTINGEN -->
        <div class="contact-info-panel">
          <div class="section-kicker" data-slot="contact_kicker">KONTAKT &amp; UNVERBINDLICHE OFFERTE · 5430 WETTINGEN (AG)</div>
          <h1 style="font-size:clamp(1.65rem,2.5vw,2.15rem);font-weight:700;margin-bottom:12px;" data-slot="contact_title">
            Ihr direkter Draht zu Jonathan Muggli &amp; Marco Keller.
          </h1>
          <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:18px;" data-slot="contact_lead">
            Ob Einfamilienhaus, Mehrfamilienhaus mit ZEV, Batteriespeicher-Nachrüstung oder gewerbliche Grossanlage: Starten Sie rechts die 3-Schritte Smart-Anfrage oder rufen Sie uns direkt in Wettingen an.
          </p>

          <img src="images/team-gruppe-hero.jpg" alt="Das Team der JOMA Solar GmbH in Wettingen" style="width:100%;height:200px;object-fit:cover;object-position:center top;border-radius:var(--radius-sm);margin-bottom:16px;" loading="lazy" decoding="async">

          <div class="contact-direct-list">
            <div class="contact-direct-item">
              <div class="contact-direct-role">Standort &amp; Projektleitung</div>
              <div class="contact-direct-person">JOMA Solar GmbH · CHE-334.571.911</div>
              <div class="contact-direct-links">Tägerhardstrasse 90 · CH-5430 Wettingen (Kanton Aargau)</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Gründer &amp; Geschäftsführer (Elektrotechnik &amp; Planung)</div>
              <div class="contact-direct-person">Jonathan Muggli (Elektroinstallateur EFZ · Energietechniker HF · Wirtschaftsingenieur FH)</div>
              <div class="contact-direct-links">Direktwahl: 056 558 48 82 · E-Mail: info@joma-solar.ch</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Gründer &amp; Geschäftsführer (Beratung, ZEV &amp; Gewerbe)</div>
              <div class="contact-direct-person">Marco Keller (Wirtschaftsingenieur · &gt;10 Jahre PV-Erfahrung)</div>
              <div class="contact-direct-links">Direktwahl: 056 558 98 67 · E-Mail: info@joma-solar.ch</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Einsatzgebiet ab Wettingen</div>
              <div class="contact-direct-person">Kanton Aargau &amp; angrenzender Kanton Zürich</div>
              <div class="contact-direct-links">Wettingen, Baden, Rütihof, Untersiggenthal, Fislisbach, Brugg, Riniken, Limmattal &amp; Wehntal</div>
            </div>
          </div>
        </div>

        <!-- RIGHT COLUMN: GEFÜHRTER 3-SCHRITTE SMART-ANFRAGE-ASSISTENT -->
        <div class="wizard-card">
          <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:14px;">
            <div>
              <div class="section-kicker" style="margin-bottom:4px;">3-SCHRITTE SMART-ANFRAGE · JOMA-SOLAR.CH</div>
              <h2 style="font-size:1.35rem;font-weight:700;" id="wpWizardTitle">1. Für welches Objekt planen Sie eine Solaranlage?</h2>
            </div>
            <span class="meta-badge" id="wpActiveAssigneeBadge">Ansprechpartner: Jonathan Muggli &amp; Marco Keller</span>
          </div>

          <div class="wp-stepper" aria-label="Fortschritt">
            <div class="wp-step-pill active" id="wpStepPill1">
              <span class="wp-step-num">1</span>
              <span>Objekt &amp; System</span>
            </div>
            <div class="wp-step-pill" id="wpStepPill2">
              <span class="wp-step-num">2</span>
              <span>Dach &amp; Zeitplan</span>
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

            <!-- SCHRITT 1: OBJEKT & SYSTEM -->
            <div class="wp-step-pane active" id="wpStep1">
              <div class="wp-role-grid" id="wpTopicGrid">
                <button type="button" class="wp-role-tile selected" data-topic="Einfamilienhaus: Photovoltaik, Speicher & Solar Manager" onclick="wpSelectIsTopic('Einfamilienhaus: Photovoltaik, Speicher & Solar Manager')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_SUN}</span>
                    <span class="wp-role-title" data-slot="topic_opt_1">1. Einfamilienhaus (PV &amp; Speicher)</span>
                  </div>
                  <span class="wp-role-desc">Aufdach oder 3S Indach, Batteriespeicher, Solar Manager, Wärmepumpe &amp; Wallbox</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Mehrfamilienhaus & ZEV (Eigenverbrauchsgemeinschaft)" onclick="wpSelectIsTopic('Mehrfamilienhaus & ZEV (Eigenverbrauchsgemeinschaft)')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_BUILDING}</span>
                    <span class="wp-role-title" data-slot="topic_opt_2">2. Mehrfamilienhaus &amp; ZEV</span>
                  </div>
                  <span class="wp-role-desc">Solarstrom für Mieter &amp; Stockwerkeigentümer inkl. Smart-Me Abrechnung &amp; ETV-Begleitung</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Gewerbeanlage, Grossanlage oder Solar-Contracting" onclick="wpSelectIsTopic('Gewerbeanlage, Grossanlage oder Solar-Contracting')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_ZAP}</span>
                    <span class="wp-role-title" data-slot="topic_opt_3">3. Gewerbe, Grossanlage &amp; Contracting</span>
                  </div>
                  <span class="wp-role-desc">Gewerbedächer ab 30 kWp, Lastspitzen-Speicher oder Contracting ohne eigene Investition</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Batteriespeicher-Nachrüstung, Service oder E-Ladestation" onclick="wpSelectIsTopic('Batteriespeicher-Nachrüstung, Service oder E-Ladestation')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_BATTERY}</span>
                    <span class="wp-role-title" data-slot="topic_opt_4">4. Speicher-Nachrüstung &amp; Service</span>
                  </div>
                  <span class="wp-role-desc">Bestehende Anlage um Speicher, Notstrom, Solar Manager oder E-Mobilität erweitern</span>
                </button>
              </div>

              <button type="button" class="btn-cta btn-cta-primary" style="width:100%;" onclick="wpNextStep(2)">
                <span>Weiter zu Schritt 2: Dach &amp; Zeitplan</span>
                {SVG_ARROW}
              </button>
            </div>

            <!-- SCHRITT 2: DACH & ZEITPLAN -->
            <div class="wp-step-pane" id="wpStep2">
              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="wpDetail1" class="form-label" id="wpDetail1Label">Dachtyp &amp; ungefähre Grösse / Stromverbrauch</label>
                  <input type="text" id="wpDetail1" class="form-input" placeholder="z. B. Steildach Ziegel / Flachdach · ca. 7'500 kWh/Jahr">
                </div>
                <div class="form-field">
                  <label for="wpDetail2" class="form-label" id="wpDetail2Label">Wunsch-Komponenten (Speicher / Wallbox / WP)</label>
                  <input type="text" id="wpDetail2" class="form-input" placeholder="z. B. Mit Batteriespeicher (10 kWh), Solar Manager &amp; Wallbox">
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label class="form-label">Gewünschter Realisierungs-Zeitraum</label>
                <div class="wp-role-grid" id="wpUrgencyGrid" style="margin-bottom:0;">
                  <button type="button" class="wp-role-tile selected" data-urg="Zeitnah (Beratung & Offerte in den nächsten 1–2 Wochen)" onclick="wpSelectIsUrgency('Zeitnah (Beratung & Offerte in den nächsten 1–2 Wochen)')">
                    <span class="wp-role-title">1. Zeitnahe Beratung &amp; Offerte</span>
                    <span class="wp-role-desc">Vor-Ort-Besichtigung oder Dachprüfung in den nächsten 1–2 Wochen</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urg="In Planung (Neubau, Dachsanierung oder Heizungsersatz)" onclick="wpSelectIsUrgency('In Planung (Neubau, Dachsanierung oder Heizungsersatz)')">
                    <span class="wp-role-title">2. Neubau oder Sanierung in Planung</span>
                    <span class="wp-role-desc">Frühzeitige Abstimmung mit Architektur, Dachdecker oder Heizungsplanung</span>
                  </button>
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label for="contactMessage" class="form-label">Ergänzende Angaben zum Gebäude oder Fragen (optional)</label>
                <textarea id="contactMessage" class="form-textarea" placeholder="Gerne können Sie hier die Objektadresse für die Luftbild-Vorabprüfung oder Fragen notieren..."></textarea>
              </div>

              <div class="wp-upload-zone" style="margin-bottom:16px;">
                <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
                  <div>
                    <div style="font-family:'Lexend',sans-serif;font-size:0.8rem;font-weight:700;color:var(--charcoal-deep);">Optional: Foto von Dach, Zählerkasten oder Plänen beifügen</div>
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
                <strong>Live-Vorschau-Modus (Selbsttest aktiv):</strong> Beim Absenden erstellt das System sofort ein echtes <strong>1-Seiten-A4-PDF-Dossier</strong> im Erscheinungsbild der <strong>JOMA Solar GmbH (Wettingen)</strong> zum direkten Öffnen und Prüfen.
              </div>

              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactName" class="form-label" data-slot="lbl_name">Vor- und Nachname *</label>
                  <input type="text" id="contactName" name="name" class="form-input" placeholder="z. B. Thomas Meier" required>
                </div>
                <div class="form-field">
                  <label for="contactCompany" class="form-label">Firma / Eigentümergemeinschaft (optional)</label>
                  <input type="text" id="contactCompany" name="company" class="form-input" placeholder="z. B. Privatperson oder Muster AG">
                </div>
              </div>

              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactLoc" class="form-label">PLZ &amp; Objekt-Standort *</label>
                  <input type="text" id="contactLoc" name="plz" class="form-input" placeholder="z. B. 5430 Wettingen / 5400 Baden" oninput="wpCheckIsPlz(this.value)" required>
                </div>
                <div class="form-field">
                  <label for="contactStreet" class="form-label">Strasse &amp; Nr. des Gebäudes (für Luftbild-Check)</label>
                  <input type="text" id="contactStreet" name="street" class="form-input" placeholder="z. B. Tägerhardstrasse 90">
                </div>
              </div>

              <div class="wp-plz-badge" id="wpPlzBadge" style="margin-bottom:14px;">
                {SVG_CHECK}
                <span id="wpPlzBadgeText">PLZ 5430: Direktes Kerngebiet JOMA Solar GmbH (Wettingen / Aargau)</span>
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
                  <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.08rem;color:var(--charcoal-deep);">Solar-Anfrage &amp; 1-Seiten-PDF-Dossier erfolgreich erstellt</div>
                  <div style="font-size:0.78rem;color:var(--text-muted);" id="wpResChannels">1-Seiten-PDF-Dossier bereit zum Download</div>
                </div>
              </div>
              <span class="top-bar-badge" style="background-color:#D64B13;color:#FFFFFF;" id="wpResRef">#WP-2026</span>
            </div>

            <div class="form-grid-2" style="background-color:#F3F5FA;padding:12px 14px;border-radius:4px;border:1px solid var(--border-light);font-size:0.84rem;">
              <div>
                <div style="color:var(--text-muted);font-size:0.75rem;">Zuständige Projektleitung (Wettingen):</div>
                <strong style="color:var(--charcoal-deep);" id="wpResAssigned">Jonathan Muggli &amp; Marco Keller</strong>
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
      topic: 'Einfamilienhaus: Photovoltaik, Speicher & Solar Manager',
      urgency: 'Zeitnah (Beratung & Offerte in den nächsten 1–2 Wochen)',
      photos: []
    }};

    var wpIsRoleConfig = {{
      'Einfamilienhaus: Photovoltaik, Speicher & Solar Manager': {{
        assignee: 'Jonathan Muggli & Marco Keller (EFH & Speicher)',
        l1: 'Dachtyp & ungefähre Grösse / Jahresverbrauch',
        p1: 'z. B. Steildach Ziegel oder Flachdach · ca. 7500 kWh/Jahr',
        l2: 'Wunsch-Komponenten (Speicher / Wallbox / Wärmepumpe)',
        p2: 'z. B. Mit Batteriespeicher, Solar Manager & E-Ladestation'
      }},
      'Mehrfamilienhaus & ZEV (Eigenverbrauchsgemeinschaft)': {{
        assignee: 'Marco Keller (MFH & ZEV-Lösungen)',
        l1: 'Anzahl Wohnungen / Parteien & Dachform',
        p1: 'z. B. 8 Parteien · Flachdach begrünt oder Steildach',
        l2: 'Gewünschte Leistung (ZEV / Smart-Me / ETV-Begleitung)',
        p2: 'z. B. ZEV-Gründung inkl. Smart-Me Zähler & Eigentümerversammlung'
      }},
      'Gewerbeanlage, Grossanlage oder Solar-Contracting': {{
        assignee: 'Marco Keller & Jonathan Muggli (Gewerbe & Contracting)',
        l1: 'Art des Betriebs & ungefähre Dachfläche / Jahresstrombedarf',
        p1: 'z. B. Produktions-/Kühlbetrieb · ca. 800 m² Dachfläche',
        l2: 'Bevorzugtes Modell (Kauf / Lastspitzen-Speicher / Contracting)',
        p2: 'z. B. Vergleich Eigeninvestition vs. Solar-Contracting'
      }},
      'Batteriespeicher-Nachrüstung, Service oder E-Ladestation': {{
        assignee: 'Jonathan Muggli (Speicher, Elektrotechnik & Service)',
        l1: 'Bestehende Solaranlage (Leistung kWp & Wechselrichter)',
        p1: 'z. B. Bestehende 14 kWp Anlage aus 2021',
        l2: 'Gewünschte Erweiterung (Speicher / Notstrom / Solar Manager)',
        p2: 'z. B. Nachrüstung 10 kWh Batteriespeicher & Solar Manager'
      }}
    }};

    function wpUpdateIsHeader() {{
      var titles = {{
        1: '1. Für welches Objekt planen Sie eine Solaranlage?',
        2: '2. Eckdaten zu Dach, Speicher & Zeitplan',
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
      var cfg = wpIsRoleConfig[topic] || wpIsRoleConfig['Einfamilienhaus: Photovoltaik, Speicher & Solar Manager'];
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
        txt.textContent = 'PLZ ' + m[1] + ': Direktes Einsatzgebiet JOMA Solar GmbH (Wettingen / Kanton Aargau)';
      }} else if (plz >= 8000 && plz <= 8999) {{
        txt.textContent = 'PLZ ' + m[1] + ': Direktes Einsatzgebiet Region Zürich / Limmattal / Wehntal';
      }} else {{
        txt.textContent = 'PLZ ' + m[1] + ': Persönliche Projektprüfung durch JOMA Solar Wettingen';
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
      wpSelectIsTopic('Einfamilienhaus: Photovoltaik, Speicher & Solar Manager');
      wpSelectIsUrgency('Zeitnah (Beratung & Offerte in den nächsten 1–2 Wochen)');
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

      var cfg = wpIsRoleConfig[wpIsState.topic] || wpIsRoleConfig['Einfamilienhaus: Photovoltaik, Speicher & Solar Manager'];
      var extra = {{}};
      extra[cfg.l1] = d1 || 'Vor-Ort-Besichtigung / Luftbild-Prüfung';
      extra[cfg.l2] = d2 || 'Persönliche Abstimmung mit JOMA Solar';

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
        message: msg || ('Solar-Anfrage zu ' + wpIsState.topic),
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
        document.getElementById('wpResAssigned').textContent = res.assigned_to || 'Jonathan Muggli & Marco Keller';
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
          errBox.textContent = 'Netzwerkfehler bei der Übermittlung. Bitte schreiben Sie direkt an info@joma-solar.ch oder rufen Sie 056 558 48 82 an.';
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
          'efh': 'Einfamilienhaus: Photovoltaik, Speicher & Solar Manager',
          'mfh': 'Mehrfamilienhaus & ZEV (Eigenverbrauchsgemeinschaft)',
          'zev': 'Mehrfamilienhaus & ZEV (Eigenverbrauchsgemeinschaft)',
          'gewerbe': 'Gewerbeanlage, Grossanlage oder Solar-Contracting',
          'contracting': 'Gewerbeanlage, Grossanlage oder Solar-Contracting',
          'speicher': 'Batteriespeicher-Nachrüstung, Service oder E-Ladestation'
        }};
        if (map[t]) {{
          wpSelectIsTopic(map[t]);
        }}
        var kwp = params.get('kwp');
        var speicher = params.get('speicher');
        if (kwp) {{
          var d1 = document.getElementById('wpDetail1');
          if (d1) d1.value = 'Vorab-Rechner: ca. ' + kwp + ' kWp Solaranlage';
        }}
        if (speicher) {{
          var d2 = document.getElementById('wpDetail2');
          if (d2) d2.value = 'Speicher-Wunsch: ' + speicher;
        }}
      }} catch(err) {{}}
    }})();
  </script>
"""


# 3. Alle Seiten für Variante 1 (Vollversion) schreiben
v1_pages = [
    ("index.html", "JOMA Solar GmbH · Wettingen | Solaranlagen, Batteriespeicher & ZEV im Aargau", "startseite", V1_INDEX_BODY),
    ("leistungen.html", "Leistungen: Privatkunden, Gewerbe, Batteriespeicher & Contracting | JOMA Solar GmbH Wettingen", "leistungen", V1_LEISTUNGEN_BODY),
    ("referenzen.html", "Referenzprojekte aus Wettingen, Baden, Rütihof & Untersiggenthal | JOMA Solar GmbH", "referenzen", V1_REFERENZEN_BODY),
    ("ueber-uns.html", "Über JOMA Solar GmbH, 5er-Team & Karriere in Wettingen | Jonathan Muggli & Marco Keller", "ueber-uns", V1_UEBER_UNS_BODY),
    ("kontakt.html", "Kontakt & 3-Schritte Smart-Anfrage | JOMA Solar GmbH · Tägerhardstrasse 90, 5430 Wettingen", "kontakt", build_kontakt_body("joma-v1", "preview-joma/kontakt.html")),
]

for fname, title, nav_key, body in v1_pages:
    full_html = render_v1_shell(fname, title, nav_key, body)
    (V1_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V1] Wrote {fname} ({len(full_html)} bytes)")

# 4. Alle Seiten für Variante 2 (Zeigeversion / Vorschau-Entwurf) schreiben
v2_pages = [
    ("index.html", "JOMA Solar GmbH · Wettingen (Zeigeversion / Vorschau-Entwurf) | Solar einfach effizient", "startseite", V2_INDEX_BODY),
    ("kontakt.html", "Kontakt & 3-Schritte Smart-Anfrage (Zeigeversion) | JOMA Solar GmbH Wettingen", "kontakt", build_kontakt_body("joma", "preview-joma-v2/kontakt.html")),
]

for fname, title, nav_key, body in v2_pages:
    full_html = render_v2_shell(fname, title, nav_key, body)
    (V2_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V2] Wrote {fname} ({len(full_html)} bytes)")

for stale in ["leistungen.html", "referenzen.html", "projekte.html", "ueber-uns.html"]:
    p = V2_DIR / stale
    if p.exists():
        p.unlink()

# 5. Partner-Attribution (#wpPartnerModal für Jenny Ettle JE-MI) injizieren
subprocess.run(["python3", str(BASE_DIR / "scripts" / "inject_partner_attribution.py")], check=True)

# 6. Studio Cockpit v4.0 (cockpit.html) für beide Varianten generieren
subprocess.run(["python3", str(BASE_DIR / "scripts" / "build_client_cockpit.py"), "--slug", "preview-joma"], check=True)
subprocess.run(["python3", str(BASE_DIR / "scripts" / "build_client_cockpit.py"), "--slug", "preview-joma-v2"], check=True)

# 7. Compile Site Pipeline (Pre-Build Gates & Airbag)
subprocess.run(["python3", str(BASE_DIR / "scripts" / "compile_site.py"), "--site", "preview-joma", "--skip-device-audit"], check=True)
subprocess.run(["python3", str(BASE_DIR / "scripts" / "compile_site.py"), "--site", "preview-joma-v2", "--skip-device-audit"], check=True)
print("Successfully built and compiled preview-joma and preview-joma-v2.")

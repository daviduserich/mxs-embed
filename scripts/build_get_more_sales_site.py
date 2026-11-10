#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator für die WebPilot-Referenz-Aufbereitung von get-more-sales.org (get.more.sales · Carmen Caselli, Zofingen, Kanton Aargau):
- Variante 1 (Vollversion): /home/brainuser/workspaces/mxs-embed/preview-get-more-sales
  Live-URL: https://vorschau.magnet-xs.ch/get-more-sales-vollversion/ (5 voll ausgebaute Seiten + Studio Cockpit v4.0)
- Variante 2 (Zeigeversion / Vorschau-Entwurf): /home/brainuser/workspaces/mxs-embed/preview-get-more-sales-v2
  Live-URL: https://vorschau.magnet-xs.ch/get-more-sales-v2/ (2 ausgearbeitete Beispiel-Seiten: Startseite inkl. B2B-Potenzial-Rechner + 3-Schritte Smart-Anfrage,
  plus transparente Themenbereich-Vorschaukarten für die 3 weiteren Unterseiten).

Exklusiv zugeordnet auf: David Hügli (Magnet XS) — partner_id = "david"

Strikt nach:
- UI-LAYOUT-RULES.md (Canary: UI-LAYOUT-2026-V1, #UI-01, #UI-02, #UI-13, #UI-14, #UI-16 Evolution-Modus Light Lock S-27)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1, 0 Eszett, 0 Em-Dash im Satz, Einser-Ausschreibungs-Regel, 100 % Schweizer Hochdeutsch)
"""

import json
import subprocess
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
V1_DIR = BASE_DIR / "preview-get-more-sales"
V2_DIR = BASE_DIR / "preview-get-more-sales-v2"

V1_DIR.mkdir(parents=True, exist_ok=True)
V2_DIR.mkdir(parents=True, exist_ok=True)

BEFORE_INVENTORY = {
    "source_url": "https://get-more-sales.org/",
    "crawled_at": "2026-11-10",
    "company_name": "get.more.sales · Carmen Caselli",
    "legal_entity": "Carmen Caselli get.more.sales",
    "uid": "CHE-471.125.841",
    "claim": "Entfesseln Sie Ihr Verkaufspotenzial. Strukturiert, menschlich, messbar.",
    "subline": "B2B-Verkaufsberatung, praxisnahes Vertriebstraining und 1:1 Sales-Sparring für Geschäftsführer, Verkaufsleiter und Vertriebsteams im Raum Zofingen, Aargau und im gesamten DACH-Raum mit Carmen Caselli.",
    "address": {
        "street": "Zofingen",
        "zip": "4800",
        "city": "Zofingen",
        "canton": "AG",
        "country": "Schweiz"
    },
    "contact": {
        "email": "beratungs-termin@get-more-sales.org",
        "email_impressum": "impressum@get-more-sales.org",
        "phone_primary": "",
        "phone_display": "",
        "linkedin": "https://www.linkedin.com/in/carmen-caselli/",
        "hours": "Persönliche Rückmeldung in der Regel innerhalb von 5 bis 12 Arbeitsstunden | Termine vor Ort, telefonisch oder via Video-Call"
    },
    "team": [
        {
            "name": "Carmen Caselli",
            "role": "Geschäftsführerin get.more.sales · Verkaufsberaterin & Business Mentorin",
            "phone": "",
            "phone_href": "",
            "image": "images/carmen-caselli-portrait-color.jpg",
            "qualification": "18+ Jahre Finanz- & Bankenpraxis (Treasury & Portfolio Management CHF Bonds) · Vollzeit-Tauchlehrerin (Thailand) · Seit 2019 Geschäftsführerin get.more.sales & Business Mentorin",
            "bio": "Carmen Caselli verbindet die analytische Schärfe aus 18 Jahren Finanz- und Kapitalmarktpraxis mit der absoluten Klarheit einer erfahrenen Tauchlehrerin und über sieben Jahren B2B-Vertriebs- und Führungsexpertise. Seit 2019 begleitet sie mit get.more.sales Unternehmen, Verkaufsteams und Entscheider dabei, Verkaufsprozesse zu strukturieren, Abschlussquoten nachhaltig zu steigern und Kunden auf Augenhöhe zu gewinnen."
        }
    ],
    "references": [
        {
            "title": "Kundenstimme Matthias · Strategie & Umsatz",
            "category": "Kundenstimme · B2B",
            "highlight": "Mehr Umsatz & Neukunden",
            "scope": "Massgeschneiderte Verkaufsstrategie und nachhaltige Umsatzsteigerung",
            "before_img": "images/leistung-verkaufsstrategie-beratung.png",
            "after_img": "images/carmen-caselli-portrait-color.jpg",
            "desc": "«Dank Carmen von get-more-sales hat sich unsere Verkaufsstrategie erheblich verbessert. Ihre Expertenberatung hat uns geholfen, mehr Kunden anzuziehen und unseren Umsatz zu steigern. Wir sind mit ihren Dienstleistungen äusserst zufrieden und empfehlen sie jedem Unternehmen, das seine Umsätze steigern möchte!»"
        },
        {
            "title": "B2B-Vertriebsarchitektur & Pipeline-Klarheit",
            "category": "Praxis-Einblick · Strategie",
            "highlight": "Klare Kundenreise",
            "scope": "Vom reaktiven Offert-Versand zur strukturierten Nachfass- und Abschluss-Routine",
            "before_img": "images/hero-sales-dashboard-analytics.png",
            "after_img": "images/sales-gallery-meeting-sparring.png",
            "desc": "Viele KMU verlieren wertvolle Aufträge nach dem Versenden der Offerte. Durch klar definierte Kontaktpunkte, verbindliche nächste Schritte im Erstgespräch und ein sauberes Pipeline-Management steigt die Abschlussquote planbar an."
        },
        {
            "title": "Preisgespräche & Abschlussstärke ohne Rabattschlacht",
            "category": "Praxis-Einblick · Training",
            "highlight": "Marge schützen",
            "scope": "Wertargumentation und souveräne Einwandbehandlung im B2B-Verkauf",
            "before_img": "images/leistung-vertriebstraining-entwicklung.png",
            "after_img": "images/carmen-caselli-portrait-duplex-card.jpg",
            "desc": "Statt bei Einwänden sofort über den Preis nachzugeben, trainiert Ihr Team eine präzise Bedarfs- und Nutzen-Frageführung. So erkennen Entscheider den wirtschaftlichen Mehrwert Ihrer Lösung vor der Preisverhandlung."
        },
        {
            "title": "Marktforschung & Zielgruppen-Positionierung",
            "category": "Praxis-Einblick · Analyse",
            "highlight": "Potenziale erkennen",
            "scope": "Fundierte Marktdaten, Kundenbedürfnisse und lukrative Zielsegmente identifizieren",
            "before_img": "images/leistung-marktforschung-analyse.png",
            "after_img": "images/hero-sales-dashboard-analytics.png",
            "desc": "Unsere Marktforschungs- und Analysedienste liefern Ihnen wertvolle Einblicke in Ihren Markt und Ihre Zielgruppe. Sie erkennen frühzeitig zukünftige Chancen und richten Ihre Verkaufsaktivitäten auf die profitabelsten Kundensegmente aus."
        },
        {
            "title": "Moderne B2B-Akquise: Telefon & LinkedIn",
            "category": "Praxis-Einblick · Akquise",
            "highlight": "Termine auf Augenhöhe",
            "scope": "Kombinierte Ansprache über Telefon, Empfehlungsaufbau und Social Selling",
            "before_img": "images/sales-gallery-meeting-sparring.png",
            "after_img": "images/carmen-caselli-portrait-full-card.jpg",
            "desc": "Kein aufgesetztes Skript-Ablesen: Wir entwickeln für Ihr Team eine menschliche, respektvolle Ansprache per Telefon und LinkedIn, die bei Geschäftsführern und Einkäufern echtes Interesse weckt und zu qualifizierten Erstterminen führt."
        },
        {
            "title": "1:1 Executive Sales-Sparring für Entscheider",
            "category": "Praxis-Einblick · Sparring",
            "highlight": "Verhandlungssicherheit",
            "scope": "Persönliche Vorbereitung auf Schlüsselkunden, Pitches und Jahresgespräche",
            "before_img": "images/carmen-caselli-portrait-duplex-card.jpg",
            "after_img": "images/boost-your-sales-stage.png",
            "desc": "Vor entscheidenden Grosskunden-Terminen oder komplexen Vergaben reflektieren wir gemeinsam Verhandlungsstrategie, Entscheidungsmotive und Einwände: ruhig, ehrlich und fokussiert wie beim Check vor einem Tauchgang."
        }
    ],
    "faqs": [
        {
            "q": "Für welche Unternehmen eignet sich die Zusammenarbeit mit get.more.sales?",
            "a": "Wir begleiten B2B-Unternehmen, KMU-Geschäftsführer, Verkaufsleiter, Aussendienst-Teams sowie beratungsintensive Dienstleister in der Schweiz und im DACH-Raum, die ihre Verkaufsstrategie schärfen, ihre Abschlussquote erhöhen und eine verlässliche Neukunden-Routine aufbauen wollen."
        },
        {
            "q": "Was unterscheidet Carmen Casellis Ansatz von klassischen Verkaufstrainings?",
            "a": "Bei get.more.sales gibt es keine aggressiven Druck-Techniken und keine auswendig gelernten Phrasen. Carmen Caselli verbindet analytische Klarheit aus 18 Jahren Finanzpraxis mit echter, menschlicher Begeisterung. Ihr Team lernt, durch präzise Fragen, ehrliches Interesse und glasklare Prozesse auf Augenhöhe abzuschliessen."
        },
        {
            "q": "Wie schnell erhalte ich eine Rückmeldung auf meine Anfrage?",
            "a": "Auf Ihre Anfrage über unsere 3-Schritte Smart-Anfrage oder per E-Mail an beratungs-termin@get-more-sales.org antwortet Carmen Caselli persönlich in der Regel innerhalb von 5 bis 12 Arbeitsstunden."
        },
        {
            "q": "Wie läuft ein kostenloser erster Beratungstermin ab?",
            "a": "Im unverbindlichen Erstgespräch (telefonisch oder per Video-Call) beleuchten wir Ihre aktuelle Vertriebssituation, Ihre Zielgruppe und die grössten Hebel in Ihrem Verkaufsprozess. Sie erhalten bereits im Gespräch eine ehrliche Einschätzung, welche Schritte den schnellsten ROI bringen."
        },
        {
            "q": "Können Strategieberatung und praktisches Vertriebstraining kombiniert werden?",
            "a": "Ja, genau diese Kombination erzielt in der Praxis die stärkste Wirkung: Zuerst schärfen wir Ihre Verkaufsstrategie, Positionierung und Pipeline-Struktur, und anschliessend verankern wir die Gesprächsführung, Einwandbehandlung und Abschlussroutine direkt im Alltag Ihres Verkaufsteams."
        },
        {
            "q": "Wo hat get.more.sales seinen Sitz und wo finden Trainings statt?",
            "a": "Sitz von Carmen Caselli get.more.sales (CHE-471.125.841) ist in Zofingen im Kanton Aargau. Beratungen, Workshops und Verkaufstrainings führen wir direkt bei Ihnen im Unternehmen in der ganzen Schweiz, im DACH-Raum oder flexibel online durch."
        }
    ]
}

(V1_DIR / "before.json").write_text(json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False), encoding="utf-8")
(V2_DIR / "before.json").write_text(json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False), encoding="utf-8")

for target_dir, slug_val, pub_slug, is_v2 in [
    (V1_DIR, "preview-get-more-sales", "get-more-sales-vollversion", False),
    (V2_DIR, "preview-get-more-sales-v2", "get-more-sales-v2", True)
]:
    (target_dir / "company.json").write_text(json.dumps({
        "company_name": "get.more.sales · Carmen Caselli" + (" (Zeigeversion / Vorschau-Entwurf)" if is_v2 else " · Verkaufsberatung & Vertriebstraining"),
        "slug": slug_val,
        "public_slug": pub_slug,
        "cockpit_token": "getmoresales2026",
        "city": "Zofingen",
        "canton": "AG",
        "postal_code": "4800",
        "street_address": "Zofingen (Kanton Aargau)",
        "phone": "",
        "email": "beratungs-termin@get-more-sales.org",
        "uid": "CHE-471.125.841",
        "source_url": "https://get-more-sales.org/",
        "linkedin_url": "https://www.linkedin.com/in/carmen-caselli/",
        "partner_id": "david"
    }, indent=2, ensure_ascii=False), encoding="utf-8")

v1_config = {
    "company_name": "get.more.sales · Carmen Caselli · Zofingen / Aargau",
    "slug": "preview-get-more-sales",
    "public_slug": "get-more-sales-vollversion",
    "cockpit_token": "getmoresales2026",
    "template": "executive-sales-authority-v1",
    "partner_id": "david",
    "pages": ["index.html", "leistungen.html", "referenzen.html", "ueber-uns.html", "kontakt.html"]
}
(V1_DIR / "config.json").write_text(json.dumps(v1_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V1_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-get-more-sales",
    "public_slug": "get-more-sales-vollversion",
    "token": "getmoresales2026",
    "name": "get.more.sales · Carmen Caselli · Verkaufsberatung & Vertriebstraining (Vollversion)",
    "Updated": "2026-11-10",
    "PagesCount": 5,
    "ReferencesCount": 6,
    "TeamCount": 1
}, indent=2, ensure_ascii=False), encoding="utf-8")

v2_config = dict(v1_config)
v2_config.update({
    "company_name": "get.more.sales · Carmen Caselli (Zeigeversion / Vorschau-Entwurf)",
    "slug": "preview-get-more-sales-v2",
    "public_slug": "get-more-sales-v2",
    "cockpit_token": "getmoresales2026",
    "template": "executive-sales-authority-preview-v2",
    "partner_id": "david",
    "pages": ["index.html", "kontakt.html"]
})
(V2_DIR / "config.json").write_text(json.dumps(v2_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V2_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-get-more-sales-v2",
    "public_slug": "get-more-sales-v2",
    "token": "getmoresales2026",
    "name": "get.more.sales · Carmen Caselli (Zeigeversion / Vorschau-Entwurf)",
    "Updated": "2026-11-10",
    "PagesCount": 2,
    "ReferencesCount": 6,
    "TeamCount": 1
}, indent=2, ensure_ascii=False), encoding="utf-8")

print("Wrote before.json, company.json, config.json, site.json for V1 and V2.")

SHARED_CSS = """
    :root {
      --charcoal: #003366;
      --charcoal-deep: #0E1721;
      --charcoal-mid: #1E3A5F;
      --wp-expected-hero-polarity: "light";
      --wp-archetype: "executive_sales_authority";
      --gold: #0B5CAB;
      --gold-hover: #003E7E;
      --gold-dark: #003E7E;
      --gold-soft: #E9F2FC;
      --gold-border: #BDD4EE;
      --crimson: #0B5CAB;
      --crimson-soft: #E9F2FC;
      --green: #15803D;
      --green-soft: #DCFCE7;
      --bg-page: #F7FAFF;
      --bg-card: #FFFFFF;
      --bg-Warm: #EBF3FC;
      --text-main: #0E1721;
      --text-body: #243447;
      --text-muted: #4A5B6E;
      --border-light: #D5E1EF;
      --border-strong: #B8CBE0;
      --radius-sm: 4px;
      --radius-md: 8px;
      --shadow-sm: 0 2px 10px rgba(14, 23, 33, 0.05);
      --shadow-md: 0 12px 30px rgba(14, 23, 33, 0.08);
      --shadow-lg: 0 20px 44px rgba(14, 23, 33, 0.12);
      --container: 1180px;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    ::selection {
      background-color: rgba(11, 92, 171, 0.18);
      color: #0E1721;
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
      background-color: #EBF3FC;
      color: #243447;
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
      background-color: #E9F2FC;
      color: #003E7E;
      border: 1px solid #BDD4EE;
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
      color: #0E1721;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-height: 32px;
      padding: 5px 8px;
    }
    .top-bar-links a:hover {
      color: #0B5CAB;
    }

    /* Sticky Main Header (#UI-02: 1-Zeilen-Navigations-Gesetz) */
    .site-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background-color: rgba(247, 250, 255, 0.97);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border-light);
      box-shadow: 0 2px 12px rgba(14, 23, 33, 0.05);
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
      color: #003E7E;
      background: transparent;
      border-bottom-color: #0B5CAB;
    }
    .nav-link-preview {
      color: var(--text-muted);
      background: transparent;
      border: none;
      border-bottom: 2px dashed rgba(11, 92, 171, 0.42);
      font-size: 0.86rem;
    }
    .nav-link-preview:hover {
      color: #003E7E;
      background: transparent;
      border-bottom-color: #0B5CAB;
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
      background-color: #0B5CAB;
      color: #FFFFFF;
      border-color: #0B5CAB;
      font-weight: 600;
    }
    .btn-cta-gold:hover {
      background-color: #003E7E;
      color: #FFFFFF;
      border-color: #003E7E;
      transform: translateY(-1px);
    }
    .btn-cta-primary {
      background-color: #0B5CAB;
      color: #FFFFFF;
      border-color: #0B5CAB;
    }
    .btn-cta-primary:hover {
      background-color: #003E7E;
      color: #FFFFFF;
      border-color: #003E7E;
    }
    .btn-cta-outline {
      background-color: #FFFFFF;
      color: #0E1721;
      border-color: var(--border-strong);
    }
    .btn-cta-outline:hover {
      border-color: #0B5CAB;
      color: #003E7E;
      background-color: var(--gold-soft);
    }
    .btn-cta-outline-light {
      background-color: #FFFFFF;
      color: #0E1721;
      border-color: rgba(11, 92, 171, 0.38);
    }
    .btn-cta-outline-light:hover {
      background-color: #E9F2FC;
      color: #003E7E;
      border-color: #0B5CAB;
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
      color: #0E1721;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }
    .mobile-drawer {
      display: none;
      flex-direction: column;
      gap: 8px;
      padding: 16px 24px 22px;
      background-color: #F7FAFF;
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
      color: #0E1721;
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
      color: #003E7E;
      border-style: dashed;
      border-color: rgba(11, 92, 171, 0.45);
    }

    /* Hero Section: Hell, warm & handwerklich klar (#UI-16 Evolution, S-27 Light Lock & #UI-02 Bottom-Edge Baseline Lock) */
    .hero-section {
      background: linear-gradient(135deg, #FFFFFF 0%, #F7FAFF 55%, #EBF3FC 100%);
      background-color: #F7FAFF;
      color: #0E1721;
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
      color: #0E1721;
      line-height: 1.14;
      margin-bottom: 18px;
    }
    .hero-title span {
      color: #0B5CAB;
    }
    .hero-lead {
      font-size: 1.04rem;
      color: #243447;
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
      border-left: 3px solid #0B5CAB;
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
      color: #003E7E;
    }
    .hero-badge-lbl {
      font-size: 0.78rem;
      color: #243447;
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
      background-color: #EBF3FC;
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
      background: linear-gradient(135deg, #FFFFFF 0%, #E9F2FC 100%);
      background-color: #E9F2FC;
      color: #0E1721;
      border-color: #BDD4EE;
      border-top: 4px solid #0B5CAB;
    }
    .content-card.card-dark h3 {
      color: #0E1721;
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
      background-color: #E9F2FC;
      color: #0B5CAB;
      border: 1px solid #BDD4EE;
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
      border: 2px solid var(--border-strong);
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
      background-color: #EBF3FC;
      border-top: 2px dashed rgba(11, 92, 171, 0.38);
      border-bottom: 2px dashed rgba(11, 92, 171, 0.38);
      padding: 76px 0 88px;
    }
    .preview-scope-banner {
      background-color: #FFFFFF;
      color: #0E1721;
      border: 2px dashed #0B5CAB;
      border-radius: var(--radius-md);
      padding: 28px 30px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-md);
    }
    .preview-module-card {
      background-color: #FFFFFF;
      border: 2px dashed #0B5CAB;
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
      background-color: #EBF3FC;
      color: #0E1721;
      padding: 68px 0 36px;
      border-top: 3px solid #0B5CAB;
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
      color: #0E1721;
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
      color: #243447;
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
      color: #0B5CAB;
    }
    .footer-bottom {
      padding-top: 26px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      font-size: 0.82rem;
      color: #243447;
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
      background-color: rgba(14, 23, 33, 0.76);
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
      background-color: #0B5CAB;
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
      border: 2px solid var(--border-strong);
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
      background-color: #E9F2FC;
      color: #0B5CAB;
      border: 1px solid #BDD4EE;
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
      box-shadow: 0 0 0 3px rgba(11, 92, 171, 0.16);
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
      color: #002B59;
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
"""

SVG_CHECK = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>'
SVG_ARROW = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'
SVG_HOME = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>'
SVG_HEART = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'
SVG_LAYERS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>'
SVG_SHIELD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
SVG_AWARD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>'
SVG_USERS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
SVG_COMPASS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>'
SVG_MAP_PIN = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'
SVG_PHONE = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
SVG_MAIL = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'


def render_references_grid(limit: int = 6, is_v2: bool = False) -> str:
    cards = []
    for ref in BEFORE_INVENTORY["references"][:limit]:
        cta_html = (
            f'''<button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Praxis-Einblick: {ref['title']}', '{ref['category']} · {ref['scope']} · {ref.get('highlight', 'Echtes Resultat')}', 'Carmen Caselli (get.more.sales)')">
              <span>Praxis-Einblick &amp; Resultat ansehen</span>
              {SVG_ARROW}
            </button>'''
            if is_v2
            else f'''<a href="kontakt.html?thema=strategie" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Ähnliches Vertriebsziel mit Carmen besprechen</span>
              {SVG_ARROW}
            </a>'''
        )
        cards.append(f"""
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="{ref['after_img']}" alt="get.more.sales Carmen Caselli B2B Vertriebsberatung: {ref['title']}" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">{ref['category']}</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.76rem;font-weight:700;color:var(--gold-dark);">{ref.get('highlight', 'Praxis-Einblick')}</span>
              </div>
              <h3 style="font-size:1.2rem;font-weight:700;margin-bottom:6px;">{ref['title']}</h3>
              <p style="font-size:0.82rem;font-weight:700;color:var(--gold-dark);margin-bottom:10px;">{ref['scope']}</p>
              <p style="font-size:0.89rem;color:var(--text-body);margin-bottom:12px;">{ref['desc']}</p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span><strong>Fokus:</strong> {ref['scope']}</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Wirkung:</strong> {ref.get('highlight', 'Messbares Umsatzwachstum')}</span></div>
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
              <span class="meta-badge">Häufige Frage #{idx+1}</span>
              <span class="icon-box">{SVG_COMPASS}</span>
            </div>
            <h3 style="font-size:1.14rem;font-weight:700;margin-bottom:10px;">{f['q']}</h3>
            <p style="font-size:0.9rem;color:var(--text-body);line-height:1.62;">{f['a']}</p>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Persönlich mit Carmen Caselli klären</span>
            {SVG_ARROW}
          </a>
        </div>""")
    return '<div class="grid-2">\n' + "\n".join(cards) + "\n      </div>"


def render_sales_advisor() -> str:
    return f"""
  <!-- INTERAKTIVER B2B-VERTRIEBS- & AKQUISE-POTENZIAL-RECHNER / SPARRING-FINDER -->
  <section data-section="projektberater" id="projektberater" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="calc_kicker">INTERAKTIVER B2B-POTENZIAL- &amp; SPARRING-FINDER · GET.MORE.SALES</div>
        <h2 class="section-title" data-slot="calc_title">Welcher Vertriebs-Hebel bringt Ihrem Unternehmen den schnellsten Ertrag?</h2>
        <p class="section-desc" data-slot="calc_desc">
          Wählen Sie Ihre Rolle, Ihren aktuell grössten Engpass im Verkauf und das gewünschte Begleitungsformat. Unser Potenzial-Finder zeigt Ihnen sofort die passende Empfehlung von Carmen Caselli:
        </p>
      </div>

      <div class="grid-2">
        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">In 15 Sekunden auswählen</span>
              <span class="icon-box">{SVG_COMPASS}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:14px;">1. Ihre Rolle &amp; Ausgangslage</h3>
            <div class="calc-option-grid" id="susiCalcRoleGrid">
              <button type="button" class="calc-option-btn active" data-role="privat" onclick="susiSetCalc('role','privat')">
                <span class="calc-opt-title">Geschäftsführung</span>
                <span class="calc-opt-sub">Inhaber, CEO &amp; KMU-Entscheider</span>
              </button>
              <button type="button" class="calc-option-btn" data-role="architektur" onclick="susiSetCalc('role','architektur')">
                <span class="calc-opt-title">Verkaufsleitung</span>
                <span class="calc-opt-sub">B2B-Vertriebsteam &amp; Aussendienst</span>
              </button>
              <button type="button" class="calc-option-btn" data-role="bau" onclick="susiSetCalc('role','bau')">
                <span class="calc-opt-title">Expertin / Berater</span>
                <span class="calc-opt-sub">Dienstleister &amp; Key Account</span>
              </button>
            </div>

            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:14px;">2. Wichtigster Engpass im Verkauf</h3>
            <div class="calc-option-grid" id="susiCalcScopeGrid">
              <button type="button" class="calc-option-btn active" data-scope="dach" onclick="susiSetCalc('scope','dach')">
                <span class="calc-opt-title">Strategie</span>
                <span class="calc-opt-sub">Struktur, Pipeline &amp; Prozesse</span>
              </button>
              <button type="button" class="calc-option-btn" data-scope="innen" onclick="susiSetCalc('scope','innen')">
                <span class="calc-opt-title">Neukunden</span>
                <span class="calc-opt-sub">Telefon, LinkedIn &amp; Ersttermine</span>
              </button>
              <button type="button" class="calc-option-btn" data-scope="aussen" onclick="susiSetCalc('scope','aussen')">
                <span class="calc-opt-title">Abschlussstärke</span>
                <span class="calc-opt-sub">Einwände, Preis &amp; Nachfassen</span>
              </button>
            </div>

            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:14px;">3. Gewünschtes Begleitungsformat</h3>
            <div class="calc-option-grid" id="susiCalcModeGrid" style="margin-bottom:0;">
              <button type="button" class="calc-option-btn active" data-mode="komplett" onclick="susiSetCalc('mode','komplett')">
                <span class="calc-opt-title">Strategie &amp; Audit</span>
                <span class="calc-opt-sub">Standortbestimmung &amp; Fahrplan</span>
              </button>
              <button type="button" class="calc-option-btn" data-mode="mithilfe" onclick="susiSetCalc('mode','mithilfe')">
                <span class="calc-opt-title">Team-Training</span>
                <span class="calc-opt-sub">Praxis-Workshop &amp; Leitfäden</span>
              </button>
              <button type="button" class="calc-option-btn" data-mode="leitung" onclick="susiSetCalc('mode','leitung')">
                <span class="calc-opt-title">1:1 Sparring</span>
                <span class="calc-opt-sub">Persönliches Mentoring mit Carmen</span>
              </button>
            </div>
          </div>
          <div style="padding-top:14px;border-top:1px solid var(--border-light);font-size:0.82rem;color:var(--text-body);display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;">
            <span>Verkaufen auf Augenhöhe mit Klarheit &amp; Struktur</span>
            <strong style="color:var(--gold-dark);font-family:'Lexend',sans-serif;">get.more.sales · Carmen Caselli</strong>
          </div>
        </div>

        <div class="content-card card-dark">
          <div>
            <div class="card-badge-row">
              <span class="top-bar-badge" id="susiCalcRefBadge">EMPFEHLUNG: B2B-VERKAUFSSTRATEGIE &amp; PROZESS-OPTIMIERUNG</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 style="font-size:1.36rem;font-weight:700;margin-bottom:8px;" id="susiCalcHeadline">Massgeschneiderte Verkaufsstrategie &amp; strukturierte B2B-Pipeline</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;" id="susiCalcDesc">
              Gemeinsam analysieren wir Ihre aktuellen Verkaufsprozesse, schärfen Ihre Zielgruppen-Positionierung und bauen eine verlässliche Kundenreise vom Erstkontakt bis zum unterschriebenen Auftrag auf.
            </p>

            <div class="calc-kpi-grid">
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="susiCalcLead">5–12 Arbeitsstunden</div>
                <div class="calc-kpi-lbl">Persönliche Reaktionszeit von Carmen Caselli</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="susiCalcModeOut">Strategie &amp; Prozess-Audit</div>
                <div class="calc-kpi-lbl">Gewähltes Begleitungsformat</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="susiCalcPartner">Zofingen / AG &amp; DACH</div>
                <div class="calc-kpi-lbl">Vor Ort bei Ihnen oder via Video-Call</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="susiCalcStep">Kostenloses Erstgespräch</div>
                <div class="calc-kpi-lbl">Unverbindliche Potenzial-Einschätzung</div>
              </div>
            </div>

            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Analytische Klarheit:</strong> 18 Jahre Finanz- &amp; Kapitalmarkterfahrung kombiniert mit B2B-Vertriebspraxis</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Ohne künstlichen Kaufdruck:</strong> Bedarfsanalyse, Wertargumentation und Abschluss auf Augenhöhe</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Messbare Umsetzung:</strong> Direkt anwendbare Leitfäden, Playbooks und 1:1 Sparring im Verkaufsalltag</span></div>
            </div>
          </div>

          <a href="kontakt.html?thema=strategie" id="susiCalcCta" class="btn-cta btn-cta-gold" style="width:100%;">
            <span>Kostenlosen Beratungstermin mit Carmen Caselli anfragen</span>
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
      <div class="section-kicker">RECHTLICHE ANGABEN · KANTON AARGAU (SCHWEIZ)</div>
      <h3 id="wpImpTitle" style="font-size:1.36rem;font-weight:700;margin-bottom:10px;">Impressum &amp; Datenschutz (get.more.sales)</h3>
      <div style="font-size:0.88rem;color:var(--text-body);line-height:1.62;display:flex;flex-direction:column;gap:12px;">
        <div style="background-color:var(--bg-page);border:1px solid var(--border-light);border-left:4px solid var(--gold);padding:12px 14px;border-radius:var(--radius-sm);">
          <strong>Carmen Caselli get.more.sales</strong><br>
          Inhaberin &amp; Geschäftsführerin: Carmen Caselli · CH-4800 Zofingen (Kanton Aargau, Schweiz)<br>
          Unternehmens-Identifikationsnummer (UID): <strong>CHE-471.125.841</strong><br>
          E-Mail: beratungs-termin@get-more-sales.org · Impressum: impressum@get-more-sales.org
        </div>
        <p>
          <strong>Verantwortliche Person &amp; Tätigkeit:</strong><br>
          Carmen Caselli, Zofingen. Verkaufsberatung, Marktforschung, Vertriebstraining und Business Mentoring für Unternehmen im Raum Schweiz und DACH.
        </p>
        <p>
          <strong>Urheber- &amp; Bildrechte:</strong><br>
          Sämtliche auf dieser Website gezeigten Porträts, Grafiken, Konzepte, Texte und Logos sind urheberrechtlich geschütztes Eigentum von Carmen Caselli get.more.sales.
        </p>
        <p>
          <strong>Datenschutz (Schweizer DSG &amp; DSGVO):</strong><br>
          Alle Angaben aus der 3-Schritte Smart-Anfrage werden streng vertraulich behandelt, ausschliesslich zur Beantwortung Ihrer Anfrage und Terminvereinbarung durch Carmen Caselli verwendet und niemals an unbefugte Dritte weitergegeben.
        </p>
      </div>
      <div style="margin-top:16px;display:flex;justify-content:flex-end;">
        <button type="button" class="btn-cta btn-cta-primary btn-sm" onclick="wpCloseImpressumModal()">
          <span>Schliessen</span>
        </button>
      </div>
    </div>
  </div>"""


COMMON_UI_JS = """
  <script>
    function wpOpenImpressumModal() {
      var m = document.getElementById('wpImpressumModal');
      if (m) m.classList.add('open');
    }
    function wpCloseImpressumModal() {
      var m = document.getElementById('wpImpressumModal');
      if (m) m.classList.remove('open');
    }
    function wpOpenBlueprintModal(title, category, person) {
      var m = document.getElementById('wpBlueprintModal');
      if (!m) return;
      var tEl = document.getElementById('wpBpTitle');
      var cEl = document.getElementById('wpBpCategory');
      var pEl = document.getElementById('wpBpContact');
      if (tEl && title) tEl.textContent = title;
      if (cEl && category) cEl.textContent = 'Leistungs- & Themenbereich: ' + category;
      if (pEl && person) pEl.textContent = 'Verantwortliche Expertin: ' + person;
      m.classList.add('open');
    }
    function wpCloseBlueprintModal() {
      var m = document.getElementById('wpBlueprintModal');
      if (m) m.classList.remove('open');
    }
    function wpToggleMobileMenu() {
      var d = document.getElementById('mobileDrawer');
      if (d) d.classList.toggle('open');
    }
    function wpCloseMobileMenu() {
      var d = document.getElementById('mobileDrawer');
      if (d) d.classList.remove('open');
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
        ? 'Team-Training & Workshop'
        : (susiCalcState.mode === 'leitung' ? '1:1 Executive Sales-Sparring' : 'Strategie & Prozess-Audit');
      if (mEl) mEl.textContent = modeLabel;

      if (susiCalcState.role === 'architektur') {
        badge.textContent = 'FÜR VERKAUFSLEITUNG & B2B-VERTRIEBSTEAMS';
        head.textContent = 'Praxisnahes Vertriebstraining & aktive Abschluss-Routine im Team';
        desc.textContent = 'Wir trainieren Ihr Verkaufsteam direkt an echten Praxisfällen: strukturierte Bedarfsanalyse, souveräne Einwandbehandlung und verbindliche Nachfass-Prozesse ohne Rabattschlacht.';
        lEl.textContent = '5–12 Arbeitsstunden';
        pEl.textContent = 'Inhouse & Live-Training';
        sEl.textContent = 'Praxis-Transfer ab Tag 1';
        if (cta) cta.href = 'kontakt.html?thema=training';
      } else if (susiCalcState.role === 'bau') {
        badge.textContent = 'FÜR BERATER, EXPERTEN & KEY ACCOUNT MANAGEMENT';
        head.textContent = '1:1 Sales-Sparring & Positionierung für beratungsintensive Angebote';
        desc.textContent = 'Gewinnen Sie Entscheider auf Augenhöhe über Telefon, Empfehlungen und LinkedIn: klare Nutzenargumentation, hohe Abschlussquote und verlässliche Neukunden-Routine.';
        lEl.textContent = '5–12 Arbeitsstunden';
        pEl.textContent = '1:1 Mentoring mit Carmen';
        sEl.textContent = 'Kostenloses Erstgespräch';
        if (cta) cta.href = 'kontakt.html?thema=sparring';
      } else {
        if (susiCalcState.scope === 'innen') {
          badge.textContent = 'NEUKUNDEN-GEWINNUNG · TELEFON, LINKEDIN & MARKTANALYSE';
          head.textContent = 'Gezielte Marktforschung & moderne B2B-Akquise auf Augenhöhe';
          desc.textContent = 'Wir identifizieren Ihre lukrativsten Zielkunden und richten eine verbindliche Kontakt- und Terminroutine über Telefon und Social Selling ein.';
          lEl.textContent = '5–12 Arbeitsstunden';
          pEl.textContent = 'Akquise & Zielgruppen-Fokus';
          sEl.textContent = 'Qualifizierte Ersttermine';
          if (cta) cta.href = 'kontakt.html?thema=analyse';
        } else if (susiCalcState.scope === 'aussen') {
          badge.textContent = 'PREISVERHANDLUNG & ABSCHLUSSSTÄRKE IM B2B-VERTRIEB';
          head.textContent = 'Höhere Abschlussquote bei Offerten & souveräne Preisgespräche';
          desc.textContent = 'Schluss mit versandeten Offerten: Wir verankern eine klare Entscheidungs- und Nachfass-Architektur, die Ihre Marge schützt und Abschlüsse beschleunigt.';
          lEl.textContent = '5–12 Arbeitsstunden';
          pEl.textContent = 'Marge & Abschlussquote';
          sEl.textContent = 'Sofort umsetzbarer Leitfaden';
          if (cta) cta.href = 'kontakt.html?thema=training';
        } else {
          badge.textContent = 'EMPFEHLUNG: B2B-VERKAUFSSTRATEGIE & PROZESS-OPTIMIERUNG';
          head.textContent = 'Massgeschneiderte Verkaufsstrategie & strukturierte B2B-Pipeline';
          desc.textContent = 'Gemeinsam analysieren wir Ihre aktuellen Verkaufsprozesse, schärfen Ihre Zielgruppen-Positionierung und bauen eine verlässliche Kundenreise vom Erstkontakt bis zum unterschriebenen Auftrag auf.';
          lEl.textContent = '5–12 Arbeitsstunden';
          pEl.textContent = 'Zofingen / AG & DACH';
          sEl.textContent = 'Kostenloses Erstgespräch';
          if (cta) cta.href = 'kontakt.html?thema=strategie';
        }
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
  <meta name="description" content="get.more.sales · Carmen Caselli (Zofingen): Massgeschneiderte B2B-Verkaufsberatung, Marktforschung, praxisnahes Vertriebstraining und 1:1 Sales-Sparring in der Schweiz und im DACH-Raum.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "get.more.sales · Carmen Caselli",
    "legalName": "Carmen Caselli get.more.sales",
    "taxID": "CHE-471.125.841",
    "url": "https://get-more-sales.org",
    "email": "beratungs-termin@get-more-sales.org",
    "founder": {{
      "@type": "Person",
      "name": "Carmen Caselli",
      "jobTitle": "Geschäftsführerin, Verkaufsberaterin & Business Mentorin",
      "sameAs": ["https://www.linkedin.com/in/carmen-caselli/"]
    }},
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Zofingen",
      "postalCode": "4800",
      "addressLocality": "Zofingen",
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
        <span class="top-bar-badge" data-slot="topbar_badge">GET.MORE.SALES · CARMEN CASELLI</span>
        <span data-slot="topbar_sub">Zofingen (AG) · Antwort in 5–12 Arbeitsstunden</span>
      </div>
      <div class="top-bar-links">
        <a href="https://www.linkedin.com/in/carmen-caselli/" target="_blank" rel="noopener noreferrer">{SVG_USERS} <span>LinkedIn · Carmen Caselli</span></a>
        <a href="mailto:beratungs-termin@get-more-sales.org">{SVG_MAIL} <span>beratungs-termin@get-more-sales.org</span></a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER (1-ROW DESKTOP NAV S-22) -->
  <header class="site-header" data-section="header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="get.more.sales Carmen Caselli Startseite">
        <img src="images/logo-get-more-sales.png" alt="get.more.sales Carmen Caselli Logo" class="brand-logo" width="50" height="50" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">get.more.sales</span>
          <span class="brand-sub" data-slot="brand_sub">Carmen Caselli · Verkaufsberatung</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}" data-nav-href="index.html">Startseite</a>
        <a href="leistungen.html" class="nav-link {nav_leistungen}" data-nav-href="leistungen.html">Leistungen</a>
        <a href="referenzen.html" class="nav-link {nav_referenzen}" data-nav-href="referenzen.html">Referenzen</a>
        <a href="ueber-uns.html" class="nav-link {nav_ueber}" data-nav-href="ueber-uns.html">Über Carmen</a>
        <a href="kontakt.html" class="nav-link {nav_kontakt}" data-nav-href="kontakt.html">Kontakt</a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" data-slot="header_cta">
          <span>Beratungstermin buchen</span>
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
    <a href="leistungen.html" onclick="wpCloseMobileMenu()">Leistungen &amp; Trainings</a>
    <a href="referenzen.html" onclick="wpCloseMobileMenu()">Kundenstimmen &amp; Praxis-Cases</a>
    <a href="ueber-uns.html" onclick="wpCloseMobileMenu()">Über Carmen Caselli</a>
    <a href="kontakt.html" onclick="wpCloseMobileMenu()">Kontakt &amp; 3-Schritte Smart-Anfrage</a>
  </div>

  <main>
{body_html}
  </main>

  <!-- FOOTER (VOLLVERSION) -->
  <footer class="site-footer" data-section="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
            <img src="images/logo-get-more-sales.png" alt="get.more.sales Carmen Caselli" width="54" height="54" style="border-radius:4px;" loading="lazy" decoding="async">
            <div>
              <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#0E1721;">get.more.sales</div>
              <div style="font-size:0.78rem;color:#003E7E;font-weight:700;">Carmen Caselli · Verkaufsberatung &amp; Training</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#243447;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Entfesseln Sie Ihr Verkaufspotenzial: Massgeschneiderte B2B-Verkaufsstrategie, Marktforschung, praxisnahes Vertriebstraining und 1:1 Sales-Sparring auf Augenhöhe.
          </p>
          <div style="font-size:0.84rem;color:#0E1721;font-weight:600;">
            Carmen Caselli get.more.sales · Zofingen · UID: CHE-471.125.841
          </div>
        </div>

        <div>
          <div class="footer-title">Leistungen &amp; Fokus</div>
          <ul class="footer-list">
            <li><a href="leistungen.html#strategie">Verkaufsstrategie &amp; Beratung</a></li>
            <li><a href="leistungen.html#marktforschung">Marktforschung &amp; Potenzialanalyse</a></li>
            <li><a href="leistungen.html#vertriebstraining">Vertriebstraining &amp; Entwicklung</a></li>
            <li><a href="leistungen.html#sparring">1:1 Executive Sales-Sparring</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Einblicke &amp; Profil</div>
          <ul class="footer-list">
            <li><a href="index.html#projektberater">Interaktiver B2B-Potenzial-Rechner</a></li>
            <li><a href="referenzen.html">Kundenstimmen &amp; Praxis-Resultate</a></li>
            <li><a href="ueber-uns.html">Über Carmen Caselli &amp; Werdegang</a></li>
            <li><a href="https://www.linkedin.com/in/carmen-caselli/" target="_blank" rel="noopener noreferrer">LinkedIn-Profil Carmen Caselli</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; Rechtliches</div>
          <ul class="footer-list">
            <li><a href="https://www.linkedin.com/in/carmen-caselli/" target="_blank" rel="noopener noreferrer">LinkedIn: Carmen Caselli</a></li>
            <li><a href="mailto:beratungs-termin@get-more-sales.org">beratungs-termin@get-more-sales.org</a></li>
            <li><a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">Kostenloser Beratungstermin &amp; Smart-Anfrage</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Carmen Caselli get.more.sales (Zofingen · CHE-471.125.841). Alle Rechte vorbehalten.</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
          <a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">Beratungstermin buchen</a>
          <a href="https://www.linkedin.com/in/carmen-caselli/" target="_blank" rel="noopener noreferrer" style="color:#243447;">LinkedIn</a>
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
  <meta name="description" content="get.more.sales · Carmen Caselli (Zeigeversion): B2B-Verkaufsberatung, Marktforschung, praxisnahes Vertriebstraining und 1:1 Sales-Sparring in Zofingen und im DACH-Raum.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "get.more.sales · Carmen Caselli",
    "legalName": "Carmen Caselli get.more.sales",
    "taxID": "CHE-471.125.841",
    "url": "https://get-more-sales.org",
    "email": "beratungs-termin@get-more-sales.org",
    "founder": "Carmen Caselli",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Zofingen",
      "postalCode": "4800",
      "addressLocality": "Zofingen",
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

  <!-- STICKY HEADER (ZEIGEVERSION OHNE OBEREN TOP-BALKEN GEMÄSS PROTOKOLL #031) -->
  <header class="site-header" data-section="header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="get.more.sales Carmen Caselli Startseite">
        <img src="images/logo-get-more-sales.png" alt="get.more.sales Logo" class="brand-logo" width="50" height="50" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">get.more.sales</span>
          <span class="brand-sub" data-slot="brand_sub">Carmen Caselli · Verkaufsberatung</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}" data-nav-href="index.html">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#15803D"/></svg>
          <span>Startseite</span>
        </a>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="leistungen.html" onclick="wpOpenBlueprintModal('Alle 6 Leistungs-Module, Trainings &amp; Beratungsformate im Detail', 'Verkaufsstrategie &amp; Beratung, Marktforschung &amp; Analyse, Vertriebstraining, Telefon- &amp; LinkedIn-Akquise sowie 1:1 Executive Sales-Sparring', 'Carmen Caselli')">
          <span>Leistungen</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="referenzen.html" onclick="wpOpenBlueprintModal('Kundenstimmen, B2B-Praxis-Cases &amp; Resultate', 'Kundenstimme von Matthias sowie 6 Vorher/Nachher-Fallbeispiele aus Strategie, Akquise, Preisverhandlung und 1:1 Sparring', 'Carmen Caselli')">
          <span>Referenzen</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="ueber-uns.html" onclick="wpOpenBlueprintModal('Über Carmen Caselli, Haltung &amp; Werdegang', '18 Jahre Finanz- &amp; Kapitalmarktpraxis (CHF Bonds), Vollzeit-Tauchlehrerin in Thailand &amp; seit 2019 Geschäftsführerin get.more.sales', 'Carmen Caselli')">
          <span>Über Carmen</span>
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
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu();wpOpenBlueprintModal('Alle 6 Leistungs-Module, Trainings &amp; Beratungsformate im Detail', 'Verkaufsstrategie, Marktforschung, Vertriebstraining &amp; 1:1 Sales-Sparring', 'Carmen Caselli')">
      <span>Leistungen</span>
      <span class="preview-status-badge">Folgt beim Ausbau</span>
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu();wpOpenBlueprintModal('Kundenstimmen, B2B-Praxis-Cases &amp; Resultate', 'Echte Rückmeldungen &amp; B2B-Erfolgsbeispiele von get.more.sales', 'Carmen Caselli')">
      <span>Referenzen</span>
      <span class="preview-status-badge">Folgt beim Ausbau</span>
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu();wpOpenBlueprintModal('Über Carmen Caselli, Haltung &amp; Werdegang', '18 Jahre Finanzwelt, Tauchlehrerin &amp; Geschäftsführerin get.more.sales', 'Carmen Caselli')">
      <span>Über Carmen</span>
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
            <img src="images/logo-get-more-sales.png" alt="get.more.sales Carmen Caselli" width="54" height="54" style="border-radius:4px;" loading="lazy" decoding="async">
            <div>
              <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#0E1721;">get.more.sales</div>
              <div style="font-size:0.78rem;color:#003E7E;font-weight:700;">Carmen Caselli · Verkaufsberatung</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#243447;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Entfesseln Sie Ihr Verkaufspotenzial: Massgeschneiderte B2B-Verkaufsstrategie, Marktforschung, praxisnahes Vertriebstraining und 1:1 Sales-Sparring mit Carmen Caselli.
          </p>
          <div style="font-size:0.84rem;color:#0E1721;font-weight:600;">
            Zofingen (Kanton Aargau) · UID: CHE-471.125.841
          </div>
        </div>

        <div>
          <div class="footer-title">Bereits in dieser Vorschau live</div>
          <ul class="footer-list">
            <li><a href="index.html">Startseite mit allen 6 Leistungs-Modulen</a></li>
            <li><a href="index.html#projektberater">Interaktiver B2B-Potenzial-Rechner</a></li>
            <li><a href="index.html#referenzen">Kundenstimme Matthias &amp; Praxis-Einblicke</a></li>
            <li><a href="kontakt.html">3-Schritte Smart-Anfrage (Live-Test)</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Geplante Detail-Unterseiten</div>
          <ul class="footer-list">
            <li><button type="button" onclick="wpOpenBlueprintModal('Leistungen, Trainings &amp; Beratungs-Module', 'Verkaufsstrategie, Marktforschung, Vertriebstraining &amp; 1:1 Sparring', 'Carmen Caselli')">Leistungen &amp; Trainings (Vorschau)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Kundenstimmen &amp; B2B-Praxis-Cases', 'Vorher/Nachher-Resultate aus Strategie, Akquise &amp; Abschluss', 'Carmen Caselli')">Referenzen &amp; Erfolge (Vorschau)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Über Carmen Caselli &amp; Philosophie', '18 Jahre Finanzwelt, Tauchlehrerin &amp; B2B-Mentorin', 'Carmen Caselli')">Über Carmen Caselli (Vorschau)</button></li>
            <li><a href="https://www.linkedin.com/in/carmen-caselli/" target="_blank" rel="noopener noreferrer">LinkedIn-Profil Carmen Caselli</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; Rechtliches</div>
          <ul class="footer-list">
            <li><a href="https://www.linkedin.com/in/carmen-caselli/" target="_blank" rel="noopener noreferrer">LinkedIn: Carmen Caselli</a></li>
            <li><a href="mailto:beratungs-termin@get-more-sales.org">beratungs-termin@get-more-sales.org</a></li>
            <li><a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">Smart-Anfrage &amp; Beratungstermin</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Carmen Caselli get.more.sales (Zofingen · CHE-471.125.841). Alle Rechte vorbehalten.</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
          <a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">Beratungstermin buchen</a>
          <a href="https://www.linkedin.com/in/carmen-caselli/" target="_blank" rel="noopener noreferrer" style="color:#243447;">LinkedIn</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- BLUEPRINT PREVIEW MODAL (ZEIGEVERSION V2) -->
  <div class="wp-modal-backdrop" id="wpBlueprintModal" role="dialog" aria-modal="true" aria-labelledby="wpBpTitle" data-allow-scroll="true">
    <div class="wp-modal-dialog" data-allow-scroll="true">
      <button type="button" class="wp-modal-close" aria-label="Dialog schliessen" onclick="wpCloseBlueprintModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="section-kicker">AUSBAUSTUFEN-VORSCHAU · GET.MORE.SALES</div>
      <h3 id="wpBpTitle" style="font-size:1.34rem;font-weight:700;margin-bottom:8px;">Detailseite im Komplett-Ausbau enthalten</h3>
      <p id="wpBpCategory" style="font-size:0.86rem;font-weight:700;color:var(--gold-dark);margin-bottom:6px;">Leistungs- &amp; Themenbereich: Verkaufsberatung, Training &amp; Sparring</p>
      <p id="wpBpContact" style="font-size:0.84rem;color:var(--text-muted);margin-bottom:14px;">Verantwortliche Expertin: Carmen Caselli</p>
      <div style="background-color:var(--bg-page);border:1px solid var(--border-light);border-left:4px solid var(--gold);padding:14px 16px;border-radius:var(--radius-sm);font-size:0.88rem;color:var(--text-body);line-height:1.6;margin-bottom:18px;">
        In dieser <strong>Zeigeversion (2 Seiten)</strong> sind die komplette Startseite mit dem interaktiven B2B-Potenzial-Rechner sowie die 3-Schritte Smart-Anfrage bereits voll funktionsfähig ausgearbeitet. Die zusätzlichen Detail-Unterseiten (Leistungen, Referenzen, Über Carmen) sind in der 5-seitigen Vollversion bereits komplett umgesetzt.
      </div>
      <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:flex-end;">
        <button type="button" class="btn-cta btn-cta-outline btn-sm" onclick="wpCloseBlueprintModal()">
          <span>Weiter auf der Startseite umsehen</span>
        </button>
        <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm">
          <span>Direkt zur 3-Schritte Smart-Anfrage</span>
          {SVG_ARROW}
        </a>
      </div>
    </div>
  </div>

{render_impressum_modal()}
{COMMON_UI_JS}
</body>
</html>"""

# ==============================================================================
# SEITEN-INHALTE: V1 VOLLVERSION STARTSEITE (preview-get-more-sales/index.html)
# ==============================================================================
V1_INDEX_BODY = f"""
  <!-- HERO SECTION -->
  <section class="hero-section" data-section="hero">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light" data-slot="hero_kicker">B2B VERKAUFSBERATUNG, VERTRIEBSTRAINING &amp; SPARRING · ZOFINGEN / AARGAU &amp; DACH</div>
        <h1 class="hero-title" data-slot="hero_title">
          Entfesseln Sie Ihr Verkaufspotenzial. <span>Strukturiert, menschlich, messbar.</span>
        </h1>
        <p class="hero-lead" data-slot="hero_lead">
          Bei get.more.sales begleitet Carmen Caselli Geschäftsführer, Verkaufsleiter und B2B-Vertriebsteams dabei, ihre Verkaufsprozesse glasklar zu strukturieren, Abschlussquoten nachhaltig zu steigern und Neukunden auf Augenhöhe zu gewinnen: ohne künstlichen Kaufdruck, sondern mit analytischer Klarheit und echter Begeisterung.
        </p>

        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
            <span>Kostenlosen Beratungstermin anfragen</span>
            {SVG_ARROW}
          </a>
          <a href="#projektberater" class="btn-cta btn-cta-outline-light" data-slot="hero_cta_secondary">
            <span>B2B-Potenzial-Rechner starten</span>
          </a>
        </div>

        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">18+ Jahre Finanzpraxis</span>
            <span class="hero-badge-lbl">Treasury &amp; Portfolio Management (CHF Bonds) kombiniert mit 7+ Jahren B2B-Vertriebsberatung</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Verkaufsstrategie &amp; Prozesse</span>
            <span class="hero-badge-lbl">Massgeschneiderte Vertriebsarchitektur, Pipeline-Struktur und klare Kundenreisen</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Praxisnahes Vertriebstraining</span>
            <span class="hero-badge-lbl">Bedarfsanalyse, souveräne Einwandbehandlung und Abschlussstärke ohne Rabattschlacht</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Antwort in 5–12 Arbeitsstunden</span>
            <span class="hero-badge-lbl">Direkter Draht zu Carmen Caselli in Zofingen · CHE-471.125.841</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/carmen-caselli-portrait-color.jpg" alt="Carmen Caselli, Geschäftsführerin get.more.sales Verkaufsberatung und Vertriebstraining" width="600" height="390" data-slot="hero_image">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#0E1721;">Carmen Caselli · get.more.sales</div>
            <div style="font-size:0.8rem;color:#243447;">Verkaufsberatung, Marktforschung &amp; B2B-Vertriebstraining · Zofingen / AG</div>
          </div>
          <span class="top-bar-badge">BOOST YOUR SALES</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 3 KERNHEBEL (STRATEGIE, MARKTFORSCHUNG, TRAINING) -->
  <section data-section="zielgruppen" id="zielgruppen" style="background-color:var(--bg-Warm);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="audiences_kicker">STRATEGIE · MARKTFORSCHUNG · VERTRIEBSTRAINING</div>
        <h2 class="section-title" data-slot="audiences_title">Drei ineinandergreifende Hebel für nachhaltiges Umsatzwachstum</h2>
        <p class="section-desc" data-slot="audiences_desc">
          Als führende Verkaufsberatungs-Agentur kombinieren wir strategische Prozessklarheit mit fundierter Marktanalyse und praxisnaher Umsetzung direkt in Ihrem Verkaufsteam:
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">1. Strategie &amp; Prozesse</span>
              <span class="icon-box">{SVG_COMPASS}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Verkaufsstrategie &amp; Beratung</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Unsere massgeschneiderten Verkaufsstrategien helfen Ihrem Unternehmen, Verkaufsprozesse zu optimieren, Reibungsverluste in der Pipeline zu beseitigen und Umsätze planbar zu steigern.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Individuelle Ist-Analyse Ihrer bestehenden Verkaufsprozesse</span></div>
              <div class="check-item">{SVG_CHECK} <span>Klare Kontakt-, Angebots- und Nachfass-Standards für Ihr Team</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=strategie" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Verkaufsstrategie besprechen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">2. Markt &amp; Positionierung</span>
              <span class="icon-box">{SVG_LAYERS}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Marktforschung &amp; Analyse</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Unsere Marktforschungs- und Analysedienste liefern Ihnen wertvolle Einblicke in Ihren Markt und Ihre Zielgruppe, damit Sie fundierte Entscheidungen treffen und zukünftige Chancen frühzeitig nutzen.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Identifikation der profitabelsten B2B-Kundensegmente und Entscheider</span></div>
              <div class="check-item">{SVG_CHECK} <span>Schärfung Ihrer Nutzenargumentation gegenüber Mitbewerbern</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=analyse" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Potenzialanalyse anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">3. Team &amp; Umsetzung</span>
              <span class="icon-box">{SVG_USERS}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Vertriebstraining &amp; Entwicklung</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Unsere massgeschneiderten Vertriebstrainings unterstützen Ihr Verkaufsteam dabei, seine Fähigkeiten auszubauen, Einwände souverän zu wandeln und die Abschlussleistung im Alltag spürbar zu erhöhen.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Praxisnahes Training an Ihren echten Kundenfällen und Offerten</span></div>
              <div class="check-item">{SVG_CHECK} <span>Persönliches 1:1 Sales-Sparring für Verkaufsleiter und Inhaber</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=training" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Vertriebstraining klären</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 6 LEISTUNGS-MODULE (3x2 SYMMETRISCHES RASTER) -->
  <section data-section="kernangebote" id="kernangebote">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="pillars_kicker">LEISTUNGSÜBERSICHT · GET.MORE.SALES CARMEN CASELLI</div>
        <h2 class="section-title" data-slot="pillars_title">Sechs Leistungs-Module für messbare Verkaufserfolge</h2>
        <p class="section-desc" data-slot="pillars_desc">
          Vom strategischen Prozess-Audit über die Marktanalyse bis zum praxisnahen Team-Training und persönlichen 1:1 Sparring vor entscheidenden Schlüsselkunden-Gesprächen:
        </p>
      </div>

      <div class="grid-3">
        <!-- 1. Verkaufsstrategie -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/leistung-verkaufsstrategie-beratung.png" alt="Verkaufsstrategie und Beratung bei get.more.sales Carmen Caselli" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Modul 01 · Strategie</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Pipeline &amp; Prozesse</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Verkaufsstrategie &amp; Beratung</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Wir strukturieren Ihre gesamte B2B-Kundenreise vom Erstkontakt über die Bedarfsanalyse bis zum verbindlichen Abschluss.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Klare Vertriebsziele, Kennzahlen und Prozess-Standards</span></div>
                <div class="check-item">{SVG_CHECK} <span>Individuelle Verkaufs-Playbooks für Innen- und Aussendienst</span></div>
              </div>
            </div>
            <a href="leistungen.html#strategie" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zur Strategieberatung</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 2. Marktforschung -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/leistung-marktforschung-analyse.png" alt="Marktforschung und Potenzialanalyse bei get.more.sales" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Modul 02 · Analyse</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Markt &amp; Zielgruppe</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Marktforschung &amp; Analyse</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Datenbasierte Einblicke in Ihre Zielmärkte, Kaufmotive von Entscheidern und ungenutzte Umsatzpotenziale im Bestandskunden- und Neukundenmarkt.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Idealkunden-Profile (ICP) und Entscheider-Landkarten</span></div>
                <div class="check-item">{SVG_CHECK} <span>Wettbewerbs- und Angebots-Positionierung mit klarem Mehrwert</span></div>
              </div>
            </div>
            <a href="leistungen.html#marktforschung" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zur Marktanalyse</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 3. Vertriebstraining -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/leistung-vertriebstraining-entwicklung.png" alt="B2B Vertriebstraining und Entwicklung mit Carmen Caselli" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Modul 03 · Training</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Team &amp; Abschluss</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">B2B-Vertriebstraining</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Massgeschneiderte Trainings für Verkaufsteams: Gesprächsführung, Fragetechnik, Einwandbehandlung und souveräne Preisverhandlung.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Hohe Abschlussquote ohne künstlichen Druck oder Rabatte</span></div>
                <div class="check-item">{SVG_CHECK} <span>Direkter Transfer an Ihren realen Kunden- und Offertfällen</span></div>
              </div>
            </div>
            <a href="leistungen.html#vertriebstraining" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zum Vertriebstraining</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 4. Telefon- & LinkedIn-Akquise -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/sales-gallery-meeting-sparring.png" alt="Moderne B2B Akquise über Telefon und LinkedIn" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Modul 04 · Akquise</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Telefon &amp; LinkedIn</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">B2B-Neukunden-Akquise</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Verbindliche Kontaktaufnahme über Telefon, Empfehlungsmanagement und LinkedIn, die bei Entscheidern Vertrauen schafft und Termine sichert.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Natürliche Gesprächseinstiege statt starrer Callcenter-Skripte</span></div>
                <div class="check-item">{SVG_CHECK} <span>Kombination aus LinkedIn-Sichtbarkeit und direktem Dialog</span></div>
              </div>
            </div>
            <a href="leistungen.html#akquise" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zur Akquise-Begleitung</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 5. 1:1 Executive Sales-Sparring -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/carmen-caselli-portrait-duplex-card.jpg" alt="1:1 Executive Sales-Sparring mit Carmen Caselli" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Modul 05 · Mentoring</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">1:1 auf Augenhöhe</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">1:1 Executive Sales-Sparring</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Persönliche Begleitung für Geschäftsführer, Verkaufsleiter und Berater vor wichtigen Pitches, Grosskunden-Verhandlungen und Jahresgesprächen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Ehrliches Sparring mit 18 Jahren Finanz- und Verhandlungserfahrung</span></div>
                <div class="check-item">{SVG_CHECK} <span>Klare Vorbereitung von Strategie, Zahlenrahmen und Einwänden</span></div>
              </div>
            </div>
            <a href="leistungen.html#sparring" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zum 1:1 Sales-Sparring</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 6. Verkaufsprozess-Audit -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/hero-sales-dashboard-analytics.png" alt="Verkaufsprozess-Audit und Standortbestimmung" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Modul 06 · Einstieg</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Schneller Überblick</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Prozess-Audit &amp; Erstgespräch</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Kompakte Standortbestimmung Ihrer aktuellen Vertriebspipeline: Wo gehen aktuell Anfragen, Offerten oder Margen verloren, und welche Massnahme wirkt sofort?
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Unverbindliches Erstgespräch per Telefon oder Video-Call</span></div>
                <div class="check-item">{SVG_CHECK} <span>Persönliche Rückmeldung innerhalb von 5 bis 12 Arbeitsstunden</span></div>
              </div>
            </div>
            <a href="kontakt.html?thema=kennenlernen" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Kostenlosen Termin buchen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

{render_sales_advisor()}

  <!-- ÜBER CARMEN CASELLI (KOMPAKT-SEKTION STARTSEITE) -->
  <section data-section="inhaberin" id="inhaberin">
    <div class="container">
      <div class="grid-2">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Geschäftsführerin · get.more.sales</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h2 style="font-size:1.65rem;font-weight:700;margin-bottom:10px;">Carmen Caselli: Analytische Schärfe trifft menschliche Klarheit</h2>
            <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:12px;">
              Achtzehn Jahre lang verantwortete Carmen Caselli in der Schweizer Bank- und Finanzwelt anspruchsvolle Treasury- und Portfolio-Mandate (CHF Bonds bei Staatskasse und Pensionskasse). Danach lebte sie ihren Traum als Vollzeit-Tauchlehrerin in Thailand, bevor sie 2019 <strong>get.more.sales</strong> gründete.
            </p>
            <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:14px;">
              Ihre Überzeugung aus dem Tauchsport und der Finanzwelt prägt jedes Training: <em>«Auf 40 Metern Tiefe unter Wasser gibt es kein Schummeln. Dort zählen nur hundertprozentige Vorbereitung, ruhige Führung und echtes Vertrauen.»</em> Genau diese Klarheit bringt sie in Ihre Verkaufsstrategie.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>18 Jahre Finanz- &amp; Kapitalmarktpraxis:</strong> Zahlenfokus, Renditedenken und Verhandlungsstärke auf C-Level</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Seit 2019 Geschäftsführerin get.more.sales:</strong> B2B-Verkaufsberatung &amp; Business Mentoring (CHE-471.125.841)</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Direkt vernetzen:</strong> Austausch auf Augenhöhe via LinkedIn, E-Mail oder direkt vor Ort</span></div>
            </div>
          </div>
          <div style="display:flex;gap:12px;flex-wrap:wrap;">
            <a href="ueber-uns.html" class="btn-cta btn-cta-primary btn-sm">
              <span>Mehr über Carmen Caselli erfahren</span>
              {SVG_ARROW}
            </a>
            <a href="https://www.linkedin.com/in/carmen-caselli/" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-outline btn-sm">
              <span>Auf LinkedIn vernetzen</span>
            </a>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap" style="height:290px;">
            <img src="images/carmen-caselli-portrait-full-card.jpg" alt="Carmen Caselli, Inhaberin get.more.sales in Zofingen" style="object-position:center top;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Standort Zofingen</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">CHE-471.125.841</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Persönliche Begleitung statt anonymer Berater-Folien</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:10px;">
                Bei get.more.sales arbeiten Sie direkt mit Carmen Caselli zusammen. Jede Strategie, jede Marktanalyse und jedes Training wird exakt auf Ihr Geschäftsmodell, Ihre Branche und Ihr Team zugeschnitten.
              </p>
            </div>
            <a href="kontakt.html" class="btn-cta btn-cta-gold btn-sm" style="width:100%;">
              <span>Jetzt unverbindliches Erstgespräch vereinbaren</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- KUNDENSTIMMEN & PRAXIS-EINBLICKE -->
  <section data-section="referenzen" id="referenzen" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="refs_kicker">KUNDENSTIMMEN &amp; PRAXIS-RESULTATE · GET.MORE.SALES</div>
        <h2 class="section-title" data-slot="refs_title">Was unsere Kunden über die Zusammenarbeit sagen</h2>
        <p class="section-desc" data-slot="refs_desc">
          Echte Rückmeldungen und typische B2B-Praxisbeispiele aus Verkaufsstrategie, Marktforschung, Vertriebstraining und persönlichem 1:1 Sales-Sparring:
        </p>
      </div>

      {render_references_grid(limit=6, is_v2=False)}
    </div>
  </section>

  <!-- FAQ SEKTION -->
  <section data-section="faq" id="faq">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="faq_kicker">HÄUFIGE FRAGEN · VERKAUFSBERATUNG &amp; TRAINING</div>
        <h2 class="section-title" data-slot="faq_title">Antworten rund um Ablauf, Strategie und Erstgespräch</h2>
        <p class="section-desc" data-slot="faq_desc">
          Die wichtigsten Fragen von Geschäftsführern und Verkaufsleitern vor dem ersten Beratungstermin mit Carmen Caselli:
        </p>
      </div>

      {render_faqs_grid()}
    </div>
  </section>
"""


# ==============================================================================
# SEITEN-INHALTE: V1 LEISTUNGEN & TRAININGS (leistungen.html)
# ==============================================================================
V1_LEISTUNGEN_BODY = f"""
  <section class="hero-section" data-section="hero">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">LEISTUNGEN &amp; TRAININGS · GET.MORE.SALES CARMEN CASELLI</div>
        <h1 class="hero-title">
          Massgeschneiderte Verkaufsberatung, <span>die im Alltag wirkt.</span>
        </h1>
        <p class="hero-lead">
          Ob Sie Ihre Verkaufsstrategie von Grund auf strukturieren, neue Zielmärkte erschliessen oder Ihr Vertriebsteam in Akquise, Einwandbehandlung und Abschlussstärke trainieren möchten: Unsere sechs Leistungs-Module greifen nahtlos ineinander.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>Beratungstermin zu Ihrem Anliegen buchen</span>
            {SVG_ARROW}
          </a>
          <a href="#projektberater" class="btn-cta btn-cta-outline-light">
            <span>Potenzial-Rechner nutzen</span>
          </a>
        </div>
        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">01 · Verkaufsstrategie</span>
            <span class="hero-badge-lbl">Prozess-Optimierung, Pipeline-Design und massgeschneiderte B2B-Playbooks</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">02 · Marktforschung</span>
            <span class="hero-badge-lbl">Zielgruppen-Schärfung, Kaufmotive und datenbasierte Marktchancen</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">03 · Vertriebstraining</span>
            <span class="hero-badge-lbl">Gesprächsführung, Preisverhandlung und Abschlussstärke für Ihr Team</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">04 · 1:1 Sales-Sparring</span>
            <span class="hero-badge-lbl">Executive Mentoring für Geschäftsführer, Verkaufsleiter und Berater</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/sales-gallery-meeting-sparring.png" alt="B2B Verkaufsstrategie und Vertriebstraining bei get.more.sales" width="600" height="390">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#0E1721;">Praxisnahe B2B-Begleitung</div>
            <div style="font-size:0.8rem;color:#243447;">Inhouse bei Ihnen vor Ort, in Zofingen / AG oder flexibel via Video-Call</div>
          </div>
          <span class="top-bar-badge">6 KERNMODULE</span>
        </div>
      </div>
    </div>
  </section>

  <section data-section="leistungen-detail" id="leistungen-detail">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">ALLE 6 LEISTUNGSBEREICHE IM DETAIL</div>
        <h2 class="section-title">Von der strategischen Analyse bis zum sicheren Abschluss</h2>
        <p class="section-desc">
          Jedes Modul wird individuell auf Ihre Branche, Ihre Angebotsstruktur und den Erfahrungsstand Ihres Teams abgestimmt:
        </p>
      </div>

      <div class="grid-2">
        <!-- 1. Verkaufsstrategie -->
        <div class="content-card card-accent-top" id="strategie">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">01 · Strategie &amp; Prozess-Architektur</span>
              <span class="icon-box">{SVG_COMPASS}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Verkaufsstrategie &amp; Beratung</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Unsere massgeschneiderten Verkaufsstrategien helfen Ihrem Unternehmen, Verkaufsprozesse zu optimieren und Umsätze nachhaltig zu steigern. Wir ersetzen den Zufallsverkauf durch eine glasklare, wiederholbare Struktur.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Vollständige Durchleuchtung Ihrer aktuellen Kundenreise und Verkaufsstufen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Klare Kriterien für Lead-Qualifizierung, Offert-Nachfassung und Abschluss</span></div>
              <div class="check-item">{SVG_CHECK} <span>Massgeschneidertes Vertriebs-Playbook für neue und erfahrene Mitarbeitende</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=strategie" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Verkaufsstrategie &amp; Beratung anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- 2. Marktforschung -->
        <div class="content-card card-accent-top" id="marktforschung">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">02 · Markt-, Kunden- &amp; Potenzialanalyse</span>
              <span class="icon-box">{SVG_LAYERS}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Marktforschung &amp; Analyse</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Unsere Marktforschungs- und Analysedienste liefern Ihnen wertvolle Einblicke in Ihren Markt und Ihre Zielgruppe. Sie treffen fundierte Entscheidungen und erkennen zukünftige Marktchancen vor Ihren Mitbewerbern.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Schärfung Ihres Idealkunden-Profils (ICP) und der wichtigsten Entscheider-Rollen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Analyse von Kundenbedürfnissen, Kaufmotiven und Wechselbarrieren</span></div>
              <div class="check-item">{SVG_CHECK} <span>Klare Wert- und Nutzenpositionierung für margenstarke Angebote</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=analyse" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Marktforschung &amp; Potenzialanalyse anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- 3. Vertriebstraining -->
        <div class="content-card card-accent-top" id="vertriebstraining">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">03 · Team-Entwicklung &amp; Abschlussstärke</span>
              <span class="icon-box">{SVG_USERS}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Vertriebstraining &amp; Entwicklung</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Unsere massgeschneiderten Vertriebstrainings unterstützen Ihr Verkaufsteam dabei, seine Fähigkeiten zu verbessern und die Verkaufsleistung direkt im Kundenkontakt zu steigern.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Präzise Bedarfs- und Nutzen-Frageführung im Erst- und Zweitgespräch</span></div>
              <div class="check-item">{SVG_CHECK} <span>Souveräne Einwandbehandlung und Preisgespräche ohne vorschnelle Rabatte</span></div>
              <div class="check-item">{SVG_CHECK} <span>Verbindliche Abschluss- und Nachfass-Routine bei offenen Offerten</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=training" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Vertriebstraining für Ihr Team anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- 4. Moderne B2B-Akquise -->
        <div class="content-card card-accent-top" id="akquise">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">04 · Telefon, Empfehlungen &amp; Social Selling</span>
              <span class="icon-box">{SVG_HOME}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Moderne B2B-Akquise auf Augenhöhe</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Wie gewinnen Sie heute die Aufmerksamkeit von stark beschäftigten Geschäftsführern und Einkäufern? Durch eine kluge Kombination aus persönlicher Ansprache, Telefon-Exzellenz und sichtbarer LinkedIn-Präsenz.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Sympathische, wirksame Telefon-Leitfäden, die zu Ihrem Team passen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Systematischer Aufbau von Kundenempfehlungen und strategischen Netzwerken</span></div>
              <div class="check-item">{SVG_CHECK} <span>Social Selling auf LinkedIn: Vom sichtbaren Expertenbeitrag zum Ersttermin</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=analyse" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Akquise-Training &amp; Begleitung anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- 5. 1:1 Executive Sales-Sparring -->
        <div class="content-card card-accent-top" id="sparring">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">05 · Persönliches Mentoring für Entscheider</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">1:1 Executive Sales-Sparring mit Carmen Caselli</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Als Geschäftsführer, Verkaufsleiter oder spezialisierter Berater haben Sie oft niemanden im eigenen Haus, der Ihre Verkaufs- und Verhandlungsstrategie ungeschminkt und auf Augenhöhe spiegelt.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Gezielte Vorbereitung auf Schlüsselkunden-Termine, Pitches und Vergaben</span></div>
              <div class="check-item">{SVG_CHECK} <span>Kombination aus 18 Jahren Finanz-Know-how und praxiserprobter Verhandlungspsychologie</span></div>
              <div class="check-item">{SVG_CHECK} <span>Flexible Sparring-Sessions per Video-Call, Telefon oder persönlich vor Ort</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=sparring" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>1:1 Sales-Sparring anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- 6. Kostenloser Beratungstermin -->
        <div class="content-card card-accent-top" id="erstgespraech">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">06 · Unverbindliche Standortbestimmung</span>
              <span class="icon-box">{SVG_SHIELD}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Kostenloser Beratungstermin (5–12 Std. Antwortzeit)</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Lernen Sie Carmen Caselli und die Arbeitsweise von get.more.sales unverbindlich kennen. Im ersten Gespräch prüfen wir gemeinsam, wo in Ihrem Vertrieb aktuell das grösste ungenutzte Umsatzpotenzial liegt.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Persönliche Rückmeldung in der Regel innerhalb von 5 bis 12 Arbeitsstunden</span></div>
              <div class="check-item">{SVG_CHECK} <span>Konkrete Ersteinschätzung Ihrer dringendsten Vertriebs- und Akquise-Fragen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Direkt buchbar über unsere 3-Schritte Smart-Anfrage oder per E-Mail an beratungs-termin@get-more-sales.org</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=kennenlernen" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Kostenlosen Beratungstermin vereinbaren</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

{render_sales_advisor()}
"""


# ==============================================================================
# SEITEN-INHALTE: V1 REFERENZEN & PRAXIS-CASES (referenzen.html)
# ==============================================================================
def render_full_before_after_cards() -> str:
    cards = []
    for ref in BEFORE_INVENTORY["references"]:
        cards.append(f"""
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">{ref['category']}</span>
              <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">{ref.get('highlight', 'Praxis-Resultat')}</span>
            </div>
            <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:6px;">{ref['title']}</h3>
            <p style="font-size:0.84rem;font-weight:700;color:var(--gold-dark);margin-bottom:12px;">{ref['scope']}</p>
            <div class="form-grid-2" style="margin-bottom:14px;">
              <div style="border:1px solid var(--border-light);border-radius:var(--radius-sm);overflow:hidden;background-color:var(--bg-page);">
                <img src="{ref['before_img']}" alt="Analyse & Ausgangslage: {ref['title']}" style="width:100%;height:175px;object-fit:cover;" loading="lazy" decoding="async">
                <div style="padding:6px 10px;font-size:0.75rem;font-weight:700;color:var(--text-muted);background-color:#EBF3FC;">Fokus &amp; Analyse</div>
              </div>
              <div style="border:1px solid var(--gold-border);border-radius:var(--radius-sm);overflow:hidden;background-color:var(--bg-page);">
                <img src="{ref['after_img']}" alt="Ergebnis & Wirkung: {ref['title']}" style="width:100%;height:175px;object-fit:cover;" loading="lazy" decoding="async">
                <div style="padding:6px 10px;font-size:0.75rem;font-weight:700;color:var(--gold-dark);background-color:var(--gold-soft);">Umsetzung &amp; Resultat</div>
              </div>
            </div>
            <p style="font-size:0.9rem;color:var(--text-body);line-height:1.6;margin-bottom:12px;">{ref['desc']}</p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Schwerpunkt:</strong> {ref['scope']}</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Mehrwert:</strong> {ref.get('highlight', 'Nachhaltiges Wachstum')}</span></div>
            </div>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Ähnliches Vorhaben mit Carmen Caselli besprechen</span>
            {SVG_ARROW}
          </a>
        </div>""")
    return '<div class="grid-2">\n' + "\n".join(cards) + "\n      </div>"


V1_REFERENZEN_BODY = f"""
  <section class="hero-section" data-section="hero">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">KUNDENSTIMMEN &amp; PRAXIS-RESULTATE · GET.MORE.SALES</div>
        <h1 class="hero-title">
          Messbare Ergebnisse. <span>Vertrauen auf Augenhöhe.</span>
        </h1>
        <p class="hero-lead">
          Erfahren Sie, wie Unternehmen durch die Zusammenarbeit mit Carmen Caselli und get.more.sales ihre Verkaufsstrategie geschärft, neue Kunden gewonnen und ihre Umsätze nachhaltig gesteigert haben.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>Eigenes Verkaufspotenzial besprechen</span>
            {SVG_ARROW}
          </a>
          <a href="leistungen.html" class="btn-cta btn-cta-outline-light">
            <span>Alle 6 Leistungs-Module ansehen</span>
          </a>
        </div>
        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Kundenstimme Matthias</span>
            <span class="hero-badge-lbl">«Verkaufsstrategie erheblich verbessert, mehr Kunden angezogen und Umsatz gesteigert»</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Struktur statt Zufall</span>
            <span class="hero-badge-lbl">Verlässliche Pipeline-Führung vom ersten Kontakt bis zum unterschriebenen Auftrag</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Marge &amp; Preisstärke</span>
            <span class="hero-badge-lbl">Wertorientierte Argumentation in B2B-Verhandlungen statt vorschneller Preisnachlässe</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Praxisnaher Transfer</span>
            <span class="hero-badge-lbl">Keine trockene Theorie: Jedes Training arbeitet an Ihren realen Kundenfällen</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/boost-your-sales-stage.png" alt="Boost Your Sales - get.more.sales Carmen Caselli Referenzen und Kundenstimmen" width="600" height="390">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#0E1721;">get.more.sales · Praxis-Wirkung</div>
            <div style="font-size:0.8rem;color:#243447;">Strategie, Marktforschung &amp; B2B-Vertriebstraining in der Schweiz &amp; DACH</div>
          </div>
          <span class="top-bar-badge">KUNDENRESULTATE</span>
        </div>
      </div>
    </div>
  </section>

  <section data-section="referenzen-liste" id="referenzen-liste">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">KUNDENSTIMMEN &amp; B2B-FALLBEISPIELE</div>
        <h2 class="section-title">Sechs Einblicke in unsere Beratungs- und Trainingspraxis</h2>
        <p class="section-desc">
          Von der originalen Kundenrückmeldung bis zu den typischen Hebeln in Strategie, Marktanalyse, Akquise und Executive Sparring:
        </p>
      </div>

      {render_full_before_after_cards()}
    </div>
  </section>
"""


# ==============================================================================
# SEITEN-INHALTE: V1 ÜBER CARMEN CASELLI (ueber-uns.html)
# ==============================================================================
V1_UEBER_UNS_BODY = f"""
  <section class="hero-section" data-section="hero">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">ÜBER CARMEN CASELLI · GESCHÄFTSFÜHRERIN GET.MORE.SALES</div>
        <h1 class="hero-title">
          18 Jahre Finanzwelt. Vollzeit-Tauchlehrerin. <span>Verkauf mit Haltung.</span>
        </h1>
        <p class="hero-lead">
          Hinter get.more.sales steht Carmen Caselli: Eine Beraterin und Trainerin, die Zahlenverständnis aus dem Schweizer Kapitalmarkt mit der Ruhe und Klarheit einer erfahrenen Tauchlehrerin verbindet. Seit 2019 begleitet sie von Zofingen aus Unternehmen im gesamten DACH-Raum.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>Persönliches Gespräch mit Carmen vereinbaren</span>
            {SVG_ARROW}
          </a>
          <a href="https://www.linkedin.com/in/carmen-caselli/" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-outline-light">
            <span>LinkedIn-Profil besuchen</span>
          </a>
        </div>
        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">18 Jahre Finanzpraxis</span>
            <span class="hero-badge-lbl">Treasury Generalist &amp; Junior Portfolio Managerin (CHF Bonds) bei Staatskasse &amp; Pensionskasse</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Tauchlehrerin (Thailand)</span>
            <span class="hero-badge-lbl">Auf 40 Metern Tiefe zählen nur Klarheit, Vorbereitung und hundertprozentiges Vertrauen</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Seit 2019 · get.more.sales</span>
            <span class="hero-badge-lbl">Inhaberin &amp; Geschäftsführerin Carmen Caselli get.more.sales (UID: CHE-471.125.841)</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Verkaufen auf Augenhöhe</span>
            <span class="hero-badge-lbl">Echte Begeisterung, saubere Prozesse und ehrliche Bedarfsanalyse statt Kaufdruck</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/carmen-caselli-portrait-full-card.jpg" alt="Carmen Caselli, Inhaberin und Geschäftsführerin get.more.sales" width="600" height="390">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#0E1721;">Carmen Caselli</div>
            <div style="font-size:0.8rem;color:#243447;">Geschäftsführerin get.more.sales · Zofingen (AG)</div>
          </div>
          <span class="top-bar-badge">SEIT 2019</span>
        </div>
      </div>
    </div>
  </section>

  <section data-section="vita-stationen" id="vita-stationen">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">WERDEGANG &amp; HALTUNG · CARMEN CASELLI</div>
        <h2 class="section-title">Warum diese Kombination im B2B-Vertrieb den Unterschied macht</h2>
        <p class="section-desc">
          Verkaufserfolg im B2B entsteht dort, wo kaufmännische Präzision auf menschliche Vertrauenswürdigkeit trifft:
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Station 01 · 18 Jahre Finanzwelt</span>
              <span class="icon-box">{SVG_SHIELD}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Analytisches Fundament &amp; Zahlenfokus</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Über 18 Jahre in der Finanzbranche, unter anderem im Treasury und als Portfolio Managerin für CHF-Anleihen bei einer Staatskasse und Pensionskasse, schärften den Blick für wirtschaftliche Zusammenhänge, Risikoabwägung und klare Entscheidungsvorlagen.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Souveränes Auftreten auf Geschäftsleitungs- und Investorenebene</span></div>
              <div class="check-item">{SVG_CHECK} <span>Fokus auf Deckungsbeitrag, Marge und messbaren Return on Investment</span></div>
            </div>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Strategiegespräch anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Station 02 · Tauchlehrerin</span>
              <span class="icon-box">{SVG_COMPASS}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Führung und Ruhe unter Druck</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Als Vollzeit-Tauchlehrerin in Thailand begleitete Carmen Caselli Menschen in eine ungewohnte Welt unter Wasser. Wer dort führt, darf keine Unsicherheit ausstrahlen, sondern braucht glasklare Zeichen, Vorbereitung und Empathie.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Menschen auch in anspruchsvollen Verhandlungen ruhig und sicher führen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Echtes Vertrauen aufbauen, bevor über Details verhandelt wird</span></div>
            </div>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Training &amp; Sparring klären</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Station 03 · Seit 2019</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">get.more.sales &amp; Business Mentoring</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Seit 2019 bündelt Carmen Caselli ihre Erfahrung in get.more.sales (CHE-471.125.841). Ihr Ziel: Unternehmen und Verkaufsteams so zu befähigen, dass Verkaufen wieder Freude macht und planbare Spitzenresultate liefert.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Individuelle Begleitung für KMU, B2B-Teams und Selbstständige</span></div>
              <div class="check-item">{SVG_CHECK} <span>Aktive Präsenz und direkter Fachaustausch auf LinkedIn</span></div>
            </div>
          </div>
          <a href="https://www.linkedin.com/in/carmen-caselli/" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Carmen Caselli auf LinkedIn folgen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>
"""


# ==============================================================================
# SEITEN-INHALTE: V2 ZEIGEVERSION STARTSEITE (preview-get-more-sales-v2/index.html)
# ==============================================================================
V2_INDEX_BODY = f"""
  <!-- HERO SECTION -->
  <section class="hero-section" data-section="hero">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light" data-slot="hero_kicker">B2B VERKAUFSBERATUNG, VERTRIEBSTRAINING &amp; SPARRING · ZOFINGEN / AARGAU &amp; DACH</div>
        <h1 class="hero-title" data-slot="hero_title">
          Entfesseln Sie Ihr Verkaufspotenzial. <span>Strukturiert, menschlich, messbar.</span>
        </h1>
        <p class="hero-lead" data-slot="hero_lead">
          Bei get.more.sales begleitet Carmen Caselli Geschäftsführer, Verkaufsleiter und B2B-Vertriebsteams dabei, ihre Verkaufsprozesse glasklar zu strukturieren, Abschlussquoten nachhaltig zu steigern und Neukunden auf Augenhöhe zu gewinnen: ohne künstlichen Kaufdruck, sondern mit analytischer Klarheit und echter Begeisterung.
        </p>

        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
            <span>3-Schritte Smart-Anfrage testen</span>
            {SVG_ARROW}
          </a>
          <a href="#projektberater" class="btn-cta btn-cta-outline-light" data-slot="hero_cta_secondary">
            <span>B2B-Potenzial-Rechner starten</span>
          </a>
        </div>

        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">18+ Jahre Finanzpraxis</span>
            <span class="hero-badge-lbl">Treasury &amp; Portfolio Management (CHF Bonds) kombiniert mit 7+ Jahren B2B-Vertriebsberatung</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Verkaufsstrategie &amp; Prozesse</span>
            <span class="hero-badge-lbl">Massgeschneiderte Vertriebsarchitektur, Pipeline-Struktur und klare Kundenreisen</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Praxisnahes Vertriebstraining</span>
            <span class="hero-badge-lbl">Bedarfsanalyse, souveräne Einwandbehandlung und Abschlussstärke ohne Rabattschlacht</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Antwort in 5–12 Arbeitsstunden</span>
            <span class="hero-badge-lbl">Direkter Draht zu Carmen Caselli in Zofingen · CHE-471.125.841</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/carmen-caselli-portrait-color.jpg" alt="Carmen Caselli, Geschäftsführerin get.more.sales Verkaufsberatung und Vertriebstraining" width="600" height="390" data-slot="hero_image">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#0E1721;">Carmen Caselli · get.more.sales</div>
            <div style="font-size:0.8rem;color:#243447;">Verkaufsberatung, Marktforschung &amp; B2B-Vertriebstraining · Zofingen / AG</div>
          </div>
          <span class="top-bar-badge">BOOST YOUR SALES</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 3 KERNHEBEL -->
  <section data-section="zielgruppen" id="zielgruppen" style="background-color:var(--bg-Warm);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="audiences_kicker">STRATEGIE · MARKTFORSCHUNG · VERTRIEBSTRAINING</div>
        <h2 class="section-title" data-slot="audiences_title">Drei ineinandergreifende Hebel für nachhaltiges Umsatzwachstum</h2>
        <p class="section-desc" data-slot="audiences_desc">
          Als führende Verkaufsberatungs-Agentur kombinieren wir strategische Prozessklarheit mit fundierter Marktanalyse und praxisnaher Umsetzung direkt in Ihrem Verkaufsteam:
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">1. Strategie &amp; Prozesse</span>
              <span class="icon-box">{SVG_COMPASS}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Verkaufsstrategie &amp; Beratung</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Unsere massgeschneiderten Verkaufsstrategien helfen Ihrem Unternehmen, Verkaufsprozesse zu optimieren, Reibungsverluste in der Pipeline zu beseitigen und Umsätze planbar zu steigern.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Individuelle Ist-Analyse Ihrer bestehenden Verkaufsprozesse</span></div>
              <div class="check-item">{SVG_CHECK} <span>Klare Kontakt-, Angebots- und Nachfass-Standards für Ihr Team</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=strategie" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Verkaufsstrategie besprechen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">2. Markt &amp; Positionierung</span>
              <span class="icon-box">{SVG_LAYERS}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Marktforschung &amp; Analyse</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Unsere Marktforschungs- und Analysedienste liefern Ihnen wertvolle Einblicke in Ihren Markt und Ihre Zielgruppe, damit Sie fundierte Entscheidungen treffen und zukünftige Chancen frühzeitig nutzen.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Identifikation der profitabelsten B2B-Kundensegmente und Entscheider</span></div>
              <div class="check-item">{SVG_CHECK} <span>Schärfung Ihrer Nutzenargumentation gegenüber Mitbewerbern</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=analyse" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Potenzialanalyse anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">3. Team &amp; Umsetzung</span>
              <span class="icon-box">{SVG_USERS}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Vertriebstraining &amp; Entwicklung</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Unsere massgeschneiderten Vertriebstrainings unterstützen Ihr Verkaufsteam dabei, seine Fähigkeiten auszubauen, Einwände souverän zu wandeln und die Abschlussleistung im Alltag spürbar zu erhöhen.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Praxisnahes Training an Ihren echten Kundenfällen und Offerten</span></div>
              <div class="check-item">{SVG_CHECK} <span>Persönliches 1:1 Sales-Sparring für Verkaufsleiter und Inhaber</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=training" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Vertriebstraining klären</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 6 LEISTUNGS-MODULE (V2 MIT BLUEPRINT-PREVIEW) -->
  <section data-section="kernangebote" id="kernangebote">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="pillars_kicker">LEISTUNGSÜBERSICHT · GET.MORE.SALES CARMEN CASELLI</div>
        <h2 class="section-title" data-slot="pillars_title">Sechs Leistungs-Module für messbare Verkaufserfolge</h2>
        <p class="section-desc" data-slot="pillars_desc">
          Vom strategischen Prozess-Audit über die Marktanalyse bis zum praxisnahen Team-Training und persönlichen 1:1 Sparring:
        </p>
      </div>

      <div class="grid-3">
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/leistung-verkaufsstrategie-beratung.png" alt="Verkaufsstrategie und Beratung bei get.more.sales" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Modul 01 · Strategie</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Pipeline &amp; Prozesse</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Verkaufsstrategie &amp; Beratung</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Wir strukturieren Ihre gesamte B2B-Kundenreise vom Erstkontakt über die Bedarfsanalyse bis zum verbindlichen Abschluss.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Klare Vertriebsziele, Kennzahlen und Prozess-Standards</span></div>
                <div class="check-item">{SVG_CHECK} <span>Individuelle Verkaufs-Playbooks für Innen- und Aussendienst</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Verkaufsstrategie &amp; Prozess-Beratung', 'Ist-Analyse, Pipeline-Architektur, Offert-Standards &amp; Playbooks', 'Carmen Caselli')">
              <span>Modul-Vorschau öffnen</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/leistung-marktforschung-analyse.png" alt="Marktforschung und Potenzialanalyse bei get.more.sales" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Modul 02 · Analyse</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Markt &amp; Zielgruppe</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Marktforschung &amp; Analyse</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Datenbasierte Einblicke in Ihre Zielmärkte, Kaufmotive von Entscheidern und ungenutzte Umsatzpotenziale.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Idealkunden-Profile (ICP) und Entscheider-Landkarten</span></div>
                <div class="check-item">{SVG_CHECK} <span>Wettbewerbs- und Angebots-Positionierung mit klarem Mehrwert</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Marktforschung &amp; Potenzialanalyse', 'Zielgruppen-Schärfung, Entscheider-Analyse &amp; zukünftige Marktchancen', 'Carmen Caselli')">
              <span>Modul-Vorschau öffnen</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/leistung-vertriebstraining-entwicklung.png" alt="B2B Vertriebstraining mit Carmen Caselli" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Modul 03 · Training</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Team &amp; Abschluss</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">B2B-Vertriebstraining</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Massgeschneiderte Trainings für Verkaufsteams: Gesprächsführung, Fragetechnik, Einwandbehandlung und Preisverhandlung.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Hohe Abschlussquote ohne künstlichen Druck oder Rabatte</span></div>
                <div class="check-item">{SVG_CHECK} <span>Direkter Transfer an Ihren realen Kunden- und Offertfällen</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Vertriebstraining &amp; Team-Entwicklung', 'Bedarfsanalyse, Einwandbehandlung, Preisgespräche &amp; Abschluss-Routine', 'Carmen Caselli')">
              <span>Modul-Vorschau öffnen</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/sales-gallery-meeting-sparring.png" alt="Moderne B2B Akquise über Telefon und LinkedIn" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Modul 04 · Akquise</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Telefon &amp; LinkedIn</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">B2B-Neukunden-Akquise</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Verbindliche Kontaktaufnahme über Telefon, Empfehlungsmanagement und LinkedIn, die bei Entscheidern Vertrauen schafft.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Natürliche Gesprächseinstiege statt starrer Callcenter-Skripte</span></div>
                <div class="check-item">{SVG_CHECK} <span>Kombination aus LinkedIn-Sichtbarkeit und direktem Dialog</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Moderne B2B-Akquise: Telefon &amp; LinkedIn', 'Natürliche Erstansprache, Empfehlungsaufbau &amp; Social Selling', 'Carmen Caselli')">
              <span>Modul-Vorschau öffnen</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/carmen-caselli-portrait-duplex-card.jpg" alt="1:1 Executive Sales-Sparring mit Carmen Caselli" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Modul 05 · Mentoring</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">1:1 auf Augenhöhe</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">1:1 Executive Sales-Sparring</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Persönliche Begleitung für Geschäftsführer, Verkaufsleiter und Berater vor wichtigen Pitches und Grosskunden-Verhandlungen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Ehrliches Sparring mit 18 Jahren Finanz- und Verhandlungserfahrung</span></div>
                <div class="check-item">{SVG_CHECK} <span>Klare Vorbereitung von Strategie, Zahlenrahmen und Einwänden</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('1:1 Executive Sales-Sparring', 'Persönliches Mentoring für Geschäftsführer, Verkaufsleiter &amp; Berater', 'Carmen Caselli')">
              <span>Modul-Vorschau öffnen</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/hero-sales-dashboard-analytics.png" alt="Verkaufsprozess-Audit und Standortbestimmung" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Modul 06 · Einstieg</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Schneller Überblick</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Prozess-Audit &amp; Erstgespräch</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Kompakte Standortbestimmung Ihrer aktuellen Vertriebspipeline: Wo gehen aktuell Anfragen, Offerten oder Margen verloren?
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Unverbindliches Erstgespräch per Telefon oder Video-Call</span></div>
                <div class="check-item">{SVG_CHECK} <span>Persönliche Rückmeldung innerhalb von 5 bis 12 Arbeitsstunden</span></div>
              </div>
            </div>
            <a href="kontakt.html?thema=kennenlernen" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Kostenlosen Termin buchen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

{render_sales_advisor()}

  <!-- KUNDENSTIMMEN & PRAXIS-EINBLICKE (V2) -->
  <section data-section="referenzen" id="referenzen" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="refs_kicker">KUNDENSTIMMEN &amp; PRAXIS-RESULTATE · GET.MORE.SALES</div>
        <h2 class="section-title" data-slot="refs_title">Was unsere Kunden über die Zusammenarbeit sagen</h2>
        <p class="section-desc" data-slot="refs_desc">
          Echte Rückmeldungen und typische B2B-Praxisbeispiele aus Verkaufsstrategie, Marktforschung, Vertriebstraining und 1:1 Sales-Sparring:
        </p>
      </div>

      {render_references_grid(limit=6, is_v2=True)}
    </div>
  </section>

  <!-- FAQ SEKTION -->
  <section data-section="faq" id="faq">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="faq_kicker">HÄUFIGE FRAGEN · VERKAUFSBERATUNG &amp; TRAINING</div>
        <h2 class="section-title" data-slot="faq_title">Antworten rund um Ablauf, Strategie und Erstgespräch</h2>
        <p class="section-desc" data-slot="faq_desc">
          Die wichtigsten Fragen von Geschäftsführern und Verkaufsleitern vor dem ersten Beratungstermin mit Carmen Caselli:
        </p>
      </div>

      {render_faqs_grid()}
    </div>
  </section>
"""


# ==============================================================================
# SEITEN-INHALTE: KONTAKT & 3-SCHRITTE SMART-ANFRAGE (kontakt.html V1 & V2)
# ==============================================================================
def build_kontakt_body(client_slug: str, source_page: str) -> str:
    return f"""
  <section data-section="kontakt-zentrale" style="padding: 56px 0 84px;">
    <div class="container">
      <div class="contact-layout">
        <!-- LEFT COLUMN: DIREKTKONTAKT CARMEN CASELLI -->
        <div class="contact-info-panel">
          <div class="section-kicker" data-slot="contact_kicker">KONTAKT &amp; BERATUNGSTERMIN · ZOFINGEN & DACH-RAUM</div>
          <h1 style="font-size:clamp(1.65rem,2.5vw,2.15rem);font-weight:700;margin-bottom:12px;" data-slot="contact_title">
            Ihr direkter Draht zu Carmen Caselli.
          </h1>
          <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:18px;" data-slot="contact_lead">
            Ob massgeschneiderte Verkaufsstrategie, Marktforschung, praxisnahes Vertriebstraining für Ihr Verkaufsteam oder ein kostenloser erster Beratungstermin: Starten Sie rechts die 3-Schritte Smart-Anfrage oder kontaktieren Sie uns direkt.
          </p>

          <img src="images/carmen-caselli-portrait-color.jpg" alt="Carmen Caselli, Geschäftsführerin get.more.sales in Zofingen" style="width:100%;height:200px;object-fit:cover;object-position:center top;border-radius:var(--radius-sm);margin-bottom:16px;" loading="lazy" decoding="async">

          <div class="contact-direct-list">
            <div class="contact-direct-item">
              <div class="contact-direct-role">Inhaberin &amp; Geschäftsführerin</div>
              <div class="contact-direct-person">Carmen Caselli get.more.sales · CHE-471.125.841</div>
              <div class="contact-direct-links">E-Mail: beratungs-termin@get-more-sales.org · LinkedIn: carmen-caselli</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Verbindliche Reaktionszeit</div>
              <div class="contact-direct-person">Persönliche Antwort in 5 bis 12 Arbeitsstunden</div>
              <div class="contact-direct-links">Direkte Bearbeitung durch Carmen Caselli ohne Umwege über ein Callcenter</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Unternehmenssitz &amp; Einzugsgebiet</div>
              <div class="contact-direct-person">CH-4800 Zofingen (Kanton Aargau)</div>
              <div class="contact-direct-links">Inhouse-Trainings und Beratung in der gesamten Schweiz, im DACH-Raum &amp; via Video-Call</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Direkte Vernetzung auf LinkedIn</div>
              <div class="contact-direct-person">linkedin.com/in/carmen-caselli</div>
              <div class="contact-direct-links"><a href="https://www.linkedin.com/in/carmen-caselli/" target="_blank" rel="noopener noreferrer" style="color:var(--gold-dark);font-weight:700;">Jetzt mit Carmen Caselli auf LinkedIn vernetzen &rarr;</a></div>
            </div>
          </div>
        </div>

        <!-- RIGHT COLUMN: GEFÜHRTER 3-SCHRITTE SMART-ANFRAGE-ASSISTENT -->
        <div class="wizard-card">
          <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:14px;">
            <div>
              <div class="section-kicker" style="margin-bottom:4px;">3-SCHRITTE SMART-ANFRAGE · GET-MORE-SALES.ORG</div>
              <h2 style="font-size:1.35rem;font-weight:700;" id="wpWizardTitle">1. Welches Vertriebsziel steht im Fokus?</h2>
            </div>
            <span class="meta-badge" id="wpActiveAssigneeBadge">Expertin: Carmen Caselli</span>
          </div>

          <div class="wp-stepper" aria-label="Fortschritt">
            <div class="wp-step-pill active" id="wpStepPill1">
              <span class="wp-step-num">1</span>
              <span>Schwerpunkt</span>
            </div>
            <div class="wp-step-pill" id="wpStepPill2">
              <span class="wp-step-num">2</span>
              <span>Team &amp; Ziel</span>
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

            <!-- SCHRITT 1: LEISTUNGSBEREICH -->
            <div class="wp-step-pane active" id="wpStep1">
              <div class="wp-role-grid" id="wpTopicGrid">
                <button type="button" class="wp-role-tile selected" data-topic="Verkaufsstrategie & Prozess-Optimierung" onclick="wpSelectIsTopic('Verkaufsstrategie & Prozess-Optimierung')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_COMPASS}</span>
                    <span class="wp-role-title" data-slot="topic_opt_1">1. Verkaufsstrategie</span>
                  </div>
                  <span class="wp-role-desc">Verkaufsprozesse strukturieren, Pipeline-Klarheit schaffen &amp; Umsätze steigern</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Marktforschung, Zielgruppen & Akquise" onclick="wpSelectIsTopic('Marktforschung, Zielgruppen & Akquise')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_LAYERS}</span>
                    <span class="wp-role-title" data-slot="topic_opt_2">2. Marktforschung</span>
                  </div>
                  <span class="wp-role-desc">Markt- &amp; Zielgruppenanalyse, Positionierung sowie Telefon- &amp; LinkedIn-Akquise</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Vertriebstraining & Team-Entwicklung" onclick="wpSelectIsTopic('Vertriebstraining & Team-Entwicklung')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_USERS}</span>
                    <span class="wp-role-title" data-slot="topic_opt_3">3. Vertriebstraining</span>
                  </div>
                  <span class="wp-role-desc">Bedarfsanalyse, souveräne Einwandbehandlung, Preisgespräche &amp; Abschlussstärke</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="1:1 Sales-Sparring & Kostenloser Beratungstermin" onclick="wpSelectIsTopic('1:1 Sales-Sparring & Kostenloser Beratungstermin')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_AWARD}</span>
                    <span class="wp-role-title" data-slot="topic_opt_4">4. Beratungstermin</span>
                  </div>
                  <span class="wp-role-desc">Kostenlose Standortbestimmung oder persönliches 1:1 Mentoring mit Carmen Caselli</span>
                </button>
              </div>

              <button type="button" class="btn-cta btn-cta-primary" style="width:100%;" onclick="wpNextStep(2)">
                <span>Weiter zu Schritt 2: Team &amp; Ausgangslage</span>
                {SVG_ARROW}
              </button>
            </div>

            <!-- SCHRITT 2: TEAM & ZIELSETZUNG -->
            <div class="wp-step-pane" id="wpStep2">
              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="wpDetail1" class="form-label" id="wpDetail1Label">Branche &amp; Grösse Ihres Verkaufsteams</label>
                  <input type="text" id="wpDetail1" class="form-input" placeholder="z. B. B2B-Industrie, 5 Mitarbeitende im Vertrieb">
                </div>
                <div class="form-field">
                  <label for="wpDetail2" class="form-label" id="wpDetail2Label">Gewünschter Rahmen (Vor Ort, Zofingen oder Video-Call)</label>
                  <input type="text" id="wpDetail2" class="form-input" placeholder="z. B. Erstgespräch per Video-Call oder Inhouse">
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label class="form-label">Gewünschter Zeitraum</label>
                <div class="wp-role-grid" id="wpUrgencyGrid" style="margin-bottom:0;">
                  <button type="button" class="wp-role-tile selected" data-urg="Zeitnaher Beratungstermin (Rückmeldung in 5–12 Arbeitsstunden)" onclick="wpSelectIsUrgency('Zeitnaher Beratungstermin (Rückmeldung in 5–12 Arbeitsstunden)')">
                    <span class="wp-role-title">1. Zeitnaher Beratungstermin</span>
                    <span class="wp-role-desc">Unverbindliches Erstgespräch in den nächsten Tagen vereinbaren</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urg="Mittelfristige Planung (Quartals-Workshop / Jahrestraining)" onclick="wpSelectIsUrgency('Mittelfristige Planung (Quartals-Workshop / Jahrestraining)')">
                    <span class="wp-role-title">2. Quartals- / Jahresplanung</span>
                    <span class="wp-role-desc">Strategie-Workshop oder Vertriebstraining für das kommende Quartal planen</span>
                  </button>
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label for="contactMessage" class="form-label">Welchen Engpass oder welches Ziel möchten Sie lösen? (optional)</label>
                <textarea id="contactMessage" class="form-textarea" placeholder="Beschreiben Sie kurz Ihr Anliegen (z. B. höhere Abschlussquote bei Offerten, strukturierte Neukunden-Akquise, Preisgespräche oder 1:1 Sparring)..."></textarea>
              </div>

              <div class="form-field" style="margin-bottom:18px;">
                <label class="form-label">Optional: Unterlagen, Organigramm oder Angebots-Kurzprofil anhängen (max. 3 Dateien)</label>
                <div class="wp-upload-zone" onclick="document.getElementById('wpPhotoInput').click()">
                  <input type="file" id="wpPhotoInput" accept="image/*,.pdf" multiple style="display:none;" onchange="wpHandlePhotos(this.files)">
                  <div style="font-size:0.86rem;font-weight:600;color:var(--text-main);">Klicken zum Auswählen (PDF, Screenshot oder Bild)</div>
                  <div style="font-size:0.78rem;color:var(--text-muted);">Wird vertraulich direkt Ihrem 1-Seiten-Beratungsdossier beigefügt</div>
                  <div class="wp-upload-preview" id="wpPhotoPreview"></div>
                </div>
              </div>

              <div style="display:flex;gap:12px;justify-content:space-between;">
                <button type="button" class="btn-cta btn-cta-outline" onclick="wpNextStep(1)">
                  <span>Zurück</span>
                </button>
                <button type="button" class="btn-cta btn-cta-primary" style="flex:1;" onclick="wpNextStep(3)">
                  <span>Weiter zu Schritt 3: Kontaktdaten</span>
                  {SVG_ARROW}
                </button>
              </div>
            </div>

            <!-- SCHRITT 3: KONTAKTDATEN & ABSENDEN -->
            <div class="wp-step-pane" id="wpStep3">
              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactName" class="form-label">Vor- und Nachname *</label>
                  <input type="text" id="contactName" class="form-input" placeholder="z. B. Matthias Müller" required>
                </div>
                <div class="form-field">
                  <label for="contactCompany" class="form-label">Unternehmen &amp; Funktion (optional)</label>
                  <input type="text" id="contactCompany" class="form-input" placeholder="z. B. Muster AG · Geschäftsführung">
                </div>
              </div>

              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactPhone" class="form-label">Telefon / Mobile für Rückruf *</label>
                  <input type="tel" id="contactPhone" class="form-input" placeholder="z. B. 079 123 45 67" required>
                </div>
                <div class="form-field">
                  <label for="contactEmail" class="form-label">E-Mail-Adresse *</label>
                  <input type="email" id="contactEmail" class="form-input" placeholder="ihre.email@unternehmen.ch" required>
                </div>
              </div>

              <div class="form-grid-2" style="margin-bottom:16px;">
                <div class="form-field">
                  <label for="contactStreet" class="form-label">Strasse &amp; Nr. (optional)</label>
                  <input type="text" id="contactStreet" class="form-input" placeholder="z. B. Industriestrasse 12">
                </div>
                <div class="form-field">
                  <label for="contactLocation" class="form-label">PLZ &amp; Ort *</label>
                  <input type="text" id="contactLocation" class="form-input" placeholder="z. B. 4800 Zofingen" required>
                </div>
              </div>

              <div id="wpFormError" style="display:none;background-color:#FEF2F2;border:1px solid #FECACA;color:#991B1B;padding:10px 14px;border-radius:var(--radius-sm);font-size:0.86rem;font-weight:600;margin-bottom:14px;"></div>

              <div style="display:flex;gap:12px;justify-content:space-between;">
                <button type="button" class="btn-cta btn-cta-outline" onclick="wpNextStep(2)">
                  <span>Zurück</span>
                </button>
                <button type="submit" id="wpSubmitBtn" class="btn-cta btn-cta-gold" style="flex:1;">
                  <span id="wpSubmitBtnText">1-Seiten-Dossier &amp; Anfrage senden</span>
                  {SVG_ARROW}
                </button>
              </div>
            </div>
          </form>

          <!-- LIVE BESTÄTIGUNGS-COCKPIT NACH ABSENDEN -->
          <div class="wp-success-box" id="wpSuccessBox" aria-live="polite">
            <div class="section-kicker" style="color:#15803D;margin-bottom:6px;">ANFRAGE ERFOLGREICH ÜBERMITTELT · GET.MORE.SALES</div>
            <h3 style="font-size:1.34rem;font-weight:700;color:#0E1721;margin-bottom:8px;">Vielen Dank! Ihr 1-Seiten-Beratungsdossier ist bereit.</h3>
            <p style="font-size:0.9rem;color:#243447;margin-bottom:16px;">
              Carmen Caselli hat Ihre Angaben erhalten und meldet sich in der Regel innerhalb von 5 bis 12 Arbeitsstunden persönlich bei Ihnen.
            </p>
            <div class="form-grid-2" style="margin-bottom:16px;">
              <div style="background-color:#FFFFFF;border:1px solid #86EFAC;padding:10px 12px;border-radius:var(--radius-sm);">
                <div style="font-size:0.74rem;font-weight:700;color:#166534;text-transform:uppercase;">Referenz-Code</div>
                <div style="font-family:'Lexend',sans-serif;font-size:0.98rem;font-weight:700;color:#0E1721;" id="wpResRef">#WP-2026</div>
              </div>
              <div style="background-color:#FFFFFF;border:1px solid #86EFAC;padding:10px 12px;border-radius:var(--radius-sm);">
                <div style="font-size:0.74rem;font-weight:700;color:#166534;text-transform:uppercase;">Zuständige Ansprechpartnerin</div>
                <div style="font-family:'Lexend',sans-serif;font-size:0.94rem;font-weight:700;color:#0E1721;" id="wpResAssigned">Carmen Caselli (get.more.sales)</div>
              </div>
            </div>
            <div style="background-color:#FFFFFF;border:1px solid #86EFAC;padding:12px 14px;border-radius:var(--radius-sm);margin-bottom:14px;font-size:0.85rem;color:#243447;">
              <div><strong>Rückmeldung:</strong> <span id="wpResCallback">In der Regel innerhalb von 5–12 Arbeitsstunden</span></div>
              <div style="margin-top:4px;"><strong>Zustellung:</strong> <span id="wpResChannels">1-Seiten-PDF-Dossier erstellt</span></div>
            </div>
            <pre id="wpResWaPreview" style="background-color:#F7FAFF;border:1px solid var(--border-light);padding:10px 12px;border-radius:var(--radius-sm);font-size:0.78rem;white-space:pre-wrap;color:#243447;margin-bottom:14px;"></pre>
            <div style="display:flex;gap:12px;flex-wrap:wrap;">
              <a href="#" id="wpResPdfBtn" target="_blank" rel="noopener" class="btn-cta btn-cta-primary btn-sm">
                <span>1-Seiten-PDF-Dossier öffnen</span>
                {SVG_ARROW}
              </a>
              <a href="index.html" class="btn-cta btn-cta-outline btn-sm">
                <span>Zurück zur Startseite</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <script>
    var wpIsState = {{
      step: 1,
      topic: 'Verkaufsstrategie & Prozess-Optimierung',
      urgency: 'Zeitnaher Beratungstermin (Rückmeldung in 5–12 Arbeitsstunden)',
      photos: []
    }};

    function wpStripEmojisForDom(str) {{
      return String(str || '').replace(/[\\u{{1F300}}-\\u{{1FAFF}}\\u{{2600}}-\\u{{27BF}}]/gu, '').trim();
    }}

    function wpSelectIsTopic(topic) {{
      wpIsState.topic = topic;
      var tiles = document.querySelectorAll('#wpTopicGrid .wp-role-tile');
      for (var i = 0; i < tiles.length; i++) {{
        tiles[i].classList.toggle('selected', tiles[i].getAttribute('data-topic') === topic);
      }}
    }}

    function wpSelectIsUrgency(urg) {{
      wpIsState.urgency = urg;
      var tiles = document.querySelectorAll('#wpUrgencyGrid .wp-role-tile');
      for (var i = 0; i < tiles.length; i++) {{
        tiles[i].classList.toggle('selected', tiles[i].getAttribute('data-urg') === urg);
      }}
    }}

    function wpNextStep(step) {{
      wpIsState.step = step;
      for (var i = 1; i <= 3; i++) {{
        var pane = document.getElementById('wpStep' + i);
        var pill = document.getElementById('wpStepPill' + i);
        if (pane) pane.classList.toggle('active', i === step);
        if (pill) {{
          pill.classList.toggle('active', i === step);
          pill.classList.toggle('done', i < step);
        }}
      }}
      var titles = {{
        1: '1. Welches Vertriebsziel steht im Fokus?',
        2: '2. Angaben zu Ihrem Team & Anliegen',
        3: '3. Ihre Kontaktdaten für das Erstgespräch'
      }};
      var tEl = document.getElementById('wpWizardTitle');
      if (tEl && titles[step]) tEl.textContent = titles[step];
    }}

    function wpHandlePhotos(files) {{
      if (!files || !files.length) return;
      var maxFiles = Math.min(files.length, 3 - wpIsState.photos.length);
      for (var i = 0; i < maxFiles; i++) {{
        (function(file) {{
          var reader = new FileReader();
          reader.onload = function(e) {{
            wpIsState.photos.push({{ name: file.name, data_url: e.target.result }});
            wpRenderPhotos();
          }};
          reader.readAsDataURL(file);
        }})(files[i]);
      }}
    }}

    function wpRenderPhotos() {{
      var box = document.getElementById('wpPhotoPreview');
      if (!box) return;
      box.innerHTML = '';
      for (var i = 0; i < wpIsState.photos.length; i++) {{
        var img = document.createElement('img');
        img.src = wpIsState.photos[i].data_url;
        img.alt = wpIsState.photos[i].name || 'Upload';
        box.appendChild(img);
      }}
    }}

    function wpSubmitIsLead(e) {{
      if (e) e.preventDefault();
      var errBox = document.getElementById('wpFormError');
      if (errBox) errBox.style.display = 'none';

      var name = (document.getElementById('contactName').value || '').trim();
      var company = (document.getElementById('contactCompany').value || '').trim();
      var phone = (document.getElementById('contactPhone').value || '').trim();
      var email = (document.getElementById('contactEmail').value || '').trim();
      var street = (document.getElementById('contactStreet').value || '').trim();
      var loc = (document.getElementById('contactLocation').value || '').trim();
      var msg = (document.getElementById('contactMessage').value || '').trim();
      var d1 = (document.getElementById('wpDetail1').value || '').trim();
      var d2 = (document.getElementById('wpDetail2').value || '').trim();
      var hp = (document.getElementById('wpHoneypot').value || '').trim();

      if (!name || !phone || !email || !loc) {{
        if (errBox) {{
          errBox.textContent = 'Bitte füllen Sie Name, Telefon, E-Mail und PLZ/Ort vollständig aus.';
          errBox.style.display = 'block';
        }}
        return false;
      }}

      var btn = document.getElementById('wpSubmitBtn');
      var btnTxt = document.getElementById('wpSubmitBtnText');
      if (btn) btn.disabled = true;
      if (btnTxt) btnTxt.textContent = '1-Seiten-Dossier wird erstellt...';

      var extra = {{
        'Gewählter Schwerpunkt': wpIsState.topic,
        'Branche & Teamgrösse': d1 || 'Nach Rücksprache',
        'Gewünschter Rahmen': d2 || 'Telefon / Video-Call oder vor Ort',
        'Zeitraum': wpIsState.urgency
      }};
      if (street) extra['Strasse / Ort'] = street + ', ' + loc;

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
        message: msg || ('get.more.sales Anfrage zu ' + wpIsState.topic),
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
        document.getElementById('wpResAssigned').textContent = res.assigned_to || 'Carmen Caselli (get.more.sales)';
        document.getElementById('wpResCallback').textContent = res.callback_window || 'Innerhalb von 5–12 Arbeitsstunden';
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
          errBox.textContent = 'Netzwerkfehler bei der Übermittlung. Bitte schreiben Sie direkt an beratungs-termin@get-more-sales.org.';
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
          'strategie': 'Verkaufsstrategie & Prozess-Optimierung',
          'analyse': 'Marktforschung, Zielgruppen & Akquise',
          'training': 'Vertriebstraining & Team-Entwicklung',
          'sparring': '1:1 Sales-Sparring & Kostenloser Beratungstermin',
          'kennenlernen': '1:1 Sales-Sparring & Kostenloser Beratungstermin'
        }};
        if (t && map[t]) {{
          wpSelectIsTopic(map[t]);
        }}
      }} catch (err) {{}}
    }})();
  </script>
"""


# 3. Alle Seiten für Variante 1 (Vollversion) schreiben
v1_pages = [
    ("index.html", "get.more.sales · Carmen Caselli | B2B-Verkaufsberatung, Marktforschung & Vertriebstraining Zofingen / Aargau", "startseite", V1_INDEX_BODY),
    ("leistungen.html", "Leistungen & Trainings | Verkaufsstrategie, Marktforschung, Vertriebstraining & 1:1 Sparring – get.more.sales", "leistungen", V1_LEISTUNGEN_BODY),
    ("referenzen.html", "Kundenstimmen & B2B-Praxis-Resultate | get.more.sales Carmen Caselli Verkaufsberatung", "referenzen", V1_REFERENZEN_BODY),
    ("ueber-uns.html", "Über Carmen Caselli | 18 Jahre Finanzwelt, Tauchlehrerin & B2B-Vertriebsexpertin – get.more.sales", "ueber-uns", V1_UEBER_UNS_BODY),
    ("kontakt.html", "Kontakt, Beratungstermin & 3-Schritte Smart-Anfrage | get.more.sales Carmen Caselli Zofingen", "kontakt", build_kontakt_body("get-more-sales-vv", "preview-get-more-sales/kontakt.html")),
]

for fname, title, nav_key, body in v1_pages:
    full_html = render_v1_shell(fname, title, nav_key, body)
    (V1_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V1] Wrote {fname} ({len(full_html)} bytes)")

# 4. Alle Seiten für Variante 2 (Zeigeversion / Vorschau-Entwurf) schreiben
v2_pages = [
    ("index.html", "get.more.sales · Carmen Caselli | B2B-Verkaufsberatung & Vertriebstraining (Zeigeversion / Vorschau-Entwurf)", "startseite", V2_INDEX_BODY),
    ("kontakt.html", "Kontakt & 3-Schritte Smart-Anfrage (Zeigeversion) | get.more.sales Carmen Caselli Zofingen / Aargau", "kontakt", build_kontakt_body("get-more-sales-v2", "preview-get-more-sales-v2/kontakt.html")),
]

for fname, title, nav_key, body in v2_pages:
    full_html = render_v2_shell(fname, title, nav_key, body)
    (V2_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V2] Wrote {fname} ({len(full_html)} bytes)")

# 5. Partner-Attribution (#wpPartnerModal exklusiv für David Hügli · magnet-Xs gmbh) injizieren
subprocess.run(["python3", str(BASE_DIR / "scripts" / "inject_partner_attribution.py")], check=True)

# 6. Studio Cockpit v4.0 (cockpit.html) für beide Varianten generieren
subprocess.run(["python3", str(BASE_DIR / "scripts" / "build_client_cockpit.py"), "--slug", "preview-get-more-sales"], check=True)
subprocess.run(["python3", str(BASE_DIR / "scripts" / "build_client_cockpit.py"), "--slug", "preview-get-more-sales-v2"], check=True)

# 7. Compile Site Pipeline (Pre-Build Gates & Airbag)
subprocess.run(["python3", str(BASE_DIR / "scripts" / "compile_site.py"), "--site", "preview-get-more-sales", "--skip-device-audit"], check=True)
subprocess.run(["python3", str(BASE_DIR / "scripts" / "compile_site.py"), "--site", "preview-get-more-sales-v2", "--skip-device-audit"], check=True)
print("Successfully built and compiled preview-get-more-sales and preview-get-more-sales-v2.")

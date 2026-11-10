#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator für die WebPilot-Referenz-Aufbereitung von mondocani.ch (MONDOCANI · Die mobile Hundeschule · Dorette Sieber, Flumenthal / Solothurn & Trainingsplatz Derendingen):
- Variante 1 (Vollversion): /home/brainuser/workspaces/mxs-embed/preview-mondocani
  Live-URL: https://vorschau.magnet-xs.ch/mondocani-vollversion/ (5 voll ausgebaute Seiten + Studio Cockpit v4.0)
- Variante 2 (Zeigeversion / Vorschau-Entwurf): /home/brainuser/workspaces/mxs-embed/preview-mondocani-v2
  Live-URL: https://vorschau.magnet-xs.ch/mondocani-v2/ (2 ausgearbeitete Beispiel-Seiten: Startseite inkl. Mensch-Hund-Angebotsfinder + 3-Schritte Smart-Anfrage,
  plus transparente Themenbereich-Vorschaukarten für die 3 weiteren Unterseiten).

Strikt nach:
- UI-LAYOUT-RULES.md (Canary: UI-LAYOUT-2026-V1, #UI-01, #UI-02, #UI-13, #UI-14, #UI-16 Evolution-Modus Light Lock S-27)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1, 0 Eszett, 0 Em-Dash im Satz, Einser-Ausschreibungs-Regel, 100 % Schweizer Hochdeutsch)
"""

import json
import subprocess
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
V1_DIR = BASE_DIR / "preview-mondocani"
V2_DIR = BASE_DIR / "preview-mondocani-v2"

V1_DIR.mkdir(parents=True, exist_ok=True)
V2_DIR.mkdir(parents=True, exist_ok=True)

BEFORE_INVENTORY = {
    "source_url": "https://mondocani.ch/",
    "crawled_at": "2026-11-10",
    "company_name": "MONDOCANI · Die mobile Hundeschule",
    "legal_entity": "MONDOCANI · Dorette Sieber",
    "uid": "",
    "claim": "Verstehe deinen Hund. Erkenne dich selbst.",
    "subline": "Ganzheitliche Mensch-Hund-Begleitung in Solothurn, Flumenthal, Derendingen, Bern und Basel: Beziehung statt Erziehung, natürliche Kommunikation und bewusstes Miteinander auf Augenhöhe mit Dorette Sieber.",
    "address": {
        "street": "Sportstrasse (Trainingsplatz Derendingen) · Sitz Flumenthal",
        "zip": "4552",
        "city": "Derendingen / Solothurn",
        "canton": "SO",
        "country": "Schweiz"
    },
    "contact": {
        "email": "mail@mondocani.ch",
        "phone_primary": "+41 79 446 70 43",
        "phone_display": "079 446 70 43",
        "hours": "Einzelcoaching & Hausbesuche nach Vereinbarung | Rudeltreffen jeden Freitag 14:00 – 15:30 Uhr & 16:00 – 17:30 Uhr in 4552 Derendingen"
    },
    "team": [
        {
            "name": "Dorette Sieber",
            "role": "Inhaberin MONDOCANI · Coach für Mensch & Hund",
            "phone": "079 446 70 43",
            "phone_href": "tel:+41794467043",
            "image": "images/team-dorette-sieber-portrait.jpg",
            "qualification": "Wegbereiterin Mensch-Hund-Kommunikation (nach Maja Nowak) · Tierkommunikation (Sybille Lüthi) · NLP/Mentalcoach BMC · Sozialarbeit",
            "bio": "Seit 2018 begleitet Dorette Sieber mit MONDOCANI Mensch-Hund-Teams in der Region Solothurn, Bern und Basel. Geprägt durch viele Jahre als Älplerin mit Hunden in den Schweizer Bergen, ihre Podenco-Garafiano-Hündin Tajuya auf La Palma sowie die Arbeit in europäischen Hundeauffangstationen verbindet sie feinsprachliche Hunde-Wahrnehmung mit pädagogischer und therapeutischer Erfahrung."
        }
    ],
    "references": [
        {
            "title": "Doris & Claude mit Podengo Milu",
            "category": "Kundenstimme · Podengo",
            "highlight": "Vertrauen & Freude",
            "scope": "Begleitung in Stärken & Schwächen · Respekt und Führung im Einklang",
            "before_img": "images/ref-einzelcoaching-kontakt.jpg",
            "after_img": "images/ref-begleitung-augenhoehe.jpg",
            "desc": "«Seither werden meine Milu, Claude und ich ganz stimmig, bestimmt und sanft zugleich von dir begleitet. Das Sein mit meinem Podengo Milu ist wieder freudig geworden, Respekt und Beziehung stehen nicht mehr im Widerspruch.»"
        },
        {
            "title": "Ute mit Foxy & Róisín",
            "category": "Kundenstimme · Zwei Hunde",
            "highlight": "Ohne Leckerli & Ziehen",
            "scope": "Unterschiedliche Wesensarten zweier Hunde fein und ruhig führen",
            "before_img": "images/ref-einzelcoaching-spaziergang.jpg",
            "after_img": "images/ref-einzelcoaching-ruhe-vertrauen.jpg",
            "desc": "«Kein Ziehen des Hundes, sondern Gemeinsamkeit und feinste Aufmerksamkeit war das Resultat nach wenigen Minuten. In ihrer Ruhe erkannte Dorette sofort die unterschiedlichen Wesensarten meiner zwei Hunde, ganz leise, ohne Manipulation und ohne Leckerlis.»"
        },
        {
            "title": "Angeborene Rudelstellung erkennen",
            "category": "Kundenstimme · Rudel-Rolle",
            "highlight": "Klarheit im Alltag",
            "scope": "Den angeborenen «Beruf» des Hundes verstehen und wertschätzen",
            "before_img": "images/ref-galerie-hund-blick-02.jpg",
            "after_img": "images/ref-gruppentreffen-rudel-derendingen.jpg",
            "desc": "«Mir hat ihr entspannter Umgang mit Hunden gefallen. Sie hat mir die Stellung gezeigt, die mein Hund in einem Rudel haben könnte. Das hilft mir, ihn als ganzes Wesen zu respektieren und klarer sowie bewusster zu führen.»"
        },
        {
            "title": "Strassenhunde & Tierschutzhunde begleiten",
            "category": "Praxis-Einblick",
            "highlight": "Sicherheit geben",
            "scope": "Traumatisierte oder unsichere Hunde mit Vorgeschichte einfühlsam stabilisieren",
            "before_img": "images/ref-galerie-begegnung-05.jpg",
            "after_img": "images/ref-hundegestuetztes-coaching-natur.jpg",
            "desc": "Ein übernommener Strassenhund bringt seine eigene Geschichte mit. Im ruhigen Tempo lernen Mensch und Hund, Ängste abzubauen, Orientierung anzunehmen und im neuen Lebensraum tiefe Sicherheit zu finden."
        },
        {
            "title": "Welpen-Coaching & Fragen vor dem Hundekauf",
            "category": "Praxis-Einblick",
            "highlight": "Welpen & Kauf",
            "scope": "Prüfung der passenden Wesensart vor der Adoption & friedvoller Beziehungsaufbau",
            "before_img": "images/ref-galerie-vertrauen-06.jpg",
            "after_img": "images/ref-galerie-hund-wiese-01.jpg",
            "desc": "Schon vor dem Kauf prüfen wir, welcher Hund nicht nur herzig wirkt, sondern wirklich zu Ihrer Lebenssituation passt. Nach dem Einzug legen wir ohne Überforderung ein ruhiges Fundament für das ganze Hundeleben."
        },
        {
            "title": "Hundegestütztes Coaching als Spiegel",
            "category": "Co-Coach Hund",
            "highlight": "Klare Reflexion",
            "scope": "Körpersprache, Selbstwert, innere Haltung und gesunde Grenzen stärken",
            "before_img": "images/ref-kontakt-portrait-hund.jpg",
            "after_img": "images/ref-hundegestuetztes-coaching-reflexion.jpg",
            "desc": "Hunde bewerten nicht, sie reagieren unmittelbar auf unsere innere Klarheit. Als Co-Trainer helfen sie uns, eigene Muster zu erkennen, präsenter zu kommunizieren und im Alltag wie im Beruf souverän zu führen."
        }
    ],
    "faqs": [
        {
            "q": "Was bedeutet «Beziehung statt Erziehung» bei MONDOCANI?",
            "a": "Statt den Hund über Kommandos, Leckerli-Ablenkung oder starre Dressur nach menschlichen Vorstellungen zu formen, schauen wir auf seine Bedürfnisse, seine Körpersprache und Ihre gemeinsame Verbindung. Wenn der Hund spürt, dass Sie ruhig, klar und verlässlich führen, folgt er Ihnen freiwillig aus Vertrauen."
        },
        {
            "q": "Wie läuft der erste Termin im Einzelcoaching ab und was kostet er?",
            "a": "Für den ersten Termin komme ich gerne direkt zu Ihnen nach Hause (Dauer ca. 1.5 bis 2 Stunden), um die Wohn-, Fütterungs- und Lebenssituation kennenzulernen. Anschliessend beobachten wir Ihr Zusammenspiel auf einem Spaziergang in gewohnter Umgebung. Der Stundenansatz beträgt CHF 80.— pro Stunde."
        },
        {
            "q": "Wann und wo finden die wöchentlichen Rudeltreffen statt?",
            "a": "Unsere Rudeltreffen finden jeden Freitagnachmittag in zwei Gruppen von 14:00 bis 15:30 Uhr sowie von 16:00 bis 17:30 Uhr statt. Nach einem gemeinsamen Spaziergang treffen wir uns auf dem grossen eingezäunten Platz des Clubs für Deutsche Doggen an der Sportstrasse in 4552 Derendingen (direkt neben dem Fussballplatz). Der Beitrag liegt bei CHF 40.— pro 1.5 Stunden."
        },
        {
            "q": "Brauche ich für das hundegestützte Coaching einen eigenen Hund?",
            "a": "Nein. Beim hundegestützten Coaching für persönliche Weiterentwicklung, Selbstbewusstsein, Stressbewältigung oder Führungsfragen können Sie entweder mit Ihrem eigenen Hund kommen oder mit meinem erfahrenen Hund als feinfühligem Co-Coach arbeiten."
        },
        {
            "q": "In welchen Regionen sind Hausbesuche möglich?",
            "a": "Vom Standort Flumenthal / Solothurn aus begleite ich Mensch-Hund-Teams mobil im ganzen Raum Solothurn, Derendingen, Zuchwil und Oberaargau sowie regelmässig in der Umgebung Bern, Basel und Münchenstein."
        },
        {
            "q": "Kann ich Ihre Arbeitsweise vorab unverbindlich kennenlernen?",
            "a": "Sehr gerne. Sie können jederzeit ein kostenloses 15-minütiges Erstgespräch per Telefon (079 446 70 43) oder Zoom nutzen oder am Freitag ab 16:00 Uhr unseren Erlebnisvortrag zum Kennenlernen auf dem eingezäunten Hundeplatz in Derendingen besuchen."
        }
    ]
}

(V1_DIR / "before.json").write_text(json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False), encoding="utf-8")
(V2_DIR / "before.json").write_text(json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False), encoding="utf-8")

for target_dir, slug_val, pub_slug, is_v2 in [
    (V1_DIR, "preview-mondocani", "mondocani-vollversion", False),
    (V2_DIR, "preview-mondocani-v2", "mondocani-v2", True)
]:
    (target_dir / "company.json").write_text(json.dumps({
        "company_name": "MONDOCANI · Die mobile Hundeschule" + (" (Zeigeversion / Vorschau-Entwurf)" if is_v2 else " · Dorette Sieber"),
        "slug": slug_val,
        "public_slug": pub_slug,
        "cockpit_token": "mondocani2026",
        "city": "Flumenthal / Solothurn & Derendingen",
        "canton": "SO",
        "postal_code": "4552",
        "street_address": "Sportstrasse (Trainingsplatz Derendingen) · Sitz Flumenthal",
        "phone": "+41 79 446 70 43",
        "email": "mail@mondocani.ch",
        "uid": "",
        "source_url": "https://mondocani.ch/",
        "partner_id": "jenny"
    }, indent=2, ensure_ascii=False), encoding="utf-8")

v1_config = {
    "company_name": "MONDOCANI · Die mobile Hundeschule · Solothurn",
    "slug": "preview-mondocani",
    "public_slug": "mondocani-vollversion",
    "cockpit_token": "mondocani2026",
    "template": "warm-humanist-editorial-v1",
    "partner_id": "jenny",
    "pages": ["index.html", "leistungen.html", "referenzen.html", "ueber-uns.html", "kontakt.html"]
}
(V1_DIR / "config.json").write_text(json.dumps(v1_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V1_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-mondocani",
    "public_slug": "mondocani-vollversion",
    "token": "mondocani2026",
    "name": "MONDOCANI · Die mobile Hundeschule · Dorette Sieber Solothurn (Vollversion)",
    "Updated": "2026-11-10",
    "PagesCount": 5,
    "ReferencesCount": 6,
    "TeamCount": 1
}, indent=2, ensure_ascii=False), encoding="utf-8")

v2_config = dict(v1_config)
v2_config.update({
    "company_name": "MONDOCANI · Die mobile Hundeschule (Zeigeversion / Vorschau-Entwurf)",
    "slug": "preview-mondocani-v2",
    "public_slug": "mondocani-v2",
    "cockpit_token": "mondocani2026",
    "template": "warm-humanist-editorial-preview-v2",
    "pages": ["index.html", "kontakt.html"]
})
(V2_DIR / "config.json").write_text(json.dumps(v2_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V2_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-mondocani-v2",
    "public_slug": "mondocani-v2",
    "token": "mondocani2026",
    "name": "MONDOCANI · Die mobile Hundeschule (Zeigeversion / Vorschau-Entwurf)",
    "Updated": "2026-11-10",
    "PagesCount": 2,
    "ReferencesCount": 6,
    "TeamCount": 1
}, indent=2, ensure_ascii=False), encoding="utf-8")

print("Wrote before.json, company.json, config.json, site.json for V1 and V2.")


SHARED_CSS = """
    :root {
      --charcoal: #2B1E11;
      --charcoal-deep: #1E140A;
      --charcoal-mid: #4A3522;
      --wp-expected-hero-polarity: "light";
      --wp-archetype: "warm_humanist_editorial";
      --gold: #AB6900;
      --gold-hover: #8C5500;
      --gold-dark: #8C5500;
      --gold-soft: #FDF3E6;
      --gold-border: #E8CBA5;
      --crimson: #AB6900;
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
"""



SVG_CHECK = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>'
SVG_ARROW = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'
SVG_HOME = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'
SVG_HEART = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>'
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
            f'''<button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Praxis-Einblick: {ref['title']}', '{ref['category']} · {ref['scope']} · {ref.get('highlight', 'Echte Rückmeldung')}', 'Dorette Sieber (Coach für Mensch &amp; Hund)')">
              <span>Erfahrungsbericht &amp; Einblick lesen</span>
              {SVG_ARROW}
            </button>'''
            if is_v2
            else f'''<a href="kontakt.html?thema=einzelcoaching" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Ähnliches Anliegen mit Dorette besprechen</span>
              {SVG_ARROW}
            </a>'''
        )
        cards.append(f"""
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="{ref['after_img']}" alt="MONDOCANI Mensch-Hund-Begleitung Solothurn: {ref['title']}" loading="lazy" decoding="async">
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
                <div class="check-item">{SVG_CHECK} <span><strong>Wirkung:</strong> {ref.get('highlight', 'Ruhe & Vertrauen')}</span></div>
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
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 style="font-size:1.14rem;font-weight:700;margin-bottom:10px;">{f['q']}</h3>
            <p style="font-size:0.9rem;color:var(--text-body);line-height:1.62;">{f['a']}</p>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Persönlich mit Dorette Sieber klären</span>
            {SVG_ARROW}
          </a>
        </div>""")
    return '<div class="grid-2">\n' + "\n".join(cards) + "\n      </div>"


def render_mondocani_advisor() -> str:
    return f"""
  <!-- INTERAKTIVER MENSCH-HUND-ANGEBOTS- & BEGLEITUNGS-FINDER -->
  <section data-section="projektberater" id="projektberater" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="calc_kicker">INTERAKTIVER ANGEBOTS- &amp; BEGLEITUNGS-FINDER · SOLOTHURN &amp; DERENDINGEN</div>
        <h2 class="section-title" data-slot="calc_title">Welche Begleitung passt zu Ihnen und Ihrem Hund?</h2>
        <p class="section-desc" data-slot="calc_desc">
          Wählen Sie Ihre aktuelle Situation, Ihr wichtigstes Thema und den gewünschten Einstiegsort. Unser Begleitungs-Finder zeigt Ihnen sofort den passenden Weg bei MONDOCANI inklusive transparentem Tarif:
        </p>
      </div>

      <div class="grid-2">
        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">In 15 Sekunden auswählen</span>
              <span class="icon-box">{SVG_COMPASS}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:14px;">1. Ihre aktuelle Ausgangslage</h3>
            <div class="calc-option-grid" id="susiCalcRoleGrid">
              <button type="button" class="calc-option-btn active" data-role="privat" onclick="susiSetCalc('role','privat')">
                <span class="calc-opt-title">Mensch &amp; Hund</span>
                <span class="calc-opt-sub">Alltag, Bindung, Junghund oder Welpe</span>
              </button>
              <button type="button" class="calc-option-btn" data-role="architektur" onclick="susiSetCalc('role','architektur')">
                <span class="calc-opt-title">Tierschutzhund</span>
                <span class="calc-opt-sub">Strassenhund, Unsicherheit &amp; Ängste</span>
              </button>
              <button type="button" class="calc-option-btn" data-role="bau" onclick="susiSetCalc('role','bau')">
                <span class="calc-opt-title">Co-Coach Hund</span>
                <span class="calc-opt-sub">Hund als Co-Coach &amp; ehrlicher Spiegel</span>
              </button>
            </div>

            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:14px;">2. Gewünschte Begleitungsform</h3>
            <div class="calc-option-grid" id="susiCalcScopeGrid">
              <button type="button" class="calc-option-btn active" data-scope="dach" onclick="susiSetCalc('scope','dach')">
                <span class="calc-opt-title">Einzelcoaching</span>
                <span class="calc-opt-sub">Individuell zu Hause &amp; unterwegs</span>
              </button>
              <button type="button" class="calc-option-btn" data-scope="innen" onclick="susiSetCalc('scope','innen')">
                <span class="calc-opt-title">Rudeltreffen</span>
                <span class="calc-opt-sub">Freitags-Gruppe &amp; Wiese Derendingen</span>
              </button>
              <button type="button" class="calc-option-btn" data-scope="aussen" onclick="susiSetCalc('scope','aussen')">
                <span class="calc-opt-title">Workshops</span>
                <span class="calc-opt-sub">Erlebnisvortrag &amp; Rudelbeobachtung</span>
              </button>
            </div>

            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:14px;">3. Gewünschter erster Schritt</h3>
            <div class="calc-option-grid" id="susiCalcModeGrid" style="margin-bottom:0;">
              <button type="button" class="calc-option-btn active" data-mode="komplett" onclick="susiSetCalc('mode','komplett')">
                <span class="calc-opt-title">Hausbesuch</span>
                <span class="calc-opt-sub">Erster Termin (1.5–2 Std.) bei Ihnen</span>
              </button>
              <button type="button" class="calc-option-btn" data-mode="mithilfe" onclick="susiSetCalc('mode','mithilfe')">
                <span class="calc-opt-title">Derendingen</span>
                <span class="calc-opt-sub">Eingezäunter Platz Sportstrasse</span>
              </button>
              <button type="button" class="calc-option-btn" data-mode="leitung" onclick="susiSetCalc('mode','leitung')">
                <span class="calc-opt-title">Erstgespräch</span>
                <span class="calc-opt-sub">Kostenlos per Telefon oder Zoom</span>
              </button>
            </div>
          </div>
          <div style="padding-top:14px;border-top:1px solid var(--border-light);font-size:0.82rem;color:var(--text-body);display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;">
            <span>Beziehung statt Erziehung · Kontakt statt Kontrolle</span>
            <strong style="color:var(--gold-dark);font-family:'Lexend',sans-serif;">MONDOCANI · Dorette Sieber</strong>
          </div>
        </div>

        <div class="content-card card-dark">
          <div>
            <div class="card-badge-row">
              <span class="top-bar-badge" id="susiCalcRefBadge">EMPFEHLUNG: INDIVIDUELLES EINZELCOACHING &amp; HAUSBESUCH</span>
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 style="font-size:1.36rem;font-weight:700;margin-bottom:8px;" id="susiCalcHeadline">Einzelcoaching für eine ruhige, vertrauensvolle Mensch-Hund-Beziehung</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;" id="susiCalcDesc">
              Beim ersten Treffen (ca. 1.5 bis 2 Stunden) besucht Dorette Sieber Sie gerne zu Hause, um Ihre Wohn- und Alltagssituation kennenzulernen. Anschliessend beobachten wir Ihr Zusammenspiel auf einem entspannten Spaziergang.
            </p>

            <div class="calc-kpi-grid">
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="susiCalcLead">CHF 80.— / Std.</div>
                <div class="calc-kpi-lbl">Transparenter Tarif im Einzelcoaching</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="susiCalcModeOut">Hausbesuch &amp; Alltag</div>
                <div class="calc-kpi-lbl">Gewählter Einstieg &amp; Treffpunkt</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="susiCalcPartner">Solothurn, Bern &amp; Basel</div>
                <div class="calc-kpi-lbl">Mobiles Einsatzgebiet &amp; Derendingen</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="susiCalcStep">15 Min. kostenlos</div>
                <div class="calc-kpi-lbl">Vorgespräch per Telefon oder Zoom</div>
              </div>
            </div>

            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Ohne Leckerli-Dressur &amp; ohne Druck:</strong> Wir fördern eine ruhige, feinsprachliche und klare innere Haltung, der Ihr Hund freiwillig vertraut.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Persönliche Begleitung durch Dorette Sieber:</strong> Einfühlsam, lebensnah und individuell auf das Temperament Ihres Hundes abgestimmt.</span></div>
            </div>
          </div>

          <a href="kontakt.html?thema=einzelcoaching" id="susiCalcCta" class="btn-cta btn-cta-gold" style="width:100%;">
            <span>Termin oder Erstgespräch anfragen</span>
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
      <div class="section-kicker">RECHTLICHE ANGABEN · KANTON SOLOTHURN</div>
      <h3 id="wpImpTitle" style="font-size:1.36rem;font-weight:700;margin-bottom:10px;">Impressum &amp; Datenschutz (MONDOCANI)</h3>
      <div style="font-size:0.88rem;color:var(--text-body);line-height:1.62;display:flex;flex-direction:column;gap:12px;">
        <div style="background-color:var(--bg-page);border:1px solid var(--border-light);border-left:4px solid var(--gold);padding:12px 14px;border-radius:var(--radius-sm);">
          <strong>MONDOCANI · Die mobile Hundeschule</strong><br>
          Inhaberin: Dorette Sieber · Flumenthal / Solothurn (Kanton Solothurn)<br>
          Eingezäunter Trainingsplatz: Club für Deutsche Doggen · Sportstrasse · CH-4552 Derendingen<br>
          Telefon: +41 79 446 70 43 · E-Mail: mail@mondocani.ch · Web: https://mondocani.ch
        </div>
        <p>
          <strong>Verantwortliche Person &amp; Tätigkeit:</strong><br>
          Dorette Sieber, freischaffender Coach für Mensch und Hund (Gründung MONDOCANI 2018), Flumenthal / Solothurn. Mobile Hundeschule in Solothurn, Derendingen, Umgebung Bern, Basel und Münchenstein.
        </p>
        <p>
          <strong>Urheber- &amp; Bildrechte:</strong><br>
          Sämtliche auf dieser Website gezeigten Fotografien, Hunde- und Naturaufnahmen, Porträts, Texte und Logos sind urheberrechtlich geschütztes Eigentum von MONDOCANI (Dorette Sieber).
        </p>
        <p>
          <strong>Datenschutz (Schweizer DSG):</strong><br>
          Alle Angaben aus der 3-Schritte Smart-Anfrage werden streng vertraulich behandelt, ausschliesslich zur Beantwortung Ihrer Anfrage und Terminvereinbarung durch Dorette Sieber verwendet und niemals an unbefugte Dritte weitergegeben.
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
      if (cEl && category) cEl.textContent = 'Themen- & Angebotsbereich: ' + category;
      if (pEl && person) pEl.textContent = 'Persönliche Begleitung: ' + person;
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
        ? 'Hundeplatz 4552 Derendingen'
        : (susiCalcState.mode === 'leitung' ? '15-Min.-Telefonat / Zoom' : 'Hausbesuch & Spaziergang');
      if (mEl) mEl.textContent = modeLabel;

      if (susiCalcState.role === 'architektur') {
        badge.textContent = 'SPEZIALBEGLEITUNG: STRASSENHUNDE, TIERSCHUTZ & UNSICHERHEIT';
        head.textContent = 'Einfühlsame Begleitung für Strassenhunde und unsichere Hunde';
        desc.textContent = 'Hunde mit bewegter Vorgeschichte brauchen Ruhe, Verlässlichkeit und feine Körpersprache statt Druck. Gemeinsam bauen wir Vertrauen und Sicherheit im neuen Lebensraum auf.';
        lEl.textContent = 'CHF 80.— / Std.';
        pEl.textContent = 'Hausbesuch & Ruhetraining';
        sEl.textContent = '1.5–2 Std. Ersttermin';
        if (cta) cta.href = 'kontakt.html?thema=einzelcoaching';
      } else if (susiCalcState.role === 'bau') {
        badge.textContent = 'PERSÖNLICHKEITS-COACHING: HUNDEGESTÜTZTES COACHING';
        head.textContent = 'Hundegestütztes Coaching: Ehrlich, achtsam und berührend';
        desc.textContent = 'Mit Ihrem eigenen Hund oder mit meinem Hund als Co-Coach spiegeln wir Körpersprache, Grenzen und unbewusste Muster für mehr Selbstwert, Präsenz und natürliche Führungskraft.';
        lEl.textContent = 'Individuell nach Thema';
        pEl.textContent = 'Mit eigenem / Co-Coach-Hund';
        sEl.textContent = '15 Min. Vorgespräch gratis';
        if (cta) cta.href = 'kontakt.html?thema=hundecoaching';
      } else {
        if (susiCalcState.scope === 'innen') {
          badge.textContent = 'JEDEN FREITAGNACHMITTAG · SPORTSTRASSE 4552 DERENDINGEN';
          head.textContent = 'Rudeltreffen & Wiesenstunde in kleinen Gruppen (Freitag)';
          desc.textContent = 'Gemeinsamer Spaziergang in der Natur und anschliessend freie Begegnung auf dem grossen eingezäunten Platz neben dem Fussballplatz in Derendingen (14:00–15:30 Uhr & 16:00–17:30 Uhr).';
          lEl.textContent = 'CHF 40.— / 1.5 Std.';
          pEl.textContent = 'Club Deutsche Doggen Derendingen';
          sEl.textContent = 'Es hat freie Plätze';
          if (cta) cta.href = 'kontakt.html?thema=rudeltreffen';
        } else if (susiCalcState.scope === 'aussen') {
          badge.textContent = 'KENNENLERNEN & VERTIEFUNG · ERLEBNISVORTRAG & WORKSHOPS';
          head.textContent = 'Erlebnisvortrag (Freitag ab 16:00 Uhr) & Rudel-Workshops';
          desc.textContent = 'Spüren Sie in Ruhe, ob meine Arbeitsweise zu Ihnen und Ihrem Hund passt, oder tauchen Sie in einem 3–4-stündigen Workshop (CHF 80.— pro Team) tief in die Sprache der Hunde ein.';
          lEl.textContent = 'Workshop CHF 80.—';
          pEl.textContent = 'Eingezäunter Platz mit Unterstand';
          sEl.textContent = 'Freitag ab 16:00 Uhr';
          if (cta) cta.href = 'kontakt.html?thema=kennenlernen';
        } else {
          badge.textContent = 'EMPFEHLUNG: INDIVIDUELLES EINZELCOACHING & HAUSBESUCH';
          head.textContent = 'Einzelcoaching für eine ruhige, vertrauensvolle Mensch-Hund-Beziehung';
          desc.textContent = 'Beim ersten Treffen (ca. 1.5 bis 2 Stunden) besucht Dorette Sieber Sie gerne zu Hause, um Ihre Wohn- und Alltagssituation kennenzulernen. Anschliessend beobachten wir Ihr Zusammenspiel auf einem entspannten Spaziergang.';
          lEl.textContent = 'CHF 80.— / Std.';
          pEl.textContent = 'Solothurn, Bern & Basel';
          sEl.textContent = '15 Min. kostenlos';
          if (cta) cta.href = 'kontakt.html?thema=einzelcoaching';
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
  <meta name="description" content="MONDOCANI – Die mobile Hundeschule in Solothurn, Flumenthal, Derendingen, Bern und Basel: Ganzheitliche Mensch-Hund-Begleitung, Einzelcoaching, Rudeltreffen und hundegestütztes Coaching mit Dorette Sieber.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "MONDOCANI · Die mobile Hundeschule",
    "url": "https://mondocani.ch",
    "telephone": "+41 79 446 70 43",
    "email": "mail@mondocani.ch",
    "founder": "Dorette Sieber",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Sportstrasse (Trainingsplatz Derendingen) · Sitz Flumenthal",
      "postalCode": "4552",
      "addressLocality": "Derendingen / Solothurn",
      "addressRegion": "SO",
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
        <span class="top-bar-badge" data-slot="topbar_badge">MONDOCANI · MOBILE HUNDESCHULE</span>
        <span data-slot="topbar_sub">Dorette Sieber · Solothurn, 4552 Derendingen, Bern &amp; Basel</span>
      </div>
      <div class="top-bar-links">
        <a href="tel:+41794467043">{SVG_PHONE} <span>079 446 70 43</span></a>
        <a href="mailto:mail@mondocani.ch">{SVG_MAIL} <span>mail@mondocani.ch</span></a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER -->
  <header class="site-header" data-section="header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="MONDOCANI Mobile Hundeschule Solothurn Startseite">
        <img src="images/logo-mondocani.png" alt="MONDOCANI Logo" class="brand-logo" width="50" height="50" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">MONDOCANI</span>
          <span class="brand-sub" data-slot="brand_sub">Mobile Hundeschule · Solothurn</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}" data-nav-href="index.html">Startseite</a>
        <a href="leistungen.html" class="nav-link {nav_leistungen}" data-nav-href="leistungen.html">Angebot</a>
        <a href="referenzen.html" class="nav-link {nav_referenzen}" data-nav-href="referenzen.html">Einblicke</a>
        <a href="ueber-uns.html" class="nav-link {nav_ueber}" data-nav-href="ueber-uns.html">Über mich</a>
        <a href="kontakt.html" class="nav-link {nav_kontakt}" data-nav-href="kontakt.html">Kontakt</a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" data-slot="header_cta">
          <span>Gespräch anfragen</span>
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
    <a href="leistungen.html" onclick="wpCloseMobileMenu()">Angebot (Einzelcoaching, Rudeltreffen, Hundegestütztes Coaching &amp; Vortrag)</a>
    <a href="referenzen.html" onclick="wpCloseMobileMenu()">Kundenstimmen, Praxis-Einblicke &amp; Galerie</a>
    <a href="ueber-uns.html" onclick="wpCloseMobileMenu()">Über Dorette Sieber, Philosophie &amp; Lebensweg</a>
    <a href="kontakt.html" onclick="wpCloseMobileMenu()">3-Schritte Smart-Anfrage &amp; Standorte</a>
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
            <img src="images/logo-mondocani.png" alt="MONDOCANI Mobile Hundeschule" width="54" height="54" style="border-radius:4px;" loading="lazy" decoding="async">
            <div>
              <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#1E140A;">MONDOCANI</div>
              <div style="font-size:0.78rem;color:#8C5500;font-weight:700;">Dorette Sieber · Mobile Hundeschule</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#3A2918;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Verstehe deinen Hund. Erkenne dich selbst. Ganzheitliche Mensch-Hund-Begleitung in Solothurn, Flumenthal, Derendingen, Umgebung Bern, Basel und Münchenstein.
          </p>
          <div style="font-size:0.84rem;color:#1E140A;font-weight:600;">
            Flumenthal / Solothurn · Hundeplatz: Sportstrasse, 4552 Derendingen
          </div>
        </div>

        <div>
          <div class="footer-title">Angebot &amp; Begleitung</div>
          <ul class="footer-list">
            <li><a href="leistungen.html#einzelcoaching">Einzelcoaching &amp; Hausbesuch (CHF 80.— / Std.)</a></li>
            <li><a href="leistungen.html#rudeltreffen">Freitags-Rudeltreffen Derendingen (CHF 40.—)</a></li>
            <li><a href="leistungen.html#hundecoaching">Hundegestütztes Coaching (Co-Coach)</a></li>
            <li><a href="leistungen.html#workshops">Workshops &amp; Erlebnisvortrag</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Einblicke &amp; Philosophie</div>
          <ul class="footer-list">
            <li><a href="index.html#projektberater">Interaktiver Begleitungs-Finder</a></li>
            <li><a href="referenzen.html">Kundenstimmen &amp; Erfahrungsberichte</a></li>
            <li><a href="referenzen.html#impulse">Blog-Impulse &amp; Galerie</a></li>
            <li><a href="ueber-uns.html">Über Dorette Sieber &amp; Vita</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; Rechtliches</div>
          <ul class="footer-list">
            <li><a href="tel:+41794467043">Telefon: 079 446 70 43</a></li>
            <li><a href="mailto:mail@mondocani.ch">E-Mail: mail@mondocani.ch</a></li>
            <li><a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">15-Min.-Erstgespräch &amp; Smart-Anfrage</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 MONDOCANI · Die mobile Hundeschule (Dorette Sieber, Flumenthal / Solothurn). Alle Rechte vorbehalten.</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
          <a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">Termin anfragen</a>
          <a href="referenzen.html" style="color:#3A2918;">Kundenstimmen</a>
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
  <meta name="description" content="MONDOCANI – Die mobile Hundeschule in Solothurn & Derendingen (Zeigeversion): Ganzheitliche Mensch-Hund-Begleitung, Einzelcoaching, Rudeltreffen und hundegestütztes Coaching mit Dorette Sieber.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "MONDOCANI · Die mobile Hundeschule",
    "url": "https://mondocani.ch",
    "telephone": "+41 79 446 70 43",
    "email": "mail@mondocani.ch",
    "founder": "Dorette Sieber",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Sportstrasse (Trainingsplatz Derendingen) · Sitz Flumenthal",
      "postalCode": "4552",
      "addressLocality": "Derendingen / Solothurn",
      "addressRegion": "SO",
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
      <a href="index.html" class="brand-link" aria-label="MONDOCANI Mobile Hundeschule Solothurn Startseite">
        <img src="images/logo-mondocani.png" alt="MONDOCANI Logo" class="brand-logo" width="50" height="50" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">MONDOCANI</span>
          <span class="brand-sub" data-slot="brand_sub">Mobile Hundeschule · Solothurn</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}" data-nav-href="index.html">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#15803D"/></svg>
          <span>Startseite</span>
        </a>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="leistungen.html" onclick="wpOpenBlueprintModal('Alle 6 Angebote, Preise &amp; Freitags-Rudeltreffen im Detail', 'Einzelcoaching (CHF 80.—/Std.), Rudeltreffen Derendingen (CHF 40.—/1.5 Std.), Hundegestütztes Coaching, Workshops &amp; Erlebnisvortrag', 'Dorette Sieber')">
          <span>Angebot</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="referenzen.html" onclick="wpOpenBlueprintModal('Kundenstimmen, Erfahrungsberichte, Blog-Impulse &amp; Fotogalerie', 'Rückmeldungen von Doris &amp; Claude mit Milu, Ute mit Foxy &amp; Róisín sowie Blog-Beiträge (Tajuya, Strassenhunde, Welpen)', 'Dorette Sieber')">
          <span>Einblicke</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="ueber-uns.html" onclick="wpOpenBlueprintModal('Über Dorette Sieber, Lebensweg &amp; Ausbildungen', 'Seit 2018 MONDOCANI · Wegbereiterin nach Maja Nowak · Tierkommunikation Sybille Lüthi · Älplerin &amp; La Palma (Tajuya)', 'Dorette Sieber')">
          <span>Über mich</span>
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
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu();wpOpenBlueprintModal('Alle 6 Angebote, Preise &amp; Freitags-Rudeltreffen im Detail', 'Einzelcoaching, Rudeltreffen Derendingen, Hundegestütztes Coaching &amp; Workshops', 'Dorette Sieber')">
      <span>Angebot</span>
      <span class="preview-status-badge">Folgt beim Ausbau</span>
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu();wpOpenBlueprintModal('Kundenstimmen, Erfahrungsberichte, Blog-Impulse &amp; Fotogalerie', 'Alle echten Rückmeldungen, Geschichten &amp; Naturbilder von MONDOCANI', 'Dorette Sieber')">
      <span>Einblicke</span>
      <span class="preview-status-badge">Folgt beim Ausbau</span>
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu();wpOpenBlueprintModal('Über Dorette Sieber, Lebensweg &amp; Ausbildungen', 'Porträt, Vita seit 2018, Ausbildungen bei Maja Nowak &amp; Sybille Lüthi', 'Dorette Sieber')">
      <span>Über mich</span>
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
            <img src="images/logo-mondocani.png" alt="MONDOCANI Mobile Hundeschule" width="54" height="54" style="border-radius:4px;" loading="lazy" decoding="async">
            <div>
              <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#1E140A;">MONDOCANI</div>
              <div style="font-size:0.78rem;color:#8C5500;font-weight:700;">Dorette Sieber · Mobile Hundeschule</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#3A2918;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Verstehe deinen Hund. Erkenne dich selbst. Ganzheitliche Mensch-Hund-Begleitung in Solothurn, Flumenthal, Derendingen, Umgebung Bern, Basel und Münchenstein.
          </p>
          <div style="font-size:0.84rem;color:#1E140A;font-weight:600;">
            Flumenthal / Solothurn · Hundeplatz: Sportstrasse, 4552 Derendingen
          </div>
        </div>

        <div>
          <div class="footer-title">Bereits in dieser Vorschau live</div>
          <ul class="footer-list">
            <li><a href="index.html">Startseite mit allen 6 Angeboten &amp; Philosophie</a></li>
            <li><a href="index.html#projektberater">Interaktiver Mensch-Hund-Begleitungs-Finder</a></li>
            <li><a href="kontakt.html">3-Schritte Smart-Anfrage (inkl. PDF-Dossier)</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Weitere Detailseiten (Ausbau)</div>
          <ul class="footer-list">
            <li><button type="button" onclick="wpOpenBlueprintModal('Alle 6 Angebote, Preise &amp; Freitags-Rudeltreffen', 'Einzelcoaching (CHF 80.—/Std.), Rudeltreffen (CHF 40.—/1.5 Std.), Hundegestütztes Coaching &amp; Workshops', 'Dorette Sieber')">Angebot im Detail (Vorschau)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Kundenstimmen, Blog-Impulse &amp; Galerie', 'Erfahrungsberichte (Milu, Foxy &amp; Róisín), Blog-Beiträge &amp; Naturgalerie', 'Dorette Sieber')">Einblicke &amp; Stimmen (Vorschau)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Über Dorette Sieber &amp; Vita', 'Persönlicher Weg, Maja Nowak, Sybille Lüthi, La Palma &amp; Alpen', 'Dorette Sieber')">Über Dorette Sieber (Vorschau)</button></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; Rechtliches</div>
          <ul class="footer-list">
            <li><a href="tel:+41794467043">Telefon: 079 446 70 43</a></li>
            <li><a href="mailto:mail@mondocani.ch">E-Mail: mail@mondocani.ch</a></li>
            <li><a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">3-Schritte Smart-Anfrage starten</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 MONDOCANI · Die mobile Hundeschule (Dorette Sieber) · Unverbindlicher Vorschau-Entwurf (Zeigeversion).</div>
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
      <div class="section-kicker">UNVERBINDLICHER VORSCHAU-ENTWURF FÜR MONDOCANI.CH</div>
      <h3 id="wpBpTitle" style="font-size:1.36rem;font-weight:700;margin-bottom:8px;">Unverbindlicher Vorschau-Entwurf für MONDOCANI</h3>
      <p id="wpBpSub" style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
        In dieser <strong>Zeigeversion (2 Beispiel-Seiten ausgearbeitet)</strong> sehen Sie Ihre neue Startseite mit allen 6 Angeboten, Ihrer Philosophie «Beziehung statt Erziehung», dem interaktiven Mensch-Hund-Begleitungs-Finder sowie den live funktionierenden 3-Schritte Smart-Anfrage-Assistenten. Dieser vertiefte Themenbereich wird beim gemeinsamen Ausbau schlüsselfertig mit allen Originaltexten und Bildern freigeschaltet.
      </p>
      <div style="background-color:var(--gold-soft);border-left:4px solid var(--gold);padding:12px 14px;border-radius:var(--radius-sm);font-size:0.86rem;margin-bottom:14px;">
        <div style="font-weight:700;color:var(--charcoal-deep);" id="wpBpCategory">Themen- &amp; Angebotsbereich: Vorbereitet für den gemeinsamen Ausbau</div>
        <div style="color:var(--text-body);margin-top:2px;" id="wpBpContact">Persönliche Begleitung MONDOCANI: Dorette Sieber</div>
      </div>

      <div class="wp-modal-checklist">
        <div style="font-family:'Lexend',sans-serif;font-size:0.8rem;font-weight:700;text-transform:uppercase;color:var(--charcoal-deep);">
          Was beim gemeinsamen Ausbau in diesem Themenbereich enthalten ist:
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Vollständige Angebotsseite mit Einzelcoaching (CHF 80.—/Std.), Freitags-Rudeltreffen in Derendingen (CHF 40.—/1.5 Std.), hundegestütztem Coaching, Workshops und Erlebnisvortrag</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Eigene Einblicke- &amp; Referenzenseite mit allen ungekürzten Kundenstimmen (Milu, Foxy &amp; Róisín), der Bildergalerie sowie den Blog-Beiträgen (Tajuya, Strassenhunde, Welpen)</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Persönliche Porträtseite über Dorette Sieber, ihren Lebensweg von den Schweizer Alpen und La Palma bis Solothurn sowie ihre Ausbildungen (u. a. Maja Nowak &amp; Sybille Lüthi)</span>
        </div>
      </div>

      <div style="display:flex;gap:10px;flex-wrap:wrap;justify-content:flex-end;">
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
        <div class="section-kicker kicker-light" data-slot="hero_kicker">MENSCH-HUND-BEGLEITUNG · SOLOTHURN, DERENDINGEN, BERN &amp; BASEL</div>
        <h1 class="hero-title" data-slot="hero_title">
          Verstehe deinen Hund. <span>Erkenne dich selbst.</span>
        </h1>
        <p class="hero-lead" data-slot="hero_lead">
          Hunde sind feinfühlige Wegbegleiter und ehrliche Spiegel. Bei MONDOCANI begleitet Dorette Sieber Sie und Ihren Hund auf dem Weg zu einer ruhigen, vertrauensvollen Verbindung: ohne Leckerli-Dressur, ohne Druck, sondern in echter Beziehung auf Augenhöhe.
        </p>

        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
            <span>Erstgespräch &amp; Termin anfragen</span>
            {SVG_ARROW}
          </a>
          <a href="#projektberater" class="btn-cta btn-cta-outline-light" data-slot="hero_cta_secondary">
            <span>Begleitungs-Finder starten</span>
          </a>
        </div>

        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Beziehung statt Erziehung</span>
            <span class="hero-badge-lbl">Kontakt statt Kontrolle: Ruhe, Klarheit und feinsprachliche Führung ohne Dressur</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Einzelcoaching &amp; Hausbesuch</span>
            <span class="hero-badge-lbl">Individuelle Begleitung bei Ihnen zu Hause und unterwegs (CHF 80.— / Std.)</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Freitags-Rudeltreffen</span>
            <span class="hero-badge-lbl">Spaziergang &amp; eingezäunter Platz in 4552 Derendingen (CHF 40.— / 1.5 Std.)</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Seit 2018 · Dorette Sieber</span>
            <span class="hero-badge-lbl">Wegbereiterin Mensch-Hund-Kommunikation (nach Maja Nowak) &amp; Tierkommunikation</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/hero-mensch-hund-bindung.jpg" alt="Dorette Sieber, MONDOCANI Mobile Hundeschule in Solothurn und Derendingen" width="600" height="390" data-slot="hero_image">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#1E140A;">Dorette Sieber · MONDOCANI</div>
            <div style="font-size:0.8rem;color:#3A2918;">Mobile Hundeschule in Solothurn, Derendingen, Bern &amp; Basel</div>
          </div>
          <span class="top-bar-badge">AUF AUGENHÖHE</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 3 KERNWEGE (BEZIEHUNG, RUDEL, PERSÖNLICHES WACHSTUM) -->
  <section data-section="zielgruppen" id="zielgruppen" style="background-color:var(--bg-Warm);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="audiences_kicker">ECHTE VERBINDUNG · NATÜRLICHE KOMMUNIKATION · BEWUSSTES MITEINANDER</div>
        <h2 class="section-title" data-slot="audiences_title">Drei Zugänge für eine tiefe Mensch-Hund-Bindung</h2>
        <p class="section-desc" data-slot="audiences_desc">
          Ob Sie das Verhalten Ihres Hundes im Alltag verstehen möchten, den sozialen Austausch im Rudel suchen oder persönlich durch die ehrliche Rückmeldung eines Hundes wachsen wollen:
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">1. Einzelcoaching</span>
              <span class="icon-box">{SVG_HOME}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Mensch und Hund im Alltag</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Den Hund nicht nach starren Vorstellungen formen, sondern sein Wesen verstehen: Wir betrachten Ihre Wohn- und Alltagssituation zu Hause und üben auf gemeinsamen Spaziergängen eine ruhige, klare Führung.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Erster Termin gerne als Hausbesuch (ca. 1.5 bis 2 Stunden)</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>CHF 80.— pro Stunde:</strong> Für Welpen, Junghunde, erwachsene Hunde &amp; Strassenhunde</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=einzelcoaching" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Einzelcoaching anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">2. Gruppentreffen</span>
              <span class="icon-box">{SVG_USERS}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Rudeltreffen &amp; Wiesenstunde</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Jeden Freitagnachmittag (14:00–15:30 Uhr und 16:00–17:30 Uhr) geniessen wir in kleinen Gruppen einen Spaziergang in der Natur und beobachten die Hunde danach frei auf dem grossen eingezäunten Platz in Derendingen.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Treffpunkt: Club für Deutsche Doggen, Sportstrasse, 4552 Derendingen</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>CHF 40.— pro 1.5 Stunden:</strong> Es hat aktuell noch freie Plätze</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=rudeltreffen" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Platz im Rudeltreffen sichern</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">3. Hundegestütztes Coaching</span>
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Persönlich wachsen mit Hund</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Hunde spiegeln unsere Körpersprache, Emotionen und unbewussten Muster völlig wertfrei. Mit Ihrem eigenen Hund oder meinem Hund als Co-Coach stärken Sie Selbstwert, Präsenz und gesunde Abgrenzung.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Klarer kommunizieren, Grenzen setzen und souverän führen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Für Beruf, Beziehung, emotionale Balance und Neuorientierung</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=hundecoaching" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Hundegestütztes Coaching klären</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 6 KERNANGEBOTE (3x2 SYMMETRISCHES RASTER) -->
  <section data-section="kernangebote" id="kernangebote">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="pillars_kicker">ANGEBOTSÜBERSICHT · MONDOCANI MOBILE HUNDESCHULE SOLOTHURN</div>
        <h2 class="section-title" data-slot="pillars_title">Sechs Begleitungsformen für ein harmonisches Miteinander</h2>
        <p class="section-desc" data-slot="pillars_desc">
          Ob junger Welpe, übernommener Strassenhund mit Vorgeschichte, wöchentliches Rudeltreffen oder persönliche Standortbestimmung: Jede Begleitung richtet sich nach dem, was sich in Ihrer Beziehung zeigt.
        </p>
      </div>

      <div class="grid-3">
        <!-- 1. Einzelcoaching -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-einzelcoaching-kontakt.jpg" alt="Individuelles Einzelcoaching und Hausbesuch bei MONDOCANI Solothurn" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">CHF 80.— / Std.</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Hausbesuch &amp; Alltag</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Individuelles Einzelcoaching</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Persönliche 1:1-Begleitung bei Ihnen zu Hause und auf Ihren gewohnten Spazierwegen: Ruhe, Klarheit und respektvolle Beziehungsverhandlungen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Erster Termin (1.5–2 Std.) inkl. Wohn- und Alltagssituation</span></div>
                <div class="check-item">{SVG_CHECK} <span>Artgerechtes Führen ohne Kommandos oder Leckerli-Manipulation</span></div>
              </div>
            </div>
            <a href="leistungen.html#einzelcoaching" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zum Einzelcoaching</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 2. Rudeltreffen -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-gruppentreffen-rudel-derendingen.jpg" alt="Freitags-Rudeltreffen und Wiesenstunde in 4552 Derendingen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">CHF 40.— / 1.5 Std.</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Jeden Freitag</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Rudeltreffen &amp; Wiesenstunden</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Spaziergänge in kleinen Gruppen und anschliessend freie Rudelbegegnung auf dem grossen eingezäunten Platz an der Sportstrasse in 4552 Derendingen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Freitag 14:00–15:30 Uhr sowie 16:00–17:30 Uhr (freie Plätze)</span></div>
                <div class="check-item">{SVG_CHECK} <span>Sprache der Hunde verstehen, Ruhe beim Gassigehen &amp; Austausch</span></div>
              </div>
            </div>
            <a href="leistungen.html#rudeltreffen" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zum Rudeltreffen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 3. Hundegestütztes Coaching -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-hundegestuetztes-coaching-reflexion.jpg" alt="Hundegestütztes Coaching bei MONDOCANI Dorette Sieber" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Co-Coach Hund</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Persönliches Wachstum</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Hundegestütztes Coaching</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Ehrlich, achtsam und berührend: Im geschützten Reflexionsraum mit eigenem Hund oder Co-Coach-Hund persönliche Blockaden lösen und Präsenz stärken.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Selbstbewusstsein, emotionale Balance &amp; Stressbewältigung</span></div>
                <div class="check-item">{SVG_CHECK} <span>Souverän und wertschätzend führen sowie klar Grenzen setzen</span></div>
              </div>
            </div>
            <a href="leistungen.html#hundecoaching" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zum Coaching</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 4. Workshops & Seminare -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-hundegestuetztes-coaching-natur.jpg" alt="Workshops und Seminare zur Mensch-Hund-Beziehung in Derendingen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">CHF 80.— / Team</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">3–4 Stunden</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Workshops &amp; Tagesseminare</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Gemeinsames Erleben und Beobachten auf dem eingezäunten Platz mit Unterstand in Derendingen: Wo braucht Ihr Hund Führung und wo mehr Freiraum?
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Prozesse, Aufgaben und natürliche Ressourcen im Rudel erkennen</span></div>
                <div class="check-item">{SVG_CHECK} <span>Der eigenen Wahrnehmung vertrauen und Konflikte ruhig lösen</span></div>
              </div>
            </div>
            <a href="leistungen.html#workshops" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zu Workshops</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 5. Strassenhunde & Welpen -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-einzelcoaching-ruhe-vertrauen.jpg" alt="Strassenhunde und Welpen begleiten bei MONDOCANI" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Spezialbegleitung</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Welpen &amp; Tierschutz</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Welpen &amp; Strassenhunde</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Ob Beratung vor dem Hundekauf, friedvoller Start mit einem Welpen oder einfühlsame Begleitung für traumatisierte Tierschutz- und Strassenhunde.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Überwindung von Unsicherheiten, Ängsten und Leinenstress</span></div>
                <div class="check-item">{SVG_CHECK} <span>Einbezug aller Familienmitglieder für einen klaren Alltag</span></div>
              </div>
            </div>
            <a href="leistungen.html#einzelcoaching" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Begleitung ansehen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 6. Erlebnisvortrag & Kennenlernen -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-erlebnisvortrag-kennenlernen.jpg" alt="MONDOCANI kennenlernen und Erlebnisvortrag in Derendingen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Unverbindlich</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Freitag ab 16:00 Uhr</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Erlebnisvortrag &amp; Erstgespräch</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Möchten Sie in Ruhe spüren, ob meine Art und Weise zu Ihnen und Ihrem Hund passt, bevor Sie sich für ein Coaching oder Rudeltreffen entscheiden?
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Erlebnisvortrag für Interessierte (Freitag ab 16:00 Uhr, Derendingen)</span></div>
                <div class="check-item">{SVG_CHECK} <span>Kostenlose 15-minütige Beratung per Telefon oder Zoom</span></div>
              </div>
            </div>
            <a href="kontakt.html?thema=kennenlernen" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Kennenlernen vereinbaren</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

{render_mondocani_advisor()}

  <!-- KUNDENSTIMMEN & PRAXIS-EINBLICKE -->
  <section data-section="referenzen-auszug" id="referenzen">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="refs_kicker">EURE RÜCKMELDUNGEN &amp; PRAXIS-SCHWERPUNKTE · ECHTE VERÄNDERUNG</div>
        <h2 class="section-title" data-slot="refs_title">Was Mensch-Hund-Teams bei MONDOCANI erleben</h2>
        <p class="section-desc" data-slot="refs_desc">
          Wenn Druck und Leckerli-Manipulation wegfallen und an ihre Stelle Ruhe, Präsenz und gegenseitiges Verstehen treten, verändert sich der Alltag oft schon nach kurzer Zeit spürbar:
        </p>
      </div>

      {render_references_grid(limit=6, is_v2=False)}

      <div style="margin-top:34px;display:flex;justify-content:center;">
        <a href="referenzen.html" class="btn-cta btn-cta-outline">
          <span>Alle Kundenstimmen, Blog-Impulse &amp; Galerie ansehen</span>
          {SVG_ARROW}
        </a>
      </div>
    </div>
  </section>

  <!-- ÜBER DORETTE SIEBER & PHILOSOPHIE -->
  <section data-section="ueber-susi-kurz" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="about_kicker">ÜBER MICH · DEINE WEGBEGLEITERIN FÜR MENSCH UND HUND</div>
        <h2 class="section-title" data-slot="about_title">Dorette Sieber &amp; die Philosophie von MONDOCANI</h2>
        <p class="section-desc" data-slot="about_desc">
          «Mich interessiert das, was zwischen den Zeilen steht. Das, was sichtbar wird, wenn ich mich einlasse, still werde und mich öffne.»
        </p>
      </div>

      <div class="grid-2">
        <div class="founder-card">
          <div class="founder-top">
            <img src="images/team-dorette-sieber-portrait.jpg" alt="Dorette Sieber, Inhaberin von MONDOCANI Mobile Hundeschule" class="founder-portrait" loading="lazy" decoding="async">
            <div>
              <span class="meta-badge" style="margin-bottom:8px;">Inhaberin &amp; Coach (seit 2018)</span>
              <h3 style="font-size:1.35rem;font-weight:700;margin-bottom:6px;">Dorette Sieber</h3>
              <p style="font-size:0.84rem;font-weight:700;color:var(--gold-dark);margin-bottom:8px;">
                Wegbereiterin Mensch-Hund-Kommunikation · Tierkommunikation · Mentalcoach
              </p>
              <p style="font-size:0.88rem;color:var(--text-body);line-height:1.58;">
                Schon nach meiner Geburt nahm Barry, ein Berner Sennenhund, Platz an meiner Seite. Viele Jahre arbeitete ich als Älplerin mit Hunden in den Schweizer Bergen, lebte auf La Palma mit meiner Podenco-Garafiano-Hündin Tajuya und engagierte mich in europäischen Hundeauffangstationen.
              </p>
            </div>
          </div>
          <div class="founder-body">
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Fundierte Ausbildungen:</strong> Wegbereiterin Mensch-Hund-Kommunikation nach Maja Nowak (Berlin) sowie Basis- und Vertiefungsausbildung in Tierkommunikation bei Sybille Lüthi (Thalwil).</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Ganzheitlicher Hintergrund:</strong> NLP/Mentalcoach BMC (Andreas Lüthi), Mal- und Gestaltungstherapeutin (Eva Brenner), Biographie- und Sozialarbeit.</span></div>
            </div>
            <a href="ueber-uns.html" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Porträt &amp; Lebensweg von Dorette Sieber lesen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Philosophie · Kontakt statt Kontrolle</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 style="font-size:1.28rem;font-weight:700;margin-bottom:10px;">13 Kernpunkte meiner Begleitung auf Augenhöhe</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:14px;">
              Hunde können unser Verhalten widerspiegeln und erzählen uns viel über uns selbst. Wir sind gleichbedeutende Wesen in einem eigenen Lernprozess. Im Dialog und Sich-Einfühlen schauen wir hin, wo die Bedürfnisse und Qualitäten von Hund und Mensch liegen:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Wer ist mein Hund:</strong> Angeborene Kompetenzen, Temperament und Bedürfnisse erkennen und der eigenen Wahrnehmung vertrauen.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Ruhe, Klarheit &amp; stressfreie Führung:</strong> Feinsprachlich kommunizieren, Bindung stärken, Unsicherheiten überwinden und alle Familienmitglieder einbeziehen.</span></div>
            </div>
          </div>
          <a href="ueber-uns.html#philosophie" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Unsere Philosophie im Detail</span>
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
        <div class="section-kicker" data-slot="faq_kicker">HÄUFIGE FRAGEN · ABLAUF, RUDELTREFFEN &amp; TARIFE</div>
        <h2 class="section-title" data-slot="faq_title">Antworten auf die wichtigsten Fragen vor dem Start</h2>
        <p class="section-desc" data-slot="faq_desc">
          Transparente Informationen rund um den ersten Hausbesuch, die Freitags-Rudeltreffen in Derendingen, das hundegestützte Coaching und unser mobiles Einzugsgebiet.
        </p>
      </div>

      {render_faqs_grid()}
    </div>
  </section>
"""

# ==============================================================================
# SEITEN-INHALTE: V1 ANGEBOT (leistungen.html)
# ==============================================================================
V1_LEISTUNGEN_BODY = f"""
  <section class="hero-section" data-section="hero-leistungen">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">ANGEBOT &amp; PREISE IM DETAIL · MONDOCANI SOLOTHURN &amp; DERENDINGEN</div>
        <h1 class="hero-title">
          Beziehung statt Erziehung: <span>Individuelle Begleitung</span> für Mensch und Hund.
        </h1>
        <p class="hero-lead">
          Ob persönliches Einzelcoaching bei Ihnen zu Hause, wöchentliches Freitags-Rudeltreffen auf dem eingezäunten Platz in Derendingen oder hundegestütztes Coaching für Ihre persönliche Weiterentwicklung: Entdecken Sie alle Angebote von MONDOCANI.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>Termin oder Erstgespräch anfragen</span>
            {SVG_ARROW}
          </a>
          <a href="referenzen.html" class="btn-cta btn-cta-outline-light">
            <span>Kundenstimmen lesen</span>
          </a>
        </div>
        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">CHF 80.— / Stunde</span>
            <span class="hero-badge-lbl">Individuelles Einzelcoaching inkl. Hausbesuch &amp; Alltagsspaziergang</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">CHF 40.— / 1.5 Std.</span>
            <span class="hero-badge-lbl">Rudeltreffen jeden Freitagnachmittag (14:00 &amp; 16:00 Uhr) in Derendingen</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">CHF 80.— / Team</span>
            <span class="hero-badge-lbl">Intensiv-Workshops &amp; Seminare (3–4 Std.) auf dem Hundeplatz Derendingen</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">15 Min. kostenlos</span>
            <span class="hero-badge-lbl">Unverbindliches Kennenlerngespräch per Telefon oder Zoom</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/ref-einzelcoaching-spaziergang.jpg" alt="Einzelcoaching und Spaziergang bei MONDOCANI Dorette Sieber" width="600" height="390">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#1E140A;">Ruhige, feinsprachliche Führung</div>
            <div style="font-size:0.8rem;color:#3A2918;">Ohne Kommandos, ohne Leckerlis und ohne Druck im Alltag</div>
          </div>
          <span class="top-bar-badge">6 ANGEBOTE</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 6 ANGEBOTE IM DETAIL -->
  <section data-section="leistungen-detail" id="einzelcoaching">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">ALLE 6 BEGLEITUNGSFORMEN IM ÜBERBLICK</div>
        <h2 class="section-title">Wege zu einer tiefen, vertrauensvollen Mensch-Hund-Verbindung</h2>
        <p class="section-desc">
          Jedes Mensch-Hund-Team bringt seine eigene Geschichte und sein eigenes Temperament mit. Wir gestalten die Begleitung genau nach Ihren aktuellen Bedürfnissen.
        </p>
      </div>

      <div class="grid-2">
        <!-- 1. Einzelcoaching -->
        <div class="content-card card-accent-top" id="einzelcoaching-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">01 · Einzelcoaching · CHF 80.— / Std.</span>
              <span class="icon-box">{SVG_HOME}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Einzelcoaching &amp; Hausbesuch</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Statt Dressur mit Belohnungsleckerlis bauen wir eine fundierte Beziehung auf. Für den ersten Termin (ca. 1.5 bis 2 Stunden) komme ich gerne zu Ihnen nach Hause, um Wohn-, Fütterungs- und Lebensbedingungen einzubeziehen, bevor wir gemeinsam spazieren gehen.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Bedürfnisse, Charakter und Unsicherheiten Ihres Hundes erkennen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Verhaltensauffälligkeiten und ihre wahren Ursachen im Alltag verstehen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Ruhige, feinsprachliche und klare innere Haltung für freiwillige Folge</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=einzelcoaching" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Einzelcoaching &amp; Hausbesuch anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- 2. Rudeltreffen -->
        <div class="content-card card-accent-top" id="rudeltreffen">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">02 · Gruppentreffen · CHF 40.— / 1.5 Std.</span>
              <span class="icon-box">{SVG_USERS}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Rudeltreffen &amp; Wiesenstunde (Freitag)</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              In einer kleinen Gruppe geniessen wir jeden Freitagnachmittag (14:00–15:30 Uhr und 16:00–17:30 Uhr) einen Spaziergang in der Natur und treffen uns danach auf dem grossen eingezäunten Platz in Derendingen.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Treffpunkt: Club für Deutsche Doggen, Sportstrasse, 4552 Derendingen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Freie Begegnung im Rudel, Ruhe beim Gassigehen &amp; Hundesprache lesen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Wertvoller Erfahrungsaustausch unter Hundehalterinnen und Hundehaltern</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=rudeltreffen" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Freien Platz für Freitag anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- 3. Hundegestütztes Coaching -->
        <div class="content-card card-accent-top" id="hundecoaching">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">03 · Persönliches Wachstum mit Hund</span>
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Hundegestütztes Coaching (Co-Coach)</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Hunde denken nicht erst nach, ob sie uns ihre Meinung sagen möchten: Sie spiegeln unsere Körpersprache, Emotionen und unbewussten Muster unmittelbar und wertfrei. Möglich mit Ihrem eigenen Hund oder meinem Hund.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Klarer kommunizieren, zielgerichteter handeln &amp; souverän führen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Selbstwert stärken, eigene Stärken nutzen und besser Grenzen setzen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Begleitung bei Stressbewältigung, Neuorientierung und Beziehungsfragen</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=hundecoaching" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Hundegestütztes Coaching anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- 4. Workshops & Seminare -->
        <div class="content-card card-accent-top" id="workshops">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">04 · Workshops · CHF 80.— / Team (3–4 Std.)</span>
              <span class="icon-box">{SVG_LAYERS}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Workshops &amp; Seminare in Derendingen</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Auf dem grossen eingezäunten Platz mit Unterstand und Sitzgelegenheit an der Sportstrasse in 4552 Derendingen beobachten wir intensiv, was sich die Hunde im Rudel untereinander anzubieten haben.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Erkennen, wo Ihr Hund Unterstützung und Führung oder mehr Freiraum braucht</span></div>
              <div class="check-item">{SVG_CHECK} <span>Prozesse, Aufgaben und Ressourcen unter Hunden verstehen lernen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Respektvolle Beziehungsverhandlungen und Vertrauen in die eigene Wahrnehmung</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=rudeltreffen" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Interesse für nächsten Workshop melden</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- 5. Welpen & Strassenhunde -->
        <div class="content-card card-accent-top" id="welpen-strassenhunde">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">05 · Welpen, Junghunde &amp; Tierschutz</span>
              <span class="icon-box">{SVG_SHIELD}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Welpen-Coaching &amp; Strassenhunde begleiten</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Ob Sie vor dem Kauf prüfen möchten, welcher Hund wirklich zu Ihrer Lebenssituation passt, einen Welpen friedvoll ins Leben begleiten oder einen traumatisierten Strassenhund aufgenommen haben:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Beratung vor der Anschaffung: Passt das Wesen des Hundes zu Ihrem Alltag?</span></div>
              <div class="check-item">{SVG_CHECK} <span>Einfühlsamer Vertrauensaufbau bei Ängsten, Unsicherheit und Vorgeschichte</span></div>
              <div class="check-item">{SVG_CHECK} <span>Einbezug aller Familienmitglieder für klare, liebevolle Strukturen</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=einzelcoaching" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Welpen- oder Strassenhund-Begleitung anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <!-- 6. Erlebnisvortrag & 15-Min.-Beratung -->
        <div class="content-card card-accent-top" id="erlebnisvortrag">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">06 · Unverbindliches Kennenlernen</span>
              <span class="icon-box">{SVG_COMPASS}</span>
            </div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:10px;">Erlebnisvortrag &amp; 15-Min.-Erstgespräch</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Lernen Sie meine Arbeitsweise offen, ehrlich und in aller Ruhe kennen, bevor Sie sich für ein Einzelcoaching oder das Rudeltreffen entscheiden.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Erlebnisvortrag für Interessierte: Freitag ab 16:00 Uhr in 4552 Derendingen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Kostenloses 15-minütiges Erstgespräch per Telefon (079 446 70 43) oder Zoom</span></div>
              <div class="check-item">{SVG_CHECK} <span>Mobiles Einsatzgebiet: Solothurn, Flumenthal, Derendingen, Bern, Basel &amp; Münchenstein</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=kennenlernen" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Kostenloses Erstgespräch vereinbaren</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>
"""

# ==============================================================================
# SEITEN-INHALTE: V1 EINBLICKE, REFERENZEN & IMPULSE (referenzen.html)
# ==============================================================================
def render_full_before_after_cards() -> str:
    cards = []
    for ref in BEFORE_INVENTORY["references"]:
        cards.append(f"""
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">{ref['category']}</span>
              <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">{ref.get('highlight', 'Praxis-Einblick')}</span>
            </div>
            <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:6px;">{ref['title']}</h3>
            <p style="font-size:0.84rem;font-weight:700;color:var(--gold-dark);margin-bottom:12px;">{ref['scope']}</p>
            <div class="form-grid-2" style="margin-bottom:14px;">
              <div style="border:1px solid var(--border-light);border-radius:var(--radius-sm);overflow:hidden;background-color:var(--bg-page);">
                <img src="{ref['before_img']}" alt="Begegnung & Beobachtung: {ref['title']}" style="width:100%;height:175px;object-fit:cover;" loading="lazy" decoding="async">
                <div style="padding:6px 10px;font-size:0.75rem;font-weight:700;color:var(--text-muted);background-color:#F8EEE5;">Hinschauen &amp; Verstehen</div>
              </div>
              <div style="border:1px solid var(--gold-border);border-radius:var(--radius-sm);overflow:hidden;background-color:var(--bg-page);">
                <img src="{ref['after_img']}" alt="Verbindung & Ruhe: {ref['title']}" style="width:100%;height:175px;object-fit:cover;" loading="lazy" decoding="async">
                <div style="padding:6px 10px;font-size:0.75rem;font-weight:700;color:var(--gold-dark);background-color:var(--gold-soft);">Verbindung &amp; Vertrauen</div>
              </div>
            </div>
            <p style="font-size:0.9rem;color:var(--text-body);line-height:1.6;">{ref['desc']}</p>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Eigenes Anliegen mit Dorette Sieber besprechen</span>
            {SVG_ARROW}
          </a>
        </div>""")
    return '<div class="grid-2">\n' + "\n".join(cards) + "\n      </div>"


V1_REFERENZEN_BODY = f"""
  <section class="hero-section" data-section="hero-referenzen">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">KUNDENSTIMMEN, BLOG-IMPULSE &amp; GALERIE · MONDOCANI SOLOTHURN</div>
        <h1 class="hero-title">
          Echte Rückmeldungen &amp; <span>glückliche Momente</span> mit Hund.
        </h1>
        <p class="hero-lead">
          Lesen Sie, wie Hundehalterinnen und Hundehalter die Begleitung durch Dorette Sieber erleben, und entdecken Sie ausgewählte Blog-Gedanken sowie Bilder aus der Welt von MONDOCANI.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>Eigene Anfrage starten</span>
            {SVG_ARROW}
          </a>
          <a href="#impulse" class="btn-cta btn-cta-outline-light">
            <span>Blog-Impulse &amp; Geschichten</span>
          </a>
        </div>
        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Echte Kundenstimmen</span>
            <span class="hero-badge-lbl">Authentische Erfahrungsberichte aus dem Einzelcoaching und Rudeltreffen</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Ohne Leckerli &amp; Druck</span>
            <span class="hero-badge-lbl">Feinsprachliche Verbindung statt Ziehen an der Leine oder Manipulation</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Blog &amp; Einsichten</span>
            <span class="hero-badge-lbl">Gedanken zu Hundesprache, Strassenhunden, Welpen und Hündin Tajuya</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Natur &amp; Begegnung</span>
            <span class="hero-badge-lbl">Einblicke aus Solothurn, Derendingen, den Alpen und La Palma</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/ref-galerie-rudel-harmonie-03.jpg" alt="Glückliche Momente im Rudel bei MONDOCANI Dorette Sieber" width="600" height="390">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#1E140A;">Vertrauen &amp; Ruhe im Rudel</div>
            <div style="font-size:0.8rem;color:#3A2918;">Wenn Mensch und Hund einander in ihrem Wesen wirklich sehen</div>
          </div>
          <span class="top-bar-badge">KUNDENSTIMMEN</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ALLE 6 KUNDENSTIMMEN & PRAXIS-SCHWERPUNKTE -->
  <section data-section="alle-referenzen">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">6 ERFAHRUNGSBERICHTE &amp; PRAXIS-EINBLICKE</div>
        <h2 class="section-title">Wie sich die Mensch-Hund-Beziehung im Alltag wandelt</h2>
        <p class="section-desc">
          Wenn der Mensch in seine eigene Ruhe kommt und die angeborene Wesensart seines Hundes erkennt, entsteht aus Unsicherheit oder Leinenziehen ein entspanntes Miteinander.
        </p>
      </div>

      {render_full_before_after_cards()}
    </div>
  </section>

  <!-- BLOG-IMPULSE & GESCHICHTEN VON DORETTE SIEBER -->
  <section data-section="partnernetzwerk" id="impulse" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">BEITRÄGE &amp; EINSICHTEN AUS DEM MONDOCANI BLOG</div>
        <h2 class="section-title">Sechs Impulse zum Verstehen der Hundesprache</h2>
        <p class="section-desc">
          Ausgewählte Gedanken und Beiträge von Dorette Sieber rund um das Lesen von Körpersprache, die Arbeit mit unterschiedlichen Hundepersönlichkeiten und ihre Hündin Tajuya:
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Erinnerung &amp; Dankbarkeit</span>
            <h3 style="font-size:1.15rem;font-weight:700;margin-bottom:6px;">Zum Gedenken an meine Hündin und Lehrerin Tajuya</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Auf der Insel La Palma begegnete ich meiner grossen Liebe, einer Podenco-Garafiano-Hündin. Viele Jahre durfte ich von ihrer Feinfühligkeit, Klarheit und ihrem freien Wesen lernen.
            </p>
          </div>
          <div style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Wegbegleiterin &amp; Lehrmeisterin</div>
        </div>

        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Körpersprache</span>
            <h3 style="font-size:1.15rem;font-weight:700;margin-bottom:6px;">Einsichten: Die Sprache deines Begleiters sprechen</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Hunde kommunizieren mit ihrem ganzen Körper und sind sehr schnell in ihren Botschaften. Sie lesen feine Interaktionen rascher als wir Menschen und laden uns zu echter Präsenz ein.
            </p>
          </div>
          <div style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Wahrnehmung &amp; Feinsprachlichkeit</div>
        </div>

        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Arbeitsweise</span>
            <h3 style="font-size:1.15rem;font-weight:700;margin-bottom:6px;">Wie ich als Wegbegleiterin mit Mensch und Hund arbeite</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Vom Zerren an der Leine bis zu traumatisierten Angsthunden: Ich nehme wahr, mit welchen Persönlichkeiten ich es zu tun habe, und gehe mental wie herzlich in Verbindung.
            </p>
          </div>
          <div style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Individuell für jedes Team</div>
        </div>

        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Tierschutz &amp; Vertrauen</span>
            <h3 style="font-size:1.15rem;font-weight:700;margin-bottom:6px;">Strassenhunde begleiten und verstehen lernen</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Die Beziehung zu einem Strassenhund verlangt Geduld, Klarheit und ein sicheres Fundament, damit der Hund in seiner neuen Welt ankommen und Vertrauen fassen kann.
            </p>
          </div>
          <div style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Sicherheit statt Überforderung</div>
        </div>

        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Von Anfang an</span>
            <h3 style="font-size:1.15rem;font-weight:700;margin-bottom:6px;">Welpen-Coaching für einen friedvollen Start</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Wer einen Welpen adoptiert, legt in den ersten Wochen den Grundstein. Gemeinsam bauen wir von Beginn an eine ruhige, vertrauensvolle Orientierung im Familienalltag auf.
            </p>
          </div>
          <div style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Orientierung &amp; Geborgenheit</div>
        </div>

        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Inspiration &amp; Poesie</span>
            <h3 style="font-size:1.15rem;font-weight:700;margin-bottom:6px;">Lebendig sein &amp; «Drei Hunde» (Khalil Gibran)</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Philosophische Geschichten und Naturbeobachtungen, die uns daran erinnern, wie eng Achtsamkeit, innere Stille und unsere Beziehung zu Tieren miteinander verwoben sind.
            </p>
          </div>
          <div style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Achtsamkeit im Alltag</div>
        </div>
      </div>
    </div>
  </section>
"""

# ==============================================================================
# SEITEN-INHALTE: V1 ÜBER MICH (ueber-uns.html)
# ==============================================================================
V1_UEBER_UNS_BODY = f"""
  <section class="hero-section" data-section="hero-ueber">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">ÜBER DORETTE SIEBER · INHABERIN MONDOCANI SOLOTHURN</div>
        <h1 class="hero-title">
          Ein Leben an der Seite der Hunde: <span>intuitiv, klar und herzlich.</span>
        </h1>
        <p class="hero-lead">
          «Bereits nach meiner Geburt nahm Barry, ein Berner Sennenhund, Platz an meiner Seite. Ich möchte, dass der Hund seine Wesensart behalten darf und der Mensch sich dabei wohl und sicher fühlt.»
        </p>
        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>Persönlich Kontakt aufnehmen</span>
            {SVG_ARROW}
          </a>
          <a href="#philosophie" class="btn-cta btn-cta-outline-light">
            <span>Philosophie &amp; Ausbildungen</span>
          </a>
        </div>
        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Gründung 2018</span>
            <span class="hero-badge-lbl">Freischaffend als Coach für Mensch und Hund mit MONDOCANI in Solothurn</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Maja Nowak &amp; Sybille Lüthi</span>
            <span class="hero-badge-lbl">Wegbereiterin Mensch-Hund-Kommunikation &amp; vertiefte Tierkommunikation</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Alpen, La Palma &amp; Tierschutz</span>
            <span class="hero-badge-lbl">Jahre als Älplerin mit Hunden, freilebende Rudel &amp; Auffangstationen in Europa</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Pädagogik &amp; Therapie</span>
            <span class="hero-badge-lbl">NLP/Mentalcoach BMC, Mal- &amp; Gestaltungstherapie, Biographie- &amp; Sozialarbeit</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/team-dorette-sieber-begegnung.jpg" alt="Dorette Sieber im vertrauensvollen Kontakt mit Hund" width="600" height="390">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#1E140A;">Dorette Sieber</div>
            <div style="font-size:0.8rem;color:#3A2918;">Coach für Mensch &amp; Hund · Flumenthal / Solothurn</div>
          </div>
          <span class="top-bar-badge">SEIT 2018</span>
        </div>
      </div>
    </div>
  </section>

  <!-- LEBENSWEG & AUSBILDUNGEN (VITA) -->
  <section data-section="werdegang">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">MEIN LEBENSWEG &amp; MEINE VITA</div>
        <h2 class="section-title">Von den Schweizer Bergen und La Palma nach Solothurn</h2>
        <p class="section-desc">
          Schon als Kind lernte ich von der Natur, den Steinen, den Pflanzen und den Tieren: hinzuschauen, still zu werden und das wahre Wesen hinter dem Verhalten wahrzunehmen.
        </p>
      </div>

      <div class="grid-2">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Berufung &amp; Erfahrung</span>
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:10px;">Prägende Stationen mit Hunden und Menschen</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Als Kind spazierte ich mit dem Hund des Dorfarztes, später hatte ich meinen ersten eigenen Hund in Zürich, bildete eine Herdenhündin aus und arbeitete viele Jahre als <strong>Älplerin mit Hunden in den Schweizer Bergen</strong>.
            </p>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Auf der Insel <strong>La Palma</strong>, wo ich eine Zeit lang lebte, traf ich meine grosse Liebe, die <strong>Podenco-Garafiano-Hündin Tajuya</strong>, von der ich über viele Jahre tiefgreifend lernen durfte. Dazu kamen intensive Erfahrungen mit freilebenden Hunderudeln und in Tierschutz-Stationen:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Hundeauffangstationen &amp; Tierheime:</strong> Mitarbeit in Spanien, Italien und Frankreich sowie Beobachtung freilebender Hunderudel</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Mensch-Hund-Kommunikation:</strong> Wegbereiterin nach Maja Nowak (Berlin) sowie Tierkommunikation bei Sybille Lüthi (Thalwil)</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Seit 2018 MONDOCANI:</strong> Freischaffende Begleitung für Mensch und Hund im Raum Solothurn, Derendingen, Bern und Basel</span></div>
            </div>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Persönliches Gespräch mit Dorette Sieber vereinbaren</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Aus- &amp; Weiterbildungen</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:10px;">Fachliche Vita in Hundekommunikation, Coaching &amp; Sozialarbeit</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              In meiner Begleitung verbinden sich jahrzehntelange Hunde-Erfahrung und fundierte pädagogisch-therapeutische Ausbildungen zu einem ganzheitlichen Blick auf Mensch und Tier:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Maja Nowak (Berlin):</strong> Wegbereiterin Mensch-Hund-Kommunikation sowie Basis- und Fortgeschrittenen-Seminare zu Mensch und Hund.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Sybille Lüthi (Thalwil):</strong> Basis- und Vertiefungsausbildung in einfühlsamer Tierkommunikation.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Mentalcoaching &amp; Therapie:</strong> NLP/Mentalcoach BMC bei Andreas Lüthi sowie Mal- und Gestaltungstherapeutin bei Eva Brenner.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Sozialarbeit &amp; Betreuung:</strong> Biographiearbeit, Sozialarbeit und Betreuung von Menschen mit Unterstützungsbedarf (Biodynamischer Bauernhof Zürcher Oberland).</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Körper- &amp; Energiearbeit:</strong> Klassische und ayurvedische Gesundheitsmassage sowie energetisches Heilen.</span></div>
            </div>
          </div>
          <a href="leistungen.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Alle Angebote &amp; Tarife ansehen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- PHILOSOPHIE & TRAININGSPLATZ DERENDINGEN -->
  <section data-section="engagement" id="philosophie" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">BEZIEHUNG STATT ERZIEHUNG · KONTAKT STATT KONTROLLE</div>
        <h2 class="section-title">Unsere Haltung &amp; unser Treffpunkt in 4552 Derendingen</h2>
        <p class="section-desc">
          Artgerechtes Führen kommt ohne laute Kommandos, Leckerlis oder Unterwerfungsrituale aus: Ihr Hund folgt Ihnen freiwillig, weil er Ihre Ruhe und Kompetenz anerkennt.
        </p>
      </div>

      <div class="grid-2">
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-begleitung-augenhoehe.jpg" alt="Beziehung statt Erziehung bei MONDOCANI Dorette Sieber" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Philosophie</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Auf Augenhöhe</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Mensch und Hund als gleichbedeutende Partner</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Hunde spiegeln unsere innere Haltung unmittelbar. Im Dialog und Sich-Einfühlen schauen wir gemeinsam, welche Bedürfnisse, Kompetenzen und Grenzen Ihr Hund und Sie selbst mitbringen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Ruhe, Klarheit und feinsprachliche Körpersprache im Alltag</span></div>
                <div class="check-item">{SVG_CHECK} <span>Innere und äussere Konflikte gemeinsam erkennen und friedvoll lösen</span></div>
              </div>
            </div>
            <a href="kontakt.html?thema=einzelcoaching" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Einzelbegleitung anfragen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-gruppentreffen-rudel-derendingen.jpg" alt="Eingezäunter Trainingsplatz Club für Deutsche Doggen in 4552 Derendingen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">4552 Derendingen</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Sportstrasse</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Eingezäunter Platz mit Unterstand &amp; Hausbesuche</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Für unsere Freitags-Rudeltreffen, Workshops und Erlebnisvorträge nutzen wir den grosszügigen, sicher eingezäunten Platz des Clubs für Deutsche Doggen an der Sportstrasse in 4552 Derendingen (direkt neben dem Fussballplatz).
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Ausgestattet mit geschütztem Unterstand und Sitzgelegenheit</span></div>
                <div class="check-item">{SVG_CHECK} <span>Hausbesuche in Solothurn, Flumenthal, Bern, Basel &amp; Münchenstein</span></div>
              </div>
            </div>
            <a href="kontakt.html?thema=rudeltreffen" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Zum Rudeltreffen anmelden</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

# ==============================================================================
# SEITEN-INHALTE: V2 ZEIGEVERSION STARTSEITE (preview-mondocani-v2/index.html)
# ==============================================================================
V2_INDEX_BODY = f"""
  <!-- HERO SECTION -->
  <section class="hero-section" data-section="hero">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light" data-slot="hero_kicker">MENSCH-HUND-BEGLEITUNG · SOLOTHURN, DERENDINGEN, BERN &amp; BASEL</div>
        <h1 class="hero-title" data-slot="hero_title">
          Verstehe deinen Hund. <span>Erkenne dich selbst.</span>
        </h1>
        <p class="hero-lead" data-slot="hero_lead">
          Hunde sind feinfühlige Wegbegleiter und ehrliche Spiegel. Bei MONDOCANI begleitet Dorette Sieber Sie und Ihren Hund auf dem Weg zu einer ruhigen, vertrauensvollen Verbindung: ohne Leckerli-Dressur, ohne Druck, sondern in echter Beziehung auf Augenhöhe.
        </p>

        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
            <span>3-Schritte Smart-Anfrage testen</span>
            {SVG_ARROW}
          </a>
          <a href="#projektberater" class="btn-cta btn-cta-outline-light" data-slot="hero_cta_secondary">
            <span>Begleitungs-Finder starten</span>
          </a>
        </div>

        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Beziehung statt Erziehung</span>
            <span class="hero-badge-lbl">Kontakt statt Kontrolle: Ruhe, Klarheit und feinsprachliche Führung ohne Dressur</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Einzelcoaching &amp; Hausbesuch</span>
            <span class="hero-badge-lbl">Individuelle Begleitung bei Ihnen zu Hause und unterwegs (CHF 80.— / Std.)</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Freitags-Rudeltreffen</span>
            <span class="hero-badge-lbl">Spaziergang &amp; eingezäunter Platz in 4552 Derendingen (CHF 40.— / 1.5 Std.)</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Seit 2018 · Dorette Sieber</span>
            <span class="hero-badge-lbl">Wegbereiterin Mensch-Hund-Kommunikation (nach Maja Nowak) &amp; Tierkommunikation</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/hero-mensch-hund-bindung.jpg" alt="Dorette Sieber, MONDOCANI Mobile Hundeschule in Solothurn und Derendingen" width="600" height="390" data-slot="hero_image">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Lexend',sans-serif;font-weight:700;font-size:1.0rem;color:#1E140A;">Dorette Sieber · MONDOCANI</div>
            <div style="font-size:0.8rem;color:#3A2918;">Mobile Hundeschule in Solothurn, Derendingen, Bern &amp; Basel</div>
          </div>
          <span class="top-bar-badge">AUF AUGENHÖHE</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 3 KERNWEGE -->
  <section data-section="zielgruppen" id="zielgruppen" style="background-color:var(--bg-Warm);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="audiences_kicker">ECHTE VERBINDUNG · NATÜRLICHE KOMMUNIKATION · BEWUSSTES MITEINANDER</div>
        <h2 class="section-title" data-slot="audiences_title">Drei Zugänge für eine tiefe Mensch-Hund-Bindung</h2>
        <p class="section-desc" data-slot="audiences_desc">
          Ob Sie das Verhalten Ihres Hundes im Alltag verstehen möchten, den sozialen Austausch im Rudel suchen oder persönlich durch die ehrliche Rückmeldung eines Hundes wachsen wollen:
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">1. Einzelcoaching</span>
              <span class="icon-box">{SVG_HOME}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Mensch und Hund im Alltag</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Den Hund nicht nach starren Vorstellungen formen, sondern sein Wesen verstehen: Wir betrachten Ihre Wohn- und Alltagssituation zu Hause und üben auf gemeinsamen Spaziergängen eine ruhige, klare Führung.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Erster Termin gerne als Hausbesuch (ca. 1.5 bis 2 Stunden)</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>CHF 80.— pro Stunde:</strong> Für Welpen, Junghunde, erwachsene Hunde &amp; Strassenhunde</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=einzelcoaching" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Einzelcoaching anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">2. Gruppentreffen</span>
              <span class="icon-box">{SVG_USERS}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Rudeltreffen &amp; Wiesenstunde</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Jeden Freitagnachmittag (14:00–15:30 Uhr und 16:00–17:30 Uhr) geniessen wir in kleinen Gruppen einen Spaziergang in der Natur und beobachten die Hunde danach frei auf dem grossen eingezäunten Platz in Derendingen.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Treffpunkt: Club für Deutsche Doggen, Sportstrasse, 4552 Derendingen</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>CHF 40.— pro 1.5 Stunden:</strong> Es hat aktuell noch freie Plätze</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=rudeltreffen" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Platz im Rudeltreffen sichern</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">3. Hundegestütztes Coaching</span>
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 style="font-size:1.24rem;font-weight:700;margin-bottom:8px;">Persönlich wachsen mit Hund</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Hunde spiegeln unsere Körpersprache, Emotionen und unbewussten Muster völlig wertfrei. Mit Ihrem eigenen Hund oder meinem Hund als Co-Coach stärken Sie Selbstwert, Präsenz und gesunde Abgrenzung.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Klarer kommunizieren, Grenzen setzen und souverän führen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Für Beruf, Beziehung, emotionale Balance und Neuorientierung</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=hundecoaching" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Hundegestütztes Coaching klären</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 6 KERNANGEBOTE -->
  <section data-section="kernangebote" id="kernangebote">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="pillars_kicker">ANGEBOTSÜBERSICHT · MONDOCANI MOBILE HUNDESCHULE SOLOTHURN</div>
        <h2 class="section-title" data-slot="pillars_title">Sechs Begleitungsformen für ein harmonisches Miteinander</h2>
        <p class="section-desc" data-slot="pillars_desc">
          Ob junger Welpe, übernommener Strassenhund mit Vorgeschichte, wöchentliches Rudeltreffen oder persönliche Standortbestimmung:
        </p>
      </div>

      <div class="grid-3">
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-einzelcoaching-kontakt.jpg" alt="Individuelles Einzelcoaching und Hausbesuch bei MONDOCANI Solothurn" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">CHF 80.— / Std.</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Hausbesuch &amp; Alltag</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Individuelles Einzelcoaching</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Persönliche 1:1-Begleitung bei Ihnen zu Hause und auf Ihren gewohnten Spazierwegen: Ruhe, Klarheit und respektvolle Beziehungsverhandlungen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Erster Termin (1.5–2 Std.) inkl. Wohn- und Alltagssituation</span></div>
                <div class="check-item">{SVG_CHECK} <span>Artgerechtes Führen ohne Kommandos oder Leckerli-Manipulation</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Individuelles Einzelcoaching &amp; Hausbesuch (CHF 80.— / Std.)', '1.5–2 Std. Ersttermin zu Hause, Alltagsspaziergänge &amp; feinsprachliche Führung', 'Dorette Sieber')">
              <span>Details zum Einzelcoaching</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-gruppentreffen-rudel-derendingen.jpg" alt="Freitags-Rudeltreffen und Wiesenstunde in 4552 Derendingen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">CHF 40.— / 1.5 Std.</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Jeden Freitag</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Rudeltreffen &amp; Wiesenstunden</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Spaziergänge in kleinen Gruppen und anschliessend freie Rudelbegegnung auf dem grossen eingezäunten Platz an der Sportstrasse in 4552 Derendingen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Freitag 14:00–15:30 Uhr sowie 16:00–17:30 Uhr (freie Plätze)</span></div>
                <div class="check-item">{SVG_CHECK} <span>Sprache der Hunde verstehen, Ruhe beim Gassigehen &amp; Austausch</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Freitags-Rudeltreffen &amp; Wiesenstunden in 4552 Derendingen', 'Spaziergang &amp; freie Begegnung auf dem eingezäunten Platz (CHF 40.— / 1.5 Std.)', 'Dorette Sieber')">
              <span>Details zum Rudeltreffen</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-hundegestuetztes-coaching-reflexion.jpg" alt="Hundegestütztes Coaching bei MONDOCANI Dorette Sieber" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Co-Coach Hund</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Persönliches Wachstum</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Hundegestütztes Coaching</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Ehrlich, achtsam und berührend: Im geschützten Reflexionsraum mit eigenem Hund oder Co-Coach-Hund persönliche Blockaden lösen und Präsenz stärken.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Selbstbewusstsein, emotionale Balance &amp; Stressbewältigung</span></div>
                <div class="check-item">{SVG_CHECK} <span>Souverän und wertschätzend führen sowie klar Grenzen setzen</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Hundegestütztes Coaching für persönliche Weiterentwicklung', 'Reflexion von Körpersprache, Grenzen &amp; Führung mit eigenem oder Co-Coach-Hund', 'Dorette Sieber')">
              <span>Details zum Coaching</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-hundegestuetztes-coaching-natur.jpg" alt="Workshops und Seminare zur Mensch-Hund-Beziehung in Derendingen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">CHF 80.— / Team</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">3–4 Stunden</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Workshops &amp; Tagesseminare</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Gemeinsames Erleben und Beobachten auf dem eingezäunten Platz mit Unterstand in Derendingen: Wo braucht Ihr Hund Führung und wo mehr Freiraum?
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Prozesse, Aufgaben und natürliche Ressourcen im Rudel erkennen</span></div>
                <div class="check-item">{SVG_CHECK} <span>Der eigenen Wahrnehmung vertrauen und Konflikte ruhig lösen</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Workshops &amp; Seminare auf dem Hundeplatz Derendingen', 'Rudelbeobachtung, Ressourcen &amp; Kommunikation unter Hunden (CHF 80.— / Team)', 'Dorette Sieber')">
              <span>Details zu Workshops</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-einzelcoaching-ruhe-vertrauen.jpg" alt="Strassenhunde und Welpen begleiten bei MONDOCANI" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Spezialbegleitung</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Welpen &amp; Tierschutz</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Welpen &amp; Strassenhunde</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Ob Beratung vor dem Hundekauf, friedvoller Start mit einem Welpen oder einfühlsame Begleitung für traumatisierte Tierschutz- und Strassenhunde.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Überwindung von Unsicherheiten, Ängsten und Leinenstress</span></div>
                <div class="check-item">{SVG_CHECK} <span>Einbezug aller Familienmitglieder für einen klaren Alltag</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Welpen-Coaching &amp; Strassenhunde einfühlsam begleiten', 'Beratung vor dem Hundekauf, Welpen-Orientierung &amp; Vertrauensaufbau für Tierschutzhunde', 'Dorette Sieber')">
              <span>Begleitung ansehen</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/ref-erlebnisvortrag-kennenlernen.jpg" alt="MONDOCANI kennenlernen und Erlebnisvortrag in Derendingen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Unverbindlich</span>
                <span style="font-family:'Lexend',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Freitag ab 16:00 Uhr</span>
              </div>
              <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Erlebnisvortrag &amp; Erstgespräch</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Möchten Sie in Ruhe spüren, ob meine Art und Weise zu Ihnen und Ihrem Hund passt, bevor Sie sich für ein Coaching oder Rudeltreffen entscheiden?
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Erlebnisvortrag für Interessierte (Freitag ab 16:00 Uhr, Derendingen)</span></div>
                <div class="check-item">{SVG_CHECK} <span>Kostenlose 15-minütige Beratung per Telefon oder Zoom</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Erlebnisvortrag Derendingen &amp; Kostenloses 15-Min.-Erstgespräch', 'Freitag ab 16:00 Uhr auf dem Hundeplatz Derendingen oder telefonisch / per Zoom', 'Dorette Sieber')">
              <span>Kennenlernen vereinbaren</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

{render_mondocani_advisor()}

  <!-- KUNDENSTIMMEN & PRAXIS-EINBLICKE -->
  <section data-section="referenzen-auszug" id="referenzen">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="refs_kicker">EURE RÜCKMELDUNGEN &amp; PRAXIS-SCHWERPUNKTE · ECHTE VERÄNDERUNG</div>
        <h2 class="section-title" data-slot="refs_title">Was Mensch-Hund-Teams bei MONDOCANI erleben</h2>
        <p class="section-desc" data-slot="refs_desc">
          Lesen Sie echte Rückmeldungen (u. a. von Doris &amp; Claude mit Milu sowie Ute mit Foxy &amp; Róisín) und entdecken Sie unsere Praxis-Schwerpunkte:
        </p>
      </div>

      {render_references_grid(limit=6, is_v2=True)}
    </div>
  </section>

  <!-- V2 AUSBLICK AUF DIE 3 WEITEREN UNTERSEITEN -->
  <section class="preview-scope-section" id="weitere-themenbereiche" data-section="vorschau-umfang">
    <div class="container">
      <div class="preview-scope-banner">
        <div class="section-kicker">UNVERBINDLICHER VORSCHAU-ENTWURF · 2 BEISPIEL-SEITEN AUSGEARBEITET</div>
        <h2 style="font-size:clamp(1.55rem,2.5vw,2.1rem);font-weight:700;margin-bottom:10px;">
          Ausblick: Diese 3 weiteren Detailseiten folgen beim gemeinsamen Ausbau
        </h2>
        <p style="font-size:0.95rem;color:var(--text-body);line-height:1.62;">
          In dieser <strong>Zeigeversion</strong> sind Ihre neue <strong>Startseite</strong> (inklusive interaktivem Mensch-Hund-Begleitungs-Finder) sowie die <strong>Kontaktseite mit dem 3-Schritte Smart-Anfrage-Assistenten</strong> bereits vollständig ausgearbeitet und live testbar. Beim gemeinsamen Ausbau schalten wir zusätzlich die folgenden drei vertieften Unterseiten mit allen Originaltexten und Ihren Originalbildern frei:
        </p>
      </div>

      <div class="grid-3">
        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Folgt beim Ausbau · Unterseite 1</span>
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Angebot: Alle 6 Begleitungsformen, Ablauf &amp; Preise</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Übersichtliche Darstellung aller Angebote für Mensch und Hund:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Einzelcoaching &amp; Hausbesuch (CHF 80.—/Std.) inkl. Ersttermin-Ablauf</span></div>
              <div class="check-item">{SVG_CHECK} <span>Freitags-Rudeltreffen in 4552 Derendingen (CHF 40.—/1.5 Std.)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Hundegestütztes Coaching, Workshops (CHF 80.—) &amp; Erlebnisvortrag</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Angebot: Alle 6 Begleitungsformen, Ablauf &amp; Preise', 'Einzelcoaching, Rudeltreffen Derendingen, Hundegestütztes Coaching, Workshops &amp; Vortrag', 'Dorette Sieber')">
            <span>Vorschau-Details zum Angebot öffnen</span>
            {SVG_ARROW}
          </button>
        </div>

        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Folgt beim Ausbau · Unterseite 2</span>
              <span class="icon-box">{SVG_USERS}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Einblicke: Kundenstimmen, Blog-Impulse &amp; Galerie</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Authentische Geschichten, Rückmeldungen und Naturfotografien:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Ungekürzte Referenzen (Doris &amp; Claude mit Milu, Ute mit Foxy &amp; Róisín)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Blog-Impulse: Gedenken an Hündin Tajuya, Strassenhunde &amp; Welpen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Bildergalerie aus Solothurn, Derendingen, den Alpen und La Palma</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Einblicke: Kundenstimmen, Blog-Impulse &amp; Galerie', 'Erfahrungsberichte, Blog-Beiträge (Tajuya, Strassenhunde, Welpen) &amp; Fotogalerie', 'Dorette Sieber')">
            <span>Vorschau-Details zu Einblicken öffnen</span>
            {SVG_ARROW}
          </button>
        </div>

        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Folgt beim Ausbau · Unterseite 3</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:700;margin-bottom:8px;">Über Dorette Sieber, Philosophie &amp; Vita</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Persönliches Porträt und fachlicher Hintergrund seit der Gründung 2018:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Lebensweg: Berner Sennenhund Barry, Älplerin in den Bergen &amp; La Palma</span></div>
              <div class="check-item">{SVG_CHECK} <span>Wegbereiterin nach Maja Nowak (Berlin) &amp; Tierkommunikation Sybille Lüthi</span></div>
              <div class="check-item">{SVG_CHECK} <span>NLP/Mentalcoach BMC, Mal- &amp; Gestaltungstherapie sowie Sozialarbeit</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Über Dorette Sieber, Philosophie &amp; Vita', 'Persönlicher Weg, Ausbildungen bei Maja Nowak &amp; Sybille Lüthi sowie 13 Philosophie-Kernpunkte', 'Dorette Sieber')">
            <span>Vorschau-Details zu Über mich öffnen</span>
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
        <!-- LEFT COLUMN: DIREKTKONTAKT SOLOTHURN & DERENDINGEN -->
        <div class="contact-info-panel">
          <div class="section-kicker" data-slot="contact_kicker">KONTAKT &amp; ERSTGESPRÄCH · SOLOTHURN &amp; 4552 DERENDINGEN</div>
          <h1 style="font-size:clamp(1.65rem,2.5vw,2.15rem);font-weight:700;margin-bottom:12px;" data-slot="contact_title">
            Ihr direkter Draht zu Dorette Sieber.
          </h1>
          <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:18px;" data-slot="contact_lead">
            Ob individuelles Einzelcoaching mit Hausbesuch, Anmeldung zum Freitags-Rudeltreffen in Derendingen, hundegestütztes Coaching oder ein kostenloses 15-minütiges Kennenlerngespräch: Starten Sie rechts die 3-Schritte Smart-Anfrage oder rufen Sie direkt an.
          </p>

          <img src="images/ref-kontakt-hund-natur.jpg" alt="Dorette Sieber, MONDOCANI Mobile Hundeschule in Solothurn" style="width:100%;height:200px;object-fit:cover;object-position:center;border-radius:var(--radius-sm);margin-bottom:16px;" loading="lazy" decoding="async">

          <div class="contact-direct-list">
            <div class="contact-direct-item">
              <div class="contact-direct-role">Inhaberin &amp; Persönliche Begleitung</div>
              <div class="contact-direct-person">MONDOCANI · Die mobile Hundeschule · Dorette Sieber</div>
              <div class="contact-direct-links">Telefon &amp; WhatsApp: 079 446 70 43 · E-Mail: mail@mondocani.ch</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Eingezäunter Trainings- &amp; Rudeltreffplatz</div>
              <div class="contact-direct-person">Club für Deutsche Doggen · Sportstrasse · CH-4552 Derendingen</div>
              <div class="contact-direct-links">Direkt neben dem Fussballplatz · Mit geschütztem Unterstand &amp; Sitzgelegenheit</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Feste Rudeltreffen &amp; Erlebnisvortrag</div>
              <div class="contact-direct-person">Jeden Freitagnachmittag: 14:00 – 15:30 Uhr &amp; 16:00 – 17:30 Uhr</div>
              <div class="contact-direct-links">Erlebnisvortrag Freitag ab 16:00 Uhr · Einzelcoaching nach Vereinbarung</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Mobiles Einsatzgebiet für Hausbesuche</div>
              <div class="contact-direct-person">Standort Flumenthal / Solothurn · Umgebung Bern · Basel &amp; Münchenstein</div>
              <div class="contact-direct-links">Hausbesuche und Alltagsspaziergänge direkt in Ihrer gewohnten Umgebung</div>
            </div>
          </div>
        </div>

        <!-- RIGHT COLUMN: GEFÜHRTER 3-SCHRITTE SMART-ANFRAGE-ASSISTENT -->
        <div class="wizard-card">
          <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:14px;">
            <div>
              <div class="section-kicker" style="margin-bottom:4px;">3-SCHRITTE SMART-ANFRAGE · MONDOCANI.CH</div>
              <h2 style="font-size:1.35rem;font-weight:700;" id="wpWizardTitle">1. Welche Begleitung wünschen Sie sich?</h2>
            </div>
            <span class="meta-badge" id="wpActiveAssigneeBadge">Begleitung: Dorette Sieber</span>
          </div>

          <div class="wp-stepper" aria-label="Fortschritt">
            <div class="wp-step-pill active" id="wpStepPill1">
              <span class="wp-step-num">1</span>
              <span>Angebot wählen</span>
            </div>
            <div class="wp-step-pill" id="wpStepPill2">
              <span class="wp-step-num">2</span>
              <span>Hund &amp; Alltag</span>
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

            <!-- SCHRITT 1: ANGEBOTSBEREICH -->
            <div class="wp-step-pane active" id="wpStep1">
              <div class="wp-role-grid" id="wpTopicGrid">
                <button type="button" class="wp-role-tile selected" data-topic="Einzelcoaching & Hausbesuch (CHF 80.— / Std.)" onclick="wpSelectIsTopic('Einzelcoaching & Hausbesuch (CHF 80.— / Std.)')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_HOME}</span>
                    <span class="wp-role-title" data-slot="topic_opt_1">1. Einzelcoaching</span>
                  </div>
                  <span class="wp-role-desc">Individuelle Mensch-Hund-Begleitung, Hausbesuch (1.5–2 Std.), Welpen &amp; Strassenhunde</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Freitags-Rudeltreffen & Gruppentreffen Derendingen (CHF 40.—)" onclick="wpSelectIsTopic('Freitags-Rudeltreffen & Gruppentreffen Derendingen (CHF 40.—)')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_USERS}</span>
                    <span class="wp-role-title" data-slot="topic_opt_2">2. Rudeltreffen</span>
                  </div>
                  <span class="wp-role-desc">Freitag 14:00–15:30 oder 16:00–17:30 Uhr · Spaziergang &amp; Platz 4552 Derendingen</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Hundegestütztes Coaching & Persönlichkeitsentwicklung" onclick="wpSelectIsTopic('Hundegestütztes Coaching & Persönlichkeitsentwicklung')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_HEART}</span>
                    <span class="wp-role-title" data-slot="topic_opt_3">3. Hundecoaching</span>
                  </div>
                  <span class="wp-role-desc">Körpersprache, Selbstwert, Grenzen &amp; Führung mit eigenem Hund oder Co-Coach-Hund</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Kennenlernen, Erlebnisvortrag oder 15-Min.-Erstgespräch" onclick="wpSelectIsTopic('Kennenlernen, Erlebnisvortrag oder 15-Min.-Erstgespräch')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_COMPASS}</span>
                    <span class="wp-role-title" data-slot="topic_opt_4">4. Erstgespräch</span>
                  </div>
                  <span class="wp-role-desc">15-Min.-Beratung per Telefon/Zoom, Erlebnisvortrag (Fr 16:00 Uhr) oder Workshop</span>
                </button>
              </div>

              <button type="button" class="btn-cta btn-cta-primary" style="width:100%;" onclick="wpNextStep(2)">
                <span>Weiter zu Schritt 2: Hund &amp; Anliegen</span>
                {SVG_ARROW}
              </button>
            </div>

            <!-- SCHRITT 2: HUND & ANLIEGEN -->
            <div class="wp-step-pane" id="wpStep2">
              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="wpDetail1" class="form-label" id="wpDetail1Label">Name, Alter &amp; Rasse/Herkunft Ihres Hundes</label>
                  <input type="text" id="wpDetail1" class="form-input" placeholder="z. B. Milu, 2 Jahre, Podengo aus dem Tierschutz">
                </div>
                <div class="form-field">
                  <label for="wpDetail2" class="form-label" id="wpDetail2Label">Gewünschter Ort (Hausbesuch, Derendingen oder Telefon/Zoom)</label>
                  <input type="text" id="wpDetail2" class="form-input" placeholder="z. B. Hausbesuch Region Solothurn oder Platz Derendingen">
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label class="form-label">Gewünschter Zeitraum</label>
                <div class="wp-role-grid" id="wpUrgencyGrid" style="margin-bottom:0;">
                  <button type="button" class="wp-role-tile selected" data-urg="Zeitnah (Termin oder 15-Min.-Telefonat in den nächsten Tagen)" onclick="wpSelectIsUrgency('Zeitnah (Termin oder 15-Min.-Telefonat in den nächsten Tagen)')">
                    <span class="wp-role-title">1. Zeitnaher Termin / Telefonat</span>
                    <span class="wp-role-desc">Kennenlerngespräch, Hausbesuch oder nächstes Freitags-Rudeltreffen</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urg="In Ruhe vorab informieren (Fragen vor Hundekauf / Workshop)" onclick="wpSelectIsUrgency('In Ruhe vorab informieren (Fragen vor Hundekauf / Workshop)')">
                    <span class="wp-role-title">2. Vorab-Orientierung</span>
                    <span class="wp-role-desc">Beratung vor dem Hundekauf, Erlebnisvortrag oder kommender Workshop</span>
                  </button>
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label for="contactMessage" class="form-label">Was beschäftigt Sie und Ihren Hund aktuell? (optional)</label>
                <textarea id="contactMessage" class="form-textarea" placeholder="Beschreiben Sie kurz Ihr Anliegen (z. B. Ruhe beim Spaziergang, Unsicherheit, Hundebegegnungen, Rudeltreffen am Freitag oder persönliches Coaching)..."></textarea>
              </div>

              <div class="form-field" style="margin-bottom:18px;">
                <label class="form-label">Optional: Foto Ihres Hundes beifügen (max. 3 Bilder)</label>
                <div class="wp-upload-zone" onclick="document.getElementById('wpPhotoInput').click()">
                  <div style="font-weight:700;font-size:0.86rem;color:var(--charcoal-deep);margin-bottom:2px;">Hier tippen, um bis zu 3 Fotos auszuwählen (JPG/PNG)</div>
                  <div style="font-size:0.78rem;color:var(--text-muted);">Ideal für einen ersten Eindruck im Begleitungs-Dossier für Dorette Sieber</div>
                  <input type="file" id="wpPhotoInput" accept="image/*" multiple style="display:none;" onchange="wpHandlePhotoFiles(this.files)">
                </div>
                <div class="wp-photo-thumbs" id="wpPhotoThumbs"></div>
              </div>

              <div class="wizard-nav-row">
                <button type="button" class="btn-cta btn-cta-outline btn-sm" onclick="wpNextStep(1)">
                  <span>Zurück zu Schritt 1</span>
                </button>
                <button type="button" class="btn-cta btn-cta-primary btn-sm" onclick="wpNextStep(3)">
                  <span>Weiter zu Schritt 3: Kontaktdaten</span>
                  {SVG_ARROW}
                </button>
              </div>
            </div>

            <!-- SCHRITT 3: KONTAKTDATEN & ABSENDEN -->
            <div class="wp-step-pane" id="wpStep3">
              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactName" class="form-label">Ihr Vor- und Nachname *</label>
                  <input type="text" id="contactName" class="form-input" placeholder="z. B. Doris Muster" required>
                </div>
                <div class="form-field">
                  <label for="contactCompany" class="form-label">Name Ihres Hundes (optional)</label>
                  <input type="text" id="contactCompany" class="form-input" placeholder="z. B. Hündin Milu">
                </div>
              </div>

              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactStreet" class="form-label">Strasse &amp; Hausnummer (für Hausbesuch)</label>
                  <input type="text" id="contactStreet" class="form-input" placeholder="z. B. Hauptstrasse 12">
                </div>
                <div class="form-field">
                  <label for="contactPlz" class="form-label">PLZ &amp; Wohnort *</label>
                  <input type="text" id="contactPlz" class="form-input" placeholder="z. B. 4500 Solothurn" required>
                </div>
              </div>

              <div class="form-grid-2" style="margin-bottom:16px;">
                <div class="form-field">
                  <label for="contactPhone" class="form-label">Telefon / Mobile (für Rückruf / WhatsApp) *</label>
                  <input type="tel" id="contactPhone" class="form-input" placeholder="z. B. 079 123 45 67" required>
                </div>
                <div class="form-field">
                  <label for="contactEmail" class="form-label">E-Mail-Adresse *</label>
                  <input type="email" id="contactEmail" class="form-input" placeholder="ihre.adresse@beispiel.ch" required>
                </div>
              </div>

              <div id="wpFormError" style="display:none;background-color:#FEF2F2;border:1px solid #FECACA;color:#991B1B;padding:10px 12px;border-radius:var(--radius-sm);font-size:0.84rem;font-weight:600;margin-bottom:14px;"></div>

              <div class="wizard-nav-row">
                <button type="button" class="btn-cta btn-cta-outline btn-sm" onclick="wpNextStep(2)">
                  <span>Zurück zu Schritt 2</span>
                </button>
                <button type="submit" class="btn-cta btn-cta-gold" id="wpSubmitBtn">
                  <span id="wpSubmitBtnText">1-Seiten-Dossier &amp; Anfrage senden</span>
                  {SVG_ARROW}
                </button>
              </div>
            </div>
          </form>

          <!-- SUCCESS DOSSIER BOX -->
          <div class="wp-success-box" id="wpSuccessBox" role="status" aria-live="polite">
            <div class="section-kicker" style="color:var(--green);margin-bottom:6px;">ANFRAGE ERFOLGREICH AUFBEREITET</div>
            <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:8px;">Vielen Dank! Ihr 1-Seiten-Begleitungs-Dossier für MONDOCANI steht bereit.</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Ihre Angaben wurden strukturiert an <strong>Dorette Sieber</strong> übermittelt:
            </p>
            <div style="background-color:#FFFFFF;border:1px solid var(--border-light);border-radius:var(--radius-sm);padding:12px 14px;font-size:0.84rem;margin-bottom:14px;display:grid;gap:6px;">
              <div><strong>Referenz-Nummer:</strong> <span id="wpResRef">#WP-2026</span></div>
              <div><strong>Ansprechpartnerin:</strong> <span id="wpResAssigned">Dorette Sieber (MONDOCANI)</span></div>
              <div><strong>Rückmeldung:</strong> <span id="wpResCallback">Persönlich per Telefon oder E-Mail</span></div>
              <div><strong>Zustell-Kanäle:</strong> <span id="wpResChannels">1-Seiten-PDF-Dossier + E-Mail + WhatsApp</span></div>
            </div>
            <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:12px;">
              <a href="kontakt.html" id="wpResPdfBtn" target="_blank" rel="noopener" class="btn-cta btn-cta-primary btn-sm">
                <span>1-Seiten-PDF-Dossier öffnen</span>
                {SVG_ARROW}
              </a>
              <button type="button" class="btn-cta btn-cta-outline btn-sm" onclick="wpResetWizard()">
                <span>Weitere Anfrage erfassen</span>
              </button>
            </div>
            <div style="font-size:0.78rem;color:var(--text-muted);background-color:#F8EEE5;padding:10px 12px;border-radius:var(--radius-sm);white-space:pre-line;" id="wpResWaPreview"></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <script>
    var wpIsState = {{
      step: 1,
      topic: 'Einzelcoaching & Hausbesuch (CHF 80.— / Std.)',
      urgency: 'Zeitnah (Termin oder 15-Min.-Telefonat in den nächsten Tagen)',
      photos: []
    }};

    function wpStripEmojisForDom(str) {{
      if (!str) return '';
      return String(str).replace(/[\\u{{1F300}}-\\u{{1FAFF}}\\u{{2600}}-\\u{{27BF}}]/gu, '');
    }}

    function wpSelectIsTopic(topic) {{
      wpIsState.topic = topic;
      var btns = document.querySelectorAll('#wpTopicGrid .wp-role-tile');
      for (var i = 0; i < btns.length; i++) {{
        btns[i].classList.toggle('selected', btns[i].getAttribute('data-topic') === topic);
      }}
      var l1 = document.getElementById('wpDetail1Label');
      var i1 = document.getElementById('wpDetail1');
      var l2 = document.getElementById('wpDetail2Label');
      var i2 = document.getElementById('wpDetail2');
      if (topic.indexOf('Rudeltreffen') !== -1) {{
        if (l1) l1.textContent = 'Name, Alter & Sozialverträglichkeit Ihres Hundes';
        if (i1) i1.placeholder = 'z. B. Freundliche Hündin, 3 Jahre · gerne im Rudel';
        if (l2) l2.textContent = 'Gewünschte Freitags-Gruppe in 4552 Derendingen';
        if (i2) i2.placeholder = 'z. B. Freitag 14:00–15:30 Uhr oder 16:00–17:30 Uhr';
      }} else if (topic.indexOf('Hundegestütztes') !== -1) {{
        if (l1) l1.textContent = 'Ihr persönliches Coaching-Thema';
        if (i1) i1.placeholder = 'z. B. Selbstbewusstsein, klare Führung, Grenzen setzen';
        if (l2) l2.textContent = 'Mit eigenem Hund oder mit Co-Coach-Hund von Dorette?';
        if (i2) i2.placeholder = 'z. B. Mit eigenem Hund oder mit Co-Coach-Hund';
      }} else if (topic.indexOf('Kennenlernen') !== -1) {{
        if (l1) l1.textContent = 'Gewünschte Kennenlern-Form';
        if (i1) i1.placeholder = 'z. B. 15-Min.-Telefonat/Zoom oder Erlebnisvortrag Fr 16:00 Uhr';
        if (l2) l2.textContent = 'Haben Sie bereits einen Hund oder planen Sie eine Anschaffung?';
        if (i2) i2.placeholder = 'z. B. Junger Hund seit 2 Monaten / Fragen vor dem Kauf';
      }} else {{
        if (l1) l1.textContent = 'Name, Alter & Rasse/Herkunft Ihres Hundes';
        if (i1) i1.placeholder = 'z. B. Milu, 2 Jahre, Podengo aus dem Tierschutz';
        if (l2) l2.textContent = 'Gewünschter Ort (Hausbesuch, Derendingen oder Telefon/Zoom)';
        if (i2) i2.placeholder = 'z. B. Hausbesuch Region Solothurn oder Platz Derendingen';
      }}
      setTimeout(function() {{ wpNextStep(2); }}, 120);
    }}

    function wpSelectIsUrgency(urg) {{
      wpIsState.urgency = urg;
      var btns = document.querySelectorAll('#wpUrgencyGrid .wp-role-tile');
      for (var i = 0; i < btns.length; i++) {{
        btns[i].classList.toggle('selected', btns[i].getAttribute('data-urg') === urg);
      }}
    }}

    function wpNextStep(step) {{
      wpIsState.step = step;
      for (var s = 1; s <= 3; s++) {{
        var pane = document.getElementById('wpStep' + s);
        var pill = document.getElementById('wpStepPill' + s);
        if (pane) pane.classList.toggle('active', s === step);
        if (pill) {{
          pill.classList.toggle('active', s === step);
          pill.classList.toggle('done', s < step);
        }}
      }}
      var titles = {{
        1: '1. Welche Begleitung wünschen Sie sich?',
        2: '2. Erzählen Sie uns kurz von Ihrem Hund & Anliegen',
        3: '3. Wohin darf Dorette Sieber sich bei Ihnen melden?'
      }};
      var tEl = document.getElementById('wpWizardTitle');
      if (tEl && titles[step]) tEl.textContent = titles[step];
    }}

    function wpHandlePhotoFiles(fileList) {{
      if (!fileList || !fileList.length) return;
      var maxFiles = 3;
      for (var i = 0; i < fileList.length && wpIsState.photos.length < maxFiles; i++) {{
        (function(file) {{
          if (!file.type || file.type.indexOf('image/') !== 0) return;
          var reader = new FileReader();
          reader.onload = function(ev) {{
            var img = new Image();
            img.onload = function() {{
              var canvas = document.createElement('canvas');
              var maxDim = 900;
              var w = img.width;
              var h = img.height;
              if (w > maxDim || h > maxDim) {{
                if (w > h) {{ h = Math.round(h * maxDim / w); w = maxDim; }}
                else {{ w = Math.round(w * maxDim / h); h = maxDim; }}
              }}
              canvas.width = w;
              canvas.height = h;
              var ctx = canvas.getContext('2d');
              ctx.drawImage(img, 0, 0, w, h);
              var dataUrl = canvas.toDataURL('image/jpeg', 0.8);
              wpIsState.photos.push({{ name: file.name, data_url: dataUrl }});
              wpRenderPhotoThumbs();
            }};
            img.src = ev.target.result;
          }};
          reader.readAsDataURL(file);
        }})(fileList[i]);
      }}
    }}

    function wpRenderPhotoThumbs() {{
      var box = document.getElementById('wpPhotoThumbs');
      if (!box) return;
      while (box.firstChild) box.removeChild(box.firstChild);
      wpIsState.photos.forEach(function(p) {{
        var img = document.createElement('img');
        img.src = p.data_url;
        img.alt = p.name || 'Hundefoto';
        img.className = 'wp-photo-thumb';
        box.appendChild(img);
      }});
    }}

    function wpResetWizard() {{
      document.getElementById('wpSuccessBox').classList.remove('visible');
      document.getElementById('isContactForm').style.display = 'block';
      wpNextStep(1);
    }}

    function wpSubmitIsLead(e) {{
      if (e) e.preventDefault();
      var errBox = document.getElementById('wpFormError');
      if (errBox) errBox.style.display = 'none';

      var name = (document.getElementById('contactName').value || '').trim();
      var company = (document.getElementById('contactCompany').value || '').trim();
      var street = (document.getElementById('contactStreet').value || '').trim();
      var loc = (document.getElementById('contactPlz').value || '').trim();
      var phone = (document.getElementById('contactPhone').value || '').trim();
      var email = (document.getElementById('contactEmail').value || '').trim();
      var msg = (document.getElementById('contactMessage').value || '').trim();
      var d1 = (document.getElementById('wpDetail1').value || '').trim();
      var d2 = (document.getElementById('wpDetail2').value || '').trim();
      var hp = (document.getElementById('wpHoneypot').value || '').trim();

      if (!name || !loc || !phone || !email) {{
        if (errBox) {{
          errBox.textContent = 'Bitte füllen Sie Name, PLZ/Wohnort, Telefonnummer und E-Mail-Adresse vollständig aus.';
          errBox.style.display = 'block';
        }}
        return false;
      }}

      var btn = document.getElementById('wpSubmitBtn');
      var btnTxt = document.getElementById('wpSubmitBtnText');
      if (btn) btn.disabled = true;
      if (btnTxt) btnTxt.textContent = '1-Seiten-Dossier wird erstellt...';

      var extra = {{
        'Gewünschte Begleitung': wpIsState.topic,
        'Hund / Thema': d1 || 'Wird im Gespräch geklärt',
        'Gewünschter Ort / Gruppe': d2 || 'Hausbesuch oder Derendingen',
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
        message: msg || ('MONDOCANI-Anfrage zu ' + wpIsState.topic),
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
        document.getElementById('wpResAssigned').textContent = res.assigned_to || 'Dorette Sieber (MONDOCANI)';
        document.getElementById('wpResCallback').textContent = res.callback_window || 'Persönlich per Telefon oder E-Mail';
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
          errBox.textContent = 'Netzwerkfehler bei der Übermittlung. Bitte schreiben Sie direkt an mail@mondocani.ch oder rufen Sie 079 446 70 43 an.';
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
          'einzelcoaching': 'Einzelcoaching & Hausbesuch (CHF 80.— / Std.)',
          'rudeltreffen': 'Freitags-Rudeltreffen & Gruppentreffen Derendingen (CHF 40.—)',
          'hundecoaching': 'Hundegestütztes Coaching & Persönlichkeitsentwicklung',
          'kennenlernen': 'Kennenlernen, Erlebnisvortrag oder 15-Min.-Erstgespräch'
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
    ("index.html", "MONDOCANI · Die mobile Hundeschule Solothurn | Verstehe deinen Hund. Erkenne dich selbst.", "startseite", V1_INDEX_BODY),
    ("leistungen.html", "Angebot & Preise | Einzelcoaching, Rudeltreffen Derendingen & Hundegestütztes Coaching – MONDOCANI", "leistungen", V1_LEISTUNGEN_BODY),
    ("referenzen.html", "Kundenstimmen, Blog-Impulse & Galerie | MONDOCANI Mobile Hundeschule Solothurn", "referenzen", V1_REFERENZEN_BODY),
    ("ueber-uns.html", "Über Dorette Sieber & Philosophie | MONDOCANI Mobile Hundeschule Solothurn", "ueber-uns", V1_UEBER_UNS_BODY),
    ("kontakt.html", "Kontakt, Standorte & 3-Schritte Smart-Anfrage | MONDOCANI Dorette Sieber Solothurn & Derendingen", "kontakt", build_kontakt_body("mondocani-vv", "preview-mondocani/kontakt.html")),
]

for fname, title, nav_key, body in v1_pages:
    full_html = render_v1_shell(fname, title, nav_key, body)
    (V1_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V1] Wrote {fname} ({len(full_html)} bytes)")

# 4. Alle Seiten für Variante 2 (Zeigeversion / Vorschau-Entwurf) schreiben
v2_pages = [
    ("index.html", "MONDOCANI · Die mobile Hundeschule Solothurn (Zeigeversion / Vorschau-Entwurf)", "startseite", V2_INDEX_BODY),
    ("kontakt.html", "Kontakt & 3-Schritte Smart-Anfrage (Zeigeversion) | MONDOCANI Dorette Sieber Solothurn", "kontakt", build_kontakt_body("mondocani-v2", "preview-mondocani-v2/kontakt.html")),
]

for fname, title, nav_key, body in v2_pages:
    full_html = render_v2_shell(fname, title, nav_key, body)
    (V2_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V2] Wrote {fname} ({len(full_html)} bytes)")

# 5. Partner-Attribution (#wpPartnerModal für Jenny Ettle JE-MI) injizieren
subprocess.run(["python3", str(BASE_DIR / "scripts" / "inject_partner_attribution.py")], check=True)

# 6. Studio Cockpit v4.0 (cockpit.html) für beide Varianten generieren
subprocess.run(["python3", str(BASE_DIR / "scripts" / "build_client_cockpit.py"), "--slug", "preview-mondocani"], check=True)
subprocess.run(["python3", str(BASE_DIR / "scripts" / "build_client_cockpit.py"), "--slug", "preview-mondocani-v2"], check=True)

# 7. Compile Site Pipeline (Pre-Build Gates & Airbag)
subprocess.run(["python3", str(BASE_DIR / "scripts" / "compile_site.py"), "--site", "preview-mondocani", "--skip-device-audit"], check=True)
subprocess.run(["python3", str(BASE_DIR / "scripts" / "compile_site.py"), "--site", "preview-mondocani-v2", "--skip-device-audit"], check=True)
print("Successfully built and compiled preview-mondocani and preview-mondocani-v2.")

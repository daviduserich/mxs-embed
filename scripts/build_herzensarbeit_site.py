#!/usr/bin/env python3
"""
Generator für die WebPilot-Referenz-Aufbereitung von herzensarbeit.ch (Anne-Katrin Koch, Härkingen & Oensingen SO):
- Variante 1 (Vollversion): /home/brainuser/workspaces/mxs-embed/preview-herzensarbeit
  Live-URL: https://vorschau.magnet-xs.ch/herzensarbeit-vollversion/ (5 voll ausgebaute Seiten + Studio Cockpit v4.0)
- Variante 2 (Zeigeversion / Vorschau-Entwurf): /home/brainuser/workspaces/mxs-embed/preview-herzensarbeit-v2
  Live-URL: https://vorschau.magnet-xs.ch/herzensarbeit-v2/ (2 ausgearbeitete Beispiel-Seiten: Startseite + 3-Schritte Smart-Anfrage,
  plus anschauliche Themenbereich-Vorschaukarten für die 3 weiteren Unterseiten).

Strikt nach:
- UI-LAYOUT-RULES.md (Canary: UI-LAYOUT-2026-V1)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1, 0 Eszett, 100 % Schweizer Hochdeutsch)
- #SYS-01 (Kein oberer Versions-/Cockpit-Balken, 0 Hinweise auf Vollversion/Cockpit auf Kundenseiten)
"""

import json
import subprocess
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
V1_DIR = BASE_DIR / "preview-herzensarbeit"
V2_DIR = BASE_DIR / "preview-herzensarbeit-v2"

V1_DIR.mkdir(parents=True, exist_ok=True)
V2_DIR.mkdir(parents=True, exist_ok=True)

BEFORE_INVENTORY = {
    "source_url": "https://herzensarbeit.ch/",
    "crawled_at": "2026-11-05",
    "company_name": "Herzensarbeit — Anne-Katrin Koch",
    "legal_entity": "Herzensarbeit · Anne-Katrin Koch Künzle",
    "claim": "Mit offenem Herzen lieben und leben",
    "subline": "Paartherapie, Trennungsberatung, Trauerbegleitung, Achtsamkeit & Frauen-Workshops in Härkingen (SO) und Online",
    "address": {
        "building": "Praxis Herzensarbeit",
        "street": "Usserdorf 24",
        "zip": "4624",
        "city": "Härkingen",
        "canton": "SO",
        "country": "Schweiz",
        "workshop_venue": "Gemeinschaftspraxis Oensingen, Dünnernstrasse 2, CH-4702 Oensingen (SO)"
    },
    "contact": {
        "email": "a.koch@herzensarbeit.ch",
        "phone_primary": "+41 79 103 63 31",
        "phone_display": "079 103 63 31",
        "channels": "Telefon, WhatsApp, SMS, E-Mail & Online-Beratung (Deutsch / Englisch)",
        "provenexpert": "https://www.provenexpert.com/herzensarbeit-anne-katrin-koch/"
    },
    "founder": {
        "name": "Anne-Katrin Koch",
        "full_name": "Anne-Katrin Koch Künzle",
        "born": "1967 in Bern",
        "practice_since": "2009",
        "experience_hours": "Über 5'000 Stunden Paartherapie und Einzelberatung",
        "family": "Verheiratet mit Mathias, Mutter von zwei erwachsenen Kindern (Ramon *2003 und Sarah *2006)",
        "method": "Körperzentrierte Herzensarbeit nach Safi Nidiaye",
        "portrait_hero": "images/portrait-anne-katrin-hero.jpg",
        "portrait_praxis": "images/portrait-anne-katrin-praxis.jpg",
        "qualifications": [
            "Ausbildung in Körperzentrierter Herzensarbeit bei Safi Nidiaye (2006–2008)",
            "Über 5'000 Stunden praktische Erfahrung in Paartherapie, Trennungs- und Lebensberatung (seit 2009)",
            "Weiterbildungen in Sexological Bodywork & Tantra-Massage",
            "Bewusstseins- und Wahrnehmungstraining am Monroe Institut in Virginia (USA)",
            "Patentierte Primarlehrerin (Kanton Bern) & Taketina-Rhythmuspädagogin",
            "Eigene tiefgreifende Heilerfahrung (Überwindung von schwerer Neurodermitis, Hashimoto und chronischen Entzündungen)"
        ]
    },
    "books_safi_nidiaye": [
        "Herz öffnen statt Kopf zerbrechen",
        "Aufwachen und Lachen",
        "Der entscheidende Schritt",
        "Das befreite Herz",
        "Gefühle sind zum Fühlen da",
        "Die 10 Herzensschlüssel"
    ],
    "testimonials": [
        {
            "author": "Michelle und Joshua Moser",
            "role": "Ehepaar · Paartherapie & Paarcoaching",
            "topic": "Paartherapie & Eheberatung",
            "quote": "Wir haben uns von der ersten Minute an bei Anne-Katrin wohl und verstanden gefühlt. Ihre einfühlsame, aber gleichzeitig sehr klare und strukturierte Art hat uns geholfen, aus festgefahrenen Mustern auszusteigen und wieder mit offenem Herzen aufeinander zuzugehen. Unsere Beziehung hat heute eine ganz neue Tiefe und Leichtigkeit."
        },
        {
            "author": "Sarah",
            "role": "Klientin · Paartherapie & Beziehungs-Klärung",
            "topic": "Paartherapie & Beziehungs-Klärung",
            "quote": "Durch die Sitzungen bei Anne-Katrin habe ich gelernt, meine wahren Gefühle hinter der Wut oder dem Rückzug wahrzunehmen und auszusprechen, ohne meinen Partner anzugreifen. Die Kombination aus Einzel- und Paarsitzungen war für uns der Schlüssel, um uns wirklich wieder zu verstehen."
        },
        {
            "author": "Maria & Simu",
            "role": "Paar · Paarcoaching in Härkingen",
            "topic": "Paartherapie & Kommunikation",
            "quote": "Anne-Katrin schafft einen Raum voller Vertrauen und Wärme. Sie ergreift keine Partei, sondern übersetzt zwischen uns, wenn wir uns im Kreis drehen. Besonders wertvoll waren für uns auch die konkreten Audio-Übungen für den Alltag zu Hause."
        },
        {
            "author": "Pascal",
            "role": "Klient · Paar- & Einzelberatung",
            "topic": "Paartherapie & Standortbestimmung",
            "quote": "Als Mann war ich zuerst skeptisch gegenüber einer Paartherapie. Doch Anne-Katrins bodenständige, unkomplizierte und direkt auf den Punkt kommende Begleitung hat mich sofort abgeholt. Ich habe enorm viel über mich selbst und über unsere Dynamik als Paar gelernt."
        },
        {
            "author": "Katharina Bär",
            "role": "Oftringen · Achtsamkeit & Selbstliebe",
            "topic": "Achtsamkeit & Selbstliebe lernen",
            "quote": "Die Körperzentrierte Herzensarbeit bei Anne-Katrin hat mein Leben nachhaltig verändert. Ich zerbreche mir nicht mehr endlos den Kopf, sondern spüre viel schneller, was in mir vorgeht und was ich wirklich brauche. Ich bin innerlich ruhiger, klarer und liebevoller mit mir selbst geworden."
        },
        {
            "author": "Nadine",
            "role": "Klientin · Trennungsverarbeitung",
            "topic": "Trennung verarbeiten & Neubeginn",
            "quote": "Nach der Trennung hatte ich das Gefühl, den Boden unter den Füssen zu verlieren. Anne-Katrin hat mich Schritt für Schritt durch den ersten Schock, den Schmerz und die Neuorientierung begleitet. Dass ich ihr zwischen den Sitzungen auch per WhatsApp schreiben durfte, gab mir enormen Halt."
        },
        {
            "author": "Barbara Wagner",
            "role": "Klientin · Trauerbegleitung",
            "topic": "Trauerbegleitung & Verlust",
            "quote": "In meiner tiefsten Trauer um einen geliebten Menschen durfte ich bei Anne-Katrin einfach sein, weinen, fühlen und atmen. Ihre Begleitung hat mir geholfen, den Schmerz nicht wegzudrücken, sondern ihn in eine stille, dankbare Verbundenheit und neue Lebenskraft zu verwandeln."
        },
        {
            "author": "Lisa (67)",
            "role": "Teilnehmerin · Frauen-Seminare & Workshops",
            "topic": "Frauen-Workshop «Kraftvoll Frau sein»",
            "quote": "Mit 67 Jahren durfte ich im Seminar von Anne-Katrin noch einmal ganz neue Türen in meinem Herzen öffnen. Die Atmosphäre unter den Frauen war so tragend, ehrlich und heilsam. Ich bin mit einem tiefen Gefühl von Frieden und neuer Lebensfreude nach Hause gereist."
        },
        {
            "author": "Romy",
            "role": "Teilnehmerin · Seminar Herzensarbeit",
            "topic": "Frauen-Workshop & Körperzentrierte Herzensarbeit",
            "quote": "Anne-Katrin leitet ihre Workshops mit einer wunderbaren Mischung aus Tiefe, feinem Humor und grosser Präsenz. Die angeleiteten Übungen wirken noch Wochen später im Alltag nach."
        },
        {
            "author": "Sarah (32)",
            "role": "Klientin · Trauer- & Lebensbegleitung",
            "topic": "Trauerbegleitung & Morgenrot",
            "quote": "Ich wusste nicht, wie es nach dem Verlust weitergehen soll. Bei Anne-Katrin habe ich Schritt für Schritt wieder Licht am Horizont gesehen und Vertrauen ins Leben gefasst."
        },
        {
            "author": "Susanne",
            "role": "Klientin · Achtsamkeit & Gefühlsarbeit",
            "topic": "Achtsamkeit & Fremdgefühle klären",
            "quote": "Zu erkennen, welche Gefühle wirklich meine eigenen sind und welche ich unbewusst von anderen übernommen habe, war für mich eine riesige Befreiung. Danke von Herzen, liebe Anne-Katrin!"
        },
        {
            "author": "Jürg Baiker",
            "role": "Leser & Klient · Herzensarbeit-Impulse",
            "topic": "Herzensarbeit-Impulse & Begleitung",
            "quote": "Deine Worte und Impulse treffen immer mitten ins Herz. Sie sind lebensnah, ehrlich und erinnern mich im Alltag immer wieder daran, innezuhalten und vom Kopf zurück ins Herz zu kommen."
        }
    ]
}

for target_dir in (V1_DIR, V2_DIR):
    (target_dir / "before.json").write_text(
        json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False), encoding="utf-8"
    )

base_company_data = {
    "slug": "herzensarbeit",
    "name": "Herzensarbeit — Anne-Katrin Koch",
    "company_name": "Herzensarbeit — Anne-Katrin Koch · Paartherapie & Beratung",
    "legal_name": "Herzensarbeit · Anne-Katrin Koch Künzle",
    "short_name": "Herzensarbeit",
    "claim": "Mit offenem Herzen lieben und leben",
    "subline": "Paartherapie, Trennungsberatung, Trauerbegleitung, Achtsamkeit & Frauen-Workshops in Härkingen (SO) und Online",
    "street": "Usserdorf 24",
    "zip": "4624",
    "city": "Härkingen",
    "canton": "SO",
    "country": "Schweiz",
    "email": "a.koch@herzensarbeit.ch",
    "phone": "+41 79 103 63 31",
    "phone_secondary": "079 103 63 31",
    "phone_clean": "+41791036331",
    "website": "https://herzensarbeit.ch",
    "industry": "Paartherapie, Eheberatung, Trennungs- & Trauerbegleitung, Frauen-Workshops",
    "industry_id": "coaching_beratung_therapie",
    "industry_label": "Praxis für Körperzentrierte Herzensarbeit, Paartherapie & Lebensberatung",
    "work_category_label": "Begleitungs-Angebote, Workshops & Klienten-Stimmen",
    "studio_title": "WEBPILOT STUDIO",
    "is_website_studio": True,
    "host_url": "https://vorschau.magnet-xs.ch/herzensarbeit-vollversion/cockpit?token=herzensarbeit2026",
    "host_jobs_url": "https://vorschau.magnet-xs.ch/herzensarbeit-vollversion/",
    "copyright": "© 2026 Herzensarbeit · Anne-Katrin Koch (Usserdorf 24, CH-4624 Härkingen SO). Alle Rechte vorbehalten.",
    "hosting_status": "Live-Betrieb & Hosting: Schweizer Edge · WebPilot Studio v4.0",
    "provenexpert_profile": "https://www.provenexpert.com/herzensarbeit-anne-katrin-koch/"
}

(V1_DIR / "company.json").write_text(json.dumps(base_company_data, indent=2, ensure_ascii=False), encoding="utf-8")
v1_config = dict(base_company_data)
v1_config.update({
    "preview_url": "https://vorschau.magnet-xs.ch/herzensarbeit-vollversion/",
    "cockpit_token": "herzensarbeit2026",
    "template": "coaching-therapy-flagship-v1",
    "pages": ["index.html", "angebot.html", "workshops.html", "ueber-mich.html", "kontakt.html"]
})
(V1_DIR / "config.json").write_text(json.dumps(v1_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V1_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-herzensarbeit",
    "public_slug": "herzensarbeit",
    "token": "herzensarbeit2026",
    "name": "Herzensarbeit — Anne-Katrin Koch",
    "Updated": "2026-11-05",
    "PagesCount": 5,
    "WorkshopsCount": 4,
    "TestimonialsCount": 12
}, indent=2, ensure_ascii=False), encoding="utf-8")

v2_company = dict(base_company_data)
v2_company.update({
    "slug": "herzensarbeit-v2",
    "name": "Herzensarbeit — Anne-Katrin Koch (Zeigeversion)",
    "host_url": "https://vorschau.magnet-xs.ch/herzensarbeit-v2/cockpit?token=herzensarbeit2026",
    "host_jobs_url": "https://vorschau.magnet-xs.ch/herzensarbeit-v2/"
})
(V2_DIR / "company.json").write_text(json.dumps(v2_company, indent=2, ensure_ascii=False), encoding="utf-8")
v2_config = dict(v2_company)
v2_config.update({
    "preview_url": "https://vorschau.magnet-xs.ch/herzensarbeit-v2/",
    "cockpit_token": "herzensarbeit2026",
    "template": "coaching-therapy-preview-v2",
    "pages": ["index.html", "kontakt.html"]
})
(V2_DIR / "config.json").write_text(json.dumps(v2_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V2_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-herzensarbeit-v2",
    "public_slug": "herzensarbeit-v2",
    "token": "herzensarbeit2026",
    "name": "Herzensarbeit — Anne-Katrin Koch (Zeigeversion / Vorschau-Entwurf)",
    "Updated": "2026-11-05",
    "PagesCount": 2,
    "WorkshopsCount": 4,
    "TestimonialsCount": 12
}, indent=2, ensure_ascii=False), encoding="utf-8")

print("Wrote before.json, company.json, config.json, site.json for V1 and V2.")

SHARED_CSS = """
    :root {
      --charcoal: #3d212b;
      --charcoal-deep: #2b161e;
      --charcoal-mid: #5a3744;
      --gold: #9b2c47;
      --gold-hover: #b43757;
      --gold-dark: #9b2c47;
      --gold-soft: #fdf2f5;
      --gold-border: #ebcad3;
      --crimson: #9b2c47;
      --crimson-soft: #fdf2f5;
      --green: #15803D;
      --green-soft: #DCFCE7;
      --bg-page: #fdf8f5;
      --bg-card: #FFFFFF;
      --bg-Warm: #f7ebe8;
      --text-main: #2b161e;
      --text-body: #4a2c36;
      --text-muted: #684551;
      --border-light: #ead8d3;
      --border-strong: #d5b8b0;
      --radius-sm: 4px;
      --radius-md: 8px;
      --shadow-sm: 0 2px 10px rgba(155, 44, 71, 0.06);
      --shadow-md: 0 12px 30px rgba(155, 44, 71, 0.10);
      --shadow-lg: 0 20px 44px rgba(155, 44, 71, 0.14);
      --container: 1180px;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    ::selection {
      background-color: rgba(154, 21, 54, 0.18);
      color: #18232C;
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

    /* Freistehende Marken-Kicker (#UI-01: Josefin Sans Bold, 0 JetBrains Mono, 0 //) */
    .section-kicker {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-family: 'Josefin Sans', sans-serif;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--gold-dark);
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
      background-color: var(--gold-dark);
      border-radius: 0px;
      flex-shrink: 0;
    }
    .section-kicker.kicker-light {
      color: var(--gold);
    }
    .section-kicker.kicker-light::before {
      background-color: var(--gold);
    }

    h1, h2, h3, h4 {
      font-family: 'Josefin Sans', sans-serif;
      color: var(--text-main);
      line-height: 1.2;
      letter-spacing: -0.01em;
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

    /* Sub-Topbar (Praxis Härkingen SO & Direktkontakt) */
    .top-bar {
      background-color: #f7ebe8;
      color: #4a2c36;
      font-size: 0.78rem;
      padding: 8px 0;
      border-bottom: 1px solid rgba(155, 44, 71, 0.14);
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
      background-color: #fdf2f5;
      color: #9b2c47;
      border: 1px solid rgba(155, 44, 71, 0.28);
      font-family: 'Josefin Sans', sans-serif;
      font-size: 0.72rem;
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
      color: #2b161e;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-height: 32px;
      padding: 5px 8px;
    }
    .top-bar-links a:hover {
      color: #9b2c47;
    }

    /* Sticky Main Header */
    .site-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background-color: rgba(255, 255, 255, 0.97);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border-light);
      box-shadow: 0 2px 12px rgba(24, 35, 44, 0.05);
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
      width: 52px;
      height: 52px;
      object-fit: contain;
      border-radius: var(--radius-sm);
      flex-shrink: 0;
    }
    .brand-text {
      display: flex;
      flex-direction: column;
    }
    .brand-name {
      font-family: 'Josefin Sans', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--charcoal-deep);
      letter-spacing: 0.01em;
      line-height: 1.15;
    }
    .brand-sub {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--gold-dark);
      text-transform: uppercase;
      letter-spacing: 0.05em;
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
      font-family: 'Josefin Sans', sans-serif;
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
      color: var(--gold-dark);
      background-color: var(--gold-soft);
      border-color: var(--gold-border);
    }
    .nav-link-preview {
      color: var(--text-muted);
      background-color: #F1F5F9;
      border: 1px dashed #94A3B8;
      font-size: 0.82rem;
    }
    .nav-link-preview:hover {
      color: var(--gold-dark);
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
      font-family: 'Josefin Sans', sans-serif;
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
      background-color: #9b2c47;
      color: #FFFFFF;
      border-color: #9b2c47;
      font-weight: 700;
    }
    .btn-cta-gold:hover {
      background-color: #b43757;
      color: #FFFFFF;
      border-color: #b43757;
      transform: translateY(-1px);
    }
    .btn-cta-primary {
      background-color: #9b2c47;
      color: #FFFFFF;
      border-color: #9b2c47;
    }
    .btn-cta-primary:hover {
      background-color: #b43757;
      color: #FFFFFF;
      border-color: #b43757;
    }
    .btn-cta-outline {
      background-color: #FFFFFF;
      color: #2b161e;
      border-color: var(--border-strong);
    }
    .btn-cta-outline:hover {
      border-color: #9b2c47;
      color: #9b2c47;
      background-color: var(--gold-soft);
    }
    .btn-cta-outline-light {
      background-color: #FFFFFF;
      color: #2b161e;
      border-color: rgba(155, 44, 71, 0.32);
    }
    .btn-cta-outline-light:hover {
      background-color: #fdf2f5;
      color: #9b2c47;
      border-color: #9b2c47;
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
      color: #2b161e;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }
    .mobile-drawer {
      display: none;
      flex-direction: column;
      gap: 8px;
      padding: 16px 24px 22px;
      background-color: #fdf8f5;
      border-top: 1px solid rgba(155, 44, 71, 0.18);
    }
    .mobile-drawer.open {
      display: flex;
    }
    .mobile-drawer a,
    .mobile-drawer button.mobile-nav-btn {
      font-family: 'Josefin Sans', sans-serif;
      font-size: 0.95rem;
      font-weight: 700;
      color: #2b161e;
      padding: 12px 14px;
      min-height: 44px;
      border-radius: var(--radius-sm);
      background-color: #FFFFFF;
      border: 1px solid rgba(155, 44, 71, 0.18);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      text-align: left;
      width: 100%;
      cursor: pointer;
    }
    .mobile-drawer button.mobile-nav-btn {
      color: #9b2c47;
      border-style: dashed;
      border-color: rgba(155, 44, 71, 0.45);
    }

    /* Hero Section — Hell, warm & herzlich wie herzensarbeit.ch */
    .hero-section {
      background: linear-gradient(135deg, #fdf8f5 0%, #f7ebe8 55%, #f3e2dd 100%);
      background-color: #fdf8f5;
      color: #2b161e;
      padding: 72px 0 84px;
      border-bottom: 1px solid rgba(155, 44, 71, 0.14);
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
      font-weight: 700;
      color: #2b161e;
      line-height: 1.14;
      margin-bottom: 18px;
    }
    .hero-title span {
      color: #9b2c47;
    }
    .hero-lead {
      font-size: 1.05rem;
      color: #4a2c36;
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
      background-color: rgba(255, 255, 255, 0.88);
      border: 1px solid rgba(155, 44, 71, 0.16);
      border-left: 3px solid #9b2c47;
      border-radius: var(--radius-sm);
      padding: 10px 14px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 2px;
      box-shadow: var(--shadow-sm);
    }
    .hero-badge-val {
      font-family: 'Josefin Sans', sans-serif;
      font-size: 0.92rem;
      font-weight: 700;
      color: #9b2c47;
    }
    .hero-badge-lbl {
      font-size: 0.78rem;
      color: #4a2c36;
      line-height: 1.35;
    }

    .hero-media-card {
      background-color: #FFFFFF;
      border: 1px solid rgba(155, 44, 71, 0.18);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-lg);
    }
    .hero-media-card img {
      width: 100%;
      height: 390px;
      object-fit: cover;
      object-position: center top;
    }
    .hero-media-caption {
      padding: 16px 20px;
      background-color: #fdf8f5;
      border-top: 1px solid rgba(155, 44, 71, 0.14);
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
      border-top: 4px solid var(--gold-dark);
    }
    .content-card.card-dark {
      background: linear-gradient(135deg, #fdf8f5 0%, #f7ebe8 100%);
      background-color: #f7ebe8;
      color: #2b161e;
      border-color: rgba(155, 44, 71, 0.24);
      border-top: 4px solid #9b2c47;
    }
    .content-card.card-dark h3 {
      color: #2b161e;
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
      font-family: 'Josefin Sans', sans-serif;
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
      background-color: #fdf2f5;
      color: #9b2c47;
      border: 1px solid rgba(155, 44, 71, 0.22);
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
      color: var(--gold-dark);
      flex-shrink: 0;
      margin-top: 3px;
    }
    .card-dark .check-item {
      color: #4a2c36;
    }
    .card-dark .check-item svg {
      color: #9b2c47;
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
      height: 210px;
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

    /* Founder Cards */
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
      grid-template-columns: 200px 1fr;
      gap: 22px;
      padding: 26px 26px 0;
      align-items: start;
    }
    .founder-portrait {
      width: 100%;
      height: 230px;
      object-fit: cover;
      object-position: center top;
      border-radius: var(--radius-md);
      border: 2px solid var(--gold-dark);
    }
    .founder-body {
      padding: 20px 26px 26px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex: 1;
      gap: 16px;
    }

    /* Testimonial Cards */
    .testimonial-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-top: 3px solid var(--gold-dark);
      border-radius: var(--radius-md);
      padding: 26px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 18px;
      height: 100%;
    }
    .testimonial-quote {
      font-size: 0.93rem;
      color: var(--text-body);
      line-height: 1.65;
      font-style: italic;
    }
    .testimonial-author-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding-top: 14px;
      border-top: 1px solid var(--border-light);
    }
    .testimonial-author {
      font-family: 'Josefin Sans', sans-serif;
      font-size: 0.98rem;
      font-weight: 700;
      color: var(--charcoal-deep);
    }
    .testimonial-role {
      font-size: 0.8rem;
      color: var(--gold-dark);
      font-weight: 600;
    }

    /* V2 Vorschau-Entwurf (Zeigeversion) Spezifische Styles (#UI-03 Kunden-Sprache) */
    .preview-scope-section {
      background-color: #f7ebe8;
      border-top: 2px dashed rgba(155, 44, 71, 0.32);
      border-bottom: 2px dashed rgba(155, 44, 71, 0.32);
      padding: 76px 0 88px;
    }
    .preview-scope-banner {
      background-color: #FFFFFF;
      color: #2b161e;
      border: 2px dashed #9b2c47;
      border-radius: var(--radius-md);
      padding: 28px 30px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-md);
    }
    .preview-module-card {
      background-color: #FFFFFF;
      border: 2px dashed #9b2c47;
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
      font-family: 'Josefin Sans', sans-serif;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
    }

    /* Footer */
    .site-footer {
      background-color: #f3e2dd;
      color: #2b161e;
      padding: 68px 0 36px;
      border-top: 3px solid #9b2c47;
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 1.3fr 1fr 1fr 1.1fr;
      gap: 36px;
      padding-bottom: 42px;
      border-bottom: 1px solid rgba(155, 44, 71, 0.16);
    }
    .footer-title {
      font-family: 'Josefin Sans', sans-serif;
      font-size: 0.94rem;
      font-weight: 700;
      color: #2b161e;
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
      color: #4a2c36;
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
      color: #9b2c47;
    }
    .footer-bottom {
      padding-top: 26px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      font-size: 0.82rem;
      color: #4a2c36;
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
      border: 2px solid var(--gold-dark);
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
      color: var(--gold-dark);
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
      border-left: 3px solid var(--gold-dark);
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
    }
    .contact-direct-role {
      font-family: 'Josefin Sans', sans-serif;
      font-size: 0.74rem;
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
      font-family: 'Josefin Sans', sans-serif;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--text-muted);
      text-align: center;
    }
    .wp-step-pill.active {
      background-color: #9b2c47;
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
      background-color: rgba(255, 255, 255, 0.16);
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
      border-color: var(--gold-dark);
      background-color: #FFFFFF;
    }
    .wp-role-tile.selected {
      border: 2px solid var(--gold-dark);
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
      background-color: #fdf2f5;
      color: #9b2c47;
      border: 1px solid rgba(155, 44, 71, 0.22);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .wp-role-title {
      font-family: 'Josefin Sans', sans-serif;
      font-size: 0.88rem;
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
      font-family: 'Josefin Sans', sans-serif;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--charcoal-deep);
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
      border-color: var(--gold-dark);
      box-shadow: 0 0 0 3px rgba(154, 21, 54, 0.16);
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
      font-family: 'Josefin Sans', sans-serif;
      font-size: 0.82rem;
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
      border-left: 4px solid var(--gold-dark);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      font-size: 0.8rem;
      color: #680D24;
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
      .founder-top {
        grid-template-columns: 1fr;
      }
      .header-actions .btn-cta {
        display: none;
      }
      .brand-link {
        flex-shrink: 1;
        min-width: 0;
      }
      .brand-text {
        min-width: 0;
      }
      .brand-name {
        font-size: 1rem;
      }
      .brand-sub {
        font-size: 0.64rem;
        line-height: 1.2;
      }
      .hero-media-card img {
        height: 270px;
      }
      .founder-portrait {
        height: 250px;
      }
      .wizard-card,
      .content-card {
        padding: 20px;
      }
    }
"""

SVG_CHECK = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>'
SVG_ARROW = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'
SVG_HEART = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>'
SVG_COMPASS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>'
SVG_SUN = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>'
SVG_AWARD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>'
SVG_USERS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
SVG_SPARKLES = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3Z"/></svg>'
SVG_BOOK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>'
SVG_MAP_PIN = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'
SVG_PHONE = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
SVG_MAIL = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'


def render_testimonials_grid(limit: int = 8) -> str:
    cards = []
    for idx, t in enumerate(BEFORE_INVENTORY["testimonials"][:limit]):
        cards.append(f"""
        <div class="testimonial-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">{t['topic']}</span>
              <span style="color:var(--gold-dark);font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;">Verifizierte Stimme #{idx+1}</span>
            </div>
            <p class="testimonial-quote">«{t['quote']}»</p>
          </div>
          <div class="testimonial-author-row">
            <div>
              <div class="testimonial-author">{t['author']}</div>
              <div class="testimonial-role">{t['role']}</div>
            </div>
            <a href="kontakt.html?thema=paartherapie" class="btn-cta btn-cta-outline btn-sm">
              <span>Gespräch anfragen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>""")
    return '<div class="grid-2">\n' + "\n".join(cards) + "\n      </div>"


def render_impressum_modal() -> str:
    return f"""
  <!-- IMPRESSUM & DATENSCHUTZ MODAL -->
  <div class="wp-modal-backdrop" id="wpImpressumModal" role="dialog" aria-modal="true" aria-labelledby="wpImpTitle" data-allow-scroll="true">
    <div class="wp-modal-dialog" data-allow-scroll="true">
      <button type="button" class="wp-modal-close" aria-label="Dialog schliessen" onclick="wpCloseImpressumModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="section-kicker">RECHTLICHE ANGABEN · PRAXIS HERZENSARBEIT</div>
      <h3 id="wpImpTitle" style="font-size:1.38rem;font-weight:700;margin-bottom:10px;">Impressum &amp; Datenschutz (Herzensarbeit — Anne-Katrin Koch)</h3>
      <div style="font-size:0.88rem;color:var(--text-body);line-height:1.62;display:flex;flex-direction:column;gap:12px;">
        <div style="background-color:var(--bg-page);border:1px solid var(--border-light);border-left:4px solid var(--gold-dark);padding:12px 14px;border-radius:var(--radius-sm);">
          <strong>Herzensarbeit · Anne-Katrin Koch Künzle</strong><br>
          Usserdorf 24 · CH-4624 Härkingen (Kanton Solothurn)<br>
          Telefon / WhatsApp / SMS: +41 79 103 63 31 · E-Mail: a.koch@herzensarbeit.ch
        </div>
        <p>
          <strong>Workshop-Standort Oensingen:</strong><br>
          Gemeinschaftspraxis Oensingen · Dünnernstrasse 2 · CH-4702 Oensingen (SO).
        </p>
        <p>
          <strong>Hinweis zu Begleitung &amp; Selbstheilung:</strong><br>
          In meiner Praxis arbeite ich mit Ihrem Bewusstsein, Ihren Gedanken und Gefühlen nach der Körperzentrierten Herzensarbeit (Safi Nidiaye). Ich stelle keine medizinischen Diagnosen und gebe keine Heilversprechen ab. Die Sitzungen ersetzen keine ärztliche Behandlung und werden nicht über die Krankenkasse abgerechnet.
        </p>
        <p>
          <strong>Datenschutz (CH-DSG / DSGVO):</strong><br>
          Alle Angaben aus dem 3-Schritte Smart-Anfrage-Assistenten werden streng vertraulich behandelt, ausschliesslich zur persönlichen Kontaktaufnahme und Vorbereitung Ihres Gesprächs verwendet und niemals an Dritte weitergegeben.
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
      if (fEl && focus) fEl.textContent = 'Begleitung & Umsetzung: ' + focus;
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
    nav_angebot = "active" if active_nav == "angebot" else ""
    nav_workshops = "active" if active_nav == "workshops" else ""
    nav_ueber = "active" if active_nav == "ueber-mich" else ""
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
  <meta name="description" content="Herzensarbeit — Anne-Katrin Koch. Praxis für Paartherapie, Eheberatung, Trennungsberatung, Trauerbegleitung, Achtsamkeit und Frauen-Workshops in Härkingen (SO) und Online.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@600;700&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <style>
{SHARED_CSS}
  </style>
</head>
<body>

  <!-- TOP INFO BAR -->
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div class="top-bar-left">
        <span class="top-bar-badge" data-slot="topbar_badge">PRAXIS HÄRKINGEN (SO) · USSERDORF 24 · &amp; ONLINE (DE / EN)</span>
        <span data-slot="topbar_sub">Seit 2009 · Über 5'000 Stunden Paartherapie &amp; Körperzentrierte Herzensarbeit</span>
      </div>
      <div class="top-bar-links">
        <a href="tel:+41791036331">{SVG_PHONE} <span>079 103 63 31</span></a>
        <a href="mailto:a.koch@herzensarbeit.ch">{SVG_MAIL} <span>a.koch@herzensarbeit.ch</span></a>
        <a href="https://www.provenexpert.com/herzensarbeit-anne-katrin-koch/" target="_blank" rel="noopener noreferrer">ProvenExpert Empfehlungen</a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="Herzensarbeit Anne-Katrin Koch Startseite">
        <img src="images/logo.png" alt="Herzensarbeit — Anne-Katrin Koch" class="brand-logo" width="52" height="52" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">HERZENSARBEIT</span>
          <span class="brand-sub" data-slot="brand_sub">ANNE-KATRIN KOCH · HÄRKINGEN &amp; ONLINE</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}">Startseite</a>
        <a href="angebot.html" class="nav-link {nav_angebot}">Paartherapie &amp; Angebot</a>
        <a href="workshops.html" class="nav-link {nav_workshops}">Frauen-Workshops</a>
        <a href="ueber-mich.html" class="nav-link {nav_ueber}">Über mich &amp; Stimmen</a>
        <a href="kontakt.html" class="nav-link {nav_kontakt}">Smart-Anfrage</a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" data-slot="header_cta">
          <span>Gespräch vereinbaren</span>
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
    <a href="angebot.html" onclick="wpCloseMobileMenu()">Paartherapie, Trennung, Trauer &amp; Achtsamkeit</a>
    <a href="workshops.html" onclick="wpCloseMobileMenu()">Frauen-Workshop-Reihe «Kraftvoll Frau sein»</a>
    <a href="ueber-mich.html" onclick="wpCloseMobileMenu()">Über Anne-Katrin Koch &amp; Klienten-Stimmen</a>
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
            <img src="images/logo.png" alt="Herzensarbeit Logo" width="48" height="48" loading="lazy" decoding="async" style="border-radius:4px;background:#FFFFFF;padding:2px;">
            <div>
              <div style="font-family:'Josefin Sans',sans-serif;font-weight:700;font-size:1.1rem;color:#2b161e;">HERZENSARBEIT</div>
              <div style="font-size:0.76rem;color:var(--gold);font-weight:700;">ANNE-KATRIN KOCH · SEIT 2009</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#4a2c36;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Mit offenem Herzen lieben und leben: Seit 2009 begleite ich Paare und Einzelpersonen in Härkingen (SO), Oensingen und Online mit Körperzentrierter Herzensarbeit nach Safi Nidiaye.
          </p>
          <div style="font-size:0.84rem;color:#2b161e;font-weight:600;">
            Praxis Herzensarbeit · Usserdorf 24 · CH-4624 Härkingen (SO)
          </div>
        </div>

        <div>
          <div class="footer-title">Begleitungs-Angebote</div>
          <ul class="footer-list">
            <li><a href="angebot.html#paartherapie">Paartherapie, Eheberatung &amp; Paarcoaching</a></li>
            <li><a href="angebot.html#trennung">Trennung verarbeiten &amp; Neubeginn</a></li>
            <li><a href="angebot.html#trauer">Trauerbegleitung &amp; Verlust</a></li>
            <li><a href="angebot.html#achtsamkeit">Achtsamkeit, Selbstliebe &amp; Selbstheilung</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Workshops &amp; Methode</div>
          <ul class="footer-list">
            <li><a href="workshops.html">Frauen-Workshops «Kraftvoll Frau sein»</a></li>
            <li><a href="workshops.html#module">Die 4 Tages-Module in Oensingen (SO)</a></li>
            <li><a href="angebot.html#methode">Körperzentrierte Herzensarbeit (Safi Nidiaye)</a></li>
            <li><a href="ueber-mich.html#stimmen">Alle 12 verifizierten Klienten-Stimmen</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; Rechtliches</div>
          <ul class="footer-list">
            <li><a href="tel:+41791036331">079 103 63 31 (Tel. / WhatsApp / SMS)</a></li>
            <li><a href="mailto:a.koch@herzensarbeit.ch">a.koch@herzensarbeit.ch</a></li>
            <li><a href="kontakt.html" style="color:var(--gold);font-weight:700;">3-Schritte Smart-Anfrage starten</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Herzensarbeit · Anne-Katrin Koch (Usserdorf 24, CH-4624 Härkingen SO).</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
          <a href="kontakt.html" style="color:var(--gold);font-weight:700;">Kennenlerngespräch &amp; Smart-Anfrage</a>
          <a href="ueber-mich.html#stimmen" style="color:#4a2c36;">Klienten-Stimmen</a>
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
  <meta name="description" content="Unverbindlicher Vorschau-Entwurf (Zeigeversion) für Herzensarbeit — Anne-Katrin Koch: 2 Beispiel-Seiten sind bereits ausgearbeitet — 3 weitere Themenbereiche folgen beim Ausbau.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@600;700&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <style>
{SHARED_CSS}
  </style>
</head>
<body>

  <!-- TOP INFO BAR -->
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div class="top-bar-left">
        <span class="top-bar-badge" data-slot="topbar_badge">PRAXIS HÄRKINGEN (SO) · USSERDORF 24 · &amp; ONLINE (DE / EN)</span>
        <span data-slot="topbar_sub">Seit 2009 · Über 5'000 Stunden Paartherapie &amp; Körperzentrierte Herzensarbeit</span>
      </div>
      <div class="top-bar-links">
        <a href="tel:+41791036331">{SVG_PHONE} <span>079 103 63 31</span></a>
        <a href="mailto:a.koch@herzensarbeit.ch">{SVG_MAIL} <span>a.koch@herzensarbeit.ch</span></a>
        <a href="https://www.provenexpert.com/herzensarbeit-anne-katrin-koch/" target="_blank" rel="noopener noreferrer">ProvenExpert Empfehlungen</a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER (ZEIGEVERSION MIT KUNDENFREUNDLICHEN VORSCHAU-HINWEISEN) -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="Herzensarbeit Anne-Katrin Koch Startseite">
        <img src="images/logo.png" alt="Herzensarbeit — Anne-Katrin Koch" class="brand-logo" width="52" height="52" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">HERZENSARBEIT</span>
          <span class="brand-sub" data-slot="brand_sub">ANNE-KATRIN KOCH · HÄRKINGEN &amp; ONLINE</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#15803D"/></svg>
          <span>Startseite (Ausgearbeitet)</span>
        </a>
        <button type="button" class="nav-link nav-link-preview" onclick="wpOpenBlueprintModal('Paartherapie, Trennungs- &amp; Trauerbegleitung im Detail', 'Alle 3-Etappen-Wege, Sitzungs-Pakete, Achtsamkeit, Selbstheilung &amp; Methode Safi Nidiaye', 'Anne-Katrin Koch')">
          <span>Paartherapie &amp; Angebot (Folgt beim Ausbau)</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" onclick="wpOpenBlueprintModal('Frauen-Workshop-Reihe «Kraftvoll Frau sein»', 'Alle 4 Tages-Module in Oensingen (Mutter, Vater, Sinnlichkeit, Weitsicht), Termine &amp; Early-Bird-Preise', 'Anne-Katrin Koch')">
          <span>Frauen-Workshops (Folgt beim Ausbau)</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" onclick="wpOpenBlueprintModal('Über Anne-Katrin Koch &amp; Alle Klienten-Stimmen', 'Persönlicher Heilungsweg, Ausbildungen seit 2006, Praxis Härkingen &amp; alle verifizierten Erfahrungsberichte', 'Anne-Katrin Koch')">
          <span>Über mich &amp; Stimmen (Folgt beim Ausbau)</span>
        </button>
        <a href="kontakt.html" class="nav-link {nav_kontakt}">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#15803D"/></svg>
          <span>Smart-Anfrage (Live-Demo)</span>
        </a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" data-slot="header_cta">
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
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu(); wpOpenBlueprintModal('Paartherapie, Trennungs- &amp; Trauerbegleitung im Detail', 'Alle 3-Etappen-Wege, Sitzungs-Pakete, Achtsamkeit &amp; Methode Safi Nidiaye', 'Anne-Katrin Koch')">
      <span>Paartherapie &amp; Angebot (Folgt beim Ausbau)</span>
      {SVG_ARROW}
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu(); wpOpenBlueprintModal('Frauen-Workshop-Reihe «Kraftvoll Frau sein»', 'Alle 4 Tages-Module in Oensingen (SO), Daten &amp; Konditionen', 'Anne-Katrin Koch')">
      <span>Frauen-Workshops (Folgt beim Ausbau)</span>
      {SVG_ARROW}
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu(); wpOpenBlueprintModal('Über Anne-Katrin Koch &amp; Alle Klienten-Stimmen', 'Persönlicher Weg, Ausbildungen &amp; alle Erfahrungsberichte', 'Anne-Katrin Koch')">
      <span>Über mich &amp; Stimmen (Folgt beim Ausbau)</span>
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
            <img src="images/logo.png" alt="Herzensarbeit Logo" width="48" height="48" loading="lazy" decoding="async" style="border-radius:4px;background:#FFFFFF;padding:2px;">
            <div>
              <div style="font-family:'Josefin Sans',sans-serif;font-weight:700;font-size:1.1rem;color:#2b161e;">HERZENSARBEIT</div>
              <div style="font-size:0.76rem;color:var(--gold);font-weight:700;">VORSCHAU-ENTWURF · 2 BEISPIEL-SEITEN LIVE</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#4a2c36;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Unverbindlicher Vorschau-Entwurf für Herzensarbeit — Anne-Katrin Koch: 2 Beispiel-Seiten (Startseite &amp; 3-Schritte Smart-Anfrage) sind bereits ausgearbeitet — 3 weitere Themenbereiche folgen beim gemeinsamen Ausbau.
          </p>
          <div style="font-size:0.84rem;color:#2b161e;font-weight:600;">
            Usserdorf 24 · CH-4624 Härkingen (SO) · Tel. 079 103 63 31
          </div>
        </div>

        <div>
          <div class="footer-title">Bereits ausgearbeitet (Live)</div>
          <ul class="footer-list">
            <li><a href="index.html">Startseite: Hero &amp; 6 Begleitungswege</a></li>
            <li><a href="index.html#kurzanalyse">Beziehungs-Kurzanalyse (5 Fragen)</a></li>
            <li><a href="index.html#ueber-anne-katrin">Vorstellung Anne-Katrin Koch</a></li>
            <li><a href="kontakt.html">3-Schritte Smart-Anfrage (Live-Demo)</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Folgen beim gemeinsamen Ausbau</div>
          <ul class="footer-list">
            <li><button type="button" onclick="wpOpenBlueprintModal('Paartherapie, Trennungs- &amp; Trauerbegleitung im Detail', 'Alle 3-Etappen-Wege, Sitzungs-Pakete, Achtsamkeit, Selbstheilung &amp; Methode Safi Nidiaye', 'Anne-Katrin Koch')">Paartherapie &amp; Begleitungs-Pakete</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Frauen-Workshop-Reihe «Kraftvoll Frau sein»', 'Alle 4 Tages-Module in Oensingen (SO), Daten &amp; Early-Bird-Preise', 'Anne-Katrin Koch')">Frauen-Workshops «Kraftvoll Frau sein»</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Über Anne-Katrin Koch &amp; Alle Klienten-Stimmen', 'Biografie, Heilungsweg, Ausbildungen &amp; alle 12 Erfahrungsberichte', 'Anne-Katrin Koch')">Über mich &amp; Alle Klienten-Stimmen</button></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; Rechtliches</div>
          <ul class="footer-list">
            <li><a href="tel:+41791036331">079 103 63 31 (Tel. / WhatsApp / SMS)</a></li>
            <li><a href="mailto:a.koch@herzensarbeit.ch">a.koch@herzensarbeit.ch</a></li>
            <li><a href="kontakt.html" style="color:var(--gold);font-weight:700;">3-Schritte Smart-Anfrage starten</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Herzensarbeit · Anne-Katrin Koch (Härkingen SO) · Unverbindlicher Vorschau-Entwurf (Zeigeversion).</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
          <a href="kontakt.html" style="color:var(--gold);font-weight:700;">Smart-Anfrage testen</a>
          <a href="index.html#weitere-themenbereiche" style="color:#4a2c36;">Weitere Themenbereiche</a>
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
      <div class="section-kicker">UNVERBINDLICHER VORSCHAU-ENTWURF FÜR HERZENSARBEIT.CH</div>
      <h3 id="wpBpTitle" style="font-size:1.36rem;font-weight:700;margin-bottom:8px;">Unverbindlicher Vorschau-Entwurf für Anne-Katrin Koch</h3>
      <p id="wpBpSub" style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
        In dieser <strong>Zeigeversion (2 Beispiel-Seiten ausgearbeitet)</strong> sehen Sie oben Ihre neue Startseite mit allen 6 Begleitungswegen, der Beziehungs-Kurzanalyse, Ihrer persönlichen Vorstellung sowie den live funktionierenden 3-Schritte Smart-Anfrage-Assistenten. Dieser vertiefte Themenbereich wird beim gemeinsamen Ausbau schlüsselfertig mit allen Originaltexten und Bildern ergänzt.
      </p>
      <div style="background-color:var(--gold-soft);border-left:4px solid var(--gold-dark);padding:12px 14px;border-radius:var(--radius-sm);font-size:0.86rem;margin-bottom:14px;">
        <div style="font-weight:700;color:var(--charcoal-deep);" id="wpBpCategory">Themenbereich: Vorbereitet für den gemeinsamen Ausbau</div>
        <div style="color:var(--text-body);margin-top:2px;" id="wpBpContact">Begleitung &amp; Umsetzung: Anne-Katrin Koch</div>
      </div>

      <div class="wp-modal-checklist">
        <div style="font-family:'Josefin Sans',sans-serif;font-size:0.8rem;font-weight:700;text-transform:uppercase;color:var(--charcoal-deep);">
          Was beim gemeinsamen Ausbau in diesem Themenbereich enthalten ist:
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Vollständige Ausarbeitung aller Angebote (Paartherapie in 3 Etappen, Trennungsverarbeitung, Trauerbegleitung, Achtsamkeit &amp; Selbstheilung inkl. Sitzungs-Paketen)</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Eigene Detailseite für die 4-teilige Frauen-Workshop-Reihe «Kraftvoll Frau sein» in Oensingen (SO) inkl. Daten, Early-Bird-Preisen &amp; Paket-Vorteil</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Persönliche Porträtseite über Anne-Katrin Koch, die Methode Körperzentrierte Herzensarbeit nach Safi Nidiaye &amp; alle verifizierten Klienten-Stimmen</span>
        </div>
      </div>

      <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:18px;">
        <button type="button" class="btn-cta btn-cta-primary btn-sm" onclick="wpCloseBlueprintModal()">
          <span>Verstanden — Vorschau weiter ansehen</span>
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
        <div class="section-kicker kicker-light" data-slot="hero_kicker">PRAXIS FÜR KÖRPERZENTRIERTE HERZENSARBEIT · HÄRKINGEN (SO) &amp; ONLINE</div>
        <h1 class="hero-title" data-slot="hero_title">
          Mit offenem Herzen <span>lieben und leben.</span>
        </h1>
        <p class="hero-lead" data-slot="hero_lead">
          Ob festgefahrene Beziehungskrise, schmerzhafte Trennung, tiefer Verlust oder der Wunsch nach mehr Selbstliebe und innerer Ruhe: Seit 2009 begleite ich Paare und Einzelpersonen in meiner Praxis in Härkingen (SO), in Oensingen und Online mit Wärme, Klarheit und über 5'000 Stunden Beratungserfahrung.
        </p>

        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
            <span>Unverbindliches Gespräch vereinbaren</span>
            {SVG_ARROW}
          </a>
          <a href="angebot.html" class="btn-cta btn-cta-outline-light" data-slot="hero_cta_secondary">
            <span>Alle Begleitungswege entdecken</span>
          </a>
        </div>

        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Über 5'000 Stunden</span>
            <span class="hero-badge-lbl">Erfahrung in Paartherapie &amp; Einzelbegleitung seit 2009</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Einzel- &amp; Paarsitzungen</span>
            <span class="hero-badge-lbl">Kombiniertes 3–5 Monate Paket inkl. WhatsApp-Begleitung</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Härkingen (SO) &amp; Online</span>
            <span class="hero-badge-lbl">Zentral am A1/A2-Kreuz (Usserdorf 24) oder per Video (DE/EN)</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Safi Nidiaye Methode</span>
            <span class="hero-badge-lbl">Herz öffnen statt Kopf zerbrechen — fühlen, klären &amp; lösen</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/portrait-anne-katrin-hero.jpg" alt="Anne-Katrin Koch — Praxis Herzensarbeit Härkingen SO" width="600" height="390" data-slot="hero_image">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Josefin Sans',sans-serif;font-weight:700;font-size:1.02rem;color:#2b161e;">Anne-Katrin Koch</div>
            <div style="font-size:0.8rem;color:#4a2c36;">Paartherapie, Trennungs- &amp; Trauerbegleitung · Praxis Härkingen (SO)</div>
          </div>
          <span class="top-bar-badge">SEIT 2009 IN EIGENER PRAXIS</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 6 BEGLEITUNGSWEGE (3x2 SYMMETRISCHES RASTER) -->
  <section data-section="kernangebote" id="kernangebote">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="pillars_kicker">WIE ICH SIE BEGLEITE · PRAXIS HÄRKINGEN, OENSINGEN &amp; ONLINE</div>
        <h2 class="section-title" data-slot="pillars_title">Sechs Wege zurück in Ihre Herzkraft und Verbundenheit</h2>
        <p class="section-desc" data-slot="pillars_desc">
          Wenn wir uns nur noch den Kopf zerbrechen, drehen wir uns im Kreis. In der Körperzentrierten Herzensarbeit verbinden wir klärende Gespräche mit dem bewussten Fühlen im Körper — damit echte Entlastung, Nähe und neue Perspektiven entstehen.
        </p>
      </div>

      <div class="grid-3">
        <!-- 1. Paartherapie -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/paarcoaching-hero.jpg" alt="Paartherapie, Eheberatung und Paarcoaching in Härkingen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Paare &amp; Einzelpersonen</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">3–5 Monate Begleitung</span>
              </div>
              <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:8px;">Paartherapie, Eheberatung &amp; Paarcoaching</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Raus aus dem Streit-Kreislauf, dem Schweigen oder der Entfremdung: Gemeinsam klären wir Ihre Beziehungskrise in 3 strukturierten Etappen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>4 Einzelsitzungen à 60 Min. pro Person + 4 Paarsitzungen à 90 Min.</span></div>
                <div class="check-item">{SVG_CHECK} <span>Persönlicher WhatsApp-Support &amp; Audio-Übungen für zu Hause</span></div>
              </div>
            </div>
            <a href="angebot.html#paartherapie" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zur Paartherapie</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 2. Trennung verarbeiten -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/trennung-beratung.jpg" alt="Trennung verarbeiten und Liebeskummer überwinden" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Neubeginn &amp; Halt</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">10 Sitzungen / 4 Monate</span>
              </div>
              <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:8px;">Trennung verarbeiten &amp; Neubeginn</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Wenn eine Beziehung zerbricht, steht plötzlich alles still. Ich begleite Sie sicher durch den ersten Schock zurück zu Ihrer eigenen inneren Stärke.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>3 Phasen: Schock verarbeiten, zu sich finden, neues Leben gestalten</span></div>
                <div class="check-item">{SVG_CHECK} <span>10 Sitzungen à 60 Min. inkl. WhatsApp-Begleitung im Alltag</span></div>
              </div>
            </div>
            <a href="angebot.html#trennung" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zur Trennungsberatung</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 3. Trauerbegleitung -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/trauerbegleitung-wasser.jpg" alt="Trauerbegleitung in Härkingen und Online" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Abschied &amp; Trost</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">8–10 Sitzungen</span>
              </div>
              <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:8px;">Trauerbegleitung &amp; Verlust</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                «Weil ich dich liebe, lebst du in meinem Herzen weiter.» Ein geschützter Raum, um den Schmerz bewusst zu fühlen und wieder Morgenrot zu sehen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>3 Abschnitte: Bewusst fühlen, Morgenrot spüren, neue Kraft schöpfen</span></div>
                <div class="check-item">{SVG_CHECK} <span>Einfühlsame Begleitung auf ca. 4 Monate mit Alltags-Impulsen</span></div>
              </div>
            </div>
            <a href="angebot.html#trauer" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zur Trauerbegleitung</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 4. Achtsamkeit & Selbstliebe -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/achtsamkeit-selbstliebe.jpg" alt="Achtsamkeit und Selbstliebe lernen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Innere Klarheit</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">8–10 Sitzungen</span>
              </div>
              <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:8px;">Achtsamkeit &amp; Selbstliebe lernen</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Lernen Sie, aus dem Gedankenkarussell auszusteigen, übernommene Fremdgefühle abzugeben und Ihren eigenen Selbstwert tief im Herzen zu verankern.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Innere Ordnung schaffen &amp; liebevolle Grenzen setzen</span></div>
                <div class="check-item">{SVG_CHECK} <span>Geführte Herzensarbeit-Übungen &amp; Audio-Anleitungen</span></div>
              </div>
            </div>
            <a href="angebot.html#achtsamkeit" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zu Achtsamkeit &amp; Selbstliebe</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 5. Selbstheilung & Körper-Harmonie -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/selbstheilung-natur.jpg" alt="Selbstheilung aktivieren und Körper-Harmonie" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Körper &amp; Bewusstsein</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Eigene Heilerfahrung</span>
              </div>
              <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:8px;">Selbstheilung &amp; Körper-Harmonie</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Unser Körper spricht mit uns. Erfahren Sie, wie unterdrückte Gefühle und Stress den Körper belasten — und wie innere Klärung die Regeneration stärkt.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Authentische Erfahrung (Weg aus Neurodermitis &amp; Hashimoto)</span></div>
                <div class="check-item">{SVG_CHECK} <span>Bewusstseins- &amp; Gefühlsarbeit zur Entlastung des Nervensystems</span></div>
              </div>
            </div>
            <a href="angebot.html#selbstheilung" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Details zu Selbstheilung</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- 6. Frauen-Workshop-Reihe Kraftvoll Frau sein -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/workshop-gruppe.jpg" alt="Frauen-Workshop-Reihe Kraftvoll Frau sein in Oensingen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Oensingen (SO) · 4–12 Frauen</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Ab CHF 257.– / Modul</span>
              </div>
              <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:8px;">Frauen-Workshops «Kraftvoll Frau sein»</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Vier kraftvolle Samstage in der Gemeinschaftspraxis Oensingen: Mutter- &amp; Vaterbindung klären, Sinnlichkeit leben und das Sorgenkarussell stoppen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Einzelmodul CHF 297.– (Early Bird CHF 257.–) · Alle 4 Module CHF 927.–</span></div>
                <div class="check-item">{SVG_CHECK} <span>Samstag 10:00–17:00 Uhr in geschützter Kleingruppe inkl. Handout</span></div>
              </div>
            </div>
            <a href="workshops.html" class="btn-cta btn-cta-gold btn-sm" style="width:100%;">
              <span>Alle 4 Workshop-Module ansehen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- BEZIEHUNGS-KURZANALYSE & 3 ETAPPEN -->
  <section data-section="kurzanalyse" id="kurzanalyse" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">ORIENTIERUNG FÜR PAARE &amp; EINZELPERSONEN · BEZIEHUNGS-KURZANALYSE</div>
        <h2 class="section-title">Wo stehen Sie gerade in Ihrer Partnerschaft?</h2>
        <p class="section-desc">
          Viele Paare warten lange, bis sie sich Unterstützung holen. Diese fünf ehrlichen Standort-Fragen aus meiner Praxis zeigen Ihnen sofort, wo der Schuh drückt — und wie wir gemeinsam Schritt für Schritt wieder Boden unter die Füsse bringen.
        </p>
      </div>

      <div class="grid-2">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">5 Standort-Fragen für Frauen &amp; Männer</span>
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 style="font-size:1.35rem;font-weight:700;margin-bottom:12px;">Die 5 Kernfragen der Beziehungs-Kurzanalyse</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:16px;">
              Nehmen Sie sich einen ruhigen Moment Zeit und spüren Sie bei jeder Frage kurz in Ihr Herz hinein:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>1. Gefühl der Verbundenheit:</strong> Fühlen Sie sich von Ihrer Partnerin / Ihrem Partner im Alltag wirklich gesehen, gehört und emotional verstanden?</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>2. Konflikte &amp; Gesprächskultur:</strong> Können Sie schwierige Themen ansprechen, ohne dass es sofort in Vorwürfe, Rechtfertigung oder eisiges Schweigen kippt?</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>3. Nähe, Zärtlichkeit &amp; Sinnlichkeit:</strong> Erleben Sie körperliche Nähe und Sexualität als lebendig und nährend — oder eher als Pflicht, Druck oder Rückzug?</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>4. Eigener Freiraum &amp; Grenzen:</strong> Bleiben Sie in der Beziehung sich selbst treu, oder passen Sie sich aus Angst vor Konflikten ständig an?</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>5. Gemeinsame Zukunftsperspektive:</strong> Spüren Sie trotz der aktuellen Krise noch den Wunsch, herauszufinden, was zwischen Ihnen wieder möglich ist?</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=paartherapie" class="btn-cta btn-cta-primary" style="width:100%;">
            <span>Standortgespräch zu Ihrer Beziehung anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-dark">
          <div>
            <div class="card-badge-row">
              <span class="top-bar-badge">BEWÄHRTER 3-ETAPPEN-PROZESS</span>
              <span class="icon-box">{SVG_COMPASS}</span>
            </div>
            <h3 style="font-size:1.35rem;font-weight:700;margin-bottom:12px;">So läuft die Paarbegleitung bei mir ab</h3>
            <p style="font-size:0.92rem;color:#4a2c36;margin-bottom:16px;">
              Statt endloser Sitzungen ohne roten Faden begleite ich Sie über 3 bis 5 Monate in einer klaren Kombination aus Einzel- und Paargesprächen:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Etappe 1 — Klärung der Beziehungskrise:</strong> Wir schauen uns ehrlich an, wo Sie stehen, welche Verletzungen und Schutzmechanismen wirken und warum Gespräche bisher eskalieren.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Etappe 2 — Wo will ich hin? (Einzelsitzungen):</strong> In je 4 geschützten Einzelsitzungen (à 60 Min.) klärt jede Person ihre eigenen Gefühle, Prägungen und Bedürfnisse.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Etappe 3 — Aufbauende Schritte (Paarsitzungen):</strong> In 4 gemeinsamen Paarsitzungen (à 90 Min.) übersetzen wir das Erkannte in eine neue, ehrliche und herzensoffene Verbindung.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Begleitung zwischen den Terminen:</strong> Kurze Rückfragen per WhatsApp sowie alltagstaugliche Audio- und Text-Übungen geben Ihnen Sicherheit im Alltag.</span></div>
            </div>
          </div>
          <a href="angebot.html#paartherapie" class="btn-cta btn-cta-gold" style="width:100%;">
            <span>Das 3–5 Monate Paarpaket im Detail ansehen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- PERSÖNLICHE VORSTELLUNG ANNE-KATRIN KOCH -->
  <section data-section="ueber-anne-katrin" id="ueber-anne-katrin">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">IHRE BEGLEITERIN · ANNE-KATRIN KOCH</div>
        <h2 class="section-title">«Herz öffnen statt Kopf zerbrechen» — seit 2009 für Sie da</h2>
        <p class="section-desc">
          Ich bin 1967 in Bern geboren, verheiratet mit Mathias und Mutter von zwei erwachsenen Kindern (Ramon *2003 und Sarah *2006). Was ich weitergebe, habe ich selbst durchlebt und in über 5'000 Beratungsstunden vertieft.
        </p>
      </div>

      <div class="grid-2">
        <div class="founder-card">
          <div class="founder-top">
            <img src="images/portrait-anne-katrin-praxis.jpg" alt="Anne-Katrin Koch Porträt Praxis Härkingen" class="founder-portrait" loading="lazy" decoding="async">
            <div>
              <span class="meta-badge" style="margin-bottom:8px;">Praxis Härkingen (SO) &amp; Online</span>
              <h3 style="font-size:1.35rem;font-weight:700;margin-bottom:6px;">Anne-Katrin Koch</h3>
              <p style="font-size:0.86rem;color:var(--gold-dark);font-weight:700;margin-bottom:10px;">
                Körperzentrierte Herzensarbeit nach Safi Nidiaye · Paar- &amp; Lebensberatung
              </p>
              <p style="font-size:0.88rem;color:var(--text-body);line-height:1.58;">
                Nach meiner Erstausbildung als Primarlehrerin und Taketina-Rhythmuspädagogin führte mich mein eigener Heilungsweg (Überwindung von schwerer Neurodermitis, Hashimoto und chronischen Entzündungen) 2006 direkt zu Safi Nidiaye.
              </p>
            </div>
          </div>
          <div class="founder-body">
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>2006–2008:</strong> Fundierte Ausbildung in Körperzentrierter Herzensarbeit bei Safi Nidiaye</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Seit 2009:</strong> Eigene Praxis in Härkingen (SO) mit über 5'000 dokumentierten Beratungsstunden</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Vertiefungen:</strong> Sexological Bodywork &amp; Tantra-Massage sowie Bewusstseinstraining am Monroe Institut (Virginia, USA)</span></div>
            </div>
            <a href="ueber-mich.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Mehr über meinen Weg &amp; meine Arbeitsweise</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/praxis-sessel.jpg" alt="Einblick in den Praxisraum Usserdorf 24 in Härkingen SO" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Usserdorf 24 · CH-4624 Härkingen</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Zentral am A1/A2-Kreuz</span>
              </div>
              <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:8px;">Ein geschützter Ort zum Durchatmen — vor Ort oder Online</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Meine Praxis im Usserdorf 24 in Härkingen liegt nur wenige Minuten vom Autobahnkreuz A1/A2 entfernt und ist aus dem Raum Olten, Solothurn, Aarau, Basel, Bern, Luzern und Zürich rasch erreichbar.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Ruhige, diskrete Praxis-Atmosphäre mit kostenlosen Parkplätzen direkt vor dem Haus</span></div>
                <div class="check-item">{SVG_CHECK} <span>Ortsunabhängige Online-Sitzungen per Video-Call auf Deutsch und Englisch</span></div>
                <div class="check-item">{SVG_CHECK} <span>Frauen-Workshops in der Gemeinschaftspraxis Oensingen (Dünnernstrasse 2)</span></div>
              </div>
            </div>
            <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Termin in Härkingen oder Online anfragen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- VERIFIZIERTE KLIENTEN-STIMMEN -->
  <section data-section="klientenstimmen" id="klientenstimmen" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">ECHTE ERFAHRUNGEN · VERIFIZIERTE KLIENTEN-STIMMEN</div>
        <h2 class="section-title">Was Paare und Einzelpersonen über die Begleitung sagen</h2>
        <p class="section-desc">
          Vertrauen entsteht durch echte Erfahrungen. Hier lesen Sie ausgewählte Rückmeldungen von Paaren, Einzelklientinnen und Workshop-Teilnehmerinnen aus meiner Praxis.
        </p>
      </div>

      {render_testimonials_grid(6)}

      <div style="margin-top:32px;display:flex;justify-content:center;gap:14px;flex-wrap:wrap;">
        <a href="ueber-mich.html#stimmen" class="btn-cta btn-cta-primary">
          <span>Alle 12 Klienten-Stimmen lesen</span>
          {SVG_ARROW}
        </a>
        <a href="https://www.provenexpert.com/herzensarbeit-anne-katrin-koch/" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-outline">
          <span>ProvenExpert Bewertungsprofil öffnen</span>
        </a>
      </div>
    </div>
  </section>

  <!-- BEZIEHUNGSIMPULSE & RATGEBER-ARTIKEL -->
  <section data-section="blog-impulse" id="blog-impulse">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">IMPULSE FÜR DEN ALLTAG · AUS DEM HERZENSARBEIT-BLOG</div>
        <h2 class="section-title">Drei praxisnahe Impulse für lebendige Beziehungen</h2>
        <p class="section-desc">
          Oft sind es wiederkehrende Muster, die zwei Menschen voneinander entfernen. Diese drei Kernthemen begegnen mir in der Paarberatung besonders häufig:
        </p>
      </div>

      <div class="grid-3">
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/blog-streit-kreislauf.jpg" alt="Ausstieg aus dem Streit-Kreislauf in der Beziehung" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <span class="meta-badge" style="margin-bottom:10px;">Beziehungsimpuls #1</span>
              <h3 style="font-size:1.2rem;font-weight:700;margin-bottom:8px;">Ausstieg aus dem Streit-Kreislauf: Vom Vorwurf zum Gefühl</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">
                Hinter fast jedem Angriff steckt ein verletztes Bedürfnis oder eine alte Angst. Wenn wir aufhören, recht haben zu wollen, und stattdessen aussprechen, was uns im Innersten berührt, löst sich der Widerstand.
              </p>
            </div>
            <a href="angebot.html#paartherapie" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Wie wir Konflikte klären</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/blog-schweigen-warnzeichen.jpg" alt="Wenn Paare sich nichts mehr zu sagen haben" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <span class="meta-badge" style="margin-bottom:10px;">Beziehungsimpuls #2</span>
              <h3 style="font-size:1.2rem;font-weight:700;margin-bottom:8px;">Wenn Paare schweigen: Wie aus Distanz wieder Nähe wird</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">
                Schweigen und emotionaler Rückzug sind oft leise Schutzmauern, um weitere Verletzungen zu vermeiden. In einem geschützten Rahmen lernen Sie, diese Mauern behutsam abzubauen.
              </p>
            </div>
            <a href="angebot.html#paartherapie" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Wieder ins Gespräch finden</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/blog-grenzen-setzen.png" alt="Gesunde Grenzen setzen in der Partnerschaft" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <span class="meta-badge" style="margin-bottom:10px;">Beziehungsimpuls #3</span>
              <h3 style="font-size:1.2rem;font-weight:700;margin-bottom:8px;">Gesunde Grenzen setzen — aus Selbstliebe statt aus Härte</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">
                Wer immer nur Harmonie wahrt und die eigenen Bedürfnisse zurückstellt, verliert irgendwann die Freude und Nähe. Ein klares «Nein» aus offenem Herzen ist gleichzeitig ein ehrliches «Ja» zu sich selbst.
              </p>
            </div>
            <a href="angebot.html#achtsamkeit" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Selbstliebe &amp; Klarheit stärken</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ABSCHLUSS-CTA -->
  <section data-section="cta-banner" style="background:linear-gradient(135deg, #fdf8f5 0%, #f7ebe8 55%, #f3e2dd 100%);background-color:#f7ebe8;color:#2b161e;border-top:1px solid rgba(155, 44, 71, 0.14);border-bottom:1px solid rgba(155, 44, 71, 0.14);padding:72px 0;">
    <div class="container">
      <div class="grid-2" style="align-items:center;">
        <div>
          <div class="section-kicker kicker-light">ERSTER SCHRITT · UNVERBINDLICH &amp; VERTRAULICH</div>
          <h2 style="font-size:clamp(1.8rem,3vw,2.4rem);font-weight:700;color:#2b161e;margin-bottom:12px;">
            Bereit für ein ehrliches Gespräch von Herz zu Herz?
          </h2>
          <p style="font-size:0.98rem;color:#4a2c36;line-height:1.65;">
            Nutzen Sie unseren geführten 3-Schritte Smart-Anfrage-Assistenten für eine rasche Standortbestimmung oder melden Sie sich direkt per Telefon, WhatsApp oder E-Mail bei mir.
          </p>
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:flex-start;">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>3-Schritte Smart-Anfrage starten</span>
            {SVG_ARROW}
          </a>
          <a href="tel:+41791036331" class="btn-cta btn-cta-outline-light">
            {SVG_PHONE}
            <span>Direktwahl 079 103 63 31</span>
          </a>
        </div>
      </div>
    </div>
  </section>
"""

# ==============================================================================
# SEITEN-INHALTE: V1 ANGEBOT & METHODE (angebot.html)
# ==============================================================================
V1_ANGEBOT_BODY = f"""
  <!-- HERO ANGEBOT -->
  <section class="hero-section" data-section="angebot-hero" style="padding:64px 0 72px;">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">PAARTHERAPIE, TRENNUNG, TRAUER, ACHTSAMKEIT &amp; SELBSTHEILUNG</div>
        <h1 class="hero-title">
          Begleitung, die in die <span>Tiefe geht und im Alltag trägt.</span>
        </h1>
        <p class="hero-lead">
          Jede Lebenskrise und jede Beziehung hat ihre eigene Geschichte. Deshalb arbeite ich nicht mit starren Schablonen, sondern begleite Sie in überschaubaren, klar strukturierten Paketen über 3 bis 5 Monate — vor Ort in Härkingen (SO) oder Online auf Deutsch und Englisch.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html?thema=paartherapie" class="btn-cta btn-cta-gold">
            <span>Passendes Begleitungs-Paket anfragen</span>
            {SVG_ARROW}
          </a>
          <a href="#methode" class="btn-cta btn-cta-outline-light">
            <span>Methode Safi Nidiaye &amp; 6 Bücher</span>
          </a>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/paarcoaching-hero.jpg" alt="Paartherapie und Eheberatung bei Anne-Katrin Koch in Härkingen" width="600" height="360">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Josefin Sans',sans-serif;font-weight:700;font-size:1.02rem;color:#2b161e;">Praxis Härkingen &amp; Online</div>
            <div style="font-size:0.8rem;color:#4a2c36;">Einzelsitzungen (60 Min.) · Paarsitzungen (90 Min.) · WhatsApp-Support</div>
          </div>
          <span class="top-bar-badge">DEUTSCH &amp; ENGLISCH</span>
        </div>
      </div>
    </div>
  </section>

  <!-- 1. PAARTHERAPIE, EHEBERATUNG & PAARCOACHING -->
  <section data-section="paartherapie" id="paartherapie">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">SCHWERPUNKT 1 · FÜR PAARE &amp; EHEPARTNER</div>
        <h2 class="section-title">Paartherapie, Eheberatung &amp; Paarcoaching in 3 Etappen</h2>
        <p class="section-desc">
          Wenn Gespräche im Streit enden, Vertrauen erschüttert wurde oder Sie sich nur noch wie eine Wohngemeinschaft fühlen: In 3 klaren Etappen schaffen wir Raum für ehrliche Klärung und echte Wiederannäherung.
        </p>
      </div>

      <div class="grid-3" style="margin-bottom:28px;">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Etappe 1</span>
              <span class="icon-box">{SVG_COMPASS}</span>
            </div>
            <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:8px;">1. Klärung der Beziehungskrise</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Wir legen offen, wo Sie als Paar gerade stehen, welche unausgesprochenen Verletzungen wirken und warum bisherige Lösungsversuche immer wieder am gleichen Punkt gescheitert sind.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Schutzmechanismen (Rückzug, Angriff, Anpassung) erkennen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Allparteiliche Übersetzung ohne Schuldzuweisungen</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=paartherapie" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Etappe 1 im Erstgespräch starten</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Etappe 2</span>
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:8px;">2. Wo will ich hin? (Einzelsitzungen)</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              In geschützten Einzelsitzungen schaut jede Person für sich nach innen: Welche eigenen Prägungen aus der Herkunftsfamilie bringe ich mit? Was fühle und brauche ich wirklich?
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Je 4 Einzelsitzungen à 60 Minuten pro Partnerin / Partner</span></div>
              <div class="check-item">{SVG_CHECK} <span>Körperzentrierte Herzensarbeit zur Klärung eigener Gefühle</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=paartherapie" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Einzel- &amp; Paarkombination anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Etappe 3</span>
              <span class="icon-box">{SVG_USERS}</span>
            </div>
            <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:8px;">3. Aufbauende Schritte (Paarsitzungen)</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Mit der gewonnenen inneren Klarheit begegnen Sie sich in den Paarsitzungen neu: Sie lernen, sich mit offenem Herzen zuzuhören, Grenzen zu achten und Nähe neu zu beleben.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>4 gemeinsame Paarsitzungen à 90 Minuten</span></div>
              <div class="check-item">{SVG_CHECK} <span>Konkrete Übungen für Kommunikation, Vertrauen &amp; Sinnlichkeit</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=paartherapie" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Paarbegleitung vereinbaren</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>

      <div class="content-card card-dark">
        <div class="grid-2" style="align-items:center;">
          <div>
            <span class="top-bar-badge" style="margin-bottom:10px;">DAS KOMPLETTE PAAR-BEGLEITUNGSPAKET (3–5 MONATE)</span>
            <h3 style="font-size:1.4rem;font-weight:700;margin-bottom:10px;">Was im 3–5 Monate Paket für Paare alles enthalten ist</h3>
            <p style="font-size:0.92rem;color:#4a2c36;">
              Nachhaltige Veränderung in einer Beziehung braucht Verlässlichkeit und Begleitung auch zwischen den Terminen — damit Sie im Alltag nicht wieder in alte Muster zurückfallen:
            </p>
          </div>
          <div class="check-list">
            <div class="check-item">{SVG_CHECK} <span><strong>8 Einzelsitzungen à 60 Min.</strong> (je 4 Sitzungen pro Person für persönliche Themen)</span></div>
            <div class="check-item">{SVG_CHECK} <span><strong>4 Paarsitzungen à 90 Min.</strong> (gemeinsame Klärung, Dialog &amp; Neuausrichtung)</span></div>
            <div class="check-item">{SVG_CHECK} <span><strong>WhatsApp-Support zwischen den Sitzungen</strong> bei akuten Fragen oder Krisenmomenten</span></div>
            <div class="check-item">{SVG_CHECK} <span><strong>Geführte Audio- &amp; Text-Übungen</strong> für die Vertiefung zu Hause · Vor Ort in Härkingen oder Online</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. TRENNUNG VERARBEITEN & 3. TRAUERBEGLEITUNG -->
  <section data-section="trennung-trauer" id="trennung" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">SCHWERPUNKT 2 &amp; 3 · WENN DAS LEBEN SICH VERÄNDERT</div>
        <h2 class="section-title">Trennung verarbeiten &amp; einfühlsame Trauerbegleitung</h2>
        <p class="section-desc">
          Abschiede gehören zu den tiefsten Einschnitten im Leben. Ich begleite Sie Schritt für Schritt durch den Schmerz, damit Sie Ihren Boden wieder spüren und mit neuer Zuversicht nach vorne blicken können.
        </p>
      </div>

      <div class="grid-2">
        <!-- Trennung -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/trennung-beratung.jpg" alt="Trennung verarbeiten in 3 Phasen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Trennungsberatung</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">10 Sitzungen à 60 Min. / 4 Monate</span>
              </div>
              <h3 style="font-size:1.35rem;font-weight:700;margin-bottom:10px;">Trennung verarbeiten — in 3 Phasen zurück ins Leben</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:14px;">
                Ob Sie verlassen wurden oder selbst gegangen sind: Eine Trennung wirbelt Emotionen, Selbstwert und Lebensplanung durcheinander.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span><strong>Phase 1 — Schock verarbeiten:</strong> Auffangen im akuten Schmerz, Gefühle von Ohnmacht, Wut oder Angst sicher durchfühlen und beruhigen.</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Phase 2 — Zu sich selber finden:</strong> Alte Verstrickungen lösen, die eigene Mitte wieder spüren und gestärkt bei sich ankommen.</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Phase 3 — Schritte ins neue Leben:</strong> Neue Lebensfreude, Vertrauen und klare Perspektiven für Ihre Zukunft aufbauen.</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Paket-Umfang:</strong> 10 Sitzungen à 60 Min. verteilt auf 4 Monate inkl. WhatsApp-Support &amp; Audio-Übungen.</span></div>
              </div>
            </div>
            <a href="kontakt.html?thema=einzelberatung" class="btn-cta btn-cta-primary" style="width:100%;">
              <span>Begleitung bei Trennung anfragen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- Trauerbegleitung -->
        <div class="pillar-card" id="trauer">
          <div class="pillar-img-wrap">
            <img src="images/trauerbegleitung-wasser.jpg" alt="Trauerbegleitung — Weil ich dich liebe, lebst du in meinem Herzen weiter" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Trauerbegleitung</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">8–10 Sitzungen à 60 Min. / ca. 4 Monate</span>
              </div>
              <h3 style="font-size:1.35rem;font-weight:700;margin-bottom:10px;">«Weil ich dich liebe, lebst du in meinem Herzen weiter»</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:14px;">
                Nach dem Verlust eines geliebten Menschen braucht die Seele Zeit und einen Ort, an dem jede Träne und jedes Gefühl willkommen ist.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span><strong>Abschnitt 1 — Bewusst fühlen:</strong> Dem Schmerz, der Leere und der Sehnsucht in einem geschützten Rahmen Raum geben, ohne sie wegzudrücken.</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Abschnitt 2 — Morgenrot:</strong> Spüren, wie sich die schwere Trauer wandelt in eine stille, liebevolle Verbundenheit im Herzen.</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Abschnitt 3 — Neue Kraft:</strong> Schrittweise Rückkehr in den Alltag mit neuer innerer Tragkraft und Zuversicht.</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Paket-Umfang:</strong> 8 bis 10 Sitzungen à 60 Min. über ca. 4 Monate inkl. WhatsApp-Begleitung.</span></div>
              </div>
            </div>
            <a href="kontakt.html?thema=einzelberatung" class="btn-cta btn-cta-primary" style="width:100%;">
              <span>Gespräch zur Trauerbegleitung anfragen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 4. ACHTSAMKEIT & SELBSTLIEBE + 5. SELBSTHEILUNG -->
  <section data-section="achtsamkeit-selbstheilung" id="achtsamkeit">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">SCHWERPUNKT 4 &amp; 5 · INNERE ORDNUNG &amp; KÖRPER-HARMONIE</div>
        <h2 class="section-title">Achtsamkeit, Selbstliebe &amp; Aktivierung der Selbstheilung</h2>
        <p class="section-desc">
          «Selbstliebe ist das Fundament für jede erfüllte Beziehung — zu anderen Menschen genauso wie zu unserem eigenen Körper.»
        </p>
      </div>

      <div class="grid-2">
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/achtsamkeit-selbstliebe.jpg" alt="Achtsamkeit und Selbstliebe lernen bei Anne-Katrin Koch" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Achtsamkeit &amp; Selbstliebe</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">8–10 Sitzungen / ca. 4 Monate</span>
              </div>
              <h3 style="font-size:1.32rem;font-weight:700;margin-bottom:8px;">In 3 Schritten zu echter Selbstliebe und innerer Ruhe</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Viele feinfühlige Menschen nehmen unbewusst Stimmungen, Erwartungen und Fremdgefühle aus ihrem Umfeld auf, bis sie sich selbst kaum noch spüren.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span><strong>1. Achtsamkeit im Alltag:</strong> Innehalten, aus dem Kopf in den Körper sinken und ehrlich wahrnehmen, was jetzt gerade in Ihnen lebendig ist.</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>2. Klären, ordnen &amp; Fremdgefühle zurückgeben:</strong> Erkennen, welche Lasten gar nicht zu Ihnen gehören, und diese innerlich in Frieden zurückgeben.</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>3. Selbstwert stärken &amp; schöne Gefühle verankern:</strong> Würde, Freude und Selbstannahme spürbar im Körper verankern.</span></div>
              </div>
            </div>
            <a href="kontakt.html?thema=einzelberatung" class="btn-cta btn-cta-primary" style="width:100%;">
              <span>Achtsamkeits-Begleitung anfragen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <div class="pillar-card" id="selbstheilung">
          <div class="pillar-img-wrap">
            <img src="images/selbstheilung-natur.jpg" alt="Selbstheilung und Körper-Harmonie" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Selbstheilung &amp; Bewusstsein</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">8–10 Sitzungen / ca. 4 Monate</span>
              </div>
              <h3 style="font-size:1.32rem;font-weight:700;margin-bottom:8px;">Wenn der Körper ruft: Gedanken, Gefühle &amp; Regeneration</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Aus eigener Erfahrung weiss ich, wie eng seelischer Druck und körperliche Symptome zusammenhängen: Über Jahre litt ich selbst unter schwerer Neurodermitis, Hashimoto und chronischen Entzündungen — bis ich lernte, auf die Botschaften meines Körpers zu hören.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span><strong>Seelische Ursachen erforschen:</strong> Welche ungelebten Gefühle oder Daueranspannungen drücken sich über den Körper aus?</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Nervensystem entlasten:</strong> Durch bewusste Herzensarbeit innere Ruhe und Selbstheilungskräfte unterstützen.</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Transparenter Hinweis:</strong> Ich arbeite mit Ihrem Bewusstsein, Ihren Gedanken und Gefühlen (keine medizinische Diagnose, keine Abrechnung über die Krankenkasse).</span></div>
              </div>
            </div>
            <a href="kontakt.html?thema=einzelberatung" class="btn-cta btn-cta-primary" style="width:100%;">
              <span>Gespräch zu Selbstheilung vereinbaren</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 6. METHODE KÖRPERZENTRIERTE HERZENSARBEIT NACH SAFI NIDIAYE & 6 BÜCHER -->
  <section data-section="methode-safi-nidiaye" id="methode" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">FUNDAMENT SEIT 2006 · KÖRPERZENTRIERTE HERZENSARBEIT</div>
        <h2 class="section-title">Die Methode nach Safi Nidiaye &amp; 6 inspirierende Bücher</h2>
        <p class="section-desc">
          Von 2006 bis 2008 absolvierte ich meine Ausbildung direkt bei Safi Nidiaye, der Begründerin der Körperzentrierten Herzensarbeit. Das Kernprinzip lautet: «Gefühle sind zum Fühlen da — nicht zum Wegdenken.»
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Buch-Empfehlung #1 &amp; #2</span>
              <span class="icon-box">{SVG_BOOK}</span>
            </div>
            <h3 style="font-size:1.18rem;font-weight:700;margin-bottom:8px;">«Herz öffnen statt Kopf zerbrechen» &amp; «Aufwachen und Lachen»</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Der ideale Einstieg in die Körperzentrierte Herzensarbeit: Wie wir aufhören, Probleme im Verstand endlos zu wälzen, und stattdessen durch bewusstes Spüren im Körper sofortige innere Lösung erfahren.
            </p>
          </div>
          <span style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Autorin: Safi Nidiaye</span>
        </div>

        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Buch-Empfehlung #3 &amp; #4</span>
              <span class="icon-box">{SVG_BOOK}</span>
            </div>
            <h3 style="font-size:1.18rem;font-weight:700;margin-bottom:8px;">«Der entscheidende Schritt» &amp; «Das befreite Herz»</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Warum blosse Einsicht oft nicht reicht und welcher innere Schritt wirklich befreit: Ein Wegweiser, um alte Verletzungen, Groll und emotionale Blockaden nachhaltig loszulassen.
            </p>
          </div>
          <span style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Autorin: Safi Nidiaye</span>
        </div>

        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Buch-Empfehlung #5 &amp; #6</span>
              <span class="icon-box">{SVG_BOOK}</span>
            </div>
            <h3 style="font-size:1.18rem;font-weight:700;margin-bottom:8px;">«Gefühle sind zum Fühlen da» &amp; «Die 10 Herzensschlüssel»</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Praktische Schlüssel für Beziehungen, Selbstliebe und emotionale Reife: Wie Sie auch in stürmischen Zeiten mit Ihrem Herzen verbunden bleiben.
            </p>
          </div>
          <span style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Autorin: Safi Nidiaye</span>
        </div>
      </div>
    </div>
  </section>
"""


# ==============================================================================
# SEITEN-INHALTE: V1 FRAUEN-WORKSHOPS (workshops.html)
# ==============================================================================
V1_WORKSHOPS_BODY = f"""
  <!-- HERO WORKSHOPS -->
  <section class="hero-section" data-section="workshops-hero" style="padding:64px 0 72px;">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">4-TEILIGE FRAUEN-WORKSHOP-REIHE · OENSINGEN (SO)</div>
        <h1 class="hero-title">
          «Kraftvoll Frau sein» — <span>4 Samstage für Ihre weibliche Urkraft.</span>
        </h1>
        <p class="hero-lead">
          In einer geschützten Kleingruppe von 4 bis 12 Frauen widmen wir uns in der Gemeinschaftspraxis Oensingen (Dünnernstrasse 2) den vier grossen Wurzeln weiblicher Lebenskraft: der Bindung zu Mutter und Vater, Ihrer Sinnlichkeit und der Kraft innerer Weitsicht.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html?thema=workshop" class="btn-cta btn-cta-gold">
            <span>Workshop-Platz oder Ganze Reise reservieren</span>
            {SVG_ARROW}
          </a>
          <a href="#module" class="btn-cta btn-cta-outline-light">
            <span>Alle 4 Tages-Module &amp; Daten ansehen</span>
          </a>
        </div>
        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Samstag 10:00–17:00 Uhr</span>
            <span class="hero-badge-lbl">Gemeinschaftspraxis Oensingen · Dünnernstrasse 2 · 4702 Oensingen</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">4 bis max. 12 Frauen</span>
            <span class="hero-badge-lbl">Persönlicher Rahmen inkl. ausführlichem Handout &amp; Übungen</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">CHF 297.– / Einzelmodul</span>
            <span class="hero-badge-lbl">Early-Bird-Preis CHF 257.– (bis 6 Wochen vor dem Termin)</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">CHF 927.– Ganze Reise</span>
            <span class="hero-badge-lbl">Alle 4 Module im Gesamtpaket (Sie sparen CHF 261.–)</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/workshop-gruppe.jpg" alt="Frauen-Workshop Kraftvoll Frau sein in Oensingen SO" width="600" height="390">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Josefin Sans',sans-serif;font-weight:700;font-size:1.02rem;color:#2b161e;">Gemeinschaftspraxis Oensingen (SO)</div>
            <div style="font-size:0.8rem;color:#4a2c36;">Einzeln buchbar oder als 4-teilige Gesamtreise</div>
          </div>
          <span class="top-bar-badge">KLEINGRUPPE 4–12 FRAUEN</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 4 TAGES-MODULE IM DETAIL (2x2 RASTER) -->
  <section data-section="workshop-module" id="module">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">DIE 4 TAGES-MODULE IM ÜBERBLICK · EINZELN ODER ALS GESAMTREISE BUCHBAR</div>
        <h2 class="section-title">Vier Archetypen und Kraftquellen für Ihr Leben als Frau</h2>
        <p class="section-desc">
          Jeder Workshop-Samstag (10:00 bis 17:00 Uhr) ist in sich abgeschlossen und kann einzeln besucht werden. Zusammen bilden die vier Tage eine tiefgreifende Jahresreise zu sich selbst.
        </p>
      </div>

      <div class="grid-2">
        <!-- Modul 1 -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/workshop-modul-1.jpg" alt="Tag 1: Ich und meine Mutter — Die Urkraft der Mutter" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Tag 1 · Urkraft der Mutter</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Sa, 06. März 2027</span>
              </div>
              <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:8px;">Ich und meine Mutter: Bindung klären, frei werden</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Unsere Mutter ist unser erster Spiegel als Frau. An diesem Tag klären wir unbewusste Verstrickungen, Schuldgefühle oder alte Sehnsüchte, damit Sie Ihren eigenen Platz als erwachsene Frau frei und genährt einnehmen können.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Mutter-Wunde heilen &amp; übernommene Lasten liebevoll zurückgeben</span></div>
                <div class="check-item">{SVG_CHECK} <span>Urvertrauen, Selbstfürsorge und weibliche Verwurzelung stärken</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Termin:</strong> Samstag, 06.03.2027 (Early Bird CHF 257.– bis 23.01.2027, danach CHF 297.–)</span></div>
              </div>
            </div>
            <a href="kontakt.html?thema=workshop" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Platz für Tag 1 (oder Gesamtreise) anfragen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- Modul 2 -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/workshop-modul-2.jpg" alt="Tag 2: Ich und mein Vater — Die Urkraft des Vaters" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Tag 2 · Urkraft des Vaters</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Sa, 29. Mai 2027</span>
              </div>
              <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:8px;">Ich und mein Vater: Innere Führung stärken, den eigenen Weg gehen</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Die Beziehung zum Vater prägt unser Selbstbewusstsein in der Welt, unseren Umgang mit Grenzen und unsere Haltung gegenüber Männern. Wir lösen alte Enttäuschungen und aktivieren Ihre innere Klarheit.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Anerkennung, Fokus und gesunde Abgrenzung im Alltag leben</span></div>
                <div class="check-item">{SVG_CHECK} <span>Frieden mit der Vater-Geschichte schliessen &amp; eigene Entscheidungen treffen</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Termin:</strong> Samstag, 29.05.2027 (Early Bird CHF 257.– bis 18.04.2027, danach CHF 297.–)</span></div>
              </div>
            </div>
            <a href="kontakt.html?thema=workshop" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Platz für Tag 2 (oder Gesamtreise) anfragen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- Modul 3 -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/workshop-modul-3.jpg" alt="Tag 3: Beziehungsfähigkeit und Sinnlichkeit — Die Kraft der Liebenden" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Tag 3 · Kraft der Liebenden</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Sa, 04. September 2027</span>
              </div>
              <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:8px;">Beziehungsfähigkeit und Sinnlichkeit — die Kraft der Liebenden</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Wie gelingt Nähe, ohne sich selbst zu verlieren? Dieser Tag widmet sich Ihrer weiblichen Ausstrahlung, Ihrer Genussfähigkeit und der Kunst, mit offenem Herzen zu lieben.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Scham und alte Blockaden rund um Weiblichkeit &amp; Körpergefühl lösen</span></div>
                <div class="check-item">{SVG_CHECK} <span>Verbindung von Herz und Sinnlichkeit — für Singles und Frauen in Partnerschaft</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Termin:</strong> Samstag, 04.09.2027 (Early Bird CHF 257.– bis 24.07.2027, danach CHF 297.–)</span></div>
              </div>
            </div>
            <a href="kontakt.html?thema=workshop" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Platz für Tag 3 (oder Gesamtreise) anfragen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- Modul 4 -->
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/workshop-modul-4.jpg" alt="Tag 4: Sorgenkarussell stoppen — Die Kraft der Weitsicht und Weisheit" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Tag 4 · Weitsicht &amp; Weisheit</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.8rem;font-weight:700;color:var(--gold-dark);">Sa, 14. November 2026</span>
              </div>
              <h3 style="font-size:1.3rem;font-weight:700;margin-bottom:8px;">Sorgenkarussell stoppen — die Kraft der Weitsicht und Weisheit</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Wenn du im Alltag funktionierst, für alle mitdenkst und vor lauter Grübeln nicht mehr klar weisst, was deine innere Stimme sagt: An diesem Tag findest du zurück in deine tiefe Ruhe und Intuition.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Gedankenkreisen, Zukunftsängste und mentalen Druck spürbar beruhigen</span></div>
                <div class="check-item">{SVG_CHECK} <span>Zugang zur eigenen inneren Weisheit und Gelassenheit im Alltag</span></div>
                <div class="check-item">{SVG_CHECK} <span><strong>Termin:</strong> Samstag, 14.11.2026 (Early Bird CHF 257.– bis 03.10.2026, danach CHF 297.–)</span></div>
              </div>
            </div>
            <a href="kontakt.html?thema=workshop" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Platz für Tag 4 (oder Gesamtreise) anfragen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- KONDITIONEN & PREISÜBERSICHT -->
  <section data-section="workshop-preise" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">TRANSPARENTE KONDITIONEN · GEMEINSCHAFTSPRAXIS OENSINGEN</div>
        <h2 class="section-title">Preise, Early-Bird-Vorteil &amp; Gesamtreise</h2>
        <p class="section-desc">
          Alle Workshops finden jeweils am Samstag von 10:00 bis 17:00 Uhr in der Gemeinschaftspraxis Oensingen (Dünnernstrasse 2, 4702 Oensingen) statt — inklusive ausführlichem Handout.
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Frühbucher bis 6 Wochen vorher</span>
            <h3 style="font-size:1.5rem;font-weight:700;color:var(--charcoal-deep);margin-bottom:6px;">CHF 257.– <span style="font-size:0.9rem;font-weight:500;color:var(--text-muted);">/ Tages-Modul</span></h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:14px;">
              Bei Buchung eines einzelnen Workshop-Samstags bis spätestens 6 Wochen vor Durchführungstermin.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>1 ganzer Workshop-Tag (10:00–17:00 Uhr)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Inkl. ausführlichem Handout &amp; Übungen</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=workshop" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Einzelmodul anfragen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card">
          <div>
            <span class="meta-badge" style="margin-bottom:10px;">Regulärer Einzelpreis</span>
            <h3 style="font-size:1.5rem;font-weight:700;color:var(--charcoal-deep);margin-bottom:6px;">CHF 297.– <span style="font-size:0.9rem;font-weight:500;color:var(--text-muted);">/ Tages-Modul</span></h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:14px;">
              Regulärer Beitrag für ein einzelnes Tages-Modul nach Ablauf der Early-Bird-Frist.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Kleingruppe mit maximal 4 bis 12 Teilnehmerinnen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Persönliche Begleitung durch Anne-Katrin Koch</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=workshop" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Platz reservieren</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-dark">
          <div>
            <span class="top-bar-badge" style="margin-bottom:10px;">EMPFEHLUNG · ALLE 4 MODULE (CHF 261.– SPAREN)</span>
            <h3 style="font-size:1.5rem;font-weight:700;color:#2b161e;margin-bottom:6px;">CHF 927.– <span style="font-size:0.9rem;font-weight:500;color:var(--gold);">/ Ganze Reise (4 Tage)</span></h3>
            <p style="font-size:0.88rem;color:#4a2c36;margin-bottom:14px;">
              Buchen Sie alle 4 Tages-Module als zusammenhängende Jahresreise (statt CHF 1'188.– im Einzelkauf).
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Alle 4 Samstage (Mutter, Vater, Liebende, Weitsicht) garantiert reserviert</span></div>
              <div class="check-item">{SVG_CHECK} <span>CHF 261.– Preisvorteil gegenüber der Einzelbuchung</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=workshop" class="btn-cta btn-cta-gold btn-sm" style="width:100%;">
            <span>Ganze Reise (CHF 927.–) buchen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>
"""

# ==============================================================================
# SEITEN-INHALTE: V1 ÜBER MICH & KLIENTEN-STIMMEN (ueber-mich.html)
# ==============================================================================
V1_UEBER_MICH_BODY = f"""
  <!-- HERO ÜBER MICH -->
  <section class="hero-section" data-section="ueber-hero" style="padding:64px 0 72px;">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">ÜBER ANNE-KATRIN KOCH · PRAXIS HERZENSARBEIT SEIT 2009</div>
        <h1 class="hero-title">
          «Was ich heute weitergebe, <span>habe ich selbst durchlebt.»</span>
        </h1>
        <p class="hero-lead">
          1967 in Bern geboren, verheiratet mit Mathias und Mutter von zwei erwachsenen Kindern (Ramon *2003 und Sarah *2006): Seit 2009 begleite ich Menschen in meiner Praxis im Usserdorf 24 in Härkingen (SO) und Online durch Beziehungs- und Lebenskrisen.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>Persönliches Kennenlerngespräch anfragen</span>
            {SVG_ARROW}
          </a>
          <a href="#stimmen" class="btn-cta btn-cta-outline-light">
            <span>Alle 12 Klienten-Stimmen lesen</span>
          </a>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/portrait-anne-katrin-praxis.jpg" alt="Anne-Katrin Koch in ihrer Praxis in Härkingen SO" width="600" height="390">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Josefin Sans',sans-serif;font-weight:700;font-size:1.02rem;color:#2b161e;">Anne-Katrin Koch Künzle</div>
            <div style="font-size:0.8rem;color:#4a2c36;">Geb. 1967 in Bern · Über 5'000 Beratungsstunden</div>
          </div>
          <span class="top-bar-badge">HÄRKINGEN (SO) &amp; ONLINE</span>
        </div>
      </div>
    </div>
  </section>

  <!-- MEIN WEG & AUSBILDUNGEN -->
  <section data-section="werdegang" id="werdegang">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">MEIN WEG, MEINE HEILERFAHRUNG &amp; AUSBILDUNGEN</div>
        <h2 class="section-title">Von der eigenen Krise zur Berufung in der Herzensarbeit</h2>
        <p class="section-desc">
          Mein Weg in die therapeutische Begleitung entstand nicht aus grauer Theorie, sondern aus der tiefen Erfahrung, wie sehr das ehrliche Fühlen im Körper unser Leben und unsere Gesundheit wandeln kann.
        </p>
      </div>

      <div class="grid-2">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Persönliche Biografie &amp; Heilungsweg</span>
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 style="font-size:1.32rem;font-weight:700;margin-bottom:10px;">Mein eigener Weg zurück ins Vertrauen</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:14px;">
              Nach meiner Ausbildung als Primarlehrerin im Kanton Bern und meiner Tätigkeit als Taketina-Rhythmuspädagogin erlebte ich über viele Jahre hinweg starke körperliche Herausforderungen — darunter schwere Neurodermitis, Hashimoto und chronische Entzündungen.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Der Wendepunkt (2006):</strong> In der Körperzentrierten Herzensarbeit bei Safi Nidiaye lernte ich, meine unterdrückten Gefühle bewusst im Körper wahrzunehmen und anzunehmen.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Gelebte Partnerschaft:</strong> Als Ehefrau von Mathias und Mutter von Ramon (*2003) und Sarah (*2006) kenne ich die Höhen und Tiefen des Familien- und Paarlebens aus erster Hand.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Praxisgründung 2009:</strong> Seit über 17 Jahren begleite ich Paare und Einzelpersonen in über 5'000 Beratungsstunden.</span></div>
            </div>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Gespräch mit Anne-Katrin Koch vereinbaren</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Fachliche Qualifikationen</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 style="font-size:1.32rem;font-weight:700;margin-bottom:10px;">Aus- und Weiterbildungen im Überblick</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:14px;">
              Meine Arbeit verbindet bodenständige Pädagogik, körperzentrierte Bewusstseinsarbeit und vertiefte Beziehungs- und Körpertherapie:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>2006–2008:</strong> Ausbildung in Körperzentrierter Herzensarbeit direkt bei Safi Nidiaye</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Seit 2009:</strong> Über 5'000 Stunden Paartherapie, Trennungs- und Trauerbegleitung in eigener Praxis</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Beziehung &amp; Sinnlichkeit:</strong> Weiterbildungen in Sexological Bodywork &amp; Tantra-Massage</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Bewusstseinsforschung:</strong> Training am renommierten Monroe Institut in Virginia (USA)</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Grundausbildung:</strong> Patentierte Primarlehrerin (Kanton Bern) &amp; Taketina-Rhythmuspädagogin</span></div>
            </div>
          </div>
          <a href="angebot.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Zu meinen Begleitungs-Angeboten</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- ALLE 12 VERIFIZIERTEN KLIENTEN-STIMMEN -->
  <section data-section="alle-klientenstimmen" id="stimmen" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">VERIFIZIERTE RÜCKMELDUNGEN AUS DER PRAXIS · ALLE 6 THEMENBEREICHE</div>
        <h2 class="section-title">12 Stimmen von Paaren, Klientinnen &amp; Workshop-Teilnehmerinnen</h2>
        <p class="section-desc">
          Aus Gründen der Diskretion werden manche Rückmeldungen nur mit Vornamen veröffentlicht. Alle originalen Rückmeldungen stammen von echten Klientinnen, Klienten und Paaren aus meiner Praxis.
        </p>
      </div>

      {render_testimonials_grid(12)}
    </div>
  </section>
"""


# ==============================================================================
# SEITEN-INHALTE: V2 ZEIGEVERSION / VORSCHAU-ENTWURF (index.html)
# ==============================================================================
V2_INDEX_BODY = f"""
  <!-- HERO SECTION (ZEIGEVERSION) -->
  <section class="hero-section" data-section="hero">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light" data-slot="hero_kicker">PRAXIS FÜR KÖRPERZENTRIERTE HERZENSARBEIT · HÄRKINGEN (SO) &amp; ONLINE</div>
        <h1 class="hero-title" data-slot="hero_title">
          Mit offenem Herzen <span>lieben und leben.</span>
        </h1>
        <p class="hero-lead" data-slot="hero_lead">
          Ob festgefahrene Beziehungskrise, schmerzhafte Trennung, tiefer Verlust oder der Wunsch nach mehr Selbstliebe und innerer Ruhe: Seit 2009 begleite ich Paare und Einzelpersonen in meiner Praxis in Härkingen (SO), in Oensingen und Online mit Wärme, Klarheit und über 5'000 Stunden Beratungserfahrung.
        </p>

        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
            <span>3-Schritte Smart-Anfrage live testen</span>
            {SVG_ARROW}
          </a>
          <a href="#weitere-themenbereiche" class="btn-cta btn-cta-outline-light" data-slot="hero_cta_secondary">
            <span>Vorschau der weiteren Seiten ansehen</span>
          </a>
        </div>

        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Über 5'000 Stunden</span>
            <span class="hero-badge-lbl">Erfahrung in Paartherapie &amp; Einzelbegleitung seit 2009</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Einzel- &amp; Paarsitzungen</span>
            <span class="hero-badge-lbl">Kombiniertes 3–5 Monate Paket inkl. WhatsApp-Begleitung</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Härkingen (SO) &amp; Online</span>
            <span class="hero-badge-lbl">Zentral am A1/A2-Kreuz (Usserdorf 24) oder per Video (DE/EN)</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Safi Nidiaye Methode</span>
            <span class="hero-badge-lbl">Herz öffnen statt Kopf zerbrechen — fühlen, klären &amp; lösen</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/portrait-anne-katrin-hero.jpg" alt="Anne-Katrin Koch — Praxis Herzensarbeit Härkingen SO" width="600" height="390" data-slot="hero_image">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:'Josefin Sans',sans-serif;font-weight:700;font-size:1.02rem;color:#2b161e;">Anne-Katrin Koch</div>
            <div style="font-size:0.8rem;color:#4a2c36;">Paartherapie, Trennungs- &amp; Trauerbegleitung · Praxis Härkingen (SO)</div>
          </div>
          <span class="top-bar-badge">SEIT 2009 IN EIGENER PRAXIS</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 6 BEGLEITUNGSWEGE (AUCH IN V2 VOLL SICHTBAR) -->
  <section data-section="kernangebote" id="kernangebote">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="pillars_kicker">WIE ICH SIE BEGLEITE · PRAXIS HÄRKINGEN, OENSINGEN &amp; ONLINE</div>
        <h2 class="section-title" data-slot="pillars_title">Sechs Wege zurück in Ihre Herzkraft und Verbundenheit</h2>
        <p class="section-desc" data-slot="pillars_desc">
          Wenn wir uns nur noch den Kopf zerbrechen, drehen wir uns im Kreis. In der Körperzentrierten Herzensarbeit verbinden wir klärende Gespräche mit dem bewussten Fühlen im Körper — damit echte Entlastung, Nähe und neue Perspektiven entstehen.
        </p>
      </div>

      <div class="grid-3">
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/paarcoaching-hero.jpg" alt="Paartherapie, Eheberatung und Paarcoaching in Härkingen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Paare &amp; Einzelpersonen</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">3–5 Monate Begleitung</span>
              </div>
              <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:8px;">Paartherapie, Eheberatung &amp; Paarcoaching</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Raus aus dem Streit-Kreislauf, dem Schweigen oder der Entfremdung: Gemeinsam klären wir Ihre Beziehungskrise in 3 strukturierten Etappen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>4 Einzelsitzungen à 60 Min. pro Person + 4 Paarsitzungen à 90 Min.</span></div>
                <div class="check-item">{SVG_CHECK} <span>Persönlicher WhatsApp-Support &amp; Audio-Übungen für zu Hause</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Paartherapie, Eheberatung &amp; Paarcoaching', '3-Etappen-Modell, 3–5 Monate Paket (4 Einzel- + 4 Paarsitzungen) &amp; Beziehungs-Kurzanalyse', 'Anne-Katrin Koch')">
              <span>Vorschau-Details zur Paartherapie</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/trennung-beratung.jpg" alt="Trennung verarbeiten und Liebeskummer überwinden" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Neubeginn &amp; Halt</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">10 Sitzungen / 4 Monate</span>
              </div>
              <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:8px;">Trennung verarbeiten &amp; Neubeginn</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Wenn eine Beziehung zerbricht, steht plötzlich alles still. Ich begleite Sie sicher durch den ersten Schock zurück zu Ihrer eigenen inneren Stärke.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>3 Phasen: Schock verarbeiten, zu sich finden, neues Leben gestalten</span></div>
                <div class="check-item">{SVG_CHECK} <span>10 Sitzungen à 60 Min. inkl. WhatsApp-Begleitung im Alltag</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Trennung verarbeiten &amp; Neubeginn', '3-Phasen-Begleitung (10 Sitzungen à 60 Min. auf 4 Monate) inkl. WhatsApp-Support', 'Anne-Katrin Koch')">
              <span>Vorschau-Details zur Trennungsberatung</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/trauerbegleitung-wasser.jpg" alt="Trauerbegleitung in Härkingen und Online" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Abschied &amp; Trost</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">8–10 Sitzungen</span>
              </div>
              <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:8px;">Trauerbegleitung &amp; Verlust</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                «Weil ich dich liebe, lebst du in meinem Herzen weiter.» Ein geschützter Raum, um den Schmerz bewusst zu fühlen und wieder Morgenrot zu sehen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>3 Abschnitte: Bewusst fühlen, Morgenrot spüren, neue Kraft schöpfen</span></div>
                <div class="check-item">{SVG_CHECK} <span>Einfühlsame Begleitung auf ca. 4 Monate mit Alltags-Impulsen</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Trauerbegleitung &amp; Verlust', '3 Abschnitte (Bewusst fühlen, Morgenrot, Neue Kraft) &amp; Erfahrungsberichte', 'Anne-Katrin Koch')">
              <span>Vorschau-Details zur Trauerbegleitung</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/achtsamkeit-selbstliebe.jpg" alt="Achtsamkeit und Selbstliebe lernen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Innere Klarheit</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">8–10 Sitzungen</span>
              </div>
              <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:8px;">Achtsamkeit &amp; Selbstliebe lernen</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Lernen Sie, aus dem Gedankenkarussell auszusteigen, übernommene Fremdgefühle abzugeben und Ihren eigenen Selbstwert tief im Herzen zu verankern.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Innere Ordnung schaffen &amp; liebevolle Grenzen setzen</span></div>
                <div class="check-item">{SVG_CHECK} <span>Geführte Herzensarbeit-Übungen &amp; Audio-Anleitungen</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Achtsamkeit &amp; Selbstliebe lernen', '3 Schritte zu innerer Ordnung, Abgrenzung von Fremdgefühlen &amp; Selbstwert', 'Anne-Katrin Koch')">
              <span>Vorschau-Details zu Achtsamkeit</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/selbstheilung-natur.jpg" alt="Selbstheilung aktivieren und Körper-Harmonie" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Körper &amp; Bewusstsein</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Eigene Heilerfahrung</span>
              </div>
              <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:8px;">Selbstheilung &amp; Körper-Harmonie</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Unser Körper spricht mit uns. Erfahren Sie, wie unterdrückte Gefühle und Stress den Körper belasten — und wie innere Klärung die Regeneration stärkt.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Authentische Erfahrung (Weg aus Neurodermitis &amp; Hashimoto)</span></div>
                <div class="check-item">{SVG_CHECK} <span>Bewusstseins- &amp; Gefühlsarbeit zur Entlastung des Nervensystems</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Selbstheilung &amp; Körper-Harmonie', 'Zusammenspiel von Gedanken, Gefühlen &amp; Körper sowie persönlicher Heilungsweg', 'Anne-Katrin Koch')">
              <span>Vorschau-Details zu Selbstheilung</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/workshop-gruppe.jpg" alt="Frauen-Workshop-Reihe Kraftvoll Frau sein in Oensingen" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Oensingen (SO) · 4–12 Frauen</span>
                <span style="font-family:'Josefin Sans',sans-serif;font-size:0.78rem;font-weight:700;color:var(--gold-dark);">Ab CHF 257.– / Modul</span>
              </div>
              <h3 style="font-size:1.26rem;font-weight:700;margin-bottom:8px;">Frauen-Workshops «Kraftvoll Frau sein»</h3>
              <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
                Vier kraftvolle Samstage in der Gemeinschaftspraxis Oensingen: Mutter- &amp; Vaterbindung klären, Sinnlichkeit leben und das Sorgenkarussell stoppen.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>Einzelmodul CHF 297.– (Early Bird CHF 257.–) · Alle 4 Module CHF 927.–</span></div>
                <div class="check-item">{SVG_CHECK} <span>Samstag 10:00–17:00 Uhr in geschützter Kleingruppe inkl. Handout</span></div>
              </div>
            </div>
            <button type="button" class="btn-cta btn-cta-gold btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Frauen-Workshop-Reihe «Kraftvoll Frau sein»', 'Alle 4 Tages-Module in Oensingen (Mutter, Vater, Sinnlichkeit, Weitsicht), Termine &amp; Early-Bird-Preise', 'Anne-Katrin Koch')">
              <span>Vorschau-Details zu den 4 Workshops</span>
              {SVG_ARROW}
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- BEZIEHUNGS-KURZANALYSE & ANNE-KATRIN KOCH VORSTELLUNG -->
  <section data-section="kurzanalyse" id="kurzanalyse" style="background-color:var(--bg-Warm);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="grid-2" id="ueber-anne-katrin">
        <div class="founder-card">
          <div class="founder-top">
            <img src="images/portrait-anne-katrin-praxis.jpg" alt="Anne-Katrin Koch Porträt Praxis Härkingen" class="founder-portrait" loading="lazy" decoding="async">
            <div>
              <span class="meta-badge" style="margin-bottom:8px;">Praxis Härkingen (SO) &amp; Online</span>
              <h3 style="font-size:1.35rem;font-weight:700;margin-bottom:6px;">Anne-Katrin Koch</h3>
              <p style="font-size:0.86rem;color:var(--gold-dark);font-weight:700;margin-bottom:10px;">
                Körperzentrierte Herzensarbeit nach Safi Nidiaye · Seit 2009
              </p>
              <p style="font-size:0.88rem;color:var(--text-body);line-height:1.58;">
                Geboren 1967 in Bern, verheiratet mit Mathias, Mutter von Ramon (*2003) und Sarah (*2006). Über 5'000 Stunden Erfahrung in Paartherapie, Trennungs- und Trauerbegleitung.
              </p>
            </div>
          </div>
          <div class="founder-body">
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Ausbildung in Körperzentrierter Herzensarbeit bei Safi Nidiaye (2006–2008)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Weiterbildungen in Sexological Bodywork, Tantra-Massage &amp; am Monroe Institut (USA)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Praxis im Usserdorf 24 in Härkingen (SO) + Online-Sitzungen (Deutsch &amp; Englisch)</span></div>
            </div>
            <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Kennenlerngespräch via Smart-Anfrage starten</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Beziehungs-Kurzanalyse (5 Fragen)</span>
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 style="font-size:1.35rem;font-weight:700;margin-bottom:10px;">Wo stehen Sie gerade in Ihrer Beziehung?</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Diese 5 Fragen aus meiner Praxis helfen Frauen und Männern bei einer ersten ehrlichen Standortbestimmung:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>1. Verbundenheit:</strong> Fühlen Sie sich im Alltag wirklich gesehen und emotional verstanden?</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>2. Gesprächskultur:</strong> Können Sie Konflikte klären, ohne in Angriff oder Schweigen zu fallen?</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>3. Nähe &amp; Sinnlichkeit:</strong> Erleben Sie Zärtlichkeit als lebendig und nährend?</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>4. Eigene Grenzen:</strong> Bleiben Sie sich selbst treu, statt sich nur anzupassen?</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>5. Zukunftswunsch:</strong> Möchten Sie herausfinden, was zwischen Ihnen wieder möglich ist?</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=paartherapie" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Standortbestimmung im 3-Schritte-Assistenten starten</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- AUSGEWÄHLTE KLIENTEN-STIMMEN (4 STIMMEN IN V2) -->
  <section data-section="klientenstimmen-v2">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">AUSGEWÄHLTE KLIENTEN-STIMMEN · PRAXIS HERZENSARBEIT</div>
        <h2 class="section-title">Echte Erfahrungen von Paaren und Einzelpersonen</h2>
        <p class="section-desc">
          Bereits in dieser Zeigeversion sehen Sie 4 verifizierte Stimmen aus der Praxis — alle 12 Erfahrungsberichte aus sämtlichen 6 Themenbereichen sind für den gemeinsamen Ausbau vorbereitet.
        </p>
      </div>

      {render_testimonials_grid(4)}
    </div>
  </section>

  <!-- VORSCHAU-BEREICH DER WEITEREN UNTERSEITEN (KUNDENFREUNDLICHE ZEIGEVERSION #UI-03) -->
  <section class="preview-scope-section" id="weitere-themenbereiche" data-section="vorschau-umfang">
    <div class="container">
      <div class="preview-scope-banner">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:10px;">
          <span class="top-bar-badge">UNVERBINDLICHER VORSCHAU-ENTWURF · 2 BEISPIEL-SEITEN LIVE AUSGEARBEITET</span>
          <span style="font-size:0.82rem;color:#4a2c36;font-weight:600;">Herzensarbeit — Anne-Katrin Koch · Härkingen (SO)</span>
        </div>
        <h2 style="font-size:clamp(1.55rem,2.6vw,2.1rem);font-weight:700;color:#2b161e;margin-bottom:10px;">
          3 weitere Themenbereiche sind für den gemeinsamen Ausbau vorbereitet
        </h2>
        <p style="font-size:0.95rem;color:#4a2c36;line-height:1.65;">
          In dieser <strong>Zeigeversion</strong> haben wir die <strong>Startseite</strong> und den interaktiven <strong>3-Schritte Smart-Anfrage-Assistenten</strong> bereits live für Sie aufgebaut. Die folgenden drei vertieften Unterseiten mit allen Originaltexten, Workshop-Modulen und Klienten-Stimmen werden beim gemeinsamen Ausbau schlüsselfertig freigeschaltet:
        </p>
      </div>

      <div class="grid-3">
        <!-- Vorschau-Karte 1: Paartherapie & Angebot -->
        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Folgt beim Ausbau · Unterseite 1</span>
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:8px;">Paartherapie, Trennungs- &amp; Trauerbegleitung im Detail</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Ausführliche Darstellung aller 5 Einzel- und Paar-Angebote inklusive der Methode nach Safi Nidiaye:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>3 Etappen der Paartherapie &amp; das 3–5 Monate Paket im Detail</span></div>
              <div class="check-item">{SVG_CHECK} <span>3 Phasen der Trennungsverarbeitung &amp; 3 Abschnitte der Trauerbegleitung</span></div>
              <div class="check-item">{SVG_CHECK} <span>Achtsamkeit, Selbstliebe, Selbstheilung &amp; die 6 Bücher von Safi Nidiaye</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Paartherapie, Trennungs- &amp; Trauerbegleitung im Detail', 'Alle 3-Etappen-Wege, Sitzungs-Pakete, Achtsamkeit, Selbstheilung &amp; Methode Safi Nidiaye', 'Anne-Katrin Koch')">
            <span>Vorschau-Details zu diesem Bereich öffnen</span>
            {SVG_ARROW}
          </button>
        </div>

        <!-- Vorschau-Karte 2: Frauen-Workshops -->
        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Folgt beim Ausbau · Unterseite 2</span>
              <span class="icon-box">{SVG_SPARKLES}</span>
            </div>
            <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:8px;">Frauen-Workshop-Reihe «Kraftvoll Frau sein» (Oensingen)</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Eigene Detailseite für die 4-teilige Workshop-Reihe in der Gemeinschaftspraxis Oensingen (Dünnernstrasse 2):
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Tag 1 (Mutter · 06.03.2027) &amp; Tag 2 (Vater · 29.05.2027)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Tag 3 (Liebende · 04.09.2027) &amp; Tag 4 (Weitsicht · 14.11.2026)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Konditionen: Einzelmodul CHF 297.– (Early Bird CHF 257.–) · Ganze Reise CHF 927.–</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Frauen-Workshop-Reihe «Kraftvoll Frau sein»', 'Alle 4 Tages-Module in Oensingen (Mutter, Vater, Sinnlichkeit, Weitsicht), Termine &amp; Early-Bird-Preise', 'Anne-Katrin Koch')">
            <span>Vorschau-Details zu diesem Bereich öffnen</span>
            {SVG_ARROW}
          </button>
        </div>

        <!-- Vorschau-Karte 3: Über mich & Alle Stimmen -->
        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Folgt beim Ausbau · Unterseite 3</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:8px;">Über Anne-Katrin Koch &amp; Alle 12 Klienten-Stimmen</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Persönliche Biografie, Ausbildungen seit 2006 und die vollständige Sammlung aller Klienten-Erfahrungen:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Persönlicher Heilungsweg (Neurodermitis, Hashimoto) &amp; Familie</span></div>
              <div class="check-item">{SVG_CHECK} <span>Ausbildungen bei Safi Nidiaye, Sexological Bodywork &amp; Monroe Institut</span></div>
              <div class="check-item">{SVG_CHECK} <span>Alle 12 verifizierten Klienten-Stimmen aus allen 6 Angebotsbereichen</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Über Anne-Katrin Koch &amp; Alle Klienten-Stimmen', 'Persönlicher Heilungsweg, Ausbildungen seit 2006, Praxis Härkingen &amp; alle verifizierten Erfahrungsberichte', 'Anne-Katrin Koch')">
            <span>Vorschau-Details zu diesem Bereich öffnen</span>
            {SVG_ARROW}
          </button>
        </div>
      </div>
    </div>
  </section>
"""


def build_kontakt_body(client_slug: str, source_page: str) -> str:
    return f"""
  <section data-section="kontakt-zentrale" style="padding: 56px 0 84px;">
    <div class="container">
      <div class="contact-layout">
        <!-- LEFT COLUMN: DIREKTKONTAKT & PRAXIS HÄRKINGEN / OENSINGEN -->
        <div class="contact-info-panel">
          <div class="section-kicker" data-slot="contact_kicker">KONTAKT &amp; GESPRÄCH VEREINBAREN · HÄRKINGEN, OENSINGEN &amp; ONLINE</div>
          <h1 style="font-size:clamp(1.65rem,2.5vw,2.15rem);font-weight:700;margin-bottom:12px;" data-slot="contact_title">
            Ihr direkter Draht zu Anne-Katrin Koch.
          </h1>
          <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:18px;" data-slot="contact_lead">
            Schreiben Sie mir, rufen Sie mich an oder starten Sie rechts den geführten 3-Schritte Smart-Anfrage-Assistenten. Alle Anfragen werden absolut vertraulich behandelt und persönlich von mir beantwortet.
          </p>

          <img src="images/portrait-anne-katrin-hero.jpg" alt="Anne-Katrin Koch Praxis Herzensarbeit Härkingen" style="width:100%;height:200px;object-fit:cover;object-position:center top;border-radius:var(--radius-sm);margin-bottom:16px;" loading="lazy" decoding="async">

          <div class="contact-direct-list">
            <div class="contact-direct-item">
              <div class="contact-direct-role">Praxis für Paartherapie &amp; Einzelberatung</div>
              <div class="contact-direct-person">Herzensarbeit · Anne-Katrin Koch</div>
              <div class="contact-direct-links">Usserdorf 24 · CH-4624 Härkingen (SO) · Direkt am Autobahnkreuz A1/A2</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Direktkontakt (Telefon, WhatsApp, SMS &amp; E-Mail)</div>
              <div class="contact-direct-person">Anne-Katrin Koch (Inhaberin · Seit 2009 in eigener Praxis)</div>
              <div class="contact-direct-links">Tel. / WhatsApp: +41 79 103 63 31 · E-Mail: a.koch@herzensarbeit.ch</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Frauen-Workshops «Kraftvoll Frau sein»</div>
              <div class="contact-direct-person">Gemeinschaftspraxis Oensingen (Samstag 10:00–17:00 Uhr)</div>
              <div class="contact-direct-links">Dünnernstrasse 2 · CH-4702 Oensingen (SO) · Kleingruppe 4–12 Frauen</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Online-Beratung &amp; Bewertungen</div>
              <div class="contact-direct-person">Video-Sitzungen auf Deutsch &amp; Englisch</div>
              <div class="contact-direct-links">provenexpert.com/herzensarbeit-anne-katrin-koch</div>
            </div>
          </div>
        </div>

        <!-- RIGHT COLUMN: GEFÜHRTER 3-SCHRITTE SMART-ANFRAGE-ASSISTENT -->
        <div class="wizard-card">
          <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:14px;">
            <div>
              <div class="section-kicker" style="margin-bottom:4px;">3-SCHRITTE SMART-ANFRAGE · HERZENSARBEIT.CH</div>
              <h2 style="font-size:1.35rem;font-weight:700;" id="wpWizardTitle">1. Worum geht es bei Ihrem Anliegen?</h2>
            </div>
            <span class="meta-badge" id="wpActiveAssigneeBadge">Begleitung: Anne-Katrin Koch</span>
          </div>

          <div class="wp-stepper" aria-label="Fortschritt">
            <div class="wp-step-pill active" id="wpStepPill1">
              <span class="wp-step-num">1</span>
              <span>Worum geht es?</span>
            </div>
            <div class="wp-step-pill" id="wpStepPill2">
              <span class="wp-step-num">2</span>
              <span>Rahmen &amp; Fokus</span>
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

            <!-- SCHRITT 1: WORUM GEHT ES? (4 AUSWAHLKARTEN) -->
            <div class="wp-step-pane active" id="wpStep1">
              <div class="wp-role-grid" id="wpTopicGrid">
                <button type="button" class="wp-role-tile selected" data-topic="Paartherapie, Eheberatung & Paarcoaching" onclick="wpSelectIsTopic('Paartherapie, Eheberatung & Paarcoaching')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_HEART}</span>
                    <span class="wp-role-title" data-slot="topic_opt_1">1. Paartherapie &amp; Paarcoaching</span>
                  </div>
                  <span class="wp-role-desc">Beziehungskrise klären in 3 Etappen (Einzel- &amp; Paarsitzungen in Härkingen oder Online)</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Trennung verarbeiten, Trauerbegleitung & Einzelberatung" onclick="wpSelectIsTopic('Trennung verarbeiten, Trauerbegleitung & Einzelberatung')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_COMPASS}</span>
                    <span class="wp-role-title" data-slot="topic_opt_2">2. Trennung, Trauer &amp; Einzelberatung</span>
                  </div>
                  <span class="wp-role-desc">Trennung verarbeiten, Trauerbegleitung, Achtsamkeit, Selbstliebe oder Selbstheilung</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Frauen-Workshop «Kraftvoll Frau sein» (Oensingen SO)" onclick="wpSelectIsTopic('Frauen-Workshop «Kraftvoll Frau sein» (Oensingen SO)')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_SPARKLES}</span>
                    <span class="wp-role-title" data-slot="topic_opt_3">3. Frauen-Workshop «Kraftvoll Frau sein»</span>
                  </div>
                  <span class="wp-role-desc">Einzelmodul (CHF 297.– / Early Bird CHF 257.–) oder Ganze Reise (alle 4 Module CHF 927.–) in Oensingen</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Unverbindliches Kennenlerngespräch (Härkingen / Online)" onclick="wpSelectIsTopic('Unverbindliches Kennenlerngespräch (Härkingen / Online)')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">{SVG_USERS}</span>
                    <span class="wp-role-title" data-slot="topic_opt_4">4. Unverbindliches Kennenlerngespräch</span>
                  </div>
                  <span class="wp-role-desc">Persönliche Standortbestimmung in der Praxis Härkingen (Usserdorf 24), Online oder telefonisch</span>
                </button>
              </div>

              <button type="button" class="btn-cta btn-cta-primary" style="width:100%;" onclick="wpNextStep(2)">
                <span>Weiter zu Schritt 2: Rahmen &amp; Fokus</span>
                {SVG_ARROW}
              </button>
            </div>

            <!-- SCHRITT 2: RAHMEN & FOKUS -->
            <div class="wp-step-pane" id="wpStep2">
              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="wpDetail1" class="form-label" id="wpDetail1Label">Aktuelle Situation / Schwerpunkt</label>
                  <input type="text" id="wpDetail1" class="form-input" placeholder="z. B. Kommunikationskrise, Rückzug, Vertrauen klären">
                </div>
                <div class="form-field">
                  <label for="wpDetail2" class="form-label" id="wpDetail2Label">Gewünschter Rahmen (Härkingen / Online)</label>
                  <input type="text" id="wpDetail2" class="form-input" placeholder="z. B. Als Paar oder zuerst allein · Praxis Härkingen / Online">
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label class="form-label">Gewünschter Zeitraum &amp; Durchführungsform</label>
                <div class="wp-role-grid" id="wpUrgencyGrid" style="margin-bottom:0;">
                  <button type="button" class="wp-role-tile selected" data-urg="Zeitnah (Gesprächstermin in den nächsten 1–2 Wochen)" onclick="wpSelectIsUrgency('Zeitnah (Gesprächstermin in den nächsten 1–2 Wochen)')">
                    <span class="wp-role-title">In den nächsten 1–2 Wochen</span>
                    <span class="wp-role-desc">Zeitnahes Erstgespräch in Härkingen oder Online</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urg="Akute Beziehungskrise / Trennungsschock (Rasche Rückmeldung)" onclick="wpSelectIsUrgency('Akute Beziehungskrise / Trennungsschock (Rasche Rückmeldung)')">
                    <span class="wp-role-title">Akute Situation (Rasche Rückmeldung)</span>
                    <span class="wp-role-desc">Dringender Klärungsbedarf bei Krise oder Trennung</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urg="Workshop-Anmeldung (Oensingen SO)" onclick="wpSelectIsUrgency('Workshop-Anmeldung (Oensingen SO)')">
                    <span class="wp-role-title">Frauen-Workshop «Kraftvoll Frau sein»</span>
                    <span class="wp-role-desc">Platzreservierung für Einzelmodul oder Ganze Reise</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urg="Flexibel / Unverbindliche Orientierung" onclick="wpSelectIsUrgency('Flexibel / Unverbindliche Orientierung')">
                    <span class="wp-role-title">Flexibel / Erste Orientierung</span>
                    <span class="wp-role-desc">Kurzes telefonisches Kennenlernen vereinbaren</span>
                  </button>
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label for="contactMessage" class="form-label" data-slot="lbl_message">Was bewegt Sie gerade? (Vertrauliche Nachricht)</label>
                <textarea id="contactMessage" name="message" class="form-textarea" placeholder="Beschreiben Sie in wenigen Stichworten Ihr Anliegen oder Ihre Fragen an Anne-Katrin Koch..."></textarea>
              </div>

              <div class="wp-upload-zone" style="margin-bottom:16px;">
                <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
                  <div>
                    <div style="font-family:'Josefin Sans',sans-serif;font-size:0.82rem;font-weight:700;color:var(--charcoal-deep);">Optionale Notiz / Beilage hinzufügen (max. 3 Bilder)</div>
                    <div style="font-size:0.76rem;color:var(--text-muted);" id="wpPhotoCounter">0 / 3 Beilagen ausgewählt · Automatisch für das 1-Seiten-PDF-Dossier aufbereitet</div>
                  </div>
                  <button type="button" class="wp-upload-btn" onclick="wpTriggerPhotoUpload()">
                    <span>Beilage auswählen</span>
                  </button>
                </div>
                <input type="file" id="wpPhotoInput" accept="image/*" multiple style="display:none;" onchange="wpHandlePhotoFiles(this.files)">
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
                <strong>Live-Vorschau-Modus (Selbsttest aktiv):</strong> Beim Absenden erstellt das System sofort ein echtes <strong>1-Seiten-A4-PDF-Dossier</strong> im Erscheinungsbild von <strong>Herzensarbeit — Anne-Katrin Koch</strong> zum direkten Öffnen und Prüfen.
              </div>

              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactName" class="form-label" data-slot="lbl_name">Vor- und Nachname *</label>
                  <input type="text" id="contactName" name="name" class="form-input" placeholder="z. B. Claudia &amp; Thomas Berger" required>
                </div>
                <div class="form-field">
                  <label for="contactCompany" class="form-label">Begleitungsform (Einzelperson / Paar)</label>
                  <input type="text" id="contactCompany" name="company" class="form-input" placeholder="z. B. Paarbegleitung oder Einzelberatung">
                </div>
              </div>

              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactLoc" class="form-label">PLZ &amp; Wohnort *</label>
                  <input type="text" id="contactLoc" name="plz" class="form-input" placeholder="z. B. 4624 Härkingen / 4600 Olten" oninput="wpCheckIsPlz(this.value)" required>
                </div>
                <div class="form-field">
                  <label for="contactStreet" class="form-label">Strasse &amp; Nr. (optional)</label>
                  <input type="text" id="contactStreet" name="street" class="form-input" placeholder="z. B. Usserdorf 24">
                </div>
              </div>

              <div class="wp-plz-badge" id="wpPlzBadge" style="margin-bottom:14px;">
                {SVG_CHECK}
                <span id="wpPlzBadgeText">PLZ 4624: Direktes Einzugsgebiet Praxis Härkingen (SO)</span>
              </div>

              <div class="form-grid-2" style="margin-bottom:18px;">
                <div class="form-field">
                  <label for="contactEmail" class="form-label" data-slot="lbl_email">E-Mail-Adresse *</label>
                  <input type="email" id="contactEmail" name="email" class="form-input" placeholder="ihre.email@beispiel.ch" required>
                </div>
                <div class="form-field">
                  <label for="contactPhone" class="form-label" data-slot="lbl_phone">Telefon / Mobile (auch für WhatsApp) *</label>
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
                <span style="width:36px;height:36px;border-radius:4px;background-color:var(--green);color:#2b161e;display:inline-flex;align-items:center;justify-content:center;">
                  {SVG_CHECK}
                </span>
                <div>
                  <div style="font-family:'Josefin Sans',sans-serif;font-weight:700;font-size:1.08rem;color:var(--charcoal-deep);">Anfrage &amp; 1-Seiten-PDF-Dossier erfolgreich erstellt</div>
                  <div style="font-size:0.78rem;color:var(--text-muted);" id="wpResChannels">1-Seiten-PDF-Dossier bereit zum Download</div>
                </div>
              </div>
              <span class="top-bar-badge" style="background-color:#9b2c47;color:#FFFFFF;" id="wpResRef">#WP-2026</span>
            </div>

            <div class="form-grid-2" style="background-color:#2b161e;padding:12px 14px;border-radius:4px;border:1px solid var(--border-light);font-size:0.84rem;">
              <div>
                <div style="color:var(--text-muted);font-size:0.75rem;">Zuständige Ansprechpartnerin (Praxis Härkingen):</div>
                <strong style="color:var(--charcoal-deep);" id="wpResAssigned">Anne-Katrin Koch</strong>
              </div>
              <div>
                <div style="color:var(--text-muted);font-size:0.75rem;">Verbindliches Rückmelde-Fenster:</div>
                <strong style="color:var(--gold-dark);" id="wpResCallback">Persönliche Rückmeldung</strong>
              </div>
            </div>

            <div>
              <div style="font-family:'Josefin Sans',sans-serif;font-size:0.76rem;font-weight:700;text-transform:uppercase;color:var(--text-muted);margin-bottom:6px;">
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
      topic: 'Paartherapie, Eheberatung & Paarcoaching',
      urgency: 'Zeitnah (Gesprächstermin in den nächsten 1–2 Wochen)',
      photos: []
    }};

    var wpIsRoleConfig = {{
      'Paartherapie, Eheberatung & Paarcoaching': {{
        assignee: 'Anne-Katrin Koch (Paartherapie & Paarcoaching)',
        l1: 'Aktuelle Situation in Ihrer Beziehung',
        p1: 'z. B. Streit-Kreislauf, Schweigen, Vertrauenskrise, Standortbestimmung',
        l2: 'Gewünschter Rahmen (Härkingen / Online · Paar / Einzel)',
        p2: 'z. B. Gemeinsam als Paar in Härkingen oder per Video-Call'
      }},
      'Trennung verarbeiten, Trauerbegleitung & Einzelberatung': {{
        assignee: 'Anne-Katrin Koch (Trennung, Trauer & Einzelberatung)',
        l1: 'Themenfokus (Trennung, Trauer, Achtsamkeit, Selbstheilung)',
        p1: 'z. B. Trennung verarbeiten, Trauerbegleitung oder Selbstliebe stärken',
        l2: 'Bevorzugter Ort (Praxis Härkingen SO / Online)',
        p2: 'z. B. Vor Ort im Usserdorf 24 in Härkingen oder Online'
      }},
      'Frauen-Workshop «Kraftvoll Frau sein» (Oensingen SO)': {{
        assignee: 'Anne-Katrin Koch (Frauen-Workshops Oensingen SO)',
        l1: 'Gewünschtes Modul oder Ganze Reise (alle 4 Tage)',
        p1: 'z. B. Ganze Reise (CHF 927.–) oder Einzelmodul (Tag 1–4)',
        l2: 'Vorkenntnisse / Fragen zum Workshop-Tag',
        p2: 'z. B. Gemeinschaftspraxis Oensingen (Sa 10:00–17:00 Uhr)'
      }},
      'Unverbindliches Kennenlerngespräch (Härkingen / Online)': {{
        assignee: 'Anne-Katrin Koch (Praxis Härkingen & Online)',
        l1: 'Worum geht es in erster Linie?',
        p1: 'z. B. Erstes Kennenlernen & Fragen zum Ablauf klären',
        l2: 'Bevorzugte Gesprächsform (Härkingen / Online / Telefon)',
        p2: 'z. B. Kurzes Telefonat, Video-Call oder Praxis Härkingen'
      }}
    }};

    function wpUpdateIsHeader() {{
      var titles = {{
        1: '1. Worum geht es bei Ihrem Anliegen?',
        2: '2. Rahmen, Fokus & persönliche Nachricht',
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
      var cfg = wpIsRoleConfig[topic] || wpIsRoleConfig['Paartherapie, Eheberatung & Paarcoaching'];
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
      if (plz >= 4500 && plz <= 4999) {{
        txt.textContent = 'PLZ ' + m[1] + ': Direktes Einzugsgebiet Praxis Härkingen (Usserdorf 24) & Oensingen';
      }} else {{
        txt.textContent = 'PLZ ' + m[1] + ': Bequem erreichbar am A1/A2-Kreuz Härkingen oder per Online-Beratung';
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
      wpSelectIsTopic('Paartherapie, Eheberatung & Paarcoaching');
      wpSelectIsUrgency('Zeitnah (Gesprächstermin in den nächsten 1–2 Wochen)');
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

      var cfg = wpIsRoleConfig[wpIsState.topic] || wpIsRoleConfig['Paartherapie, Eheberatung & Paarcoaching'];
      var extra = {{}};
      extra[cfg.l1] = d1 || 'Persönliche Abstimmung im Erstgespräch';
      extra[cfg.l2] = d2 || 'Praxis Härkingen (Usserdorf 24) / Online';

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
        message: msg || ('Anfrage zu ' + wpIsState.topic),
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
        document.getElementById('wpResAssigned').textContent = res.assigned_to || 'Anne-Katrin Koch';
        document.getElementById('wpResCallback').textContent = res.callback_window || 'Persönliche Rückmeldung';
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
          errBox.textContent = 'Netzwerkfehler bei der Übermittlung. Bitte schreiben Sie direkt an a.koch@herzensarbeit.ch.';
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
          'paartherapie': 'Paartherapie, Eheberatung & Paarcoaching',
          'einzelberatung': 'Trennung verarbeiten, Trauerbegleitung & Einzelberatung',
          'workshop': 'Frauen-Workshop «Kraftvoll Frau sein» (Oensingen SO)',
          'kennenlernen': 'Unverbindliches Kennenlerngespräch (Härkingen / Online)'
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
    ("index.html", "Herzensarbeit — Anne-Katrin Koch | Paartherapie, Trennungs- & Trauerbegleitung Härkingen SO", "startseite", V1_INDEX_BODY),
    ("angebot.html", "Paartherapie, Trennung, Trauer, Achtsamkeit & Selbstheilung | Herzensarbeit Anne-Katrin Koch", "angebot", V1_ANGEBOT_BODY),
    ("workshops.html", "Frauen-Workshops «Kraftvoll Frau sein» in Oensingen SO | Herzensarbeit Anne-Katrin Koch", "workshops", V1_WORKSHOPS_BODY),
    ("ueber-mich.html", "Über Anne-Katrin Koch & Alle 12 Klienten-Stimmen | Praxis Herzensarbeit Härkingen", "ueber-mich", V1_UEBER_MICH_BODY),
    ("kontakt.html", "Kontakt & 3-Schritte Smart-Anfrage | Herzensarbeit Anne-Katrin Koch Härkingen & Online", "kontakt", build_kontakt_body("herzensarbeit", "preview-herzensarbeit/kontakt.html")),
]

for fname, title, nav_key, body in v1_pages:
    full_html = render_v1_shell(fname, title, nav_key, body)
    (V1_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V1] Wrote {fname} ({len(full_html)} bytes)")

# 4. Alle Seiten für Variante 2 (Zeigeversion / Vorschau-Entwurf) schreiben
v2_pages = [
    ("index.html", "Herzensarbeit — Anne-Katrin Koch (Zeigeversion / Vorschau-Entwurf) | Mit offenem Herzen lieben und leben", "startseite", V2_INDEX_BODY),
    ("kontakt.html", "Kontakt & 3-Schritte Smart-Anfrage (Zeigeversion) | Herzensarbeit Anne-Katrin Koch", "kontakt", build_kontakt_body("herzensarbeit-v2", "preview-herzensarbeit-v2/kontakt.html")),
]

for fname, title, nav_key, body in v2_pages:
    full_html = render_v2_shell(fname, title, nav_key, body)
    (V2_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V2] Wrote {fname} ({len(full_html)} bytes)")

# 5. Partner-Attribution (#wpPartnerModal für Jenny Ettle JE-MI) injizieren
subprocess.run(["python3", str(BASE_DIR / "scripts" / "inject_partner_attribution.py")], check=True)

# 6. Studio Cockpit v4.0 (cockpit.html) für beide Varianten generieren
subprocess.run(["python3", str(BASE_DIR / "scripts" / "build_client_cockpit.py"), "--slug", "preview-herzensarbeit"], check=True)
subprocess.run(["python3", str(BASE_DIR / "scripts" / "build_client_cockpit.py"), "--slug", "preview-herzensarbeit-v2"], check=True)

# 7. Compile Site Pipeline (Pre-Build Gates & Airbag)
subprocess.run(["python3", str(BASE_DIR / "scripts" / "compile_site.py"), "--site", "preview-herzensarbeit", "--skip-device-audit"], check=True)
subprocess.run(["python3", str(BASE_DIR / "scripts" / "compile_site.py"), "--site", "preview-herzensarbeit-v2", "--skip-device-audit"], check=True)
print("Successfully built and compiled preview-herzensarbeit and preview-herzensarbeit-v2.")

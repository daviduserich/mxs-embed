#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator fuer die WebPilot-Referenz-Aufbereitung von goodfordogs.ch
(Hundeschule Good for Dogs · Die Schule fuer Halter (und Hund) · Martina Sidler (Good), 5406 Baden & Uebungsplatz 5413 Birmenstorf):
- Variante 1 (Vollversion): /home/brainuser/workspaces/mxs-embed/preview-die-schule
  Live-URL: https://vorschau.magnet-xs.ch/die-schule-vollversion/ (5 voll ausgebaute Seiten + Studio Cockpit v4.0)
- Variante 2 (Zeigeversion / Vorschau-Entwurf): /home/brainuser/workspaces/mxs-embed/preview-die-schule-v2
  Live-URL: https://vorschau.magnet-xs.ch/die-schule-v2/ (2 ausgearbeitete Beispiel-Seiten: Startseite inkl. Kurs-Finder + 3-Schritte Smart-Anmeldung,
  plus transparente Themenbereich-Vorschaukarten fuer die 3 weiteren Unterseiten).

Strikt nach:
- UI-LAYOUT-RULES.md (Canary: UI-LAYOUT-2026-V1, #UI-01, #UI-02, #UI-13, #UI-14, #UI-16 Evolution-Modus Light Lock S-27)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1, 0 Eszett, 0 Em-Dash im Satz, Einser-Ausschreibungs-Regel, 100 % Schweizer Hochdeutsch)
"""

import json
import shutil
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
V1_DIR = BASE_DIR / "preview-die-schule"
V2_DIR = BASE_DIR / "preview-die-schule-v2"
DNA_SRC = BASE_DIR / "visual-dna" / "die-schule" / "source_visual_dna.json"

V1_DIR.mkdir(parents=True, exist_ok=True)
V2_DIR.mkdir(parents=True, exist_ok=True)

if DNA_SRC.exists():
    shutil.copy2(DNA_SRC, V1_DIR / "source_visual_dna.json")
    shutil.copy2(DNA_SRC, V2_DIR / "source_visual_dna.json")

BEFORE_INVENTORY = {
    "source_url": "https://goodfordogs.ch/index.html",
    "crawled_at": "2026-11-13",
    "company_name": "Good for Dogs · Die Schule für Halter (und Hund)",
    "legal_entity": "Hundeschule Good for Dogs · Martina Sidler (Good)",
    "uid": "",
    "claim": "Die Schule für Halter (und Hund) – fair, gewaltfrei und alltagsnah.",
    "subline": "Individuelles Einzeltraining, Welpen- und Junghundekurse, Familienhunde-Gruppen und Schnüffelspass in 5406 Baden (Rütihof), auf dem Übungsplatz in 5413 Birmenstorf und im Gelände zwischen Baden und Lenzburg.",
    "address": {
        "street": "Region 5406 Baden (Rütihof) · Übungsplatz 5413 Birmenstorf",
        "zip": "5406",
        "city": "Baden",
        "canton": "AG",
        "country": "Schweiz"
    },
    "contact": {
        "email": "info@goodfordogs.ch",
        "phone_primary": "+41 76 454 54 06",
        "phone_display": "076 454 54 06",
        "hours": "Montag 16:30 Uhr (Familienhunde) & 18:00 Uhr (Welpen) | Samstag 09:00 Uhr (Erziehungskurs 1), 10:15 Uhr (Erziehungskurs 2) & jeden 2. Samstag 10:30 Uhr (Schnüffelspass) | Einzeltraining nach Vereinbarung"
    },
    "team": [
        {
            "name": "Martina Sidler (Good)",
            "role": "Inhaberin Good for Dogs · Certodog® Hundeinstruktorin",
            "phone": "076 454 54 06",
            "phone_href": "tel:+41764545406",
            "image": "images/team-martina-sidler-portrait.jpg",
            "qualification": "Certodog® Hundeinstruktorin · FBA-Tierbetreuerin, -Züchterin & -Tiertransport · Certodog® Zuchtwartin · Studium Praktische Psychologie (2026)",
            "bio": "Martina Sidler (Good) begleitet Mensch-Hund-Teams im Raum Baden, Birmenstorf und Lenzburg nach kynologisch fundierten, gewaltfreien Methoden. Als zertifizierte Certodog® Hundeinstruktorin und Mitglied bei «Fairplay mit Hund» sowie der «Initiative für gewaltfreies Hundetraining» verbindet sie präzises Fachwissen mit viel Geduld, Humor und echter Freude am gemeinsamen Lernen."
        }
    ],
    "references": [
        {
            "title": "Ruhige Welpenprägung",
            "category": "Welpenkurs",
            "highlight": "Max. 5 Teams",
            "scope": "Montag 18:00 Uhr · Birmenstorf & Gelände",
            "before_img": "images/kurs-welpen-wiese.jpg",
            "after_img": "images/kurs-welpen-wiese.jpg",
            "obj_pos": "center 40%",
            "desc": "Statt wildem Überdrehen lernen junge Hunde ab der 8. Woche ruhige Umweltgewöhnung, feine Körpersprache, Rückruf-Grundlagen und entspannte Pausen in einer überschaubaren Kleingruppe."
        },
        {
            "title": "Klare Junghundezeit",
            "category": "Junghundekurs",
            "highlight": "Sa Vormittag",
            "scope": "Samstag 09:00 & 10:15 Uhr · Max. 6 Teams",
            "before_img": "images/kurs-junghunde-erziehung.jpg",
            "after_img": "images/kurs-junghunde-erziehung.jpg",
            "obj_pos": "center 35%",
            "desc": "Wenn die Sturm-und-Drang-Phase beginnt, schaffen klare Signale, faire Belohnung, Impulskontrolle und schrittweise aufgebaute Distanzarbeit bis zum sicheren Freilauf verlässliche Orientierung."
        },
        {
            "title": "Entspannter Hundealltag",
            "category": "Einzeltraining",
            "highlight": "1:1 vor Ort",
            "scope": "Bei Ihnen zu Hause & auf Spazierwegen",
            "before_img": "images/kurs-einzeltraining-fokus.jpg",
            "after_img": "images/kurs-einzeltraining-fokus.jpg",
            "obj_pos": "center 15%",
            "desc": "Ob Leinenaggression, Unsicherheit, Bellen, Jagdverhalten oder Alleinebleiben: Im 1:1-Training analysieren wir die Auslöser direkt in Ihrem Wohnumfeld und erarbeiten faire, umsetzbare Schritte."
        },
        {
            "title": "Aktive Familienhunde",
            "category": "Familienhunde",
            "highlight": "Mo 16:30 Uhr",
            "scope": "Einstieg jederzeit · Max. 6 Teams",
            "before_img": "images/kurs-familienhunde-wald.jpg",
            "after_img": "images/kurs-familienhunde-wald.jpg",
            "obj_pos": "center 55%",
            "desc": "Gemeinsame Erfolgserlebnisse für den Familienalltag: alltagsnahe Übungen, Körpersprache lesen, sinnvolle Beschäftigung im Gelände und ruhiges Warten auch unter Ablenkung."
        },
        {
            "title": "Feine Nasenarbeit",
            "category": "Schnüffelspass",
            "highlight": "Max. 3 Teams",
            "scope": "Jeden 2. Sa 10:30 Uhr · 5413 Birmenstorf",
            "before_img": "images/kurs-schnueffelspass-zos-01.jpg",
            "after_img": "images/kurs-schnueffelspass-zos-01.jpg",
            "obj_pos": "center 45%",
            "desc": "Nasenarbeit lastet Hunde jeder Rasse und jedes Alters geistig tief und zufriedenstellend aus. Da jedes Team einzeln sucht, eignet sich die Stunde auch hervorragend für unsichere Hunde."
        },
        {
            "title": "Geprüfte Fachqualität",
            "category": "Qualität",
            "highlight": "Certodog®",
            "scope": "Laufende Fachseminare & Verhaltenswissen",
            "before_img": "images/hund-baumstamm-portraet.jpg",
            "after_img": "images/hund-baumstamm-portraet.jpg",
            "obj_pos": "center 22%",
            "desc": "Hundetraining entwickelt sich stetig weiter. Jährliche Weiterbildungen in Verhaltensmedizin, Körpersprache, Nasenarbeit und Psychologie sichern Ihnen aktuelles Wissen ohne veralteten Zwang."
        }
    ],
    "faqs": [
        {
            "q": "Kann ich jederzeit in eine Gruppe einsteigen oder gibt es feste Startdaten?",
            "a": "In die Welpen-Gruppe (Montag 18:00 Uhr), die Familienhunde-Gruppe (Montag 16:30 Uhr) und die Schnüffelspass-Gruppe (jeden zweiten Samstag 10:30 Uhr) ist ein Einstieg jederzeit möglich, sofern ein Platz frei ist. Die beiden aufbauenden Kurse Erziehungskurs 1 und 2 starten jeweils im geschlossenen 10er-Block am Samstagvormittag."
        },
        {
            "q": "Wo finden die Trainings und Gruppenstunden genau statt?",
            "a": "Unser eingezäunter Übungsplatz befindet sich in 5413 Birmenstorf. Damit Ihr Hund das Gelernte direkt im echten Leben verknüpft, trainieren wir je nach Thema auch an wechselnden Alltagsorten im Gelände zwischen Baden und Lenzburg. Einzeltrainings finden direkt bei Ihnen zu Hause oder auf Ihren gewohnten Spazierwegen statt."
        },
        {
            "q": "Wie gross sind die Gruppen und wie arbeiten Sie mit den Hunden?",
            "a": "Qualität geht vor Menge: In der Welpen-Gruppe trainieren maximal 5 Teams, in den Erziehungs- und Familienhundekursen maximal 6 Teams und beim Schnüffelspass maximal 3 Teams. Wir arbeiten zu 100 Prozent gewaltfrei nach den Grundsätzen von «Fairplay mit Hund» und der «Initiative für gewaltfreies Hundetraining»."
        },
        {
            "q": "Was muss ich zur ersten Trainingsstunde mitbringen?",
            "a": "Bitte bringen Sie ein gut sitzendes Brustgeschirr oder Halsband, eine normale Führleine (keine Roll- oder Flexileine), ausreichend kleine, weiche Belohnungshappen, ein Lieblingsspielzeug Ihres Hundes sowie bei Bedarf Wasser und eine kleine Decke für Ruhephasen mit."
        },
        {
            "q": "Wie kann ich Kurse oder Einzelstunden bezahlen und welche Absagefristen gelten?",
            "a": "Sie können bequem per Überweisung im Voraus oder vor Ort via TWINT bezahlen. Gruppenstunden können bis 24 Stunden vor Kursbeginn kostenfrei abgemeldet werden, vereinbarte Einzeltrainings bis 48 Stunden vor dem Termin."
        },
        {
            "q": "Welche Voraussetzungen gelten bezüglich Impfungen und Versicherung?",
            "a": "Alle teilnehmenden Hunde müssen altersgemäss geimpft, frei von ansteckenden Krankheiten und über eine gültige Privathaftpflichtversicherung der Halterin oder des Halters versichert sein. Bei Erstterminen werfen wir gerne kurz gemeinsam einen Blick in den Heimtierausweis."
        }
    ]
}

(V1_DIR / "before.json").write_text(json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False), encoding="utf-8")
(V2_DIR / "before.json").write_text(json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False), encoding="utf-8")

for target_dir, slug_val, pub_slug, is_v2 in [
    (V1_DIR, "preview-die-schule", "die-schule-vollversion", False),
    (V2_DIR, "preview-die-schule-v2", "die-schule-v2", True)
]:
    (target_dir / "company.json").write_text(json.dumps({
        "company_name": "Good for Dogs · Hundeschule" + (" (Zeigeversion / Vorschau-Entwurf)" if is_v2 else " · Martina Sidler"),
        "slug": slug_val,
        "public_slug": pub_slug,
        "cockpit_token": "die-schule2026",
        "city": "Baden & 5413 Birmenstorf",
        "canton": "AG",
        "postal_code": "5406",
        "street_address": "Region 5406 Baden (Rütihof) · Übungsplatz 5413 Birmenstorf",
        "phone": "+41 76 454 54 06",
        "email": "info@goodfordogs.ch",
        "uid": "",
        "source_url": "https://goodfordogs.ch/index.html",
        "partner_id": "jenny"
    }, indent=2, ensure_ascii=False), encoding="utf-8")

v1_config = {
    "company_name": "Good for Dogs · Die Schule für Halter (und Hund) · Baden",
    "slug": "preview-die-schule",
    "public_slug": "die-schule-vollversion",
    "cockpit_token": "die-schule2026",
    "template": "warm-humanist-editorial-v1",
    "partner_id": "jenny",
    "pages": ["index.html", "leistungen.html", "referenzen.html", "ueber-uns.html", "kontakt.html"]
}
(V1_DIR / "config.json").write_text(json.dumps(v1_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V1_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-die-schule",
    "public_slug": "die-schule-vollversion",
    "token": "die-schule2026",
    "name": "Good for Dogs · Hundeschule Martina Sidler Baden (Vollversion)",
    "Updated": "2026-11-13",
    "PagesCount": 5,
    "ReferencesCount": 6,
    "TeamCount": 1
}, indent=2, ensure_ascii=False), encoding="utf-8")

v2_config = dict(v1_config)
v2_config.update({
    "company_name": "Good for Dogs · Hundeschule (Zeigeversion / Vorschau-Entwurf)",
    "slug": "preview-die-schule-v2",
    "public_slug": "die-schule-v2",
    "cockpit_token": "die-schule2026",
    "template": "warm-humanist-editorial-preview-v2",
    "pages": ["index.html", "kontakt.html"]
})
(V2_DIR / "config.json").write_text(json.dumps(v2_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V2_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-die-schule-v2",
    "public_slug": "die-schule-v2",
    "token": "die-schule2026",
    "name": "Good for Dogs · Hundeschule Baden (Zeigeversion / Vorschau-Entwurf)",
    "Updated": "2026-11-13",
    "PagesCount": 2,
    "ReferencesCount": 6,
    "TeamCount": 1
}, indent=2, ensure_ascii=False), encoding="utf-8")

print("Wrote before.json, company.json, config.json, site.json for V1 and V2.")

SHARED_CSS = """
    :root {
      /* === 1. Polaritaet & Schweizer Raster (#UI-02, #UI-16, Sensor S-27) === */
      --wp-expected-hero-polarity: "light";
      --wp-archetype: "warm_humanist_editorial";
      --container-max: 1100px;
      --container: 1100px;
      --radius-card: 8px;
      --radius-md: 8px;
      --radius-badge: 4px;
      --radius-sm: 4px;

      /* === 2. Typografie (warm_humanist_editorial: Lora + Plus Jakarta Sans) === */
      --font-display: 'Lora', Georgia, serif;
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;

      /* === 3. 60 % & 30 % Tinted Neutrals (Hue=212.8deg aus Source Visual DNA) === */
      --bg-page: #F4FCFD;
      --bg-page-oklch: oklch(0.985 0.008 212.8);
      --bg-soft: #E5F3F7;
      --bg-soft-oklch: oklch(0.955 0.016 212.8);
      --bg-Warm: #E5F3F7;
      --bg-elevated: #FFFFFF;
      --bg-card: #FFFFFF;
      --border-subtle: #D1DDE0;
      --border-subtle-oklch: oklch(0.890 0.014 212.8);
      --border-light: #D1DDE0;
      --border-strong: #B4C8CD;
      --text-main: #07191D;
      --text-main-oklch: oklch(0.200 0.025 212.8);
      --text-body: #1B3136;
      --text-muted: #415054;
      --text-muted-oklch: oklch(0.420 0.020 212.8);
      --charcoal: #0D252B;
      --charcoal-deep: #07191D;

      /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe Petrol-Blau) === */
      --primary: #00899E;
      --primary-brand-raw: #5199A8;
      --primary-oklch: oklch(0.580 0.160 212.8);
      --primary-hover: #007081;
      --gold: #007081;
      --gold-hover: #005B6A;
      --gold-dark: #005B6A;
      --gold-soft: #E5F3F7;
      --gold-border: #B3D6DF;
      --green: #15803D;
      --green-soft: #DCFCE7;

      /* === 5. OKLCH-Harmonisierte Sekundaer-Palette === */
      --accent-palette-1-soft: #E5EFFF;
      --accent-palette-1-strong: #2B5CA6;
      --accent-palette-2-soft: #EAEDFF;
      --accent-palette-2-strong: #4C53A5;
      --accent-palette-3-soft: #F5E9FF;
      --accent-palette-3-strong: #734594;
      --accent-palette-4-soft: #FFE6F5;
      --accent-palette-4-strong: #8C3B73;

      --shadow-sm: 0 2px 10px rgba(7, 25, 29, 0.05);
      --shadow-md: 0 12px 28px rgba(7, 25, 29, 0.08);
      --shadow-lg: 0 18px 40px rgba(7, 25, 29, 0.11);
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    ::selection {
      background-color: rgba(0, 137, 158, 0.18);
      color: #07191D;
    }

    html {
      scroll-behavior: smooth;
      font-size: 16px;
      overflow-x: hidden;
    }

    body {
      font-family: var(--font-sans);
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
      max-width: var(--container-max);
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Freistehende Marken-Kicker (#UI-01: Plus Jakarta Sans Bold, 0 JetBrains Mono, 0 //, 0 ::before) */
    .section-kicker {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-sans);
      font-size: 0.76rem;
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
      font-family: var(--font-display);
      color: var(--text-main);
      line-height: 1.22;
      letter-spacing: -0.01em;
    }

    .section-head {
      max-width: 760px;
      margin-bottom: 42px;
    }
    .section-title {
      font-size: clamp(1.8rem, 3.0vw, 2.45rem);
      font-weight: 700;
      margin-bottom: 14px;
    }
    .section-desc {
      font-size: 1.02rem;
      color: var(--text-body);
      line-height: 1.65;
    }

    section {
      padding: 76px 0;
      position: relative;
    }

    /* Sub-Topbar (V1) */
    .top-bar {
      background-color: var(--bg-soft);
      color: var(--text-body);
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
      background-color: #FFFFFF;
      color: var(--gold-dark);
      border: 1px solid var(--gold-border);
      font-family: var(--font-sans);
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
      color: var(--text-main);
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-height: 32px;
      padding: 4px 8px;
    }
    .top-bar-links a:hover {
      color: var(--gold);
    }

    /* Sticky Main Header (#UI-02: 1-Zeilen-Navigations-Gesetz S-22) */
    .site-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background-color: rgba(244, 252, 253, 0.97);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border-light);
      box-shadow: 0 2px 12px rgba(7, 25, 29, 0.05);
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
      min-height: 46px;
      padding: 4px 0;
    }
    .brand-logo-wide {
      height: 46px;
      width: auto;
      max-width: 176px;
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
      font-family: var(--font-display);
      font-size: 0.92rem;
      font-weight: 700;
      color: var(--charcoal-deep);
      line-height: 1.15;
      white-space: nowrap;
    }
    .brand-sub {
      font-family: var(--font-sans);
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
      gap: 22px;
      flex-wrap: nowrap;
      white-space: nowrap;
    }
    .nav-link {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: var(--font-sans);
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
      color: var(--gold-dark);
      background: transparent;
      border-bottom-color: var(--primary);
    }
    .nav-link-preview {
      color: var(--text-muted);
      background: transparent;
      border: none;
      border-bottom: 2px dashed rgba(0, 112, 129, 0.45);
      font-size: 0.86rem;
    }
    .nav-link-preview:hover {
      color: var(--gold-dark);
      background: transparent;
      border-bottom-color: var(--primary);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }

    /* Buttons (#UI-01: 8px radius, WCAG AA >= 5.7:1 contrast on #007081) */
    .btn-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      font-family: var(--font-sans);
      font-size: 0.89rem;
      font-weight: 600;
      padding: 12px 18px;
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
    .btn-cta-gold,
    .btn-cta-primary {
      background-color: #007081;
      color: #FFFFFF;
      border-color: #007081;
      font-weight: 600;
    }
    .btn-cta-gold:hover,
    .btn-cta-primary:hover {
      background-color: #005B6A;
      color: #FFFFFF;
      border-color: #005B6A;
      transform: translateY(-1px);
    }
    .btn-cta-outline,
    .btn-cta-outline-light {
      background-color: #FFFFFF;
      color: var(--text-main);
      border-color: var(--border-strong);
    }
    .btn-cta-outline:hover,
    .btn-cta-outline-light:hover {
      border-color: #007081;
      color: var(--gold-dark);
      background-color: var(--gold-soft);
    }
    .btn-sm {
      font-size: 0.84rem;
      padding: 9px 14px;
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
      color: var(--text-main);
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }
    .mobile-drawer {
      display: none;
      flex-direction: column;
      gap: 8px;
      padding: 16px 24px 22px;
      background-color: var(--bg-page);
      border-top: 1px solid var(--border-light);
    }
    .mobile-drawer.open {
      display: flex;
    }
    .mobile-drawer a,
    .mobile-drawer button.mobile-nav-btn {
      font-family: var(--font-sans);
      font-size: 0.92rem;
      font-weight: 600;
      color: var(--text-main);
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
      color: var(--gold-dark);
      border-style: dashed;
      border-color: rgba(0, 112, 129, 0.45);
    }

    /* Hero Section: Hell, freundlich & klar (#UI-16 Evolution, S-27 Light Lock & #UI-02 Bottom-Edge Baseline Lock S-23) */
    .hero-section {
      background: linear-gradient(135deg, #FFFFFF 0%, #F4FCFD 55%, #E5F3F7 100%);
      background-color: #F4FCFD;
      color: var(--text-main);
      padding: 68px 0 80px;
      border-bottom: 1px solid var(--border-light);
      overflow: hidden;
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1.12fr 0.88fr;
      gap: 40px;
      align-items: stretch;
    }
    .hero-grid > div:first-child {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .hero-title {
      font-size: clamp(2.0rem, 3.4vw, 2.95rem);
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.16;
      margin-bottom: 16px;
    }
    .hero-title span {
      color: var(--gold-dark);
    }
    .hero-lead {
      font-size: 1.02rem;
      color: var(--text-body);
      line-height: 1.65;
      margin-bottom: 18px;
    }
    .hero-quote-box {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-left: 3px solid var(--primary);
      border-radius: var(--radius-sm);
      padding: 11px 14px;
      font-family: var(--font-display);
      font-style: italic;
      font-size: 0.9rem;
      color: var(--text-body);
      margin-bottom: 22px;
      line-height: 1.5;
    }
    .hero-actions {
      display: flex;
      flex-wrap: nowrap;
      gap: 12px;
      align-items: center;
      margin-bottom: 24px;
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
      border-left: 3px solid var(--gold);
      border-radius: var(--radius-sm);
      padding: 10px 14px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      gap: 2px;
      box-shadow: var(--shadow-sm);
    }
    .hero-badge-val {
      font-family: var(--font-sans);
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--gold-dark);
    }
    .hero-badge-lbl {
      font-size: 0.77rem;
      color: var(--text-body);
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
      height: 280px;
      min-height: 260px;
      flex: 1 1 auto;
      object-fit: cover;
      object-position: center 45%;
    }
    .hero-media-caption {
      padding: 15px 18px;
      background-color: var(--bg-soft);
      border-top: 1px solid var(--border-light);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }

    /* Universal Symmetric Grids (#UI-14 & S-31 Sibling Card Anatomy Lock) */
    .grid-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 26px;
      align-items: stretch;
    }
    .grid-2 > :last-child:nth-child(odd) {
      grid-column: 1 / -1;
    }
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 22px;
      align-items: stretch;
    }
    .grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
      align-items: stretch;
    }

    /* Cards */
    .content-card {
      background-color: var(--bg-card);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 26px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 18px;
      height: 100%;
    }
    .content-card.card-accent-top {
      border-top: 4px solid var(--primary);
    }
    .content-card.card-dark {
      background: linear-gradient(135deg, #FFFFFF 0%, #E5F3F7 100%);
      background-color: #E5F3F7;
      color: var(--text-main);
      border-color: var(--gold-border);
      border-top: 4px solid var(--gold);
    }
    .content-card.card-dark h3 {
      color: var(--text-main);
    }

    .card-badge-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      flex-wrap: nowrap;
      margin-bottom: 10px;
      min-height: 28px;
    }
    .meta-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: var(--font-sans);
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      padding: 4px 9px;
      border-radius: var(--radius-sm);
      background-color: var(--gold-soft);
      color: var(--gold-dark);
      border: 1px solid var(--gold-border);
      white-space: nowrap;
    }
    .icon-box {
      width: 38px;
      height: 38px;
      border-radius: var(--radius-sm);
      background-color: var(--gold-soft);
      color: var(--gold-dark);
      border: 1px solid var(--gold-border);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    /* Synchronized card headings for S-31 internal horizontal alignment */
    .card-title-1 {
      font-size: 1.16rem;
      font-weight: 700;
      line-height: 1.26;
      margin-bottom: 8px;
    }
    .card-title-2 {
      font-size: 1.15rem;
      font-weight: 700;
      line-height: 1.28;
      min-height: 2.95rem;
      margin-bottom: 8px;
    }

    .check-list {
      display: flex;
      flex-direction: column;
      gap: 9px;
      margin-top: 8px;
    }
    .check-item {
      display: flex;
      align-items: flex-start;
      gap: 9px;
      font-size: 0.9rem;
      color: var(--text-body);
      line-height: 1.48;
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
      height: 205px;
      overflow: hidden;
      background-color: var(--bg-soft);
      position: relative;
    }
    .pillar-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 40%;
    }
    .pillar-body {
      padding: 22px 24px;
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
      grid-template-columns: 185px 1fr;
      gap: 22px;
      padding: 26px 26px 0;
      align-items: start;
    }
    .founder-portrait {
      width: 100%;
      height: 185px;
      object-fit: cover;
      object-position: 38% 25%;
      border-radius: var(--radius-md);
      border: 2px solid var(--primary);
    }
    .founder-body {
      padding: 20px 26px 26px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex: 1;
      gap: 16px;
    }

    /* Quality Seal Badges Row */
    .seal-strip {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
      margin-top: 14px;
    }
    .seal-item {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 14px;
      background-color: var(--bg-page);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-sm);
    }
    .seal-item img {
      width: 52px;
      height: 52px;
      object-fit: contain;
      flex-shrink: 0;
      border-radius: var(--radius-sm);
      background-color: #FFFFFF;
      padding: 2px;
    }

    /* Interactive Kurs-Finder Styles */
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
      font-family: var(--font-sans);
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
      font-family: var(--font-sans);
      font-size: 1.02rem;
      font-weight: 700;
      color: var(--gold-dark);
    }
    .calc-kpi-lbl {
      font-size: 0.77rem;
      color: var(--text-body);
      margin-top: 2px;
    }

    /* V2 Vorschau-Entwurf (Zeigeversion) Spezifische Styles (#UI-03 Kunden-Sprache) */
    .preview-scope-section {
      background-color: var(--bg-soft);
      border-top: 2px dashed rgba(0, 112, 129, 0.38);
      border-bottom: 2px dashed rgba(0, 112, 129, 0.38);
      padding: 74px 0 84px;
    }
    .preview-scope-banner {
      background-color: #FFFFFF;
      color: var(--text-main);
      border: 2px dashed var(--gold);
      border-radius: var(--radius-md);
      padding: 26px 28px;
      margin-bottom: 34px;
      box-shadow: var(--shadow-md);
    }
    .preview-module-card {
      background-color: #FFFFFF;
      border: 2px dashed var(--gold);
      border-radius: var(--radius-md);
      padding: 24px;
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
      font-family: var(--font-sans);
      font-size: 0.7rem;
      font-weight: 700;
      padding: 4px 9px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      white-space: nowrap;
    }

    /* Footer */
    .site-footer {
      background-color: var(--bg-soft);
      color: var(--text-main);
      padding: 64px 0 34px;
      border-top: 3px solid var(--primary);
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 1.3fr 1fr 1fr 1.1fr;
      gap: 34px;
      padding-bottom: 40px;
      border-bottom: 1px solid var(--border-strong);
    }
    .footer-title {
      font-family: var(--font-sans);
      font-size: 0.86rem;
      font-weight: 700;
      color: var(--text-main);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 15px;
    }
    .footer-list {
      display: flex;
      flex-direction: column;
      gap: 9px;
    }
    .footer-list a,
    .footer-list button {
      color: var(--text-body);
      font-size: 0.87rem;
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
      color: var(--gold-dark);
    }
    .footer-bottom {
      padding-top: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      font-size: 0.82rem;
      color: var(--text-body);
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
      background-color: rgba(7, 25, 29, 0.74);
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
      max-width: 660px;
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
      margin-bottom: 18px;
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

    /* 3-Schritte Smart-Anmeldung & Anfrage Assistent (kontakt.html) */
    .contact-layout {
      display: grid;
      grid-template-columns: 0.88fr 1.12fr;
      gap: 36px;
      align-items: stretch;
    }
    .contact-info-panel {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 26px;
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
      margin-top: 18px;
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
      font-family: var(--font-sans);
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
      padding: 28px;
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
      font-family: var(--font-sans);
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--text-muted);
      text-align: center;
    }
    .wp-step-pill.active {
      background-color: #007081;
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
      background-color: #FFFFFF;
      color: var(--gold-dark);
      border: 1px solid var(--gold-border);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .wp-role-title {
      font-family: var(--font-sans);
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
      font-family: var(--font-sans);
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--charcoal-deep);
      line-height: 1.3;
    }
    .form-input,
    .form-textarea {
      width: 100%;
      font-family: var(--font-sans);
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
      box-shadow: 0 0 0 3px rgba(0, 137, 158, 0.16);
    }
    .form-textarea {
      min-height: 96px;
      resize: vertical;
    }

    .wp-upload-zone {
      border: 1px dashed var(--border-strong);
      background-color: var(--bg-page);
      border-radius: var(--radius-md);
      padding: 14px;
      cursor: pointer;
    }
    .wp-photo-thumbs {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 10px;
    }
    .wp-photo-thumb {
      width: 72px;
      height: 72px;
      object-fit: cover;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-strong);
    }
    .wizard-nav-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }

    .wp-success-box {
      display: none;
      flex-direction: column;
      gap: 14px;
      padding: 22px;
      background-color: var(--bg-page);
      border: 2px solid var(--green);
      border-radius: var(--radius-md);
    }
    .wp-success-box.visible {
      display: flex;
    }

    @media (max-width: 1020px) {
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
        padding: 54px 0;
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
      .calc-kpi-grid,
      .seal-strip {
        grid-template-columns: 1fr;
      }
      .card-title-2 {
        min-height: 0;
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
      .brand-logo-wide {
        height: 36px;
        max-width: 128px;
      }
      .brand-text {
        display: none;
      }
      .hero-media-card img {
        height: 245px;
      }
      .founder-portrait {
        height: 225px;
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
SVG_SHIELD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
SVG_AWARD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>'
SVG_USERS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
SVG_COMPASS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>'
SVG_CALENDAR = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>'
SVG_SEARCH = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>'
SVG_CAMERA = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>'
SVG_BOOK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>'
SVG_PHONE = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
SVG_MAIL = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'

COURSES_DATA = [
    {
        "id": "einzeltraining",
        "topic_param": "einzeltraining",
        "badge": "CHF 80.— / Std.",
        "schedule": "Individuell",
        "title": "Einzeltraining & Beratung",
        "img": "images/kurs-einzeltraining-fokus.jpg",
        "obj_pos": "center 15%",
        "desc": "Individuelles 1:1-Training bei Ihnen zu Hause und im gewohnten Umfeld: ideal bei Leinenaggression, Angst, Bellen, Jagdverhalten oder Rückruf-Themen.",
        "b1": "Massgeschneiderter Trainingsplan für Ihren Alltag",
        "b2": "CHF 80.— pro 60 Min. (Anfahrt CHF 1.— pro km)",
        "cta_v1": "Einzeltermin anfragen",
        "cta_v2": "Details zum Einzeltraining"
    },
    {
        "id": "welpen",
        "topic_param": "welpen",
        "badge": "CHF 35.— / Lekt.",
        "schedule": "Mo 18:00 Uhr",
        "title": "Welpen-Gruppe (ab 8 Wo.)",
        "img": "images/kurs-welpen-wiese.jpg",
        "obj_pos": "center 40%",
        "desc": "Behutsamer Start ins Leben auf dem Platz in Birmenstorf und im Gelände Baden–Lenzburg: Umweltgewöhnung, Rückruf, Ruheübungen und soziales Lernen.",
        "b1": "Einstieg jederzeit möglich · Maximal 5 Teams",
        "b2": "10er-Abo CHF 300.— (4 Monate gültig, übertragbar)",
        "cta_v1": "Welpenplatz anfragen",
        "cta_v2": "Details zur Welpen-Gruppe"
    },
    {
        "id": "erziehung1",
        "topic_param": "junghunde",
        "badge": "CHF 300.— / Kurs",
        "schedule": "Sa 09:00 Uhr",
        "title": "Erziehungskurs 1",
        "img": "images/kurs-junghunde-erziehung.jpg",
        "obj_pos": "center 35%",
        "desc": "Für junge Hunde ab 6 Monaten und neu übernommene Hunde: verlässliche Grundsignale, lockere Leine, Impulskontrolle und ruhige Begegnungen.",
        "b1": "Fester Kursblock à 10 Lektionen · Maximal 6 Teams",
        "b2": "Übungsplatz 5413 Birmenstorf & Alltagsgelände",
        "cta_v1": "Kursplatz vormerken",
        "cta_v2": "Details zu Erziehungskurs 1"
    },
    {
        "id": "erziehung2",
        "topic_param": "junghunde",
        "badge": "CHF 300.— / Kurs",
        "schedule": "Sa 10:15 Uhr",
        "title": "Erziehungskurs 2",
        "img": "images/hero-mensch-hund-alltag.jpg",
        "obj_pos": "center 45%",
        "desc": "Der Aufbaukurs für fortgeschrittene Teams: Fokus auf sichere Distanzkontrolle, Orientierung trotz starker Ablenkung und entspannten Freilauf.",
        "b1": "10 Lektionen à 60 Min. · Maximal 6 Teams",
        "b2": "Praxisnahe Trainingsorte zwischen Baden & Lenzburg",
        "cta_v1": "Aufbaukurs anfragen",
        "cta_v2": "Details zu Erziehungskurs 2"
    },
    {
        "id": "familienhunde",
        "topic_param": "familienhunde",
        "badge": "CHF 35.— / Lekt.",
        "schedule": "Mo 16:30 Uhr",
        "title": "Familienhunde-Gruppe",
        "img": "images/kurs-familienhunde-wald.jpg",
        "obj_pos": "center 55%",
        "desc": "Abwechslungsreiche Alltags- und Beschäftigungsstunde für Hunde ab 16 Wochen: Körpersprache, sinnvolle Bewegung, Spass und Alltagssicherheit.",
        "b1": "Einstieg jederzeit möglich · Maximal 6 Teams",
        "b2": "Einzellektion CHF 35.— oder 10er-Abo CHF 300.—",
        "cta_v1": "Schnupperstunde anfragen",
        "cta_v2": "Details zu Familienhunden"
    },
    {
        "id": "schnueffelspass",
        "topic_param": "schnueffelspass",
        "badge": "CHF 40.— / Lekt.",
        "schedule": "2. Sa 10:30 Uhr",
        "title": "Schnüffelspass-Gruppe",
        "img": "images/kurs-schnueffelspass-zos-01.jpg",
        "obj_pos": "center 45%",
        "desc": "Geistige Auslastung ab 6 Monaten auf dem eingezäunten Gelände in 5413 Birmenstorf: Zielobjektsuche, Geruchsdifferenzierung und Mantrailing-Elemente.",
        "b1": "Maximal 3 Teams (jeder Hund arbeitet einzeln)",
        "b2": "Einstieg jederzeit · 10er-Abo CHF 350.— (6 Mt.)",
        "cta_v1": "Schnüffelplatz anfragen",
        "cta_v2": "Details zum Schnüffelspass"
    }
]


def render_courses_grid(is_v2: bool = False) -> str:
    cards = []
    for c in COURSES_DATA:
        if is_v2:
            cta_html = f'''<button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('{c['title']} ({c['schedule']})', '{c['badge']} · {c['b1']}', 'Martina Sidler (Certodog® Hundeinstruktorin)')">
              <span>{c['cta_v2']}</span>
              {SVG_ARROW}
            </button>'''
        else:
            cta_html = f'''<a href="kontakt.html?thema={c['topic_param']}" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>{c['cta_v1']}</span>
              {SVG_ARROW}
            </a>'''
        cards.append(f"""
        <div class="pillar-card" id="{c['id']}">
          <div class="pillar-img-wrap">
            <img src="{c['img']}" alt="Good for Dogs Baden &amp; Birmenstorf: {c['title']}" style="object-position:{c['obj_pos']};" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">{c['badge']}</span>
                <span style="font-family:var(--font-sans);font-size:0.75rem;font-weight:700;color:var(--gold-dark);white-space:nowrap;">{c['schedule']}</span>
              </div>
              <h3 class="card-title-1">{c['title']}</h3>
              <p style="font-size:0.89rem;color:var(--text-body);margin-bottom:12px;">{c['desc']}</p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK} <span>{c['b1']}</span></div>
                <div class="check-item">{SVG_CHECK} <span>{c['b2']}</span></div>
              </div>
            </div>
            {cta_html}
          </div>
        </div>""")
    return '<div class="grid-3">\n' + "\n".join(cards) + "\n      </div>"


def render_references_grid(limit: int = 6, is_v2: bool = False) -> str:
    cards = []
    for ref in BEFORE_INVENTORY["references"][:limit]:
        cta_html = (
            f'''<button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Trainings-Einblick: {ref['title']}', '{ref['category']} · {ref['scope']}', 'Martina Sidler (Good for Dogs)')">
              <span>Trainings-Einblick öffnen</span>
              {SVG_ARROW}
            </button>'''
            if is_v2
            else f'''<a href="kontakt.html?thema=einzeltraining" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Passenden Kurs mit Martina klären</span>
              {SVG_ARROW}
            </a>'''
        )
        cards.append(f"""
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="{ref['after_img']}" alt="Good for Dogs Hundeschule Baden: {ref['title']}" style="object-position:{ref['obj_pos']};" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">{ref['category']}</span>
                <span style="font-family:var(--font-sans);font-size:0.75rem;font-weight:700;color:var(--gold-dark);white-space:nowrap;">{ref['highlight']}</span>
              </div>
              <h3 class="card-title-1">{ref['title']}</h3>
              <p style="font-size:0.8rem;font-weight:700;color:var(--gold-dark);margin-bottom:8px;">{ref['scope']}</p>
              <p style="font-size:0.88rem;color:var(--text-body);">{ref['desc']}</p>
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
            <h3 class="card-title-2">{f['q']}</h3>
            <p style="font-size:0.9rem;color:var(--text-body);line-height:1.62;">{f['a']}</p>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Persönlich mit Martina Sidler klären</span>
            {SVG_ARROW}
          </a>
        </div>""")
    return '<div class="grid-2">\n' + "\n".join(cards) + "\n      </div>"


def render_acp_bridge_sections(is_v2: bool = False) -> str:
    social_cta_1 = (
        f'''<button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Trainings-Momente @goodfordogs.ch', 'Instagram &amp; Facebook Einblicke aus 5413 Birmenstorf und Region Baden', 'Martina Sidler')"><span>Einblick ansehen</span>{SVG_ARROW}</button>'''
        if is_v2 else
        f'''<a href="referenzen.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Weitere Einblicke ansehen</span>{SVG_ARROW}</a>'''
    )
    blog_cta_1 = (
        f'''<button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Hunde-Ratgeber &amp; Alltagswissen', 'Praxistipps zu Welpenstart, Leinenführigkeit und Nasenarbeit', 'Martina Sidler')"><span>Praxistipp lesen</span>{SVG_ARROW}</button>'''
        if is_v2 else
        f'''<a href="leistungen.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Passendes Training entdecken</span>{SVG_ARROW}</a>'''
    )
    return f"""
  <!-- ACP BRÜCKE 1: SOCIAL MEDIA & ECHTE TRAININGS-MOMENTE -->
  <section data-section="social-media" id="social-media" style="background-color:var(--bg-page);border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="social_kicker">AKTUELLE EINBLICKE · @GOODFORDOGS.CH AUF INSTAGRAM &amp; FACEBOOK</div>
        <h2 class="section-title" data-slot="social_title">Frisch ab Übungsplatz Birmenstorf und aus dem Aargauer Gelände</h2>
        <p class="section-desc" data-slot="social_desc">
          Auf <strong>@goodfordogs.ch</strong> teilen wir regelmässig echte Übungsmomente, Lernfortschritte unserer Teams und kleine Alltags-Impulse aus Birmenstorf, Baden-Rütihof und der Region Lenzburg.
        </p>
      </div>

      <div class="grid-3">
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/kurs-schnueffelspass-zos-02.jpg" alt="Zielobjektsuche und Nasenarbeit auf dem Platz in Birmenstorf" style="object-position:center 50%;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Nasenarbeit</span>
                <span style="font-size:0.75rem;font-weight:700;color:var(--gold-dark);white-space:nowrap;">Birmenstorf</span>
              </div>
              <h3 class="card-title-1">Fokus bei der Schatzsuche</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">
                Beim Schnüffelspass arbeiten maximal drei Teams nacheinander im eingezäunten Gelände: ruhig, fokussiert und für jeden Hund ein echtes Erfolgserlebnis.
              </p>
            </div>
            {social_cta_1}
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/kurs-welpen-wiese.jpg" alt="Welpenstunde im Grünen bei Good for Dogs" style="object-position:center 40%;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Welpenstunde</span>
                <span style="font-size:0.75rem;font-weight:700;color:var(--gold-dark);white-space:nowrap;">Mo 18:00 Uhr</span>
              </div>
              <h3 class="card-title-1">Sicher ins Leben starten</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">
                In unserer Montags-Welpengruppe stehen Sicherheit, Bindung zur Bezugsperson und wohldosierte Umweltreize vor blossem Herumtoben.
              </p>
            </div>
            {social_cta_1}
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/kurs-familienhunde-wald.jpg" alt="Familienhunde-Training im Wald zwischen Baden und Lenzburg" style="object-position:center 55%;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Alltagstraining</span>
                <span style="font-size:0.75rem;font-weight:700;color:var(--gold-dark);white-space:nowrap;">Region Baden</span>
              </div>
              <h3 class="card-title-1">Gelassen im Wald unterwegs</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">
                Gemeinsames Training im Wald und an Alltagsorten stärkt die gelassene Impulskontrolle genau dort, wo Sie täglich unterwegs sind.
              </p>
            </div>
            {social_cta_1}
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ACP BRÜCKE 2: RATGEBER & ALLTAGSWISSEN FÜR HUNDEHALTER -->
  <section data-section="blog" id="blog" style="background-color:var(--bg-soft);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="blog_kicker">HUNDE-RATGEBER &amp; PRAXISWISSEN · FÜR HALTERINNEN &amp; HALTER</div>
        <h2 class="section-title" data-slot="blog_title">Drei Fragen, die im Hundealltag den grössten Unterschied machen</h2>
        <p class="section-desc" data-slot="blog_desc">
          Gutes Hundetraining beginnt immer am oberen Ende der Leine: mit verständlicher Körpersprache, fairem Timing und den richtigen Pausen.
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Ratgeber #1 · Welpenzeit</span>
              <span class="icon-box">{SVG_BOOK}</span>
            </div>
            <h3 class="card-title-1">Ruhe in der Welpenzeit</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Viele junge Hunde sind nicht unterfordert, sondern durch zu viele Eindrücke überreizt. Gezielte Ruhephasen und maximal fünf Teams pro Gruppe schaffen ein stabiles Nervenkostüm.
            </p>
          </div>
          {blog_cta_1}
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Ratgeber #2 · Begegnungen</span>
              <span class="icon-box">{SVG_COMPASS}</span>
            </div>
            <h3 class="card-title-1">Faire Hundebegegnungen</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Ziehen oder Bellen an der Leine löst sich selten über Druck. Wer Distanzen rechtzeitig liest und Alternativverhalten klar belohnt, gewinnt Schritt für Schritt Entspannung zurück.
            </p>
          </div>
          {blog_cta_1}
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Ratgeber #3 · Auslastung</span>
              <span class="icon-box">{SVG_SEARCH}</span>
            </div>
            <h3 class="card-title-1">Auslastung über die Nase</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Hektische Hetzspiele putschen das Stresshormonlevel hoch. Konzentrierte Zielobjektsuche und Spurensuche fördern dagegen Gelassenheit, Selbstvertrauen und tiefe Zufriedenheit.
            </p>
          </div>
          {blog_cta_1}
        </div>
      </div>
    </div>
  </section>"""


def render_kurs_finder() -> str:
    return f"""
  <!-- INTERAKTIVER KURS- & TRAININGS-FINDER -->
  <section data-section="projektberater" id="projektberater" style="background-color:var(--bg-soft);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="calc_kicker">INTERAKTIVER KURS- &amp; TRAININGS-FINDER · BADEN &amp; 5413 BIRMENSTORF</div>
        <h2 class="section-title" data-slot="calc_title">Welcher Kurs passt zu Ihnen und Ihrem Hund?</h2>
        <p class="section-desc" data-slot="calc_desc">
          Wählen Sie das Alter Ihres Hundes, Ihren aktuellen Schwerpunkt und den bevorzugten Trainingstag. Unser Finder zeigt Ihnen sofort das passende Angebot bei Good for Dogs inklusive Uhrzeit und transparentem Tarif:
        </p>
      </div>

      <div class="grid-2">
        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">In 15 Sekunden auswählen</span>
              <span class="icon-box">{SVG_COMPASS}</span>
            </div>
            <h3 class="card-title-1" style="margin-bottom:12px;">1. Alter &amp; Lebensphase Ihres Hundes</h3>
            <div class="calc-option-grid" id="gfdCalcAgeGrid">
              <button type="button" class="calc-option-btn active" data-age="welpe" onclick="gfdSetCalc('age','welpe')">
                <span class="calc-opt-title">Welpe</span>
                <span class="calc-opt-sub">Ab der 8. bis ca. 16. Lebenswoche</span>
              </button>
              <button type="button" class="calc-option-btn" data-age="junghund" onclick="gfdSetCalc('age','junghund')">
                <span class="calc-opt-title">Junghund</span>
                <span class="calc-opt-sub">Ab 4 bis 6 Monaten &amp; Aufbau</span>
              </button>
              <button type="button" class="calc-option-btn" data-age="erwachsen" onclick="gfdSetCalc('age','erwachsen')">
                <span class="calc-opt-title">Erwachsen</span>
                <span class="calc-opt-sub">Familienhund, Tierschutz oder Senior</span>
              </button>
            </div>

            <h3 class="card-title-1" style="margin-bottom:12px;">2. Wichtigstes Trainingsziel</h3>
            <div class="calc-option-grid" id="gfdCalcGoalGrid">
              <button type="button" class="calc-option-btn active" data-goal="alltag" onclick="gfdSetCalc('goal','alltag')">
                <span class="calc-opt-title">Alltag &amp; Gruppe</span>
                <span class="calc-opt-sub">Grundsignale, Rückruf &amp; Soziales</span>
              </button>
              <button type="button" class="calc-option-btn" data-goal="nase" onclick="gfdSetCalc('goal','nase')">
                <span class="calc-opt-title">Nasenarbeit</span>
                <span class="calc-opt-sub">Schatzsuche, ZOS &amp; Spurensuche</span>
              </button>
              <button type="button" class="calc-option-btn" data-goal="verhalten" onclick="gfdSetCalc('goal','verhalten')">
                <span class="calc-opt-title">Einzelthema</span>
                <span class="calc-opt-sub">Leine, Bellen, Angst oder Zuhause</span>
              </button>
            </div>

            <h3 class="card-title-1" style="margin-bottom:12px;">3. Bevorzugter Trainingstag</h3>
            <div class="calc-option-grid" id="gfdCalcDayGrid" style="margin-bottom:0;">
              <button type="button" class="calc-option-btn active" data-day="montag" onclick="gfdSetCalc('day','montag')">
                <span class="calc-opt-title">Montag</span>
                <span class="calc-opt-sub">Nachmittag / früher Abend</span>
              </button>
              <button type="button" class="calc-option-btn" data-day="samstag" onclick="gfdSetCalc('day','samstag')">
                <span class="calc-opt-title">Samstag</span>
                <span class="calc-opt-sub">Vormittags in Kleingruppen</span>
              </button>
              <button type="button" class="calc-option-btn" data-day="flexibel" onclick="gfdSetCalc('day','flexibel')">
                <span class="calc-opt-title">Individuell</span>
                <span class="calc-opt-sub">Nach Vereinbarung bei Ihnen</span>
              </button>
            </div>
          </div>
          <div style="padding-top:14px;border-top:1px solid var(--border-light);font-size:0.82rem;color:var(--text-body);display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;">
            <span>Fairplay mit Hund · Gewaltfreies Training</span>
            <strong style="color:var(--gold-dark);">Good for Dogs · Martina Sidler</strong>
          </div>
        </div>

        <div class="content-card card-dark">
          <div>
            <div class="card-badge-row">
              <span class="top-bar-badge" id="gfdCalcBadge">EMPFEHLUNG: WELPEN-GRUPPE (AB 8 WOCHEN)</span>
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 style="font-size:1.34rem;font-weight:700;margin-bottom:8px;" id="gfdCalcHeadline">Welpen-Gruppe am Montagabend in Birmenstorf &amp; Region Baden</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;" id="gfdCalcDesc">
              Behutsame Sozialisierung, Rückruf-Aufbau, Umweltgewöhnung und gezielte Ruheübungen in einer überschaubaren Gruppe mit maximal fünf Teams. Ein Einstieg ist jederzeit möglich.
            </p>

            <div class="calc-kpi-grid">
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="gfdCalcPrice">CHF 35.— / Std.</div>
                <div class="calc-kpi-lbl" id="gfdCalcPriceSub">oder 10er-Abo CHF 300.— (4 Mt.)</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="gfdCalcSchedule">Montag, 18:00 Uhr</div>
                <div class="calc-kpi-lbl">Fester Kurstermin (60 Minuten)</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="gfdCalcGroup">Max. 5 Teams</div>
                <div class="calc-kpi-lbl">Viel Raum &amp; persönliche Anleitung</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="gfdCalcLoc">5413 Birmenstorf</div>
                <div class="calc-kpi-lbl">&amp; Gelände Baden – Lenzburg</div>
              </div>
            </div>

            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Ehrlich &amp; gewaltfrei:</strong> Wir trainieren mit positiver Verstärkung, klarer Körpersprache und ohne Leinenruck oder Einschüchterung.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Bequeme Zahlung:</strong> Unkompliziert per Überweisung oder direkt vor Ort via TWINT.</span></div>
            </div>
          </div>

          <a href="kontakt.html?thema=welpen" id="gfdCalcCta" class="btn-cta btn-cta-gold" style="width:100%;">
            <span>Platz unverbindlich anfragen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>"""


def render_impressum_modal() -> str:
    return f"""
  <!-- IMPRESSUM, AGB & DATENSCHUTZ MODAL -->
  <div class="wp-modal-backdrop" id="wpImpressumModal" role="dialog" aria-modal="true" aria-labelledby="wpImpTitle" data-allow-scroll="true">
    <div class="wp-modal-dialog" data-allow-scroll="true">
      <button type="button" class="wp-modal-close" aria-label="Dialog schliessen" onclick="wpCloseImpressumModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="section-kicker">RECHTLICHE ANGABEN &amp; TRAININGSBEDINGUNGEN · KANTON AARGAU</div>
      <h3 id="wpImpTitle" style="font-size:1.34rem;font-weight:700;margin-bottom:10px;">Impressum, AGB &amp; Datenschutz (Good for Dogs)</h3>
      <div style="font-size:0.87rem;color:var(--text-body);line-height:1.6;display:flex;flex-direction:column;gap:12px;">
        <div style="background-color:var(--bg-page);border:1px solid var(--border-light);border-left:4px solid var(--gold);padding:12px 14px;border-radius:var(--radius-sm);">
          <strong>Hundeschule Good for Dogs · Die Schule für Halter (und Hund)</strong><br>
          Inhaberin: Martina Sidler (Good) · Certodog® Hundeinstruktorin<br>
          Standort: Region 5406 Baden (Rütihof) · Eingezäunter Übungsplatz: CH-5413 Birmenstorf<br>
          Telefon: +41 76 454 54 06 · E-Mail: info@goodfordogs.ch · Web: https://goodfordogs.ch
        </div>
        <p>
          <strong>Wichtige Trainingsbedingungen (Auszug AGB):</strong><br>
          Teilnehmende Hunde müssen altersgemäss geimpft, frei von ansteckenden Krankheiten und über eine gültige Privathaftpflichtversicherung der Halterin oder des Halters gedeckt sein. Läufige Hündinnen bitte vorab kurz melden. Die Kursleitung arbeitet gewaltfrei; tierschutzwidriges Zubehör ist auf dem Platz und im Gelände ausgeschlossen.
        </p>
        <p>
          <strong>Abmeldung &amp; Abonnemente:</strong><br>
          Gruppenstunden können bis 24 Stunden vor Beginn, Einzeltrainings bis 48 Stunden vor dem vereinbarten Termin kostenfrei verschoben oder abgesagt werden. 10er-Abonnemente der Welpen- und Familienhundegruppe sind 4 Monate gültig (Welpen-Restguthaben übertragbar auf Folgekurs), Schnüffelspass-10er-Abos sind 6 Monate gültig. Zahlung per Überweisung oder TWINT.
        </p>
        <p>
          <strong>Datenschutz (Schweizer DSG) &amp; Urheberrecht:</strong><br>
          Alle Angaben aus der 3-Schritte Smart-Anmeldung werden vertraulich behandelt und ausschliesslich zur Kursorganisation und Rückmeldung durch Martina Sidler verwendet. Sämtliche Fotografien, Logos und Texte sind urheberrechtlich geschütztes Eigentum von Good for Dogs.
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
      if (cEl && category) cEl.textContent = 'Kurs- & Themenbereich: ' + category;
      if (pEl && person) pEl.textContent = 'Kursleitung: ' + person;
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

    var gfdCalcState = { age: 'welpe', goal: 'alltag', day: 'montag' };
    function gfdSetCalc(group, val) {
      gfdCalcState[group] = val;
      var gridId = group === 'age' ? 'gfdCalcAgeGrid' : (group === 'goal' ? 'gfdCalcGoalGrid' : 'gfdCalcDayGrid');
      var attr = 'data-' + group;
      var btns = document.querySelectorAll('#' + gridId + ' .calc-option-btn');
      for (var i = 0; i < btns.length; i++) {
        btns[i].classList.toggle('active', btns[i].getAttribute(attr) === val);
      }
      gfdUpdateCalcView();
    }
    function gfdUpdateCalcView() {
      var badge = document.getElementById('gfdCalcBadge');
      var head = document.getElementById('gfdCalcHeadline');
      var desc = document.getElementById('gfdCalcDesc');
      var pEl = document.getElementById('gfdCalcPrice');
      var pSub = document.getElementById('gfdCalcPriceSub');
      var sEl = document.getElementById('gfdCalcSchedule');
      var gEl = document.getElementById('gfdCalcGroup');
      var lEl = document.getElementById('gfdCalcLoc');
      var cta = document.getElementById('gfdCalcCta');
      if (!head) return;

      if (gfdCalcState.goal === 'verhalten' || gfdCalcState.day === 'flexibel') {
        badge.textContent = 'EMPFEHLUNG: INDIVIDUELLES EINZELTRAINING (1:1)';
        head.textContent = 'Einzeltraining & Verhaltensberatung bei Ihnen im Alltag';
        desc.textContent = 'Wir schauen uns Ihre Situation direkt im Wohnumfeld und auf Ihren Spazierwegen an: massgeschneidert bei Leinenstress, Unsicherheit, Rückruf, Bellen oder Alleinebleiben.';
        pEl.textContent = 'CHF 80.— / 60 Min.';
        pSub.textContent = 'Anfahrt CHF 1.— pro km';
        sEl.textContent = 'Nach Vereinbarung';
        gEl.textContent = '1:1 Begleitung';
        lEl.textContent = 'Hausbesuch & Region Baden';
        if (cta) cta.href = 'kontakt.html?thema=einzeltraining';
      } else if (gfdCalcState.goal === 'nase') {
        badge.textContent = 'EMPFEHLUNG: SCHNÜFFELSPASS-GRUPPE (AB 6 MONATEN)';
        head.textContent = 'Schnüffelspass: Zielobjektsuche, Geruch & Mantrailing';
        desc.textContent = 'Ruhige, hochkonzentrierte Nasenarbeit auf dem eingezäunten Gelände in Birmenstorf. Da jedes Team einzeln arbeitet, fühlen sich auch sensible Hunde rundum wohl.';
        pEl.textContent = 'CHF 40.— / 60 Min.';
        pSub.textContent = 'oder 10er-Abo CHF 350.— (6 Mt.)';
        sEl.textContent = 'Jeden 2. Sa, 10:30 Uhr';
        gEl.textContent = 'Max. 3 Teams';
        lEl.textContent = '5413 Birmenstorf (eingezäunt)';
        if (cta) cta.href = 'kontakt.html?thema=schnueffelspass';
      } else if (gfdCalcState.age === 'welpe') {
        badge.textContent = 'EMPFEHLUNG: WELPEN-GRUPPE (AB 8 WOCHEN)';
        head.textContent = 'Welpen-Gruppe am Montagabend in Birmenstorf & Region Baden';
        desc.textContent = 'Behutsame Sozialisierung, Rückruf-Aufbau, Umweltgewöhnung und gezielte Ruheübungen in einer überschaubaren Gruppe mit maximal fünf Teams. Ein Einstieg ist jederzeit möglich.';
        pEl.textContent = 'CHF 35.— / 60 Min.';
        pSub.textContent = 'oder 10er-Abo CHF 300.— (4 Mt.)';
        sEl.textContent = 'Montag, 18:00 Uhr';
        gEl.textContent = 'Max. 5 Teams';
        lEl.textContent = '5413 Birmenstorf & Gelände';
        if (cta) cta.href = 'kontakt.html?thema=welpen';
      } else if (gfdCalcState.age === 'junghund' && gfdCalcState.day === 'samstag') {
        badge.textContent = 'EMPFEHLUNG: ERZIEHUNGSKURS 1 & 2 (SAMSTAGVORMITTAG)';
        head.textContent = 'Aufbauender Erziehungskurs 1 (09:00 Uhr) oder 2 (10:15 Uhr)';
        desc.textContent = 'Strukturierter 10-Lektionen-Kurs für Junghunde ab 6 Monaten und neu übernommene Hunde: von lockerer Leine und Impulskontrolle bis zu Distanzarbeit und Freilauf.';
        pEl.textContent = 'CHF 300.— / Kurs';
        pSub.textContent = '10 Lektionen à 60 Minuten';
        sEl.textContent = 'Samstag, 09:00 / 10:15';
        gEl.textContent = 'Max. 6 Teams';
        lEl.textContent = 'Birmenstorf & Baden–Lenzburg';
        if (cta) cta.href = 'kontakt.html?thema=junghunde';
      } else {
        badge.textContent = 'EMPFEHLUNG: FAMILIENHUNDE-GRUPPE (AB 16 WOCHEN)';
        head.textContent = 'Familienhunde-Gruppe am Montagnachmittag';
        desc.textContent = 'Spass, Alltagstauglichkeit, feine Körpersprache und abwechslungsreiche Beschäftigung für junge und erwachsene Familienhunde. Ein Einstieg ist jederzeit möglich.';
        pEl.textContent = 'CHF 35.— / 60 Min.';
        pSub.textContent = 'oder 10er-Abo CHF 300.— (4 Mt.)';
        sEl.textContent = 'Montag, 16:30 Uhr';
        gEl.textContent = 'Max. 6 Teams';
        lEl.textContent = 'Birmenstorf & Baden–Lenzburg';
        if (cta) cta.href = 'kontakt.html?thema=familienhunde';
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
  <meta name="description" content="Hundeschule Good for Dogs in 5406 Baden (Rütihof), 5413 Birmenstorf und Region Lenzburg: Gewaltfreies Einzeltraining, Welpengruppe, Junghunde-Erziehungskurse, Familienhunde und Schnüffelspass mit Certodog® Hundeinstruktorin Martina Sidler.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,400&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Good for Dogs · Hundeschule Martina Sidler",
    "url": "https://goodfordogs.ch",
    "telephone": "+41 76 454 54 06",
    "email": "info@goodfordogs.ch",
    "founder": "Martina Sidler",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Region Baden-Rütihof · Übungsplatz 5413 Birmenstorf",
      "postalCode": "5406",
      "addressLocality": "Baden",
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
        <span class="top-bar-badge" data-slot="topbar_badge">CERTODOG® HUNDEINSTRUKTORIN · FAIRPLAY MIT HUND</span>
        <span data-slot="topbar_sub">Martina Sidler · 5406 Baden, Übungsplatz 5413 Birmenstorf &amp; Region Lenzburg</span>
      </div>
      <div class="top-bar-links">
        <a href="tel:+41764545406">{SVG_PHONE} <span>076 454 54 06</span></a>
        <a href="mailto:info@goodfordogs.ch">{SVG_MAIL} <span>info@goodfordogs.ch</span></a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER -->
  <header class="site-header" data-section="header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="Good for Dogs Hundeschule Baden Startseite">
        <img src="images/logo-good-for-dogs.png" alt="Good for Dogs Logo" class="brand-logo-wide" width="142" height="46" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">Good for Dogs</span>
          <span class="brand-sub" data-slot="brand_sub">Baden &amp; Birmenstorf</span>
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
          <span>Kurs anfragen</span>
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
    <a href="leistungen.html" onclick="wpCloseMobileMenu()">Angebot &amp; Preise (Alle 6 Kurse &amp; Einzeltraining)</a>
    <a href="referenzen.html" onclick="wpCloseMobileMenu()">Trainings-Einblicke, Übungsplatz &amp; Qualitätssiegel</a>
    <a href="ueber-uns.html" onclick="wpCloseMobileMenu()">Über Martina Sidler, Ausbildungen &amp; Philosophie</a>
    <a href="kontakt.html" onclick="wpCloseMobileMenu()">3-Schritte Kursanmeldung &amp; Direktkontakt</a>
  </div>

  <main>
{body_html}
  </main>

  <!-- FOOTER -->
  <footer class="site-footer" data-section="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div style="margin-bottom:14px;">
            <img src="images/logo-good-for-dogs.png" alt="Good for Dogs Hundeschule Baden" width="168" height="54" style="height:50px;width:auto;" loading="lazy" decoding="async">
          </div>
          <p style="font-size:0.86rem;color:var(--text-body);line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Die Schule für Halter (und Hund). Gewaltfreies, kynologisch fundiertes Hundetraining in Kleingruppen und im 1:1-Alltag in Baden, Birmenstorf und der Region Lenzburg.
          </p>
          <div style="font-size:0.84rem;color:var(--text-main);font-weight:600;">
            Region 5406 Baden (Rütihof) · Übungsplatz: 5413 Birmenstorf
          </div>
        </div>

        <div>
          <div class="footer-title">Kurse &amp; Training</div>
          <ul class="footer-list">
            <li><a href="leistungen.html#einzeltraining">Einzeltraining &amp; Beratung (CHF 80.—)</a></li>
            <li><a href="leistungen.html#welpen">Welpen-Gruppe (Mo 18:00 Uhr)</a></li>
            <li><a href="leistungen.html#erziehung1">Erziehungskurs 1 &amp; 2 (Samstag)</a></li>
            <li><a href="leistungen.html#familienhunde">Familienhunde &amp; Schnüffelspass</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Orientierung &amp; Wissen</div>
          <ul class="footer-list">
            <li><a href="index.html#projektberater">Interaktiver Kurs-Finder</a></li>
            <li><a href="referenzen.html">Übungsplatz &amp; Einblicke</a></li>
            <li><a href="ueber-uns.html">Über Martina Sidler (Certodog®)</a></li>
            <li><a href="https://www.instagram.com/goodfordogs.ch/" target="_blank" rel="noopener">Instagram @goodfordogs.ch</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; AGB</div>
          <ul class="footer-list">
            <li><a href="tel:+41764545406">Telefon: 076 454 54 06</a></li>
            <li><a href="mailto:info@goodfordogs.ch">E-Mail: info@goodfordogs.ch</a></li>
            <li><a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">3-Schritte Kursanmeldung</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum, AGB &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Hundeschule Good for Dogs · Martina Sidler (5406 Baden &amp; 5413 Birmenstorf). Alle Rechte vorbehalten.</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
          <a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">Kursplatz anfragen</a>
          <a href="https://g.page/r/CYlfntsgxqtfEBM/review" target="_blank" rel="noopener" style="color:var(--text-body);">Google-Bewertungen</a>
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
  <meta name="description" content="Hundeschule Good for Dogs in Baden & Birmenstorf (Zeigeversion): Gewaltfreies Einzeltraining, Welpengruppe, Erziehungskurse, Familienhunde und Schnüffelspass mit Martina Sidler.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,400&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Good for Dogs · Hundeschule Martina Sidler",
    "url": "https://goodfordogs.ch",
    "telephone": "+41 76 454 54 06",
    "email": "info@goodfordogs.ch",
    "founder": "Martina Sidler",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Region Baden-Rütihof · Übungsplatz 5413 Birmenstorf",
      "postalCode": "5406",
      "addressLocality": "Baden",
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
      <a href="index.html" class="brand-link" aria-label="Good for Dogs Hundeschule Baden Startseite">
        <img src="images/logo-good-for-dogs.png" alt="Good for Dogs Logo" class="brand-logo-wide" width="142" height="46" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">Good for Dogs</span>
          <span class="brand-sub" data-slot="brand_sub">Baden &amp; Birmenstorf</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}" data-nav-href="index.html">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#15803D"/></svg>
          <span>Startseite</span>
        </a>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="leistungen.html" onclick="wpOpenBlueprintModal('Alle 6 Kurse, Wochenplan, Abos &amp; Preise im Detail', 'Einzeltraining (CHF 80.—), Welpen (Mo 18:00), Erziehungskurs 1 &amp; 2 (Sa), Familienhunde (Mo 16:30) &amp; Schnüffelspass', 'Martina Sidler (Certodog®)')">
          <span>Angebot</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="referenzen.html" onclick="wpOpenBlueprintModal('Trainings-Einblicke, Übungsplatz Birmenstorf &amp; Qualitätssiegel', 'Kleingruppen (max. 3 bis 6 Teams), Fairplay mit Hund, Gewaltfreies Hundetraining &amp; Google-Stimmen', 'Martina Sidler')">
          <span>Einblicke</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="ueber-uns.html" onclick="wpOpenBlueprintModal('Über Martina Sidler, Certodog®-Ausbildungen &amp; Fachseminare', 'Certodog® Hundeinstruktorin, FBA-Ausbildungen, Praktische Psychologie (2026) &amp; 18+ Fachweiterbildungen', 'Martina Sidler')">
          <span>Über mich</span>
        </button>
        <a href="kontakt.html" class="nav-link {nav_kontakt}" data-nav-href="kontakt.html">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#15803D"/></svg>
          <span>Kontakt</span>
        </a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" data-slot="header_cta">
          <span>3-Schritte-Anmeldung testen</span>
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
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu();wpOpenBlueprintModal('Alle 6 Kurse, Wochenplan, Abos &amp; Preise im Detail', 'Einzeltraining, Welpen, Erziehungskurs 1 &amp; 2, Familienhunde &amp; Schnüffelspass', 'Martina Sidler')">
      <span>Angebot</span>
      <span class="preview-status-badge">Folgt beim Ausbau</span>
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu();wpOpenBlueprintModal('Trainings-Einblicke, Übungsplatz Birmenstorf &amp; Qualitätssiegel', 'Echte Bilder aus dem Training, Fairplay mit Hund &amp; Initiative gewaltfreies Hundetraining', 'Martina Sidler')">
      <span>Einblicke</span>
      <span class="preview-status-badge">Folgt beim Ausbau</span>
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu();wpOpenBlueprintModal('Über Martina Sidler, Certodog®-Ausbildungen &amp; Fachseminare', 'Porträt, Philosophie &amp; vollständiges Aus- und Weiterbildungs-Dossier (2020–2026)', 'Martina Sidler')">
      <span>Über mich</span>
      <span class="preview-status-badge">Folgt beim Ausbau</span>
    </button>
    <a href="kontakt.html" onclick="wpCloseMobileMenu()">Kontakt &amp; 3-Schritte Kursanmeldung (Ausgearbeitet)</a>
  </div>

  <main>
{body_html}
  </main>

  <!-- FOOTER (ZEIGEVERSION) -->
  <footer class="site-footer" data-section="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div style="margin-bottom:14px;">
            <img src="images/logo-good-for-dogs.png" alt="Good for Dogs Hundeschule Baden" width="168" height="54" style="height:50px;width:auto;" loading="lazy" decoding="async">
          </div>
          <p style="font-size:0.86rem;color:var(--text-body);line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Die Schule für Halter (und Hund). Gewaltfreies, kynologisch fundiertes Hundetraining in Kleingruppen und im 1:1-Alltag in Baden, Birmenstorf und der Region Lenzburg.
          </p>
          <div style="font-size:0.84rem;color:var(--text-main);font-weight:600;">
            Region 5406 Baden (Rütihof) · Übungsplatz: 5413 Birmenstorf
          </div>
        </div>

        <div>
          <div class="footer-title">Bereits in dieser Vorschau live</div>
          <ul class="footer-list">
            <li><a href="index.html">Startseite mit allen 6 Kursen &amp; Tarifen</a></li>
            <li><a href="index.html#projektberater">Interaktiver Kurs- &amp; Trainings-Finder</a></li>
            <li><a href="kontakt.html">3-Schritte Smart-Anmeldung (inkl. PDF)</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Weitere Detailseiten (Ausbau)</div>
          <ul class="footer-list">
            <li><button type="button" onclick="wpOpenBlueprintModal('Alle 6 Kurse, Wochenplan &amp; Preise im Detail', 'Einzeltraining, Welpen, Erziehungskurs 1 &amp; 2, Familienhunde &amp; Schnüffelspass', 'Martina Sidler')">Angebot im Detail (Vorschau)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Trainings-Einblicke &amp; Übungsplatz Birmenstorf', 'Kleingruppen, Alltagsorte Baden–Lenzburg &amp; Qualitätssiegel', 'Martina Sidler')">Einblicke &amp; Platz (Vorschau)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Über Martina Sidler &amp; Ausbildungen', 'Certodog®, FBA, Praktische Psychologie &amp; Fachweiterbildungen', 'Martina Sidler')">Über Martina Sidler (Vorschau)</button></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; Rechtliches</div>
          <ul class="footer-list">
            <li><a href="tel:+41764545406">Telefon: 076 454 54 06</a></li>
            <li><a href="mailto:info@goodfordogs.ch">E-Mail: info@goodfordogs.ch</a></li>
            <li><a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">3-Schritte-Anmeldung testen</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum, AGB &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Hundeschule Good for Dogs (Martina Sidler) · Unverbindlicher Vorschau-Entwurf (Zeigeversion).</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;">
          <a href="kontakt.html" style="color:var(--gold-dark);font-weight:700;">Smart-Anmeldung testen</a>
          <a href="index.html#weitere-themenbereiche" style="color:var(--text-body);">Weitere Detailseiten</a>
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
      <div class="section-kicker">UNVERBINDLICHER VORSCHAU-ENTWURF FÜR GOODFORDOGS.CH</div>
      <h3 id="wpBpTitle" style="font-size:1.34rem;font-weight:700;margin-bottom:8px;">Unverbindlicher Vorschau-Entwurf für Good for Dogs</h3>
      <p id="wpBpSub" style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
        In dieser <strong>Zeigeversion (2 Beispiel-Seiten ausgearbeitet)</strong> sehen Sie Ihre neue Startseite mit allen 6 Kursangeboten, dem interaktiven Kurs-Finder, den Social-Media- &amp; Ratgeber-Einblicken sowie den live funktionierenden 3-Schritte Smart-Anmelde-Assistenten. Dieser vertiefte Bereich wird beim gemeinsamen Ausbau schlüsselfertig mit allen Originaldaten freigeschaltet.
      </p>
      <div style="background-color:var(--gold-soft);border-left:4px solid var(--gold);padding:12px 14px;border-radius:var(--radius-sm);font-size:0.86rem;margin-bottom:14px;">
        <div style="font-weight:700;color:var(--charcoal-deep);" id="wpBpCategory">Kurs- &amp; Themenbereich: Vorbereitet für den gemeinsamen Ausbau</div>
        <div style="color:var(--text-body);margin-top:2px;" id="wpBpContact">Kursleitung: Martina Sidler (Certodog® Hundeinstruktorin)</div>
      </div>

      <div class="wp-modal-checklist">
        <div style="font-family:var(--font-sans);font-size:0.8rem;font-weight:700;text-transform:uppercase;color:var(--charcoal-deep);">
          Was beim gemeinsamen Ausbau in diesem Themenbereich enthalten ist:
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Vollständige Angebotsseite mit Einzeltraining (CHF 80.—/60 Min.), Welpen-Gruppe (Mo 18:00), Erziehungskurs 1 &amp; 2 (Sa), Familienhunden (Mo 16:30), Schnüffelspass und Mitbring-Checkliste</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Eigene Einblicke-Seite zum eingezäunten Übungsplatz in 5413 Birmenstorf, den Alltagsorten zwischen Baden und Lenzburg sowie den Siegeln «Fairplay mit Hund» und «Gewaltfreies Hundetraining»</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Persönliche Porträtseite über Martina Sidler mit sämtlichen Certodog®- und FBA-Qualifikationen sowie allen Fachweiterbildungen (2020–2026)</span>
        </div>
      </div>

      <div style="display:flex;gap:10px;flex-wrap:wrap;justify-content:flex-end;">
        <button type="button" class="btn-cta btn-cta-primary btn-sm" onclick="wpCloseBlueprintModal()">
          <span>Verstanden · Vorschau weiter ansehen</span>
        </button>
        <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm">
          <span>3-Schritte-Anmeldung testen</span>
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
        <div class="section-kicker kicker-light" data-slot="hero_kicker">HUNDESCHULE IN BADEN, 5413 BIRMENSTORF &amp; REGION LENZBURG</div>
        <h1 class="hero-title" data-slot="hero_title">
          Die Schule für Halter <span>(und Hund).</span>
        </h1>
        <p class="hero-lead" data-slot="hero_lead">
          Bei <strong>Good for Dogs</strong> begleite ich Sie und Ihren Hund fair, gewaltfrei und mit viel Alltagsbezug: vom behutsamen Welpenstart über Junghunde- und Familienhundekurse bis zum individuellen Einzeltraining und konzentrierten Schnüffelspass.
        </p>
        <div class="hero-quote-box">
          «Ein gut erzogener Hund klaut dir kein Essen, er macht dir solange ein schlechtes Gewissen, bis du freiwillig teilst.»
        </div>
        <div class="hero-actions">
          <a href="#projektberater" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
            <span>Passenden Kurs finden</span>
            {SVG_ARROW}
          </a>
          <a href="kontakt.html" class="btn-cta btn-cta-outline-light" data-slot="hero_cta_secondary">
            <span>Kursplatz oder Termin anfragen</span>
          </a>
        </div>
        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Certodog® &amp; FBA</span>
            <span class="hero-badge-lbl">Geprüfte Hundeinstruktorin Martina Sidler</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Max. 3 bis 6 Teams</span>
            <span class="hero-badge-lbl">Kleine Gruppen für individuelle Betreuung</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Fair &amp; Gewaltfrei</span>
            <span class="hero-badge-lbl">Mitglied Fairplay mit Hund &amp; IGH</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Birmenstorf &amp; Baden</span>
            <span class="hero-badge-lbl">Eingezäunter Platz &amp; echtes Alltagsgelände</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/hero-mensch-hund-alltag.jpg" alt="Martina Sidler beim Hundetraining mit aufmerksamem Hund im Freien" width="880" height="586" data-slot="hero_image">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:var(--font-sans);font-size:0.74rem;font-weight:700;text-transform:uppercase;color:var(--gold-dark);">Training auf Augenhöhe · Kanton Aargau</div>
            <div style="font-size:0.88rem;font-weight:700;color:var(--text-main);">Übungsplatz 5413 Birmenstorf &amp; Gelände Baden–Lenzburg</div>
          </div>
          <a href="leistungen.html" class="btn-cta btn-cta-outline btn-sm">
            <span>Alle 6 Angebote</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- 3 KERN-SÄULEN (ZIELGRUPPEN) -->
  <section data-section="zielgruppen" id="zielgruppen">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="pillars_kicker">WARUM DIE SCHULE FÜR HALTER (UND HUND)?</div>
        <h2 class="section-title" data-slot="pillars_title">Verständliche Körpersprache, faire Führung und echte Freude</h2>
        <p class="section-desc" data-slot="pillars_desc">
          Ob frisch eingezogener Welpe, stürmischer Junghund oder ein konkretes Alltagsthema: Wir trainieren in ruhigen Kleingruppen ohne Überforderung, damit Lernen auf beiden Seiten der Leine Spass macht.
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Säule 1 · Junge Hunde</span>
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 class="card-title-1">Welpen &amp; Junghunde</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Vom sicheren Bindungsaufbau ab der 8. Woche bis zu den aufbauenden Erziehungskursen 1 und 2 am Samstagvormittag.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Dosierte Umweltreize &amp; bewusste Ruhephasen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Lockere Leine, Rückruf &amp; Impulskontrolle</span></div>
            </div>
          </div>
          <a href="leistungen.html#welpen" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Welpen- &amp; Junghundekurse</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Säule 2 · Alltag &amp; Nase</span>
              <span class="icon-box">{SVG_SEARCH}</span>
            </div>
            <h3 class="card-title-1">Familienhunde &amp; Nase</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Sinnvolle geistige und körperliche Auslastung für Hunde ab 16 Wochen in der Familienhunde-Gruppe oder beim Schnüffelspass.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Zielobjektsuche, Geruch &amp; Mantrailing (max. 3 Teams)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Einstieg jederzeit möglich · 10er-Abo verfügbar</span></div>
            </div>
          </div>
          <a href="leistungen.html#familienhunde" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Gruppenstunden ansehen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Säule 3 · Individuell</span>
              <span class="icon-box">{SVG_HOME}</span>
            </div>
            <h3 class="card-title-1">1:1 Einzeltraining</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Persönliche Verhaltensberatung direkt bei Ihnen zu Hause und auf Ihren gewohnten Spazierwegen im Raum Baden und Aargau.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Hilfe bei Leinenstress, Unsicherheit, Angst &amp; Bellen</span></div>
              <div class="check-item">{SVG_CHECK} <span>CHF 80.— pro 60 Min. (zzgl. CHF 1.— / km Anfahrt)</span></div>
            </div>
          </div>
          <a href="leistungen.html#einzeltraining" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Einzeltraining entdecken</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- ALLE 6 KURSE & PREISE -->
  <section data-section="kernangebote" id="angebot" style="background-color:#FFFFFF;border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="services_kicker">ALLE 6 ANGEBOTE AUF EINEN BLICK · TRANSPARENTE TARIFE</div>
        <h2 class="section-title" data-slot="services_title">Unsere Kurse, Wochentage und Preise</h2>
        <p class="section-desc" data-slot="services_desc">
          Kleine Gruppen garantieren, dass jedes Mensch-Hund-Team individuell begleitet wird. Bequeme Zahlung per Überweisung oder direkt vor Ort via TWINT:
        </p>
      </div>

      {render_courses_grid(is_v2=False)}
    </div>
  </section>

{render_kurs_finder()}

  <!-- TRAININGS-EINBLICKE & QUALITÄTSSIEGEL -->
  <section data-section="referenzen-auszug" id="einblicke">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="refs_kicker">PRAXIS-EINBLICKE · 5413 BIRMENSTORF &amp; GELÄNDE BADEN–LENZBURG</div>
        <h2 class="section-title" data-slot="refs_title">So trainieren wir bei Good for Dogs</h2>
        <p class="section-desc" data-slot="refs_desc">
          Kombination aus geschütztem, eingezäuntem Übungsplatz in Birmenstorf und abwechslungsreichen Trainingsorten im Alltag zwischen Baden und Lenzburg:
        </p>
      </div>

      {render_references_grid(limit=6, is_v2=False)}
    </div>
  </section>

{render_acp_bridge_sections(is_v2=False)}

  <!-- ÜBER MARTINA SIDLER AUSZUG -->
  <section data-section="ueber-uns" id="ueber-martina" style="background-color:#FFFFFF;border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="grid-2">
        <div class="founder-card">
          <div class="founder-top">
            <img src="images/team-martina-sidler-portrait.jpg" alt="Martina Sidler, Inhaberin Hundeschule Good for Dogs in Baden" class="founder-portrait" loading="lazy" decoding="async">
            <div>
              <div class="section-kicker" style="margin-bottom:6px;">IHRE ANSPRECHPARTNERIN</div>
              <h2 style="font-size:1.55rem;font-weight:700;margin-bottom:6px;">Martina Sidler (Good)</h2>
              <p style="font-size:0.84rem;font-weight:700;color:var(--gold-dark);margin-bottom:10px;">
                Certodog® Hundeinstruktorin · FBA-Tierbetreuerin &amp; -Züchterin
              </p>
              <p style="font-size:0.9rem;color:var(--text-body);">
                Mit fundiertem kynologischem Wissen, laufendem Psychologie-Studium (2026) und viel Einfühlungsvermögen begleite ich Halterinnen, Halter und ihre Hunde auf dem Weg zu einem entspannten Miteinander.
              </p>
            </div>
          </div>
          <div class="founder-body">
            <div class="seal-strip">
              <div class="seal-item">
                <img src="images/siegel-fairplay-mit-hund.png" alt="Qualitätssiegel Fairplay mit Hund" loading="lazy" decoding="async">
                <div>
                  <div style="font-weight:700;font-size:0.84rem;color:var(--text-main);">Fairplay mit Hund</div>
                  <div style="font-size:0.76rem;color:var(--text-muted);">Respektvoller Umgang</div>
                </div>
              </div>
              <div class="seal-item">
                <img src="images/siegel-initiative-gewaltfrei.jpg" alt="Initiative für gewaltfreies Hundetraining" loading="lazy" decoding="async">
                <div>
                  <div style="font-weight:700;font-size:0.84rem;color:var(--text-main);">Gewaltfreies Training</div>
                  <div style="font-size:0.76rem;color:var(--text-muted);">Geprüftes Mitglied</div>
                </div>
              </div>
            </div>
            <a href="ueber-uns.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
              <span>Alle Ausbildungen &amp; Fachseminare ansehen</span>
              {SVG_ARROW}
            </a>
          </div>
        </div>

        <div class="content-card card-dark">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Unsere Grundsätze</span>
              <span class="icon-box">{SVG_SHIELD}</span>
            </div>
            <h3 style="font-size:1.38rem;font-weight:700;margin-bottom:10px;">Warum Halterinnen und Halter gerne zu uns kommen</h3>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:14px;">
              Jedes Mensch-Hund-Team bringt seine eigene Persönlichkeit mit. Darum gibt es bei Good for Dogs kein starres Schema, sondern individuell angepasste Lernschritte:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Kleine Gruppengrössen:</strong> Maximal 3 Teams beim Schnüffelspass, 5 Teams bei den Welpen und 6 Teams in den Erziehungskursen.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Alltagsnahes Training:</strong> Eingezäunter Platz in 5413 Birmenstorf kombiniert mit echten Begegnungsorten zwischen Baden und Lenzburg.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>18+ Fachweiterbildungen (2020–2026):</strong> Aktuelles Wissen u. a. bei Dr. Esther Schalke, Celina del Amo, Dr. Annika Bremhorst &amp; Dr. Sabine Mai.</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Faire Konditionen:</strong> Transparente Einzellektionen oder 10er-Abos, zahlbar per Überweisung oder TWINT.</span></div>
            </div>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-primary" style="width:100%;">
            <span>Jetzt unverbindlich Kontakt aufnehmen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- HÄUFIGE FRAGEN (FAQS) -->
  <section data-section="faqs" id="faqs">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="faq_kicker">HÄUFIGE FRAGEN · KURSE, MITBRINGEN &amp; ORGANISATION</div>
        <h2 class="section-title" data-slot="faq_title">Gut vorbereitet in Ihre erste Trainingsstunde</h2>
        <p class="section-desc" data-slot="faq_desc">
          Die wichtigsten Antworten rund um Einstieg, Übungsplatz Birmenstorf, Ausrüstung, TWINT-Zahlung und Abmeldefristen auf einen Blick:
        </p>
      </div>

      {render_faqs_grid()}
    </div>
  </section>
"""


# ==============================================================================
# SEITEN-INHALTE: V1 LEISTUNGEN (leistungen.html)
# ==============================================================================
V1_LEISTUNGEN_BODY = f"""
  <section class="hero-section" data-section="hero-leistungen">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">ANGEBOT, WOCHENPLAN &amp; TARIFE · BADEN &amp; 5413 BIRMENSTORF</div>
        <h1 class="hero-title">
          Kurse &amp; Einzeltraining <span>mit System und Herz.</span>
        </h1>
        <p class="hero-lead">
          Ob Einzelberatung bei Ihnen zu Hause, behutsame Welpenprägung am Montagabend, strukturierte Erziehungskurse am Samstagvormittag oder konzentrierte Nasenarbeit: Hier finden Sie alle sechs Angebote transparent im Überblick.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>Direkt zur 3-Schritte-Anmeldung</span>
            {SVG_ARROW}
          </a>
          <a href="#mitbringen" class="btn-cta btn-cta-outline-light">
            <span>Was mitbringen?</span>
          </a>
        </div>
        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Montag 16:30 &amp; 18:00</span>
            <span class="hero-badge-lbl">Familienhunde &amp; Welpen-Gruppe</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Samstag ab 09:00 Uhr</span>
            <span class="hero-badge-lbl">Erziehungskurs 1, Kurs 2 &amp; Schnüffelspass</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/kurs-junghunde-erziehung.jpg" alt="Aufmerksamer Junghund blickt beim Training zu seiner Halterin hoch" style="object-position:center 35%;">
        <div class="hero-media-caption">
          <div>
            <div style="font-size:0.74rem;font-weight:700;text-transform:uppercase;color:var(--gold-dark);">Kleine Gruppen · Grosse Wirkung</div>
            <div style="font-size:0.88rem;font-weight:700;color:var(--text-main);">Maximal 3 bis 6 Teams pro Kursstunde</div>
          </div>
          <a href="tel:+41764545406" class="btn-cta btn-cta-outline btn-sm">
            <span>076 454 54 06</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <section data-section="alle-kurse">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">DETAILLIERTE KURSÜBERSICHT · ALLE 6 ANGEBOTE</div>
        <h2 class="section-title">Wählen Sie das passende Training für Ihr Team</h2>
        <p class="section-desc">
          Alle Gruppenstunden dauern 60 Minuten. Die Bezahlung erfolgt unkompliziert im Voraus per Überweisung oder vor Ort via TWINT.
        </p>
      </div>

      {render_courses_grid(is_v2=False)}
    </div>
  </section>

  <section id="mitbringen" data-section="ausruestung" style="background-color:var(--bg-soft);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">PRAKTISCHE CHECKLISTE &amp; KONDITIONEN</div>
        <h2 class="section-title">Gut ausgerüstet auf den Platz und ins Gelände</h2>
        <p class="section-desc">
          Damit wir die Trainingszeit optimal nutzen können, helfen Ihnen diese praktischen Hinweise zur Vorbereitung:
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Ausrüstung</span>
              <span class="icon-box">{SVG_CHECK}</span>
            </div>
            <h3 class="card-title-1">Bitte ans Training mitbringen</h3>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Gut sitzendes Brustgeschirr oder Halsband</span></div>
              <div class="check-item">{SVG_CHECK} <span>Normale Führleine (keine Flexi- oder Rollleine)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Viele kleine, weiche Belohnungshappen &amp; Spielzeug</span></div>
              <div class="check-item">{SVG_CHECK} <span>Wasser für den Hund &amp; Decke für Ruheübungen</span></div>
            </div>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Frage zur Ausrüstung stellen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Abos &amp; Gültigkeit</span>
              <span class="icon-box">{SVG_CALENDAR}</span>
            </div>
            <h3 class="card-title-1">Faire Abo-Regelungen</h3>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Welpen- &amp; Familienhunde-10er-Abo: CHF 300.— (4 Monate gültig)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Offene Welpen-Lektionen auf den Junghundekurs übertragbar</span></div>
              <div class="check-item">{SVG_CHECK} <span>Schnüffelspass-10er-Abo: CHF 350.— (6 Monate gültig)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Erziehungskurs 1 &amp; 2: fester 10er-Kursblock für CHF 300.—</span></div>
            </div>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>10er-Abo oder Kurs buchen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Fristen &amp; Schutz</span>
              <span class="icon-box">{SVG_SHIELD}</span>
            </div>
            <h3 class="card-title-1">Abmeldung &amp; Gesundheit</h3>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Gruppenstunden bis 24 Std. vorher kostenfrei abmeldbar</span></div>
              <div class="check-item">{SVG_CHECK} <span>Einzeltrainings bis 48 Std. vor Termin kostenfrei verschiebbar</span></div>
              <div class="check-item">{SVG_CHECK} <span>Altersgemässer Impfschutz &amp; Privathaftpflicht obligatorisch</span></div>
              <div class="check-item">{SVG_CHECK} <span>Läufige Hündinnen bitte vorab kurz telefonisch melden</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenImpressumModal()">
            <span>Vollständige AGB lesen</span>
            {SVG_ARROW}
          </button>
        </div>
      </div>
    </div>
  </section>
"""


# ==============================================================================
# SEITEN-INHALTE: V1 EINBLICKE & REFERENZEN (referenzen.html)
# ==============================================================================
V1_REFERENZEN_BODY = f"""
  <section class="hero-section" data-section="hero-referenzen">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">TRAININGS-EINBLICKE, PLATZ BIRMENSTORF &amp; QUALITÄT</div>
        <h1 class="hero-title">
          Echte Lernmomente aus <span>Platz und Alltag.</span>
        </h1>
        <p class="hero-lead">
          Ein Hund lernt ortsbezogen. Darum verbinden wir die Ruhe unseres eingezäunten Übungsplatzes in 5413 Birmenstorf gezielt mit realen Alltagssituationen im Wald, im Quartier und im Gelände zwischen Baden und Lenzburg.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>Schnupperlektion anfragen</span>
            {SVG_ARROW}
          </a>
          <a href="https://g.page/r/CYlfntsgxqtfEBM/review" target="_blank" rel="noopener" class="btn-cta btn-cta-outline-light">
            <span>Google-Bewertungen ansehen</span>
          </a>
        </div>
        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">5413 Birmenstorf</span>
            <span class="hero-badge-lbl">Geschütztes, eingezäuntes Trainingsgelände</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">@goodfordogs.ch</span>
            <span class="hero-badge-lbl">Aktuelle Einblicke auf Instagram &amp; Facebook</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/kurs-schnueffelspass-zos-01.jpg" alt="Konzentrierte Zielobjektsuche beim Schnüffelspass in Birmenstorf" style="object-position:center 45%;">
        <div class="hero-media-caption">
          <div>
            <div style="font-size:0.74rem;font-weight:700;text-transform:uppercase;color:var(--gold-dark);">Konzentration &amp; Freude</div>
            <div style="font-size:0.88rem;font-weight:700;color:var(--text-main);">Nasenarbeit &amp; Alltagstraining ohne Leistungsdruck</div>
          </div>
          <a href="https://www.instagram.com/goodfordogs.ch/" target="_blank" rel="noopener" class="btn-cta btn-cta-outline btn-sm">
            <span>@goodfordogs.ch</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <section data-section="praxis-einblicke">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">6 PRAXIS-SCHWERPUNKTE IM ÜBERBLICK</div>
        <h2 class="section-title">Einblicke in unsere Gruppen- und Einzeltrainings</h2>
        <p class="section-desc">
          Vom ersten Abruf im Welpenalter über ruhiges Warten im Familienalltag bis zur präzisen Geruchsdifferenzierung:
        </p>
      </div>

      {render_references_grid(limit=6, is_v2=False)}
    </div>
  </section>

{render_acp_bridge_sections(is_v2=False)}
"""


# ==============================================================================
# SEITEN-INHALTE: V1 ÜBER MICH (ueber-uns.html)
# ==============================================================================
V1_UEBER_UNS_BODY = f"""
  <section class="hero-section" data-section="hero-ueber-uns">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light">ÜBER MARTINA SIDLER (GOOD) · INHABERIN GOOD FOR DOGS</div>
        <h1 class="hero-title">
          Fachwissen, Geduld und <span>echtes Verständnis.</span>
        </h1>
        <p class="hero-lead">
          Hunde begleiten und faszinieren mich seit vielen Jahren. Als zertifizierte <strong>Certodog® Hundeinstruktorin</strong>, ausgebildete FBA-Tierbetreuerin und -Züchterin ist es mein Ziel, Halterinnen und Haltern das Lesen ihres Hundes verständlich, fair und mit einer Prise Humor näherzubringen.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html" class="btn-cta btn-cta-gold">
            <span>Persönlich kennenlernen</span>
            {SVG_ARROW}
          </a>
          <a href="#weiterbildungen" class="btn-cta btn-cta-outline-light">
            <span>Aus- &amp; Weiterbildungen</span>
          </a>
        </div>
        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">6 Fach-Zertifikate</span>
            <span class="hero-badge-lbl">Certodog® Instruktorin, Zuchtwartin &amp; FBA</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Studium 2026</span>
            <span class="hero-badge-lbl">Praktische Psychologie (Laudius Akademie)</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/team-martina-sidler-portrait.jpg" alt="Martina Sidler unterwegs in der Natur mit ihrem Hund" style="object-position:38% 25%;">
        <div class="hero-media-caption">
          <div>
            <div style="font-size:0.74rem;font-weight:700;text-transform:uppercase;color:var(--gold-dark);">Martina Sidler (Good)</div>
            <div style="font-size:0.88rem;font-weight:700;color:var(--text-main);">Region 5406 Baden (Rütihof) &amp; 5413 Birmenstorf</div>
          </div>
          <a href="tel:+41764545406" class="btn-cta btn-cta-outline btn-sm">
            <span>076 454 54 06</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- GRUND-AUSBILDUNGEN & QUALITÄTS-MITGLIEDSCHAFTEN -->
  <section data-section="qualifikationen">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">GEPRÜFTE GRUNDLAGEN · CERTODOG® &amp; FBA</div>
        <h2 class="section-title">Fundierte kynologische und psychologische Ausbildung</h2>
        <p class="section-desc">
          Weil gutes Training sowohl den Hund als auch den Menschen abholt, verbinde ich anerkannte Schweizer Kynologie-Abschlüsse mit laufender Weiterbildung in praktischer Psychologie:
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Hundetraining</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 class="card-title-1">Certodog® Instruktorin</h3>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Zertifizierte Certodog® Hundeinstruktorin (HIK)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Moderne Lerntheorie, Trainingsaufbau &amp; Methodik</span></div>
              <div class="check-item">{SVG_CHECK} <span>Körpersprache, Ausdrucksverhalten &amp; Gruppenleitung</span></div>
            </div>
          </div>
          <a href="leistungen.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Zum Kursangebot</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Betreuung &amp; Zucht</span>
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 class="card-title-1">FBA &amp; Zuchtwartin</h3>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>FBA-Tierbetreuerin, FBA-Züchterin &amp; FBA-Tiertransport</span></div>
              <div class="check-item">{SVG_CHECK} <span>Certodog® Zuchtwartin sowie Dogsitterin / Dogwalkerin</span></div>
              <div class="check-item">{SVG_CHECK} <span>Tiefes Wissen von der Welpenstube bis zum Seniorhund</span></div>
            </div>
          </div>
          <a href="leistungen.html#welpen" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Welpen-Gruppe ansehen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Mensch &amp; Ethik</span>
              <span class="icon-box">{SVG_SHIELD}</span>
            </div>
            <h3 class="card-title-1">Psychologie &amp; Ethik</h3>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>2026: Lehrgang Praktische Psychologie (Laudius)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Mitglied «Fairplay mit Hund»</span></div>
              <div class="check-item">{SVG_CHECK} <span>Mitglied «Initiative für gewaltfreies Hundetraining»</span></div>
            </div>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Beratung anfragen</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- CHRONOLOGISCHE FACHWEITERBILDUNGEN 2020 - 2026 -->
  <section id="weiterbildungen" data-section="weiterbildungen" style="background-color:var(--bg-soft);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">KONTINUIERLICHE FORTBILDUNG · 2020 BIS 2026</div>
        <h2 class="section-title">Auszug aus besuchten Fachseminaren und Lehrgängen</h2>
        <p class="section-desc">
          Regelmässiger Fachaustausch bei führenden Tierärztinnen, Verhaltensbiologinnen und Spezialistinnen im deutschsprachigen Raum:
        </p>
      </div>

      <div class="grid-2">
        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Schwerpunkt Verhalten &amp; Medizin</span>
              <span class="icon-box">{SVG_BOOK}</span>
            </div>
            <h3 class="card-title-1">Verhaltensmedizin, Angst &amp; Begegnungen</h3>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>med. vet. Celina del Amo &amp; Dr. Annika Bremhorst:</strong> Ausdrucksverhalten, Emotionen &amp; Verhaltensanalyse</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Karin Jüngling:</strong> Constructive Aggression Training (C.A.T.) &amp; Begegnungstraining</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Dr. Barbara Schöning &amp; Dr. med. vet. Christina Sigrist:</strong> Aggressionsverhalten &amp; Verhaltensmedizin</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Gerd Schreiber &amp; Sonja Meiburg:</strong> Leinenführigkeit, Aufmerksamkeit &amp; soziale Prozesse</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Stiftung Tier im Recht &amp; Prof. Dr. Iris Reichler:</strong> Hunderecht Schweiz, Kastration &amp; Fortpflanzungsmedizin</span></div>
            </div>
          </div>
          <a href="leistungen.html#einzeltraining" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Einzelberatung bei Verhaltensthemen</span>
            {SVG_ARROW}
          </a>
        </div>

        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Schwerpunkt Nase, Körper &amp; Alltag</span>
              <span class="icon-box">{SVG_SEARCH}</span>
            </div>
            <h3 class="card-title-1">Mantrailing, ZOS, Physiotherapie &amp; Dummy</h3>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span><strong>Dr. Esther Schalke:</strong> Mantrailing Module 1 bis 3 sowie Geruchsdifferenzierung</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Susan Schulze &amp; Maya Bachmann:</strong> Zielobjektsuche (ZOS) &amp; strukturierte Nasenarbeit</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Tina Schnatz:</strong> Faire Dummyarbeit &amp; Apportieren für Familienhunde</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Dr. Sabine Mai &amp; Dr. Michaela Artwohl:</strong> Bewegungsapparat, Physiotherapie &amp; gesunde Auslastung</span></div>
              <div class="check-item">{SVG_CHECK} <span><strong>Qualitätssiegel:</strong> Aktives Mitglied bei «Fairplay mit Hund» &amp; «Initiative für gewaltfreies Hundetraining»</span></div>
            </div>
          </div>
          <a href="leistungen.html#schnueffelspass" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Schnüffelspass entdecken</span>
            {SVG_ARROW}
          </a>
        </div>
      </div>
    </div>
  </section>
"""


# ==============================================================================
# SEITEN-INHALTE: V2 ZEIGEVERSION STARTSEITE (preview-die-schule-v2/index.html)
# ==============================================================================
V2_INDEX_BODY = f"""
  <!-- HERO SECTION (ZEIGEVERSION) -->
  <section class="hero-section" data-section="hero">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light" data-slot="hero_kicker">HUNDESCHULE IN BADEN, 5413 BIRMENSTORF &amp; REGION LENZBURG</div>
        <h1 class="hero-title" data-slot="hero_title">
          Die Schule für Halter <span>(und Hund).</span>
        </h1>
        <p class="hero-lead" data-slot="hero_lead">
          Bei <strong>Good for Dogs</strong> begleitet Martina Sidler Sie und Ihren Hund fair, gewaltfrei und alltagsnah: vom behutsamen Welpenstart über Junghunde- und Familienhundekurse bis zum individuellen Einzeltraining und konzentrierten Schnüffelspass.
        </p>
        <div class="hero-quote-box">
          «Ein gut erzogener Hund klaut dir kein Essen, er macht dir solange ein schlechtes Gewissen, bis du freiwillig teilst.»
        </div>
        <div class="hero-actions">
          <a href="#projektberater" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
            <span>Passenden Kurs finden</span>
            {SVG_ARROW}
          </a>
          <a href="kontakt.html" class="btn-cta btn-cta-outline-light" data-slot="hero_cta_secondary">
            <span>3-Schritte-Anmeldung testen</span>
          </a>
        </div>
        <div class="hero-badges">
          <div class="hero-badge-card">
            <span class="hero-badge-val">Certodog® &amp; FBA</span>
            <span class="hero-badge-lbl">Geprüfte Hundeinstruktorin Martina Sidler</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Max. 3 bis 6 Teams</span>
            <span class="hero-badge-lbl">Kleine Gruppen für individuelle Betreuung</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Fair &amp; Gewaltfrei</span>
            <span class="hero-badge-lbl">Mitglied Fairplay mit Hund &amp; IGH</span>
          </div>
          <div class="hero-badge-card">
            <span class="hero-badge-val">Birmenstorf &amp; Baden</span>
            <span class="hero-badge-lbl">Eingezäunter Platz &amp; echtes Alltagsgelände</span>
          </div>
        </div>
      </div>

      <div class="hero-media-card">
        <img src="images/hero-mensch-hund-alltag.jpg" alt="Martina Sidler beim Hundetraining mit aufmerksamem Hund im Freien" width="880" height="586" data-slot="hero_image">
        <div class="hero-media-caption">
          <div>
            <div style="font-family:var(--font-sans);font-size:0.74rem;font-weight:700;text-transform:uppercase;color:var(--gold-dark);">Training auf Augenhöhe · Kanton Aargau</div>
            <div style="font-size:0.88rem;font-weight:700;color:var(--text-main);">Übungsplatz 5413 Birmenstorf &amp; Gelände Baden–Lenzburg</div>
          </div>
          <a href="#angebot" class="btn-cta btn-cta-outline btn-sm">
            <span>Alle 6 Kurse</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- 3 KERN-SÄULEN -->
  <section data-section="zielgruppen" id="zielgruppen">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="pillars_kicker">WARUM DIE SCHULE FÜR HALTER (UND HUND)?</div>
        <h2 class="section-title" data-slot="pillars_title">Verständliche Körpersprache, faire Führung und echte Freude</h2>
        <p class="section-desc" data-slot="pillars_desc">
          Ob frisch eingezogener Welpe, stürmischer Junghund oder ein konkretes Alltagsthema: Wir trainieren in ruhigen Kleingruppen ohne Überforderung, damit Lernen auf beiden Seiten der Leine Spass macht.
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Säule 1 · Junge Hunde</span>
              <span class="icon-box">{SVG_HEART}</span>
            </div>
            <h3 class="card-title-1">Welpen &amp; Junghunde</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Vom sicheren Bindungsaufbau ab der 8. Woche bis zu den aufbauenden Erziehungskursen 1 und 2 am Samstagvormittag.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Dosierte Umweltreize &amp; bewusste Ruhephasen</span></div>
              <div class="check-item">{SVG_CHECK} <span>Lockere Leine, Rückruf &amp; Impulskontrolle</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Welpen-Gruppe &amp; Junghunde-Erziehungskurse 1 &amp; 2', 'Welpen Montag 18:00 Uhr (max. 5 Teams) · Erziehungskurs 1 &amp; 2 Samstag 09:00 &amp; 10:15 Uhr', 'Martina Sidler')">
            <span>Welpen &amp; Junghunde ansehen</span>
            {SVG_ARROW}
          </button>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Säule 2 · Alltag &amp; Nase</span>
              <span class="icon-box">{SVG_SEARCH}</span>
            </div>
            <h3 class="card-title-1">Familienhunde &amp; Nase</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Sinnvolle geistige und körperliche Auslastung für Hunde ab 16 Wochen in der Familienhunde-Gruppe oder beim Schnüffelspass.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Zielobjektsuche, Geruch &amp; Mantrailing (max. 3 Teams)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Einstieg jederzeit möglich · 10er-Abo verfügbar</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Familienhunde-Gruppe &amp; Schnüffelspass in Birmenstorf', 'Familienhunde Montag 16:30 Uhr · Schnüffelspass jeden 2. Samstag 10:30 Uhr (eingezäunt)', 'Martina Sidler')">
            <span>Gruppenstunden ansehen</span>
            {SVG_ARROW}
          </button>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Säule 3 · Individuell</span>
              <span class="icon-box">{SVG_HOME}</span>
            </div>
            <h3 class="card-title-1">1:1 Einzeltraining</h3>
            <p style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
              Persönliche Verhaltensberatung direkt bei Ihnen zu Hause und auf Ihren gewohnten Spazierwegen im Raum Baden und Aargau.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Hilfe bei Leinenstress, Unsicherheit, Angst &amp; Bellen</span></div>
              <div class="check-item">{SVG_CHECK} <span>CHF 80.— pro 60 Min. (zzgl. CHF 1.— / km Anfahrt)</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Individuelles 1:1 Einzeltraining &amp; Verhaltensberatung', 'CHF 80.— / 60 Min. (Anfahrt CHF 1.— / km) · Direkt bei Ihnen zu Hause &amp; im Alltag', 'Martina Sidler')">
            <span>Einzeltraining entdecken</span>
            {SVG_ARROW}
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- ALLE 6 KURSE & PREISE -->
  <section data-section="kernangebote" id="angebot" style="background-color:#FFFFFF;border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="services_kicker">ALLE 6 ANGEBOTE AUF EINEN BLICK · TRANSPARENTE TARIFE</div>
        <h2 class="section-title" data-slot="services_title">Unsere Kurse, Wochentage und Preise</h2>
        <p class="section-desc" data-slot="services_desc">
          Kleine Gruppen garantieren, dass jedes Mensch-Hund-Team individuell begleitet wird. Bequeme Zahlung per Überweisung oder direkt vor Ort via TWINT:
        </p>
      </div>

      {render_courses_grid(is_v2=True)}
    </div>
  </section>

{render_kurs_finder()}

  <!-- TRAININGS-EINBLICKE -->
  <section data-section="referenzen-auszug" id="einblicke">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="refs_kicker">PRAXIS-EINBLICKE · 5413 BIRMENSTORF &amp; GELÄNDE BADEN–LENZBURG</div>
        <h2 class="section-title" data-slot="refs_title">So trainieren wir bei Good for Dogs</h2>
        <p class="section-desc" data-slot="refs_desc">
          Kombination aus geschütztem, eingezäuntem Übungsplatz in Birmenstorf und abwechslungsreichen Trainingsorten im Alltag zwischen Baden und Lenzburg:
        </p>
      </div>

      {render_references_grid(limit=6, is_v2=True)}
    </div>
  </section>

{render_acp_bridge_sections(is_v2=True)}

  <!-- V2 AUSBLICK AUF DIE 3 WEITEREN UNTERSEITEN -->
  <section class="preview-scope-section" id="weitere-themenbereiche" data-section="vorschau-umfang">
    <div class="container">
      <div class="preview-scope-banner">
        <div class="section-kicker">UNVERBINDLICHER VORSCHAU-ENTWURF · 2 BEISPIEL-SEITEN AUSGEARBEITET</div>
        <h2 style="font-size:clamp(1.5rem,2.4vw,2.05rem);font-weight:700;margin-bottom:10px;">
          Ausblick: Diese 3 weiteren Detailseiten folgen beim gemeinsamen Ausbau
        </h2>
        <p style="font-size:0.94rem;color:var(--text-body);line-height:1.62;">
          In dieser <strong>Zeigeversion</strong> sind Ihre neue <strong>Startseite</strong> (inklusive interaktivem Kurs-Finder) sowie die <strong>Kontaktseite mit dem 3-Schritte Smart-Anmelde-Assistenten</strong> bereits vollständig ausgearbeitet und live testbar. Beim gemeinsamen Ausbau schalten wir zusätzlich die folgenden drei vertieften Unterseiten mit allen Originaltexten und Bildern frei:
        </p>
      </div>

      <div class="grid-3">
        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Folgt beim Ausbau · Seite 1</span>
              <span class="icon-box">{SVG_CALENDAR}</span>
            </div>
            <h3 class="card-title-1">Angebot &amp; Wochenplan</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Vertiefte Darstellung aller sechs Trainingsangebote und Konditionen:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Einzeltraining (CHF 80.—), Welpen &amp; Familienhunde (Montag)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Erziehungskurs 1 &amp; 2 sowie Schnüffelspass (Samstag)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Mitbring-Checkliste, Abo-Regelung &amp; TWINT-Zahlung</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Angebot &amp; Wochenplan im Detail', 'Alle 6 Kurse, 10er-Abos, Mitbring-Checkliste &amp; Trainingsbedingungen', 'Martina Sidler')">
            <span>Vorschau zu Angebot öffnen</span>
            {SVG_ARROW}
          </button>
        </div>

        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Folgt beim Ausbau · Seite 2</span>
              <span class="icon-box">{SVG_CAMERA}</span>
            </div>
            <h3 class="card-title-1">Einblicke &amp; Übungsplatz</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Authentische Trainingsmomente und geprüfte Qualitätsversprechen:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Eingezäunter Übungsplatz in 5413 Birmenstorf im Porträt</span></div>
              <div class="check-item">{SVG_CHECK} <span>Alltagsorte im Gelände zwischen Baden und Lenzburg</span></div>
              <div class="check-item">{SVG_CHECK} <span>Siegel «Fairplay mit Hund» &amp; «Gewaltfreies Hundetraining»</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Einblicke, Übungsplatz Birmenstorf &amp; Qualitätssiegel', 'Fotogalerie, @goodfordogs.ch Einblicke &amp; Google-Bewertungen', 'Martina Sidler')">
            <span>Vorschau zu Einblicken öffnen</span>
            {SVG_ARROW}
          </button>
        </div>

        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Folgt beim Ausbau · Seite 3</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 class="card-title-1">Über Martina Sidler</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:12px;">
              Persönliches Porträt und lückenloser Ausbildungs-Nachweis:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK} <span>Certodog® Hundeinstruktorin, Zuchtwartin &amp; 3x FBA</span></div>
              <div class="check-item">{SVG_CHECK} <span>Lehrgang Praktische Psychologie (2026)</span></div>
              <div class="check-item">{SVG_CHECK} <span>Chronologie aller 18+ Fachweiterbildungen (2020–2026)</span></div>
            </div>
          </div>
          <button type="button" class="btn-cta btn-cta-primary btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Über Martina Sidler &amp; Ausbildungen', 'Certodog®, FBA, Psychologie &amp; Fachseminare 2020–2026', 'Martina Sidler')">
            <span>Vorschau zu Über mich öffnen</span>
            {SVG_ARROW}
          </button>
        </div>
      </div>
    </div>
  </section>
"""


# ==============================================================================
# SEITEN-INHALTE: KONTAKT & 3-SCHRITTE SMART-KURSANMELDUNG (kontakt.html)
# ==============================================================================
def build_kontakt_body(client_slug: str, source_page: str) -> str:
    return f"""
  <section data-section="kontakt-zentrale" style="padding: 54px 0 80px;">
    <div class="container">
      <div class="contact-layout">
        <!-- LEFT COLUMN: DIREKTKONTAKT BADEN & BIRMENSTORF -->
        <div class="contact-info-panel">
          <div>
            <div class="section-kicker" data-slot="contact_kicker">KONTAKT &amp; KURSANMELDUNG · BADEN &amp; 5413 BIRMENSTORF</div>
            <h1 style="font-size:clamp(1.65rem,2.4vw,2.1rem);font-weight:700;margin-bottom:12px;" data-slot="contact_title">
              Ihr direkter Draht zu Martina Sidler.
            </h1>
            <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:18px;" data-slot="contact_lead">
              Ob Anmeldung für die Welpen-, Junghunde-, Familienhunde- oder Schnüffelspass-Gruppe oder Terminwunsch fürs 1:1-Einzeltraining: Nutzen Sie rechts die 3-Schritte Smart-Anmeldung oder melden Sie sich direkt telefonisch.
            </p>

            <img src="images/team-martina-sidler-portrait.jpg" alt="Martina Sidler, Hundeschule Good for Dogs in Baden und Birmenstorf" style="width:100%;height:195px;object-fit:cover;object-position:38% 25%;border-radius:var(--radius-sm);margin-bottom:16px;" loading="lazy" decoding="async">

            <div class="contact-direct-list">
              <div class="contact-direct-item">
                <div class="contact-direct-role">Inhaberin &amp; Kursleitung</div>
                <div class="contact-direct-person">Good for Dogs · Martina Sidler (Certodog®)</div>
                <div class="contact-direct-links">Telefon &amp; WhatsApp: 076 454 54 06 · E-Mail: info@goodfordogs.ch</div>
              </div>

              <div class="contact-direct-item">
                <div class="contact-direct-role">Trainingsorte &amp; Einzugsgebiet</div>
                <div class="contact-direct-person">Übungsplatz CH-5413 Birmenstorf &amp; Region 5406 Baden</div>
                <div class="contact-direct-links">Eingezäuntes Gelände in Birmenstorf sowie Alltagsorte zwischen Baden &amp; Lenzburg</div>
              </div>

              <div class="contact-direct-item">
                <div class="contact-direct-role">Feste Gruppen-Wochenzeiten</div>
                <div class="contact-direct-person">Mo 16:30 (Familienhunde) · Mo 18:00 (Welpen)</div>
                <div class="contact-direct-links">Sa 09:00 &amp; 10:15 (Erziehungskurs 1 &amp; 2) · Jeden 2. Sa 10:30 (Schnüffelspass)</div>
              </div>

              <div class="contact-direct-item">
                <div class="contact-direct-role">Zahlung &amp; Qualitätssiegel</div>
                <div class="contact-direct-person">Bequem per TWINT oder Überweisung</div>
                <div class="contact-direct-links">Mitglied Fairplay mit Hund &amp; Initiative für gewaltfreies Hundetraining</div>
              </div>
            </div>
          </div>
        </div>

        <!-- RIGHT COLUMN: GEFÜHRTER 3-SCHRITTE SMART-ANMELDE-ASSISTENT -->
        <div class="wizard-card">
          <div>
            <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:14px;">
              <div>
                <div class="section-kicker" style="margin-bottom:4px;">3-SCHRITTE SMART-KURSANMELDUNG · GOODFORDOGS.CH</div>
                <h2 style="font-size:1.32rem;font-weight:700;" id="wpWizardTitle">1. Welchen Kurs oder Termin wünschen Sie?</h2>
              </div>
              <span class="meta-badge" id="wpActiveAssigneeBadge">Kursleitung: Martina Sidler</span>
            </div>

            <div class="wp-stepper" aria-label="Fortschritt">
              <div class="wp-step-pill active" id="wpStepPill1">
                <span class="wp-step-num">1</span>
                <span>Kurs wählen</span>
              </div>
              <div class="wp-step-pill" id="wpStepPill2">
                <span class="wp-step-num">2</span>
                <span>Angaben zum Hund</span>
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

              <!-- SCHRITT 1: KURSBEREICH -->
              <div class="wp-step-pane active" id="wpStep1">
                <div class="wp-role-grid" id="wpTopicGrid">
                  <button type="button" class="wp-role-tile selected" data-topic="Einzeltraining & Verhaltensberatung (CHF 80.— / 60 Min.)" onclick="wpSelectIsTopic('Einzeltraining & Verhaltensberatung (CHF 80.— / 60 Min.)')">
                    <div class="wp-role-head">
                      <span class="wp-role-icon">{SVG_HOME}</span>
                      <span class="wp-role-title" data-slot="topic_opt_1">1. Einzeltraining</span>
                    </div>
                    <span class="wp-role-desc">1:1 im Wohnumfeld &amp; Alltag · Leine, Begegnungen, Angst, Rückruf (CHF 80.— / Std.)</span>
                  </button>

                  <button type="button" class="wp-role-tile" data-topic="Welpen-Gruppe (Montag 18:00 Uhr · ab 8 Wochen)" onclick="wpSelectIsTopic('Welpen-Gruppe (Montag 18:00 Uhr · ab 8 Wochen)')">
                    <div class="wp-role-head">
                      <span class="wp-role-icon">{SVG_HEART}</span>
                      <span class="wp-role-title" data-slot="topic_opt_2">2. Welpen-Gruppe</span>
                    </div>
                    <span class="wp-role-desc">Montag 18:00 Uhr · Max. 5 Teams · Einstieg jederzeit (CHF 35.— / 10er CHF 300.—)</span>
                  </button>

                  <button type="button" class="wp-role-tile" data-topic="Erziehungskurs 1 & 2 / Familienhunde-Gruppe" onclick="wpSelectIsTopic('Erziehungskurs 1 & 2 / Familienhunde-Gruppe')">
                    <div class="wp-role-head">
                      <span class="wp-role-icon">{SVG_USERS}</span>
                      <span class="wp-role-title" data-slot="topic_opt_3">3. Junghunde &amp; Familie</span>
                    </div>
                    <span class="wp-role-desc">Erziehungskurs 1 &amp; 2 (Sa 09:00 / 10:15) oder Familienhunde (Mo 16:30 Uhr)</span>
                  </button>

                  <button type="button" class="wp-role-tile" data-topic="Schnüffelspass-Gruppe (Jeden 2. Samstag 10:30 Uhr)" onclick="wpSelectIsTopic('Schnüffelspass-Gruppe (Jeden 2. Samstag 10:30 Uhr)')">
                    <div class="wp-role-head">
                      <span class="wp-role-icon">{SVG_SEARCH}</span>
                      <span class="wp-role-title" data-slot="topic_opt_4">4. Schnüffelspass</span>
                    </div>
                    <span class="wp-role-desc">Jeden 2. Sa 10:30 Uhr in 5413 Birmenstorf · Max. 3 Teams · ZOS &amp; Mantrailing</span>
                  </button>
                </div>

                <button type="button" class="btn-cta btn-cta-primary" style="width:100%;" onclick="wpNextStep(2)">
                  <span>Weiter zu Schritt 2: Angaben zum Hund</span>
                  {SVG_ARROW}
                </button>
              </div>

              <!-- SCHRITT 2: HUND & THEMA (INKL. ANMELDE-FELDER VON GOODFORDOGS.CH) -->
              <div class="wp-step-pane" id="wpStep2">
                <div class="form-grid-2" style="margin-bottom:14px;">
                  <div class="form-field">
                    <label for="wpDetail1" class="form-label" id="wpDetail1Label">Rufname, Rasse/Mix &amp; Geburtsdatum Ihres Hundes</label>
                    <input type="text" id="wpDetail1" class="form-input" placeholder="z. B. Balu, Labrador-Mix, geb. 14.05.2026">
                  </div>
                  <div class="form-field">
                    <label for="wpDetail2" class="form-label" id="wpDetail2Label">Geschlecht &amp; Kastrationsstatus</label>
                    <input type="text" id="wpDetail2" class="form-input" placeholder="z. B. Rüde intakt / Hündin kastriert">
                  </div>
                </div>

                <div class="form-field" style="margin-bottom:14px;">
                  <label class="form-label">Gewünschter Einstieg / Tarif-Wunsch</label>
                  <div class="wp-role-grid" id="wpUrgencyGrid" style="margin-bottom:0;">
                    <button type="button" class="wp-role-tile selected" data-urg="Zeitnah starten (Nächster freier Termin / Schnupperstunde)" onclick="wpSelectIsUrgency('Zeitnah starten (Nächster freier Termin / Schnupperstunde)')">
                      <span class="wp-role-title">1. Zeitnah einsteigen</span>
                      <span class="wp-role-desc">Nächstmögliche Gruppenstunde oder zeitnaher 1:1-Termin</span>
                    </button>
                    <button type="button" class="wp-role-tile" data-urg="Vormerkung für nächsten Kursstart / Unverbindliche Frage" onclick="wpSelectIsUrgency('Vormerkung für nächsten Kursstart / Unverbindliche Frage')">
                      <span class="wp-role-title">2. Kursstart vormerken / Frage</span>
                      <span class="wp-role-desc">Platz für kommenden Kursblock sichern oder vorab telefonisch klären</span>
                    </button>
                  </div>
                </div>

                <div class="form-field" style="margin-bottom:14px;">
                  <label for="contactMessage" class="form-label">Was ist Ihnen im Training besonders wichtig? (optional)</label>
                  <textarea id="contactMessage" class="form-textarea" placeholder="Erzählen Sie kurz von Ihrem Hund oder Ihrem Wunschthema (z. B. Welpenstart, Leinenführigkeit, Hundebegegnungen, Rückruf oder Nasenarbeit)..."></textarea>
                </div>

                <div class="form-field" style="margin-bottom:18px;">
                  <label class="form-label">Optional: Foto Ihres Hundes beifügen (max. 3 Bilder)</label>
                  <div class="wp-upload-zone" onclick="document.getElementById('wpPhotoInput').click()">
                    <div style="font-weight:700;font-size:0.86rem;color:var(--charcoal-deep);margin-bottom:2px;">Hier tippen, um bis zu 3 Hundefotos auszuwählen (JPG/PNG)</div>
                    <div style="font-size:0.78rem;color:var(--text-muted);">Erscheint direkt im 1-Seiten-Anmeldedossier für Martina Sidler</div>
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
                    <input type="text" id="contactName" class="form-input" placeholder="z. B. Sandra Meier" required>
                  </div>
                  <div class="form-field">
                    <label for="contactCompany" class="form-label">Rufname Ihres Hundes (optional)</label>
                    <input type="text" id="contactCompany" class="form-input" placeholder="z. B. Balu">
                  </div>
                </div>

                <div class="form-grid-2" style="margin-bottom:14px;">
                  <div class="form-field">
                    <label for="contactStreet" class="form-label">Strasse &amp; Nr. (für Anfahrt / Kursliste)</label>
                    <input type="text" id="contactStreet" class="form-input" placeholder="z. B. Dorfstrasse 18">
                  </div>
                  <div class="form-field">
                    <label for="contactPlz" class="form-label">PLZ &amp; Wohnort *</label>
                    <input type="text" id="contactPlz" class="form-input" placeholder="z. B. 5406 Baden-Rütihof" required>
                  </div>
                </div>

                <div class="form-grid-2" style="margin-bottom:14px;">
                  <div class="form-field">
                    <label for="contactPhone" class="form-label">Mobile / Telefon (für Rückruf / WhatsApp) *</label>
                    <input type="tel" id="contactPhone" class="form-input" placeholder="z. B. 079 123 45 67" required>
                  </div>
                  <div class="form-field">
                    <label for="contactEmail" class="form-label">E-Mail-Adresse *</label>
                    <input type="email" id="contactEmail" class="form-input" placeholder="ihre.adresse@beispiel.ch" required>
                  </div>
                </div>

                <div style="font-size:0.78rem;color:var(--text-muted);margin-bottom:14px;background-color:var(--bg-page);padding:10px 12px;border-radius:var(--radius-sm);border:1px solid var(--border-light);">
                  Mit dem Absenden bestätigen Sie, dass Ihr Hund altersgemäss geimpft und haftpflichtversichert ist (<button type="button" onclick="wpOpenImpressumModal()" style="background:none;border:none;color:var(--gold-dark);font-weight:700;cursor:pointer;text-decoration:underline;font-family:inherit;font-size:inherit;">AGB &amp; Datenschutz einsehen</button>).
                </div>

                <div id="wpFormError" style="display:none;background-color:#FEF2F2;border:1px solid #FECACA;color:#991B1B;padding:10px 12px;border-radius:var(--radius-sm);font-size:0.84rem;font-weight:600;margin-bottom:14px;"></div>

                <div class="wizard-nav-row">
                  <button type="button" class="btn-cta btn-cta-outline btn-sm" onclick="wpNextStep(2)">
                    <span>Zurück zu Schritt 2</span>
                  </button>
                  <button type="submit" class="btn-cta btn-cta-gold" id="wpSubmitBtn">
                    <span id="wpSubmitBtnText">Anmeldung &amp; 1-Seiten-Dossier senden</span>
                    {SVG_ARROW}
                  </button>
                </div>
              </div>
            </form>

            <!-- SUCCESS DOSSIER BOX -->
            <div class="wp-success-box" id="wpSuccessBox" role="status" aria-live="polite">
              <div class="section-kicker" style="color:var(--green);margin-bottom:4px;">ANMELDUNG &amp; ANFRAGE AUFBEREITET</div>
              <h3 style="font-size:1.28rem;font-weight:700;margin-bottom:6px;">Vielen Dank! Ihr 1-Seiten-Trainingsdossier für Good for Dogs steht bereit.</h3>
              <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:10px;">
                Ihre Angaben wurden übersichtlich für <strong>Martina Sidler</strong> zusammengestellt:
              </p>
              <div style="background-color:#FFFFFF;border:1px solid var(--border-light);border-radius:var(--radius-sm);padding:12px 14px;font-size:0.84rem;margin-bottom:12px;display:grid;gap:6px;">
                <div><strong>Referenz-Nummer:</strong> <span id="wpResRef">#WP-2026</span></div>
                <div><strong>Kursleitung:</strong> <span id="wpResAssigned">Martina Sidler (Good for Dogs)</span></div>
                <div><strong>Rückmeldung:</strong> <span id="wpResCallback">Persönlich per Telefon, WhatsApp oder E-Mail</span></div>
                <div><strong>Zustell-Kanäle:</strong> <span id="wpResChannels">1-Seiten-PDF-Dossier + E-Mail + WhatsApp</span></div>
              </div>
              <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:10px;">
                <a href="kontakt.html" id="wpResPdfBtn" target="_blank" rel="noopener" class="btn-cta btn-cta-primary btn-sm">
                  <span>1-Seiten-PDF-Dossier öffnen</span>
                  {SVG_ARROW}
                </a>
                <button type="button" class="btn-cta btn-cta-outline btn-sm" onclick="wpResetWizard()">
                  <span>Weitere Anfrage erfassen</span>
                </button>
              </div>
              <div style="font-size:0.78rem;color:var(--text-muted);background-color:var(--bg-soft);padding:10px 12px;border-radius:var(--radius-sm);white-space:pre-line;" id="wpResWaPreview"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <script>
    var wpIsState = {{
      step: 1,
      topic: 'Einzeltraining & Verhaltensberatung (CHF 80.— / 60 Min.)',
      urgency: 'Zeitnah starten (Nächster freier Termin / Schnupperstunde)',
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
      if (topic.indexOf('Welpen') !== -1) {{
        if (l1) l1.textContent = 'Rufname, Rasse & Wurfdatum Ihres Welpen';
        if (i1) i1.placeholder = 'z. B. Nala, Golden Retriever, 10 Wochen alt';
        if (l2) l2.textContent = 'Geschlecht & gewünschtes Startdatum (Montag 18:00 Uhr)';
        if (i2) i2.placeholder = 'z. B. Hündin, Einstieg ab nächstem Montag';
      }} else if (topic.indexOf('Erziehungskurs') !== -1) {{
        if (l1) l1.textContent = 'Rufname, Rasse/Mix & Alter Ihres Hundes';
        if (i1) i1.placeholder = 'z. B. Milo, Australian Shepherd, 8 Monate';
        if (l2) l2.textContent = 'Gewünschte Gruppe (Erziehungskurs 1/2 Sa oder Familienhunde Mo 16:30)';
        if (i2) i2.placeholder = 'z. B. Erziehungskurs 1 (Sa 09:00) oder Familienhunde (Mo 16:30)';
      }} else if (topic.indexOf('Schnüffelspass') !== -1) {{
        if (l1) l1.textContent = 'Rufname, Rasse & Alter Ihres Hundes (ab 6 Monaten)';
        if (i1) i1.placeholder = 'z. B. Kira, Mischling, 3 Jahre · liebt Suchspiele';
        if (l2) l2.textContent = 'Geschlecht (intakt/kastriert) & Vorkenntnisse Nasenarbeit';
        if (i2) i2.placeholder = 'z. B. Hündin kastriert · Einsteigerin ohne Vorkenntnisse';
      }} else {{
        if (l1) l1.textContent = 'Rufname, Rasse/Mix & Geburtsdatum Ihres Hundes';
        if (i1) i1.placeholder = 'z. B. Balu, Labrador-Mix, 2 Jahre';
        if (l2) l2.textContent = 'Geschlecht (intakt/kastriert) & gewünschter Trainingsort';
        if (i2) i2.placeholder = 'z. B. Rüde intakt · Hausbesuch Region Baden';
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
        1: '1. Welchen Kurs oder Termin wünschen Sie?',
        2: '2. Erzählen Sie uns kurz von Ihrem Hund',
        3: '3. Wohin darf Martina Sidler sich melden?'
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
          errBox.textContent = 'Bitte füllen Sie Vor- und Nachname, PLZ/Wohnort, Telefonnummer und E-Mail-Adresse vollständig aus.';
          errBox.style.display = 'block';
        }}
        return false;
      }}

      var btn = document.getElementById('wpSubmitBtn');
      var btnTxt = document.getElementById('wpSubmitBtnText');
      if (btn) btn.disabled = true;
      if (btnTxt) btnTxt.textContent = '1-Seiten-Dossier wird erstellt...';

      var extra = {{
        'Gewünschter Kurs / Angebot': wpIsState.topic,
        'Hund (Rufname / Rasse / Alter)': d1 || company || 'Wird im Gespräch ergänzt',
        'Geschlecht / Gruppe / Ort': d2 || 'Übungsplatz Birmenstorf oder Region Baden',
        'Einstiegswunsch': wpIsState.urgency
      }};
      if (street) extra['Adresse'] = street + ', ' + loc;

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
        message: msg || ('Good for Dogs Kursanfrage zu ' + wpIsState.topic),
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
        if (btnTxt) btnTxt.textContent = 'Anmeldung & 1-Seiten-Dossier senden';
        if (!res || !res.ok) {{
          if (errBox) {{
            errBox.textContent = (res && res.error) ? res.error : 'Übermittlung fehlgeschlagen. Bitte versuchen Sie es erneut.';
            errBox.style.display = 'block';
          }}
          return;
        }}
        document.getElementById('isContactForm').style.display = 'none';
        document.getElementById('wpResRef').textContent = res.ref_code || '#WP-2026';
        document.getElementById('wpResAssigned').textContent = res.assigned_to || 'Martina Sidler (Good for Dogs)';
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
        if (btnTxt) btnTxt.textContent = 'Anmeldung & 1-Seiten-Dossier senden';
        if (errBox) {{
          errBox.textContent = 'Netzwerkfehler bei der Übermittlung. Bitte schreiben Sie direkt an info@goodfordogs.ch oder rufen Sie 076 454 54 06 an.';
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
          'einzeltraining': 'Einzeltraining & Verhaltensberatung (CHF 80.— / 60 Min.)',
          'welpen': 'Welpen-Gruppe (Montag 18:00 Uhr · ab 8 Wochen)',
          'junghunde': 'Erziehungskurs 1 & 2 / Familienhunde-Gruppe',
          'familienhunde': 'Erziehungskurs 1 & 2 / Familienhunde-Gruppe',
          'schnueffelspass': 'Schnüffelspass-Gruppe (Jeden 2. Samstag 10:30 Uhr)'
        }};
        if (t && map[t]) {{
          wpSelectIsTopic(map[t]);
        }}
      }} catch (err) {{}}
    }})();
  </script>
"""


# 3. Alle Seiten fuer Variante 1 (Vollversion) schreiben
v1_pages = [
    ("index.html", "Good for Dogs · Hundeschule Baden & Birmenstorf | Die Schule für Halter (und Hund)", "startseite", V1_INDEX_BODY),
    ("leistungen.html", "Kurse, Wochenplan & Preise | Welpen, Junghunde, Schnüffelspass & Einzeltraining – Good for Dogs", "leistungen", V1_LEISTUNGEN_BODY),
    ("referenzen.html", "Trainings-Einblicke & Übungsplatz 5413 Birmenstorf | Hundeschule Good for Dogs Baden", "referenzen", V1_REFERENZEN_BODY),
    ("ueber-uns.html", "Über Martina Sidler (Certodog®) & Ausbildungen | Hundeschule Good for Dogs Baden", "ueber-uns", V1_UEBER_UNS_BODY),
    ("kontakt.html", "Kontakt & 3-Schritte Kursanmeldung | Hundeschule Good for Dogs Baden & Birmenstorf", "kontakt", build_kontakt_body("die-schule-vv", "preview-die-schule/kontakt.html")),
]

for fname, title, nav_key, body in v1_pages:
    full_html = render_v1_shell(fname, title, nav_key, body)
    (V1_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V1] Wrote {fname} ({len(full_html)} bytes)")

# 4. Alle Seiten fuer Variante 2 (Zeigeversion / Vorschau-Entwurf) schreiben
v2_pages = [
    ("index.html", "Good for Dogs · Hundeschule Baden & Birmenstorf (Zeigeversion / Vorschau-Entwurf)", "startseite", V2_INDEX_BODY),
    ("kontakt.html", "Kontakt & 3-Schritte Kursanmeldung (Zeigeversion) | Good for Dogs Baden", "kontakt", build_kontakt_body("die-schule-v2", "preview-die-schule-v2/kontakt.html")),
]

for fname, title, nav_key, body in v2_pages:
    full_html = render_v2_shell(fname, title, nav_key, body)
    (V2_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V2] Wrote {fname} ({len(full_html)} bytes)")

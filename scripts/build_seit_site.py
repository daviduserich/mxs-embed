#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deterministischer Dual-Showcase Generator fuer Clean Equipe GmbH (5727 Oberkulm, Karolina Fabic)
Auftrag: job_seit_20261118_100951 (Partnerin: Jenny Ettle / JE-MI)
Quell-URL: https://clean-equipe.ch/

Erzeugt beide Versionen nach dem 3-Stufen «Source Visual DNA & Design-Sommelier»-Standard (#UI-16):
- Vollversion:  /home/brainuser/workspaces/mxs-embed/preview-seit
                Live-URL: https://vorschau.magnet-xs.ch/seit-vollversion/ (5 Seiten + Studio Cockpit v4.0 + Light)
- Zeigeversion: /home/brainuser/workspaces/mxs-embed/preview-seit-v2
                Live-URL: https://vorschau.magnet-xs.ch/seit-v2/ (Startseite + 3-Schritte-Kontakt + #wpBlueprintModal)

Regel-Konformitaet:
- UI-LAYOUT-RULES.md (Canary: UI-LAYOUT-2026-V1, #UI-01, #UI-02, #UI-10, #UI-13, #UI-14, #UI-16, #UI-22, #UI-23)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1, 0 Eszett, 0 Satz-Geviertstriche, 0 nackte Ziffer 1, 100 % Schweizer Hochdeutsch)
"""

import json
import shutil
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
V1_DIR = BASE_DIR / "preview-seit"
V2_DIR = BASE_DIR / "preview-seit-v2"
DNA_SRC = BASE_DIR / "visual-dna" / "seit" / "source_visual_dna.json"

V1_DIR.mkdir(parents=True, exist_ok=True)
V2_DIR.mkdir(parents=True, exist_ok=True)

if DNA_SRC.exists():
    shutil.copy2(DNA_SRC, V1_DIR / "source_visual_dna.json")
    shutil.copy2(DNA_SRC, V2_DIR / "source_visual_dna.json")

BEFORE_INVENTORY = {
    "source_url": "https://clean-equipe.ch/",
    "crawled_at": "2026-11-18",
    "company_name": "Clean Equipe GmbH",
    "legal_entity": "Clean Equipe GmbH",
    "uid": "CHE-115.334.918",
    "chid": "CH-400.4.032.386-7",
    "founded": "2010-01-08",
    "claim": "Seit über 20 Jahren professionell im Einsatz – Karolina Fabic bringt Glanz in Ihren Alltag.",
    "subline": "Zuverlässige Unterhaltsreinigung, Büroreinigung, Fenster- und Storenreinigung sowie Baureinigung in 5727 Oberkulm, im Wynental und in der gesamten Region Aarau–Lenzburg.",
    "address": {
        "street": "Kreuzbündtenstrasse 8",
        "zip": "5727",
        "city": "Oberkulm",
        "canton": "AG",
        "country": "Schweiz"
    },
    "contact": {
        "email": "info@clean-equipe.ch",
        "phone_primary": "+41 76 577 57 22",
        "phone_display": "076 577 57 22",
        "whatsapp": "+41765775722",
        "instagram": "https://www.instagram.com/cleanequipe/",
        "facebook": "https://www.facebook.com/profile.php?id=100063723174622",
        "hours": "Montag–Freitag: 08:00–17:00 Uhr | Samstag: 09:00–14:00 Uhr | Sonntag: geschlossen"
    },
    "team": [
        {
            "name": "Karolina Fabic",
            "role": "Inhaberin & Geschäftsleitung Clean Equipe GmbH",
            "phone": "076 577 57 22",
            "phone_href": "tel:+41765775722",
            "image": "images/karolina-fabic-portrait.jpg",
            "qualification": "Über 20 Jahre Berufserfahrung · Handelsregistereintrag seit 2010 (CHE-115.334.918)",
            "bio": "Karolina Fabic führt die Clean Equipe GmbH in Oberkulm mit persönlichem Engagement, hoher Sorgfalt und echter Verlässlichkeit. Seit über 20 Jahren sorgt sie gemeinsam mit ihrem eingespielten Team für gepflegte Privathaushalte, saubere Geschäftsräume und bezugsbereite Neubauten im Wynental und im Raum Aarau."
        }
    ],
    "reviews": [
        {
            "author": "Anita Biehler",
            "source": "Verifizierte Google-Bewertung",
            "rating": "5.0 / 5.0",
            "text": "Sehr zuverlässiges und professionelles Putzinstitut! Die Reinigung wird äusserst gründlich, genau und trotzdem speditiv erledigt. Man merkt sofort, dass hier mit viel Sorgfalt und Engagement gearbeitet wird. Ich bin sehr zufrieden mit der Leistung und kann das Putzinstitut mit bestem Gewissen weiterempfehlen. Vielen Dank für die tolle Arbeit!"
        },
        {
            "author": "Nadja Kyburz",
            "source": "Verifizierte Google-Bewertung",
            "rating": "5.0 / 5.0",
            "text": "Absolut zuverlässig, sehr sauber, sehr loyal! Sehr zu empfehlen!"
        }
    ]
}

(V1_DIR / "before.json").write_text(json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False), encoding="utf-8")
(V2_DIR / "before.json").write_text(json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False), encoding="utf-8")

for target_dir, slug_val, pub_slug, is_v2 in [
    (V1_DIR, "preview-seit", "seit-vollversion", False),
    (V2_DIR, "preview-seit-v2", "seit-v2", True),
]:
    (target_dir / "company.json").write_text(json.dumps({
        "company_name": "Clean Equipe GmbH" + (" (Zeigeversion / Vorschau-Entwurf)" if is_v2 else " · Oberkulm"),
        "slug": slug_val,
        "public_slug": pub_slug,
        "cockpit_token": "seit2026",
        "city": "Oberkulm",
        "canton": "AG",
        "postal_code": "5727",
        "street_address": "Kreuzbündtenstrasse 8",
        "phone": "+41 76 577 57 22",
        "email": "info@clean-equipe.ch",
        "uid": "CHE-115.334.918",
        "source_url": "https://clean-equipe.ch/",
        "partner_id": "jenny"
    }, indent=2, ensure_ascii=False), encoding="utf-8")

v1_config = {
    "company_name": "Clean Equipe GmbH · Gebäudereinigung & Unterhaltsreinigung Oberkulm",
    "slug": "preview-seit",
    "public_slug": "seit-vollversion",
    "cockpit_token": "seit2026",
    "template": "swiss-architectural-craft-v1",
    "partner_id": "jenny",
    "pages": ["index.html", "leistungen.html", "referenzen.html", "ueber-uns.html", "kontakt.html"]
}
(V1_DIR / "config.json").write_text(json.dumps(v1_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V1_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-seit",
    "public_slug": "seit-vollversion",
    "token": "seit2026",
    "name": "Clean Equipe GmbH · Oberkulm (Vollversion)",
    "Updated": "2026-11-18",
    "PagesCount": 5,
    "ReferencesCount": 6,
    "TeamCount": 1
}, indent=2, ensure_ascii=False), encoding="utf-8")

v2_config = dict(v1_config)
v2_config.update({
    "company_name": "Clean Equipe GmbH · Oberkulm (Zeigeversion / Vorschau-Entwurf)",
    "slug": "preview-seit-v2",
    "public_slug": "seit-v2",
    "cockpit_token": "seit2026",
    "template": "swiss-architectural-craft-preview-v2",
    "pages": ["index.html", "kontakt.html"]
})
(V2_DIR / "config.json").write_text(json.dumps(v2_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V2_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-seit-v2",
    "public_slug": "seit-v2",
    "token": "seit2026",
    "name": "Clean Equipe GmbH · Oberkulm (Zeigeversion / Vorschau-Entwurf)",
    "Updated": "2026-11-18",
    "PagesCount": 2,
    "ReferencesCount": 6,
    "TeamCount": 1
}, indent=2, ensure_ascii=False), encoding="utf-8")

print("Wrote before.json, company.json, config.json, site.json for V1 and V2.")

# === LUCIDE VECTOR SVGS (0 UNICODE EMOJIS, #UI-01 & S-11) ===
SVG_CHECK = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>'
SVG_ARROW = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'
SVG_PHONE = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
SVG_MAIL = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>'
SVG_PIN = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>'
SVG_CLOCK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'
SVG_HOME = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.0" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'
SVG_BUILDING = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.0" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M8 10h.01"/><path d="M16 10h.01"/><path d="M8 14h.01"/><path d="M16 14h.01"/></svg>'
SVG_SPARKLES = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.0" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3Z"/></svg>'
SVG_HARDHAT = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.0" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 18a1 1 0 0 0 1 1h18a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v2z"/><path d="M10 10V5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v5"/><path d="M4 15v-3a6 6 0 0 1 6-6"/><path d="M14 6a6 6 0 0 1 6 6v3"/></svg>'
SVG_SHIELD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.0" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>'
SVG_BOOK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.0" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>'
SVG_AWARD = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.0" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/></svg>'
SVG_CHAT = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>'
SVG_STAR = '<svg width="15" height="15" viewBox="0 0 24 24" fill="#EAB308" stroke="#CA8A04" stroke-width="1.5" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'
SVG_5STARS = f'<span style="display:inline-flex;align-items:center;gap:2px;" aria-label="5.0 von 5.0 Sternen">{SVG_STAR}{SVG_STAR}{SVG_STAR}{SVG_STAR}{SVG_STAR}</span>'
SVG_CHEVRON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>'
SVG_CLOSE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'
SVG_CAMERA = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.0" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/></svg>'
SVG_INSTA = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.0" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>'

SHARED_CSS = """
    :root {
      /* === 1. Polaritaet & Schweizer Raster (#UI-02, #UI-16, Sensor S-27) === */
      --wp-expected-hero-polarity: "dark";
      --wp-archetype: "swiss_architectural_craft";
      --container-max: 1100px;
      --radius-card: 8px;
      --radius-md: 8px;
      --radius-badge: 4px;
      --radius-sm: 4px;

      /* === 2. Typografie (swiss_architectural_craft) === */
      --font-display: 'Lexend', 'Plus Jakarta Sans', sans-serif;
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;

      /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=229.2deg) === */
      --bg-page: #F5FBFE;
      --bg-page-oklch: oklch(0.985 0.008 229.2);
      --bg-soft: #E6F2F9;
      --bg-soft-oklch: oklch(0.955 0.016 229.2);
      --bg-elevated: #FFFFFF;
      --bg-card: #FFFFFF;
      --border-subtle: #D2DDE2;
      --border-subtle-oklch: oklch(0.890 0.014 229.2);
      --border-light: #D2DDE2;
      --border-strong: #AFC3CE;
      --text-main: #09181F;
      --text-main-oklch: oklch(0.200 0.025 229.2);
      --text-body: #1E333E;
      --text-muted: #424F56;
      --text-muted-oklch: oklch(0.420 0.020 229.2);
      --stage-dark: #071923;
      --stage-mid: #0C2B3B;

      /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
      --primary: #0086B0;
      --primary-brand-raw: #52BCE9;
      --primary-oklch: oklch(0.580 0.160 229.2);
      --primary-hover: #006D90;
      --primary-text: #006687;
      --primary-border: #A8D4E6;

      /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung) === */
      --accent-palette-1-soft: #E2F5DF;
      --accent-palette-1-strong: #2E6E20;
      --accent-palette-2-soft: #EFECFF;
      --accent-palette-2-strong: #624C9F;
      --accent-palette-3-soft: #FBE7FC;
      --accent-palette-3-strong: #813F85;
      --accent-palette-4-soft: #FFE7EF;
      --accent-palette-4-strong: #94385E;

      --shadow-sm: 0 2px 10px rgba(9, 24, 31, 0.05);
      --shadow-md: 0 12px 28px rgba(9, 24, 31, 0.08);
      --shadow-lg: 0 18px 40px rgba(9, 24, 31, 0.14);
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    ::selection {
      background-color: rgba(0, 134, 176, 0.20);
      color: #09181F;
    }

    html {
      scroll-behavior: smooth;
      font-size: 16px;
      overflow-x: clip;
    }

    body {
      font-family: var(--font-sans);
      color: var(--text-main);
      background-color: var(--bg-page);
      line-height: 1.62;
      overflow-x: clip;
      -webkit-font-smoothing: antialiased;
      font-variant-numeric: tabular-nums;
      caret-color: var(--primary);
    }

    img {
      max-width: 100%;
      height: auto;
      display: block;
    }

    a {
      color: inherit;
      text-decoration: none;
      text-underline-offset: 3px;
      transition: color 0.18s ease, background-color 0.18s ease, border-color 0.18s ease, transform 0.18s ease;
    }

    a:focus-visible,
    button:focus-visible,
    input:focus-visible,
    textarea:focus-visible,
    summary:focus-visible {
      outline: 2px solid var(--primary);
      outline-offset: 2px;
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

    /* Freistehende Marken-Kicker (#UI-01: Lexend Bold, 0 JetBrains Mono, 0 //, 0 ::before) */
    .section-kicker {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-display);
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--primary-text);
      background: transparent !important;
      border: none !important;
      padding: 0 !important;
      box-shadow: none !important;
      margin-bottom: 12px;
    }
    .section-kicker.kicker-on-dark {
      color: #7DD3FC;
    }

    h1, h2, h3, h4 {
      font-family: var(--font-display);
      color: var(--text-main);
      line-height: 1.22;
      letter-spacing: -0.015em;
    }

    .section-head {
      max-width: 760px;
      margin-bottom: 40px;
    }
    .section-title {
      font-size: clamp(1.75rem, 2.9vw, 2.38rem);
      font-weight: 700;
      margin-bottom: 14px;
    }
    .section-desc {
      font-size: 1.01rem;
      color: var(--text-body);
      line-height: 1.65;
    }

    section {
      padding: 76px 0;
      position: relative;
    }

    /* Top Info Bar (V1) */
    .top-bar {
      background-color: #05131B;
      color: #D7E8F0;
      font-size: 0.78rem;
      padding: 8px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.10);
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
      background-color: rgba(78, 172, 58, 0.22);
      color: #9AE68B;
      border: 1px solid rgba(154, 230, 139, 0.35);
      font-family: var(--font-display);
      font-size: 0.69rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      padding: 3px 8px;
      border-radius: var(--radius-badge);
    }
    .top-bar-links {
      display: flex;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }
    .top-bar-links a {
      color: #F0F9FF;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-height: 32px;
      padding: 4px 6px;
    }
    .top-bar-links a:hover {
      color: #7DD3FC;
    }

    /* Sticky Dark Slate-Petrol Header (#UI-16 Original Logo Contrast & #UI-02 1-Line Nav S-22) */
    .site-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background-color: #081E29;
      border-bottom: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 4px 16px rgba(5, 19, 27, 0.22);
    }
    .header-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 18px;
      min-height: 76px;
      padding: 10px 0;
    }
    .brand-link {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
      min-height: 44px;
      padding: 2px 0;
    }
    .brand-logo-wide {
      height: 42px;
      width: auto;
      max-width: 205px;
      object-fit: contain;
      flex-shrink: 0;
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
      color: #E2F1F8;
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
      color: #FFFFFF;
      background: transparent;
      border-bottom-color: #52BCE9;
    }
    .nav-link-preview {
      color: #B8D4E3;
      background: transparent;
      border: none;
      border-bottom: 2px dashed rgba(82, 188, 233, 0.55);
      font-size: 0.86rem;
    }
    .nav-link-preview:hover {
      color: #FFFFFF;
      background: transparent;
      border-bottom-color: #52BCE9;
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }

    /* Buttons (#UI-01: 8px radius, crisp contrast) */
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
      border-radius: var(--radius-card);
      border: 1px solid transparent;
      cursor: pointer;
      text-align: center;
      line-height: 1.25;
      transition: all 0.18s ease;
    }
    .btn-cta svg {
      flex-shrink: 0;
    }
    .btn-cta-primary {
      background-color: var(--primary);
      color: #FFFFFF;
      border-color: var(--primary);
    }
    .btn-cta-primary:hover {
      background-color: var(--primary-hover);
      color: #FFFFFF;
      border-color: var(--primary-hover);
      transform: translateY(-1px);
    }
    .btn-cta-green {
      background-color: var(--accent-palette-1-strong);
      color: #FFFFFF;
      border-color: var(--accent-palette-1-strong);
    }
    .btn-cta-green:hover {
      background-color: #235718;
      color: #FFFFFF;
      border-color: #235718;
      transform: translateY(-1px);
    }
    .btn-cta-outline {
      background-color: #FFFFFF;
      color: var(--text-main);
      border-color: var(--border-strong);
    }
    .btn-cta-outline:hover {
      border-color: var(--primary);
      color: var(--primary-text);
      background-color: var(--bg-soft);
    }
    .btn-cta-ghost-dark {
      background-color: rgba(255, 255, 255, 0.10);
      color: #FFFFFF;
      border-color: rgba(255, 255, 255, 0.30);
    }
    .btn-cta-ghost-dark:hover {
      background-color: rgba(255, 255, 255, 0.18);
      color: #FFFFFF;
      border-color: #7DD3FC;
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
      border-radius: var(--radius-card);
      border: 1px solid rgba(255, 255, 255, 0.28);
      background-color: rgba(255, 255, 255, 0.08);
      color: #FFFFFF;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }
    .mobile-drawer {
      display: none;
      background-color: #081E29;
      border-bottom: 2px solid var(--primary);
      padding: 14px 24px 20px;
      flex-direction: column;
      gap: 6px;
    }
    .mobile-drawer.open {
      display: flex;
    }
    .mobile-drawer a,
    .mobile-nav-btn {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      width: 100%;
      padding: 12px 10px;
      min-height: 44px;
      color: #F0F9FF;
      font-family: var(--font-sans);
      font-size: 0.94rem;
      font-weight: 600;
      border: none;
      border-bottom: 1px solid rgba(255, 255, 255, 0.10);
      background: transparent;
      text-align: left;
      cursor: pointer;
    }

    /* Dark Slate-Petrol Hero Stage (#UI-16 Evolution Dark Polarity S-27 & #UI-02 Baseline Lock S-23) */
    .hero-section {
      background: linear-gradient(135deg, #071923 0%, #0B2736 56%, #0F3A4F 100%);
      background-color: #091F2C;
      color: #FFFFFF;
      padding: 68px 0 76px;
      border-bottom: 4px solid var(--primary);
      overflow: hidden;
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1.12fr 0.88fr;
      gap: 44px;
      align-items: stretch;
    }
    .hero-col-left {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .hero-title {
      font-size: clamp(2.05rem, 3.5vw, 3.02rem);
      font-weight: 700;
      color: #FFFFFF;
      line-height: 1.14;
      margin-bottom: 18px;
    }
    .hero-title span {
      color: #74E35E;
    }
    .hero-lead {
      font-size: 1.03rem;
      color: #DCEBF2;
      line-height: 1.65;
      margin-bottom: 26px;
    }
    .hero-actions {
      display: flex;
      flex-wrap: nowrap;
      gap: 12px;
      align-items: center;
      margin-bottom: 28px;
    }
    .hero-actions .btn-cta {
      padding: 12px 18px;
      font-size: 0.88rem;
      white-space: nowrap;
    }
    .hero-badges {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-top: auto;
    }
    .hero-badge-card {
      background-color: rgba(255, 255, 255, 0.07);
      border: 1px solid rgba(255, 255, 255, 0.16);
      border-left: 3px solid #52BCE9;
      border-radius: var(--radius-badge);
      padding: 11px 14px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 2px;
    }
    .hero-badge-val {
      font-family: var(--font-display);
      font-size: 0.90rem;
      font-weight: 700;
      color: #FFFFFF;
    }
    .hero-badge-lbl {
      font-size: 0.77rem;
      color: #CFE3ED;
      line-height: 1.35;
    }

    .hero-media-card {
      background-color: #0D2D3E;
      border: 1px solid rgba(255, 255, 255, 0.20);
      border-radius: var(--radius-card);
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }
    .hero-media-card img {
      width: 100%;
      height: 310px;
      min-height: 270px;
      flex: 1 1 auto;
      object-fit: cover;
      object-position: center 20%;
    }
    .hero-media-caption {
      padding: 15px 18px;
      background-color: #071923;
      border-top: 1px solid rgba(255, 255, 255, 0.14);
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
    .split-grid {
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: 32px;
      align-items: stretch;
    }

    /* Cards */
    .content-card {
      background-color: var(--bg-card);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-card);
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
    .content-card.card-green-top {
      border-top: 4px solid var(--accent-palette-1-strong);
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
      font-size: 0.70rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      padding: 4px 9px;
      border-radius: var(--radius-badge);
      background-color: var(--bg-soft);
      color: var(--primary-text);
      border: 1px solid var(--primary-border);
      white-space: nowrap;
    }
    .meta-badge-green {
      background-color: var(--accent-palette-1-soft);
      color: var(--accent-palette-1-strong);
      border-color: #B7DFB0;
    }
    .icon-box {
      width: 38px;
      height: 38px;
      border-radius: var(--radius-badge);
      background-color: var(--bg-soft);
      color: var(--primary-text);
      border: 1px solid var(--primary-border);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    /* Synchronized card headings for S-31 internal horizontal alignment */
    .card-title-1 {
      font-size: 1.14rem;
      font-weight: 700;
      line-height: 1.26;
      margin-bottom: 8px;
    }

    .check-list {
      display: flex;
      flex-direction: column;
      gap: 9px;
      margin-top: 10px;
    }
    .check-item {
      display: flex;
      align-items: flex-start;
      gap: 9px;
      font-size: 0.90rem;
      color: var(--text-body);
      line-height: 1.48;
    }
    .check-item svg {
      color: var(--accent-palette-1-strong);
      flex-shrink: 0;
      margin-top: 3px;
    }

    /* Pillar Media Cards */
    .pillar-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-card);
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
      background-color: var(--bg-soft);
      position: relative;
    }
    .pillar-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 28%;
    }
    .pillar-body {
      padding: 22px 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex: 1;
      gap: 16px;
    }

    /* Interactive Reinigungs-Berater */
    .calc-option-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-bottom: 18px;
      align-items: stretch;
    }
    .calc-option-btn {
      background-color: var(--bg-page);
      border: 2px solid var(--border-strong);
      border-radius: var(--radius-badge);
      padding: 13px 14px;
      text-align: left;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      gap: 4px;
      font-family: inherit;
      min-height: 78px;
      transition: all 0.16s ease;
    }
    .calc-option-btn:hover {
      border-color: var(--primary);
      background-color: #FFFFFF;
    }
    .calc-option-btn.active {
      border: 2px solid var(--primary);
      background-color: var(--bg-soft);
    }
    .calc-opt-title {
      font-family: var(--font-display);
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-main);
    }
    .calc-opt-sub {
      font-size: 0.77rem;
      color: var(--text-body);
      line-height: 1.38;
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
      border-left: 3px solid var(--primary);
      border-radius: var(--radius-badge);
      padding: 12px 14px;
    }
    .calc-kpi-val {
      font-family: var(--font-display);
      font-size: 0.96rem;
      font-weight: 700;
      color: var(--primary-text);
    }
    .calc-kpi-lbl {
      font-size: 0.77rem;
      color: var(--text-body);
      margin-top: 2px;
    }

    /* FAQ Accordion (#UI-23: zero h1..h6 inside summary) */
    .faq-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .faq-item {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-card);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }
    .faq-item summary {
      list-style: none;
      cursor: pointer;
      padding: 18px 22px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      font-family: var(--font-display);
      font-size: 0.98rem;
      font-weight: 600;
      color: var(--text-main);
      min-height: 54px;
    }
    .faq-item summary::-webkit-details-marker {
      display: none;
    }
    .faq-item summary svg {
      flex-shrink: 0;
      color: var(--primary-text);
      transition: transform 0.2s ease;
    }
    .faq-item[open] summary svg {
      transform: rotate(180deg);
    }
    .faq-answer {
      padding: 0 22px 20px;
      font-size: 0.92rem;
      color: var(--text-body);
      line-height: 1.65;
      border-top: 1px solid var(--bg-soft);
      padding-top: 14px;
    }

    /* V2 Vorschau-Entwurf (Zeigeversion) */
    .preview-scope-section {
      background-color: var(--bg-soft);
      border-top: 2px dashed rgba(0, 134, 176, 0.38);
      border-bottom: 2px dashed rgba(0, 134, 176, 0.38);
      padding: 74px 0 84px;
    }
    .preview-scope-banner {
      background-color: #FFFFFF;
      color: var(--text-main);
      border: 2px dashed var(--primary);
      border-radius: var(--radius-card);
      padding: 26px 28px;
      margin-bottom: 34px;
      box-shadow: var(--shadow-md);
    }
    .preview-module-card {
      background-color: #FFFFFF;
      border: 2px dashed var(--primary);
      border-radius: var(--radius-card);
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
      background-color: var(--bg-soft);
      border: 1px solid var(--primary-border);
      color: var(--primary-text);
      font-family: var(--font-sans);
      font-size: 0.70rem;
      font-weight: 700;
      padding: 4px 9px;
      border-radius: var(--radius-badge);
      text-transform: uppercase;
      white-space: nowrap;
    }

    /* Dark Slate-Petrol Footer (#UI-16 Logo Brilliance) */
    .site-footer {
      background-color: #081E29;
      color: #E2F1F8;
      padding: 64px 0 34px;
      border-top: 4px solid var(--primary);
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 1.3fr 1fr 1fr 1.1fr;
      gap: 34px;
      padding-bottom: 40px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.14);
    }
    .footer-title {
      font-family: var(--font-display);
      font-size: 0.84rem;
      font-weight: 700;
      color: #FFFFFF;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 15px;
    }
    .footer-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .footer-list a,
    .footer-list button {
      color: #CFE3ED;
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
      color: #7DD3FC;
    }
    .footer-bottom {
      padding-top: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      font-size: 0.82rem;
      color: #B8D4E3;
    }
    .footer-bottom a,
    .footer-bottom button {
      display: inline-flex;
      align-items: center;
      min-height: 34px;
      padding: 4px 0;
      background: none;
      border: none;
      color: #CFE3ED;
      font-family: inherit;
      font-size: 0.82rem;
      cursor: pointer;
    }

    /* Modals (#wpBlueprintModal & #wpImpressumModal) */
    .wp-modal-backdrop {
      position: fixed;
      inset: 0;
      background-color: rgba(7, 25, 35, 0.76);
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
      border: 2px solid var(--primary);
      border-radius: var(--radius-card);
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
      border-radius: var(--radius-badge);
      border: 1px solid var(--border-strong);
      background-color: var(--bg-page);
      color: var(--text-main);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }
    .wp-modal-checklist {
      background-color: var(--bg-page);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-card);
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
      color: var(--accent-palette-1-strong);
      flex-shrink: 0;
      margin-top: 2px;
    }

    /* 3-Schritte Smart-Offerten-Assistent (kontakt.html) */
    .contact-layout {
      display: grid;
      grid-template-columns: 0.88fr 1.12fr;
      gap: 34px;
      align-items: stretch;
    }
    .contact-info-panel {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-card);
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
      border-left: 3px solid var(--primary);
      border-radius: var(--radius-badge);
      font-size: 0.85rem;
    }
    .contact-direct-role {
      font-family: var(--font-display);
      font-size: 0.71rem;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--primary-text);
      letter-spacing: 0.04em;
    }
    .contact-direct-person {
      font-weight: 700;
      color: var(--text-main);
      margin-top: 2px;
    }
    .contact-direct-person a {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-height: 34px;
      min-width: 44px;
      padding: 5px 0;
    }
    .contact-direct-links {
      color: var(--text-body);
      font-size: 0.83rem;
      margin-top: 2px;
    }

    .wizard-card {
      background-color: #FFFFFF;
      border: 2px solid var(--stage-dark);
      border-radius: var(--radius-card);
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
      background-color: var(--bg-soft);
      border-radius: var(--radius-card);
    }
    .wp-step-pill {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 10px 8px;
      border-radius: var(--radius-badge);
      font-family: var(--font-sans);
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--text-muted);
      text-align: center;
    }
    .wp-step-pill.active {
      background-color: var(--primary);
      color: #FFFFFF;
    }
    .wp-step-pill.done {
      background-color: var(--accent-palette-1-soft);
      color: var(--accent-palette-1-strong);
    }
    .wp-step-num {
      width: 22px;
      height: 22px;
      border-radius: var(--radius-badge);
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
      border-radius: var(--radius-card);
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
      border-color: var(--primary);
      background-color: #FFFFFF;
    }
    .wp-role-tile.selected {
      border: 2px solid var(--primary);
      background-color: var(--bg-soft);
    }
    .wp-role-head {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .wp-role-icon {
      width: 28px;
      height: 28px;
      border-radius: var(--radius-badge);
      background-color: #FFFFFF;
      color: var(--primary-text);
      border: 1px solid var(--primary-border);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .wp-role-title {
      font-family: var(--font-display);
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-main);
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
      font-size: 0.80rem;
      font-weight: 700;
      color: var(--text-main);
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
      border-radius: var(--radius-badge);
      padding: 11px 14px;
      min-height: 44px;
    }
    .form-input:focus,
    .form-textarea:focus {
      outline: none;
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(0, 134, 176, 0.16);
    }
    .form-textarea {
      min-height: 96px;
      resize: vertical;
    }

    .wp-upload-zone {
      border: 1px dashed var(--border-strong);
      background-color: var(--bg-page);
      border-radius: var(--radius-card);
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
      border-radius: var(--radius-badge);
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
      border: 2px solid var(--accent-palette-1-strong);
      border-radius: var(--radius-card);
    }
    .wp-success-box.visible {
      display: flex;
    }

    @media (max-width: 1020px) {
      .hero-grid,
      .split-grid,
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
      .brand-logo-wide {
        height: 36px;
        max-width: 175px;
      }
      .hero-media-card img {
        height: 250px;
      }
      .wizard-card,
      .content-card {
        padding: 20px;
      }
    }
"""


def render_services_pillar_cards(is_v2: bool = False) -> str:
    cta_unterhalt = (
        f'<a href="kontakt.html?thema=unterhalt" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Offerte für Unterhalt</span>{SVG_ARROW}</a>'
        if is_v2 else
        f'<a href="leistungen.html#unterhalt" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Unterhaltsreinigung ansehen</span>{SVG_ARROW}</a>'
    )
    cta_buero = (
        f'<a href="kontakt.html?thema=buero" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Offerte für Büroräume</span>{SVG_ARROW}</a>'
        if is_v2 else
        f'<a href="leistungen.html#buero" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Büroreinigung ansehen</span>{SVG_ARROW}</a>'
    )
    cta_bau = (
        f'<a href="kontakt.html?thema=baureinigung" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Offerte für Baureinigung</span>{SVG_ARROW}</a>'
        if is_v2 else
        f'<a href="leistungen.html#baureinigung" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Baureinigung ansehen</span>{SVG_ARROW}</a>'
    )
    return f"""
      <div class="grid-3">
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/objekt-detail-02.jpg" alt="Gründliche Bad- und Haushaltsreinigung durch Clean Equipe GmbH" style="object-position:center 45%;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Privathaushalt</span>
                <span class="icon-box">{SVG_HOME}</span>
              </div>
              <h3 class="card-title-1" data-slot="srv_1_title">Unterhaltsreinigung</h3>
              <p style="font-size:0.89rem;color:var(--text-body);">
                Regelmässige Pflege für Ihr Zuhause, wöchentlich, alle zwei Wochen oder genau nach Ihrem persönlichen Rhythmus.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK}<span>Haus- und Wohnungsreinigung</span></div>
                <div class="check-item">{SVG_CHECK}<span>Fenster- und Storenreinigung</span></div>
                <div class="check-item">{SVG_CHECK}<span>Treppenhäuser und Bügelservice</span></div>
              </div>
            </div>
            {cta_unterhalt}
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/reinigung-einsatz-02.jpg" alt="Karolina Fabic bei der Büroreinigung in der Region Oberkulm und Aarau" style="object-position:center 22%;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">KMU &amp; Praxis</span>
                <span class="icon-box">{SVG_BUILDING}</span>
              </div>
              <h3 class="card-title-1" data-slot="srv_2_title">Büroreinigung</h3>
              <p style="font-size:0.89rem;color:var(--text-body);">
                Saubere Arbeitswelten für konzentriertes Arbeiten und einen repräsentativen Empfang Ihrer Kundschaft.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK}<span>Arbeitsplätze und Empfang</span></div>
                <div class="check-item">{SVG_CHECK}<span>Sitzungszimmer und Böden</span></div>
                <div class="check-item">{SVG_CHECK}<span>Sanitäranlagen, Küchen und Pause</span></div>
              </div>
            </div>
            {cta_buero}
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/banner-reinigung-02.jpg" alt="Gründliche Bauendreinigung bei Neubau und Umbau im Kanton Aargau" style="object-position:44% center;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge meta-badge-green">Neubau &amp; Umbau</span>
                <span class="icon-box">{SVG_HARDHAT}</span>
              </div>
              <h3 class="card-title-1" data-slot="srv_3_title">Baureinigung</h3>
              <p style="font-size:0.89rem;color:var(--text-body);">
                Sorgfältige Grobreinigung und bezugsbereite Bauendreinigung auf den vereinbarten Übergabetermin hin.
              </p>
              <div class="check-list">
                <div class="check-item">{SVG_CHECK}<span>Neubauten und frisch sanierte Räume</span></div>
                <div class="check-item">{SVG_CHECK}<span>Umbauten und Renovationen</span></div>
                <div class="check-item">{SVG_CHECK}<span>Bezugsbereite Bauendreinigung</span></div>
              </div>
            </div>
            {cta_bau}
          </div>
        </div>
      </div>"""


def render_cleaning_advisor() -> str:
    return f"""
  <!-- INTERAKTIVER 15-SEKUNDEN REINIGUNGS- & INTERVALL-BERATER -->
  <section data-section="projektberater" id="projektberater" style="background-color:var(--bg-soft);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="calc_kicker">15-SEKUNDEN ORIENTIERUNG · WELCHER EINSATZ PASST ZU IHNEN?</div>
        <h2 class="section-title" data-slot="calc_title">Finden Sie in einem Klick den passenden Reinigungs-Rhythmus</h2>
        <p class="section-desc">
          Ob regelmässige Entlastung im Alltag, gepflegte Büroräume oder bezugsbereiter Neubau: Tippen Sie links auf Ihr Objekt für unsere direkte Empfehlung.
        </p>
      </div>

      <div class="split-grid">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Auswahl · Ihr Anliegen</span>
              <span class="icon-box">{SVG_HOME}</span>
            </div>
            <h3 class="card-title-1">Ihr Objekt &amp; Bereich</h3>
            <p style="font-size:0.90rem;color:var(--text-body);margin-bottom:18px;">
              Wählen Sie den gewünschten Schwerpunkt für Ihr Zuhause, Ihr Unternehmen oder Ihren Neubau:
            </p>

            <div class="calc-option-grid" id="ceAdvisorButtons">
              <button type="button" class="calc-option-btn active" data-adv="unterhalt" onclick="ceSelectAdvisor('unterhalt')">
                <span class="calc-opt-title">Haus &amp; Wohnung</span>
                <span class="calc-opt-sub">Wöchentlich, 14-täglich oder mit Bügelservice</span>
              </button>
              <button type="button" class="calc-option-btn" data-adv="buero" onclick="ceSelectAdvisor('buero')">
                <span class="calc-opt-title">Büro &amp; Gewerbe</span>
                <span class="calc-opt-sub">Arbeitsplätze, Sitzungszimmer &amp; Sanitär</span>
              </button>
              <button type="button" class="calc-option-btn" data-adv="fenster" onclick="ceSelectAdvisor('fenster')">
                <span class="calc-opt-title">Fenster &amp; Storen</span>
                <span class="calc-opt-sub">Streifenfreie Glasflächen, Rahmen &amp; Lamellen</span>
              </button>
              <button type="button" class="calc-option-btn" data-adv="baureinigung" onclick="ceSelectAdvisor('baureinigung')">
                <span class="calc-opt-title">Neubau &amp; Umbau</span>
                <span class="calc-opt-sub">Sorgfältige Baufein- und Bauendreinigung</span>
              </button>
            </div>
          </div>

          <div style="font-size:0.82rem;color:var(--text-muted);display:flex;align-items:center;gap:8px;">
            {SVG_SHIELD}
            <span>Persönliche Besichtigung und unverbindliche Offerte durch Karolina Fabic</span>
          </div>
        </div>

        <div class="content-card card-green-top" id="ceAdvisorResultCard">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge meta-badge-green" id="ceAdvBadge">Empfehlung · Privathaushalt</span>
              <span class="icon-box">{SVG_SPARKLES}</span>
            </div>
            <h3 class="card-title-1" id="ceAdvTitle">
              Unterhaltsreinigung nach Wunsch
            </h3>
            <p style="font-size:0.90rem;color:var(--text-body);margin-bottom:16px;" id="ceAdvDesc">
              Ideal für Familien, Berufstätige und Seniorinnen oder Senioren im Raum Oberkulm, Wynental und Aarau: Wir pflegen Wohnräume, Bäder, Küche, Treppenhaus und auf Wunsch auch Ihre Bügelwäsche zuverlässig zum festen Termin.
            </p>

            <div class="calc-kpi-grid">
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="ceAdvKpi1Val">Wöchentlich / 14-täglich</div>
                <div class="calc-kpi-lbl" id="ceAdvKpi1Lbl">Flexibel anpassbarer Rhythmus</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="ceAdvKpi2Val">Feste Vertrauensperson</div>
                <div class="calc-kpi-lbl" id="ceAdvKpi2Lbl">Sorgfältig, loyal und diskret</div>
              </div>
            </div>
          </div>

          <div style="display:flex;gap:10px;flex-wrap:wrap;">
            <a href="kontakt.html?thema=unterhalt" id="ceAdvCtaLink" class="btn-cta btn-cta-primary" style="flex:1 1 220px;">
              <span id="ceAdvCtaText">Unverbindliche Offerte anfragen</span>
              {SVG_ARROW}
            </a>
            <a href="tel:+41765775722" class="btn-cta btn-cta-outline" style="flex:0 0 auto;">
              {SVG_PHONE}
              <span>076 577 57 22</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>"""


def render_reviews_and_karolina_section(is_v2: bool = False) -> str:
    more_link = (
        f'<button type="button" class="btn-cta btn-cta-outline btn-sm" onclick="wpOpenBlueprintModal(\'Über Karolina Fabic &amp; 20 Jahre Clean Equipe\', \'Persönliches Porträt, Handelsregister-Fakten (CHE-115.334.918) &amp; Einsatzgebiet Wynental\', \'Karolina Fabic\')"><span>Mehr über Clean Equipe</span>{SVG_ARROW}</button>'
        if is_v2 else
        f'<a href="ueber-uns.html" class="btn-cta btn-cta-outline btn-sm"><span>Mehr über Karolina Fabic</span>{SVG_ARROW}</a>'
    )
    return f"""
  <!-- ÜBER KAROLINA FABIC & ECHTE GOOGLE-KUNDENSTIMMEN -->
  <section data-section="ueber-uns" id="ueber-uns" style="background-color:#FFFFFF;border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="split-grid">
        <div class="content-card card-accent-top">
          <div>
            <div class="section-kicker" data-slot="about_kicker">ÜBER UNS · WARUM CLEAN EQUIPE GMBH?</div>
            <h2 style="font-size:clamp(1.55rem,2.5vw,2.08rem);font-weight:700;margin-bottom:12px;" data-slot="about_title">
              Karolina Fabic bringt Glanz in Ihren Alltag
            </h2>
            <p style="font-size:0.94rem;color:var(--text-body);margin-bottom:16px;" data-slot="about_desc">
              Seit über 20 Jahren steht Clean Equipe in <strong>5727 Oberkulm</strong> und der Region Aargau für gründliche, ehrliche Reinigungsarbeit. Ob Privathaushalt, KMU-Büro oder Neubau: Sie haben eine direkte Ansprechpartnerin, die mitdenkt und jedes Objekt so pflegt, als wäre es das eigene.
            </p>
            <div class="check-list" style="margin-bottom:18px;">
              <div class="check-item">{SVG_CHECK}<span><strong>Jahrelange Erfahrung:</strong> Über 20 Jahre Praxis, seit 2010 als GmbH im Handelsregister (CHE-115.334.918).</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Zuverlässig &amp; loyal:</strong> Pünktliche Einsätze, sorgfältiger Umgang mit Materialien und gelebte Diskretion.</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Faire Preise &amp; flexible Termine:</strong> Transparente Offerten von Montag bis Samstag (auch Randzeiten).</span></div>
            </div>
          </div>
          <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;">
            {more_link}
            <a href="tel:+41765775722" class="btn-cta btn-cta-primary btn-sm">
              {SVG_PHONE}
              <span>Direkt anrufen: 076 577 57 22</span>
            </a>
          </div>
        </div>

        <div style="display:flex;flex-direction:column;justify-content:space-between;gap:18px;height:100%;">
          <div class="content-card card-green-top" style="padding:22px 24px;">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge meta-badge-green">Google-Bewertung · 5.0 / 5.0</span>
                {SVG_5STARS}
              </div>
              <p style="font-size:0.91rem;color:var(--text-main);font-style:italic;line-height:1.62;margin-bottom:12px;" data-slot="review_1_text">
                «Sehr zuverlässiges und professionelles Putzinstitut! Die Reinigung wird äusserst gründlich, genau und trotzdem speditiv erledigt. Man merkt sofort, dass hier mit viel Sorgfalt und Engagement gearbeitet wird. Ich bin sehr zufrieden mit der Leistung und kann das Putzinstitut mit bestem Gewissen weiterempfehlen. Vielen Dank für die tolle Arbeit!»
              </p>
            </div>
            <div style="font-size:0.83rem;font-weight:700;color:var(--primary-text);">
              Anita Biehler · Verifizierte Google-Rezension
            </div>
          </div>

          <div class="content-card" style="padding:22px 24px;">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge meta-badge-green">Google-Bewertung · 5.0 / 5.0</span>
                {SVG_5STARS}
              </div>
              <p style="font-size:0.93rem;color:var(--text-main);font-style:italic;line-height:1.62;margin-bottom:12px;" data-slot="review_2_text">
                «Absolut zuverlässig, sehr sauber, sehr loyal! Sehr zu empfehlen!»
              </p>
            </div>
            <div style="font-size:0.83rem;font-weight:700;color:var(--primary-text);">
              Nadja Kyburz · Verifizierte Google-Rezension
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>"""


def render_acp_bridge_sections(is_v2: bool = False) -> str:
    social_cta = (
        f'<button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal(\'Praxis-Einblicke @cleanequipe\', \'Echte Arbeitsmomente aus Oberkulm, dem Wynental und der Region Aarau\', \'Karolina Fabic\')"><span>Einblick ansehen</span>{SVG_ARROW}</button>'
        if is_v2 else
        f'<a href="referenzen.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Weitere Einblicke ansehen</span>{SVG_ARROW}</a>'
    )
    blog_cta = (
        f'<button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal(\'Pflege-Ratgeber &amp; Werterhalt\', \'Praxistipps aus über 20 Jahren Gebäudereinigung für Fenster, Storen und Böden\', \'Karolina Fabic\')"><span>Praxistipp lesen</span>{SVG_ARROW}</button>'
        if is_v2 else
        f'<a href="leistungen.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Passenden Service wählen</span>{SVG_ARROW}</a>'
    )
    return f"""
  <!-- ACP BRÜCKE 1: SOCIAL MEDIA & ECHTE EINBLICKE (@CLEANEQUIPE) -->
  <section data-section="social-media" id="social-media" style="background-color:var(--bg-page);border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="social_kicker">AKTUELLE EINBLICKE · @CLEANEQUIPE AUF INSTAGRAM &amp; FACEBOOK</div>
        <h2 class="section-title" data-slot="social_title">Direkt aus unserem Reinigungsalltag im Wynental und Aargau</h2>
        <p class="section-desc" data-slot="social_desc">
          Auf <strong>@cleanequipe</strong> zeigen wir echte Handgriffe aus Privathaushalten, Geschäftsräumen und Neubauten rund um Oberkulm, Reinach und Aarau.
        </p>
      </div>

      <div class="grid-3">
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/fensterreinigung-fachfrau.jpg" alt="Streifenfreie Fensterreinigung durch Karolina Fabic von Clean Equipe" style="object-position:center 20%;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Fenster &amp; Glas</span>
                <span style="font-size:0.75rem;font-weight:700;color:var(--primary-text);white-space:nowrap;">Oberkulm</span>
              </div>
              <h3 class="card-title-1">Klare Sicht ohne Streifen</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">
                Vom grossen Wohnzimmerfenster bis zu Rahmen, Falzen und Lamellenstoren sorgen wir im Frühling, Herbst und ganzjährig für klaren Durchblick.
              </p>
            </div>
            {social_cta}
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/header-raum-01.jpg" alt="Schonende Reinigungsmittel und saubere Mikrofasertücher im Einsatz" style="object-position:center 50%;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge meta-badge-green">Materialschutz</span>
                <span style="font-size:0.75rem;font-weight:700;color:var(--accent-palette-1-strong);white-space:nowrap;">Farbsystem</span>
              </div>
              <h3 class="card-title-1">Sorgfalt auf jeder Fläche</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">
                Mit abgestimmten Reinigungsmitteln und getrennten Mikrofasertüchern pflegen wir Naturstein, Parkett, Chromstahl und Sanitärkeramik werterhaltend.
              </p>
            </div>
            {social_cta}
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/banner-reinigung-03.jpg" alt="Gepflegte Büro- und Sitzungsräume nach der Reinigung durch Clean Equipe" style="object-position:center 50%;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row">
                <span class="meta-badge">Geschäftsräume</span>
                <span style="font-size:0.75rem;font-weight:700;color:var(--primary-text);white-space:nowrap;">Region Aarau</span>
              </div>
              <h3 class="card-title-1">Frische Büros am Morgen</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">
                Wenn Ihr Team am Morgen eintrifft, sind Schreibtische, Sitzungszimmer, Kaffeeküche und Sanitäranlagen bereits tadellos gepflegt.
              </p>
            </div>
            {social_cta}
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ACP BRÜCKE 2: PFLEGE-RATGEBER & ALLTAGSWISSEN -->
  <section data-section="blog" id="blog" style="background-color:var(--bg-soft);border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="blog_kicker">PFLEGE-RATGEBER &amp; PRAXISWISSEN · AUS ÜBER 20 JAHREN ERFAHRUNG</div>
        <h2 class="section-title" data-slot="blog_title">Drei Praxistipps für dauerhaft gepflegte Wohn- und Geschäftsräume</h2>
        <p class="section-desc" data-slot="blog_desc">
          Fachgerechte Reinigung schützt Oberflächen langfristig und spart bei Übergaben oder im Büroalltag wertvolle Zeit.
        </p>
      </div>

      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Ratgeber #1 · Fenster</span>
              <span class="icon-box">{SVG_BOOK}</span>
            </div>
            <h3 class="card-title-1">Storen vor dem Glas pflegen</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Wer Lamellenstoren und Fensterrahmen vor der Glasfläche von Blütenstaub und Feinstaub befreit, verhindert neue Schmutzläufer beim nächsten Sommerregen.
            </p>
          </div>
          {blog_cta}
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Ratgeber #2 · Büro</span>
              <span class="icon-box">{SVG_BUILDING}</span>
            </div>
            <h3 class="card-title-1">Kontaktflächen im Fokus</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Türgriffe, Lichtschalter, Kaffeemaschinen und Armaturen entscheiden im Büro über Hygiene und Wohlbefinden. Ein fester Wochenplan hält das Niveau konstant hoch.
            </p>
          </div>
          {blog_cta}
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Ratgeber #3 · Neubau</span>
              <span class="icon-box">{SVG_HARDHAT}</span>
            </div>
            <h3 class="card-title-1">Baustaub schonend lösen</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Feiner Zementschleier und Bohrstaub wirken wie Schleifpapier auf neuen Armaturen und Fenstern. Bei der Bauendreinigung arbeiten wir deshalb strikt mehrstufig.
            </p>
          </div>
          {blog_cta}
        </div>
      </div>
    </div>
  </section>"""


def render_faqs_section() -> str:
    return f"""
  <!-- HÄUFIG GESTELLTE FRAGEN (FAQs) -->
  <section data-section="faqs" id="faqs" style="background-color:var(--bg-page);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="faq_kicker">HÄUFIG GESTELLTE FRAGEN · KLARE ANTWORTEN</div>
        <h2 class="section-title" data-slot="faq_title">Wichtige Fragen rund um Ihre Reinigung</h2>
        <p class="section-desc" data-slot="faq_desc">
          Hier beantworten wir die wichtigsten Fragen von Privatpersonen, KMU und Verwaltungen aus Oberkulm und der Region.
        </p>
      </div>

      <div class="faq-list">
        <details class="faq-item" open>
          <summary>
            <span>Welche Reinigungsdienstleistungen bietet Clean Equipe an?</span>
            {SVG_CHEVRON}
          </summary>
          <div class="faq-answer">
            Clean Equipe bietet professionelle Reinigungsdienstleistungen für Privatpersonen und Unternehmen an. Unser Angebot umfasst Unterhaltsreinigungen (Haus, Wohnung, Treppenhäuser und Bügelservice), Büroreinigungen, Fenster- und Storenreinigungen sowie Baureinigungen für Neubauten und Umbauten. Mit über 20 Jahren Erfahrung sorgen wir zuverlässig für Sauberkeit und gepflegte Räumlichkeiten.
          </div>
        </details>

        <details class="faq-item">
          <summary>
            <span>Kann ich auch eine regelmässige Reinigung buchen?</span>
            {SVG_CHEVRON}
          </summary>
          <div class="faq-answer">
            Ja, selbstverständlich. Ob wöchentlich, alle zwei Wochen oder nach individuellem Bedarf: Wir passen unsere Reinigungsdienstleistungen flexibel an Ihre Wünsche an. Gemeinsam finden wir eine passende Lösung für Ihr Zuhause oder Ihre Geschäftsräume.
          </div>
        </details>

        <details class="faq-item">
          <summary>
            <span>Wie kann ich eine Reinigungsofferte anfordern?</span>
            {SVG_CHEVRON}
          </summary>
          <div class="faq-answer">
            Sie können uns direkt telefonisch oder per WhatsApp unter <strong>076 577 57 22</strong> erreichen, an <strong>info@clean-equipe.ch</strong> schreiben oder unseren geführten 3-Schritte-Offerten-Assistenten auf der Kontaktseite nutzen. Gerne besprechen wir Ihre Wünsche persönlich und erstellen Ihnen eine individuelle, unverbindliche Offerte.
          </div>
        </details>

        <details class="faq-item">
          <summary>
            <span>In welchen Gemeinden ist die Clean Equipe GmbH im Einsatz?</span>
            {SVG_CHEVRON}
          </summary>
          <div class="faq-answer">
            Von unserem Firmensitz an der Kreuzbündtenstrasse 8 in <strong>5727 Oberkulm</strong> aus betreuen wir Privat- und Geschäftskunden im gesamten Wynental (Unterkulm, Teufenthal, Dürrenäsch, Reinach AG, Menziken, Zetzwil) sowie im Raum Gränichen, Suhr, Aarau, Buchs und Lenzburg.
          </div>
        </details>

        <details class="faq-item">
          <summary>
            <span>Sind auch Einsätze am Samstag oder ausserhalb der Bürozeiten möglich?</span>
            {SVG_CHEVRON}
          </summary>
          <div class="faq-answer">
            Ja. Unsere regulären Einsatzzeiten sind Montag bis Freitag von 08:00 bis 17:00 Uhr sowie am Samstag von 09:00 bis 14:00 Uhr. Für Büro- und Praxisreinigungen vereinbaren wir gerne passende Randzeiten, damit Ihr Tagesgeschäft ungestört läuft.
          </div>
        </details>
      </div>
    </div>
  </section>"""


def render_impressum_modal() -> str:
    return f"""
  <!-- IMPRESSUM & DATENSCHUTZ MODAL (#wpImpressumModal) -->
  <div class="wp-modal-backdrop" id="wpImpressumModal" role="dialog" aria-modal="true" aria-labelledby="wpImpTitle" data-allow-scroll="true">
    <div class="wp-modal-dialog" data-allow-scroll="true">
      <button type="button" class="wp-modal-close" aria-label="Dialog schliessen" onclick="wpCloseImpressumModal()">
        {SVG_CLOSE}
      </button>
      <div class="section-kicker">RECHTLICHE ANGABEN · SCHWEIZER DATENSCHUTZ (CH-REVDSG)</div>
      <h2 id="wpImpTitle" style="font-size:1.45rem;font-weight:700;margin-bottom:14px;">Impressum &amp; Datenschutzerklärung</h2>

      <div class="wp-modal-checklist">
        <div>
          <strong style="display:block;color:var(--text-main);margin-bottom:4px;">Verantwortliche Stelle &amp; Firmensitz</strong>
          <div style="font-size:0.88rem;color:var(--text-body);line-height:1.6;">
            Clean Equipe GmbH · Karolina Fabic<br>
            Kreuzbündtenstrasse 8, 5727 Oberkulm, Schweiz<br>
            <span style="display:inline-flex;flex-wrap:wrap;gap:12px;margin-top:4px;">
              <a href="tel:+41765775722" style="color:var(--primary-text);font-weight:600;display:inline-flex;align-items:center;min-height:34px;padding:4px 0;">+41 76 577 57 22</a>
              <a href="mailto:info@clean-equipe.ch" style="color:var(--primary-text);font-weight:600;display:inline-flex;align-items:center;min-height:34px;padding:4px 0;">info@clean-equipe.ch</a>
            </span>
          </div>
        </div>
        <div style="border-top:1px solid var(--border-light);padding-top:10px;">
          <strong style="display:block;color:var(--text-main);margin-bottom:4px;">Handelsregister &amp; Unternehmens-Identifikation</strong>
          <div style="font-size:0.88rem;color:var(--text-body);line-height:1.6;">
            Rechtsform: Gesellschaft mit beschränkter Haftung (GmbH)<br>
            UID: <strong>CHE-115.334.918</strong> · Handelsregister-Nr.: <strong>CH-400.4.032.386-7</strong><br>
            Eingetragen im Handelsregister des Kantons Aargau seit 08.01.2010 · Branche: Reinigung von Gebäuden
          </div>
        </div>
        <div style="border-top:1px solid var(--border-light);padding-top:10px;">
          <strong style="display:block;color:var(--text-main);margin-bottom:4px;">Datenschutz nach Schweizer DSG (revDSG)</strong>
          <div style="font-size:0.85rem;color:var(--text-body);line-height:1.6;">
            Der Schutz Ihrer persönlichen Daten ist uns wichtig. Wir bearbeiten Personendaten (Name, Kontaktdaten, Objektangaben und optionale Fotos im Offerten-Assistenten) ausschliesslich zweckgebunden zur Offert- und Auftragsabwicklung im Einklang mit dem Schweizer Datenschutzgesetz (DSG). Diese Website verzichtet auf aufdringliche Werbe-Tracker und kommt ohne Cookie-Banner oder Google-reCAPTCHA-Rätsel aus. Auskunfts- oder Löschbegehren richten Sie jederzeit an info@clean-equipe.ch.
          </div>
        </div>
      </div>

      <div style="display:flex;justify-content:flex-end;">
        <button type="button" class="btn-cta btn-cta-primary btn-sm" onclick="wpCloseImpressumModal()">
          <span>Schliessen</span>
        </button>
      </div>
    </div>
  </div>"""


def render_global_js() -> str:
    return """
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
    function wpOpenBlueprintModal(title, subtitle, owner) {
      var m = document.getElementById('wpBlueprintModal');
      if (!m) return;
      var t = document.getElementById('wpBpTitle');
      var s = document.getElementById('wpBpSubtitle');
      var o = document.getElementById('wpBpOwner');
      if (t && title) t.textContent = title;
      if (s && subtitle) s.textContent = subtitle;
      if (o && owner) o.textContent = owner;
      m.classList.add('open');
    }
    function wpCloseBlueprintModal() {
      var m = document.getElementById('wpBlueprintModal');
      if (m) m.classList.remove('open');
    }
    document.addEventListener('keydown', function(ev) {
      if (ev.key === 'Escape') {
        wpCloseImpressumModal();
        wpCloseBlueprintModal();
      }
    });

    var CE_ADVISOR_DATA = {
      unterhalt: {
        badge: 'Empfehlung · Privathaushalt',
        title: 'Unterhaltsreinigung nach Wunsch',
        desc: 'Ideal für Familien, Berufstätige und Seniorinnen oder Senioren im Raum Oberkulm, Wynental und Aarau: Wir pflegen Wohnräume, Bäder, Küche, Treppenhaus und auf Wunsch auch Ihre Bügelwäsche zuverlässig zum festen Termin.',
        kpi1Val: 'Wöchentlich / 14-täglich',
        kpi1Lbl: 'Flexibel anpassbarer Rhythmus',
        kpi2Val: 'Feste Vertrauensperson',
        kpi2Lbl: 'Sorgfältig, loyal und diskret',
        ctaHref: 'kontakt.html?thema=unterhalt',
        ctaText: 'Offerte für Unterhalt'
      },
      buero: {
        badge: 'Empfehlung · KMU & Praxis',
        title: 'Büro- & Praxisreinigung',
        desc: 'Für Unternehmen im Wynental und Raum Aarau: Saubere Arbeitsplätze, hygienische Sanitäranlagen und einladende Empfangs- und Pausenräume, auf Wunsch auch früh morgens, abends oder am Samstag.',
        kpi1Val: 'Mo–Sa Randzeiten',
        kpi1Lbl: 'Ungestörter Betriebsablauf',
        kpi2Val: 'Klare Pauschale',
        kpi2Lbl: 'Nach Vor-Ort-Besichtigung',
        ctaHref: 'kontakt.html?thema=buero',
        ctaText: 'Offerte für Büroreinigung'
      },
      fenster: {
        badge: 'Empfehlung · Glas & Storen',
        title: 'Fenster-, Rahmen- & Storenpflege',
        desc: 'Gründliche Reinigung von Glasflächen, Fensterrahmen, Falzen, Simsen, Wintergärten und Lamellenstoren für Privathäuser, Wohnungen und Gewerbeobjekte.',
        kpi1Val: 'Inkl. Rahmen & Storen',
        kpi1Lbl: 'Werterhaltend und streifenfrei',
        kpi2Val: 'Einzeln oder im Abo',
        kpi2Lbl: 'Frühling, Herbst oder nach Bedarf',
        ctaHref: 'kontakt.html?thema=fenster',
        ctaText: 'Offerte für Fenster & Storen'
      },
      baureinigung: {
        badge: 'Empfehlung · Neubau & Umbau',
        title: 'Baufein- & Bauendreinigung',
        desc: 'Nach Neubau, Umbau oder Sanierung entfernen wir Baustaub, Farb- und Zementspuren schonend und übergeben sämtliche Räume, Fenster und Sanitäranlagen termingerecht bezugsbereit.',
        kpi1Val: 'Termingarantie',
        kpi1Lbl: 'Pünktlich zur Schlüsselübergabe',
        kpi2Val: 'Über 20 Jahre Praxis',
        kpi2Lbl: 'Schonend auf neuen Oberflächen',
        ctaHref: 'kontakt.html?thema=baureinigung',
        ctaText: 'Offerte für Baureinigung'
      }
    };

    function ceSelectAdvisor(key) {
      var d = CE_ADVISOR_DATA[key];
      if (!d) return;
      var btns = document.querySelectorAll('#ceAdvisorButtons .calc-option-btn');
      for (var i = 0; i < btns.length; i++) {
        btns[i].classList.toggle('active', btns[i].getAttribute('data-adv') === key);
      }
      var setTxt = function(id, val) { var el = document.getElementById(id); if (el) el.textContent = val; };
      setTxt('ceAdvBadge', d.badge);
      setTxt('ceAdvTitle', d.title);
      setTxt('ceAdvDesc', d.desc);
      setTxt('ceAdvKpi1Val', d.kpi1Val);
      setTxt('ceAdvKpi1Lbl', d.kpi1Lbl);
      setTxt('ceAdvKpi2Val', d.kpi2Val);
      setTxt('ceAdvKpi2Lbl', d.kpi2Lbl);
      setTxt('ceAdvCtaText', d.ctaText);
      var link = document.getElementById('ceAdvCtaLink');
      if (link) link.setAttribute('href', d.ctaHref);
    }
  </script>"""


def render_v1_shell(filename: str, page_title: str, active_nav: str, body_html: str, extra_js: str = "") -> str:
    nav_start = "active" if active_nav == "startseite" else ""
    nav_leistungen = "active" if active_nav == "leistungen" else ""
    nav_referenzen = "active" if active_nav == "referenzen" else ""
    nav_ueber = "active" if active_nav == "ueber-uns" else ""
    nav_kontakt = "active" if active_nav == "kontakt" else ""

    return f"""<!DOCTYPE html>
<html lang="de-CH" data-expected-hero-polarity="dark" data-design-mode="evolution">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-XSS-Protection" content="1; mode=block">
  <meta name="referrer" content="no-referrer">
  <title>{page_title}</title>
  <meta name="description" content="Clean Equipe GmbH in 5727 Oberkulm: Seit über 20 Jahren Ihr zuverlässiges Reinigungsunternehmen für Unterhaltsreinigung, Büroreinigung, Fenster &amp; Storen sowie Baureinigung im Wynental und Raum Aarau.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700;800&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "CleaningService",
    "name": "Clean Equipe GmbH",
    "url": "https://clean-equipe.ch/",
    "telephone": "+41 76 577 57 22",
    "email": "info@clean-equipe.ch",
    "founder": "Karolina Fabic",
    "taxID": "CHE-115.334.918",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Kreuzbündtenstrasse 8",
      "postalCode": "5727",
      "addressLocality": "Oberkulm",
      "addressRegion": "AG",
      "addressCountry": "CH"
    }},
    "openingHoursSpecification": [
      {{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "opens": "08:00",
        "closes": "17:00"
      }},
      {{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Saturday"],
        "opens": "09:00",
        "closes": "14:00"
      }}
    ]
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
        <span class="top-bar-badge" data-slot="topbar_badge">SEIT ÜBER 20 JAHREN IM EINSATZ</span>
        <span data-slot="topbar_sub">Clean Equipe GmbH · Kreuzbündtenstrasse 8, 5727 Oberkulm · Wynental &amp; Region Aarau</span>
      </div>
      <div class="top-bar-links">
        <a href="tel:+41765775722">{SVG_PHONE} <span>076 577 57 22</span></a>
        <a href="mailto:info@clean-equipe.ch">{SVG_MAIL} <span>info@clean-equipe.ch</span></a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER -->
  <header class="site-header" data-section="header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="Clean Equipe GmbH Oberkulm Startseite">
        <img src="images/logo-clean-equipe-retina.png" alt="Clean Equipe Reinigung Logo" class="brand-logo-wide" width="201" height="42" data-slot="brand_logo">
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}" data-nav-href="index.html">Startseite</a>
        <a href="leistungen.html" class="nav-link {nav_leistungen}" data-nav-href="leistungen.html">Angebot</a>
        <a href="referenzen.html" class="nav-link {nav_referenzen}" data-nav-href="referenzen.html">Einblicke</a>
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
    <a href="leistungen.html" onclick="wpCloseMobileMenu()">Reinigungsangebot (Unterhalt, Büro, Fenster &amp; Bau)</a>
    <a href="referenzen.html" onclick="wpCloseMobileMenu()">Praxis-Einblicke &amp; Google-Kundenstimmen</a>
    <a href="ueber-uns.html" onclick="wpCloseMobileMenu()">Über Karolina Fabic &amp; Clean Equipe GmbH</a>
    <a href="kontakt.html" onclick="wpCloseMobileMenu()">3-Schritte Offerte &amp; Direktkontakt</a>
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
            <img src="images/logo-clean-equipe-retina.png" alt="Clean Equipe GmbH Oberkulm" width="196" height="42" style="height:42px;width:auto;" loading="lazy" decoding="async">
          </div>
          <p style="font-size:0.86rem;color:#CFE3ED;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Seit über 20 Jahren professionell im Einsatz: Zuverlässige Unterhalts-, Büro-, Fenster- und Baureinigung mit fairen Preisen und flexiblen Terminen ab Oberkulm.
          </p>
          <div style="font-size:0.84rem;color:#FFFFFF;font-weight:600;">
            Kreuzbündtenstrasse 8 · 5727 Oberkulm (CHE-115.334.918)
          </div>
        </div>

        <div>
          <div class="footer-title">Unser Angebot</div>
          <ul class="footer-list">
            <li><a href="leistungen.html#unterhalt">Unterhaltsreinigung &amp; Wohnung</a></li>
            <li><a href="leistungen.html#fenster">Fenster-, Rahmen- &amp; Storenpflege</a></li>
            <li><a href="leistungen.html#buero">Büro- &amp; Praxisreinigung</a></li>
            <li><a href="leistungen.html#baureinigung">Baureinigung Neubau &amp; Umbau</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Unternehmen</div>
          <ul class="footer-list">
            <li><a href="index.html#projektberater">15s Reinigungs-Berater</a></li>
            <li><a href="referenzen.html">Einblicke &amp; Kundenstimmen</a></li>
            <li><a href="ueber-uns.html">Über Karolina Fabic</a></li>
            <li><a href="https://www.instagram.com/cleanequipe/" target="_blank" rel="noopener noreferrer">{SVG_INSTA}<span>Instagram @cleanequipe</span></a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Kontakt &amp; Zeiten</div>
          <ul class="footer-list">
            <li><a href="tel:+41765775722">{SVG_PHONE}<span>076 577 57 22</span></a></li>
            <li><a href="mailto:info@clean-equipe.ch">{SVG_MAIL}<span>info@clean-equipe.ch</span></a></li>
            <li><span style="display:inline-flex;align-items:center;gap:6px;font-size:0.84rem;color:#CFE3ED;min-height:34px;">{SVG_CLOCK}<span>Mo–Fr 08:00–17:00 · Sa 09:00–14:00</span></span></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Clean Equipe GmbH · 5727 Oberkulm · Alle Rechte vorbehalten.</div>
        <div style="display:flex;gap:18px;flex-wrap:wrap;align-items:center;">
          <button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; CH-revDSG</button>
          <a href="kontakt.html" style="color:#7DD3FC;font-weight:700;">Unverbindliche Offerte anfordern</a>
        </div>
      </div>
    </div>
  </footer>

{render_impressum_modal()}
{render_global_js()}
{extra_js}
</body>
</html>"""


def render_v2_shell(filename: str, page_title: str, active_nav: str, body_html: str, extra_js: str = "") -> str:
    nav_start = "active" if active_nav == "startseite" else ""
    nav_kontakt = "active" if active_nav == "kontakt" else ""

    return f"""<!DOCTYPE html>
<html lang="de-CH" data-expected-hero-polarity="dark" data-design-mode="evolution">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-XSS-Protection" content="1; mode=block">
  <meta name="referrer" content="no-referrer">
  <title>{page_title}</title>
  <meta name="description" content="Clean Equipe GmbH in 5727 Oberkulm (Zeigeversion): Zuverlässige Unterhaltsreinigung, Büroreinigung, Fenster &amp; Storen sowie Baureinigung mit Karolina Fabic.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700;800&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "CleaningService",
    "name": "Clean Equipe GmbH",
    "url": "https://clean-equipe.ch/",
    "telephone": "+41 76 577 57 22",
    "email": "info@clean-equipe.ch",
    "founder": "Karolina Fabic",
    "taxID": "CHE-115.334.918",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Kreuzbündtenstrasse 8",
      "postalCode": "5727",
      "addressLocality": "Oberkulm",
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
      <a href="index.html" class="brand-link" aria-label="Clean Equipe GmbH Oberkulm Startseite">
        <img src="images/logo-clean-equipe-retina.png" alt="Clean Equipe Reinigung Logo" class="brand-logo-wide" width="201" height="42" data-slot="brand_logo">
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}" data-nav-href="index.html">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#74E35E"/></svg>
          <span>Startseite</span>
        </a>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="leistungen.html" onclick="wpOpenBlueprintModal('Reinigungsangebot im Detail', 'Unterhaltsreinigung, Büro- &amp; Praxisreinigung, Fenster &amp; Storen sowie Baureinigung', 'Karolina Fabic (Clean Equipe GmbH)')">
          <span>Angebot</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="referenzen.html" onclick="wpOpenBlueprintModal('Praxis-Einblicke &amp; Verifizierte Kundenstimmen', 'Qualitätsstandards im Haushalt, Büro und Neubau sowie 5.0 / 5.0 Google-Bewertungen', 'Karolina Fabic')">
          <span>Einblicke</span>
        </button>
        <button type="button" class="nav-link nav-link-preview" data-nav-href="ueber-uns.html" onclick="wpOpenBlueprintModal('Über Karolina Fabic &amp; Clean Equipe GmbH', 'Über 20 Jahre Erfahrung, Handelsregister CHE-115.334.918 &amp; Einsatzgebiet Wynental–Aarau', 'Karolina Fabic')">
          <span>Über uns</span>
        </button>
        <a href="kontakt.html" class="nav-link {nav_kontakt}" data-nav-href="kontakt.html">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#74E35E"/></svg>
          <span>Kontakt</span>
        </a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" data-slot="header_cta">
          <span>3-Schritte-Offerte testen</span>
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
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu();wpOpenBlueprintModal('Reinigungsangebot im Detail', 'Unterhaltsreinigung, Büroreinigung, Fenster &amp; Storen sowie Baureinigung', 'Karolina Fabic')">
      <span>Angebot</span>
      <span class="preview-status-badge">Folgt beim Ausbau</span>
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu();wpOpenBlueprintModal('Praxis-Einblicke &amp; Kundenstimmen', 'Echte Einblicke aus Oberkulm &amp; 5.0 / 5.0 Google-Rezensionen', 'Karolina Fabic')">
      <span>Einblicke</span>
      <span class="preview-status-badge">Folgt beim Ausbau</span>
    </button>
    <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu();wpOpenBlueprintModal('Über Karolina Fabic &amp; Clean Equipe GmbH', 'Über 20 Jahre Berufspraxis &amp; Einsatzgebiet Wynental–Aarau', 'Karolina Fabic')">
      <span>Über uns</span>
      <span class="preview-status-badge">Folgt beim Ausbau</span>
    </button>
    <a href="kontakt.html" onclick="wpCloseMobileMenu()">Kontakt &amp; 3-Schritte-Offerte (Ausgearbeitet)</a>
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
            <img src="images/logo-clean-equipe-retina.png" alt="Clean Equipe GmbH Oberkulm" width="196" height="42" style="height:42px;width:auto;" loading="lazy" decoding="async">
          </div>
          <p style="font-size:0.86rem;color:#CFE3ED;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Seit über 20 Jahren professionell im Einsatz: Zuverlässige Unterhalts-, Büro-, Fenster- und Baureinigung mit fairen Preisen und flexiblen Terminen ab Oberkulm.
          </p>
          <div style="font-size:0.84rem;color:#FFFFFF;font-weight:600;">
            Kreuzbündtenstrasse 8 · 5727 Oberkulm
          </div>
        </div>

        <div>
          <div class="footer-title">Bereits in dieser Vorschau live</div>
          <ul class="footer-list">
            <li><a href="index.html">Startseite mit allen Leistungsbereichen</a></li>
            <li><a href="index.html#projektberater">Interaktiver 15s Reinigungs-Berater</a></li>
            <li><a href="kontakt.html">3-Schritte Smart-Offerten-Assistent</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Weitere Detailseiten (Ausbau)</div>
          <ul class="footer-list">
            <li><button type="button" onclick="wpOpenBlueprintModal('Reinigungsangebot im Detail', 'Unterhaltsreinigung, Büroreinigung, Fenster &amp; Storen sowie Baureinigung', 'Karolina Fabic')">Angebot im Detail (Vorschau)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Praxis-Einblicke &amp; Kundenstimmen', 'Qualitätsstandards &amp; verifizierte Google-Bewertungen', 'Karolina Fabic')">Einblicke &amp; Stimmen (Vorschau)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Über Karolina Fabic &amp; Clean Equipe', 'Über 20 Jahre Erfahrung &amp; regionales Einsatzgebiet', 'Karolina Fabic')">Über Clean Equipe (Vorschau)</button></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt &amp; Rechtliches</div>
          <ul class="footer-list">
            <li><a href="tel:+41765775722">{SVG_PHONE}<span>076 577 57 22</span></a></li>
            <li><a href="mailto:info@clean-equipe.ch">{SVG_MAIL}<span>info@clean-equipe.ch</span></a></li>
            <li><a href="kontakt.html" style="color:#7DD3FC;font-weight:700;">3-Schritte-Offerte testen</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Clean Equipe GmbH · Unverbindlicher Vorschau-Entwurf (Zeigeversion).</div>
        <div style="display:flex;gap:18px;flex-wrap:wrap;align-items:center;">
          <a href="kontakt.html" style="color:#7DD3FC;font-weight:700;">Smart-Offerte testen</a>
          <a href="index.html#weitere-themenbereiche">Weitere Detailseiten</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- KUNDENFREUNDLICHES VORSCHAU-MODAL (#wpBlueprintModal) -->
  <div class="wp-modal-backdrop" id="wpBlueprintModal" role="dialog" aria-modal="true" aria-labelledby="wpBpTitle" data-allow-scroll="true">
    <div class="wp-modal-dialog" data-allow-scroll="true">
      <button type="button" class="wp-modal-close" aria-label="Dialog schliessen" onclick="wpCloseBlueprintModal()">
        {SVG_CLOSE}
      </button>
      <div class="section-kicker">VORSCHAU-AUSBLICK · GEPLANTE DETAILSEITE</div>
      <h2 id="wpBpTitle" style="font-size:1.42rem;font-weight:700;margin-bottom:8px;">Reinigungsangebot im Detail</h2>
      <p id="wpBpSubtitle" style="font-size:0.92rem;color:var(--text-body);margin-bottom:16px;">
        Unterhaltsreinigung, Büroreinigung, Fenster &amp; Storen sowie Baureinigung
      </p>

      <div class="wp-modal-checklist">
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>In dieser <strong>Zeigeversion</strong> erleben Sie bereits die komplette <strong>Startseite</strong> sowie den <strong>3-Schritte Smart-Offerten-Assistenten</strong> live in Funktion.</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Beim gemeinsamen Ausbau wird diese Unterseite mit allen Leistungsdetails, Checklisten und Originalfotos von <strong id="wpBpOwner">Karolina Fabic</strong> freigeschaltet.</span>
        </div>
        <div class="wp-modal-check-item">
          {SVG_CHECK}
          <span>Sämtliche Texte, Bilder und Abschnitte lassen sich danach jederzeit bequem auf Zuruf oder selbst im Cockpit anpassen.</span>
        </div>
      </div>

      <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:space-between;align-items:center;">
        <button type="button" class="btn-cta btn-cta-outline btn-sm" onclick="wpCloseBlueprintModal()">
          <span>Zurück zur Vorschau</span>
        </button>
        <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm">
          <span>Jetzt 3-Schritte-Offerte testen</span>
          {SVG_ARROW}
        </a>
      </div>
    </div>
  </div>

{render_impressum_modal()}
{render_global_js()}
{extra_js}
</body>
</html>"""


def render_hero_index() -> str:
    return f"""
  <!-- STARTBÜHNE (DARK EVOLUTION STAGE #UI-16 & S-23 BASELINE LOCK) -->
  <section class="hero-section" data-section="hero">
    <div class="container">
      <div class="hero-grid">
        <div class="hero-col-left">
          <div>
            <div class="section-kicker kicker-on-dark" data-slot="hero_kicker">SEIT ÜBER 20 JAHREN · REINIGUNG FÜR BÜRO, ZUHAUSE &amp; NEUBAU</div>
            <h1 class="hero-title" data-slot="hero_title">
              Gründliche Sauberkeit mit <span>Handschlagqualität</span> ab Oberkulm.
            </h1>
            <p class="hero-lead" data-slot="hero_lead">
              Zuverlässig, speditiv und zu fairen Preisen: <strong>Karolina Fabic</strong> und ihr eingespieltes Team von der <strong>Clean Equipe GmbH</strong> pflegen Wohnungen, Einfamilienhäuser, Büroräume, Fenster, Storen und Neubauten im gesamten Wynental und Raum Aarau.
            </p>
            <div class="hero-actions">
              <a href="kontakt.html" class="btn-cta btn-cta-primary" data-slot="hero_cta_primary">
                <span>Offerte anfordern</span>
                {SVG_ARROW}
              </a>
              <a href="tel:+41765775722" class="btn-cta btn-cta-ghost-dark" data-slot="hero_cta_secondary">
                {SVG_PHONE}
                <span>076 577 57 22</span>
              </a>
            </div>
          </div>

          <div class="hero-badges">
            <div class="hero-badge-card">
              <span class="hero-badge-val" data-slot="kpi_1_val">Über 20 Jahre</span>
              <span class="hero-badge-lbl" data-slot="kpi_1_lbl">Berufserfahrung in der Reinigung</span>
            </div>
            <div class="hero-badge-card">
              <span class="hero-badge-val" data-slot="kpi_2_val">5.0 / 5.0 Sterne</span>
              <span class="hero-badge-lbl" data-slot="kpi_2_lbl">Verifizierte Google-Bewertungen</span>
            </div>
            <div class="hero-badge-card">
              <span class="hero-badge-val" data-slot="kpi_3_val">Mo–Sa flexibel</span>
              <span class="hero-badge-lbl" data-slot="kpi_3_lbl">Wöchentlich, 14-täglich oder nach Bedarf</span>
            </div>
            <div class="hero-badge-card">
              <span class="hero-badge-val" data-slot="kpi_4_val">5727 Oberkulm</span>
              <span class="hero-badge-lbl" data-slot="kpi_4_lbl">Wynental, Reinach, Suhr &amp; Aarau</span>
            </div>
          </div>
        </div>

        <div class="hero-media-card">
          <img src="images/fensterreinigung-fachfrau.jpg" alt="Karolina Fabic von der Clean Equipe GmbH bei der streifenfreien Fensterreinigung" fetchpriority="high" decoding="async" data-slot="hero_image">
          <div class="hero-media-caption">
            <div>
              <div style="font-family:var(--font-display);font-size:0.92rem;font-weight:700;color:#FFFFFF;" data-slot="hero_person_name">Karolina Fabic · Clean Equipe GmbH</div>
              <div style="font-size:0.78rem;color:#B8D4E3;" data-slot="hero_person_role">Persönliche Betreuung · Faire Preise · Flexible Termine</div>
            </div>
            <span class="top-bar-badge">Direkt erreichbar</span>
          </div>
        </div>
      </div>
    </div>
  </section>"""


V1_INDEX_BODY = f"""
{render_hero_index()}

  <!-- UNSER ANGEBOT IM ÜBERBLICK -->
  <section data-section="kernangebote" id="angebot" style="background-color:var(--bg-page);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="services_kicker">UNSER ANGEBOT · FÜR PRIVATPERSONEN, KMU &amp; VERWALTUNGEN</div>
        <h2 class="section-title" data-slot="services_title">Saubere Räume zum Wohlfühlen und Durchatmen</h2>
        <p class="section-desc" data-slot="services_desc">
          Vom regelmässigen Wohnungsputz mit Bügelservice über gepflegte Geschäftsräume bis zur Bauendreinigung erhalten Sie alle Arbeiten sorgfältig aus einer Hand.
        </p>
      </div>
{render_services_pillar_cards(is_v2=False)}
    </div>
  </section>

{render_cleaning_advisor()}
{render_reviews_and_karolina_section(is_v2=False)}
{render_acp_bridge_sections(is_v2=False)}
{render_faqs_section()}
"""

V2_SCOPE_SECTION = f"""
  <!-- V2 AUSBLICK AUF DIE 3 WEITEREN UNTERSEITEN -->
  <section class="preview-scope-section" id="weitere-themenbereiche" data-section="vorschau-umfang">
    <div class="container">
      <div class="preview-scope-banner">
        <div class="section-kicker">UNVERBINDLICHER VORSCHAU-ENTWURF · 2 BEISPIEL-SEITEN LIVE AUSGEARBEITET</div>
        <h2 style="font-size:clamp(1.5rem,2.4vw,2.02rem);font-weight:700;margin-bottom:10px;">
          Ausblick: Diese drei weiteren Detailseiten folgen beim gemeinsamen Ausbau
        </h2>
        <p style="font-size:0.94rem;color:var(--text-body);line-height:1.62;">
          In dieser <strong>Zeigeversion</strong> sind Ihre neue <strong>Startseite</strong> (inklusive 15-Sekunden Reinigungs-Berater) sowie die <strong>Kontaktseite mit dem 3-Schritte Smart-Offerten-Assistenten</strong> bereits vollständig ausgearbeitet und live testbar. Beim Ausbau schalten wir zusätzlich diese drei vertieften Unterseiten frei:
        </p>
      </div>

      <div class="grid-3">
        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Unterseite 1 · Angebot</span>
              <span class="icon-box">{SVG_HOME}</span>
            </div>
            <h3 class="card-title-1">Leistungen im Detail</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Klare Leistungsübersicht für Unterhaltsreinigung, Fenster &amp; Storen, Bügelservice, Büroreinigung und Baureinigung inklusive Ablauf von der Besichtigung bis zum Einsatz.
            </p>
          </div>
          <button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Leistungen &amp; Ablauf im Detail', 'Unterhaltsreinigung, Büroreinigung, Fenster &amp; Storen sowie Baureinigung', 'Karolina Fabic')">
            <span>Seiten-Ausblick öffnen</span>
            {SVG_ARROW}
          </button>
        </div>

        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Unterseite 2 · Einblicke</span>
              <span class="icon-box">{SVG_AWARD}</span>
            </div>
            <h3 class="card-title-1">Einblicke &amp; Stimmen</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Echte Arbeitsstandards aus Privathaushalten, Büros, Bädern und Neubauten kombiniert mit Ihren verifizierten 5.0 / 5.0 Google-Kundenbewertungen.
            </p>
          </div>
          <button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Praxis-Einblicke &amp; Kundenstimmen', 'Qualitätsstandards und echte 5.0 / 5.0 Google-Bewertungen aus der Region', 'Karolina Fabic')">
            <span>Seiten-Ausblick öffnen</span>
            {SVG_ARROW}
          </button>
        </div>

        <div class="preview-module-card">
          <div>
            <div class="card-badge-row">
              <span class="preview-status-badge">Unterseite 3 · Über uns</span>
              <span class="icon-box">{SVG_SHIELD}</span>
            </div>
            <h3 class="card-title-1">Über Karolina Fabic</h3>
            <p style="font-size:0.88rem;color:var(--text-body);">
              Persönliche Vorstellung, über 20 Jahre Erfahrung, Handelsregister-Nachweis (CHE-115.334.918 seit 2010) und Ihr gesamtes Einsatzgebiet rund um Oberkulm und Aarau.
            </p>
          </div>
          <button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Über Karolina Fabic &amp; Clean Equipe GmbH', 'Persönliche Werte, Geschichte seit 2010 &amp; Einsatzgebiet Wynental–Aarau', 'Karolina Fabic')">
            <span>Seiten-Ausblick öffnen</span>
            {SVG_ARROW}
          </button>
        </div>
      </div>
    </div>
  </section>"""

V2_INDEX_BODY = f"""
{render_hero_index()}

  <!-- UNSER ANGEBOT IM ÜBERBLICK -->
  <section data-section="kernangebote" id="angebot" style="background-color:var(--bg-page);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="services_kicker">UNSER ANGEBOT · FÜR PRIVATPERSONEN, KMU &amp; VERWALTUNGEN</div>
        <h2 class="section-title" data-slot="services_title">Saubere Räume zum Wohlfühlen und Durchatmen</h2>
        <p class="section-desc" data-slot="services_desc">
          Vom regelmässigen Wohnungsputz mit Bügelservice über gepflegte Geschäftsräume bis zur Bauendreinigung erhalten Sie alle Arbeiten sorgfältig aus einer Hand.
        </p>
      </div>
{render_services_pillar_cards(is_v2=True)}
    </div>
  </section>

{render_cleaning_advisor()}
{render_reviews_and_karolina_section(is_v2=True)}
{render_acp_bridge_sections(is_v2=True)}
{V2_SCOPE_SECTION}
{render_faqs_section()}
"""

V1_LEISTUNGEN_BODY = f"""
  <section class="hero-section" data-section="hero-leistungen">
    <div class="container">
      <div class="hero-grid">
        <div class="hero-col-left">
          <div>
            <div class="section-kicker kicker-on-dark">UNSER REINIGUNGSANGEBOT · MASSGESCHNEIDERT &amp; GRÜNDLICH</div>
            <h1 class="hero-title">Alle Reinigungsarbeiten aus <span>einer zuverlässigen Hand</span>.</h1>
            <p class="hero-lead">
              Ob wöchentliche Wohnungsreinigung, streifenfreie Fenster und Storen, tägliche Bürohygiene oder bezugsbereite Bauendreinigung: Wir richten uns flexibel nach Ihrem Objekt und Ihrem Terminplan.
            </p>
            <div class="hero-actions">
              <a href="kontakt.html" class="btn-cta btn-cta-primary"><span>Individuelle Offerte anfragen</span>{SVG_ARROW}</a>
              <a href="tel:+41765775722" class="btn-cta btn-cta-ghost-dark">{SVG_PHONE}<span>076 577 57 22</span></a>
            </div>
          </div>
          <div class="hero-badges">
            <div class="hero-badge-card">
              <span class="hero-badge-val">Privat &amp; Gewerbe</span>
              <span class="hero-badge-lbl">Wohnungen, Häuser, Büros &amp; Praxen</span>
            </div>
            <div class="hero-badge-card">
              <span class="hero-badge-val">Individueller Plan</span>
              <span class="hero-badge-lbl">Wöchentlich, 14-täglich oder einmalig</span>
            </div>
          </div>
        </div>
        <div class="hero-media-card">
          <img src="images/reinigung-einsatz-02.jpg" alt="Sorgfältige Büro- und Oberflächenreinigung durch Clean Equipe" fetchpriority="high" decoding="async" style="object-position:center 20%;">
          <div class="hero-media-caption">
            <div>
              <div style="font-family:var(--font-display);font-size:0.92rem;font-weight:700;color:#FFFFFF;">Sauberkeit bis ins Detail</div>
              <div style="font-size:0.78rem;color:#B8D4E3;">Schonende Pflege für Böden, Glas, Küche und Sanitär</div>
            </div>
            <span class="top-bar-badge">Faire Preise</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section data-section="alle-leistungen" style="background-color:var(--bg-page);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">VIER FACHBEREICHE · KLAR DEFINIERTE LEISTUNGEN</div>
        <h2 class="section-title">Wählen Sie genau die Unterstützung, die Ihren Alltag entlastet</h2>
        <p class="section-desc">Jeder Auftrag startet mit einem kurzen persönlichen Gespräch oder einer Besichtigung vor Ort, damit Umfang und Preis von Anfang an transparent stimmen.</p>
      </div>

      <div class="grid-2">
        <div class="content-card card-accent-top" id="unterhalt">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Fachbereich 01 · Privat</span>
              <span class="icon-box">{SVG_HOME}</span>
            </div>
            <h3 class="card-title-1">Unterhaltsreinigung &amp; Bügelservice</h3>
            <p style="font-size:0.91rem;color:var(--text-body);">
              Mehr Freizeit und ein jederzeit gepflegtes Zuhause: Wir übernehmen die regelmässige Reinigung Ihrer Wohnung oder Ihres Einfamilienhauses mit viel Umsicht.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span>Gründliche Reinigung von Wohnräumen, Küche, Bad und WC</span></div>
              <div class="check-item">{SVG_CHECK}<span>Bodenpflege (Staubsaugen und nebelfeuchtes Aufnehmen)</span></div>
              <div class="check-item">{SVG_CHECK}<span>Treppenhausreinigung für Ein- und Mehrfamilienhäuser</span></div>
              <div class="check-item">{SVG_CHECK}<span>Zuverlässiger Bügelservice direkt bei Ihnen vor Ort</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=unterhalt" class="btn-cta btn-cta-primary btn-sm" style="width:100%;"><span>Offerte für Unterhaltsreinigung</span>{SVG_ARROW}</a>
        </div>

        <div class="content-card card-accent-top" id="fenster">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Fachbereich 02 · Durchblick</span>
              <span class="icon-box">{SVG_SPARKLES}</span>
            </div>
            <h3 class="card-title-1">Fenster- &amp; Storenreinigung</h3>
            <p style="font-size:0.91rem;color:var(--text-body);">
              Saubere Glasflächen und gepflegte Storen lassen spürbar mehr Tageslicht in Ihre Räume und schützen Rahmen sowie Mechanik vor Verwitterung.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span>Streifenfreie Innen- und Aussenreinigung aller Fensterflächen</span></div>
              <div class="check-item">{SVG_CHECK}<span>Reinigung von Fensterrahmen, Falzen, Dichtungen und Simsen</span></div>
              <div class="check-item">{SVG_CHECK}<span>Schonende Pflege von Lamellenstoren und Rollläden</span></div>
              <div class="check-item">{SVG_CHECK}<span>Grosse Fensterfronten, Sitzplatzverglasungen und Schaufenster</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=fenster" class="btn-cta btn-cta-primary btn-sm" style="width:100%;"><span>Offerte für Fenster &amp; Storen</span>{SVG_ARROW}</a>
        </div>

        <div class="content-card card-green-top" id="buero">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge meta-badge-green">Fachbereich 03 · Unternehmen</span>
              <span class="icon-box">{SVG_BUILDING}</span>
            </div>
            <h3 class="card-title-1">Büro- &amp; Gewerbereinigung</h3>
            <p style="font-size:0.91rem;color:var(--text-body);">
              Ein gepflegter Empfang und hygienische Arbeitsplätze stärken das Wohlbefinden Ihres Teams und hinterlassen bei Kunden und Gästen sofort Vertrauen.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span>Arbeitsplätze, Pulte, Empfangsbereiche und Korridore</span></div>
              <div class="check-item">{SVG_CHECK}<span>Sitzungszimmer, Glastrennwände und Bodenbeläge</span></div>
              <div class="check-item">{SVG_CHECK}<span>Hygienische Sanitäranlagen inklusive Verbrauchsmaterial-Kontrolle</span></div>
              <div class="check-item">{SVG_CHECK}<span>Küchen, Kaffeestationen und Pausenräume</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=buero" class="btn-cta btn-cta-primary btn-sm" style="width:100%;"><span>Offerte für Büroreinigung</span>{SVG_ARROW}</a>
        </div>

        <div class="content-card card-green-top" id="baureinigung">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge meta-badge-green">Fachbereich 04 · Übergabe</span>
              <span class="icon-box">{SVG_HARDHAT}</span>
            </div>
            <h3 class="card-title-1">Baureinigung für Neubau &amp; Umbau</h3>
            <p style="font-size:0.91rem;color:var(--text-body);">
              Nach Handwerkerarbeiten braucht es erfahrene Profis, die feinen Baustaub, Klebereste und Zementschleier ohne Kratzer entfernen.
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span>Baugrobreinigung während der Ausbauphase</span></div>
              <div class="check-item">{SVG_CHECK}<span>Gründliche Bauendreinigung vor Einzug oder Abnahme</span></div>
              <div class="check-item">{SVG_CHECK}<span>Reinigung nach Küchen-, Bad- oder Gesamtumbauten</span></div>
              <div class="check-item">{SVG_CHECK}<span>Termingerechte Ausführung für Bauherrschaft und Architektur</span></div>
            </div>
          </div>
          <a href="kontakt.html?thema=baureinigung" class="btn-cta btn-cta-primary btn-sm" style="width:100%;"><span>Offerte für Baureinigung</span>{SVG_ARROW}</a>
        </div>
      </div>
    </div>
  </section>

  <section data-section="ablauf" style="background-color:var(--bg-soft);border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">EINFACHER ABLAUF · IN DREI KLAREN SCHRITTEN</div>
        <h2 class="section-title">So unkompliziert starten Sie mit Clean Equipe</h2>
      </div>
      <div class="grid-3">
        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Schritt 1</span>
              <span class="icon-box">{SVG_PHONE}</span>
            </div>
            <h3 class="card-title-1">Kurze Anfrage</h3>
            <p style="font-size:0.89rem;color:var(--text-body);">Melden Sie sich per Telefon unter 076 577 57 22, per WhatsApp oder über unseren 3-Schritte-Assistenten mit Ihren Eckdaten.</p>
          </div>
          <span style="font-size:0.80rem;font-weight:700;color:var(--primary-text);">Antwort innert kurzer Zeit</span>
        </div>
        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Schritt 2</span>
              <span class="icon-box">{SVG_PIN}</span>
            </div>
            <h3 class="card-title-1">Faire Offerte</h3>
            <p style="font-size:0.89rem;color:var(--text-body);">Auf Wunsch besichtigt Karolina Fabic Ihre Räume kurz vor Ort und erstellt eine klare, unverbindliche Offerte ohne versteckte Zuschläge.</p>
          </div>
          <span style="font-size:0.80rem;font-weight:700;color:var(--primary-text);">100 % Kostentransparenz</span>
        </div>
        <div class="content-card">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge meta-badge-green">Schritt 3</span>
              <span class="icon-box">{SVG_SPARKLES}</span>
            </div>
            <h3 class="card-title-1">Pünktlicher Start</h3>
            <p style="font-size:0.89rem;color:var(--text-body);">Zum vereinbarten Wunschtermin legen wir sorgfältig los – einmalig oder im entspannten Wochen- und Zweiwochen-Rhythmus.</p>
          </div>
          <span style="font-size:0.80rem;font-weight:700;color:var(--accent-palette-1-strong);">Feste Ansprechperson</span>
        </div>
      </div>
    </div>
  </section>
"""

V1_REFERENZEN_BODY = f"""
  <section class="hero-section" data-section="hero-referenzen">
    <div class="container">
      <div class="hero-grid">
        <div class="hero-col-left">
          <div>
            <div class="section-kicker kicker-on-dark">PRAXIS-EINBLICKE &amp; KUNDENSTIMMEN · 5.0 / 5.0 AUF GOOGLE</div>
            <h1 class="hero-title">Unser Ziel sind rundum <span>zufriedene Kundinnen und Kunden</span>.</h1>
            <p class="hero-lead">
              Sauberkeit sieht und spürt man sofort beim Eintreten. Entdecken Sie Einblicke in unsere tägliche Arbeit und lesen Sie, was Kundinnen aus der Region über Clean Equipe berichten.
            </p>
            <div class="hero-actions">
              <a href="kontakt.html" class="btn-cta btn-cta-primary"><span>Eigene Offerte anfordern</span>{SVG_ARROW}</a>
              <a href="https://www.instagram.com/cleanequipe/" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-ghost-dark">{SVG_INSTA}<span>@cleanequipe folgen</span></a>
            </div>
          </div>
          <div class="hero-badges">
            <div class="hero-badge-card">
              <span class="hero-badge-val">5.0 / 5.0 Sterne</span>
              <span class="hero-badge-lbl">Höchstnote in Google-Rezensionen</span>
            </div>
            <div class="hero-badge-card">
              <span class="hero-badge-val">Stammkundschaft</span>
              <span class="hero-badge-lbl">Langjährige Mandate im Wynental</span>
            </div>
          </div>
        </div>
        <div class="hero-media-card">
          <img src="images/objekt-detail-01.jpg" alt="Sorgfältige Detailreinigung von Glas- und glatten Oberflächen" fetchpriority="high" decoding="async" style="object-position:center 50%;">
          <div class="hero-media-caption">
            <div>
              <div style="font-family:var(--font-display);font-size:0.92rem;font-weight:700;color:#FFFFFF;">Sorgfalt in jedem Winkel</div>
              <div style="font-size:0.78rem;color:#B8D4E3;">Gründlich, genau und trotzdem speditiv erledigt</div>
            </div>
            <span class="top-bar-badge">Geprüfte Qualität</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section data-section="praxis-einblicke" style="background-color:var(--bg-page);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">EINSATZBEREICHE · WORAUF WIR BESONDERS ACHTEN</div>
        <h2 class="section-title">Sechs typische Aufgaben aus unserem Reinigungsalltag</h2>
      </div>
      <div class="grid-3">
        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/fensterreinigung-fachfrau.jpg" alt="Fensterreinigung im Privathaushalt und Büro" style="object-position:center 20%;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row"><span class="meta-badge">Glas &amp; Rahmen</span><span style="font-size:0.75rem;font-weight:700;color:var(--primary-text);">Privat &amp; KMU</span></div>
              <h3 class="card-title-1">Fenster &amp; Wintergärten</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">Streifenfreie Reinigung von Fensterflügeln, Rahmen, Dichtungen und Storen für helles Tageslicht in jedem Raum.</p>
            </div>
            <a href="kontakt.html?thema=fenster" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Anfragen</span>{SVG_ARROW}</a>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/reinigung-einsatz-02.jpg" alt="Pflege von Schreibtischen und Büroarbeitsplätzen" style="object-position:center 22%;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row"><span class="meta-badge">Büroalltag</span><span style="font-size:0.75rem;font-weight:700;color:var(--primary-text);">Wöchentlich</span></div>
              <h3 class="card-title-1">Pulte &amp; Sitzungszimmer</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">Diskrete Reinigung von Arbeitsplätzen, Monitoren, Tischen und Böden – pünktlich ausserhalb Ihrer Kernzeiten.</p>
            </div>
            <a href="kontakt.html?thema=buero" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Anfragen</span>{SVG_ARROW}</a>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/objekt-detail-02.jpg" alt="Hygienische Sanitär- und Badreinigung" style="object-position:center 45%;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row"><span class="meta-badge meta-badge-green">Hygiene</span><span style="font-size:0.75rem;font-weight:700;color:var(--accent-palette-1-strong);">Kalkfrei</span></div>
              <h3 class="card-title-1">Bad- &amp; Sanitärpflege</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">Strahlende Armaturen, kalkfreie Duschgläser und hygienisch frische Sanitäranlagen in Wohnungen und Betrieben.</p>
            </div>
            <a href="kontakt.html?thema=unterhalt" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Anfragen</span>{SVG_ARROW}</a>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/banner-reinigung-02.jpg" alt="Küchenfronten und Einbauschränke gründlich reinigen" style="object-position:44% center;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row"><span class="meta-badge meta-badge-green">Neubau &amp; Umbau</span><span style="font-size:0.75rem;font-weight:700;color:var(--accent-palette-1-strong);">Abnahme</span></div>
              <h3 class="card-title-1">Küchen &amp; Einbauten</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">Bis in die obersten Schrankfächer staub- und fettfrei gereinigt – ideal nach Umbauten oder vor dem Einzug.</p>
            </div>
            <a href="kontakt.html?thema=baureinigung" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Anfragen</span>{SVG_ARROW}</a>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/header-raum-01.jpg" alt="Ausgewählte Reinigungsutensilien und Pflegemittel" style="object-position:center 50%;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row"><span class="meta-badge">Ausrüstung</span><span style="font-size:0.75rem;font-weight:700;color:var(--primary-text);">Schonend</span></div>
              <h3 class="card-title-1">Passende Pflegemittel</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">Jede Oberfläche erhält die richtige Behandlung, damit Holz, Stein, Glas und Chromstahl über Jahre schön bleiben.</p>
            </div>
            <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Anfragen</span>{SVG_ARROW}</a>
          </div>
        </div>

        <div class="pillar-card">
          <div class="pillar-img-wrap">
            <img src="images/header-raum-03.jpg" alt="Farbcodierte Mikrofasertücher für saubere Bereiche" style="object-position:center 50%;" loading="lazy" decoding="async">
          </div>
          <div class="pillar-body">
            <div>
              <div class="card-badge-row"><span class="meta-badge meta-badge-green">Systematik</span><span style="font-size:0.75rem;font-weight:700;color:var(--accent-palette-1-strong);">Hygienisch</span></div>
              <h3 class="card-title-1">Getrenntes Tuchsystem</h3>
              <p style="font-size:0.88rem;color:var(--text-body);">Strikte Trennung der Reinigungstücher nach Bad, WC, Küche und Wohn- oder Bürobereich für einwandfreie Hygiene.</p>
            </div>
            <a href="kontakt.html" class="btn-cta btn-cta-outline btn-sm" style="width:100%;"><span>Anfragen</span>{SVG_ARROW}</a>
          </div>
        </div>
      </div>
    </div>
  </section>

{render_reviews_and_karolina_section(is_v2=False)}
"""

V1_UEBER_UNS_BODY = f"""
  <section class="hero-section" data-section="hero-ueber-uns">
    <div class="container">
      <div class="hero-grid">
        <div class="hero-col-left">
          <div>
            <div class="section-kicker kicker-on-dark">ÜBER CLEAN EQUIPE GMBH · VERWURZELT IN 5727 OBERKULM</div>
            <h1 class="hero-title">Persönlich geführt von <span>Karolina Fabic</span> – seit über 20 Jahren.</h1>
            <p class="hero-lead">
              Hinter einem glänzenden Zuhause oder Büro stehen Menschen, denen man gerne den Schlüssel anvertraut. Bei der Clean Equipe GmbH zählen Verlässlichkeit, Loyalität und echte Freude an sauberer Arbeit.
            </p>
            <div class="hero-actions">
              <a href="kontakt.html" class="btn-cta btn-cta-primary"><span>Persönlich kennenlernen</span>{SVG_ARROW}</a>
              <a href="tel:+41765775722" class="btn-cta btn-cta-ghost-dark">{SVG_PHONE}<span>076 577 57 22</span></a>
            </div>
          </div>
          <div class="hero-badges">
            <div class="hero-badge-card">
              <span class="hero-badge-val">08.01.2010</span>
              <span class="hero-badge-lbl">Handelsregistereintrag als GmbH</span>
            </div>
            <div class="hero-badge-card">
              <span class="hero-badge-val">CHE-115.334.918</span>
              <span class="hero-badge-lbl">Sitz an der Kreuzbündtenstrasse 8</span>
            </div>
          </div>
        </div>
        <div class="hero-media-card">
          <img src="images/karolina-fabic-portrait.jpg" alt="Karolina Fabic – Inhaberin der Clean Equipe GmbH in Oberkulm" fetchpriority="high" decoding="async" style="object-position:center 18%;">
          <div class="hero-media-caption">
            <div>
              <div style="font-family:var(--font-display);font-size:0.92rem;font-weight:700;color:#FFFFFF;">Karolina Fabic</div>
              <div style="font-size:0.78rem;color:#B8D4E3;">Inhaberin &amp; direkte Ansprechpartnerin in Oberkulm</div>
            </div>
            <span class="top-bar-badge">Seit 20+ Jahren</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section data-section="werte-und-region" style="background-color:var(--bg-page);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">UNSERE GRUNDWERTE · WORAUF SIE SICH VERLASSEN KÖNNEN</div>
        <h2 class="section-title">Warum uns Privatpersonen und Betriebe über Jahre treu bleiben</h2>
      </div>
      <div class="grid-3">
        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row"><span class="meta-badge">Wert 01</span><span class="icon-box">{SVG_SHIELD}</span></div>
            <h3 class="card-title-1">Vertrauen &amp; Loyalität</h3>
            <p style="font-size:0.90rem;color:var(--text-body);">Reinigung in privaten Wohnräumen und Büros ist Vertrauenssache. Diskretion, Pünktlichkeit und sorgsamer Umgang mit Ihrem Eigentum stehen an erster Stelle.</p>
          </div>
          <span style="font-size:0.80rem;font-weight:700;color:var(--primary-text);">Feste Bezugspersonen</span>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row"><span class="meta-badge">Wert 02</span><span class="icon-box">{SVG_SPARKLES}</span></div>
            <h3 class="card-title-1">Gründlich &amp; speditiv</h3>
            <p style="font-size:0.90rem;color:var(--text-body);">Über 20 Jahre Berufspraxis bedeuten geschulte Handgriffe: Wir arbeiten effizient und übersehen dennoch keine Kanten, Rahmen oder Armaturen.</p>
          </div>
          <span style="font-size:0.80rem;font-weight:700;color:var(--primary-text);">Hoher Qualitätsanspruch</span>
        </div>

        <div class="content-card card-green-top">
          <div>
            <div class="card-badge-row"><span class="meta-badge meta-badge-green">Wert 03</span><span class="icon-box">{SVG_CLOCK}</span></div>
            <h3 class="card-title-1">Faire Konditionen</h3>
            <p style="font-size:0.90rem;color:var(--text-body);">Klare Absprachen, faire Preise ohne Überraschungen und flexible Einsatzzeiten von Montag bis Samstag passend zu Ihrem Alltag.</p>
          </div>
          <span style="font-size:0.80rem;font-weight:700;color:var(--accent-palette-1-strong);">Transparente Offerten</span>
        </div>
      </div>
    </div>
  </section>

  <section data-section="einsatzgebiet" style="background-color:var(--bg-soft);border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker">REGIONAL VERANKERT · FIRMEN- &amp; STANDORTDATEN</div>
        <h2 class="section-title">Einsatzgebiet und offizielle Handelsregister-Angaben</h2>
      </div>
      <div class="split-grid">
        <div class="content-card card-green-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge meta-badge-green">Region · Kanton Aargau</span>
              <span class="icon-box">{SVG_PIN}</span>
            </div>
            <h3 class="card-title-1">Einsatzgebiet ab Oberkulm</h3>
            <p style="font-size:0.91rem;color:var(--text-body);margin-bottom:14px;">
              Kurze Wege ab Oberkulm ermöglichen pünktliche Einsätze und faire Konditionen für Haushalte, Praxen, Verwaltungen und Gewerbebetriebe in der ganzen Region:
            </p>
            <div class="check-list">
              <div class="check-item">{SVG_CHECK}<span><strong>Mittleres &amp; Oberes Wynental:</strong> Oberkulm, Unterkulm, Teufenthal, Dürrenäsch, Zetzwil, Gontenschwil, Reinach AG, Menziken und Burg</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Raum Aarau &amp; Suhrental:</strong> Gränichen, Suhr, Buchs AG, Aarau, Entfelden, Muhen und Schöftland</span></div>
              <div class="check-item">{SVG_CHECK}<span><strong>Seetal &amp; Lenzburg:</strong> Seon, Egliswil, Hallwil, Boniswil und Region Lenzburg</span></div>
            </div>
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm" style="align-self:flex-start;"><span>Einsatz in Ihrem Wohnort anfragen</span>{SVG_ARROW}</a>
        </div>

        <div class="content-card card-accent-top">
          <div>
            <div class="card-badge-row">
              <span class="meta-badge">Zefix · Handelsregister AG</span>
              <span class="icon-box">{SVG_SHIELD}</span>
            </div>
            <h3 class="card-title-1">Firmendaten auf einen Blick</h3>
            <div class="contact-direct-list" style="margin-top:10px;">
              <div class="contact-direct-item">
                <div class="contact-direct-role">Firma &amp; Rechtsform</div>
                <div class="contact-direct-person">Clean Equipe GmbH</div>
                <div class="contact-direct-links">Gesellschaft mit beschränkter Haftung · Eingetragen seit 08.01.2010</div>
              </div>
              <div class="contact-direct-item">
                <div class="contact-direct-role">UID &amp; Handelsregister-Nummer</div>
                <div class="contact-direct-person">CHE-115.334.918</div>
                <div class="contact-direct-links">CH-400.4.032.386-7 · Branche: Reinigung von Gebäuden</div>
              </div>
              <div class="contact-direct-item">
                <div class="contact-direct-role">Adresse &amp; Direktkontakt</div>
                <div class="contact-direct-person">Kreuzbündtenstrasse 8, 5727 Oberkulm</div>
                <div class="contact-direct-links">Telefon 076 577 57 22 · info@clean-equipe.ch</div>
              </div>
            </div>
          </div>
          <div style="font-size:0.82rem;color:var(--text-muted);">Geprüfte Angaben gemäss Zefix-Handelsregister und Impressum</div>
        </div>
      </div>
    </div>
  </section>
"""


def build_kontakt_body() -> str:
    return f"""
  <section class="hero-section" data-section="hero-kontakt" style="padding:52px 0 58px;">
    <div class="container">
      <div class="section-kicker kicker-on-dark">KONTAKT &amp; UNVERBINDLICHE OFFERTE · 5727 OBERKULM</div>
      <h1 class="hero-title" style="max-width:780px;margin-bottom:12px;">
        In drei kurzen Schritten zu Ihrer <span>persönlichen Offerte</span>.
      </h1>
      <p class="hero-lead" style="max-width:740px;margin-bottom:0;">
        Wählen Sie die gewünschte Dienstleistung, ergänzen Sie auf Wunsch Fotos Ihrer Räume oder Fenster und senden Sie Ihre Anfrage ohne Cookie-Banner und ohne Captcha-Rätsel direkt an Karolina Fabic.
      </p>
    </div>
  </section>

  <section data-section="kontakt-zentrale" style="padding:58px 0 80px;background-color:var(--bg-page);">
    <div class="container">
      <div class="contact-layout">
        <!-- LINKE SPALTE: DIREKTKONTAKT -->
        <div class="contact-info-panel">
          <div>
            <div class="section-kicker">DIREKTKONTAKT · PERSÖNLICH ERREICHBAR</div>
            <h2 style="font-size:1.52rem;font-weight:700;margin-bottom:10px;">Sprechen Sie direkt mit Karolina Fabic</h2>
            <p style="font-size:0.90rem;color:var(--text-body);">
              Sie telefonieren oder schreiben lieber kurz per WhatsApp? Wir freuen uns auf Ihre Nachricht und beraten Sie unkompliziert.
            </p>

            <div class="contact-direct-list">
              <div class="contact-direct-item">
                <div class="contact-direct-role">Telefon &amp; Direktruf</div>
                <div class="contact-direct-person"><a href="tel:+41765775722" style="color:var(--primary-text);">076 577 57 22</a></div>
                <div class="contact-direct-links">Persönliche Beratung &amp; Terminvereinbarung</div>
              </div>

              <div class="contact-direct-item">
                <div class="contact-direct-role">WhatsApp Nachricht</div>
                <div class="contact-direct-person">
                  <a href="https://wa.me/41765775722" target="_blank" rel="noopener noreferrer" style="color:var(--accent-palette-1-strong);display:inline-flex;align-items:center;gap:6px;">
                    {SVG_CHAT}<span>Direkt auf WhatsApp schreiben</span>
                  </a>
                </div>
                <div class="contact-direct-links">+41 76 577 57 22 · Gerne auch mit Handyfoto</div>
              </div>

              <div class="contact-direct-item">
                <div class="contact-direct-role">E-Mail &amp; Firmensitz</div>
                <div class="contact-direct-person"><a href="mailto:info@clean-equipe.ch" style="color:var(--primary-text);">info@clean-equipe.ch</a></div>
                <div class="contact-direct-links">Clean Equipe GmbH · Kreuzbündtenstrasse 8, 5727 Oberkulm</div>
              </div>

              <div class="contact-direct-item">
                <div class="contact-direct-role">Arbeitszeiten</div>
                <div class="contact-direct-person">Montag–Freitag: 08:00–17:00 Uhr</div>
                <div class="contact-direct-links">Samstag: 09:00–14:00 Uhr · Sonntag: geschlossen</div>
              </div>
            </div>
          </div>

          <div style="margin-top:20px;padding-top:16px;border-top:1px solid var(--border-light);display:flex;gap:12px;flex-wrap:wrap;align-items:center;justify-content:space-between;">
            <a href="https://www.instagram.com/cleanequipe/" target="_blank" rel="noopener noreferrer" style="font-size:0.84rem;font-weight:700;color:var(--primary-text);display:inline-flex;align-items:center;gap:6px;min-height:34px;">
              {SVG_INSTA}<span>Instagram @cleanequipe</span>
            </a>
            <a href="https://www.facebook.com/profile.php?id=100063723174622" target="_blank" rel="noopener noreferrer" style="font-size:0.84rem;font-weight:700;color:var(--text-body);display:inline-flex;align-items:center;gap:6px;min-height:34px;">
              <span>Facebook-Seite</span>{SVG_ARROW}
            </a>
          </div>
        </div>

        <!-- RECHTE SPALTE: 3-SCHRITTE SMART-OFFERTEN-ASSISTENT (#UI-23 WebMCP & Autofill konform) -->
        <div class="wizard-card">
          <div>
            <div class="section-kicker">3-SCHRITTE SMART-ANFRAGE · INKL. 1-SEITEN-DOSSIER</div>
            <h2 id="wpWizardTitle" style="font-size:1.42rem;font-weight:700;margin-bottom:14px;">
              Schritt 1: Welche Reinigung wünschen Sie?
            </h2>

            <div class="wp-stepper" aria-label="Fortschritt der Anfrage">
              <div class="wp-step-pill active" id="wpPill1"><span class="wp-step-num">1</span><span>Leistung</span></div>
              <div class="wp-step-pill" id="wpPill2"><span class="wp-step-num">2</span><span>Objekt &amp; Foto</span></div>
              <div class="wp-step-pill" id="wpPill3"><span class="wp-step-num">3</span><span>Kontakt</span></div>
            </div>

            <form id="isContactForm" onsubmit="return wpSubmitIsLead(event)" novalidate>
              <!-- Honeypot entkoppelt per form="wpTrapDetached" gegen KI-Agenten-Poisoning (#UI-23) -->
              <input type="text" id="wpHoneypot" name="website_url" form="wpTrapDetached" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0;">

              <!-- SCHRITT 1: LEISTUNG WÄHLEN -->
              <div class="wp-step-pane active" id="wpStep1">
                <div class="wp-role-grid" id="wpTopicGrid">
                  <button type="button" class="wp-role-tile selected" data-topic="Unterhaltsreinigung (Haus / Wohnung / Bügelservice)" onclick="wpSelectIsTopic('Unterhaltsreinigung (Haus / Wohnung / Bügelservice)')">
                    <div class="wp-role-head">
                      <span class="wp-role-icon">{SVG_HOME}</span>
                      <span class="wp-role-title" data-slot="topic_opt_1">Unterhaltsreinigung</span>
                    </div>
                    <span class="wp-role-desc">Haus, Wohnung, Treppenhaus oder Bügelservice · wöchentlich, 14-täglich oder nach Bedarf</span>
                  </button>

                  <button type="button" class="wp-role-tile" data-topic="Büro- & Gewerbereinigung (Arbeitsplätze / Sanitär / Praxis)" onclick="wpSelectIsTopic('Büro- & Gewerbereinigung (Arbeitsplätze / Sanitär / Praxis)')">
                    <div class="wp-role-head">
                      <span class="wp-role-icon">{SVG_BUILDING}</span>
                      <span class="wp-role-title" data-slot="topic_opt_2">Büro &amp; Gewerbe</span>
                    </div>
                    <span class="wp-role-desc">Arbeitsplätze, Sitzungszimmer, Küchen, Pausenräume &amp; Sanitäranlagen</span>
                  </button>

                  <button type="button" class="wp-role-tile" data-topic="Fenster- & Storenreinigung (Glas / Rahmen / Lamellen)" onclick="wpSelectIsTopic('Fenster- & Storenreinigung (Glas / Rahmen / Lamellen)')">
                    <div class="wp-role-head">
                      <span class="wp-role-icon">{SVG_SPARKLES}</span>
                      <span class="wp-role-title" data-slot="topic_opt_3">Fenster &amp; Storen</span>
                    </div>
                    <span class="wp-role-desc">Streifenfreie Glasflächen, Fensterrahmen, Falze, Wintergärten &amp; Lamellenstoren</span>
                  </button>

                  <button type="button" class="wp-role-tile" data-topic="Baureinigung (Neubau / Umbau / Bauendreinigung)" onclick="wpSelectIsTopic('Baureinigung (Neubau / Umbau / Bauendreinigung)')">
                    <div class="wp-role-head">
                      <span class="wp-role-icon">{SVG_HARDHAT}</span>
                      <span class="wp-role-title" data-slot="topic_opt_4">Baureinigung</span>
                    </div>
                    <span class="wp-role-desc">Neubauten, Umbauten &amp; bezugsbereite Bauendreinigung auf Übergabetermin</span>
                  </button>
                </div>

                <button type="button" class="btn-cta btn-cta-primary" style="width:100%;" onclick="wpNextStep(2)">
                  <span>Weiter zu Schritt 2: Objekt &amp; Rhythmus</span>
                  {SVG_ARROW}
                </button>
              </div>

              <!-- SCHRITT 2: OBJEKT, RHYTHMUS & FOTO -->
              <div class="wp-step-pane" id="wpStep2">
                <div class="form-grid-2" style="margin-bottom:14px;">
                  <div class="form-field">
                    <label for="wpDetail1" class="form-label">Objektgrösse / Anzahl Zimmer oder Fläche</label>
                    <input type="text" id="wpDetail1" name="object_size" class="form-input" placeholder="z. B. 4.5-Zimmer-Wohnung oder 180 m² Büro">
                  </div>
                  <div class="form-field">
                    <label for="wpDetail2" class="form-label">Wunschtag / bevorzugte Tageszeit</label>
                    <input type="text" id="wpDetail2" name="preferred_schedule" class="form-input" placeholder="z. B. Donnerstag Vormittag / Samstag">
                  </div>
                </div>

                <div class="form-field" style="margin-bottom:14px;">
                  <label class="form-label">Gewünschter Rhythmus / Terminwunsch</label>
                  <div class="wp-role-grid" id="wpUrgencyGrid" style="margin-bottom:0;">
                    <button type="button" class="wp-role-tile selected" data-urg="Regelmässiger Einsatz (wöchentlich / alle 2 Wochen)" onclick="wpSelectIsUrgency('Regelmässiger Einsatz (wöchentlich / alle 2 Wochen)')">
                      <span class="wp-role-title">Regelmässige Pflege</span>
                      <span class="wp-role-desc">Wöchentlich, alle zwei Wochen oder monatlich</span>
                    </button>
                    <button type="button" class="wp-role-tile" data-urg="Einmaliger Einsatz / Besichtigung vor Ort gewünscht" onclick="wpSelectIsUrgency('Einmaliger Einsatz / Besichtigung vor Ort gewünscht')">
                      <span class="wp-role-title">Einmalig / Besichtigung</span>
                      <span class="wp-role-desc">Fensterputz, Baureinigung oder kurze Vor-Ort-Offerte</span>
                    </button>
                  </div>
                </div>

                <div class="form-field" style="margin-bottom:14px;">
                  <label for="contactMessage" class="form-label">Ihre Wünsche oder Besonderheiten (optional)</label>
                  <textarea id="contactMessage" name="message" class="form-textarea" placeholder="z. B. Fenster inklusive Lamellenstoren, Bügelservice gewünscht, Haustiere im Haushalt oder Übergabetermin beim Neubau..."></textarea>
                </div>

                <div class="form-field" style="margin-bottom:18px;">
                  <label class="form-label">Optional: Fotos von Räumen, Fenstern oder Objekt beifügen (max. 3 Bilder)</label>
                  <div class="wp-upload-zone" onclick="document.getElementById('wpPhotoInput').click()">
                    <div style="display:flex;align-items:center;gap:8px;font-weight:700;font-size:0.86rem;color:var(--text-main);margin-bottom:2px;">
                      {SVG_CAMERA}<span>Hier tippen, um bis zu 3 Fotos auszuwählen (JPG/PNG)</span>
                    </div>
                    <div style="font-size:0.78rem;color:var(--text-muted);">Hilft Karolina Fabic für eine noch genauere Ersteinschätzung im 1-Seiten-Dossier</div>
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
                    <input type="text" id="contactName" name="name" autocomplete="name" class="form-input" placeholder="z. B. Anita Muster" required>
                  </div>
                  <div class="form-field">
                    <label for="contactCompany" class="form-label">Firma / Verwaltung (optional)</label>
                    <input type="text" id="contactCompany" name="organization" autocomplete="organization" class="form-input" placeholder="z. B. Muster Treuhand GmbH">
                  </div>
                </div>

                <div class="form-grid-2" style="margin-bottom:14px;">
                  <div class="form-field">
                    <label for="contactStreet" class="form-label">Strasse &amp; Hausnummer (Objektadresse)</label>
                    <input type="text" id="contactStreet" name="street-address" autocomplete="street-address" class="form-input" placeholder="z. B. Hauptstrasse 14">
                  </div>
                  <div class="form-field">
                    <label for="contactPlz" class="form-label">PLZ &amp; Ort *</label>
                    <input type="text" id="contactPlz" name="postal-code" autocomplete="postal-code" class="form-input" placeholder="z. B. 5727 Oberkulm" required>
                  </div>
                </div>

                <div class="form-grid-2" style="margin-bottom:14px;">
                  <div class="form-field">
                    <label for="contactPhone" class="form-label">Telefon / Mobile (für Rückruf / WhatsApp) *</label>
                    <input type="tel" id="contactPhone" name="tel" autocomplete="tel" class="form-input" placeholder="z. B. 079 123 45 67" required>
                  </div>
                  <div class="form-field">
                    <label for="contactEmail" class="form-label">E-Mail-Adresse *</label>
                    <input type="email" id="contactEmail" name="email" autocomplete="email" class="form-input" placeholder="ihre.adresse@beispiel.ch" required>
                  </div>
                </div>

                <div style="font-size:0.78rem;color:var(--text-muted);margin-bottom:14px;background-color:var(--bg-page);padding:10px 12px;border-radius:var(--radius-badge);border:1px solid var(--border-light);display:flex;flex-wrap:wrap;align-items:center;gap:6px;">
                  <span>Ihre Angaben werden vertraulich nach Schweizer Datenschutzgesetz verwendet.</span>
                  <button type="button" onclick="wpOpenImpressumModal()" style="background:none;border:none;color:var(--primary-text);font-weight:700;cursor:pointer;text-decoration:underline;font-family:inherit;font-size:inherit;display:inline-flex;align-items:center;min-height:34px;padding:4px 6px;">Datenschutz &amp; Impressum einsehen</button>
                </div>

                <div id="wpFormError" style="display:none;background-color:#FEF2F2;border:1px solid #FECACA;color:#991B1B;padding:10px 12px;border-radius:var(--radius-badge);font-size:0.84rem;font-weight:600;margin-bottom:14px;"></div>

                <div class="wizard-nav-row">
                  <button type="button" class="btn-cta btn-cta-outline btn-sm" onclick="wpNextStep(2)">
                    <span>Zurück zu Schritt 2</span>
                  </button>
                  <button type="submit" class="btn-cta btn-cta-primary" id="wpSubmitBtn">
                    <span id="wpSubmitBtnText">Unverbindliche Offerte anfordern</span>
                    {SVG_ARROW}
                  </button>
                </div>
              </div>
            </form>

            <!-- SUCCESS DOSSIER BOX -->
            <div class="wp-success-box" id="wpSuccessBox">
              <div style="display:flex;align-items:center;gap:10px;">
                <span class="icon-box" style="background-color:var(--accent-palette-1-soft);color:var(--accent-palette-1-strong);border-color:#B7DFB0;">{SVG_CHECK}</span>
                <div>
                  <div style="font-family:var(--font-display);font-size:1.08rem;font-weight:700;color:var(--text-main);">Vielen Dank – Ihr Offerten-Dossier ist bereit!</div>
                  <div style="font-size:0.82rem;color:var(--text-muted);">Referenz: <strong id="wpResRef">#WP-2026</strong> · Zuständig: <strong id="wpResAssigned">Karolina Fabic (Clean Equipe GmbH)</strong></div>
                </div>
              </div>
              <div style="font-size:0.88rem;color:var(--text-body);line-height:1.58;">
                <div><strong>Rückmeldung:</strong> <span id="wpResCallback">Persönlich per Telefon, WhatsApp oder E-Mail</span></div>
                <div><strong>Status:</strong> <span id="wpResChannels">1-Seiten-PDF-Dossier erstellt</span></div>
              </div>
              <div id="wpResWaPreview" style="font-size:0.80rem;color:var(--text-muted);background-color:#FFFFFF;border:1px solid var(--border-light);border-radius:var(--radius-badge);padding:10px 12px;white-space:pre-line;"></div>
              <div style="display:flex;gap:10px;flex-wrap:wrap;">
                <a href="#" target="_blank" rel="noopener noreferrer" id="wpResPdfBtn" class="btn-cta btn-cta-primary btn-sm">
                  <span>1-Seiten-PDF-Dossier öffnen</span>
                  {SVG_ARROW}
                </a>
                <button type="button" class="btn-cta btn-cta-outline btn-sm" onclick="wpResetWizard()">
                  <span>Weitere Anfrage erfassen</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>"""


def build_kontakt_js(client_slug: str, source_page: str) -> str:
    return f"""
  <script>
    var wpIsState = {{
      step: 1,
      topic: 'Unterhaltsreinigung (Haus / Wohnung / Bügelservice)',
      urgency: 'Regelmässiger Einsatz (wöchentlich / alle 2 Wochen)',
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
      for (var s = 1; s <= 3; s++) {{
        var pane = document.getElementById('wpStep' + s);
        var pill = document.getElementById('wpPill' + s);
        if (pane) pane.classList.toggle('active', s === step);
        if (pill) {{
          pill.classList.toggle('active', s === step);
          pill.classList.toggle('done', s < step);
        }}
      }}
      var titles = {{
        1: 'Schritt 1: Welche Reinigung wünschen Sie?',
        2: 'Schritt 2: Angaben zum Objekt & Wunsch-Rhythmus',
        3: 'Schritt 3: Ihre Kontaktdaten für die Offerte'
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
        img.alt = p.name || 'Objektfoto';
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
          errBox.textContent = 'Bitte füllen Sie Vor- und Nachname, PLZ/Ort, Telefonnummer und E-Mail-Adresse vollständig aus.';
          errBox.style.display = 'block';
        }}
        return false;
      }}

      var btn = document.getElementById('wpSubmitBtn');
      var btnTxt = document.getElementById('wpSubmitBtnText');
      if (btn) btn.disabled = true;
      if (btnTxt) btnTxt.textContent = '1-Seiten-Dossier wird erstellt...';

      var extra = {{
        'Gewünschte Reinigung': wpIsState.topic,
        'Objektgrösse / Zimmer / Fläche': d1 || 'Wird im Gespräch ergänzt',
        'Wunschtag / Tageszeit': d2 || 'Flexibel nach Absprache',
        'Rhythmus / Einsatzart': wpIsState.urgency
      }};
      if (street) extra['Objektadresse'] = street + ', ' + loc;

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
        message: msg || ('Offertenanfrage an Clean Equipe GmbH zu ' + wpIsState.topic),
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
        if (btnTxt) btnTxt.textContent = 'Unverbindliche Offerte anfordern';
        if (!res || !res.ok) {{
          if (errBox) {{
            errBox.textContent = (res && res.error) ? res.error : 'Übermittlung fehlgeschlagen. Bitte versuchen Sie es erneut.';
            errBox.style.display = 'block';
          }}
          return;
        }}
        document.getElementById('isContactForm').style.display = 'none';
        document.getElementById('wpResRef').textContent = res.ref_code || '#WP-2026';
        document.getElementById('wpResAssigned').textContent = res.assigned_to || 'Karolina Fabic (Clean Equipe GmbH)';
        document.getElementById('wpResCallback').textContent = res.callback_window || 'Persönlich per Telefon, WhatsApp oder E-Mail';
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
        if (btnTxt) btnTxt.textContent = 'Unverbindliche Offerte anfordern';
        if (errBox) {{
          errBox.textContent = 'Netzwerkfehler bei der Übermittlung. Bitte rufen Sie direkt 076 577 57 22 an oder schreiben Sie an info@clean-equipe.ch.';
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
          'unterhalt': 'Unterhaltsreinigung (Haus / Wohnung / Bügelservice)',
          'buero': 'Büro- & Gewerbereinigung (Arbeitsplätze / Sanitär / Praxis)',
          'fenster': 'Fenster- & Storenreinigung (Glas / Rahmen / Lamellen)',
          'baureinigung': 'Baureinigung (Neubau / Umbau / Bauendreinigung)'
        }};
        if (t && map[t]) {{
          wpSelectIsTopic(map[t]);
        }}
      }} catch (err) {{}}
    }})();
  </script>"""


v1_pages = [
    ("index.html", "Clean Equipe GmbH · 5727 Oberkulm | Reinigung für Büro, Zuhause &amp; Neubau", "startseite", V1_INDEX_BODY, ""),
    ("leistungen.html", "Reinigungsangebot | Unterhaltsreinigung, Büro, Fenster, Storen &amp; Baureinigung – Clean Equipe GmbH", "leistungen", V1_LEISTUNGEN_BODY, ""),
    ("referenzen.html", "Praxis-Einblicke &amp; Google-Kundenstimmen (5.0 / 5.0) | Clean Equipe GmbH Oberkulm", "referenzen", V1_REFERENZEN_BODY, ""),
    ("ueber-uns.html", "Über Karolina Fabic &amp; 20 Jahre Erfahrung | Clean Equipe GmbH 5727 Oberkulm", "ueber-uns", V1_UEBER_UNS_BODY, ""),
    ("kontakt.html", "Kontakt &amp; 3-Schritte Offerte | Clean Equipe GmbH Oberkulm (076 577 57 22)", "kontakt", build_kontakt_body(), build_kontakt_js("seit", "preview-seit/kontakt.html")),
]

for fname, title, nav_key, body, extra_script in v1_pages:
    full_html = render_v1_shell(fname, title, nav_key, body, extra_script)
    (V1_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V1] Wrote {fname} ({len(full_html)} bytes)")

v2_pages = [
    ("index.html", "Clean Equipe GmbH · Oberkulm (Zeigeversion / Vorschau-Entwurf)", "startseite", V2_INDEX_BODY, ""),
    ("kontakt.html", "Kontakt &amp; 3-Schritte Offerte (Zeigeversion) | Clean Equipe GmbH Oberkulm", "kontakt", build_kontakt_body(), build_kontakt_js("seit-v2", "preview-seit-v2/kontakt.html")),
]

for fname, title, nav_key, body, extra_script in v2_pages:
    full_html = render_v2_shell(fname, title, nav_key, body, extra_script)
    (V2_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"[V2] Wrote {fname} ({len(full_html)} bytes)")

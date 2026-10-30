#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator fuer HER11 (preview-her11) — Ausbildung & Karrierebegleitung für junge Fussballerinnen
Setzt das 9-seitige Redaktionskonzept (HER11_Webseitenkonzept.pdf, Oktober 2026), das Brand-Board
(#0B1A3B Deep Blue, #FF0066 Power Pink, #FFFFFF White, Montserrat Bold / SemiBold / Regular) sowie Jennys
Wachstums-Sektionen (Ausbildungsbetriebe/Sponsoren, Stimmen, ACP Social Media & Ratgeber) 1:1 um.
"""

import json
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
SITE_DIR = BASE_DIR / "preview-her11"
SITE_DIR.mkdir(parents=True, exist_ok=True)

# 1. company.json, config.json & site.json
company_data = {
    "name": "HER11",
    "company_name": "HER11 — Ihr Weg. Ihr Spiel. Ihre Zukunft.",
    "legal_name": "HER11 — Initiative fuer Ausbildung & Karrierebegleitung im Frauenfussball",
    "short_name": "HER11",
    "claim": "Ihr Weg. Ihr Spiel. Ihre Zukunft.",
    "subline": "Ausbildung & Karrierebegleitung für junge Fussballerinnen",
    "street": "Schweizweite Anlaufstelle",
    "zip": "8000",
    "city": "Zürich / Schweiz",
    "canton": "CH",
    "country": "Schweiz",
    "email": "info@her11.ch",
    "phone": "+41 44 500 11 11",
    "phone_clean": "+41445001111",
    "website": "https://www.her11.ch",
    "industry": "Sportförderung, Berufsbildung & Karrierebegleitung",
    "industry_id": "sport_ausbildung_karriere",
    "industry_label": "Ausbildung & Karrierebegleitung für junge Fussballerinnen",
    "work_category_label": "Spielerinnen, Ausbildung & Stadion",
    "studio_title": "WEBPILOT STUDIO",
    "is_website_studio": True,
    "host_url": "https://vorschau.magnet-xs.ch/her11/cockpit.html",
    "host_jobs_url": "https://vorschau.magnet-xs.ch/her11/",
    "copyright": "© 2026 HER11 — Ihr Weg. Ihr Spiel. Ihre Zukunft. Alle Rechte vorbehalten.",
    "hosting_status": "Live-Betrieb & Hosting: Schweizer Edge · WebPilot Studio v3.4.1",
    "instagram_profile": "https://www.instagram.com/",
    "linkedin_profile": "https://www.linkedin.com/",
    "enabled_sections": {
        "partner_network": True,
        "testimonials": True,
        "social_media_wall": True,
        "blog_section": True
    }
}

(SITE_DIR / "company.json").write_text(json.dumps(company_data, indent=2, ensure_ascii=False), encoding="utf-8")
(SITE_DIR / "config.json").write_text(json.dumps(company_data, indent=2, ensure_ascii=False), encoding="utf-8")

site_manifest = {
    "slug": "preview-her11",
    "public_slug": "her11",
    "token": "her112026",
    "brand": {
        "name": "HER11",
        "claim": "Ihr Weg. Ihr Spiel. Ihre Zukunft.",
        "subline": "Ausbildung & Karrierebegleitung für junge Fussballerinnen",
        "colors": {
            "deep_blue": "#0B1A3B",
            "power_pink": "#FF0066",
            "white": "#FFFFFF",
            "light_surface": "#F6F8FC"
        },
        "typography": {
            "headlines": "Montserrat Bold / ExtraBold",
            "subtitles": "Montserrat SemiBold",
            "body": "Montserrat Regular",
            "kicker": "Montserrat Bold"
        }
    },
    "pages": [
        {"file": "index.html", "nav": "Startseite", "title": "HER11 — Dein Talent. Dein Weg. Deine Zukunft."},
        {"file": "ueber-uns.html", "nav": "Über uns", "title": "Über uns — Weil jede Spielerin ihren eigenen Weg hat | HER11"},
        {"file": "ausbildung.html", "nav": "Ausbildung", "title": "Ausbildung — Zwei Karrieren. Eine Zukunft. | HER11"},
        {"file": "begleitung.html", "nav": "Begleitung", "title": "Begleitung — Du stehst im Mittelpunkt | HER11"},
        {"file": "mach-mit.html", "nav": "Mach mit", "title": "Mach mit — Gemeinsam schaffen wir Chancen | HER11"},
        {"file": "kontakt.html", "nav": "Kontakt", "title": "Kontakt — Lass uns gemeinsam etwas bewegen | HER11"}
    ]
}
(SITE_DIR / "site.json").write_text(json.dumps(site_manifest, indent=2, ensure_ascii=False), encoding="utf-8")

print("Saved company.json, config.json, site.json")

SHARED_CSS = """
    :root {
      --navy: #0B1A3B;
      --navy-deep: #071128;
      --navy-surface: #132654;
      --navy-card: #10214A;
      --pink: #FF0066;
      --pink-hover: #D90057;
      --pink-soft: rgba(255, 0, 102, 0.08);
      --pink-border: rgba(255, 0, 102, 0.32);
      --pink-glow: rgba(255, 0, 102, 0.24);
      --white: #FFFFFF;
      --bg-light: #FFFFFF;
      --surface-light: #F6F8FC;
      --surface-light-2: #EDF2F9;
      --text-dark: #0B1A3B;
      --text-muted: #475569;
      --text-on-dark: #FFFFFF;
      --text-muted-dark: #CBD5E1;
      --border-light: #DCE4F0;
      --border-dark: rgba(255, 255, 255, 0.12);
      --radius-badge: 4px;
      --radius-card: 8px;
      --shadow-sm: 0 2px 8px rgba(11, 26, 59, 0.06);
      --shadow-md: 0 12px 30px -6px rgba(11, 26, 59, 0.12);
      --shadow-dark: 0 14px 34px -6px rgba(4, 9, 22, 0.45);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
    ::selection { background: rgba(255, 0, 102, 0.22); color: #0B1A3B; }
    html { overflow-x: clip; }
    body {
      width: 100%;
      min-height: 100vh;
      overflow-x: clip;
      background: var(--bg-light);
      color: var(--text-dark);
      font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.6;
      font-size: 15px;
      font-variant-numeric: tabular-nums;
      caret-color: var(--pink);
      padding-bottom: calc(96px + env(safe-area-inset-bottom, 24px)) !important;
    }
    @media (min-width: 980px) {
      body { padding-bottom: 0 !important; }
    }
    h1, h2, h3, h4 {
      font-family: 'Montserrat', sans-serif;
      letter-spacing: -0.02em;
      line-height: 1.18;
    }
    a { text-underline-offset: 3px; }
    img { max-width: 100%; display: block; border-radius: var(--radius-card); }

    /* TOP TRUST & SLOGAN STRIP */
    .trust-strip {
      width: 100%;
      background: var(--navy-deep);
      color: #E2E8F0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding: 8px 16px;
      font-size: 0.76rem;
    }
    .trust-strip-inner {
      max-width: 1100px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 8px 16px;
    }
    .trust-strip-group {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px 16px;
    }
    .trust-badge-pink {
      background: rgba(255, 0, 102, 0.18);
      border: 1px solid rgba(255, 0, 102, 0.5);
      color: #FFD6E6;
      padding: 3px 8px;
      border-radius: var(--radius-badge);
      font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif; font-variant-numeric: tabular-nums;
      font-size: 0.7rem;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .trust-dot {
      width: 7px;
      height: 7px;
      border-radius: var(--radius-badge);
      background: var(--pink);
      display: inline-block;
    }
    .trust-strip-link {
      color: #F8FAFC;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-weight: 600;
      min-height: 34px;
      min-width: 34px;
      padding: 2px 4px;
    }
    .trust-strip-link:hover { color: var(--pink); }

    /* STICKY HEADER IN DEEP BLUE */
    .top-bar {
      padding: 12px 16px;
      background: rgba(11, 26, 59, 0.97);
      border-bottom: 1px solid var(--border-dark);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      position: sticky;
      top: 0;
      z-index: 1000;
      width: 100%;
    }
    .top-bar-inner {
      max-width: 1100px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 14px;
    }
    .brand-logo-wrap {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: var(--white);
      min-height: 44px;
      min-width: 44px;
    }
    .brand-emblem-img {
      width: 46px;
      height: 46px;
      object-fit: cover;
      border-radius: var(--radius-card);
      border: 1px solid rgba(255, 255, 255, 0.22);
      flex: 0 0 46px;
    }
    .brand-wordmark-box {
      display: flex;
      flex-direction: column;
      line-height: 1.05;
    }
    .brand-wordmark {
      font-size: 1.45rem;
      font-weight: 900;
      font-style: italic;
      letter-spacing: -0.03em;
      color: var(--white);
    }
    .brand-wordmark span {
      color: var(--pink);
    }
    .brand-subclaim {
      font-size: 0.66rem;
      font-weight: 600;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: #CBD5E1;
      margin-top: 2px;
    }

    .desktop-nav {
      display: none;
      align-items: center;
      gap: 6px;
    }
    .desk-nav-link {
      font-size: 0.84rem;
      font-weight: 700;
      color: #CBD5E1;
      text-decoration: none;
      padding: 8px 11px;
      border-radius: var(--radius-badge);
      transition: all 0.15s ease;
      min-height: 36px;
      display: inline-flex;
      align-items: center;
    }
    .desk-nav-link:hover,
    .desk-nav-link.active {
      color: var(--white);
      background: rgba(255, 255, 255, 0.08);
    }
    .desk-nav-link.active {
      border-bottom: 2px solid var(--pink);
    }
    .btn-desk-cta {
      font-size: 0.82rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--white) !important;
      background: var(--pink);
      padding: 9px 16px;
      border-radius: var(--radius-card);
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-height: 38px;
      box-shadow: 0 4px 14px var(--pink-glow);
      transition: background 0.15s ease;
    }
    .btn-desk-cta:hover { background: var(--pink-hover); }

    .nav-burger {
      width: 44px;
      height: 44px;
      min-width: 44px;
      min-height: 44px;
      border: 1px solid var(--border-dark);
      background: var(--navy-surface);
      border-radius: var(--radius-card);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: var(--white);
    }
    .nav-drawer {
      display: none;
      position: fixed;
      inset: 198px 0 0 0;
      background: rgba(7, 17, 40, 0.98);
      backdrop-filter: blur(16px);
      z-index: 900;
      padding: 20px 16px 110px 16px;
      flex-direction: column;
      gap: 8px;
      overflow-y: auto;
    }
    .nav-drawer.open { display: flex; }
    .drawer-nav-link {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--white);
      text-decoration: none;
      padding: 12px 14px;
      border-radius: var(--radius-card);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-dark);
      display: flex;
      justify-content: space-between;
      align-items: center;
      min-height: 46px;
    }
    .drawer-nav-link.active {
      border-color: var(--pink);
      background: rgba(255, 0, 102, 0.14);
    }

    @media (min-width: 980px) {
      .desktop-nav { display: flex; }
      .nav-burger { display: none !important; }
    }

    /* FREESTANDING KICKERS (#UI-01 & #UI-13: 100% FREISTEHEND, NO PILLS) */
    .section-kicker,
    .hero-kicker {
      font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif; font-variant-numeric: tabular-nums;
      font-size: 0.74rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.09em;
      color: var(--pink);
      background: transparent !important;
      border: none !important;
      padding: 0 !important;
      box-shadow: none !important;
      display: block;
      margin-bottom: 8px;
    }
    .section-kicker::before,
    .hero-kicker::before {
      content: "";
      display: inline-block;
      width: 16px;
      height: 2px;
      background: currentColor;
      vertical-align: middle;
      margin-right: 8px;
      border-radius: 2px;
      position: relative;
      top: -1px;
    }

    /* HERO SECTIONS (DARK STADIUM LOOK #0B1A3B) */
    .hero-wrap {
      width: 100%;
      background-color: #0B1A3B;
      background-image: radial-gradient(circle at 82% 18%, rgba(255, 0, 102, 0.22) 0%, #132654 42%, #0B1A3B 85%);
      color: var(--white);
      border-bottom: 1px solid var(--border-dark);
      padding: 36px 16px 48px 16px;
    }
    .hero-inner {
      max-width: 1100px;
      margin: 0 auto;
      width: 100%;
      display: grid;
      grid-template-columns: 1fr;
      gap: 28px;
      align-items: center;
    }
    .hero-title {
      font-size: 1.95rem;
      font-weight: 900;
      text-transform: uppercase;
      line-height: 1.1;
      letter-spacing: -0.025em;
      color: var(--white);
      margin-bottom: 10px;
    }
    .hero-title span {
      color: var(--pink);
    }
    .hero-subheadline {
      font-size: 1.12rem;
      font-weight: 600;
      color: #F8FAFC;
      margin-bottom: 14px;
    }
    .hero-lead {
      font-size: 0.95rem;
      color: var(--text-muted-dark);
      line-height: 1.65;
      margin-bottom: 12px;
    }
    .hero-badges-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 14px;
    }
    .meta-badge-dark {
      font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif; font-variant-numeric: tabular-nums;
      font-size: 0.72rem;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.07);
      border: 1px solid rgba(255, 255, 255, 0.16);
      color: #F8FAFC;
      padding: 6px 10px;
      border-radius: var(--radius-badge);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .hero-actions {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-top: 22px;
    }
    .btn-cta {
      width: 100%;
      min-height: 48px;
      min-width: 44px;
      padding: 12px 22px;
      border-radius: var(--radius-card);
      font-family: 'Montserrat', sans-serif;
      font-size: 0.9rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      cursor: pointer;
      border: none;
      transition: all 0.15s ease;
    }
    .btn-cta-pink {
      background: var(--pink);
      color: var(--white) !important;
      box-shadow: 0 6px 20px var(--pink-glow);
    }
    .btn-cta-pink:hover { background: var(--pink-hover); }
    .btn-cta-outline-light {
      background: rgba(255, 255, 255, 0.08);
      color: var(--white) !important;
      border: 1px solid rgba(255, 255, 255, 0.25);
    }
    .btn-cta-outline-light:hover {
      background: rgba(255, 255, 255, 0.15);
    }
    .btn-cta-navy {
      background: var(--navy);
      color: var(--white) !important;
      border: 1px solid var(--navy);
    }
    .btn-cta-navy:hover { background: var(--navy-surface); }

    .hero-visual-card {
      background: var(--navy-surface);
      border: 1px solid rgba(255, 255, 255, 0.14);
      box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.1), var(--shadow-dark);
      border-radius: var(--radius-card);
      padding: 10px;
      position: relative;
    }
    .hero-visual-img {
      width: 100%;
      height: 290px;
      object-fit: cover;
      object-position: center 20%;
      border-radius: var(--radius-card);
    }
    .hero-visual-caption {
      margin-top: 10px;
      padding: 8px 10px;
      background: rgba(7, 17, 40, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: var(--radius-badge);
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
      font-size: 0.78rem;
      color: #E2E8F0;
    }

    /* SECTIONS (LIGHT & DARK ALTERNATING, #UI-02 1100PX FLUCHTLINIE) */
    .section-wrap {
      width: 100%;
      background: var(--bg-light);
      color: var(--text-dark);
      border-bottom: 1px solid var(--border-light);
    }
    .section-wrap.section-surface {
      background: var(--surface-light);
    }
    .section-wrap.section-dark {
      background: var(--navy);
      color: var(--white);
      border-bottom: 1px solid var(--border-dark);
    }
    .section-inner {
      max-width: 1100px;
      margin: 0 auto;
      padding: 44px 16px;
      width: 100%;
    }
    .section-header {
      margin-bottom: 28px;
      max-width: 780px;
    }
    .section-title {
      font-size: 1.65rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: -0.02em;
      line-height: 1.18;
      margin-bottom: 10px;
      color: inherit;
    }
    .section-subtitle {
      font-size: 1.04rem;
      font-weight: 600;
      color: var(--pink);
      margin-bottom: 10px;
    }
    .section-desc {
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.65;
    }
    .section-dark .section-desc {
      color: var(--text-muted-dark);
    }

    /* 2-COL SPLIT BLOCK */
    .split-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 28px;
      align-items: stretch;
    }
    .split-col-card {
      background: var(--surface-light);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-card);
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }
    .section-dark .split-col-card {
      background: var(--navy-surface);
      border: 1px solid var(--border-dark);
      box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.08);
    }
    .split-media-img {
      width: 100%;
      height: 280px;
      object-fit: cover;
      border-radius: var(--radius-card);
    }

    /* BENTO GRIDS (2-COL, 3-COL, 4-COL WITH ZERO RAGGED RIGHT EDGE) */
    .pillar-cards,
    .social-grid,
    .blog-grid,
    .testimonials-grid,
    .team-dept-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
      align-items: stretch;
    }
    .values-grid,
    .partner-grid,
    .foerder-grid,
    .timeline-list {
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
      align-items: stretch;
    }
    .check-grid,
    .begleitung-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
      align-items: stretch;
    }

    /* CARDS */
    .her-card {
      background: var(--white);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-card);
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      height: 100%;
      box-shadow: var(--shadow-sm);
    }
    .her-card-dark {
      background: var(--navy-surface);
      border: 1px solid var(--border-dark);
      box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-card);
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      height: 100%;
      color: var(--white);
    }
    .her-card-pink-callout {
      background: linear-gradient(135deg, rgba(255, 0, 102, 0.14) 0%, rgba(19, 38, 84, 0.95) 100%);
      border: 1px solid var(--pink-border);
      border-radius: var(--radius-card);
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      height: 100%;
      color: var(--white);
    }
    .card-top-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      margin-bottom: 4px;
    }
    .icon-box-pink {
      width: 42px;
      height: 42px;
      border-radius: var(--radius-card);
      background: var(--pink-soft);
      border: 1px solid var(--pink-border);
      color: var(--pink);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex: 0 0 42px;
    }
    .card-tag-badge {
      font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif; font-variant-numeric: tabular-nums;
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      padding: 4px 8px;
      border-radius: var(--radius-badge);
      background: var(--pink-soft);
      color: var(--pink);
      border: 1px solid var(--pink-border);
    }
    .her-card-dark .card-tag-badge,
    .her-card-pink-callout .card-tag-badge {
      background: rgba(255, 0, 102, 0.2);
      color: #FFD6E6;
      border-color: rgba(255, 0, 102, 0.45);
    }
    .card-title {
      font-size: 1.08rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: -0.01em;
      color: inherit;
    }
    .card-text {
      font-size: 0.9rem;
      color: var(--text-muted);
      line-height: 1.6;
      flex: 1 1 auto;
    }
    .her-card-dark .card-text,
    .her-card-pink-callout .card-text {
      color: var(--text-muted-dark);
    }
    .card-link {
      margin-top: auto;
      padding-top: 8px;
      color: var(--pink);
      font-weight: 700;
      font-size: 0.86rem;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-height: 36px;
      min-width: 36px;
    }
    .card-link:hover { text-decoration: underline; }

    /* SOCIAL & BLOG MEDIA CARDS */
    .media-card-img {
      width: 100%;
      height: 210px;
      object-fit: cover;
      border-radius: var(--radius-card);
      margin-bottom: 8px;
    }

    /* BANNER CALLOUT */
    .cta-banner-box {
      background: radial-gradient(circle at 90% 20%, rgba(255, 0, 102, 0.24) 0%, #0B1A3B 75%);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: var(--radius-card);
      padding: 28px 24px;
      color: var(--white);
      display: flex;
      flex-direction: column;
      gap: 18px;
      align-items: flex-start;
      justify-content: space-between;
    }

    /* CONTACT FORM & TOPIC SELECTOR */
    .topic-selector-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 10px;
      margin-bottom: 20px;
    }
    .topic-chip-btn {
      width: 100%;
      min-height: 44px;
      padding: 10px 14px;
      border-radius: var(--radius-card);
      border: 1px solid var(--border-light);
      background: var(--surface-light);
      color: var(--text-dark);
      font-family: 'Montserrat', sans-serif;
      font-size: 0.85rem;
      font-weight: 700;
      text-align: left;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .topic-chip-btn.active,
    .topic-chip-btn:hover {
      background: var(--pink-soft);
      border-color: var(--pink);
      color: var(--navy);
    }
    .form-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 16px;
    }
    .form-field {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 6px;
    }
    .form-label {
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-dark);
    }
    .form-input,
    .form-select,
    .form-textarea {
      width: 100%;
      min-height: 46px;
      padding: 11px 14px;
      border-radius: var(--radius-card);
      border: 1px solid var(--border-light);
      background: var(--white);
      color: var(--text-dark);
      font-family: 'Montserrat', sans-serif;
      font-size: 0.92rem;
    }
    .form-textarea {
      min-height: 120px;
      resize: vertical;
    }
    .form-input:focus,
    .form-select:focus,
    .form-textarea:focus {
      outline: 2px solid var(--pink);
      border-color: var(--pink);
    }
    .consent-row {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 12px;
      background: var(--surface-light);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-card);
    }
    .consent-checkbox {
      width: 36px;
      height: 36px;
      min-width: 36px;
      min-height: 36px;
      flex: 0 0 36px;
      border-radius: var(--radius-badge);
      accent-color: var(--pink);
      cursor: pointer;
    }


    /* WEBPILOT 3-SCHRITTE SMART-ANFRAGE ASSISTENT (HER11 EDITION) */
    .wp-wizard-top {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 14px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border-light);
    }
    .wp-step-indicator {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.76rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--pink);
      background: var(--pink-soft);
      padding: 5px 10px;
      border-radius: var(--radius-badge);
    }
    .wp-nav-mini-group {
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }
    .wp-btn-mini {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: var(--surface-light);
      color: var(--navy);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-badge);
      min-height: 36px;
      min-width: 44px;
      padding: 7px 12px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.75rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .wp-btn-mini:hover {
      border-color: var(--pink);
      color: var(--pink);
    }
    .wp-progress-track {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 6px;
      margin-bottom: 18px;
    }
    .wp-progress-seg {
      height: 6px;
      border-radius: var(--radius-badge);
      background: #E2E8F0;
      transition: background 0.2s ease;
    }
    .wp-progress-seg.active {
      background: var(--pink);
    }
    .wp-progress-seg.done {
      background: var(--navy);
    }
    .wp-step-pane {
      display: none;
    }
    .wp-step-pane.active {
      display: block;
    }
    .wp-role-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 10px;
      margin-bottom: 18px;
      align-items: stretch;
    }
    @media (min-width: 560px) {
      .wp-role-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }
    }
    .wp-role-tile {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: flex-start;
      gap: 6px;
      width: 100%;
      min-width: 0;
      max-width: 100%;
      box-sizing: border-box;
      overflow-x: hidden;
      text-align: left;
      background: var(--white);
      border: 1.5px solid var(--border-light);
      border-radius: var(--radius-card);
      padding: 12px 14px;
      font-family: 'Montserrat', sans-serif;
      cursor: pointer;
      transition: all 0.15s ease;
      color: var(--text-dark);
    }
    .wp-role-tile:hover {
      border-color: var(--pink);
      background: var(--surface-light);
    }
    .wp-role-tile.selected {
      border-color: var(--pink);
      background: var(--pink-soft);
      box-shadow: 0 0 0 1px var(--pink);
    }
    .wp-role-head {
      display: flex;
      align-items: center;
      gap: 8px;
      width: 100%;
      min-width: 0;
    }
    .wp-role-icon {
      width: 30px;
      height: 30px;
      border-radius: var(--radius-badge);
      background: rgba(11, 26, 59, 0.08);
      color: var(--navy);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .wp-role-tile.selected .wp-role-icon {
      background: var(--pink);
      color: var(--white);
    }
    .wp-role-title {
      font-size: 0.86rem;
      font-weight: 800;
      color: var(--navy);
      line-height: 1.25;
      word-break: break-word;
    }
    .wp-role-desc {
      font-size: 0.75rem;
      color: var(--text-muted);
      line-height: 1.35;
      word-break: break-word;
    }
    .wp-upload-zone {
      border: 1.5px dashed #94A3B8;
      border-radius: var(--radius-card);
      background: var(--surface-light);
      padding: 14px;
      text-align: center;
      margin-top: 4px;
    }
    .wp-upload-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      background: var(--white);
      color: var(--navy);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-card);
      padding: 9px 14px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
    }
    .wp-upload-btn:hover {
      border-color: var(--pink);
      color: var(--pink);
    }
    .wp-photo-thumbs {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 8px;
      margin-top: 10px;
    }
    .wp-thumb-item {
      position: relative;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-card);
      overflow: hidden;
      background: var(--white);
      height: 74px;
    }
    .wp-thumb-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    .wp-thumb-del {
      position: absolute;
      top: 4px;
      right: 4px;
      background: rgba(11, 26, 59, 0.88);
      color: var(--white);
      border: 1px solid rgba(255, 255, 255, 0.3);
      border-radius: var(--radius-badge);
      padding: 2px 6px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.68rem;
      font-weight: 700;
      cursor: pointer;
    }
    .wp-plz-badge {
      display: none;
      align-items: center;
      gap: 6px;
      padding: 8px 12px;
      border-radius: var(--radius-card);
      font-size: 0.78rem;
      font-weight: 700;
    }
    .wp-plz-badge.in-area {
      display: inline-flex;
      background: rgba(5, 150, 105, 0.1);
      border: 1px solid rgba(5, 150, 105, 0.35);
      color: #047857;
    }
    .wp-demo-banner {
      background: rgba(11, 26, 59, 0.05);
      border: 1px solid rgba(11, 26, 59, 0.2);
      border-left: 4px solid var(--pink);
      border-radius: var(--radius-card);
      padding: 12px 14px;
      font-size: 0.8rem;
      color: var(--navy);
      line-height: 1.45;
    }
    .wp-success-box {
      display: none;
      background: var(--surface-light);
      border: 1.5px solid var(--pink);
      border-radius: var(--radius-card);
      padding: 20px 18px;
    }
    .wp-success-box.visible {
      display: block;
    }
    .wp-wa-preview {
      background: var(--navy);
      color: #E2E8F0;
      border-radius: var(--radius-card);
      padding: 12px 14px;
      font-size: 0.78rem;
      line-height: 1.45;
      white-space: pre-wrap;
      word-break: break-word;
      margin-top: 10px;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }

    /* FOOTER IN DEEPEST NAVY */
    .footer-wrap {
      width: 100%;
      background: var(--navy-deep);
      color: #94A3B8;
      border-top: 2px solid var(--pink);
    }
    .footer-inner {
      max-width: 1100px;
      margin: 0 auto;
      padding: 44px 16px 28px 16px;
      display: grid;
      grid-template-columns: 1fr;
      gap: 28px;
    }
    .footer-col h4 {
      color: var(--white);
      font-size: 0.92rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 12px;
    }
    .footer-links {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .footer-link-a {
      color: #CBD5E1;
      text-decoration: none;
      font-size: 0.86rem;
      font-weight: 500;
      display: inline-flex;
      align-items: center;
      min-height: 34px;
      min-width: 34px;
      padding: 3px 0;
    }
    .footer-link-a:hover { color: var(--pink); }
    .footer-bottom {
      max-width: 1100px;
      margin: 0 auto;
      padding: 18px 16px 24px 16px;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 10px 20px;
      font-size: 0.8rem;
      color: #94A3B8;
    }

    /* MOBILE THUMB BAR (375PX SAFE, #UI-13) */
    .mobile-thumb-bar {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(7, 17, 40, 0.97);
      backdrop-filter: blur(12px);
      border-top: 1px solid rgba(255, 255, 255, 0.15);
      padding: 10px 12px;
      padding-bottom: calc(10px + env(safe-area-inset-bottom, 0px));
      display: flex;
      gap: 8px;
      z-index: 950;
    }
    .thumb-btn {
      flex: 1 1 0;
      min-width: 0;
      max-width: 100%;
      min-height: 44px;
      padding: 0 8px;
      border-radius: var(--radius-card);
      font-size: 0.76rem;
      font-weight: 800;
      text-transform: uppercase;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      text-decoration: none;
    }
    .thumb-btn-navy {
      background: var(--navy-surface);
      color: var(--white);
      border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .thumb-btn-pink {
      background: var(--pink);
      color: var(--white);
    }

    /* TABLET & DESKTOP BREAKPOINTS */
    @media (min-width: 768px) {
      .hero-wrap { padding: 64px 24px 72px 24px; }
      .hero-inner { grid-template-columns: 1.15fr 0.85fr; gap: 44px; }
      .hero-title { font-size: 2.55rem; }
      .hero-visual-img { height: 380px; }
      .hero-actions { flex-direction: row; flex-wrap: wrap; }
      .btn-cta { width: auto; }
      .section-inner { padding: 64px 24px; }
      .section-title { font-size: 2.05rem; }
      .split-grid { grid-template-columns: 1fr 1fr; gap: 32px; }
      .pillar-cards,
      .social-grid,
      .blog-grid,
      .testimonials-grid,
      .team-dept-grid {
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 22px;
      }
      .values-grid,
      .partner-grid,
      .foerder-grid,
      .timeline-list {
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 22px;
      }
      .check-grid,
      .begleitung-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 22px;
      }
      /* Last item in 5-element grids spans full row for 100% right-edge alignment (#UI-14 Law 6) */
      .check-grid > *:last-child:nth-child(odd),
      .begleitung-grid > *:last-child:nth-child(odd) {
        grid-column: 1 / -1;
      }
      .topic-selector-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr)); }
      .form-grid-2 {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px;
      }
      .cta-banner-box {
        flex-direction: row;
        align-items: center;
        padding: 36px 36px;
      }
      .footer-inner {
        grid-template-columns: 1.3fr 1fr 1fr 1fr;
        gap: 32px;
      }
    }
    @media (max-width: 767px) {
      .trust-claim-text { display: none; }
    }
    @media (min-width: 980px) {
      .mobile-thumb-bar { display: none !important; }
    }
"""

def render_shell(filename: str, page_title: str, active_nav: str, body_html: str) -> str:
    nav_items = [
        ("index.html", "Startseite", "startseite"),
        ("ueber-uns.html", "Über uns", "ueber-uns"),
        ("ausbildung.html", "Ausbildung", "ausbildung"),
        ("begleitung.html", "Begleitung", "begleitung"),
        ("mach-mit.html", "Mach mit", "mach-mit"),
        ("kontakt.html", "Kontakt", "kontakt"),
    ]
    desk_links = []
    drawer_links = []
    for href, label, key in nav_items:
        cls = " active" if key == active_nav else ""
        desk_links.append(f'<a href="{href}" class="desk-nav-link{cls}" data-slot="nav_{key}">{label}</a>')
        drawer_links.append(
            f'<a href="{href}" class="drawer-nav-link{cls}" data-slot="drawer_{key}">'
            f'<span>{label}</span>'
            f'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>'
            f'</a>'
        )
    desk_nav_html = "\n          ".join(desk_links)
    drawer_nav_html = "\n      ".join(drawer_links)

    return f"""<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-XSS-Protection" content="1; mode=block">
  <meta name="referrer" content="no-referrer">
  <title>{page_title}</title>
  <meta name="description" content="HER11 — Ihr Weg. Ihr Spiel. Ihre Zukunft. Ausbildung und Karrierebegleitung für junge Fussballerinnen in der Schweiz.">
  <link rel="icon" href="images/favicon-h11.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,800;1,900&display=swap" rel="stylesheet">
  <style>{SHARED_CSS}
  </style>
</head>
<body>

  <!-- TOP SLOGAN & KONTAKT STRIP -->
  <div class="trust-strip" data-section-id="top-strip" data-section="top-strip" data-section-label="Oberes Infoband">
    <div class="trust-strip-inner">
      <div class="trust-strip-group">
        <span class="trust-badge-pink">
          <span class="trust-dot"></span>
          <span data-slot="strip_badge">HER11 · SCHWEIZ</span>
        </span>
        <span class="trust-claim-text" data-slot="strip_claim" style="font-weight: 600;">Ihr Weg. Ihr Spiel. Ihre Zukunft. — Ausbildung &amp; Karrierebegleitung für junge Fussballerinnen</span>
      </div>
      <div class="trust-strip-group">
        <a href="mailto:info@her11.ch" class="trust-strip-link" aria-label="E-Mail an info@her11.ch">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
          <span data-slot="email">info@her11.ch</span>
        </a>
        <a href="ausbildung.html" class="trust-strip-link" aria-label="Sportfreundliche Lehrstellen">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
          <span data-slot="strip_ausbildung">Sportfreundliche Lehrstellen</span>
        </a>
      </div>
    </div>
  </div>

  <!-- HAUPTNAVIGATION -->
  <header class="top-bar" id="top-bar" data-section-id="top-bar" data-section="top-bar" data-section-label="Kopfzeile &amp; Navigation">
    <div class="top-bar-inner">
      <a href="index.html" class="brand-logo-wrap" aria-label="HER11 Startseite">
        <img src="images/logo-her11.webp" alt="HER11 Offizielles Emblem" class="brand-emblem-img" data-slot="brand_logo">
        <div class="brand-wordmark-box">
          <div class="brand-wordmark" data-slot="brand_wordmark">HER<span>11</span></div>
          <div class="brand-subclaim" data-slot="brand_subclaim">Ihr Weg. Ihr Spiel. Ihre Zukunft.</div>
        </div>
      </a>

      <nav class="desktop-nav" aria-label="Hauptnavigation">
        {desk_nav_html}
        <a href="mach-mit.html" class="btn-desk-cta" data-slot="nav_cta_btn">
          <span>Mach mit!</span>
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
        </a>
      </nav>

      <button type="button" class="nav-burger" id="navBurgerBtn" aria-label="Menü öffnen" onclick="document.getElementById('mobileNavDrawer').classList.toggle('open')">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </div>
  </header>

  <div class="nav-drawer" id="mobileNavDrawer">
    {drawer_nav_html}
    <a href="kontakt.html" class="btn-cta btn-cta-pink" style="margin-top: 8px;" data-slot="drawer_cta">
      <span>Jetzt Kontakt aufnehmen</span>
    </a>
  </div>

{body_html}

  <!-- FUSSZEILE (SEITE 9 REDAKTIONSKONZEPT) -->
  <footer class="footer-wrap" id="footer" data-section-id="footer" data-section="footer" data-section-label="Fusszeile &amp; Direktkontakt">
    <div class="footer-inner">
      <div class="footer-col">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
          <img src="images/logo-her11.webp" alt="HER11 Logo" style="width: 42px; height: 42px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.2);" data-slot="footer_logo">
          <div>
            <div style="font-size: 1.25rem; font-weight: 900; font-style: italic; color: #FFFFFF;" data-slot="footer_brand">HER<span style="color: #FF0066;">11</span></div>
            <div style="font-size: 0.72rem; color: #CBD5E1; font-weight: 600;" data-slot="footer_claim">Ihr Weg. Ihr Spiel. Ihre Zukunft.</div>
          </div>
        </div>
        <p style="font-size: 0.86rem; line-height: 1.6; color: #CBD5E1; margin-bottom: 12px;" data-slot="footer_subline">
          Ausbildung &amp; Karrierebegleitung für junge Fussballerinnen. Unabhängige Anlaufstelle für Talente, Familien, Ausbildungsbetriebe und Partner.
        </p>
      </div>

      <div class="footer-col">
        <h4 data-slot="footer_nav_heading">Seiten &amp; Überblick</h4>
        <ul class="footer-links">
          <li><a href="index.html" class="footer-link-a" data-slot="footer_nav_1">01 | Startseite</a></li>
          <li><a href="ueber-uns.html" class="footer-link-a" data-slot="footer_nav_2">02 | Über uns &amp; Werte</a></li>
          <li><a href="ausbildung.html" class="footer-link-a" data-slot="footer_nav_3">03 | Ausbildung &amp; Lehrstellen</a></li>
          <li><a href="begleitung.html" class="footer-link-a" data-slot="footer_nav_4">04 | Ganzheitliche Begleitung</a></li>
          <li><a href="mach-mit.html" class="footer-link-a" data-slot="footer_nav_5">05 | Mach mit (Partner &amp; Sponsoren)</a></li>
          <li><a href="kontakt.html" class="footer-link-a" data-slot="footer_nav_6">06 | Kontakt &amp; Anfrage</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 data-slot="footer_wege_heading">Direkte Einstiege</h4>
        <ul class="footer-links">
          <li><a href="kontakt.html?thema=ausbildung" class="footer-link-a" data-slot="footer_weg_1">Ausbildung als Spielerin suchen</a></li>
          <li><a href="kontakt.html?thema=beratung" class="footer-link-a" data-slot="footer_weg_2">Beratung &amp; Begleitung anfragen</a></li>
          <li><a href="kontakt.html?thema=betrieb" class="footer-link-a" data-slot="footer_weg_3">Ausbildungsbetrieb werden</a></li>
          <li><a href="kontakt.html?thema=sponsor" class="footer-link-a" data-slot="footer_weg_4">Sponsoring / Partnerschaft</a></li>
          <li><a href="kontakt.html?thema=netzwerk" class="footer-link-a" data-slot="footer_weg_5">Netzwerkpartner werden</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 data-slot="footer_contact_heading">Direkter Kontakt</h4>
        <ul class="footer-links">
          <li>
            <a href="mailto:info@her11.ch" class="footer-link-a" data-slot="footer_email_link">
              E-Mail: info@her11.ch
            </a>
          </li>
          <li>
            <a href="https://www.her11.ch" target="_blank" rel="noopener" class="footer-link-a" data-slot="footer_web_link">
              Webseite: www.her11.ch
            </a>
          </li>
          <li>
            <a href="kontakt.html#impressum-datenschutz" class="footer-link-a" data-slot="footer_impressum_link">
              Impressum &amp; Datenschutz
            </a>
          </li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <div data-slot="copyright">© 2026 HER11 — Ihr Weg. Ihr Spiel. Ihre Zukunft. Ausbildung &amp; Karrierebegleitung für junge Fussballerinnen.</div>
      <div style="display: inline-flex; align-items: center; gap: 8px;">
        <span style="display: inline-block; width: 6px; height: 6px; border-radius: 4px; background: #FF0066;"></span>
        <span data-slot="hosting_status">info@her11.ch · www.her11.ch · Impressum · Datenschutz</span>
      </div>
    </div>
  </footer>

  <!-- MOBILE DAUMENZONE (#UI-13) -->
  <div class="mobile-thumb-bar" id="mobileThumbBar">
    <a href="ausbildung.html" class="thumb-btn thumb-btn-navy" aria-label="Sportfreundliche Lehrstellen">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
      <span data-slot="thumb_ausbildung">Ausbildung</span>
    </a>
    <a href="mach-mit.html" class="thumb-btn thumb-btn-navy" aria-label="Partner oder Sponsor werden">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
      <span data-slot="thumb_machmit">Mach mit</span>
    </a>
    <a href="kontakt.html" class="thumb-btn thumb-btn-pink" aria-label="Jetzt Kontakt aufnehmen">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
      <span data-slot="thumb_kontakt">Kontakt</span>
    </a>
  </div>

  <script>
    (function() {{
      function sendHeight() {{
        if (window.parent && window.parent !== window) {{
          var h = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);
          window.parent.postMessage({{ type: "acp-embed-resize", height: h }}, "*");
        }}
      }}
      window.addEventListener("load", sendHeight);
      window.addEventListener("resize", sendHeight);
      setTimeout(sendHeight, 600);
    }})();
  </script>
</body>
</html>
"""

# Update company.json & config.json with proper umlauts (100% ss, no Eszett)
company_data["legal_name"] = "HER11 — Initiative für Ausbildung & Karrierebegleitung im Frauenfussball"
company_data["subline"] = "Ausbildung & Karrierebegleitung für junge Fussballerinnen"
company_data["city"] = "Zürich / Schweiz"
company_data["industry"] = "Sportförderung, Berufsbildung & Karrierebegleitung"
company_data["industry_label"] = "Ausbildung & Karrierebegleitung für junge Fussballerinnen"
(SITE_DIR / "company.json").write_text(json.dumps(company_data, indent=2, ensure_ascii=False), encoding="utf-8")
(SITE_DIR / "config.json").write_text(json.dumps(company_data, indent=2, ensure_ascii=False), encoding="utf-8")

# ==============================================================================
# 01 | STARTSEITE (index.html)
# ==============================================================================
INDEX_BODY = """
  <!-- HERO SECTION (01 | STARTSEITE) -->
  <section class="hero-wrap" id="hero" data-section-id="hero" data-section="hero" data-section-label="01 | Hero: Dein Talent. Dein Weg. Deine Zukunft.">
    <div class="hero-inner">
      <div>
        <span class="hero-kicker" data-slot="index_hero_kicker">HER11 · AUSBILDUNG &amp; KARRIEREBEGLEITUNG</span>
        <h1 class="hero-title" data-slot="index_hero_title">DEIN TALENT. DEIN WEG. <span>DEINE ZUKUNFT.</span></h1>
        <div class="hero-subheadline" data-slot="index_hero_sub">Wir schaffen Perspektiven für junge Fussballerinnen.</div>
        <p class="hero-lead" data-slot="index_hero_p1">
          Grosse Träume brauchen die richtigen Möglichkeiten. HER11 unterstützt ambitionierte junge Fussballerinnen dabei, ihre sportlichen Ziele zu verfolgen und gleichzeitig eine berufliche Zukunft aufzubauen.
        </p>
        <p class="hero-lead" data-slot="index_hero_p2">
          Unser Schwerpunkt liegt auf der Vereinbarkeit von Leistungssport und Ausbildung. Gemeinsam mit engagierten Unternehmen möchten wir sportfreundliche Lehrstellen ermöglichen. Darüber hinaus begleiten wir Spielerinnen und ihre Familien bei wichtigen Entscheidungen auf und neben dem Fussballplatz.
        </p>
        <div class="hero-badges-row">
          <span class="meta-badge-dark" data-slot="index_badge_1">Sportfreundliche Lehrstellen</span>
          <span class="meta-badge-dark" data-slot="index_badge_2">Ganzheitliche Begleitung</span>
          <span class="meta-badge-dark" data-slot="index_badge_3">Starkes Schweizer Netzwerk</span>
        </div>
        <div class="hero-actions">
          <a href="ueber-uns.html" class="btn-cta btn-cta-pink" data-slot="index_hero_cta1">
            <span>Entdecke HER11</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
          <a href="mach-mit.html" class="btn-cta btn-cta-outline-light" data-slot="index_hero_cta2">
            <span>Mach mit!</span>
          </a>
        </div>
      </div>

      <div class="hero-visual-card">
        <img src="images/hero-stadion-11.webp" alt="Spielerin mit Rückennummer HER11 im Stadion-Flutlicht" class="hero-visual-img" data-slot="index_hero_img">
        <div class="hero-visual-caption">
          <span style="font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif; font-variant-numeric: tabular-nums; font-weight: 700; color: #FF0066;" data-slot="index_hero_cap_tag">HER11 · #11</span>
          <span data-slot="index_hero_cap_text">Ihr Weg. Ihr Spiel. Ihre Zukunft.</span>
        </div>
      </div>
    </div>
  </section>

  <!-- SEKTION 2: FUSSBALL UND AUSBILDUNG. BEIDES IST MÖGLICH. -->
  <section class="section-wrap" id="ausbildung-intro" data-section-id="ausbildung-intro" data-section="ausbildung-intro" data-section-label="02 | Fussball und Ausbildung: Beides ist möglich">
    <div class="section-inner">
      <div class="split-grid" style="margin-bottom: 32px;">
        <div class="split-col-card">
          <div>
            <span class="section-kicker" data-slot="ausb_intro_kicker">DUALE KARRIERE IM FRAUENFUSSBALL</span>
            <h2 class="section-title" data-slot="ausb_intro_title">FUSSBALL UND AUSBILDUNG. BEIDES IST MÖGLICH.</h2>
            <p class="section-desc" style="margin-top: 12px;" data-slot="ausb_intro_desc">
              Wer im Fussball erfolgreich sein möchte, braucht Zeit für Training, Wettkämpfe und Regeneration. Eine passende Ausbildung sollte diese Entwicklung unterstützen – nicht verhindern. HER11 bringt junge Talente mit Unternehmen zusammen, die bereit sind, Leistungssport und Berufsbildung miteinander zu verbinden.
            </p>
          </div>
          <div style="margin-top: 22px;">
            <a href="ausbildung.html" class="btn-cta btn-cta-pink" data-slot="ausb_intro_cta">
              <span>Mehr über Ausbildung erfahren</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </a>
          </div>
        </div>

        <div class="split-col-card" style="padding: 12px;">
          <img src="images/perspektive-alpen-see.webp" alt="Spielerin mit HER11 Rucksack bei Sonnenaufgang über Schweizer See und Alpen" class="split-media-img" style="height: 100%; min-height: 260px;" data-slot="ausb_intro_img">
        </div>
      </div>

      <div class="pillar-cards">
        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="pillar_1_badge">SÄULE 01</span>
          </div>
          <h3 class="card-title" data-slot="pillar_1_title">Sportfreundliche Lehrstellen</h3>
          <p class="card-text" data-slot="pillar_1_text">
            Wir vernetzen junge Fussballerinnen mit Schweizer Ausbildungsbetrieben, die Morgentrainings, Wettkämpfe und eine erstklassige Berufslehre gemeinsam möglich machen.
          </p>
          <a href="ausbildung.html" class="card-link" data-slot="pillar_1_link">
            <span>Zur Ausbildungs-Übersicht</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="pillar_2_badge">SÄULE 02</span>
          </div>
          <h3 class="card-title" data-slot="pillar_2_title">Ganzheitliche Begleitung</h3>
          <p class="card-text" data-slot="pillar_2_text">
            Ob Karriereplanung, Ausbildungswahl, Gesundheit, mentale Stärke oder Familie: Wir stehen Spielerinnen und Eltern als unabhängige Ansprechstelle persönlich zur Seite.
          </p>
          <a href="begleitung.html" class="card-link" data-slot="pillar_2_link">
            <span>Alle 5 Begleitungs-Bereiche</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="pillar_3_badge">SÄULE 03</span>
          </div>
          <h3 class="card-title" data-slot="pillar_3_title">Starkes Partner-Netzwerk</h3>
          <p class="card-text" data-slot="pillar_3_text">
            Gemeinsam mit Ausbildungsbetrieben, Sponsoren und Fachpersonen aus Sportmedizin, Physiotherapie, Athletik und Mentaltraining bauen wir echte Zukunftschancen auf.
          </p>
          <a href="mach-mit.html" class="card-link" data-slot="pillar_3_link">
            <span>Partner &amp; Unterstützer werden</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- SEKTION 3: GEMEINSAM MACHEN WIR DEN UNTERSCHIED (DEEP BLUE) -->
  <section class="section-wrap section-dark" id="mach-mit-intro" data-section-id="mach-mit-intro" data-section="mach-mit-intro" data-section-label="03 | Gemeinsam machen wir den Unterschied">
    <div class="section-inner">
      <div class="section-header">
        <span class="section-kicker" data-slot="diff_kicker">NETZWERK FÜR CHANCENGLEICHHEIT</span>
        <h2 class="section-title" data-slot="diff_title">GEMEINSAM MACHEN WIR DEN UNTERSCHIED.</h2>
        <p class="section-desc" data-slot="diff_desc">
          Wir suchen Menschen und Unternehmen, die an das Potenzial junger Fussballerinnen glauben. Ob mit einer sportfreundlichen Lehrstelle, einer Partnerschaft oder finanzieller Unterstützung: Gemeinsam eröffnen wir jungen Frauen neue Perspektiven.
        </p>
      </div>

      <div class="pillar-cards">
        <div class="her-card-dark">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="diff_c1_tag">01 · LEHRBETRIEBE</span>
          </div>
          <h3 class="card-title" data-slot="diff_c1_title">Ausbildungspartner werden</h3>
          <p class="card-text" data-slot="diff_c1_text">
            Ermöglichen Sie einer jungen Leistungssportlerin eine sportfreundliche Lehrstelle und gewinnen Sie extrem disziplinierte, zielstrebige Lernende für Ihren Betrieb.
          </p>
          <a href="kontakt.html?thema=betrieb" class="card-link" data-slot="diff_c1_link">
            <span>Als Ausbildungsbetrieb melden</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card-dark">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="diff_c2_tag">02 · SPONSORING</span>
          </div>
          <h3 class="card-title" data-slot="diff_c2_title">Sponsor &amp; Förderpartner werden</h3>
          <p class="card-text" data-slot="diff_c2_text">
            Investieren Sie nicht nur in den Fussball, sondern in die berufliche und persönliche Zukunft junger Frauen. Partnerschaften mit nachhaltiger gesellschaftlicher Wirkung.
          </p>
          <a href="kontakt.html?thema=sponsor" class="card-link" data-slot="diff_c2_link">
            <span>Sponsoring-Möglichkeiten prüfen</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card-dark">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="diff_c3_tag">03 · FACHNETZWERK</span>
          </div>
          <h3 class="card-title" data-slot="diff_c3_title">Netzwerkpartner werden</h3>
          <p class="card-text" data-slot="diff_c3_text">
            Bringen Sie Ihre Expertise in Sportmedizin, Physiotherapie, Athletik, Mentaltraining, Bildung oder Berufsberatung in das HER11-Kompetenznetzwerk ein.
          </p>
          <a href="kontakt.html?thema=netzwerk" class="card-link" data-slot="diff_c3_link">
            <span>Fachnetzwerk beitreten</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>
      </div>

      <div style="margin-top: 28px;">
        <a href="mach-mit.html" class="btn-cta btn-cta-pink" data-slot="diff_main_cta">
          <span>Mach mit!</span>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
        </a>
      </div>
    </div>
  </section>

  <!-- SEKTION 4: WACHSENDES PARTNER-, AUSBILDUNGSBETRIEB- & SPONSOREN-NETZWERK -->
  <section class="section-wrap section-surface" id="partner-netzwerk" data-section-id="partner-netzwerk" data-section="partner-netzwerk" data-section-label="04 | Wachsende Ausbildungsbetriebe &amp; Sponsoren">
    <div class="section-inner">
      <div class="section-header">
        <span class="section-kicker" data-slot="part_kicker">UNSERE WEGBEGLEITER &amp; PIONIERE</span>
        <h2 class="section-title" data-slot="part_title">UNTERNEHMEN, DIE AN JUNGE TALENTE GLAUBEN.</h2>
        <p class="section-desc" data-slot="part_desc">
          Dieses Netzwerk wächst laufend. Hier stellen wir Ausbildungsbetriebe, Sponsoren und Fachpartner vor, die gemeinsam mit HER11 sportfreundliche Lehrstellen und echte Förderstrukturen in der Schweiz aufbauen.
        </p>
      </div>

      <div class="partner-grid">
        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 21h18"/><path d="M5 21V7l8-4v18"/><path d="M19 21V11l-6-4"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="pcard_1_badge">AUSBILDUNGSBETRIEB · PIONIER</span>
          </div>
          <h3 class="card-title" data-slot="pcard_1_title">Schweizer KMU &amp; Lehrbetriebe (Slot #01)</h3>
          <p class="card-text" data-slot="pcard_1_text">
            Offizieller Platzhalter für die ersten zertifizierten HER11-Ausbildungsbetriebe (KV, Gesundheit, IT, Gewerbe &amp; Dienstleistung) mit flexiblen Trainings- und Arbeitszeitmodellen.
          </p>
          <a href="kontakt.html?thema=betrieb" class="card-link" data-slot="pcard_1_link">
            <span>Jetzt Lehrbetrieb-Profil eintragen lassen</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="pcard_2_badge">HAUPT- &amp; FÖRDERPARTNER</span>
          </div>
          <h3 class="card-title" data-slot="pcard_2_title">HER11 Sponsoring-Partner (Slot #02)</h3>
          <p class="card-text" data-slot="pcard_2_text">
            Offizieller Platzhalter für engagierte Unternehmen und Stiftungen, die Chancengleichheit, Talentförderung und duale Karrieren im Schweizer Frauenfussball unterstützen.
          </p>
          <a href="kontakt.html?thema=sponsor" class="card-link" data-slot="pcard_2_link">
            <span>Förderpartnerschaft anfragen</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="pcard_3_badge">MEDIZIN, ATHLETIK &amp; MENTAL</span>
          </div>
          <h3 class="card-title" data-slot="pcard_3_title">Kompetenz- &amp; Fachpartner (Slot #03)</h3>
          <p class="card-text" data-slot="pcard_3_text">
            Spezialisierte Anlaufstellen für Sportphysiotherapie, Verletzungsprävention, Leistungsdiagnostik, Ernährung, Sportpsychologie und Laufbahnberatung.
          </p>
          <a href="kontakt.html?thema=netzwerk" class="card-link" data-slot="pcard_3_link">
            <span>Netzwerkpartner werden</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card-pink-callout">
          <div class="card-top-row">
            <span class="icon-box-pink" style="background: rgba(255,0,102,0.25); color: #FFFFFF;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="pcard_4_badge">IHR UNTERNEHMEN HIER?</span>
          </div>
          <h3 class="card-title" data-slot="pcard_4_title">Werden Sie Partner der ersten Stunde</h3>
          <p class="card-text" data-slot="pcard_4_text">
            Setzen Sie ein sichtbares Zeichen für junge Talente im Frauenfussball. Wir präsentieren Ihr Unternehmen mit Logo, Porträt und direktem Link an dieser Stelle.
          </p>
          <a href="mach-mit.html" class="card-link" style="color: #FFD6E6;" data-slot="pcard_4_link">
            <span>Alle Partner-Wege im Überblick</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- SEKTION 5: STIMMEN & PERSPEKTIVEN (MITWACHSENDE TESTIMONIALS) -->
  <section class="section-wrap" id="stimmen" data-section-id="stimmen" data-section="stimmen" data-section-label="05 | Stimmen &amp; Perspektiven (Spielerinnen, Eltern, Betriebe)">
    <div class="section-inner">
      <div class="section-header">
        <span class="section-kicker" data-slot="stimmen_kicker">STIMMEN ZU HER11 · PERSPEKTIVEN AUS DER PRAXIS</span>
        <h2 class="section-title" data-slot="stimmen_title">WAS SPIELERINNEN, ELTERN UND BETRIEBE BEWEGT.</h2>
        <p class="section-desc" data-slot="stimmen_desc">
          Grosse sportliche Ziele und eine fundierte Berufsausbildung brauchen ein starkes Zusammenspiel zwischen Spielerin, Familie, Verein und Lehrbetrieb.
        </p>
      </div>

      <div class="testimonials-grid">
        <div class="her-card">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="quote_1_badge">PERSPEKTIVE SPIELERIN</span>
          </div>
          <h3 class="card-title" data-slot="quote_1_title">«Fussball ist mein grosser Traum – und meine Lehre gibt mir Sicherheit.»</h3>
          <p class="card-text" data-slot="quote_1_text">
            «Durch die Abstimmung zwischen Trainingsplan, Morgentrainings und meinem Ausbildungsbetrieb muss ich mich nicht gegen den Sport oder gegen den Beruf entscheiden, sondern kann in beiden Bereichen Vollgas geben.»
          </p>
          <div style="font-size: 0.8rem; font-weight: 700; color: var(--navy); padding-top: 8px; border-top: 1px solid var(--border-light);" data-slot="quote_1_author">
            Nachwuchsspielerin U17 / U19 · Duale Karriere
          </div>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="quote_2_badge">PERSPEKTIVE LEHRBETRIEB</span>
          </div>
          <h3 class="card-title" data-slot="quote_2_title">«Leistungssportlerinnen bringen aussergewöhnliche Disziplin ins Team.»</h3>
          <p class="card-text" data-slot="quote_2_text">
            «Junge Fussballerinnen wissen, was Fokus, Pünktlichkeit, Teamgeist und Eigenverantwortung bedeuten. Mit klaren Absprachen rund um Trainings- und Wettkampfzeiten gewinnen beide Seiten.»
          </p>
          <div style="font-size: 0.8rem; font-weight: 700; color: var(--navy); padding-top: 8px; border-top: 1px solid var(--border-light);" data-slot="quote_2_author">
            Berufsbildner / Ausbildungsbetrieb · HER11 Partnernetzwerk
          </div>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="quote_3_badge">PERSPEKTIVE ELTERN</span>
          </div>
          <h3 class="card-title" data-slot="quote_3_title">«Endlich eine unabhängige Anlaufstelle auf Augenhöhe.»</h3>
          <p class="card-text" data-slot="quote_3_text">
            «Beim Übergang von der Schule in die Berufswelt prallen viele Fragen gleichzeitig aufeinander. Eine persönliche Begleitung, die Sport, Schule, Gesundheit und Familie zusammendenkt, entlastet enorm.»
          </p>
          <div style="font-size: 0.8rem; font-weight: 700; color: var(--navy); padding-top: 8px; border-top: 1px solid var(--border-light);" data-slot="quote_3_author">
            Eltern einer Nachwuchsspielerin · Familienbegleitung
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SEKTION 6: SOCIAL MEDIA HUB (ACP FEED INTEGRATION) -->
  <section class="section-wrap section-dark" id="social-media" data-section-id="social-media" data-section="social-media" data-section-label="06 | Social Media Einblicke (@her11.ch)">
    <div class="section-inner">
      <div class="section-header">
        <span class="section-kicker" data-slot="social_kicker">AUF UND NEBEN DEM PLATZ · @HER11.CH</span>
        <h2 class="section-title" data-slot="social_title">EINBLICKE AUS DER BILDWELT VON HER11.</h2>
        <p class="section-desc" data-slot="social_desc">
          Stark. Authentisch. Gemeinsam. Zukunftsorientiert. Verfolge auf unseren Social-Media-Kanälen aktuelle Einblicke, Erfolgsgeschichten junger Talente und Neuigkeiten aus unserem Partnernetzwerk.
        </p>
      </div>

      <div class="social-grid">
        <div class="her-card-dark">
          <img src="images/fokus-flutlicht-closeup.webp" alt="Stark — Mentale Stärke und Fokus im Flutlicht" class="media-card-img" data-slot="social_1_img">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="social_1_badge">STARK. · FOKUS</span>
          </div>
          <h3 class="card-title" data-slot="social_1_title">Mentale Stärke in entscheidenden Momenten</h3>
          <p class="card-text" data-slot="social_1_text">
            Leistungsdruck, Schule, Training und grosse Ziele unter einen Hut bringen: Warum die richtige Begleitung neben dem Platz genauso zählt wie das Training auf dem Rasen.
          </p>
          <a href="begleitung.html" class="card-link" data-slot="social_1_link">
            <span>Mehr zur Begleitung</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card-dark">
          <img src="images/social-authentisch-stollen.webp" alt="Authentisch — Fussballschuh auf dem Rasen im Stadionlicht" class="media-card-img" data-slot="social_2_img">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="social_2_badge">AUTHENTISCH. · DUALER WEG</span>
          </div>
          <h3 class="card-title" data-slot="social_2_title">Vom Morgentraining direkt in den Lehrbetrieb</h3>
          <p class="card-text" data-slot="social_2_text">
            Wenn Ausbildungsbetrieb und sportliches Umfeld Hand in Hand arbeiten, entstehen Wege, die jungen Fussballerinnen beides eröffnen: Spitzensport und Berufsabschluss.
          </p>
          <a href="ausbildung.html" class="card-link" data-slot="social_2_link">
            <span>Sportfreundliche Lehrstellen</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card-dark">
          <img src="images/social-gemeinsam-team11.webp" alt="Gemeinsam — Vier Spielerinnen mit Rückennummer 11 Arm in Arm" class="media-card-img" data-slot="social_3_img">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="social_3_badge">GEMEINSAM. · #HER11</span>
          </div>
          <h3 class="card-title" data-slot="social_3_title">Ein starkes Team hinter jedem einzelnen Talent</h3>
          <p class="card-text" data-slot="social_3_text">
            Keine Spielerin geht ihren Weg allein. Gemeinsam mit Familien, Ausbildungsbetrieben, Sponsoren und Fachpersonen schaffen wir faire Chancen im Schweizer Frauenfussball.
          </p>
          <a href="mach-mit.html" class="card-link" data-slot="social_3_link">
            <span>Teil des Netzwerks werden</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- SEKTION 7: RATGEBER & MAGAZIN (BLOG FÜR ACP INTEGRATION) -->
  <section class="section-wrap" id="blog" data-section-id="blog" data-section="blog" data-section-label="07 | Ratgeber &amp; Wissen rund um duale Karrieren">
    <div class="section-inner">
      <div class="section-header">
        <span class="section-kicker" data-slot="blog_kicker">WISSEN FÜR SPIELERINNEN, ELTERN &amp; BETRIEBE</span>
        <h2 class="section-title" data-slot="blog_title">RATGEBER &amp; ORIENTIERUNG RUND UM DUALE KARRIEREN.</h2>
        <p class="section-desc" data-slot="blog_desc">
          Praxisnahe Antworten auf die wichtigsten Fragen beim Übergang von der Schule in die Berufswelt und bei der Förderung junger Fussballerinnen.
        </p>
      </div>

      <div class="blog-grid">
        <div class="her-card">
          <img src="images/nachwuchs-spielfeldrand.webp" alt="Junge Spielerin am Spielfeldrand im Abendflutlicht" class="media-card-img" data-slot="blog_1_img">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="blog_1_tag">FÜR SPIELERINNEN &amp; ELTERN</span>
          </div>
          <h3 class="card-title" data-slot="blog_1_title">Berufslehre und Leistungssport: Worauf es bei der Berufswahl ankommt</h3>
          <p class="card-text" data-slot="blog_1_text">
            Wie lässt sich eine Lehre mit Morgentrainings, Auswärtsspielen und Regenerationszeiten vereinbaren? Ein Leitfaden für die frühzeitige Planung mit Familie, Verein und Betrieb.
          </p>
          <a href="ausbildung.html" class="card-link" data-slot="blog_1_link">
            <span>Mehr erfahren</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card">
          <img src="images/perspektive-alpen-see.webp" alt="Weitblick über See und Alpen mit HER11 Rucksack" class="media-card-img" data-slot="blog_2_img">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="blog_2_tag">FÜR UNTERNEHMEN &amp; KMU</span>
          </div>
          <h3 class="card-title" data-slot="blog_2_title">Warum junge Fussballerinnen ein Gewinn für jeden Lehrbetrieb sind</h3>
          <p class="card-text" data-slot="blog_2_text">
            Disziplin, Teamgeist, Eigenverantwortung und hohe Belastbarkeit: Wie kleine, mittlere und grosse Unternehmen mit flexiblen Rahmenbedingungen Top-Nachwuchskräfte gewinnen.
          </p>
          <a href="ausbildung.html#zusammenarbeit-ablauf" class="card-link" data-slot="blog_2_link">
            <span>Ablauf für Unternehmen ansehen</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card">
          <img src="images/social-zukunft-stadion.webp" alt="Stadiontor im pink-blauen Flutlicht" class="media-card-img" data-slot="blog_3_img">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="blog_3_tag">GANZHEITLICHE ENTWICKLUNG</span>
          </div>
          <h3 class="card-title" data-slot="blog_3_title">Gesundheit, Prävention und mentale Stärke im Nachwuchsfussball</h3>
          <p class="card-text" data-slot="blog_3_text">
            Langfristige Entwicklung braucht ein gesundes Fundament: Wie qualifizierte Fachpersonen aus Sportmedizin, Physiotherapie und Mentaltraining junge Spielerinnen stärken.
          </p>
          <a href="begleitung.html" class="card-link" data-slot="blog_3_link">
            <span>Zu den 5 Begleitungs-Säulen</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>
      </div>
    </div>
  </section>
"""

# ==============================================================================
# 02 | ÜBER UNS (ueber-uns.html — SEITE 3 REDAKTIONSKONZEPT)
# ==============================================================================
UEBER_UNS_BODY = """
  <!-- HERO SECTION (02 | ÜBER UNS) -->
  <section class="hero-wrap" id="ueber-hero" data-section-id="ueber-hero" data-section="ueber-hero" data-section-label="02 | Über uns: Weil jede Spielerin ihren eigenen Weg hat">
    <div class="hero-inner">
      <div>
        <span class="hero-kicker" data-slot="ueber_hero_kicker">02 | ÜBER UNS · UNABHÄNGIGE ANLAUFSTELLE</span>
        <h1 class="hero-title" data-slot="ueber_hero_title">WEIL JEDE SPIELERIN IHREN <span>EIGENEN WEG</span> HAT.</h1>
        <div class="hero-subheadline" data-slot="ueber_hero_sub">HER11 stellt die Spielerin ins Zentrum.</div>
        <p class="hero-lead" data-slot="ueber_hero_p1">
          Der Frauenfussball wächst. Die Möglichkeiten für junge Talente entwickeln sich weiter. Gleichzeitig steigen die Anforderungen an Spielerinnen und ihre Familien. Training, Schule, Beruf, Gesundheit und persönliche Entwicklung müssen miteinander vereinbart werden.
        </p>
        <p class="hero-lead" data-slot="ueber_hero_p2">
          HER11 ist eine unabhängige Anlaufstelle für ambitionierte junge Fussballerinnen und ihre Familien. Wir setzen uns dafür ein, dass sportliche Träume nicht an fehlenden Ausbildungs- und Unterstützungsmöglichkeiten scheitern.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html?thema=beratung" class="btn-cta btn-cta-pink" data-slot="ueber_hero_cta1">
            <span>Persönliches Gespräch anfragen</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
          <a href="begleitung.html" class="btn-cta btn-cta-outline-light" data-slot="ueber_hero_cta2">
            <span>Unsere Begleitung entdecken</span>
          </a>
        </div>
      </div>

      <div class="hero-visual-card">
        <img src="images/nachwuchs-spielfeldrand.webp" alt="Junge Spielerin mit Fussball am Spielfeldrand" class="hero-visual-img" data-slot="ueber_hero_img">
        <div class="hero-visual-caption">
          <span style="font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif; font-variant-numeric: tabular-nums; font-weight: 700; color: #FF0066;" data-slot="ueber_cap_tag">UNABHÄNGIG &amp; PERSÖNLICH</span>
          <span data-slot="ueber_cap_text">Auf und neben dem Platz an deiner Seite.</span>
        </div>
      </div>
    </div>
  </section>

  <!-- UNSERE VISION -->
  <section class="section-wrap" id="vision" data-section-id="vision" data-section="vision" data-section-label="Unsere Vision">
    <div class="section-inner">
      <div class="split-grid">
        <div class="split-col-card">
          <div>
            <span class="section-kicker" data-slot="vision_kicker">UNSERE LEITIDEE</span>
            <h2 class="section-title" data-slot="vision_title">UNSERE VISION</h2>
            <p class="section-desc" style="font-size: 1.02rem; color: var(--text-dark); font-weight: 500; margin-top: 12px;" data-slot="vision_text">
              Jede ambitionierte Fussballerin soll die Chance erhalten, ihr Potenzial auszuschöpfen – unabhängig von ihrem familiären Hintergrund oder bestehenden Kontakten. Wir möchten Rahmenbedingungen schaffen, in denen junge Frauen ihren sportlichen Weg verfolgen und gleichzeitig eine solide berufliche Zukunft aufbauen können.
            </p>
          </div>
          <div style="margin-top: 24px;">
            <a href="ausbildung.html" class="btn-cta btn-cta-navy" data-slot="vision_cta">
              <span>Wie wir Sport &amp; Ausbildung verbinden</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </a>
          </div>
        </div>

        <div class="split-col-card" style="padding: 12px;">
          <img src="images/perspektive-alpen-see.webp" alt="Weitblick und Zukunftsperspektive für junge Fussballerinnen" class="split-media-img" style="height: 100%; min-height: 260px;" data-slot="vision_img">
        </div>
      </div>
    </div>
  </section>

  <!-- UNSERE WERTE (4 ORIGINAL-WERTE AUS SEITE 3) -->
  <section class="section-wrap section-dark" id="werte" data-section-id="werte" data-section="werte" data-section-label="Unsere 4 Grundwerte">
    <div class="section-inner">
      <div class="section-header">
        <span class="section-kicker" data-slot="werte_kicker">WOFÜR HER11 STEHT</span>
        <h2 class="section-title" data-slot="werte_title">UNSERE WERTE</h2>
        <p class="section-desc" data-slot="werte_desc">
          Vier klare Grundsätze leiten unser Handeln in der Zusammenarbeit mit Spielerinnen, Familien, Vereinen, Ausbildungsbetrieben und Partnern.
        </p>
      </div>

      <div class="values-grid">
        <div class="her-card-dark">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="wert_1_badge">WERT 01</span>
          </div>
          <h3 class="card-title" data-slot="wert_1_title">DIE SPIELERIN IM MITTELPUNKT</h3>
          <p class="card-text" data-slot="wert_1_text">
            Die Interessen und die langfristige Entwicklung der Spielerin stehen bei uns an erster Stelle.
          </p>
        </div>

        <div class="her-card-dark">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="wert_2_badge">WERT 02</span>
          </div>
          <h3 class="card-title" data-slot="wert_2_title">CHANCENGLEICHHEIT</h3>
          <p class="card-text" data-slot="wert_2_text">
            Wir möchten Zugänge schaffen und bestehende Hindernisse abbauen.
          </p>
        </div>

        <div class="her-card-dark">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="wert_3_badge">WERT 03</span>
          </div>
          <h3 class="card-title" data-slot="wert_3_title">VERTRAUEN</h3>
          <p class="card-text" data-slot="wert_3_text">
            Wir begleiten persönlich, unabhängig und auf Augenhöhe.
          </p>
        </div>

        <div class="her-card-dark">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="wert_4_badge">WERT 04</span>
          </div>
          <h3 class="card-title" data-slot="wert_4_title">ZUKUNFTSORIENTIERUNG</h3>
          <p class="card-text" data-slot="wert_4_text">
            Wir denken über die nächste Saison hinaus und unterstützen eine nachhaltige Entwicklung.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- HINTER HER11: ENGAGEMENT & ANSPRECHSTELLE -->
  <section class="section-wrap section-surface" id="team-beirat" data-section-id="team-beirat" data-section="team-beirat" data-section-label="Menschen &amp; Netzwerk hinter HER11">
    <div class="section-inner">
      <div class="section-header">
        <span class="section-kicker" data-slot="team_kicker">PERSÖNLICH · UNABHÄNGIG · VERNETZT</span>
        <h2 class="section-title" data-slot="team_title">GEMEINSAM FÜR DIE NÄCHSTE GENERATION IM FRAUENFUSSBALL.</h2>
        <p class="section-desc" data-slot="team_desc">
          Hinter HER11 stehen Menschen aus Sport, Berufsbildung, Wirtschaft und Fachbegleitung, die ihre Erfahrung bündeln, um jungen Fussballerinnen den Weg in eine erfolgreiche sportliche und berufliche Zukunft zu ebnen.
        </p>
      </div>

      <div class="team-dept-grid">
        <div class="her-card">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="tcard_1_tag">KARRIERE &amp; DIALOG</span>
          </div>
          <h3 class="card-title" data-slot="tcard_1_title">Anlaufstelle für Spielerinnen &amp; Eltern</h3>
          <p class="card-text" data-slot="tcard_1_text">
            Unabhängige Orientierung bei der Vereins- und Laufbahnplanung, bei Fragen zu Sportschulen sowie beim Übergang in eine passende Berufslehre.
          </p>
          <a href="kontakt.html?thema=beratung" class="card-link" data-slot="tcard_1_link">
            <span>Beratungsgespräch vereinbaren</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="tcard_2_tag">WIRTSCHAFT &amp; LEHRSTELLEN</span>
          </div>
          <h3 class="card-title" data-slot="tcard_2_title">Brückenbauer zu Ausbildungsbetrieben</h3>
          <p class="card-text" data-slot="tcard_2_text">
            Direkte Begleitung von KMU und Grossunternehmen beim Schaffen sportfreundlicher Lehrstellen und bei der Abstimmung von Trainings- und Arbeitszeiten.
          </p>
          <a href="kontakt.html?thema=betrieb" class="card-link" data-slot="tcard_2_link">
            <span>Als Betrieb Kontakt aufnehmen</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="tcard_3_tag">FACHEXPERTISE</span>
          </div>
          <h3 class="card-title" data-slot="tcard_3_title">Qualifiziertes Experten-Netzwerk</h3>
          <p class="card-text" data-slot="tcard_3_text">
            Gezielte Vermittlung an erfahrene Spezialistinnen und Spezialisten aus Sportmedizin, Physiotherapie, Athletik, Mentaltraining und Berufsberatung.
          </p>
          <a href="kontakt.html?thema=netzwerk" class="card-link" data-slot="tcard_3_link">
            <span>Fachnetzwerk kennenlernen</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>
      </div>
    </div>
  </section>
"""

# ==============================================================================
# 03 | AUSBILDUNG (ausbildung.html — SEITE 4 & 5 REDAKTIONSKONZEPT)
# ==============================================================================
AUSBILDUNG_BODY = """
  <!-- HERO SECTION (03 | AUSBILDUNG) -->
  <section class="hero-wrap" id="ausbildung-hero" data-section-id="ausbildung-hero" data-section="ausbildung-hero" data-section-label="03 | Ausbildung: Zwei Karrieren. Eine Zukunft.">
    <div class="hero-inner">
      <div>
        <span class="hero-kicker" data-slot="ausb_hero_kicker">03 | AUSBILDUNG · DUALE KARRIERE</span>
        <h1 class="hero-title" data-slot="ausb_hero_title">ZWEI KARRIEREN. <span>EINE ZUKUNFT.</span></h1>
        <div class="hero-subheadline" data-slot="ausb_hero_sub">Leistungssport und Berufsbildung gehören zusammen.</div>
        <p class="hero-lead" data-slot="ausb_hero_p1">
          Junge Fussballerinnen investieren viel Zeit und Energie in ihren Sport. Doch gerade beim Übergang von der Schule in die Berufswelt stehen viele vor einer grossen Herausforderung: Wie lässt sich eine Berufslehre mit intensiven Trainings, Morgentrainings und Wettkämpfen vereinbaren?
        </p>
        <p class="hero-lead" data-slot="ausb_hero_p2">
          HER11 möchte genau hier etwas bewegen. Unser Ziel ist es, gemeinsam mit Unternehmen ein Netzwerk sportfreundlicher Ausbildungsbetriebe aufzubauen. Wir suchen Firmen, die jungen Fussballerinnen eine Lehrstelle anbieten und bereit sind, ihre sportlichen Verpflichtungen bei der Ausbildungsplanung zu berücksichtigen. Damit junge Talente ihre sportliche Entwicklung fortsetzen und gleichzeitig eine qualifizierte Berufsausbildung absolvieren können.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html?thema=ausbildung" class="btn-cta btn-cta-pink" data-slot="ausb_hero_cta1">
            <span>Ich suche eine Ausbildung</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
          <a href="kontakt.html?thema=betrieb" class="btn-cta btn-cta-outline-light" data-slot="ausb_hero_cta2">
            <span>Jetzt Ausbildungsbetrieb werden</span>
          </a>
        </div>
      </div>

      <div class="hero-visual-card">
        <img src="images/perspektive-alpen-see.webp" alt="Spielerin mit HER11 Rucksack und Fussball mit Blick in die Zukunft" class="hero-visual-img" data-slot="ausb_hero_img">
        <div class="hero-visual-caption">
          <span style="font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif; font-variant-numeric: tabular-nums; font-weight: 700; color: #FF0066;" data-slot="ausb_cap_tag">BERUFSBILDUNG &amp; SPORT</span>
          <span data-slot="ausb_cap_text">Qualifizierte Lehre &amp; Leistungssport vereint.</span>
        </div>
      </div>
    </div>
  </section>

  <!-- SPORTFREUNDLICHE LEHRSTELLEN (5 MERKMALE AUS SEITE 4) -->
  <section class="section-wrap" id="sportfreundliche-lehrstellen" data-section-id="sportfreundliche-lehrstellen" data-section="sportfreundliche-lehrstellen" data-section-label="Sportfreundliche Lehrstellen: 5 Bausteine">
    <div class="section-inner">
      <div class="section-header">
        <span class="section-kicker" data-slot="sf_kicker">WAS DAS KONKRET BEDEUTET</span>
        <h2 class="section-title" data-slot="sf_title">SPORTFREUNDLICHE LEHRSTELLEN</h2>
        <div class="section-subtitle" data-slot="sf_sub">Unternehmen, die Talente fördern. Auf und neben dem Platz.</div>
        <p class="section-desc" data-slot="sf_desc">
          Eine sportfreundliche Lehrstelle bedeutet, dass Ausbildungsbetrieb und Spielerin gemeinsam Lösungen finden, um Berufsbildung und Leistungssport zu vereinbaren. Dazu können gehören:
        </p>
      </div>

      <div class="check-grid">
        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="sf_1_badge">BAUSTEIN 01</span>
          </div>
          <h3 class="card-title" data-slot="sf_1_title">Flexible Arbeitszeiten, abgestimmt auf den Trainingsplan</h3>
          <p class="card-text" data-slot="sf_1_text">
            Verlässliche Wochen- und Saisonplanung, die betriebliche Abläufe und sportliche Trainingsfenster sinnvoll aufeinander abstimmt.
          </p>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4"/><path d="m16.2 7.8 2.9-2.9"/><path d="M18 12h4"/><path d="m16.2 16.2 2.9 2.9"/><path d="M12 18v4"/><path d="m4.9 19.1 2.9-2.9"/><path d="M2 12h4"/><path d="m4.9 4.9 2.9 2.9"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="sf_2_badge">BAUSTEIN 02</span>
          </div>
          <h3 class="card-title" data-slot="sf_2_title">Möglichkeiten zur Teilnahme an Morgentrainings</h3>
          <p class="card-text" data-slot="sf_2_text">
            Freiräume für morgendliche Technik- und Athletikeinheiten durch individuell verschobene oder kompensierte Arbeitszeiten.
          </p>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="sf_3_badge">BAUSTEIN 03</span>
          </div>
          <h3 class="card-title" data-slot="sf_3_title">Berücksichtigung von Wettkämpfen und sportlichen Verpflichtungen</h3>
          <p class="card-text" data-slot="sf_3_text">
            Frühzeitige Koordination bei Meisterschaftsspielen, Cup-Einsätzen, Trainingslagern oder Aufgeboten für Auswahlteams.
          </p>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="sf_4_badge">BAUSTEIN 04</span>
          </div>
          <h3 class="card-title" data-slot="sf_4_title">Individuelle Abstimmung der Ausbildungsorganisation</h3>
          <p class="card-text" data-slot="sf_4_text">
            Massgeschneiderte Lösungen je nach Berufsfeld, Berufsfachschule und Lehrjahr, damit die Ausbildungsqualität jederzeit gewährleistet bleibt.
          </p>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="sf_5_badge">BAUSTEIN 05</span>
          </div>
          <h3 class="card-title" data-slot="sf_5_title">Regelmässiger Austausch zwischen Spielerin, Betrieb und sportlichem Umfeld</h3>
          <p class="card-text" data-slot="sf_5_text">
            Die Qualität der Berufsausbildung bleibt dabei zentral. HER11 unterstützt Unternehmen und Spielerinnen dabei, passende Rahmenbedingungen zu finden.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- FÜR SPIELERINNEN & FÜR UNTERNEHMEN (SEITE 4 & 5) -->
  <section class="section-wrap section-dark" id="zielgruppen-split" data-section-id="zielgruppen-split" data-section="zielgruppen-split" data-section-label="Für Spielerinnen &amp; Für Unternehmen">
    <div class="section-inner">
      <div class="split-grid">
        <div class="split-col-card">
          <div>
            <span class="section-kicker" data-slot="zg_spielerin_kicker">PERSPEKTIVE TALENT</span>
            <h2 class="section-title" data-slot="zg_spielerin_title">FÜR SPIELERINNEN</h2>
            <div class="section-subtitle" data-slot="zg_spielerin_sub">Dein Fussball. Deine Ausbildung. Dein Weg.</div>
            <p class="section-desc" style="margin-top: 10px;" data-slot="zg_spielerin_text">
              Du möchtest im Fussball weiterkommen und suchst eine passende Ausbildung? HER11 hilft dir, deine Möglichkeiten zu entdecken. Wir unterstützen dich bei der beruflichen Orientierung, der Suche nach einer sportfreundlichen Lehrstelle und bei Fragen zu Sportschulen oder anderen Ausbildungswegen. Gemeinsam schauen wir, welcher Weg zu deinen Zielen und deiner persönlichen Situation passt.
            </p>
          </div>
          <div style="margin-top: 24px;">
            <a href="kontakt.html?thema=ausbildung" class="btn-cta btn-cta-pink" data-slot="zg_spielerin_cta">
              <span>Ich suche eine Ausbildung</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </a>
          </div>
        </div>

        <div class="split-col-card">
          <div>
            <span class="section-kicker" data-slot="zg_firma_kicker">PERSPEKTIVE AUSBILDUNGSBETRIEB</span>
            <h2 class="section-title" data-slot="zg_firma_title">FÜR UNTERNEHMEN: MACHEN SIE MIT.</h2>
            <p class="section-desc" style="margin-top: 10px;" data-slot="zg_firma_p1">
              Geben Sie Talenten eine Chance. Junge Leistungssportlerinnen bringen Eigenschaften mit, die auch in der Berufswelt wertvoll sind: Disziplin, Teamgeist, Eigenverantwortung, Belastbarkeit und Zielstrebigkeit.
            </p>
            <p class="section-desc" style="margin-top: 12px;" data-slot="zg_firma_p2">
              Mit einer sportfreundlichen Lehrstelle ermöglichen Sie einer jungen Frau, ihre sportlichen Ambitionen mit einer beruflichen Ausbildung zu verbinden. Gleichzeitig gewinnen Sie Zugang zu motivierten Nachwuchstalenten und positionieren sich als engagierter Ausbildungsbetrieb.
            </p>
          </div>
          <div style="margin-top: 24px;">
            <a href="kontakt.html?thema=betrieb" class="btn-cta btn-cta-outline-light" data-slot="zg_firma_cta">
              <span>Als Ausbildungsbetrieb mitmachen</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SO FUNKTIONIERT DIE ZUSAMMENARBEIT (4 SCHRITTE AUS SEITE 5) -->
  <section class="section-wrap section-surface" id="zusammenarbeit-ablauf" data-section-id="zusammenarbeit-ablauf" data-section="zusammenarbeit-ablauf" data-section-label="So funktioniert die Zusammenarbeit (4 Schritte)">
    <div class="section-inner">
      <div class="section-header">
        <span class="section-kicker" data-slot="ablauf_kicker">DER WEG ZUR SPORTFREUNDLICHEN LEHRSTELLE</span>
        <h2 class="section-title" data-slot="ablauf_title">SO FUNKTIONIERT DIE ZUSAMMENARBEIT</h2>
        <p class="section-desc" data-slot="ablauf_desc">
          In vier klaren Schritten begleiten wir Ihr Unternehmen und die Spielerin von der ersten Idee bis zum erfolgreichen Lehrabschluss.
        </p>
      </div>

      <div class="timeline-list">
        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="step_1_badge">SCHRITT 01</span>
          </div>
          <h3 class="card-title" data-slot="step_1_title">1. Unternehmen kennenlernen</h3>
          <p class="card-text" data-slot="step_1_text">
            Wir besprechen Ihre Ausbildungsmöglichkeiten und die betrieblichen Rahmenbedingungen.
          </p>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="step_2_badge">SCHRITT 02</span>
          </div>
          <h3 class="card-title" data-slot="step_2_title">2. Möglichkeiten schaffen</h3>
          <p class="card-text" data-slot="step_2_text">
            Gemeinsam prüfen wir, wie sich Trainingszeiten und Ausbildung vereinbaren lassen.
          </p>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="step_3_badge">SCHRITT 03</span>
          </div>
          <h3 class="card-title" data-slot="step_3_title">3. Talente verbinden</h3>
          <p class="card-text" data-slot="step_3_text">
            Wir stellen den Kontakt zu passenden Spielerinnen her.
          </p>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="step_4_badge">SCHRITT 04</span>
          </div>
          <h3 class="card-title" data-slot="step_4_title">4. Gemeinsam begleiten</h3>
          <p class="card-text" data-slot="step_4_text">
            HER11 bleibt bei Bedarf Ansprechstelle für die Spielerin und den Ausbildungsbetrieb.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA BANNER: WERDEN SIE HER11-AUSBILDUNGSPARTNER (SEITE 5) -->
  <section class="section-wrap" id="ausbildungspartner-cta" data-section-id="ausbildungspartner-cta" data-section="ausbildungspartner-cta" data-section-label="Aufruf: Werden Sie HER11-Ausbildungspartner">
    <div class="section-inner">
      <div class="cta-banner-box">
        <div style="max-width: 680px;">
          <span class="section-kicker" data-slot="ap_cta_kicker">JEDER LEHRBETRIEB ZÄHLT</span>
          <h2 class="section-title" style="color: #FFFFFF; margin-bottom: 8px;" data-slot="ap_cta_title">WERDEN SIE HER11-AUSBILDUNGSPARTNER.</h2>
          <p style="font-size: 0.96rem; color: #CBD5E1; line-height: 1.6;" data-slot="ap_cta_text">
            Ob kleines, mittleres oder grosses Unternehmen: Jede sportfreundliche Lehrstelle kann einen entscheidenden Unterschied machen.
          </p>
        </div>
        <div>
          <a href="kontakt.html?thema=betrieb" class="btn-cta btn-cta-pink" data-slot="ap_cta_btn">
            <span>Jetzt Ausbildungsbetrieb werden</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
        </div>
      </div>
    </div>
  </section>
"""

# ==============================================================================
# 04 | BEGLEITUNG (begleitung.html — SEITE 6 REDAKTIONSKONZEPT)
# ==============================================================================
BEGLEITUNG_BODY = """
  <!-- HERO SECTION (04 | BEGLEITUNG) -->
  <section class="hero-wrap" id="begleitung-hero" data-section-id="begleitung-hero" data-section="begleitung-hero" data-section-label="04 | Begleitung: Du stehst im Mittelpunkt">
    <div class="hero-inner">
      <div>
        <span class="hero-kicker" data-slot="begl_hero_kicker">04 | BEGLEITUNG · GANZHEITLICHE FÖRDERUNG</span>
        <h1 class="hero-title" data-slot="begl_hero_title">DU STEHST IM <span>MITTELPUNKT.</span></h1>
        <div class="hero-subheadline" data-slot="begl_hero_sub">Wir begleiten dich. Auf und neben dem Platz.</div>
        <p class="hero-lead" data-slot="begl_hero_p1">
          Der Weg im Leistungssport ist voller Chancen, aber auch Herausforderungen. HER11 unterstützt junge Fussballerinnen und ihre Familien bei wichtigen Entscheidungen und hilft dabei, ein Umfeld zu schaffen, das ihre Entwicklung fördert. Dabei betrachten wir die Spielerin ganzheitlich.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html?thema=beratung" class="btn-cta btn-cta-pink" data-slot="begl_hero_cta1">
            <span>Erstgespräch anfragen</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
          <a href="ausbildung.html" class="btn-cta btn-cta-outline-light" data-slot="begl_hero_cta2">
            <span>Sportfreundliche Lehrstellen</span>
          </a>
        </div>
      </div>

      <div class="hero-visual-card">
        <img src="images/fokus-flutlicht-closeup.webp" alt="Fokus und mentale Stärke einer jungen Fussballerin im Flutlicht" class="hero-visual-img" data-slot="begl_hero_img">
        <div class="hero-visual-caption">
          <span style="font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif; font-variant-numeric: tabular-nums; font-weight: 700; color: #FF0066;" data-slot="begl_cap_tag">5 BEREICHE · 1 ZIEL</span>
          <span data-slot="begl_cap_text">Ganzheitliche Begleitung für Spielerin &amp; Familie.</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DIE 5 BEGLEITUNGS-BEREICHE (SEITE 6) -->
  <section class="section-wrap" id="begleitung-bereiche" data-section-id="begleitung-bereiche" data-section="begleitung-bereiche" data-section-label="Die 5 Bereiche unserer Begleitung">
    <div class="section-inner">
      <div class="section-header">
        <span class="section-kicker" data-slot="bb_kicker">RUNDUM GESTÄRKT DURCH DEINE ENTWICKLUNG</span>
        <h2 class="section-title" data-slot="bb_title">UNSERE 5 BEGLEITUNGS-BEREICHE</h2>
        <p class="section-desc" data-slot="bb_desc">
          Sportlicher Erfolg und persönliche Reife hängen eng zusammen. Deshalb betrachten wir deine Situation immer als Ganzes.
        </p>
      </div>

      <div class="begleitung-grid">
        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="12 7 16.5 10.5 14.8 16 9.2 16 7.5 10.5 12 7"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="bb_1_badge">BEREICH 01</span>
          </div>
          <h3 class="card-title" data-slot="bb_1_title">FUSSBALL</h3>
          <p class="card-text" data-slot="bb_1_text">
            Wir unterstützen dich bei Fragen zur Karriereplanung, Vereinswahl und persönlichen Entwicklung im Fussball.
          </p>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="bb_2_badge">BEREICH 02</span>
          </div>
          <h3 class="card-title" data-slot="bb_2_title">AUSBILDUNG &amp; BERUF</h3>
          <p class="card-text" data-slot="bb_2_text">
            Wir begleiten dich bei der Wahl eines Ausbildungswegs, der zu deinen sportlichen Zielen passt.
          </p>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="bb_3_badge">BEREICH 03</span>
          </div>
          <h3 class="card-title" data-slot="bb_3_title">GESUNDHEIT &amp; LEISTUNGSFÄHIGKEIT</h3>
          <p class="card-text" data-slot="bb_3_text">
            Wir helfen dir, bei Bedarf geeignete Fachpersonen für körperliche Entwicklung, Verletzungsprävention und Rehabilitation zu finden.
          </p>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a8 8 0 0 0-8 8c0 5.25 8 12 8 12s8-6.75 8-12a8 8 0 0 0-8-8z"/><circle cx="12" cy="10" r="3"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="bb_4_badge">BEREICH 04</span>
          </div>
          <h3 class="card-title" data-slot="bb_4_title">MENTALE STÄRKE</h3>
          <p class="card-text" data-slot="bb_4_text">
            Wir unterstützen dich bei Herausforderungen wie Leistungsdruck, Rückschlägen und Unsicherheiten und vermitteln bei Bedarf qualifizierte Fachpersonen.
          </p>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="bb_5_badge">BEREICH 05</span>
          </div>
          <h3 class="card-title" data-slot="bb_5_title">FAMILIE &amp; UMFELD</h3>
          <p class="card-text" data-slot="bb_5_text">
            Wir stehen auch Eltern als unabhängige Ansprechstelle zur Seite.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- DEIN WEG MIT HER11 (SEITE 6) -->
  <section class="section-wrap section-surface" id="dein-weg" data-section-id="dein-weg" data-section="dein-weg" data-section-label="Dein Weg mit HER11: Erstgespräch anfragen">
    <div class="section-inner">
      <div class="cta-banner-box">
        <div style="max-width: 680px;">
          <span class="section-kicker" data-slot="dw_kicker">PERSÖNLICH &amp; UNVERBINDLICH</span>
          <h2 class="section-title" style="color: #FFFFFF; margin-bottom: 10px;" data-slot="dw_title">DEIN WEG MIT HER11</h2>
          <p style="font-size: 0.96rem; color: #CBD5E1; line-height: 1.65;" data-slot="dw_text">
            Alles beginnt mit einem persönlichen Gespräch. Wir lernen dich, deine Ziele und deine aktuelle Situation kennen. Gemeinsam schauen wir, wo du Unterstützung benötigst und welche nächsten Schritte sinnvoll sind.
          </p>
        </div>
        <div>
          <a href="kontakt.html?thema=beratung" class="btn-cta btn-cta-pink" data-slot="dw_cta_btn">
            <span>Erstgespräch anfragen</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
        </div>
      </div>
    </div>
  </section>
"""

# ==============================================================================
# 05 | MACH MIT (mach-mit.html — SEITE 7 & 8 REDAKTIONSKONZEPT)
# ==============================================================================
MACH_MIT_BODY = """
  <!-- HERO SECTION (05 | MACH MIT) -->
  <section class="hero-wrap" id="machmit-hero" data-section-id="machmit-hero" data-section="machmit-hero" data-section-label="05 | Mach mit: Gemeinsam schaffen wir Chancen">
    <div class="hero-inner">
      <div>
        <span class="hero-kicker" data-slot="mm_hero_kicker">05 | MACH MIT · ENGAGEMENT MIT WIRKUNG</span>
        <h1 class="hero-title" data-slot="mm_hero_title">GEMEINSAM SCHAFFEN WIR <span>CHANCEN.</span></h1>
        <div class="hero-subheadline" data-slot="mm_hero_sub">Die Zukunft des Frauenfussballs gestalten wir gemeinsam.</div>
        <p class="hero-lead" data-slot="mm_hero_p1">
          Talent allein reicht nicht immer aus. Junge Fussballerinnen brauchen Menschen und Unternehmen, die an sie glauben und bereit sind, sie auf ihrem Weg zu unterstützen. HER11 möchte ein starkes Netzwerk aufbauen, das jungen Frauen neue Möglichkeiten eröffnet.
        </p>
        <div class="hero-actions">
          <a href="kontakt.html?thema=betrieb" class="btn-cta btn-cta-pink" data-slot="mm_hero_cta1">
            <span>Ausbildungsbetrieb werden</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
          <a href="kontakt.html?thema=sponsor" class="btn-cta btn-cta-outline-light" data-slot="mm_hero_cta2">
            <span>Sponsor werden</span>
          </a>
        </div>
      </div>

      <div class="hero-visual-card">
        <img src="images/social-gemeinsam-team11.webp" alt="Vier HER11 Spielerinnen Arm in Arm vor dem Stadion" class="hero-visual-img" data-slot="mm_hero_img">
        <div class="hero-visual-caption">
          <span style="font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif; font-variant-numeric: tabular-nums; font-weight: 700; color: #FF0066;" data-slot="mm_cap_tag">3 WEGE ZUM MITMACHEN</span>
          <span data-slot="mm_cap_text">Ausbildungspartner · Sponsor · Netzwerkpartner</span>
        </div>
      </div>
    </div>
  </section>

  <!-- 01 – AUSBILDUNGSPARTNER WERDEN (SEITE 7) -->
  <section class="section-wrap" id="saeule-ausbildungspartner" data-section-id="saeule-ausbildungspartner" data-section="saeule-ausbildungspartner" data-section-label="01 – Ausbildungspartner werden">
    <div class="section-inner">
      <div class="split-grid">
        <div class="split-col-card">
          <div>
            <span class="section-kicker" data-slot="mm_s1_kicker">WEG 01 · SPORTFREUNDLICHE LEHRSTELLE</span>
            <h2 class="section-title" data-slot="mm_s1_title">01 – AUSBILDUNGSPARTNER WERDEN</h2>
            <p class="section-desc" style="margin-top: 12px;" data-slot="mm_s1_text">
              Ermöglichen Sie eine sportfreundliche Lehrstelle. Sie bilden Lernende aus und möchten jungen Fussballerinnen eine Chance geben? Werden Sie Teil unseres Netzwerks von Ausbildungsbetrieben. Gemeinsam entwickeln wir Lösungen, die eine qualifizierte Berufsausbildung mit den Anforderungen des Leistungssports verbinden. Ihr Engagement schafft konkrete Perspektiven.
            </p>
          </div>
          <div style="margin-top: 24px;">
            <a href="kontakt.html?thema=betrieb" class="btn-cta btn-cta-pink" data-slot="mm_s1_cta">
              <span>Ausbildungsbetrieb werden</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </a>
          </div>
        </div>

        <div class="split-col-card" style="padding: 12px;">
          <img src="images/perspektive-alpen-see.webp" alt="Spielerin mit HER11 Rucksack über See und Alpen" class="split-media-img" style="height: 100%; min-height: 260px;" data-slot="mm_s1_img">
        </div>
      </div>
    </div>
  </section>

  <!-- 02 – SPONSOR WERDEN & 4 FÖRDERBEREICHE (SEITE 7 & 8) -->
  <section class="section-wrap section-dark" id="saeule-sponsor" data-section-id="saeule-sponsor" data-section="saeule-sponsor" data-section-label="02 – Sponsor werden &amp; 4 Förderbereiche">
    <div class="section-inner">
      <div class="section-header">
        <span class="section-kicker" data-slot="mm_s2_kicker">WEG 02 · ZUKUNFT FÖRDERN</span>
        <h2 class="section-title" data-slot="mm_s2_title">02 – SPONSOR WERDEN</h2>
        <div class="section-subtitle" data-slot="mm_s2_sub">UNTERSTÜTZEN SIE IHREN WEG.</div>
        <p class="section-desc" data-slot="mm_s2_desc">
          Investieren Sie nicht nur in den Fussball. Investieren Sie in die Zukunft junger Frauen. Mit Ihrem Engagement unterstützen Sie HER11 dabei, ambitionierten Fussballerinnen bessere Rahmenbedingungen für ihre sportliche und persönliche Entwicklung zu ermöglichen. Als Sponsor tragen Sie dazu bei, Chancen zu schaffen und bestehende Hürden abzubauen.
        </p>
      </div>

      <div style="margin-bottom: 18px;">
        <span class="section-kicker" data-slot="mm_foerder_kicker">IHR ENGAGEMENT KANN VIEL BEWEGEN.</span>
      </div>

      <div class="foerder-grid" style="margin-bottom: 32px;">
        <div class="her-card-dark">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="fb_1_badge">FÖRDERBEREICH 01</span>
          </div>
          <h3 class="card-title" data-slot="fb_1_title">AUSBILDUNG &amp; ZUKUNFT</h3>
          <p class="card-text" data-slot="fb_1_text">
            Unterstützen Sie unsere Arbeit beim Aufbau eines Netzwerks sportfreundlicher Ausbildungsbetriebe.
          </p>
        </div>

        <div class="her-card-dark">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="fb_2_badge">FÖRDERBEREICH 02</span>
          </div>
          <h3 class="card-title" data-slot="fb_2_title">TALENTFÖRDERUNG</h3>
          <p class="card-text" data-slot="fb_2_text">
            Helfen Sie mit, jungen Spielerinnen den Zugang zu individueller Beratung und Entwicklungsbegleitung zu ermöglichen.
          </p>
        </div>

        <div class="her-card-dark">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="fb_3_badge">FÖRDERBEREICH 03</span>
          </div>
          <h3 class="card-title" data-slot="fb_3_title">GESUNDHEIT &amp; ENTWICKLUNG</h3>
          <p class="card-text" data-slot="fb_3_text">
            Fördern Sie Angebote in den Bereichen Prävention, körperliche Entwicklung und mentale Gesundheit.
          </p>
        </div>

        <div class="her-card-dark">
          <div class="card-top-row">
            <span class="icon-box-pink">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </span>
            <span class="card-tag-badge" data-slot="fb_4_badge">FÖRDERBEREICH 04</span>
          </div>
          <h3 class="card-title" data-slot="fb_4_title">CHANCENGLEICHHEIT</h3>
          <p class="card-text" data-slot="fb_4_text">
            Tragen Sie dazu bei, dass junge Fussballerinnen unabhängig von ihren finanziellen oder familiären Voraussetzungen Unterstützung erhalten können.
          </p>
        </div>
      </div>

      <!-- PARTNERSCHAFT MIT WIRKUNG (SEITE 8) -->
      <div class="her-card-pink-callout">
        <span class="section-kicker" data-slot="pmw_kicker">MEHR ALS REINE LOGO-PRÄSENZ</span>
        <h3 class="card-title" style="font-size: 1.35rem;" data-slot="pmw_title">PARTNERSCHAFT MIT WIRKUNG</h3>
        <p class="card-text" style="font-size: 0.95rem;" data-slot="pmw_p1">
          Wir möchten Partnerschaften aufbauen, die mehr bewirken als reine Logo-Präsenz. Gemeinsam mit unseren Sponsoren möchten wir konkrete Projekte und Fördermöglichkeiten entwickeln. Ob als langfristiger HER11-Partner, Förderpartner für ein bestimmtes Thema oder Unterstützer einzelner Spielerinnen: Wir suchen Unternehmen, die unsere Vision teilen.
        </p>
        <p class="card-text" style="font-size: 0.95rem; margin-top: 6px;" data-slot="pmw_p2">
          Mit einer Partnerschaft bei HER11 engagieren Sie sich für die Förderung des Mädchen- und Frauenfussballs, Chancengleichheit, die Vereinbarkeit von Leistungssport und Berufsbildung, nachhaltige Nachwuchsförderung und konkrete Zukunftsperspektiven.
        </p>
        <div style="margin-top: 14px;">
          <a href="kontakt.html?thema=sponsor" class="btn-cta btn-cta-pink" data-slot="pmw_cta">
            <span>Sponsor werden</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- 03 – NETZWERKPARTNER WERDEN (SEITE 8) -->
  <section class="section-wrap section-surface" id="saeule-netzwerkpartner" data-section-id="saeule-netzwerkpartner" data-section="saeule-netzwerkpartner" data-section-label="03 – Netzwerkpartner werden">
    <div class="section-inner">
      <div class="split-grid">
        <div class="split-col-card" style="background: var(--white);">
          <div>
            <span class="section-kicker" data-slot="mm_s3_kicker">WEG 03 · KOMPETENZ &amp; FACHWISSEN</span>
            <h2 class="section-title" data-slot="mm_s3_title">03 – NETZWERKPARTNER WERDEN</h2>
            <p class="section-desc" style="margin-top: 12px;" data-slot="mm_s3_text">
              Gemeinsam sind wir stärker. HER11 setzt auf ein Netzwerk kompetenter Fachpersonen und Organisationen. Wir suchen Partner aus den Bereichen Sportmedizin, Physiotherapie, Athletik, Mentaltraining, Bildung und Berufsberatung. Sie möchten Ihr Wissen und Ihre Erfahrung einbringen?
            </p>
          </div>
          <div style="margin-top: 24px;">
            <a href="kontakt.html?thema=netzwerk" class="btn-cta btn-cta-navy" data-slot="mm_s3_cta">
              <span>Netzwerkpartner werden</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </a>
          </div>
        </div>

        <div class="split-col-card" style="padding: 12px; background: var(--white);">
          <img src="images/fokus-flutlicht-closeup.webp" alt="Fokus und professionelle Begleitung im Frauenfussball" class="split-media-img" style="height: 100%; min-height: 260px;" data-slot="mm_s3_img">
        </div>
      </div>
    </div>
  </section>


  <!-- WACHSENDE SPONSOREN- & PARTNER-ÜBERSICHT AUF MACH-MIT.HTML -->
  <section class="section-wrap" id="sponsoren-showcase" data-section-id="sponsoren-showcase" data-section="sponsoren-showcase" data-section-label="Wachsende Sponsoren- &amp; Partner-Übersicht">
    <div class="section-inner">
      <div class="section-header">
        <span class="section-kicker" data-slot="mm_show_kicker">UNSERE PARTNER, SPONSOREN &amp; LEHRBETRIEBE</span>
        <h2 class="section-title" data-slot="mm_show_title">ENGAGIERTE WEGBEGLEITER IM HER11-NETZWERK.</h2>
        <p class="section-desc" data-slot="mm_show_desc">
          Hier machen wir Unternehmen, Sponsoren, Ausbildungsbetriebe und Fachpartner sichtbar, die gemeinsam mit HER11 Perspektiven für junge Fussballerinnen schaffen.
        </p>
      </div>

      <div class="partner-grid">
        <div class="her-card">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="mm_sp_1_badge">AUSBILDUNGSPARTNER · 01</span>
          </div>
          <h3 class="card-title" data-slot="mm_sp_1_title">Pionier-Ausbildungsbetriebe</h3>
          <p class="card-text" data-slot="mm_sp_1_text">
            Lehrbetriebe, die jungen Fussballerinnen durch flexible Arbeitszeiten und abgestimmte Trainingsfenster eine vollwertige Berufsausbildung ermöglichen.
          </p>
          <a href="kontakt.html?thema=betrieb" class="card-link" data-slot="mm_sp_1_link">
            <span>Betrieb hier eintragen lassen</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="mm_sp_2_badge">SPONSORING · 02</span>
          </div>
          <h3 class="card-title" data-slot="mm_sp_2_title">Offizielle HER11-Sponsoren</h3>
          <p class="card-text" data-slot="mm_sp_2_text">
            Unternehmen und Förderpartner, die gezielt in Talentförderung, Ausbildungsnetzwerke, Gesundheit und Chancengleichheit investieren.
          </p>
          <a href="kontakt.html?thema=sponsor" class="card-link" data-slot="mm_sp_2_link">
            <span>Sponsor-Profil anfragen</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="mm_sp_3_badge">NETZWERKPARTNER · 03</span>
          </div>
          <h3 class="card-title" data-slot="mm_sp_3_title">Fachpersonen &amp; Spezialisten</h3>
          <p class="card-text" data-slot="mm_sp_3_text">
            Kompetenzpartner aus Sportmedizin, Physiotherapie, Athletik, Mentaltraining, Bildung und Berufsberatung für eine ganzheitliche Begleitung.
          </p>
          <a href="kontakt.html?thema=netzwerk" class="card-link" data-slot="mm_sp_3_link">
            <span>Als Fachpartner beitreten</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>

        <div class="her-card-pink-callout">
          <div class="card-top-row">
            <span class="card-tag-badge" data-slot="mm_sp_4_badge">FREIER PARTNER-SLOT</span>
          </div>
          <h3 class="card-title" data-slot="mm_sp_4_title">Ihr Logo &amp; Engagement an dieser Stelle</h3>
          <p class="card-text" data-slot="mm_sp_4_text">
            Jeder neue Partner wird im HER11-Netzwerk auf der Startseite und unter «Mach mit» sichtbar präsentiert. Lassen Sie uns ins Gespräch kommen.
          </p>
          <a href="kontakt.html" class="card-link" style="color: #FFD6E6;" data-slot="mm_sp_4_link">
            <span>Jetzt Gespräch vereinbaren</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- SEIEN SIE TEIL IHRER GESCHICHTE (SEITE 8 ABSCHLUSS-CTA) -->
  <section class="section-wrap" id="machmit-cta" data-section-id="machmit-cta" data-section="machmit-cta" data-section-label="Aufruf: Seien Sie Teil ihrer Geschichte">
    <div class="section-inner">
      <div class="cta-banner-box">
        <div style="max-width: 680px;">
          <span class="section-kicker" data-slot="mm_final_kicker">JEDE GROSSE KARRIERE BEGINNT MIT EINER CHANCE</span>
          <h2 class="section-title" style="color: #FFFFFF; margin-bottom: 10px;" data-slot="mm_final_title">SEIEN SIE TEIL IHRER GESCHICHTE.</h2>
          <p style="font-size: 0.96rem; color: #CBD5E1; line-height: 1.65;" data-slot="mm_final_text">
            Jede grosse Karriere beginnt mit einer Chance. Gemeinsam können wir dafür sorgen, dass junge Fussballerinnen die Unterstützung erhalten, die sie auf ihrem Weg benötigen.
          </p>
        </div>
        <div>
          <a href="kontakt.html" class="btn-cta btn-cta-pink" data-slot="mm_final_btn">
            <span>Jetzt mitmachen</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
        </div>
      </div>
    </div>
  </section>
"""

# ==============================================================================
# 06 | KONTAKT (kontakt.html — SEITE 9 REDAKTIONSKONZEPT)
# ==============================================================================
KONTAKT_BODY = r"""
  <!-- HERO SECTION (06 | KONTAKT) -->
  <section class="hero-wrap" id="kontakt-hero" data-section-id="kontakt-hero" data-section="kontakt-hero" data-section-label="06 | Kontakt: Lass uns gemeinsam etwas bewegen">
    <div class="hero-inner">
      <div>
        <span class="hero-kicker" data-slot="kon_hero_kicker">06 | KONTAKT · PERSÖNLICHE ANLAUFSTELLE</span>
        <h1 class="hero-title" data-slot="kon_hero_title">LASS UNS GEMEINSAM <span>ETWAS BEWEGEN.</span></h1>
        <p class="hero-lead" data-slot="kon_hero_p1">
          Wir freuen uns auf deine Nachricht. Du bist Spielerin und suchst Unterstützung? Sie möchten als Unternehmen sportfreundliche Lehrstellen anbieten? Oder interessieren Sie sich für eine Partnerschaft mit HER11? Wir freuen uns darauf, Sie kennenzulernen.
        </p>
        <div class="hero-badges-row">
          <span class="meta-badge-dark" data-slot="kon_badge_1">info@her11.ch</span>
          <span class="meta-badge-dark" data-slot="kon_badge_2">www.her11.ch</span>
          <span class="meta-badge-dark" data-slot="kon_badge_3">Persönlich &amp; Unabhängig</span>
        </div>
      </div>

      <div class="hero-visual-card">
        <img src="images/hero-stadion-11.webp" alt="HER11 Spielerin im Stadion" class="hero-visual-img" style="height: 250px;" data-slot="kon_hero_img">
        <div class="hero-visual-caption">
          <span style="font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif; font-variant-numeric: tabular-nums; font-weight: 700; color: #FF0066;" data-slot="kon_cap_tag">DIREKTER DRAHT</span>
          <span data-slot="kon_cap_text">Wir melden uns persönlich bei dir / Ihnen.</span>
        </div>
      </div>
    </div>
  </section>

  <!-- KONTAKTFORMULAR & DIREKTER KONTAKT (SEITE 9 — 3-SCHRITTE SMART-ANFRAGE) -->
  <section class="section-wrap" id="kontaktformular" data-section-id="kontaktformular" data-section="kontaktformular" data-section-label="Kontaktformular &amp; Direkter Kontakt">
    <div class="section-inner">
      <div class="split-grid">
        <div class="her-card" style="padding: 24px 20px; overflow-x: hidden; box-sizing: border-box;">
          <div class="wp-wizard-top">
            <span class="wp-step-indicator" id="wpStepLabel" data-slot="form_kicker">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
              <span>Schritt 1/3: Rolle &amp; Thema</span>
            </span>
            <div class="wp-nav-mini-group">
              <button type="button" class="wp-btn-mini" id="wpBtnBackTop" onclick="wpPrevStep()" style="display:none;">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="15 18 9 12 15 6"/></svg>
                <span>Zurück</span>
              </button>
              <button type="button" class="wp-btn-mini" id="wpBtnResetTop" onclick="wpResetWizard()">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/></svg>
                <span>Neu starten</span>
              </button>
            </div>
          </div>

          <div class="wp-progress-track" aria-hidden="true">
            <div class="wp-progress-seg active" id="wpProg1"></div>
            <div class="wp-progress-seg" id="wpProg2"></div>
            <div class="wp-progress-seg" id="wpProg3"></div>
          </div>

          <h2 class="section-title" style="font-size: 1.38rem;" data-slot="form_title">WIE KÖNNEN WIR HELFEN?</h2>
          <p class="section-desc" style="margin-bottom: 16px;" data-slot="form_desc">
            Wähle deine Rolle — wir erstellen in Echtzeit dein persönliches 1-Seiten-Anfrage-Dossier für Jenny Ettle &amp; Ramona Bachmann:
          </p>

          <form id="her11ContactForm" class="form-grid" onsubmit="return wpSubmitHer11Lead(event)" novalidate>
            <input type="text" name="website_url" id="wpHoneypot" value="" style="display:none !important;" tabindex="-1" autocomplete="off">

            <!-- SCHRITT 1: 2x3 ROLLEN-KACHELN -->
            <div class="wp-step-pane active" id="wpStep1">
              <div class="wp-role-grid" id="wpRoleGrid" role="group" aria-label="Themenauswahl">
                <button type="button" class="wp-role-tile selected" data-topic="Ausbildung als Spielerin" onclick="wpSelectHer11Topic('Ausbildung als Spielerin')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_1">Ausbildung als Spielerin</span>
                  </div>
                  <span class="wp-role-desc">Sportfreundliche Lehre, KV oder Schule passend zum Trainingsalltag finden</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Beratung und Begleitung" onclick="wpSelectHer11Topic('Beratung und Begleitung')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_2">Beratung und Begleitung</span>
                  </div>
                  <span class="wp-role-desc">360°-Mentoring: Karriereplanung, Athletik, Mentaltraining &amp; Vorsorge</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Ausbildungsbetrieb werden" onclick="wpSelectHer11Topic('Ausbildungsbetrieb werden')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_3">Ausbildungsbetrieb werden</span>
                  </div>
                  <span class="wp-role-desc">Als KMU oder Unternehmen motivierte Nachwuchs-Fussballerinnen ausbilden</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Sponsoring / Partnerschaft" onclick="wpSelectHer11Topic('Sponsoring / Partnerschaft')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_4">Sponsoring / Partnerschaft</span>
                  </div>
                  <span class="wp-role-desc">Sichtbares Engagement für Chancengleichheit im Schweizer Frauenfussball</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Netzwerkpartner werden" onclick="wpSelectHer11Topic('Netzwerkpartner werden')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_5">Netzwerkpartner werden</span>
                  </div>
                  <span class="wp-role-desc">Kooperation für Schulen, Vereine, Verbände &amp; Fachexpertinnen</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Allgemeine Anfrage" onclick="wpSelectHer11Topic('Allgemeine Anfrage')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_6">Allgemeine Anfrage</span>
                  </div>
                  <span class="wp-role-desc">Medien, Keynotes, Events oder persönlicher Austausch mit HER11</span>
                </button>
              </div>

              <button type="button" class="btn-cta btn-cta-pink" style="width: 100%;" onclick="wpNextStep(2)">
                <span>Weiter zu Schritt 2: Details &amp; Unterlagen</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
              </button>
            </div>

            <!-- SCHRITT 2: DYNAMISCHE ROLLEN-DETAILS & FOTO-UPLOAD -->
            <div class="wp-step-pane" id="wpStep2">
              <div class="form-grid-2" style="margin-bottom: 14px;">
                <div class="form-field">
                  <label for="wpDetail1" class="form-label" id="wpDetail1Label">Jahrgang &amp; Aktueller Verein</label>
                  <input type="text" id="wpDetail1" class="form-input" placeholder="z. B. Jg. 2009 · FC Luzern Frauen U17">
                </div>
                <div class="form-field">
                  <label for="wpDetail2" class="form-label" id="wpDetail2Label">Wunsch-Ausbildung / Profil</label>
                  <input type="text" id="wpDetail2" class="form-input" placeholder="z. B. Kauffrau EFZ / Sportgymnasium">
                </div>
              </div>

              <div class="form-field" style="margin-bottom: 14px;">
                <label class="form-label">Gewünschter Zeithorizont / Dringlichkeit</label>
                <div class="wp-role-grid" id="wpUrgencyGrid" style="margin-bottom: 0;">
                  <button type="button" class="wp-role-tile" data-urg="Diese Woche" onclick="wpSelectHer11Urgency('Diese Woche')">
                    <span class="wp-role-title">Diese Woche</span>
                    <span class="wp-role-desc">Zeitnahes Kennenlerngespräch</span>
                  </button>
                  <button type="button" class="wp-role-tile selected" data-urg="Planbar / Nach Absprache" onclick="wpSelectHer11Urgency('Planbar / Nach Absprache')">
                    <span class="wp-role-title">Planbar / Nach Absprache</span>
                    <span class="wp-role-desc">Reguläre Terminabstimmung</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urg="Kommendes Lehrjahr / Saison" onclick="wpSelectHer11Urgency('Kommendes Lehrjahr / Saison')">
                    <span class="wp-role-title">Kommendes Lehrjahr / Saison</span>
                    <span class="wp-role-desc">Frühzeitige Planung &amp; Aufbau</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urg="Heute (Dringend)" onclick="wpSelectHer11Urgency('Heute (Dringend)')">
                    <span class="wp-role-title">Dringende Rückfrage</span>
                    <span class="wp-role-desc">Rasche Rückmeldung erwünscht</span>
                  </button>
                </div>
              </div>

              <div class="form-field" style="margin-bottom: 14px;">
                <label for="contactMessage" class="form-label" data-slot="lbl_message">Persönliche Nachricht / Anliegen *</label>
                <textarea id="contactMessage" name="message" class="form-textarea" placeholder="Wie können wir dich oder Ihr Unternehmen unterstützen?" required></textarea>
              </div>

              <div class="form-field" style="margin-bottom: 18px;">
                <label class="form-label">Fotos oder Impressionen beifügen (optional, max. 3 Bilder für PDF-Dossier)</label>
                <div class="wp-upload-zone">
                  <input type="file" id="wpPhotoInput" accept="image/*" multiple style="display:none;" onchange="wpHandlePhotoFiles(this.files)">
                  <button type="button" class="wp-upload-btn" onclick="wpTriggerPhotoUpload()">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
                    <span>Bild auswählen (Spielerinnen-Porträt, Verein oder Ausbildungsbetrieb)</span>
                  </button>
                  <div style="font-size:0.74rem;color:var(--text-muted);margin-top:6px;" id="wpPhotoCounter">0 / 3 Bilder ausgewählt · Automatisch für 1-Seiten-PDF optimiert</div>
                  <div class="wp-photo-thumbs" id="wpPhotoThumbs"></div>
                </div>
              </div>

              <div class="form-grid-2">
                <button type="button" class="btn-cta btn-cta-navy" style="width: 100%;" onclick="wpPrevStep()">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="15 18 9 12 15 6"/></svg>
                  <span>Zurück zu Schritt 1</span>
                </button>
                <button type="button" class="btn-cta btn-cta-pink" style="width: 100%;" onclick="wpNextStep(3)">
                  <span>Weiter zu Schritt 3: Kontakt</span>
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
                </button>
              </div>
            </div>

            <!-- SCHRITT 3: KONTAKT, PLZ & LIVE-DEMO SELBSTTEST -->
            <div class="wp-step-pane" id="wpStep3">
              <div class="form-grid-2" style="margin-bottom: 12px;">
                <div class="form-field">
                  <label for="contactName" class="form-label" data-slot="lbl_name">Vorname / Nachname *</label>
                  <input type="text" id="contactName" name="name" class="form-input" placeholder="Dein Vor- und Nachname" required>
                </div>
                <div class="form-field">
                  <label for="contactCompany" class="form-label" data-slot="lbl_company">Unternehmen / Verein (optional)</label>
                  <input type="text" id="contactCompany" name="company" class="form-input" placeholder="Firma, Organisation oder Verein">
                </div>
              </div>

              <div class="form-grid-2" style="margin-bottom: 8px;">
                <div class="form-field">
                  <label for="contactLoc" class="form-label">PLZ &amp; Ort / Region *</label>
                  <input type="text" id="contactLoc" name="plz" class="form-input" placeholder="z. B. 6003 Luzern oder 8001 Zürich" oninput="wpCheckHer11Plz(this.value)" required>
                </div>
                <div class="form-field">
                  <label for="contactStreet" class="form-label">Strasse &amp; Nr. (optional)</label>
                  <input type="text" id="contactStreet" name="street" class="form-input" placeholder="Für Standort-QR-Code im Dossier">
                </div>
              </div>

              <div style="margin-bottom: 12px;">
                <div class="wp-plz-badge" id="wpPlzBadge">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
                  <span id="wpPlzBadgeText">Schweizweites HER11 Netzwerk aktiv</span>
                </div>
              </div>

              <div class="form-grid-2" style="margin-bottom: 12px;">
                <div class="form-field">
                  <label for="contactEmail" class="form-label" data-slot="lbl_email">E-Mail-Adresse (für PDF-Dossier) *</label>
                  <input type="email" id="contactEmail" name="email" class="form-input" placeholder="name@beispiel.ch" required>
                </div>
                <div class="form-field">
                  <label for="contactPhone" class="form-label" data-slot="lbl_phone">Mobiltelefon (für Rückruf &amp; WhatsApp) *</label>
                  <input type="tel" id="contactPhone" name="phone" class="form-input" placeholder="+41 79 000 00 00" required>
                </div>
              </div>

              <div class="consent-row" style="margin-bottom: 12px;">
                <input type="checkbox" id="contactConsent" name="consent" class="consent-checkbox" checked required aria-label="Einwilligung zur Datenbearbeitung">
                <label for="contactConsent" style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.45; cursor: pointer;" data-slot="lbl_consent">
                  <strong>Einwilligung zur Datenbearbeitung (nDSG):</strong> Ich bin damit einverstanden, dass meine Angaben zur persönlichen Beantwortung meiner Anfrage durch HER11 bearbeitet werden.
                </label>
              </div>

              <div class="wp-demo-banner" style="margin-bottom: 14px;">
                <div style="font-weight:800;display:flex;align-items:center;gap:6px;margin-bottom:3px;color:var(--pink);">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                  <span>Live-Demo aktiv (Selbsttest-Modus):</span>
                </div>
                <div>
                  Gib deine eigene E-Mail und Handynummer ein — du erhältst nach dem Absenden sofort das echte <strong>1-Seiten-PDF-Dossier im HER11-Design</strong> inklusive QR-Codes sowie den WhatsApp-Ping direkt auf dein Handy!
                </div>
              </div>

              <div id="wpFormError" style="display:none;padding:10px 12px;border-radius:8px;background:#FEF2F2;border:1px solid #EF4444;color:#991B1B;font-size:0.82rem;font-weight:700;margin-bottom:12px;"></div>

              <div class="form-grid-2">
                <button type="button" class="btn-cta btn-cta-navy" style="width: 100%;" onclick="wpPrevStep()">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="15 18 9 12 15 6"/></svg>
                  <span>Zurück zu Schritt 2</span>
                </button>
                <button type="submit" class="btn-cta btn-cta-pink" id="wpSubmitBtn" style="width: 100%;" data-slot="form_submit_btn">
                  <span id="wpSubmitBtnText">1-Seiten-Dossier &amp; Anfrage senden</span>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                </button>
              </div>
            </div>
          </form>

          <!-- ERFOLGS-COCKPIT NACH ABSENDEN -->
          <div class="wp-success-box" id="wpSuccessBox">
            <div style="display:flex;align-items:center;gap:8px;color:var(--navy);font-weight:800;font-size:1.02rem;margin-bottom:8px;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FF0066" stroke-width="2.4"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
              <span>Deine HER11 Smart-Anfrage ist eingegangen!</span>
            </div>
            <p style="font-size:0.85rem;color:var(--text-dark);line-height:1.5;margin-bottom:14px;">
              Dein strukturiertes 1-Seiten-Anfrage-Dossier wurde in Echtzeit generiert und an das HER11-Team übermittelt.
            </p>
            <div style="background:var(--white);border:1px solid var(--border-light);border-radius:8px;padding:12px 14px;margin-bottom:14px;font-size:0.84rem;line-height:1.65;">
              <div><strong>Referenz-Nummer:</strong> <span id="wpResRef" style="color:var(--pink);font-weight:800;">#WP-2026-0000</span></div>
              <div><strong>Zuständig bei HER11:</strong> <span id="wpResAssigned" style="font-weight:700;">Jenny Ettle &amp; Ramona Bachmann</span></div>
              <div><strong>Verbindliche Rückmeldung:</strong> <span id="wpResCallback" style="color:#047857;font-weight:700;">Zeitnahe Rückmeldung</span></div>
              <div><strong>Dual-Delivery Status:</strong> <span id="wpResChannels">1-Seiten-PDF erstellt · E-Mail &amp; WhatsApp ausgelöst</span></div>
            </div>

            <a href="#" target="_blank" rel="noopener" id="wpResPdfBtn" class="btn-cta btn-cta-pink" style="width:100%;margin-bottom:14px;text-decoration:none;">
              <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
              <span>1-Seiten-PDF-Dossier (HER11 Anfrage-Blatt) öffnen</span>
            </a>

            <div style="font-size:0.76rem;font-weight:800;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.04em;">
              Übermittelte WhatsApp-Sofortmeldung an HER11:
            </div>
            <div class="wp-wa-preview" id="wpResWaPreview"></div>

            <button type="button" class="wp-btn-mini" style="margin-top:14px;" onclick="wpResetWizard()">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/></svg>
              <span>Weitere Anfrage erfassen</span>
            </button>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 20px;">
          <div class="her-card-dark" style="height: auto;">
            <span class="section-kicker" data-slot="dir_kicker">DIREKTER KONTAKT</span>
            <h3 class="card-title" style="font-size: 1.3rem;" data-slot="dir_title">PERSÖNLICH ERREICHBAR</h3>
            <p class="card-text" data-slot="dir_desc">
              Du kannst uns jederzeit auch direkt per E-Mail kontaktieren. Wir melden uns zeitnah und persönlich bei dir zurück.
            </p>
            <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 12px;">
              <a href="mailto:info@her11.ch" class="btn-cta btn-cta-pink" style="justify-content: flex-start;" data-slot="dir_email_btn">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
                <span>E-Mail: info@her11.ch</span>
              </a>
              <a href="https://www.her11.ch" target="_blank" rel="noopener" class="btn-cta btn-cta-outline-light" style="justify-content: flex-start;" data-slot="dir_web_btn">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                <span>Webseite: www.her11.ch</span>
              </a>
            </div>
          </div>

          <div class="her-card" style="height: auto;">
            <span class="section-kicker" data-slot="orient_kicker">ORIENTIERUNG</span>
            <h3 class="card-title" data-slot="orient_title">FÜR WEN IST HER11 DA?</h3>
            <p class="card-text" data-slot="orient_text">
              <strong>Spielerinnen &amp; Eltern:</strong> Unabhängige Begleitung bei Ausbildungswahl, Sportschulen, Karriereplanung und Gesundheit.<br><br>
              <strong>Ausbildungsbetriebe &amp; KMU:</strong> Unterstützung bei der Einrichtung sportfreundlicher Lehrstellen und Vermittlung motivierter Talente.<br><br>
              <strong>Sponsoren &amp; Fachpartner:</strong> Sinnstiftende Partnerschaften für Chancengleichheit im Frauenfussball.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- IMPRESSUM & DATENSCHUTZ -->
  <section class="section-wrap section-surface" id="impressum-datenschutz" data-section-id="impressum-datenschutz" data-section="impressum-datenschutz" data-section-label="Impressum &amp; Datenschutz">
    <div class="section-inner">
      <div class="split-grid">
        <div class="her-card">
          <span class="section-kicker" data-slot="imp_kicker">RECHTLICHES</span>
          <h3 class="card-title" data-slot="imp_title">IMPRESSUM</h3>
          <p class="card-text" data-slot="imp_text">
            <strong>HER11 — Ihr Weg. Ihr Spiel. Ihre Zukunft.</strong><br>
            Ausbildung &amp; Karrierebegleitung für junge Fussballerinnen<br>
            Schweiz<br>
            E-Mail: info@her11.ch<br>
            Webseite: www.her11.ch
          </p>
        </div>

        <div class="her-card">
          <span class="section-kicker" data-slot="ds_kicker">SCHWEIZER DATENSCHUTZ (nDSG)</span>
          <h3 class="card-title" data-slot="ds_title">DATENSCHUTZ</h3>
          <p class="card-text" data-slot="ds_text">
            Der Schutz deiner persönlichen Daten ist uns ein zentrales Anliegen. Alle über das Kontaktformular oder per E-Mail übermittelten Angaben werden vertraulich und ausschliesslich zur persönlichen Beantwortung deiner Anfrage gemäss Schweizer Datenschutzgesetz (nDSG) bearbeitet und niemals ohne Rücksprache an Dritte weitergegeben.
          </p>
        </div>
      </div>
    </div>
  </section>

  <script>
    var wpHer11State = {
      step: 1,
      topic: 'Ausbildung als Spielerin',
      urgency: 'Planbar / Nach Absprache',
      photos: []
    };

    var wpHer11StepTitles = {
      1: 'Schritt 1/3: Rolle & Thema',
      2: 'Schritt 2/3: Details & Unterlagen',
      3: 'Schritt 3/3: Kontakt & Dossier-Versand'
    };

    var wpHer11RoleConfig = {
      'Ausbildung als Spielerin': {
        l1: 'Jahrgang & Aktueller Verein',
        p1: 'z. B. Jg. 2009 · FC Luzern Frauen U17',
        l2: 'Wunsch-Ausbildung / Schulprofil',
        p2: 'z. B. Kauffrau EFZ / Sportgymnasium'
      },
      'Beratung und Begleitung': {
        l1: 'Schwerpunkt der 360°-Begleitung',
        p1: 'z. B. Karriereplanung, Mentaltraining, Athletik',
        l2: 'Aktueller Verein / Kaderstufe',
        p2: 'z. B. NLA / U19-Auswahl'
      },
      'Ausbildungsbetrieb werden': {
        l1: 'Branche & Unternehmensgrösse',
        p1: 'z. B. Treuhand, IT, Gesundheit (25 Mitarbeitende)',
        l2: 'Mögliche Lehrberufe & Startjahr',
        p2: 'z. B. Kauffrau EFZ ab Sommer 2027'
      },
      'Sponsoring / Partnerschaft': {
        l1: 'Gewünschte Partnerschafts-Form',
        p1: 'z. B. Hauptpartner, Förderpartner, Ausbildungs-Pate',
        l2: 'Fokus / Zielsetzung Ihres Engagements',
        p2: 'z. B. Nachwuchsförderung & Employer Branding'
      },
      'Netzwerkpartner werden': {
        l1: 'Fachgebiet / Institution',
        p1: 'z. B. Sportschule, Sportmedizin, Verband, Verein',
        l2: 'Region & Kooperations-Idee',
        p2: 'z. B. Zentralschweiz / Gemeinsame Workshops'
      },
      'Allgemeine Anfrage': {
        l1: 'Betreff / Kontext Ihrer Anfrage',
        p1: 'z. B. Medienanfrage, Podium, Event',
        l2: 'Organisation / Funktion',
        p2: 'z. B. Redaktion / Vereinsvorstand'
      }
    };

    function wpUpdateHeader() {
      var lbl = document.getElementById('wpStepLabel');
      if (lbl) {
        var span = lbl.querySelector('span');
        if (span) span.textContent = wpHer11StepTitles[wpHer11State.step] || wpHer11StepTitles[1];
      }
      var backBtn = document.getElementById('wpBtnBackTop');
      if (backBtn) backBtn.style.display = wpHer11State.step > 1 ? 'inline-flex' : 'none';
      for (var i = 1; i <= 3; i++) {
        var seg = document.getElementById('wpProg' + i);
        var pane = document.getElementById('wpStep' + i);
        if (seg) {
          seg.className = 'wp-progress-seg' + (i === wpHer11State.step ? ' active' : (i < wpHer11State.step ? ' done' : ''));
        }
        if (pane) {
          pane.className = 'wp-step-pane' + (i === wpHer11State.step ? ' active' : '');
        }
      }
    }

    function wpNextStep(targetStep) {
      wpHer11State.step = targetStep;
      wpUpdateHeader();
    }

    function wpPrevStep() {
      if (wpHer11State.step > 1) {
        wpHer11State.step -= 1;
        wpUpdateHeader();
      }
    }

    function wpSelectHer11Topic(topicVal) {
      wpHer11State.topic = topicVal;
      var btns = document.querySelectorAll('#wpRoleGrid .wp-role-tile');
      for (var i = 0; i < btns.length; i++) {
        btns[i].classList.toggle('selected', btns[i].getAttribute('data-topic') === topicVal);
      }
      var cfg = wpHer11RoleConfig[topicVal] || wpHer11RoleConfig['Ausbildung als Spielerin'];
      var l1 = document.getElementById('wpDetail1Label');
      var i1 = document.getElementById('wpDetail1');
      var l2 = document.getElementById('wpDetail2Label');
      var i2 = document.getElementById('wpDetail2');
      if (l1) l1.textContent = cfg.l1;
      if (i1) i1.placeholder = cfg.p1;
      if (l2) l2.textContent = cfg.l2;
      if (i2) i2.placeholder = cfg.p2;
    }

    function wpSelectHer11Urgency(urg) {
      wpHer11State.urgency = urg;
      var btns = document.querySelectorAll('#wpUrgencyGrid .wp-role-tile');
      for (var i = 0; i < btns.length; i++) {
        btns[i].classList.toggle('selected', btns[i].getAttribute('data-urg') === urg);
      }
    }

    function wpTriggerPhotoUpload() {
      var inp = document.getElementById('wpPhotoInput');
      if (inp) inp.click();
    }

    function wpCompressImageFile(file, callback) {
      var reader = new FileReader();
      reader.onload = function(ev) {
        var img = new Image();
        img.onload = function() {
          var maxDim = 1000;
          var w = img.width;
          var h = img.height;
          if (w > maxDim || h > maxDim) {
            if (w >= h) {
              h = Math.round(h * (maxDim / w));
              w = maxDim;
            } else {
              w = Math.round(w * (maxDim / h));
              h = maxDim;
            }
          }
          var canvas = document.createElement('canvas');
          canvas.width = w;
          canvas.height = h;
          var ctx = canvas.getContext('2d');
          ctx.drawImage(img, 0, 0, w, h);
          callback(canvas.toDataURL('image/jpeg', 0.82));
        };
        img.src = ev.target.result;
      };
      reader.readAsDataURL(file);
    }

    function wpRenderPhotos() {
      var wrap = document.getElementById('wpPhotoThumbs');
      var cnt = document.getElementById('wpPhotoCounter');
      if (cnt) cnt.textContent = wpHer11State.photos.length + ' / 3 Bilder ausgewählt · Automatisch für 1-Seiten-PDF optimiert';
      if (!wrap) return;
      wrap.innerHTML = '';
      for (var i = 0; i < wpHer11State.photos.length; i++) {
        (function(idx) {
          var div = document.createElement('div');
          div.className = 'wp-thumb-item';
          var im = document.createElement('img');
          im.src = wpHer11State.photos[idx];
          im.alt = 'Anhang ' + (idx + 1);
          var btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'wp-thumb-del';
          btn.textContent = 'Entfernen';
          btn.onclick = function() { wpRemovePhoto(idx); };
          div.appendChild(im);
          div.appendChild(btn);
          wrap.appendChild(div);
        })(i);
      }
    }

    function wpHandlePhotoFiles(files) {
      if (!files || !files.length) return;
      for (var i = 0; i < files.length; i++) {
        if (wpHer11State.photos.length >= 3) break;
        wpCompressImageFile(files[i], function(b64) {
          if (wpHer11State.photos.length < 3) {
            wpHer11State.photos.push(b64);
            wpRenderPhotos();
          }
        });
      }
    }

    function wpRemovePhoto(idx) {
      wpHer11State.photos.splice(idx, 1);
      wpRenderPhotos();
    }

    function wpCheckHer11Plz(val) {
      var badge = document.getElementById('wpPlzBadge');
      var txt = document.getElementById('wpPlzBadgeText');
      if (!badge || !txt) return;
      var m = String(val || '').match(/\b(\d{4})\b/);
      if (!m) {
        badge.className = 'wp-plz-badge';
        return;
      }
      badge.className = 'wp-plz-badge in-area';
      txt.textContent = 'PLZ ' + m[1] + ': Im schweizweiten HER11 Partner- & Ausbildungs-Netzwerk';
    }

    function wpStripEmojisForDom(str) {
      return String(str || '').replace(/[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/gu, '').replace(/\s+\n/g, '\n').trim();
    }

    function wpResetWizard() {
      wpHer11State.step = 1;
      wpHer11State.photos = [];
      wpRenderPhotos();
      var form = document.getElementById('her11ContactForm');
      if (form) {
        form.reset();
        form.style.display = 'grid';
      }
      var sBox = document.getElementById('wpSuccessBox');
      if (sBox) sBox.classList.remove('visible');
      var err = document.getElementById('wpFormError');
      if (err) err.style.display = 'none';
      var badge = document.getElementById('wpPlzBadge');
      if (badge) badge.className = 'wp-plz-badge';
      wpSelectHer11Topic('Ausbildung als Spielerin');
      wpSelectHer11Urgency('Planbar / Nach Absprache');
      wpUpdateHeader();
    }

    function wpSubmitHer11Lead(e) {
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

      var cfg = wpHer11RoleConfig[wpHer11State.topic] || wpHer11RoleConfig['Ausbildung als Spielerin'];
      var extra = {};
      extra[cfg.l1] = d1 || 'Keine Angabe';
      extra[cfg.l2] = d2 || 'Keine Angabe';

      var btn = document.getElementById('wpSubmitBtn');
      var btnTxt = document.getElementById('wpSubmitBtnText');
      if (btn) btn.disabled = true;
      if (btnTxt) btnTxt.textContent = '1-Seiten-PDF-Dossier wird erstellt...';

      var payload = {
        client_slug: 'her11',
        source_page: 'preview-her11/kontakt.html',
        website_url: hp,
        category: wpHer11State.topic,
        sparte: wpHer11State.topic,
        urgency: wpHer11State.urgency,
        name: name,
        company: company,
        street: street,
        plz: loc,
        phone: phone,
        email: email,
        message: msg || ('Anfrage zum Bereich ' + wpHer11State.topic),
        extra_fields: extra,
        photos: wpHer11State.photos,
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
        document.getElementById('her11ContactForm').style.display = 'none';
        document.getElementById('wpResRef').textContent = res.ref_code || '#WP-2026';
        document.getElementById('wpResAssigned').textContent = res.assigned_to || 'Jenny Ettle & Ramona Bachmann';
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
      })
      .catch(function() {
        if (btn) btn.disabled = false;
        if (btnTxt) btnTxt.textContent = '1-Seiten-Dossier & Anfrage senden';
        if (errBox) {
          errBox.textContent = 'Netzwerkfehler bei der Übermittlung. Bitte schreibe uns direkt an info@her11.ch.';
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
          'ausbildung': 'Ausbildung als Spielerin',
          'beratung': 'Beratung und Begleitung',
          'betrieb': 'Ausbildungsbetrieb werden',
          'sponsor': 'Sponsoring / Partnerschaft',
          'netzwerk': 'Netzwerkpartner werden',
          'allgemein': 'Allgemeine Anfrage'
        };
        if (map[t]) {
          wpSelectHer11Topic(map[t]);
        }
      } catch(err) {}
    })();
  </script>
"""

pages_to_write = [
    ("index.html", "HER11 — Dein Talent. Dein Weg. Deine Zukunft.", "startseite", INDEX_BODY),
    ("ueber-uns.html", "Über uns — Weil jede Spielerin ihren eigenen Weg hat | HER11", "ueber-uns", UEBER_UNS_BODY),
    ("ausbildung.html", "Ausbildung — Zwei Karrieren. Eine Zukunft. | HER11", "ausbildung", AUSBILDUNG_BODY),
    ("begleitung.html", "Begleitung — Du stehst im Mittelpunkt | HER11", "begleitung", BEGLEITUNG_BODY),
    ("mach-mit.html", "Mach mit — Gemeinsam schaffen wir Chancen | HER11", "mach-mit", MACH_MIT_BODY),
    ("kontakt.html", "Kontakt — Lass uns gemeinsam etwas bewegen | HER11", "kontakt", KONTAKT_BODY),
]

for fname, title, nav_key, body in pages_to_write:
    full_html = render_shell(fname, title, nav_key, body)
    (SITE_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"Wrote {fname} ({len(full_html)} bytes)")

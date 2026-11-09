#!/usr/bin/env python3
"""
Builds the complete 3-page WebPilot showcase for FC Schlieren (preview-fcschlieren):
  - index.html (Das Vereins-Flaggschiff mit 100% Original-Daten & allen 11 Sponsoren)
  - herren-1.html (Die Beispiel-Team-Seite Herren 1 & Frauen 1 + 33-Teams-Matrix + Blaupausen-Modal)
  - kontakt.html (Die zentrale Vereins-, Probetraining-, Spielbetriebs- & Sponsoring-Zentrale)
Plus company.json, config.json, and site.json.
Strict adherence to #UI-01..#UI-14, #LANG-01..#LANG-02 (100% ss, zero emojis in DOM, 2-Radius 0/4/8px).
"""
import json
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
SITE_DIR = BASE_DIR / "preview-fcschlieren"
SITE_DIR.mkdir(parents=True, exist_ok=True)

# 1. Write company.json, config.json, site.json
company_data = {
    "slug": "fcschlieren",
    "company_name": "FC Schlieren",
    "legal_name": "Fussballclub Schlieren (SFV-Verein Nr. 530)",
    "tagline": "Kämpfe mit Leidenschaft, siege mit Stolz, verliere mit Respekt, aber gib niemals auf!",
    "founded": "21. März 1921",
    "president": "Roger Küng",
    "head_office": "Jana Seifriz",
    "sport_director": "Zoran Perak",
    "youth_boys": "Luigi Schiavano",
    "youth_girls": "Mario De Meo",
    "finance": "Luigi Voci",
    "address": "Sportanlage Zelgli (im Rohr), Postfach, 8952 Schlieren",
    "phone": "+41 79 400 20 93",
    "email": "j.seifriz@fcschlieren.ch",
    "website": "https://fcschlieren.ch",
    "colors": {
        "primary": "#006EAB",
        "primary_dark": "#0F172A",
        "accent_gold": "#FDC500",
        "pitch_green": "#009245"
    }
}
(SITE_DIR / "company.json").write_text(json.dumps(company_data, indent=2, ensure_ascii=False), encoding="utf-8")

config_data = {
    "slug": "fcschlieren",
    "name": "FC Schlieren",
    "company_name": "FC Schlieren",
    "domain": "fcschlieren.ch",
    "preview_url": "https://vorschau.magnet-xs.ch/fcschlieren-vollversion/",
    "cockpit_token": "fcschlieren2026",
    "template": "sports-club-flagship-v1",
    "pages": ["index.html", "herren-1.html", "kontakt.html"]
}
(SITE_DIR / "config.json").write_text(json.dumps(config_data, indent=2, ensure_ascii=False), encoding="utf-8")

site_data = {
    "name": "FC Schlieren",
    "slug": "fcschlieren",
    "Updated": "2026-10-31",
    "TeamsCount": 33,
    "SponsorsCount": 11
}
(SITE_DIR / "site.json").write_text(json.dumps(site_data, indent=2, ensure_ascii=False), encoding="utf-8")


SHARED_CSS = """
    :root {
      --fcs-blue: #006EAB;
      --fcs-blue-bright: #1D82BD;
      --fcs-blue-soft: #EBF5FB;
      --fcs-navy: #0F172A;
      --fcs-navy-deep: #0B1324;
      --fcs-gold: #FDC500;
      --fcs-gold-dark: #B45309;
      --fcs-gold-soft: #FEF9C3;
      --fcs-green: #009245;
      --fcs-green-soft: #DCFCE7;
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
      --shadow-md: 0 10px 28px rgba(15, 23, 42, 0.08);
      --shadow-lg: 0 18px 42px rgba(15, 23, 42, 0.14);
      --container: 1240px;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      font-size: 16px;
      overflow-x: hidden;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      color: var(--text-main);
      background-color: var(--bg-page);
      line-height: 1.6;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    img {
      max-width: 100%;
      height: auto;
      display: block;
    }

    a {
      color: inherit;
      text-decoration: none;
      transition: color 0.2s ease, background-color 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
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

    /* Section Kickers (#UI-06: No JetBrains Mono, No //) */
    .section-kicker {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.76rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--fcs-blue);
      margin-bottom: 12px;
    }
    .section-kicker.kicker-light {
      color: var(--fcs-gold);
    }

    h1, h2, h3, h4 {
      font-family: 'Montserrat', sans-serif;
      color: var(--fcs-navy);
      line-height: 1.18;
      letter-spacing: -0.02em;
    }

    .section-head {
      max-width: 780px;
      margin-bottom: 44px;
    }
    .section-title {
      font-size: clamp(1.85rem, 3.2vw, 2.65rem);
      font-weight: 800;
      margin-bottom: 14px;
    }
    .section-desc {
      font-size: 1.04rem;
      color: var(--text-body);
      line-height: 1.65;
    }

    section {
      padding: 84px 0;
      position: relative;
    }


    /* Variant 1 / 2 Switcher Bar (David & Jenny Direct Comparison) */
    .wp-v1-switch-bar {
      background-color: #0B1528;
      color: #F8FAFC;
      border-bottom: 1px solid rgba(245, 158, 11, 0.38);
      font-size: 0.8rem;
      position: relative;
      z-index: 1003;
      padding: 7px 0;
    }
    .wp-v1-switch-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }
    .wp-v1-switch-left {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      font-weight: 600;
      color: #E2E8F0;
    }
    .wp-v1-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: rgba(0, 110, 171, 0.35);
      border: 1px solid rgba(56, 189, 248, 0.45);
      color: #7DD3FC;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.7rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }
    .wp-v1-switch-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 7px;
      background-color: #F59E0B;
      color: #0B1528;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.76rem;
      font-weight: 800;
      padding: 6px 12px;
      min-height: 34px;
      border-radius: var(--radius-sm);
      border: 1px solid #FBBF24;
      text-align: center;
      line-height: 1.25;
    }
    .wp-v1-switch-btn:hover {
      background-color: #FBBF24;
      color: #0B1528;
    }
    @media (max-width: 720px) {
      .wp-v1-switch-inner {
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
      }
      .wp-v1-switch-btn {
        width: 100%;
      }
    }

    /* Top Info Bar */
    .top-bar {
      background-color: var(--fcs-navy-deep);
      color: #E2E8F0;
      font-size: 0.8rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      position: relative;
      z-index: 1002;
    }
    .top-bar-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      min-height: 38px;
      gap: 16px;
      flex-wrap: wrap;
      padding-top: 6px;
      padding-bottom: 6px;
    }
    .top-bar-left {
      display: flex;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
      font-weight: 500;
    }
    .top-bar-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: rgba(253, 197, 0, 0.16);
      color: var(--fcs-gold);
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
      color: var(--fcs-gold);
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
      gap: 20px;
    }
    .brand-link {
      display: inline-flex;
      align-items: center;
      gap: 14px;
      flex-shrink: 0;
    }
    .brand-logo {
      width: 48px;
      height: 56px;
      object-fit: contain;
      flex-shrink: 0;
    }
    .brand-text {
      display: flex;
      flex-direction: column;
    }
    .brand-name {
      font-family: 'Montserrat', sans-serif;
      font-size: 1.22rem;
      font-weight: 800;
      color: var(--fcs-navy);
      letter-spacing: -0.02em;
      line-height: 1.1;
    }
    .brand-sub {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.68rem;
      font-weight: 700;
      color: var(--fcs-blue);
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-top: 3px;
    }

    .main-nav {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .nav-link {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text-body);
      padding: 8px 9px;
      border-radius: var(--radius-sm);
      white-space: nowrap;
      min-height: 34px;
      display: inline-flex;
      align-items: center;
    }
    .nav-link:hover, .nav-link.active {
      color: var(--fcs-blue);
      background-color: var(--fcs-blue-soft);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
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
      background-color: var(--fcs-blue);
      color: #FFFFFF;
      box-shadow: 0 4px 14px rgba(0, 110, 171, 0.24);
    }
    .btn-cta-primary:hover {
      background-color: #00598A;
      transform: translateY(-1px);
    }
    .btn-cta-gold {
      background-color: var(--fcs-gold);
      color: var(--fcs-navy);
      font-weight: 800;
      box-shadow: 0 4px 14px rgba(253, 197, 0, 0.28);
    }
    .btn-cta-gold:hover {
      background-color: #EAB308;
      transform: translateY(-1px);
    }
    .btn-cta-navy {
      background-color: var(--fcs-navy);
      color: #FFFFFF;
    }
    .btn-cta-navy:hover {
      background-color: #1E293B;
    }
    .btn-cta-outline {
      background-color: #FFFFFF;
      color: var(--fcs-navy);
      border-color: var(--border-strong);
    }
    .btn-cta-outline:hover {
      border-color: var(--fcs-blue);
      color: var(--fcs-blue);
      background-color: var(--fcs-blue-soft);
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
      color: var(--fcs-navy);
      cursor: pointer;
    }
    .mobile-drawer {
      display: none;
      position: fixed;
      top: 82px;
      left: 0;
      right: 0;
      background-color: var(--fcs-navy);
      border-bottom: 2px solid var(--fcs-gold);
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
      background-color: var(--fcs-blue);
    }

    /* Hero Section */
    .hero-section {
      background: linear-gradient(135deg, #0B1324 0%, #0F2547 55%, #004E7C 100%);
      color: #FFFFFF;
      padding: 68px 0 76px;
      position: relative;
      overflow: hidden;
      border-bottom: 4px solid var(--fcs-gold);
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
      color: #FFFFFF;
      font-size: clamp(2.15rem, 4vw, 3.35rem);
      font-weight: 800;
      line-height: 1.12;
      margin-bottom: 18px;
    }
    .hero-title span {
      color: var(--fcs-gold);
    }
    .hero-motto-box {
      background-color: rgba(253, 197, 0, 0.12);
      border-left: 4px solid var(--fcs-gold);
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
      font-size: 1.05rem;
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
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--fcs-gold);
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
      justify-content: space-between;
      height: 100%;
      gap: 16px;
    }
    .hero-photo-card {
      flex: 1 1 auto;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .hero-photo-card img {
      flex: 1 1 auto;
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
      object-position: center 25%;
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
      color: var(--fcs-gold);
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
      height: 148px;
      object-fit: cover;
    }
    .hero-mini-body {
      padding: 10px 14px;
      font-size: 0.78rem;
      color: #E2E8F0;
    }
    .hero-centenary-box {
      background-color: rgba(255, 255, 255, 0.96);
      color: var(--fcs-navy);
      border-radius: var(--radius-md);
      padding: 14px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      gap: 8px;
    }
    .hero-centenary-box img {
      width: 112px;
      height: 84px;
      object-fit: contain;
    }
    .hero-centenary-box strong {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.8rem;
      color: var(--fcs-navy);
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
    .card-media {
      position: relative;
      height: 210px;
      background-color: var(--fcs-navy);
      overflow: hidden;
    }
    .card-media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .card-badge {
      position: absolute;
      top: 12px;
      left: 12px;
      background-color: var(--fcs-navy);
      color: var(--fcs-gold);
      font-family: 'Montserrat', sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }
    .card-body {
      padding: 24px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
      gap: 12px;
    }
    .card-title {
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--fcs-navy);
    }
    .card-text {
      font-size: 0.93rem;
      color: var(--text-body);
      line-height: 1.6;
    }
    .card-meta-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
      padding: 12px 14px;
      background-color: var(--bg-muted);
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      color: var(--text-main);
    }
    .card-meta-item {
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }
    .card-meta-item svg {
      color: var(--fcs-blue);
      flex-shrink: 0;
      margin-top: 3px;
    }
    .card-footer {
      padding: 0 24px 24px;
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }

    /* Department Pillar Cards */
    .pillar-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-top: 4px solid var(--fcs-blue);
      border-radius: var(--radius-md);
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 16px;
      box-shadow: var(--shadow-sm);
    }
    .pillar-card.pillar-gold {
      border-top-color: var(--fcs-gold);
    }
    .pillar-card.pillar-green {
      border-top-color: var(--fcs-green);
    }
    .pillar-count {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--fcs-blue);
      background-color: var(--fcs-blue-soft);
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      align-self: flex-start;
      text-transform: uppercase;
    }
    .pillar-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }
    .pillar-tag {
      font-size: 0.76rem;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      background-color: var(--bg-muted);
      color: var(--text-main);
      border: 1px solid var(--border-light);
    }

    /* Board / Vorstand Grid */
    .board-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-top: 24px;
    }
    .board-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .board-role {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--fcs-blue);
    }
    .board-name {
      font-family: 'Montserrat', sans-serif;
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--fcs-navy);
    }
    .board-links {
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-top: 6px;
      font-size: 0.84rem;
      color: var(--text-body);
    }
    .board-links a:hover {
      color: var(--fcs-blue);
    }

    /* Timeline */
    .timeline-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-top: 28px;
    }
    .timeline-box {
      background-color: var(--fcs-navy);
      color: #FFFFFF;
      border-radius: var(--radius-md);
      padding: 20px;
      border-top: 3px solid var(--fcs-gold);
    }
    .timeline-year {
      font-family: 'Montserrat', sans-serif;
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--fcs-gold);
      margin-bottom: 6px;
    }
    .timeline-text {
      font-size: 0.85rem;
      color: #E2E8F0;
      line-height: 1.55;
    }

    /* Sponsors Showcase (Gold / Silver / Bronze) */
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
      background-color: var(--fcs-gold-soft);
      color: #92400E;
      border: 1px solid #FDE047;
    }
    .tier-silver {
      background-color: #F1F5F9;
      color: #1E293B;
      border: 1px solid #CBD5E1;
    }
    .tier-bronze {
      background-color: #FFEDD5;
      color: #9A3412;
      border: 1px solid #FDBA74;
    }

    .sponsors-gold-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
    }
    .sponsors-silver-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }
    .sponsors-bronze-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }
    .sponsor-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 22px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      text-align: center;
      gap: 14px;
      box-shadow: var(--shadow-sm);
      transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
    }
    .sponsor-card:hover {
      transform: translateY(-2px);
      border-color: var(--fcs-blue);
      box-shadow: var(--shadow-md);
    }
    .sponsor-card.gold-card {
      border: 2px solid #FDE047;
      padding: 28px;
    }
    .sponsor-logo-wrap {
      width: 100%;
      height: 110px;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #FFFFFF;
      padding: 8px;
    }
    .sponsor-card.gold-card .sponsor-logo-wrap {
      height: 140px;
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
      font-size: 1rem;
      font-weight: 800;
      color: var(--fcs-navy);
    }
    .sponsor-role-tag {
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--text-muted);
    }

    /* Social Wall */
    .social-filter-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 28px;
    }
    .social-tab-btn {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-strong);
      background-color: #FFFFFF;
      color: var(--text-body);
      cursor: pointer;
    }
    .social-tab-btn.active, .social-tab-btn:hover {
      background-color: var(--fcs-blue);
      color: #FFFFFF;
      border-color: var(--fcs-blue);
    }

    /* Footer */
    .site-footer {
      background-color: var(--fcs-navy-deep);
      color: #E2E8F0;
      padding: 68px 0 36px;
      border-top: 4px solid var(--fcs-gold);
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
    .board-links a,
    .staff-card a,
    .team-sponsor-strip a {
      display: inline-flex;
      align-items: center;
      min-height: 32px;
      padding: 4px 0;
    }
    .footer-list a:hover, .footer-list button:hover {
      color: var(--fcs-gold);
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
      border: 2px solid var(--fcs-gold);
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
      color: var(--fcs-navy);
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
      color: var(--fcs-green);
      flex-shrink: 0;
      margin-top: 2px;
    }

    /* Responsive Breakpoints */
    @media (max-width: 1080px) {
      .hero-grid {
        grid-template-columns: 1fr;
      }
      .grid-4, .timeline-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .grid-3, .board-grid, .sponsors-silver-grid, .sponsors-bronze-grid {
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
      .hero-kpi-strip {
        grid-template-columns: repeat(2, 1fr);
      }
      .hero-secondary-row,
      .grid-2,
      .grid-3,
      .grid-4,
      .board-grid,
      .timeline-grid,
      .sponsors-gold-grid,
      .sponsors-silver-grid,
      .sponsors-bronze-grid,
      .footer-grid {
        grid-template-columns: 1fr;
      }
      .header-actions .btn-cta-primary {
        padding: 9px 12px;
        font-size: 0.78rem;
      }
    }
"""


def render_shell(filename: str, page_title: str, active_nav: str, body_html: str, extra_css: str = "") -> str:
    nav_start = "active" if active_nav == "startseite" else ""
    nav_teams = "active" if active_nav == "teams" else ""
    nav_kontakt = "active" if active_nav == "kontakt" else ""
    v2_href = "/fcschlieren-v2/" if filename == "index.html" else f"/fcschlieren-v2/{filename}"

    return f"""<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self' https: data: blob:; script-src 'self' 'unsafe-inline' https:; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com data:; img-src 'self' https: data: blob:; connect-src 'self' https:;">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta http-equiv="Permissions-Policy" content="camera=(), microphone=(), geolocation=()">
  <title>{page_title}</title>
  <meta name="description" content="Fussballclub Schlieren (gegründet 1921) – 33 Teams, Aktive Herren &amp; Frauen, Junioren A–G, Juniorinnen, Fussballschule &amp; Sportplatz Zelgli in 8952 Schlieren.">
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
  <!-- TOP BAR -->
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div class="top-bar-left">
        <span class="top-bar-badge" data-slot="topbar_badge">SEIT 21. MÄRZ 1921</span>
        <span data-slot="topbar_info">Fussballanlage Zelgli · 8952 Schlieren · 33 Mannschaften im SFV</span>
      </div>
      <div class="top-bar-links">
        <a href="index.html#zelgli-verein">Sportplatz Zelgli &amp; Beizli</a>
        <a href="index.html#sponsoren">Sponsoren &amp; Supporter</a>
        <button type="button" onclick="wpOpenBlueprintModal('Vereinsdokumente: Statuten, Schutz- &amp; Notfallkonzept', 'Geschäftsstelle &amp; Präsidium', 'Roger Küng (r.kueng@fcschlieren.ch) &amp; Jana Seifriz (j.seifriz@fcschlieren.ch)')">Notfallkonzept &amp; Statuten</button>
        <a href="kontakt.html?thema=spielbetrieb">Spielverschiebung melden</a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="FC Schlieren Startseite">
        <img src="images/logo-fcschlieren.webp" alt="Wappen FC Schlieren" class="brand-logo" width="48" height="56" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">FC SCHLIEREN</span>
          <span class="brand-sub" data-slot="brand_sub">GEGRÜNDET 1921 · ZELGLI</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}">Startseite</a>
        <a href="herren-1.html" class="nav-link {nav_teams}">Teams (33)</a>
        <a href="index.html#aktuelles-camps" class="nav-link">Fussballschule &amp; Camps</a>
        <a href="index.html#zelgli-verein" class="nav-link">Zelgli &amp; Verein</a>
        <a href="index.html#sponsoren" class="nav-link">Sponsoren</a>
        <a href="kontakt.html" class="nav-link {nav_kontakt}">Vereins-Zentrale</a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-primary btn-sm" data-slot="header_cta">
          <span>Probetraining &amp; Kontakt</span>
        </a>
        <button type="button" class="mobile-toggle" id="mobileMenuBtn" aria-label="Menü öffnen" onclick="wpToggleMobileMenu()">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    </div>

    <div class="mobile-drawer" id="mobileDrawer">
      <a href="index.html" onclick="wpCloseMobileMenu()">Startseite</a>
      <a href="herren-1.html" onclick="wpCloseMobileMenu()">Beispiel-Team (Herren 1 / Frauen 1) &amp; 33 Teams</a>
      <a href="index.html#aktuelles-camps" onclick="wpCloseMobileMenu()">Fussballschule &amp; Fussballcamps</a>
      <a href="index.html#zelgli-verein" onclick="wpCloseMobileMenu()">Sportplatz Zelgli, Beizli &amp; Vorstand</a>
      <a href="index.html#sponsoren" onclick="wpCloseMobileMenu()">Sponsoren, Supporter &amp; Business-Club</a>
      <a href="kontakt.html" onclick="wpCloseMobileMenu()">Vereins- &amp; Probetraining-Zentrale</a>
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
            <img src="images/logo-fcschlieren.webp" alt="FC Schlieren Wappen" width="44" height="52" loading="lazy" decoding="async" style="object-fit:contain;">
            <div>
              <div style="font-family:'Montserrat',sans-serif;font-weight:800;font-size:1.1rem;color:#FFFFFF;">FC SCHLIEREN</div>
              <div style="font-size:0.76rem;color:#FDC500;font-weight:700;">SEIT 21. MÄRZ 1921 · SFV NR. 530</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#CBD5E1;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Heimat für 33 Mannschaften im Limmattal: Aktive Herren &amp; Senioren, Aktive Frauen, 17 Junioren-Teams, 8 Juniorinnen-Teams und unsere Fussballschule auf der Sportanlage Zelgli.
          </p>
          <div style="font-size:0.84rem;color:#E2E8F0;font-weight:600;">
            Fussballanlage Zelgli («im Rohr») · Postfach · 8952 Schlieren
          </div>
        </div>

        <div>
          <div class="footer-title">Mannschaften &amp; Sport</div>
          <ul class="footer-list">
            <li><a href="herren-1.html?team=herren1">Herren 1 (Beispiel-Team-Seite)</a></li>
            <li><a href="herren-1.html?team=frauen1">Frauen 1 (Beispiel-Team-Seite)</a></li>
            <li><a href="herren-1.html#alle-teams-matrix">Alle 33 Teams in der Matrix</a></li>
            <li><a href="index.html#aktuelles-camps">Fussballschule (Mittwoch 16:15 Uhr)</a></li>
            <li><a href="index.html#aktuelles-camps">Kohler Fussballcamps &amp; Trailer</a></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Wintertrainings- &amp; Hallenplan 2026', 'Spielbetrieb FC Schlieren', 'Roger Mehr (r.mehr@fcschlieren.ch) &amp; Jana Seifriz (j.seifriz@fcschlieren.ch)')">Wintertrainings- &amp; Hallenplan</button></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Verein, Sponsoren &amp; Zelgli</div>
          <ul class="footer-list">
            <li><a href="index.html#zelgli-verein">Vorstand &amp; Funktionäre</a></li>
            <li><a href="index.html#zelgli-verein">Sportplatz Zelgli &amp; Club-Beizli</a></li>
            <li><a href="index.html#zelgli-verein">Vereinschronik seit 1921</a></li>
            <li><a href="index.html#sponsoren">Gold-, Silber- &amp; Bronze-Sponsoren</a></li>
            <li><a href="kontakt.html?thema=sponsoring">Supporter-Vereinigung (ab CHF 150.–)</a></li>
            <li><a href="kontakt.html?thema=sponsoring">Business-Club (CHF 850.–) &amp; Bandenwerbung</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direkt-Service &amp; Formulare</div>
          <ul class="footer-list">
            <li><a href="kontakt.html?thema=probetraining">Probetraining anfragen</a></li>
            <li><a href="kontakt.html?thema=spielbetrieb">Spielverschiebungsgesuch einreichen</a></li>
            <li><a href="kontakt.html?thema=kleider">Kleiderbestellung / Vereinskollektion</a></li>
            <li><a href="kontakt.html?thema=mitgliedschaft">Adressänderung / Mutation / Austritt</a></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Statuten, Schutzkonzept &amp; Ehrenkodex', 'Präsidium FC Schlieren', 'Roger Küng (r.kueng@fcschlieren.ch)')">Statuten, Schutz- &amp; Notfallkonzept</button></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Fussballclub Schlieren (8952 Schlieren) · Alle Rechte vorbehalten.</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;">
          <a href="herren-1.html" style="color:#FDC500;font-weight:700;">Beispiel-Teams (Herren 1 / Frauen 1 &amp; 33 Teams)</a>
          <a href="kontakt.html" style="color:#E2E8F0;">Vereins-Zentrale</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- SEITEN-VORSCHAU-MODAL -->
  <div class="wp-modal-backdrop" id="wpBlueprintModal" role="dialog" aria-modal="true" aria-labelledby="wpBpTitle" data-allow-scroll="true">
    <div class="wp-modal-dialog" data-allow-scroll="true">
      <button type="button" class="wp-modal-close" aria-label="Dialog schliessen" onclick="wpCloseBlueprintModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="section-kicker">SEITEN-VORSCHAU · FC SCHLIEREN</div>
      <h3 id="wpBpTitle" style="font-size:1.35rem;font-weight:800;margin-bottom:8px;">Team-Vorschau: Mannschaft</h3>
      <p id="wpBpSub" style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
        Stellvertretend für alle 33 Mannschaften und Unterseiten des FC Schlieren sind in dieser Vorschau die Startseite, die Beispiel-Teams <strong>Herren 1</strong> und <strong>Frauen 1</strong> sowie die zentrale <strong>Vereins- &amp; Probetraining-Zentrale</strong> komplett mit Originaldaten ausgebaut.
      </p>
      <div style="background-color:var(--fcs-blue-soft);border-left:4px solid var(--fcs-blue);padding:12px 14px;border-radius:var(--radius-sm);font-size:0.86rem;margin-bottom:14px;">
        <div style="font-weight:700;color:var(--fcs-navy);" id="wpBpCategory">Abteilung: Nachwuchs / Aktive</div>
        <div style="color:var(--text-body);margin-top:2px;" id="wpBpContact">Zuständige Leitung: Zoran Perak / Luigi Schiavano</div>
      </div>

      <div class="wp-modal-checklist">
        <div style="font-family:'Montserrat',sans-serif;font-size:0.78rem;font-weight:800;text-transform:uppercase;color:var(--fcs-navy);">
          Beim kompletten Ausbau (analog Herren 1 &amp; Frauen 1) enthalten:
        </div>
        <div class="wp-modal-check-item">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Offizielles Mannschaftsfoto, Trainingszeiten auf dem Sportplatz Zelgli &amp; Hallenplan</span>
        </div>
        <div class="wp-modal-check-item">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Spielerkader nach Position (Tor, Verteidigung, Mittelfeld, Sturm) &amp; Trainerstaff mit Direktkontakt</span>
        </div>
        <div class="wp-modal-check-item">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
          <span>SFV-Resultate, Matchprogramm-Download sowie zugeordnete Team-Sponsoren &amp; Dress-Partner</span>
        </div>
        <div class="wp-modal-check-item">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Direkte 1-Klick-Anbindung an Probetraining, Spielverschiebung und Kleiderbestellung</span>
        </div>
      </div>

      <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:18px;">
        <a href="team-update.html?team=1-mannschaft" id="wpBpTeamUpdateLink" class="btn-cta btn-cta-gold btn-sm">
          <span>Mannschafts-Daten &amp; Kader einreichen (Trainer-Formular)</span>
        </a>
        <a href="herren-1.html" class="btn-cta btn-cta-primary btn-sm" onclick="wpCloseBlueprintModal()">
          <span>Ausgearbeitete Beispiel-Teams (Herren 1 / Frauen 1) ansehen</span>
        </a>
        <a href="kontakt.html?thema=probetraining" id="wpBpCtaLink" class="btn-cta btn-cta-outline btn-sm">
          <span>Anfrage / Probetraining für diesen Bereich starten</span>
        </a>
      </div>
    </div>
  </div>

  <!-- IMPRESSUM MODAL -->
  <div class="wp-modal-backdrop" id="wpImpressumModal" role="dialog" aria-modal="true" aria-labelledby="wpImpTitle">
    <div class="wp-modal-dialog" data-allow-scroll="true">
      <button type="button" class="wp-modal-close" aria-label="Impressum schliessen" onclick="wpCloseImpressumModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="section-kicker">RECHTLICHE ANGABEN · SCHWEIZER DSG</div>
      <h3 id="wpImpTitle" style="font-size:1.3rem;font-weight:800;margin-bottom:10px;">Impressum &amp; Datenschutz – FC Schlieren</h3>
      <div style="font-size:0.88rem;color:var(--text-body);display:flex;flex-direction:column;gap:10px;">
        <p><strong>Vereinsadresse:</strong><br>Fussballclub Schlieren · Sportanlage Zelgli («im Rohr») · Postfach · 8952 Schlieren</p>
        <p><strong>Vertretungsberechtigter Vorstand:</strong><br>Roger Küng (Präsident, r.kueng@fcschlieren.ch) · Jana Seifriz (Leiterin Geschäftsstelle &amp; Spielbetrieb, j.seifriz@fcschlieren.ch) · Luigi Voci (Leiter Finanzen, l.voci@fcschlieren.ch)</p>
        <p><strong>Webverantwortlicher &amp; J+S Coach:</strong><br>Sven Seifriz (s.seifriz@fcschlieren.ch)</p>
        <p><strong>Datenschutz (Schweizer Datenschutzgesetz revDSG):</strong><br>Personendaten aus Kontakt-, Probetraining-, Mutations- und Sponsoring-Anfragen werden ausschliesslich zur Vereinsadministration innerhalb des FC Schlieren verwendet und niemals an unbefugte Dritte weitergegeben.</p>
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
    function wpOpenBlueprintModal(title, category, contact, topicParam) {{
      var m = document.getElementById('wpBlueprintModal');
      if (!m) return;
      var tEl = document.getElementById('wpBpTitle');
      var cEl = document.getElementById('wpBpCategory');
      var pEl = document.getElementById('wpBpContact');
      var linkEl = document.getElementById('wpBpCtaLink');
      if (tEl) tEl.textContent = title || 'Team-Vorschau';
      if (cEl) cEl.textContent = 'Bereich / Abteilung: ' + (category || 'FC Schlieren');
      if (pEl) pEl.textContent = 'Zuständige Ansprechperson: ' + (contact || 'Geschäftsstelle FC Schlieren (j.seifriz@fcschlieren.ch)');
      if (linkEl) linkEl.href = 'kontakt.html?thema=' + (topicParam || 'probetraining');
      var uEl = document.getElementById('wpBpTeamUpdateLink');
      if (uEl) {{
        var rawT = (title || '').split(':').pop().trim().toLowerCase()
          .replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue')
          .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
        uEl.href = 'team-update.html?team=' + encodeURIComponent(rawT || '1-mannschaft');
      }}
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

INDEX_BODY = """
  <!-- 1. HERO SECTION -->
  <section class="hero-section" data-section="hero">
    <div class="container hero-grid">
      <div>
        <div class="section-kicker kicker-light" data-slot="hero_kicker">FUSSBALLCLUB SCHLIEREN · GEGRÜNDET 21. MÄRZ 1921</div>
        <h1 class="hero-title" data-slot="hero_title">
          Leidenschaft, Stolz und <span>33 Teams</span> auf dem Zelgli.
        </h1>
        <div class="hero-motto-box" data-slot="hero_motto">
          «KÄMPFE MIT LEIDENSCHAFT, SIEGE MIT STOLZ – VERLIERE MIT RESPEKT, ABER GIB NIEMALS AUF!»
        </div>
        <p class="hero-sub" data-slot="hero_sub">
          Vom ersten Ballkontakt in der Fussballschule über 25 Nachwuchs-Mannschaften bis zu unseren Aktivteams Herren 1 und Frauen 1: Der FC Schlieren verbindet seit über 100 Jahren sportlichen Ehrgeiz, gelebte Integration und Vereinsfamilie im Herzen des Limmattals.
        </p>

        <div class="hero-cta-row">
          <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
            <span>Probetraining &amp; Vereins-Zentrale</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
          <a href="herren-1.html" class="btn-cta btn-cta-ghost-light" data-slot="hero_cta_secondary">
            <span>Beispiel-Team (Herren 1 / Frauen 1) &amp; 33 Teams</span>
          </a>
        </div>

        <div class="hero-kpi-strip">
          <div class="hero-kpi-card">
            <div class="hero-kpi-num" data-slot="kpi_1_num">1921</div>
            <div class="hero-kpi-lbl" data-slot="kpi_1_lbl">Gründung am 21. März 1921 · Über 100 Jahre Tradition</div>
          </div>
          <div class="hero-kpi-card">
            <div class="hero-kpi-num" data-slot="kpi_2_num">33 Teams</div>
            <div class="hero-kpi-lbl" data-slot="kpi_2_lbl">5 Herren/Sen. · 3 Frauen · 17 Junioren · 8 Juniorinnen</div>
          </div>
          <div class="hero-kpi-card">
            <div class="hero-kpi-num" data-slot="kpi_3_num">Zelgli</div>
            <div class="hero-kpi-lbl" data-slot="kpi_3_lbl">Hauptplatz, Kunstrasen &amp; rauchfreies Club-Beizli</div>
          </div>
          <div class="hero-kpi-card">
            <div class="hero-kpi-num" data-slot="kpi_4_num">11+ Partner</div>
            <div class="hero-kpi-lbl" data-slot="kpi_4_lbl">Gold-, Silber- &amp; Bronze-Sponsoren + Business-Club</div>
          </div>
        </div>
      </div>

      <div class="hero-visual-stack">
        <div class="hero-photo-card">
          <img src="images/hero-herren-1.webp" alt="FC Schlieren 1. Mannschaft Herren 1 auf dem Sportplatz Zelgli" width="640" height="270" data-slot="hero_img_main">
          <div class="hero-photo-caption">
            <strong>1. Mannschaft – Herren 1 (Sportplatz Zelgli)</strong>
            <span>Hauptsponsor: Emil Frey AG, Schlieren</span>
          </div>
        </div>

        <div class="hero-secondary-row">
          <div class="hero-mini-card">
            <img src="images/hero-frauen-1.webp" alt="FC Schlieren Frauen 1 Mannschaft" width="400" height="148" data-slot="hero_img_secondary">
            <div class="hero-mini-body">
              <strong style="color:#FDC500;font-family:'Montserrat',sans-serif;">Frauen 1 – Tradition seit 1979</strong><br>
              <span>Partner: J.F. Jost &amp; Co. · Waser Facility Management</span>
            </div>
          </div>
          <div class="hero-centenary-box">
            <img src="images/fcs-100-jahre.webp" alt="100 Jahre FC Schlieren Jubiläumslogo" width="112" height="84" data-slot="hero_img_centenary">
            <strong>Über 100 Jahre FC Schlieren</strong>
            <span style="font-size:0.73rem;color:var(--text-muted);">SFV-Verein Nr. 530 · 8952 Schlieren</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. AKTUELLES, FUSSBALLSCHULE & FUSSBALLCAMPS -->
  <section id="aktuelles-camps" data-section="aktuelles-camps" style="background-color:#FFFFFF;border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="camps_kicker">NACHWUCHS &amp; FERIEN-HIGHLIGHTS AUF DEM ZELGLI</div>
        <h2 class="section-title" data-slot="camps_title">Fussballschule 2026 &amp; Kohler Fussballcamps in Schlieren.</h2>
        <p class="section-desc" data-slot="camps_desc">
          Beim FC Schlieren beginnt die Freude am Fussball bereits bei den Jüngsten. Hier findest du alle aktuellen Trainingszeiten der Fussballschule, die Anmeldedaten der Kohler Fussballcamps sowie den offiziellen Camp-Trailer.
        </p>
      </div>

      <div class="grid-3">
        <!-- Card 1: Fussballschule -->
        <article class="card">
          <div class="card-media">
            <img src="images/zelgli-anlage-1.webp" alt="Fussballschule auf dem Sportplatz Zelgli Schlieren" width="420" height="210" loading="lazy" decoding="async" data-slot="camp_1_img">
            <span class="card-badge">1. Training: 19. August 2026</span>
          </div>
          <div class="card-body">
            <h3 class="card-title" data-slot="camp_1_title">Fussballschule FC Schlieren (Jg. 2016–2022)</h3>
            <p class="card-text" data-slot="camp_1_desc">
              Spielerischer Einstieg für Mädchen und Knaben direkt auf unserer Sportanlage Zelgli. Geleitet von unserem Nachwuchs-Team um Gianfranco Gennaro und Luigi Schiavano.
            </p>
            <div class="card-meta-list">
              <div class="card-meta-item">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
                <span><strong>Jahrgänge:</strong> 2016 / 2017 (Jun. E) · 2018 / 2019 (Jun. F) · 2020–2022 (Jun. G)</span>
              </div>
              <div class="card-meta-item">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                <span><strong>Trainingszeit:</strong> Jeden Mittwoch, 16:15 – 17:45 Uhr</span>
              </div>
              <div class="card-meta-item">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                <span><strong>Ort &amp; Start:</strong> Sportplatz Zelgli Schlieren · Start 19.08.2026</span>
              </div>
            </div>
          </div>
          <div class="card-footer">
            <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
              <span>Kind für Fussballschule / Schnuppertraining melden</span>
            </a>
          </div>
        </article>

        <!-- Card 2: Kohler Fussballcamps -->
        <article class="card">
          <div class="card-media">
            <img src="images/fussballcamp-kohler.webp" alt="Kohler Fussballcamps beim FC Schlieren" width="420" height="210" loading="lazy" decoding="async" data-slot="camp_2_img">
            <span class="card-badge">Ferien-Camp auf dem Zelgli</span>
          </div>
          <div class="card-body">
            <h3 class="card-title" data-slot="camp_2_title">Kohler Fussballcamps auf dem Zelgli</h3>
            <p class="card-text" data-slot="camp_2_desc">
              Intensives Technik- und Spieltraining während den Schulferien auf der Sportanlage Zelgli. Inklusive kompletter Trainingsausrüstung, kindergerechter Mittagsverpflegung und Abschlussturnier.
            </p>
            <div class="card-meta-list">
              <div class="card-meta-item">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="20 6 9 17 4 12"/></svg>
                <span>Offizieller Camp-Partner: <strong>kohler-camp.ch</strong></span>
              </div>
              <div class="card-meta-item">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="20 6 9 17 4 12"/></svg>
                <span>Für Vereinsmitglieder und Gastkinder aus dem ganzen Limmattal</span>
              </div>
            </div>
          </div>
          <div class="card-footer">
            <a href="https://kohler-camp.ch" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-outline btn-sm" style="flex:1;">
              <span>Zu kohler-camp.ch</span>
            </a>
            <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-navy btn-sm" style="flex:1;">
              <span>Frage ans Sekretariat</span>
            </a>
          </div>
        </article>

        <!-- Card 3: Camp Trailer & Trainingspläne -->
        <article class="card">
          <div class="card-media">
            <img src="images/camp-trailer-thumb.webp" alt="FC Schlieren Fussballcamp Trailer Video" width="420" height="210" loading="lazy" decoding="async" data-slot="camp_3_img">
            <span class="card-badge">Video-Trailer &amp; Pläne</span>
          </div>
          <div class="card-body">
            <h3 class="card-title" data-slot="camp_3_title">Camp-Trailer &amp; Saison-Trainingspläne</h3>
            <p class="card-text" data-slot="camp_3_desc">
              Schau dir den offiziellen Video-Trailer unseres Fussballcamps auf dem Zelgli an oder öffne direkt die aktuellen Platz-, Wintertrainings- und Hallenbelegungspläne des FC Schlieren.
            </p>
            <div class="card-meta-list">
              <div class="card-meta-item">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
                <span><strong>Offizielles Video:</strong> Fussballcamp-Trailer (YouTube)</span>
              </div>
              <div class="card-meta-item">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/></svg>
                <span><strong>Spielbetrieb:</strong> Sommer-, Winter- &amp; Hallentrainingsplan</span>
              </div>
            </div>
          </div>
          <div class="card-footer">
            <a href="https://youtu.be/R_uQ5BWDFuc" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-gold btn-sm" style="flex:1;">
              <span>Video-Trailer starten</span>
            </a>
            <button type="button" class="btn-cta btn-cta-outline btn-sm" style="flex:1;" onclick="wpOpenBlueprintModal('Wintertrainings- &amp; Hallenbelegungsplan', 'Spielbetrieb Zelgli &amp; Sporthallen Schlieren', 'Roger Mehr (r.mehr@fcschlieren.ch) &amp; Jana Seifriz (j.seifriz@fcschlieren.ch)', 'spielbetrieb')">
              <span>Trainingspläne</span>
            </button>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- 3. DIE 4 SPORTLICHEN SÄULEN (ALLE 33 TEAMS) -->
  <section id="abteilungen" data-section="abteilungen">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="dept_kicker">SPORTLICHE HEIMAT FÜR JEDES ALTER</div>
        <h2 class="section-title" data-slot="dept_title">33 Mannschaften in 4 starken Abteilungen.</h2>
        <p class="section-desc" data-slot="dept_desc">
          Als einer der grössten Ausbildungs- und Breitensportvereine im Bezirk Dietikon bietet der FC Schlieren durchgängige Teams von den G-Junioren bis zu den Senioren 50+. Klicke auf unsere Beispiel-Team-Seite für den vollen Kader-Einblick.
        </p>
      </div>

      <div class="grid-4">
        <!-- Säule 1: Aktive Herren & Senioren -->
        <div class="pillar-card">
          <div>
            <span class="pillar-count">5 Mannschaften</span>
            <h3 style="font-size:1.22rem;font-weight:800;margin:12px 0 8px;" data-slot="pillar_1_title">Aktive Herren &amp; Senioren</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:14px;" data-slot="pillar_1_desc">
              Unser sportliches Aushängeschild <strong>Herren 1</strong> (Trainer: Diego Bürger &amp; Livio Sanseverino), die 2. Mannschaft sowie drei traditionsreiche Senioren-Teams (30+, 40+, 50+).
            </p>
            <div class="pillar-tags">
              <span class="pillar-tag">Herren 1 (Beispiel-Team)</span>
              <span class="pillar-tag">Herren 2</span>
              <span class="pillar-tag">Senioren 30+</span>
              <span class="pillar-tag">Senioren 40+</span>
              <span class="pillar-tag">Senioren 50+</span>
            </div>
          </div>
          <div style="padding-top:12px;border-top:1px solid var(--border-light);font-size:0.8rem;color:var(--text-muted);">
            <strong>Leiter Aktive:</strong> Zoran Perak (z.perak@fcschlieren.ch)
          </div>
          <a href="herren-1.html?team=herren1" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">
            <span>Beispiel-Team Herren 1 öffnen</span>
          </a>
        </div>

        <!-- Säule 2: Aktive Frauen -->
        <div class="pillar-card pillar-gold">
          <div>
            <span class="pillar-count" style="background-color:var(--fcs-gold-soft);color:#92400E;">3 Mannschaften · Seit 1979</span>
            <h3 style="font-size:1.22rem;font-weight:800;margin:12px 0 8px;" data-slot="pillar_2_title">Aktive Frauen 1, 2 &amp; 3</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:14px;" data-slot="pillar_2_desc">
              Bereits 1979 gegründet: Mit drei aktiven Frauenteams gehört der FC Schlieren zu den führenden Adressen für Frauenfussball in der Region Zürich und im Limmattal.
            </p>
            <div class="pillar-tags">
              <span class="pillar-tag">Frauen 1 (Beispiel-Team)</span>
              <span class="pillar-tag">Frauen 2</span>
              <span class="pillar-tag">Frauen 3</span>
            </div>
          </div>
          <div style="padding-top:12px;border-top:1px solid var(--border-light);font-size:0.8rem;color:var(--text-muted);">
            <strong>Trainer Frauen 1:</strong> Konstantinos Vettas &amp; Sergio Zamora
          </div>
          <a href="herren-1.html?team=frauen1" class="btn-cta btn-cta-gold btn-sm" style="width:100%;">
            <span>Beispiel-Team Frauen 1 öffnen</span>
          </a>
        </div>

        <!-- Säule 3: Junioren A bis G -->
        <div class="pillar-card pillar-green">
          <div>
            <span class="pillar-count" style="background-color:var(--fcs-green-soft);color:#166534;">17 Mannschaften</span>
            <h3 style="font-size:1.22rem;font-weight:800;margin:12px 0 8px;" data-slot="pillar_3_title">Junioren A bis G</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:14px;" data-slot="pillar_3_desc">
              Strukturierte Nachwuchsarbeit über alle Altersstufen: Von den A-, B- und C-Junioren über vier D-Teams (9er &amp; 7er) bis zum Kinderfussball der E-, F- und G-Junioren.
            </p>
            <div class="pillar-tags">
              <span class="pillar-tag">Jun. A</span>
              <span class="pillar-tag">B1 &amp; B2</span>
              <span class="pillar-tag">C1–C3</span>
              <span class="pillar-tag">D1/D2 (9er &amp; 7er)</span>
              <span class="pillar-tag">E1–E4</span>
              <span class="pillar-tag">F1–F4 &amp; G</span>
            </div>
          </div>
          <div style="padding-top:12px;border-top:1px solid var(--border-light);font-size:0.8rem;color:var(--text-muted);">
            <strong>Leiter Junioren:</strong> Luigi Schiavano · Koord.: O. Otero &amp; G. Gennaro
          </div>
          <a href="herren-1.html#alle-teams-matrix" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Alle 17 Junioren-Teams ansehen</span>
          </a>
        </div>

        <!-- Säule 4: Juniorinnen U16 bis F -->
        <div class="pillar-card">
          <div>
            <span class="pillar-count">8 Mannschaften</span>
            <h3 style="font-size:1.22rem;font-weight:800;margin:12px 0 8px;" data-slot="pillar_4_title">Juniorinnen U16 bis F</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:14px;" data-slot="pillar_4_desc">
              Eigene Mädchenteams von den F- und E-Juniorinnen über D7er, D9er und U14 Mädchen bis zu den C-, B-Juniorinnen und Frauen U16, der direkte Weg in unsere Aktivteams.
            </p>
            <div class="pillar-tags">
              <span class="pillar-tag">Frauen U16</span>
              <span class="pillar-tag">B &amp; C Juniorinnen</span>
              <span class="pillar-tag">U14 Mädchen</span>
              <span class="pillar-tag">D9er &amp; D7er</span>
              <span class="pillar-tag">E &amp; F Juniorinnen</span>
            </div>
          </div>
          <div style="padding-top:12px;border-top:1px solid var(--border-light);font-size:0.8rem;color:var(--text-muted);">
            <strong>Leiter Juniorinnen:</strong> Mario De Meo · Koord.: L. Mussolin &amp; A. Paradiso
          </div>
          <a href="herren-1.html#alle-teams-matrix" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">
            <span>Alle 8 Juniorinnen-Teams ansehen</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- 4. SPORTPLATZ ZELGLI, CLUBHAUS, VORSTAND & 100+ JAHRE GESCHICHTE -->
  <section id="zelgli-verein" data-section="zelgli-verein" style="background-color:#FFFFFF;border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="club_kicker">HEIMSTÄTTE · CLUB-BEIZLI · VORSTAND · CHRONIK</div>
        <h2 class="section-title" data-slot="club_title">Sportanlage Zelgli, Clubhaus &amp; Vereinsführung.</h2>
        <p class="section-desc" data-slot="club_desc">
          Seit dem Einzug auf der neuerbauten Sportanlage Zelgli im Jahr 1982 schlägt unser Vereinsherz «im Rohr» in 8952 Schlieren, mit Hauptplatz, Kunstrasen, unserem gemütlichen Club-Beizli und einem engagierten Vorstand.
        </p>
      </div>

      <!-- Zelgli & Clubhaus 2-Column Showcase -->
      <div class="grid-2" style="margin-bottom:44px;">
        <article class="card">
          <div class="card-media" style="height:240px;">
            <img src="images/zelgli-luftbild.webp" alt="Luftbild Fussballanlage Zelgli 8952 Schlieren" width="580" height="240" loading="lazy" decoding="async" data-slot="zelgli_img">
            <span class="card-badge">Sportanlage Zelgli («im Rohr»)</span>
          </div>
          <div class="card-body">
            <h3 class="card-title" data-slot="zelgli_title">Fussballanlage Zelgli, 8952 Schlieren</h3>
            <p class="card-text" data-slot="zelgli_desc">
              Unsere Heimstätte umfasst den grossen Hauptplatz (Platz 1 mit Flutlicht und Bandenwerbung), die Trainings- und Wettkampfplätze 2 &amp; 3 (Natur- und Kunstrasen) sowie das Garderobengebäude.
            </p>
            <div class="card-meta-list">
              <div class="card-meta-item">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                <span><strong>Standort:</strong> Sportplatz Zelgli (im Rohr), 8952 Schlieren · Postfach</span>
              </div>
              <div class="card-meta-item">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="20 6 9 17 4 12"/></svg>
                <span><strong>Platzwart &amp; Anlage:</strong> Müslüm Bozan (079 260 63 63 · m.bozan@fcschlieren.ch)</span>
              </div>
            </div>
          </div>
        </article>

        <article class="card">
          <div class="card-media" style="height:240px;">
            <img src="images/clubhaus-beizli-1.webp" alt="Clubhaus und Beizli FC Schlieren" width="580" height="240" loading="lazy" decoding="async" data-slot="beizli_img">
            <span class="card-badge">Club-Beizli · 40–50 Sitzplätze</span>
          </div>
          <div class="card-body">
            <h3 class="card-title" data-slot="beizli_title">Clubhaus &amp; Beizli FC Schlieren</h3>
            <p class="card-text" data-slot="beizli_desc">
              Das rauchfreie Club-Beizli bietet 40 bis 50 gemütliche Innensitzplätze, eine grosse Terrasse direkt am Hauptplatz sowie Beamer und Leinwand für Mannschaftssitzungen, Theorieblöcke oder Vereinsanlässe.
            </p>
            <div class="card-meta-list">
              <div class="card-meta-item">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                <span><strong>Öffnungszeiten:</strong> Mo–Fr 16:45 – 23:00 Uhr · Sa/So gemäss Spielbetrieb</span>
              </div>
              <div class="card-meta-item">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                <span><strong>Reservation &amp; Wirt:</strong> Müslüm Bozan · Tel. 079 260 63 63</span>
              </div>
            </div>
          </div>
        </article>
      </div>

      <!-- 100+ Jahre Geschichte (Original-Meilensteine) -->
      <div style="background-color:var(--bg-muted);border:1px solid var(--border-light);border-radius:var(--radius-md);padding:28px;margin-bottom:44px;">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;">
          <div>
            <div class="section-kicker" style="margin-bottom:6px;">VEREINSGESCHICHTE SEIT 1921</div>
            <h3 style="font-size:1.4rem;font-weight:800;">Vom Platz «am Kanal» über Ceylon bis zum 100-Jahr-Jubiläum.</h3>
          </div>
          <img src="images/geschichte-chronik.webp" alt="Historische Vereinschronik FC Schlieren" width="180" height="64" loading="lazy" decoding="async" style="border-radius:var(--radius-sm);object-fit:cover;height:64px;width:180px;">
        </div>

        <div class="timeline-grid">
          <div class="timeline-box">
            <div class="timeline-year">21. März 1921</div>
            <p class="timeline-text">Offizielle Gründung des FC Schlieren (1. Präsident Emil Wild, erster Sportplatz «am Kanal»). 1922 Beitritt zum SFV, 1929 Aufstieg in die Serie B und 1932 Gründung der 1. Junioren-Mannschaft.</p>
          </div>
          <div class="timeline-box">
            <div class="timeline-year">1968 &amp; 1970</div>
            <p class="timeline-text">Saison 1968/69 Zürcher Regionalmeister der 2. Liga. 1970 legendäre dreiwöchige Asien-Reise nach Bangkok, Singapur, Hongkong und Ceylon, mit Freundschaftsspiel vor 11'000 Zuschauern.</p>
          </div>
          <div class="timeline-box">
            <div class="timeline-year">1973 &amp; 1979</div>
            <p class="timeline-text">1973 Gründung der Supporter-Vereinigung. 1975 und 1978 zweifacher Gewinn des Limmattal-Cups. 1979 Gründung der Frauenabteilung des FC Schlieren als Pionierverein der Region.</p>
          </div>
          <div class="timeline-box">
            <div class="timeline-year">1982 – 2026</div>
            <p class="timeline-text">1982 Einzug auf der neuerbauten Sportanlage Zelgli. 1997 Gründung des Business-Clubs. 2021 grosses 100-Jahr-Jubiläum, heute Heimat für 33 Teams im Limmattal.</p>
          </div>
        </div>
      </div>

      <!-- Vorstand (6 Original-Mitglieder) -->
      <div>
        <div class="section-kicker" style="margin-bottom:6px;">VEREINSFÜHRUNG &amp; ANSPRECHPARTNER</div>
        <h3 style="font-size:1.45rem;font-weight:800;margin-bottom:6px;">Der Vorstand des FC Schlieren</h3>
        <p style="font-size:0.92rem;color:var(--text-body);">Direkte Erreichbarkeit für Mitglieder, Eltern, Vereine und Partner.</p>

        <div class="board-grid">
          <div class="board-card">
            <span class="board-role">Präsident</span>
            <div class="board-name">Roger Küng</div>
            <div class="board-links">
              <a href="mailto:r.kueng@fcschlieren.ch">r.kueng@fcschlieren.ch</a>
              <a href="tel:+41794002093">079 400 20 93</a>
            </div>
          </div>

          <div class="board-card">
            <span class="board-role">Leiterin Geschäftsstelle &amp; Spielbetrieb</span>
            <div class="board-name">Jana Seifriz</div>
            <div class="board-links">
              <a href="mailto:j.seifriz@fcschlieren.ch">j.seifriz@fcschlieren.ch</a>
              <a href="tel:+41792424156">079 242 41 56</a>
            </div>
          </div>

          <div class="board-card">
            <span class="board-role">Leiter Finanzen</span>
            <div class="board-name">Luigi Voci</div>
            <div class="board-links">
              <a href="mailto:l.voci@fcschlieren.ch">l.voci@fcschlieren.ch</a>
              <a href="tel:+41797883324">079 788 33 24</a>
            </div>
          </div>

          <div class="board-card">
            <span class="board-role">Leiter Junioren (A bis G)</span>
            <div class="board-name">Luigi Schiavano</div>
            <div class="board-links">
              <a href="mailto:l.schiavano@fcschlieren.ch">l.schiavano@fcschlieren.ch</a>
              <a href="tel:+41791095288">079 109 52 88</a>
            </div>
          </div>

          <div class="board-card">
            <span class="board-role">Leiter Juniorinnen (U16 bis F)</span>
            <div class="board-name">Mario De Meo</div>
            <div class="board-links">
              <a href="mailto:m.demeo@fcschlieren.ch">m.demeo@fcschlieren.ch</a>
              <a href="tel:+41793543723">079 354 37 23</a>
            </div>
          </div>

          <div class="board-card">
            <span class="board-role">Leiter Aktive (Herren &amp; Frauen)</span>
            <div class="board-name">Zoran Perak</div>
            <div class="board-links">
              <a href="mailto:z.perak@fcschlieren.ch">z.perak@fcschlieren.ch</a>
              <a href="tel:+41762642022">076 264 20 22</a>
            </div>
          </div>
        </div>

        <!-- Weitere Funktionäre Kompaktleiste -->
        <div style="margin-top:16px;padding:16px 20px;background-color:var(--fcs-blue-soft);border:1px solid #BAE6FD;border-radius:var(--radius-md);font-size:0.84rem;color:var(--fcs-navy);display:flex;flex-wrap:wrap;gap:18px;align-items:center;justify-content:space-between;">
          <div>
            <strong>Weitere Funktionäre:</strong>
            Roger Mehr (Leiter Spielbetrieb · r.mehr@fcschlieren.ch · 079 402 83 87) ·
            Oscar Otero (Koord. D &amp; E Jun.) ·
            Gianfranco Gennaro (Koord. F &amp; G Jun.) ·
            Luca Mussolin &amp; Angela Paradiso (Koord. Juniorinnen) ·
            Sven Seifriz (J+S Coach &amp; Web · s.seifriz@fcschlieren.ch) ·
            Céline Bürgisser (Material · c.buergisser@fcschlieren.ch) ·
            Dani Galantucci (Sponsoring · d.galantucci@fcschlieren.ch)
          </div>
          <a href="kontakt.html" class="btn-cta btn-cta-primary btn-sm">Direkt zur Vereins-Zentrale</a>
        </div>
      </div>
    </div>
  </section>

  <!-- 5. ACP LIVE SOCIAL WALL -->
  <section id="social-wall" data-section="social-media">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="social_kicker">LIVE VOM SPORTPLATZ ZELGLI · VEREINSLEBEN AKTUELL</div>
        <h2 class="section-title" data-slot="social_title">Einblicke aus Spielbetrieb, Nachwuchs &amp; Vereinsalltag.</h2>
        <p class="section-desc" data-slot="social_desc">
          Aktuelle Impressionen unserer Aktivmannschaften, Nachwuchs-Turniere und Vereinsanlässe auf der Sportanlage Zelgli.
        </p>
      </div>

      <div class="social-filter-bar" role="tablist" aria-label="Beiträge filtern">
        <button type="button" class="social-tab-btn active" onclick="wpFilterSocial('all', this)">Alle Beiträge</button>
        <button type="button" class="social-tab-btn" onclick="wpFilterSocial('aktive', this)">Aktive Herren &amp; Frauen</button>
        <button type="button" class="social-tab-btn" onclick="wpFilterSocial('nachwuchs', this)">Fussballschule &amp; Nachwuchs</button>
        <button type="button" class="social-tab-btn" onclick="wpFilterSocial('verein', this)">Zelgli &amp; Sponsoren</button>
      </div>

      <div class="grid-3" id="wpSocialGrid">
        <article class="card wp-social-item" data-cat="aktive">
          <div class="card-media">
            <img src="images/team-herren-1.webp" alt="FC Schlieren Herren 1 Teamfoto" width="420" height="210" loading="lazy" decoding="async" data-slot="social_1_img">
            <span class="card-badge">Herren 1 · Heimspiel Zelgli</span>
          </div>
          <div class="card-body">
            <div style="font-size:0.76rem;font-weight:700;color:var(--fcs-blue);text-transform:uppercase;">1. Mannschaft · Aktive Herren</div>
            <h3 class="card-title" style="font-size:1.08rem;" data-slot="social_1_title">Voller Einsatz auf Platz 1 mit Hauptsponsor Emil Frey AG Schlieren</h3>
            <p class="card-text" data-slot="social_1_text">
              Unser Fanionteam unter Trainer Diego Bürger und Co-Trainer Livio Sanseverino bedankt sich bei den zahlreichen Zuschauern und Supportern auf dem Zelgli.
            </p>
          </div>
          <div class="card-footer">
            <a href="herren-1.html?team=herren1" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">Zum Kader Herren 1 (19 Spieler)</a>
          </div>
        </article>

        <article class="card wp-social-item" data-cat="aktive">
          <div class="card-media">
            <img src="images/team-frauen-1.webp" alt="FC Schlieren Frauen 1 Teamfoto" width="420" height="210" loading="lazy" decoding="async" data-slot="social_2_img">
            <span class="card-badge">Frauen 1 · Tradition seit 1979</span>
          </div>
          <div class="card-body">
            <div style="font-size:0.76rem;font-weight:700;color:var(--fcs-blue);text-transform:uppercase;">Frauenabteilung · 3 Aktiv- &amp; 8 Nachwuchsteams</div>
            <h3 class="card-title" style="font-size:1.08rem;" data-slot="social_2_title">Starke Frauen-Abteilung mit Partner J.F. Jost &amp; Co. &amp; Waser Facility Management</h3>
            <p class="card-text" data-slot="social_2_text">
              Drei aktive Frauenteams und acht Juniorinnen-Mannschaften machen den FC Schlieren zu einem Leuchtturm im Zürcher Frauen- und Mädchenfussball.
            </p>
          </div>
          <div class="card-footer">
            <a href="herren-1.html?team=frauen1" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">Zum Kader Frauen 1 (17 Spielerinnen)</a>
          </div>
        </article>

        <article class="card wp-social-item" data-cat="nachwuchs verein">
          <div class="card-media">
            <img src="images/zelgli-hauptplatz.webp" alt="Sportplatz Zelgli Hauptplatz FC Schlieren" width="420" height="210" loading="lazy" decoding="async" data-slot="social_3_img">
            <span class="card-badge">Zelgli · Nachwuchs &amp; Partner</span>
          </div>
          <div class="card-body">
            <div style="font-size:0.76rem;font-weight:700;color:var(--fcs-blue);text-transform:uppercase;">Fussballschule &amp; Vereinsleben</div>
            <h3 class="card-title" style="font-size:1.08rem;" data-slot="social_3_title">Mittwochnachmittag auf dem Zelgli: Unsere Jüngsten (Jg. 2016–2022) am Ball</h3>
            <p class="card-text" data-slot="social_3_text">
              Jeden Mittwoch von 16:15 bis 17:45 Uhr trainieren die Kinder der Fussballschule auf dem Zelgli, während im Club-Beizli bei Müslüm Bozan für Eltern gesorgt ist.
            </p>
          </div>
          <div class="card-footer">
            <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-outline btn-sm" style="width:100%;">Schnuppertraining anfragen</a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- 6. UNSERE SPONSOREN, GÖNNER & PARTNER (100% ORIGINAL-BESTAND) -->
  <section id="sponsoren" data-section="sponsoren" style="background-color:#FFFFFF;border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="sponsors_kicker">HERZLICHEN DANK AN UNSERE PARTNER</div>
        <h2 class="section-title" data-slot="sponsors_title">Unsere Gold-, Silber- und Bronze-Sponsoren.</h2>
        <p class="section-desc" data-slot="sponsors_desc">
          Ein herzliches Dankeschön an unsere treuen Haupt-, Silber- und Bronze-Sponsoren, die Supporter-Vereinigung (seit 1973) und den Business-Club (seit 1997). Ihr Engagement ermöglicht den Spielbetrieb von 33 Mannschaften auf dem Zelgli.
        </p>
      </div>

      <!-- TIER 1: GOLD SPONSOREN (2) -->
      <div class="sponsor-tier-block">
        <div class="sponsor-tier-header">
          <span class="sponsor-tier-badge tier-gold">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            <span>GOLD SPONSOREN &amp; HAUPTSPONSOREN</span>
          </span>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Offizielle Hauptpartner Herren 1 &amp; Frauen 1</span>
        </div>

        <div class="sponsors-gold-grid">
          <a href="http://www.emilfrey.ch/schlieren" target="_blank" rel="noopener noreferrer" class="sponsor-card gold-card">
            <div class="sponsor-logo-wrap">
              <img src="images/sponsors/gold-01-emil-frey-ag.jpg" alt="Emil Frey AG Schlieren – Gold Sponsor FC Schlieren" width="320" height="120" loading="lazy" decoding="async" data-slot="sponsor_gold_1_img">
            </div>
            <div>
              <div class="sponsor-name" data-slot="sponsor_gold_1_name">Emil Frey AG, Schlieren</div>
              <div class="sponsor-role-tag">Gold-Sponsor · Offizieller Hauptsponsor Herren 1 · emilfrey.ch/schlieren</div>
            </div>
          </a>

          <a href="http://www.lilie-schlieren.ch" target="_blank" rel="noopener noreferrer" class="sponsor-card gold-card">
            <div class="sponsor-logo-wrap">
              <img src="images/sponsors/gold-02-j-f-jost-co.jpg" alt="J.F. Jost und Co. – Gold Sponsor FC Schlieren" width="320" height="120" loading="lazy" decoding="async" data-slot="sponsor_gold_2_img">
            </div>
            <div>
              <div class="sponsor-name" data-slot="sponsor_gold_2_name">J.F. Jost &amp; Co.</div>
              <div class="sponsor-role-tag">Gold-Sponsor · Offizieller Hauptsponsor Frauen 1 · lilie-schlieren.ch</div>
            </div>
          </a>
        </div>
      </div>

      <!-- TIER 2: SILBER SPONSOREN (3) -->
      <div class="sponsor-tier-block">
        <div class="sponsor-tier-header">
          <span class="sponsor-tier-badge tier-silver">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>
            <span>SILBER SPONSOREN</span>
          </span>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">3 offizielle Silber-Partner</span>
        </div>

        <div class="sponsors-silver-grid">
          <a href="https://www.sopex.ch/" target="_blank" rel="noopener noreferrer" class="sponsor-card">
            <div class="sponsor-logo-wrap">
              <img src="images/sponsors/silver-01-sopex.jpg" alt="SOPEX – Silber Sponsor FC Schlieren" width="240" height="96" loading="lazy" decoding="async" data-slot="sponsor_silver_1_img">
            </div>
            <div>
              <div class="sponsor-name" data-slot="sponsor_silver_1_name">SOPEX</div>
              <div class="sponsor-role-tag">Silber-Sponsor · sopex.ch</div>
            </div>
          </a>

          <div class="sponsor-card">
            <div class="sponsor-logo-wrap">
              <img src="images/sponsors/silver-02-vr-ag.jpg" alt="VR AG – Silber Sponsor FC Schlieren" width="240" height="96" loading="lazy" decoding="async" data-slot="sponsor_silver_2_img">
            </div>
            <div>
              <div class="sponsor-name" data-slot="sponsor_silver_2_name">VR AG</div>
              <div class="sponsor-role-tag">Silber-Sponsor · Region Schlieren</div>
            </div>
          </div>

          <div class="sponsor-card">
            <div class="sponsor-logo-wrap">
              <img src="images/sponsors/silver-03-waser-facility-managment.png" alt="Waser Facility Management – Silber Sponsor FC Schlieren" width="240" height="96" loading="lazy" decoding="async" data-slot="sponsor_silver_3_img">
            </div>
            <div>
              <div class="sponsor-name" data-slot="sponsor_silver_3_name">Waser Facility Management</div>
              <div class="sponsor-role-tag">Silber-Sponsor &amp; Co-Sponsor Frauen 1</div>
            </div>
          </div>
        </div>
      </div>

      <!-- TIER 3: BRONZE SPONSOREN (6) -->
      <div class="sponsor-tier-block">
        <div class="sponsor-tier-header">
          <span class="sponsor-tier-badge tier-bronze">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span>BRONZE SPONSOREN &amp; INSTITUTIONELLE PARTNER</span>
          </span>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">6 offizielle Bronze-Partner</span>
        </div>

        <div class="sponsors-bronze-grid">
          <a href="http://www.pizzeria-corona.ch" target="_blank" rel="noopener noreferrer" class="sponsor-card">
            <div class="sponsor-logo-wrap" style="height:86px;">
              <img src="images/sponsors/bronze-01-corona-gastro-ag.jpg" alt="Corona Gastro AG Pizzeria Corona Schlieren" width="200" height="80" loading="lazy" decoding="async" data-slot="sponsor_bronze_1_img">
            </div>
            <div>
              <div class="sponsor-name">Corona Gastro AG</div>
              <div class="sponsor-role-tag">Bronze-Sponsor · pizzeria-corona.ch</div>
            </div>
          </a>

          <a href="http://www.physio-welt.ch" target="_blank" rel="noopener noreferrer" class="sponsor-card">
            <div class="sponsor-logo-wrap" style="height:86px;">
              <img src="images/sponsors/bronze-02-physio-welt.png" alt="Physio Welt Schlieren" width="200" height="80" loading="lazy" decoding="async" data-slot="sponsor_bronze_2_img">
            </div>
            <div>
              <div class="sponsor-name">Physio Welt</div>
              <div class="sponsor-role-tag">Bronze-Sponsor · physio-welt.ch</div>
            </div>
          </a>

          <a href="http://www.seifrizag.ch" target="_blank" rel="noopener noreferrer" class="sponsor-card">
            <div class="sponsor-logo-wrap" style="height:86px;">
              <img src="images/sponsors/bronze-03-seifriz-ag.jpg" alt="Seifriz AG Schlieren" width="200" height="80" loading="lazy" decoding="async" data-slot="sponsor_bronze_3_img">
            </div>
            <div>
              <div class="sponsor-name">Seifriz AG</div>
              <div class="sponsor-role-tag">Bronze-Sponsor · seifrizag.ch</div>
            </div>
          </a>

          <div class="sponsor-card">
            <div class="sponsor-logo-wrap" style="height:86px;">
              <img src="images/sponsors/bronze-04-stadt-schlieren.png" alt="Stadt Schlieren" width="200" height="80" loading="lazy" decoding="async" data-slot="sponsor_bronze_4_img">
            </div>
            <div>
              <div class="sponsor-name">Stadt Schlieren</div>
              <div class="sponsor-role-tag">Standortgemeinde &amp; Sportförderung</div>
            </div>
          </div>

          <a href="https://syna.ch/zuerich-schaffhausen/" target="_blank" rel="noopener noreferrer" class="sponsor-card">
            <div class="sponsor-logo-wrap" style="height:86px;">
              <img src="images/sponsors/bronze-05-syna-die-gewerkschaft.jpg" alt="Syna Die Gewerkschaft Zürich Schaffhausen" width="200" height="80" loading="lazy" decoding="async" data-slot="sponsor_bronze_5_img">
            </div>
            <div>
              <div class="sponsor-name">Syna - Die Gewerkschaft</div>
              <div class="sponsor-role-tag">Bronze-Sponsor · syna.ch</div>
            </div>
          </a>

          <a href="http://www.zkb.ch" target="_blank" rel="noopener noreferrer" class="sponsor-card">
            <div class="sponsor-logo-wrap" style="height:86px;">
              <img src="images/sponsors/bronze-06-zuercher-kantonalbank-filiale-schlieren.jpg" alt="Zürcher Kantonalbank Filiale Schlieren" width="200" height="80" loading="lazy" decoding="async" data-slot="sponsor_bronze_6_img">
            </div>
            <div>
              <div class="sponsor-name">Zürcher Kantonalbank Filiale Schlieren</div>
              <div class="sponsor-role-tag">Bronze-Sponsor · zkb.ch</div>
            </div>
          </a>
        </div>
      </div>

      <!-- SUPPORTER-VEREINIGUNG, BUSINESS-CLUB & BANDENWERBUNG -->
      <div class="grid-3" style="margin-top:36px;">
        <div class="card" style="padding:24px;background-color:var(--fcs-navy);color:#FFFFFF;border-color:var(--fcs-navy);">
          <div>
            <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:14px;">
              <span class="top-bar-badge">SEIT 1973 · RUND 120 MITGLIEDER</span>
              <img src="images/logo-supporter.webp" alt="Supporter-Vereinigung FC Schlieren" width="84" height="36" loading="lazy" decoding="async" style="object-fit:contain;background:#fff;padding:4px;border-radius:4px;">
            </div>
            <h3 style="color:#FFFFFF;font-size:1.18rem;font-weight:800;margin-bottom:8px;">Supporter-Vereinigung FC Schlieren</h3>
            <p style="font-size:0.88rem;color:#E2E8F0;margin-bottom:14px;">
              Unterstützt gezielt unsere Junioren- und Aktivabteilung. Freier Eintritt zu sämtlichen Heimspielen auf dem Zelgli sowie Einladung zum jährlichen Supporter-Apéro (Präsident: Dany Tännler).
            </p>
            <div style="font-size:0.84rem;color:var(--fcs-gold);font-weight:700;margin-bottom:16px;">
              Einzelmitgliedschaft: CHF 150.– / Jahr · Paarmitgliedschaft: CHF 250.– / Jahr
            </div>
          </div>
          <a href="kontakt.html?thema=sponsoring" class="btn-cta btn-cta-gold btn-sm" style="width:100%;">Supporter werden</a>
        </div>

        <div class="card" style="padding:24px;background-color:var(--fcs-navy);color:#FFFFFF;border-color:var(--fcs-navy);">
          <div>
            <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:14px;">
              <span class="top-bar-badge">SEIT 1997 · 49 FIRMENMITGLIEDER</span>
              <img src="images/logo-businessclub.webp" alt="Business-Club FC Schlieren" width="84" height="36" loading="lazy" decoding="async" style="object-fit:contain;background:#fff;padding:4px;border-radius:4px;">
            </div>
            <h3 style="color:#FFFFFF;font-size:1.18rem;font-weight:800;margin-bottom:8px;">Business-Club FC Schlieren</h3>
            <p style="font-size:0.88rem;color:#E2E8F0;margin-bottom:14px;">
              Das Unternehmer-Netzwerk im Limmattal mit monatlichem Business-Lunch im Restaurant Corona und gemeinsamen Events (Vorstand: Thomas Bolliger, Diego Würmli, Jürg Zahner, Monika Höhn).
            </p>
            <div style="font-size:0.84rem;color:var(--fcs-gold);font-weight:700;margin-bottom:16px;">
              Jahresbeitrag Business-Club: CHF 850.– / Jahr
            </div>
          </div>
          <a href="kontakt.html?thema=sponsoring" class="btn-cta btn-cta-gold btn-sm" style="width:100%;">Business-Club anfragen</a>
        </div>

        <div class="card" style="padding:24px;background-color:var(--fcs-blue-soft);border-color:#93C5FD;">
          <div>
            <span class="pillar-count" style="margin-bottom:14px;">HAUPTPLATZ ZELGLI · SICHTBARKEIT</span>
            <h3 style="font-size:1.18rem;font-weight:800;margin-bottom:8px;">Bandenwerbung, Dress- &amp; Matchball-Sponsoring</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:14px;">
              Präsentiere dein Unternehmen direkt am Hauptplatz 1 der Sportanlage Zelgli vor tausenden Spielerinnen, Spielern, Eltern und Zuschauern pro Saison (Kontakt: Dani Galantucci).
            </p>
            <div style="font-size:0.84rem;color:var(--fcs-navy);font-weight:700;margin-bottom:16px;">
              Bandenwerbung Platz 1 (3 Meter): CHF 120.– / Laufmeter = CHF 360.– / Jahr
            </div>
          </div>
          <a href="kontakt.html?thema=sponsoring" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">Sponsoring &amp; Bande anfragen</a>
        </div>
      </div>
    </div>
  </section>

  <script>
    function wpFilterSocial(cat, btn) {
      var btns = document.querySelectorAll('.social-tab-btn');
      for (var i = 0; i < btns.length; i++) btns[i].classList.remove('active');
      if (btn) btn.classList.add('active');
      var items = document.querySelectorAll('.wp-social-item');
      for (var j = 0; j < items.length; j++) {
        var c = items[j].getAttribute('data-cat') || '';
        if (cat === 'all' || c.indexOf(cat) !== -1) {
          items[j].style.display = 'flex';
        } else {
          items[j].style.display = 'none';
        }
      }
    }
  </script>
"""

HERREN_1_CSS = """
    .architect-banner {
      background: linear-gradient(135deg, #0B1324 0%, #0F2547 100%);
      color: #FFFFFF;
      border-bottom: 3px solid var(--fcs-gold);
      padding: 28px 0;
    }
    .architect-box {
      background-color: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(253, 197, 0, 0.45);
      border-left: 5px solid var(--fcs-gold);
      border-radius: var(--radius-md);
      padding: 20px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      flex-wrap: wrap;
    }
    .team-switcher-bar {
      display: inline-flex;
      flex-wrap: wrap;
      gap: 10px;
      background-color: var(--bg-muted);
      padding: 6px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-strong);
      margin-bottom: 32px;
    }
    .team-switch-btn {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.9rem;
      font-weight: 800;
      padding: 12px 22px;
      border-radius: var(--radius-sm);
      border: none;
      background: transparent;
      color: var(--text-body);
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .team-switch-btn.active {
      background-color: var(--fcs-blue);
      color: #FFFFFF;
      box-shadow: var(--shadow-sm);
    }
    .team-switch-badge {
      font-size: 0.68rem;
      padding: 2px 7px;
      border-radius: var(--radius-sm);
      background-color: rgba(253, 197, 0, 0.22);
      color: var(--fcs-gold);
      text-transform: uppercase;
    }
    .team-pane {
      display: none;
    }
    .team-pane.active {
      display: block;
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
      grid-template-columns: 1.25fr 0.75fr;
    }
    .team-photo-stage {
      background-color: var(--fcs-navy);
      position: relative;
      min-height: 360px;
    }
    .team-photo-stage img {
      width: 100%;
      height: 100%;
      max-height: 440px;
      object-fit: cover;
    }
    .team-info-stage {
      padding: 32px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 20px;
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
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-bottom: 40px;
    }
    .staff-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 18px;
      display: flex;
      align-items: center;
      gap: 16px;
      box-shadow: var(--shadow-sm);
    }
    .staff-avatar {
      width: 74px;
      height: 88px;
      border-radius: var(--radius-sm);
      object-fit: cover;
      background-color: var(--fcs-navy);
      flex-shrink: 0;
      border: 2px solid var(--fcs-blue);
    }
    .staff-avatar-placeholder {
      width: 74px;
      height: 88px;
      border-radius: var(--radius-sm);
      background: linear-gradient(135deg, var(--fcs-navy) 0%, var(--fcs-blue) 100%);
      color: var(--fcs-gold);
      font-family: 'Montserrat', sans-serif;
      font-weight: 800;
      font-size: 1.2rem;
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
      border-bottom: 2px solid var(--fcs-blue-soft);
    }
    .roster-pos-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 1rem;
      font-weight: 800;
      color: var(--fcs-navy);
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
      width: 30px;
      height: 30px;
      border-radius: var(--radius-sm);
      background-color: var(--fcs-navy);
      color: var(--fcs-gold);
      font-family: 'Montserrat', sans-serif;
      font-size: 0.78rem;
      font-weight: 800;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .player-name {
      font-size: 0.86rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.25;
    }

    /* 33-Teams Matrix */
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
      gap: 12px;
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
      border-color: var(--fcs-blue);
      box-shadow: var(--shadow-sm);
      transform: translateY(-2px);
    }
    .matrix-team-btn.live-built {
      border: 2px solid var(--fcs-blue);
      background-color: var(--fcs-blue-soft);
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
      font-size: 0.92rem;
      font-weight: 800;
      color: var(--fcs-navy);
    }
    .matrix-status-pill {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.65rem;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      white-space: nowrap;
    }
    .pill-live {
      background-color: var(--fcs-green);
      color: #FFFFFF;
    }
    .pill-blueprint {
      background-color: var(--bg-muted);
      color: var(--text-muted);
      border: 1px solid var(--border-strong);
    }

    @media (max-width: 1080px) {
      .team-hero-grid, .roster-pos-grid {
        grid-template-columns: 1fr;
      }
      .staff-grid, .matrix-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    @media (max-width: 720px) {
      .staff-grid, .roster-player-list, .matrix-grid {
        grid-template-columns: 1fr;
      }
    }
"""

HERREN_1_BODY = """
  <!-- ORIENTIERUNGS-BANNER: BEISPIEL-TEAMS -->
  <section class="architect-banner" data-section="vorschau-hinweis">
    <div class="container">
      <div class="architect-box">
        <div style="max-width:780px;">
          <div class="section-kicker kicker-light" style="margin-bottom:6px;" data-slot="arch_kicker">BEISPIEL-ANSICHT · STELLVERTRETEND FÜR ALLE 33 MANNSCHAFTEN</div>
          <h1 style="color:#FFFFFF;font-size:clamp(1.45rem,2.5vw,2rem);font-weight:800;margin-bottom:8px;" data-slot="arch_title">
            Beispiel-Team-Seite: Herren 1 &amp; Frauen 1 (stellvertretend für alle 33 Teams)
          </h1>
          <p style="font-size:0.9rem;color:#E2E8F0;line-height:1.55;" data-slot="arch_desc">
            Der FC Schlieren stellt <strong>33 Mannschaften</strong>. Damit du als Vorstand oder Mitglied sofort erlebst, wie jede einzelne Mannschaftsseite künftig aussieht, haben wir hier die <strong>1. Mannschaft (Herren 1)</strong> und die <strong>Frauen 1</strong> komplett mit Original-Mannschaftsfoto, Spielerkader, Trainerstab und Sponsoren ausgebaut. Unten findest du zudem die interaktive <strong>33-Teams-Matrix</strong>.
          </p>
        </div>
        <div style="display:flex;flex-direction:column;gap:8px;max-width:100%;">
          <a href="team-update.html?team=1-mannschaft" class="btn-cta btn-cta-gold btn-sm" style="white-space:normal;text-align:center;">Mannschafts-Daten &amp; Kader einreichen (Trainer-Formular)</a>
          <a href="#alle-teams-matrix" class="btn-cta btn-cta-ghost-light btn-sm">Zur 33-Teams-Matrix springen</a>
          <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-ghost-light btn-sm">Probetraining anmelden</a>
        </div>
      </div>
    </div>
  </section>

  <!-- BEISPIEL-TEAM SEKTION (HERREN 1 & FRAUEN 1 UMSCHALTBAR) -->
  <section id="beispiel-team-detail" data-section="beispiel-team-detail">
    <div class="container">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;margin-bottom:12px;">
        <div class="team-switcher-bar" role="tablist" aria-label="Beispiel-Team auswählen">
          <button type="button" class="team-switch-btn active" id="tabBtnHerren1" onclick="wpSwitchTeam('herren1')">
            <span>Herren 1 – 1. Mannschaft</span>
            <span class="team-switch-badge">19 Spieler · Live</span>
          </button>
          <button type="button" class="team-switch-btn" id="tabBtnFrauen1" onclick="wpSwitchTeam('frauen1')">
            <span>Frauen 1 – 1. Mannschaft</span>
            <span class="team-switch-badge">17 Spielerinnen · Live</span>
          </button>
        </div>

        <div style="font-size:0.84rem;color:var(--text-muted);font-weight:600;">
          Sportchef Aktive: <strong>Zoran Perak</strong> (z.perak@fcschlieren.ch · 076 264 20 22)
        </div>
      </div>

      <!-- ================= TAB 1: HERREN 1 ================= -->
      <div class="team-pane active" id="paneHerren1">
        <div class="team-hero-card">
          <div class="team-hero-grid">
            <div class="team-photo-stage">
              <img src="images/team-herren-1.webp" alt="FC Schlieren Herren 1 Mannschaftsfoto" width="760" height="420" data-slot="h1_team_photo">
              <span class="card-badge">Herren 1 · 1. Mannschaft · Sportplatz Zelgli</span>
            </div>
            <div class="team-info-stage">
              <div>
                <div class="section-kicker" style="margin-bottom:8px;">FANIONTEAM AKTIVE HERREN</div>
                <h2 style="font-size:1.75rem;font-weight:800;margin-bottom:10px;" data-slot="h1_title">FC Schlieren · Herren 1</h2>
                <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:16px;" data-slot="h1_desc">
                  Unsere 1. Mannschaft trägt die Farben Blau-Gelb auf dem Hauptplatz der Sportanlage Zelgli. Unter Cheftrainer Diego Bürger, Co-Trainer Livio Sanseverino und Sportchef Zoran Perak steht das Team für leidenschaftlichen Offensivfussball im Limmattal.
                </p>

                <div class="card-meta-list" style="margin-bottom:16px;">
                  <div class="card-meta-item">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                    <span><strong>Heimstätte:</strong> Sportanlage Zelgli, Platz 1 (8952 Schlieren)</span>
                  </div>
                  <div class="card-meta-item">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
                    <span><strong>Cheftrainer:</strong> Diego Bürger · <strong>Co-Trainer:</strong> Livio Sanseverino</span>
                  </div>
                  <div class="card-meta-item">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/></svg>
                    <span><strong>Kader:</strong> 19 Spieler (2 Torhüter, 6 Verteidiger, 8 Mittelfeld, 3 Sturm)</span>
                  </div>
                </div>

                <!-- Team Sponsor -->
                <div class="team-sponsor-strip">
                  <img src="images/sponsors/gold-01-emil-frey-ag.jpg" alt="Emil Frey AG Schlieren Hauptsponsor Herren 1" width="96" height="44" loading="lazy" decoding="async">
                  <div style="font-size:0.8rem;">
                    <div style="font-weight:800;color:var(--fcs-navy);">Hauptsponsor Herren 1: Emil Frey AG, Schlieren</div>
                    <a href="http://www.emilfrey.ch/schlieren" target="_blank" rel="noopener noreferrer" style="color:var(--fcs-blue);font-weight:600;">www.emilfrey.ch/schlieren</a>
                  </div>
                </div>
              </div>

              <div style="display:flex;flex-wrap:wrap;gap:10px;">
                <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-primary btn-sm" style="flex:1;">
                  <span>Probetraining / Kontakt Herren 1</span>
                </a>
                <a href="https://fcschlieren.ch/files/filemanager/download/inline/14205da44ffad9f4e13bcefb6759042d" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-outline btn-sm" style="flex:1;">
                  <span>Matchprogramm (PDF)</span>
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- Trainer & Staff Herren 1 -->
        <h3 style="font-size:1.3rem;font-weight:800;margin-bottom:16px;">Trainer- &amp; Betreuerstab – Herren 1</h3>
        <div class="staff-grid">
          <div class="staff-card">
            <img src="images/staff-diego-buerger.webp" alt="Diego Bürger Trainer Herren 1 FC Schlieren" class="staff-avatar" width="74" height="88" loading="lazy" decoding="async" data-slot="h1_staff_1_img">
            <div>
              <span class="board-role">Cheftrainer Herren 1</span>
              <div class="board-name" data-slot="h1_staff_1_name">Diego Bürger</div>
              <div style="font-size:0.82rem;color:var(--text-body);margin-top:4px;">
                <a href="mailto:d.buerger@hotmail.com" style="color:var(--fcs-blue);">d.buerger@hotmail.com</a>
              </div>
            </div>
          </div>

          <div class="staff-card">
            <img src="images/staff-livio-sanseverino.webp" alt="Livio Sanseverino Co-Trainer Herren 1 FC Schlieren" class="staff-avatar" width="74" height="88" loading="lazy" decoding="async" data-slot="h1_staff_2_img">
            <div>
              <span class="board-role">Co-Trainer Herren 1</span>
              <div class="board-name" data-slot="h1_staff_2_name">Livio Sanseverino</div>
              <div style="font-size:0.82rem;color:var(--text-body);margin-top:4px;">
                1. Mannschaft · Sportplatz Zelgli
              </div>
            </div>
          </div>

          <div class="staff-card">
            <img src="images/staff-zoran-perak.webp" alt="Zoran Perak Sportchef Aktive FC Schlieren" class="staff-avatar" width="74" height="88" loading="lazy" decoding="async" data-slot="h1_staff_3_img">
            <div>
              <span class="board-role">Leiter Aktive / Sportchef</span>
              <div class="board-name" data-slot="h1_staff_3_name">Zoran Perak</div>
              <div style="font-size:0.82rem;color:var(--text-body);margin-top:4px;">
                <a href="mailto:z.perak@fcschlieren.ch" style="color:var(--fcs-blue);">z.perak@fcschlieren.ch</a> · 076 264 20 22
              </div>
            </div>
          </div>
        </div>

        <!-- Spielerkader Herren 1 (19 Original-Spieler) -->
        <h3 style="font-size:1.3rem;font-weight:800;margin-bottom:16px;">Offizielles Spielerkader – Herren 1 (19 Spieler)</h3>
        <div class="roster-pos-grid">
          <!-- Torhüter -->
          <div class="roster-pos-box">
            <div class="roster-pos-head">
              <span class="roster-pos-title">Torhüter</span>
              <span class="pillar-count">2 Spieler</span>
            </div>
            <div class="roster-player-list">
              <div class="player-pill"><span class="player-num">1</span><span class="player-name">Ardian Biljali</span></div>
              <div class="player-pill"><span class="player-num">12</span><span class="player-name">Sven Schnell</span></div>
            </div>
          </div>

          <!-- Sturm -->
          <div class="roster-pos-box">
            <div class="roster-pos-head">
              <span class="roster-pos-title">Sturm / Angriff</span>
              <span class="pillar-count">3 Spieler</span>
            </div>
            <div class="roster-player-list">
              <div class="player-pill"><span class="player-num">7</span><span class="player-name">Leon Buqaj</span></div>
              <div class="player-pill"><span class="player-num">10</span><span class="player-name">Patrick Vitiello</span></div>
              <div class="player-pill"><span class="player-num">23</span><span class="player-name">Eldin Kolenovic</span></div>
            </div>
          </div>

          <!-- Verteidigung -->
          <div class="roster-pos-box">
            <div class="roster-pos-head">
              <span class="roster-pos-title">Verteidigung</span>
              <span class="pillar-count">6 Spieler</span>
            </div>
            <div class="roster-player-list">
              <div class="player-pill"><span class="player-num">2</span><span class="player-name">Urban Brunner</span></div>
              <div class="player-pill"><span class="player-num">3</span><span class="player-name">Alex Costa</span></div>
              <div class="player-pill"><span class="player-num">5</span><span class="player-name">Andrés Pablos</span></div>
              <div class="player-pill"><span class="player-num">14</span><span class="player-name">Ilyas Dendic</span></div>
              <div class="player-pill"><span class="player-num">14</span><span class="player-name">Nail Gicic</span></div>
              <div class="player-pill"><span class="player-num">17</span><span class="player-name">Francesco Fragapane</span></div>
            </div>
          </div>

          <!-- Mittelfeld -->
          <div class="roster-pos-box">
            <div class="roster-pos-head">
              <span class="roster-pos-title">Mittelfeld</span>
              <span class="pillar-count">8 Spieler</span>
            </div>
            <div class="roster-player-list">
              <div class="player-pill"><span class="player-num">8</span><span class="player-name">Christian Romano</span></div>
              <div class="player-pill"><span class="player-num">9</span><span class="player-name">David Deuber</span></div>
              <div class="player-pill"><span class="player-num">11</span><span class="player-name">Teo Dukic</span></div>
              <div class="player-pill"><span class="player-num">13</span><span class="player-name">Loris Da Silva Marques</span></div>
              <div class="player-pill"><span class="player-num">15</span><span class="player-name">Laurent Sabedini</span></div>
              <div class="player-pill"><span class="player-num">18</span><span class="player-name">Augusto Silva Pereira</span></div>
              <div class="player-pill"><span class="player-num">20</span><span class="player-name">Michael Goncalves</span></div>
              <div class="player-pill"><span class="player-num">22</span><span class="player-name">Albion Hoti</span></div>
            </div>
          </div>
        </div>
      </div>

      <!-- ================= TAB 2: FRAUEN 1 ================= -->
      <div class="team-pane" id="paneFrauen1">
        <div class="team-hero-card">
          <div class="team-hero-grid">
            <div class="team-photo-stage">
              <img src="images/team-frauen-1.webp" alt="FC Schlieren Frauen 1 Mannschaftsfoto" width="760" height="420" loading="lazy" decoding="async" data-slot="f1_team_photo">
              <span class="card-badge">Frauen 1 · 1. Mannschaft · Seit 1979</span>
            </div>
            <div class="team-info-stage">
              <div>
                <div class="section-kicker" style="margin-bottom:8px;">FANIONTEAM AKTIVE FRAUEN · SEIT 1979</div>
                <h2 style="font-size:1.75rem;font-weight:800;margin-bottom:10px;" data-slot="f1_title">FC Schlieren · Frauen 1</h2>
                <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:16px;" data-slot="f1_desc">
                  Seit der Gründung der Frauenabteilung im Jahr 1979 gehört der FC Schlieren zu den Pioniervereinen im Schweizer Frauenfussball. Unser Fanionteam Frauen 1 wird von Konstantinos Vettas, Sergio Zamora und einem engagierten Spezialisten-Staff betreut.
                </p>

                <div class="card-meta-list" style="margin-bottom:16px;">
                  <div class="card-meta-item">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                    <span><strong>Heimstätte:</strong> Sportanlage Zelgli, 8952 Schlieren</span>
                  </div>
                  <div class="card-meta-item">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
                    <span><strong>Trainerduo:</strong> Konstantinos Vettas &amp; Sergio Zamora · <strong>Co-Trainer:</strong> Stefano Amato</span>
                  </div>
                  <div class="card-meta-item">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/></svg>
                    <span><strong>Kader:</strong> 17 Spielerinnen (inkl. Spielerinnen-Patronat)</span>
                  </div>
                </div>

                <!-- Team Sponsors Frauen 1 -->
                <div class="team-sponsor-strip">
                  <img src="images/sponsors/gold-02-j-f-jost-co.jpg" alt="J.F. Jost und Co. Hauptsponsor Frauen 1" width="96" height="44" loading="lazy" decoding="async">
                  <div style="font-size:0.8rem;">
                    <div style="font-weight:800;color:var(--fcs-navy);">Hauptsponsor: J.F. Jost &amp; Co. · Co-Sponsor: Waser Facility Management</div>
                    <a href="http://www.lilie-schlieren.ch" target="_blank" rel="noopener noreferrer" style="color:var(--fcs-blue);font-weight:600;">www.lilie-schlieren.ch</a>
                  </div>
                </div>
              </div>

              <div style="display:flex;flex-wrap:wrap;gap:10px;">
                <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-primary btn-sm" style="flex:1;">
                  <span>Probetraining / Kontakt Frauen 1</span>
                </a>
                <a href="kontakt.html?thema=sponsoring" class="btn-cta btn-cta-gold btn-sm" style="flex:1;">
                  <span>Spielerinnen-Patronat übernehmen</span>
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- Trainer & Staff Frauen 1 -->
        <h3 style="font-size:1.3rem;font-weight:800;margin-bottom:16px;">Trainer- &amp; Betreuerstab – Frauen 1</h3>
        <div class="staff-grid">
          <div class="staff-card">
            <img src="images/staff-konstantinos-vettas.webp" alt="Konstantinos Vettas Trainer Frauen 1" class="staff-avatar" width="74" height="88" loading="lazy" decoding="async">
            <div>
              <span class="board-role">Trainer Frauen 1</span>
              <div class="board-name">Konstantinos Vettas</div>
              <div style="font-size:0.82rem;color:var(--text-body);margin-top:4px;">
                <a href="mailto:costa.vettas@bluewin.ch" style="color:var(--fcs-blue);">costa.vettas@bluewin.ch</a> · 076 347 16 11
              </div>
            </div>
          </div>

          <div class="staff-card">
            <div class="staff-avatar-placeholder">SZ</div>
            <div>
              <span class="board-role">Trainer &amp; Co-Trainer</span>
              <div class="board-name">Sergio Zamora &amp; Stefano Amato</div>
              <div style="font-size:0.82rem;color:var(--text-body);margin-top:4px;">
                Trainerduo &amp; Assistenz Frauen 1
              </div>
            </div>
          </div>

          <div class="staff-card">
            <img src="images/staff-daniel-konrad.webp" alt="Daniel Konrad Torwarttrainer Frauen 1" class="staff-avatar" width="74" height="88" loading="lazy" decoding="async">
            <div>
              <span class="board-role">Torwarttrainer Frauen 1</span>
              <div class="board-name">Daniel Konrad &amp; Christian Leite Nieva</div>
              <div style="font-size:0.82rem;color:var(--text-body);margin-top:4px;">
                Torhüterinnen-Ausbildung
              </div>
            </div>
          </div>

          <div class="staff-card">
            <img src="images/staff-rahel-gaechter.webp" alt="Rahel Gächter Masseurin Frauen 1" class="staff-avatar" width="74" height="88" loading="lazy" decoding="async">
            <div>
              <span class="board-role">Medizinische Betreuung / Masseurin</span>
              <div class="board-name">Rahel Gächter</div>
              <div style="font-size:0.82rem;color:var(--text-body);margin-top:4px;">
                Physio &amp; Regeneration Frauen 1
              </div>
            </div>
          </div>

          <div class="staff-card">
            <img src="images/staff-zoran-perak.webp" alt="Zoran Perak Sportchef Aktive" class="staff-avatar" width="74" height="88" loading="lazy" decoding="async">
            <div>
              <span class="board-role">Sportchef Aktive</span>
              <div class="board-name">Zoran Perak</div>
              <div style="font-size:0.82rem;color:var(--text-body);margin-top:4px;">
                <a href="mailto:z.perak@fcschlieren.ch" style="color:var(--fcs-blue);">z.perak@fcschlieren.ch</a> · 076 264 20 22
              </div>
            </div>
          </div>
        </div>

        <!-- Spielerkader Frauen 1 (17 Original-Spielerinnen) -->
        <h3 style="font-size:1.3rem;font-weight:800;margin-bottom:16px;">Offizielles Spielerkader – Frauen 1 (17 Spielerinnen)</h3>
        <div class="roster-pos-grid">
          <div class="roster-pos-box">
            <div class="roster-pos-head">
              <span class="roster-pos-title">Torhüterinnen</span>
              <span class="pillar-count">2 Spielerinnen</span>
            </div>
            <div class="roster-player-list">
              <div class="player-pill"><span class="player-num">1</span><span class="player-name">Ramona Erismann</span></div>
              <div class="player-pill"><span class="player-num">23</span><span class="player-name">Annina Eigenmann</span></div>
            </div>
          </div>

          <div class="roster-pos-box">
            <div class="roster-pos-head">
              <span class="roster-pos-title">Verteidigung</span>
              <span class="pillar-count">4 Spielerinnen</span>
            </div>
            <div class="roster-player-list">
              <div class="player-pill"><span class="player-num">10</span><span class="player-name">Céline Bürgisser</span></div>
              <div class="player-pill"><span class="player-num">12</span><span class="player-name">Celiné Bürgler</span></div>
              <div class="player-pill"><span class="player-num">16</span><span class="player-name">Aliche Vono Oviedo</span></div>
              <div class="player-pill"><span class="player-num">20</span><span class="player-name">Leah Gächter</span></div>
            </div>
          </div>

          <div class="roster-pos-box">
            <div class="roster-pos-head">
              <span class="roster-pos-title">Mittelfeld</span>
              <span class="pillar-count">5 Spielerinnen</span>
            </div>
            <div class="roster-player-list">
              <div class="player-pill"><span class="player-num">6</span><span class="player-name">Anja Jasmin Michel</span></div>
              <div class="player-pill"><span class="player-num">9</span><span class="player-name">Saranda Hashani</span></div>
              <div class="player-pill"><span class="player-num">11</span><span class="player-name">Luana Bonfardin</span></div>
              <div class="player-pill"><span class="player-num">27</span><span class="player-name">Kathrin Rohr</span></div>
              <div class="player-pill"><span class="player-num">29</span><span class="player-name">Valerie Spiess</span></div>
            </div>
          </div>

          <div class="roster-pos-box">
            <div class="roster-pos-head">
              <span class="roster-pos-title">Sturm / Angriff</span>
              <span class="pillar-count">6 Spielerinnen</span>
            </div>
            <div class="roster-player-list">
              <div class="player-pill"><span class="player-num">17</span><span class="player-name">Sanja Mijovic</span></div>
              <div class="player-pill"><span class="player-num">18</span><span class="player-name">Stefanie Raschle</span></div>
              <div class="player-pill"><span class="player-num">19</span><span class="player-name">Norah Gächter</span></div>
              <div class="player-pill"><span class="player-num">21</span><span class="player-name">Chantal Rochat</span></div>
              <div class="player-pill"><span class="player-num">24</span><span class="player-name">Anna Davydenko</span></div>
              <div class="player-pill"><span class="player-num">30</span><span class="player-name">Melina Metzger</span></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ALLE 33 MANNSCHAFTEN IM ÜBERBLICK (MANNSCHAFTS-ÜBERSICHT) -->
  <section id="alle-teams-matrix" data-section="alle-teams-matrix" style="background-color:#FFFFFF;border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="matrix_kicker">MANNSCHAFTS-ÜBERSICHT · ALLE 33 MANNSCHAFTEN</div>
        <h2 class="section-title" data-slot="matrix_title">Alle 33 Mannschaften des FC Schlieren.</h2>
        <p class="section-desc" data-slot="matrix_desc">
          <strong>Herren 1</strong> und <strong>Frauen 1</strong> sind oben als vollständige Beispiel-Teams live ausgebaut. Klicke auf eines der weiteren 31 Teams, um die Team-Vorschau mit zuständiger Abteilungsleitung und direkter Probetraining-Anmeldung zu öffnen.
        </p>
      </div>

      <!-- Gruppe 1: Aktive Herren & Senioren (5 Teams) -->
      <div class="matrix-group-block">
        <div class="matrix-group-header">
          <h3 style="font-size:1.18rem;font-weight:800;">1. Aktive Herren &amp; Senioren (5 Teams)</h3>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Leitung: Zoran Perak (z.perak@fcschlieren.ch · 076 264 20 22)</span>
        </div>
        <div class="matrix-grid">
          <button type="button" class="matrix-team-btn live-built" onclick="wpSwitchTeam('herren1'); window.scrollTo({top: 260, behavior: 'smooth'});">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Herren 1</span>
              <span class="matrix-status-pill pill-live">Live ausgebaut</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-body);">1. Mannschaft · 19 Spieler · Trainer: Diego Bürger</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: Herren 2', 'Aktive Herren (2. Mannschaft)', 'Zoran Perak (z.perak@fcschlieren.ch · 076 264 20 22)', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Herren 2</span>
              <span class="matrix-status-pill pill-blueprint">Vorschau</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">2. Mannschaft · Sportplatz Zelgli</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: Senioren 30+', 'Senioren-Abteilung FC Schlieren', 'Zoran Perak &amp; Roger Mehr (r.mehr@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Senioren 30+</span>
              <span class="matrix-status-pill pill-blueprint">Vorschau</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Meisterschaft &amp; Cup · Sportplatz Zelgli</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: Senioren 40+', 'Senioren-Abteilung FC Schlieren', 'Zoran Perak &amp; Roger Mehr (r.mehr@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Senioren 40+</span>
              <span class="matrix-status-pill pill-blueprint">Vorschau</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Senioren 40+ · Sportplatz Zelgli</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: Senioren 50+', 'Senioren-Abteilung FC Schlieren', 'Zoran Perak &amp; Roger Mehr (r.mehr@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Senioren 50+</span>
              <span class="matrix-status-pill pill-blueprint">Vorschau</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Senioren 50+ · Sportplatz Zelgli</span>
          </button>
        </div>
      </div>

      <!-- Gruppe 2: Aktive Frauen (3 Teams) -->
      <div class="matrix-group-block">
        <div class="matrix-group-header">
          <h3 style="font-size:1.18rem;font-weight:800;">2. Aktive Frauen (3 Teams · Seit 1979)</h3>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Leitung: Zoran Perak &amp; Konstantinos Vettas (costa.vettas@bluewin.ch)</span>
        </div>
        <div class="matrix-grid">
          <button type="button" class="matrix-team-btn live-built" onclick="wpSwitchTeam('frauen1'); window.scrollTo({top: 260, behavior: 'smooth'});">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Frauen 1</span>
              <span class="matrix-status-pill pill-live">Live ausgebaut</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-body);">1. Mannschaft · 17 Spielerinnen · Vettas / Zamora</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: Frauen 2', 'Aktive Frauen (2. Mannschaft)', 'Zoran Perak (z.perak@fcschlieren.ch · 076 264 20 22)', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Frauen 2</span>
              <span class="matrix-status-pill pill-blueprint">Vorschau</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">2. Mannschaft Frauen · Sportplatz Zelgli</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: Frauen 3', 'Aktive Frauen (3. Mannschaft)', 'Zoran Perak (z.perak@fcschlieren.ch · 076 264 20 22)', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Frauen 3</span>
              <span class="matrix-status-pill pill-blueprint">Vorschau</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">3. Mannschaft Frauen · Sportplatz Zelgli</span>
          </button>
        </div>
      </div>

      <!-- Gruppe 3: Junioren A bis G (17 Teams) -->
      <div class="matrix-group-block">
        <div class="matrix-group-header">
          <h3 style="font-size:1.18rem;font-weight:800;">3. Junioren A bis G (17 Nachwuchs-Teams)</h3>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Leiter Junioren: Luigi Schiavano (l.schiavano@fcschlieren.ch · 079 109 52 88)</span>
        </div>
        <div class="matrix-grid">
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: Junioren A', 'Junioren-Abteilung (U19/U20)', 'Luigi Schiavano (l.schiavano@fcschlieren.ch · 079 109 52 88)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">Junioren A</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">A-Junioren · 11er-Fussball</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: B1 Junioren', 'Junioren-Abteilung B', 'Luigi Schiavano (l.schiavano@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">B1 Junioren</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">B-Junioren · 11er-Fussball</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: B2 Junioren', 'Junioren-Abteilung B', 'Luigi Schiavano (l.schiavano@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">B2 Junioren</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">B-Junioren · 11er-Fussball</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: C1 Junioren', 'Junioren-Abteilung C', 'Luigi Schiavano (l.schiavano@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">C1 Junioren</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">C-Junioren · 11er-Fussball</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: C2 Junioren', 'Junioren-Abteilung C', 'Luigi Schiavano (l.schiavano@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">C2 Junioren</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">C-Junioren · 11er-Fussball</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: C3 Junioren', 'Junioren-Abteilung C', 'Luigi Schiavano (l.schiavano@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">C3 Junioren</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">C-Junioren · 11er-Fussball</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: D1 Junioren (9er)', 'Koordination D &amp; E Junioren', 'Oscar Otero &amp; Luigi Schiavano (l.schiavano@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">D1 Junioren</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">D-Junioren 9er · Koord. O. Otero</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: D2 Junioren (9er)', 'Koordination D &amp; E Junioren', 'Oscar Otero &amp; Luigi Schiavano (l.schiavano@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">D2 Junioren</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">D-Junioren 9er · Koord. O. Otero</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: D1 (7er) Junioren', 'Koordination D &amp; E Junioren', 'Oscar Otero &amp; Luigi Schiavano (l.schiavano@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">D1 (7er) Junioren</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">D-Junioren 7er · Koord. O. Otero</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: D2 (7er) Junioren', 'Koordination D &amp; E Junioren', 'Oscar Otero &amp; Luigi Schiavano (l.schiavano@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">D2 (7er) Junioren</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">D-Junioren 7er · Koord. O. Otero</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: E1 Junioren', 'Koordination D &amp; E Junioren', 'Oscar Otero &amp; Luigi Schiavano (l.schiavano@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">E1 Junioren</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">Kinderfussball E · Play More Football</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: E2 Junioren', 'Koordination D &amp; E Junioren', 'Oscar Otero &amp; Luigi Schiavano (l.schiavano@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">E2 Junioren</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">Kinderfussball E · Play More Football</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: E3 Junioren', 'Koordination D &amp; E Junioren', 'Oscar Otero &amp; Luigi Schiavano (l.schiavano@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">E3 Junioren</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">Kinderfussball E · Play More Football</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: E4 Junioren', 'Koordination D &amp; E Junioren', 'Oscar Otero &amp; Luigi Schiavano (l.schiavano@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">E4 Junioren</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">Kinderfussball E · Play More Football</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: F1 &amp; F2 Junioren', 'Koordination F &amp; G Junioren', 'Gianfranco Gennaro &amp; Luigi Schiavano (l.schiavano@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">F1–F2 Junioren</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">F-Junioren · Koord. G. Gennaro</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: F3 &amp; F4 Junioren', 'Koordination F &amp; G Junioren', 'Gianfranco Gennaro &amp; Luigi Schiavano (l.schiavano@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">F3–F4 Junioren</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">F-Junioren · Koord. G. Gennaro</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: Junioren G &amp; Fussballschule', 'Koordination F &amp; G Junioren', 'Gianfranco Gennaro &amp; Luigi Schiavano (Mittwoch 16:15–17:45 Uhr)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">Junioren G</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">Jg. 2020–2022 · Mi 16:15–17:45 Uhr</span>
          </button>
        </div>
      </div>

      <!-- Gruppe 4: Juniorinnen U16 bis F (8 Teams) -->
      <div class="matrix-group-block" style="margin-bottom:0;">
        <div class="matrix-group-header">
          <h3 style="font-size:1.18rem;font-weight:800;">4. Juniorinnen U16 bis F (8 Mädchen-Teams)</h3>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Leiter Juniorinnen: Mario De Meo (m.demeo@fcschlieren.ch · 079 354 37 23)</span>
        </div>
        <div class="matrix-grid">
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: Frauen U16', 'Juniorinnen-Abteilung (Leistungsstufe)', 'Mario De Meo (m.demeo@fcschlieren.ch) &amp; Luca Mussolin', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">Frauen U16</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">Juniorinnen U16 · Koord. L. Mussolin</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: B Juniorinnen', 'Juniorinnen-Abteilung B', 'Mario De Meo (m.demeo@fcschlieren.ch · 079 354 37 23)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">B Juniorinnen</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">B-Juniorinnen · Sportplatz Zelgli</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: C Juniorinnen', 'Juniorinnen-Abteilung C', 'Mario De Meo (m.demeo@fcschlieren.ch · 079 354 37 23)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">C Juniorinnen</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">C-Juniorinnen · Sportplatz Zelgli</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: U14 Mädchen', 'Juniorinnen-Abteilung U14', 'Mario De Meo &amp; Luca Mussolin (m.demeo@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">U14 Mädchen</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">U14 Mädchen · Koord. L. Mussolin</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: D9er Juniorinnen', 'Juniorinnen-Abteilung D', 'Mario De Meo (m.demeo@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">D9er Juniorinnen</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">D-Juniorinnen (9er) · Zelgli</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: D7er Juniorinnen', 'Juniorinnen-Abteilung D', 'Mario De Meo (m.demeo@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">D7er Juniorinnen</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">D-Juniorinnen (7er) · Zelgli</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: E Juniorinnen', 'Koordination E &amp; F Juniorinnen', 'Angela Paradiso &amp; Mario De Meo (m.demeo@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">E Juniorinnen</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">E-Juniorinnen · Koord. A. Paradiso</span>
          </button>
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team-Seite: F Juniorinnen', 'Koordination E &amp; F Juniorinnen', 'Angela Paradiso &amp; Mario De Meo (m.demeo@fcschlieren.ch)', 'probetraining')">
            <div class="matrix-team-top"><span class="matrix-team-name">F Juniorinnen</span><span class="matrix-status-pill pill-blueprint">Vorschau</span></div>
            <span style="font-size:0.76rem;color:var(--text-muted);">F-Juniorinnen · Koord. A. Paradiso</span>
          </button>
        </div>
      </div>
    </div>
  </section>

  <script>
    function wpSwitchTeam(key) {
      var bH = document.getElementById('tabBtnHerren1');
      var bF = document.getElementById('tabBtnFrauen1');
      var pH = document.getElementById('paneHerren1');
      var pF = document.getElementById('paneFrauen1');
      if (key === 'frauen1') {
        if (bH) bH.classList.remove('active');
        if (bF) bF.classList.add('active');
        if (pH) pH.classList.remove('active');
        if (pF) pF.classList.add('active');
      } else {
        if (bF) bF.classList.remove('active');
        if (bH) bH.classList.add('active');
        if (pF) pF.classList.remove('active');
        if (pH) pH.classList.add('active');
      }
    }
    (function() {
      try {
        var params = new URLSearchParams(window.location.search);
        if ((params.get('team') || '').toLowerCase() === 'frauen1') {
          wpSwitchTeam('frauen1');
        }
      } catch(e) {}
    })();
  </script>
"""

KONTAKT_CSS = """
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
      gap: 12px;
      margin-top: 20px;
    }
    .contact-direct-item {
      padding: 12px 14px;
      background-color: var(--bg-page);
      border: 1px solid var(--border-light);
      border-left: 3px solid var(--fcs-blue);
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
    }
    .contact-direct-role {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--fcs-blue);
      letter-spacing: 0.04em;
    }
    .contact-direct-person {
      font-weight: 700;
      color: var(--fcs-navy);
      margin-top: 2px;
    }
    .contact-direct-links {
      color: var(--text-body);
      font-size: 0.82rem;
      margin-top: 2px;
    }

    /* Smart Wizard Card */
    .wizard-card {
      background-color: #FFFFFF;
      border: 2px solid var(--fcs-blue);
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
      background-color: var(--fcs-blue);
      color: #FFFFFF;
    }
    .wp-step-pill.done {
      background-color: var(--fcs-green-soft);
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
      border-color: var(--fcs-blue);
      background-color: #FFFFFF;
    }
    .wp-role-tile.selected {
      border: 2px solid var(--fcs-blue);
      background-color: var(--fcs-blue-soft);
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
      color: var(--fcs-blue);
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
      color: var(--fcs-navy);
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
      color: var(--fcs-navy);
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
      border-color: var(--fcs-blue);
      box-shadow: 0 0 0 3px rgba(0, 110, 171, 0.14);
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
      color: var(--fcs-navy);
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
      background-color: var(--fcs-navy);
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
      background-color: var(--fcs-green-soft);
      color: #166534;
      border: 1px solid #86EFAC;
    }

    .wp-selftest-banner {
      background-color: var(--fcs-gold-soft);
      border: 1px solid #FDE047;
      border-left: 4px solid var(--fcs-gold-dark);
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
      border: 2px solid var(--fcs-green);
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
      border-left: 4px solid var(--fcs-green);
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

KONTAKT_BODY = """
  <section data-section="kontakt-zentrale" style="padding: 60px 0 84px;">
    <div class="container">
      <div class="contact-layout">
        <!-- LEFT COLUMN: VEREINS-ANLAUFSTELLEN -->
        <div class="contact-info-panel">
          <div class="section-kicker" data-slot="contact_kicker">VEREINS-, PROBETRAINING- &amp; SPONSORING-ZENTRALE</div>
          <h1 style="font-size:clamp(1.65rem,2.6vw,2.2rem);font-weight:800;margin-bottom:12px;" data-slot="contact_title">
            Alle 10 Vereinsformulare gebündelt an einem Ort.
          </h1>
          <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:18px;" data-slot="contact_lead">
            Ob Probetraining für dein Kind, Spielverschiebungsgesuch, Kleiderbestellung, Adressänderung oder Sponsoring-Partnerschaft: Unser geführter 3-Schritte-Assistent leitet dein Anliegen inklusive 1-Seiten-PDF-Dossier direkt an das zuständige Ressort im FC Schlieren weiter.
          </p>

          <div class="contact-direct-list">
            <div class="contact-direct-item">
              <div class="contact-direct-role">Präsidium &amp; Vereinsführung</div>
              <div class="contact-direct-person">Roger Küng (Präsident)</div>
              <div class="contact-direct-links">r.kueng@fcschlieren.ch · Tel. 079 400 20 93</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Geschäftsstelle, Mitglieder &amp; Mutationen</div>
              <div class="contact-direct-person">Jana Seifriz (Leiterin Geschäftsstelle &amp; Spielbetrieb)</div>
              <div class="contact-direct-links">j.seifriz@fcschlieren.ch · Tel. 079 242 41 56</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Sportliche Leitung &amp; Probetraining</div>
              <div class="contact-direct-person">Zoran Perak (Aktive) · Luigi Schiavano (Junioren) · Mario De Meo (Juniorinnen)</div>
              <div class="contact-direct-links">z.perak@fcschlieren.ch · l.schiavano@fcschlieren.ch · m.demeo@fcschlieren.ch</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Spielbetrieb &amp; Spielverschiebungen</div>
              <div class="contact-direct-person">Roger Mehr (Leiter Spielbetrieb) &amp; Jana Seifriz</div>
              <div class="contact-direct-links">r.mehr@fcschlieren.ch · Tel. 079 402 83 87</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Material &amp; Kleiderbestellung</div>
              <div class="contact-direct-person">Céline Bürgisser (Material Junioren &amp; Juniorinnen)</div>
              <div class="contact-direct-links">c.buergisser@fcschlieren.ch</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Sponsoring, Supporter, Business-Club &amp; Finanzen</div>
              <div class="contact-direct-person">Dani Galantucci (Sponsoring/Banden) &amp; Luigi Voci (Finanzen)</div>
              <div class="contact-direct-links">d.galantucci@fcschlieren.ch · l.voci@fcschlieren.ch (079 788 33 24)</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Sportplatz Zelgli &amp; Clubhaus / Beizli</div>
              <div class="contact-direct-person">Müslüm Bozan (Platzwart &amp; Clubhauswirt)</div>
              <div class="contact-direct-links">m.bozan@fcschlieren.ch · Tel. 079 260 63 63 · 8952 Schlieren</div>
            </div>
          </div>
        </div>

        <!-- RIGHT COLUMN: 3-STEP SMART WIZARD -->
        <div class="wizard-card">
          <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:14px;">
            <div>
              <div class="section-kicker" style="margin-bottom:4px;">DIGITALE VEREINS-ZENTRALE · FC SCHLIEREN</div>
              <h2 style="font-size:1.35rem;font-weight:800;" id="wpWizardTitle">1. Wähle dein Anliegen</h2>
            </div>
            <span class="pillar-count" id="wpActiveAssigneeBadge">Zuständig: Sportliche Leitung</span>
          </div>

          <div class="wp-stepper" aria-label="Fortschritt">
            <div class="wp-step-pill active" id="wpStepPill1">
              <span class="wp-step-num">1</span>
              <span>Anliegen &amp; Bereich</span>
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

          <form id="fcsContactForm" onsubmit="return wpSubmitFcsLead(event)" novalidate>
            <!-- Honeypot -->
            <div style="display:none;" aria-hidden="true">
              <label for="wpHoneypot">Website URL</label>
              <input type="text" id="wpHoneypot" name="website_url" tabindex="-1" autocomplete="off">
            </div>

            <!-- STEP 1: TOPIC SELECTION (6 TILES) -->
            <div class="wp-step-pane active" id="wpStep1">
              <div class="wp-role-grid" id="wpTopicGrid">
                <button type="button" class="wp-role-tile selected" data-topic="Probetraining / Neumitglied" onclick="wpSelectFcsTopic('Probetraining / Neumitglied')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_1">Probetraining / Neumitglied</span>
                  </div>
                  <span class="wp-role-desc">Anmeldung für Junioren A–G, Juniorinnen, Fussballschule, Herren oder Frauen</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Sponsoring / Supporter / Business-Club" onclick="wpSelectFcsTopic('Sponsoring / Supporter / Business-Club')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_2">Sponsoring / Supporter</span>
                  </div>
                  <span class="wp-role-desc">Hauptsponsor, Bandenwerbung (CHF 360), Supporter (CHF 150) &amp; Business-Club</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Spielbetrieb / Spielverschiebung" onclick="wpSelectFcsTopic('Spielbetrieb / Spielverschiebung')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_3">Spielbetrieb / Verschiebung</span>
                  </div>
                  <span class="wp-role-desc">Spielverschiebungsgesuch, Platzbelegung Zelgli, Schiedsrichter oder Turniere</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Kleiderbestellung / Vereinskollektion" onclick="wpSelectFcsTopic('Kleiderbestellung / Vereinskollektion')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M20.38 3.46L16 2a4 4 0 0 1-8 0L3.62 3.46a2 2 0 0 0-1.34 2.23l.58 3.47a1 1 0 0 0 .99.84H6v10c0 1.1.9 2 2 2h8a2 2 0 0 0 2-2V10h2.15a1 1 0 0 0 .99-.84l.58-3.47a2 2 0 0 0-1.34-2.23z"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_4">Kleiderbestellung / Material</span>
                  </div>
                  <span class="wp-role-desc">Offizielle FC Schlieren Trainingskleider, Trikots, Stulpen &amp; Ausrüstung</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Mitgliedschaft / Mutation / Austritt" onclick="wpSelectFcsTopic('Mitgliedschaft / Mutation / Austritt')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_5">Mutation / Adresse / Austritt</span>
                  </div>
                  <span class="wp-role-desc">Adressänderung, Vereinswechsel, Passwesen, Mitgliederbeitrag oder Austritt</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Clubhaus / Beizli / Allgemeine Anfrage" onclick="wpSelectFcsTopic('Clubhaus / Beizli / Allgemeine Anfrage')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_6">Club-Beizli &amp; Allgemeines</span>
                  </div>
                  <span class="wp-role-desc">Reservation Club-Beizli (40–50 Plätze), Sponsorenlauf oder Anfrage an Vorstand</span>
                </button>
              </div>

              <button type="button" class="btn-cta btn-cta-primary" style="width:100%;" onclick="wpNextStep(2)">
                <span>Weiter zu Schritt 2: Angaben &amp; Unterlagen</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
              </button>
            </div>

            <!-- STEP 2: DYNAMIC DETAILS & PHOTO UPLOAD -->
            <div class="wp-step-pane" id="wpStep2">
              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="wpDetail1" class="form-label" id="wpDetail1Label">Name &amp; Jahrgang Spieler/in</label>
                  <input type="text" id="wpDetail1" class="form-input" placeholder="z. B. Jahrgang 2015 · Bisheriger Verein / Einsteiger">
                </div>
                <div class="form-field">
                  <label for="wpDetail2" class="form-label" id="wpDetail2Label">Gewünschte Mannschaft / Abteilung</label>
                  <input type="text" id="wpDetail2" class="form-input" placeholder="z. B. Junioren D / Fussballschule / Herren 1">
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label class="form-label">Gewünschter Zeithorizont / Dringlichkeit</label>
                <div class="wp-role-grid" id="wpUrgencyGrid" style="margin-bottom:0;">
                  <button type="button" class="wp-role-tile" data-urg="Aktuelle Woche / Nächstes Training" onclick="wpSelectFcsUrgency('Aktuelle Woche / Nächstes Training')">
                    <span class="wp-role-title">Nächstes Training / Diese Woche</span>
                    <span class="wp-role-desc">Zeitnahe Rückmeldung erwünscht</span>
                  </button>
                  <button type="button" class="wp-role-tile selected" data-urg="Planbar / Laufende Saison" onclick="wpSelectFcsUrgency('Planbar / Laufende Saison')">
                    <span class="wp-role-title">Planbar / Laufende Saison</span>
                    <span class="wp-role-desc">Reguläre Bearbeitung durch Ressort</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urg="Kommende Saison / Fussballschule" onclick="wpSelectFcsUrgency('Kommende Saison / Fussballschule')">
                    <span class="wp-role-title">Neue Saison / Fussballschule</span>
                    <span class="wp-role-desc">Voranmeldung &amp; Kaderplanung</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urg="Heute (Dringend / Spielbetrieb)" onclick="wpSelectFcsUrgency('Heute (Dringend / Spielbetrieb)')">
                    <span class="wp-role-title">Dringend (Spielbetrieb / Frist)</span>
                    <span class="wp-role-desc">Kurzfristiges Gesuch / Rückruf</span>
                  </button>
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label for="contactMessage" class="form-label" data-slot="lbl_message">Nachricht / Zusatzangaben ans Ressort *</label>
                <textarea id="contactMessage" name="message" class="form-textarea" placeholder="Beschreibe kurz dein Anliegen (z. B. Position, Kleidergrössen, Wunschtermin oder Sponsoring-Interesse)..." required></textarea>
              </div>

              <div class="form-field" style="margin-bottom:18px;">
                <label class="form-label">Fotos, Formularbeilagen oder Sponsoren-Logo beifügen (optional, max. 3 Bilder)</label>
                <div class="wp-upload-zone">
                  <input type="file" id="wpPhotoInput" accept="image/*" multiple style="display:none;" onchange="wpHandlePhotoFiles(this.files)">
                  <button type="button" class="wp-upload-btn" onclick="wpTriggerPhotoUpload()">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
                    <span>Bild / Beilage auswählen (z. B. Ausweis, Spielplan, Firmenlogo)</span>
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
                <strong>Vorschau- &amp; Selbst-Test-Modus aktiv:</strong> Du kannst dieses Formular jetzt live testen. Das System generiert sofort ein echtes <strong>1-Seiten-PDF-Vereinsdossier</strong> mit FC-Schlieren-Briefkopf zum Herunterladen, ohne den Vorstand mit Test-Mails zu belasten.
              </div>

              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactName" class="form-label" data-slot="lbl_name">Vor- und Nachname (oder Eltern) *</label>
                  <input type="text" id="contactName" name="name" class="form-input" placeholder="z. B. Marco Muster" required>
                </div>
                <div class="form-field">
                  <label for="contactCompany" class="form-label">Team / Firma / Organisation (optional)</label>
                  <input type="text" id="contactCompany" name="company" class="form-input" placeholder="z. B. Junioren D1 / Muster AG Schlieren">
                </div>
              </div>

              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactLoc" class="form-label">PLZ &amp; Wohnort *</label>
                  <input type="text" id="contactLoc" name="plz" class="form-input" placeholder="z. B. 8952 Schlieren" oninput="wpCheckFcsPlz(this.value)" required>
                </div>
                <div class="form-field">
                  <label for="contactStreet" class="form-label">Strasse &amp; Nr. (für Mutationen / Rechnungen)</label>
                  <input type="text" id="contactStreet" name="street" class="form-input" placeholder="z. B. Badenerstrasse 12">
                </div>
              </div>

              <div class="wp-plz-badge" id="wpPlzBadge" style="margin-bottom:14px;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
                <span id="wpPlzBadgeText">PLZ 8952: Einzugsgebiet Schlieren &amp; Limmattal</span>
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
                <span style="width:36px;height:36px;border-radius:4px;background-color:var(--fcs-green);color:#FFFFFF;display:inline-flex;align-items:center;justify-content:center;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><polyline points="20 6 9 17 4 12"/></svg>
                </span>
                <div>
                  <div style="font-family:'Montserrat',sans-serif;font-weight:800;font-size:1.05rem;color:var(--fcs-navy);">Vereins-Anfrage &amp; 1-Seiten-PDF-Dossier erstellt</div>
                  <div style="font-size:0.78rem;color:var(--text-muted);" id="wpResChannels">1-Seiten-PDF-Dossier bereit zum Download</div>
                </div>
              </div>
              <span class="top-bar-badge" style="background-color:var(--fcs-navy);color:var(--fcs-gold);" id="wpResRef">#FCS-2026</span>
            </div>

            <div class="form-grid-2" style="background-color:#FFFFFF;padding:12px 14px;border-radius:4px;border:1px solid var(--border-light);font-size:0.84rem;">
              <div>
                <div style="color:var(--text-muted);font-size:0.75rem;">Zuständiges Ressort im FC Schlieren:</div>
                <strong style="color:var(--fcs-navy);" id="wpResAssigned">Geschäftsstelle &amp; Sportliche Leitung</strong>
              </div>
              <div>
                <div style="color:var(--text-muted);font-size:0.75rem;">Erwartete Rückmeldung:</div>
                <strong style="color:var(--fcs-blue);" id="wpResCallback">Innert 24–48 Stunden</strong>
              </div>
            </div>

            <div>
              <div style="font-family:'Montserrat',sans-serif;font-size:0.75rem;font-weight:800;text-transform:uppercase;color:var(--fcs-navy);margin-bottom:6px;">
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
    var wpFcsState = {
      step: 1,
      topic: 'Probetraining / Neumitglied',
      urgency: 'Planbar / Laufende Saison',
      photos: []
    };

    var wpFcsRoleConfig = {
      'Probetraining / Neumitglied': {
        assignee: 'Zoran Perak (Aktive), Luigi Schiavano (Junioren) & Mario De Meo (Juniorinnen)',
        l1: 'Name & Jahrgang Spieler/in',
        p1: 'z. B. Noah Muster · Jahrgang 2015',
        l2: 'Gewünschte Mannschaft / Bisheriger Verein',
        p2: 'z. B. Junioren D / Fussballschule / Herren 1'
      },
      'Sponsoring / Supporter / Business-Club': {
        assignee: 'Dani Galantucci (Sponsoring), Roger Küng (Präsident) & Luigi Voci (Finanzen)',
        l1: 'Gewünschtes Engagement / Plattform',
        p1: 'z. B. Bandenwerbung Platz 1 (CHF 360), Supporter (CHF 150) oder Business-Club',
        l2: 'Unternehmen / Wunsch-Team für Patronat',
        p2: 'z. B. Muster AG Schlieren · Herren 1 / Frauen 1'
      },
      'Spielbetrieb / Spielverschiebung': {
        assignee: 'Roger Mehr (Leiter Spielbetrieb) & Jana Seifriz (Geschäftsstelle)',
        l1: 'Mannschaft, Spielnummer & Gegner',
        p1: 'z. B. Junioren C1 · Spiel-Nr. 40219 vs. FC Dietikon',
        l2: 'Bisheriges Spieldatum & Neuer Wunschtermin',
        p2: 'z. B. Verschiebung auf Mittwoch 19:30 Uhr, Platz 2 Zelgli'
      },
      'Kleiderbestellung / Vereinskollektion': {
        assignee: 'Céline Bürgisser (Material Junioren & Juniorinnen)',
        l1: 'Mannschaft & Name Spieler/in',
        p1: 'z. B. E2 Junioren · Levin Muster',
        l2: 'Gewünschte Artikel & Kleidergrösse',
        p2: 'z. B. Trainingsanzug & Stulpen · Grösse 152'
      },
      'Mitgliedschaft / Mutation / Austritt': {
        assignee: 'Jana Seifriz (Geschäftsstelle) & Luigi Voci (Finanzen)',
        l1: 'Art der Mutation / Meldung',
        p1: 'z. B. Adressänderung / Übertritt / Austritt per Saisonende',
        l2: 'Name Mitglied, Jahrgang & Mannschaft',
        p2: 'z. B. Sara Muster · Jg. 2010 · B Juniorinnen'
      },
      'Clubhaus / Beizli / Allgemeine Anfrage': {
        assignee: 'Müslüm Bozan (Clubhauswirt & Platzwart) & Roger Küng (Präsident)',
        l1: 'Betreff / Anlass im Club-Beizli',
        p1: 'z. B. Mannschaftsessen im Beizli / Anfrage an den Vorstand',
        l2: 'Wunschdatum & Personenanzahl',
        p2: 'z. B. Freitag 19:00 Uhr · ca. 25 Personen'
      }
    };

    function wpUpdateHeader() {
      var titles = {
        1: '1. Wähle dein Anliegen',
        2: '2. Angaben & Beilagen ergänzen',
        3: '3. Kontaktdaten & PDF-Dossier'
      };
      var tEl = document.getElementById('wpWizardTitle');
      if (tEl) tEl.textContent = titles[wpFcsState.step] || titles[1];
      for (var i = 1; i <= 3; i++) {
        var pane = document.getElementById('wpStep' + i);
        var pill = document.getElementById('wpStepPill' + i);
        if (pane) {
          if (i === wpFcsState.step) pane.classList.add('active');
          else pane.classList.remove('active');
        }
        if (pill) {
          pill.className = 'wp-step-pill';
          if (i === wpFcsState.step) pill.classList.add('active');
          else if (i < wpFcsState.step) pill.classList.add('done');
        }
      }
    }

    function wpSelectFcsTopic(topic) {
      wpFcsState.topic = topic;
      var tiles = document.querySelectorAll('#wpTopicGrid .wp-role-tile');
      for (var i = 0; i < tiles.length; i++) {
        if (tiles[i].getAttribute('data-topic') === topic) tiles[i].classList.add('selected');
        else tiles[i].classList.remove('selected');
      }
      var cfg = wpFcsRoleConfig[topic] || wpFcsRoleConfig['Probetraining / Neumitglied'];
      var badge = document.getElementById('wpActiveAssigneeBadge');
      if (badge) badge.textContent = 'Ressort: ' + cfg.assignee.split('(')[0].trim();
      var l1 = document.getElementById('wpDetail1Label');
      var i1 = document.getElementById('wpDetail1');
      var l2 = document.getElementById('wpDetail2Label');
      var i2 = document.getElementById('wpDetail2');
      if (l1) l1.textContent = cfg.l1;
      if (i1) i1.placeholder = cfg.p1;
      if (l2) l2.textContent = cfg.l2;
      if (i2) i2.placeholder = cfg.p2;
    }

    function wpSelectFcsUrgency(urg) {
      wpFcsState.urgency = urg;
      var tiles = document.querySelectorAll('#wpUrgencyGrid .wp-role-tile');
      for (var i = 0; i < tiles.length; i++) {
        if (tiles[i].getAttribute('data-urg') === urg) tiles[i].classList.add('selected');
        else tiles[i].classList.remove('selected');
      }
    }

    function wpNextStep(stepNum) {
      wpFcsState.step = stepNum;
      wpUpdateHeader();
    }

    function wpPrevStep() {
      if (wpFcsState.step > 1) {
        wpFcsState.step -= 1;
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
      if (cnt) cnt.textContent = wpFcsState.photos.length + ' / 3 Bilder ausgewählt · Automatisch für das 1-Seiten-PDF-Dossier optimiert';
      if (!box) return;
      box.innerHTML = '';
      for (var i = 0; i < wpFcsState.photos.length; i++) {
        (function(idx) {
          var wrap = document.createElement('div');
          wrap.className = 'wp-thumb-item';
          var im = document.createElement('img');
          im.src = wpFcsState.photos[idx];
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
        if (wpFcsState.photos.length >= 3) break;
        wpCompressImageFile(files[i], function(b64) {
          if (wpFcsState.photos.length < 3) {
            wpFcsState.photos.push(b64);
            wpRenderPhotos();
          }
        });
      }
    }

    function wpRemovePhoto(idx) {
      wpFcsState.photos.splice(idx, 1);
      wpRenderPhotos();
    }

    function wpCheckFcsPlz(val) {
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
      if (plz >= 8900 && plz <= 8967) {
        txt.textContent = 'PLZ ' + m[1] + ': Direktes Einzugsgebiet Schlieren & Limmattal (Sportanlage Zelgli)';
      } else {
        txt.textContent = 'PLZ ' + m[1] + ': Region Zürich / Schweiz – Herzlich willkommen beim FC Schlieren';
      }
    }

    function wpStripEmojisForDom(str) {
      return String(str || '').replace(/[\\u{1F300}-\\u{1FAFF}\\u{2600}-\\u{27BF}]/gu, '').replace(/\\s+\\n/g, '\\n').trim();
    }

    function wpResetWizard() {
      wpFcsState.step = 1;
      wpFcsState.photos = [];
      wpRenderPhotos();
      var form = document.getElementById('fcsContactForm');
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
      wpSelectFcsTopic('Probetraining / Neumitglied');
      wpSelectFcsUrgency('Planbar / Laufende Saison');
      wpUpdateHeader();
    }

    function wpSubmitFcsLead(e) {
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

      var cfg = wpFcsRoleConfig[wpFcsState.topic] || wpFcsRoleConfig['Probetraining / Neumitglied'];
      var extra = {};
      extra[cfg.l1] = d1 || 'Keine Angabe';
      extra[cfg.l2] = d2 || 'Keine Angabe';

      var btn = document.getElementById('wpSubmitBtn');
      var btnTxt = document.getElementById('wpSubmitBtnText');
      if (btn) btn.disabled = true;
      if (btnTxt) btnTxt.textContent = '1-Seiten-PDF-Dossier wird erstellt...';

      var payload = {
        client_slug: 'fcschlieren',
        source_page: 'preview-fcschlieren/kontakt.html',
        website_url: hp,
        category: wpFcsState.topic,
        sparte: wpFcsState.topic,
        urgency: wpFcsState.urgency,
        name: name,
        company: company,
        street: street,
        plz: loc,
        phone: phone,
        email: email,
        message: msg || ('Anfrage zum Bereich ' + wpFcsState.topic),
        extra_fields: extra,
        photos: wpFcsState.photos,
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
        document.getElementById('fcsContactForm').style.display = 'none';
        document.getElementById('wpResRef').textContent = res.ref_code || '#FCS-2026';
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
          errBox.textContent = 'Netzwerkfehler bei der Übermittlung. Bitte schreibe direkt an j.seifriz@fcschlieren.ch.';
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
          'sponsoring': 'Sponsoring / Supporter / Business-Club',
          'spielbetrieb': 'Spielbetrieb / Spielverschiebung',
          'kleider': 'Kleiderbestellung / Vereinskollektion',
          'mitgliedschaft': 'Mitgliedschaft / Mutation / Austritt',
          'allgemein': 'Clubhaus / Beizli / Allgemeine Anfrage'
        };
        if (map[t]) {
          wpSelectFcsTopic(map[t]);
        }
      } catch(err) {}
    })();
  </script>
"""

pages_to_write = [
    ("index.html", "FC Schlieren · Gegründet 1921 | 33 Teams, Fussballschule & Sportplatz Zelgli", "startseite", INDEX_BODY, ""),
    ("herren-1.html", "Herren 1, Frauen 1 & Alle 33 Teams (Architekten-Musterhaus) | FC Schlieren", "teams", HERREN_1_BODY, HERREN_1_CSS),
    ("kontakt.html", "Vereins-, Probetraining-, Spielbetriebs- & Sponsoring-Zentrale | FC Schlieren", "kontakt", KONTAKT_BODY, KONTAKT_CSS),
]

for fname, title, nav_key, body, extra_css in pages_to_write:
    full_html = render_shell(fname, title, nav_key, body, extra_css)
    (SITE_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"Wrote {fname} ({len(full_html)} bytes)")

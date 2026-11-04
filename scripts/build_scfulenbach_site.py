#!/usr/bin/env python3
"""
Builds the complete 3-page WebPilot showcase for SC Fulenbach (preview-scfulenbach)
directly in Variant 2 («Bauplan- & Musterhaus-Modus»):
  - index.html (Startseite im Bauplan- & Musterhaus-Modus: Hero + 100% Original-Sponsoren + 4 weitere Bereiche für 40 offene Seiten)
  - herren-1.html (Beispiel-Team 1. Mannschaft 2. Liga regional fertig + 13 weitere Mannschaften als Rohbau-Drahtgitter in der 14-Teams-Matrix)
  - kontakt.html (3-Schritte Smart-Anfrage-Zentrale + 1-Seiten-PDF-Vereinsdossier für alle 6 Vereinsbereiche)
Plus company.json, config.json, and site.json.
Strict adherence to #UI-01..#UI-16, #LANG-01..#LANG-02 (100% ss, zero emojis in DOM, 2-Radius 0/4/8px).
"""
import html
import json
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
SITE_DIR = Path("/home/brainuser/workspaces/mxs-embed/preview-scfulenbach")
SITE_DIR.mkdir(parents=True, exist_ok=True)

# 1. Write company.json, config.json, site.json
company_data = {
    "slug": "scfulenbach",
    "company_name": "SC Fulenbach",
    "legal_name": "Sportclub Fulenbach (SOFV-Verein Nr. 1826)",
    "tagline": "Tradition, Teamgeist und Nachwuchsförderung auf dem Sportplatz Bad seit Sommer 1944.",
    "founded": "Sommer 1944",
    "president": "Willi von Arx",
    "vice_president": "Elias Sidler",
    "honorary_president": "Urs Lehmann",
    "sport_director": "Mirko Ferrari",
    "youth_director": "Michael «Mike» Frieder",
    "sponsoring": "Andreas Guldimann",
    "clubhouse_rental": "René Hofstetter",
    "media_support": "David Ackermann",
    "finance": "Roland Wiss",
    "actuary": "Rahel Napoli",
    "infrastructure": "Alfred Ammann",
    "address": "Sportplatz Bad, Ewigkeitstrasse 5, 4629 Fulenbach",
    "phone": "+41 79 397 87 73",
    "email": "vorstand@scfulenbach.ch",
    "website": "https://www.scfulenbach.ch",
    "colors": {
        "primary": "#0F8A4B",
        "primary_dark": "#0B1528",
        "accent_blue": "#0284C7",
        "accent_amber": "#F59E0B"
    }
}
(SITE_DIR / "company.json").write_text(json.dumps(company_data, indent=2, ensure_ascii=False), encoding="utf-8")

config_data = {
    "slug": "scfulenbach",
    "name": "SC Fulenbach",
    "company_name": "SC Fulenbach",
    "domain": "scfulenbach.ch",
    "preview_url": "https://vorschau.magnet-xs.ch/scfulenbach/",
    "cockpit_token": "scfulenbach2026",
    "template": "sports-club-blueprint-v2",
    "pages": ["index.html", "herren-1.html", "kontakt.html"]
}
(SITE_DIR / "config.json").write_text(json.dumps(config_data, indent=2, ensure_ascii=False), encoding="utf-8")

site_data = {
    "name": "SC Fulenbach",
    "slug": "scfulenbach",
    "Updated": "2026-11-01",
    "PagesTotal": 43,
    "PagesBuilt": 3,
    "CompletionPercent": 7,
    "TeamsCount": 14,
    "SponsorsCount": 88
}
(SITE_DIR / "site.json").write_text(json.dumps(site_data, indent=2, ensure_ascii=False), encoding="utf-8")

# Load enriched sponsors from sponsors.json
sponsors_list = json.loads((SITE_DIR / "sponsors.json").read_text(encoding="utf-8"))


def build_sponsors_html() -> str:
    silver = [s for s in sponsors_list if s.get("category") == "Silbersponsoren"]
    banden = [s for s in sponsors_list if s.get("category") == "Bandensponsoren / Sponsoren"]

    silver_cards = []
    for idx, sp in enumerate(silver, 1):
        name_esc = html.escape(sp["name"])
        lines = [l for l in sp.get("lines", []) if l != sp["name"] and not l.startswith("www.") and not l.startswith("http")]
        loc_esc = html.escape(" · ".join(lines[:2])) if lines else "Region Fulenbach"
        href = sp.get("href", "").strip()
        logo = html.escape(sp.get("local_logo", ""))
        inner = f"""            <div class="sponsor-logo-wrap">
              <img src="{logo}" alt="{name_esc} — Silbersponsor SC Fulenbach" width="240" height="96" loading="lazy" decoding="async" data-slot="sponsor_silver_{idx}_img">
            </div>
            <div>
              <div class="sponsor-name" data-slot="sponsor_silver_{idx}_name">{name_esc}</div>
              <div class="sponsor-role-tag">Silbersponsor · {loc_esc}</div>
            </div>"""
        if href:
            silver_cards.append(f'          <a href="{html.escape(href)}" target="_blank" rel="noopener noreferrer" class="sponsor-card">\n{inner}\n          </a>')
        else:
            silver_cards.append(f'          <div class="sponsor-card">\n{inner}\n          </div>')

    banden_cards = []
    for idx, sp in enumerate(banden, 1):
        name_esc = html.escape(sp["name"])
        lines = [l for l in sp.get("lines", []) if l != sp["name"] and not l.startswith("www.") and not l.startswith("http")]
        loc_esc = html.escape(lines[-1] if lines else "Partner SC Fulenbach")
        href = sp.get("href", "").strip()
        logo = html.escape(sp.get("local_logo", ""))
        inner = f"""            <div class="sponsor-logo-wrap" style="height:78px;">
              <img src="{logo}" alt="{name_esc} — Sponsor SC Fulenbach" width="180" height="70" loading="lazy" decoding="async" data-slot="sponsor_bande_{idx}_img">
            </div>
            <div>
              <div class="sponsor-name" style="font-size:0.88rem;">{name_esc}</div>
              <div class="sponsor-role-tag" style="font-size:0.74rem;">{loc_esc}</div>
            </div>"""
        if href:
            banden_cards.append(f'          <a href="{html.escape(href)}" target="_blank" rel="noopener noreferrer" class="sponsor-card" style="padding:16px;">\n{inner}\n          </a>')
        else:
            banden_cards.append(f'          <div class="sponsor-card" style="padding:16px;">\n{inner}\n          </div>')

    return "\n".join(silver_cards), "\n".join(banden_cards), len(banden)


SILVER_CARDS_HTML, BANDEN_CARDS_HTML, BANDEN_COUNT = build_sponsors_html()


SHARED_CSS = """
    :root {
      --scf-green: #0F8A4B;
      --scf-green-bright: #10B060;
      --scf-green-soft: #ECFDF5;
      --scf-blue: #0284C7;
      --scf-blue-bright: #0EA5E9;
      --scf-blue-soft: #F0F9FF;
      --scf-navy: #0F172A;
      --scf-navy-deep: #0B1528;
      --scf-gold: #F59E0B;
      --scf-gold-bright: #FBBF24;
      --scf-gold-soft: #FEF3C7;
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

    /* Section Kickers (#UI-06: No JetBrains Mono, No double slashes) */
    .section-kicker {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.76rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--scf-green);
      margin-bottom: 12px;
    }
    .section-kicker::before {
      content: "";
      display: inline-block;
      width: 16px;
      height: 2px;
      background-color: var(--scf-gold);
      border-radius: 0px;
      flex-shrink: 0;
    }
    .section-kicker.kicker-light {
      color: var(--scf-gold-bright);
    }
    .section-kicker.kicker-light::before {
      background-color: #FFFFFF;
    }

    h1, h2, h3, h4 {
      font-family: 'Montserrat', sans-serif;
      color: var(--scf-navy);
      line-height: 1.18;
      letter-spacing: -0.02em;
    }

    .section-head {
      max-width: 800px;
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

    /* Permanente Architektur-Top-Bar (#0B1528 mit #F59E0B Amber-Akzent) */
    .wp-arch-topbar {
      background-color: #0B1528;
      color: #F8FAFC;
      border-bottom: 2px solid #F59E0B;
      font-size: 0.79rem;
      position: relative;
      z-index: 1002;
      padding: 8px 0;
    }
    .wp-arch-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      flex-wrap: wrap;
    }
    .wp-arch-left {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .wp-arch-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: rgba(245, 158, 11, 0.2);
      border: 1px solid rgba(245, 158, 11, 0.55);
      color: #FBBF24;
      font-family: 'Montserrat', sans-serif;
      font-weight: 800;
      font-size: 0.7rem;
      padding: 3px 9px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }
    .wp-arch-progress-wrap {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background-color: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(148, 163, 184, 0.3);
      padding: 4px 12px;
      border-radius: var(--radius-sm);
    }
    .wp-arch-bar-track {
      width: 96px;
      height: 7px;
      background-color: rgba(255, 255, 255, 0.14);
      border-radius: var(--radius-sm);
      overflow: hidden;
      flex-shrink: 0;
    }
    .wp-arch-bar-fill {
      width: 14%;
      height: 100%;
      background: linear-gradient(90deg, #10B981 0%, #F59E0B 100%);
      border-radius: var(--radius-sm);
    }
    .wp-arch-progress-label {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.72rem;
      font-weight: 700;
      color: #E2E8F0;
    }
    .wp-arch-right {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .wp-arch-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #CBD5E1;
      font-size: 0.76rem;
      font-weight: 600;
    }
    .wp-arch-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background-color: #F59E0B;
      color: #0B1528;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.74rem;
      font-weight: 800;
      padding: 5px 11px;
      min-height: 32px;
      border-radius: var(--radius-sm);
      border: 1px solid #FBBF24;
    }
    .wp-arch-cta:hover {
      background-color: #FBBF24;
      color: #0B1528;
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
      gap: 16px;
    }
    .brand-link {
      display: inline-flex;
      align-items: center;
      gap: 12px;
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
      color: var(--scf-navy);
      letter-spacing: -0.02em;
      line-height: 1.1;
    }
    .brand-sub {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.67rem;
      font-weight: 700;
      color: var(--scf-green);
      letter-spacing: 0.07em;
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
      font-size: 0.69rem;
      font-weight: 700;
      color: var(--text-body);
      padding: 6px 7px;
      min-height: 34px;
      border-radius: var(--radius-sm);
      transition: all 0.2s ease;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background: none;
      border: 1px solid transparent;
      cursor: pointer;
    }
    .header-actions .btn-cta {
      display: none;
    }
    .nav-link:hover, .nav-link.active {
      color: var(--scf-green);
      background-color: var(--scf-green-soft);
    }
    .nav-link.nav-blueprint-trigger {
      border: 1px dashed #94A3B8;
      background-color: #F8FAFC;
      color: #334155;
    }
    .nav-link.nav-blueprint-trigger:hover {
      border-color: var(--scf-gold);
      background-color: var(--scf-gold-soft);
      color: #92400E;
    }
    .wp-status-dot {
      width: 8px;
      height: 8px;
      border-radius: 4px;
      display: inline-block;
      flex-shrink: 0;
    }
    .wp-dot-green {
      background-color: #10B981;
      box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.2);
    }
    .wp-dot-amber {
      background-color: #F59E0B;
      box-shadow: 0 0 0 2px rgba(245, 158, 11, 0.22);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }

    /* Buttons */
    .btn-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.86rem;
      font-weight: 700;
      padding: 12px 20px;
      min-height: 44px;
      border-radius: var(--radius-sm);
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.2s ease;
      text-align: center;
      line-height: 1.25;
    }
    .btn-cta-primary {
      background-color: var(--scf-green);
      color: #FFFFFF;
      box-shadow: 0 4px 12px rgba(15, 138, 75, 0.24);
    }
    .btn-cta-primary:hover {
      background-color: #0B6E3B;
      transform: translateY(-1px);
    }
    .btn-cta-gold {
      background-color: var(--scf-gold);
      color: var(--scf-navy-deep);
      font-weight: 800;
      box-shadow: 0 4px 14px rgba(245, 158, 11, 0.28);
    }
    .btn-cta-gold:hover {
      background-color: var(--scf-gold-bright);
      transform: translateY(-1px);
    }
    .btn-cta-navy {
      background-color: var(--scf-navy);
      color: #FFFFFF;
    }
    .btn-cta-navy:hover {
      background-color: #1E293B;
    }
    .btn-cta-outline {
      background-color: #FFFFFF;
      color: var(--scf-navy);
      border-color: var(--border-strong);
    }
    .btn-cta-outline:hover {
      border-color: var(--scf-green);
      color: var(--scf-green);
      background-color: var(--scf-green-soft);
    }
    .btn-cta-ghost-light {
      background-color: rgba(255, 255, 255, 0.1);
      color: #FFFFFF;
      border-color: rgba(255, 255, 255, 0.28);
    }
    .btn-cta-ghost-light:hover {
      background-color: rgba(255, 255, 255, 0.18);
      border-color: #FFFFFF;
    }
    .btn-sm {
      padding: 9px 14px;
      font-size: 0.8rem;
      min-height: 38px;
    }

    /* Mobile Menu Button & Drawer */
    .mobile-toggle {
      display: none;
      width: 44px;
      height: 44px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-light);
      background: #FFFFFF;
      color: var(--scf-navy);
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }
    .mobile-drawer {
      display: none;
      position: fixed;
      top: 82px;
      left: 0;
      right: 0;
      background-color: var(--scf-navy-deep);
      border-bottom: 2px solid var(--scf-gold);
      padding: 20px 24px 28px;
      z-index: 999;
      flex-direction: column;
      gap: 10px;
      box-shadow: var(--shadow-lg);
    }
    .mobile-drawer.open {
      display: flex;
    }
    .mobile-drawer a, .mobile-drawer button {
      display: flex;
      align-items: center;
      gap: 8px;
      width: 100%;
      text-align: left;
      padding: 12px 14px;
      min-height: 44px;
      font-family: 'Montserrat', sans-serif;
      font-weight: 700;
      font-size: 0.92rem;
      color: #FFFFFF;
      border: none;
      border-radius: var(--radius-sm);
      background-color: rgba(255, 255, 255, 0.06);
      cursor: pointer;
    }
    .mobile-drawer a:hover, .mobile-drawer button:hover {
      background-color: var(--scf-green);
    }

    /* Hero Section */
    .hero-section {
      background: radial-gradient(circle at 82% 20%, rgba(15, 138, 75, 0.34) 0%, rgba(2, 132, 199, 0.18) 38%, rgba(11, 21, 40, 0.98) 78%), linear-gradient(135deg, #0B1528 0%, #0F2942 100%);
      color: #FFFFFF;
      padding: 72px 0 84px;
      border-bottom: 4px solid var(--scf-green);
      overflow: hidden;
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1.08fr 0.92fr;
      gap: 44px;
      align-items: center;
    }
    .hero-title {
      color: #FFFFFF;
      font-size: clamp(2.1rem, 3.8vw, 3.3rem);
      font-weight: 800;
      margin-bottom: 18px;
      line-height: 1.12;
    }
    .hero-title span {
      color: #34D399;
    }
    .hero-lead {
      font-size: 1.05rem;
      color: #E2E8F0;
      margin-bottom: 26px;
      line-height: 1.65;
    }
    .hero-cta-row {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 32px;
    }
    .hero-kpi-strip {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      padding-top: 24px;
      border-top: 1px solid rgba(255, 255, 255, 0.16);
    }
    .hero-kpi-box {
      background-color: rgba(15, 23, 42, 0.72);
      border: 1px solid rgba(255, 255, 255, 0.16);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
    }
    .hero-kpi-num {
      font-family: 'Montserrat', sans-serif;
      font-size: 1.3rem;
      font-weight: 800;
      color: #FBBF24;
      line-height: 1.15;
    }
    .hero-kpi-label {
      font-size: 0.75rem;
      color: #E2E8F0;
      margin-top: 4px;
      font-weight: 600;
    }

    .hero-visual-stack {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .hero-main-photo-card {
      position: relative;
      background-color: var(--scf-navy);
      border: 2px solid rgba(52, 211, 153, 0.45);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-lg);
    }
    .hero-main-photo-card img {
      width: 100%;
      height: 300px;
      object-fit: cover;
    }
    .hero-photo-caption {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 12px 16px;
      background-color: rgba(11, 21, 40, 0.96);
      border-top: 1px solid rgba(255, 255, 255, 0.12);
      flex-wrap: wrap;
    }
    .hero-photo-caption strong {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.84rem;
      color: #FFFFFF;
    }
    .hero-photo-caption span {
      font-size: 0.76rem;
      color: #FBBF24;
      font-weight: 700;
    }
    .hero-secondary-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }
    .hero-mini-card {
      background-color: rgba(15, 23, 42, 0.88);
      border: 1px solid rgba(255, 255, 255, 0.16);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .hero-mini-card img {
      width: 100%;
      height: 136px;
      object-fit: cover;
    }
    .hero-mini-body {
      padding: 10px 14px;
      font-size: 0.78rem;
      color: #E2E8F0;
    }

    /* Grids & Cards */
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
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
      border-color: var(--border-strong);
    }

    /* Seiten-Übersicht Section Styles */
    .wp-uebersicht-section {
      background-color: #E2E8F0;
      background-image: radial-gradient(#94A3B8 1px, transparent 1px);
      background-size: 20px 20px;
      border-top: 3px dashed #64748B;
      border-bottom: 3px dashed #64748B;
    }
    .wp-uebersicht-banner {
      background-color: #0B1528;
      color: #FFFFFF;
      border: 2px solid #F59E0B;
      border-radius: var(--radius-md);
      padding: 24px 28px;
      margin-bottom: 32px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      flex-wrap: wrap;
      box-shadow: var(--shadow-md);
    }
    .wp-wireframe-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
    }
    .wp-wireframe-card {
      background-color: #F8FAFC;
      border: 2px dashed #64748B;
      border-radius: var(--radius-md);
      padding: 26px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 16px;
      box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
    }
    .wp-wireframe-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      flex-wrap: wrap;
    }
    .wp-wireframe-tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: #FEF3C7;
      color: #92400E;
      border: 1px solid #F59E0B;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
    }
    .wp-wireframe-count {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.75rem;
      font-weight: 800;
      color: #334155;
      background-color: #E2E8F0;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
    }
    .wp-wireframe-thumb-row {
      display: grid;
      grid-template-columns: 120px 1fr;
      gap: 14px;
      align-items: center;
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-sm);
      padding: 10px;
    }
    .wp-wireframe-thumb-row img {
      width: 120px;
      height: 76px;
      object-fit: cover;
      border-radius: var(--radius-sm);
    }
    .wp-wireframe-list {
      display: flex;
      flex-direction: column;
      gap: 7px;
      padding: 12px 14px;
      background-color: #FFFFFF;
      border: 1px dashed #CBD5E1;
      border-radius: var(--radius-sm);
      font-size: 0.84rem;
      color: var(--text-body);
    }
    .wp-wireframe-list-item {
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }
    .wp-wireframe-list-item svg {
      color: #D97706;
      flex-shrink: 0;
      margin-top: 3px;
    }

    /* Sponsors Showcase */
    .sponsor-tier-block {
      margin-bottom: 36px;
    }
    .sponsor-tier-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
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
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      padding: 5px 12px;
      border-radius: var(--radius-sm);
    }
    .tier-gold {
      background-color: var(--scf-gold-soft);
      color: #92400E;
      border: 1px solid #F59E0B;
    }
    .tier-silver {
      background-color: #F1F5F9;
      color: #1E293B;
      border: 1px solid #CBD5E1;
    }
    .tier-green {
      background-color: var(--scf-green-soft);
      color: #065F46;
      border: 1px solid #6EE7B7;
    }

    .sponsors-gold-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }
    .sponsors-silver-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 18px;
    }
    .sponsors-banden-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
    }
    .sponsor-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 20px;
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
      border-color: var(--scf-green);
      box-shadow: var(--shadow-md);
    }
    .sponsor-card.gold-card {
      border: 2px solid #F59E0B;
      padding: 24px;
    }
    .sponsor-logo-wrap {
      width: 100%;
      height: 104px;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #FFFFFF;
      padding: 6px;
    }
    .sponsor-card.gold-card .sponsor-logo-wrap {
      height: 124px;
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
      font-size: 0.96rem;
      font-weight: 800;
      color: var(--scf-navy);
      line-height: 1.25;
    }
    .sponsor-role-tag {
      font-size: 0.77rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-top: 3px;
    }

    .pillar-count {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.75rem;
      font-weight: 800;
      color: #065F46;
      background-color: var(--scf-green-soft);
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      align-self: flex-start;
      text-transform: uppercase;
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
      color: var(--scf-green);
      flex-shrink: 0;
      margin-top: 3px;
    }
    .card-badge {
      position: absolute;
      top: 12px;
      left: 12px;
      background-color: var(--scf-navy-deep);
      color: var(--scf-gold-bright);
      font-family: 'Montserrat', sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }

    .board-role {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--scf-green);
    }
    .board-name {
      font-family: 'Montserrat', sans-serif;
      font-size: 1.02rem;
      font-weight: 800;
      color: var(--scf-navy);
    }

    /* Footer */
    .site-footer {
      background-color: var(--scf-navy-deep);
      color: #E2E8F0;
      padding: 68px 0 36px;
      border-top: 4px solid var(--scf-green);
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
      gap: 8px;
    }
    .footer-list a, .footer-list button {
      color: #CBD5E1;
      font-size: 0.87rem;
      background: none;
      border: none;
      text-align: left;
      cursor: pointer;
      font-family: inherit;
      padding: 5px 0;
      min-height: 32px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
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
      color: var(--scf-gold-bright);
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
      background-color: rgba(11, 21, 40, 0.8);
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
      border: 2px solid var(--scf-gold);
      border-radius: var(--radius-md);
      max-width: 640px;
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
      color: var(--scf-navy);
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
      color: var(--scf-green);
      flex-shrink: 0;
      margin-top: 2px;
    }

    /* Responsive Breakpoints */
    @media (max-width: 1120px) {
      .hero-grid {
        grid-template-columns: 1fr;
      }
      .grid-4, .sponsors-banden-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .grid-3, .sponsors-gold-grid, .sponsors-silver-grid {
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
      .wp-arch-inner {
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
      }
      .wp-arch-cta {
        width: 100%;
      }
      .hero-kpi-strip {
        grid-template-columns: repeat(2, 1fr);
      }
      .hero-secondary-row,
      .grid-2,
      .grid-3,
      .grid-4,
      .wp-wireframe-grid,
      .wp-wireframe-thumb-row,
      .sponsors-gold-grid,
      .sponsors-silver-grid,
      .sponsors-banden-grid,
      .footer-grid {
        grid-template-columns: 1fr;
      }
      .wp-wireframe-thumb-row img {
        width: 100%;
        height: 150px;
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
  <meta name="description" content="Sportclub Fulenbach (gegründet Sommer 1944, SOFV-Verein Nr. 1826) — 14 Mannschaften, 1. Mannschaft (2. Liga regional), Juniorengruppierung rot/blau, Sportplatz Bad &amp; Clubhaus in 4629 Fulenbach.">
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
  <!-- STICKY HEADER MIT STATUS-DOTS -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="SC Fulenbach Startseite">
        <img src="images/logo-scfulenbach.webp" alt="Wappen SC Fulenbach" class="brand-logo" width="50" height="50" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">SC FULENBACH</span>
          <span class="brand-sub" data-slot="brand_sub">SEIT 1944 · SPORTPLATZ BAD</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation">
        <a href="index.html" class="nav-link {nav_start}">
          <span class="wp-status-dot wp-dot-green" aria-hidden="true"></span>
          <span>Startseite (Beispiel)</span>
        </a>
        <a href="herren-1.html" class="nav-link {nav_teams}">
          <span class="wp-status-dot wp-dot-amber" aria-hidden="true"></span>
          <span>Beispiel-Team: 1. Mannschaft (1/14)</span>
        </a>
        <a href="index.html#sponsoren" class="nav-link">
          <span class="wp-status-dot wp-dot-green" aria-hidden="true"></span>
          <span>Sponsoren (Übernommen)</span>
        </a>
        <button type="button" class="nav-link nav-blueprint-trigger" onclick="wpOpenBlueprintModal('Verein, Vorstand, Clubhaus &amp; Events (40 weitere Seiten)', 'Bereiche B, C &amp; D (40 von 43 Seiten vorbereitet)', 'Präsident Willi von Arx (vorstand@scfulenbach.ch) · Clubhaus: René Hofstetter (079 302 62 47)', 'clubhaus')">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          <span>Verein &amp; Sportanlage (40 Seiten offen)</span>
        </button>
        <a href="kontakt.html" class="nav-link {nav_kontakt}">
          <span class="wp-status-dot wp-dot-green" aria-hidden="true"></span>
          <span>Smart-Anfrage (Live-Demo)</span>
        </a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-primary btn-sm" data-slot="header_cta">
          <span>Probetraining &amp; Anfrage</span>
        </a>
        <button type="button" class="mobile-toggle" id="mobileMenuBtn" aria-label="Menü öffnen" onclick="wpToggleMobileMenu()">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    </div>

    <div class="mobile-drawer" id="mobileDrawer">
      <a href="index.html" onclick="wpCloseMobileMenu()">
        <span class="wp-status-dot wp-dot-green"></span>
        <span>Startseite (Beispiel-Ansicht)</span>
      </a>
      <a href="herren-1.html" onclick="wpCloseMobileMenu()">
        <span class="wp-status-dot wp-dot-amber"></span>
        <span>Beispiel-Team: 1. Mannschaft (1/14 ausgearbeitet · 13 weitere folgen)</span>
      </a>
      <a href="index.html#sponsoren" onclick="wpCloseMobileMenu()">
        <span class="wp-status-dot wp-dot-green"></span>
        <span>Sponsoren &amp; 100er-Club (100 % übernommen)</span>
      </a>
      <a href="index.html#seiten-uebersicht" onclick="wpCloseMobileMenu()">
        <span class="wp-status-dot wp-dot-amber"></span>
        <span>Verein, Sportplatz Bad &amp; Anlässe (40 weitere Seiten)</span>
      </a>
      <a href="kontakt.html" onclick="wpCloseMobileMenu()">
        <span class="wp-status-dot wp-dot-green"></span>
        <span>Smart-Anfrage &amp; 1-Seiten-PDF-Dossier (Live-Demo)</span>
      </a>
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
            <img src="images/logo-scfulenbach.webp" alt="SC Fulenbach Wappen" width="46" height="46" loading="lazy" decoding="async" style="object-fit:contain;">
            <div>
              <div style="font-family:'Montserrat',sans-serif;font-weight:800;font-size:1.1rem;color:#FFFFFF;">SC FULENBACH</div>
              <div style="font-size:0.75rem;color:#FBBF24;font-weight:700;">GEGRÜNDET SOMMER 1944 · SOFV NR. 1826</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#CBD5E1;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Heimat für 14 Mannschaften im Gäu und Untergäu: 1. Mannschaft (2. Liga regional), 2. Mannschaft (4. Liga), Senioren 30+, 5 Teams der Juniorengruppierung rot/blau (mit FC Wolfwil &amp; FC Kestenholz) sowie 6 Junioren-Teams D bis G auf dem Sportplatz Bad.
          </p>
          <div style="font-size:0.84rem;color:#E2E8F0;font-weight:600;">
            Sportplatz Bad · Ewigkeitstrasse 5 · 4629 Fulenbach
          </div>
        </div>

        <div>
          <div class="footer-title">Ausgearbeitete Beispiel-Seiten (3 von 43)</div>
          <ul class="footer-list">
            <li><a href="index.html"><span class="wp-status-dot wp-dot-green"></span><span>Startseite &amp; Seiten-Übersicht</span></a></li>
            <li><a href="herren-1.html"><span class="wp-status-dot wp-dot-amber"></span><span>Beispiel-Team: 1. Mannschaft (2. Liga)</span></a></li>
            <li><a href="herren-1.html#alle-teams-matrix"><span class="wp-status-dot wp-dot-amber"></span><span>Alle 14 Teams in der Übersicht</span></a></li>
            <li><a href="index.html#sponsoren"><span class="wp-status-dot wp-dot-green"></span><span>Alle 88 Sponsoren-Einträge &amp; 100er-Club</span></a></li>
            <li><a href="kontakt.html"><span class="wp-status-dot wp-dot-green"></span><span>Smart-Anfrage &amp; PDF-Dossier testen</span></a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Weitere Bereiche (40 von 43 vorbereitet)</div>
          <ul class="footer-list">
            <li><button type="button" onclick="wpOpenBlueprintModal('Bereich A: 13 weitere Mannschaften (11 Unterseiten)', '2. Mannschaft, Senioren 30+, Gruppierung rot/blau &amp; Junioren D–G', 'Sportchef Mirko Ferrari (079 397 87 73) &amp; Juniorenobmann Michael «Mike» Frieder (079 647 13 33)', 'probetraining')">13 weitere Teams (Bereich A)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Bereich B: Verein, Vorstand (11), Schiedsrichter &amp; Chronik 1944', '11 Vereins-Unterseiten für den Hauptauftrag vorgemerkt', 'Präsident Willi von Arx (vorstand@scfulenbach.ch) · Ehrenpräsident Urs Lehmann', 'mitgliedschaft')">Vorstand, SR &amp; Chronik 1944 (Bereich B)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Bereich C: Sportplatz Bad, Clubhaus (100 Plätze) &amp; Events', '11 Anlage- &amp; Anlass-Unterseiten (folgen beim Ausbau)', 'Clubhaus-Vermietung: René Hofstetter (Tel. 079 302 62 47) · Infrastruktur: Alfred Ammann', 'clubhaus')">Clubhaus mieten &amp; Badfest (Bereich C)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Bereich D: Spielbetrieb, Matchberichte, Lagerwoche &amp; Fanshop', '7 Spielbetriebs- &amp; Shop-Unterseiten (folgen beim Ausbau)', 'Medien &amp; Support: David Ackermann (david.ackermann@scfulenbach.ch)', 'fanshop')">Lagerwoche &amp; SCF-Fanshop (Bereich D)</button></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direkt-Service &amp; Ressorts</div>
          <ul class="footer-list">
            <li><a href="kontakt.html?thema=probetraining">Probetraining / Junioren anmelden</a></li>
            <li><a href="kontakt.html?thema=sponsoring">Sponsoring, Bande &amp; 100er-Club G&amp;F</a></li>
            <li><a href="kontakt.html?thema=clubhaus">Clubhaus Bad mieten (100 Plätze)</a></li>
            <li><a href="kontakt.html?thema=spielbetrieb">Schiedsrichter werden (CHF 500/Jahr)</a></li>
            <li><a href="kontakt.html?thema=fanshop">SCF-Fanshop (Cap CHF 25 / Wimpel CHF 15)</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz (revDSG)</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Sportclub Fulenbach (4629 Fulenbach) · Unverbindlicher Vorschau-Entwurf (3 Beispiel-Seiten live, 40 weitere vorbereitet).</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;">
          <a href="herren-1.html" style="color:#FBBF24;font-weight:700;">Beispiel-Team 1. Mannschaft &amp; 14-Teams-Matrix</a>
          <a href="kontakt.html" style="color:#E2E8F0;">Smart-Anfrage-Zentrale</a>
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
      <div class="section-kicker">SEITEN-VORSCHAU · SC FULENBACH (FOLGT BEIM AUSBAU)</div>
      <h3 id="wpBpTitle" style="font-size:1.32rem;font-weight:800;margin-bottom:8px;">Weitere Vereins-Seite: Vorbereitet für den Ausbau</h3>
      <p id="wpBpSub" style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
        Die aktuelle Website <strong>scfulenbach.ch</strong> umfasst <strong>43 Seiten</strong> und <strong>14 Mannschaften</strong>. Damit der Vorstand das neue Design, die Sponsoren-Integration und die digitale Anfrage-Zentrale vorab ohne Risiko prüfen kann, wurden in diesem Prototyp bewusst <strong>3 von 43 Seiten (7 %)</strong> exemplarisch bis ins Detail gebaut.
      </p>
      <div style="background-color:var(--scf-green-soft);border-left:4px solid var(--scf-green);padding:12px 14px;border-radius:var(--radius-sm);font-size:0.86rem;margin-bottom:14px;">
        <div style="font-weight:700;color:var(--scf-navy);" id="wpBpCategory">Bereich: Verein / Mannschaften / Sportplatz Bad</div>
        <div style="color:var(--text-body);margin-top:2px;" id="wpBpContact">Zuständige Ansprechperson im SC Fulenbach: Vorstand / Sportchef</div>
      </div>

      <div class="wp-modal-checklist">
        <div style="font-family:'Montserrat',sans-serif;font-size:0.78rem;font-weight:800;text-transform:uppercase;color:var(--scf-navy);">
          Was bei Freigabe des Hauptauftrags in diesem Modul eins zu eins ausgebaut wird:
        </div>
        <div class="wp-modal-check-item">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Vollständige Übernahme aller Original-Fotos, Kaderlisten, Trainingszeiten und Berichte von scfulenbach.ch</span>
        </div>
        <div class="wp-modal-check-item">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Direkte SOFV-Resultate- und Spielplan-Einbindung (Verein Nr. 1826) sowie Sponsoren-Zuordnung pro Team</span>
        </div>
        <div class="wp-modal-check-item">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Direkt-Routing von Anfragen (Probetraining, Clubhaus-Miete, Sponsoring) mit 1-Seiten-PDF-Dossier ans Ressort</span>
        </div>
        <div class="wp-modal-check-item">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Einfache Einreichung von Mannschaftsfotos, Kaderlisten und Trainerangaben über das Online-Trainerformular</span>
        </div>
      </div>

      <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:18px;">
        <a href="team-update.html?team=1-mannschaft" id="wpBpTeamUpdateLink" class="btn-cta btn-cta-gold btn-sm">
          <span>Mannschafts-Daten &amp; Kader einreichen (Trainer-Formular)</span>
        </a>
        <a href="herren-1.html" class="btn-cta btn-cta-primary btn-sm" onclick="wpCloseBlueprintModal()">
          <span>Ausgearbeitetes Beispiel-Team (1. Mannschaft) ansehen</span>
        </a>
        <a href="kontakt.html?thema=probetraining" id="wpBpCtaLink" class="btn-cta btn-cta-outline btn-sm">
          <span>Anfrage für dieses Ressort live testen</span>
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
      <h3 id="wpImpTitle" style="font-size:1.3rem;font-weight:800;margin-bottom:10px;">Impressum &amp; Datenschutz — Sportclub Fulenbach</h3>
      <div style="font-size:0.88rem;color:var(--text-body);display:flex;flex-direction:column;gap:10px;">
        <p><strong>Vereinsadresse &amp; Sportanlage:</strong><br>Sportclub Fulenbach (SOFV-Verein Nr. 1826) · Sportplatz Bad · Ewigkeitstrasse 5 · 4629 Fulenbach</p>
        <p><strong>Vertretungsberechtigter Vorstand:</strong><br>Willi von Arx (Präsident · vorstand@scfulenbach.ch) · Elias Sidler (Vize-Präsident / Anlässe) · Rahel Napoli (Aktuarin) · Roland Wiss (Finanzen &amp; Verwaltung a.i.) · Mirko Ferrari (Sportchef · mirko.ferrari@scfulenbach.ch) · Andreas Guldimann (Sponsoring / Marketing · andreas.guldimann@scfulenbach.ch) · Michael «Mike» Frieder (Juniorenobmann) · Alfred Ammann (Infrastruktur)</p>
        <p><strong>Medien, Support &amp; Webmaster:</strong><br>David Ackermann (david.ackermann@scfulenbach.ch) · Robin Müller (Social Media / Anlässe)</p>
        <p><strong>Datenschutz (Schweizer Datenschutzgesetz revDSG):</strong><br>Personendaten aus Kontakt-, Probetraining-, Clubhaus- und Sponsoring-Anfragen werden ausschliesslich zur Vereinsadministration innerhalb des Sportclub Fulenbach verwendet und niemals an unbefugte Dritte weitergegeben.</p>
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
      var lEl = document.getElementById('wpBpCtaLink');
      if (tEl && title) tEl.textContent = title;
      if (cEl && category) cEl.textContent = 'Bereich / Umfang: ' + category;
      if (pEl && contact) pEl.textContent = 'Zuständig im SC Fulenbach: ' + contact;
      if (lEl) {{
        var q = topicParam ? ('?thema=' + encodeURIComponent(topicParam)) : '?thema=probetraining';
        lEl.href = 'kontakt.html' + q;
      }}
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
      }}
    }});
  </script>
</body>
</html>
"""

INDEX_BODY = f"""
  <!-- 1. HERO (VOLL AUSGEBAUTE MUSTER-SEKTION 1) -->
  <section class="hero-section" data-section="hero">
    <div class="container">
      <div class="hero-grid">
        <div>
          <div class="section-kicker kicker-light" data-slot="hero_kicker">GEGRÜNDET SOMMER 1944 · SOFV-VEREIN NR. 1826 · SPORTPLATZ BAD</div>
          <h1 class="hero-title" data-slot="hero_title">
            Herzblut, Nachwuchs &amp; <span>Fussballtradition in 4629 Fulenbach.</span>
          </h1>
          <p class="hero-lead" data-slot="hero_lead">
            Vom historischen Aufstieg unserer <strong>1. Mannschaft in die 2. Liga regional</strong> über die 2. Mannschaft («Zwöi» · 4. Liga) und die Senioren 30+ bis zur starken <strong>Juniorengruppierung rot/blau</strong> (mit FC Wolfwil &amp; FC Kestenholz) und den Junioren D bis G: Auf dem Sportplatz Bad lebt der SC Fulenbach seit 1944 echten Vereinsgeist.
          </p>

          <div class="hero-cta-row">
            <a href="herren-1.html" class="btn-cta btn-cta-gold" data-slot="hero_cta_primary">
              <span>Beispiel-Team: 1. Mannschaft (1/14)</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </a>
            <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-primary" data-slot="hero_cta_secondary">
              <span>Smart-Anfrage &amp; PDF-Dossier testen</span>
            </a>
            <a href="#seiten-uebersicht" class="btn-cta btn-cta-ghost-light">
              <span>Übersicht (40 weitere Seiten)</span>
            </a>
          </div>

          <div class="hero-kpi-strip">
            <div class="hero-kpi-box">
              <div class="hero-kpi-num" data-slot="kpi_1_num">1944</div>
              <div class="hero-kpi-label" data-slot="kpi_1_label">Gegründet in Fulenbach</div>
            </div>
            <div class="hero-kpi-box">
              <div class="hero-kpi-num" data-slot="kpi_2_num">14 Teams</div>
              <div class="hero-kpi-label" data-slot="kpi_2_label">Aktive, Senioren &amp; Junioren</div>
            </div>
            <div class="hero-kpi-box">
              <div class="hero-kpi-num" data-slot="kpi_3_num">Sportplatz Bad</div>
              <div class="hero-kpi-label" data-slot="kpi_3_label">Clubhaus mit 100 Plätzen</div>
            </div>
            <div class="hero-kpi-box">
              <div class="hero-kpi-num" data-slot="kpi_4_num">88 Partner</div>
              <div class="hero-kpi-label" data-slot="kpi_4_label">Sponsoren &amp; 100er-Club</div>
            </div>
          </div>
        </div>

        <div class="hero-visual-stack">
          <div class="hero-main-photo-card">
            <img src="images/team-herren-1.webp" alt="SC Fulenbach 1. Mannschaft 2. Liga regional" width="760" height="300" data-slot="hero_img_main">
            <div class="hero-photo-caption">
              <strong>1. Mannschaft — 2. Liga regional (Beispiel-Team 1/14 fertig)</strong>
              <span>Trainer: Kay Ackermann &amp; Roland Wiss · 20 Kaderspieler</span>
            </div>
          </div>

          <div class="hero-secondary-row">
            <div class="hero-mini-card">
              <img src="images/sportplatz-bad-1.webp" alt="Sportplatz Bad und Clubhaus SC Fulenbach" width="380" height="136" data-slot="hero_img_secondary">
              <div class="hero-mini-body">
                <strong style="color:#FBBF24;font-family:'Montserrat',sans-serif;">Sportplatz Bad &amp; Clubhaus (100 Plätze)</strong><br>
                <span>Ewigkeitstrasse 5 · Vermietung: René Hofstetter (079 302 62 47)</span>
              </div>
            </div>
            <div class="hero-mini-card">
              <img src="images/vorstand-gruppe.webp" alt="Vorstand SC Fulenbach um Präsident Willi von Arx" width="380" height="136" data-slot="hero_img_board">
              <div class="hero-mini-body">
                <strong style="color:#34D399;font-family:'Montserrat',sans-serif;">Vorstand &amp; Tradition seit 1944</strong><br>
                <span>Präsident Willi von Arx · Ehrenpräsident Urs Lehmann · 11 Vorstandsmitglieder</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. SEITEN-ÜBERSICHT (40 WEITERE SEITEN VORBEREITET) -->
  <section id="seiten-uebersicht" class="wp-uebersicht-section" data-section="seiten-uebersicht">
    <div class="container">
      <div class="wp-uebersicht-banner">
        <div style="max-width:780px;">
          <div class="section-kicker kicker-light" style="margin-bottom:6px;">ÜBERSICHT DER WEITEREN SEITEN (40 VON 43 SEITEN FOLGEN BEIM AUSBAU)</div>
          <h2 style="color:#FFFFFF;font-size:clamp(1.45rem,2.4vw,2rem);font-weight:800;margin-bottom:8px;">
            Vorschau-Entwurf: 3 Beispiel-Seiten sind bereits ausgearbeitet — 40 weitere Unterseiten folgen beim Ausbau.
          </h2>
          <p style="font-size:0.92rem;color:#E2E8F0;line-height:1.58;">
            Die bestehende ClubDesk-Website <strong>scfulenbach.ch</strong> umfasst exakt <strong>43 Seiten</strong> und <strong>14 Mannschaften</strong>. In diesem Entwurf V2 siehst du die Startseite, die <strong>1. Mannschaft (1/14)</strong>, alle <strong>88 Sponsoren-Einträge</strong> sowie die <strong>Smart-Anfrage-Zentrale</strong> im fertigen Vollausbau. Die folgenden <strong>4 weitere Bereiche (40 Unterseiten)</strong> sind als übersichtliche Platzhalter vorbereitet und werden bei Auftragserteilung 1:1 mit allen Originaldaten übertragen.
          </p>
        </div>
        <div style="display:flex;flex-direction:column;gap:8px;flex-shrink:0;">
          <a href="herren-1.html" class="btn-cta btn-cta-gold btn-sm">Beispiel-Team (1/14) öffnen</a>
          <a href="kontakt.html" class="btn-cta btn-cta-ghost-light btn-sm">Smart-Anfrage live testen</a>
        </div>
      </div>

      <div class="wp-wireframe-grid">
        <!-- BEREICH A -->
        <article class="wp-wireframe-card">
          <div>
            <div class="wp-wireframe-top">
              <span class="wp-wireframe-tag">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/></svg>
                <span>BEREICH A · MANNSCHAFTEN</span>
              </span>
              <span class="wp-wireframe-count">Ausbaustufe: 1 / 14 Teams = 7 % (11 Seiten offen)</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:800;margin:14px 0 8px;">13 weitere Mannschafts-Seiten &amp; Trainer-Übersicht</h3>
            <p style="font-size:0.89rem;color:var(--text-body);margin-bottom:14px;">
              Neben der fertig ausgebauten <strong>1. Mannschaft (2. Liga regional)</strong> führt der SC Fulenbach 13 weitere Teams im aktiven Spielbetrieb. Jedes Team erhält im Hauptauftrag dieselbe Kader-, Trainer- und Sponsoren-Darstellung wie das Beispiel-Team.
            </p>
            <div class="wp-wireframe-thumb-row" style="margin-bottom:14px;">
              <img src="images/team-herren-2.webp" alt="SC Fulenbach 2. Mannschaft 4. Liga und Senioren 30+" width="120" height="76" loading="lazy" decoding="async">
              <div style="font-size:0.8rem;color:var(--text-body);">
                <strong style="color:var(--scf-navy);">Original-Teamfotos bereits gesichert:</strong><br>
                2. Mannschaft («Zwöi» · 4. Liga, Marc Haldemann &amp; Emanuel Wyss, 29 Spieler) &amp; Senioren 30+ (Walter Müller &amp; Christian Napoli, 26 Spieler).
              </div>
            </div>
            <div class="wp-wireframe-list">
              <div class="wp-wireframe-list-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                <span><strong>Aktive &amp; Senioren:</strong> 2. Mannschaft (4. Liga SOFV) &amp; Senioren 30+ (Meisterschaft &amp; Cup)</span>
              </div>
              <div class="wp-wireframe-list-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                <span><strong>Juniorengruppierung rot/blau (5 Teams):</strong> Junioren B, Ca, Cb, D (9er) &amp; D (7er) mit FC Wolfwil &amp; FC Kestenholz</span>
              </div>
              <div class="wp-wireframe-list-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                <span><strong>Junioren SC Fulenbach (6 Teams):</strong> Junioren D (9er/7er), Ea, Eb, F &amp; G (Obmann: Michael «Mike» Frieder)</span>
              </div>
            </div>
          </div>
          <div style="display:flex;gap:10px;flex-wrap:wrap;">
            <a href="herren-1.html#alle-teams-matrix" class="btn-cta btn-cta-navy btn-sm" style="flex:1;">
              <span>Zur 14-Teams-Übersicht</span>
            </a>
            <button type="button" class="btn-cta btn-cta-outline btn-sm" style="flex:1;" onclick="wpOpenBlueprintModal('Bereich A: 13 weitere Mannschaften &amp; Trainer-Übersicht', '11 Mannschafts-Unterseiten auf scfulenbach.ch (1/14 fertig)', 'Sportchef Mirko Ferrari (079 397 87 73) &amp; Juniorenobmann Michael «Mike» Frieder (079 647 13 33)', 'probetraining')">
              <span>Modul-Details öffnen</span>
            </button>
          </div>
        </article>

        <!-- BEREICH B -->
        <article class="wp-wireframe-card">
          <div>
            <div class="wp-wireframe-top">
              <span class="wp-wireframe-tag">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span>BEREICH B · VEREIN &amp; VORSTAND</span>
              </span>
              <span class="wp-wireframe-count">11 Seiten offen (Ausbaustufe: 0 %)</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:800;margin:14px 0 8px;">Verein, Vorstand (11), Schiedsrichter, 100er-Club &amp; Chronik 1944</h3>
            <p style="font-size:0.89rem;color:var(--text-body);margin-bottom:14px;">
              Alle Vereinsorgane, die 82-jährige Vereinsgeschichte seit Sommer 1944 (Gründung durch 7 Fulenbacher Spieler aus dem SC Wynau; erster Präsident Hans Buchmann) sowie das Schiedsrichterwesen werden hier gebündelt.
            </p>
            <div class="wp-wireframe-thumb-row" style="margin-bottom:14px;">
              <img src="images/vorstand-gruppe.webp" alt="Vorstand SC Fulenbach Gruppenfoto" width="120" height="76" loading="lazy" decoding="async">
              <div style="font-size:0.8rem;color:var(--text-body);">
                <strong style="color:var(--scf-navy);">11 Vorstandsmitglieder &amp; 4 aktive Schiedsrichter:</strong><br>
                Willi von Arx (Präsident), Elias Sidler (Vize), Urs Lehmann (Ehrenpräsident), Rahel Napoli, Andreas Guldimann, Alfred Ammann, Mirko Ferrari, Mike Frieder, David Ackermann, Roland Wiss &amp; Robin Müller.
              </div>
            </div>
            <div class="wp-wireframe-list">
              <div class="wp-wireframe-list-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                <span><strong>Schiedsrichter-wesen (4 SR):</strong> Fisnik Kadriu, Musanje Beka, Patrik Hugentobler &amp; Serdar Sönmez (CHF 500/Jahr + Ausrüstung &amp; SFV-Ausweis)</span>
              </div>
              <div class="wp-wireframe-list-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                <span><strong>Gönner &amp; Freunde (100er-Club):</strong> Gezielte Förderung von Junioren &amp; Gesamtverein (c/o Schaad Treuhand AG)</span>
              </div>
              <div class="wp-wireframe-list-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                <span><strong>Dokumente &amp; Chronik:</strong> Vereinsstatuten, Datenschutz, 82. Generalversammlung &amp; Chronik seit 1944</span>
              </div>
            </div>
          </div>
          <div style="display:flex;gap:10px;flex-wrap:wrap;">
            <button type="button" class="btn-cta btn-cta-navy btn-sm" style="flex:1;" onclick="wpOpenBlueprintModal('Bereich B: Verein, Vorstand (11), Schiedsrichter &amp; Chronik 1944', '11 Vereins-Unterseiten (Vorstand, Statuten, Geschichte, Datenschutz, SR-Ausbildung, G&amp;F 100er-Club, GV)', 'Präsident Willi von Arx (vorstand@scfulenbach.ch) · SR-Verantwortlicher Mirko Ferrari (079 397 87 73)', 'mitgliedschaft')">
              <span>Seiten-Übersicht (11 Seiten) ansehen</span>
            </button>
            <a href="kontakt.html?thema=mitgliedschaft" class="btn-cta btn-cta-outline btn-sm" style="flex:1;">
              <span>Vorstand kontaktieren</span>
            </a>
          </div>
        </article>

        <!-- BEREICH C -->
        <article class="wp-wireframe-card">
          <div>
            <div class="wp-wireframe-top">
              <span class="wp-wireframe-tag">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span>BEREICH C · SPORTPLATZ BAD &amp; EVENTS</span>
              </span>
              <span class="wp-wireframe-count">11 Seiten offen (Ausbaustufe: 0 %)</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:800;margin:14px 0 8px;">Sportplatz Bad, Clubhaus-Vermietung (100 Plätze) &amp; Anlässe</h3>
            <p style="font-size:0.89rem;color:var(--text-body);margin-bottom:14px;">
              Das gemütliche Clubhaus auf dem Sportplatz Bad (Ewigkeitstrasse 5, 4629 Fulenbach) bietet Platz für bis zu <strong>100 Personen</strong> und kann für Familienfeste, Firmenanlässe und Vereinsversammlungen gemietet werden.
            </p>
            <div class="wp-wireframe-thumb-row" style="margin-bottom:14px;">
              <img src="images/clubhaus-aussen.webp" alt="Clubhaus SC Fulenbach Sportplatz Bad" width="120" height="76" loading="lazy" decoding="async">
              <div style="font-size:0.8rem;color:var(--text-body);">
                <strong style="color:var(--scf-navy);">Clubhaus-Vermietung &amp; Belegungsplan:</strong><br>
                Direkte Reservationsanfrage bei <strong>René Hofstetter</strong> (Tel. 079 302 62 47) inkl. Innen- &amp; Aussenansichten und Live-Belegungskalender.
              </div>
            </div>
            <div class="wp-wireframe-list">
              <div class="wp-wireframe-list-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                <span><strong>Sportanlage &amp; Clubhaus:</strong> Standortkarte Ewigkeitstrasse 5, Clubhaus-Miete (100 Plätze) &amp; Belegungsplan</span>
              </div>
              <div class="wp-wireframe-list-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                <span><strong>Traditions-Anlässe:</strong> Badfest mit Dorfturnier &amp; KUBB-Turnier, Whisky Night, Raclette-Abend vom Zwöii, Cordon-bleu-Festival &amp; SCF-Tag</span>
              </div>
              <div class="wp-wireframe-list-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                <span><strong>Fotogalerie (33 Alben):</strong> Anlässe, Aufstiegsspiele, Gönner-Events &amp; Juniorenturniere seit 2018</span>
              </div>
            </div>
          </div>
          <div style="display:flex;gap:10px;flex-wrap:wrap;">
            <button type="button" class="btn-cta btn-cta-navy btn-sm" style="flex:1;" onclick="wpOpenBlueprintModal('Bereich C: Sportplatz Bad, Clubhaus (100 Plätze) &amp; Vereinsanlässe', '11 Unterseiten (Standort, Clubhaus mieten, Belegungsplan, Badfest/Dorfturnier, Whisky Night, Raclette-Abend, Cordon-bleu-Festival, 33 Fotoalben)', 'Clubhaus-Vermietung: René Hofstetter (Tel. 079 302 62 47) · Vize-Präsident / Anlässe: Elias Sidler', 'clubhaus')">
              <span>Seiten-Übersicht (11 Seiten) ansehen</span>
            </button>
            <a href="kontakt.html?thema=clubhaus" class="btn-cta btn-cta-outline btn-sm" style="flex:1;">
              <span>Clubhaus-Miete anfragen</span>
            </a>
          </div>
        </article>

        <!-- BEREICH D -->
        <article class="wp-wireframe-card">
          <div>
            <div class="wp-wireframe-top">
              <span class="wp-wireframe-tag">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span>BEREICH D · SPIELBETRIEB, LAGER &amp; SHOP</span>
              </span>
              <span class="wp-wireframe-count">7 Seiten offen (Ausbaustufe: 0 %)</span>
            </div>
            <h3 style="font-size:1.22rem;font-weight:800;margin:14px 0 8px;">Spielbetrieb, Matchberichte, Juniorenlager &amp; SCF-Fanshop</h3>
            <p style="font-size:0.89rem;color:var(--text-body);margin-bottom:14px;">
              Von den laufenden Matchberichten der Aktiv- und Seniorenteams über die legendäre Juniorenlager-Woche auf dem Sportplatz Bad bis zum offiziellen SCF-Onlineshop.
            </p>
            <div class="wp-wireframe-thumb-row" style="margin-bottom:14px;">
              <img src="images/junioren-lager.webp" alt="Juniorenlager-Woche SC Fulenbach auf dem Sportplatz Bad" width="120" height="76" loading="lazy" decoding="async">
              <div style="font-size:0.8rem;color:var(--text-body);">
                <strong style="color:var(--scf-navy);">Juniorenlager-Woche &amp; Sponsorenlauf:</strong><br>
                Über 50 begeisterte Kinder, 20 Helferinnen und Helfer sowie unvergessliche Highlights auf dem Sportplatz Bad.
              </div>
            </div>
            <div class="wp-wireframe-list">
              <div class="wp-wireframe-list-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                <span><strong>News &amp; Matchberichte:</strong> Aktuelle Spielberichte der 1. Mannschaft (2. Liga), 2. Mannschaft &amp; Senioren 30+</span>
              </div>
              <div class="wp-wireframe-list-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                <span><strong>Nachwuchs-Highlights:</strong> Juniorenlager-Woche &amp; Sponsorenlauf (Formulare &amp; Impressionen)</span>
              </div>
              <div class="wp-wireframe-list-item">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                <span><strong>Fanartikel &amp; Onlineshop:</strong> Offizielle SCF-Cap (CHF 25.–) &amp; SCF-Wimpel (CHF 15.–) direkt bestellbar</span>
              </div>
            </div>
          </div>
          <div style="display:flex;gap:10px;flex-wrap:wrap;">
            <button type="button" class="btn-cta btn-cta-navy btn-sm" style="flex:1;" onclick="wpOpenBlueprintModal('Bereich D: Spielbetrieb, Matchberichte, Lagerwoche &amp; SCF-Fanshop', '7 Unterseiten (News, Matchberichte 1./2. Mannschaft &amp; Senioren, Juniorenlager, Sponsorenlauf, Fanshop)', 'Medien &amp; Support: David Ackermann (david.ackermann@scfulenbach.ch) · Sportchef: Mirko Ferrari', 'fanshop')">
              <span>Seiten-Übersicht (7 Seiten) ansehen</span>
            </button>
            <a href="kontakt.html?thema=fanshop" class="btn-cta btn-cta-outline btn-sm" style="flex:1;">
              <span>Fanartikel / Lager anfragen</span>
            </a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- 3. UNSERE SPONSOREN, GÖNNER & PARTNER (VOLL AUSGEBAUTE MUSTER-SEKTION 2: 100% ORIGINAL-BESTAND) -->
  <section id="sponsoren" data-section="sponsoren" style="background-color:#FFFFFF;">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="sponsors_kicker">VOLLSTÄNDIG ÜBERNOMMEN · ALLE 88 SPONSOREN-EINTRÄGE VON SCFULENBACH.CH</div>
        <h2 class="section-title" data-slot="sponsors_title">Unsere Hauptsponsoren, Co-Sponsoren, Silbersponsoren &amp; Bandenpartner.</h2>
        <p class="section-desc" data-slot="sponsors_desc">
          Ein herzliches Dankeschön an unsere Haupt- und Co-Sponsoren, die 6 Silbersponsoren, die 3 Mannschaftssponsoren der 1. Mannschaft, alle {BANDEN_COUNT} Banden- und Vereinssponsoren sowie die <strong>Gönner und Freunde des Sportclub Fulenbach (100er-Club)</strong>. Sämtliche Partner wurden eins zu eins mit Original-Logo und Verlinkung übernommen.
        </p>
      </div>

      <!-- TIER 1: HAUPTSPONSOREN (2) & CO-SPONSOR (1) -->
      <div class="sponsor-tier-block">
        <div class="sponsor-tier-header">
          <span class="sponsor-tier-badge tier-gold">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            <span>HAUPTSPONSOREN &amp; OFFIZIELLER CO-SPONSOR</span>
          </span>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">2 Hauptsponsoren &amp; 1 Co-Sponsor des SC Fulenbach</span>
        </div>

        <div class="sponsors-gold-grid">
          <div class="sponsor-card gold-card">
            <div class="sponsor-logo-wrap">
              <img src="images/sponsors/sponsor-1000837-goenner-und-freunde-des-sportclub-fulenb.webp" alt="Gönner und Freunde des Sportclub Fulenbach 100er-Club" width="280" height="110" loading="lazy" decoding="async" data-slot="sponsor_main_1_img">
            </div>
            <div>
              <div class="sponsor-name" data-slot="sponsor_main_1_name">Gönner und Freunde des Sportclub Fulenbach</div>
              <div class="sponsor-role-tag">Offizieller Hauptsponsor (100er-Club) · c/o Schaad Treuhand AG · Dorfstrasse 10 · 4629 Fulenbach</div>
            </div>
          </div>

          <a href="http://www.lemp.ch" target="_blank" rel="noopener noreferrer" class="sponsor-card gold-card">
            <div class="sponsor-logo-wrap">
              <img src="images/sponsors/sponsor-1000839-lemp-haustechnik-ag.webp" alt="Lemp Haustechnik AG Murgenthal — Hauptsponsor SC Fulenbach" width="280" height="110" loading="lazy" decoding="async" data-slot="sponsor_main_2_img">
            </div>
            <div>
              <div class="sponsor-name" data-slot="sponsor_main_2_name">Lemp Haustechnik AG</div>
              <div class="sponsor-role-tag">Offizieller Hauptsponsor · Brückenstrasse 15 · 4853 Murgenthal · www.lemp.ch</div>
            </div>
          </a>

          <a href="http://www.raiffeisen.ch/aare-langete/de.html" target="_blank" rel="noopener noreferrer" class="sponsor-card gold-card">
            <div class="sponsor-logo-wrap">
              <img src="images/sponsors/sponsor-1000838-raiffeisenbank-aare-langete.webp" alt="Raiffeisenbank Aare-Langete — Co-Sponsor SC Fulenbach" width="280" height="110" loading="lazy" decoding="async" data-slot="sponsor_co_1_img">
            </div>
            <div>
              <div class="sponsor-name" data-slot="sponsor_co_1_name">Raiffeisenbank Aare-Langete</div>
              <div class="sponsor-role-tag">Offizieller Co-Sponsor · Breitenstrasse 2 · 4629 Fulenbach · raiffeisen.ch/aare-langete</div>
            </div>
          </a>
        </div>
      </div>

      <!-- TIER 2: SILBERSPONSOREN (6) -->
      <div class="sponsor-tier-block">
        <div class="sponsor-tier-header">
          <span class="sponsor-tier-badge tier-silver">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>
            <span>SILBERSPONSOREN (6 PARTNER)</span>
          </span>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Offizielle Silbersponsoren des SC Fulenbach</span>
        </div>

        <div class="sponsors-silver-grid">
{SILVER_CARDS_HTML}
        </div>
      </div>

      <!-- TIER 3: MANNSCHAFTSSPONSOREN 1. MANNSCHAFT (3) -->
      <div class="sponsor-tier-block">
        <div class="sponsor-tier-header">
          <span class="sponsor-tier-badge tier-green">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span>MANNSCHAFTSSPONSOREN 1. MANNSCHAFT (2. LIGA REGIONAL)</span>
          </span>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Offizielle Partner unseres Fanionteams</span>
        </div>

        <div class="sponsors-silver-grid">
          <a href="http://www.ehrenbolger-suter.ch" target="_blank" rel="noopener noreferrer" class="sponsor-card">
            <div class="sponsor-logo-wrap">
              <img src="images/sponsors/sponsor-1004354-ehrenbolger-suter-ag.webp" alt="Ehrenbolger und Suter AG — Mannschaftssponsor 1. Mannschaft" width="240" height="96" loading="lazy" decoding="async">
            </div>
            <div>
              <div class="sponsor-name">Ehrenbolger &amp; Suter AG</div>
              <div class="sponsor-role-tag">Mannschaftssponsor 1. Mannschaft · ehrenbolger-suter.ch</div>
            </div>
          </a>

          <a href="http://www.roth-dach.ch" target="_blank" rel="noopener noreferrer" class="sponsor-card">
            <div class="sponsor-logo-wrap">
              <img src="images/sponsors/sponsor-1004347-roth-dach-gmbh.webp" alt="Roth Dach GmbH — Mannschaftssponsor 1. Mannschaft" width="240" height="96" loading="lazy" decoding="async">
            </div>
            <div>
              <div class="sponsor-name">Roth Dach GmbH</div>
              <div class="sponsor-role-tag">Mannschaftssponsor 1. Mannschaft · roth-dach.ch</div>
            </div>
          </a>

          <a href="http://www.fischerschreinerei.ch" target="_blank" rel="noopener noreferrer" class="sponsor-card">
            <div class="sponsor-logo-wrap">
              <img src="images/sponsors/sponsor-1000961-fischer-schreinerei-gmbh.webp" alt="Fischer Schreinerei GmbH — Mannschaftssponsor 1. Mannschaft" width="240" height="96" loading="lazy" decoding="async">
            </div>
            <div>
              <div class="sponsor-name">Fischer Schreinerei GmbH</div>
              <div class="sponsor-role-tag">Mannschaftssponsor 1. Mannschaft · fischerschreinerei.ch</div>
            </div>
          </a>
        </div>
      </div>

      <!-- TIER 4: ALLE 79 BANDENSPONSOREN & VEREINSSPONSOREN -->
      <div class="sponsor-tier-block">
        <div class="sponsor-tier-header">
          <span class="sponsor-tier-badge tier-silver">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
            <span>BANDENSPONSOREN &amp; SPONSOREN ({BANDEN_COUNT} PARTNER)</span>
          </span>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Kompletter Original-Bestand von scfulenbach.ch</span>
        </div>

        <div class="sponsors-banden-grid">
{BANDEN_CARDS_HTML}
        </div>
      </div>

      <!-- SPONSORING- & GÖNNER-PLATTFORMEN -->
      <div class="grid-3" style="margin-top:36px;">
        <div class="card" style="padding:24px;background-color:var(--scf-navy-deep);color:#FFFFFF;border-color:var(--scf-navy-deep);">
          <div>
            <span class="wp-arch-badge" style="margin-bottom:14px;">100ER-CLUB · GÖNNER &amp; FREUNDE</span>
            <h3 style="color:#FFFFFF;font-size:1.18rem;font-weight:800;margin-bottom:8px;">Gönner und Freunde des SC Fulenbach</h3>
            <p style="font-size:0.88rem;color:#E2E8F0;margin-bottom:14px;">
              Der 100er-Club unterstützt gezielt die Juniorenabteilung und den Gesamtverein des SC Fulenbach und pflegt das gesellschaftliche Netzwerk rund um den Sportplatz Bad (c/o Schaad Treuhand AG, Dorfstrasse 10, 4629 Fulenbach).
            </p>
          </div>
          <a href="kontakt.html?thema=sponsoring" class="btn-cta btn-cta-gold btn-sm" style="width:100%;">Mitglied im 100er-Club werden</a>
        </div>

        <div class="card" style="padding:24px;background-color:var(--scf-navy-deep);color:#FFFFFF;border-color:var(--scf-navy-deep);">
          <div>
            <span class="wp-arch-badge" style="margin-bottom:14px;">SPORTPLATZ BAD · SICHTBARKEIT IM GÄU</span>
            <h3 style="color:#FFFFFF;font-size:1.18rem;font-weight:800;margin-bottom:8px;">Banden-, Dress- &amp; Matchball-Sponsoring</h3>
            <p style="font-size:0.88rem;color:#E2E8F0;margin-bottom:14px;">
              Präsentiere dein Unternehmen auf dem Sportplatz Bad bei den Spielen der 2. Liga regional, den Juniorenturnieren und Traditions-Events wie dem Badfest. Kontakt: <strong>Andreas Guldimann</strong> (079 413 76 51).
            </p>
          </div>
          <a href="kontakt.html?thema=sponsoring" class="btn-cta btn-cta-primary btn-sm" style="width:100%;">Sponsoring &amp; Bande anfragen</a>
        </div>

        <div class="card" style="padding:24px;background-color:var(--scf-green-soft);border-color:#6EE7B7;">
          <div>
            <span class="pillar-count" style="margin-bottom:14px;">CLUBHAUS BAD · 100 PLÄTZE</span>
            <h3 style="font-size:1.18rem;font-weight:800;margin-bottom:8px;">Clubhaus für deinen Anlass mieten</h3>
            <p style="font-size:0.88rem;color:var(--text-body);margin-bottom:14px;">
              Unser Clubhaus an der Ewigkeitstrasse 5 bietet Platz für bis zu 100 Personen. Ideal für Geburtstage, Firmenessen und Vereinsanlässe. Zuständig: <strong>René Hofstetter</strong> (Tel. 079 302 62 47).
            </p>
          </div>
          <a href="kontakt.html?thema=clubhaus" class="btn-cta btn-cta-navy btn-sm" style="width:100%;">Clubhaus-Termin anfragen</a>
        </div>
      </div>
    </div>
  </section>
"""

HERREN_1_CSS = """
    .architect-banner {
      background: linear-gradient(135deg, #0B1528 0%, #0F2942 100%);
      color: #FFFFFF;
      border-bottom: 3px solid var(--scf-gold);
      padding: 32px 0;
    }
    .architect-box {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      flex-wrap: wrap;
    }

    .team-hero-card {
      background-color: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-md);
      overflow: hidden;
      margin-bottom: 36px;
    }
    .team-hero-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
    }
    .team-photo-stage {
      position: relative;
      background-color: var(--scf-navy-deep);
      min-height: 360px;
    }
    .team-photo-stage img {
      width: 100%;
      height: 100%;
      max-height: 460px;
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
      gap: 12px;
      padding: 12px 14px;
      background-color: var(--bg-muted);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-sm);
      flex-wrap: wrap;
    }
    .team-sponsor-strip img {
      width: 86px;
      height: 42px;
      object-fit: contain;
      background-color: #FFFFFF;
      padding: 4px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-light);
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
      height: 92px;
      border-radius: var(--radius-sm);
      object-fit: cover;
      background-color: var(--scf-navy);
      flex-shrink: 0;
      border: 2px solid var(--scf-green);
    }
    .staff-avatar-placeholder {
      width: 74px;
      height: 92px;
      border-radius: var(--radius-sm);
      background: linear-gradient(135deg, var(--scf-navy-deep) 0%, var(--scf-green) 100%);
      color: var(--scf-gold-bright);
      font-family: 'Montserrat', sans-serif;
      font-weight: 800;
      font-size: 1.2rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    /* Roster Box */
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
      border-bottom: 2px solid var(--scf-green-soft);
    }
    .roster-pos-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 1rem;
      font-weight: 800;
      color: var(--scf-navy);
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
      background-color: var(--scf-navy-deep);
      color: var(--scf-gold-bright);
      font-family: 'Montserrat', sans-serif;
      font-size: 0.76rem;
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
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
    }
    .matrix-team-btn {
      background-color: #F8FAFC;
      border: 2px dashed #94A3B8;
      border-radius: var(--radius-md);
      padding: 16px;
      text-align: left;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 8px;
      transition: all 0.2s ease;
      font-family: inherit;
      min-height: 92px;
    }
    .matrix-team-btn:hover {
      border-color: var(--scf-gold);
      background-color: #FEF3C7;
      transform: translateY(-2px);
    }
    .matrix-team-btn.live-built {
      border: 2px solid var(--scf-green);
      background-color: var(--scf-green-soft);
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
      font-size: 0.94rem;
      font-weight: 800;
      color: var(--scf-navy);
    }
    .matrix-status-pill {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.66rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      white-space: nowrap;
    }
    .pill-live {
      background-color: var(--scf-green);
      color: #FFFFFF;
    }
    .pill-blueprint {
      background-color: #FEF3C7;
      color: #92400E;
      border: 1px solid #F59E0B;
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
  <!-- KOPFBEREICH-BANNER: 1 VON 14 TEAMS (7 %) ALS MUSTER-VORLAGE -->
  <section class="architect-banner" data-section="vorschau-hinweis">
    <div class="container">
      <div class="architect-box">
        <div style="max-width:780px;">
          <div class="section-kicker kicker-light" style="margin-bottom:6px;" data-slot="arch_kicker">MANNSCHAFTS-ÜBERSICHT: 1 BEISPIEL-TEAM AUSGEARBEITET — 13 WEITERE TEAMS VORBEREITET</div>
          <h1 style="color:#FFFFFF;font-size:clamp(1.45rem,2.5vw,2.05rem);font-weight:800;margin-bottom:8px;" data-slot="arch_title">
            Beispiel-Team: 1. Mannschaft (2. Liga regional) — Vorlage für alle 14 Teams
          </h1>
          <p style="font-size:0.9rem;color:#E2E8F0;line-height:1.58;" data-slot="arch_desc">
            Der SC Fulenbach stellt insgesamt <strong>14 Mannschaften</strong> (3 Aktiv-/Senioren-Teams, 5 Teams der Juniorengruppierung rot/blau und 6 Nachwuchs-Teams D bis G). In diesem Prototyp ist die <strong>1. Mannschaft (1/14 = 7 %)</strong> komplett mit Original-Mannschaftsfoto, Trainer- &amp; Betreuerstab, allen 20 Kaderspielern und den 3 Mannschaftssponsoren ausgebaut. Unten in der <strong>14-Teams-Übersicht</strong> sind alle 13 weiteren Teams als Platzhalter vorbereitet.
          </p>
        </div>
        <div style="display:flex;flex-direction:column;gap:8px;max-width:100%;">
          <a href="team-update.html?team=1-mannschaft" class="btn-cta btn-cta-gold btn-sm" style="white-space:normal;text-align:center;">Mannschafts-Daten &amp; Kader einreichen (Trainer-Formular)</a>
          <a href="#alle-teams-matrix" class="btn-cta btn-cta-ghost-light btn-sm">Zur 14-Teams-Übersicht</a>
          <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-ghost-light btn-sm">Probetraining anmelden</a>
        </div>
      </div>
    </div>
  </section>

  <!-- BEISPIEL-TEAM SEKTION: 1. MANNSCHAFT (2. LIGA REGIONAL) -->
  <section id="beispiel-team-detail" data-section="beispiel-team-detail">
    <div class="container">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;margin-bottom:18px;">
        <div style="display:inline-flex;align-items:center;gap:10px;background-color:var(--scf-green-soft);border:1px solid #6EE7B7;padding:8px 14px;border-radius:var(--radius-sm);">
          <span class="wp-status-dot wp-dot-green"></span>
          <span style="font-family:'Montserrat',sans-serif;font-size:0.82rem;font-weight:800;color:#065F46;">BEISPIEL-TEAM (1 VON 14 AUSGEARBEITET) · 1. MANNSCHAFT (2. LIGA REGIONAL SOFV)</span>
        </div>

        <div style="font-size:0.84rem;color:var(--text-muted);font-weight:600;">
          Sportchef SC Fulenbach: <strong>Mirko Ferrari</strong> (mirko.ferrari@scfulenbach.ch · Tel. 079 397 87 73)
        </div>
      </div>

      <div class="team-hero-card">
        <div class="team-hero-grid">
          <div class="team-photo-stage">
            <img src="images/team-herren-1.webp" alt="SC Fulenbach 1. Mannschaft 2. Liga regional Mannschaftsfoto" width="760" height="440" data-slot="h1_team_photo">
            <span class="card-badge">1. Mannschaft · 2. Liga regional · Sportplatz Bad</span>
          </div>
          <div class="team-info-stage">
            <div>
              <div class="section-kicker" style="margin-bottom:8px;">FANIONTEAM SC FULENBACH · AUFSTEIGER 2. LIGA REGIONAL</div>
              <h2 style="font-size:1.75rem;font-weight:800;margin-bottom:10px;" data-slot="h1_title">SC Fulenbach — 1. Mannschaft</h2>
              <p style="font-size:0.92rem;color:var(--text-body);margin-bottom:16px;" data-slot="h1_desc">
                Als gefeierter 3.-Liga-Meister (5:2-Heimsieg im Entscheidungsspiel gegen den Türkischen FC Solothurn) spielt unser Fanionteam in der <strong>2. Liga regional</strong> des Solothurner Fussballverbands (SOFV). Trainiert wird die Mannschaft von Cheftrainer <strong>Kay Ackermann</strong> und Co-Trainer <strong>Roland Wiss</strong>.
              </p>

              <div class="card-meta-list" style="margin-bottom:16px;">
                <div class="card-meta-item">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                  <span><strong>Trainingszeiten:</strong> Dienstag &amp; Donnerstag, 19:30 – 21:00 Uhr</span>
                </div>
                <div class="card-meta-item">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                  <span><strong>Heimstätte:</strong> Sportplatz Bad, Ewigkeitstrasse 5, 4629 Fulenbach</span>
                </div>
                <div class="card-meta-item">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
                  <span><strong>Staff:</strong> Kay Ackermann (Trainer) · Roland Wiss (Co-Trainer) · Roland Mäder (Betreuer/Masseur) · Marcel Künzli (Torwarttrainer)</span>
                </div>
              </div>

              <!-- Team Sponsors 1. Mannschaft -->
              <div class="team-sponsor-strip">
                <img src="images/sponsors/sponsor-1004354-ehrenbolger-suter-ag.webp" alt="Ehrenbolger und Suter AG" width="86" height="42" loading="lazy" decoding="async">
                <img src="images/sponsors/sponsor-1004347-roth-dach-gmbh.webp" alt="Roth Dach GmbH" width="86" height="42" loading="lazy" decoding="async">
                <img src="images/sponsors/sponsor-1000961-fischer-schreinerei-gmbh.webp" alt="Fischer Schreinerei GmbH" width="86" height="42" loading="lazy" decoding="async">
                <div style="font-size:0.78rem;width:100%;">
                  <strong style="color:var(--scf-navy);">Mannschaftssponsoren 1. Mannschaft:</strong> Ehrenbolger &amp; Suter AG · Roth Dach GmbH · Fischer Schreinerei GmbH
                </div>
              </div>
            </div>

            <div style="display:flex;flex-wrap:wrap;gap:10px;">
              <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-primary btn-sm" style="flex:1;">
                <span>Probetraining / Kontakt 1. Mannschaft</span>
              </a>
              <a href="https://www.sofv.ch/de/verein.aspx?v=1826&amp;a=trr" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta-outline btn-sm" style="flex:1;">
                <span>SOFV Spielplan &amp; Tabelle</span>
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- Trainer & Staff 1. Mannschaft -->
      <h3 style="font-size:1.3rem;font-weight:800;margin-bottom:16px;">Trainer- &amp; Betreuerstab — 1. Mannschaft (2. Liga regional)</h3>
      <div class="staff-grid">
        <div class="staff-card">
          <img src="images/staff-kay-ackermann.webp" alt="Kay Ackermann Trainer 1. Mannschaft SC Fulenbach" class="staff-avatar" width="74" height="92" loading="lazy" decoding="async">
          <div>
            <span class="board-role">Cheftrainer 1. Mannschaft</span>
            <div class="board-name">Kay Ackermann</div>
            <div style="font-size:0.82rem;color:var(--text-body);margin-top:4px;">
              2. Liga regional · Di &amp; Do 19:30–21:00 Uhr
            </div>
          </div>
        </div>

        <div class="staff-card">
          <img src="images/staff-roland-wiss.webp" alt="Roland Wiss Co-Trainer 1. Mannschaft SC Fulenbach" class="staff-avatar" width="74" height="92" loading="lazy" decoding="async">
          <div>
            <span class="board-role">Co-Trainer &amp; Finanzen a.i.</span>
            <div class="board-name">Roland Wiss</div>
            <div style="font-size:0.82rem;color:var(--text-body);margin-top:4px;">
              Assistenztrainer 1. Mannschaft &amp; Vorstand
            </div>
          </div>
        </div>

        <div class="staff-card">
          <div class="staff-avatar-placeholder">RM</div>
          <div>
            <span class="board-role">Betreuer &amp; Masseur</span>
            <div class="board-name">Roland Mäder</div>
            <div style="font-size:0.82rem;color:var(--text-body);margin-top:4px;">
              Medizinische Betreuung &amp; Team-Support
            </div>
          </div>
        </div>

        <div class="staff-card">
          <div class="staff-avatar-placeholder">MK</div>
          <div>
            <span class="board-role">Torwarttrainer</span>
            <div class="board-name">Marcel Künzli</div>
            <div style="font-size:0.82rem;color:var(--text-body);margin-top:4px;">
              Torhüter-Training Aktive SC Fulenbach
            </div>
          </div>
        </div>

        <div class="staff-card">
          <div class="staff-avatar-placeholder">MF</div>
          <div>
            <span class="board-role">Sportchef &amp; SR-Verantwortlicher</span>
            <div class="board-name">Mirko Ferrari</div>
            <div style="font-size:0.82rem;color:var(--text-body);margin-top:4px;">
              <a href="mailto:mirko.ferrari@scfulenbach.ch" style="color:var(--scf-green);font-weight:600;">mirko.ferrari@scfulenbach.ch</a> · 079 397 87 73
            </div>
          </div>
        </div>
      </div>

      <!-- Spielerkader 1. Mannschaft (Alle 20 Original-Spieler von scfulenbach.ch) -->
      <h3 style="font-size:1.3rem;font-weight:800;margin-bottom:16px;">Offizielles Spielerkader — 1. Mannschaft (20 Original-Kaderspieler)</h3>
      <div class="roster-pos-grid">
        <div class="roster-pos-box">
          <div class="roster-pos-head">
            <span class="roster-pos-title">Kaderspieler A – K</span>
            <span class="pillar-count">11 Spieler</span>
          </div>
          <div class="roster-player-list">
            <div class="player-pill"><span class="player-num">01</span><span class="player-name">Sandro Albuquerque Sampaio</span></div>
            <div class="player-pill"><span class="player-num">02</span><span class="player-name">Nik Berger</span></div>
            <div class="player-pill"><span class="player-num">03</span><span class="player-name">Yanick Boss</span></div>
            <div class="player-pill"><span class="player-num">04</span><span class="player-name">Nico Ferrari</span></div>
            <div class="player-pill"><span class="player-num">05</span><span class="player-name">Florian Fischer</span></div>
            <div class="player-pill"><span class="player-num">06</span><span class="player-name">André Grob</span></div>
            <div class="player-pill"><span class="player-num">07</span><span class="player-name">Minas Iakovidis</span></div>
            <div class="player-pill"><span class="player-num">08</span><span class="player-name">Glen Jäggi</span></div>
            <div class="player-pill"><span class="player-num">09</span><span class="player-name">Loris Jäggi</span></div>
            <div class="player-pill"><span class="player-num">10</span><span class="player-name">Ron Jäggi</span></div>
            <div class="player-pill"><span class="player-num">11</span><span class="player-name">Enrik Kqiraj</span></div>
          </div>
        </div>

        <div class="roster-pos-box">
          <div class="roster-pos-head">
            <span class="roster-pos-title">Kaderspieler K – W</span>
            <span class="pillar-count">9 Spieler</span>
          </div>
          <div class="roster-player-list">
            <div class="player-pill"><span class="player-num">12</span><span class="player-name">Fabian Kuster</span></div>
            <div class="player-pill"><span class="player-num">13</span><span class="player-name">Dzenis Poljak</span></div>
            <div class="player-pill"><span class="player-num">14</span><span class="player-name">Flavio Premori</span></div>
            <div class="player-pill"><span class="player-num">15</span><span class="player-name">Joel Roth</span></div>
            <div class="player-pill"><span class="player-num">16</span><span class="player-name">Jonas Ruf</span></div>
            <div class="player-pill"><span class="player-num">17</span><span class="player-name">Yves Rütimann</span></div>
            <div class="player-pill"><span class="player-num">18</span><span class="player-name">Levin Wiss</span></div>
            <div class="player-pill"><span class="player-num">19</span><span class="player-name">Daren Wyss</span></div>
            <div class="player-pill"><span class="player-num">20</span><span class="player-name">Jonas Wyss</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 14-MANNSCHAFTEN-ÜBERSICHT (1 BEISPIEL-TEAM, 13 VORBEREITET) -->
  <section id="alle-teams-matrix" data-section="alle-teams-matrix" style="background-color:#FFFFFF;border-top:1px solid var(--border-light);">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="matrix_kicker">MANNSCHAFTS-ÜBERSICHT · ALLE 14 MANNSCHAFTEN DES SC FULENBACH</div>
        <h2 class="section-title" data-slot="matrix_title">Alle 14 Mannschaften im Überblick (1 Beispiel-Team ausgearbeitet · 13 weitere vorbereitet).</h2>
        <p class="section-desc" data-slot="matrix_desc">
          Klicke auf eine der <strong>13 vorbereiteten Team-Kacheln</strong>, um die bereits hinterlegten Original-Trainer, Trainingszeiten und Kadergrössen von <strong>scfulenbach.ch</strong> zu prüfen. Bei Auftragserteilung erhält jedes Team seine voll ausgebaute Seite nach dem Vorbild der 1. Mannschaft.
        </p>
      </div>

      <!-- Gruppe 1: Aktive & Senioren (3 Teams) -->
      <div class="matrix-group-block">
        <div class="matrix-group-header">
          <h3 style="font-size:1.18rem;font-weight:800;">1. Aktive &amp; Senioren (3 Mannschaften — 1 Beispiel-Team ausgearbeitet, 2 vorbereitet)</h3>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Sportchef: Mirko Ferrari (mirko.ferrari@scfulenbach.ch · 079 397 87 73)</span>
        </div>
        <div class="matrix-grid">
          <a href="#beispiel-team-detail" class="matrix-team-btn live-built">
            <div class="matrix-team-top">
              <span class="matrix-team-name">1. Mannschaft (2. Liga reg.)</span>
              <span class="matrix-status-pill pill-live">1/14 · Ausgearbeitet</span>
            </div>
            <span style="font-size:0.78rem;color:#065F46;font-weight:600;">Trainer: Kay Ackermann &amp; Roland Wiss · Di/Do 19:30–21:00 Uhr · 20 Spieler</span>
          </a>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team (2/14 · vorbereitet): 2. Mannschaft («Zwöi» · 4. Liga SOFV)', 'Aktive Herren · 29 Kaderspieler · Training Di &amp; Do 19:30–21:00 Uhr auf dem Sportplatz Bad', 'Trainer: Marc Haldemann · Co-Trainer: Emanuel Wyss · Sportchef: Mirko Ferrari (079 397 87 73)', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">2. Mannschaft («Zwöi» · 4. Liga)</span>
              <span class="matrix-status-pill pill-blueprint">Noch nicht migriert</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Trainer: Marc Haldemann &amp; Emanuel Wyss · Di/Do 19:30 Uhr · 29 Spieler · Teil des Hauptauftrags</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team (3/14 · vorbereitet): Senioren 30+ (Meisterschaft &amp; Cup)', 'Senioren 30+ · 26 Kaderspieler · Training Mittwoch 19:30–21:00 Uhr, Spiele Freitagabend', 'Trainer: Walter Müller &amp; Christian Napoli · Sportplatz Bad Fulenbach', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Senioren 30+</span>
              <span class="matrix-status-pill pill-blueprint">Noch nicht migriert</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Trainer: Walter Müller &amp; Christian Napoli · Mi 19:30 Uhr · 26 Spieler · Teil des Hauptauftrags</span>
          </button>
        </div>
      </div>

      <!-- Gruppe 2: Juniorengruppierung rot/blau (5 Teams) -->
      <div class="matrix-group-block">
        <div class="matrix-group-header">
          <h3 style="font-size:1.18rem;font-weight:800;">2. Juniorengruppierung rot/blau — SC Fulenbach / FC Wolfwil / FC Kestenholz (5 Teams vorbereitet)</h3>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Juniorenobmann: Michael «Mike» Frieder (Tel. 079 647 13 33)</span>
        </div>
        <div class="matrix-grid">
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team (4/14 · vorbereitet): Junioren B rot/blau', 'Juniorengruppierung SC Fulenbach / FC Wolfwil / FC Kestenholz · 18 Kaderspieler', 'Trainer: Luca Albuquerque Sampaio (C-Diplom), Nico Leber &amp; Jagvir Singh Nagra', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Junioren B rot/blau</span>
              <span class="matrix-status-pill pill-blueprint">Noch nicht migriert</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Trainer: L. Albuquerque Sampaio, N. Leber &amp; J. Singh Nagra · 18 Spieler · Teil des Hauptauftrags</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team (5/14 · vorbereitet): Junioren Ca rot/blau', 'Juniorengruppierung SC Fulenbach / FC Wolfwil / FC Kestenholz · 19 Kaderspieler', 'Trainer: Marco Wagner &amp; Remo Wagner · Juniorenobmann: Mike Frieder (079 647 13 33)', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Junioren Ca rot/blau</span>
              <span class="matrix-status-pill pill-blueprint">Noch nicht migriert</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Trainer: Marco Wagner &amp; Remo Wagner · 19 Spieler · Teil des Hauptauftrags</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team (6/14 · vorbereitet): Junioren Cb rot/blau', 'Juniorengruppierung SC Fulenbach / FC Wolfwil / FC Kestenholz · 22 Kaderspieler', 'Trainer: Raphael Kronenberg &amp; Nivio Madeira · Juniorenobmann: Mike Frieder (079 647 13 33)', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Junioren Cb rot/blau</span>
              <span class="matrix-status-pill pill-blueprint">Noch nicht migriert</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Trainer: Raphael Kronenberg &amp; Nivio Madeira · 22 Spieler · Teil des Hauptauftrags</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team (7/14 · vorbereitet): Junioren D rot/blau (9er-Fussball)', 'Juniorengruppierung SC Fulenbach / FC Wolfwil / FC Kestenholz · 24 Kaderspieler', 'Trainer: Hanspeter Ehrenbolger, Fabian Wyss &amp; Roman Wyss', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Junioren D rot/blau (9er)</span>
              <span class="matrix-status-pill pill-blueprint">Noch nicht migriert</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Trainer: H. Ehrenbolger, F. Wyss &amp; R. Wyss · 9er-Fussball · Teil des Hauptauftrags</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team (8/14 · vorbereitet): Junioren D rot/blau (7er-Fussball)', 'Juniorengruppierung SC Fulenbach / FC Wolfwil / FC Kestenholz · D7er-Meisterschaft', 'Trainer: Hanspeter Ehrenbolger, Fabian Wyss &amp; Roman Wyss', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Junioren D rot/blau (7er)</span>
              <span class="matrix-status-pill pill-blueprint">Noch nicht migriert</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Trainer: H. Ehrenbolger, F. Wyss &amp; R. Wyss · 7er-Fussball · Teil des Hauptauftrags</span>
          </button>
        </div>
      </div>

      <!-- Gruppe 3: Junioren SC Fulenbach D bis G (6 Teams) -->
      <div class="matrix-group-block" style="margin-bottom:0;">
        <div class="matrix-group-header">
          <h3 style="font-size:1.18rem;font-weight:800;">3. Nachwuchs SC Fulenbach — Junioren D bis G (6 Teams vorbereitet)</h3>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Sportplatz Bad Fulenbach · Juniorenobmann: Michael «Mike» Frieder (079 647 13 33)</span>
        </div>
        <div class="matrix-grid">
          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team (9/14 · vorbereitet): Junioren D SC Fulenbach (9er-Fussball)', 'Junioren D SC Fulenbach · 21 Kaderspieler auf dem Sportplatz Bad', 'Trainer: Roger Baumgartner, Martin Nyfeler, Fabian Sager, Emanuel Wyss &amp; Andreas Guldimann', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Junioren D (9er)</span>
              <span class="matrix-status-pill pill-blueprint">Noch nicht migriert</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Trainer: R. Baumgartner, M. Nyfeler, F. Sager, E. Wyss &amp; A. Guldimann · Teil des Hauptauftrags</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team (10/14 · vorbereitet): Junioren D SC Fulenbach (7er-Fussball)', 'Junioren D SC Fulenbach · 7er-Meisterschaft SOFV', 'Trainer: Roger Baumgartner, Martin Nyfeler, Fabian Sager, Emanuel Wyss &amp; Andreas Guldimann', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Junioren D (7er)</span>
              <span class="matrix-status-pill pill-blueprint">Noch nicht migriert</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Trainer: R. Baumgartner, M. Nyfeler, F. Sager, E. Wyss &amp; A. Guldimann · Teil des Hauptauftrags</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team (11/14 · vorbereitet): Junioren Ea SC Fulenbach', 'Junioren E SC Fulenbach · 26 Kinder auf dem Sportplatz Bad', 'Trainer: Stephan Bitterli, Christian Napoli, Michel Allemann &amp; Roland Marti', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Junioren Ea</span>
              <span class="matrix-status-pill pill-blueprint">Noch nicht migriert</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Trainer: S. Bitterli, C. Napoli, M. Allemann &amp; R. Marti · 26 Kinder · Teil des Hauptauftrags</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team (12/14 · vorbereitet): Junioren Eb SC Fulenbach', 'Junioren E SC Fulenbach · Play More Football SOFV', 'Trainer: Stephan Bitterli, Christian Napoli, Michel Allemann &amp; Roland Marti', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Junioren Eb</span>
              <span class="matrix-status-pill pill-blueprint">Noch nicht migriert</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Trainer: S. Bitterli, C. Napoli, M. Allemann &amp; R. Marti · Teil des Hauptauftrags</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team (13/14 · vorbereitet): Junioren F SC Fulenbach', 'Junioren F SC Fulenbach · 17 Kinder auf dem Sportplatz Bad', 'Trainer: David Ackermann, Fabrice Indermühle &amp; Beat Wiesmann', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Junioren F</span>
              <span class="matrix-status-pill pill-blueprint">Noch nicht migriert</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Trainer: D. Ackermann, F. Indermühle &amp; B. Wiesmann · 17 Kinder · Teil des Hauptauftrags</span>
          </button>

          <button type="button" class="matrix-team-btn" onclick="wpOpenBlueprintModal('Team (14/14 · vorbereitet): Junioren G (Bambini) SC Fulenbach', 'Junioren G SC Fulenbach · 11 Kinder · Spielerischer Einstieg auf dem Sportplatz Bad', 'Trainer: Giory Bortoluzzi &amp; Markus Wyss · Juniorenobmann: Mike Frieder (079 647 13 33)', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Junioren G (Bambini)</span>
              <span class="matrix-status-pill pill-blueprint">Noch nicht migriert</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-muted);">Trainer: Giory Bortoluzzi &amp; Markus Wyss · 11 Kinder · Teil des Hauptauftrags</span>
          </button>
        </div>
      </div>
    </div>
  </section>
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
      border-left: 3px solid var(--scf-green);
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
    }
    .contact-direct-role {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--scf-green);
      letter-spacing: 0.04em;
    }
    .contact-direct-person {
      font-weight: 700;
      color: var(--scf-navy);
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
      border: 2px solid var(--scf-green);
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
      background-color: var(--scf-green);
      color: #FFFFFF;
    }
    .wp-step-pill.done {
      background-color: var(--scf-green-soft);
      color: #065F46;
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
      gap: 6px;
      transition: all 0.2s ease;
      font-family: inherit;
    }
    .wp-role-tile:hover {
      border-color: var(--scf-green);
      background-color: #FFFFFF;
    }
    .wp-role-tile.selected {
      border: 2px solid var(--scf-green);
      background-color: var(--scf-green-soft);
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
      background-color: var(--scf-navy-deep);
      color: var(--scf-gold-bright);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .wp-role-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.88rem;
      font-weight: 800;
      color: var(--scf-navy);
    }
    .wp-role-desc {
      font-size: 0.76rem;
      color: var(--text-body);
      line-height: 1.4;
    }

    .form-grid-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
    }
    .form-field {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .form-label {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--scf-navy);
    }
    .form-input, .form-textarea {
      width: 100%;
      padding: 11px 14px;
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-sm);
      font-family: 'Inter', sans-serif;
      font-size: 0.9rem;
      color: var(--text-main);
      background-color: #FFFFFF;
    }
    .form-input:focus, .form-textarea:focus {
      outline: none;
      border-color: var(--scf-green);
      box-shadow: 0 0 0 3px rgba(15, 138, 75, 0.15);
    }
    .form-textarea {
      min-height: 96px;
      resize: vertical;
    }

    .wp-upload-zone {
      border: 2px dashed var(--border-strong);
      border-radius: var(--radius-md);
      padding: 16px;
      text-align: center;
      background-color: var(--bg-page);
    }
    .wp-upload-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 14px;
      min-height: 38px;
      background-color: #FFFFFF;
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-sm);
      font-family: 'Montserrat', sans-serif;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--scf-navy);
      cursor: pointer;
    }
    .wp-photo-thumbs {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      justify-content: center;
      margin-top: 10px;
    }
    .wp-thumb-item {
      position: relative;
      width: 68px;
      height: 68px;
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
      background-color: rgba(15, 23, 42, 0.85);
      color: #FFFFFF;
      border: none;
      border-radius: var(--radius-sm);
      font-size: 0.7rem;
      cursor: pointer;
    }

    .wp-selftest-banner {
      background-color: var(--scf-gold-soft);
      border: 1px solid #F59E0B;
      color: #92400E;
      padding: 12px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      margin-bottom: 16px;
      line-height: 1.5;
    }
    .wp-plz-badge {
      display: none;
      align-items: center;
      gap: 8px;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
      font-weight: 700;
    }
    .wp-plz-badge.in-area {
      display: inline-flex;
      background-color: var(--scf-green-soft);
      color: #065F46;
      border: 1px solid #6EE7B7;
    }

    .wp-success-box {
      display: none;
      flex-direction: column;
      gap: 16px;
      background-color: var(--bg-page);
      border: 2px solid var(--scf-green);
      border-radius: var(--radius-md);
      padding: 22px;
    }
    .wp-success-box.visible {
      display: flex;
    }
    .wp-wa-preview {
      background-color: #0B1528;
      color: #E2E8F0;
      padding: 14px;
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
      white-space: pre-wrap;
      line-height: 1.5;
      border-left: 3px solid var(--scf-green-bright);
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
        <!-- LEFT COLUMN: VEREINS-ANLAUFSTELLEN SC FULENBACH -->
        <div class="contact-info-panel">
          <div class="section-kicker" data-slot="contact_kicker">SMART-ANFRAGE-ZENTRALE · SC FULENBACH</div>
          <h1 style="font-size:clamp(1.65rem,2.6vw,2.2rem);font-weight:800;margin-bottom:12px;" data-slot="contact_title">
            Alle Vereinsanliegen, Probetrainings &amp; Clubhaus-Reservationen an einem Ort.
          </h1>
          <p style="font-size:0.93rem;color:var(--text-body);margin-bottom:18px;" data-slot="contact_lead">
            Ob Schnuppertraining bei den Junioren,Sponsoring-Anfrage, Mitgliedschaft im 100er-Club, Reservation unseres Clubhauses (100 Plätze) oder Fanartikel-Bestellung: Unser 3-Schritte-Assistent erstellt sofort ein übersichtliches <strong>1-Seiten-PDF-Vereinsdossier</strong> für das zuständige Vorstandsressort.
          </p>

          <div class="contact-direct-list">
            <div class="contact-direct-item">
              <div class="contact-direct-role">Präsidium &amp; Vereinsführung</div>
              <div class="contact-direct-person">Willi von Arx (Präsident) &amp; Elias Sidler (Vize-Präsident / Anlässe)</div>
              <div class="contact-direct-links">vorstand@scfulenbach.ch · Sportplatz Bad, Ewigkeitstrasse 5, 4629 Fulenbach</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Sportliche Leitung &amp; Schiedsrichterwesen</div>
              <div class="contact-direct-person">Mirko Ferrari (Sportchef &amp; SR-Verantwortlicher)</div>
              <div class="contact-direct-links">mirko.ferrari@scfulenbach.ch · Tel. 079 397 87 73</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Juniorenabteilung &amp; Gruppierung rot/blau</div>
              <div class="contact-direct-person">Michael «Mike» Frieder (Juniorenobmann)</div>
              <div class="contact-direct-links">Tel. 079 647 13 33 · Junioren B bis G &amp; Juniorenlager</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Sponsoring, Bandenwerbung &amp; Marketing</div>
              <div class="contact-direct-person">Andreas Guldimann (Sponsoring / Marketing)</div>
              <div class="contact-direct-links">andreas.guldimann@scfulenbach.ch · Tel. 079 413 76 51</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Clubhaus-Vermietung (100 Plätze) &amp; Infrastruktur</div>
              <div class="contact-direct-person">René Hofstetter (Vermietung) &amp; Alfred Ammann (Infrastruktur)</div>
              <div class="contact-direct-links">Tel. 079 302 62 47 · Ewigkeitstrasse 5, 4629 Fulenbach</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Gönner &amp; Freunde (100er-Club)</div>
              <div class="contact-direct-person">Gönner und Freunde des Sportclub Fulenbach</div>
              <div class="contact-direct-links">c/o Schaad Treuhand AG · Dorfstrasse 10 · 4629 Fulenbach</div>
            </div>

            <div class="contact-direct-item">
              <div class="contact-direct-role">Medien, Web, Finanzen &amp; Aktuariat</div>
              <div class="contact-direct-person">David Ackermann (Medien/Support) · Roland Wiss (Finanzen a.i.) · Rahel Napoli (Aktuarin)</div>
              <div class="contact-direct-links">david.ackermann@scfulenbach.ch · Robin Müller (Social Media)</div>
            </div>
          </div>
        </div>

        <!-- RIGHT COLUMN: 3-STEP SMART WIZARD -->
        <div class="wizard-card">
          <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:14px;">
            <div>
              <div class="section-kicker" style="margin-bottom:4px;">DIGITALE VEREINS-ZENTRALE · SC FULENBACH</div>
              <h2 style="font-size:1.35rem;font-weight:800;" id="wpWizardTitle">1. Wähle dein Anliegen</h2>
            </div>
            <span class="pillar-count" id="wpActiveAssigneeBadge">Ressort: Sportchef &amp; Juniorenobmann</span>
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
              <span>Kontakt &amp; PDF-Dossier</span>
            </div>
          </div>

          <form id="scfContactForm" onsubmit="return wpSubmitScfLead(event)" novalidate>
            <!-- Honeypot -->
            <div style="display:none;" aria-hidden="true">
              <label for="wpHoneypot">Website URL</label>
              <input type="text" id="wpHoneypot" name="website_url" tabindex="-1" autocomplete="off">
            </div>

            <!-- STEP 1: TOPIC SELECTION (6 TILES) -->
            <div class="wp-step-pane active" id="wpStep1">
              <div class="wp-role-grid" id="wpTopicGrid">
                <button type="button" class="wp-role-tile selected" data-topic="Probetraining / Neumitglied" onclick="wpSelectScfTopic('Probetraining / Neumitglied')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_1">Probetraining / Neumitglied</span>
                  </div>
                  <span class="wp-role-desc">Schnuppertraining für Junioren G bis B (rot/blau), 1./2. Mannschaft oder Senioren 30+</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Sponsoring / Gönner 100er-Club" onclick="wpSelectScfTopic('Sponsoring / Gönner 100er-Club')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_2">Sponsoring / 100er-Club</span>
                  </div>
                  <span class="wp-role-desc">Hauptsponsor, Silbersponsor, Bandenwerbung Sportplatz Bad oder Gönner &amp; Freunde</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Clubhaus mieten (100 Plätze)" onclick="wpSelectScfTopic('Clubhaus mieten (100 Plätze)')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_3">Clubhaus Bad mieten</span>
                  </div>
                  <span class="wp-role-desc">Reservationsanfrage für das SCF-Clubhaus (bis 100 Plätze, René Hofstetter)</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Spielbetrieb / Schiedsrichter / Turniere" onclick="wpSelectScfTopic('Spielbetrieb / Schiedsrichter / Turniere')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_4">Spielbetrieb &amp; Schiedsrichter</span>
                  </div>
                  <span class="wp-role-desc">Spielverschiebung, Schiedsrichter werden (CHF 500/Jahr), Dorfturnier oder KUBB-Turnier</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Fanshop / Sponsorenlauf / Juniorenlager" onclick="wpSelectScfTopic('Fanshop / Sponsorenlauf / Juniorenlager')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M20.38 3.46L16 2a4 4 0 0 1-8 0L3.62 3.46a2 2 0 0 0-1.34 2.23l.58 3.47a1 1 0 0 0 .99.84H6v10c0 1.1.9 2 2 2h8a2 2 0 0 0 2-2V10h2.15a1 1 0 0 0 .99-.84l.58-3.47a2 2 0 0 0-1.34-2.23z"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_5">Fanshop &amp; Juniorenlager</span>
                  </div>
                  <span class="wp-role-desc">SCF-Cap (CHF 25.–), SCF-Wimpel (CHF 15.–), Juniorenlager-Woche &amp; Sponsorenlauf</span>
                </button>

                <button type="button" class="wp-role-tile" data-topic="Mitgliedschaft / Mutation / Allgemein" onclick="wpSelectScfTopic('Mitgliedschaft / Mutation / Allgemein')">
                  <div class="wp-role-head">
                    <span class="wp-role-icon">
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
                    </span>
                    <span class="wp-role-title" data-slot="topic_opt_6">Mitgliedschaft &amp; Vorstand</span>
                  </div>
                  <span class="wp-role-desc">Adressänderung, Mitgliederbeitrag, Anmeldung Vereinsanlass oder allgemeine Frage</span>
                </button>
              </div>

              <button type="button" class="btn-cta btn-cta-primary" style="width:100%;" onclick="wpNextStep(2)">
                <span>Weiter zu Schritt 2: Details &amp; Beilagen</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 18 15 12 9 6"/></svg>
              </button>
            </div>

            <!-- STEP 2: DYNAMIC DETAILS & PHOTO UPLOAD -->
            <div class="wp-step-pane" id="wpStep2">
              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="wpDetail1" class="form-label" id="wpDetail1Label">Name &amp; Jahrgang Spieler/in</label>
                  <input type="text" id="wpDetail1" class="form-input" placeholder="z. B. Levin Muster · Jahrgang 2014">
                </div>
                <div class="form-field">
                  <label for="wpDetail2" class="form-label" id="wpDetail2Label">Gewünschte Mannschaft / Erfahrung</label>
                  <input type="text" id="wpDetail2" class="form-input" placeholder="z. B. Junioren D / 1. Mannschaft / Bambini">
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label class="form-label">Zeitrahmen / Dringlichkeit</label>
                <div class="wp-role-grid" id="wpUrgencyGrid" style="margin-bottom:0;">
                  <button type="button" class="wp-role-tile selected" data-urg="Planbar / Laufende Saison" onclick="wpSelectScfUrgency('Planbar / Laufende Saison')">
                    <span class="wp-role-title">Planbar / Laufende Saison</span>
                    <span class="wp-role-desc">Reguläre Bearbeitung durch das Ressort</span>
                  </button>
                  <button type="button" class="wp-role-tile" data-urg="Dringend (Spielbetrieb / Termin)" onclick="wpSelectScfUrgency('Dringend (Spielbetrieb / Termin)')">
                    <span class="wp-role-title">Dringend (Spielbetrieb / Termin)</span>
                    <span class="wp-role-desc">Kurzfristige Rückmeldung erwünscht</span>
                  </button>
                </div>
              </div>

              <div class="form-field" style="margin-bottom:14px;">
                <label for="contactMessage" class="form-label" data-slot="lbl_message">Nachricht / Zusatzangaben ans Ressort *</label>
                <textarea id="contactMessage" name="message" class="form-textarea" placeholder="Beschreibe kurz dein Anliegen (z. B. Wunschdatum für Probetraining oder Clubhaus-Miete, Sponsoring-Paket oder Fanartikel)..." required></textarea>
              </div>

              <div class="form-field" style="margin-bottom:18px;">
                <label class="form-label">Fotos, Sponsoren-Logo oder Dokument beifügen (optional, max. 3 Bilder)</label>
                <div class="wp-upload-zone">
                  <input type="file" id="wpPhotoInput" accept="image/*" multiple style="display:none;" onchange="wpHandlePhotoFiles(this.files)">
                  <button type="button" class="wp-upload-btn" onclick="wpTriggerPhotoUpload()">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
                    <span>Bild / Beilage auswählen (z. B. Firmenlogo, Ausweis, Skizze)</span>
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
                <strong>Vorschau- &amp; Selbst-Test-Modus aktiv:</strong> Du kannst dieses Formular jetzt live testen. Das System generiert sofort ein echtes <strong>1-Seiten-PDF-Vereinsdossier</strong> mit SC-Fulenbach-Wappen zum Herunterladen, ohne den Vorstand mit Test-Mails zu belasten.
              </div>

              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactName" class="form-label" data-slot="lbl_name">Vor- und Nachname (oder Eltern) *</label>
                  <input type="text" id="contactName" name="name" class="form-input" placeholder="z. B. Lukas Muster" required>
                </div>
                <div class="form-field">
                  <label for="contactCompany" class="form-label">Team / Firma / Verein (optional)</label>
                  <input type="text" id="contactCompany" name="company" class="form-input" placeholder="z. B. Junioren Ea / Muster AG Fulenbach">
                </div>
              </div>

              <div class="form-grid-2" style="margin-bottom:14px;">
                <div class="form-field">
                  <label for="contactLoc" class="form-label">PLZ &amp; Wohnort *</label>
                  <input type="text" id="contactLoc" name="plz" class="form-input" placeholder="z. B. 4629 Fulenbach" oninput="wpCheckScfPlz(this.value)" required>
                </div>
                <div class="form-field">
                  <label for="contactStreet" class="form-label">Strasse &amp; Nr. (optional)</label>
                  <input type="text" id="contactStreet" name="street" class="form-input" placeholder="z. B. Ewigkeitstrasse 5">
                </div>
              </div>

              <div class="wp-plz-badge" id="wpPlzBadge" style="margin-bottom:14px;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
                <span id="wpPlzBadgeText">PLZ 4629: Direktes Einzugsgebiet Fulenbach, Gäu &amp; Untergäu</span>
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
                <span style="width:36px;height:36px;border-radius:4px;background-color:var(--scf-green);color:#FFFFFF;display:inline-flex;align-items:center;justify-content:center;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><polyline points="20 6 9 17 4 12"/></svg>
                </span>
                <div>
                  <div style="font-family:'Montserrat',sans-serif;font-weight:800;font-size:1.05rem;color:var(--scf-navy);">Vereins-Anfrage &amp; 1-Seiten-PDF-Dossier erstellt</div>
                  <div style="font-size:0.78rem;color:var(--text-muted);" id="wpResChannels">1-Seiten-PDF-Dossier bereit zum Download</div>
                </div>
              </div>
              <span class="wp-arch-badge" style="background-color:var(--scf-navy-deep);color:var(--scf-gold-bright);" id="wpResRef">#SCF-2026</span>
            </div>

            <div class="form-grid-2" style="background-color:#FFFFFF;padding:12px 14px;border-radius:4px;border:1px solid var(--border-light);font-size:0.84rem;">
              <div>
                <div style="color:var(--text-muted);font-size:0.75rem;">Zuständiges Ressort im SC Fulenbach:</div>
                <strong style="color:var(--scf-navy);" id="wpResAssigned">Sportliche Leitung &amp; Vorstand</strong>
              </div>
              <div>
                <div style="color:var(--text-muted);font-size:0.75rem;">Erwartete Rückmeldung:</div>
                <strong style="color:var(--scf-green);" id="wpResCallback">Innert 24–48 Stunden</strong>
              </div>
            </div>

            <div>
              <div style="font-family:'Montserrat',sans-serif;font-size:0.75rem;font-weight:800;text-transform:uppercase;color:var(--scf-navy);margin-bottom:6px;">
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
    var wpScfState = {
      step: 1,
      topic: 'Probetraining / Neumitglied',
      urgency: 'Planbar / Laufende Saison',
      photos: []
    };

    var wpScfRoleConfig = {
      'Probetraining / Neumitglied': {
        assignee: 'Mirko Ferrari (Sportchef · 079 397 87 73) & Michael «Mike» Frieder (Juniorenobmann · 079 647 13 33)',
        l1: 'Name & Jahrgang Spieler/in',
        p1: 'z. B. Levin Muster · Jahrgang 2014',
        l2: 'Gewünschte Mannschaft / Bisheriger Verein',
        p2: 'z. B. Junioren Ea / Junioren B rot-blau / 1. Mannschaft'
      },
      'Sponsoring / Gönner 100er-Club': {
        assignee: 'Andreas Guldimann (Sponsoring · 079 413 76 51) & Willi von Arx (Präsident)',
        l1: 'Gewünschtes Engagement / Paket',
        p1: 'z. B. Bandenwerbung Sportplatz Bad, Silbersponsor oder 100er-Club G&F',
        l2: 'Unternehmen / Wunsch-Team',
        p2: 'z. B. Muster AG Fulenbach · 1. Mannschaft / Nachwuchs'
      },
      'Clubhaus mieten (100 Plätze)': {
        assignee: 'René Hofstetter (Clubhaus-Vermietung · Tel. 079 302 62 47) & Alfred Ammann (Infrastruktur)',
        l1: 'Wunschdatum & Art des Anlasses',
        p1: 'z. B. Samstag 14. November · Familienfest / Firmenapéro',
        l2: 'Erwartete Personenanzahl (max. 100 Plätze)',
        p2: 'z. B. ca. 45 Personen'
      },
      'Spielbetrieb / Schiedsrichter / Turniere': {
        assignee: 'Mirko Ferrari (Sportchef & SR-Verantwortlicher · 079 397 87 73) & Rahel Napoli (Aktuarin)',
        l1: 'Betreff / Mannschaft / Turnier',
        p1: 'z. B. Schiedsrichter-Ausbildung (CHF 500/Jahr) / Anmeldung Dorfturnier Badfest',
        l2: 'Termin / Spielnummer / Teamname',
        p2: 'z. B. SOFV-Meisterschaft / KUBB-Turnier / Dorfturnier'
      },
      'Fanshop / Sponsorenlauf / Juniorenlager': {
        assignee: 'David Ackermann (Medien/Support) & Michael «Mike» Frieder (Juniorenobmann)',
        l1: 'Artikel oder Anlass',
        p1: 'z. B. SCF-Cap (CHF 25.–) / SCF-Wimpel (CHF 15.–) / Juniorenlager-Woche',
        l2: 'Stückzahl oder Name & Jahrgang Kind',
        p2: 'z. B. 2x SCF-Cap + 1x Wimpel'
      },
      'Mitgliedschaft / Mutation / Allgemein': {
        assignee: 'Willi von Arx (Präsident), Roland Wiss (Finanzen a.i.) & Rahel Napoli (Aktuarin)',
        l1: 'Art der Meldung / Anfrage',
        p1: 'z. B. Adressänderung / Mitgliederbeitrag / Frage an den Vorstand',
        l2: 'Name Mitglied & Mannschaft',
        p2: 'z. B. Noah Muster · Senioren 30+'
      }
    };

    function wpUpdateHeader() {
      var titles = {
        1: '1. Wähle dein Anliegen',
        2: '2. Angaben & Beilagen ergänzen',
        3: '3. Kontaktdaten & PDF-Dossier'
      };
      var tEl = document.getElementById('wpWizardTitle');
      if (tEl) tEl.textContent = titles[wpScfState.step] || titles[1];
      for (var i = 1; i <= 3; i++) {
        var pane = document.getElementById('wpStep' + i);
        var pill = document.getElementById('wpStepPill' + i);
        if (pane) {
          if (i === wpScfState.step) pane.classList.add('active');
          else pane.classList.remove('active');
        }
        if (pill) {
          pill.className = 'wp-step-pill';
          if (i === wpScfState.step) pill.classList.add('active');
          else if (i < wpScfState.step) pill.classList.add('done');
        }
      }
    }

    function wpSelectScfTopic(topic) {
      wpScfState.topic = topic;
      var tiles = document.querySelectorAll('#wpTopicGrid .wp-role-tile');
      for (var i = 0; i < tiles.length; i++) {
        if (tiles[i].getAttribute('data-topic') === topic) tiles[i].classList.add('selected');
        else tiles[i].classList.remove('selected');
      }
      var cfg = wpScfRoleConfig[topic] || wpScfRoleConfig['Probetraining / Neumitglied'];
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

    function wpSelectScfUrgency(urg) {
      wpScfState.urgency = urg;
      var tiles = document.querySelectorAll('#wpUrgencyGrid .wp-role-tile');
      for (var i = 0; i < tiles.length; i++) {
        if (tiles[i].getAttribute('data-urg') === urg) tiles[i].classList.add('selected');
        else tiles[i].classList.remove('selected');
      }
    }

    function wpNextStep(stepNum) {
      wpScfState.step = stepNum;
      wpUpdateHeader();
    }

    function wpPrevStep() {
      if (wpScfState.step > 1) {
        wpScfState.step -= 1;
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
      if (cnt) cnt.textContent = wpScfState.photos.length + ' / 3 Bilder ausgewählt · Automatisch für das 1-Seiten-PDF-Dossier optimiert';
      if (!box) return;
      box.innerHTML = '';
      for (var i = 0; i < wpScfState.photos.length; i++) {
        (function(idx) {
          var wrap = document.createElement('div');
          wrap.className = 'wp-thumb-item';
          var im = document.createElement('img');
          im.src = wpScfState.photos[idx];
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
        if (wpScfState.photos.length >= 3) break;
        wpCompressImageFile(files[i], function(b64) {
          if (wpScfState.photos.length < 3) {
            wpScfState.photos.push(b64);
            wpRenderPhotos();
          }
        });
      }
    }

    function wpRemovePhoto(idx) {
      wpScfState.photos.splice(idx, 1);
      wpRenderPhotos();
    }

    function wpCheckScfPlz(val) {
      var badge = document.getElementById('wpPlzBadge');
      var txt = document.getElementById('wpPlzBadgeText');
      if (!badge || !txt) return;
      var rx = new RegExp('\\\\b(\\\\d{4})\\\\b');
      var m = String(val || '').match(rx);
      if (!m) {
        badge.className = 'wp-plz-badge';
        return;
      }
      var plz = parseInt(m[1], 10);
      badge.className = 'wp-plz-badge in-area';
      if (plz >= 4600 && plz <= 4999) {
        txt.textContent = 'PLZ ' + m[1] + ': Direktes Einzugsgebiet Fulenbach, Gäu, Olten & Oberaargau (Sportplatz Bad)';
      } else {
        txt.textContent = 'PLZ ' + m[1] + ': Region Solothurn / Mittelland — Herzlich willkommen beim SC Fulenbach';
      }
    }

    function wpStripEmojisForDom(str) {
      var rx1 = new RegExp('[\\\\u{1F300}-\\\\u{1FAFF}\\\\u{2600}-\\\\u{27BF}]', 'gu');
      var rx2 = new RegExp('\\\\s+\\\\n', 'g');
      return String(str || '').replace(rx1, '').replace(rx2, '\\n').trim();
    }

    function wpResetWizard() {
      wpScfState.step = 1;
      wpScfState.photos = [];
      wpRenderPhotos();
      var form = document.getElementById('scfContactForm');
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
      wpSelectScfTopic('Probetraining / Neumitglied');
      wpSelectScfUrgency('Planbar / Laufende Saison');
      wpUpdateHeader();
    }

    function wpSubmitScfLead(e) {
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

      var cfg = wpScfRoleConfig[wpScfState.topic] || wpScfRoleConfig['Probetraining / Neumitglied'];
      var extra = {};
      extra[cfg.l1] = d1 || 'Keine Angabe';
      extra[cfg.l2] = d2 || 'Keine Angabe';

      var btn = document.getElementById('wpSubmitBtn');
      var btnTxt = document.getElementById('wpSubmitBtnText');
      if (btn) btn.disabled = true;
      if (btnTxt) btnTxt.textContent = '1-Seiten-PDF-Dossier wird erstellt...';

      var payload = {
        client_slug: 'scfulenbach',
        source_page: 'preview-scfulenbach/kontakt.html',
        website_url: hp,
        category: wpScfState.topic,
        sparte: wpScfState.topic,
        urgency: wpScfState.urgency,
        name: name,
        company: company,
        street: street,
        plz: loc,
        phone: phone,
        email: email,
        message: msg || ('Anfrage zum Bereich ' + wpScfState.topic),
        extra_fields: extra,
        photos: wpScfState.photos,
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
        document.getElementById('scfContactForm').style.display = 'none';
        document.getElementById('wpResRef').textContent = res.ref_code || '#SCF-2026';
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
          errBox.textContent = 'Netzwerkfehler bei der Übermittlung. Bitte schreibe direkt an vorstand@scfulenbach.ch.';
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
          'sponsoring': 'Sponsoring / Gönner 100er-Club',
          'clubhaus': 'Clubhaus mieten (100 Plätze)',
          'spielbetrieb': 'Spielbetrieb / Schiedsrichter / Turniere',
          'fanshop': 'Fanshop / Sponsorenlauf / Juniorenlager',
          'mitgliedschaft': 'Mitgliedschaft / Mutation / Allgemein'
        };
        if (map[t]) {
          wpSelectScfTopic(map[t]);
        }
      } catch(err) {}
    })();
  </script>
"""

pages_to_write = [
    ("index.html", "SC Fulenbach — Gegründet 1944 | Vorschau-Entwurf V2 (14 Teams & 88 Sponsoren)", "startseite", INDEX_BODY, ""),
    ("herren-1.html", "Beispiel-Team: 1. Mannschaft (2. Liga reg.) & 14-Teams-Übersicht | SC Fulenbach", "teams", HERREN_1_BODY, HERREN_1_CSS),
    ("kontakt.html", "Smart-Anfrage-Zentrale (Probetraining, Clubhaus, Sponsoring & 1-Seiten-PDF) | SC Fulenbach", "kontakt", KONTAKT_BODY, KONTAKT_CSS),
]

for fname, title, nav_key, body, extra_css in pages_to_write:
    full_html = render_shell(fname, title, nav_key, body, extra_css)
    (SITE_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"Wrote {fname} ({len(full_html)} bytes)")

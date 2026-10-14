#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from pathlib import Path

SITE_DIR = Path("/home/brainuser/workspaces/mxs-embed/preview-birchmeier")

# --- 1. UPDATE KARRIERE.HTML ---
karriere_path = SITE_DIR / "karriere.html"
if karriere_path.exists():
    c = karriere_path.read_text(encoding="utf-8")
    
    # Reset hero image
    c = c.replace("images/niesen_i_20190316_180802.jpg", "images/sanitaer_hero.jpg")
    
    # Replace top bar CSS in karriere.html
    # Find .top-bar { ... } up to .nav-drawer.open
    css_old_pattern = r"\.top-bar\s*\{.*?\.nav-drawer\.open\s*\{[^\}]+\}"
    new_topbar_css = """.top-bar {
      padding: 10px 16px;
      border-bottom: 1px solid var(--border);
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      position: -webkit-sticky;
      position: sticky;
      top: 0;
      z-index: 1000;
      width: 100%;
      box-sizing: border-box;
    }
    .top-bar-inner {
      max-width: 1100px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      box-sizing: border-box;
    }
    .brand-logo-wrap {
      display: flex;
      align-items: center;
      text-decoration: none;
      color: inherit;
      min-width: 0;
      flex: 0 1 auto;
    }
    .brand-logo-img {
      height: 36px;
      max-width: 195px;
      width: auto;
      object-fit: contain;
      display: block;
    }
    .brand-subline {
      display: none;
      font-size: 0.72rem;
      color: var(--text-muted, #64748b);
      font-weight: 500;
      margin-left: 12px;
      padding-left: 12px;
      border-left: 1px solid var(--border, #e2e8f0);
      white-space: nowrap;
    }
    @media (min-width: 960px) {
      .brand-subline { display: inline-block; }
      .brand-logo-img { height: 40px; max-width: 220px; }
    }
    .desktop-nav {
      display: none;
      align-items: center;
      gap: 18px;
    }
    .desk-nav-link {
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text);
      text-decoration: none;
      transition: color 0.15s ease;
      white-space: nowrap;
    }
    .desk-nav-link:hover, .desk-nav-link.active {
      color: var(--primary);
    }
    .btn-desk-direct {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.85rem;
      font-weight: 700;
      color: #fff !important;
      background: var(--primary);
      padding: 9px 18px;
      border-radius: var(--radius-sm);
      text-decoration: none;
      box-shadow: 0 2px 8px var(--primary-glow);
      transition: background 0.15s ease;
      white-space: nowrap;
    }
    .btn-desk-direct:hover {
      background: var(--primary-dark);
    }
    .nav-burger {
      width: 44px;
      height: 44px;
      flex: 0 0 44px;
      margin-left: auto;
      border: 1px solid var(--border);
      background: var(--surface);
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
      -webkit-tap-highlight-color: transparent;
    }
    .nav-burger svg {
      width: 22px;
      height: 22px;
      stroke: var(--text);
    }
    @media (min-width: 860px) {
      .desktop-nav { display: flex !important; }
      .nav-burger { display: none !important; }
    }
    .nav-drawer {
      display: none;
      position: fixed;
      inset: 60px 0 0 0;
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      z-index: 999;
      padding: 24px 20px;
      flex-direction: column;
      gap: 14px;
      box-sizing: border-box;
      overflow-y: auto;
    }
    .nav-drawer.open {
      display: flex !important;
    }
    .nav-drawer .nav-link {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--text);
      text-decoration: none;
      padding: 12px 0;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }"""
    c = re.sub(css_old_pattern, new_topbar_css, c, flags=re.DOTALL)
    
    # Replace Header HTML in karriere.html
    header_old_pattern = r"<!-- TOP BAR -->\s*<header class=\"top-bar\"[^>]*>.*?</header>\s*<!-- MOBILE DRAWER -->\s*<div class=\"nav-drawer\"[^>]*>.*?</div>"
    header_new_html = """<!-- TOP BAR -->
  <header class="top-bar" data-section="top-bar">
    <div class="top-bar-inner">
      <a href="index.html" class="brand-logo-wrap" aria-label="Birchmeier-Hohler Startseite">
        <img src="images/logo.jpg" alt="Birchmeier-Hohler GmbH Logo" class="brand-logo-img" data-slot="brand-logo">
        <span class="brand-subline">Sanitär & Heizungen • Bremgarten AG</span>
      </a>
      <nav class="desktop-nav">
        <a href="index.html" class="desk-nav-link">Startseite</a>
        <a href="team.html" class="desk-nav-link">Über uns & Team</a>
        <a href="#stellen" class="desk-nav-link active">Offene Stellen</a>
        <a href="#vorteile" class="desk-nav-link">Deine Vorteile</a>
        <a href="#bewerben" class="desk-nav-link">Express-Bewerbung</a>
        <a href="kontakt.html" class="desk-nav-link">Kontakt</a>
        <a href="tel:+41566333375" class="btn-desk-direct">
          <span>📞</span> 056 633 33 75
        </a>
      </nav>
      <button class="nav-burger" onclick="toggleDrawer()" aria-label="Menü öffnen">
        <svg viewBox="0 0 24 24" fill="none" stroke-width="2.2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      </button>
    </div>
  </header>

  <!-- MOBILE DRAWER -->
  <div class="nav-drawer" id="navDrawer">
    <a href="index.html" class="nav-link" onclick="toggleDrawer()"><span>🏠 Startseite</span> <span>➔</span></a>
    <a href="team.html" class="nav-link" onclick="toggleDrawer()"><span>👥 Über uns & Team</span> <span>➔</span></a>
    <a href="#stellen" class="nav-link" onclick="toggleDrawer()" style="color:var(--primary); font-weight:800;"><span>🚀 Offene Stellen EFZ</span> <span>➔</span></a>
    <a href="#vorteile" class="nav-link" onclick="toggleDrawer()"><span>⭐ Deine Vorteile</span> <span>➔</span></a>
    <a href="#bewerben" class="nav-link" onclick="toggleDrawer()"><span>⚡ 30s-Express-Bewerbung</span> <span>➔</span></a>
    <a href="kontakt.html" class="nav-link" onclick="toggleDrawer()"><span>📍 Kontakt & Pikett</span> <span>➔</span></a>
    <a href="tel:+41566333375" class="btn-primary" style="margin-top: 14px; width: 100%; text-align: center; justify-content: center; display: flex; align-items: center; gap: 8px;">
      <span>📞</span> Direkt anrufen: 056 633 33 75
    </a>
  </div>"""
    c = re.sub(header_old_pattern, header_new_html, c, flags=re.DOTALL)
    karriere_path.write_text(c, encoding="utf-8")
    print("karriere.html updated.")

# --- 2. UPDATE INDEX.HTML ---
index_path = SITE_DIR / "index.html"
if index_path.exists():
    c = index_path.read_text(encoding="utf-8")
    
    # Title & Metadata
    c = re.sub(r"<title>.*?</title>", "<title>Birchmeier-Hohler GmbH — Sanitär, Heizung & Badumbauten Bremgarten</title>", c)
    c = c.replace("Haustechnik AG", "GmbH")
    c = c.replace("056 648 20 20", "056 633 33 75")
    c = c.replace("+41566482020", "+41566333375")
    c = c.replace("seit 1978", "seit 1931 • 3. Generation")
    c = c.replace("0.3s Edge Speed", "Familienbetrieb seit 1931")
    
    # CSS Top Bar
    css_old_pattern = r"/\* HEADER \(STICKY\) \*/.*?\.nav-drawer\.open\s*\{[^\}]+\}"
    new_index_css = """/* UNIFIED TOP BAR */
    .top-bar {
      padding: 10px 16px;
      border-bottom: 1px solid var(--border);
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      position: -webkit-sticky;
      position: sticky;
      top: 0;
      z-index: 1000;
      width: 100%;
      box-sizing: border-box;
    }
    .top-bar-inner {
      max-width: 1100px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      box-sizing: border-box;
    }
    .brand-logo-wrap {
      display: flex;
      align-items: center;
      text-decoration: none;
      color: inherit;
      min-width: 0;
      flex: 0 1 auto;
    }
    .brand-logo-img {
      height: 36px;
      max-width: 195px;
      width: auto;
      object-fit: contain;
      display: block;
    }
    .brand-subline {
      display: none;
      font-size: 0.72rem;
      color: var(--muted, #64748b);
      font-weight: 500;
      margin-left: 12px;
      padding-left: 12px;
      border-left: 1px solid var(--border, #e2e8f0);
      white-space: nowrap;
    }
    @media (min-width: 960px) {
      .brand-subline { display: inline-block; }
      .brand-logo-img { height: 40px; max-width: 220px; }
    }
    .desktop-nav {
      display: none;
      align-items: center;
      gap: 20px;
    }
    .desk-nav-link {
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text);
      text-decoration: none;
      transition: color 0.15s ease;
      white-space: nowrap;
    }
    .desk-nav-link:hover, .desk-nav-link.active {
      color: var(--primary);
    }
    .btn-desk-contact {
      font-size: 0.85rem;
      font-weight: 700;
      color: #fff !important;
      background: var(--primary);
      padding: 8px 16px;
      border-radius: var(--radius-sm, 6px);
      text-decoration: none;
      box-shadow: 0 2px 8px var(--primary-glow);
      white-space: nowrap;
    }
    .nav-burger {
      width: 44px;
      height: 44px;
      flex: 0 0 44px;
      margin-left: auto;
      border: 1px solid var(--border);
      background: var(--surface);
      border-radius: var(--radius-sm, 6px);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
      -webkit-tap-highlight-color: transparent;
    }
    .nav-burger svg {
      width: 22px;
      height: 22px;
      stroke: var(--text);
    }
    @media (min-width: 860px) {
      .desktop-nav { display: flex !important; }
      .nav-burger { display: none !important; }
    }
    .nav-drawer {
      display: none;
      position: fixed;
      inset: 60px 0 0 0;
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      z-index: 999;
      padding: 24px 20px;
      flex-direction: column;
      gap: 14px;
      box-sizing: border-box;
      overflow-y: auto;
    }
    .nav-drawer.open {
      display: flex !important;
    }
    .nav-drawer .nav-link {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--text);
      text-decoration: none;
      padding: 12px 0;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }"""
    c = re.sub(css_old_pattern, new_index_css, c, flags=re.DOTALL)
    
    # Replace Header HTML in index.html
    header_old_pattern = r"<!-- HEADER -->\s*<header class=\"top-bar\">.*?</header>\s*<!-- MOBILE NAV DRAWER -->\s*<nav class=\"nav-drawer\"[^>]*>.*?</nav>"
    header_new_html = """<!-- HEADER -->
  <header class="top-bar" data-section="top-bar">
    <div class="top-bar-inner">
      <a href="index.html" class="brand-logo-wrap" aria-label="Birchmeier-Hohler Startseite">
        <img src="images/logo.jpg" alt="Birchmeier-Hohler GmbH Logo" class="brand-logo-img" data-slot="brand-logo">
        <span class="brand-subline">Sanitär & Heizungen • Bremgarten AG</span>
      </a>
      <nav class="desktop-nav">
        <a href="index.html" class="desk-nav-link active">Startseite</a>
        <a href="#leistungen" class="desk-nav-link">Leistungen</a>
        <a href="team.html" class="desk-nav-link">Über uns & Team</a>
        <a href="karriere.html" class="desk-nav-link">Karriere / Jobs</a>
        <a href="kontakt.html" class="desk-nav-link">Kontakt & Pikett</a>
        <a href="tel:+41566333375" class="btn-desk-contact">📞 056 633 33 75</a>
      </nav>
      <button class="nav-burger" onclick="toggleDrawer()" aria-label="Menü öffnen">
        <svg viewBox="0 0 24 24" fill="none" stroke-width="2.2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      </button>
    </div>
  </header>

  <!-- MOBILE NAV DRAWER -->
  <nav class="nav-drawer" id="navDrawer">
    <a href="index.html" class="nav-link" onclick="toggleDrawer()"><span>🏠 Startseite</span> <span>➔</span></a>
    <a href="#leistungen" class="nav-link" onclick="toggleDrawer()"><span>🚿 Leistungen & Pikett</span> <span>➔</span></a>
    <a href="team.html" class="nav-link" onclick="toggleDrawer()"><span>👥 Über uns & Team</span> <span>➔</span></a>
    <a href="karriere.html" class="nav-link" onclick="toggleDrawer()" style="color:var(--primary); font-weight:800;"><span>🚀 Offene Stellen (Karriere)</span> <span>➔</span></a>
    <a href="kontakt.html" class="nav-link" onclick="toggleDrawer()"><span>📍 Kontakt & Pikett</span> <span>➔</span></a>
    <a href="tel:+41566333375" class="btn-cta btn-cta-primary" style="margin-top: 14px; text-decoration: none; border-radius: 8px;">
      <span>📞</span> 056 633 33 75 anrufen
    </a>
  </nav>"""
    c = re.sub(header_old_pattern, header_new_html, c, flags=re.DOTALL)
    
    # Upgrade hero stage with real image
    c = c.replace('<div class="hero-stage">\n          <div style="font-size: 3rem; margin-bottom: 10px;">🚿 ♨️ 💧</div>\n          <div style="font-size: 1.25rem; font-weight: 800; letter-spacing: -0.02em;">Haustechnik aus einer Hand</div>\n          <div style="font-size: 0.85rem; color: #94a3b8; margin-top: 6px; max-width: 320px;">Sanitär • Heizung • Badplanung • 24h Pikettdienst</div>\n        </div>',
                  '<img src="images/badumbau.jpg" alt="Sanitär & Badumbau Birchmeier-Hohler" style="width: 100%; height: 100%; object-fit: cover;">')
    
    # Upgrade thumb-bar for mobile
    c = c.replace('<a href="https://wa.me/41790000000" class="btn-thumb btn-thumb-whatsapp">\n      <span>💬</span> WhatsApp\n    </a>',
                  '<a href="karriere.html" class="btn-thumb" style="background:#0f172a; border:1px solid #334155;">\n      <span>🚀</span> Jobs & Karriere\n    </a>')
    
    # Upgrade Teaser Grid in index.html to highlight career
    c = c.replace('<h3 class="service-title">Offene Stellen & Karriere</h3>\n          <p style="font-size: 0.85rem; color: var(--muted);">Verstärken Sie unser Team in Bremgarten. Attraktive Bedingungen & modernste Ausrüstung.</p>\n          <a href="karriere.html" class="teaser-link">Offene Stellen ansehen →</a>',
                  '<h3 class="service-title" style="color:var(--primary);">🚀 Offene Stellen: Sanitär & Heizung EFZ</h3>\n          <p style="font-size: 0.85rem; color: var(--muted);">Wir suchen engagierte Sanitär- und Heizungsinstallateure EFZ in Bremgarten. 4.5-Tage-Woche, eigenes Geschäftsfahrzeug & 30s-Express-Bewerbung ohne Lebenslauf.</p>\n          <a href="karriere.html" class="teaser-link" style="font-weight:800;">Direkt zur Karriereseite & Express-Bewerbung →</a>')

    index_path.write_text(c, encoding="utf-8")
    print("index.html updated.")

# --- 3. UPDATE TEAM.HTML ---
team_path = SITE_DIR / "team.html"
if team_path.exists():
    c = team_path.read_text(encoding="utf-8")
    c = re.sub(r"<title>.*?</title>", "<title>Über uns & Team — Birchmeier-Hohler GmbH Bremgarten</title>", c)
    c = c.replace("Haustechnik AG", "GmbH")
    c = c.replace("056 648 20 20", "056 633 33 75")
    c = c.replace("056 648 20 22", "056 633 33 75")
    c = c.replace("+41566482020", "+41566333375")
    c = c.replace("seit 1978", "seit 1931 • 3. Generation")
    c = c.replace("vier Jahrzehnten", "neun Jahrzehnten")
    
    # CSS
    css_old_pattern = r"/\* HEADER \(STICKY\) \*/.*?\.nav-drawer\.open\s*\{[^\}]+\}"
    c = re.sub(css_old_pattern, new_index_css, c, flags=re.DOTALL)
    
    # Header
    header_old_pattern = r"<!-- HEADER -->\s*<header class=\"top-bar\">.*?</header>\s*<!-- MOBILE NAV DRAWER -->\s*<nav class=\"nav-drawer\"[^>]*>.*?</nav>"
    header_team_html = """<!-- HEADER -->
  <header class="top-bar" data-section="top-bar">
    <div class="top-bar-inner">
      <a href="index.html" class="brand-logo-wrap" aria-label="Birchmeier-Hohler Startseite">
        <img src="images/logo.jpg" alt="Birchmeier-Hohler GmbH Logo" class="brand-logo-img" data-slot="brand-logo">
        <span class="brand-subline">Sanitär & Heizungen • Bremgarten AG</span>
      </a>
      <nav class="desktop-nav">
        <a href="index.html" class="desk-nav-link">Startseite</a>
        <a href="team.html" class="desk-nav-link active">Über uns & Team</a>
        <a href="karriere.html" class="desk-nav-link">Karriere / Jobs</a>
        <a href="kontakt.html" class="desk-nav-link">Kontakt & Pikett</a>
        <a href="tel:+41566333375" class="btn-desk-contact">📞 056 633 33 75</a>
      </nav>
      <button class="nav-burger" onclick="toggleDrawer()" aria-label="Menü öffnen">
        <svg viewBox="0 0 24 24" fill="none" stroke-width="2.2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      </button>
    </div>
  </header>

  <!-- MOBILE NAV DRAWER -->
  <nav class="nav-drawer" id="navDrawer">
    <a href="index.html" class="nav-link" onclick="toggleDrawer()"><span>🏠 Startseite</span> <span>➔</span></a>
    <a href="index.html#leistungen" class="nav-link" onclick="toggleDrawer()"><span>🚿 Leistungen & Pikett</span> <span>➔</span></a>
    <a href="team.html" class="nav-link" onclick="toggleDrawer()" style="color:var(--primary); font-weight:800;"><span>👥 Über uns & Team</span> <span>➔</span></a>
    <a href="karriere.html" class="nav-link" onclick="toggleDrawer()"><span>🚀 Offene Stellen (Karriere)</span> <span>➔</span></a>
    <a href="kontakt.html" class="nav-link" onclick="toggleDrawer()"><span>📍 Kontakt & Pikett</span> <span>➔</span></a>
    <a href="tel:+41566333375" class="btn-cta btn-cta-primary" style="margin-top: 14px; text-decoration: none; border-radius: 8px;">
      <span>📞</span> 056 633 33 75 anrufen
    </a>
  </nav>"""
    c = re.sub(header_old_pattern, header_team_html, c, flags=re.DOTALL)
    team_path.write_text(c, encoding="utf-8")
    print("team.html updated.")

# --- 4. UPDATE KONTAKT.HTML ---
kontakt_path = SITE_DIR / "kontakt.html"
if kontakt_path.exists():
    c = kontakt_path.read_text(encoding="utf-8")
    c = re.sub(r"<title>.*?</title>", "<title>Kontakt & 24h-Pikett — Birchmeier-Hohler GmbH Bremgarten</title>", c)
    c = c.replace("Haustechnik AG", "GmbH")
    c = c.replace("056 648 20 20", "056 633 33 75")
    c = c.replace("+41566482020", "+41566333375")
    
    # CSS
    css_old_pattern = r"/\* HEADER \(STICKY\) \*/.*?\.nav-drawer\.open\s*\{[^\}]+\}"
    c = re.sub(css_old_pattern, new_index_css, c, flags=re.DOTALL)
    
    # Header
    header_old_pattern = r"<!-- HEADER -->\s*<header class=\"top-bar\">.*?</header>\s*<!-- MOBILE NAV DRAWER -->\s*<nav class=\"nav-drawer\"[^>]*>.*?</nav>"
    header_kontakt_html = """<!-- HEADER -->
  <header class="top-bar" data-section="top-bar">
    <div class="top-bar-inner">
      <a href="index.html" class="brand-logo-wrap" aria-label="Birchmeier-Hohler Startseite">
        <img src="images/logo.jpg" alt="Birchmeier-Hohler GmbH Logo" class="brand-logo-img" data-slot="brand-logo">
        <span class="brand-subline">Sanitär & Heizungen • Bremgarten AG</span>
      </a>
      <nav class="desktop-nav">
        <a href="index.html" class="desk-nav-link">Startseite</a>
        <a href="team.html" class="desk-nav-link">Über uns & Team</a>
        <a href="karriere.html" class="desk-nav-link">Karriere / Jobs</a>
        <a href="kontakt.html" class="desk-nav-link active">Kontakt & Pikett</a>
        <a href="tel:+41566333375" class="btn-desk-contact">📞 056 633 33 75</a>
      </nav>
      <button class="nav-burger" onclick="toggleDrawer()" aria-label="Menü öffnen">
        <svg viewBox="0 0 24 24" fill="none" stroke-width="2.2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      </button>
    </div>
  </header>

  <!-- MOBILE NAV DRAWER -->
  <nav class="nav-drawer" id="navDrawer">
    <a href="index.html" class="nav-link" onclick="toggleDrawer()"><span>🏠 Startseite</span> <span>➔</span></a>
    <a href="index.html#leistungen" class="nav-link" onclick="toggleDrawer()"><span>🚿 Leistungen & Pikett</span> <span>➔</span></a>
    <a href="team.html" class="nav-link" onclick="toggleDrawer()"><span>👥 Über uns & Team</span> <span>➔</span></a>
    <a href="karriere.html" class="nav-link" onclick="toggleDrawer()"><span>🚀 Offene Stellen (Karriere)</span> <span>➔</span></a>
    <a href="kontakt.html" class="nav-link" onclick="toggleDrawer()" style="color:var(--primary); font-weight:800;"><span>📍 Kontakt & Pikett</span> <span>➔</span></a>
    <a href="tel:+41566333375" class="btn-cta btn-cta-primary" style="margin-top: 14px; text-decoration: none; border-radius: 8px;">
      <span>📞</span> 056 633 33 75 anrufen
    </a>
  </nav>"""
    c = re.sub(header_old_pattern, header_kontakt_html, c, flags=re.DOTALL)
    kontakt_path.write_text(c, encoding="utf-8")
    print("kontakt.html updated.")

print("All refinements applied successfully.")

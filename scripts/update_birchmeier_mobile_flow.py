#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Harmonisiert Header, Mobile-Tauglichkeit, Hamburger-Menü und Unternehmensdaten 
über alle Birchmeier-Hohler Seiten (index.html, karriere.html, team.html, kontakt.html).
"""

import re
from pathlib import Path

SITE_DIR = Path("/home/brainuser/workspaces/mxs-embed/preview-birchmeier")

UNIFIED_HEADER_CSS = """
    /* UNIFIED TOP BAR (100% MOBILE-SAFE) */
    .top-bar {
      padding: 10px 16px;
      position: -webkit-sticky;
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      width: 100%;
      box-sizing: border-box;
    }
    .top-bar-inner {
      max-width: 1100px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
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
      box-shadow: 0 2px 8px var(--primary-glow, rgba(2,132,199,0.2));
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
    .nav-drawer.open { display: flex !important; }
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
    }
"""

def generate_header_html(active_page="index"):
    def is_act(p): return " active" if p == active_page else ""
    return f"""  <!-- HEADER -->
  <header class="top-bar" data-section="top-bar">
    <div class="top-bar-inner">
      <a href="index.html" class="brand-logo-wrap" aria-label="Birchmeier-Hohler Startseite">
        <img src="images/logo.jpg" alt="Birchmeier-Hohler GmbH Logo" class="brand-logo-img" data-slot="brand-logo">
        <span class="brand-subline">Sanitär & Heizungen • Bremgarten AG</span>
      </a>
      <nav class="desktop-nav">
        <a href="index.html" class="desk-nav-link{is_act('index')}">Startseite</a>
        <a href="index.html#leistungen" class="desk-nav-link">Leistungen</a>
        <a href="team.html" class="desk-nav-link{is_act('team')}">Über uns & Team</a>
        <a href="karriere.html" class="desk-nav-link{is_act('karriere')}">Karriere / Jobs</a>
        <a href="kontakt.html" class="desk-nav-link{is_act('kontakt')}">Kontakt & Pikett</a>
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
    <a href="karriere.html" class="nav-link" onclick="toggleDrawer()" style="color:var(--primary); font-weight:800;"><span>🚀 Offene Stellen (Karriere)</span> <span>➔</span></a>
    <a href="kontakt.html" class="nav-link" onclick="toggleDrawer()"><span>📍 Kontakt & Standort</span> <span>➔</span></a>
    <a href="tel:+41566333375" class="btn-cta btn-cta-primary" style="margin-top: 14px; text-decoration: none; border-radius: 8px;">
      <span>📞</span> 056 633 33 75 anrufen
    </a>
  </nav>"""

print("Script template ready.")

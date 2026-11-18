#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Multi-Domain Site Generator: Jakob Hauser AG / autohauser® (Oftringen)
Erzeugt:
  - preview-autohauser (Vollversion inkl. WebPilot Studio Cockpit & Stil-Matrix)
  - preview-autohauser-v2 (Zeigeversion ohne Cockpit-Links)
Inkl. aller 3 Sparten (Unfallreparatur, Autobeschriftung, Classic Cars),
26 Ratgeber-Detailseiten, 72 lokalen PDFs, 6 Team-Portraits & Smart-Pro Lead-Assistent.
"""

import html as _html
import json
import os
import re
import shutil
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
OUT_V1 = BASE_DIR / "preview-autohauser"
OUT_V2 = BASE_DIR / "preview-autohauser-v2"
SCRAPED_JSON = Path("/tmp/autohauser_clean_content.json")
DIMS_JSON = Path("/tmp/autohauser_img_dims.json")
PDFS_JSON = Path("/tmp/autohauser_core_pdfs.json")
PDF_META_JSON = Path("/tmp/pimcore_pdfs_meta.json")

# Helvetischer Text-Sanitizer (#LANG-01 / #LANG-02)
def ch_text(s: str) -> str:
    if not s:
        return ""
    s = s.replace("\u00a0", " ")
    s = s.replace("\u00df", "ss")
    # Em-Dash ausser nach Punkt bei CHF (.—) ersetzen
    s = re.sub(r"(?<!\.)\s*\u2014\s*", " – ", s)
    # Typische Bundesdeutsch-Begriffe bereinigen
    repls = [
        ("Kostenvoranschlag", "Offerte"),
        ("Kostenvoranschlags", "Offert"),
        ("Gerichsturteil", "Gerichtsurteil"),
        ("schlafende Hunde", "schlafende Hunde"),
        ("Ersatwagen", "Ersatzwagen"),
        ("entspechenden", "entsprechenden"),
        ("Ansprechsperson", "Ansprechperson"),
        ("Garantier-Anspruches", "Garantieanspruchs"),
        ("Mehrwehrtsteuernummer", "Mehrwertsteuernummer"),
        ("Verfügen", "Verfügen"),
        ("autohauser ®", "autohauser®"),
        ("folioCar ®", "folioCar®"),
        ("YellowFox ®", "YellowFox®"),
        (" ,", ","),
    ]
    for old, new in repls:
        s = s.replace(old, new)
    s = re.sub(r"\s{2,}", " ", s).strip()
    return s

def esc(s: str) -> str:
    return _html.escape(ch_text(s), quote=True)

def load_data():
    scraped = json.loads(SCRAPED_JSON.read_text(encoding="utf-8"))
    dims = json.loads(DIMS_JSON.read_text(encoding="utf-8"))
    pdfs = json.loads(PDFS_JSON.read_text(encoding="utf-8"))
    pdf_meta = json.loads(PDF_META_JSON.read_text(encoding="utf-8")) if PDF_META_JSON.exists() else {}
    return scraped, dims, pdfs, pdf_meta

def img_tag(dims: dict, fname: str, alt: str, css_class: str = "", prefix: str = "", is_hero: bool = False, extra_style: str = "") -> str:
    info = dims.get(fname, {"w": 800, "h": 500})
    w, h = info["w"], info["h"]
    src = f"{prefix}assets/{fname}"
    load_attr = 'fetchpriority="high" decoding="async"' if is_hero else 'loading="lazy" decoding="async"'
    cls_attr = f' class="{css_class}"' if css_class else ""
    st_attr = f' style="{extra_style}"' if extra_style else ""
    return f'<img src="{src}" alt="{esc(alt)}" width="{w}" height="{h}"{cls_attr}{st_attr} {load_attr}>'

# --- SVG Icons (100 % Lucide, 0 Unicode-Emojis!) ---
ICONS = {
    "phone": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "shield": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
    "wrench": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
    "car": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/></svg>',
    "cloud-rain": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242"/><path d="M16 14v6"/><path d="M8 14v6"/><path d="M12 16v6"/></svg>',
    "sparkles": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 3-1.9 5.8a2 2 0 0 1-1.287 1.288L3 12l5.8 1.9a2 2 0 0 1 1.288 1.287L12 21l1.9-5.8a2 2 0 0 1 1.287-1.288L21 12l-5.8-1.9a2 2 0 0 1-1.288-1.287Z"/></svg>',
    "layers": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>',
    "file-text": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>',
    "download": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>',
    "arrow-right": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
    "check": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>',
    "map-pin": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
    "mail": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>',
    "clock": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
    "camera": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/></svg>',
    "users": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    "award": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/></svg>',
    "menu": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>',
    "x": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>',
    "chevron-left": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="15 18 9 12 15 6"/></svg>',
    "external": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>',
    "briefcase": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="20" height="14" x="2" y="7" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
}

SHARED_CSS = """
:root {
  --bg: #ffffff;
  --bg-alt: #f6f8fb;
  --surface: #ffffff;
  --primary: #0067b2;
  --primary-dark: #00468b;
  --primary-soft: #eef5fc;
  --accent: #0067b2;
  --navy: #0b2545;
  --text-main: #0f172a;
  --text-muted: #475569;
  --border: #e2e8f0;
  --border-strong: rgba(15, 23, 42, 0.16);
  --success: #059669;
  --danger: #dc2626;
  --radius-sm: 4px;
  --radius-md: 8px;
  --font-display: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --container: 1120px;
}

*, *::before, *::after { box-sizing: border-box; }
html { scroll-behavior: smooth; interpolate-size: allow-keywords; }
@media (prefers-reduced-motion: no-preference) {
  @view-transition { navigation: auto; }
}
body {
  margin: 0;
  padding: 0;
  background: var(--bg);
  color: var(--text-main);
  font-family: var(--font-body);
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  overflow-x: clip;
}
::selection { background: rgba(0, 103, 178, 0.16); color: var(--primary-dark); }
:focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; }

h1, h2, h3, h4 {
  font-family: var(--font-display);
  color: var(--text-main);
  margin: 0 0 12px 0;
  line-height: 1.18;
  letter-spacing: -0.02em;
}
h1 { font-size: clamp(1.85rem, 3.4vw, 2.7rem); font-weight: 800; }
h2 { font-size: clamp(1.45rem, 2.5vw, 2.05rem); font-weight: 800; }
h3 { font-size: 1.15rem; font-weight: 700; }
p { margin: 0 0 14px 0; color: var(--text-muted); }
a { color: var(--primary); text-decoration-thickness: 1.5px; text-underline-offset: 3px; }
img { max-width: 100%; height: auto; display: block; }
.tabular { font-variant-numeric: tabular-nums; }

.container {
  width: 100%;
  max-width: var(--container);
  margin: 0 auto;
  padding: 0 24px;
}

/* Kicker: 100 % pur linksbuendig ohne Vor-Strich (#UI-01) */
.section-kicker {
  display: block;
  font-family: var(--font-display);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--primary);
  margin: 0 0 8px 0;
  background: transparent;
  border: none;
  padding: 0;
}
.section-head {
  max-width: 720px;
  margin-bottom: 36px;
}
.section { padding: 72px 0; }
.section-alt { background: var(--bg-alt); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); }
.dark-section { background: var(--navy); color: #ffffff; }
.dark-section h2, .dark-section h3 { color: #ffffff; }
.dark-section p { color: #cbd5e1; }
.dark-section .section-kicker { color: #7dd3fc; }

/* Sparten Top Bar */
.ah-sparten-bar {
  background: var(--primary-dark);
  color: #ffffff;
  font-size: 0.8rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.14);
}
.ah-sparten-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 40px;
}
.ah-sparten-tabs {
  display: flex;
  align-items: center;
  gap: 4px;
  overflow-x: auto;
  scrollbar-width: none;
}
.ah-sparten-tabs::-webkit-scrollbar { display: none; }
.ah-sparte-tab {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  color: rgba(255, 255, 255, 0.82);
  text-decoration: none;
  font-weight: 600;
  white-space: nowrap;
  border-bottom: 2px solid transparent;
  transition: color 0.15s ease, background 0.15s ease;
}
.ah-sparte-tab:hover { color: #ffffff; background: rgba(255, 255, 255, 0.08); }
.ah-sparte-tab.is-active {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.12);
  border-bottom-color: #ffffff;
}
.ah-top-hotline {
  display: flex;
  align-items: center;
  gap: 16px;
  white-space: nowrap;
}
.ah-top-hotline a {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: #ffffff;
  font-weight: 700;
  text-decoration: none;
}
.ah-top-meta { color: rgba(255, 255, 255, 0.8); }

/* Header & Single-Line Desktop Nav (#UI-02 / S-22) */
.site-header {
  position: sticky;
  top: 0;
  z-index: 90;
  background: rgba(255, 255, 255, 0.97);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--border);
}
.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  min-height: 70px;
}
.brand-logo {
  display: inline-flex;
  align-items: center;
  flex-shrink: 0;
  text-decoration: none;
}
.brand-logo img {
  height: 36px;
  width: auto;
  object-fit: contain;
}
.nav-links {
  display: flex;
  align-items: center;
  gap: 20px;
  flex-wrap: nowrap;
}
.nav-links a {
  color: var(--text-main);
  text-decoration: none;
  font-family: var(--font-display);
  font-size: 0.9rem;
  font-weight: 600;
  white-space: nowrap;
  padding: 6px 2px;
  border-bottom: 2px solid transparent;
  transition: color 0.15s ease, border-color 0.15s ease;
}
.nav-links a:hover, .nav-links a.active {
  color: var(--primary);
  border-bottom-color: var(--primary);
}
.header-actions {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
}
.mobile-menu-btn {
  display: none;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 42px;
  border: 1px solid var(--border-strong);
  border-radius: var(--radius-md);
  background: #ffffff;
  color: var(--text-main);
  cursor: pointer;
}
.mobile-drawer {
  display: none;
  background: #ffffff;
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  padding: 16px 24px 20px;
}
.mobile-drawer.open { display: block; }
.mobile-drawer-links {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 14px;
}
.mobile-drawer-links a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 12px;
  border-radius: var(--radius-md);
  color: var(--text-main);
  text-decoration: none;
  font-weight: 600;
  background: var(--bg-alt);
}
.mobile-drawer-links a.active {
  background: var(--primary-soft);
  color: var(--primary-dark);
}

/* Buttons & Badges (Strikte 4px / 8px Architektur!) */
.btn, .btn-cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 11px 18px;
  border-radius: var(--radius-md);
  font-family: var(--font-display);
  font-size: 0.92rem;
  font-weight: 700;
  text-decoration: none;
  cursor: pointer;
  border: 1px solid transparent;
  transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease;
  white-space: nowrap;
}
.btn-primary, .btn-cta {
  background: var(--primary);
  color: #ffffff;
  border-color: var(--primary);
}
.btn-primary:hover, .btn-cta:hover {
  background: var(--primary-dark);
  border-color: var(--primary-dark);
  color: #ffffff;
}
.btn-outline {
  background: #ffffff;
  color: var(--primary-dark);
  border-color: var(--border-strong);
}
.btn-outline:hover {
  background: var(--primary-soft);
  border-color: var(--primary);
}
.btn-sm { padding: 8px 14px; font-size: 0.84rem; }
.meta-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  border-radius: var(--radius-sm);
  font-size: 0.76rem;
  font-weight: 700;
  background: var(--primary-soft);
  color: var(--primary-dark);
  border: 1px solid rgba(0, 103, 178, 0.18);
}

/* Hero & Bottom-Edge Baseline Lock (#UI-02 / S-23) */
.hero-section {
  padding: 52px 0 60px;
  background: #ffffff;
  border-bottom: 1px solid var(--border);
}
.hero-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(0, 0.85fr);
  gap: 40px;
  align-items: stretch;
}
.hero-grid > div:first-child {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 24px;
}
.hero-lead {
  font-size: 1.08rem;
  color: var(--text-muted);
  max-width: 60ch;
}
.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 20px;
}
.hero-metrics {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}
.metric-box {
  background: var(--bg-alt);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 14px 16px;
}
.metric-val {
  font-family: var(--font-display);
  font-size: 1.12rem;
  font-weight: 800;
  color: var(--primary-dark);
  margin-bottom: 2px;
}
.metric-lbl { font-size: 0.82rem; color: var(--text-muted); }

.hero-media-card {
  background: var(--bg-alt);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}
.hero-media-img {
  width: 100%;
  aspect-ratio: 16 / 10;
  object-fit: cover;
}
.hero-media-body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  flex: 1;
  justify-content: space-between;
}
.hero-contact-strip {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding-top: 12px;
  border-top: 1px solid var(--border);
  font-size: 0.85rem;
}

/* Grids & Cards (Kompatibel mit Stil- & Handschrift-Matrix + S-31) */
.grid-2 { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px; }
.grid-3 { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }
.grid-4 { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 20px; }

.card, .content-card, .service-card, .feature-card, .founder-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 14px;
}
.card-img-top {
  width: calc(100% + 48px);
  margin: -24px -24px 8px -24px;
  aspect-ratio: 16 / 10;
  object-fit: cover;
  border-bottom: 1px solid var(--border);
  border-radius: var(--radius-md) var(--radius-md) 0 0;
}
.card-badge-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
}
.icon-box {
  width: 38px;
  height: 38px;
  border-radius: var(--radius-md);
  background: var(--primary-soft);
  color: var(--primary);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.sparte-logo-wrap {
  height: 44px;
  display: flex;
  align-items: center;
  margin-bottom: 6px;
}
.sparte-logo-wrap img {
  max-height: 38px;
  width: auto;
  object-fit: contain;
}
.team-portrait {
  width: 84px;
  height: 84px;
  border-radius: var(--radius-md);
  object-fit: cover;
  border: 1px solid var(--border);
}
.list-check {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.list-check li {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  font-size: 0.92rem;
  color: var(--text-muted);
}
.list-check svg { color: var(--primary); flex-shrink: 0; margin-top: 3px; }

/* Smart-Pro Wizard */
.wp-wizard-card {
  background: #ffffff;
  border: 1px solid var(--border-strong);
  border-radius: var(--radius-md);
  padding: 28px;
  box-shadow: 0 12px 32px rgba(15, 23, 42, 0.06);
}
.wp-wizard-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}
.wp-step-indicator {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--primary-dark);
  background: var(--primary-soft);
  padding: 4px 10px;
  border-radius: var(--radius-sm);
}
.wp-progress-track {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 6px;
  margin-bottom: 18px;
}
.wp-progress-seg {
  height: 4px;
  border-radius: 4px;
  background: var(--border);
}
.wp-progress-seg.active { background: var(--primary); }
.wp-step-pane { display: none; }
.wp-step-pane.active { display: block; }
.wp-tile-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 10px;
  margin-bottom: 16px;
}
.wp-tile-btn {
  text-align: left;
  padding: 12px 14px;
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  background: var(--bg-alt);
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  gap: 4px;
  font-family: var(--font-body);
  transition: border-color 0.15s ease, background 0.15s ease;
}
.wp-tile-btn:hover { border-color: var(--primary); background: #ffffff; }
.wp-tile-btn.selected {
  border-color: var(--primary);
  background: var(--primary-soft);
  box-shadow: inset 0 0 0 1px var(--primary);
}
.wp-tile-title { font-weight: 700; font-size: 0.92rem; color: var(--text-main); line-height: 1.3; min-height: 2.6em; }
.wp-tile-sub { font-size: 0.78rem; color: var(--text-muted); line-height: 1.4; }
.wp-form-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
  margin-bottom: 14px;
}
.wp-field { display: flex; flex-direction: column; gap: 5px; }
.wp-field-full { grid-column: 1 / -1; }
.wp-label { font-size: 0.84rem; font-weight: 600; color: var(--text-main); }
.form-input, .form-textarea, .wp-select {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #cbd5e1;
  border-radius: var(--radius-md);
  font-family: var(--font-body);
  font-size: 16px;
  color: var(--text-main);
  background: #ffffff;
}
.form-input:user-invalid, .form-textarea:user-invalid { border-color: var(--danger) !important; outline: none; }
.wp-photo-drop {
  border: 1px dashed #94a3b8;
  border-radius: var(--radius-md);
  padding: 14px;
  background: var(--bg-alt);
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}
.wp-photo-thumbs { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px; }
.wp-photo-thumb {
  position: relative;
  width: 68px;
  height: 68px;
  border-radius: var(--radius-sm);
  overflow: hidden;
  border: 1px solid var(--border);
}
.wp-photo-thumb img { width: 100%; height: 100%; object-fit: cover; }
.wp-photo-rm {
  position: absolute;
  top: 2px;
  right: 2px;
  width: 20px;
  height: 20px;
  border: none;
  border-radius: var(--radius-sm);
  background: rgba(15, 23, 42, 0.78);
  color: #ffffff;
  font-size: 12px;
  cursor: pointer;
}
.wp-err-box {
  display: none;
  padding: 10px 12px;
  border-radius: var(--radius-md);
  background: #fef2f2;
  border: 1px solid #fecaca;
  color: #991b1b;
  font-size: 0.86rem;
  margin-bottom: 12px;
}
.wp-result-box {
  display: none;
  padding: 20px;
  border-radius: var(--radius-md);
  background: #ecfdf5;
  border: 1px solid #6ee7b7;
}

/* Tabs & Filters */
.tab-bar, .filter-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 24px;
}
.tab-btn, .filter-btn {
  padding: 9px 15px;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-strong);
  background: #ffffff;
  color: var(--text-main);
  font-family: var(--font-display);
  font-size: 0.86rem;
  font-weight: 700;
  cursor: pointer;
}
.tab-btn.active, .filter-btn.active {
  background: var(--primary);
  border-color: var(--primary);
  color: #ffffff;
}

/* JotForm Modal */
.jf-modal-backdrop {
  display: none;
  position: fixed;
  inset: 0;
  z-index: 200;
  background: rgba(15, 23, 42, 0.72);
  padding: 20px;
  align-items: center;
  justify-content: center;
}
.jf-modal-backdrop.open { display: flex; }
.jf-modal-dialog {
  width: 100%;
  max-width: 860px;
  max-height: 90vh;
  background: #ffffff;
  border-radius: var(--radius-md);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border: 1px solid var(--border);
}
.jf-modal-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 14px 20px;
  border-bottom: 1px solid var(--border);
  background: var(--bg-alt);
}
.jf-modal-body {
  flex: 1;
  overflow-y: auto;
  min-height: 460px;
}
.jf-modal-body iframe {
  width: 100%;
  height: 540px;
  border: 0;
}

/* Specs Table */
.spec-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}
.spec-table th, .spec-table td {
  padding: 8px 10px;
  border-bottom: 1px solid var(--border);
  text-align: left;
}
.spec-table th { color: var(--text-muted); font-weight: 600; width: 46%; }
.spec-table td { color: var(--text-main); font-weight: 700; }

/* Footer */
.site-footer {
  background: var(--navy);
  color: #e2e8f0;
  padding: 56px 0 28px;
}
.footer-grid {
  display: grid;
  grid-template-columns: 1.3fr 1fr 1fr 1.1fr;
  gap: 32px;
  padding-bottom: 36px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.14);
}
.site-footer h4 { color: #ffffff; font-size: 0.95rem; margin-bottom: 14px; }
.site-footer p, .site-footer li, .site-footer a {
  color: #cbd5e1;
  font-size: 0.88rem;
  text-decoration: none;
}
.site-footer a:hover { color: #ffffff; text-decoration: underline; }
.footer-list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 8px; }
.footer-bottom {
  padding-top: 20px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  font-size: 0.82rem;
  color: #94a3b8;
}

/* Responsive */
@media (min-width: 1024px) {
  .hero-actions { flex-wrap: nowrap; }
  .founder-header-row { min-height: 92px; align-items: flex-start; }
  .stimme-card { justify-content: flex-start; }
  .stimme-header-row { min-height: 112px; align-items: flex-start; }
  .stimme-header-row h3 { min-height: 3.1em; }
}
@media (max-width: 1023px) {
  .nav-links, .header-actions .btn-desktop-only { display: none; }
  .mobile-menu-btn { display: inline-flex; }
  .ah-top-meta { display: none; }
}
@media (max-width: 900px) {
  .hero-grid, .grid-3, .grid-4, .footer-grid { grid-template-columns: 1fr; }
  .grid-2 { grid-template-columns: 1fr; }
}
@media (max-width: 767px) {
  .ah-top-hotline { display: none; }
  .ah-sparten-tabs { width: 100%; justify-content: space-between; }
  .ah-sparte-tab { min-height: 38px; padding: 8px 10px; }
  .footer-list a, .footer-bottom a, .founder-contact-links a, .contact-direct-list a, .hero-contact-strip a {
    display: inline-flex;
    align-items: center;
    min-height: 36px;
    padding: 4px 0;
  }
}
@media (max-width: 640px) {
  .container { padding: 0 16px; }
  .section { padding: 48px 0; }
  .hero-section { padding: 32px 0 40px; }
  .hero-metrics, .wp-tile-grid-2, .wp-form-grid { grid-template-columns: 1fr; }
  .ah-sparten-bar { font-size: 0.76rem; }
  .wp-wizard-card { padding: 18px; }
}
body.is-embedded .ah-sparten-bar,
body.is-embedded .site-header { position: static; }
"""

def render_head(title: str, desc: str, prefix: str = "", canonical_page: str = "index.html") -> str:
    return f"""<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-XSS-Protection" content="1; mode=block">
  <meta name="referrer" content="no-referrer">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
  <style id="ah-core-styles">{SHARED_CSS}</style>
  <style id="wp-custom-design-vibe"></style>
</head>"""

def render_header(active_sparte: str, active_nav: str, dims: dict, prefix: str = "", show_cockpit: bool = False) -> str:
    logo_html = img_tag(dims, "autohauser_logo.png", "autohauser® – Jakob Hauser AG Oftringen", prefix=prefix, is_hero=False)
    nav_items = [
        ("index.html", "Unfall & Glas", "unfall"),
        ("beschriftung.html", "Beschriftung", "beschriftung"),
        ("classics.html", "Classic Cars", "classics"),
        ("ratgeber.html", "Ratgeber", "ratgeber"),
        ("team-unternehmen.html", "Team", "team"),
        ("karriere.html", "Karriere", "karriere"),
    ]
    nav_html = "\n        ".join(
        f'<a href="{prefix}{href}" class="{"active" if active_nav == key else ""}">{label}</a>'
        for href, label, key in nav_items
    )
    mob_html = "\n        ".join(
        f'<a href="{prefix}{href}" class="{"active" if active_nav == key else ""}"><span>{label}</span>{ICONS["arrow-right"]}</a>'
        for href, label, key in nav_items
    )
    cockpit_btn = (
        f'<a href="{prefix}cockpit.html" class="btn btn-outline btn-sm btn-desktop-only" title="WebPilot Studio Cockpit öffnen">Cockpit</a>'
        if show_cockpit else ""
    )
    return f"""
  <div class="ah-sparten-bar">
    <div class="container ah-sparten-inner">
      <div class="ah-sparten-tabs" role="navigation" aria-label="autohauser Sparten">
        <a href="{prefix}index.html" class="ah-sparte-tab {"is-active" if active_sparte == "unfall" else ""}">Unfallreparatur</a>
        <a href="{prefix}beschriftung.html" class="ah-sparte-tab {"is-active" if active_sparte == "beschriftung" else ""}">Autobeschriftung</a>
        <a href="{prefix}classics.html" class="ah-sparte-tab {"is-active" if active_sparte == "classics" else ""}">Classic Cars</a>
      </div>
      <div class="ah-top-hotline">
        <span class="ah-top-meta">Oftringen · Seit 1948</span>
        <a href="tel:0800875875">{ICONS["phone"]}<span class="tabular">0800 875 875</span></a>
      </div>
    </div>
  </div>
  <header class="site-header">
    <div class="container header-inner">
      <a href="{prefix}index.html" class="brand-logo" aria-label="autohauser Startseite">
        {logo_html}
      </a>
      <nav class="nav-links" aria-label="Hauptnavigation">
        {nav_html}
      </nav>
      <div class="header-actions">
        {cockpit_btn}
        <a href="{prefix}schaden-kontakt.html" class="btn btn-primary btn-sm btn-desktop-only">Schaden melden</a>
        <button type="button" class="mobile-menu-btn" aria-label="Menü öffnen" aria-expanded="false" onclick="toggleMobileDrawer(this)">
          {ICONS["menu"]}
        </button>
      </div>
    </div>
    <div class="mobile-drawer" id="mobileMenu">
      <div class="mobile-drawer-links">
        {mob_html}
        <a href="{prefix}schaden-kontakt.html" class="{"active" if active_nav == "kontakt" else ""}"><span>Schaden &amp; Kontakt</span>{ICONS["arrow-right"]}</a>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:8px;">
        <a href="{prefix}schaden-kontakt.html" class="btn btn-primary" style="flex:1;">Schaden melden</a>
        <a href="tel:0800875875" class="btn btn-outline" style="flex:1;">{ICONS["phone"]}<span>0800 875 875</span></a>
      </div>
    </div>
  </header>"""

def render_footer(prefix: str = "", show_cockpit: bool = False) -> str:
    cockpit_li = f'<li><a href="{prefix}cockpit.html">WebPilot Studio Cockpit</a></li>' if show_cockpit else ""
    return f"""
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <h4>Jakob Hauser AG · autohauser®</h4>
          <p>Carrosserie, Unfallinstandstellung, Fahrzeugbeschriftung, folioCar® und Classic Cars seit 1948.</p>
          <p>Äussere Luzernerstrasse 12, 4665 Oftringen<br>Postfach 950, CH-4800 Zofingen<br>UID: CHE-103.749.299</p>
        </div>
        <div>
          <h4>Die 3 Sparten</h4>
          <ul class="footer-list">
            <li><a href="{prefix}index.html">Unfallreparatur &amp; Hagel</a></li>
            <li><a href="{prefix}beschriftung.html">Autobeschriftung &amp; folioCar®</a></li>
            <li><a href="{prefix}classics.html">Classic Cars &amp; YellowFox®</a></li>
            <li><a href="{prefix}schaden-kontakt.html">Glasschaden &amp; Rückruf</a></li>
          </ul>
        </div>
        <div>
          <h4>Wissen &amp; Unternehmen</h4>
          <ul class="footer-list">
            <li><a href="{prefix}ratgeber.html">26 Ratgeber &amp; Merkblätter</a></li>
            <li><a href="{prefix}team-unternehmen.html">Team &amp; 6 Ansprechpersonen</a></li>
            <li><a href="{prefix}karriere.html">Offene Stellen</a></li>
            <li><a href="{prefix}team-unternehmen.html#rechtliches">Impressum, Datenschutz &amp; AGB</a></li>
            {cockpit_li}
          </ul>
        </div>
        <div>
          <h4>24h-Hotline &amp; Zentrale</h4>
          <ul class="footer-list">
            <li><a href="tel:0800875875" class="tabular">Gratis-Hotline: 0800 875 875</a></li>
            <li><a href="tel:+41627893330" class="tabular">Zentrale: +41 62 789 33 30</a></li>
            <li><a href="mailto:info@autohauser.ch">info@autohauser.ch</a></li>
            <li>Mo–Fr: 07:30–12:00 &amp; 13:15–17:30</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© 2026 Jakob Hauser AG · autohauser® · Oftringen / Zofingen (seit 1948)</span>
        <span>Alle Rechte vorbehalten · <a href="{prefix}team-unternehmen.html#rechtliches" style="color:#cbd5e1;">Impressum &amp; Datenschutz</a></span>
      </div>
    </div>
  </footer>

  <!-- Lazy JotForm Modal (Zero-Bloat beim Initial-Load) -->
  <div class="jf-modal-backdrop" id="jfModal" role="dialog" aria-modal="true" aria-labelledby="jfModalTitle">
    <div class="jf-modal-dialog">
      <div class="jf-modal-head">
        <div>
          <span class="section-kicker" style="margin-bottom:2px;">SPEZIALFORMULAR</span>
          <h3 id="jfModalTitle" style="margin:0;font-size:1.05rem;">Formular wird geladen</h3>
        </div>
        <div style="display:flex;align-items:center;gap:8px;">
          <a id="jfExternalLink" href="#" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">{ICONS["external"]}<span>Neuer Tab</span></a>
          <button type="button" class="btn btn-outline btn-sm" onclick="closeJotFormModal()" aria-label="Modal schliessen">{ICONS["x"]}</button>
        </div>
      </div>
      <div class="jf-modal-body" id="jfModalBody"></div>
    </div>
  </div>

  <script>
    function toggleMobileDrawer(btn) {{
      var m = document.getElementById('mobileMenu');
      if (!m) return;
      var open = m.classList.toggle('open');
      if (btn) btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    }}
    function openJotFormModal(title, url) {{
      var m = document.getElementById('jfModal');
      var t = document.getElementById('jfModalTitle');
      var ext = document.getElementById('jfExternalLink');
      var body = document.getElementById('jfModalBody');
      if (!m || !body) return;
      if (t) t.textContent = title;
      if (ext) ext.href = url;
      body.innerHTML = '<iframe src="' + url + '" title="' + title.replace(/"/g, '') + '" allow="camera; microphone; geolocation"></iframe>';
      m.classList.add('open');
    }}
    function closeJotFormModal() {{
      var m = document.getElementById('jfModal');
      var body = document.getElementById('jfModalBody');
      if (m) m.classList.remove('open');
      if (body) body.innerHTML = '';
    }}
    function notifyParentHeight() {{
      try {{
        if (window.parent && window.parent !== window) {{
          var h = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);
          window.parent.postMessage({{ type: 'acp-embed-resize', height: h }}, '*');
        }}
      }} catch (e) {{}}
    }}
    (function() {{
      if (window.location.search.indexOf('embed=true') !== -1) {{
        document.body.classList.add('is-embedded');
      }}
      if (typeof ResizeObserver !== 'undefined') {{
        var ro = new ResizeObserver(notifyParentHeight);
        ro.observe(document.body);
      }}
      window.addEventListener('load', notifyParentHeight);
    }})();
  </script>"""

def render_smart_wizard(default_sparte: str = "Unfall & Hagel / Glasschaden", default_cat: str = "Unfallschaden", source_page: str = "schaden-kontakt.html", heading: str = "Schadenmeldung in 60 Sekunden", sub: str = "In 60 Sekunden zur strukturierten Meldung inklusive 1-Seiten-Auftrags-PDF und direkter Zuweisung an Ihre Ansprechperson in Oftringen.", show_extra_vehicle: bool = True) -> str:
    sparten_opts = [
        ("Unfall & Hagel / Glasschaden", "Unfallschaden", "Unfall & Carrosserie", "Javier Jimenez · Richtbank & Originalteile"),
        ("Hagelschaden 2026", "Hagelschaden", "Hagelschaden 2026", "Javier Jimenez · Versicherungs-Check inklusive"),
        ("Glasschaden & Sofort-Rückruf", "Glasschaden", "Glas & Frontscheibe", "Andrea Heimgartner · 1 Tag Gratis-Ersatzwagen"),
        ("Autobeschriftung & Folierung", "Beschriftung / Folierung", "Beschriftung & folioCar®", "Fabienne Zingg · Flotten, Design & Lackschutz"),
        ("Classic Cars", "Classic Cars / Oldtimer", "Classic Cars", "Thomas Hauser · Besichtigung, Ankauf, YellowFox"),
        ("Karriere / Bewerbung", "Kurzbewerbung", "Karriere / Bewerbung", "Daniela Dähler · HR Oftringen"),
    ]
    tiles_html = "\n".join(
        f'''<button type="button" class="wp-tile-btn {"selected" if sp == default_sparte else ""}" data-sparte="{esc(sp)}" data-cat="{esc(cat)}" onclick="wpSelectSparte(this)">
            <span class="wp-tile-title">{esc(title)}</span>
            <span class="wp-tile-sub">{esc(hint)}</span>
          </button>'''
        for sp, cat, title, hint in sparten_opts
    )
    vehicle_fields = """
            <div class="wp-field">
              <label for="wpVehicle" class="wp-label">Fahrzeug-Marke &amp; Modell</label>
              <input type="text" id="wpVehicle" name="vehicle" class="form-input" placeholder="z. B. VW Golf, Volvo XC90, Flotte 12 Fahrzeuge">
            </div>
            <div class="wp-field">
              <label for="wpPlateOrIns" class="wp-label">Kontrollschild / Versicherung (optional)</label>
              <input type="text" id="wpPlateOrIns" name="insurance" class="form-input" placeholder="z. B. AG 123456 · Mobiliar">
            </div>""" if show_extra_vehicle else """
            <div class="wp-field">
              <label for="wpVehicle" class="wp-label">Gewünschte Position / Bereich</label>
              <input type="text" id="wpVehicle" name="role_interest" class="form-input" placeholder="z. B. Gestalter/in Werbetechnik EFZ">
            </div>
            <div class="wp-field">
              <label for="wpPlateOrIns" class="wp-label">Möglicher Eintritt / Pensum</label>
              <input type="text" id="wpPlateOrIns" name="availability" class="form-input" placeholder="z. B. per sofort, 30 %">
            </div>"""

    return f"""
    <div class="wp-wizard-card" id="wpSmartWizardCard">
      <div class="wp-wizard-top">
        <span class="wp-step-indicator" id="wpStepLabel">
          {ICONS["file-text"]}
          <span>Schritt 1/3: Bereich &amp; Dringlichkeit</span>
        </span>
        <div style="display:flex;gap:8px;">
          <button type="button" class="btn btn-outline btn-sm" id="wpBtnBackTop" onclick="wpGoStep(wpState.step - 1)" style="display:none;">{ICONS["chevron-left"]}<span>Zurück</span></button>
          <button type="button" class="btn btn-outline btn-sm" onclick="wpResetWizard()">Neu starten</button>
        </div>
      </div>
      <div class="wp-progress-track" aria-hidden="true">
        <div class="wp-progress-seg active" id="wpProg1"></div>
        <div class="wp-progress-seg" id="wpProg2"></div>
        <div class="wp-progress-seg" id="wpProg3"></div>
      </div>
      <h3 data-slot="wizard_title">{esc(heading)}</h3>
      <p style="font-size:0.9rem;margin-bottom:18px;" data-slot="wizard_sub">{esc(sub)}</p>

      <form id="wpLeadForm" onsubmit="return wpSubmitLead(event)" novalidate toolname="autohauser_anfrage_vorbereiten" tooldescription="Bereitet eine strukturierte Anfrage oder Schadenmeldung bei Jakob Hauser AG (autohauser) in Oftringen zur Prüfung vor.">
        <input type="text" name="website_url" id="wpHoneypot" value="" style="display:none !important;" tabindex="-1" autocomplete="off" form="wpTrapDetached">

        <!-- SCHRITT 1 -->
        <div class="wp-step-pane active" id="wpStep1">
          <p class="wp-label" style="margin-bottom:10px;">1. Welchen Bereich betrifft Ihr Anliegen?</p>
          <div class="wp-tile-grid-2">
            {tiles_html}
          </div>
          <p class="wp-label" style="margin-bottom:10px;">2. Wie dringend ist Ihr Anliegen?</p>
          <div class="wp-tile-grid-2">
            <button type="button" class="wp-tile-btn selected" data-urg="Sofort-Rückruf / Schadenfall" onclick="wpSelectUrgency(this)">
              <span class="wp-tile-title">Sofort-Rückruf / Schadenfall</span>
              <span class="wp-tile-sub">Rückmeldung innert kurzer Frist oder Ersatzwagen-Bedarf</span>
            </button>
            <button type="button" class="wp-tile-btn" data-urg="Planbar / Offerte &amp; Termin" onclick="wpSelectUrgency(this)">
              <span class="wp-tile-title">Planbar / Offerte &amp; Termin</span>
              <span class="wp-tile-sub">Besichtigung, Flotten-Offerte oder Classic-Beratung</span>
            </button>
          </div>
          <div style="display:flex;justify-content:flex-end;">
            <button type="button" class="btn btn-primary" onclick="wpGoStep(2)"><span>Weiter zu Fotos &amp; Details</span>{ICONS["arrow-right"]}</button>
          </div>
        </div>

        <!-- SCHRITT 2 -->
        <div class="wp-step-pane" id="wpStep2">
          <div class="wp-form-grid">
            {vehicle_fields}
            <div class="wp-field wp-field-full">
              <label for="wpMessage" class="wp-label">Kurzbeschreibung (Schadenbild, Wunschdesign oder Anliegen)</label>
              <textarea id="wpMessage" name="message" class="form-textarea" rows="3" placeholder="Beschreiben Sie kurz den Hergang, die betroffene Fahrzeugseite oder Ihr Projekt..."></textarea>
            </div>
            <div class="wp-field wp-field-full">
              <label for="wpPhotoInput" class="wp-label">Fotos hochladen (optional, bis zu 3 Bilder für das Auftrags-PDF)</label>
              <div class="wp-photo-drop">
                <span style="display:inline-flex;align-items:center;gap:8px;font-size:0.86rem;color:var(--text-muted);">{ICONS["camera"]}<span>Schaden-, Fahrzeug- oder Detailfotos direkt anhängen</span></span>
                <label class="btn btn-outline btn-sm" style="cursor:pointer;">
                  <span>Fotos wählen</span>
                  <input type="file" id="wpPhotoInput" accept="image/*" multiple style="display:none;" onchange="wpHandlePhotos(this.files)">
                </label>
              </div>
              <div class="wp-photo-thumbs" id="wpPhotoThumbs"></div>
            </div>
          </div>
          <div style="display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;">
            <button type="button" class="btn btn-outline" onclick="wpGoStep(1)">{ICONS["chevron-left"]}<span>Zurück</span></button>
            <button type="button" class="btn btn-primary" onclick="wpGoStep(3)"><span>Weiter zu den Kontaktdaten</span>{ICONS["arrow-right"]}</button>
          </div>
        </div>

        <!-- SCHRITT 3 -->
        <div class="wp-step-pane" id="wpStep3">
          <div class="wp-form-grid">
            <div class="wp-field">
              <label for="wpName" class="wp-label">Vorname &amp; Nachname *</label>
              <input type="text" id="wpName" name="name" autocomplete="name" class="form-input" placeholder="Max Muster" required>
            </div>
            <div class="wp-field">
              <label for="wpCompany" class="wp-label">Firma (optional)</label>
              <input type="text" id="wpCompany" name="company" autocomplete="organization" class="form-input" placeholder="Firma AG">
            </div>
            <div class="wp-field">
              <label for="wpEmail" class="wp-label">E-Mail-Adresse *</label>
              <input type="email" id="wpEmail" name="email" autocomplete="email" class="form-input" placeholder="name@beispiel.ch" required>
            </div>
            <div class="wp-field">
              <label for="wpPhone" class="wp-label">Telefonnummer *</label>
              <input type="tel" id="wpPhone" name="phone" autocomplete="tel" class="form-input" placeholder="+41 79 000 00 00" required>
            </div>
            <div class="wp-field">
              <label for="wpPlzCity" class="wp-label">PLZ &amp; Ort</label>
              <input type="text" id="wpPlzCity" name="postal-code" autocomplete="postal-code" class="form-input" placeholder="4665 Oftringen">
            </div>
            <div class="wp-field">
              <label for="wpCallbackPref" class="wp-label">Bevorzugtes Zeitfenster</label>
              <select id="wpCallbackPref" name="callback_pref" class="wp-select">
                <option value="Vormittag (07:30–12:00)">Vormittag (07:30–12:00)</option>
                <option value="Nachmittag (13:15–17:30)">Nachmittag (13:15–17:30)</option>
                <option value="So rasch wie möglich">So rasch wie möglich</option>
              </select>
            </div>
          </div>
          <div class="wp-err-box" id="wpFormErr"></div>
          <div style="display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;align-items:center;">
            <button type="button" class="btn btn-outline" onclick="wpGoStep(2)">{ICONS["chevron-left"]}<span>Zurück</span></button>
            <button type="submit" class="btn btn-primary" id="wpSubmitBtn">
              <span id="wpSubmitBtnTxt">Meldung &amp; 1-Seiten-Auftrags-PDF jetzt erstellen</span>
              {ICONS["arrow-right"]}
            </button>
          </div>
        </div>
      </form>

      <div class="wp-result-box" id="wpResultBox" aria-live="polite">
        <div style="display:flex;align-items:center;gap:8px;color:#065f46;font-weight:800;font-size:1.02rem;margin-bottom:8px;">
          {ICONS["check"]}
          <span>Meldung erfolgreich erfasst (<span id="wpResRef">#WP-2026</span>)</span>
        </div>
        <p style="color:#0f172a;font-size:0.9rem;margin-bottom:10px;">
          <strong>Zuständig:</strong> <span id="wpResAssignee">–</span><br>
          <strong>Rückruf-Fenster:</strong> <span id="wpResWindow">–</span><br>
          <strong>Vorschau-Schutzmodus:</strong> Die E-Mail inkl. 1-Seiten-Auftrags-PDF wurde im sicheren Vorschau-Modus direkt an Ihre angegebene Test-Adresse gesendet.
        </p>
        <div style="display:flex;flex-wrap:wrap;gap:10px;">
          <a href="#" id="wpResPdfUrl" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">{ICONS["download"]}<span>1-Seiten-Auftrags-PDF öffnen</span></a>
          <button type="button" class="btn btn-outline btn-sm" onclick="wpResetWizard()">Neue Meldung erfassen</button>
        </div>
      </div>
    </div>
    <script>
      var wpState = {{
        step: 1,
        sparte: {json.dumps(default_sparte, ensure_ascii=False)},
        category: {json.dumps(default_cat, ensure_ascii=False)},
        urgency: "Sofort-Rückruf / Schadenfall",
        photos: []
      }};
      function wpSelectSparte(btn) {{
        var all = document.querySelectorAll('[data-sparte]');
        for (var i = 0; i < all.length; i++) all[i].classList.remove('selected');
        btn.classList.add('selected');
        wpState.sparte = btn.getAttribute('data-sparte');
        wpState.category = btn.getAttribute('data-cat');
      }}
      function wpSelectUrgency(btn) {{
        var all = document.querySelectorAll('[data-urg]');
        for (var i = 0; i < all.length; i++) all[i].classList.remove('selected');
        btn.classList.add('selected');
        wpState.urgency = btn.getAttribute('data-urg');
      }}
      function wpGoStep(n) {{
        if (n < 1) n = 1;
        if (n > 3) n = 3;
        wpState.step = n;
        for (var i = 1; i <= 3; i++) {{
          var p = document.getElementById('wpStep' + i);
          var seg = document.getElementById('wpProg' + i);
          if (p) p.classList.toggle('active', i === n);
          if (seg) seg.classList.toggle('active', i <= n);
        }}
        var lbl = document.getElementById('wpStepLabel');
        var back = document.getElementById('wpBtnBackTop');
        var titles = ['Schritt 1/3: Bereich & Dringlichkeit', 'Schritt 2/3: Details & Fotos', 'Schritt 3/3: Ihre Kontaktdaten'];
        if (lbl) lbl.querySelector('span').textContent = titles[n - 1];
        if (back) back.style.display = n > 1 ? 'inline-flex' : 'none';
        notifyParentHeight();
      }}
      function wpSetPreset(sparte, cat, urg) {{
        var btns = document.querySelectorAll('[data-sparte]');
        for (var i = 0; i < btns.length; i++) {{
          if (btns[i].getAttribute('data-sparte') === sparte) wpSelectSparte(btns[i]);
        }}
        if (urg) {{
          var ubtns = document.querySelectorAll('[data-urg]');
          for (var j = 0; j < ubtns.length; j++) {{
            if (ubtns[j].getAttribute('data-urg').indexOf(urg) !== -1) wpSelectUrgency(ubtns[j]);
          }}
        }}
      }}
      function wpHandlePhotos(files) {{
        if (!files || !files.length) return;
        Array.prototype.slice.call(files, 0, 3 - wpState.photos.length).forEach(function(file) {{
          var reader = new FileReader();
          reader.onload = function(ev) {{
            var img = new Image();
            img.onload = function() {{
              var maxW = 1200;
              var scale = img.width > maxW ? maxW / img.width : 1;
              var c = document.createElement('canvas');
              c.width = Math.round(img.width * scale);
              c.height = Math.round(img.height * scale);
              c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
              wpState.photos.push(c.toDataURL('image/jpeg', 0.8));
              wpRenderPhotos();
            }};
            img.src = ev.target.result;
          }};
          reader.readAsDataURL(file);
        }});
      }}
      function wpRenderPhotos() {{
        var wrap = document.getElementById('wpPhotoThumbs');
        if (!wrap) return;
        wrap.innerHTML = '';
        wpState.photos.forEach(function(src, idx) {{
          var d = document.createElement('div');
          d.className = 'wp-photo-thumb';
          d.innerHTML = '<img src="' + src + '" alt="Upload ' + (idx+1) + '"><button type="button" class="wp-photo-rm" onclick="wpRemovePhoto(' + idx + ')">×</button>';
          wrap.appendChild(d);
        }});
        notifyParentHeight();
      }}
      function wpRemovePhoto(idx) {{
        wpState.photos.splice(idx, 1);
        wpRenderPhotos();
      }}
      function wpResetWizard() {{
        var f = document.getElementById('wpLeadForm');
        var r = document.getElementById('wpResultBox');
        var e = document.getElementById('wpFormErr');
        if (f) {{ f.reset(); f.style.display = 'block'; }}
        if (r) r.style.display = 'none';
        if (e) e.style.display = 'none';
        wpState.photos = [];
        wpRenderPhotos();
        wpGoStep(1);
      }}
      function wpSubmitLead(ev) {{
        if (ev) ev.preventDefault();
        var name = (document.getElementById('wpName').value || '').trim();
        var email = (document.getElementById('wpEmail').value || '').trim();
        var phone = (document.getElementById('wpPhone').value || '').trim();
        var company = (document.getElementById('wpCompany').value || '').trim();
        var plzCity = (document.getElementById('wpPlzCity').value || '').trim();
        var cbPref = (document.getElementById('wpCallbackPref').value || '').trim();
        var vehicle = (document.getElementById('wpVehicle').value || '').trim();
        var ins = (document.getElementById('wpPlateOrIns').value || '').trim();
        var msg = (document.getElementById('wpMessage').value || '').trim();
        var hp = (document.getElementById('wpHoneypot').value || '').trim();
        var err = document.getElementById('wpFormErr');
        if (err) err.style.display = 'none';

        if (!name || (!email && !phone)) {{
          wpGoStep(3);
          if (err) {{
            err.textContent = 'Bitte geben Sie Ihren Namen sowie E-Mail oder Telefonnummer an.';
            err.style.display = 'block';
          }}
          return false;
        }}
        var btn = document.getElementById('wpSubmitBtn');
        var btnTxt = document.getElementById('wpSubmitBtnTxt');
        if (btn) btn.disabled = true;
        if (btnTxt) btnTxt.textContent = 'Auftrags-PDF wird erstellt...';

        fetch('/api/lead-submit', {{
          method: 'POST',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify({{
            client_slug: 'autohauser',
            source_page: {json.dumps(f"preview-autohauser/{source_page}")},
            website_url: hp,
            category: wpState.category,
            sparte: wpState.sparte,
            urgency: wpState.urgency,
            name: name,
            company: company,
            plz: plzCity,
            email: email,
            phone: phone,
            callback_pref: cbPref,
            message: msg,
            extra_fields: {{
              'Fahrzeug / Position': vehicle || 'Keine Angabe',
              'Schild / Versicherung / Pensum': ins || 'Keine Angabe'
            }},
            photos: wpState.photos,
            self_test_mode: true
          }})
        }})
        .then(function(r) {{ return r.json(); }})
        .then(function(res) {{
          if (btn) btn.disabled = false;
          if (btnTxt) btnTxt.textContent = 'Meldung & 1-Seiten-Auftrags-PDF jetzt erstellen';
          if (!res || !res.ok) {{
            if (err) {{
              err.textContent = (res && res.error) ? res.error : 'Übermittlung fehlgeschlagen.';
              err.style.display = 'block';
            }}
            return;
          }}
          document.getElementById('wpLeadForm').style.display = 'none';
          document.getElementById('wpResRef').textContent = res.ref_code || '#WP-2026';
          document.getElementById('wpResAssignee').textContent = res.assigned_to || 'autohauser Team';
          document.getElementById('wpResWindow').textContent = res.callback_window || 'Zeitnah';
          var pdfA = document.getElementById('wpResPdfUrl');
          if (pdfA) pdfA.href = res.pdf_url || '#';
          document.getElementById('wpResultBox').style.display = 'block';
          notifyParentHeight();
        }})
        .catch(function() {{
          if (btn) btn.disabled = false;
          if (btnTxt) btnTxt.textContent = 'Meldung & 1-Seiten-Auftrags-PDF jetzt erstellen';
          if (err) {{
            err.textContent = 'Netzwerkfehler. Bitte versuchen Sie es direkt telefonisch über 0800 875 875.';
            err.style.display = 'block';
          }}
        }});
        return false;
      }}
    </script>"""

# Categorize the 26 Ratgeber articles + map to best matching local PDF
RATGEBER_META = {
    "rat-mehr-rechte": ("Unfall & Recht", "25-sie-haben-mehr-rechte-als-sie-glauben.pdf"),
    "rat-schlafende-hunde": ("Versicherung", "31-unsere-berattung-kann-fuer-sie-bares-geld-wert-sein.pdf"),
    "rat-hp-ohne-schuld": ("Unfall & Recht", "38-haftpflichtschaden-ohne-schuldige.pdf"),
    "rat-vollkasko": ("Versicherung", "04-wie-lange-macht-eine-vollkasko-sinn.pdf"),
    "rat-ebike-auto": ("Velo & Haftpflicht", "12-bei-unfall-mit-velo-gilt-die-gefaehrdungshaftung.pdf"),
    "rat-so-erfuellen-sie-die-schadenminderungspflicht": ("Unfall & Recht", "11-was-ist-die-schadenminderungspflicht.pdf"),
    "rat-ihre-sicherheit-ist-ihr-gutes-recht": ("Unfall & Recht", "39-keine-kompromisse-bei-ihrer-sicherheit.pdf"),
    "rat-kleiner-kratzer-grosser-aufwand": ("Unfall & Recht", "32-kleiner-kratzer-grosser-aufwand.pdf"),
    "rat-das-schnelle-geld--lassen-sie-es-sein-": ("Versicherung", "22-verfallen-sie-im-totalschaden-nicht-dem-lockruf-des-geldes.pdf"),
    "rat-parkschaden": ("Hagel & Glas", "16-was-ist-eine-parkschadenversicherung.pdf"),
    "rat-hagel": ("Hagel & Glas", "05-hagelschaden-was-nun.pdf"),
    "rat-vertrauensmissbrauch": ("Unfall & Recht", "43-krasser-fall-von-vertrauensmissbrauch.pdf"),
    "rat-lockruf": ("Versicherung", "22-verfallen-sie-im-totalschaden-nicht-dem-lockruf-des-geldes.pdf"),
    "rat-gefaehrdungshaftung": ("Velo & Haftpflicht", "12-bei-unfall-mit-velo-gilt-die-gefaehrdungshaftung.pdf"),
    "rat-kein-aerger-bei-der-autorueckgabe": ("Leasing & Occasion", "10-kein-aerger-bei-der-rueckgabe-des-leasingfahrzeuges.pdf"),
    "rat-haftpflichtschaden-ohne-schuldige-": ("Unfall & Recht", "38-haftpflichtschaden-ohne-schuldige.pdf"),
    "rat-im-auftrag-und-interesse-des-kunden": ("Unfall & Recht", "30-im-auftrag-und-interesse-des-kunden.pdf"),
    "rat-auto-versichern--mit-vernunft": ("Versicherung", "47-eine-gute-kasko-heisst-gute-leistungen-im-schadenfall.pdf"),
    "rat-schnelles-geld": ("Versicherung", "45-was-wir-im-totalschaden-fuer-sie-tun-koennen.pdf"),
    "rat-occasion": ("Leasing & Occasion", "41-moegliche-folgen-unkorrekter-instandstellung.pdf"),
    "rat-frontscheibe": ("Hagel & Glas", "01-frontscheibe-ist-mittragendes-strukturteil.pdf"),
    "rat-hat-nichts-gemacht": ("Unfall & Recht", "07-wie-verhalte-ich-mich-bei-einem-unfall-richtig.pdf"),
    "rat-wer-wahrt-ihre-interessen-im-schadenfall-": ("Unfall & Recht", "03_rg_wer_repariert_mein_auto.pdf"),
    "rat-wie-lange-macht-vollkaskodeckung-sinn-": ("Versicherung", "04-wie-lange-macht-eine-vollkasko-sinn.pdf"),
    "rat-finanzielle-risiken-eines-velofahrers": ("Velo & Haftpflicht", "09-regress-nach-unfall-mit-einem-fussgaenger.pdf"),
    "rat-unklares-verschulden--und-jetzt-": ("Unfall & Recht", "36-kein-kuhhandel-im-haftplichtschaden.pdf"),
}

def build_pages(out_dir: Path, scraped: dict, dims: dict, pdfs: list, pdf_meta: dict, show_cockpit: bool):
    out_dir.mkdir(parents=True, exist_ok=True)
    rg_dir = out_dir / "ratgeber"
    rg_dir.mkdir(parents=True, exist_ok=True)

    # 1. index.html (Unfallreparatur & Carrosserie)
    index_html = f"""{render_head("autohauser® – Unfallreparatur, Hagelschaden & Carrosserie Oftringen", "Jakob Hauser AG (autohauser®) in Oftringen: Unfallinstandstellung nach Herstellervorgabe, Hagelschaden 2026, Glasschaden, Autobeschriftung und Classic Cars seit 1948.", canonical_page="index.html")}
<body>
{render_header("unfall", "unfall", dims, show_cockpit=show_cockpit)}

<main>
  <section class="hero-section" data-section="hero">
    <div class="container">
      <div class="hero-grid">
        <div>
          <div>
            <span class="section-kicker" data-slot="hero_kicker">CARROSSERIE &amp; UNFALLINSTANDSTELLUNG · OFTRINGEN</span>
            <h1 data-slot="hero_h1">Unfall- oder Hagelschaden? Makellos repariert nach Herstellervorgabe.</h1>
            <p class="hero-lead" data-slot="hero_sub">
              Seit 1948 steht die Jakob Hauser AG unter der Marke autohauser® für kompromisslose Qualität mit Originalersatzteilen, digitaler Farbmessung, eigenen Ersatzwagen und lebenslanger Swissgarant-Garantie – unabhängig von Versicherungsvorgaben.
            </p>
            <div class="hero-actions">
              <a href="#smart-schaden" class="btn btn-primary btn-cta"><span>Schadenmeldung starten</span>{ICONS["arrow-right"]}</a>
              <a href="tel:0800875875" class="btn btn-outline">{ICONS["phone"]}<span class="tabular">Gratis-Hotline: 0800 875 875</span></a>
            </div>
          </div>
          <div class="hero-metrics">
            <div class="metric-box">
              <div class="metric-val tabular">Seit 1948</div>
              <div class="metric-lbl">Traditionsbetrieb in Oftringen / Zofingen</div>
            </div>
            <div class="metric-box">
              <div class="metric-val">Lebenslange Garantie</div>
              <div class="metric-lbl">Swissgarant-Zertifikat auf alle Arbeiten</div>
            </div>
            <div class="metric-box">
              <div class="metric-val tabular">15 Ersatzwagen</div>
              <div class="metric-lbl">12 Personen- und 3 Lieferwagen bereit</div>
            </div>
            <div class="metric-box">
              <div class="metric-val tabular">0800 875 875</div>
              <div class="metric-lbl">24-Stunden-Service gratis erreichbar</div>
            </div>
          </div>
        </div>
        <div class="hero-media-card">
          {img_tag(dims, "volvo_xc90_hagelschaden_1600x650.png", "autohauser Unfall- und Hagelinstandstellung Oftringen", css_class="hero-media-img", is_hero=True)}
          <div class="hero-media-body">
            <div>
              <span class="meta-badge" style="margin-bottom:8px;">Ihre Interessen zuerst</span>
              <h3 style="margin-bottom:6px;">Unabhängig von Schadensteuerung</h3>
              <p style="font-size:0.9rem;margin-bottom:0;">Wir sind keiner Versicherung verpflichtet und reparieren Ihr Fahrzeug ausschliesslich nach Herstellervorgabe mit Originalteilen.</p>
            </div>
            <div class="hero-contact-strip">
              <span style="font-weight:700;color:var(--text-main);">Äussere Luzernerstr. 12, Oftringen</span>
              <a href="schaden-kontakt.html" style="font-weight:700;">Alle Kontaktwege</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 3 SPARTEN PORTAL -->
  <section class="section section-alt" data-section="sparten">
    <div class="container">
      <div class="section-head">
        <span class="section-kicker">DREI KOMPETENZEN UNTER EINEM DACH</span>
        <h2>Ein Betrieb in Oftringen, drei spezialisierte Welten</h2>
        <p>Ob moderner Unfallschaden, professionelle Fahrzeugflotte oder seltener Klassiker: Alle drei Sparten arbeiten mit derselben handwerklichen Präzision Hand in Hand.</p>
      </div>
      <div class="grid-3">
        <div class="card service-card">
          <div>
            <div class="sparte-logo-wrap">{img_tag(dims, "unfallreparatur_logo.png", "autohauser Unfallreparaturen Logo")}</div>
            <h3>Unfall, Hagel &amp; Glas</h3>
            <p>Karosserie-Richtbank, Lackiererei mit digitaler Farbmessung, Hagelschaden-Zentrum, Frontscheiben-Ersatz und komplettes Schadenmanagement.</p>
          </div>
          <a href="schaden-kontakt.html" class="btn btn-outline"><span>Zur Schaden-Zentrale</span>{ICONS["arrow-right"]}</a>
        </div>
        <div class="card service-card">
          <div>
            <div class="sparte-logo-wrap">{img_tag(dims, "autobeschriftung_logo.png", "autohauser Autobeschriftung Logo")}</div>
            <h3>Autobeschriftung &amp; folioCar®</h3>
            <p>Flottenbranding von 3 bis 500 Fahrzeugen, Premium-Vollfolierung mit 100µ Q4-Folie, Steinschlagschutz und Sondermodelle für Autoimporteure.</p>
          </div>
          <a href="beschriftung.html" class="btn btn-outline"><span>Zur Sparte Beschriftung</span>{ICONS["arrow-right"]}</a>
        </div>
        <div class="card service-card">
          <div>
            <div class="sparte-logo-wrap">{img_tag(dims, "classiccars_logo.png", "autohauser Classic Cars Logo")}</div>
            <h3>Classic Cars &amp; YellowFox®</h3>
            <p>Unrestaurierte und restaurierte Klassiker (Alfa Romeo 2000 GTV, Fiat 124 Abarth), Ankauf, Konsignation, Fahrzeugsuche und Diebstahlschutz.</p>
          </div>
          <a href="classics.html" class="btn btn-outline"><span>Zur Sparte Classic Cars</span>{ICONS["arrow-right"]}</a>
        </div>
      </div>
    </div>
  </section>

  <!-- LEISTUNGEN -->
  <section class="section" data-section="leistungen">
    <div class="container">
      <div class="section-head">
        <span class="section-kicker">UNFALL- &amp; CARROSSERIE-KOMPETENZ</span>
        <h2>Jeder Schadenfall fachgerecht und sicher gelöst</h2>
        <p>Von der Struktur-Richtbank über den Steinschlag in der Frontscheibe bis zur direkten Abklärung mit Ihrer Versicherung.</p>
      </div>
      <div class="grid-2">
        <div class="card feature-card">
          <div>
            <div class="card-badge-row" style="margin-bottom:10px;">
              <span class="icon-box">{ICONS["wrench"]}</span>
              <span class="meta-badge">Herstellervorgaben</span>
            </div>
            <h3>Unfallinstandstellung &amp; Richtbank</h3>
            <p>Fahrzeugvermessung, Struktur-Richtarbeiten, eigene Lackiererei mit digitaler Farbmessung und ausschliesslich Originalersatzteile des Fahrzeugherstellers.</p>
            <ul class="list-check">
              <li>{ICONS["check"]}<span>Erhalt der vollen Fahrzeugsicherheit &amp; Werksgarantie</span></li>
              <li>{ICONS["check"]}<span>Kein Eintauschverlust bei späterem Verkauf</span></li>
            </ul>
          </div>
          <a href="schaden-kontakt.html" class="btn btn-outline btn-sm"><span>Unfallschaden melden</span>{ICONS["arrow-right"]}</a>
        </div>
        <div class="card feature-card">
          <div>
            <div class="card-badge-row" style="margin-bottom:10px;">
              <span class="icon-box">{ICONS["cloud-rain"]}</span>
              <span class="meta-badge">Hagel-Spezialist 2026</span>
            </div>
            <h3>Hagelschaden 2026</h3>
            <p>Kommen Sie direkt zu uns statt ins Versicherungs-Drive-In. Wir klären vorab transparent, ob Ihre Versicherung ohne Einschränkungen zu unseren Konditionen übernimmt.</p>
            <ul class="list-check">
              <li>{ICONS["check"]}<span>Hinweis zu Generali &amp; Vaudoise: transparente Voraus-Klärung</span></li>
              <li>{ICONS["check"]}<span>Differenzübernahme bei begleitetem Versicherungswechsel</span></li>
            </ul>
          </div>
          <a href="schaden-kontakt.html?tab=hagel" class="btn btn-outline btn-sm"><span>Hagelschaden 2026 melden</span>{ICONS["arrow-right"]}</a>
        </div>
        <div class="card feature-card">
          <div>
            <div class="card-badge-row" style="margin-bottom:10px;">
              <span class="icon-box">{ICONS["shield"]}</span>
              <span class="meta-badge">Strukturteil Frontscheibe</span>
            </div>
            <h3>Glasschaden &amp; Frontscheiben-Ersatz</h3>
            <p>Die Frontscheibe trägt zur Torsionssteifigkeit bei und stützt den Beifahrer-Airbag. Wir prüfen objektiv, ob Reparatur oder Ersatz die sicherere Lösung ist.</p>
            <ul class="list-check">
              <li>{ICONS["check"]}<span>1 Tag kostenloser Ersatzwagen beim Scheibenersatz</span></li>
              <li>{ICONS["check"]}<span>Kostenlose Innenreinigung und Versicherungsabklärung inklusive</span></li>
            </ul>
          </div>
          <a href="schaden-kontakt.html?tab=glas" class="btn btn-outline btn-sm"><span>Glas-Rückruf anfordern</span>{ICONS["arrow-right"]}</a>
        </div>
        <div class="card feature-card">
          <div>
            <div class="card-badge-row" style="margin-bottom:10px;">
              <span class="icon-box">{ICONS["car"]}</span>
              <span class="meta-badge">Mobilitätsgarantie</span>
            </div>
            <h3>Parkschaden &amp; 15 Ersatzfahrzeuge</h3>
            <p>Ob fremdverursachter Parkschaden, Kasko oder Haftpflicht: Wir prüfen Ihre Police auf die günstigste Abwicklung und halten Sie mit 12 PW und 3 Lieferwagen mobil.</p>
            <ul class="list-check">
              <li>{ICONS["check"]}<span>Wahl aus 12 Personenwagen und 3 Lieferwagen</span></li>
              <li>{ICONS["check"]}<span>Rundum-Betreuung von der Bergung bis zur Auslieferung</span></li>
            </ul>
          </div>
          <a href="schaden-kontakt.html" class="btn btn-outline btn-sm"><span>Termin &amp; Ersatzwagen anfragen</span>{ICONS["arrow-right"]}</a>
        </div>
      </div>
    </div>
  </section>

  <!-- WARUM AUTOHAUSER + SWISSGARANT -->
  <section class="section section-alt" data-section="qualitaet">
    <div class="container">
      <div class="grid-2" style="align-items:center;">
        <div>
          <span class="section-kicker">UNABHÄNGIGKEIT &amp; GARANTIE</span>
          <h2>Warum Sie als Kunde bei autohauser® am besten fahren</h2>
          <p>Gewisse Versicherer versuchen im Schadenfall, Geschädigte in gebundene Partnerbetriebe zu lenken. Als unabhängiger Fachbetrieb wahren wir ausschliesslich Ihre Interessen und stehen mit lebenslanger Garantie hinter jeder Reparatur.</p>
          <ul class="list-check" style="margin-bottom:20px;">
            <li>{ICONS["check"]}<span><strong>100 % Originalersatzteile:</strong> Keine Kompromisse bei Passgenauigkeit und Crash-Sicherheit</span></li>
            <li>{ICONS["check"]}<span><strong>Lebenslange Swissgarant-Garantie:</strong> Gilt sogar nach dem Verkauf Ihres Fahrzeugs weiter</span></li>
            <li>{ICONS["check"]}<span><strong>Digitale Farbmessung:</strong> Exakter Farbton auch bei anspruchsvollen Metallic-Lacken</span></li>
            <li>{ICONS["check"]}<span><strong>Eigene Schadenmanager:</strong> Direkte Vertretung Ihrer Ansprüche gegenüber der Versicherung</span></li>
          </ul>
          <a href="assets/pdfs/zertifikat-swissgrant-2017.pdf" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">{ICONS["download"]}<span>Swissgarant-Zertifikat (PDF)</span></a>
        </div>
        <div class="card content-card">
          {img_tag(dims, "dsc_5262.jpeg", "autohauser Werkstatt und Fachbetrieb Oftringen", css_class="card-img-top")}
          <div style="display:flex;align-items:center;gap:14px;">
            {img_tag(dims, "logo-swissgarant.jpeg", "IG Swissgarant Mitglied", extra_style="height:46px;width:auto;object-fit:contain;")}
            <div>
              <h3 style="margin-bottom:4px;">Geprüfter Swissgarant-Betrieb</h3>
              <p style="font-size:0.86rem;margin:0;">Dokumentierte Arbeitsprozesse, modernste Fügetechniken und volle Garantie gemäss Swissgarant-Bestimmungen.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SMART-SCHADENASSISTENT DIREKT AUF STARTSEITE -->
  <section class="section" id="smart-schaden" data-section="smart-assistent">
    <div class="container">
      <div class="section-head">
        <span class="section-kicker">SCHNELL-MELDUNG &amp; FOTO-UPLOAD · OFTRINGEN</span>
        <h2>Schaden oder Anfrage in 60 Sekunden direkt melden</h2>
        <p>Schluss mit toten Altformularen: Wählen Sie Ihren Bereich, laden Sie auf Wunsch bis zu 3 Fotos hoch und erhalten Sie sofort ein strukturiertes 1-Seiten-Auftrags-PDF.</p>
      </div>
      {render_smart_wizard("Unfall & Hagel / Glasschaden", "Unfallschaden", "index.html")}
    </div>
  </section>

  <!-- KUNDENSTIMMEN & RATGEBER-TEASER -->
  <section class="section section-alt" data-section="stimmen">
    <div class="container">
      <div class="section-head">
        <span class="section-kicker">ECHTE KUNDENMEINUNGEN &amp; WISSEN</span>
        <h2>Erfahrungen unserer Kundinnen und Kunden</h2>
      </div>
      <div class="grid-2" style="margin-bottom:32px;">
        <div class="card content-card stimme-card">
          <div class="stimme-header-row" style="display:flex;gap:16px;align-items:flex-start;">
            {img_tag(dims, "iwan-hunziker_2.jpeg", "Iwan Hunziker mit seinem reparierten Suzuki SX4", extra_style="width:84px;height:84px;object-fit:cover;border-radius:8px;flex-shrink:0;")}
            <div>
              <h3 style="margin-bottom:4px;">«Bei einem Carrosserieschaden gibt es für mich nur autohauser»</h3>
              <p style="font-size:0.84rem;margin:0;">Iwan Hunziker, Oftringen · Suzuki SX4 Parkschaden</p>
            </div>
          </div>
          <p style="margin:0;">Nach einem Parkschaden am Kotflügel beim Perry Center in Oftringen stellte autohauser den Wagen makellos instand: «Da war einfach alles perfekt gemacht. Ich kann autohauser jederzeit weiterempfehlen.»</p>
        </div>
        <div class="card content-card stimme-card">
          <div class="stimme-header-row" style="display:flex;gap:16px;align-items:flex-start;">
            {img_tag(dims, "dsc_4668klein.jpeg", "Christian Guidi Porsche GT3 RS Steinschlagschutz", extra_style="width:84px;height:84px;object-fit:cover;border-radius:8px;flex-shrink:0;")}
            <div>
              <h3 style="margin-bottom:4px;">Porsche GT3 RS Steinschlagschutz</h3>
              <p style="font-size:0.84rem;margin:0;">Christian Guidi · Frontpartie Steinschlagschutz-Folie</p>
            </div>
          </div>
          <p style="margin:0;">Stossstange, Kotflügel, Haube, A-Säulen und Aussenspiegel mit selbstheilender Steinschlagschutz-Folie präzise geschützt – sauber montiert ohne Schnittspuren auf dem Lack.</p>
        </div>
      </div>
      <div class="card" style="background:var(--navy);color:#ffffff;border-color:var(--navy);flex-direction:row;flex-wrap:wrap;align-items:center;justify-content:space-between;">
        <div>
          <span class="section-kicker" style="color:#7dd3fc;">26 RATGEBER-BEITRÄGE &amp; 72 PDF-MERKBLÄTTER</span>
          <h3 style="color:#ffffff;margin-bottom:4px;">Kennen Sie Ihre Rechte nach einem Unfall oder Hagelschaden?</h3>
          <p style="color:#cbd5e1;margin:0;">Freie Werkstattwahl, Schadenminderungspflicht, Totalschaden-Lockruf, Vollkasko und Leasingrückgabe verständlich erklärt.</p>
        </div>
        <a href="ratgeber.html" class="btn btn-primary"><span>Alle 26 Ratgeber &amp; PDFs öffnen</span>{ICONS["arrow-right"]}</a>
      </div>
    </div>
  </section>
</main>

{render_footer(show_cockpit=show_cockpit)}
</body>
</html>"""

    # 2. beschriftung.html
    beschriftung_html = f"""{render_head("Autobeschriftung, Flottenbranding & folioCar® – autohauser®", "Fahrzeugbeschriftung, Teil- und Vollfolierung, Lackschutz und Sondermodelle für Autoimporteure in Oftringen. Mit folioCar® 100µ Q4-Folie.", canonical_page="beschriftung.html")}
<body>
{render_header("beschriftung", "beschriftung", dims, show_cockpit=show_cockpit)}

<main>
  <section class="hero-section" data-section="hero-beschriftung">
    <div class="container">
      <div class="hero-grid">
        <div>
          <div>
            <span class="section-kicker">AUTOBESCHRIFTUNG &amp; FOLIOCAR® WERBETECHNIK</span>
            <h1>Fahrzeugdesign, das funktioniert – von 3 bis 500 Fahrzeugen.</h1>
            <p class="hero-lead">
              autohauser® beschäftigt sich exklusiv mit Fahrzeugoberflächen. Als Generalimporteur von folioCar® und Carrosseriebetrieb mit eigener Lackiererei beherrschen wir Flottenbranding, Vollfolierung, Lackschutz und Sondermodelle aus einer Hand.
            </p>
            <div class="hero-actions">
              <a href="#beschriftung-anfrage" class="btn btn-primary btn-cta"><span>Beschriftung anfragen</span>{ICONS["arrow-right"]}</a>
              <a href="tel:+41627893352" class="btn btn-outline">{ICONS["phone"]}<span class="tabular">+41 62 789 33 52</span></a>
            </div>
          </div>
          <div class="hero-metrics">
            <div class="metric-box">
              <div class="metric-val">100 % Fahrzeug-Fokus</div>
              <div class="metric-lbl">Einziger reiner Fahrzeug-Werbetechniker der CH</div>
            </div>
            <div class="metric-box">
              <div class="metric-val tabular">100µ Q4-Folie</div>
              <div class="metric-lbl">Über 100 Farbtöne &amp; rückstandslose Rückrüstung</div>
            </div>
            <div class="metric-box">
              <div class="metric-val">1:1 Prototyp</div>
              <div class="metric-lbl">Gut zur Produktion vor Flotten-Rollout</div>
            </div>
            <div class="metric-box">
              <div class="metric-val">Eigene Lackiererei</div>
              <div class="metric-lbl">Null Schneideschäden auf dem Originallack</div>
            </div>
          </div>
        </div>
        <div class="hero-media-card">
          {img_tag(dims, "hauser-789breit.jpeg", "autohauser Fahrzeugbeschriftung und Folierung Oftringen", css_class="hero-media-img", is_hero=True)}
          <div class="hero-media-body">
            <div>
              <span class="meta-badge" style="margin-bottom:8px;">Terminvereinbarung &amp; Beratung</span>
              <h3 style="margin-bottom:6px;">Persönliche Beratung durch Fabienne Zingg</h3>
              <p style="font-size:0.9rem;margin-bottom:0;">Wegen hoher Auslastung empfangen wir Besucherinnen und Besucher ausschliesslich nach vorgängiger Terminvereinbarung.</p>
            </div>
            <div class="hero-contact-strip">
              <a href="mailto:fabienne.zingg@autohauser.ch" style="font-weight:700;">fabienne.zingg@autohauser.ch</a>
              <a href="#spezial-formulare" style="font-weight:700;">Bestellformulare</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- LEISTUNGEN BESCHRIFTUNG -->
  <section class="section section-alt" data-section="beschriftung-leistungen">
    <div class="container">
      <div class="section-head">
        <span class="section-kicker">UNSER LEISTUNGSANGEBOT</span>
        <h2>Erfolgreiches Autodesign ist planbar</h2>
        <p>Von der Design-Kreation durch erfahrene Autodesigner bis zum mobilen Rollout Ihrer gesamten Firmenflotte.</p>
      </div>
      <div class="grid-2">
        <div class="card service-card">
          <div>
            <div class="card-badge-row" style="margin-bottom:10px;">
              <span class="icon-box">{ICONS["layers"]}</span>
              <span class="meta-badge">3 bis 500 Fahrzeuge</span>
            </div>
            <h3>Firmenfahrzeuge &amp; Flottenbranding</h3>
            <p>Vom Logobranding im Folienschnitt bis zur Teil- oder Vollfolierung in Corporate-Farben. Wir organisieren Design, 1:1-Prototyp, Montage (auch mobil vor Ort oder im Logistikcenter) sowie Aftersales-Unfallreparaturen.</p>
          </div>
          <a href="assets/pdfs/zusammenarbeit-mit-autohauser.pdf" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">{ICONS["download"]}<span>Factsheet Zusammenarbeit (PDF)</span></a>
        </div>
        <div class="card service-card">
          <div>
            <div class="card-badge-row" style="margin-bottom:10px;">
              <span class="icon-box">{ICONS["sparkles"]}</span>
              <span class="meta-badge">Exklusiv in der Schweiz</span>
            </div>
            <h3>folioCar® Premium-Folierungen</h3>
            <p>Gemeinsam mit MACtac entwickelt: 100µ Materialdicke für besten Steinschlagschutz, hoher Glanzgrad, waschstrassentauglich und nach Jahren sauber rückrüstbar ohne Kleberrückstände auf einwandfreiem Originallack.</p>
          </div>
          <a href="assets/pdfs/6_04_02_infos_zur_folienbeschichtung.pdf" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">{ICONS["download"]}<span>Infos zur Folienbeschichtung (PDF)</span></a>
        </div>
        <div class="card service-card">
          <div>
            <div class="card-badge-row" style="margin-bottom:10px;">
              <span class="icon-box">{ICONS["shield"]}</span>
              <span class="meta-badge">Selbstheilend</span>
            </div>
            <h3>Lack schützen &amp; Matt-Folierung</h3>
            <p>Transparente selbstheilende Steinschlagschutz-Folie (z. B. für Sportwagen und Frontpartien) oder edle Matt- und Metallic-Beschichtungen – perfekt abgestimmt auf Karosserie-Sicken und -Mulden.</p>
          </div>
          <a href="assets/pdfs/vorgaben-druckdaten.pdf" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">{ICONS["download"]}<span>Vorgaben Druckdaten (PDF)</span></a>
        </div>
        <div class="card service-card">
          <div>
            <div class="card-badge-row" style="margin-bottom:10px;">
              <span class="icon-box">{ICONS["car"]}</span>
              <span class="meta-badge">Autoimporteure &amp; Decor</span>
            </div>
            <h3>Sondermodelle &amp; individuelles Decor</h3>
            <p>Spezielle Fahrzeugdecors abseits der Stange sowie komplette Veredelung von Serienmodellen für Autoimporteure und Leasingprovider – auf Wunsch inklusive Lackierung komplexer Anbauteile.</p>
          </div>
          <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Decor bestellen (Autohauser)', 'https://form.jotform.com/70001994754962')"><span>Decor-Formular öffnen</span>{ICONS["arrow-right"]}</button>
        </div>
      </div>
    </div>
  </section>

  <!-- REFERENZ GALERIE -->
  <section class="section" data-section="beschriftung-referenzen">
    <div class="container">
      <div class="section-head">
        <span class="section-kicker">AUSGEWÄHLTE REFERENZPROJEKTE</span>
        <h2>Echte Umsetzungen aus unserer Werkstatt in Oftringen</h2>
      </div>
      <div class="grid-3">
        <div class="card content-card">
          {img_tag(dims, "tesla-bachmann.jpeg", "Tesla Firmenbeschriftung Bachmann", css_class="card-img-top")}
          <div><h3>Tesla Flottenbranding</h3><p style="margin:0;">Präzises Corporate-Design auf Elektrofahrzeugen.</p></div>
        </div>
        <div class="card content-card">
          {img_tag(dims, "postpandas.jpeg", "Schweizerische Post Fahrzeugflotte", css_class="card-img-top")}
          <div><h3>Flotten-Rollout</h3><p style="margin:0;">Grossserien-Beschriftung mit definierter Prozesssicherheit.</p></div>
        </div>
        <div class="card content-card">
          {img_tag(dims, "mobility-smart.jpeg", "Mobility Smart Carsharing Folierung", css_class="card-img-top")}
          <div><h3>Carsharing &amp; Mobility</h3><p style="margin:0;">Wiedererkennbare Markenführung im urbanen Raum.</p></div>
        </div>
        <div class="card content-card">
          {img_tag(dims, "yf-servicemobil.jpeg", "YellowFox Servicemobil", css_class="card-img-top")}
          <div><h3>YellowFox® Servicemobil</h3><p style="margin:0;">Dynamisches Nutzfahrzeug-Branding mit Klarheit.</p></div>
        </div>
        <div class="card content-card">
          {img_tag(dims, "porsche-gt3-1.jpeg", "Porsche GT3 RS Steinschlagschutz", css_class="card-img-top")}
          <div><h3>Porsche GT3 RS Lackschutz</h3><p style="margin:0;">Selbstheilende Steinschlagschutz-Folie auf höchstem Niveau.</p></div>
        </div>
        <div class="card content-card">
          {img_tag(dims, "bmw-i8.jpeg", "BMW i8 Vollfolierung", css_class="card-img-top")}
          <div><h3>BMW i8 Individualisierung</h3><p style="margin:0;">Anspruchsvolle 3D-Geometrien faltenfrei foliert.</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SPEZIAL-JOTFORMS (LAZY MODAL) -->
  <section class="section section-alt" id="spezial-formulare" data-section="beschriftung-jotforms">
    <div class="container">
      <div class="section-head">
        <span class="section-kicker">SPEZIAL-BESTELLUNG &amp; PROJEKTERFASSUNG</span>
        <h2>Direktzugang zu den ausführlichen Fachformularen</h2>
        <p>Für wiederkehrende B2B-Prozesse öffnen sich die Spezialformulare bei Klick direkt hier im sicheren Overlay ohne lange Ladezeit.</p>
      </div>
      <div class="grid-3">
        <div class="card">
          <div>
            <h3>Firmenfahrzeuge beschriften</h3>
            <p>Ausführliche Flotten-Checkliste (30 Felder) inkl. Fahrzeugliste und Logo-Upload.</p>
          </div>
          <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Beschriften Firmenfahrzeuge', 'https://form.jotform.com/63610509063955')"><span>Formular laden</span>{ICONS["arrow-right"]}</button>
        </div>
        <div class="card">
          <div>
            <h3>Decor bestellen</h3>
            <p>Spezialformular für individuelle Streifen, Sonderdecors und Einzelanfertigungen.</p>
          </div>
          <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Decor bestellen', 'https://form.jotform.com/70001994754962')"><span>Formular laden</span>{ICONS["arrow-right"]}</button>
        </div>
        <div class="card">
          <div>
            <h3>Autoimporteure Sondermodell</h3>
            <p>Projektbriefing für Fahrzeugimporteure, Kleinserien und Sonderausstattungen.</p>
          </div>
          <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Sondermodell Autoimporteure', 'https://form.jotform.com/63581323012950')"><span>Formular laden</span>{ICONS["arrow-right"]}</button>
        </div>
      </div>
    </div>
  </section>

  <!-- SMART-PRO ANFRAGE BESCHRIFTUNG -->
  <section class="section" id="beschriftung-anfrage" data-section="beschriftung-smart">
    <div class="container">
      {render_smart_wizard("Autobeschriftung & Folierung", "Beschriftung / Folierung", "beschriftung.html", heading="Schnellanfrage Autobeschriftung & Folierung", sub="Direkt an Fabienne Zingg (Leiterin Werbetechnik) – inklusive Fahrzeugfoto-Upload und 1-Seiten-Projektblatt.")}
    </div>
  </section>
</main>

{render_footer(show_cockpit=show_cockpit)}
</body>
</html>"""

    # 3. classics.html
    classics_html = f"""{render_head("autohauser® classics – Oldtimer, Youngtimer & YellowFox®", "Toprestaurierte und unrestaurierte Klassiker (Alfa Romeo 2000 GTV, Fiat 124 Abarth), Oldtimer-Unfallinstandstellung, Ankauf, Konsignation und YellowFox Diebstahlschutz.", canonical_page="classics.html")}
<body>
{render_header("classics", "classics", dims, show_cockpit=show_cockpit)}

<main>
  <section class="hero-section" data-section="hero-classics">
    <div class="container">
      <div class="hero-grid">
        <div>
          <div>
            <span class="section-kicker">AUTOHAUSER® CLASSICS · OFTRINGEN</span>
            <h1>War früher alles besser? Nein, aber manchmal war es schöner.</h1>
            <p class="hero-lead">
              Unter autohauser® classics handeln wir ausgesuchte klassische Fahrzeuge im Originalzustand oder in erstklassiger Restauration. Und im Schadenfall ist Ihr Klassiker in unserem seit 1948 bestehenden Carrosseriebetrieb in besten Händen.
            </p>
            <div class="hero-actions">
              <a href="#fahrzeuge" class="btn btn-primary btn-cta"><span>Verfügbare Klassiker ansehen</span>{ICONS["arrow-right"]}</a>
              <a href="#classics-anfrage" class="btn btn-outline"><span>Besichtigung anfragen</span></a>
            </div>
          </div>
          <div class="hero-metrics">
            <div class="metric-box">
              <div class="metric-val">Ungeschweisste Substanz</div>
              <div class="metric-lbl">Strenge Selektion bei Karosserie &amp; Lack</div>
            </div>
            <div class="metric-box">
              <div class="metric-val">Carrosserie seit 1948</div>
              <div class="metric-lbl">Fachgerechte Oldtimer-Instandstellung</div>
            </div>
            <div class="metric-box">
              <div class="metric-val">YellowFox® Ortung</div>
              <div class="metric-lbl">Unsichtbarer Diebstahlschutz für Klassiker</div>
            </div>
            <div class="metric-box">
              <div class="metric-val">Thomas Hauser</div>
              <div class="metric-lbl">Persönliche Beratung · +41 62 789 33 32</div>
            </div>
          </div>
        </div>
        <div class="hero-media-card">
          {img_tag(dims, "dsc_0077-breit.jpeg", "autohauser Classics Oldtimer und Youngtimer", css_class="hero-media-img", is_hero=True)}
          <div class="hero-media-body">
            <div>
              <span class="meta-badge" style="margin-bottom:8px;">Aktuell verfügbar</span>
              <h3 style="margin-bottom:6px;">Alfa Romeo 2000 GTV &amp; Fiat 124 Abarth</h3>
              <p style="font-size:0.9rem;margin-bottom:0;">Zwei seltene italienische Klassiker mit nachvollziehbarer Schweizer Historie – ab sofort nach Vereinbarung in Oftringen zu besichtigen.</p>
            </div>
            <div class="hero-contact-strip">
              <span style="font-weight:700;color:var(--text-main);">Ansprechperson: Thomas Hauser</span>
              <a href="#classics-services" style="font-weight:700;">Ankauf &amp; Konsignation</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- VERKAUFSFAHRZEUGE -->
  <section class="section section-alt" id="fahrzeuge" data-section="classics-fahrzeuge">
    <div class="container">
      <div class="section-head">
        <span class="section-kicker">IHR TRAUMAUTO</span>
        <h2>Diese Klassiker sind jetzt bei uns verfügbar</h2>
        <p>Vollständige Dokumentation, garantierte Kilometerstände und persönliche Übergabe.</p>
      </div>
      <div class="grid-2">
        <!-- ALFA ROMEO 2000 GTV -->
        <div class="card content-card">
          <div>
            {img_tag(dims, "dsc_9610.jpeg", "Alfa Romeo 2000 GTV Bertone Baujahr 1974", css_class="card-img-top")}
            <div class="card-badge-row" style="margin-bottom:10px;">
              <span class="meta-badge">04.1974</span>
              <span class="meta-badge tabular">85'688 km garantiert</span>
              <span class="meta-badge tabular">CHF 74'900.—</span>
            </div>
            <h3>Alfa Romeo 2000 GTV (Bertone)</h3>
            <p>Fahrzeug befindet sich im ungeschweissten Originalzustand mit Patina. Seit 32 Jahren im selben Besitz und somit aus 3. Hand, Kilometerstand garantiert.</p>
            <table class="spec-table" style="margin-bottom:14px;">
              <tr><th>1. Inverkehrssetzung</th><td class="tabular">04.1974</td></tr>
              <tr><th>Fahrgestell-Nr.</th><td>AR2442912 (Typenschein 001718)</td></tr>
              <tr><th>Motor &amp; Hubraum</th><td class="tabular">4-Zyl. Reihe Vergaser · 1'962 ccm</td></tr>
              <tr><th>Leistung &amp; Getriebe</th><td class="tabular">131 PS · 5-Gang + Sperrdifferential</td></tr>
              <tr><th>Gewicht / Vmax</th><td class="tabular">1'040 kg · 193 km/h (0–100 in 9,6 s)</td></tr>
            </table>
            <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-bottom:14px;">
              {img_tag(dims, "dsc_9611.jpeg", "Alfa Romeo 2000 GTV Detail 1", extra_style="aspect-ratio:4/3;object-fit:cover;border-radius:4px;")}
              {img_tag(dims, "dsc_9612.jpeg", "Alfa Romeo 2000 GTV Detail 2", extra_style="aspect-ratio:4/3;object-fit:cover;border-radius:4px;")}
              {img_tag(dims, "dsc_9613.jpeg", "Alfa Romeo 2000 GTV Detail 3", extra_style="aspect-ratio:4/3;object-fit:cover;border-radius:4px;")}
              {img_tag(dims, "dsc_9615.jpeg", "Alfa Romeo 2000 GTV Detail 4", extra_style="aspect-ratio:4/3;object-fit:cover;border-radius:4px;")}
            </div>
          </div>
          <div style="display:flex;flex-wrap:wrap;gap:8px;">
            <a href="#classics-anfrage" onclick="wpSetPreset('Classic Cars','Besichtigung Alfa Romeo 2000 GTV','Planbar')" class="btn btn-primary btn-sm"><span>Besichtigung anfragen</span></a>
            <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Besichtigungstermin Klassiker', 'https://form.jotform.com/70161783748968')"><span>JotForm Termin</span></button>
          </div>
        </div>

        <!-- FIAT 124 ABARTH -->
        <div class="card content-card">
          <div>
            {img_tag(dims, "p3300230-titel_7071.jpeg", "Fiat 124 Abarth Rally 124 CSA Baujahr 1974", css_class="card-img-top")}
            <div class="card-badge-row" style="margin-bottom:10px;">
              <span class="meta-badge">05.1974</span>
              <span class="meta-badge tabular">99'200 km</span>
              <span class="meta-badge tabular">CHF 84'900.—</span>
            </div>
            <h3>Fiat 124 Abarth (124 CSA)</h3>
            <p>Einer von ca. 250 weltweit noch existierenden 124 CSA (von 1'013 gebauten). Sehr seltene CH-Auslieferung aus 2. Hand im ungeschweissten Originalzustand, mit Colotti-Getriebe, Gruppe-4-Hardtop, 170 PS Gr.4-Spezifikation (Originalgetriebe &amp; Teile vorhanden).</p>
            <table class="spec-table" style="margin-bottom:14px;">
              <tr><th>1. Inverkehrssetzung</th><td class="tabular">05.1974 · MFK 16.05.2018</td></tr>
              <tr><th>Chassis-Nr.</th><td>124 CSA 006 4663 (031061C)</td></tr>
              <tr><th>Motor &amp; Hubraum</th><td class="tabular">1'755 ccm Weber Doppelvergaser</td></tr>
              <tr><th>Leistung</th><td class="tabular">128 PS Serie / 170 PS Gr. 4</td></tr>
              <tr><th>Zubehör inklusive</th><td>Serviceheft, 8 Cromodora-Felgen, Orig.-Getriebe</td></tr>
            </table>
            <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-bottom:14px;">
              {img_tag(dims, "p3300246.jpeg", "Fiat 124 Abarth Detail 1", extra_style="aspect-ratio:4/3;object-fit:cover;border-radius:4px;")}
              {img_tag(dims, "p3300247.jpeg", "Fiat 124 Abarth Detail 2", extra_style="aspect-ratio:4/3;object-fit:cover;border-radius:4px;")}
              {img_tag(dims, "p3300248.jpeg", "Fiat 124 Abarth Detail 3", extra_style="aspect-ratio:4/3;object-fit:cover;border-radius:4px;")}
              {img_tag(dims, "p3300249.jpeg", "Fiat 124 Abarth Detail 4", extra_style="aspect-ratio:4/3;object-fit:cover;border-radius:4px;")}
            </div>
          </div>
          <div style="display:flex;flex-wrap:wrap;gap:8px;">
            <a href="#classics-anfrage" onclick="wpSetPreset('Classic Cars','Besichtigung Fiat 124 Abarth','Planbar')" class="btn btn-primary btn-sm"><span>Besichtigung anfragen</span></a>
            <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Besichtigungstermin Klassiker', 'https://form.jotform.com/70161783748968')"><span>JotForm Termin</span></button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SERVICES CLASSICS -->
  <section class="section" id="classics-services" data-section="classics-services">
    <div class="container">
      <div class="section-head">
        <span class="section-kicker">SPEZIALISTEN-LEISTUNGEN</span>
        <h2>Schutz, Suche, Ankauf &amp; Instandstellung für Klassiker</h2>
      </div>
      <div class="grid-2">
        <div class="card service-card">
          <div>
            {img_tag(dims, "ausschnitt-fiat-spider-1jpg.jpeg", "YellowFox Diebstahlschutz für Oldtimer", css_class="card-img-top")}
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
              {img_tag(dims, "yellowfox.gif", "YellowFox Schweiz", extra_style="height:24px;width:auto;")}
              <span class="meta-badge">Telematik-Ortung</span>
            </div>
            <h3>YellowFox® Diebstahlschutz</h3>
            <p>Obwohl Klassiker oft versichert sind, ersetzt Geld niemals die Suche nach dem verlorenen Einzelstück. Unsere Telematiklösung schützt und ortet Ihren Oldtimer zuverlässig.</p>
          </div>
          <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Angebot Diebstahlschutz (YellowFox)', 'https://form.jotform.com/70080311962953')"><span>Diebstahlschutz-Offerte anfragen</span>{ICONS["arrow-right"]}</button>
        </div>
        <div class="card service-card">
          <div>
            {img_tag(dims, "porsche-911-l-1965--23klein.jpeg", "Ankauf klassischer Fahrzeuge autohauser", css_class="card-img-top")}
            <span class="meta-badge" style="margin-bottom:8px;">Direktankauf</span>
            <h3>Ankauf klassischer Fahrzeuge</h3>
            <p>Wir suchen gepflegte Klassiker älter als Baujahr 1987 oder aus 1. Hand (1988–1995) mit garantiertem Kilometerstand – im Originalzustand oder einwandfrei restauriert.</p>
          </div>
          <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Klassisches Auto verkaufen (Ankauf)', 'https://form.jotform.com/70061239210947')"><span>Ankauf-Fragebogen öffnen</span>{ICONS["arrow-right"]}</button>
        </div>
        <div class="card service-card">
          <div>
            {img_tag(dims, "ausschnitt-alfa-spider-1.jpeg", "Konsignation Oldtimer Verkauf", css_class="card-img-top")}
            <span class="meta-badge" style="margin-bottom:8px;">Vermittlung</span>
            <h3>Konsignation &amp; Verkauf im Auftrag</h3>
            <p>Sie möchten Ihren Klassiker professionell präsentieren und verkaufen lassen? Wir übernehmen Aufbereitung, Dokumentation und Verkaufsgespräche.</p>
          </div>
          <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Konsignation Klassiker', 'https://form.jotform.com/70080831017951')"><span>Konsignations-Formular öffnen</span>{ICONS["arrow-right"]}</button>
        </div>
        <div class="card service-card">
          <div>
            {img_tag(dims, "dsc_9448klein.jpeg", "Fahrzeugsuche und Unfallinstandstellung Klassiker", css_class="card-img-top")}
            <span class="meta-badge" style="margin-bottom:8px;">Suche &amp; Schadenfall</span>
            <h3>Fahrzeugsuche &amp; Oldtimer-Unfallinstandstellung</h3>
            <p>Evaluation Ihres Wunschfahrzeugs (Schweiz und Ausland) sowie werkgetreue Carrosserie- und Lackierarbeiten bei Schäden an Klassikern.</p>
          </div>
          <div style="display:flex;flex-wrap:wrap;gap:8px;">
            <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Klassisches Auto suchen', 'https://form.jotform.com/70081174973963')"><span>Fahrzeugsuche</span></button>
            <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Schaden Klassiker melden', 'https://form.jotform.com/70160835652959')"><span>Schaden Klassiker</span></button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SMART-PRO ANFRAGE CLASSICS -->
  <section class="section section-alt" id="classics-anfrage" data-section="classics-smart">
    <div class="container">
      {render_smart_wizard("Classic Cars", "Classic Cars / Oldtimer", "classics.html", heading="Direktanfrage an Thomas Hauser (autohauser® classics)", sub="Für Besichtigungen, Fahrzeugsuche, Konsignation oder YellowFox® Diebstahlschutz – inklusive PDF-Dossier.")}
    </div>
  </section>
</main>

{render_footer(show_cockpit=show_cockpit)}
</body>
</html>"""

    # 4. schaden-kontakt.html (Heilt 503 & tote Glas-JotForm!)
    schaden_html = f"""{render_head("Schaden-, Hagel-, Glas- & Kontakt-Zentrale – autohauser® Oftringen", "Melden Sie Ihren Unfall-, Hagel- oder Glasschaden in 60 Sekunden inklusive Foto-Upload und 1-Seiten-Auftrags-PDF. Gratis-Hotline 0800 875 875.", canonical_page="schaden-kontakt.html")}
<body>
{render_header("unfall", "kontakt", dims, show_cockpit=show_cockpit)}

<main>
  <section class="section" data-section="schaden-zentrale">
    <div class="container">
      <div class="section-head">
        <span class="section-kicker">SCHADEN-, GLAS- &amp; KONTAKT-ZENTRALE</span>
        <h1>Direkt melden – ohne Wartezeit und ohne defekte Formulare</h1>
        <p>Wählen Sie den passenden Weg: Schnelle Erfassung mit Foto-Upload, Hagel-Check 2026, direkter Glas-Rückruf oder auf Wunsch das ausführliche 100-Felder-Versicherungsformular.</p>
      </div>

      <div class="tab-bar" role="tablist" aria-label="Schadenmeldungs-Wege">
        <button type="button" class="tab-btn active" onclick="switchSchadenTab('kurz', this)">1. Kurzmeldung &amp; Foto-Upload</button>
        <button type="button" class="tab-btn" onclick="switchSchadenTab('hagel', this)">2. Hagelschaden 2026</button>
        <button type="button" class="tab-btn" onclick="switchSchadenTab('glas', this)">3. Glasschaden &amp; Sofort-Rückruf</button>
        <button type="button" class="tab-btn" onclick="switchSchadenTab('lang', this)">4. Ausführliche Meldung (JotForm)</button>
      </div>

      <div id="tabInfoBanner" class="card" style="margin-bottom:24px;background:var(--primary-soft);border-color:rgba(0,103,178,0.22);">
        <div id="tabBannerKurz">
          <h3 style="margin-bottom:4px;">Schnelle Schadenmeldung mit Foto-Upload (Empfohlen)</h3>
          <p style="margin:0;">Erfassen Sie in unter einer Minute Ihren Schadenfall inklusive bis zu 3 Fotos. Sie erhalten umgehend ein strukturiertes 1-Seiten-Auftrags-PDF mit Rückruf-Zeitfenster.</p>
        </div>
        <div id="tabBannerHagel" style="display:none;">
          <h3 style="margin-bottom:4px;">Hagelschaden 2026 – Transparente Versicherungsprüfung</h3>
          <p style="margin-bottom:8px;">Wir klären vorab für Sie ab, ob Ihr Hagelschaden ohne Einschränkungen zu unseren Konditionen übernommen wird. Sollte dies bei Generali oder Vaudoise nicht vollumfänglich der Fall sein, informieren wir Sie transparent – und übernehmen bei einem begleiteten Versicherungswechsel die allfällige Differenz.</p>
          <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Hagelschaden 2026 melden (JotForm)', 'https://form.jotform.com/262393351245052')"><span>Optional: Klassisches Hagel-JotForm öffnen</span></button>
        </div>
        <div id="tabBannerGlas" style="display:none;">
          <h3 style="margin-bottom:4px;">Glasschaden &amp; Sofort-Rückruf (Andrea Heimgartner)</h3>
          <p style="margin-bottom:8px;">Die Frontscheibe ist ein tragendes Bauteil und stützt den Beifahrer-Airbag. Beim Scheibenersatz schenken wir Ihnen 1 Tag Gratis-Ersatzwagen sowie eine Innenreinigung. Nutzen Sie das direkte Formular unten für den Sofort-Rückruf – das veraltete externe Formular wurde komplett durch unseren schnellen Rückruf-Assistenten ersetzt.</p>
        </div>
        <div id="tabBannerLang" style="display:none;">
          <h3 style="margin-bottom:4px;">Ausführliche Versicherungsmeldung &amp; Spezial-JotForms</h3>
          <p style="margin-bottom:12px;">Falls Sie bereits sämtliche Unfallbeteiligten-, Zeugen- und Versicherungsdaten vollständig erfassen möchten, öffnen Sie hier direkt die ausführlichen Formulare:</p>
          <div style="display:flex;flex-wrap:wrap;gap:10px;">
            <button type="button" class="btn btn-primary btn-sm" onclick="openJotFormModal('Ausführliche Schadenmeldung (100 Felder)', 'https://form.jotform.com/63390924290963')"><span>Ausführliche Schadenmeldung (100 Felder)</span></button>
            <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Schadenmeldung kurz (JotForm)', 'https://form.jotform.com/63471863529970')"><span>JotForm Schadenmeldung kurz</span></button>
            <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Hagelschaden 2026 (JotForm)', 'https://form.jotform.com/262393351245052')"><span>JotForm Hagelschaden 2026</span></button>
          </div>
        </div>
      </div>

      <div class="grid-2" style="align-items:start;">
        <div>
          {render_smart_wizard("Unfall & Hagel / Glasschaden", "Unfallschaden", "schaden-kontakt.html")}
        </div>
        <div style="display:flex;flex-direction:column;gap:20px;">
          <div class="card">
            <span class="section-kicker">DIREKTE ERREICHBARKEIT</span>
            <h3>Jakob Hauser AG · autohauser®</h3>
            <ul class="list-check contact-direct-list">
              <li>{ICONS["phone"]}<span><strong>24h-Gratis-Hotline:</strong> <a href="tel:0800875875" class="tabular">0800 875 875</a></span></li>
              <li>{ICONS["phone"]}<span><strong>Zentrale Oftringen:</strong> <a href="tel:+41627893330" class="tabular">+41 62 789 33 30</a></span></li>
              <li>{ICONS["mail"]}<span><strong>E-Mail:</strong> <a href="mailto:info@autohauser.ch">info@autohauser.ch</a></span></li>
              <li>{ICONS["map-pin"]}<span><strong>Werkstatt:</strong> Äussere Luzernerstrasse 12, 4665 Oftringen</span></li>
              <li>{ICONS["clock"]}<span><strong>Öffnungszeiten:</strong> Mo–Fr 07:30–12:00 / 13:15–17:30 Uhr</span></li>
            </ul>
            <a href="https://maps.google.com/?q=Aeussere+Luzernerstrasse+12,+4665+Oftringen" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">{ICONS["map-pin"]}<span>Route in Google Maps öffnen</span></a>
          </div>
          <div class="card">
            <span class="section-kicker">IHRE ANSPRECHPERSONEN</span>
            <h3>Kurze Wege nach Sparte</h3>
            <p style="font-size:0.9rem;margin-bottom:8px;"><strong>Unfall &amp; Hagel:</strong> Javier Jimenez (+41 62 789 33 34)</p>
            <p style="font-size:0.9rem;margin-bottom:8px;"><strong>Kundendienst &amp; Glas:</strong> Andrea Heimgartner (+41 62 789 33 49)</p>
            <p style="font-size:0.9rem;margin-bottom:8px;"><strong>Beschriftung &amp; Folierung:</strong> Fabienne Zingg (+41 62 789 33 52)</p>
            <p style="font-size:0.9rem;margin-bottom:12px;"><strong>Classic Cars &amp; Geschäftsleitung:</strong> Thomas Hauser (+41 62 789 33 32)</p>
            <a href="team-unternehmen.html" class="btn btn-outline btn-sm"><span>Alle 6 Team-Profile ansehen</span>{ICONS["arrow-right"]}</a>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>

<script>
  function switchSchadenTab(tab, btn) {{
    var btns = document.querySelectorAll('.tab-bar .tab-btn');
    for (var i = 0; i < btns.length; i++) btns[i].classList.remove('active');
    if (btn) btn.classList.add('active');
    ['Kurz', 'Hagel', 'Glas', 'Lang'].forEach(function(k) {{
      var el = document.getElementById('tabBanner' + k);
      if (el) el.style.display = (k.toLowerCase() === tab) ? 'block' : 'none';
    }});
    if (tab === 'hagel') wpSetPreset('Hagelschaden 2026', 'Hagelschaden 2026', 'Sofort');
    else if (tab === 'glas') wpSetPreset('Glasschaden & Sofort-Rückruf', 'Glasschaden & Sofort-Rückruf', 'Sofort');
    else if (tab === 'kurz') wpSetPreset('Unfall & Hagel / Glasschaden', 'Unfallschaden', 'Sofort');
    notifyParentHeight();
  }}
  (function() {{
    var p = new URLSearchParams(window.location.search);
    var t = p.get('tab');
    if (t === 'hagel') switchSchadenTab('hagel', document.querySelectorAll('.tab-btn')[1]);
    if (t === 'glas') switchSchadenTab('glas', document.querySelectorAll('.tab-btn')[2]);
  }})();
</script>
{render_footer(show_cockpit=show_cockpit)}
</body>
</html>"""

    # 5. Build all 26 Ratgeber detail pages + ratgeber.html + 72 PDFs library
    rg_cards = []
    rg_entries = []
    for slug, rg_data in scraped.get("ratgeber", {}).items():
        items = rg_data.get("items", [])
        title_txt = ""
        for it in items:
            if it.get("tag") in ("h1", "h2", "h3") and it.get("text"):
                title_txt = ch_text(it["text"])
                break
        if not title_txt:
            title_txt = slug.replace("rat-", "").replace("-", " ").title()
        cat_label, pdf_file = RATGEBER_META.get(slug, ("Unfall & Recht", "03_rg_wer_repariert_mein_auto.pdf"))
        if pdf_file not in pdfs and pdfs:
            pdf_file = pdfs[0]
        # Clean blocks
        body_blocks = []
        excerpt = ""
        for it in items:
            tag = it.get("tag", "p")
            txt = ch_text(it.get("text", ""))
            if not txt or txt in ("kontakt", "Bitte nehmen Sie Kontakt mit uns auf.", "Home"):
                continue
            if not excerpt and tag == "p" and len(txt) > 40:
                excerpt = txt[:160] + ("..." if len(txt) > 160 else "")
            body_blocks.append((tag, txt))
        if not excerpt:
            excerpt = f"Wichtiger Praxis-Ratgeber von autohauser® zum Thema {title_txt}."
        rg_entries.append((slug, title_txt, cat_label, pdf_file, excerpt, body_blocks))

    for idx, (slug, title_txt, cat_label, pdf_file, excerpt, body_blocks) in enumerate(rg_entries):
        next_slug, next_title = rg_entries[(idx + 1) % len(rg_entries)][:2]
        content_html = "\n".join(
            f'<{tag if tag in ("h2","h3","h4","p") else "p"}>{esc(txt)}</{tag if tag in ("h2","h3","h4","p") else "p"}>'
            if tag != "li" else f'<li style="margin-bottom:6px;">{esc(txt)}</li>'
            for tag, txt in body_blocks[1:]
        )
        # Wrap consecutive li items cleanly if any
        detail_html = f"""{render_head(f"{title_txt} – Ratgeber autohauser®", excerpt, prefix="../", canonical_page=f"ratgeber/{slug}.html")}
<body>
{render_header("unfall", "ratgeber", dims, prefix="../", show_cockpit=show_cockpit)}

<main>
  <section class="section" data-section="ratgeber-detail">
    <div class="container" style="max-width:860px;">
      <div style="margin-bottom:18px;">
        <a href="../ratgeber.html" class="btn btn-outline btn-sm">{ICONS["chevron-left"]}<span>Zurück zu allen 26 Ratgebern</span></a>
      </div>
      <span class="section-kicker">RATGEBER · {esc(cat_label.upper())}</span>
      <h1>{esc(title_txt)}</h1>
      <div style="margin:18px 0 28px;border-radius:8px;overflow:hidden;border:1px solid var(--border);">
        {img_tag(dims, "autohauser_header-bild_landingpage_1170x500px_ratgeber.png", f"autohauser Ratgeber: {title_txt}", prefix="../", is_hero=True)}
      </div>
      <div class="card content-card" style="padding:32px;">
        <div style="font-size:1.02rem;line-height:1.72;">
          {content_html or f"<p>{esc(excerpt)}</p>"}
        </div>
        <div style="margin-top:24px;padding-top:20px;border-top:1px solid var(--border);display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between;">
          <a href="../assets/pdfs/{pdf_file}" target="_blank" rel="noopener noreferrer" class="btn btn-outline">{ICONS["download"]}<span>Passendes Merkblatt als PDF öffnen</span></a>
          <a href="../schaden-kontakt.html" class="btn btn-primary"><span>Schadenfall unverbindlich abklären</span>{ICONS["arrow-right"]}</a>
        </div>
      </div>
      <div style="margin-top:24px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <a href="../ratgeber.html" class="btn btn-outline btn-sm">Alle 26 Ratgeber</a>
        <a href="{next_slug}.html" class="btn btn-outline btn-sm"><span>Nächster Ratgeber: {esc(next_title[:38])}</span>{ICONS["arrow-right"]}</a>
      </div>
    </div>
  </section>
</main>

{render_footer(prefix="../", show_cockpit=show_cockpit)}
</body>
</html>"""
        (rg_dir / f"{slug}.html").write_text(detail_html, encoding="utf-8")

        rg_cards.append(f"""
        <div class="card content-card rg-item" data-cat="{esc(cat_label)}">
          <div>
            <div class="card-badge-row" style="margin-bottom:8px;">
              <span class="meta-badge">{esc(cat_label)}</span>
              <span class="meta-badge" style="background:var(--bg-alt);color:var(--text-muted);border-color:var(--border);">Ratgeber + PDF</span>
            </div>
            <h3>{esc(title_txt)}</h3>
            <p style="font-size:0.9rem;">{esc(excerpt)}</p>
          </div>
          <div style="display:flex;flex-wrap:wrap;gap:8px;">
            <a href="ratgeber/{slug}.html" class="btn btn-primary btn-sm"><span>Artikel lesen</span>{ICONS["arrow-right"]}</a>
            <a href="assets/pdfs/{pdf_file}" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">{ICONS["download"]}<span>PDF</span></a>
          </div>
        </div>""")

    # Build PDF cards for all 72 local PDFs
    pdf_cards = []
    for pfn in pdfs:
        info = pdf_meta.get(pfn, {})
        fld = ch_text(info.get("folder") or "Dokumente & Merkblätter")
        nice_name = ch_text(re.sub(r"^\d+[-_]", "", pfn.replace(".pdf", "")).replace("-", " ").replace("_", " ").strip().capitalize())
        pdf_cards.append(f"""
        <a href="assets/pdfs/{pfn}" target="_blank" rel="noopener noreferrer" class="card pdf-item" data-folder="{esc(fld)}" style="text-decoration:none;padding:16px 18px;gap:6px;">
          <div style="display:flex;align-items:center;justify-content:space-between;gap:8px;">
            <span class="meta-badge">{esc(fld)}</span>
            {ICONS["download"]}
          </div>
          <div style="font-weight:700;color:var(--text-main);font-size:0.92rem;line-height:1.35;">{esc(nice_name)}</div>
          <div style="font-size:0.76rem;color:var(--text-muted);word-break:break-all;">{esc(pfn)}</div>
        </a>""")

    ratgeber_hub_html = f"""{render_head("Ratgeber & 72 PDF-Merkblätter – autohauser® Oftringen", "Alle 26 Versicherungs-, Unfall-, Hagel- und Leasing-Ratgeber von autohauser® sowie die komplette lokale PDF-Merkblatt-Bibliothek.", canonical_page="ratgeber.html")}
<body>
{render_header("unfall", "ratgeber", dims, show_cockpit=show_cockpit)}

<main>
  <section class="section" data-section="ratgeber-hub">
    <div class="container">
      <div class="section-head">
        <span class="section-kicker">UNABHÄNGIGER KUNDEN-RATGEBER</span>
        <h1>Alle 26 Ratgeber-Beiträge &amp; 72 PDF-Merkblätter</h1>
        <p>Klares Praxiswissen zu freier Werkstattwahl, Schadenminderungspflicht, Totalschaden, Vollkasko, Leasingrückgabe und Glasschäden – vollständig lokal archiviert ohne externe Ladefehler.</p>
      </div>
      <div class="filter-bar" role="group" aria-label="Ratgeber nach Thema filtern">
        <button type="button" class="filter-btn active" onclick="filterRatgeber('alle', this)">Alle (26)</button>
        <button type="button" class="filter-btn" onclick="filterRatgeber('Unfall & Recht', this)">Unfall &amp; Recht</button>
        <button type="button" class="filter-btn" onclick="filterRatgeber('Versicherung', this)">Versicherung</button>
        <button type="button" class="filter-btn" onclick="filterRatgeber('Hagel & Glas', this)">Hagel &amp; Glas</button>
        <button type="button" class="filter-btn" onclick="filterRatgeber('Leasing & Occasion', this)">Leasing &amp; Occasion</button>
        <button type="button" class="filter-btn" onclick="filterRatgeber('Velo & Haftpflicht', this)">Velo &amp; Haftpflicht</button>
      </div>
      <div class="grid-3">
        {"".join(rg_cards)}
      </div>
    </div>
  </section>

  <section class="section section-alt" id="pdf-bibliothek" data-section="pdf-bibliothek">
    <div class="container">
      <div class="section-head">
        <span class="section-kicker">LOKALE DOKUMENTEN-BIBLIOTHEK</span>
        <h2>Alle {len(pdfs)} PDF-Merkblätter, Zertifikate &amp; Druckvorgaben</h2>
        <p>Sämtliche Merkblätter, KTI-Crashtests, Swissgarant-Bestimmungen und Folien-Datenblätter direkt zum Öffnen oder Herunterladen.</p>
      </div>
      <div class="grid-3">
        {"".join(pdf_cards)}
      </div>
    </div>
  </section>
</main>

<script>
  function filterRatgeber(cat, btn) {{
    var btns = document.querySelectorAll('.filter-bar .filter-btn');
    for (var i = 0; i < btns.length; i++) btns[i].classList.remove('active');
    if (btn) btn.classList.add('active');
    var cards = document.querySelectorAll('.rg-item');
    for (var j = 0; j < cards.length; j++) {{
      var c = cards[j].getAttribute('data-cat');
      cards[j].style.display = (cat === 'alle' || c === cat) ? 'flex' : 'none';
    }}
    notifyParentHeight();
  }}
</script>
{render_footer(show_cockpit=show_cockpit)}
</body>
</html>"""

    # 6. team-unternehmen.html
    team_members = [
        ("Thomas Hauser", "Geschäftsleitung | dipl. Masch. Ing. HTL | Wirtschaftsing. STV M-V", "Verantwortlich für Geschäftsleitung, Vertrieb, Marketing, Classic Cars und strategische Verhandlungen mit Kunden, Lieferanten und Behörden.", "+41 62 789 33 32", "thomas.hauser@autohauser.ch", "thomas-hauser_mod_1.jpeg"),
        ("Javier Jimenez", "Betriebsleiter | Schadenmanager", "Direkte Ansprechperson für unsere Kunden, ermittelt den optimalen Reparaturweg, leitet die komplette Schadenabwicklung und koordiniert das Werkstattteam.", "+41 62 789 33 34", "javier.jimenez@autohauser.ch", "20220609_javi-klein.jpeg"),
        ("Andrea Heimgartner", "Schadenmanagerin", "Drehscheibe für Kundendienst, Glasschäden und sämtliche Aspekte der Schadenerledigung sowie Lieferantenkoordination.", "+41 62 789 33 49", "andrea.heimgartner@autohauser.ch", "20230203_andrea-klein.jpeg"),
        ("Fabienne Zingg", "Leiterin Werbetechnik", "Ihre Ansprechperson für Autobeschriftung, Flottenbranding (3 bis 500 Fahrzeuge), folioCar® Folierungen und Terminvereinbarungen.", "+41 62 789 33 52", "fabienne.zingg@autohauser.ch", "fabienne_zingg_1.jpeg"),
        ("Tatjana de Rose", "Administration & Rechnungswesen | Eidg. dipl. Kauffrau EFZ", "Zuständig für Rechnungen, Zahlungen, administrative Fragen und die Finanzbuchhaltung der Jakob Hauser AG.", "+41 62 789 33 30", "tatjana.derose@autohauser.ch", "20190618_tatjana-klein.jpeg"),
        ("Daniela Dähler", "Leiterin HR & FRW | Fachfrau Finanz- und Rechnungswesen mit eidg. FA", "Betreut alle Personal- und Sozialversicherungsfragen der Jakob Hauser AG sowie die Buchhaltungen der autohauser gmbh und immohauser oftringen AG.", "+41 62 789 33 54", "daniela.daehler@autohauser.ch", "danieladaehler.jpeg"),
    ]
    team_cards_html = "\n".join(
        f"""<div class="card founder-card">
          <div>
            <div class="founder-header-row" style="display:flex;gap:14px;align-items:flex-start;margin-bottom:14px;">
              {img_tag(dims, photo, f"{name} – {role}", css_class="team-portrait")}
              <div>
                <h3 style="margin-bottom:4px;">{esc(name)}</h3>
                <p style="font-size:0.84rem;color:var(--primary-dark);font-weight:600;margin:0;">{esc(role)}</p>
              </div>
            </div>
            <p style="font-size:0.9rem;">{esc(bio)}</p>
          </div>
          <div class="founder-contact-links" style="display:flex;flex-direction:column;gap:6px;padding-top:12px;border-top:1px solid var(--border);font-size:0.88rem;">
            <a href="tel:{tel.replace(' ', '')}" style="display:inline-flex;align-items:center;gap:6px;font-weight:700;" class="tabular">{ICONS["phone"]}<span>{esc(tel)}</span></a>
            <a href="mailto:{mail}" style="display:inline-flex;align-items:center;gap:6px;">{ICONS["mail"]}<span>{esc(mail)}</span></a>
          </div>
        </div>"""
        for name, role, bio, tel, mail, photo in team_members
    )

    team_html = f"""{render_head("Team & Unternehmen seit 1948 – Jakob Hauser AG / autohauser®", "Alle 6 Ansprechpersonen mit Direktdurchwahlen, Firmengeschichte seit 1948, Standort Oftringen, UID CHE-103.749.299, Impressum und Datenschutz.", canonical_page="team-unternehmen.html")}
<body>
{render_header("unfall", "team", dims, show_cockpit=show_cockpit)}

<main>
  <section class="section" data-section="team-ansprechpersonen">
    <div class="container">
      <div class="section-head">
        <span class="section-kicker">IHRE 6 DIREKTEN ANSPRECHPERSONEN</span>
        <h1>Persönlich erreichbar in Oftringen</h1>
        <p>Bei autohauser® landen Sie nicht in anonymen Callcentern, sondern direkt bei den verantwortlichen Fachpersonen für Schadenmanagement, Werbetechnik, Classic Cars und Administration.</p>
      </div>
      <div class="grid-3">
        {team_cards_html}
      </div>
    </div>
  </section>

  <section class="section section-alt" data-section="unternehmen-historie">
    <div class="container">
      <div class="grid-2" style="align-items:center;">
        <div>
          <span class="section-kicker">FORTSCHRITTLICH TROTZ TRADITION</span>
          <h2>Jakob Hauser AG: Über 75 Jahre Carrosserie-Kompetenz seit 1948</h2>
          <p>Die Jakob Hauser AG ist ein traditionsreicher Carrosseriebetrieb, der seit 2012 unter der gemeinsamen Marke autohauser® auftritt. Unsere Kernkompetenz ist die Schadeninstandstellung von Automobilen nach Herstellervorgabe mit Originalersatzteilen.</p>
          <p>Mit der Marke folioCar® (Schweiz) brachte Thomas Hauser Anfang der 2000er Jahre das vollflächige Folieren von Autos in die Schweiz. Ergänzt wird das Angebot durch Classic Cars sowie durch das Partnerunternehmen autohauser gmbh mit YellowFox® (Schweiz) Telematik- und Ortungssystemen.</p>
          <ul class="list-check">
            <li>{ICONS["map-pin"]}<span><strong>Standort Werkstatt:</strong> Äussere Luzernerstrasse 12, 4665 Oftringen</span></li>
            <li>{ICONS["mail"]}<span><strong>Postadresse:</strong> Jakob Hauser AG, Postfach 950, CH-4800 Zofingen</span></li>
            <li>{ICONS["file-text"]}<span><strong>Handelsregister &amp; MWST:</strong> UID CHE-103.749.299 (seit 1995, Kanton Aargau, Gründungsjahr 1948)</span></li>
          </ul>
        </div>
        <div class="card content-card">
          {img_tag(dims, "dsc_5262.jpeg", "Standort Jakob Hauser AG Oftringen", css_class="card-img-top")}
          <h3>Drei Marken, eine Qualitätskultur</h3>
          <p style="margin:0;">Ob Unfallreparatur, Werbetechnik oder Classic Cars: Unsere Infrastruktur in Oftringen verbindet Spenglerei, Lackiererei, Folierzentrum und Schadenmanagement an einem Standort.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="rechtliches" data-section="impressum-datenschutz">
    <div class="container">
      <div class="section-head">
        <span class="section-kicker">RECHTLICHE ANGABEN</span>
        <h2>Impressum, Datenschutz (DSG) &amp; AGB</h2>
      </div>
      <div class="grid-3">
        <div class="card">
          <div>
            <h3>Impressum</h3>
            <p style="font-size:0.88rem;"><strong>Jakob Hauser AG</strong><br>Äussere Luzernerstrasse 12, 4665 Oftringen<br>Postfach 950, CH-4800 Zofingen<br>Geschäftsleitung: Thomas Hauser<br>UID / MWST: CHE-103.749.299<br>Gründungsjahr: 1948<br>Telefon: +41 62 789 33 30<br>E-Mail: info@autohauser.ch</p>
          </div>
        </div>
        <div class="card">
          <div>
            <h3>Datenschutz</h3>
            <p style="font-size:0.88rem;">Gestützt auf Artikel 13 der schweizerischen Bundesverfassung und das Bundesgesetz über den Datenschutz (DSG) behandeln wir Ihre Schaden-, Fahrzeug- und Kontaktdaten streng vertraulich und ausschliesslich zur Auftragsabwicklung. Einer Nutzung veröffentlichter Kontaktdaten für unaufgeforderte Werbung wird widersprochen.</p>
          </div>
        </div>
        <div class="card">
          <div>
            <h3>Garantie &amp; AGB</h3>
            <p style="font-size:0.88rem;">Für alle Unfallinstandstellungen gelten die Swissgarant-Garantiebestimmungen vom 11. Mai 2010. Urheberrechte an Bildern, Texten und Dokumenten liegen bei der Jakob Hauser AG.</p>
          </div>
          <a href="assets/pdfs/garantie_zertifikat_bestimmungen_05_2010.pdf" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">{ICONS["download"]}<span>Garantiebestimmungen (PDF)</span></a>
        </div>
      </div>
    </div>
  </section>
</main>

{render_footer(show_cockpit=show_cockpit)}
</body>
</html>"""

    # 7. karriere.html
    karriere_html = f"""{render_head("Karriere & Offene Stellen – autohauser® Oftringen", "Offene Stellen bei autohauser® und YellowFox® Schweiz in Oftringen: Carrosserie-Techniker, Gestalter/in Werbetechnik EFZ (20–40%) und Verkaufsprofi YellowFox.", canonical_page="karriere.html")}
<body>
{render_header("unfall", "karriere", dims, show_cockpit=show_cockpit)}

<main>
  <section class="section" data-section="karriere-stellen">
    <div class="container">
      <div class="section-head">
        <span class="section-kicker">KARRIERE BEI AUTOHAUSER® &amp; YELLOWFOX®</span>
        <h1>Offene Stellen in Oftringen</h1>
        <p>Kollegiales Team, moderne Werkstatt und spannende Fahrzeuge: Bewerben Sie sich direkt über die 60-Sekunden-Kurzbewerbung an Daniela Dähler (Leiterin HR).</p>
      </div>
      <div class="grid-3">
        <div class="card service-card">
          <div>
            {img_tag(dims, "mechaniker.jpeg", "Carrosserie-Techniker Stelle bei autohauser", css_class="card-img-top")}
            <div class="card-badge-row" style="margin-bottom:8px;">
              <span class="meta-badge">100 %</span>
              <span class="meta-badge">Unfallinstandstellung</span>
            </div>
            <h3>Carrosserie-Techniker / Carrosseriespengler EFZ</h3>
            <p style="font-size:0.9rem;">Für fachgerechte Reparaturen nach Herstellervorgaben auf Richtbank und mit Originalersatzteilen in unserem Swissgarant-Betrieb.</p>
            <ul class="list-check">
              <li>{ICONS["check"]}<span>Abgeschlossene Ausbildung als Carrosseriespengler/in EFZ</span></li>
              <li>{ICONS["check"]}<span>Präzise, qualitätsbewusste Arbeitsweise</span></li>
            </ul>
          </div>
          <a href="#kurzbewerbung" onclick="wpSetPreset('Karriere / Bewerbung','Bewerbung Carrosserie-Techniker','Planbar')" class="btn btn-primary btn-sm"><span>Jetzt kurz bewerben</span>{ICONS["arrow-right"]}</a>
        </div>

        <div class="card service-card">
          <div>
            {img_tag(dims, "andrea1.jpeg", "Gestalterin Werbetechnik EFZ Stelle", css_class="card-img-top")}
            <div class="card-badge-row" style="margin-bottom:8px;">
              <span class="meta-badge tabular">20–40 %</span>
              <span class="meta-badge">Werbetechnik</span>
            </div>
            <h3>Gestalter/in Werbetechnik EFZ</h3>
            <p style="font-size:0.9rem;">Druckdatenaufbereitung (Adobe Illustrator), Digitaldruck, Cut-Arbeiten, Fahrzeugbeschriftung und Carwrapping-Komplettfolierungen.</p>
            <ul class="list-check">
              <li>{ICONS["check"]}<span>Abgeschlossene Lehre als Gestalter/in Werbetechnik EFZ</span></li>
              <li>{ICONS["check"]}<span>Führerausweis Kat. B &amp; Freude an Automobilen</span></li>
            </ul>
          </div>
          <div style="display:flex;flex-wrap:wrap;gap:8px;">
            <a href="#kurzbewerbung" onclick="wpSetPreset('Karriere / Bewerbung','Bewerbung Werbetechnik 20-40%','Planbar')" class="btn btn-primary btn-sm"><span>Kurzbewerbung</span></a>
            <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Kurzbewerbung Werbetechnik', 'https://form.jotform.com/51061581490956')"><span>JotForm</span></button>
          </div>
        </div>

        <div class="card service-card">
          <div>
            {img_tag(dims, "fotolia_45325894_subscription_l_montage.jpeg", "Verkaufsprofi mit Biss YellowFox", css_class="card-img-top")}
            <div class="card-badge-row" style="margin-bottom:8px;">
              <span class="meta-badge">100 %</span>
              <span class="meta-badge">YellowFox® Schweiz</span>
            </div>
            <h3>Verkaufsprofi mit Biss (m/w)</h3>
            <p style="font-size:0.9rem;">Für unser Partnerunternehmen YellowFox® (Schweiz) Telematik- und Ortungssysteme: Verkaufsgespräche, Offerten, Abschlüsse für Schweizer KMU.</p>
            <ul class="list-check">
              <li>{ICONS["check"]}<span>Nachweisbare Verkaufserfolge &amp; hohe IT-Affinität</span></li>
              <li>{ICONS["check"]}<span>Führerausweis Kat. B &amp; Provisionsmodell</span></li>
            </ul>
          </div>
          <div style="display:flex;flex-wrap:wrap;gap:8px;">
            <a href="#kurzbewerbung" onclick="wpSetPreset('Karriere / Bewerbung','Bewerbung Verkäufer YellowFox','Planbar')" class="btn btn-primary btn-sm"><span>Kurzbewerbung</span></a>
            <button type="button" class="btn btn-outline btn-sm" onclick="openJotFormModal('Bewerbungsformular YellowFox', 'https://form.jotform.com/folioboat/bewerbungsformular-yellowfox')"><span>JotForm</span></button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-alt" id="kurzbewerbung" data-section="karriere-form">
    <div class="container">
      {render_smart_wizard("Karriere / Bewerbung", "Kurzbewerbung", "karriere.html", heading="60-Sekunden-Kurzbewerbung an Daniela Dähler", sub="Kein kompliziertes Portal nötig: Tragen Sie Ihre Wunschposition und Kontaktdaten ein – wir melden uns persönlich bei Ihnen.", show_extra_vehicle=False)}
    </div>
  </section>
</main>

{render_footer(show_cockpit=show_cockpit)}
</body>
</html>"""

    pages = {
        "index.html": index_html,
        "beschriftung.html": beschriftung_html,
        "classics.html": classics_html,
        "schaden-kontakt.html": schaden_html,
        "ratgeber.html": ratgeber_hub_html,
        "team-unternehmen.html": team_html,
        "karriere.html": karriere_html,
    }
    for fname, html_txt in pages.items():
        (out_dir / fname).write_text(html_txt, encoding="utf-8")

    # Write _redirects for Pimcore legacy paths
    redirects = """/de/online-services/kontakt /schaden-kontakt.html 301
/de/online-services/schadenmeldung /schaden-kontakt.html 301
/de/unternehmen/hagelschaden-2026 /schaden-kontakt.html?tab=hagel 301
/de/weitere-leistungen/glasschaden /schaden-kontakt.html?tab=glas 301
/de/unternehmen/ratgeber /ratgeber.html 301
/de/unternehmen/ansprechpersonen /team-unternehmen.html 301
/de/unternehmen/ueber-uns /team-unternehmen.html 301
/de/unternehmen/verkaeufer-mit-biss /karriere.html 301
"""
    (out_dir / "_redirects").write_text(redirects, encoding="utf-8")

    # Write company.json, config.json, site.json
    slug_name = out_dir.name
    pub_slug = "autohauser-vollversion" if show_cockpit else "autohauser-v2"
    company = {
        "company_name": "Jakob Hauser AG · autohauser®",
        "legal_entity": "Jakob Hauser AG",
        "uid": "CHE-103.749.299",
        "city": "Oftringen",
        "canton": "AG",
        "street": "Äussere Luzernerstrasse 12",
        "zip": "4665",
        "phone": "+41 62 789 33 30",
        "email": "info@autohauser.ch",
        "website": "https://www.autohauser.ch/",
        "partner_id": "david",
        "design_mode": "evolution",
        "industry": "Carrosserie & Fahrzeugtechnik",
    }
    config = {
        "company_name": "Jakob Hauser AG · autohauser®",
        "slug": slug_name,
        "public_slug": pub_slug,
        "cockpit_token": "autohauser2026",
        "template": "autohauser-multi-sparten-v1",
        "studio_title": "AUTOHAUSER WEBPILOT STUDIO",
        "partner_id": "david",
        "pages": ["index.html", "beschriftung.html", "classics.html", "schaden-kontakt.html", "ratgeber.html", "team-unternehmen.html", "karriere.html"],
    }
    site = {
        "slug": slug_name,
        "public_slug": pub_slug,
        "token": "autohauser2026",
        "name": f"Jakob Hauser AG · autohauser® ({'Vollversion' if show_cockpit else 'Zeigeversion'})",
        "Updated": "2026-11-18",
        "PagesCount": len(pages) + len(rg_entries),
        "TeamCount": 6,
    }
    (out_dir / "company.json").write_text(json.dumps(company, indent=2, ensure_ascii=False), encoding="utf-8")
    (out_dir / "config.json").write_text(json.dumps(config, indent=2, ensure_ascii=False), encoding="utf-8")
    (out_dir / "site.json").write_text(json.dumps(site, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Built {out_dir.name}: {len(pages)} main pages + {len(rg_entries)} ratgeber pages (cockpit={show_cockpit})")

def main():
    scraped, dims, pdfs, pdf_meta = load_data()
    # Build preview-autohauser (Vollversion mit Cockpit)
    build_pages(OUT_V1, scraped, dims, pdfs, pdf_meta, show_cockpit=True)
    # Mirror curated assets into preview-autohauser-v2/assets/
    v2_assets = OUT_V2 / "assets"
    if v2_assets.exists():
        shutil.rmtree(v2_assets)
    shutil.copytree(OUT_V1 / "assets", v2_assets)
    # Build preview-autohauser-v2 (Zeigeversion ohne Cockpit-Chrome)
    build_pages(OUT_V2, scraped, dims, pdfs, pdf_meta, show_cockpit=False)

if __name__ == "__main__":
    main()

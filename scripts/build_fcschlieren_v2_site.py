#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the 3-page WebPilot showcase Variant 2 for FC Schlieren (preview-fcschlieren-v2):
«6-%-Bauplan- & Musterhaus-Modus» (3 von 48 Seiten / 1 von 33 Teams ausgearbeitet, 94% im Rohbau-Bauplan).
Strict adherence to #UI-01..#UI-14, #LANG-01..#LANG-02 (100% ss, zero emojis in DOM, 2-Radius 0/4/8px).
"""
import json
import shutil
from pathlib import Path
import build_fcschlieren_site as v1

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
V1_DIR = BASE_DIR / "preview-fcschlieren"
SITE_DIR = BASE_DIR / "preview-fcschlieren-v2"
SITE_DIR.mkdir(parents=True, exist_ok=True)

# 1. Copy images from preview-fcschlieren/images/ to preview-fcschlieren-v2/images/
if (V1_DIR / "images").exists():
    shutil.copytree(V1_DIR / "images", SITE_DIR / "images", dirs_exist_ok=True)

# 2. Write company.json, config.json, site.json for preview-fcschlieren-v2
company_data = dict(v1.company_data)
company_data["slug"] = "fcschlieren-v2"
(SITE_DIR / "company.json").write_text(json.dumps(company_data, indent=2, ensure_ascii=False), encoding="utf-8")

config_data = {
    "slug": "fcschlieren-v2",
    "name": "FC Schlieren (V2 Bauplan)",
    "company_name": "FC Schlieren",
    "domain": "fcschlieren.ch",
    "preview_url": "https://vorschau.magnet-xs.ch/fcschlieren-v2/",
    "cockpit_token": "fcschlieren2026",
    "template": "sports-club-blueprint-v2",
    "pages": ["index.html", "herren-1.html", "kontakt.html"]
}
(SITE_DIR / "config.json").write_text(json.dumps(config_data, indent=2, ensure_ascii=False), encoding="utf-8")

site_data = {
    "name": "FC Schlieren (V2 Bauplan-Modus)",
    "slug": "fcschlieren-v2",
    "Updated": "2026-11-01",
    "TeamsCount": 33,
    "SponsorsCount": 11,
    "PrototypeCompletionPct": 6
}
(SITE_DIR / "site.json").write_text(json.dumps(site_data, indent=2, ensure_ascii=False), encoding="utf-8")


V2_BLUEPRINT_CSS = """
    /* ==========================================================================
       V2: 6-%-BAUPLAN- & MUSTERHAUS-MODUS (ARCHITEKTEN-BLUEPRINT-LOOK)
       ========================================================================== */
    .wp-v2-blueprint-bar {
      background-color: #0B1528;
      color: #F8FAFC;
      border-bottom: 2px solid #F59E0B;
      font-size: 0.8rem;
      position: relative;
      z-index: 1003;
      padding: 10px 0;
    }
    .wp-v2-bar-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      flex-wrap: wrap;
    }
    .wp-v2-bar-left {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .wp-v2-study-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: rgba(245, 158, 11, 0.18);
      border: 1px solid #F59E0B;
      color: #FBBF24;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.7rem;
      font-weight: 800;
      padding: 4px 9px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }
    .wp-v2-bar-status-text {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.78rem;
      font-weight: 700;
      color: #F8FAFC;
    }
    .wp-v2-bar-middle {
      display: flex;
      align-items: center;
      gap: 10px;
      background-color: rgba(255, 255, 255, 0.06);
      border: 1px dashed rgba(245, 158, 11, 0.55);
      padding: 5px 10px;
      border-radius: var(--radius-sm);
      flex-wrap: wrap;
    }
    .wp-v2-progress-track {
      width: 108px;
      height: 10px;
      background-color: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.24);
      border-radius: var(--radius-sm);
      overflow: hidden;
      display: flex;
      flex-shrink: 0;
    }
    .wp-v2-progress-fill {
      width: 10%;
      background-color: #F59E0B;
      height: 100%;
    }
    .wp-v2-progress-label {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.73rem;
      font-weight: 700;
      color: #FDE68A;
    }
    .wp-v2-switch-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 7px;
      background-color: #F59E0B;
      color: #0B1528;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.76rem;
      font-weight: 800;
      padding: 7px 13px;
      min-height: 34px;
      border-radius: var(--radius-sm);
      border: 1px solid #FBBF24;
      text-align: center;
      line-height: 1.25;
      flex-shrink: 0;
    }
    .wp-v2-switch-btn:hover {
      background-color: #FBBF24;
      color: #0B1528;
    }

    /* Navigation with Status Dots & Lock Icon */
    .header-inner {
      gap: 12px;
    }
    .brand-link {
      gap: 10px;
      flex-shrink: 0;
    }
    .main-nav {
      gap: 5px;
    }
    .nav-link {
      font-size: 0.73rem;
      padding: 7px 9px;
      gap: 5px;
      border: 1px solid transparent;
      background: transparent;
      cursor: pointer;
    }
    .header-actions .btn-cta {
      display: none;
    }
    .nav-link-locked {
      color: #475569;
      background-color: #F1F5F9;
      border: 1px dashed #94A3B8;
    }
    .nav-link-locked:hover {
      color: var(--fcs-navy);
      background-color: #E2E8F0;
      border-color: var(--fcs-navy);
    }
    .mobile-drawer button.mobile-nav-btn {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.92rem;
      font-weight: 700;
      color: #FDE68A;
      padding: 12px 14px;
      border-radius: var(--radius-sm);
      background-color: rgba(245, 158, 11, 0.12);
      border: 1px dashed rgba(245, 158, 11, 0.55);
      text-align: left;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      cursor: pointer;
      width: 100%;
    }

    /* Architecture Cut Zone (#bauplan-schnitt) */
    .blueprint-zone-section {
      background-color: #E2E8F0;
      background-image:
        linear-gradient(to right, rgba(15, 23, 42, 0.06) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(15, 23, 42, 0.06) 1px, transparent 1px);
      background-size: 28px 28px;
      border-top: 3px dashed #0F172A;
      border-bottom: 3px dashed #0F172A;
      padding: 76px 0 88px;
    }
    .blueprint-cut-banner {
      background-color: #0B1528;
      color: #F8FAFC;
      border: 2px dashed #F59E0B;
      border-radius: var(--radius-md);
      padding: 28px 30px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-md);
    }
    .blueprint-cut-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      margin-bottom: 14px;
      padding-bottom: 14px;
      border-bottom: 1px dashed rgba(245, 158, 11, 0.4);
    }
    .blueprint-cut-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background-color: rgba(245, 158, 11, 0.2);
      border: 1px solid #F59E0B;
      color: #FBBF24;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.74rem;
      font-weight: 800;
      padding: 5px 11px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }
    .blueprint-kpi-row {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
      margin-top: 20px;
    }
    .blueprint-kpi-box {
      background-color: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: var(--radius-sm);
      padding: 14px 16px;
    }
    .blueprint-kpi-box.is-open-scope {
      border: 1px dashed #F59E0B;
      background-color: rgba(245, 158, 11, 0.08);
    }

    /* 4 Dashed Blueprint Module Cards */
    .blueprint-modules-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 28px;
    }
    .blueprint-module-card {
      background-color: rgba(248, 250, 252, 0.96);
      border: 2px dashed #475569;
      border-radius: var(--radius-md);
      padding: 26px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 20px;
      box-shadow: 0 6px 20px rgba(15, 23, 42, 0.07);
    }
    .blueprint-module-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 12px;
    }
    .blueprint-mod-tag {
      font-family: 'Montserrat', sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      color: #0F172A;
      background-color: #E2E8F0;
      border: 1px solid #94A3B8;
      padding: 4px 9px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .blueprint-lock-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: #FEF3C7;
      border: 1px solid #D97706;
      color: #92400E;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.7rem;
      font-weight: 800;
      padding: 4px 9px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
    }
    .blueprint-module-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 1.22rem;
      font-weight: 800;
      color: #0F172A;
      margin-bottom: 10px;
      line-height: 1.25;
    }
    .blueprint-module-desc {
      font-size: 0.9rem;
      color: #334155;
      line-height: 1.6;
      margin-bottom: 14px;
    }
    .blueprint-mod-progress {
      background-color: #E2E8F0;
      border: 1px solid #CBD5E1;
      border-radius: var(--radius-sm);
      padding: 10px 12px;
      margin-bottom: 4px;
    }
    .blueprint-mod-progress-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.74rem;
      font-weight: 800;
      color: #1E293B;
      margin-bottom: 6px;
    }
    .blueprint-mod-bar {
      width: 100%;
      height: 8px;
      background-color: #CBD5E1;
      border-radius: var(--radius-sm);
      overflow: hidden;
    }
    .blueprint-mod-bar-fill {
      height: 100%;
      background-color: #D97706;
    }

    /* Wireframe Skeleton Placeholder Box inside Blueprint Card */
    .wireframe-skeleton-stage {
      background-color: #E2E8F0;
      border: 1px dashed #64748B;
      border-radius: var(--radius-sm);
      padding: 14px;
    }
    .wireframe-stage-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.68rem;
      font-weight: 800;
      color: #475569;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 10px;
    }
    .wireframe-grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-bottom: 12px;
    }
    .wireframe-box {
      background: repeating-linear-gradient(
        -45deg,
        #CBD5E1,
        #CBD5E1 6px,
        #DCE4EE 6px,
        #DCE4EE 12px
      );
      border: 1px dashed #64748B;
      border-radius: var(--radius-sm);
      height: 54px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #334155;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.66rem;
      font-weight: 800;
      text-align: center;
      padding: 4px;
    }
    .wireframe-lines {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 12px;
    }
    .wireframe-line {
      height: 8px;
      background-color: #CBD5E1;
      border-radius: var(--radius-sm);
    }
    .wireframe-line.w-80 { width: 80%; }
    .wireframe-line.w-60 { width: 60%; }

    /* V2 Team Wireframe Tiles (32 Locked Teams on herren-1.html) */
    .matrix-team-btn.wireframe-locked {
      background-color: #F1F5F9;
      border: 2px dashed #94A3B8;
      color: #334155;
    }
    .matrix-team-btn.wireframe-locked:hover {
      border-color: #0F172A;
      background-color: #E2E8F0;
    }
    .wireframe-mini-skeleton {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 6px 8px;
      background-color: #E2E8F0;
      border: 1px dashed #94A3B8;
      border-radius: var(--radius-sm);
      width: 100%;
    }
    .wireframe-mini-thumb {
      width: 28px;
      height: 22px;
      background: repeating-linear-gradient(
        -45deg,
        #CBD5E1,
        #CBD5E1 4px,
        #94A3B8 4px,
        #94A3B8 8px
      );
      border-radius: var(--radius-sm);
      flex-shrink: 0;
    }
    .wireframe-mini-bars {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .wireframe-mini-bar {
      height: 5px;
      background-color: #94A3B8;
      border-radius: var(--radius-sm);
    }
    .pill-wireframe-lock {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background-color: #FEF3C7;
      color: #92400E;
      border: 1px solid #F59E0B;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.62rem;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      flex-shrink: 0;
    }

    @media (max-width: 1080px) {
      .blueprint-modules-grid,
      .blueprint-kpi-row {
        grid-template-columns: 1fr;
      }
    }
    @media (max-width: 720px) {
      .wp-v2-bar-inner {
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
      }
      .wp-v2-bar-middle {
        width: 100%;
      }
      .wp-v2-switch-btn {
        width: 100%;
      }
      .blueprint-cut-banner {
        padding: 20px 18px;
      }
      .blueprint-module-card {
        padding: 20px 18px;
      }
      .wireframe-grid-3 {
        grid-template-columns: 1fr;
      }
    }
"""


def render_v2_shell(filename: str, page_title: str, active_nav: str, body_html: str, extra_css: str = "") -> str:
    nav_start = "active" if active_nav == "startseite" else ""
    nav_teams = "active" if active_nav == "teams" else ""
    nav_kontakt = "active" if active_nav == "kontakt" else ""
    v1_href = "/fcschlieren/" if filename == "index.html" else f"/fcschlieren/{filename}"

    return f"""<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self' https: data: blob:; script-src 'self' 'unsafe-inline' https:; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com data:; img-src 'self' https: data: blob:; connect-src 'self' https:;">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta http-equiv="Permissions-Policy" content="camera=(), microphone=(), geolocation=()">
  <title>{page_title}</title>
  <meta name="description" content="Architektur-Studie &amp; 6-%-Prototyp (Vorschau V2) für den Fussballclub Schlieren: 3 von 48 Seiten exemplarisch ausgearbeitet, 45 Unterseiten &amp; 32 Teams im Bauplan.">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Montserrat:wght@600;700;800&amp;display=swap" rel="stylesheet">
  <style>
{v1.SHARED_CSS}
{V2_BLUEPRINT_CSS}
{extra_css}
  </style>
</head>
<body>

  <!-- 1. UNUEBERSEHBARE KONZEPT- & AUSBAUSTUFEN-LEISTE (V2: 6-%-BAUPLAN-MODUS) -->
  <div class="wp-v2-blueprint-bar">
    <div class="container wp-v2-bar-inner">
      <div class="wp-v2-bar-left">
        <span class="wp-v2-study-badge">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
          <span>ARCHITEKTUR-STUDIE · VORSCHAU V2</span>
        </span>
        <span class="wp-v2-bar-status-text">Ausbaustufe Prototyp: 6 % (3 von 48 Seiten exemplarisch ausgearbeitet)</span>
      </div>

      <div class="wp-v2-bar-middle" aria-label="Bauplan-Fortschritt 6 Prozent">
        <div class="wp-v2-progress-track">
          <div class="wp-v2-progress-fill"></div>
        </div>
        <span class="wp-v2-progress-label">6 % fertig · 45 Unterseiten &amp; 32 Teams im Rohbau</span>
      </div>

      <a href="{v1_href}" class="wp-v2-switch-btn">
        <span>Zu Variante 1 (Voll-Ansicht) wechseln</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
    </div>
  </div>

  <!-- TOP BAR -->
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div class="top-bar-left">
        <span class="top-bar-badge" data-slot="topbar_badge">PROTOTYP-AUSBAU: 3 / 48 SEITEN</span>
        <span data-slot="topbar_info">1 von 33 Teams (Herren 1) &amp; 11 Sponsoren als Musterhaus ausgearbeitet · 94 % Rohbau-Bauplan</span>
      </div>
      <div class="top-bar-links">
        <a href="index.html#sponsoren">11 Sponsoren (Übernommen)</a>
        <a href="index.html#bauplan-schnitt">Bauplan-Schnitt (45 offene Seiten)</a>
        <button type="button" onclick="wpOpenBlueprintModal('Rohbau-Modul B: Vereinsdokumente, Statuten &amp; Chronik (7 Unterseiten)', 'Vereinsführung FC Schlieren', 'Roger Küng (r.kueng@fcschlieren.ch) &amp; Jana Seifriz (j.seifriz@fcschlieren.ch)')">Verein &amp; Chronik (0/7 offen)</button>
        <a href="kontakt.html?thema=probetraining">Smart-Anfrage (Live-Demo)</a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER (HAUPTNAVIGATION MIT STATUS-PUNKTEN & SCHLOSS-SYMBOL) -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="index.html" class="brand-link" aria-label="FC Schlieren Startseite">
        <img src="images/logo-fcschlieren.webp" alt="Wappen FC Schlieren" class="brand-logo" width="48" height="56" data-slot="brand_logo">
        <div class="brand-text">
          <span class="brand-name" data-slot="brand_name">FC SCHLIEREN</span>
          <span class="brand-sub" data-slot="brand_sub">SEIT 1921 · BAUPLAN V2</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Hauptnavigation mit Ausbau-Status">
        <a href="index.html" class="nav-link {nav_start}">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#10B981"/></svg>
          <span>Startseite (Muster)</span>
        </a>
        <a href="herren-1.html" class="nav-link {nav_teams}">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#10B981"/></svg>
          <span>Muster-Team: Herren 1 (1/33)</span>
        </a>
        <a href="index.html#sponsoren" class="nav-link">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#F59E0B"/></svg>
          <span>Sponsoren (Übernommen)</span>
        </a>
        <button type="button" class="nav-link nav-link-locked" onclick="wpOpenBlueprintModal('Rohbau-Modul B &amp; C: Verein, Vorstand, Chronik &amp; Sportanlage Zelgli (7 Seiten offen)', 'Vereinsführung &amp; Infrastruktur (Noch nicht migriert · 0 %)', 'Roger Küng (Präsident) &amp; Jana Seifriz (Geschäftsstelle)', 'allgemein')">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" aria-hidden="true"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          <span>Verein &amp; Zelgli (7 Seiten offen)</span>
        </button>
        <a href="kontakt.html" class="nav-link {nav_kontakt}">
          <svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="#10B981"/></svg>
          <span>Smart-Anfrage (Live-Demo)</span>
        </a>
      </nav>

      <div class="header-actions">
        <a href="kontakt.html?thema=probetraining" class="btn-cta btn-cta-primary btn-sm" data-slot="header_cta">
          <span>Smart-Anfrage testen</span>
        </a>
        <button type="button" class="mobile-toggle" id="mobileMenuBtn" aria-label="Menü öffnen" onclick="wpToggleMobileMenu()">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    </div>

    <div class="mobile-drawer" id="mobileDrawer">
      <a href="index.html" onclick="wpCloseMobileMenu()">Startseite (Muster · 6 % Prototyp)</a>
      <a href="herren-1.html" onclick="wpCloseMobileMenu()">Muster-Team: Herren 1 (1/33 fertig · 32 im Rohbau)</a>
      <a href="index.html#sponsoren" onclick="wpCloseMobileMenu()">Sponsoren (Alle 11 übernommen)</a>
      <button type="button" class="mobile-nav-btn" onclick="wpCloseMobileMenu(); wpOpenBlueprintModal('Rohbau-Modul B &amp; C: Verein, Vorstand, Chronik &amp; Sportanlage Zelgli (7 Seiten offen)', 'Vereinsführung &amp; Infrastruktur (Noch nicht migriert · 0 %)', 'Roger Küng &amp; Jana Seifriz', 'allgemein')">
        <span>Verein &amp; Zelgli (7 Seiten offen · Rohbau)</span>
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      </button>
      <a href="kontakt.html" onclick="wpCloseMobileMenu()">Smart-Anfrage (Live-Demo)</a>
      <a href="{v1_href}" onclick="wpCloseMobileMenu()" style="background-color:#F59E0B;color:#0B1528;">Zu Variante 1 (Voll-Ansicht) wechseln</a>
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
              <div style="font-size:0.76rem;color:#FDC500;font-weight:700;">ARCHITEKTUR-STUDIE V2 · 6 % PROTOTYP</div>
            </div>
          </div>
          <p style="font-size:0.86rem;color:#CBD5E1;line-height:1.6;margin-bottom:14px;" data-slot="footer_about">
            Architekten-Musterhaus &amp; Bauplan-Vorschau für den FC Schlieren: 3 von 48 Seiten (Startseite, 1 Muster-Team Herren 1, Smart-Anfrage) als Qualitätsbeweis ausgearbeitet — 45 Unterseiten &amp; 32 Teams folgen im Hauptauftrag.
          </p>
          <div style="font-size:0.84rem;color:#E2E8F0;font-weight:600;">
            Fussballanlage Zelgli («im Rohr») · Postfach · 8952 Schlieren
          </div>
        </div>

        <div>
          <div class="footer-title">Prototyp (6 % ausgearbeitet)</div>
          <ul class="footer-list">
            <li><a href="index.html">Startseite: Hero &amp; Sponsoren (Muster)</a></li>
            <li><a href="herren-1.html">Muster-Team: Herren 1 (1 von 33 fertig)</a></li>
            <li><a href="index.html#sponsoren">Alle 11 Sponsoren (Übernommen)</a></li>
            <li><a href="kontakt.html">Smart-Anfrage-Zentrale (Live-Demo)</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Rohbau-Bauplan (94 % offen)</div>
          <ul class="footer-list">
            <li><a href="herren-1.html#alle-teams-matrix">32 weitere Mannschaften (Rohbau)</a></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Rohbau-Modul B: Verein, Vorstand (6), Funktionäre &amp; Chronik (7 Unterseiten)', 'Vereinsführung FC Schlieren (0 % übertragen)', 'Roger Küng &amp; Jana Seifriz')">Verein, Vorstand &amp; Chronik (0/7)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Rohbau-Modul C: Sportanlage Zelgli, Platzbelegung &amp; Club-Beizli (3 Unterseiten)', 'Infrastruktur &amp; Gastronomie (0 % übertragen)', 'Müslüm Bozan &amp; Geschäftsstelle')">Sportanlage Zelgli &amp; Beizli (0/3)</button></li>
            <li><button type="button" onclick="wpOpenBlueprintModal('Rohbau-Modul D: Spielbetrieb, Trainingspläne, Fussballschule &amp; Camps (5 Unterseiten)', 'Spielbetrieb &amp; Nachwuchs (0 % übertragen)', 'Luigi Schiavano &amp; Roger Mehr')">Trainingspläne &amp; Camps (0/5)</button></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Ansichten-Vergleich &amp; Rechtliches</div>
          <ul class="footer-list">
            <li><a href="{v1_href}" style="color:#FDC500;font-weight:700;">Zu Variante 1 (Voll-Ansicht) wechseln</a></li>
            <li><a href="index.html#bauplan-schnitt">Architektur-Bauplan-Schnitt ansehen</a></li>
            <li><button type="button" onclick="wpOpenImpressumModal()">Impressum &amp; Datenschutz</button></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Fussballclub Schlieren (8952 Schlieren) · Konzept- &amp; Bauplan-Studie V2 (Ausbaustufe 6 %).</div>
        <div style="display:flex;gap:16px;flex-wrap:wrap;">
          <a href="{v1_href}" style="color:#FDC500;font-weight:700;">Variante 1 (Voll-Ansicht) öffnen</a>
          <a href="herren-1.html" style="color:#E2E8F0;">Muster-Team Herren 1 (1/33)</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- ARCHITEKTUR-BLAUPAUSEN-MODAL (V2 BAUPLAN-MODUS) -->
  <div class="wp-modal-backdrop" id="wpBlueprintModal" role="dialog" aria-modal="true" aria-labelledby="wpBpTitle">
    <div class="wp-modal-dialog">
      <button type="button" class="wp-modal-close" aria-label="Dialog schliessen" onclick="wpCloseBlueprintModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="section-kicker">BAUPLAN-STATUS: ROHBAU (NOCH NICHT MIGRIERT · TEIL DES HAUPTAUFTRAGS)</div>
      <h3 id="wpBpTitle" style="font-size:1.35rem;font-weight:800;margin-bottom:8px;">Rohbau-Modul: Noch nicht übertragen</h3>
      <p id="wpBpSub" style="font-size:0.9rem;color:var(--text-body);margin-bottom:12px;">
        In dieser <strong>Architektur-Studie (Ausbaustufe 6 % · 3 von 48 Seiten)</strong> sind oben das Design, die 11 Sponsoren und exakt <strong>1 Muster-Team (Herren 1)</strong> ausgearbeitet. Dieses Modul befindet sich bewusst noch im <strong>unbefüllten Rohbau (0 % übertragen)</strong> und wird nach Auftragserteilung komplett mit allen Originaldaten, Fotos und Kadern eingerichtet.
      </p>
      <div style="background-color:#FEF3C7;border-left:4px solid #D97706;padding:12px 14px;border-radius:var(--radius-sm);font-size:0.86rem;margin-bottom:14px;">
        <div style="font-weight:800;color:#92400E;" id="wpBpCategory">Bereich / Abteilung: Rohbau-Modul</div>
        <div style="color:#78350F;margin-top:2px;" id="wpBpContact">Zuständige Ansprechperson im Verein: Geschäftsstelle FC Schlieren</div>
      </div>

      <div class="wp-modal-checklist">
        <div style="font-family:'Montserrat',sans-serif;font-size:0.78rem;font-weight:800;text-transform:uppercase;color:var(--fcs-navy);">
          Wird nach Auftragserteilung (analog Muster-Team Herren 1) schlüsselfertig übertragen:
        </div>
        <div class="wp-modal-check-item">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Vollständige Übernahme aller bestehenden Texte, Mannschaftsfotos, Porträts &amp; PDF-Dokumente</span>
        </div>
        <div class="wp-modal-check-item">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Einrichtung aller 32 weiteren Mannschafts-Seiten (~480 Spieler- &amp; Trainerporträts nach Position)</span>
        </div>
        <div class="wp-modal-check-item">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Direkte Anbindung an das WebPilot Studio-Cockpit für Sekundenschnelle Änderungen per KI oder 1-Klick</span>
        </div>
      </div>

      <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:18px;">
        <a href="herren-1.html" class="btn-cta btn-cta-primary btn-sm" onclick="wpCloseBlueprintModal()">
          <span>Fertiges Muster-Team (Herren 1 · 1/33) ansehen</span>
        </a>
        <a href="kontakt.html?thema=probetraining" id="wpBpCtaLink" class="btn-cta btn-cta-gold btn-sm">
          <span>Smart-Anfrage (Live-Demo) testen</span>
        </a>
      </div>
    </div>
  </div>

  <!-- IMPRESSUM MODAL -->
  <div class="wp-modal-backdrop" id="wpImpressumModal" role="dialog" aria-modal="true" aria-labelledby="wpImpTitle">
    <div class="wp-modal-dialog">
      <button type="button" class="wp-modal-close" aria-label="Impressum schliessen" onclick="wpCloseImpressumModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="section-kicker">RECHTLICHE ANGABEN · SCHWEIZER DSG</div>
      <h3 id="wpImpTitle" style="font-size:1.3rem;font-weight:800;margin-bottom:10px;">Impressum &amp; Datenschutz — FC Schlieren</h3>
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
      if (tEl) tEl.textContent = title || 'Rohbau-Modul';
      if (cEl) cEl.textContent = 'Bereich / Ausbaustatus: ' + (category || 'Rohbau (0 % übertragen · Teil des Hauptauftrags)');
      if (pEl) pEl.textContent = 'Zuständige Ansprechperson: ' + (contact || 'Geschäftsstelle FC Schlieren (j.seifriz@fcschlieren.ch)');
      if (linkEl) linkEl.href = 'kontakt.html?thema=' + (topicParam || 'probetraining');
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


# Extract Hero and Sponsors sections from v1.INDEX_BODY
hero_part = v1.INDEX_BODY.split("<!-- 2. AKTUELLES, FUSSBALLSCHULE & FUSSBALLCAMPS -->")[0]
hero_part = hero_part.replace(
    '<span>Muster-Team (Herren 1 / Frauen 1) &amp; 33 Teams</span>',
    '<span>Muster-Team: Herren 1 (1/33 fertig) &amp; 32 Rohbau-Teams</span>'
)

sponsors_part = "  <!-- 2. UNSERE SPONSOREN, GÖNNER & PARTNER (100% ORIGINAL-BESTAND DIREKT NACH DEM HERO) -->\n  <section id=\"sponsoren\"" + v1.INDEX_BODY.split('<section id="sponsoren"')[1].split("<script>")[0]

BAUPLAN_SCHNITT_SECTION = """
  <!-- 3. ARCHITEKTUR-BAUPLAN-SCHNITT (NOCH NICHT UEBERTRAGENE MODULE: 45 VON 48 SEITEN) -->
  <section id="bauplan-schnitt" class="blueprint-zone-section" data-section="bauplan-schnitt">
    <div class="container">

      <!-- UNUEBERSEHBARES ARCHITEKTEN-SCHNITT-BANNER -->
      <div class="blueprint-cut-banner">
        <div class="blueprint-cut-top">
          <span class="blueprint-cut-pill">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            <span>ARCHITEKTUR-BAUPLAN-ZONE · NOCH NICHT ÜBERTRAGENE MODULE (45 VON 48 SEITEN)</span>
          </span>
          <span style="font-family:'Montserrat',sans-serif;font-size:0.78rem;font-weight:800;color:#FDE68A;">
            PROTOTYP-STAND: 6 % FERTIG · 94 % ROHBAU-GERÜST
          </span>
        </div>

        <h2 style="color:#FFFFFF;font-size:clamp(1.55rem,2.8vw,2.25rem);font-weight:800;margin-bottom:10px;" data-slot="bp_zone_title">
          Sichtbarer Architektur-Schnitt: Was oben glänzt vs. was im Hauptauftrag folgt.
        </h2>
        <p style="font-size:0.95rem;color:#E2E8F0;line-height:1.65;max-width:920px;" data-slot="bp_zone_desc">
          Oben siehst du am Hero-Auftritt, an den <strong>11 Original-Sponsoren</strong> und am <strong>Muster-Team Herren 1</strong>, wie hochwertig die neue Plattform des FC Schlieren wirkt. Direkt hier darunter siehst du im gestrichelten Architekten-Bauplan schwarz auf weiss, dass erst <strong>6 % (3 von 48 Seiten / 1 von 33 Teams)</strong> als Prototyp ausgearbeitet sind und die weiteren <strong>94 % (45 Unterseiten &amp; 32 Mannschaften)</strong> erst nach Auftragserteilung übertragen werden.
        </p>

        <div class="blueprint-kpi-row">
          <div class="blueprint-kpi-box">
            <div style="font-family:'Montserrat',sans-serif;font-size:0.72rem;font-weight:800;color:#34D399;text-transform:uppercase;margin-bottom:4px;">
              BEREITS AUSGEARBEITET IM PROTOTYP (6 % · 3 VON 48 SEITEN)
            </div>
            <div style="font-size:0.86rem;color:#F8FAFC;font-weight:600;">
              1. Startseite (Hero &amp; alle 11 Sponsoren) · 2. Muster-Team <strong>Herren 1 (1/33)</strong> · 3. Smart-Anfrage-Zentrale (Live-Demo inkl. 1-Seiten-PDF)
            </div>
          </div>
          <div class="blueprint-kpi-box is-open-scope">
            <div style="font-family:'Montserrat',sans-serif;font-size:0.72rem;font-weight:800;color:#FBBF24;text-transform:uppercase;margin-bottom:4px;">
              OFFEN FÜR HAUPTAUFTRAG (94 % · 45 VON 48 UNTERSEITEN IM ROHBAU)
            </div>
            <div style="font-size:0.86rem;color:#F8FAFC;font-weight:600;">
              32 weitere Mannschafts-Seiten (~480 Porträts) · 7 Vereins-, Vorstands- &amp; Chronik-Seiten · 3 Zelgli- &amp; Beizli-Seiten · 5 Spielbetriebs- &amp; Camp-Seiten
            </div>
          </div>
        </div>
      </div>

      <!-- 4 GESTRICHELTE ARCHITEKTEN-BAUPLAN-KARTEN MIT DRAHTGITTER-SKELETONS -->
      <div class="blueprint-modules-grid">

        <!-- ROHBAU-MODUL A -->
        <article class="blueprint-module-card">
          <div>
            <div class="blueprint-module-top">
              <span class="blueprint-mod-tag">ROHBAU-MODUL A · MANNSCHAFTEN</span>
              <span class="blueprint-lock-badge">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span>STATUS: ROHBAU / 3 % ÜBERTRAGEN</span>
              </span>
            </div>
            <h3 class="blueprint-module-title" data-slot="bp_mod_a_title">
              32 weitere Mannschafts-Seiten (~480 Spieler- &amp; Trainerporträts)
            </h3>
            <p class="blueprint-module-desc" data-slot="bp_mod_a_desc">
              <strong>Status: 1 von 33 Teams (3 %)</strong> als Muster ausgearbeitet (<strong>Herren 1</strong>). Offen für Hauptauftrag: Herren 2, Senioren 30+/40+/50+, Frauen 1–3, 17&times; Junioren A–G, 8&times; Juniorinnen inkl. Kaderlisten, Einzelfotos und Trainingszeiten.
            </p>
            <div class="blueprint-mod-progress">
              <div class="blueprint-mod-progress-head">
                <span>Ausbaustatus Mannschafts-Seiten</span>
                <span>1 von 33 Teams (3 %) · 32 Teams offen</span>
              </div>
              <div class="blueprint-mod-bar">
                <div class="blueprint-mod-bar-fill" style="width: 6%;"></div>
              </div>
            </div>
          </div>

          <div class="wireframe-skeleton-stage">
            <div class="wireframe-stage-header">
              <span>DRAHTGITTER-PLATZHALTER (32 OFFENE TEAM-SEITEN)</span>
              <span>BEFÜLLUNG BEI AUFTRAG</span>
            </div>
            <div class="wireframe-grid-3">
              <div class="wireframe-box">FOTO-PLATZHALTER<br>FRAUEN 1–3</div>
              <div class="wireframe-box">FOTO-PLATZHALTER<br>HERREN 2 / SEN.</div>
              <div class="wireframe-box">FOTO-PLATZHALTER<br>25&times; NACHWUCHS</div>
            </div>
            <div class="wireframe-lines">
              <div class="wireframe-line w-80"></div>
              <div class="wireframe-line w-60"></div>
            </div>
            <a href="herren-1.html#alle-teams-matrix" class="btn-cta btn-cta-navy btn-sm" style="width:100%;">
              <span>1 Muster-Team (Herren 1) &amp; 32 Rohbau-Kacheln ansehen</span>
            </a>
          </div>
        </article>

        <!-- ROHBAU-MODUL B -->
        <article class="blueprint-module-card">
          <div>
            <div class="blueprint-module-top">
              <span class="blueprint-mod-tag">ROHBAU-MODUL B · VEREIN &amp; CHRONIK</span>
              <span class="blueprint-lock-badge">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span>STATUS: ROHBAU / 0 % ÜBERTRAGEN</span>
              </span>
            </div>
            <h3 class="blueprint-module-title" data-slot="bp_mod_b_title">
              Verein, Vorstand (6), Funktionäre &amp; 100-Jahr-Chronik (7 Unterseiten)
            </h3>
            <p class="blueprint-module-desc" data-slot="bp_mod_b_desc">
              <strong>Status: 0 von 7 Seiten (0 %)</strong> übertragen. Offen für Hauptauftrag: Vorstands- &amp; Funktionärsporträts, Schiedsrichter, Vereinsgeschichte 1921–2021, Statuten, Schutzkonzepte &amp; PDF-Downloads.
            </p>
            <div class="blueprint-mod-progress">
              <div class="blueprint-mod-progress-head">
                <span>Ausbaustatus Vereins- &amp; Chronik-Seiten</span>
                <span>0 von 7 Seiten (0 %) · Komplett im Rohbau</span>
              </div>
              <div class="blueprint-mod-bar">
                <div class="blueprint-mod-bar-fill" style="width: 0%;"></div>
              </div>
            </div>
          </div>

          <div class="wireframe-skeleton-stage">
            <div class="wireframe-stage-header">
              <span>DRAHTGITTER-PLATZHALTER (VORSTAND &amp; CHRONIK 1921)</span>
              <span>BEFÜLLUNG BEI AUFTRAG</span>
            </div>
            <div class="wireframe-grid-3">
              <div class="wireframe-box">6&times; VORSTAND<br>PORTRÄT-GERÜST</div>
              <div class="wireframe-box">CHRONIK-TIMELINE<br>1921–2026</div>
              <div class="wireframe-box">STATUTEN &amp; PDF<br>DOKUMENTE</div>
            </div>
            <div class="wireframe-lines">
              <div class="wireframe-line w-80"></div>
              <div class="wireframe-line w-60"></div>
            </div>
            <button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Rohbau-Modul B: Verein, Vorstand (6), Funktionäre &amp; 100-Jahr-Chronik (7 Unterseiten)', '0 von 7 Seiten übertragen (Teil des Hauptauftrags)', 'Roger Küng (Präsident) &amp; Jana Seifriz (Geschäftsstelle)', 'allgemein')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
              <span>Bauplan-Umfang für Modul B (7 Seiten) prüfen</span>
            </button>
          </div>
        </article>

        <!-- ROHBAU-MODUL C -->
        <article class="blueprint-module-card">
          <div>
            <div class="blueprint-module-top">
              <span class="blueprint-mod-tag">ROHBAU-MODUL C · SPORTANLAGE ZELGLI</span>
              <span class="blueprint-lock-badge">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span>STATUS: ROHBAU / 0 % ÜBERTRAGEN</span>
              </span>
            </div>
            <h3 class="blueprint-module-title" data-slot="bp_mod_c_title">
              Sportanlage Zelgli, Platzbelegung &amp; Club-Beizli (3 Unterseiten)
            </h3>
            <p class="blueprint-module-desc" data-slot="bp_mod_c_desc">
              <strong>Status: 0 von 3 Seiten (0 %)</strong> übertragen. Offen für Hauptauftrag: Luftbild &amp; Platzplan Zelgli, Öffnungszeiten &amp; Reservation Club-Beizli, Anfahrt &amp; Parkplätze.
            </p>
            <div class="blueprint-mod-progress">
              <div class="blueprint-mod-progress-head">
                <span>Ausbaustatus Zelgli &amp; Club-Beizli</span>
                <span>0 von 3 Seiten (0 %) · Komplett im Rohbau</span>
              </div>
              <div class="blueprint-mod-bar">
                <div class="blueprint-mod-bar-fill" style="width: 0%;"></div>
              </div>
            </div>
          </div>

          <div class="wireframe-skeleton-stage">
            <div class="wireframe-stage-header">
              <span>DRAHTGITTER-PLATZHALTER (ZELGLI &amp; CLUB-BEIZLI)</span>
              <span>BEFÜLLUNG BEI AUFTRAG</span>
            </div>
            <div class="wireframe-grid-3">
              <div class="wireframe-box">LUFTBILD &amp;<br>PLATZPLAN ZELGLI</div>
              <div class="wireframe-box">CLUB-BEIZLI<br>40–50 PLÄTZE</div>
              <div class="wireframe-box">ANFAHRT &amp;<br>PARKPLÄTZE</div>
            </div>
            <div class="wireframe-lines">
              <div class="wireframe-line w-80"></div>
              <div class="wireframe-line w-60"></div>
            </div>
            <button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Rohbau-Modul C: Sportanlage Zelgli, Platzbelegung &amp; Club-Beizli (3 Unterseiten)', '0 von 3 Seiten übertragen (Teil des Hauptauftrags)', 'Müslüm Bozan (Wirt Club-Beizli) &amp; Geschäftsstelle FC Schlieren', 'allgemein')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
              <span>Bauplan-Umfang für Modul C (3 Seiten) prüfen</span>
            </button>
          </div>
        </article>

        <!-- ROHBAU-MODUL D -->
        <article class="blueprint-module-card">
          <div>
            <div class="blueprint-module-top">
              <span class="blueprint-mod-tag">ROHBAU-MODUL D · SPIELBETRIEB &amp; CAMPS</span>
              <span class="blueprint-lock-badge">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span>STATUS: ROHBAU / 0 % ÜBERTRAGEN</span>
              </span>
            </div>
            <h3 class="blueprint-module-title" data-slot="bp_mod_d_title">
              Spielbetrieb, Trainingspläne, Fussballschule &amp; Camps (5 Unterseiten)
            </h3>
            <p class="blueprint-module-desc" data-slot="bp_mod_d_desc">
              <strong>Status: 0 von 5 Seiten (0 %)</strong> übertragen. Offen für Hauptauftrag: Sommer-/Winter-Trainingsplan, Mittwoch-Fussballschule (Jun. E/F/G), Kohler Fussballcamps &amp; FVRZ-Resultate-Anbindung.
            </p>
            <div class="blueprint-mod-progress">
              <div class="blueprint-mod-progress-head">
                <span>Ausbaustatus Spielbetrieb &amp; Nachwuchs</span>
                <span>0 von 5 Seiten (0 %) · Komplett im Rohbau</span>
              </div>
              <div class="blueprint-mod-bar">
                <div class="blueprint-mod-bar-fill" style="width: 0%;"></div>
              </div>
            </div>
          </div>

          <div class="wireframe-skeleton-stage">
            <div class="wireframe-stage-header">
              <span>DRAHTGITTER-PLATZHALTER (TRAININGSPLÄNE &amp; CAMPS)</span>
              <span>BEFÜLLUNG BEI AUFTRAG</span>
            </div>
            <div class="wireframe-grid-3">
              <div class="wireframe-box">TRAININGS- &amp;<br>HALLENPLAN</div>
              <div class="wireframe-box">MITTWOCH-<br>FUSSBALLSCHULE</div>
              <div class="wireframe-box">KOHLER CAMPS &amp;<br>FVRZ-RESULTATE</div>
            </div>
            <div class="wireframe-lines">
              <div class="wireframe-line w-80"></div>
              <div class="wireframe-line w-60"></div>
            </div>
            <button type="button" class="btn-cta btn-cta-outline btn-sm" style="width:100%;" onclick="wpOpenBlueprintModal('Rohbau-Modul D: Spielbetrieb, Trainingspläne, Fussballschule &amp; Camps (5 Unterseiten)', '0 von 5 Seiten übertragen (Teil des Hauptauftrags)', 'Luigi Schiavano (Leiter Junioren) &amp; Roger Mehr (Spielbetrieb)', 'spielbetrieb')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
              <span>Bauplan-Umfang für Modul D (5 Seiten) prüfen</span>
            </button>
          </div>
        </article>

      </div>
    </div>
  </section>
"""

V2_INDEX_BODY = hero_part + "\n" + sponsors_part + "\n" + BAUPLAN_SCHNITT_SECTION


# Build V2 HERREN_1_BODY: Only Herren 1 (1/33) built out, Frauen 1 + 31 other teams = 32 locked wireframe tiles!
herren1_pane_only = v1.HERREN_1_BODY.split("<!-- ================= TAB 1: HERREN 1 ================= -->")[1].split("<!-- ================= TAB 2: FRAUEN 1 ================= -->")[0]


def make_locked_team_tile(team_name: str, modal_title: str, dept_label: str, contact_label: str, subtitle: str) -> str:
    return f"""          <button type="button" class="matrix-team-btn wireframe-locked" onclick="wpOpenBlueprintModal('{modal_title}', '{dept_label} (Status: Rohbau · Noch nicht migriert)', '{contact_label}', 'probetraining')">
            <div class="matrix-team-top">
              <span class="matrix-team-name">{team_name}</span>
              <span class="pill-wireframe-lock">
                <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span>ROHBAU</span>
              </span>
            </div>
            <div class="wireframe-mini-skeleton" aria-hidden="true">
              <div class="wireframe-mini-thumb"></div>
              <div class="wireframe-mini-bars">
                <div class="wireframe-mini-bar" style="width:82%;"></div>
                <div class="wireframe-mini-bar" style="width:58%;"></div>
              </div>
            </div>
            <span style="font-size:0.74rem;color:#475569;font-weight:700;">Status: Noch nicht migriert · Teil des Hauptauftrags ({subtitle})</span>
          </button>"""


V2_HERREN_1_BODY = f"""
  <!-- FORTSCHRITTS-BANNER: NUR 1 VON 33 TEAMS (3 %) ALS MUSTER FERTIG — 32 TEAMS OFFEN -->
  <section class="architect-banner" data-section="musterhaus-hinweis">
    <div class="container">
      <div class="architect-box">
        <div style="max-width:780px;">
          <div class="section-kicker kicker-light" style="margin-bottom:6px;" data-slot="arch_kicker">MANNSCHAFTS-AUSBAU: 1 VON 33 TEAMS (3 %) ALS MUSTER-VORLAGE FERTIGGESTELLT — 32 TEAMS NOCH OFFEN</div>
          <h1 style="color:#FFFFFF;font-size:clamp(1.45rem,2.5vw,2rem);font-weight:800;margin-bottom:8px;" data-slot="arch_title">
            1 Muster-Team ausgearbeitet (Herren 1) — 32 Mannschaften im Drahtgitter-Rohbau
          </h1>
          <p style="font-size:0.9rem;color:#E2E8F0;line-height:1.55;margin-bottom:14px;" data-slot="arch_desc">
            Um die künftige Qualität am echten Beispiel zu demonstrieren, ist in dieser Vorschau exakt <strong>1 von 33 Mannschaften (Herren 1 · 3 %)</strong> komplett mit Original-Mannschaftsfoto, den 3 Trainern und allen 19 Spielern ausgearbeitet. Alle weiteren <strong>32 Mannschaften (97 %)</strong> — inklusive <em>Frauen 1–3</em>, <em>Herren 2</em>, <em>Senioren</em> und <em>25 Nachwuchs-Teams</em> — stehen unten als <strong>gestrichelte Drahtgitter-Rohbau-Kacheln</strong> bereit und werden erst nach Auftragserteilung migriert.
          </p>
          <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:rgba(15,23,42,0.75);border:1px dashed #F59E0B;padding:8px 12px;border-radius:var(--radius-sm);">
            <div class="wp-v2-progress-track" style="width:140px;">
              <div class="wp-v2-progress-fill" style="width:6%;"></div>
            </div>
            <span style="font-family:'Montserrat',sans-serif;font-size:0.75rem;font-weight:800;color:#FDE68A;">
              1 / 33 Teams fertig (3 %) · 32 Teams im Rohbau (~480 Spielerporträts offen)
            </span>
          </div>
        </div>
        <div style="display:flex;flex-direction:column;gap:8px;flex-shrink:0;">
          <a href="#alle-teams-matrix" class="btn-cta btn-cta-gold btn-sm">Zu den 32 offenen Rohbau-Teams</a>
          <a href="/fcschlieren/herren-1.html" class="btn-cta btn-cta-ghost-light btn-sm">Variante 1 (inkl. Frauen 1) vergleichen</a>
        </div>
      </div>
    </div>
  </section>

  <!-- MUSTER-TEAM SEKTION (NUR HERREN 1 AUSGEARBEITET · 1 VON 33) -->
  <section id="muster-team-detail" data-section="muster-team-detail">
    <div class="container">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;margin-bottom:20px;">
        <div class="team-switcher-bar" style="margin-bottom:0;">
          <span class="team-switch-btn active" style="cursor:default;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Muster-Team 1/33: Herren 1 (Fertig ausgearbeitet)</span>
            <span class="team-switch-badge">19 Spieler · Muster</span>
          </span>
          <a href="#alle-teams-matrix" class="team-switch-btn" style="border:1px dashed #94A3B8;background-color:#E2E8F0;color:#334155;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            <span>Teams 2–33: Frauen 1, Herren 2 &amp; 30 weitere (Im Rohbau · Noch offen)</span>
          </a>
        </div>

        <div style="font-size:0.84rem;color:var(--text-muted);font-weight:600;">
          Sportchef Aktive: <strong>Zoran Perak</strong> (z.perak@fcschlieren.ch · 076 264 20 22)
        </div>
      </div>

      <!-- EINZIGES AUSGEARBEITETES MUSTER-TEAM IN V2: HERREN 1 -->
      <div class="team-pane active" id="paneHerren1">
{herren1_pane_only}
  </section>

  <!-- ALLE 33 MANNSCHAFTEN: 1 MUSTER FERTIG + 32 GESTRICHELTE DRAHTGITTER-ROHBAU-KACHELN -->
  <section id="alle-teams-matrix" data-section="alle-teams-matrix" style="background-color:#FFFFFF;border-top:2px dashed #64748B;">
    <div class="container">
      <div class="section-head">
        <div class="section-kicker" data-slot="matrix_kicker">BAUPLAN-RASTER · 1 MUSTER-TEAM FERTIG (3 %) vs. 32 TEAMS IM ROHBAU (97 %)</div>
        <h2 class="section-title" data-slot="matrix_title">1 ausgearbeitetes Muster-Team &amp; 32 unbefüllte Rohbau-Kacheln.</h2>
        <p class="section-desc" data-slot="matrix_desc">
          Ausschliesslich <strong>Herren 1 (1 von 33 Teams)</strong> ist oben als Prototyp-Musterhaus ausgearbeitet. Alle weiteren <strong>32 Mannschaften</strong> (inklusive <strong>Frauen 1–3</strong>, <strong>Herren 2</strong>, <strong>Senioren</strong> und allen <strong>25 Nachwuchs-Teams</strong>) stehen hier als gestrichelte Drahtgitter-Rohbauten und werden erst im Hauptauftrag migriert.
        </p>
      </div>

      <!-- Gruppe 1: Aktive Herren & Senioren (1 Muster fertig + 4 Rohbau) -->
      <div class="matrix-group-block">
        <div class="matrix-group-header">
          <h3 style="font-size:1.18rem;font-weight:800;">1. Aktive Herren &amp; Senioren (1 Muster fertig · 4 Teams im Rohbau)</h3>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Leitung: Zoran Perak (z.perak@fcschlieren.ch · 076 264 20 22)</span>
        </div>
        <div class="matrix-grid">
          <button type="button" class="matrix-team-btn live-built" onclick="window.scrollTo({{top: 220, behavior: 'smooth'}});">
            <div class="matrix-team-top">
              <span class="matrix-team-name">Herren 1</span>
              <span class="matrix-status-pill pill-live">1/33 Muster fertig</span>
            </div>
            <span style="font-size:0.78rem;color:var(--text-body);font-weight:600;">Als einziges Muster-Team ausgearbeitet (3 Trainer &amp; 19 Spieler oben sichtbar)</span>
          </button>
{make_locked_team_tile("Herren 2", "Rohbau-Team: Herren 2", "Aktive Herren (2. Mannschaft)", "Zoran Perak (z.perak@fcschlieren.ch · 076 264 20 22)", "2. Mannschaft")}
{make_locked_team_tile("Senioren 30+", "Rohbau-Team: Senioren 30+", "Senioren-Abteilung FC Schlieren", "Zoran Perak &amp; Roger Mehr (r.mehr@fcschlieren.ch)", "Senioren 30+")}
{make_locked_team_tile("Senioren 40+", "Rohbau-Team: Senioren 40+", "Senioren-Abteilung FC Schlieren", "Zoran Perak &amp; Roger Mehr (r.mehr@fcschlieren.ch)", "Senioren 40+")}
{make_locked_team_tile("Senioren 50+", "Rohbau-Team: Senioren 50+", "Senioren-Abteilung FC Schlieren", "Zoran Perak &amp; Roger Mehr (r.mehr@fcschlieren.ch)", "Senioren 50+")}
        </div>
      </div>

      <!-- Gruppe 2: Aktive Frauen (Alle 3 Teams im Rohbau in V2!) -->
      <div class="matrix-group-block">
        <div class="matrix-group-header">
          <h3 style="font-size:1.18rem;font-weight:800;">2. Aktive Frauen (0 von 3 Teams migriert · Alle 3 im Rohbau)</h3>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Leitung: Zoran Perak &amp; Konstantinos Vettas (costa.vettas@bluewin.ch)</span>
        </div>
        <div class="matrix-grid">
{make_locked_team_tile("Frauen 1", "Rohbau-Team: Frauen 1", "Aktive Frauen (1. Mannschaft)", "Konstantinos Vettas &amp; Sergio Zamora (costa.vettas@bluewin.ch)", "1. Mannschaft Frauen")}
{make_locked_team_tile("Frauen 2", "Rohbau-Team: Frauen 2", "Aktive Frauen (2. Mannschaft)", "Zoran Perak (z.perak@fcschlieren.ch · 076 264 20 22)", "2. Mannschaft Frauen")}
{make_locked_team_tile("Frauen 3", "Rohbau-Team: Frauen 3", "Aktive Frauen (3. Mannschaft)", "Zoran Perak (z.perak@fcschlieren.ch · 076 264 20 22)", "3. Mannschaft Frauen")}
        </div>
      </div>

      <!-- Gruppe 3: Junioren A bis G (Alle 17 Teams im Rohbau) -->
      <div class="matrix-group-block">
        <div class="matrix-group-header">
          <h3 style="font-size:1.18rem;font-weight:800;">3. Junioren A bis G (0 von 17 Teams migriert · Alle 17 im Rohbau)</h3>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Leiter Junioren: Luigi Schiavano (l.schiavano@fcschlieren.ch · 079 109 52 88)</span>
        </div>
        <div class="matrix-grid">
{make_locked_team_tile("Junioren A", "Rohbau-Team: Junioren A", "Junioren-Abteilung (U19/U20)", "Luigi Schiavano (l.schiavano@fcschlieren.ch)", "A-Junioren 11er")}
{make_locked_team_tile("B1 Junioren", "Rohbau-Team: B1 Junioren", "Junioren-Abteilung B", "Luigi Schiavano (l.schiavano@fcschlieren.ch)", "B-Junioren 11er")}
{make_locked_team_tile("B2 Junioren", "Rohbau-Team: B2 Junioren", "Junioren-Abteilung B", "Luigi Schiavano (l.schiavano@fcschlieren.ch)", "B-Junioren 11er")}
{make_locked_team_tile("C1 Junioren", "Rohbau-Team: C1 Junioren", "Junioren-Abteilung C", "Luigi Schiavano (l.schiavano@fcschlieren.ch)", "C-Junioren 11er")}
{make_locked_team_tile("C2 Junioren", "Rohbau-Team: C2 Junioren", "Junioren-Abteilung C", "Luigi Schiavano (l.schiavano@fcschlieren.ch)", "C-Junioren 11er")}
{make_locked_team_tile("C3 Junioren", "Rohbau-Team: C3 Junioren", "Junioren-Abteilung C", "Luigi Schiavano (l.schiavano@fcschlieren.ch)", "C-Junioren 11er")}
{make_locked_team_tile("D1 Junioren", "Rohbau-Team: D1 Junioren (9er)", "Koordination D &amp; E Junioren", "Oscar Otero &amp; Luigi Schiavano", "D-Junioren 9er")}
{make_locked_team_tile("D2 Junioren", "Rohbau-Team: D2 Junioren (9er)", "Koordination D &amp; E Junioren", "Oscar Otero &amp; Luigi Schiavano", "D-Junioren 9er")}
{make_locked_team_tile("D1 (7er) Junioren", "Rohbau-Team: D1 (7er) Junioren", "Koordination D &amp; E Junioren", "Oscar Otero &amp; Luigi Schiavano", "D-Junioren 7er")}
{make_locked_team_tile("D2 (7er) Junioren", "Rohbau-Team: D2 (7er) Junioren", "Koordination D &amp; E Junioren", "Oscar Otero &amp; Luigi Schiavano", "D-Junioren 7er")}
{make_locked_team_tile("E1 Junioren", "Rohbau-Team: E1 Junioren", "Koordination D &amp; E Junioren", "Oscar Otero &amp; Luigi Schiavano", "E-Junioren")}
{make_locked_team_tile("E2 Junioren", "Rohbau-Team: E2 Junioren", "Koordination D &amp; E Junioren", "Oscar Otero &amp; Luigi Schiavano", "E-Junioren")}
{make_locked_team_tile("E3 Junioren", "Rohbau-Team: E3 Junioren", "Koordination D &amp; E Junioren", "Oscar Otero &amp; Luigi Schiavano", "E-Junioren")}
{make_locked_team_tile("F1 Junioren", "Rohbau-Team: F1 Junioren", "Koordination F &amp; G Junioren", "Gianfranco Gennaro &amp; Luigi Schiavano", "F-Junioren")}
{make_locked_team_tile("F2 Junioren", "Rohbau-Team: F2 Junioren", "Koordination F &amp; G Junioren", "Gianfranco Gennaro &amp; Luigi Schiavano", "F-Junioren")}
{make_locked_team_tile("F3 Junioren", "Rohbau-Team: F3 Junioren", "Koordination F &amp; G Junioren", "Gianfranco Gennaro &amp; Luigi Schiavano", "F-Junioren")}
{make_locked_team_tile("Junioren G", "Rohbau-Team: Junioren G &amp; Fussballschule", "Koordination F &amp; G Junioren", "Gianfranco Gennaro &amp; Luigi Schiavano", "Jg. 2020–2022")}
        </div>
      </div>

      <!-- Gruppe 4: Juniorinnen U16 bis F (Alle 8 Teams im Rohbau) -->
      <div class="matrix-group-block" style="margin-bottom:0;">
        <div class="matrix-group-header">
          <h3 style="font-size:1.18rem;font-weight:800;">4. Juniorinnen U16 bis F (0 von 8 Teams migriert · Alle 8 im Rohbau)</h3>
          <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Leiter Juniorinnen: Mario De Meo (m.demeo@fcschlieren.ch · 079 354 37 23)</span>
        </div>
        <div class="matrix-grid">
{make_locked_team_tile("Frauen U16", "Rohbau-Team: Frauen U16", "Juniorinnen-Abteilung (Leistungsstufe)", "Mario De Meo &amp; Luca Mussolin", "Juniorinnen U16")}
{make_locked_team_tile("B Juniorinnen", "Rohbau-Team: B Juniorinnen", "Juniorinnen-Abteilung B", "Mario De Meo (m.demeo@fcschlieren.ch)", "B-Juniorinnen")}
{make_locked_team_tile("C Juniorinnen", "Rohbau-Team: C Juniorinnen", "Juniorinnen-Abteilung C", "Mario De Meo (m.demeo@fcschlieren.ch)", "C-Juniorinnen")}
{make_locked_team_tile("U14 Mädchen", "Rohbau-Team: U14 Mädchen", "Juniorinnen-Abteilung U14", "Mario De Meo &amp; Luca Mussolin", "U14 Mädchen")}
{make_locked_team_tile("D9er Juniorinnen", "Rohbau-Team: D9er Juniorinnen", "Juniorinnen-Abteilung D", "Mario De Meo (m.demeo@fcschlieren.ch)", "D-Juniorinnen 9er")}
{make_locked_team_tile("D7er Juniorinnen", "Rohbau-Team: D7er Juniorinnen", "Juniorinnen-Abteilung D", "Mario De Meo (m.demeo@fcschlieren.ch)", "D-Juniorinnen 7er")}
{make_locked_team_tile("E Juniorinnen", "Rohbau-Team: E Juniorinnen", "Koordination E &amp; F Juniorinnen", "Angela Paradiso &amp; Mario De Meo", "E-Juniorinnen")}
{make_locked_team_tile("F Juniorinnen", "Rohbau-Team: F Juniorinnen", "Koordination E &amp; F Juniorinnen", "Angela Paradiso &amp; Mario De Meo", "F-Juniorinnen")}
        </div>
      </div>
    </div>
  </section>
"""

V2_KONTAKT_BODY = v1.KONTAKT_BODY.replace(
    "source_page: 'preview-fcschlieren/kontakt.html'",
    "source_page: 'preview-fcschlieren-v2/kontakt.html'"
)

pages_to_write = [
    ("index.html", "FC Schlieren (V2 Bauplan-Modus: 6 % Prototyp / 94 % Rohbau) | Architektur-Studie", "startseite", V2_INDEX_BODY, ""),
    ("herren-1.html", "Muster-Team Herren 1 (1/33 fertig) & 32 Rohbau-Teams | FC Schlieren V2", "teams", V2_HERREN_1_BODY, v1.HERREN_1_CSS),
    ("kontakt.html", "Smart-Anfrage Live-Demo (Ausbaustufe 6 % Prototyp) | FC Schlieren V2", "kontakt", V2_KONTAKT_BODY, v1.KONTAKT_CSS),
]

for fname, title, nav_key, body, extra_css in pages_to_write:
    full_html = render_v2_shell(fname, title, nav_key, body, extra_css)
    (SITE_DIR / fname).write_text(full_html, encoding="utf-8")
    print(f"Wrote V2 {fname} ({len(full_html)} bytes)")

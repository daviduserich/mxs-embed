#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator für Atelier Piede – Praxis für Fusspflege (Christina Widmer – von Moos, 5742 Kölliken AG)
Pragmatischer, edler One-Pager «Flyer = Webseite» unter preview-atelier-piede/.

Regel-Konformität:
- UI-LAYOUT-RULES.md (Canary: UI-LAYOUT-2026-V1, #UI-01, #UI-02, #UI-10, #UI-13, #UI-14, #UI-16, #UI-23)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1, 100 % ss statt Eszett, 0 \\u2014, Einser-Ausschreibungs-Regel)
- BACKEND-DB-RULES.md (Canary: BACKEND-DB-2026-V1)
- DEPLOY-MAP.md (Canary: DEPLOY-MAP-2026-V1)
"""

from __future__ import annotations

import html
import json
from pathlib import Path
from PIL import Image

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
SITE_DIR = BASE_DIR / "preview-atelier-piede"

# --- Lucide Inline SVGs (100 % Lucide SVG Pflicht, 0 Unicode-Emojis) ---
SVG_PHONE = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
SVG_MAIL = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>'
SVG_MAP_PIN = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>'
SVG_MSG = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>'
SVG_CHECK = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
SVG_CLOCK = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'
SVG_HOME = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>'
SVG_ARROW = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>'
SVG_FILE = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/></svg>'
SVG_MENU = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>'
SVG_SEND = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>'


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def sanitize_ch(text: str) -> str:
    """Erzwingt 100 % ss und verhindert englische Em-Dashes im Satzbau (#LANG-01)."""
    text = text.replace("\u00df", "ss")
    text = text.replace(".\u2014", ".—")
    text = text.replace("\u2014", "\u2013")
    return text


def img_dims(rel_path: str) -> tuple[int, int]:
    p = SITE_DIR / rel_path
    if p.exists():
        with Image.open(p) as im:
            return im.size
    return (800, 800)


COMMON_CSS = """
    :root {
      --bg-page: #FAF4EC;
      --bg-card: #F3E7DA;
      --bg-elevated: #FDF9F4;
      --espresso: #4A3327;
      --espresso-dark: #3E271C;
      --accent: #9C643B;
      --accent-hover: #7F4F2C;
      --text-main: #3E271C;
      --text-muted: #6E5445;
      --text-on-dark: #FAF4EC;
      --text-on-dark-muted: #E6D6C5;
      --border-light: #E2D1BE;
      --border-dark: rgba(250, 244, 236, 0.22);
      --radius-sm: 4px;
      --radius-md: 8px;
      --maxw: 1100px;
      --font-head: 'Cormorant Garamond', Georgia, serif;
      --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    @media (prefers-reduced-motion: no-preference) {
      @view-transition { navigation: auto; }
    }

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; overflow-x: clip; }
    body {
      font-family: var(--font-body);
      background: var(--bg-page);
      color: var(--text-main);
      line-height: 1.62;
      -webkit-font-smoothing: antialiased;
      overflow-x: clip;
      font-variant-numeric: tabular-nums;
      caret-color: var(--accent);
    }
    ::selection { background: rgba(156, 100, 59, 0.2); color: var(--espresso-dark); }
    :focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }

    a { color: inherit; text-decoration: none; text-underline-offset: 3px; }
    img { max-width: 100%; height: auto; display: block; }
    button { font-family: inherit; }

    .wrap {
      max-width: var(--maxw);
      margin: 0 auto;
      padding: 0 24px;
      width: 100%;
    }

    /* Header (1-Zeilen-Gesetz #UI-02) */
    .site-header {
      position: sticky;
      top: 0;
      z-index: 60;
      background: rgba(250, 244, 236, 0.96);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border-light);
    }
    .header-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      min-height: 74px;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      flex: 0 0 auto;
    }
    .brand img {
      height: 44px;
      width: auto;
      object-fit: contain;
    }
    .brand-text {
      display: flex;
      flex-direction: column;
      line-height: 1.15;
    }
    .brand-name {
      font-family: var(--font-head);
      font-size: 21px;
      font-weight: 700;
      letter-spacing: 0.06em;
      color: var(--espresso-dark);
      white-space: nowrap;
    }
    .brand-sub {
      font-size: 11px;
      font-weight: 500;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--text-muted);
      white-space: nowrap;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 24px;
      flex-wrap: nowrap;
    }
    .nav-links a {
      font-size: 14px;
      font-weight: 500;
      color: var(--text-main);
      white-space: nowrap;
      padding: 6px 0;
      border-bottom: 2px solid transparent;
      transition: color 0.15s ease, border-color 0.15s ease;
    }
    .nav-links a:hover {
      color: var(--accent);
      border-bottom-color: var(--accent);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 12px;
      flex: 0 0 auto;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      min-height: 44px;
      padding: 10px 18px;
      border-radius: var(--radius-md);
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease;
      white-space: nowrap;
    }
    .btn-primary {
      background: var(--espresso);
      color: var(--text-on-dark);
      border-color: var(--espresso);
    }
    .btn-primary:hover {
      background: var(--espresso-dark);
      border-color: var(--espresso-dark);
    }
    .btn-secondary {
      background: var(--bg-elevated);
      color: var(--espresso-dark);
      border-color: var(--accent);
    }
    .btn-secondary:hover {
      background: var(--bg-card);
      border-color: var(--espresso);
    }
    .btn-on-dark {
      background: var(--bg-page);
      color: var(--espresso-dark);
      border-color: var(--bg-page);
    }
    .btn-on-dark:hover {
      background: var(--bg-card);
    }
    .btn-on-dark-outline {
      background: rgba(250, 244, 236, 0.08);
      color: var(--text-on-dark);
      border-color: rgba(250, 244, 236, 0.36);
    }
    .btn-on-dark-outline:hover {
      background: rgba(250, 244, 236, 0.16);
      border-color: var(--bg-page);
    }

    .burger-btn {
      display: none;
      align-items: center;
      justify-content: center;
      width: 44px;
      height: 44px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-light);
      background: var(--bg-elevated);
      color: var(--espresso-dark);
      cursor: pointer;
    }
    .mobile-nav {
      display: none;
      flex-direction: column;
      gap: 4px;
      padding: 12px 24px 18px;
      background: var(--bg-page);
      border-top: 1px solid var(--border-light);
    }
    @media (max-width: 980px) { .mobile-nav.open { display: flex; } }
    @media (min-width: 981px) { .mobile-nav { display: none !important; } }
    .mobile-nav a {
      padding: 12px 10px;
      font-size: 15px;
      font-weight: 500;
      border-radius: var(--radius-md);
      color: var(--espresso-dark);
    }
    .mobile-nav a:hover { background: var(--bg-card); }

    /* Kicker (#UI-01: pur linksbuendig ohne Vorstrich) */
    .section-kicker {
      display: block;
      font-family: var(--font-body);
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 10px;
      background: transparent;
      border: none;
      padding: 0;
    }

    /* Hero Section (#UI-02 Bottom-Edge Baseline Lock) */
    .hero-section {
      padding: 52px 0 56px;
      background: var(--bg-page);
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: 44px;
      align-items: stretch;
    }
    .hero-left {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 28px;
    }
    .hero-title {
      font-family: var(--font-head);
      font-size: clamp(46px, 5.2vw, 66px);
      font-weight: 600;
      font-style: italic;
      line-height: 1.04;
      color: var(--espresso-dark);
      margin-bottom: 14px;
      letter-spacing: -0.01em;
    }
    .hero-subtitle {
      font-family: var(--font-head);
      font-size: clamp(22px, 2.4vw, 28px);
      font-weight: 500;
      font-style: italic;
      line-height: 1.3;
      color: var(--espresso);
      margin-bottom: 18px;
    }
    .hero-lead {
      font-size: 16px;
      color: var(--text-muted);
      max-width: 50ch;
      margin-bottom: 26px;
    }
    .hero-ctas {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .trust-row {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 12px;
    }
    .trust-card {
      background: var(--bg-card);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 14px 12px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      gap: 4px;
    }
    .trust-title {
      font-size: 13px;
      font-weight: 600;
      color: var(--espresso-dark);
      line-height: 1.3;
    }
    .trust-sub {
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.35;
    }

    .hero-media {
      height: 100%;
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border-light);
      background: var(--bg-card);
    }
    .hero-media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 45%;
    }

    /* Sections */
    .section-block {
      padding: 56px 0;
      border-top: 1px solid var(--border-light);
    }
    .section-header {
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      gap: 20px;
      flex-wrap: wrap;
      margin-bottom: 28px;
    }
    .section-title {
      font-family: var(--font-head);
      font-size: clamp(32px, 3.6vw, 42px);
      font-weight: 600;
      line-height: 1.12;
      color: var(--espresso-dark);
    }
    .pdf-link {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      font-size: 13px;
      font-weight: 600;
      color: var(--accent);
      padding: 8px 14px;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      background: var(--bg-elevated);
      transition: background 0.15s ease, border-color 0.15s ease;
    }
    .pdf-link:hover {
      background: var(--bg-card);
      border-color: var(--accent);
    }

    /* Treatment Cards (#UI-14 S-15, S-31, S-34) */
    .treatments-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 20px;
      align-items: stretch;
    }
    .treatment-card {
      background: var(--bg-card);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 26px 24px;
      display: flex;
      flex-direction: column;
      height: 100%;
    }
    .treatment-top {
      padding-bottom: 18px;
      border-bottom: 1px solid var(--border-light);
      margin-bottom: 18px;
    }
    .treatment-name {
      font-family: var(--font-head);
      font-size: 28px;
      font-weight: 700;
      color: var(--espresso-dark);
      line-height: 1.15;
      margin-bottom: 6px;
    }
    .treatment-meta {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 12px;
    }
    .treatment-price {
      font-family: var(--font-head);
      font-size: 26px;
      font-weight: 700;
      color: var(--espresso);
      font-variant-numeric: tabular-nums;
    }
    .treatment-duration {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 13px;
      font-style: italic;
      color: var(--text-muted);
    }
    .treatment-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 24px;
    }
    .treatment-list li {
      display: flex;
      align-items: flex-start;
      gap: 9px;
      font-size: 15px;
      color: var(--text-main);
      line-height: 1.45;
    }
    .treatment-list li svg {
      flex: 0 0 auto;
      margin-top: 3px;
      color: var(--accent);
    }
    .treatment-cta {
      margin-top: auto;
      width: 100%;
    }

    /* Mobile Fusspflege Banner (#mobil) */
    .mobile-care-card {
      margin-top: 22px;
      background: var(--bg-card);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 28px 28px;
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: 28px;
      align-items: center;
    }
    .mobile-care-head {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .mobile-care-title-row {
      display: flex;
      align-items: baseline;
      gap: 14px;
      flex-wrap: wrap;
    }
    .mobile-care-title {
      font-family: var(--font-head);
      font-size: 28px;
      font-weight: 700;
      color: var(--espresso-dark);
      line-height: 1.15;
    }
    .mobile-care-price {
      display: inline-block;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.04em;
      color: var(--espresso-dark);
      background: var(--bg-elevated);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-sm);
      padding: 4px 10px;
    }
    .mobile-care-desc {
      font-size: 15px;
      color: var(--text-muted);
      max-width: 48ch;
    }
    .mobile-care-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .mobile-care-list li {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 15px;
      font-weight: 500;
      color: var(--espresso-dark);
    }
    .mobile-care-list li svg {
      flex: 0 0 auto;
      margin-top: 3px;
      color: var(--accent);
    }

    /* Dark Espresso Contact & Appointment Section (#termin) */
    .contact-section {
      padding: 60px 0;
      background: var(--espresso);
      color: var(--text-on-dark);
    }
    .contact-grid {
      display: grid;
      grid-template-columns: 0.95fr 1.05fr;
      gap: 40px;
      align-items: stretch;
    }
    .contact-info {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 24px;
    }
    .contact-heading {
      font-family: var(--font-head);
      font-size: clamp(34px, 3.8vw, 44px);
      font-weight: 600;
      font-style: italic;
      line-height: 1.1;
      color: var(--text-on-dark);
      margin-bottom: 12px;
    }
    .owner-name {
      font-size: 19px;
      font-weight: 600;
      color: var(--text-on-dark);
      margin-bottom: 2px;
    }
    .owner-role {
      font-size: 15px;
      color: var(--text-on-dark-muted);
      margin-bottom: 18px;
    }
    .address-block {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 15px;
      color: var(--text-on-dark);
      padding: 14px 16px;
      border-radius: var(--radius-md);
      background: rgba(62, 39, 28, 0.55);
      border: 1px solid var(--border-dark);
      margin-bottom: 18px;
    }
    .address-block svg {
      flex: 0 0 auto;
      margin-top: 3px;
      color: #E6C7A8;
    }
    .contact-actions {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 10px;
    }
    .contact-actions .btn {
      width: 100%;
      justify-content: flex-start;
      padding: 10px 14px;
    }

    /* Standard Terminanfrage-Formular (CHF 35.—/Mt. Basis) */
    .form-card {
      background: var(--bg-page);
      color: var(--text-main);
      border-radius: var(--radius-md);
      padding: 28px 26px;
      border: 1px solid var(--border-light);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .form-title {
      font-family: var(--font-head);
      font-size: 26px;
      font-weight: 700;
      color: var(--espresso-dark);
      margin-bottom: 4px;
    }
    .form-sub {
      font-size: 14px;
      color: var(--text-muted);
      margin-bottom: 18px;
    }
    .form-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 14px;
    }
    .field {
      display: flex;
      flex-direction: column;
      gap: 5px;
      margin-bottom: 14px;
    }
    .field label {
      font-size: 13px;
      font-weight: 600;
      color: var(--espresso-dark);
    }
    .field input,
    .field select,
    .field textarea {
      width: 100%;
      min-height: 44px;
      padding: 10px 12px;
      border-radius: var(--radius-md);
      border: 1px solid #CBB69F;
      background: #FFFFFF;
      color: var(--espresso-dark);
      font-family: inherit;
      font-size: 15px;
      transition: border-color 0.15s ease;
    }
    .field textarea {
      min-height: 88px;
      resize: vertical;
    }
    .field input:focus,
    .field select:focus,
    .field textarea:focus {
      outline: none;
      border-color: var(--accent);
      box-shadow: 0 0 0 2px rgba(156, 100, 59, 0.18);
    }
    .field input:user-invalid,
    .field select:user-invalid {
      border-color: #B42318;
    }
    .check-row {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 13px;
      color: var(--text-muted);
      margin-bottom: 16px;
      cursor: pointer;
    }
    .check-row input {
      width: 18px;
      height: 18px;
      margin-top: 2px;
      accent-color: var(--espresso);
      flex: 0 0 auto;
    }
    .form-feedback {
      display: none;
      margin-top: 12px;
      padding: 12px 14px;
      border-radius: var(--radius-md);
      font-size: 14px;
      font-weight: 500;
    }
    .form-feedback.ok {
      display: block;
      background: #ECFDF3;
      color: #065F46;
      border: 1px solid #A7F3D0;
    }
    .form-feedback.err {
      display: block;
      background: #FEF2F2;
      color: #991B1B;
      border: 1px solid #FECACA;
    }

    /* Footer */
    .site-footer {
      background: var(--espresso-dark);
      color: var(--text-on-dark-muted);
      padding: 34px 0;
      border-top: 1px solid var(--border-dark);
    }
    .footer-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      flex-wrap: wrap;
    }
    .footer-brand {
      font-size: 14px;
      color: var(--text-on-dark);
    }
    .footer-links {
      display: flex;
      align-items: center;
      gap: 18px;
      flex-wrap: wrap;
      font-size: 13px;
    }
    .footer-links a:hover {
      color: var(--text-on-dark);
      text-decoration: underline;
    }

    /* Mobile Sticky Bar (#UI-13) */
    .mobile-sticky-bar {
      display: none;
      position: fixed;
      left: 0;
      right: 0;
      bottom: 0;
      z-index: 70;
      background: rgba(250, 244, 236, 0.98);
      border-top: 1px solid var(--border-light);
      padding: 10px 14px calc(10px + env(safe-area-inset-bottom, 0px));
      gap: 10px;
    }
    .mobile-sticky-bar .btn {
      flex: 1 1 0;
      min-height: 44px;
      font-size: 14px;
    }

    /* Legal Pages */
    .legal-hero {
      padding: 46px 0 28px;
      border-bottom: 1px solid var(--border-light);
    }
    .legal-box {
      background: var(--bg-card);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      padding: 32px 28px;
      max-width: 780px;
    }
    .legal-box h2 {
      font-family: var(--font-head);
      font-size: 24px;
      font-weight: 700;
      color: var(--espresso-dark);
      margin: 22px 0 8px;
    }
    .legal-box h2:first-child { margin-top: 0; }
    .legal-box p { font-size: 15px; color: var(--text-main); margin-bottom: 10px; }

    /* Responsive */
    @media (max-width: 980px) {
      .nav-links, .header-cta-desktop { display: none; }
      .burger-btn { display: inline-flex; }
      .hero-grid,
      .treatments-grid,
      .mobile-care-card,
      .contact-grid {
        grid-template-columns: 1fr;
      }
      .hero-media {
        max-height: 420px;
      }
    }
    @media (max-width: 640px) {
      .wrap { padding: 0 18px; }
      .hero-section { padding: 32px 0 38px; }
      .trust-row,
      .contact-actions,
      .form-grid {
        grid-template-columns: 1fr;
      }
      .field input,
      .field select,
      .field textarea {
        font-size: 16px;
      }
      .mobile-sticky-bar { display: flex; }
      .site-footer { padding-bottom: 92px; }
      .brand-sub { display: none; }
      .footer-links { gap: 8px; }
      .footer-links a, .legal-box a {
        display: inline-flex;
        align-items: center;
        min-height: 36px;
        padding: 6px 8px;
      }
    }
"""


def build_head(title: str, desc: str, noindex: bool = False) -> str:
    robots_meta = '<meta name="robots" content="noindex, nofollow">\n  ' if noindex else ''
    return f"""<!DOCTYPE html>
<html lang="de-CH" data-design-mode="evolution" data-expected-hero-polarity="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-Frame-Options" content="DENY">
  <meta http-equiv="X-XSS-Protection" content="1; mode=block">
  <meta name="referrer" content="no-referrer">
  {robots_meta}<title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <style>{COMMON_CSS}</style>
</head>"""


def build_header(is_subpage: bool = False) -> str:
    lw, lh = img_dims("images/logo-ap.png")
    prefix = "index.html" if is_subpage else ""
    return f"""  <header class="site-header">
    <div class="wrap">
      <div class="header-row">
        <a href="index.html" class="brand" aria-label="Atelier Piede Startseite">
          <img src="images/logo-ap.png" alt="Atelier Piede Monogramm-Logo" width="{lw}" height="{lh}" decoding="async">
          <span class="brand-text">
            <span class="brand-name" data-slot="brand_short">ATELIER PIEDE</span>
            <span class="brand-sub" data-slot="brand_subtitle">Praxis für Fusspflege</span>
          </span>
        </a>
        <nav class="nav-links" aria-label="Hauptnavigation">
          <a href="{prefix}#preise">Behandlungen &amp; Preise</a>
          <a href="{prefix}#mobil">Mobile Fusspflege</a>
          <a href="{prefix}#termin">Kontakt</a>
        </nav>
        <div class="header-actions">
          <a href="{prefix}#termin" class="btn btn-primary header-cta-desktop">{SVG_PHONE}<span>Termin vereinbaren</span></a>
          <button type="button" class="burger-btn" id="burgerBtn" aria-label="Menü öffnen" aria-expanded="false" onclick="toggleMobileNav()">{SVG_MENU}</button>
        </div>
      </div>
    </div>
    <div class="mobile-nav" id="mobileNav" role="navigation" aria-label="Mobile Navigation">
      <a href="{prefix}#preise" onclick="closeMobileNav()">Behandlungen &amp; Preise</a>
      <a href="{prefix}#mobil" onclick="closeMobileNav()">Mobile Fusspflege</a>
      <a href="{prefix}#termin" onclick="closeMobileNav()">Kontakt &amp; Termin</a>
      <a href="tel:+41799399988" onclick="closeMobileNav()">Anrufen: 079 939 99 88</a>
    </div>
  </header>"""


def build_footer(is_subpage: bool = False) -> str:
    prefix = "index.html" if is_subpage else ""
    return f"""  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-inner">
        <div class="footer-brand">
          <strong data-slot="footer_company">Atelier Piede · Praxis für Fusspflege</strong> · Christina Widmer – von Moos · Wiesenstrasse 44 · 5742 Kölliken
        </div>
        <div class="footer-links">
          <a href="{prefix}#preise">Behandlungen &amp; Preise</a>
          <a href="assets/atelier-piede-flyer.pdf" target="_blank" rel="noopener">Flyer als PDF</a>
          <a href="impressum.html">Impressum</a>
          <a href="datenschutz.html">Datenschutz</a>
        </div>
      </div>
    </div>
  </footer>
  <div class="mobile-sticky-bar" id="mobileStickyBar">
    <a href="tel:+41799399988" class="btn btn-secondary">{SVG_PHONE}<span>Anrufen</span></a>
    <a href="{prefix}#termin" class="btn btn-primary">{SVG_MSG}<span>Termin / WhatsApp</span></a>
  </div>
  <script>
    function toggleMobileNav() {{
      var nav = document.getElementById('mobileNav');
      var btn = document.getElementById('burgerBtn');
      if (!nav || !btn) return;
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    }}
    function closeMobileNav() {{
      var nav = document.getElementById('mobileNav');
      var btn = document.getElementById('burgerBtn');
      if (nav) nav.classList.remove('open');
      if (btn) btn.setAttribute('aria-expanded', 'false');
    }}
  </script>"""


def build_index_html() -> str:
    hw, hh = img_dims("images/hero-fusspflege.jpg")
    head = build_head(
        "Atelier Piede – Praxis für Fusspflege | Christina Widmer – von Moos, 5742 Kölliken",
        "Atelier Piede in 5742 Kölliken: Diplomierte Fusspflegerin Christina Widmer – von Moos. Behandlung in der Praxis oder mobil bei Ihnen zu Hause, im Heim oder Spital."
    )
    header = build_header(is_subpage=False)
    footer = build_footer(is_subpage=False)

    treatments = [
        {
            "key": "Small",
            "price": "CHF 79.–",
            "duration": "50 Minuten",
            "items": [
                "Fussbad",
                "Nägel kürzen und in Form bringen",
                "Hornhautbehandlung",
                "Entfernen von Druckstellen",
                "Füsse eincremen",
            ],
        },
        {
            "key": "Standard",
            "price": "CHF 89.–",
            "duration": "65 Minuten",
            "items": [
                "Fussbad",
                "Nägel kürzen und in Form bringen",
                "Hornhautbehandlung",
                "Entfernen von Druckstellen",
                "Fussmassage",
            ],
        },
        {
            "key": "Premium",
            "price": "CHF 115.–",
            "duration": "80 Minuten",
            "items": [
                "Ein Glas Prosecco und etwas zum Knabbern",
                "Fussbad",
                "Nägel kürzen und in Form bringen",
                "Hornhautbehandlung",
                "Entfernen von Druckstellen",
                "Fusspeeling",
                "Fussmassage",
            ],
        },
    ]

    cards_html = []
    for idx, t in enumerate(treatments, start=1):
        items_html = "\n".join(
            f'              <li>{SVG_CHECK}<span>{esc(item)}</span></li>'
            for item in t["items"]
        )
        cards_html.append(f"""          <article class="treatment-card">
            <div class="treatment-top">
              <h3 class="treatment-name" data-slot="treatment_{idx}_name">{esc(t["key"])}</h3>
              <div class="treatment-meta">
                <span class="treatment-price" data-slot="treatment_{idx}_price">{esc(t["price"])}</span>
                <span class="treatment-duration" data-slot="treatment_{idx}_duration">{SVG_CLOCK}<span>{esc(t["duration"])}</span></span>
              </div>
            </div>
            <ul class="treatment-list">
{items_html}
            </ul>
            <a href="#termin" class="btn btn-secondary treatment-cta" onclick="selectTreatment('{esc(t['key'])}')">Termin anfragen {SVG_ARROW}</a>
          </article>""")

    body = f"""<body>
{header}
  <main id="main-content">
    <section class="hero-section" id="top">
      <div class="wrap">
        <div class="hero-grid">
          <div class="hero-left">
            <div>
              <span class="section-kicker" data-slot="hero_kicker">ATELIER PIEDE · PRAXIS FÜR FUSSPFLEGE</span>
              <h1 class="hero-title" data-slot="hero_title">Fusspflege</h1>
              <p class="hero-subtitle" data-slot="hero_subtitle">Behandlung in der Praxis oder bei Ihnen zu Hause</p>
              <p class="hero-lead" data-slot="hero_lead">Sorgfältige, persönliche Fusspflege in ruhiger Atmosphäre an der Wiesenstrasse 44 in Kölliken oder direkt bei Ihnen vor Ort.</p>
              <div class="hero-ctas">
                <a href="#termin" class="btn btn-primary">{SVG_PHONE}<span>Termin vereinbaren</span></a>
                <a href="#preise" class="btn btn-secondary">Behandlungen &amp; Preise {SVG_ARROW}</a>
              </div>
            </div>
            <div class="trust-row">
              <div class="trust-card">
                <span class="trust-title" data-slot="trust_1_title">5742 Kölliken</span>
                <span class="trust-sub" data-slot="trust_1_sub">Wiesenstrasse 44</span>
              </div>
              <div class="trust-card">
                <span class="trust-title" data-slot="trust_2_title">Dipl. Fusspflegerin</span>
                <span class="trust-sub" data-slot="trust_2_sub">Christina Widmer – von Moos</span>
              </div>
              <div class="trust-card">
                <span class="trust-title" data-slot="trust_3_title">Praxis &amp; Mobil</span>
                <span class="trust-sub" data-slot="trust_3_sub">Auch im Heim oder Spital</span>
              </div>
            </div>
          </div>
          <div class="hero-media">
            <img src="images/hero-fusspflege.jpg" alt="Atelier Piede Fusspflege in warmer Spa-Atmosphäre mit Handtüchern, Kerzenlicht und wohltuender Fussmassage" width="{hw}" height="{hh}" fetchpriority="high" decoding="async" data-slot="hero_image">
          </div>
        </div>
      </div>
    </section>

    <section class="section-block" id="preise">
      <div class="wrap">
        <div class="section-header">
          <div>
            <span class="section-kicker" data-slot="prices_kicker">BEHANDLUNGEN &amp; PREISE</span>
            <h2 class="section-title" data-slot="prices_title">Behandlungen in der Praxis</h2>
          </div>
          <a href="assets/atelier-piede-flyer.pdf" class="pdf-link" target="_blank" rel="noopener">{SVG_FILE}<span>Original-Flyer als PDF</span></a>
        </div>
        <div class="treatments-grid">
{chr(10).join(cards_html)}
        </div>

        <div class="mobile-care-card" id="mobil">
          <div class="mobile-care-head">
            <span class="section-kicker" data-slot="mobile_kicker">AUSSERHALB DER PRAXIS</span>
            <div class="mobile-care-title-row">
              <h3 class="mobile-care-title" data-slot="mobile_title">Mobile Fusspflege</h3>
              <span class="mobile-care-price" data-slot="mobile_price">Nach Aufwand</span>
            </div>
            <p class="mobile-care-desc" data-slot="mobile_desc">Für alle, die ihre Fusspflege bequem in vertrauter Umgebung wünschen.</p>
            <div style="margin-top:6px;">
              <a href="#termin" class="btn btn-secondary" onclick="selectTreatment('Mobile Fusspflege')">{SVG_HOME}<span>Hausbesuch anfragen</span></a>
            </div>
          </div>
          <ul class="mobile-care-list">
            <li>{SVG_CHECK}<span>Bei Ihnen zu Hause</span></li>
            <li>{SVG_CHECK}<span>In Seniorenresidenzen und Pflegeheimen</span></li>
            <li>{SVG_CHECK}<span>Im Spital oder in einer Klinik</span></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="contact-section" id="termin">
      <div class="wrap">
        <div class="contact-grid">
          <div class="contact-info">
            <div>
              <h2 class="contact-heading" data-slot="contact_title">Termin vereinbaren</h2>
              <p class="owner-name" data-slot="owner_name">Christina Widmer – von Moos</p>
              <p class="owner-role" data-slot="owner_role">Diplomierte Fusspflegerin</p>
              <div class="address-block">
                {SVG_MAP_PIN}
                <div>
                  <div data-slot="street">Wiesenstrasse 44</div>
                  <div data-slot="city_zip">5742 Kölliken</div>
                </div>
              </div>
            </div>
            <div class="contact-actions">
              <a href="tel:+41799399988" class="btn btn-on-dark" data-slot="phone_cta">{SVG_PHONE}<span>079 939 99 88</span></a>
              <a href="https://wa.me/41799399988" target="_blank" rel="noopener" class="btn btn-on-dark-outline">{SVG_MSG}<span>WhatsApp schreiben</span></a>
              <a href="mailto:christina@atelierpiede.ch" class="btn btn-on-dark-outline" data-slot="email_cta">{SVG_MAIL}<span>christina@atelierpiede.ch</span></a>
              <a href="https://www.google.com/maps/search/?api=1&amp;query=Wiesenstrasse+44,+5742+K%C3%B6lliken" target="_blank" rel="noopener" class="btn btn-on-dark-outline">{SVG_MAP_PIN}<span>Route in Google Maps</span></a>
            </div>
          </div>

          <div class="form-card">
            <div>
              <h3 class="form-title">Terminanfrage senden</h3>
              <p class="form-sub">Gerne melde ich mich persönlich zur Terminbestätigung bei Ihnen.</p>
            </div>
            <form id="apContactForm" onsubmit="return submitApLead(event);" novalidate>
              <input type="text" id="wpHoneypot" name="website_url" form="wpTrapDetached" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0;">
              <div class="form-grid">
                <div class="field">
                  <label for="contactName">Ihr Name *</label>
                  <input type="text" id="contactName" name="name" autocomplete="name" required placeholder="Vor- und Nachname">
                </div>
                <div class="field">
                  <label for="contactPhone">Telefonnummer</label>
                  <input type="tel" id="contactPhone" name="tel" autocomplete="tel" placeholder="079 ...">
                </div>
              </div>
              <div class="form-grid">
                <div class="field">
                  <label for="contactEmail">E-Mail-Adresse *</label>
                  <input type="email" id="contactEmail" name="email" autocomplete="email" required placeholder="name@beispiel.ch">
                </div>
                <div class="field">
                  <label for="contactTreatment">Gewünschte Behandlung</label>
                  <select id="contactTreatment" name="topic">
                    <option value="Small (CHF 79.– · 50 Min.)">Small · CHF 79.–</option>
                    <option value="Standard (CHF 89.– · 65 Min.)" selected>Standard · CHF 89.–</option>
                    <option value="Premium (CHF 115.– · 80 Min.)">Premium · CHF 115.–</option>
                    <option value="Mobile Fusspflege (Nach Aufwand)">Mobile Fusspflege</option>
                  </select>
                </div>
              </div>
              <div class="field">
                <label for="contactMessage">Nachricht / Wunschtage</label>
                <textarea id="contactMessage" name="message" placeholder="z. B. Wunschtag, Tageszeit oder Hinweis für einen Hausbesuch"></textarea>
              </div>
              <label class="check-row">
                <input type="checkbox" id="contactConsent" required>
                <span>Ich bin einverstanden, dass meine Angaben zur Terminvereinbarung bearbeitet werden.</span>
              </label>
              <button type="submit" id="wpSubmitBtn" class="btn btn-primary" style="width:100%;">{SVG_SEND}<span>Terminanfrage absenden</span></button>
              <div id="wpFormOk" class="form-feedback" role="status"></div>
              <div id="wpFormErr" class="form-feedback" role="alert"></div>
            </form>
          </div>
        </div>
      </div>
    </section>
  </main>
{footer}
  <script>
    function selectTreatment(label) {{
      var sel = document.getElementById('contactTreatment');
      if (!sel) return;
      for (var i = 0; i < sel.options.length; i++) {{
        if (sel.options[i].value.indexOf(label) === 0) {{
          sel.selectedIndex = i;
          break;
        }}
      }}
    }}

    function submitApLead(ev) {{
      ev.preventDefault();
      var okBox = document.getElementById('wpFormOk');
      var errBox = document.getElementById('wpFormErr');
      if (okBox) {{ okBox.className = 'form-feedback'; okBox.textContent = ''; }}
      if (errBox) {{ errBox.className = 'form-feedback'; errBox.textContent = ''; }}

      var hp = (document.getElementById('wpHoneypot') && document.getElementById('wpHoneypot').value || '').trim();
      if (hp) {{
        if (okBox) {{ okBox.textContent = 'Vielen Dank für Ihre Anfrage.'; okBox.className = 'form-feedback ok'; }}
        return false;
      }}

      var name = (document.getElementById('contactName').value || '').trim();
      var phone = (document.getElementById('contactPhone').value || '').trim();
      var email = (document.getElementById('contactEmail').value || '').trim();
      var topic = (document.getElementById('contactTreatment').value || 'Standard').trim();
      var message = (document.getElementById('contactMessage').value || '').trim();
      var consent = document.getElementById('contactConsent');

      if (!name || !email || (consent && !consent.checked)) {{
        if (errBox) {{
          errBox.textContent = 'Bitte füllen Sie Name, E-Mail-Adresse und die Datenschutz-Bestätigung aus.';
          errBox.className = 'form-feedback err';
        }}
        return false;
      }}

      var btn = document.getElementById('wpSubmitBtn');
      if (btn) btn.disabled = true;

      fetch('/api/lead-submit', {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json' }},
        body: JSON.stringify({{
          client_slug: 'atelier-piede',
          preview_safe_mode: true,
          name: name,
          phone: phone,
          email: email,
          topic: topic,
          message: message
        }})
      }})
      .then(function(r) {{ return r.json().catch(function() {{ return {{ ok: r.ok }}; }}); }})
      .then(function() {{
        if (btn) btn.disabled = false;
        if (okBox) {{
          okBox.textContent = 'Vielen Dank. Ihre Terminanfrage wurde im Vorschau-Modus erfolgreich geprüft.';
          okBox.className = 'form-feedback ok';
        }}
        document.getElementById('apContactForm').reset();
      }})
      .catch(function() {{
        if (btn) btn.disabled = false;
        if (errBox) {{
          errBox.textContent = 'Es ist ein Fehler aufgetreten. Bitte rufen Sie direkt unter 079 939 99 88 an.';
          errBox.className = 'form-feedback err';
        }}
      }});
      return false;
    }}
  </script>
</body>
</html>
"""
    return sanitize_ch(head + "\n" + body)


def build_impressum_html() -> str:
    head = build_head(
        "Impressum | Atelier Piede – Praxis für Fusspflege",
        "Impressum von Atelier Piede – Praxis für Fusspflege, Christina Widmer – von Moos, Wiesenstrasse 44, 5742 Kölliken.",
        noindex=False,
    )
    header = build_header(is_subpage=True)
    footer = build_footer(is_subpage=True)
    body = f"""<body>
{header}
  <main id="main-content">
    <section class="legal-hero">
      <div class="wrap">
        <span class="section-kicker">Rechtliches</span>
        <h1 class="section-title">Impressum</h1>
      </div>
    </section>
    <section class="section-block" style="border-top:none;">
      <div class="wrap">
        <div class="legal-box">
          <h2>Verantwortliche Inhaberin</h2>
          <p><strong>Atelier Piede – Praxis für Fusspflege</strong><br>Christina Widmer – von Moos<br>Diplomierte Fusspflegerin<br>Wiesenstrasse 44<br>CH-5742 Kölliken<br>Schweiz</p>
          <h2>Kontakt</h2>
          <p>Telefon / WhatsApp: <a href="tel:+41799399988">079 939 99 88</a><br>E-Mail: <a href="mailto:christina@atelierpiede.ch">christina@atelierpiede.ch</a><br>Website: www.atelierpiede.ch</p>
          <h2>Haftungshinweis &amp; Urheberrechte</h2>
          <p>Alle Inhalte, Texte und Bilder auf dieser Website unterliegen dem Urheberrecht von Atelier Piede oder der jeweiligen Rechteinhaber. Trotz sorgfältiger Prüfung wird keine Gewähr für die Aktualität, Richtigkeit und Vollständigkeit der Angaben übernommen.</p>
        </div>
      </div>
    </section>
  </main>
{footer}
</body>
</html>
"""
    return sanitize_ch(head + "\n" + body)


def build_datenschutz_html() -> str:
    head = build_head(
        "Datenschutzerklärung | Atelier Piede – Praxis für Fusspflege",
        "Datenschutzerklärung gemäss Schweizer Datenschutzgesetz (DSG) für Atelier Piede, Wiesenstrasse 44, 5742 Kölliken.",
        noindex=False,
    )
    header = build_header(is_subpage=True)
    footer = build_footer(is_subpage=True)
    body = f"""<body>
{header}
  <main id="main-content">
    <section class="legal-hero">
      <div class="wrap">
        <span class="section-kicker">Datenschutz</span>
        <h1 class="section-title">Datenschutzerklärung</h1>
      </div>
    </section>
    <section class="section-block" style="border-top:none;">
      <div class="wrap">
        <div class="legal-box">
          <h2>1. Verantwortliche Stelle</h2>
          <p>Atelier Piede – Praxis für Fusspflege<br>Christina Widmer – von Moos<br>Wiesenstrasse 44<br>5742 Kölliken<br>E-Mail: christina@atelierpiede.ch<br>Telefon: 079 939 99 88</p>
          <h2>2. Erhebung und Bearbeitung von Personendaten</h2>
          <p>Beim Besuch dieser Website werden technisch notwendige Zugriffsdaten für einen sicheren Betrieb verarbeitet. Wenn Sie uns über das Terminformular, per E-Mail, Telefon oder WhatsApp kontaktieren, verwenden wir Ihre Angaben ausschliesslich zur Bearbeitung Ihrer Anfrage und Terminvereinbarung gemäss Schweizer Datenschutzgesetz (DSG).</p>
          <h2>3. Rechte der betroffenen Personen</h2>
          <p>Sie haben jederzeit das Recht auf Auskunft über Ihre gespeicherten Personendaten sowie auf Berichtigung oder Löschung im Rahmen der gesetzlichen Aufbewahrungspflichten.</p>
        </div>
      </div>
    </section>
  </main>
{footer}
</body>
</html>
"""
    return sanitize_ch(head + "\n" + body)


def build_404_html() -> str:
    head = build_head(
        "Seite nicht gefunden | Atelier Piede",
        "Die angeforderte Seite wurde nicht gefunden.",
        noindex=True,
    )
    header = build_header(is_subpage=True)
    footer = build_footer(is_subpage=True)
    body = f"""<body>
{header}
  <main id="main-content">
    <section class="section-block" style="border-top:none; padding: 80px 0;">
      <div class="wrap">
        <div class="legal-box">
          <span class="section-kicker">Hinweis 404</span>
          <h1 class="section-title" style="margin-bottom:12px;">Seite nicht gefunden</h1>
          <p style="margin-bottom:22px;">Die gewünschte Seite existiert leider nicht oder wurde verschoben. Gerne gelangen Sie direkt zurück zur Startseite von Atelier Piede.</p>
          <a href="index.html" class="btn btn-primary">Zurück zur Startseite {SVG_ARROW}</a>
        </div>
      </div>
    </section>
  </main>
{footer}
</body>
</html>
"""
    return sanitize_ch(head + "\n" + body)


def main() -> None:
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    (SITE_DIR / "index.html").write_text(build_index_html(), encoding="utf-8")
    (SITE_DIR / "impressum.html").write_text(build_impressum_html(), encoding="utf-8")
    (SITE_DIR / "datenschutz.html").write_text(build_datenschutz_html(), encoding="utf-8")
    (SITE_DIR / "404.html").write_text(build_404_html(), encoding="utf-8")

    company = {
        "company_name": "Atelier Piede – Praxis für Fusspflege",
        "brand_short": "ATELIER PIEDE",
        "legal_entity": "Atelier Piede – Christina Widmer – von Moos",
        "name": "Atelier Piede",
        "slug": "atelier-piede",
        "owner": "Christina Widmer – von Moos",
        "role": "Diplomierte Fusspflegerin",
        "city": "Kölliken",
        "canton": "AG",
        "street": "Wiesenstrasse 44",
        "zip": "5742",
        "phone": "+41 79 939 99 88",
        "phone_display": "079 939 99 88",
        "email": "christina@atelierpiede.ch",
        "website": "https://www.atelierpiede.ch",
        "partner_id": "jenny",
        "partner_name": "Jenny Ettle (JE-MI)",
        "design_mode": "one-pager-flyer-1to1",
        "footer_company": "Atelier Piede · Praxis für Fusspflege",
        "hero_kicker": "ATELIER PIEDE · PRAXIS FÜR FUSSPFLEGE",
        "hero_title": "Fusspflege",
        "hero_subtitle": "Behandlung in der Praxis oder bei Ihnen zu Hause",
        "hero_lead": "Sorgfältige, persönliche Fusspflege in ruhiger Atmosphäre an der Wiesenstrasse 44 in Kölliken oder direkt bei Ihnen vor Ort.",
        "brand_subtitle": "Praxis für Fusspflege",
        "owner_name": "Christina Widmer – von Moos",
        "owner_role": "Diplomierte Fusspflegerin",
        "city_zip": "5742 Kölliken",
        "contact_title": "Termin vereinbaren",
    }
    (SITE_DIR / "company.json").write_text(json.dumps(company, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    config = {
        "company_name": "Atelier Piede – Praxis für Fusspflege",
        "brand_short": "ATELIER PIEDE",
        "slug": "preview-atelier-piede",
        "public_slug": "atelier-piede",
        "cockpit_token": "atelierpiede2026",
        "template": "one-pager-flyer-1to1-v1",
        "partner_id": "jenny",
        "pages": ["index.html", "impressum.html", "datenschutz.html"],
    }
    (SITE_DIR / "config.json").write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    site = {
        "slug": "preview-atelier-piede",
        "public_slug": "atelier-piede",
        "token": "atelierpiede2026",
        "name": "Atelier Piede – Praxis für Fusspflege",
        "Updated": "2026-11-27",
        "PagesCount": 3,
    }
    (SITE_DIR / "site.json").write_text(json.dumps(site, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    design_vibe = {
        "mode": "flyer-1to1",
        "primary_accent": "#9C643B",
        "bg_dark": "#4A3327",
        "bg_light": "#FAF4EC",
        "bg_card": "#F3E7DA",
        "font_heading": "Cormorant Garamond",
        "font_body": "Inter",
    }
    (SITE_DIR / "design-vibe.json").write_text(json.dumps(design_vibe, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    source_dna = {
        "schema_version": "1.0.0",
        "slug": "atelier-piede",
        "source_url": "https://www.atelierpiede.ch/",
        "design_mode": "evolution",
        "target_hero_polarity": "light",
        "sommelier_decisions": {
            "polarity_decision": {
                "target_hero_polarity": "light"
            }
        },
    }
    (SITE_DIR / "source_visual_dna.json").write_text(json.dumps(source_dna, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Built preview-atelier-piede in {SITE_DIR}")


if __name__ == "__main__":
    main()

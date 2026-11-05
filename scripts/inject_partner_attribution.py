#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inject_partner_attribution.py — Zentraler Partner-Attributions- & Vorschau-Modal-Baustein
===========================================================================================
Stattet alle WebPilot-Showcases (preview-fcschlieren, preview-fcschlieren-v2,
preview-scfulenbach, preview-fcattiswil, preview-her11, preview-hochuli) idempotent aus mit:
  1. Platzierung A (Direkt unterhalb des 3-Schritte Smart-Anfrage-Formulars auf kontakt.html):
     Edle Partner-Empfehlungs-Leiste ("Powered by WebPilot · Beratung & Umsetzung: ...")
  2. Platzierung B (Im Footer jeder Unterseite in .footer-bottom):
     Klickbarer Partner-Button ("Powered by WebPilot · Partner: ... — Kontakt & Infos")
  3. Partner-Visitenkarten- & 15-Sekunden-Vorschau-Modal (#wpPartnerModal):
     - Teil 1: Direkte Partner-Visitenkarte mit 3 Direkt-Buttons (WhatsApp, Anruf, E-Mail)
     - Teil 2: 15-Sekunden-Schnellanfrage -> POST /api/lead-submit (client_slug: "webpilot_partner")
               inkl. 1-Seiten-PDF-Dossier & CC an David Huegli.

Design-System-Invarianzen (#UI-01, #UI-02, #UI-13, #UI-14, #LANG-01):
  - 100 % Lucide SVGs (0 Unicode-Emojis)
  - Strikte 2-Radius-Architektur (4px & 8px)
  - Keine JetBrains Mono & keine // auf Kunden-Webseiten
  - data-studio-ignore="true" zum Schutz der Studio-Cockpit Slot-Zaehlung
"""

import re
import json
import urllib.parse
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
LEAD_ROUTING_FILE = BASE_DIR / "config" / "lead_routing.json"

SHOWCASE_CONFIGS = {
    "preview-fcschlieren": {
        "routing_slug": "fcschlieren",
        "site_label": "FC Schlieren",
        "entity_hint": "den Fussballclub Schlieren",
        "accent_hex": "#006EAB",
        "navy_hex": "#0F172A",
        "font_heading": "'Montserrat', sans-serif",
    },
    "preview-fcschlieren-v2": {
        "routing_slug": "fcschlieren",
        "site_label": "FC Schlieren (V2 Studie)",
        "entity_hint": "den Fussballclub Schlieren",
        "accent_hex": "#006EAB",
        "navy_hex": "#0F172A",
        "font_heading": "'Montserrat', sans-serif",
    },
    "preview-scfulenbach": {
        "routing_slug": "scfulenbach",
        "site_label": "SC Fulenbach",
        "entity_hint": "den SC Fulenbach",
        "accent_hex": "#0F8A4B",
        "navy_hex": "#0B1528",
        "font_heading": "'Montserrat', sans-serif",
    },
    "preview-fcattiswil": {
        "routing_slug": "fcattiswil",
        "site_label": "FC Attiswil",
        "entity_hint": "den FC Attiswil",
        "accent_hex": "#C81E1E",
        "navy_hex": "#0F172A",
        "font_heading": "'Montserrat', sans-serif",
    },
    "preview-her11": {
        "routing_slug": "her11",
        "site_label": "HER11",
        "entity_hint": "HER11",
        "accent_hex": "#FF0066",
        "navy_hex": "#0B1A3B",
        "font_heading": "'Montserrat', sans-serif",
    },
    "preview-hochuli": {
        "routing_slug": "hochuli",
        "site_label": "Hochuli Schlossrued AG",
        "entity_hint": "die Hochuli Schlossrued AG",
        "accent_hex": "#E30613",
        "navy_hex": "#0F172A",
        "font_heading": "'Plus Jakarta Sans', 'Inter', sans-serif",
    },
    "preview-innere-staerke": {
        "routing_slug": "innere-staerke",
        "site_label": "Wüest + Paneduro — Innere Stärke entwickeln",
        "entity_hint": "Wüest + Paneduro (Nino Paneduro GmbH)",
        "accent_hex": "#AE031D",
        "navy_hex": "#232322",
        "font_heading": "'Barlow', sans-serif",
    },
    "preview-innere-staerke-v2": {
        "routing_slug": "innere-staerke-v2",
        "site_label": "Wüest + Paneduro (Zeigeversion / Vorschau-Entwurf)",
        "entity_hint": "Wüest + Paneduro (Nino Paneduro GmbH)",
        "accent_hex": "#AE031D",
        "navy_hex": "#232322",
        "font_heading": "'Barlow', sans-serif",
    },
    "preview-frees": {
        "routing_slug": "frees",
        "site_label": "Free's — Studio für Textildesign, Textildruck & Stickerei",
        "entity_hint": "Free's Stefan Fritschi (Niederrohrdorf)",
        "accent_hex": "#E12321",
        "navy_hex": "#181818",
        "font_heading": "'Barlow', sans-serif",
    },
    "preview-frees-v2": {
        "routing_slug": "frees-v2",
        "site_label": "Free's (Zeigeversion / Vorschau-Entwurf)",
        "entity_hint": "Free's Stefan Fritschi (Niederrohrdorf)",
        "accent_hex": "#E12321",
        "navy_hex": "#181818",
        "font_heading": "'Barlow', sans-serif",
    },
    "preview-herzensarbeit": {
        "routing_slug": "herzensarbeit",
        "site_label": "Herzensarbeit — Anne-Katrin Koch (Härkingen & Oensingen)",
        "entity_hint": "Praxis Herzensarbeit Anne-Katrin Koch",
        "accent_hex": "#9A1536",
        "navy_hex": "#1E2B34",
        "font_heading": "'Josefin Sans', sans-serif",
    },
    "preview-herzensarbeit-v2": {
        "routing_slug": "herzensarbeit-v2",
        "site_label": "Herzensarbeit (Zeigeversion / Vorschau-Entwurf)",
        "entity_hint": "Praxis Herzensarbeit Anne-Katrin Koch",
        "accent_hex": "#9A1536",
        "navy_hex": "#1E2B34",
        "font_heading": "'Josefin Sans', sans-serif",
    },
    "preview-imp-marketing": {
        "routing_slug": "imp-marketing",
        "site_label": "IMP GmbH — Matthias Iseli (Schreinerei- & Holzbau-Marketing)",
        "entity_hint": "die IMP GmbH (Matthias Iseli, Obersteckholz)",
        "accent_hex": "#C88A36",
        "navy_hex": "#14181D",
        "font_heading": "'Plus Jakarta Sans', sans-serif",
    },
    "preview-imp-marketing-v2": {
        "routing_slug": "imp-marketing-v2",
        "site_label": "IMP GmbH — Matthias Iseli (Zeigeversion / Vorschau-Entwurf)",
        "entity_hint": "die IMP GmbH (Matthias Iseli, Obersteckholz)",
        "accent_hex": "#C88A36",
        "navy_hex": "#14181D",
        "font_heading": "'Plus Jakarta Sans', sans-serif",
    },
}

CSS_START = "/* === WEBPILOT-PARTNER-ATTRIBUTION-CSS-START === */"
CSS_END = "/* === WEBPILOT-PARTNER-ATTRIBUTION-CSS-END === */"

BAR_START = "<!-- === WEBPILOT-PARTNER-BAR-START === -->"
BAR_END = "<!-- === WEBPILOT-PARTNER-BAR-END === -->"

FOOTER_START = "<!-- === WEBPILOT-PARTNER-FOOTER-START === -->"
FOOTER_END = "<!-- === WEBPILOT-PARTNER-FOOTER-END === -->"

MODAL_START = "<!-- === WEBPILOT-PARTNER-MODAL-START === -->"
MODAL_END = "<!-- === WEBPILOT-PARTNER-MODAL-END === -->"


def load_partner_for_showcase(routing_data: dict, routing_slug: str) -> dict:
    partners = routing_data.get("_partners") or {}
    client_cfg = routing_data.get(routing_slug) or {}
    partner_id = client_cfg.get("partner_id") or "jenny"
    partner = partners.get(partner_id) or partners.get("jenny") or {}
    return partner


def build_partner_css(cfg: dict) -> str:
    accent = cfg["accent_hex"]
    navy = cfg["navy_hex"]
    font_h = cfg["font_heading"]
    return f"""{CSS_START}
    .wp-partner-attr-bar {{
      margin-top: 20px;
      padding: 16px 18px;
      background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
      border: 1px solid #CBD5E1;
      border-left: 4px solid {accent};
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 14px;
      box-sizing: border-box;
      width: 100%;
      overflow: hidden;
    }}
    .wp-partner-attr-left {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      flex: 1 1 260px;
      min-width: 0;
    }}
    .wp-partner-attr-icon {{
      width: 36px;
      height: 36px;
      border-radius: 4px;
      background-color: {navy};
      color: #FBBF24;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 2px;
    }}
    .wp-partner-attr-text {{
      min-width: 0;
      flex: 1;
    }}
    .wp-partner-attr-title {{
      font-family: {font_h};
      font-size: 0.86rem;
      font-weight: 800;
      color: {navy};
      line-height: 1.35;
      margin: 0 0 3px 0;
    }}
    .wp-partner-attr-sub {{
      font-size: 0.79rem;
      color: #475569;
      line-height: 1.4;
      margin: 0;
    }}
    .wp-partner-cta-btn {{
      appearance: none;
      background-color: {navy};
      color: #FFFFFF !important;
      border: 1px solid {navy};
      border-radius: 8px;
      padding: 10px 15px;
      min-height: 42px;
      min-width: 44px;
      font-family: {font_h};
      font-size: 0.79rem;
      font-weight: 700;
      line-height: 1.3;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      text-align: left;
      transition: background-color 0.18s ease, border-color 0.18s ease;
      box-sizing: border-box;
      overflow: hidden;
      max-width: 100%;
    }}
    .wp-partner-cta-btn:hover {{
      background-color: {accent};
      border-color: {accent};
      color: #FFFFFF !important;
    }}
    .wp-partner-cta-btn svg {{
      flex-shrink: 0;
    }}
    .wp-partner-footer-btn {{
      appearance: none;
      background-color: rgba(255, 255, 255, 0.08);
      color: #F8FAFC !important;
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 8px;
      padding: 7px 13px;
      min-height: 36px;
      min-width: 44px;
      font-family: inherit;
      font-size: 0.78rem;
      font-weight: 700;
      line-height: 1.3;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      text-align: left;
      transition: background-color 0.18s ease, border-color 0.18s ease;
      box-sizing: border-box;
      overflow: hidden;
      max-width: 100%;
    }}
    .wp-partner-footer-btn:hover {{
      background-color: rgba(255, 255, 255, 0.16);
      border-color: #FBBF24;
      color: #FFFFFF !important;
    }}
    .wp-partner-footer-btn svg {{
      color: #FBBF24;
      flex-shrink: 0;
    }}
    /* Partner Modal (#wpPartnerModal) */
    .wp-partner-modal-backdrop {{
      display: none;
      position: fixed;
      inset: 0;
      background-color: rgba(11, 19, 36, 0.82);
      backdrop-filter: blur(6px);
      z-index: 2200;
      align-items: center;
      justify-content: center;
      padding: 14px;
      box-sizing: border-box;
    }}
    .wp-partner-modal-backdrop.open {{
      display: flex;
    }}
    .wp-partner-modal-dialog {{
      background-color: #FFFFFF;
      color: #0F172A;
      border: 2px solid {accent};
      border-radius: 8px;
      max-width: 640px;
      width: 100%;
      padding: 22px 22px 20px 22px;
      box-shadow: 0 20px 45px rgba(15, 23, 42, 0.35);
      position: relative;
      max-height: calc(100dvh - 28px);
      overflow-y: auto;
      box-sizing: border-box;
    }}
    .wp-partner-modal-head {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 10px;
    }}
    .wp-partner-modal-kicker {{
      font-family: {font_h};
      font-size: 0.7rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      color: {accent};
      display: block;
      margin-bottom: 4px;
    }}
    .wp-partner-modal-title {{
      font-family: {font_h};
      font-size: 1.15rem;
      font-weight: 800;
      color: {navy};
      line-height: 1.25;
      margin: 0;
    }}
    .wp-partner-modal-close {{
      appearance: none;
      width: 38px;
      height: 38px;
      min-width: 38px;
      min-height: 38px;
      border-radius: 8px;
      border: 1px solid #CBD5E1;
      background-color: #F8FAFC;
      color: #0F172A;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      padding: 0;
    }}
    .wp-partner-modal-close:hover {{
      background-color: #E2E8F0;
    }}
    .wp-partner-notice {{
      background-color: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-left: 4px solid {navy};
      border-radius: 4px;
      padding: 9px 12px;
      font-size: 0.78rem;
      color: #334155;
      line-height: 1.42;
      margin-bottom: 14px;
    }}
    .wp-partner-vcard {{
      background-color: #F8FAFC;
      border: 1px solid #CBD5E1;
      border-radius: 8px;
      padding: 13px 14px;
      margin-bottom: 14px;
    }}
    .wp-partner-vcard-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 10px;
    }}
    .wp-partner-vcard-name {{
      font-family: {font_h};
      font-size: 0.96rem;
      font-weight: 800;
      color: {navy};
      line-height: 1.25;
    }}
    .wp-partner-vcard-role {{
      font-size: 0.77rem;
      color: #475569;
      margin-top: 2px;
    }}
    .wp-partner-vcard-badge {{
      background-color: {navy};
      color: #FFFFFF;
      font-family: {font_h};
      font-size: 0.68rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 8px;
      border-radius: 4px;
      overflow: hidden;
    }}
    .wp-partner-direct-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 8px;
    }}
    .wp-partner-direct-btn {{
      text-decoration: none;
      border-radius: 8px;
      padding: 8px 10px;
      min-height: 40px;
      min-width: 44px;
      font-family: {font_h};
      font-size: 0.76rem;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      text-align: center;
      box-sizing: border-box;
      overflow: hidden;
      transition: opacity 0.16s ease, transform 0.16s ease;
    }}
    .wp-partner-direct-btn svg {{
      flex-shrink: 0;
    }}
    .wp-partner-direct-wa {{
      background-color: #059669;
      color: #FFFFFF !important;
      border: 1px solid #059669;
    }}
    .wp-partner-direct-tel {{
      background-color: {navy};
      color: #FFFFFF !important;
      border: 1px solid {navy};
    }}
    .wp-partner-direct-mail {{
      background-color: #FFFFFF;
      color: {navy} !important;
      border: 1px solid #94A3B8;
    }}
    .wp-partner-form-box {{
      background-color: #FFFFFF;
      border: 1px solid #CBD5E1;
      border-radius: 8px;
      padding: 14px;
    }}
    .wp-partner-form-title {{
      font-family: {font_h};
      font-size: 0.88rem;
      font-weight: 800;
      color: {navy};
      margin: 0 0 4px 0;
    }}
    .wp-partner-form-sub {{
      font-size: 0.76rem;
      color: #475569;
      margin: 0 0 12px 0;
      line-height: 1.4;
    }}
    .wp-partner-form-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 10px;
    }}
    .wp-partner-field {{
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-bottom: 10px;
    }}
    .wp-partner-form-grid .wp-partner-field {{
      margin-bottom: 0;
    }}
    .wp-partner-label {{
      font-size: 0.74rem;
      font-weight: 700;
      color: #1E293B;
      line-height: 1.25;
    }}
    .wp-partner-input {{
      width: 100%;
      min-height: 40px;
      padding: 8px 11px;
      border: 1px solid #CBD5E1;
      border-radius: 8px;
      font-family: inherit;
      font-size: 0.84rem;
      color: #0F172A;
      background-color: #FFFFFF;
      box-sizing: border-box;
    }}
    .wp-partner-input:focus {{
      outline: none;
      border-color: {accent};
    }}
    .wp-partner-submit-btn {{
      appearance: none;
      width: 100%;
      min-height: 44px;
      padding: 11px 16px;
      background-color: {accent};
      color: #FFFFFF !important;
      border: 1px solid {accent};
      border-radius: 8px;
      font-family: {font_h};
      font-size: 0.84rem;
      font-weight: 800;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-sizing: border-box;
      overflow: hidden;
    }}
    .wp-partner-submit-btn:hover {{
      opacity: 0.94;
    }}
    .wp-partner-error {{
      display: none;
      background-color: #FEE2E2;
      border: 1px solid #FCA5A5;
      color: #991B1B;
      padding: 8px 11px;
      border-radius: 4px;
      font-size: 0.78rem;
      margin-bottom: 10px;
    }}
    .wp-partner-success {{
      display: none;
      background-color: #ECFDF5;
      border: 1px solid #6EE7B7;
      border-radius: 8px;
      padding: 14px;
      margin-top: 4px;
    }}
    @media (max-width: 768px) {{
      body {{
        padding-bottom: 92px !important;
      }}
      .wp-partner-attr-bar {{
        padding: 14px;
      }}
      .wp-partner-cta-btn {{
        width: 100%;
        justify-content: space-between;
      }}
      .wp-partner-direct-grid {{
        grid-template-columns: 1fr;
      }}
      .wp-partner-form-grid {{
        grid-template-columns: 1fr;
      }}
      .wp-partner-modal-dialog {{
        padding: 16px 14px;
      }}
    }}
{CSS_END}"""


def build_partner_bar_html(partner: dict, cfg: dict) -> str:
    p_name = partner["name"]
    p_short = partner["short_agency"]
    role_prefix = "Beratung & Umsetzung" if partner["id"] == "jenny" else "Plattform & Umsetzung"
    return f"""
          {BAR_START}
          <div class="wp-partner-attr-bar" id="wpPartnerAttrBar" data-studio-ignore="true">
            <div class="wp-partner-attr-left">
              <span class="wp-partner-attr-icon" aria-hidden="true">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
              </span>
              <div class="wp-partner-attr-text">
                <div class="wp-partner-attr-title">Powered by WebPilot · {role_prefix}: {p_name} ({p_short})</div>
                <p class="wp-partner-attr-sub">Gefällt Ihnen dieser moderne Webauftritt oder der 3-Schritte Smart-Anfrage-Assistent?</p>
              </div>
            </div>
            <button type="button" class="wp-partner-cta-btn" data-studio-ignore="true" onclick="wpOpenPartnerModal('form_bar')">
              <span>Auch so eine Webseite oder Smart-Anfrage für Ihren Verein / Betrieb? · Kontakt &amp; Entwurf</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </button>
          </div>
          {BAR_END}"""


def build_partner_footer_html(partner: dict) -> str:
    p_name = partner["name"]
    p_short = partner["short_agency"]
    return f"""{FOOTER_START}
        <button type="button" class="wp-partner-footer-btn" data-studio-ignore="true" onclick="wpOpenPartnerModal('footer')">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
          <span>Powered by WebPilot · Partner: {p_name} ({p_short}) — Kontakt &amp; Infos</span>
        </button>
        {FOOTER_END}"""


def build_partner_modal_html(partner: dict, cfg: dict) -> str:
    p_name = partner["name"]
    p_agency = partner["agency"]
    p_short = partner["short_agency"]
    p_role = partner["role"]
    p_phone = partner["phone"]
    p_e164 = partner["phone_e164"]
    p_email = partner["email"]
    p_topic = partner["route_topic"]
    site_label = cfg["site_label"]
    entity_hint = cfg["entity_hint"]

    wa_text = urllib.parse.quote(
        f"Guten Tag {p_name}, ich habe den WebPilot-Auftritt von {site_label} gesehen und interessiere mich für einen unverbindlichen Vorschau-Entwurf / eine Smart-Anfrage-Zentrale."
    )
    wa_href = f"{partner['whatsapp_url']}?text={wa_text}"
    mail_subj = urllib.parse.quote(f"Anfrage WebPilot Vorschau-Entwurf (gesehen auf {site_label})")
    mail_href = f"mailto:{p_email}?subject={mail_subj}"

    return f"""
  {MODAL_START}
  <div class="wp-partner-modal-backdrop" id="wpPartnerModal" role="dialog" aria-modal="true" aria-labelledby="wpPartnerModalTitle" data-studio-ignore="true" data-allow-scroll="true">
    <div class="wp-partner-modal-dialog" data-studio-ignore="true" data-allow-scroll="true">
      <div class="wp-partner-modal-head">
        <div>
          <span class="wp-partner-modal-kicker">WEBPILOT PARTNER-KONTAKT · {p_agency.upper()}</span>
          <h3 class="wp-partner-modal-title" id="wpPartnerModalTitle">WebPilot Partner-Kontakt — Eigene Webseite oder Smart-Anfrage modernisieren</h3>
        </div>
        <button type="button" class="wp-partner-modal-close" aria-label="Partner-Dialog schliessen" onclick="wpClosePartnerModal()">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>

      <div class="wp-partner-notice">
        <strong>Hinweis zur Zuständigkeit:</strong> Direktkontakt zur ausführenden Partner-Agentur (<strong>{p_agency}</strong>). Für Anfragen an {entity_hint} nutzen Sie bitte das reguläre Formular auf der Seite.
      </div>

      <!-- TEIL 1: DIREKTE PARTNER-VISITENKARTE -->
      <div class="wp-partner-vcard">
        <div class="wp-partner-vcard-top">
          <div>
            <div class="wp-partner-vcard-name">{p_agency}</div>
            <div class="wp-partner-vcard-role">{p_role}</div>
          </div>
          <span class="wp-partner-vcard-badge">Direktkontakt</span>
        </div>
        <div class="wp-partner-direct-grid">
          <a href="{wa_href}" target="_blank" rel="noopener noreferrer" class="wp-partner-direct-btn wp-partner-direct-wa">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
            <span>WhatsApp direkt senden</span>
          </a>
          <a href="tel:{p_e164}" class="wp-partner-direct-btn wp-partner-direct-tel">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            <span>Anrufen ({p_phone})</span>
          </a>
          <a href="{mail_href}" class="wp-partner-direct-btn wp-partner-direct-mail">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
            <span>{p_email}</span>
          </a>
        </div>
      </div>

      <!-- TEIL 2: 15-SEKUNDEN-SCHNELLANFRAGE FUER VORSCHAU-ENTWURF -->
      <div class="wp-partner-form-box">
        <div class="wp-partner-form-title">15-Sekunden-Schnellanfrage: Unverbindlicher Vorschau-Entwurf</div>
        <p class="wp-partner-form-sub">
          Geben Sie Ihre bestehende Webseiten-URL oder den Namen Ihres Vereins / Betriebs an — {p_name} ({p_short}) zeigt Ihnen unverbindlich, wie Ihr moderner WebPilot-Auftritt aussieht.
        </p>

        <form id="wpPartnerLeadForm" onsubmit="return wpSubmitPartnerLead(event)" novalidate>
          <div style="display:none;" aria-hidden="true">
            <label for="wpPartnerHp">Website</label>
            <input type="text" id="wpPartnerHp" name="website_url" tabindex="-1" autocomplete="off">
          </div>

          <div class="wp-partner-field">
            <label for="wpPartnerTargetUrl" class="wp-partner-label">1. Bestehende Webseiten-URL oder Name Ihres Vereins / Betriebs *</label>
            <input type="text" id="wpPartnerTargetUrl" class="wp-partner-input" placeholder="z. B. www.mein-verein.ch oder Muster AG" required>
          </div>

          <div class="wp-partner-form-grid">
            <div class="wp-partner-field">
              <label for="wpPartnerVisitorName" class="wp-partner-label">2. Ihr Vor- und Nachname *</label>
              <input type="text" id="wpPartnerVisitorName" class="wp-partner-input" placeholder="Vorname Nachname" required>
            </div>
            <div class="wp-partner-field">
              <label for="wpPartnerVisitorContact" class="wp-partner-label">3. Ihre Telefonnummer oder E-Mail *</label>
              <input type="text" id="wpPartnerVisitorContact" class="wp-partner-input" placeholder="079 123 45 67 oder name@firma.ch" required>
            </div>
          </div>

          <div class="wp-partner-field">
            <label for="wpPartnerVisitorMsg" class="wp-partner-label">4. Kurze Nachricht (optional)</label>
            <input type="text" id="wpPartnerVisitorMsg" class="wp-partner-input" placeholder="z. B. Fokus Vereins-Zentrale, Sponsoren oder Smart-Anfrage...">
          </div>

          <div class="wp-partner-error" id="wpPartnerFormError"></div>

          <button type="submit" class="wp-partner-submit-btn" id="wpPartnerSubmitBtn">
            <span id="wpPartnerSubmitBtnTxt">Unverbindlichen Vorschau-Entwurf bei {p_name} anfordern</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </button>
        </form>

        <div class="wp-partner-success" id="wpPartnerSuccessBox" aria-live="polite">
          <div style="display:flex;align-items:center;gap:8px;font-weight:800;color:#065F46;font-size:0.94rem;margin-bottom:6px;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2.4"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Anfrage an {p_name} ({p_short}) übermittelt!</span>
          </div>
          <p style="font-size:0.8rem;color:#1E293B;line-height:1.45;margin:0 0 10px 0;">
            Ihr 1-Seiten-Anfrage-Dossier (<strong id="wpPartnerResRef">#WP-2026</strong>) wurde erstellt und direkt an <strong>{p_agency}</strong> übermittelt.
          </p>
          <div style="display:flex;flex-wrap:wrap;gap:8px;">
            <a href="#" id="wpPartnerResPdfBtn" target="_blank" rel="noopener noreferrer" class="wp-partner-direct-btn wp-partner-direct-tel" style="flex:1 1 200px;">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              <span>1-Seiten-PDF-Dossier öffnen</span>
            </a>
            <button type="button" class="wp-partner-direct-btn wp-partner-direct-mail" style="flex:1 1 140px;cursor:pointer;" onclick="wpResetPartnerModal()">
              <span>Weitere Anfrage</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script>
    var wpPartnerSourceTrigger = 'footer';
    function wpOpenPartnerModal(triggerSource) {{
      wpPartnerSourceTrigger = triggerSource || 'footer';
      var m = document.getElementById('wpPartnerModal');
      if (m) {{
        m.classList.add('open');
      }}
    }}
    function wpClosePartnerModal() {{
      var m = document.getElementById('wpPartnerModal');
      if (m) {{
        m.classList.remove('open');
      }}
    }}
    function wpResetPartnerModal() {{
      var f = document.getElementById('wpPartnerLeadForm');
      var s = document.getElementById('wpPartnerSuccessBox');
      var err = document.getElementById('wpPartnerFormError');
      if (f) {{ f.reset(); f.style.display = 'block'; }}
      if (s) {{ s.style.display = 'none'; }}
      if (err) {{ err.style.display = 'none'; }}
    }}
    function wpSubmitPartnerLead(ev) {{
      if (ev) ev.preventDefault();
      var hp = (document.getElementById('wpPartnerHp') || {{}}).value || '';
      var targetUrl = ((document.getElementById('wpPartnerTargetUrl') || {{}}).value || '').trim();
      var visitorName = ((document.getElementById('wpPartnerVisitorName') || {{}}).value || '').trim();
      var rawContact = ((document.getElementById('wpPartnerVisitorContact') || {{}}).value || '').trim();
      var msg = ((document.getElementById('wpPartnerVisitorMsg') || {{}}).value || '').trim();
      var errBox = document.getElementById('wpPartnerFormError');
      var btn = document.getElementById('wpPartnerSubmitBtn');
      var btnTxt = document.getElementById('wpPartnerSubmitBtnTxt');

      if (errBox) errBox.style.display = 'none';
      if (!targetUrl || !visitorName || !rawContact) {{
        if (errBox) {{
          errBox.textContent = 'Bitte geben Sie die gewünschte Webseiten-URL (oder Verein/Betrieb), Ihren Namen sowie Ihre Telefonnummer oder E-Mail-Adresse an.';
          errBox.style.display = 'block';
        }}
        return false;
      }}

      var isEmail = rawContact.indexOf('@') !== -1;
      var emailVal = isEmail ? rawContact : '';
      var phoneVal = isEmail ? '' : rawContact;

      if (btn) btn.disabled = true;
      if (btnTxt) btnTxt.textContent = 'Anfrage wird übermittelt...';

      var payload = {{
        client_slug: 'webpilot_partner',
        website_url: hp,
        category: 'Vorschau-Entwurf & Web-Modernisierung',
        sparte: '{p_topic}',
        topic: '{p_topic}',
        urgency: 'Vorschau-Entwurf angefordert',
        name: visitorName,
        company: targetUrl,
        phone: phoneVal,
        email: emailVal,
        source_page: window.location.pathname || '{site_label}',
        message: (msg ? msg + ' — ' : '') + 'Empfehlung über Showcase: {site_label} (' + wpPartnerSourceTrigger + ') · Gewünschte Webseite / Verein / Betrieb: ' + targetUrl,
        extra_fields: {{
          'Gewünschte Ziel-URL / Verein': targetUrl,
          'Empfehlung über': '{site_label}',
          'Partner-Agentur': '{p_agency}'
        }}
      }};

      fetch('/api/lead-submit', {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json' }},
        body: JSON.stringify(payload)
      }})
      .then(function(r) {{ return r.json(); }})
      .then(function(res) {{
        if (btn) btn.disabled = false;
        if (btnTxt) btnTxt.textContent = 'Unverbindlichen Vorschau-Entwurf bei {p_name} anfordern';
        if (!res || !res.ok) {{
          if (errBox) {{
            errBox.textContent = (res && res.error) ? res.error : 'Übermittlung fehlgeschlagen. Bitte versuchen Sie es erneut.';
            errBox.style.display = 'block';
          }}
          return;
        }}
        var formEl = document.getElementById('wpPartnerLeadForm');
        var succEl = document.getElementById('wpPartnerSuccessBox');
        var refEl = document.getElementById('wpPartnerResRef');
        var pdfBtn = document.getElementById('wpPartnerResPdfBtn');
        if (refEl && res.ref_code) refEl.textContent = res.ref_code;
        if (pdfBtn && res.pdf_url) pdfBtn.href = res.pdf_url;
        if (formEl) formEl.style.display = 'none';
        if (succEl) succEl.style.display = 'block';
      }})
      .catch(function() {{
        if (btn) btn.disabled = false;
        if (btnTxt) btnTxt.textContent = 'Unverbindlichen Vorschau-Entwurf bei {p_name} anfordern';
        if (errBox) {{
          errBox.textContent = 'Netzwerkfehler. Bitte kontaktieren Sie {p_name} direkt per WhatsApp oder Telefon.';
          errBox.style.display = 'block';
        }}
      }});
      return false;
    }}
    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') wpClosePartnerModal();
    }});
  </script>
  {MODAL_END}"""


def replace_or_inject_block(html: str, start_marker: str, end_marker: str, new_block: str) -> tuple[str, bool]:
    pattern = re.compile(re.escape(start_marker) + r".*?" + re.escape(end_marker), re.DOTALL)
    if pattern.search(html):
        return pattern.sub(lambda _: new_block.strip(), html, count=1), True
    return html, False


def find_div_closing_index(html: str, div_start_idx: int) -> int:
    """Finds the matching </div> end index starting from div_start_idx."""
    tag_re = re.compile(r"</?div\b[^>]*>", re.IGNORECASE)
    depth = 0
    for m in tag_re.finditer(html, div_start_idx):
        tok = m.group(0).lower()
        if tok.startswith("</div"):
            depth -= 1
            if depth == 0:
                return m.end()
        else:
            depth += 1
    return -1


def process_html_file(html_path: Path, partner: dict, cfg: dict) -> bool:
    orig = html_path.read_text(encoding="utf-8")
    html = orig

    # 1. Inject or update CSS inside <style> before </style>
    css_block = build_partner_css(cfg)
    html, replaced_css = replace_or_inject_block(html, CSS_START, CSS_END, css_block)
    if not replaced_css:
        style_close = html.find("</style>")
        if style_close != -1:
            html = html[:style_close] + "\n" + css_block + "\n  " + html[style_close:]

    # 2. On kontakt.html: Inject or update Platzierung A right after #wpSuccessBox
    if html_path.name == "kontakt.html":
        bar_block = build_partner_bar_html(partner, cfg)
        html, replaced_bar = replace_or_inject_block(html, BAR_START, BAR_END, bar_block)
        if not replaced_bar:
            succ_match = re.search(r'<div[^>]*\bid=["\']wpSuccessBox["\'][^>]*>', html)
            if succ_match:
                end_idx = find_div_closing_index(html, succ_match.start())
                if end_idx != -1:
                    html = html[:end_idx] + "\n" + bar_block + html[end_idx:]

    # 3. On all customer pages: Inject or update Platzierung B inside .footer-bottom
    footer_block = build_partner_footer_html(partner)
    html, replaced_footer = replace_or_inject_block(html, FOOTER_START, FOOTER_END, footer_block)
    if not replaced_footer:
        fb_match = re.search(r'<div[^>]*\bclass=["\'][^"\']*\bfooter-bottom\b[^"\']*["\'][^>]*>', html)
        if fb_match:
            end_idx = find_div_closing_index(html, fb_match.start())
            if end_idx != -1:
                close_tag_start = html.rfind("</div>", fb_match.start(), end_idx)
                if close_tag_start != -1:
                    html = html[:close_tag_start] + "  " + footer_block + "\n      " + html[close_tag_start:]

    # 4. On all customer pages: Inject or update #wpPartnerModal before </body>
    modal_block = build_partner_modal_html(partner, cfg)
    html, replaced_modal = replace_or_inject_block(html, MODAL_START, MODAL_END, modal_block)
    if not replaced_modal:
        body_close = html.rfind("</body>")
        if body_close != -1:
            html = html[:body_close] + modal_block + "\n" + html[body_close:]

    if html != orig:
        html_path.write_text(html, encoding="utf-8")
        return True
    return False


def main():
    routing_data = json.loads(LEAD_ROUTING_FILE.read_text(encoding="utf-8"))
    total_files = 0
    modified_files = 0

    for folder_name, cfg in SHOWCASE_CONFIGS.items():
        site_dir = BASE_DIR / folder_name
        if not site_dir.is_dir():
            print(f"[WARN] Showcase directory missing: {site_dir}")
            continue
        partner = load_partner_for_showcase(routing_data, cfg["routing_slug"])
        html_files = sorted(p for p in site_dir.glob("*.html") if p.name != "cockpit.html")
        site_mod = 0
        for hf in html_files:
            total_files += 1
            if process_html_file(hf, partner, cfg):
                modified_files += 1
                site_mod += 1
        print(f"[OK] {folder_name:24s} -> Partner: {partner['agency']:26s} | Files: {len(html_files)} (updated: {site_mod})")

    print(f"=== Partner Attribution Injection complete: {modified_files}/{total_files} HTML files updated ===")


if __name__ == "__main__":
    main()

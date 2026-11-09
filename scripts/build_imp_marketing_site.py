#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator für die WebPilot-Referenz-Aufbereitung von imp-marketing.ch (IMP GmbH · Matthias Iseli, Obersteckholz BE):
- Variante 1 (Vollversion): /home/brainuser/workspaces/mxs-embed/preview-imp-marketing
  Live-URL: https://vorschau.magnet-xs.ch/imp-marketing-vollversion/ (5 voll ausgebaute Seiten + Studio Cockpit v4.0)
- Variante 2 (Zeigeversion / Vorschau-Entwurf): /home/brainuser/workspaces/mxs-embed/preview-imp-marketing-v2
  Live-URL: https://vorschau.magnet-xs.ch/imp-marketing-v2/ (Startseite index.html 100 % voll ausgebaut +
  die 4 Unterseiten als edler Vorschau-Entwurf / Ausbaustufe mit interaktiver Smart-Anfrage-Schublade «Ausbau dieser Seite anfragen»).

Strikt nach:
- UI-LAYOUT-RULES.md (Canary: UI-LAYOUT-2026-V1: Plus Jakarta Sans Display, 0 JetBrains Mono, 0 //, 100 % Lucide SVGs, 0 Emojis, 2-Radius 4px/8px)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1: 100 % ss statt Eszett, Schweizer Handwerks-Terminologie: Schreiner EFZ, Zimmermann EFZ, Offerte, Leistungen)
- #SYS-01 (Kein oberer Versions-/Cockpit-Balken, 0 Hinweise auf Vollversion/Cockpit auf Kundenseiten)
"""

import json
import subprocess
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
V1_DIR = BASE_DIR / "preview-imp-marketing"
V2_DIR = BASE_DIR / "preview-imp-marketing-v2"

V1_DIR.mkdir(parents=True, exist_ok=True)
V2_DIR.mkdir(parents=True, exist_ok=True)

BEFORE_INVENTORY = {
    "source_url": "https://imp-marketing.ch/",
    "crawled_at": "2026-11-05",
    "company_name": "IMP GmbH · Matthias Iseli",
    "brand_name": "IMP-Marketing",
    "legal_entity": "IMP GmbH",
    "uid": "CHE-446.080.483",
    "claim": "Mehr Anfragen für Ihre Schreinerei, ohne Marketing-Chaos",
    "subline": "Struktur. Klarheit. Ergebnisse. Das spezialisierte Sichtbarkeits- & Anfrage-System für Schreinereien und Holzbau-Betriebe (1–15 Mitarbeitende) in der Deutschschweiz.",
    "address": {
        "street": "Herrengasse 81",
        "zip": "4924",
        "city": "Obersteckholz",
        "region": "Oberaargau",
        "canton": "Bern",
        "country": "Schweiz"
    },
    "contact": {
        "email": "kontakt@imp-marketing.ch",
        "email_Wait": "info@imp-marketing.ch",
        "phone_primary": "+41 76 227 67 20",
        "phone_display": "076 227 67 20",
        "channels": "Telefon, WhatsApp, E-Mail & Kostenlose Potenzial-Analyse (Obersteckholz / Vor-Ort im Betrieb / Online)"
    },
    "founder": {
        "name": "Matthias Iseli",
        "role": "Inhaber & Geschäftsführer IMP GmbH · Gelernte Fachkraft Schreiner EFZ",
        "experience": "Über 15 Jahre Berufserfahrung in Schreinerei und Holzbau (von Oberflächenbehandlung bis CNC-Bearbeitung) sowie mehrjährige Führungserfahrung u. a. in der Geschäftsleitung",
        "method": "Erfinder des «IMP Sichtbarkeits-Tragwerks»",
        "portrait": "images/portrait-matthias-iseli.jpg",
        "photo_credit": "Suli Photography"
    },
    "replaced_template_remnants": [
        "Removed English GoHighLevel hero quote: 'Digital Studio Solutions, absolutely fantastic! – John'",
        "Removed English fake counter bar: '25+ Years Experience / 5K+ Projects Completed / 98% Client Satisfaction'",
        "Removed 6 English Jane Doe / John Doe '[Your Agency Name]' dummy testimonials",
        "Removed 6 English digital studio FAQs ('What solutions does your digital studio provide?') and replaced with 6 authentic Swiss carpentry & timber construction FAQs",
        "Removed placeholder '[H2] Abschnitt folgt bald'"
    ],
    "services": [
        {
            "id": "webseiten",
            "title": "Webseiten für Schreinereien & Holzbau",
            "subtitle": "Moderne, klare und vertrauensvolle Webseiten für Handwerksbetriebe",
            "steps": [
                {"step": "Schritt 1", "title": "Kennenlernen & Analyse", "desc": "Wir besprechen Ihren Betrieb, Ihre Stärken im Innenausbau oder Holzbau und analysieren Ihren aktuellen Online-Auftritt.", "img": "images/web-step-1-analyse.png"},
                {"step": "Schritt 2", "title": "Konzept & Design", "desc": "Wir entwickeln ein klares Webseiten-Konzept passend zu Ihrer Werkstatt, Ihren Wunschprojekten und Ihrer regionalen Zielgruppe.", "img": "images/web-step-2-konzept.png"},
                {"step": "Schritt 3", "title": "Saubere Umsetzung", "desc": "Ihre neue Webseite wird technisch sauber, mobil-optimiert, pfeilschnell und mit Fokus auf echtes Kundenvertrauen umgesetzt.", "img": "images/web-step-3-umsetzung.jpg"},
                {"step": "Schritt 4", "title": "Veröffentlichung & Betreuung", "desc": "Nach dem Livegang begleiten wir Sie zuverlässig weiter mit Referenz-Updates, Anpassungen und laufender Pflege.", "img": "images/web-step-4-betreuung.png"}
            ]
        },
        {
            "id": "google-seo",
            "title": "Google-Geschäftsprofil & Regionale SEO",
            "subtitle": "Regional sichtbar werden, genau dann, wenn Bauherren und Privatkunden suchen",
            "steps": [
                {"step": "Schritt 1", "title": "Analyse Ihres Google-Profils", "desc": "Wir prüfen Ihr bestehendes Google-Geschäftsprofil sowie Ihre regionale Auffindbarkeit im Umkreis Ihres Standorts.", "img": "images/seo-step-1-analyse.png"},
                {"step": "Schritt 2", "title": "Optimierung & Struktur", "desc": "Wir optimieren Kategorien, Leistungsbereiche (Küchenbau, Innenausbau, Fenster, Holzbau), Werkstattfotos und lokale Suchbegriffe.", "img": "images/seo-step-2-struktur.png"},
                {"step": "Schritt 3", "title": "Bewertungen & Sichtbarkeit", "desc": "Wir richten ein einfaches System ein, mit dem zufriedene Kunden nach der Montage unkompliziert echte 5-Sterne-Bewertungen hinterlassen.", "img": "images/seo-step-3-bewertungen.png"},
                {"step": "Schritt 4", "title": "Laufende Pflege", "desc": "Optional betreuen wir Ihr Profil dauerhaft, veröffentlichen aktuelle Projektbilder und sichern Ihre Top-Position in der Region.", "img": "images/seo-step-4-pflege.png"}
            ]
        },
        {
            "id": "anfrage-systeme",
            "title": "Chat-Widgets & Anfrage-Systeme",
            "subtitle": "Qualifizierte Kundenanfragen ohne Telefon-Unterbrechung an der CNC-Fräse oder auf der Montage",
            "steps": [
                {"step": "Schritt 1", "title": "Analyse Ihrer Anfragewege", "desc": "Wir prüfen, wie Bauherren, Architekten und Privatkunden heute bei Ihnen anfragen und wo im Alltag Informationen fehlen.", "img": "images/chat-step-1-analyse.png"},
                {"step": "Schritt 2", "title": "Planung der Vorqualifizierung", "desc": "Gemeinsam definieren wir die Abfrage nach Küchenbau, Innenausbau, Möbel nach Mass, Fenster/Türen oder Reparatur inkl. Foto-Upload.", "img": "images/chat-step-2-planung.png"},
                {"step": "Schritt 3", "title": "Einrichtung & Integration", "desc": "Das interaktive Anfrage-System oder Chat-Widget wird nahtlos in Ihre Webseite eingebunden und mit Ihrem Postfach verknüpft.", "img": "images/chat-step-3-integration.png"},
                {"step": "Schritt 4", "title": "Optimierung & Feinschliff", "desc": "Wir testen den gesamten Ablauf auf Smartphone und Desktop, damit Kunden in unter 90 Sekunden alle Eckdaten für die Offerte übermitteln.", "img": "images/chat-step-4-optimierung.png"}
            ]
        },
        {
            "id": "datenautomation",
            "title": "Datenautomation & Handwerks-Prozesse",
            "subtitle": "Weniger Büro-Aufwand, strukturierte Kundendaten und saubere Übergaben bis zur Offerte",
            "steps": [
                {"step": "Schritt 1", "title": "Analyse Ihrer Büro-Abläufe", "desc": "Wir schauen gemeinsam an, welche administrativen Schritte zwischen Erstkontakt, Massaufnahme und Offerte unnötig Zeit fressen.", "img": "images/auto-step-1-ablaeufe.png"},
                {"step": "Schritt 2", "title": "Planung der Automationen", "desc": "Wir entwerfen bodenständige, übersichtliche Abläufe für automatische Eingangsbestätigungen, Kundendaten-Erfassung und Terminbuchung.", "img": "images/auto-step-2-planung.png"},
                {"step": "Schritt 3", "title": "Technische Umsetzung", "desc": "Wir verbinden Ihre Formulare, Kalender und Kontaktlisten zuverlässig im Hintergrund, ohne komplizierte Software-Experimente.", "img": "images/auto-step-3-umsetzung.png"},
                {"step": "Schritt 4", "title": "Einführung & Begleitung", "desc": "Wir schulen Sie und Ihr Büro-Team kurz und praxisnah und passen die Abläufe bei Bedarf jederzeit an Ihren Werkstatt-Alltag an.", "img": "images/auto-step-4-einfuehrung.png"}
            ]
        }
    ],
    "faqs": [
        {
            "q": "Was unterscheidet IMP-Marketing von einer klassischen Werbe- oder Webagentur?",
            "a": "Inhaber Matthias Iseli ist selbst gelernter Schreiner EFZ mit über 15 Jahren praktischer Erfahrung von der Oberflächenbehandlung und CNC-Bearbeitung bis in die Geschäftsleitung. Bei uns gibt es keine englischen Marketing-Buzzwords und keine leeren Versprechungen, sondern ein bodenständiges Sichtbarkeits-Tragwerk, das exakt auf Schreinereien und Holzbau-Betriebe mit 1 bis 15 Mitarbeitenden zugeschnitten ist."
        },
        {
            "q": "Wie viel Zeit muss ich als Inhaber oder Projektleiter für die Umsetzung einplanen?",
            "a": "Wir wissen, dass Ihre Zeit in der Werkstatt, in der Arbeitsvorbereitung (AVO) und bei Kunden vor Ort gebraucht wird. Für den Start genügt ein strukturiertes Gespräch von rund 60 Minuten. Weil wir die Fachbegriffe im Innenausbau, Möbelbau und Holzbau aus eigener Praxis kennen, erstellen wir Texte, Seitenstruktur und Anfrage-Abläufe fixfertig für Sie."
        },
        {
            "q": "Warum reicht Mundpropaganda allein heute für viele Schreinereien nicht mehr aus?",
            "a": "Persönliche Empfehlungen sind im Handwerk nach wie vor Gold wert. Doch selbst wer Ihren Betrieb empfohlen bekommt, gibt heute zuerst Ihren Firmennamen bei Google ein. Wenn die Webseite veraltet ist oder auf dem Smartphone schlecht lädt, springen kaufkräftige Bauherren für Schreinerküchen, Einbauschränke oder Gesamtsanierungen oft noch vor dem ersten Anruf ab."
        },
        {
            "q": "Wie verhindert das Anfrage-System ständige Telefon-Unterbrechungen an der CNC oder auf der Montage?",
            "a": "Statt dass das Telefon mitten beim Fräsen, Verleimen oder Montieren klingelt und Sie zwischen Tür und Angel Masse notieren müssen, führt unser Anfrage-System den Kunden online durch die wichtigsten Eckdaten (Bereich, ungefähre Masse, Fotos der Einbausituation, PLZ und Zeitrahmen). Sie erhalten ein sauberes Dossier und rufen genau dann zurück, wenn Sie im Büro Ruhe haben."
        },
        {
            "q": "Was bringt die Optimierung des Google-Geschäftsprofils konkret für meinen Betrieb in der Region?",
            "a": "Wenn Eigenheimbesitzer, Verwaltungen oder Architekten in Ihrer Region nach «Schreinerei», «Einbauschrank nach Mass» oder «Holzbau» suchen, zeigt Google zuerst die drei lokalen Karten-Einträge. Mit einem sauber gepflegten Profil, echten Werkstatt- und Referenzbildern sowie einem einfachen Bewertungs-Ablauf sichern Sie sich genau diese regionalen Direkt-Anfragen."
        },
        {
            "q": "Wie läuft der Start ab und gibt es versteckte Agentur-Knebelverträge?",
            "a": "Nein. Jede Zusammenarbeit startet mit einer kostenlosen, unverbindlichen Potenzial-Analyse Ihres bestehenden Auftritts. Danach erhalten Sie eine glasklare Schweizer Offerte mit fest definiertem Leistungsumfang und fairen Konditionen, ob Sie zuerst mit einer modernen Webseite und dem Google-Profil starten oder direkt das gesamte 4-Säulen Sichtbarkeits-Tragwerk umsetzen möchten."
        }
    ]
}

(V1_DIR / "before.json").write_text(json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False), encoding="utf-8")
(V2_DIR / "before.json").write_text(json.dumps(BEFORE_INVENTORY, indent=2, ensure_ascii=False), encoding="utf-8")

base_company_data = {
    "name": "IMP GmbH · Matthias Iseli",
    "short_name": "IMP-Marketing",
    "legal_entity": "IMP GmbH",
    "uid": "CHE-446.080.483",
    "slug": "imp-marketing",
    "industry": "Schreinerei, Holzbau & Digital-Marketing",
    "branche": "Schreinerei",
    "work_category_label": "Werkstatt, Systeme & Prozesse",
    "studio_title": "WEBPILOT STUDIO",
    "is_website_studio": True,
    "domain": "imp-marketing.ch",
    "email": "kontakt@imp-marketing.ch",
    "phone": "+41 76 227 67 20",
    "address": "Herrengasse 81, CH-4924 Obersteckholz (BE)",
    "brand_color": "#C88A36",
    "accent_color": "#8C5811",
    "topbar_badge": "SCHREINER EFZ PRAXIS · 4924 OBERSTECKHOLZ (BE) · DEUTSCHSCHWEIZ",
    "topbar_sub": "Über 15 Jahre Erfahrung in Schreinerei & Holzbau · Das IMP Sichtbarkeits-Tragwerk für 1–15 Mitarbeitende",
    "brand_name": "IMP-MARKETING",
    "brand_sub": "MATTHIAS ISELI · SCHREINEREI & HOLZBAU SYSTEME",
    "header_cta": "Potenzial-Analyse anfragen",
    "hero_kicker": "VOM SCHREINER EFZ FÜR SCHREINEREIEN & HOLZBAU-BETRIEBE (1–15 MITARBEITENDE)",
    "hero_h1": "Mehr Anfragen für Ihre Schreinerei – <span>ohne Marketing-Chaos.</span>",
    "hero_lead": "Wir helfen Schreinereien und Holzbau-Betrieben in der Deutschschweiz, online regional sichtbar zu werden, echtes Bauherren-Vertrauen aufzubauen und planbar qualifizierte Offerten-Anfragen zu gewinnen, mit Struktur, Klarheit und Handwerks-Verstand.",
    "footer_about": "IMP GmbH (Herrengasse 81, 4924 Obersteckholz BE, UID CHE-446.080.483): Spezialisiertes Digital- & Sichtbarkeits-System für Schreinereien und Holzbau-Betriebe in der Deutschschweiz. Gegründet von Matthias Iseli (Schreiner EFZ)."
}

v1_company = dict(base_company_data)
v1_company.update({
    "slug": "imp-marketing",
    "host_url": "https://vorschau.magnet-xs.ch/imp-marketing-vollversion/cockpit.html?token=impmarketing2026",
    "host_jobs_url": "https://vorschau.magnet-xs.ch/imp-marketing-vollversion/"
})
(V1_DIR / "company.json").write_text(json.dumps(v1_company, indent=2, ensure_ascii=False), encoding="utf-8")
v1_config = dict(v1_company)
v1_config.update({
    "preview_url": "https://vorschau.magnet-xs.ch/imp-marketing-vollversion/",
    "cockpit_token": "impmarketing2026",
    "template": "carpentry-b2b-flagship-v1",
    "pages": ["index.html", "leistungen.html", "methode.html", "ueber-uns.html", "kontakt.html"]
})
(V1_DIR / "config.json").write_text(json.dumps(v1_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V1_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-imp-marketing",
    "public_slug": "imp-marketing",
    "token": "impmarketing2026",
    "name": "IMP GmbH · Matthias Iseli (Schreinerei-Marketing)",
    "Updated": "2026-11-05",
    "PagesCount": 5,
    "PillarsCount": 4,
    "FaqsCount": 6
}, indent=2, ensure_ascii=False), encoding="utf-8")

v2_company = dict(base_company_data)
v2_company.update({
    "slug": "imp-marketing-v2",
    "name": "IMP GmbH · Matthias Iseli (Zeigeversion)",
    "host_url": "https://vorschau.magnet-xs.ch/imp-marketing-v2/cockpit.html?token=impmarketing2026",
    "host_jobs_url": "https://vorschau.magnet-xs.ch/imp-marketing-v2/"
})
(V2_DIR / "company.json").write_text(json.dumps(v2_company, indent=2, ensure_ascii=False), encoding="utf-8")
v2_config = dict(v2_company)
v2_config.update({
    "preview_url": "https://vorschau.magnet-xs.ch/imp-marketing-v2/",
    "cockpit_token": "impmarketing2026",
    "template": "carpentry-b2b-preview-v2",
    "pages": ["index.html", "leistungen.html", "methode.html", "ueber-uns.html", "kontakt.html"]
})
(V2_DIR / "config.json").write_text(json.dumps(v2_config, indent=2, ensure_ascii=False), encoding="utf-8")
(V2_DIR / "site.json").write_text(json.dumps({
    "slug": "preview-imp-marketing-v2",
    "public_slug": "imp-marketing-v2",
    "token": "impmarketing2026",
    "name": "IMP GmbH · Matthias Iseli (Zeigeversion / Vorschau-Entwurf)",
    "Updated": "2026-11-05",
    "PagesCount": 5,
    "PillarsCount": 4,
    "FaqsCount": 6
}, indent=2, ensure_ascii=False), encoding="utf-8")

print("Wrote before.json, company.json, config.json, site.json for V1 and V2.")

# ---------------------------------------------------------
# 2. CSS STYLESHEET (style.css) – Eichen-Gold & Werkbank-Anthrazit
# ---------------------------------------------------------
STYLE_CSS = """/* WebPilot Showcase – IMP GmbH (Matthias Iseli, Obersteckholz)
   Design-System: Schweizer Handwerks- & Architektur-Ästhetik
   Farben: Werkbank-Anthrazit (#14181d), Eichen-/Nussbaum-Gold (#c88a36 / #8c5811), Werkplan-Elfenbein (#faf8f5)
   Fonts: Plus Jakarta Sans (Display & UI), Inter (Body) – 0 JetBrains Mono, 0 // */

:root {
  --bg-ivory: #faf8f5;
  --bg-ivory-alt: #f2ede4;
  --bg-card: #ffffff;
  --bg-anthracite: #14181d;
  --bg-anthracite-soft: #1d232b;
  --text-main: #14181d;
  --text-muted: #4a525d;
  --text-light: #f5f2eb;
  --text-light-muted: #c5ccd6;
  --oak-gold: #c88a36;
  --oak-gold-hover: #b07222;
  --oak-gold-dark: #82500d;
  --oak-gold-pale: #f7efe2;
  --border-light: #e2d9c8;
  --border-dark: #2c3540;
  --success-green: #1f6f43;
  --radius-sm: 4px;
  --radius-md: 8px;
  --shadow-card: 0 10px 30px rgba(20, 24, 29, 0.06);
  --shadow-elevated: 0 18px 42px rgba(20, 24, 29, 0.12);
  --font-display: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  font-size: 16px;
}

body {
  font-family: var(--font-body);
  background-color: var(--bg-ivory);
  color: var(--text-main);
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

a {
  color: inherit;
  text-decoration: none;
  transition: color 0.2s ease, background-color 0.2s ease, border-color 0.2s ease;
}

.container {
  width: 100%;
  max-width: 1220px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

/* Kickers & Headings (#UI-01: Plus Jakarta Sans Bold, 0 JetBrains Mono, 0 //) */
.section-kicker {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-display);
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--oak-gold-dark);
  background: var(--oak-gold-pale);
  border: 1px solid rgba(200, 138, 54, 0.35);
  padding: 0.35rem 0.75rem;
  border-radius: var(--radius-sm);
  margin-bottom: 1rem;
}

.section-dark .section-kicker,
.hero-section .section-kicker,
.ausbau-banner .section-kicker {
  color: #f3c37a;
  background: rgba(200, 138, 54, 0.16);
  border-color: rgba(200, 138, 54, 0.4);
}

h1, h2, h3, h4 {
  font-family: var(--font-display);
  color: var(--text-main);
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.section-dark h1,
.section-dark h2,
.section-dark h3,
.section-dark h4,
.hero-section h1,
.hero-section h2,
.hero-section h3,
.hero-section h4,
.ausbau-banner h1,
.ausbau-banner h2,
.ausbau-banner h3,
.ausbau-banner h4,
.calc-result-panel h1,
.calc-result-panel h2,
.calc-result-panel h3,
.calc-result-panel h4,
.site-footer h1,
.site-footer h2,
.site-footer h3,
.site-footer h4 {
  color: var(--text-light);
}

.anfrage-card h1,
.anfrage-card h2,
.anfrage-card h3,
.anfrage-card h4,
.calc-wrapper h1,
.calc-wrapper h2,
.calc-wrapper h3,
.calc-wrapper h4,
.ausbau-drawer h1,
.ausbau-drawer h2,
.ausbau-drawer h3,
.ausbau-drawer h4 {
  color: var(--text-main);
}

.h1-hero {
  font-size: clamp(1.9rem, 4.2vw, 3.35rem);
  font-weight: 800;
  margin-bottom: 1.25rem;
  overflow-wrap: break-word;
  hyphens: auto;
}

.h2-section {
  font-size: clamp(1.75rem, 3vw, 2.45rem);
  font-weight: 800;
  margin-bottom: 1rem;
}

.lead-text {
  font-size: 1.125rem;
  color: var(--text-muted);
  max-width: 68ch;
}

.section-dark .lead-text,
.hero-section .lead-text,
.ausbau-banner .lead-text {
  color: var(--text-light-muted);
}

/* Top Meta Bar */
.top-meta-bar {
  background-color: var(--bg-anthracite);
  color: var(--text-light-muted);
  font-size: 0.84rem;
  border-bottom: 1px solid var(--border-dark);
  padding: 0.55rem 0;
}

.top-meta-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.top-meta-items {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 1.25rem;
}

.top-meta-item {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  color: var(--text-light-muted);
}

.top-meta-item svg {
  width: 15px;
  height: 15px;
  color: var(--oak-gold);
  flex-shrink: 0;
}

/* Header & Navigation */
.site-header {
  position: sticky;
  top: 0;
  z-index: 90;
  background-color: rgba(250, 248, 245, 0.96);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--border-light);
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 82px;
  gap: 1.25rem;
}

.brand-logo {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  flex-shrink: 0;
}

.brand-logo img {
  height: 46px;
  width: auto;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-light);
}

.brand-sub {
  display: flex;
  flex-direction: column;
}

.brand-title {
  font-family: var(--font-display);
  font-weight: 800;
  font-size: 1.05rem;
  color: var(--text-main);
  line-height: 1.15;
}

.brand-tagline {
  font-size: 0.76rem;
  color: var(--text-muted);
  font-weight: 500;
}

.main-nav {
  display: flex;
  align-items: center;
  gap: 1.4rem;
  flex-wrap: nowrap;
  white-space: nowrap;
}

.nav-link {
  font-family: var(--font-display);
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-main);
  padding: 0.4rem 0.1rem;
  border-bottom: 2px solid transparent;
  white-space: nowrap;
}

.nav-link:hover,
.nav-link.active {
  color: var(--oak-gold-dark);
  border-bottom-color: var(--oak-gold);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-shrink: 0;
}

.header-actions .btn {
  white-space: nowrap;
  padding: 0.65rem 1.15rem;
  font-size: 0.88rem;
}

.mobile-menu-btn {
  display: none;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  background: var(--bg-card);
  color: var(--text-main);
  cursor: pointer;
}

/* Buttons (#UI-01: 4px/8px radius) */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.55rem;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 0.95rem;
  padding: 0.85rem 1.45rem;
  border-radius: var(--radius-sm);
  border: 1px solid transparent;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
  line-height: 1.2;
}

.btn svg {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
}

.btn-primary {
  background-color: var(--oak-gold);
  color: #14181d;
  border-color: var(--oak-gold);
}

.btn-primary:hover {
  background-color: var(--oak-gold-hover);
  border-color: var(--oak-gold-hover);
  color: #ffffff;
}

.btn-dark {
  background-color: var(--bg-anthracite);
  color: #ffffff;
  border-color: var(--bg-anthracite);
}

.btn-dark:hover {
  background-color: var(--oak-gold-dark);
  border-color: var(--oak-gold-dark);
}

.btn-outline {
  background-color: transparent;
  color: var(--text-main);
  border-color: var(--border-light);
}

.btn-outline:hover {
  border-color: var(--oak-gold-dark);
  color: var(--oak-gold-dark);
  background-color: var(--oak-gold-pale);
}

.section-dark .btn-outline,
.hero-section .btn-outline,
.ausbau-banner .btn-outline,
.calc-result-panel .btn-outline,
.site-footer .btn-outline {
  color: var(--text-light);
  border-color: rgba(255, 255, 255, 0.38);
  background-color: rgba(255, 255, 255, 0.05);
}

.section-dark .btn-outline:hover,
.hero-section .btn-outline:hover,
.ausbau-banner .btn-outline:hover,
.calc-result-panel .btn-outline:hover,
.site-footer .btn-outline:hover {
  background-color: rgba(200, 138, 54, 0.22);
  border-color: var(--oak-gold);
  color: #ffffff;
}

/* Sections */
section {
  padding: 5rem 0;
}

.section-alt {
  background-color: var(--bg-ivory-alt);
  border-top: 1px solid var(--border-light);
  border-bottom: 1px solid var(--border-light);
}

.section-dark {
  background-color: var(--bg-anthracite);
  color: var(--text-light);
}

.section-header {
  margin-bottom: 3rem;
}

.section-header.center {
  text-align: center;
  max-width: 780px;
  margin-left: auto;
  margin-right: auto;
}

.section-header.center .lead-text {
  margin-left: auto;
  margin-right: auto;
}

/* Hero Section */
.hero-section {
  position: relative;
  padding: 4.5rem 0 5rem;
  background: linear-gradient(135deg, #14181d 0%, #1d232b 100%);
  color: var(--text-light);
  border-bottom: 3px solid var(--oak-gold);
}

.hero-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 3.25rem;
  align-items: stretch;
}
.hero-grid > div:first-child {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.hero-trust-row {
  margin-top: auto;
}

.hero-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  margin-bottom: 1.5rem;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  font-family: var(--font-display);
  font-size: 0.8rem;
  font-weight: 700;
  padding: 0.4rem 0.8rem;
  border-radius: var(--radius-sm);
  background: rgba(200, 138, 54, 0.18);
  border: 1px solid rgba(200, 138, 54, 0.45);
  color: #f5ca86;
}

.hero-badge svg {
  width: 15px;
  height: 15px;
}

.hero-cta-group {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin: 2rem 0;
}

.hero-trust-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  padding-top: 1.75rem;
  border-top: 1px solid rgba(255, 255, 255, 0.14);
}

.hero-trust-item {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.hero-trust-val {
  font-family: var(--font-display);
  font-weight: 800;
  font-size: 1.15rem;
  color: #f5ca86;
}

.hero-trust-lbl {
  font-size: 0.82rem;
  color: var(--text-light-muted);
}

.hero-visual-card {
  position: relative;
  background: var(--bg-anthracite-soft);
  border: 1px solid rgba(200, 138, 54, 0.35);
  border-radius: var(--radius-md);
  padding: 1rem;
  box-shadow: var(--shadow-elevated);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

.hero-visual-card img.hero-main-img {
  width: 100%;
  height: 360px;
  min-height: 320px;
  flex: 1 1 auto;
  object-fit: cover;
  border-radius: var(--radius-sm);
}

.hero-founder-overlay {
  display: flex;
  align-items: center;
  gap: 0.9rem;
  background: rgba(20, 24, 29, 0.94);
  border: 1px solid rgba(200, 138, 54, 0.45);
  border-radius: var(--radius-sm);
  padding: 0.85rem 1rem;
  margin-top: 0.9rem;
}

.hero-founder-overlay img {
  width: 56px;
  height: 56px;
  object-fit: cover;
  object-position: top center;
  border-radius: var(--radius-sm);
  border: 2px solid var(--oak-gold);
  flex-shrink: 0;
}

.hero-founder-meta strong {
  display: block;
  font-family: var(--font-display);
  font-size: 0.95rem;
  color: #ffffff;
}

.hero-founder-meta span {
  font-size: 0.82rem;
  color: var(--text-light-muted);
}

/* Problem / Pain Points Grid */
.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.75rem;
}

.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
}

.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

.card {
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 2rem;
  box-shadow: var(--shadow-card);
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.section-dark .card {
  background: var(--bg-anthracite-soft);
  border-color: var(--border-dark);
}

.card-icon {
  width: 48px;
  height: 48px;
  border-radius: var(--radius-sm);
  background: var(--oak-gold-pale);
  border: 1px solid rgba(200, 138, 54, 0.35);
  color: var(--oak-gold-dark);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.section-dark .card-icon {
  background: rgba(200, 138, 54, 0.15);
  color: #f5ca86;
}

.card-icon svg {
  width: 24px;
  height: 24px;
}

.card h3 {
  font-size: 1.25rem;
  font-weight: 700;
}

.card p {
  color: var(--text-muted);
  font-size: 0.96rem;
}

.section-dark .card p {
  color: var(--text-light-muted);
}

/* Tragwerk Split Section */
.tragwerk-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}

.tragwerk-visual-box {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  box-shadow: var(--shadow-card);
}

.tragwerk-visual-box img {
  width: 100%;
  max-height: 460px;
  object-fit: contain;
  margin: 0 auto;
}

.check-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-top: 0.5rem;
}

.check-list li {
  display: flex;
  align-items: flex-start;
  gap: 0.65rem;
  font-size: 0.96rem;
  color: var(--text-main);
}

.section-dark .check-list li,
.hero-section .check-list li,
.ausbau-banner .check-list li {
  color: var(--text-light);
}

.check-list li svg {
  width: 19px;
  height: 19px;
  color: var(--oak-gold-dark);
  flex-shrink: 0;
  margin-top: 0.2rem;
}

.section-dark .check-list li svg,
.hero-section .check-list li svg,
.ausbau-banner .check-list li svg {
  color: #f5ca86;
}

/* Service Pillar Cards */
.pillar-card {
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-card);
  display: flex;
  flex-direction: column;
}

.pillar-img-wrap {
  background: var(--bg-ivory-alt);
  padding: 1.5rem;
  border-bottom: 1px solid var(--border-light);
  display: flex;
  align-items: center;
  justify-content: center;
  height: 220px;
}

.pillar-img-wrap img {
  max-height: 180px;
  width: auto;
  object-fit: contain;
}

.pillar-body {
  padding: 1.75rem;
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  flex: 1;
}

.pillar-num {
  font-family: var(--font-display);
  font-size: 0.76rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--oak-gold-dark);
}

/* Interactive Calculator (Sichtbarkeits- & Anfrage-Potenzial-Rechner) */
.calc-wrapper {
  background: var(--bg-card);
  border: 2px solid var(--oak-gold);
  border-radius: var(--radius-md);
  padding: 2.5rem;
  box-shadow: var(--shadow-elevated);
  color: var(--text-main);
}

.calc-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 2.5rem;
  align-items: stretch;
}

.calc-group {
  margin-bottom: 1.75rem;
}

.calc-label {
  display: block;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 0.98rem;
  margin-bottom: 0.75rem;
  color: var(--text-main);
}

.calc-options {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.75rem;
}

.calc-options-2x2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem;
}

.calc-opt-btn {
  font-family: var(--font-display);
  font-size: 0.88rem;
  font-weight: 600;
  padding: 0.85rem 0.9rem;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  background: var(--bg-ivory);
  color: var(--text-main);
  cursor: pointer;
  text-align: left;
  transition: all 0.18s ease;
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.calc-opt-btn span.sub {
  font-family: var(--font-body);
  font-size: 0.76rem;
  font-weight: 400;
  color: var(--text-muted);
}

.calc-opt-btn:hover {
  border-color: var(--oak-gold);
}

.calc-opt-btn.active {
  background: var(--bg-anthracite);
  color: #ffffff;
  border-color: var(--bg-anthracite);
}

.calc-opt-btn.active span.sub {
  color: #f5ca86;
}

.calc-result-panel {
  background: var(--bg-anthracite);
  color: var(--text-light);
  border-radius: var(--radius-md);
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border: 1px solid var(--border-dark);
}

.calc-kpi-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin: 1.25rem 0;
}

.calc-kpi-box {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(200, 138, 54, 0.35);
  border-radius: var(--radius-sm);
  padding: 1rem;
}

.calc-kpi-val {
  font-family: var(--font-display);
  font-size: 1.65rem;
  font-weight: 800;
  color: #f5ca86;
  line-height: 1.15;
}

.calc-kpi-lbl {
  font-size: 0.8rem;
  color: var(--text-light-muted);
  margin-top: 0.25rem;
}

.calc-focus-box {
  background: rgba(200, 138, 54, 0.14);
  border-left: 3px solid var(--oak-gold);
  padding: 0.9rem 1rem;
  border-radius: var(--radius-sm);
  font-size: 0.9rem;
  color: var(--text-light);
  margin-bottom: 1.25rem;
}

/* Step Cards (4-step processes) */
.step-card {
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  box-shadow: var(--shadow-card);
}

.step-card img {
  width: 100%;
  height: 160px;
  object-fit: contain;
  background: var(--bg-ivory);
  border-radius: var(--radius-sm);
  padding: 0.5rem;
  border: 1px solid var(--border-light);
}

.step-badge {
  display: inline-block;
  align-self: flex-start;
  font-family: var(--font-display);
  font-size: 0.75rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 0.25rem 0.6rem;
  border-radius: var(--radius-sm);
  background: var(--oak-gold-pale);
  color: var(--oak-gold-dark);
}

/* Founder / About Section */
.founder-grid {
  display: grid;
  grid-template-columns: 0.85fr 1.15fr;
  gap: 3.25rem;
  align-items: center;
}

.founder-photo-card {
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 1rem;
  box-shadow: var(--shadow-elevated);
}

.founder-photo-card img {
  width: 100%;
  max-height: 540px;
  object-fit: cover;
  object-position: top center;
  border-radius: var(--radius-sm);
}

.founder-caption {
  padding: 1rem 0.5rem 0.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

/* FAQ Accordion */
.faq-list {
  max-width: 880px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 0.9rem;
}

.faq-item {
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  overflow: hidden;
}

.faq-item summary {
  list-style: none;
  cursor: pointer;
  padding: 1.25rem 1.5rem;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1.04rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  color: var(--text-main);
}

.faq-item summary::-webkit-details-marker {
  display: none;
}

.faq-item summary svg {
  width: 20px;
  height: 20px;
  color: var(--oak-gold-dark);
  flex-shrink: 0;
  transition: transform 0.2s ease;
}

.faq-item[open] summary svg {
  transform: rotate(180deg);
}

.faq-answer {
  padding: 0 1.5rem 1.35rem;
  color: var(--text-muted);
  font-size: 0.96rem;
  border-top: 1px solid var(--border-light);
  padding-top: 1rem;
}

/* 3-Step Smart-Anfrage Widget */
.anfrage-card {
  background: var(--bg-card);
  border: 2px solid var(--oak-gold);
  border-radius: var(--radius-md);
  padding: 2.5rem;
  box-shadow: var(--shadow-elevated);
  color: var(--text-main);
}

.anfrage-steps-indicator {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1.75rem;
  flex-wrap: wrap;
}

.step-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  font-family: var(--font-display);
  font-size: 0.82rem;
  font-weight: 700;
  padding: 0.4rem 0.8rem;
  border-radius: var(--radius-sm);
  background: var(--bg-ivory-alt);
  color: var(--text-muted);
  border: 1px solid var(--border-light);
}

.step-pill.active {
  background: var(--bg-anthracite);
  color: #f5ca86;
  border-color: var(--bg-anthracite);
}

.choice-chips {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem;
  margin-bottom: 1.25rem;
}

.choice-chip {
  padding: 0.85rem 1rem;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  background: var(--bg-ivory);
  font-family: var(--font-display);
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--text-main);
  cursor: pointer;
  text-align: left;
  transition: all 0.18s ease;
}

.choice-chip.selected,
.choice-chip:hover {
  border-color: var(--oak-gold-dark);
  background: var(--oak-gold-pale);
  color: var(--text-main);
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-bottom: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.form-group.full {
  grid-column: 1 / -1;
}

.form-group label {
  font-family: var(--font-display);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--text-main);
}

.form-control {
  font-family: var(--font-body);
  font-size: 0.95rem;
  padding: 0.75rem 0.9rem;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  background: #ffffff;
  color: var(--text-main);
}

.form-control:focus {
  outline: 2px solid var(--oak-gold);
  border-color: var(--oak-gold);
}

/* V2 Preview / Ausbaustufe Card & Drawer */
.ausbau-banner {
  background: linear-gradient(135deg, #14181d 0%, #222933 100%);
  color: var(--text-light);
  border: 2px solid var(--oak-gold);
  border-radius: var(--radius-md);
  padding: 2.5rem;
  box-shadow: var(--shadow-elevated);
  margin-bottom: 2.5rem;
}

.ausbau-drawer-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(20, 24, 29, 0.72);
  backdrop-filter: blur(4px);
  z-index: 200;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 1.25rem;
}

.ausbau-drawer-backdrop.open {
  display: flex;
}

.ausbau-drawer {
  background: var(--bg-card);
  color: var(--text-main);
  border: 2px solid var(--oak-gold);
  border-radius: var(--radius-md);
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  padding: 2rem;
  box-shadow: var(--shadow-elevated);
}

/* Footer */
.site-footer {
  background: var(--bg-anthracite);
  color: var(--text-light-muted);
  padding: 4.5rem 0 2.5rem;
  border-top: 3px solid var(--oak-gold);
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.3fr 1fr 1fr 1.1fr;
  gap: 2.5rem;
  margin-bottom: 3rem;
}

.footer-title {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1rem;
  color: #ffffff;
  margin-bottom: 1rem;
}

.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  font-size: 0.92rem;
}

.footer-links a,
.footer-bottom a,
.card p a {
  display: inline-flex;
  align-items: center;
  min-height: 32px;
  padding: 4px 0;
}

.footer-links a:hover {
  color: #f5ca86;
}

.footer-bottom {
  padding-top: 1.75rem;
  border-top: 1px solid var(--border-dark);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
  font-size: 0.85rem;
}

/* Responsive Media Queries */
@media (max-width: 1024px) {
  .hero-grid,
  .tragwerk-split,
  .calc-grid,
  .founder-grid {
    grid-template-columns: 1fr;
  }
  .grid-4 {
    grid-template-columns: repeat(2, 1fr);
  }
  .footer-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .top-meta-bar {
    display: none;
  }
  .brand-logo {
    flex-shrink: 1;
    min-width: 0;
    gap: 0.5rem;
  }
  .brand-logo img {
    height: 34px;
  }
  .brand-tagline {
    display: none;
  }
  .mobile-menu-btn {
    display: inline-flex;
    flex-shrink: 0;
  }
  .main-nav {
    display: none;
    position: absolute;
    top: 82px;
    left: 0;
    right: 0;
    background: var(--bg-ivory);
    border-bottom: 2px solid var(--oak-gold);
    flex-direction: column;
    align-items: flex-start;
    padding: 1.25rem 1.5rem;
    gap: 1rem;
    box-shadow: var(--shadow-elevated);
  }
  .main-nav.open {
    display: flex;
  }
  .header-actions .btn-header-cta {
    display: none;
  }
  .grid-3,
  .grid-2,
  .grid-4,
  .calc-options,
  .calc-options-2x2,
  .choice-chips,
  .form-grid,
  .footer-grid,
  .hero-trust-row {
    grid-template-columns: 1fr;
  }
  section {
    padding: 3.5rem 0;
  }
  .calc-wrapper,
  .anfrage-card,
  .ausbau-banner {
    padding: 1.5rem;
  }
}
"""

(V1_DIR / "style.css").write_text(STYLE_CSS, encoding="utf-8")
(V2_DIR / "style.css").write_text(STYLE_CSS, encoding="utf-8")
print("Wrote style.css for V1 and V2.")

# ---------------------------------------------------------
# 3. LUCIDE SVG ICONS & SHARED COMPONENTS
# ---------------------------------------------------------
ICONS = {
    "hammer": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 12-8.5 8.5c-.83.83-2.17.83-3 0 0 0 0 0 0 0a2.12 2.12 0 0 1 0-3L12 9"/><path d="M17.64 15 22 10.64"/><path d="m20.91 11.7-1.25-1.25c-.6-.6-.93-1.4-.93-2.25v-.86L16.01 4.6a5.56 5.56 0 0 0-3.94-1.64H9l.92.82A6.18 6.18 0 0 1 12 8.4v1.56l2 2h2.47l2.26 1.91"/></svg>',
    "compass": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
    "arrow_right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>',
    "map_pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/></svg>',
    "layout": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/></svg>',
    "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>',
    "message_square": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    "cpu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/></svg>',
    "calculator": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="20" x="4" y="2" rx="2"/><line x1="8" x2="16" y1="6" y2="6"/><line x1="16" x2="16" y1="14" y2="18"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/></svg>',
    "chevron_down": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
    "award": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/></svg>',
    "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/></svg>'
}


def render_calculator_section() -> str:
    return f"""
<section id="potenzial-rechner" class="section-alt">
  <div class="container">
    <div class="section-header center">
      <div class="section-kicker">{ICONS["calculator"]} Interaktiver Schreinerei-Rechner</div>
      <h2 class="h2-section">Sichtbarkeits- &amp; Anfrage-Potenzial für Ihren Betrieb berechnen</h2>
      <p class="lead-text">Wählen Sie Ihre Betriebsgrösse und Ihren handwerklichen Schwerpunkt. Der Rechner zeigt Ihnen auf Basis realer Erfahrungswerte aus dem Schweizer Holzhandwerk, welches monatliche Anfrage- und Zeitspar-Potenzial im «IMP Sichtbarkeits-Tragwerk» steckt.</p>
    </div>

    <div class="calc-wrapper">
      <div class="calc-grid">
        <div>
          <div class="calc-group">
            <label class="calc-label">1. Wie viele Mitarbeitende zählt Ihr Betrieb (inkl. Werkstatt, Montage &amp; Lernende)?</label>
            <div class="calc-options" id="calc-size-group">
              <button type="button" class="calc-opt-btn" data-size="1-5" onclick="window.updateImpCalc('size','1-5')">
                <strong>1–5 Mitarbeitende</strong>
                <span class="sub">Inhabergeführte Werkstatt</span>
              </button>
              <button type="button" class="calc-opt-btn active" data-size="6-10" onclick="window.updateImpCalc('size','6-10')">
                <strong>6–10 Mitarbeitende</strong>
                <span class="sub">Etablierter KMU-Betrieb</span>
              </button>
              <button type="button" class="calc-opt-btn" data-size="11-15" onclick="window.updateImpCalc('size','11-15')">
                <strong>11–15 Mitarbeitende</strong>
                <span class="sub">Grössere Schreinerei / Holzbau</span>
              </button>
            </div>
          </div>

          <div class="calc-group" style="margin-bottom:0;">
            <label class="calc-label">2. Wo liegt Ihr wichtigster Auftrags-Schwerpunkt?</label>
            <div class="calc-options-2x2" id="calc-focus-group">
              <button type="button" class="calc-opt-btn active" data-focus="innenausbau" onclick="window.updateImpCalc('focus','innenausbau')">
                <strong>Innenausbau &amp; Küchen</strong>
                <span class="sub">Massküchen, Badmöbel, Einbauschränke</span>
              </button>
              <button type="button" class="calc-opt-btn" data-focus="moebel" onclick="window.updateImpCalc('focus','moebel')">
                <strong>Möbel &amp; Massivholz</strong>
                <span class="sub">Tische, Einzelstücke, Objektmöbel</span>
              </button>
              <button type="button" class="calc-opt-btn" data-focus="holzbau" onclick="window.updateImpCalc('focus','holzbau')">
                <strong>Holzbau, Dach &amp; Fassade</strong>
                <span class="sub">Elementbau, Umbau, Aufstockung</span>
              </button>
              <button type="button" class="calc-opt-btn" data-focus="fenster" onclick="window.updateImpCalc('focus','fenster')">
                <strong>Fenster, Türen &amp; Sanierung</strong>
                <span class="sub">Haustüren, Brandschutz, Service</span>
              </button>
            </div>
          </div>
        </div>

        <div class="calc-result-panel">
          <div>
            <div class="section-kicker" style="margin-bottom:0.75rem;">{ICONS["compass"]} Ihre realistische Monats-Prognose</div>
            <h3 id="calc-res-title" style="font-size:1.3rem;margin-bottom:0.35rem;color:#ffffff;">6–10 Mitarbeitende · Innenausbau &amp; Küchen</h3>
            <p style="font-size:0.86rem;color:var(--text-light-muted);">Erfahrungswerte für Deutschschweizer Betriebe nach Aufbau von Webseite, Google-Profil und Anfrage-Vorqualifizierung:</p>

            <div class="calc-kpi-grid">
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="calc-res-inquiries">6 bis 10</div>
                <div class="calc-kpi-lbl">Qualifizierte regionale Projektanfragen / Monat</div>
              </div>
              <div class="calc-kpi-box">
                <div class="calc-kpi-val" id="calc-res-hours">12 bis 16 Std.</div>
                <div class="calc-kpi-lbl">Eingesparte Büro- &amp; Telefonzeit / Monat</div>
              </div>
            </div>

            <div class="calc-focus-box" id="calc-res-focus">
              <strong>Empfohlener Tragwerk-Hebel:</strong> Regionale Google-Sichtbarkeit für Küchen- &amp; Innenausbau-Suchanfragen kombiniert mit digitaler Vorqualifizierung (Budgetrahmen, Grundriss &amp; Wunschtermin vor dem ersten Rückruf).
            </div>
          </div>

          <a href="#anfrage" class="btn btn-primary" style="width:100%;" onclick="window.prefillAnfrageFromCalc()">
            Potenzial-Analyse mit diesen Werten starten {ICONS["arrow_right"]}
          </a>
        </div>
      </div>
    </div>
  </div>
</section>
"""


def render_faq_section() -> str:
    faqs = [
        (
            "Warum braucht unsere Schreinerei ein System statt nur einer schönen Webseite?",
            "Eine schön gestaltete Webseite allein bleibt im Alltag oft ein stummes Schaufenster. Erst wenn Ihre regionale Auffindbarkeit bei Google, eine klare Vertrauensführung auf der Webseite und ein geführtes Anfrage-System ineinandergreifen, entstehen daraus verlässliche, vorqualifizierte Kundenanfragen, ohne dass Sie sich täglich um Marketing kümmern müssen."
        ),
        (
            "Wir haben volle Auftragsbücher, weshalb lohnt sich das IMP Sichtbarkeits-Tragwerk trotzdem?",
            "Gerade wenn die Werkstatt ausgelastet ist, kostet jede unpassende Anfrage und jedes ständige Telefonklingeln an der CNC-Maschine oder auf der Montage wertvolle produktive Zeit. Das Sichtbarkeits-Tragwerk filtert Anfragen vorab nach Projektart (z. B. Küchenbau, Innenausbau oder Reparatur), sammelt Masse sowie Fotos strukturiert ein und sorgt dafür, dass Sie genau die Wunschprojekte mit den besten Margen gewinnen."
        ),
        (
            "Was unterscheidet Matthias Iseli (IMP GmbH) von klassischen Werbeagenturen?",
            "Matthias Iseli ist selbst gelernter Schreiner EFZ mit über 15 Jahren praktischer Erfahrung von der Oberflächenbehandlung über die CNC-Bearbeitung bis zur Geschäftsleitung. Bei IMP müssen Sie niemandem erklären, was eine Schattenfuge, eine Massivholz-Bohle oder eine saubere AVOR ist, wir sprechen Ihre Sprache und bauen Systeme, die im echten Werkstatt-Alltag funktionieren."
        ),
        (
            "Wie viel Zeit müssen wir als Betrieb für die Umsetzung investieren?",
            "Wir wissen, dass Ihre Zeit in die Werkstatt, in die Arbeitsvorbereitung und zu Ihren Kunden gehört. Nach einem kompakten Erstgespräch und einer strukturierten Aufnahme übernehmen wir Konzeption, Textierung in klarer Handwerkssprache, Design und technische Einrichtung. Sie prüfen die Etappen bequem und geben frei."
        ),
        (
            "Wie funktioniert ein digitales Anfrage-System oder Chat-Widget für eine Schreinerei?",
            "Statt eines leeren Kontaktformulars («Schreiben Sie uns») führen wir Interessenten durch 3 bis 4 gezielte Fragen: Worum geht es (Küche, Schrank nach Mass, Haustüre, Reparatur)? Wo befindet sich das Objekt? Welcher Zeitrahmen ist gewünscht? Sie erhalten alle Angaben sauber gebündelt per E-Mail oder direkt in Ihre Kundenübersicht, ganz ohne Telefon-Unterbrechung während der Arbeit."
        ),
        (
            "Bleiben wir flexibel oder binden wir uns an teure Agentur-Verträge?",
            "Transparenz und Handschlagqualität stehen bei uns an erster Stelle. Jede Zusammenarbeit startet mit einer klaren Standortbestimmung und einer transparenten Offerte (exkl. MWST). Sie entscheiden Schritt für Schritt, welche Bausteine des IMP Sichtbarkeits-Tragwerks für Ihre aktuelle Betriebsgrösse (1 bis 15 Mitarbeitende) den grössten Nutzen stiften."
        )
    ]
    items_html = []
    for idx, (q, a) in enumerate(faqs):
        open_attr = " open" if idx == 0 else ""
        items_html.append(f"""
        <details class="faq-item"{open_attr}>
          <summary>
            <span>{q}</span>
            {ICONS["chevron_down"]}
          </summary>
          <div class="faq-answer">
            <p>{a}</p>
          </div>
        </details>
        """)
    return f"""
<section id="faq">
  <div class="container">
    <div class="section-header center">
      <div class="section-kicker">{ICONS["shield"]} Häufige Fragen aus dem Handwerk</div>
      <h2 class="h2-section">Klare Antworten für Schreinereien &amp; Holzbau-Betriebe</h2>
      <p class="lead-text">Keine Agentur-Floskeln, sondern ehrliche Antworten aus der Praxis, von Schreiner EFZ zu Schreiner.</p>
    </div>
    <div class="faq-list">
      {''.join(items_html)}
    </div>
  </div>
</section>
"""


def render_smart_anfrage_section() -> str:
    return f"""
<section id="anfrage" class="section-dark">
  <div class="container">
    <div class="tragwerk-split">
      <div>
        <div class="section-kicker">{ICONS["compass"]} Unverbindliche Standortbestimmung</div>
        <h2 class="h2-section">Prüfen wir gemeinsam, wo Ihr Betrieb digital am meisten Hebel hat</h2>
        <p class="lead-text" style="margin-bottom:1.5rem;">In einem strukturierten Gespräch auf Augenhöhe (ca. 20–30 Minuten) schauen wir uns Ihren aktuellen Auftritt, Ihre regionale Google-Sichtbarkeit und Ihren Anfrage-Prozess an.</p>

        <ul class="check-list" style="margin-bottom:2rem;">
          <li>{ICONS["check"]} <span><strong>Direkt mit Matthias Iseli (Schreiner EFZ):</strong> Kein Verkaufsgespräch mit Callcenter-Mitarbeitenden, sondern echte Fachberatung.</span></li>
          <li>{ICONS["check"]} <span><strong>Klare Prioritäten:</strong> Sie erfahren ehrlich, welcher Baustein (Webseite, Google-Profil, Anfrage-System oder Automation) bei Ihnen zuerst Sinn ergibt.</span></li>
          <li>{ICONS["check"]} <span><strong>Regional verankert in Obersteckholz (BE):</strong> Persönlich in der Deutschschweiz oder unkompliziert per Video-Gespräch.</span></li>
        </ul>

        <div class="card" style="padding:1.35rem;gap:0.75rem;">
          <div style="display:flex;align-items:center;gap:0.9rem;">
            <img src="images/portrait-matthias-iseli.jpg" alt="Matthias Iseli – Inhaber IMP GmbH" style="width:62px;height:62px;object-fit:cover;object-position:top center;border-radius:var(--radius-sm);border:2px solid var(--oak-gold);">
            <div>
              <strong style="display:block;font-family:var(--font-display);color:#ffffff;font-size:1rem;">Matthias Iseli</strong>
              <span style="font-size:0.84rem;color:var(--text-light-muted);">Inhaber IMP GmbH · Gelernter Schreiner EFZ</span>
            </div>
          </div>
          <div style="display:flex;flex-wrap:wrap;gap:1.25rem;padding-top:0.5rem;border-top:1px solid var(--border-dark);font-size:0.88rem;">
            <a href="tel:+41762276720" style="display:inline-flex;align-items:center;gap:0.4rem;color:#f5ca86;font-weight:600;">{ICONS["phone"]} +41 76 227 67 20</a>
            <a href="mailto:kontakt@imp-marketing.ch" style="display:inline-flex;align-items:center;gap:0.4rem;color:#f5ca86;font-weight:600;">{ICONS["mail"]} kontakt@imp-marketing.ch</a>
          </div>
        </div>
      </div>

      <div class="anfrage-card">
        <div class="anfrage-steps-indicator">
          <span class="step-pill active" id="anf-pill-1">1. Fokus wählen</span>
          <span class="step-pill" id="anf-pill-2">2. Betriebsdaten</span>
          <span class="step-pill" id="anf-pill-3">3. Zusammenfassung</span>
        </div>

        <form id="imp-smart-anfrage-form" onsubmit="return window.submitImpAnfrage(event)">
          <div id="anf-step-1">
            <h3 style="font-size:1.2rem;margin-bottom:0.4rem;">Welcher Bereich beschäftigt Sie aktuell am meisten?</h3>
            <p style="font-size:0.88rem;color:var(--text-muted);margin-bottom:1rem;">Wählen Sie ein oder mehrere Themen für Ihre Standortbestimmung:</p>

            <div class="choice-chips" id="anf-topic-chips">
              <button type="button" class="choice-chip selected" data-topic="Webseite für Schreinerei / Holzbau" onclick="window.toggleImpChip(this)">Webseite für Schreinerei / Holzbau</button>
              <button type="button" class="choice-chip" data-topic="Google-Geschäftsprofil & Regionale SEO" onclick="window.toggleImpChip(this)">Google-Geschäftsprofil &amp; Regionale SEO</button>
              <button type="button" class="choice-chip" data-topic="Chat-Widget & Anfrage-Vorqualifizierung" onclick="window.toggleImpChip(this)">Chat-Widget &amp; Anfrage-System</button>
              <button type="button" class="choice-chip" data-topic="Datenautomation & Büro-Entlastung" onclick="window.toggleImpChip(this)">Datenautomation &amp; Büro-Entlastung</button>
            </div>

            <div class="form-grid">
              <div class="form-group">
                <label for="anf-size">Betriebsgrösse</label>
                <select id="anf-size" class="form-control">
                  <option value="1–5 Mitarbeitende">1–5 Mitarbeitende</option>
                  <option value="6–10 Mitarbeitende" selected>6–10 Mitarbeitende</option>
                  <option value="11–15 Mitarbeitende">11–15 Mitarbeitende</option>
                  <option value="Über 15 Mitarbeitende">Über 15 Mitarbeitende</option>
                </select>
              </div>
              <div class="form-group">
                <label for="anf-craft">Schwerpunkt</label>
                <select id="anf-craft" class="form-control">
                  <option value="Innenausbau & Küchen" selected>Innenausbau &amp; Küchen</option>
                  <option value="Möbel & Massivholz">Möbel &amp; Massivholz</option>
                  <option value="Holzbau, Dach & Fassade">Holzbau, Dach &amp; Fassade</option>
                  <option value="Fenster, Türen & Sanierung">Fenster, Türen &amp; Sanierung</option>
                </select>
              </div>
            </div>

            <button type="button" class="btn btn-dark" style="width:100%;margin-top:0.5rem;" onclick="window.goImpStep(2)">
              Weiter zu Ihren Kontaktdaten {ICONS["arrow_right"]}
            </button>
          </div>

          <div id="anf-step-2" style="display:none;">
            <h3 style="font-size:1.2rem;margin-bottom:0.4rem;">Wie erreicht Sie Matthias Iseli am besten?</h3>
            <p style="font-size:0.88rem;color:var(--text-muted);margin-bottom:1rem;">Ihre Angaben werden vertraulich behandelt und ausschliesslich für die Vorbereitung Ihres Gesprächs genutzt.</p>

            <div class="form-grid">
              <div class="form-group">
                <label for="anf-name">Vor- und Nachname *</label>
                <input type="text" id="anf-name" class="form-control" placeholder="z. B. Thomas Gerber" required>
              </div>
              <div class="form-group">
                <label for="anf-company">Schreinerei / Holzbau-Betrieb *</label>
                <input type="text" id="anf-company" class="form-control" placeholder="z. B. Gerber Schreinerei AG" required>
              </div>
              <div class="form-group">
                <label for="anf-phone">Telefon / Mobile *</label>
                <input type="tel" id="anf-phone" class="form-control" placeholder="+41 79 ..." required>
              </div>
              <div class="form-group">
                <label for="anf-email">E-Mail-Adresse *</label>
                <input type="email" id="anf-email" class="form-control" placeholder="info@ihre-schreinerei.ch" required>
              </div>
              <div class="form-group full">
                <label for="anf-notes">Optionale Notiz (z. B. aktuelle Webseite oder Wunschzeit für Rückruf)</label>
                <textarea id="anf-notes" class="form-control" rows="2" placeholder="z. B. Erreichbar ab 17:00 Uhr oder mittags zwischen 12:00 und 13:00 Uhr"></textarea>
              </div>
            </div>

            <div style="display:flex;gap:0.75rem;margin-top:0.5rem;">
              <button type="button" class="btn btn-outline" onclick="window.goImpStep(1)">Zurück</button>
              <button type="submit" class="btn btn-primary" style="flex:1;">Unverbindliches Erstgespräch anfragen {ICONS["arrow_right"]}</button>
            </div>
          </div>

          <div id="wpSuccessBox"><div id="anf-step-3" style="display:none;">
            <div style="background:var(--oak-gold-pale);border:1px solid var(--oak-gold);border-radius:var(--radius-sm);padding:1.25rem;margin-bottom:1.25rem;">
              <strong style="display:block;font-family:var(--font-display);font-size:1.1rem;color:var(--oak-gold-dark);margin-bottom:0.35rem;">Vielen Dank! Ihre Anfrage ist bereit.</strong>
              <p style="font-size:0.9rem;color:var(--text-main);" id="anf-summary-text">Matthias Iseli meldet sich zeitnah persönlich bei Ihnen.</p>
            </div>
            <div style="display:flex;flex-wrap:wrap;gap:0.75rem;">
              <a id="anf-mailto-link" href="mailto:kontakt@imp-marketing.ch" class="btn btn-dark" style="flex:1;">Per E-Mail absenden</a>
              <a id="anf-wa-link" href="https://wa.me/41762276720" target="_blank" rel="noopener" class="btn btn-primary" style="flex:1;">Direkt per WhatsApp senden</a>
            </div>
          </div></div>
        </form>
      </div>
    </div>
  </div>
</section>
"""


def render_v2_ausbau_drawer() -> str:
    return f"""
<div class="ausbau-drawer-backdrop" id="imp-ausbau-modal" role="dialog" aria-modal="true" aria-labelledby="imp-ausbau-title">
  <div class="ausbau-drawer">
    <div style="display:flex;align-items:center;justify-content:space-between;gap:1rem;margin-bottom:1rem;">
      <div class="section-kicker" style="margin-bottom:0;">{ICONS["layers"]} Ausbau-Anfrage</div>
      <button type="button" class="btn btn-outline" style="padding:0.4rem 0.75rem;font-size:0.82rem;" onclick="window.closeImpAusbauDrawer()">Schliessen</button>
    </div>
    <h3 id="imp-ausbau-title" style="font-size:1.35rem;margin-bottom:0.5rem;">Ausbau dieser Unterseite anfragen</h3>
    <p style="font-size:0.92rem;color:var(--text-muted);margin-bottom:1.25rem;">In dieser Vorschau ist die Startseite bereits komplett ausgearbeitet. Gerne schalten wir Ihnen auch die vollständige Detailseite <strong id="imp-ausbau-page-label">Leistungen</strong> inklusive aller Prozess-Schritte frei.</p>

    <form onsubmit="return window.submitImpAusbau(event)">
      <div class="form-grid">
        <div class="form-group">
          <label for="ausbau-name">Ihr Name *</label>
          <input type="text" id="ausbau-name" class="form-control" value="Matthias Iseli" required>
        </div>
        <div class="form-group">
          <label for="ausbau-email">Ihre E-Mail *</label>
          <input type="email" id="ausbau-email" class="form-control" value="kontakt@imp-marketing.ch" required>
        </div>
        <div class="form-group full">
          <label for="ausbau-msg">Gewünschte Schwerpunkte auf dieser Unterseite</label>
          <textarea id="ausbau-msg" class="form-control" rows="3" placeholder="Welche Referenzen, Leistungsdetails oder Abläufe sollen wir hier besonders hervorheben?"></textarea>
        </div>
      </div>
      <div id="ausbau-feedback" style="display:none;background:var(--oak-gold-pale);border:1px solid var(--oak-gold);padding:0.85rem;border-radius:var(--radius-sm);margin-bottom:1rem;font-size:0.9rem;color:var(--oak-gold-dark);font-weight:600;">
        Vielen Dank! Ihr Ausbau-Wunsch wurde erfasst. David Hügli (magnet-Xs gmbh) setzt sich direkt mit Ihnen in Verbindung.
      </div>
      <div style="display:flex;gap:0.75rem;">
        <button type="button" class="btn btn-outline" onclick="window.closeImpAusbauDrawer()">Abbrechen</button>
        <button type="submit" class="btn btn-primary" style="flex:1;">Ausbau dieser Seite anfragen {ICONS["arrow_right"]}</button>
      </div>
    </form>
  </div>
</div>
"""


SHARED_JS = """
<script>
/* Interactive Calculator & Smart-Anfrage Logic (0 double-slash comments per #UI-01) */
window.impCalcState = {
  size: '6-10',
  focus: 'innenausbau'
};

window.impCalcData = {
  '1-5': {
    'innenausbau': { inq: '3 bis 6', hrs: '8 bis 11 Std.', label: '1–5 Mitarbeitende · Innenausbau & Küchen', text: 'Empfohlener Tragwerk-Hebel: Klare Positionierung als regionaler Massküchen- & Innenausbau-Spezialist bei Google sowie Vorqualifizierung, damit Sie nicht für reine Preisvergleiche aus der Werkstatt gerufen werden.' },
    'moebel': { inq: '3 bis 5', hrs: '6 bis 9 Std.', label: '1–5 Mitarbeitende · Möbel & Massivholz', text: 'Empfohlener Tragwerk-Hebel: Bildstarke Präsentation Ihrer Massivholz- und Einzelstücke kombiniert mit einem geführten Möbel-Anfrage-Assistenten (Holzart, Masse, Budgetrahmen).' },
    'holzbau': { inq: '3 bis 5', hrs: '8 bis 12 Std.', label: '1–5 Mitarbeitende · Holzbau, Dach & Fassade', text: 'Empfohlener Tragwerk-Hebel: Regionale Sichtbarkeit für Umbau-, Dach- und Fassadenprojekte im Umkreis von 25 km sowie strukturierte Projektaufnahme vor der ersten Baustellen-Besichtigung.' },
    'fenster': { inq: '5 bis 9', hrs: '10 bis 14 Std.', label: '1–5 Mitarbeitende · Fenster, Türen & Sanierung', text: 'Empfohlener Tragwerk-Hebel: Automatisierte Unterscheidung zwischen Kleinreparaturen und lukrativen Fenster-/Haustür-Sanierungen inkl. Foto-Upload durch den Kunden.' }
  },
  '6-10': {
    'innenausbau': { inq: '6 bis 10', hrs: '12 bis 16 Std.', label: '6–10 Mitarbeitende · Innenausbau & Küchen', text: 'Empfohlener Tragwerk-Hebel: Regionale Google-Sichtbarkeit für Küchen- & Innenausbau-Suchanfragen kombiniert mit digitaler Vorqualifizierung (Budgetrahmen, Grundriss & Wunschtermin vor dem ersten Rückruf).' },
    'moebel': { inq: '5 bis 8', hrs: '10 bis 14 Std.', label: '6–10 Mitarbeitende · Möbel & Massivholz', text: 'Empfohlener Tragwerk-Hebel: Vertrauen schaffende Referenz-Architektur auf der Webseite und automatisierte Übergabe aller Kundenwünsche an Ihre AVOR und Offertstellung.' },
    'holzbau': { inq: '5 bis 9', hrs: '13 bis 17 Std.', label: '6–10 Mitarbeitende · Holzbau, Dach & Fassade', text: 'Empfohlener Tragwerk-Hebel: Gezielte regionale Präsenz für Bauherren und Architekten im Mittelland sowie strukturierte Erfassung von Plänen und Etappen vor dem Ersttermin.' },
    'fenster': { inq: '8 bis 14', hrs: '15 bis 20 Std.', label: '6–10 Mitarbeitende · Fenster, Türen & Sanierung', text: 'Empfohlener Tragwerk-Hebel: Digitaler Service- & Sanierungs-Filter, der Serienfotos und Masse direkt beim Kunden abfragt und Ihr Büro massiv von Rückfragen entlastet.' }
  },
  '11-15': {
    'innenausbau': { inq: '9 bis 15', hrs: '18 bis 24 Std.', label: '11–15 Mitarbeitende · Innenausbau & Küchen', text: 'Empfohlener Tragwerk-Hebel: Vollständiges 4-Säulen-Tragwerk mit regionaler Marktführerschaft bei Google, digitaler Vorqualifizierung und direkter Datenautomation für Geschäftsleitung und Projektleiter.' },
    'moebel': { inq: '7 bis 12', hrs: '15 bis 20 Std.', label: '11–15 Mitarbeitende · Möbel & Massivholz', text: 'Empfohlener Tragwerk-Hebel: Hochwertige digitale Markenführung für Privatkunden und Innenarchitekten kombiniert mit strukturierter Projekt-Zuweisung ans Verkaufsteam.' },
    'holzbau': { inq: '8 bis 13', hrs: '19 bis 25 Std.', label: '11–15 Mitarbeitende · Holzbau, Dach & Fassade', text: 'Empfohlener Tragwerk-Hebel: Systematische Sichtbarkeit für grössere Sanierungs-, Elementbau- und Gesamtaufträge inkl. automatisierter Nachfassung offener Offerten.' },
    'fenster': { inq: '12 bis 20', hrs: '22 bis 28 Std.', label: '11–15 Mitarbeitende · Fenster, Türen & Sanierung', text: 'Empfohlener Tragwerk-Hebel: Durchgängige Prozess-Automation vom Online-Erstkontakt über die Terminplanung bis zur strukturierten Übergabe an Service- und Montageteams.' }
  }
};

window.updateImpCalc = function(type, val) {
  window.impCalcState[type] = val;
  var sizeGroup = document.getElementById('calc-size-group');
  if (sizeGroup) {
    var btns = sizeGroup.querySelectorAll('.calc-opt-btn');
    for (var i = 0; i < btns.length; i++) {
      btns[i].classList.toggle('active', btns[i].getAttribute('data-size') === window.impCalcState.size);
    }
  }
  var focusGroup = document.getElementById('calc-focus-group');
  if (focusGroup) {
    var fbtns = focusGroup.querySelectorAll('.calc-opt-btn');
    for (var j = 0; j < fbtns.length; j++) {
      fbtns[j].classList.toggle('active', fbtns[j].getAttribute('data-focus') === window.impCalcState.focus);
    }
  }
  var entry = window.impCalcData[window.impCalcState.size][window.impCalcState.focus];
  if (entry) {
    var tEl = document.getElementById('calc-res-title');
    var iEl = document.getElementById('calc-res-inquiries');
    var hEl = document.getElementById('calc-res-hours');
    var fEl = document.getElementById('calc-res-focus');
    if (tEl) tEl.textContent = entry.label;
    if (iEl) iEl.textContent = entry.inq;
    if (hEl) hEl.textContent = entry.hrs;
    if (fEl) fEl.innerHTML = '<strong>Empfohlener Tragwerk-Hebel:</strong> ' + entry.text.replace('Empfohlener Tragwerk-Hebel: ', '');
  }
};

window.prefillAnfrageFromCalc = function() {
  var sizeSelect = document.getElementById('anf-size');
  var craftSelect = document.getElementById('anf-craft');
  if (sizeSelect) {
    var mapSize = { '1-5': '1–5 Mitarbeitende', '6-10': '6–10 Mitarbeitende', '11-15': '11–15 Mitarbeitende' };
    sizeSelect.value = mapSize[window.impCalcState.size] || '6–10 Mitarbeitende';
  }
  if (craftSelect) {
    var mapCraft = {
      'innenausbau': 'Innenausbau & Küchen',
      'moebel': 'Möbel & Massivholz',
      'holzbau': 'Holzbau, Dach & Fassade',
      'fenster': 'Fenster, Türen & Sanierung'
    };
    craftSelect.value = mapCraft[window.impCalcState.focus] || 'Innenausbau & Küchen';
  }
};

window.toggleImpChip = function(btn) {
  btn.classList.toggle('selected');
};

window.goImpStep = function(stepNum) {
  var s1 = document.getElementById('anf-step-1');
  var s2 = document.getElementById('anf-step-2');
  var s3 = document.getElementById('anf-step-3');
  var p1 = document.getElementById('anf-pill-1');
  var p2 = document.getElementById('anf-pill-2');
  var p3 = document.getElementById('anf-pill-3');
  if (s1) s1.style.display = (stepNum === 1) ? 'block' : 'none';
  if (s2) s2.style.display = (stepNum === 2) ? 'block' : 'none';
  if (s3) s3.style.display = (stepNum === 3) ? 'block' : 'none';
  if (p1) p1.classList.toggle('active', stepNum === 1);
  if (p2) p2.classList.toggle('active', stepNum === 2);
  if (p3) p3.classList.toggle('active', stepNum === 3);
};

window.submitImpAnfrage = function(ev) {
  ev.preventDefault();
  var name = (document.getElementById('anf-name') || {}).value || '';
  var company = (document.getElementById('anf-company') || {}).value || '';
  var phone = (document.getElementById('anf-phone') || {}).value || '';
  var email = (document.getElementById('anf-email') || {}).value || '';
  var size = (document.getElementById('anf-size') || {}).value || '';
  var craft = (document.getElementById('anf-craft') || {}).value || '';
  var notes = (document.getElementById('anf-notes') || {}).value || '';
  var chips = document.querySelectorAll('#anf-topic-chips .choice-chip.selected');
  var topics = [];
  for (var i = 0; i < chips.length; i++) {
    topics.push(chips[i].getAttribute('data-topic'));
  }
  var topicStr = topics.length ? topics.join(', ') : 'Allgemeine Standortbestimmung';
  var summaryEl = document.getElementById('anf-summary-text');
  if (summaryEl) {
    summaryEl.textContent = 'Betrieb: ' + company + ' (' + size + ', ' + craft + ') · Fokus: ' + topicStr + '. Wählen Sie jetzt Ihren bevorzugten Übermittlungskanal:';
  }
  var bodyLines = [
    'Guten Tag Herr Iseli',
    '',
    'gerne frage ich ein unverbindliches Erstgespräch zum IMP Sichtbarkeits-Tragwerk an:',
    '- Betrieb: ' + company,
    '- Ansprechpartner: ' + name,
    '- Betriebsgrösse: ' + size,
    '- Schwerpunkt: ' + craft,
    '- Gewünschter Fokus: ' + topicStr,
    '- Telefon: ' + phone,
    '- E-Mail: ' + email,
    notes ? ('- Notiz: ' + notes) : '',
    '',
    'Freundliche Grüsse',
    name
  ].join('\\n');
  var mailtoEl = document.getElementById('anf-mailto-link');
  if (mailtoEl) {
    mailtoEl.href = 'mailto:kontakt@imp-marketing.ch?subject=' + encodeURIComponent('Anfrage Standortbestimmung – ' + company) + '&body=' + encodeURIComponent(bodyLines);
  }
  var waEl = document.getElementById('anf-wa-link');
  if (waEl) {
    waEl.href = 'https://wa.me/41762276720?text=' + encodeURIComponent(bodyLines);
  }
  window.goImpStep(3);
  return false;
};

window.openImpAusbauDrawer = function(pageTitle) {
  var modal = document.getElementById('imp-ausbau-modal');
  var lbl = document.getElementById('imp-ausbau-page-label');
  if (lbl && pageTitle) lbl.textContent = pageTitle;
  if (modal) modal.classList.add('open');
};

window.closeImpAusbauDrawer = function() {
  var modal = document.getElementById('imp-ausbau-modal');
  if (modal) modal.classList.remove('open');
};

window.submitImpAusbau = function(ev) {
  ev.preventDefault();
  var fb = document.getElementById('ausbau-feedback');
  if (fb) fb.style.display = 'block';
  return false;
};

window.toggleImpMobileNav = function() {
  var nav = document.getElementById('imp-main-nav');
  if (nav) nav.classList.toggle('open');
};
</script>
"""


def render_page_shell(title: str, description: str, active_page: str, body_html: str, is_v2: bool = False) -> str:
    nav_items = [
        ("index.html", "Startseite"),
        ("leistungen.html", "Leistungen"),
        ("methode.html", "Methode"),
        ("ueber-uns.html", "Über uns"),
        ("kontakt.html", "Kontakt"),
    ]
    nav_html = []
    for href, label in nav_items:
        cls = "nav-link active" if href == active_page else "nav-link"
        nav_html.append(f'<a href="{href}" class="{cls}">{label}</a>')

    drawer_html = render_v2_ausbau_drawer() if is_v2 else ""

    return f"""<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <style>
  </style>
</head>
<body>
  <div class="top-meta-bar">
    <div class="container top-meta-inner">
      <div class="top-meta-items">
        <span class="top-meta-item">{ICONS["hammer"]} Von Schreiner EFZ Matthias Iseli, für Schreinereien &amp; Holzbau (1–15 Mitarbeitende)</span>
        <span class="top-meta-item">{ICONS["map_pin"]} Herrengasse 81, 4924 Obersteckholz (BE)</span>
      </div>
      <div class="top-meta-items">
        <a href="tel:+41762276720" class="top-meta-item">{ICONS["phone"]} +41 76 227 67 20</a>
        <a href="mailto:kontakt@imp-marketing.ch" class="top-meta-item">{ICONS["mail"]} kontakt@imp-marketing.ch</a>
      </div>
    </div>
  </div>

  <header class="site-header" data-section="header">
    <div class="container header-inner">
      <a href="index.html" class="brand-logo" aria-label="IMP GmbH Startseite">
        <img src="images/logo.png" alt="IMP-Marketing Logo">
        <div class="brand-sub">
          <span class="brand-title">IMP GmbH</span>
          <span class="brand-tagline">Sichtbarkeits-Systeme für Schreinereien &amp; Holzbau</span>
        </div>
      </a>

      <nav class="main-nav" id="imp-main-nav" aria-label="Hauptnavigation">
        {''.join(nav_html)}
      </nav>

      <div class="header-actions">
        <a href="#anfrage" class="btn btn-primary btn-header-cta">Erstgespräch anfragen</a>
        <button type="button" class="mobile-menu-btn" aria-label="Menü öffnen" onclick="window.toggleImpMobileNav()">
          {ICONS["menu"]}
        </button>
      </div>
    </div>
  </header>

  <main>
    {body_html}
  </main>

  {drawer_html}

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:1rem;">
            <img src="images/logo.png" alt="IMP GmbH Logo" style="height:42px;width:auto;border-radius:var(--radius-sm);background:#ffffff;padding:2px;">
            <div>
              <strong style="display:block;font-family:var(--font-display);color:#ffffff;font-size:1.05rem;">IMP GmbH</strong>
              <span style="font-size:0.8rem;color:var(--text-light-muted);">Matthias Iseli · Schreiner EFZ</span>
            </div>
          </div>
          <p style="font-size:0.9rem;margin-bottom:1rem;">Mehr qualifizierte Anfragen und weniger Büro-Aufwand für Schreinereien und Holzbau-Betriebe in der Deutschschweiz, mit klarer Struktur statt Marketing-Chaos.</p>
          <p style="font-size:0.82rem;color:#f5ca86;font-weight:600;">UID: CHE-446.080.483</p>
        </div>

        <div>
          <div class="footer-title">4 Leistungsbereiche</div>
          <ul class="footer-links">
            <li><a href="leistungen.html#webseiten">Webseiten für Schreinereien &amp; Holzbau</a></li>
            <li><a href="leistungen.html#google-seo">Google-Geschäftsprofil &amp; Regionale SEO</a></li>
            <li><a href="leistungen.html#anfrage-systeme">Chat-Widgets &amp; Anfrage-Systeme</a></li>
            <li><a href="leistungen.html#datenautomation">Datenautomation &amp; Büro-Prozesse</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Navigation &amp; Rechner</div>
          <ul class="footer-links">
            <li><a href="index.html">Startseite</a></li>
            <li><a href="index.html#potenzial-rechner">Schreinerei-Potenzial-Rechner</a></li>
            <li><a href="methode.html">Das IMP Sichtbarkeits-Tragwerk</a></li>
            <li><a href="ueber-uns.html">Über Matthias Iseli</a></li>
            <li><a href="kontakt.html">Kontakt &amp; Impressum</a></li>
          </ul>
        </div>

        <div>
          <div class="footer-title">Direktkontakt Obersteckholz</div>
          <ul class="footer-links">
            <li>Herrengasse 81, 4924 Obersteckholz</li>
            <li>Kanton Bern (Oberaargau), Schweiz</li>
            <li><a href="tel:+41762276720" style="color:#f5ca86;font-weight:600;">+41 76 227 67 20</a></li>
            <li><a href="mailto:kontakt@imp-marketing.ch" style="color:#f5ca86;font-weight:600;">kontakt@imp-marketing.ch</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <span>© 2026 IMP GmbH, 4924 Obersteckholz (CHE-446.080.483). Alle Rechte vorbehalten. Alle Preisangaben verstehen sich exkl. MWST.</span>
        <div style="display:flex;gap:1.25rem;">
          <a href="kontakt.html#impressum">Impressum</a>
          <a href="kontakt.html#datenschutz">Datenschutz</a>
        </div>
      </div>
    </div>
  </footer>

  {SHARED_JS}
</body>
</html>
"""

# ---------------------------------------------------------
# 4. PAGE BUILDERS (V1 FULL & V2 PREVIEW)
# ---------------------------------------------------------

def build_index_body() -> str:
    return f"""
<section class="hero-section">
  <div class="container hero-grid">
    <div>
      <div class="hero-badges">
        <span class="hero-badge">{ICONS["hammer"]} Von Schreiner EFZ Matthias Iseli</span>
        <span class="hero-badge">{ICONS["shield"]} Für Betriebe mit 1–15 Mitarbeitenden</span>
      </div>
      <h1 class="h1-hero">Mehr passende Anfragen für Ihre Schreinerei, ohne Marketing-Chaos.</h1>
      <p class="lead-text" style="color:var(--text-light-muted);margin-bottom:0.5rem;">
        Struktur. Klarheit. Ergebnisse. Wir verbinden moderne Schreiner-Webseiten, regionale Google-Sichtbarkeit, digitale Anfrage-Vorqualifizierung und schlanke Büro-Automation zu einem tragfähigen System, entwickelt aus über 15 Jahren echter Erfahrung in Schreinerei und Holzbau.
      </p>

      <div class="hero-cta-group">
        <a href="#anfrage" class="btn btn-primary">Unverbindliches Erstgespräch buchen {ICONS["arrow_right"]}</a>
        <a href="#potenzial-rechner" class="btn btn-outline">{ICONS["calculator"]} Anfrage-Potenzial berechnen</a>
      </div>

      <div class="hero-trust-row">
        <div class="hero-trust-item">
          <span class="hero-trust-val">15+ Jahre</span>
          <span class="hero-trust-lbl">Berufserfahrung in Schreinerei, CNC, AVOR &amp; Geschäftsleitung</span>
        </div>
        <div class="hero-trust-item">
          <span class="hero-trust-val">4 Säulen</span>
          <span class="hero-trust-lbl">Das IMP Sichtbarkeits-Tragwerk für nachhaltige Kundenanfragen</span>
        </div>
        <div class="hero-trust-item">
          <span class="hero-trust-val">100 % Handwerk</span>
          <span class="hero-trust-lbl">Klare Schweizer Fachsprache statt hohler Agentur-Versprechen</span>
        </div>
      </div>
    </div>

    <div class="hero-visual-card">
      <img src="images/hero-schreinerei.webp" alt="Schweizer Schreinerei und Holzhandwerk – IMP GmbH" class="hero-main-img">
      <div class="hero-founder-overlay">
        <img src="images/portrait-matthias-iseli.jpg" alt="Matthias Iseli – Inhaber IMP GmbH">
        <div class="hero-founder-meta">
          <strong>Matthias Iseli · Inhaber IMP GmbH</strong>
          <span>Gelernter Schreiner EFZ aus Obersteckholz (BE) – Ihr Partner auf Augenhöhe</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-header center">
      <div class="section-kicker">{ICONS["clock"]} Die Realität im Werkstatt-Alltag</div>
      <h2 class="h2-section">Warum klassisches Marketing für Schreinereien oft ins Leere läuft</h2>
      <p class="lead-text">Sie liefern erstklassige Arbeit in der Werkstatt und auf der Montage, doch digital geht wertvolles Potenzial verloren, weil einzelne Massnahmen nicht ineinandergreifen.</p>
    </div>

    <div class="grid-3">
      <div class="card">
        <div class="card-icon">{ICONS["search"]}</div>
        <h3>In der Region zu wenig sichtbar</h3>
        <p>Bauherren und Privatkunden suchen heute bei Google nach «Schreinerei in der Nähe», «Küche nach Mass» oder «Einbauschrank». Ohne gepflegtes Google-Geschäftsprofil und klare lokale Struktur landen diese Aufträge beim Mitbewerber.</p>
      </div>
      <div class="card">
        <div class="card-icon">{ICONS["phone"]}</div>
        <h3>Ständige Unterbrechungen im Betrieb</h3>
        <p>Das Telefon klingelt mitten an der CNC-Fräse, beim Verleimen oder auf der Baustelle. Oft fehlen bei unstrukturierten Anrufen wichtige Angaben wie Masse, Fotos oder Budgetsvorstellungen, das kostet täglich wertvolle Zeit.</p>
      </div>
      <div class="card">
        <div class="card-icon">{ICONS["layers"]}</div>
        <h3>Einzelmassnahmen ohne Tragwerk</h3>
        <p>Hier eine veraltete Webseite, dort ein sporadischer Social-Media-Beitrag und dazwischen Zettelwirtschaft im Büro: Wenn das Fundament und die Verbindung fehlen, verpufft jede Investition ohne messbares Ergebnis.</p>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="tragwerk-split">
      <div class="tragwerk-visual-box">
        <img src="images/sichtbarkeits-tragwerk.png" alt="Das IMP Sichtbarkeits-Tragwerk für Schreinereien und Holzbau">
      </div>
      <div>
        <div class="section-kicker">{ICONS["compass"]} Unsere Methode</div>
        <h2 class="h2-section">Das «IMP Sichtbarkeits-Tragwerk»: Gebaut wie ein sauberer Holzbau</h2>
        <p class="lead-text" style="margin-bottom:1.25rem;">Im Holzbau würde niemand ein Dach ohne tragfähiges Fundament und präzise Verbindungen aufstellen. Genau nach diesem Prinzip haben wir das IMP Sichtbarkeits-Tragwerk für Betriebe mit 1 bis 15 Mitarbeitenden entwickelt:</p>

        <ul class="check-list" style="margin-bottom:1.75rem;">
          <li>{ICONS["check"]} <span><strong>1. Fundament (Positionierung &amp; Vertrauen):</strong> Eine moderne, handwerkliche Webseite, die Ihre Stärken im Innenausbau, Möbelbau oder Holzbau auf den ersten Blick spürbar macht.</span></li>
          <li>{ICONS["check"]} <span><strong>2. Tragende Säulen (Regionale Google-Sichtbarkeit):</strong> Gezielte Auffindbarkeit im Google-Geschäftsprofil und in der lokalen Suche genau dann, wenn Kunden in Ihrer Region Bedarf haben.</span></li>
          <li>{ICONS["check"]} <span><strong>3. Verbindung (Chat-Widgets &amp; Anfrage-Systeme):</strong> Interessenten werden digital vorqualifiziert (Projektart, Masse, Zeitrahmen), bevor Sie zum Hörer greifen.</span></li>
          <li>{ICONS["check"]} <span><strong>4. Aussteifung (Datenautomation im Büro):</strong> Sauber strukturierte Kundendaten und automatische Abläufe vom Erstkontakt bis zur Offerte.</span></li>
        </ul>

        <div style="display:flex;flex-wrap:wrap;gap:0.85rem;">
          <a href="methode.html" class="btn btn-dark">Das Sichtbarkeits-Tragwerk im Detail {ICONS["arrow_right"]}</a>
          <a href="#anfrage" class="btn btn-outline">Standortbestimmung buchen</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-header center">
      <div class="section-kicker">{ICONS["layout"]} Unsere 4 Kernleistungen</div>
      <h2 class="h2-section">Alle Bausteine für Ihren digitalen Vorsprung im Holzhandwerk</h2>
      <p class="lead-text">Jeder Baustein funktioniert einzeln, seine volle Kraft entfaltet er im Zusammenspiel als durchdachtes Gesamtsystem.</p>
    </div>

    <div class="grid-2">
      <div class="pillar-card">
        <div class="pillar-img-wrap">
          <img src="images/service-webseiten.png" alt="Webseiten für Schreinereien und Holzbau">
        </div>
        <div class="pillar-body">
          <span class="pillar-num">Säule 01 · Digitale Werkbank</span>
          <h3>Webseiten für Schreinereien &amp; Holzbau</h3>
          <p>Moderne, klare und vertrauensvolle Webseiten, die Ihre handwerkliche Qualität sichtbar machen, von der Massküche über den Innenausbau bis zum Elementbau. Mobil optimiert, schnell und auf konkrete Kontaktaufnahme ausgerichtet.</p>
          <ul class="check-list" style="margin-bottom:1rem;">
            <li>{ICONS["check"]} <span>Klare Struktur für Privatkunden, Bauherren und Architekten</span></li>
            <li>{ICONS["check"]} <span>Authentische Darstellung Ihrer Referenzen, Werkstatt und Mitarbeitenden</span></li>
          </ul>
          <a href="leistungen.html#webseiten" class="btn btn-outline" style="margin-top:auto;">Mehr zu Schreiner-Webseiten {ICONS["arrow_right"]}</a>
        </div>
      </div>

      <div class="pillar-card">
        <div class="pillar-img-wrap">
          <img src="images/service-google-seo.png" alt="Google-Geschäftsprofil und Regionale SEO für Schreinereien">
        </div>
        <div class="pillar-body">
          <span class="pillar-num">Säule 02 · Regionale Auffindbarkeit</span>
          <h3>Google-Geschäftsprofil &amp; Regionale SEO</h3>
          <p>Werden Sie in Ihrer Region genau dann gefunden, wenn Kunden aktiv nach einer Schreinerei oder einem Holzbau-Betrieb suchen. Wir optimieren Ihr Google-Geschäftsprofil, Ihre lokalen Suchbegriffe und Ihren Bewertungsaufbau.</p>
          <ul class="check-list" style="margin-bottom:1rem;">
            <li>{ICONS["check"]} <span>Top-Präsenz in Google Maps und der regionalen Suche</span></li>
            <li>{ICONS["check"]} <span>Systematischer Aufbau echter 5-Sterne-Kundenbewertungen</span></li>
          </ul>
          <a href="leistungen.html#google-seo" class="btn btn-outline" style="margin-top:auto;">Mehr zu Google &amp; Regionaler SEO {ICONS["arrow_right"]}</a>
        </div>
      </div>

      <div class="pillar-card">
        <div class="pillar-img-wrap">
          <img src="images/service-anfrage-systeme.png" alt="Chat-Widgets und Anfrage-Systeme für Schreinereien">
        </div>
        <div class="pillar-body">
          <span class="pillar-num">Säule 03 · Digitale Vorqualifizierung</span>
          <h3>Chat-Widgets &amp; Anfrage-Systeme</h3>
          <p>Qualifizierte Kundenanfragen rund um die Uhr, ohne dass das Telefon Sie an der Säge oder im Kundengespräch unterbricht. Unser geführtes System fragt Projektart, Masse und Wunschtermin vorab sauber ab.</p>
          <ul class="check-list" style="margin-bottom:1rem;">
            <li>{ICONS["check"]} <span>Gezielte Vorqualifizierung nach Küche, Möbel, Innenausbau oder Service</span></li>
            <li>{ICONS["check"]} <span>Vollständige Angaben vor dem ersten Rückruf</span></li>
          </ul>
          <a href="leistungen.html#anfrage-systeme" class="btn btn-outline" style="margin-top:auto;">Mehr zu Anfrage-Systemen {ICONS["arrow_right"]}</a>
        </div>
      </div>

      <div class="pillar-card">
        <div class="pillar-img-wrap">
          <img src="images/service-datenautomation.png" alt="Datenautomation und Handwerks-Prozesse">
        </div>
        <div class="pillar-body">
          <span class="pillar-num">Säule 04 · Büro-Entlastung</span>
          <h3>Datenautomation &amp; Handwerks-Prozesse</h3>
          <p>Weniger Abtippen, keine verlorenen Notizzettel mehr: Wir verbinden Ihre Online-Anfragen direkt mit Ihrer Kundenübersicht, automatisieren Eingangsbestätigungen und strukturieren den Weg bis zur Offerte.</p>
          <ul class="check-list" style="margin-bottom:1rem;">
            <li>{ICONS["check"]} <span>Zentrale Erfassung aller Kunden- und Projektdaten</span></li>
            <li>{ICONS["check"]} <span>Spürbare Zeitersparnis für Inhaber, AVOR und Sekretariat</span></li>
          </ul>
          <a href="leistungen.html#datenautomation" class="btn btn-outline" style="margin-top:auto;">Mehr zu Datenautomation {ICONS["arrow_right"]}</a>
        </div>
      </div>
    </div>
  </div>
</section>

{render_calculator_section()}

<section class="section-dark">
  <div class="container founder-grid">
    <div class="founder-photo-card">
      <img src="images/portrait-matthias-iseli.jpg" alt="Matthias Iseli – Schreiner EFZ und Inhaber der IMP GmbH">
      <div class="founder-caption">
        <div>
          <strong style="display:block;font-family:var(--font-display);color:var(--text-main);font-size:1rem;">Matthias Iseli</strong>
          <span style="font-size:0.84rem;color:var(--text-muted);">Schreiner EFZ · Inhaber IMP GmbH, Obersteckholz</span>
        </div>
        <img src="images/icon-schreiner-efz.png" alt="Schreiner EFZ Icon" style="width:44px;height:44px;object-fit:contain;">
      </div>
    </div>

    <div>
      <div class="section-kicker">{ICONS["award"]} Aus dem Handwerk, für das Handwerk</div>
      <h2 class="h2-section">«Ich weiss aus eigener Erfahrung, wie der Alltag in einer Schreinerei wirklich aussieht.»</h2>
      <p class="lead-text" style="margin-bottom:1.25rem;">
        Als ausgebildeter <strong>Schreiner EFZ mit über 15 Jahren Berufserfahrung</strong> in Schreinerei und Holzbau, von der Oberflächenbehandlung über die CNC-Bearbeitung bis zur mehrjährigen Führungserfahrung in der Geschäftsleitung, kenne ich beide Seiten: den Stolz auf präzises Handwerk und den täglichen Spagat zwischen Werkstatt, Baustelle und Büro.
      </p>
      <p class="lead-text" style="margin-bottom:1.5rem;">
        Mit der <strong>IMP GmbH in Obersteckholz (Kanton Bern)</strong> habe ich genau den Partner geschaffen, den ich mir im Betrieb selbst immer gewünscht habe: Bodenständig, strukturiert und 100 % auf die Bedürfnisse von Schreinereien und Holzbau-Betrieben (1 bis 15 Mitarbeitende) ausgerichtet.
      </p>

      <div style="display:flex;flex-wrap:wrap;gap:1rem;">
        <a href="ueber-uns.html" class="btn btn-primary">Mehr über Matthias Iseli erfahren {ICONS["arrow_right"]}</a>
        <a href="#anfrage" class="btn btn-outline">Direkt Gespräch vereinbaren</a>
      </div>
    </div>
  </div>
</section>

{render_faq_section()}

{render_smart_anfrage_section()}
"""


def build_leistungen_v1_body() -> str:
    return f"""
<section class="hero-section" style="padding:3.75rem 0;">
  <div class="container">
    <div class="hero-badges">
      <span class="hero-badge">{ICONS["layout"]} 4 spezialisierte Leistungsbereiche</span>
      <span class="hero-badge">{ICONS["hammer"]} Exklusiv für Schreinerei &amp; Holzbau</span>
    </div>
    <h1 class="h1-hero" style="max-width:22ch;">Unsere Leistungen für Schreinereien &amp; Holzbau-Betriebe</h1>
    <p class="lead-text" style="color:var(--text-light-muted);">Jeder Baustein folgt einem klaren 4-Schritte-Ablauf, transparent geplant, sauber umgesetzt und ohne Fachchinesisch in Ihren Betriebsalltag integriert.</p>
  </div>
</section>

<section id="webseiten">
  <div class="container">
    <div class="tragwerk-split" style="margin-bottom:3rem;">
      <div>
        <div class="section-kicker">{ICONS["layout"]} Leistungsbereich 01</div>
        <h2 class="h2-section">Webseiten für Schreinereien &amp; Holzbau</h2>
        <p class="lead-text" style="margin-bottom:1.25rem;">Ihre Webseite ist heute der erste Eindruck bei Bauherren, Privatkunden, Architekten und zukünftigen Lernenden oder Fachkräften. Wir bauen Webseiten, die Ihre echte Handwerksqualität widerspiegeln und Besucher gezielt zur Anfrage führen.</p>
        <ul class="check-list">
          <li>{ICONS["check"]} <span>Klare Leistungsarchitektur (Innenausbau, Küchen, Möbel, Türen, Holzbau)</span></li>
          <li>{ICONS["check"]} <span>Perfekte Darstellung auf Smartphone, Tablet und Desktop</span></li>
          <li>{ICONS["check"]} <span>Texte in authentischer Schweizer Handwerkssprache – Sie müssen nichts selbst schreiben</span></li>
        </ul>
      </div>
      <div class="tragwerk-visual-box">
        <img src="images/service-webseiten.png" alt="Webseiten für Schreinereien">
      </div>
    </div>

    <div class="grid-4">
      <div class="step-card">
        <img src="images/web-step-1-analyse.png" alt="Schritt 1: Kennenlernen & Analyse">
        <span class="step-badge">Schritt 01</span>
        <h3>Kennenlernen &amp; Analyse</h3>
        <p>Wir besprechen Ihre Stärken, Ihre Wunschprojekte und Ihr Einzugsgebiet und prüfen Ihren bisherigen Auftritt.</p>
      </div>
      <div class="step-card">
        <img src="images/web-step-2-konzept.png" alt="Schritt 2: Konzept & Design">
        <span class="step-badge">Schritt 02</span>
        <h3>Konzept &amp; Struktur</h3>
        <p>Wir entwickeln eine klare Seitenstruktur, überzeugende Fachtexte und ein hochwertiges Design passend zu Ihrem Betrieb.</p>
      </div>
      <div class="step-card">
        <img src="images/web-step-3-umsetzung.jpg" alt="Schritt 3: Technische Umsetzung">
        <span class="step-badge">Schritt 03</span>
        <h3>Präzise Umsetzung</h3>
        <p>Saubere technische Realisierung für schnelle Ladezeiten, mobile Bedienbarkeit und direkte Anfrage-Führung.</p>
      </div>
      <div class="step-card">
        <img src="images/web-step-4-betreuung.png" alt="Schritt 4: Veröffentlichung & Betreuung">
        <span class="step-badge">Schritt 04</span>
        <h3>Go-Live &amp; Betreuung</h3>
        <p>Nach Ihrer Freigabe schalten wir die Webseite live und kümmern uns auf Wunsch laufend um Aktualisierungen.</p>
      </div>
    </div>
  </div>
</section>

<section id="google-seo" class="section-alt">
  <div class="container">
    <div class="tragwerk-split" style="margin-bottom:3rem;">
      <div class="tragwerk-visual-box">
        <img src="images/service-google-seo.png" alt="Google-Geschäftsprofil & Regionale SEO">
      </div>
      <div>
        <div class="section-kicker">{ICONS["search"]} Leistungsbereich 02</div>
        <h2 class="h2-section">Google-Geschäftsprofil &amp; Regionale SEO</h2>
        <p class="lead-text" style="margin-bottom:1.25rem;">Wer in Ihrer Region einen Schreiner oder Zimmermann sucht, entscheidet meist innerhalb der ersten drei Google-Ergebnisse. Wir sorgen dafür, dass Ihr Betrieb dort präsent und vertrauenswürdig auftritt.</p>
        <ul class="check-list">
          <li>{ICONS["check"]} <span>Vollständige Einrichtung und Pflege Ihres Google-Geschäftsprofils</span></li>
          <li>{ICONS["check"]} <span>Regionale Suchbegriffe für Ihren Ort und Ihr Einzugsgebiet</span></li>
          <li>{ICONS["check"]} <span>Einfacher Prozess für echte Kundenbewertungen nach Projektabschluss</span></li>
        </ul>
      </div>
    </div>

    <div class="grid-4">
      <div class="step-card">
        <img src="images/seo-step-1-analyse.png" alt="Schritt 1: Profil- & Standortanalyse">
        <span class="step-badge">Schritt 01</span>
        <h3>Standort-Analyse</h3>
        <p>Prüfung Ihrer aktuellen Platzierungen in Google Maps und der regionalen Suche im Vergleich zum Mitbewerb.</p>
      </div>
      <div class="step-card">
        <img src="images/seo-step-2-struktur.png" alt="Schritt 2: Struktur & lokale Keywords">
        <span class="step-badge">Schritt 02</span>
        <h3>Lokale Struktur</h3>
        <p>Optimierung aller Kategorien, Leistungsbeschreibungen, Einzugsgebiete und regionalen Suchbegriffe.</p>
      </div>
      <div class="step-card">
        <img src="images/seo-step-3-bewertungen.png" alt="Schritt 3: Aktiver Bewertungsaufbau">
        <span class="step-badge">Schritt 03</span>
        <h3>Bewertungs-System</h3>
        <p>Einrichtung einer unkomplizierten Bewertungseinladung (z. B. per QR-Code oder Kurzlink nach der Montage).</p>
      </div>
      <div class="step-card">
        <img src="images/seo-step-4-pflege.png" alt="Schritt 4: Laufende Pflege">
        <span class="step-badge">Schritt 04</span>
        <h3>Laufende Pflege</h3>
        <p>Regelmässige Projektfotos, aktuelle Beiträge und professionelle Beantwortung von Kundenrezensionen.</p>
      </div>
    </div>
  </div>
</section>

<section id="anfrage-systeme">
  <div class="container">
    <div class="tragwerk-split" style="margin-bottom:3rem;">
      <div>
        <div class="section-kicker">{ICONS["message_square"]} Leistungsbereich 03</div>
        <h2 class="h2-section">Chat-Widgets &amp; Digitale Anfrage-Systeme</h2>
        <p class="lead-text" style="margin-bottom:1.25rem;">Schluss mit unvollständigen Kontaktformularen und ständigen Telefon-Unterbrechungen an der Maschine: Unser Anfrage-System führt Interessenten freundlich und strukturiert durch die wichtigsten Eckdaten.</p>
        <ul class="check-list">
          <li>{ICONS["check"]} <span>Klare Vorqualifizierung nach Küchenbau, Innenausbau, Möbel, Fenster/Türen oder Reparatur</span></li>
          <li>{ICONS["check"]} <span>Abfrage von Ort, Zeitrahmen und optionalen Fotos/Skizzen</span></li>
          <li>{ICONS["check"]} <span>Sofortige Übersicht auf Ihrem Smartphone oder PC</span></li>
        </ul>
      </div>
      <div class="tragwerk-visual-box">
        <img src="images/service-anfrage-systeme.png" alt="Chat-Widgets & Anfrage-Systeme">
      </div>
    </div>

    <div class="grid-4">
      <div class="step-card">
        <img src="images/chat-step-1-analyse.png" alt="Schritt 1: Anfrage-Analyse">
        <span class="step-badge">Schritt 01</span>
        <h3>Anfrage-Analyse</h3>
        <p>Wir klären, welche Angaben Sie in der AVOR zwingend benötigen, um eine Anfrage rasch einschätzen zu können.</p>
      </div>
      <div class="step-card">
        <img src="images/chat-step-2-planung.png" alt="Schritt 2: Fragen- & Dialogplanung">
        <span class="step-badge">Schritt 02</span>
        <h3>Dialog-Planung</h3>
        <p>Aufbau eines kurzen, leicht verständlichen Fragenflusses für Ihre Kunden, ohne technisches Hindernis.</p>
      </div>
      <div class="step-card">
        <img src="images/chat-step-3-integration.png" alt="Schritt 3: Nahtlose Integration">
        <span class="step-badge">Schritt 03</span>
        <h3>Integration</h3>
        <p>Einbindung in Ihre Webseite und Verknüpfung mit Ihrer E-Mail oder Ihrem Benachrichtigungskanal.</p>
      </div>
      <div class="step-card">
        <img src="images/chat-step-4-optimierung.png" alt="Schritt 4: Feinabstimmung">
        <span class="step-badge">Schritt 04</span>
        <h3>Feinabstimmung</h3>
        <p>Laufende Optimierung anhand echter Kundenanfragen, damit die Qualität der Kontakte stetig steigt.</p>
      </div>
    </div>
  </div>
</section>

<section id="datenautomation" class="section-alt">
  <div class="container">
    <div class="tragwerk-split" style="margin-bottom:3rem;">
      <div class="tragwerk-visual-box">
        <img src="images/service-datenautomation.png" alt="Datenautomation & Handwerks-Prozesse">
      </div>
      <div>
        <div class="section-kicker">{ICONS["cpu"]} Leistungsbereich 04</div>
        <h2 class="h2-section">Datenautomation &amp; Büro-Entlastung</h2>
        <p class="lead-text" style="margin-bottom:1.25rem;">Damit im Büro keine Anfrage zwischen E-Mail-Postfach, WhatsApp und Werkstatt-Notizblock verloren geht, automatisieren wir wiederkehrende Abläufe pragmatisch und zuverlässig.</p>
        <ul class="check-list">
          <li>{ICONS["check"]} <span>Automatische Ablage neuer Kundenanfragen in einer klaren Projektübersicht</span></li>
          <li>{ICONS["check"]} <span>Freundliche, sofortige Eingangsbestätigung an den Kunden im Namen Ihres Betriebs</span></li>
          <li>{ICONS["check"]} <span>Strukturierte Erinnerungen für Besichtigungen und Offert-Nachfassungen</span></li>
        </ul>
      </div>
    </div>

    <div class="grid-4">
      <div class="step-card">
        <img src="images/auto-step-1-ablaeufe.png" alt="Schritt 1: Abläufe aufnehmen">
        <span class="step-badge">Schritt 01</span>
        <h3>Abläufe aufnehmen</h3>
        <p>Wir schauen uns an, wie Anfragen, Termine und Offerten heute durch Ihr Büro laufen und wo Zeit verloren geht.</p>
      </div>
      <div class="step-card">
        <img src="images/auto-step-2-planung.png" alt="Schritt 2: Prozess-Struktur planen">
        <span class="step-badge">Schritt 02</span>
        <h3>Prozess planen</h3>
        <p>Entwurf eines schlanken, übersichtlichen Ablaufs, den jeder im Betrieb sofort versteht.</p>
      </div>
      <div class="step-card">
        <img src="images/auto-step-3-umsetzung.png" alt="Schritt 3: Saubere Einrichtung">
        <span class="step-badge">Schritt 03</span>
        <h3>Einrichtung</h3>
        <p>Technische Verknüpfung Ihrer Formulare, E-Mails, Kalender und Übersichtslisten im Hintergrund.</p>
      </div>
      <div class="step-card">
        <img src="images/auto-step-4-einfuehrung.png" alt="Schritt 4: Einführung im Betrieb">
        <span class="step-badge">Schritt 04</span>
        <h3>Einführung</h3>
        <p>Verständliche Übergabe an Sie und Ihr Team inklusive persönlicher Begleitung im Alltag.</p>
      </div>
    </div>
  </div>
</section>

{render_smart_anfrage_section()}
"""


def build_methode_v1_body() -> str:
    return f"""
<section class="hero-section" style="padding:3.75rem 0;">
  <div class="container">
    <div class="hero-badges">
      <span class="hero-badge">{ICONS["compass"]} Das IMP Sichtbarkeits-Tragwerk</span>
      <span class="hero-badge">{ICONS["hammer"]} Systematik statt Zufall</span>
    </div>
    <h1 class="h1-hero" style="max-width:22ch;">Wie das «IMP Sichtbarkeits-Tragwerk» Ihren Betrieb entlastet</h1>
    <p class="lead-text" style="color:var(--text-light-muted);">Ein Tragwerk im Holzbau hält nur dann über Jahrzehnte, wenn Fundament, Stützen, Verbindungen und Aussteifung sauber aufeinander abgestimmt sind. Genau so bauen wir Ihre digitale Kundengewinnung auf.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="tragwerk-split">
      <div class="tragwerk-visual-box">
        <img src="images/sichtbarkeits-tragwerk.png" alt="IMP Sichtbarkeits-Tragwerk Diagramm">
      </div>
      <div>
        <div class="section-kicker">{ICONS["layers"]} Die 4 konstruktiven Ebenen</div>
        <h2 class="h2-section">Warum erst das Zusammenspiel zu planbaren Wunschprojekten führt</h2>
        <p class="lead-text" style="margin-bottom:1.5rem;">Viele Schreinereien haben bereits eine Webseite, aber sie bringt kaum qualifizierte Anfragen. Oder das Telefon klingelt ständig, aber für Aufträge, die gar nicht zum Maschinenpark passen. Unser Tragwerk schliesst genau diese Lücken:</p>

        <div style="display:flex;flex-direction:column;gap:1rem;">
          <div class="card" style="padding:1.25rem;">
            <h3 style="font-size:1.1rem;">Ebene 1: Das Fundament – Vertrauen auf den ersten Blick</h3>
            <p>Wenn ein Bauherr oder Architekt Ihre Webseite öffnet, erkennt er sofort Ihre Fachkompetenz, Ihre echten Referenzen und Ihre regionale Verankerung.</p>
          </div>
          <div class="card" style="padding:1.25rem;">
            <h3 style="font-size:1.1rem;">Ebene 2: Die Stützen – Regionale Auffindbarkeit bei Google</h3>
            <p>Über Ihr optimiertes Google-Geschäftsprofil und lokale Suchbegriffe stossen kaufbereite Kunden aus Ihrem Einzugsgebiet direkt auf Ihren Betrieb.</p>
          </div>
          <div class="card" style="padding:1.25rem;">
            <h3 style="font-size:1.1rem;">Ebene 3: Die Verbindung – Vorqualifizierung statt Telefon-Chaos</h3>
            <p>Das digitale Anfrage-System führt den Interessenten durch die wichtigsten Projektfragen. Sie rufen erst zurück, wenn Sie wissen, worum es geht.</p>
          </div>
          <div class="card" style="padding:1.25rem;">
            <h3 style="font-size:1.1rem;">Ebene 4: Die Aussteifung – Saubere Daten bis zur Offerte</h3>
            <p>Automatische Bestätigungen und strukturierte Kundenlisten sorgen dafür, dass kein Kontakt vergessen geht und Ihr Büro spürbar entlastet wird.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-header center">
      <div class="section-kicker">{ICONS["hammer"]} Praxis-Beispiele aus dem Holzhandwerk</div>
      <h2 class="h2-section">Wie das System in drei typischen Betriebs-Situationen wirkt</h2>
      <p class="lead-text">Ob spezialisierte Möbelschreinerei, Innenausbau-Spezialist oder Zimmerei/Holzbau, das Sichtbarkeits-Tragwerk passt sich Ihrer Werkstatt-Grösse an.</p>
    </div>

    <div class="grid-3">
      <div class="card">
        <span class="step-badge">Szenario A · 4 Mitarbeitende</span>
        <h3>Inhabergeführte Schreinerei (Möbel &amp; Innenausbau)</h3>
        <p><strong>Vorher:</strong> Der Inhaber steht selbst in der Werkstatt und an der Montage. Telefonanrufe reissen ihn ständig aus der Arbeit; abends im Büro fehlen oft Masse für die Offerte.</p>
        <p><strong>Mit dem Tragwerk:</strong> Kunden wählen online zwischen «Einbauschrank», «Massivholztisch» oder «Reparatur» und laden ein Foto hoch. Der Inhaber bearbeitet alle Anfragen gebündelt am Feierabend in der Hälfte der Zeit.</p>
      </div>
      <div class="card">
        <span class="step-badge">Szenario B · 8 Mitarbeitende</span>
        <h3>Küchen- &amp; Innenausbau-Betrieb im Mittelland</h3>
        <p><strong>Vorher:</strong> Gute Mundpropaganda, aber bei Google in den Nachbargemeinden kaum sichtbar. Hochwertige Küchen-Umbauten gehen oft an grosse Küchenstudios verloren.</p>
        <p><strong>Mit dem Tragwerk:</strong> Regionale Top-Platzierung bei Google inklusive über 35 echten Kundenbewertungen und einer modernen Referenz-Galerie. Monatlich 6 bis 9 vorqualifizierte Küchen- und Umbau-Anfragen aus der Region.</p>
      </div>
      <div class="card">
        <span class="step-badge">Szenario C · 14 Mitarbeitende</span>
        <h3>Holzbau, Fenster &amp; Sanierung</h3>
        <p><strong>Vorher:</strong> Viele Anfragen über verschiedene Kanäle (Telefon, info@-Mail, Privathandy). Im Sekretariat und in der AVOR entsteht Doppelarbeit beim Erfassen und Nachfassen.</p>
        <p><strong>Mit dem Tragwerk:</strong> Strukturierte Online-Erfassung getrennt nach «Sanierung/Umbau» und «Service/Reparatur» mit direkter Übergabe an den zuständigen Projektleiter.</p>
      </div>
    </div>
  </div>
</section>

{render_calculator_section()}

{render_smart_anfrage_section()}
"""


def build_ueber_uns_v1_body() -> str:
    return f"""
<section class="hero-section" style="padding:3.75rem 0;">
  <div class="container">
    <div class="hero-badges">
      <span class="hero-badge">{ICONS["award"]} Matthias Iseli · Schreiner EFZ</span>
      <span class="hero-badge">{ICONS["map_pin"]} Obersteckholz (Kanton Bern)</span>
    </div>
    <h1 class="h1-hero" style="max-width:22ch;">Vom Schreiner EFZ &amp; Geschäftsleiter zum Digital-Partner fürs Holzhandwerk</h1>
    <p class="lead-text" style="color:var(--text-light-muted);">Warum ich die IMP GmbH gegründet habe, und weshalb Sie bei uns niemals Marketing-Floskeln, sondern ehrliche Schweizer Handwerks-Qualität erhalten.</p>
  </div>
</section>

<section>
  <div class="container founder-grid">
    <div class="founder-photo-card">
      <img src="images/portrait-matthias-iseli.jpg" alt="Matthias Iseli – Inhaber IMP GmbH">
      <div class="founder-caption">
        <div>
          <strong style="display:block;font-family:var(--font-display);color:var(--text-main);font-size:1.05rem;">Matthias Iseli</strong>
          <span style="font-size:0.85rem;color:var(--text-muted);">Inhaber IMP GmbH · Schreiner EFZ</span>
        </div>
        <img src="images/icon-schreiner-efz.png" alt="Schreiner EFZ" style="width:46px;height:46px;object-fit:contain;">
      </div>
    </div>

    <div>
      <div class="section-kicker">{ICONS["hammer"]} Mein Hintergrund im Handwerk</div>
      <h2 class="h2-section">Über 15 Jahre gelebte Praxis zwischen Werkbank, CNC, AVOR und Geschäftsleitung</h2>
      <p class="lead-text" style="margin-bottom:1.15rem;">
        Mein beruflicher Weg begann mit der klassischen Lehre als <strong>Schreiner EFZ</strong>. In den darauffolgenden über 15 Jahren in Schreinerei und Holzbau durfte ich jede Station eines modernen Betriebs von Grund auf durchlaufen: von der Oberflächenbehandlung und dem Bankraum über die CNC-Bearbeitung und Arbeitsvorbereitung (AVOR) bis hin zur mehrjährigen Führungsverantwortung in der Geschäftsleitung.
      </p>
      <p class="lead-text" style="margin-bottom:1.15rem;">
        In dieser Zeit habe ich immer wieder erlebt, wie Standard-Werbeagenturen an der Realität von Handwerksbetrieben vorbeiarbeiten: Da werden komplizierte Kampagnen verkauft, die niemand im Betrieb pflegen kann, oder Texte geschrieben, bei denen jeder gelernte Schreiner sofort merkt, dass der Verfasser noch nie eine Werkstatt von innen gesehen hat.
      </p>
      <p class="lead-text" style="margin-bottom:1.5rem;">
        Genau deshalb habe ich in <strong>Obersteckholz (Oberaargau / Kanton Bern)</strong> die <strong>IMP GmbH</strong> aufgebaut: Wir übersetzen erstklassiges Handwerk in einen digitalen Auftritt, der Vertrauen schafft, regional gefunden wird und Ihnen im Büro den Rücken freihält.
      </p>

      <div class="grid-2" style="gap:1rem;">
        <div class="card" style="padding:1.25rem;">
          <h3 style="font-size:1.05rem;">Wir sprechen Ihre Fachsprache</h3>
          <p style="font-size:0.9rem;">Ob Massivholz, Elementbau, Haustür-Sanierung oder Küchen-AVOR: Ein kurzes Stichwort genügt, wir wissen sofort, worauf Ihre Kunden achten.</p>
        </div>
        <div class="card" style="padding:1.25rem;">
          <h3 style="font-size:1.05rem;">Pragmatisch &amp; bodenständig</h3>
          <p style="font-size:0.9rem;">Keine aufgeblasenen Konzepte, sondern klare Struktur, saubere Umsetzung und messbare Entlastung für Betriebe mit 1 bis 15 Mitarbeitenden.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="tragwerk-split">
      <div>
        <div class="section-kicker">{ICONS["shield"]} Unsere Grundwerte</div>
        <h2 class="h2-section">Wofür die IMP GmbH in jeder Zusammenarbeit einsteht</h2>
        <p class="lead-text" style="margin-bottom:1.5rem;">Gutes Handwerk beruht auf Verlässlichkeit, Präzision und Ehrlichkeit. Nach denselben Massstäben führen wir jedes Kundenprojekt:</p>

        <ul class="check-list">
          <li>{ICONS["check"]} <span><strong>Ehrliche Standortbestimmung:</strong> Wir empfehlen Ihnen nur Massnahmen, die für Ihre aktuelle Betriebsgrösse und Auslastung wirklich Sinn ergeben.</span></li>
          <li>{ICONS["check"]} <span><strong>Schlüsselfertige Umsetzung:</strong> Sie liefern uns Ihre Einblicke im Gespräch, wir übernehmen Struktur, Text, Design und Technik komplett für Sie.</span></li>
          <li>{ICONS["check"]} <span><strong>Persönlicher Ansprechpartner:</strong> Bei der IMP GmbH sprechen Sie direkt mit Matthias Iseli und nicht mit wechselnden Projektmanagern.</span></li>
          <li>{ICONS["check"]} <span><strong>Langfristige Partnerschaft:</strong> Auch nach dem Go-Live lassen wir Sie nicht allein, sondern begleiten Ihr Wachstum Schritt für Schritt.</span></li>
        </ul>
      </div>
      <div class="tragwerk-visual-box" style="padding:1rem;">
        <img src="images/werkstatt-handwerk.webp" alt="Schweizer Schreinerei-Handwerk und Präzision" style="border-radius:var(--radius-sm);object-fit:cover;max-height:420px;width:100%;">
      </div>
    </div>
  </div>
</section>

{render_smart_anfrage_section()}
"""


def build_kontakt_v1_body() -> str:
    return f"""
<section class="hero-section" style="padding:3.75rem 0;">
  <div class="container">
    <div class="hero-badges">
      <span class="hero-badge">{ICONS["map_pin"]} 4924 Obersteckholz (Kanton Bern)</span>
      <span class="hero-badge">{ICONS["phone"]} Direktkontakt zu Matthias Iseli</span>
    </div>
    <h1 class="h1-hero" style="max-width:22ch;">Kontakt, Erstgespräch &amp; Impressum</h1>
    <p class="lead-text" style="color:var(--text-light-muted);">Lassen Sie uns unkompliziert und auf Augenhöhe besprechen, wie wir Ihre Schreinerei oder Ihren Holzbau-Betrieb digital sichtbar machen und im Büro entlasten können.</p>
  </div>
</section>

{render_smart_anfrage_section()}

<section id="impressum">
  <div class="container">
    <div class="grid-2">
      <div class="card">
        <div class="section-kicker" style="align-self:flex-start;">{ICONS["map_pin"]} Impressum (Angaben gemäss Schweizer Recht)</div>
        <h3>IMP GmbH</h3>
        <p>
          <strong>Adresse:</strong><br>
          IMP GmbH<br>
          Herrengasse 81<br>
          4924 Obersteckholz<br>
          Schweiz
        </p>
        <p>
          <strong>Vertretungsberechtigte Person:</strong><br>
          Matthias Iseli (Inhaber &amp; Geschäftsführer)
        </p>
        <p>
          <strong>Kontakt:</strong><br>
          Telefon: <a href="tel:+41762276720" style="color:var(--oak-gold-dark);font-weight:600;">+41 76 227 67 20</a><br>
          E-Mail: <a href="mailto:kontakt@imp-marketing.ch" style="color:var(--oak-gold-dark);font-weight:600;">kontakt@imp-marketing.ch</a><br>
          Webseite: https://imp-marketing.ch/
        </p>
        <p>
          <strong>Unternehmens-Identifikationsnummer (UID):</strong><br>
          CHE-446.080.483 (Handelsregister des Kantons Bern)
        </p>
      </div>

      <div class="card" id="datenschutz">
        <div class="section-kicker" style="align-self:flex-start;">{ICONS["shield"]} Datenschutz &amp; Vertraulichkeit (CH-DSG)</div>
        <h3>Sorgfältiger Umgang mit Ihren Betriebs- und Kundendaten</h3>
        <p>
          Der Schutz Ihrer persönlichen Daten und Ihrer Betriebsinformationen ist uns ein zentrales Anliegen. Wir bearbeiten Personendaten streng nach den Vorgaben des schweizerischen Datenschutzgesetzes (revDSG).
        </p>
        <p>
          <strong>Zweck der Datenbearbeitung:</strong><br>
          Wenn Sie über unser Anfrage-System, per E-Mail oder telefonisch mit der IMP GmbH Kontakt aufnehmen, verwenden wir Ihre Angaben ausschliesslich zur Vorbereitung und Durchführung Ihrer Beratung sowie zur Erstellung einer individuellen Offerte.
        </p>
        <p>
          <strong>Keine Weitergabe an Dritte:</strong><br>
          Ihre Daten werden niemals an unbeteiligte Dritte verkauft oder zu fremden Werbezwecken weitergegeben. Auskunfts-, Berichtigungs- oder Löschungsbegehren richten Sie jederzeit direkt an <a href="mailto:kontakt@imp-marketing.ch" style="color:var(--oak-gold-dark);font-weight:600;">kontakt@imp-marketing.ch</a>.
        </p>
      </div>
    </div>
  </div>
</section>
"""


def build_v2_subpage_preview_body(page_title: str, page_kicker: str, summary_text: str, bullet_points: list, preview_img: str, include_impressum: bool = False) -> str:
    bullets_html = "".join(
        f'<li>{ICONS["check"]} <span>{b}</span></li>' for b in bullet_points
    )
    impressum_block = ""
    if include_impressum:
        impressum_block = """
        <div id="impressum" style="margin-top:2.5rem;" class="grid-2">
          <div class="card">
            <h3>Impressum – IMP GmbH</h3>
            <p>IMP GmbH · Matthias Iseli · Herrengasse 81, 4924 Obersteckholz, Schweiz</p>
            <p>UID: <strong>CHE-446.080.483</strong> · Tel. <a href="tel:+41762276720">+41 76 227 67 20</a> · E-Mail: <a href="mailto:kontakt@imp-marketing.ch">kontakt@imp-marketing.ch</a></p>
          </div>
          <div class="card" id="datenschutz">
            <h3>Datenschutz (Schweizer revDSG)</h3>
            <p>Alle übermittelten Angaben werden vertraulich behandelt und ausschliesslich für die persönliche Kontaktaufnahme durch Matthias Iseli (IMP GmbH) verwendet.</p>
          </div>
        </div>
        """

    return f"""
<section class="hero-section" style="padding:3.5rem 0;">
  <div class="container">
    <div class="hero-badges">
      <span class="hero-badge">{ICONS["layers"]} Vorschau-Entwurf (Ausbaustufe)</span>
      <span class="hero-badge">{ICONS["hammer"]} IMP GmbH · Matthias Iseli</span>
    </div>
    <h1 class="h1-hero">{page_title}</h1>
    <p class="lead-text" style="color:var(--text-light-muted);">{summary_text}</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="ausbau-banner">
      <div class="tragwerk-split">
        <div>
          <div class="section-kicker">{ICONS["compass"]} {page_kicker} · Konzept-Vorschau</div>
          <h2 class="h2-section" style="color:#ffffff;">Diese Unterseite ist als nächste Ausbaustufe für Ihren Auftritt vorbereitet</h2>
          <p class="lead-text" style="color:var(--text-light-muted);margin-bottom:1.25rem;">
            Auf der Startseite erleben Sie bereits das vollständige Design, den interaktiven Schreinerei-Potenzial-Rechner und die klare Struktur. Für diese Unterseite (<strong>{page_title}</strong>) haben wir die folgenden Inhalte und Prozess-Schritte bereits konzeptionell angelegt:
          </p>
          <ul class="check-list" style="margin-bottom:1.75rem;">
            {bullets_html}
          </ul>
          <div style="display:flex;flex-wrap:wrap;gap:0.85rem;">
            <button type="button" class="btn btn-primary" onclick="window.openImpAusbauDrawer('{page_title}')">
              Ausbau dieser Seite anfragen {ICONS["arrow_right"]}
            </button>
            <a href="index.html" class="btn btn-outline">Zurück zur voll ausgebauten Startseite</a>
          </div>
        </div>
        <div class="tragwerk-visual-box" style="background:#ffffff;">
          <img src="{preview_img}" alt="{page_title} – Vorschau IMP GmbH">
        </div>
      </div>
    </div>

    {impressum_block}
  </div>
</section>

{render_smart_anfrage_section()}
"""


# ---------------------------------------------------------
# 5. WRITE ALL HTML FILES FOR V1 AND V2
# ---------------------------------------------------------
v1_pages = {
    "index.html": render_page_shell(
        "IMP GmbH – Mehr Anfragen für Ihre Schreinerei ohne Marketing-Chaos | Matthias Iseli",
        "Spezialisiertes Digital- & Sichtbarkeits-System für Schreinereien und Holzbau-Betriebe (1–15 Mitarbeitende) in der Deutschschweiz. Von Schreiner EFZ Matthias Iseli, Obersteckholz.",
        "index.html",
        build_index_body(),
        is_v2=False
    ),
    "leistungen.html": render_page_shell(
        "Leistungen: Schreiner-Webseiten, Google-SEO, Anfrage-Systeme & Automation | IMP GmbH",
        "Unsere 4 Leistungsbereiche für Schreinereien und Holzbau-Betriebe: Moderne Webseiten, Google-Geschäftsprofil & Regionale SEO, Chat-Widgets & Datenautomation.",
        "leistungen.html",
        build_leistungen_v1_body(),
        is_v2=False
    ),
    "methode.html": render_page_shell(
        "Das IMP Sichtbarkeits-Tragwerk – Systematische Kundengewinnung im Holzhandwerk | IMP GmbH",
        "Wie das 4-stufige IMP Sichtbarkeits-Tragwerk für Schreinereien und Holzbau-Betriebe (1–15 Mitarbeitende) zu planbaren Wunschprojekten und weniger Büro-Aufwand führt.",
        "methode.html",
        build_methode_v1_body(),
        is_v2=False
    ),
    "ueber-uns.html": render_page_shell(
        "Über Matthias Iseli – Schreiner EFZ & Inhaber der IMP GmbH in Obersteckholz",
        "Lernen Sie Matthias Iseli kennen: Gelernter Schreiner EFZ mit über 15 Jahren Berufserfahrung in Schreinerei, CNC, AVOR und Geschäftsleitung.",
        "ueber-uns.html",
        build_ueber_uns_v1_body(),
        is_v2=False
    ),
    "kontakt.html": render_page_shell(
        "Kontakt, Erstgespräch & Impressum (CHE-446.080.483) | IMP GmbH Obersteckholz",
        "Vereinbaren Sie ein unverbindliches Erstgespräch mit Matthias Iseli (IMP GmbH, Herrengasse 81, 4924 Obersteckholz, +41 76 227 67 20).",
        "kontakt.html",
        build_kontakt_v1_body(),
        is_v2=False
    ),
}

for fname, html_content in v1_pages.items():
    (V1_DIR / fname).write_text(html_content, encoding="utf-8")

v2_pages = {
    "index.html": render_page_shell(
        "IMP GmbH – Mehr Anfragen für Ihre Schreinerei ohne Marketing-Chaos | Matthias Iseli",
        "Spezialisiertes Digital- & Sichtbarkeits-System für Schreinereien und Holzbau-Betriebe (1–15 Mitarbeitende) in der Deutschschweiz. Von Schreiner EFZ Matthias Iseli, Obersteckholz.",
        "index.html",
        build_index_body(),
        is_v2=True
    ),
    "leistungen.html": render_page_shell(
        "Leistungen (Vorschau-Entwurf) | IMP GmbH · Matthias Iseli",
        "Vorschau-Entwurf der 4 Leistungsbereiche der IMP GmbH: Schreiner-Webseiten, Google-Geschäftsprofil, Anfrage-Systeme und Datenautomation.",
        "leistungen.html",
        build_v2_subpage_preview_body(
            "Unsere 4 Leistungsbereiche im Detail",
            "Säulen 01 bis 04",
            "Hier entsteht die detaillierte Leistungsübersicht mit allen 16 Prozess-Schritten für Schreinereien und Holzbau-Betriebe.",
            [
                "Säule 1: Moderne Webseiten für Schreinereien & Holzbau (4-Schritte-Ablauf von Analyse bis Betreuung)",
                "Säule 2: Google-Geschäftsprofil & Regionale SEO (Standortanalyse, lokale Struktur, Bewertungsaufbau)",
                "Säule 3: Chat-Widgets & Anfrage-Systeme (Digitale Vorqualifizierung ohne Telefon-Unterbrechung)",
                "Säule 4: Datenautomation & Handwerks-Prozesse (Strukturierte Kundendaten vom Erstkontakt bis zur Offerte)"
            ],
            "images/service-webseiten.png",
            include_impressum=False
        ),
        is_v2=True
    ),
    "methode.html": render_page_shell(
        "Das IMP Sichtbarkeits-Tragwerk (Vorschau-Entwurf) | IMP GmbH",
        "Vorschau-Entwurf zur 4-Stufen-Methode «IMP Sichtbarkeits-Tragwerk» für Schreinereien und Holzbau-Betriebe.",
        "methode.html",
        build_v2_subpage_preview_body(
            "Das «IMP Sichtbarkeits-Tragwerk»",
            "Methode & Praxis",
            "Wie Fundament, Stützen, Verbindung und Aussteifung im digitalen Auftritt Ihrer Schreinerei zusammenwirken.",
            [
                "Konstruktiver Aufbau: Warum Einzelmassnahmen ohne Tragwerk im Handwerk verpuffen",
                "Praxis-Szenarien für Betriebe mit 1–5, 6–10 und 11–15 Mitarbeitenden",
                "Interaktiver Schreinerei-Potenzial-Rechner für Anfragen und eingesparte Büro-Stunden",
                "Direkte Anbindung an die unverbindliche Standortbestimmung mit Matthias Iseli"
            ],
            "images/sichtbarkeits-tragwerk.png",
            include_impressum=False
        ),
        is_v2=True
    ),
    "ueber-uns.html": render_page_shell(
        "Über Matthias Iseli – Schreiner EFZ (Vorschau-Entwurf) | IMP GmbH",
        "Vorschau-Entwurf: Matthias Iseli – Gelernter Schreiner EFZ mit über 15 Jahren Berufserfahrung und Inhaber der IMP GmbH in Obersteckholz.",
        "ueber-uns.html",
        build_v2_subpage_preview_body(
            "Über Matthias Iseli – Schreiner EFZ",
            "Aus dem Handwerk",
            "Vom Bankraum, der CNC-Fräse und der Geschäftsleitung zum spezialisierten Digital-Partner für Schreinereien und Holzbau.",
            [
                "Über 15 Jahre echte Berufserfahrung in Schreinerei und Holzbau (EFZ bis Geschäftsleitung)",
                "Warum wir die Fachsprache von Schreinern und Zimmerleuten ohne Erklärungsbedarf verstehen",
                "Unsere Werte: Handschlagqualität, Transparenz und pragmatische Entlastung im Alltag",
                "Regionale Verankerung an der Herrengasse 81 in 4924 Obersteckholz (Kanton Bern)"
            ],
            "images/portrait-matthias-iseli.jpg",
            include_impressum=False
        ),
        is_v2=True
    ),
    "kontakt.html": render_page_shell(
        "Kontakt & Impressum CHE-446.080.483 (Vorschau-Entwurf) | IMP GmbH",
        "Kontaktieren Sie Matthias Iseli (IMP GmbH, Herrengasse 81, 4924 Obersteckholz, +41 76 227 67 20, UID CHE-446.080.483).",
        "kontakt.html",
        build_v2_subpage_preview_body(
            "Kontakt, Erstgespräch & Impressum",
            "Direktkontakt Obersteckholz",
            "Starten Sie unten direkt Ihre 3-Schritte-Standortbestimmung oder fragen Sie den vollständigen Ausbau Ihrer Unterseiten an.",
            [
                "Direktkontakt zu Matthias Iseli (+41 76 227 67 20 · kontakt@imp-marketing.ch)",
                "Standort: Herrengasse 81, 4924 Obersteckholz (Oberaargau / Kanton Bern)",
                "Vollständiges Schweizer Impressum (UID: CHE-446.080.483) & Datenschutzerklärung nach revDSG",
                "Interaktive 3-Schritte Smart-Anfrage mit direkter E-Mail- und WhatsApp-Übergabe"
            ],
            "images/werkstatt-handwerk.webp",
            include_impressum=True
        ),
        is_v2=True
    ),
}

for fname, html_content in v2_pages.items():
    (V2_DIR / fname).write_text(html_content, encoding="utf-8")

print("Wrote all 5 HTML pages for V1 (preview-imp-marketing) and V2 (preview-imp-marketing-v2).")

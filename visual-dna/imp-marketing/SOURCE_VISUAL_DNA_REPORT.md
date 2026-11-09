# Source Visual DNA & Design-Sommelier Dossier: `imp-marketing`

- **Mandanten-Slug:** `imp-marketing`
- **Ursprungs-URL:** `file:///home/brainuser/workspaces/mxs-embed/preview-imp-marketing/index.html`
- **Design-Modus:** `redesign`
- **Branche / Kontext:** Schreinerei, Holzbau & Digital-Marketing
- **Gewaehlter Schweizer Meister-Archetyp:** **2. Swiss Architectural Craft (Handwerk, Solar, Schreinerei, Holzbau, Bau, Technik, Produktion)**
- **Vorher-Kamera-Beweise:** `visual-dna/imp-marketing/source_desktop.png` (`1440x900`) & `visual-dna/imp-marketing/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers – Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.609`**<br>• `hero_luminance`: **`0.068`**<br>• Kamera-Pixel oben/Hero: `0.277` / `0.15`<br>• Gemessene Flaechen: Body `#FAF8F5`, Hero `#191E24` | **Regel 1 (Polaritaets-Entscheid):**<br>Redesign-Modus gewaehlt: Startbuehne darf gezielt neu inszeniert werden (target_hero_polarity="dark"). | • **`target_hero_polarity: "dark"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`Dunkle Buehne erlaubt`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#FAF8F5`<br>• Primaer-Farbton `H = 70.8deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #FEF9F4` (`oklch(0.985 0.008 70.8)`)<br>• `--bg-soft: #F7EFE5` (`oklch(0.955 0.016 70.8)`)<br>• `--text-main: #1D1409` (Kontrast **`17.36:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 1`**<br>• Gefundene Akzent-Cluster: `#C88A36` (`L=0.681, C=0.124, H=70.8deg`, Gewicht 488) | **Regel 3 (60-30-10 Marken-Harmonie):**<br>Klare, fokussierte Marken-Farbwelt (1 Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt. | • **10 % Primaer-CTA (`--primary`):** `#A86B00` (Original: `#C88A36`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Plus Jakarta Sans`<br>• Body-Font: `Inter`<br>• Gemessene Radien: `0px, 4px, 8px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Plus Jakarta Sans / Inter) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`swiss_architectural_craft`** (Praezise 1100px Schweizer Fluchtlinien-Rasterung (#UI-02), messerscharfe 4px/8px Kanten, handwerkliche Substanz und klare Leistungs-Metriken.) | • `--font-display: 'Lexend', 'Plus Jakarta Sans', sans-serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`9`** (max. Breite: **`2000px`**)<br>• Hi-Res (`>=1100px`): `8` | Low-Res (`<900px`): `0`<br>• Hochformat-Anteil: `44 %` | **Regel 5 (Bild-Schutz-Regel):**<br>Hochaufloesendes Bildmaterial vorhanden (max. 2000px Breite). Sowohl "split_framed_card" (#UI-02) als auch architektonische Buehne ohne Verpixelung moeglich. | • **`recommended_hero_layout: "split_framed_card_or_architectural_stage"`**<br>• `forbid_fullscreen_bg_image: false`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>1. `hero_stage` (hero_stage) -> 2. `hero_stage` (Mehr passende Anfragen für Ihre Schreinerei, ohne Marketing) -> 3. `content_section` (Warum klassisches Marketing für Schreinereien oft ins Leere ) -> 4. `content_section` (Das «IMP Sichtbarkeits-Tragwerk»: Gebaut wie ein sauberer Ho) -> 5. `content_section` (Alle Bausteine für Ihren digitalen Vorsprung im Holzhandwerk) -> 6. `content_section` (Sichtbarkeits- & Anfrage-Potenzial für Ihren Betrieb berechn) -> 7. `content_section` («Ich weiss aus eigener Erfahrung, wie der Alltag in einer Sc) -> 8. `faq_accordion` (Klare Antworten für Schreinereien & Holzbau-Betriebe) -> 9. `content_section` (Prüfen wir gemeinsam, wo Ihr Betrieb digital am meisten Hebe) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#C88A36` (`H=70.8deg`) | `#F7EFE5` (`oklch(0.955 0.016 70.8)`) | **`#A86B00`** (`oklch(0.580 0.160 70.8)`) |
| Slot 1 (`--accent-palette-1`) | `#8E8215` (`H=102.8deg`) | `#F2F0D5` (`oklch(0.950 0.035 102.8)`) | `#695F00` (`oklch(0.480 0.130 102.8)`) |
| Slot 2 (`--accent-palette-2`) | `#609042` (`H=134.8deg`) | `#E5F4DD` (`oklch(0.950 0.035 134.8)`) | `#3B6D11` (`oklch(0.480 0.130 134.8)`) |
| Slot 3 (`--accent-palette-3`) | `#119671` (`H=166.8deg`) | `#D9F7E9` (`oklch(0.950 0.035 166.8)`) | `#006F51` (`oklch(0.480 0.130 166.8)`) |
| Slot 4 (`--accent-palette-4`) | `#009297` (`H=198.8deg`) | `#D4F6F7` (`oklch(0.950 0.035 198.8)`) | `#006B6F` (`oklch(0.480 0.130 198.8)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_imp_marketing_site.py`

```css
/* Google Fonts Import fuer Archetyp "swiss_architectural_craft":
   @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
*/
:root {
  /* === 1. Polaritaet & Schweizer Raster (#UI-02, #UI-16, Sensor S-27) === */
  --wp-expected-hero-polarity: "dark";
  --wp-archetype: "swiss_architectural_craft";
  --container-max: 1100px;
  --radius-card: 8px;
  --radius-badge: 4px;

  /* === 2. Typografie (swiss_architectural_craft) === */
  --font-display: 'Lexend', 'Plus Jakarta Sans', sans-serif;
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=70.8deg) === */
  --bg-page: #FEF9F4;
  --bg-page-oklch: oklch(0.985 0.008 70.8);
  --bg-soft: #F7EFE5;
  --bg-soft-oklch: oklch(0.955 0.016 70.8);
  --bg-elevated: #FFFFFF;
  --border-subtle: #E1D9D1;
  --border-subtle-oklch: oklch(0.890 0.014 70.8);
  --text-main: #1D1409;
  --text-main-oklch: oklch(0.200 0.025 70.8);
  --text-muted: #544B41;
  --text-muted-oklch: oklch(0.420 0.020 70.8);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #A86B00;
  --primary-brand-raw: #C88A36;
  --primary-oklch: oklch(0.580 0.160 70.8);
  --primary-hover: #895700;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #F2F0D5; /* oklch(0.950 0.035 102.8) */
  --accent-palette-1-strong: #695F00; /* oklch(0.480 0.130 102.8) */
  --accent-palette-2-soft: #E5F4DD; /* oklch(0.950 0.035 134.8) */
  --accent-palette-2-strong: #3B6D11; /* oklch(0.480 0.130 134.8) */
  --accent-palette-3-soft: #D9F7E9; /* oklch(0.950 0.035 166.8) */
  --accent-palette-3-strong: #006F51; /* oklch(0.480 0.130 166.8) */
  --accent-palette-4-soft: #D4F6F7; /* oklch(0.950 0.035 198.8) */
  --accent-palette-4-strong: #006B6F; /* oklch(0.480 0.130 198.8) */
}
```

# Source Visual DNA & Design-Sommelier Dossier: `get-more-sales`

- **Mandanten-Slug:** `get-more-sales`
- **Ursprungs-URL:** `https://get-more-sales.org/`
- **Design-Modus:** `evolution`
- **Branche / Kontext:** B2B Verkaufsberatung, Vertriebstraining & Akquise-Sparring
- **Gewaehlter Schweizer Meister-Archetyp:** **2. Swiss Architectural Craft (Handwerk, Solar, Schreinerei, Holzbau, Bau, Technik, Produktion)**
- **Vorher-Kamera-Beweise:** `visual-dna/get-more-sales/source_desktop.png` (`1440x900`) & `visual-dna/get-more-sales/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers – Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.647`**<br>• `hero_luminance`: **`0.123`**<br>• Kamera-Pixel oben/Hero: `0.034` / `0.196`<br>• Gemessene Flaechen: Body `#FFFFFF`, Hero `#FFFFFF` | **Regel 1 (Polaritaets-Entscheid):**<br>Ursprungs-Startbuehne war nachweislich dunkel gestaltet (hero_luminance=0.123 < 0.42). Dunkler/kontrastreicher Hero ist im Evolution-Modus erlaubt. | • **`target_hero_polarity: "dark"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`Dunkle Buehne erlaubt`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#FFFFFF`<br>• Primaer-Farbton `H = 253.9deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #F7FAFF` (`oklch(0.985 0.008 253.9)`)<br>• `--bg-soft: #E9F1FB` (`oklch(0.955 0.016 253.9)`)<br>• `--text-main: #0E1721` (Kontrast **`17.25:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 2`**<br>• Gefundene Akzent-Cluster: `#003366` (`L=0.323, C=0.103, H=253.9deg`, Gewicht 121), `#F0D0B0` (`L=0.877, C=0.056, H=67deg`, Gewicht 69) | **Regel 3 (60-30-10 Marken-Harmonie):**<br>Klare, fokussierte Marken-Farbwelt (2 Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt. | • **10 % Primaer-CTA (`--primary`):** `#0B68C1` (Original: `#003366`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Roboto`<br>• Body-Font: `-apple-system`<br>• Gemessene Radien: `0px, 5px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Roboto / -apple-system) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`swiss_architectural_craft`** (Praezise 1100px Schweizer Fluchtlinien-Rasterung (#UI-02), messerscharfe 4px/8px Kanten, handwerkliche Substanz und klare Leistungs-Metriken.) | • `--font-display: 'Lexend', 'Plus Jakarta Sans', sans-serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`5`** (max. Breite: **`1120px`**)<br>• Hi-Res (`>=1100px`): `1` | Low-Res (`<900px`): `4`<br>• Hochformat-Anteil: `0 %` | **Regel 5 (Bild-Schutz-Regel):**<br>Hochaufloesendes Bildmaterial vorhanden (max. 1120px Breite). Sowohl "split_framed_card" (#UI-02) als auch architektonische Buehne ohne Verpixelung moeglich. | • **`recommended_hero_layout: "split_framed_card_or_architectural_stage"`**<br>• `forbid_fullscreen_bg_image: false`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>Standard-Sektionsabfolge (Hero -> Angebot -> Ueber uns -> Kontakt) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#003366` (`H=253.9deg`) | `#E9F1FB` (`oklch(0.955 0.016 253.9)`) | **`#0B68C1`** (`oklch(0.520 0.160 253.9)`) |
| Slot 1 (`--accent-palette-1`) | `#F0D0B0` (`H=67deg`) | `#FFEBD6` (`oklch(0.950 0.035 67.0)`) | `#854F00` (`oklch(0.480 0.130 67.0)`) |
| Slot 2 (`--accent-palette-2`) | `#9E68AE` (`H=317.9deg`) | `#F9E8FE` (`oklch(0.950 0.035 317.9)`) | `#7B428C` (`oklch(0.480 0.130 317.9)`) |
| Slot 3 (`--accent-palette-3`) | `#B4608A` (`H=349.9deg`) | `#FFE7F1` (`oklch(0.950 0.035 349.9)`) | `#913968` (`oklch(0.480 0.130 349.9)`) |
| Slot 4 (`--accent-palette-4`) | `#BD605F` (`H=21.9deg`) | `#FFE8E7` (`oklch(0.950 0.035 21.9)`) | `#99393B` (`oklch(0.480 0.130 21.9)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_get_more_sales_site.py`

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

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=253.9deg) === */
  --bg-page: #F7FAFF;
  --bg-page-oklch: oklch(0.985 0.008 253.9);
  --bg-soft: #E9F1FB;
  --bg-soft-oklch: oklch(0.955 0.016 253.9);
  --bg-elevated: #FFFFFF;
  --border-subtle: #D5DBE4;
  --border-subtle-oklch: oklch(0.890 0.014 253.9);
  --text-main: #0E1721;
  --text-main-oklch: oklch(0.200 0.025 253.9);
  --text-muted: #464E58;
  --text-muted-oklch: oklch(0.420 0.020 253.9);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #0B68C1;
  --primary-brand-raw: #003366;
  --primary-oklch: oklch(0.520 0.160 253.9);
  --primary-hover: #0054A2;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #FFEBD6; /* oklch(0.950 0.035 67.0) */
  --accent-palette-1-strong: #854F00; /* oklch(0.480 0.130 67.0) */
  --accent-palette-2-soft: #F9E8FE; /* oklch(0.950 0.035 317.9) */
  --accent-palette-2-strong: #7B428C; /* oklch(0.480 0.130 317.9) */
  --accent-palette-3-soft: #FFE7F1; /* oklch(0.950 0.035 349.9) */
  --accent-palette-3-strong: #913968; /* oklch(0.480 0.130 349.9) */
  --accent-palette-4-soft: #FFE8E7; /* oklch(0.950 0.035 21.9) */
  --accent-palette-4-strong: #99393B; /* oklch(0.480 0.130 21.9) */
}
```

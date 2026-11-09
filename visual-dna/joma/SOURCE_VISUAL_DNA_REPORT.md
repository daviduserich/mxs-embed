# Source Visual DNA & Design-Sommelier Dossier: `joma`

- **Mandanten-Slug:** `joma`
- **Ursprungs-URL:** `https://www.joma-solar.ch/`
- **Design-Modus:** `evolution`
- **Branche / Kontext:** Solaranlagen, Photovoltaik, Batteriespeicher & Energietechnik
- **Gewaehlter Schweizer Meister-Archetyp:** **2. Swiss Architectural Craft (Handwerk, Solar, Schreinerei, Holzbau, Bau, Technik, Produktion)**
- **Vorher-Kamera-Beweise:** `visual-dna/joma/source_desktop.png` (`1440x900`) & `visual-dna/joma/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers – Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.599`**<br>• `hero_luminance`: **`0.094`**<br>• Kamera-Pixel oben/Hero: `0.029` / `0.148`<br>• Gemessene Flaechen: Body `#FFFFFF`, Hero `#FFFFFF` | **Regel 1 (Polaritaets-Entscheid):**<br>Ursprungs-Startbuehne war nachweislich dunkel gestaltet (hero_luminance=0.094 < 0.42). Dunkler/kontrastreicher Hero ist im Evolution-Modus erlaubt. | • **`target_hero_polarity: "dark"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`Dunkle Buehne erlaubt`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#FFFFFF`<br>• Primaer-Farbton `H = 37deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #FFF8F7` (`oklch(0.985 0.008 37.0)`)<br>• `--bg-soft: #FBEDE9` (`oklch(0.955 0.016 37.0)`)<br>• `--text-main: #20120E` (Kontrast **`17.35:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 2`**<br>• Gefundene Akzent-Cluster: `#FF4D00` (`L=0.668, C=0.224, H=37deg`, Gewicht 250), `#405020` (`L=0.406, C=0.074, H=125deg`, Gewicht 35) | **Regel 3 (60-30-10 Marken-Harmonie):**<br>Klare, fokussierte Marken-Farbwelt (2 Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt. | • **10 % Primaer-CTA (`--primary`):** `#D43E00` (Original: `#FF4D00`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Lexend`<br>• Body-Font: `Instrument Sans`<br>• Gemessene Radien: `0px, 12px, 16px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Lexend / Instrument Sans) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`swiss_architectural_craft`** (Praezise 1100px Schweizer Fluchtlinien-Rasterung (#UI-02), messerscharfe 4px/8px Kanten, handwerkliche Substanz und klare Leistungs-Metriken.) | • `--font-display: 'Lexend', 'Plus Jakarta Sans', sans-serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`13`** (max. Breite: **`1066px`**)<br>• Hi-Res (`>=1100px`): `0` | Low-Res (`<900px`): `12`<br>• Hochformat-Anteil: `23 %` | **Regel 5 (Bild-Schutz-Regel):**<br>Hochaufloesendes Bildmaterial vorhanden (max. 1066px Breite). Sowohl "split_framed_card" (#UI-02) als auch architektonische Buehne ohne Verpixelung moeglich. | • **`recommended_hero_layout: "split_framed_card_or_architectural_stage"`**<br>• `forbid_fullscreen_bg_image: false`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>1. `hero_stage` (Solareinfacheffizient) -> 2. `content_section` (Ihr Projekt.Unser Prozess.) -> 3. `content_section` (Durchdachte Energielösungen) -> 4. `content_section` (Partner) -> 5. `contact_or_cta` (Kontaktieren Sie uns.) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#FF4D00` (`H=37deg`) | `#FBEDE9` (`oklch(0.955 0.016 37.0)`) | **`#D43E00`** (`oklch(0.580 0.200 37.0)`) |
| Slot 1 (`--accent-palette-1`) | `#405020` (`H=125deg`) | `#E9F3DA` (`oklch(0.950 0.035 125.0)`) | `#4E6800` (`oklch(0.480 0.130 125.0)`) |
| Slot 2 (`--accent-palette-2`) | `#908113` (`H=101deg`) | `#F3F0D5` (`oklch(0.950 0.035 101.0)`) | `#6A5E00` (`oklch(0.480 0.130 101.0)`) |
| Slot 3 (`--accent-palette-3`) | `#638F40` (`H=133deg`) | `#E6F4DC` (`oklch(0.950 0.035 133.0)`) | `#3E6C0B` (`oklch(0.480 0.130 133.0)`) |
| Slot 4 (`--accent-palette-4`) | `#19966E` (`H=165deg`) | `#DAF6E9` (`oklch(0.950 0.035 165.0)`) | `#006F4F` (`oklch(0.480 0.130 165.0)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_joma_site.py`

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

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=37deg) === */
  --bg-page: #FFF8F7;
  --bg-page-oklch: oklch(0.985 0.008 37.0);
  --bg-soft: #FBEDE9;
  --bg-soft-oklch: oklch(0.955 0.016 37.0);
  --bg-elevated: #FFFFFF;
  --border-subtle: #E4D8D4;
  --border-subtle-oklch: oklch(0.890 0.014 37.0);
  --text-main: #20120E;
  --text-main-oklch: oklch(0.200 0.025 37.0);
  --text-muted: #574945;
  --text-muted-oklch: oklch(0.420 0.020 37.0);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #D43E00;
  --primary-brand-raw: #FF4D00;
  --primary-oklch: oklch(0.580 0.200 37.0);
  --primary-hover: #AE3100;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #E9F3DA; /* oklch(0.950 0.035 125.0) */
  --accent-palette-1-strong: #4E6800; /* oklch(0.480 0.130 125.0) */
  --accent-palette-2-soft: #F3F0D5; /* oklch(0.950 0.035 101.0) */
  --accent-palette-2-strong: #6A5E00; /* oklch(0.480 0.130 101.0) */
  --accent-palette-3-soft: #E6F4DC; /* oklch(0.950 0.035 133.0) */
  --accent-palette-3-strong: #3E6C0B; /* oklch(0.480 0.130 133.0) */
  --accent-palette-4-soft: #DAF6E9; /* oklch(0.950 0.035 165.0) */
  --accent-palette-4-strong: #006F4F; /* oklch(0.480 0.130 165.0) */
}
```

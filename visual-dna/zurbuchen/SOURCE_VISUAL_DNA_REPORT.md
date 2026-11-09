# Source Visual DNA & Design-Sommelier Dossier: `zurbuchen`

- **Mandanten-Slug:** `zurbuchen`
- **Ursprungs-URL:** `https://www.zurbuchen-holzbau.ch`
- **Design-Modus:** `evolution`
- **Branche / Kontext:** Holzbau & Zimmerei
- **Gewaehlter Schweizer Meister-Archetyp:** **2. Swiss Architectural Craft (Handwerk, Solar, Schreinerei, Holzbau, Bau, Technik, Produktion)**
- **Vorher-Kamera-Beweise:** `visual-dna/zurbuchen/source_desktop.png` (`1440x900`) & `visual-dna/zurbuchen/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers – Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.597`**<br>• `hero_luminance`: **`0.213`**<br>• Kamera-Pixel oben/Hero: `0.194` / `0.228`<br>• Gemessene Flaechen: Body `#FFFFFF`, Hero `#FFFFFF` | **Regel 1 (Polaritaets-Entscheid):**<br>Ursprungs-Startbuehne war nachweislich dunkel gestaltet (hero_luminance=0.213 < 0.42). Dunkler/kontrastreicher Hero ist im Evolution-Modus erlaubt. | • **`target_hero_polarity: "dark"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`Dunkle Buehne erlaubt`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#FFFFFF`<br>• Primaer-Farbton `H = 60deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #FEF9F5` (`oklch(0.985 0.008 60.0)`)<br>• `--bg-soft: #F9EEE6` (`oklch(0.955 0.016 60.0)`)<br>• `--text-main: #1E130A` (Kontrast **`17.43:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 2`**<br>• Gefundene Akzent-Cluster: `#BC9B81` (`L=0.713, C=0.054, H=60deg`, Gewicht 184), `#405070` (`L=0.432, C=0.057, H=263.7deg`, Gewicht 160) | **Regel 3 (60-30-10 Marken-Harmonie):**<br>Klare, fokussierte Marken-Farbwelt (2 Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt. | • **10 % Primaer-CTA (`--primary`):** `#B36300` (Original: `#BC9B81`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Open Sans`<br>• Body-Font: `Open Sans`<br>• Gemessene Radien: `0px, 2px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Open Sans / Open Sans) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`swiss_architectural_craft`** (Praezise 1100px Schweizer Fluchtlinien-Rasterung (#UI-02), messerscharfe 4px/8px Kanten, handwerkliche Substanz und klare Leistungs-Metriken.) | • `--font-display: 'Lexend', 'Plus Jakarta Sans', sans-serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`9`** (max. Breite: **`476px`**)<br>• Hi-Res (`>=1100px`): `0` | Low-Res (`<900px`): `9`<br>• Hochformat-Anteil: `0 %` | **Regel 5 (Bild-Schutz-Regel):**<br>BILD-SCHUTZ-SPERRE AKTIV: Maximale Originalbild-Breite (476px < 1000px) bzw. Hochformat-Anteil (0 %). Unscharfe Fullscreen-Hintergrundbilder sind verboten -> zwingend "split_framed_card" (links Typografie + Kennzahlen, rechts eingerahmte Bild-Karte mit Unterkanten-Buendigkeit #UI-02) bauen! | • **`recommended_hero_layout: "split_framed_card"`**<br>• `forbid_fullscreen_bg_image: true`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>Standard-Sektionsabfolge (Hero -> Angebot -> Ueber uns -> Kontakt) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#BC9B81` (`H=60deg`) | `#F9EEE6` (`oklch(0.955 0.016 60.0)`) | **`#B36300`** (`oklch(0.580 0.160 60.0)`) |
| Slot 1 (`--accent-palette-1`) | `#405070` (`H=263.7deg`) | `#E6EFFF` (`oklch(0.950 0.035 263.7)`) | `#3659A6` (`oklch(0.480 0.130 263.7)`) |
| Slot 2 (`--accent-palette-2`) | `#718C33` (`H=124deg`) | `#E9F3DA` (`oklch(0.950 0.035 124.0)`) | `#506800` (`oklch(0.480 0.130 124.0)`) |
| Slot 3 (`--accent-palette-3`) | `#359561` (`H=156deg`) | `#DDF6E5` (`oklch(0.950 0.035 156.0)`) | `#007040` (`oklch(0.480 0.130 156.0)`) |
| Slot 4 (`--accent-palette-4`) | `#00948C` (`H=188deg`) | `#D5F7F3` (`oklch(0.950 0.035 188.0)`) | `#006C66` (`oklch(0.480 0.130 188.0)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_zurbuchen_site.py`

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

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=60deg) === */
  --bg-page: #FEF9F5;
  --bg-page-oklch: oklch(0.985 0.008 60.0);
  --bg-soft: #F9EEE6;
  --bg-soft-oklch: oklch(0.955 0.016 60.0);
  --bg-elevated: #FFFFFF;
  --border-subtle: #E2D9D2;
  --border-subtle-oklch: oklch(0.890 0.014 60.0);
  --text-main: #1E130A;
  --text-main-oklch: oklch(0.200 0.025 60.0);
  --text-muted: #564B42;
  --text-muted-oklch: oklch(0.420 0.020 60.0);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #B36300;
  --primary-brand-raw: #BC9B81;
  --primary-oklch: oklch(0.580 0.160 60.0);
  --primary-hover: #935000;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #E6EFFF; /* oklch(0.950 0.035 263.7) */
  --accent-palette-1-strong: #3659A6; /* oklch(0.480 0.130 263.7) */
  --accent-palette-2-soft: #E9F3DA; /* oklch(0.950 0.035 124.0) */
  --accent-palette-2-strong: #506800; /* oklch(0.480 0.130 124.0) */
  --accent-palette-3-soft: #DDF6E5; /* oklch(0.950 0.035 156.0) */
  --accent-palette-3-strong: #007040; /* oklch(0.480 0.130 156.0) */
  --accent-palette-4-soft: #D5F7F3; /* oklch(0.950 0.035 188.0) */
  --accent-palette-4-strong: #006C66; /* oklch(0.480 0.130 188.0) */
}
```

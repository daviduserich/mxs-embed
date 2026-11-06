# Source Visual DNA & Design-Sommelier Dossier: `hochuli`

- **Mandanten-Slug:** `hochuli`
- **Ursprungs-URL:** `https://www.hochuli-gruppe.ch`
- **Design-Modus:** `evolution`
- **Branche / Kontext:** Holzbau, Zimmerei, Elementbau & Bedachungen
- **Gewaehlter Schweizer Meister-Archetyp:** **2. Swiss Architectural Craft (Handwerk, Solar, Schreinerei, Holzbau, Bau, Technik, Produktion)**
- **Vorher-Kamera-Beweise:** `visual-dna/hochuli/source_desktop.png` (`1440x900`) & `visual-dna/hochuli/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers — Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.579`**<br>• `hero_luminance`: **`0.619`**<br>• Kamera-Pixel oben/Hero: `0.831` / `0.446`<br>• Gemessene Flaechen: Body `#9C9C8C`, Hero `#FFFFFF` | **Regel 1 (Polaritaets-Entscheid):**<br>Evolution-Schutzregel (#UI-16): Mittlere Hero-Helligkeit (0.619) bei hellem Grundkoerper (0.579) -> Licht-Sperre target_hero_polarity="light" aktiv. | • **`target_hero_polarity: "light"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`>= 0.45 Pflicht!`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#9C9C8C`<br>• Primaer-Farbton `H = 51.3deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #FFF9F5` (`oklch(0.985 0.008 51.3)`)<br>• `--bg-soft: #FAEDE7` (`oklch(0.955 0.016 51.3)`)<br>• `--text-main: #1F130B` (Kontrast **`17.4:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 1`**<br>• Gefundene Akzent-Cluster: `#B85D19` (`L=0.578, C=0.139, H=51.3deg`, Gewicht 100) | **Regel 3 (60-30-10 Marken-Harmonie):**<br>Klare, fokussierte Marken-Farbwelt (1 Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt. | • **10 % Primaer-CTA (`--primary`):** `#BD5A00` (Original: `#B85D19`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Hind`<br>• Body-Font: `Open Sans`<br>• Gemessene Radien: `0px, 3px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Hind / Open Sans) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`swiss_architectural_craft`** (Praezise 1100px Schweizer Fluchtlinien-Rasterung (#UI-02), messerscharfe 4px/8px Kanten, handwerkliche Substanz und klare Leistungs-Metriken.) | • `--font-display: 'Lexend', 'Plus Jakarta Sans', sans-serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`7`** (max. Breite: **`3745px`**)<br>• Hi-Res (`>=1100px`): `1` | Low-Res (`<900px`): `2`<br>• Hochformat-Anteil: `57 %` | **Regel 5 (Bild-Schutz-Regel):**<br>BILD-SCHUTZ-SPERRE AKTIV: Maximale Originalbild-Breite (3745px < 1000px) bzw. Hochformat-Anteil (57 %). Unscharfe Fullscreen-Hintergrundbilder sind verboten -> zwingend "split_framed_card" (links Typografie + Kennzahlen, rechts eingerahmte Bild-Karte mit Unterkanten-Buendigkeit #UI-02) bauen! | • **`recommended_hero_layout: "split_framed_card"`**<br>• `forbid_fullscreen_bg_image: true`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>1. `hero_stage` (hero_stage) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#B85D19` (`H=51.3deg`) | `#FAEDE7` (`oklch(0.955 0.016 51.3)`) | **`#BD5A00`** (`oklch(0.578 0.160 51.3)`) |
| Slot 1 (`--accent-palette-1`) | `#A2780D` (`H=83.3deg`) | `#FAEDD5` (`oklch(0.950 0.035 83.3)`) | `#785700` (`oklch(0.480 0.130 83.3)`) |
| Slot 2 (`--accent-palette-2`) | `#7E8826` (`H=115.3deg`) | `#EDF2D7` (`oklch(0.950 0.035 115.3)`) | `#5C6400` (`oklch(0.480 0.130 115.3)`) |
| Slot 3 (`--accent-palette-3`) | `#499355` (`H=147.3deg`) | `#E0F5E1` (`oklch(0.950 0.035 147.3)`) | `#17702E` (`oklch(0.480 0.130 147.3)`) |
| Slot 4 (`--accent-palette-4`) | `#009582` (`H=179.3deg`) | `#D7F7EF` (`oklch(0.950 0.035 179.3)`) | `#006D5F` (`oklch(0.480 0.130 179.3)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_hochuli_site.py`

```css
/* Google Fonts Import fuer Archetyp "swiss_architectural_craft":
   @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
*/
:root {
  /* === 1. Polaritaet & Schweizer Raster (#UI-02, #UI-16, Sensor S-27) === */
  --wp-expected-hero-polarity: "light";
  --wp-archetype: "swiss_architectural_craft";
  --container-max: 1100px;
  --radius-card: 8px;
  --radius-badge: 4px;

  /* === 2. Typografie (swiss_architectural_craft) === */
  --font-display: 'Lexend', 'Plus Jakarta Sans', sans-serif;
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=51.3deg) === */
  --bg-page: #FFF9F5;
  --bg-page-oklch: oklch(0.985 0.008 51.3);
  --bg-soft: #FAEDE7;
  --bg-soft-oklch: oklch(0.955 0.016 51.3);
  --bg-elevated: #FFFFFF;
  --border-subtle: #E3D8D3;
  --border-subtle-oklch: oklch(0.890 0.014 51.3);
  --text-main: #1F130B;
  --text-main-oklch: oklch(0.200 0.025 51.3);
  --text-muted: #564A43;
  --text-muted-oklch: oklch(0.420 0.020 51.3);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #BD5A00;
  --primary-brand-raw: #B85D19;
  --primary-oklch: oklch(0.578 0.160 51.3);
  --primary-hover: #9B4800;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #FAEDD5; /* oklch(0.950 0.035 83.3) */
  --accent-palette-1-strong: #785700; /* oklch(0.480 0.130 83.3) */
  --accent-palette-2-soft: #EDF2D7; /* oklch(0.950 0.035 115.3) */
  --accent-palette-2-strong: #5C6400; /* oklch(0.480 0.130 115.3) */
  --accent-palette-3-soft: #E0F5E1; /* oklch(0.950 0.035 147.3) */
  --accent-palette-3-strong: #17702E; /* oklch(0.480 0.130 147.3) */
  --accent-palette-4-soft: #D7F7EF; /* oklch(0.950 0.035 179.3) */
  --accent-palette-4-strong: #006D5F; /* oklch(0.480 0.130 179.3) */
}
```

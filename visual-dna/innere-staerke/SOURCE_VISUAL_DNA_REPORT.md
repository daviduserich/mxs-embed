# Source Visual DNA & Design-Sommelier Dossier: `innere-staerke`

- **Mandanten-Slug:** `innere-staerke`
- **Ursprungs-URL:** `https://www.innere-staerke.business`
- **Design-Modus:** `evolution`
- **Branche / Kontext:** Executive Coaching, Fuehrungsentwicklung & Mentaltraining
- **Gewaehlter Schweizer Meister-Archetyp:** **3. Executive Authority (Beratung, Fuehrung, Executive Coaching, Treuhand, IT, Recht)**
- **Vorher-Kamera-Beweise:** `visual-dna/innere-staerke/source_desktop.png` (`1440x900`) & `visual-dna/innere-staerke/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers — Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.92`**<br>• `hero_luminance`: **`0.767`**<br>• Kamera-Pixel oben/Hero: `0.84` / `0.708`<br>• Gemessene Flaechen: Body `#FFFFFF`, Hero `#FFFFFF` | **Regel 1 (Polaritaets-Entscheid):**<br>LICHT-SPERRE AKTIV (#UI-16): Ursprungsseite ist im Gesamteindruck (body_luminance=0.92) und Hero (hero_luminance=0.767) hell/freundlich. Dunkle Startbuehnen sind strikt verboten (Sensor S-27 ueberwacht >= 0.45)! | • **`target_hero_polarity: "light"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`>= 0.45 Pflicht!`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#FFFFFF`<br>• Primaer-Farbton `H = 77deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #FDFAF4` (`oklch(0.985 0.008 77.0)`)<br>• `--bg-soft: #F6EFE5` (`oklch(0.955 0.016 77.0)`)<br>• `--text-main: #1C1509` (Kontrast **`17.38:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 2`**<br>• Gefundene Akzent-Cluster: `#F9B231` (`L=0.811, C=0.156, H=77deg`, Gewicht 671), `#5070C0` (`L=0.559, C=0.13, H=265.9deg`, Gewicht 160) | **Regel 3 (60-30-10 Marken-Harmonie):**<br>Klare, fokussierte Marken-Farbwelt (2 Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt. | • **10 % Primaer-CTA (`--primary`):** `#A26F00` (Original: `#F9B231`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Barlow`<br>• Body-Font: `Barlow`<br>• Gemessene Radien: `0px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Barlow / Barlow) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`executive_authority`** (Edles Warm-Alabaster (#F8F6F2), souveraene Typografie, ruhige Entscheidungs-Architektur fuer Geschaeftsleitung und Verwaltungsrat.) | • `--font-display: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`1`** (max. Breite: **`1440px`**)<br>• Hi-Res (`>=1100px`): `1` | Low-Res (`<900px`): `0`<br>• Hochformat-Anteil: `0 %` | **Regel 5 (Bild-Schutz-Regel):**<br>Hochaufloesendes Bildmaterial vorhanden (max. 1440px Breite). Sowohl "split_framed_card" (#UI-02) als auch architektonische Buehne ohne Verpixelung moeglich. | • **`recommended_hero_layout: "split_framed_card_or_architectural_stage"`**<br>• `forbid_fullscreen_bg_image: false`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>Standard-Sektionsabfolge (Hero -> Angebot -> Ueber uns -> Kontakt) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#F9B231` (`H=77deg`) | `#F6EFE5` (`oklch(0.955 0.016 77.0)`) | **`#A26F00`** (`oklch(0.580 0.160 77.0)`) |
| Slot 1 (`--accent-palette-1`) | `#5070C0` (`H=265.9deg`) | `#E7EFFF` (`oklch(0.950 0.035 265.9)`) | `#3A58A6` (`oklch(0.480 0.130 265.9)`) |
| Slot 2 (`--accent-palette-2`) | `#55924B` (`H=141deg`) | `#E2F5DF` (`oklch(0.950 0.035 141.0)`) | `#2C6F21` (`oklch(0.480 0.130 141.0)`) |
| Slot 3 (`--accent-palette-3`) | `#00967A` (`H=173deg`) | `#D8F7EC` (`oklch(0.950 0.035 173.0)`) | `#006E59` (`oklch(0.480 0.130 173.0)`) |
| Slot 4 (`--accent-palette-4`) | `#00919D` (`H=205deg`) | `#D4F6FA` (`oklch(0.950 0.035 205.0)`) | `#006B74` (`oklch(0.480 0.130 205.0)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_innere_staerke_site.py`

```css
/* Google Fonts Import fuer Archetyp "executive_authority":
   @import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,600;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
*/
:root {
  /* === 1. Polaritaet & Schweizer Raster (#UI-02, #UI-16, Sensor S-27) === */
  --wp-expected-hero-polarity: "light";
  --wp-archetype: "executive_authority";
  --container-max: 1100px;
  --radius-card: 8px;
  --radius-badge: 4px;

  /* === 2. Typografie (executive_authority) === */
  --font-display: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=77deg) === */
  --bg-page: #FDFAF4;
  --bg-page-oklch: oklch(0.985 0.008 77.0);
  --bg-soft: #F6EFE5;
  --bg-soft-oklch: oklch(0.955 0.016 77.0);
  --bg-elevated: #FFFFFF;
  --border-subtle: #E0DAD1;
  --border-subtle-oklch: oklch(0.890 0.014 77.0);
  --text-main: #1C1509;
  --text-main-oklch: oklch(0.200 0.025 77.0);
  --text-muted: #534C41;
  --text-muted-oklch: oklch(0.420 0.020 77.0);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #A26F00;
  --primary-brand-raw: #F9B231;
  --primary-oklch: oklch(0.580 0.160 77.0);
  --primary-hover: #845A00;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #E7EFFF; /* oklch(0.950 0.035 265.9) */
  --accent-palette-1-strong: #3A58A6; /* oklch(0.480 0.130 265.9) */
  --accent-palette-2-soft: #E2F5DF; /* oklch(0.950 0.035 141.0) */
  --accent-palette-2-strong: #2C6F21; /* oklch(0.480 0.130 141.0) */
  --accent-palette-3-soft: #D8F7EC; /* oklch(0.950 0.035 173.0) */
  --accent-palette-3-strong: #006E59; /* oklch(0.480 0.130 173.0) */
  --accent-palette-4-soft: #D4F6FA; /* oklch(0.950 0.035 205.0) */
  --accent-palette-4-strong: #006B74; /* oklch(0.480 0.130 205.0) */
}
```

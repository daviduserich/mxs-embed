# Source Visual DNA & Design-Sommelier Dossier: `frees`

- **Mandanten-Slug:** `frees`
- **Ursprungs-URL:** `https://www.frees.ch`
- **Design-Modus:** `evolution`
- **Branche / Kontext:** Textildruck, Stickerei, Arbeitskleidung & Teamsport
- **Gewaehlter Schweizer Meister-Archetyp:** **2. Swiss Architectural Craft (Handwerk, Solar, Schreinerei, Holzbau, Bau, Technik, Produktion)**
- **Vorher-Kamera-Beweise:** `visual-dna/frees/source_desktop.png` (`1440x900`) & `visual-dna/frees/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers – Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.99`**<br>• `hero_luminance`: **`0.596`**<br>• Kamera-Pixel oben/Hero: `0.979` / `0.283`<br>• Gemessene Flaechen: Body `#FFFFFF`, Hero `#FFFFFF` | **Regel 1 (Polaritaets-Entscheid):**<br>LICHT-SPERRE AKTIV (#UI-16): Ursprungsseite ist im Gesamteindruck (body_luminance=0.99) und Hero (hero_luminance=0.596) hell/freundlich. Dunkle Startbuehnen sind strikt verboten (Sensor S-27 ueberwacht >= 0.45)! | • **`target_hero_polarity: "light"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`>= 0.45 Pflicht!`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#FFFFFF`<br>• Primaer-Farbton `H = 23.8deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #FFF8F8` (`oklch(0.985 0.008 23.8)`)<br>• `--bg-soft: #FBECEB` (`oklch(0.955 0.016 23.8)`)<br>• `--text-main: #201110` (Kontrast **`17.42:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 1`**<br>• Gefundene Akzent-Cluster: `#D02030` (`L=0.553, C=0.207, H=23.8deg`, Gewicht 170) | **Regel 3 (60-30-10 Marken-Harmonie):**<br>Klare, fokussierte Marken-Farbwelt (1 Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt. | • **10 % Primaer-CTA (`--primary`):** `#CD2733` (Original: `#D02030`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `oswald-extralight`<br>• Body-Font: `Arial`<br>• Gemessene Radien: `0px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Alte System-/Fallback-Schrift erkannt (oswald-extralight / Arial) -> wird als handwerklicher Alt-Baufehler geheilt.<br>• Archetyp: **`swiss_architectural_craft`** (Praezise 1100px Schweizer Fluchtlinien-Rasterung (#UI-02), messerscharfe 4px/8px Kanten, handwerkliche Substanz und klare Leistungs-Metriken.) | • `--font-display: 'Lexend', 'Plus Jakarta Sans', sans-serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`2`** (max. Breite: **`940px`**)<br>• Hi-Res (`>=1100px`): `0` | Low-Res (`<900px`): `1`<br>• Hochformat-Anteil: `0 %` | **Regel 5 (Bild-Schutz-Regel):**<br>BILD-SCHUTZ-SPERRE AKTIV: Maximale Originalbild-Breite (940px < 1000px) bzw. Hochformat-Anteil (0 %). Unscharfe Fullscreen-Hintergrundbilder sind verboten -> zwingend "split_framed_card" (links Typografie + Kennzahlen, rechts eingerahmte Bild-Karte mit Unterkanten-Buendigkeit #UI-02) bauen! | • **`recommended_hero_layout: "split_framed_card"`**<br>• `forbid_fullscreen_bg_image: true`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>Standard-Sektionsabfolge (Hero -> Angebot -> Ueber uns -> Kontakt) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#D02030` (`H=23.8deg`) | `#FBECEB` (`oklch(0.955 0.016 23.8)`) | **`#CD2733`** (`oklch(0.553 0.200 23.8)`) |
| Slot 1 (`--accent-palette-1`) | `#B66B30` (`H=55.8deg`) | `#FFEADC` (`oklch(0.950 0.035 55.8)`) | `#8E4800` (`oklch(0.480 0.130 55.8)`) |
| Slot 2 (`--accent-palette-2`) | `#9E7B0B` (`H=87.8deg`) | `#F8EED5` (`oklch(0.950 0.035 87.8)`) | `#755900` (`oklch(0.480 0.130 87.8)`) |
| Slot 3 (`--accent-palette-3`) | `#788A2C` (`H=119.8deg`) | `#EBF2D8` (`oklch(0.950 0.035 119.8)`) | `#566600` (`oklch(0.480 0.130 119.8)`) |
| Slot 4 (`--accent-palette-4`) | `#3F945B` (`H=151.8deg`) | `#DEF6E3` (`oklch(0.950 0.035 151.8)`) | `#007136` (`oklch(0.480 0.130 151.8)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_frees_site.py`

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

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=23.8deg) === */
  --bg-page: #FFF8F8;
  --bg-page-oklch: oklch(0.985 0.008 23.8);
  --bg-soft: #FBECEB;
  --bg-soft-oklch: oklch(0.955 0.016 23.8);
  --bg-elevated: #FFFFFF;
  --border-subtle: #E4D7D6;
  --border-subtle-oklch: oklch(0.890 0.014 23.8);
  --text-main: #201110;
  --text-main-oklch: oklch(0.200 0.025 23.8);
  --text-muted: #584948;
  --text-muted-oklch: oklch(0.420 0.020 23.8);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #CD2733;
  --primary-brand-raw: #D02030;
  --primary-oklch: oklch(0.553 0.200 23.8);
  --primary-hover: #B30020;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #FFEADC; /* oklch(0.950 0.035 55.8) */
  --accent-palette-1-strong: #8E4800; /* oklch(0.480 0.130 55.8) */
  --accent-palette-2-soft: #F8EED5; /* oklch(0.950 0.035 87.8) */
  --accent-palette-2-strong: #755900; /* oklch(0.480 0.130 87.8) */
  --accent-palette-3-soft: #EBF2D8; /* oklch(0.950 0.035 119.8) */
  --accent-palette-3-strong: #566600; /* oklch(0.480 0.130 119.8) */
  --accent-palette-4-soft: #DEF6E3; /* oklch(0.950 0.035 151.8) */
  --accent-palette-4-strong: #007136; /* oklch(0.480 0.130 151.8) */
}
```

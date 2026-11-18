# Source Visual DNA & Design-Sommelier Dossier: `seit`

- **Mandanten-Slug:** `seit`
- **Ursprungs-URL:** `https://clean-equipe.ch/`
- **Design-Modus:** `evolution`
- **Branche / Kontext:** Aus Seiteninhalt ermittelt
- **Gewaehlter Schweizer Meister-Archetyp:** **2. Swiss Architectural Craft (Handwerk, Solar, Schreinerei, Holzbau, Bau, Technik, Produktion)**
- **Vorher-Kamera-Beweise:** `visual-dna/seit/source_desktop.png` (`1440x900`) & `visual-dna/seit/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers – Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.705`**<br>• `hero_luminance`: **`0.232`**<br>• Kamera-Pixel oben/Hero: `0.094` / `0.344`<br>• Gemessene Flaechen: Body `#FFFFFF`, Hero `#FFFFFF` | **Regel 1 (Polaritaets-Entscheid):**<br>Ursprungs-Startbuehne war nachweislich dunkel gestaltet (hero_luminance=0.232 < 0.42). Dunkler/kontrastreicher Hero ist im Evolution-Modus erlaubt. | • **`target_hero_polarity: "dark"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`Dunkle Buehne erlaubt`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#FFFFFF`<br>• Primaer-Farbton `H = 229.2deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #F5FBFE` (`oklch(0.985 0.008 229.2)`)<br>• `--bg-soft: #E6F2F9` (`oklch(0.955 0.016 229.2)`)<br>• `--text-main: #09181F` (Kontrast **`17.31:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 2`**<br>• Gefundene Akzent-Cluster: `#52BCE9` (`L=0.751, C=0.116, H=229.2deg`, Gewicht 233), `#4EAC3A` (`L=0.663, C=0.176, H=140.4deg`, Gewicht 40) | **Regel 3 (60-30-10 Marken-Harmonie):**<br>Klare, fokussierte Marken-Farbwelt (2 Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt. | • **10 % Primaer-CTA (`--primary`):** `#0086B0` (Original: `#52BCE9`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Quicksand`<br>• Body-Font: `Montserrat`<br>• Gemessene Radien: `0px, 15px, 50px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Quicksand / Montserrat) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`swiss_architectural_craft`** (Praezise 1100px Schweizer Fluchtlinien-Rasterung (#UI-02), messerscharfe 4px/8px Kanten, handwerkliche Substanz und klare Leistungs-Metriken.) | • `--font-display: 'Lexend', 'Plus Jakarta Sans', sans-serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`3`** (max. Breite: **`1080px`**)<br>• Hi-Res (`>=1100px`): `0` | Low-Res (`<900px`): `2`<br>• Hochformat-Anteil: `33 %` | **Regel 5 (Bild-Schutz-Regel):**<br>Hochaufloesendes Bildmaterial vorhanden (max. 1080px Breite). Sowohl "split_framed_card" (#UI-02) als auch architektonische Buehne ohne Verpixelung moeglich. | • **`recommended_hero_layout: "split_framed_card_or_architectural_stage"`**<br>• `forbid_fullscreen_bg_image: false`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>Standard-Sektionsabfolge (Hero -> Angebot -> Ueber uns -> Kontakt) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#52BCE9` (`H=229.2deg`) | `#E6F2F9` (`oklch(0.955 0.016 229.2)`) | **`#0086B0`** (`oklch(0.580 0.160 229.2)`) |
| Slot 1 (`--accent-palette-1`) | `#4EAC3A` (`H=140.4deg`) | `#E2F5DF` (`oklch(0.950 0.035 140.4)`) | `#2E6E20` (`oklch(0.480 0.130 140.4)`) |
| Slot 2 (`--accent-palette-2`) | `#8471C1` (`H=293.2deg`) | `#EFECFF` (`oklch(0.950 0.035 293.2)`) | `#624C9F` (`oklch(0.480 0.130 293.2)`) |
| Slot 3 (`--accent-palette-3`) | `#A465A7` (`H=325.2deg`) | `#FBE7FC` (`oklch(0.950 0.035 325.2)`) | `#813F85` (`oklch(0.480 0.130 325.2)`) |
| Slot 4 (`--accent-palette-4`) | `#B85F81` (`H=357.2deg`) | `#FFE7EF` (`oklch(0.950 0.035 357.2)`) | `#94385E` (`oklch(0.480 0.130 357.2)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_seit_site.py`

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

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=229.2deg) === */
  --bg-page: #F5FBFE;
  --bg-page-oklch: oklch(0.985 0.008 229.2);
  --bg-soft: #E6F2F9;
  --bg-soft-oklch: oklch(0.955 0.016 229.2);
  --bg-elevated: #FFFFFF;
  --border-subtle: #D2DDE2;
  --border-subtle-oklch: oklch(0.890 0.014 229.2);
  --text-main: #09181F;
  --text-main-oklch: oklch(0.200 0.025 229.2);
  --text-muted: #424F56;
  --text-muted-oklch: oklch(0.420 0.020 229.2);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #0086B0;
  --primary-brand-raw: #52BCE9;
  --primary-oklch: oklch(0.580 0.160 229.2);
  --primary-hover: #006D90;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #E2F5DF; /* oklch(0.950 0.035 140.4) */
  --accent-palette-1-strong: #2E6E20; /* oklch(0.480 0.130 140.4) */
  --accent-palette-2-soft: #EFECFF; /* oklch(0.950 0.035 293.2) */
  --accent-palette-2-strong: #624C9F; /* oklch(0.480 0.130 293.2) */
  --accent-palette-3-soft: #FBE7FC; /* oklch(0.950 0.035 325.2) */
  --accent-palette-3-strong: #813F85; /* oklch(0.480 0.130 325.2) */
  --accent-palette-4-soft: #FFE7EF; /* oklch(0.950 0.035 357.2) */
  --accent-palette-4-strong: #94385E; /* oklch(0.480 0.130 357.2) */
}
```

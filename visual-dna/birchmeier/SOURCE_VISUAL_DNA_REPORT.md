# Source Visual DNA & Design-Sommelier Dossier: `birchmeier`

- **Mandanten-Slug:** `birchmeier`
- **Ursprungs-URL:** `https://birchmeier-hohler.ch`
- **Design-Modus:** `evolution`
- **Branche / Kontext:** Sanitaer, Heizung, Haustechnik & Badumbau
- **Gewaehlter Schweizer Meister-Archetyp:** **2. Swiss Architectural Craft (Handwerk, Solar, Schreinerei, Holzbau, Bau, Technik, Produktion)**
- **Vorher-Kamera-Beweise:** `visual-dna/birchmeier/source_desktop.png` (`1440x900`) & `visual-dna/birchmeier/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers – Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.077`**<br>• `hero_luminance`: **`0.143`**<br>• Kamera-Pixel oben/Hero: `0.021` / `0.242`<br>• Gemessene Flaechen: Body `#000000`, Hero `#000000` | **Regel 1 (Polaritaets-Entscheid):**<br>Ursprungs-Startbuehne war nachweislich dunkel gestaltet (hero_luminance=0.143 < 0.42). Dunkler/kontrastreicher Hero ist im Evolution-Modus erlaubt. | • **`target_hero_polarity: "dark"`**<br>• **`target_page_polarity: "dark"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`Dunkle Buehne erlaubt`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#000000`<br>• Primaer-Farbton `H = 138.7deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #F7FBF6` (`oklch(0.985 0.008 138.7)`)<br>• `--bg-soft: #EBF3E9` (`oklch(0.955 0.016 138.7)`)<br>• `--text-main: #10190E` (Kontrast **`17.2:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 2`**<br>• Gefundene Akzent-Cluster: `#70D050` (`L=0.772, C=0.189, H=138.7deg`, Gewicht 240), `#337AB7` (`L=0.564, C=0.118, H=247.7deg`, Gewicht 10) | **Regel 3 (60-30-10 Marken-Harmonie):**<br>Klare, fokussierte Marken-Farbwelt (2 Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt. | • **10 % Primaer-CTA (`--primary`):** `#359200` (Original: `#70D050`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Roboto`<br>• Body-Font: `Roboto`<br>• Gemessene Radien: `0px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Roboto / Roboto) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`swiss_architectural_craft`** (Praezise 1100px Schweizer Fluchtlinien-Rasterung (#UI-02), messerscharfe 4px/8px Kanten, handwerkliche Substanz und klare Leistungs-Metriken.) | • `--font-display: 'Lexend', 'Plus Jakarta Sans', sans-serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`5`** (max. Breite: **`300px`**)<br>• Hi-Res (`>=1100px`): `0` | Low-Res (`<900px`): `5`<br>• Hochformat-Anteil: `0 %` | **Regel 5 (Bild-Schutz-Regel):**<br>BILD-SCHUTZ-SPERRE AKTIV: Maximale Originalbild-Breite (300px < 1000px) bzw. Hochformat-Anteil (0 %). Unscharfe Fullscreen-Hintergrundbilder sind verboten -> zwingend "split_framed_card" (links Typografie + Kennzahlen, rechts eingerahmte Bild-Karte mit Unterkanten-Buendigkeit #UI-02) bauen! | • **`recommended_hero_layout: "split_framed_card"`**<br>• `forbid_fullscreen_bg_image: true`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>Standard-Sektionsabfolge (Hero -> Angebot -> Ueber uns -> Kontakt) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#70D050` (`H=138.7deg`) | `#EBF3E9` (`oklch(0.955 0.016 138.7)`) | **`#359200`** (`oklch(0.580 0.189 138.7)`) |
| Slot 1 (`--accent-palette-1`) | `#337AB7` (`H=247.7deg`) | `#E2F1FF` (`oklch(0.950 0.035 247.7)`) | `#0061A2` (`oklch(0.480 0.130 247.7)`) |
| Slot 2 (`--accent-palette-2`) | `#00929B` (`H=202.7deg`) | `#D4F6F9` (`oklch(0.950 0.035 202.7)`) | `#006B72` (`oklch(0.480 0.130 202.7)`) |
| Slot 3 (`--accent-palette-3`) | `#1A8ABD` (`H=234.7deg`) | `#DDF2FF` (`oklch(0.950 0.035 234.7)`) | `#00668E` (`oklch(0.480 0.130 234.7)`) |
| Slot 4 (`--accent-palette-4`) | `#5F7DC8` (`H=266.7deg`) | `#E7EFFF` (`oklch(0.950 0.035 266.7)`) | `#3C58A6` (`oklch(0.480 0.130 266.7)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_birchmeier_site.py`

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

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=138.7deg) === */
  --bg-page: #F7FBF6;
  --bg-page-oklch: oklch(0.985 0.008 138.7);
  --bg-soft: #EBF3E9;
  --bg-soft-oklch: oklch(0.955 0.016 138.7);
  --bg-elevated: #FFFFFF;
  --border-subtle: #D6DDD4;
  --border-subtle-oklch: oklch(0.890 0.014 138.7);
  --text-main: #10190E;
  --text-main-oklch: oklch(0.200 0.025 138.7);
  --text-muted: #485045;
  --text-muted-oklch: oklch(0.420 0.020 138.7);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #359200;
  --primary-brand-raw: #70D050;
  --primary-oklch: oklch(0.580 0.189 138.7);
  --primary-hover: #297700;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #E2F1FF; /* oklch(0.950 0.035 247.7) */
  --accent-palette-1-strong: #0061A2; /* oklch(0.480 0.130 247.7) */
  --accent-palette-2-soft: #D4F6F9; /* oklch(0.950 0.035 202.7) */
  --accent-palette-2-strong: #006B72; /* oklch(0.480 0.130 202.7) */
  --accent-palette-3-soft: #DDF2FF; /* oklch(0.950 0.035 234.7) */
  --accent-palette-3-strong: #00668E; /* oklch(0.480 0.130 234.7) */
  --accent-palette-4-soft: #E7EFFF; /* oklch(0.950 0.035 266.7) */
  --accent-palette-4-strong: #3C58A6; /* oklch(0.480 0.130 266.7) */
}
```

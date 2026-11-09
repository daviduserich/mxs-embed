# Source Visual DNA & Design-Sommelier Dossier: `hiltbrand`

- **Mandanten-Slug:** `hiltbrand`
- **Ursprungs-URL:** `https://hiltbrand.swiss`
- **Design-Modus:** `evolution`
- **Branche / Kontext:** Gebaeudehuellen, Dachdecker, Fassadenbau & Solar
- **Gewaehlter Schweizer Meister-Archetyp:** **2. Swiss Architectural Craft (Handwerk, Solar, Schreinerei, Holzbau, Bau, Technik, Produktion)**
- **Vorher-Kamera-Beweise:** `visual-dna/hiltbrand/source_desktop.png` (`1440x900`) & `visual-dna/hiltbrand/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers – Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.995`**<br>• `hero_luminance`: **`0.638`**<br>• Kamera-Pixel oben/Hero: `0.99` / `0.35`<br>• Gemessene Flaechen: Body `#FFFFFF`, Hero `#FFFFFF` | **Regel 1 (Polaritaets-Entscheid):**<br>LICHT-SPERRE AKTIV (#UI-16): Ursprungsseite ist im Gesamteindruck (body_luminance=0.995) und Hero (hero_luminance=0.638) hell/freundlich. Dunkle Startbuehnen sind strikt verboten (Sensor S-27 ueberwacht >= 0.45)! | • **`target_hero_polarity: "light"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`>= 0.45 Pflicht!`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#FFFFFF`<br>• Primaer-Farbton `H = 241.1deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #F6FBFF` (`oklch(0.985 0.008 241.1)`)<br>• `--bg-soft: #E7F2FA` (`oklch(0.955 0.016 241.1)`)<br>• `--text-main: #0B1720` (Kontrast **`17.41:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 2`**<br>• Gefundene Akzent-Cluster: `#205070` (`L=0.414, C=0.074, H=241.1deg`, Gewicht 120), `#EF4035` (`L=0.631, C=0.213, H=28.4deg`, Gewicht 45) | **Regel 3 (60-30-10 Marken-Harmonie):**<br>Klare, fokussierte Marken-Farbwelt (2 Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt. | • **10 % Primaer-CTA (`--primary`):** `#0070A8` (Original: `#205070`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Exo`<br>• Body-Font: `Exo`<br>• Gemessene Radien: `0px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Exo / Exo) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`swiss_architectural_craft`** (Praezise 1100px Schweizer Fluchtlinien-Rasterung (#UI-02), messerscharfe 4px/8px Kanten, handwerkliche Substanz und klare Leistungs-Metriken.) | • `--font-display: 'Lexend', 'Plus Jakarta Sans', sans-serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`12`** (max. Breite: **`1920px`**)<br>• Hi-Res (`>=1100px`): `1` | Low-Res (`<900px`): `11`<br>• Hochformat-Anteil: `0 %` | **Regel 5 (Bild-Schutz-Regel):**<br>Hochaufloesendes Bildmaterial vorhanden (max. 1920px Breite). Sowohl "split_framed_card" (#UI-02) als auch architektonische Buehne ohne Verpixelung moeglich. | • **`recommended_hero_layout: "split_framed_card_or_architectural_stage"`**<br>• `forbid_fullscreen_bg_image: false`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>Standard-Sektionsabfolge (Hero -> Angebot -> Ueber uns -> Kontakt) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#205070` (`H=241.1deg`) | `#E7F2FA` (`oklch(0.955 0.016 241.1)`) | **`#0070A8`** (`oklch(0.520 0.160 241.1)`) |
| Slot 1 (`--accent-palette-1`) | `#EF4035` (`H=28.4deg`) | `#FFE9E5` (`oklch(0.950 0.035 28.4)`) | `#993A31` (`oklch(0.480 0.130 28.4)`) |
| Slot 2 (`--accent-palette-2`) | `#916CB9` (`H=305.1deg`) | `#F3EAFF` (`oklch(0.950 0.035 305.1)`) | `#6F4797` (`oklch(0.480 0.130 305.1)`) |
| Slot 3 (`--accent-palette-3`) | `#AD629A` (`H=337.1deg`) | `#FFE6F7` (`oklch(0.950 0.035 337.1)`) | `#8A3C78` (`oklch(0.480 0.130 337.1)`) |
| Slot 4 (`--accent-palette-4`) | `#BC5F71` (`H=9.1deg`) | `#FFE8EB` (`oklch(0.950 0.035 9.1)`) | `#98374E` (`oklch(0.480 0.130 9.1)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_hiltbrand_site.py`

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

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=241.1deg) === */
  --bg-page: #F6FBFF;
  --bg-page-oklch: oklch(0.985 0.008 241.1);
  --bg-soft: #E7F2FA;
  --bg-soft-oklch: oklch(0.955 0.016 241.1);
  --bg-elevated: #FFFFFF;
  --border-subtle: #D3DCE3;
  --border-subtle-oklch: oklch(0.890 0.014 241.1);
  --text-main: #0B1720;
  --text-main-oklch: oklch(0.200 0.025 241.1);
  --text-muted: #444F57;
  --text-muted-oklch: oklch(0.420 0.020 241.1);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #0070A8;
  --primary-brand-raw: #205070;
  --primary-oklch: oklch(0.520 0.160 241.1);
  --primary-hover: #005B8A;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #FFE9E5; /* oklch(0.950 0.035 28.4) */
  --accent-palette-1-strong: #993A31; /* oklch(0.480 0.130 28.4) */
  --accent-palette-2-soft: #F3EAFF; /* oklch(0.950 0.035 305.1) */
  --accent-palette-2-strong: #6F4797; /* oklch(0.480 0.130 305.1) */
  --accent-palette-3-soft: #FFE6F7; /* oklch(0.950 0.035 337.1) */
  --accent-palette-3-strong: #8A3C78; /* oklch(0.480 0.130 337.1) */
  --accent-palette-4-soft: #FFE8EB; /* oklch(0.950 0.035 9.1) */
  --accent-palette-4-strong: #98374E; /* oklch(0.480 0.130 9.1) */
}
```

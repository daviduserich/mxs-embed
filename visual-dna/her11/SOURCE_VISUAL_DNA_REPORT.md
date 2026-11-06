# Source Visual DNA & Design-Sommelier Dossier: `her11`

- **Mandanten-Slug:** `her11`
- **Ursprungs-URL:** `https://www.her11.ch`
- **Design-Modus:** `redesign`
- **Branche / Kontext:** Sportfoerderung, Berufsbildung & Karrierebegleitung im Frauenfussball
- **Gewaehlter Schweizer Meister-Archetyp:** **4. Dynamic Club & Community Spirit (Vereine, Verbaende, Teamsport, Sportfoerderung)**
- **Vorher-Kamera-Beweise:** `visual-dna/her11/source_desktop.png` (`1440x900`) & `visual-dna/her11/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers — Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.95`**<br>• `hero_luminance`: **`0.703`**<br>• Kamera-Pixel oben/Hero: `0.9` / `0.541`<br>• Gemessene Flaechen: Body `#FFFFFF`, Hero `#FFFFFF` | **Regel 1 (Polaritaets-Entscheid):**<br>Redesign-Modus gewaehlt: Startbuehne darf gezielt neu inszeniert werden (target_hero_polarity="dark"). | • **`target_hero_polarity: "dark"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`Dunkle Buehne erlaubt`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#FFFFFF`<br>• Primaer-Farbton `H = 307.4deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #FBF9FE` (`oklch(0.985 0.008 307.4)`)<br>• `--bg-soft: #F3EDF9` (`oklch(0.955 0.016 307.4)`)<br>• `--text-main: #19131F` (Kontrast **`17.4:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 1`**<br>• Gefundene Akzent-Cluster: `#9373B1` (`L=0.61, C=0.098, H=307.4deg`, Gewicht 341) | **Regel 3 (60-30-10 Marken-Harmonie):**<br>Klare, fokussierte Marken-Farbwelt (1 Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt. | • **10 % Primaer-CTA (`--primary`):** `#945CC3` (Original: `#9373B1`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Montserrat`<br>• Body-Font: `Montserrat`<br>• Gemessene Radien: `0px, 22px, 30px, 40px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Montserrat / Montserrat) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`dynamic_club_spirit`** (Stolze Vereinsfarben im 60-30-10-Raster, emotionale Vereins-Identitaet kombiniert mit aufgeraeumter Kader-, Spielplan- und Sponsoren-Struktur.) | • `--font-display: 'Montserrat', 'Plus Jakarta Sans', sans-serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`3`** (max. Breite: **`1024px`**)<br>• Hi-Res (`>=1100px`): `0` | Low-Res (`<900px`): `2`<br>• Hochformat-Anteil: `0 %` | **Regel 5 (Bild-Schutz-Regel):**<br>Hochaufloesendes Bildmaterial vorhanden (max. 1024px Breite). Sowohl "split_framed_card" (#UI-02) als auch architektonische Buehne ohne Verpixelung moeglich. | • **`recommended_hero_layout: "split_framed_card_or_architectural_stage"`**<br>• `forbid_fullscreen_bg_image: false`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>1. `hero_stage` (hero_stage) -> 2. `content_section` (content_section) -> 3. `content_section` (content_section) -> 4. `content_section` (content_section) -> 5. `content_section` (content_section) -> 6. `content_section` (content_section) -> 7. `content_section` (content_section) -> 8. `content_section` (content_section) -> 9. `content_section` (Je&Mi) -> 10. `content_section` (content_section) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#9373B1` (`H=307.4deg`) | `#F3EDF9` (`oklch(0.955 0.016 307.4)`) | **`#945CC3`** (`oklch(0.580 0.160 307.4)`) |
| Slot 1 (`--accent-palette-1`) | `#AE6297` (`H=339.4deg`) | `#FFE6F6` (`oklch(0.950 0.035 339.4)`) | `#8B3B75` (`oklch(0.480 0.130 339.4)`) |
| Slot 2 (`--accent-palette-2`) | `#BC5F6E` (`H=11.4deg`) | `#FFE8EA` (`oklch(0.950 0.035 11.4)`) | `#98374B` (`oklch(0.480 0.130 11.4)`) |
| Slot 3 (`--accent-palette-3`) | `#BB6641` (`H=43.4deg`) | `#FFE9E0` (`oklch(0.950 0.035 43.4)`) | `#973F12` (`oklch(0.480 0.130 43.4)`) |
| Slot 4 (`--accent-palette-4`) | `#A97415` (`H=75.4deg`) | `#FDECD5` (`oklch(0.950 0.035 75.4)`) | `#7E5400` (`oklch(0.480 0.130 75.4)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_her11_site.py`

```css
/* Google Fonts Import fuer Archetyp "dynamic_club_spirit":
   @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
*/
:root {
  /* === 1. Polaritaet & Schweizer Raster (#UI-02, #UI-16, Sensor S-27) === */
  --wp-expected-hero-polarity: "dark";
  --wp-archetype: "dynamic_club_spirit";
  --container-max: 1100px;
  --radius-card: 8px;
  --radius-badge: 4px;

  /* === 2. Typografie (dynamic_club_spirit) === */
  --font-display: 'Montserrat', 'Plus Jakarta Sans', sans-serif;
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=307.4deg) === */
  --bg-page: #FBF9FE;
  --bg-page-oklch: oklch(0.985 0.008 307.4);
  --bg-soft: #F3EDF9;
  --bg-soft-oklch: oklch(0.955 0.016 307.4);
  --bg-elevated: #FFFFFF;
  --border-subtle: #DDD8E2;
  --border-subtle-oklch: oklch(0.890 0.014 307.4);
  --text-main: #19131F;
  --text-main-oklch: oklch(0.200 0.025 307.4);
  --text-muted: #504A56;
  --text-muted-oklch: oklch(0.420 0.020 307.4);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #945CC3;
  --primary-brand-raw: #9373B1;
  --primary-oklch: oklch(0.580 0.160 307.4);
  --primary-hover: #7C43A8;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #FFE6F6; /* oklch(0.950 0.035 339.4) */
  --accent-palette-1-strong: #8B3B75; /* oklch(0.480 0.130 339.4) */
  --accent-palette-2-soft: #FFE8EA; /* oklch(0.950 0.035 11.4) */
  --accent-palette-2-strong: #98374B; /* oklch(0.480 0.130 11.4) */
  --accent-palette-3-soft: #FFE9E0; /* oklch(0.950 0.035 43.4) */
  --accent-palette-3-strong: #973F12; /* oklch(0.480 0.130 43.4) */
  --accent-palette-4-soft: #FDECD5; /* oklch(0.950 0.035 75.4) */
  --accent-palette-4-strong: #7E5400; /* oklch(0.480 0.130 75.4) */
}
```

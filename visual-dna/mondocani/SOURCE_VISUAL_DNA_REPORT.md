# Source Visual DNA & Design-Sommelier Dossier: `mondocani`

- **Mandanten-Slug:** `mondocani`
- **Ursprungs-URL:** `https://mondocani.ch/`
- **Design-Modus:** `evolution`
- **Branche / Kontext:** Hundeschule, Mensch-Hund-Begleitung & Coaching
- **Gewaehlter Schweizer Meister-Archetyp:** **1. Warm Humanist Editorial (Praxis, Coaching, Therapie, Gesundheit, Paedagogik)**
- **Vorher-Kamera-Beweise:** `visual-dna/mondocani/source_desktop.png` (`1440x900`) & `visual-dna/mondocani/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers – Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.817`**<br>• `hero_luminance`: **`0.518`**<br>• Kamera-Pixel oben/Hero: `0.775` / `0.308`<br>• Gemessene Flaechen: Body `#E9F0EE`, Hero `#E9F0EE` | **Regel 1 (Polaritaets-Entscheid):**<br>LICHT-SPERRE AKTIV (#UI-16): Ursprungsseite ist im Gesamteindruck (body_luminance=0.817) und Hero (hero_luminance=0.518) hell/freundlich. Dunkle Startbuehnen sind strikt verboten (Sensor S-27 ueberwacht >= 0.45)! | • **`target_hero_polarity: "light"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`>= 0.45 Pflicht!`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#E9F0EE`<br>• Primaer-Farbton `H = 67.7deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #FEF9F5` (`oklch(0.985 0.008 67.7)`)<br>• `--bg-soft: #F8EEE5` (`oklch(0.955 0.016 67.7)`)<br>• `--text-main: #1E1409` (Kontrast **`17.31:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 1`**<br>• Gefundene Akzent-Cluster: `#C39C73` (`L=0.719, C=0.072, H=67.7deg`, Gewicht 490) | **Regel 3 (60-30-10 Marken-Harmonie):**<br>Klare, fokussierte Marken-Farbwelt (1 Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt. | • **10 % Primaer-CTA (`--primary`):** `#AB6900` (Original: `#C39C73`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Poppins`<br>• Body-Font: `Roboto`<br>• Gemessene Radien: `0px, 1px, 10px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Poppins / Roboto) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`warm_humanist_editorial`** (Helle, warme Tinted Neutrals, entschleunigte Lesbarkeit, hohe menschliche Naehe und Vertrauenswuerdigkeit ohne sterile Spital-Kaelte.) | • `--font-display: 'Lora', Georgia, serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`4`** (max. Breite: **`2000px`**)<br>• Hi-Res (`>=1100px`): `1` | Low-Res (`<900px`): `3`<br>• Hochformat-Anteil: `25 %` | **Regel 5 (Bild-Schutz-Regel):**<br>Hochaufloesendes Bildmaterial vorhanden (max. 2000px Breite). Sowohl "split_framed_card" (#UI-02) als auch architektonische Buehne ohne Verpixelung moeglich. | • **`recommended_hero_layout: "split_framed_card_or_architectural_stage"`**<br>• `forbid_fullscreen_bg_image: false`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>Standard-Sektionsabfolge (Hero -> Angebot -> Ueber uns -> Kontakt) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#C39C73` (`H=67.7deg`) | `#F8EEE5` (`oklch(0.955 0.016 67.7)`) | **`#AB6900`** (`oklch(0.580 0.160 67.7)`) |
| Slot 1 (`--accent-palette-1`) | `#928111` (`H=99.7deg`) | `#F4F0D5` (`oklch(0.950 0.035 99.7)`) | `#6B5E00` (`oklch(0.480 0.130 99.7)`) |
| Slot 2 (`--accent-palette-2`) | `#658F3E` (`H=131.7deg`) | `#E6F4DC` (`oklch(0.950 0.035 131.7)`) | `#416C05` (`oklch(0.480 0.130 131.7)`) |
| Slot 3 (`--accent-palette-3`) | `#1F966C` (`H=163.7deg`) | `#DAF6E8` (`oklch(0.950 0.035 163.7)`) | `#006F4D` (`oklch(0.480 0.130 163.7)`) |
| Slot 4 (`--accent-palette-4`) | `#009394` (`H=195.7deg`) | `#D5F6F6` (`oklch(0.950 0.035 195.7)`) | `#006C6C` (`oklch(0.480 0.130 195.7)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_mondocani_site.py`

```css
/* Google Fonts Import fuer Archetyp "warm_humanist_editorial":
   @import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
*/
:root {
  /* === 1. Polaritaet & Schweizer Raster (#UI-02, #UI-16, Sensor S-27) === */
  --wp-expected-hero-polarity: "light";
  --wp-archetype: "warm_humanist_editorial";
  --container-max: 1100px;
  --radius-card: 8px;
  --radius-badge: 4px;

  /* === 2. Typografie (warm_humanist_editorial) === */
  --font-display: 'Lora', Georgia, serif;
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=67.7deg) === */
  --bg-page: #FEF9F5;
  --bg-page-oklch: oklch(0.985 0.008 67.7);
  --bg-soft: #F8EEE5;
  --bg-soft-oklch: oklch(0.955 0.016 67.7);
  --bg-elevated: #FFFFFF;
  --border-subtle: #E1D9D1;
  --border-subtle-oklch: oklch(0.890 0.014 67.7);
  --text-main: #1E1409;
  --text-main-oklch: oklch(0.200 0.025 67.7);
  --text-muted: #554B42;
  --text-muted-oklch: oklch(0.420 0.020 67.7);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #AB6900;
  --primary-brand-raw: #C39C73;
  --primary-oklch: oklch(0.580 0.160 67.7);
  --primary-hover: #8C5500;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #F4F0D5; /* oklch(0.950 0.035 99.7) */
  --accent-palette-1-strong: #6B5E00; /* oklch(0.480 0.130 99.7) */
  --accent-palette-2-soft: #E6F4DC; /* oklch(0.950 0.035 131.7) */
  --accent-palette-2-strong: #416C05; /* oklch(0.480 0.130 131.7) */
  --accent-palette-3-soft: #DAF6E8; /* oklch(0.950 0.035 163.7) */
  --accent-palette-3-strong: #006F4D; /* oklch(0.480 0.130 163.7) */
  --accent-palette-4-soft: #D5F6F6; /* oklch(0.950 0.035 195.7) */
  --accent-palette-4-strong: #006C6C; /* oklch(0.480 0.130 195.7) */
}
```

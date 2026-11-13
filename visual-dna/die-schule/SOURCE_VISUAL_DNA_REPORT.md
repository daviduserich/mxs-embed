# Source Visual DNA & Design-Sommelier Dossier: `die-schule`

- **Mandanten-Slug:** `die-schule`
- **Ursprungs-URL:** `https://goodfordogs.ch/index.html`
- **Design-Modus:** `evolution`
- **Branche / Kontext:** Aus Seiteninhalt ermittelt
- **Gewaehlter Schweizer Meister-Archetyp:** **1. Warm Humanist Editorial (Praxis, Coaching, Therapie, Gesundheit, Paedagogik)**
- **Vorher-Kamera-Beweise:** `visual-dna/die-schule/source_desktop.png` (`1440x900`) & `visual-dna/die-schule/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers – Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.972`**<br>• `hero_luminance`: **`0.985`**<br>• Kamera-Pixel oben/Hero: `0.997` / `0.976`<br>• Gemessene Flaechen: Body `#F9F9F9`, Hero `#F9F9F9` | **Regel 1 (Polaritaets-Entscheid):**<br>LICHT-SPERRE AKTIV (#UI-16): Ursprungsseite ist im Gesamteindruck (body_luminance=0.972) und Hero (hero_luminance=0.985) hell/freundlich. Dunkle Startbuehnen sind strikt verboten (Sensor S-27 ueberwacht >= 0.45)! | • **`target_hero_polarity: "light"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`>= 0.45 Pflicht!`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#F9F9F9`<br>• Primaer-Farbton `H = 212.8deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #F4FCFD` (`oklch(0.985 0.008 212.8)`)<br>• `--bg-soft: #E5F3F7` (`oklch(0.955 0.016 212.8)`)<br>• `--text-main: #07191D` (Kontrast **`17.32:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 2`**<br>• Gefundene Akzent-Cluster: `#5199A8` (`L=0.642, C=0.075, H=212.8deg`, Gewicht 51), `#0073FF` (`L=0.589, C=0.226, H=258.8deg`, Gewicht 50) | **Regel 3 (60-30-10 Marken-Harmonie):**<br>Klare, fokussierte Marken-Farbwelt (2 Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt. | • **10 % Primaer-CTA (`--primary`):** `#00899E` (Original: `#5199A8`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Lora`<br>• Body-Font: `Raleway`<br>• Gemessene Radien: `0px, 3px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Lora / Raleway) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`warm_humanist_editorial`** (Helle, warme Tinted Neutrals, entschleunigte Lesbarkeit, hohe menschliche Naehe und Vertrauenswuerdigkeit ohne sterile Spital-Kaelte.) | • `--font-display: 'Lora', Georgia, serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`2`** (max. Breite: **`621px`**)<br>• Hi-Res (`>=1100px`): `0` | Low-Res (`<900px`): `2`<br>• Hochformat-Anteil: `0 %` | **Regel 5 (Bild-Schutz-Regel):**<br>BILD-SCHUTZ-SPERRE AKTIV: Maximale Originalbild-Breite (621px < 1000px) bzw. Hochformat-Anteil (0 %). Unscharfe Fullscreen-Hintergrundbilder sind verboten -> zwingend "split_framed_card" (links Typografie + Kennzahlen, rechts eingerahmte Bild-Karte mit Unterkanten-Buendigkeit #UI-02) bauen! | • **`recommended_hero_layout: "split_framed_card"`**<br>• `forbid_fullscreen_bg_image: true`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>Standard-Sektionsabfolge (Hero -> Angebot -> Ueber uns -> Kontakt) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#5199A8` (`H=212.8deg`) | `#E5F3F7` (`oklch(0.955 0.016 212.8)`) | **`#00899E`** (`oklch(0.580 0.160 212.8)`) |
| Slot 1 (`--accent-palette-1`) | `#0073FF` (`H=258.8deg`) | `#E5EFFF` (`oklch(0.950 0.035 258.8)`) | `#2B5CA6` (`oklch(0.480 0.130 258.8)`) |
| Slot 2 (`--accent-palette-2`) | `#6E78C7` (`H=276.8deg`) | `#EAEDFF` (`oklch(0.950 0.035 276.8)`) | `#4C53A5` (`oklch(0.480 0.130 276.8)`) |
| Slot 3 (`--accent-palette-3`) | `#956BB6` (`H=308.8deg`) | `#F5E9FF` (`oklch(0.950 0.035 308.8)`) | `#734594` (`oklch(0.480 0.130 308.8)`) |
| Slot 4 (`--accent-palette-4`) | `#AF6196` (`H=340.8deg`) | `#FFE6F5` (`oklch(0.950 0.035 340.8)`) | `#8C3B73` (`oklch(0.480 0.130 340.8)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_die_schule_site.py`

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

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=212.8deg) === */
  --bg-page: #F4FCFD;
  --bg-page-oklch: oklch(0.985 0.008 212.8);
  --bg-soft: #E5F3F7;
  --bg-soft-oklch: oklch(0.955 0.016 212.8);
  --bg-elevated: #FFFFFF;
  --border-subtle: #D1DDE0;
  --border-subtle-oklch: oklch(0.890 0.014 212.8);
  --text-main: #07191D;
  --text-main-oklch: oklch(0.200 0.025 212.8);
  --text-muted: #415054;
  --text-muted-oklch: oklch(0.420 0.020 212.8);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #00899E;
  --primary-brand-raw: #5199A8;
  --primary-oklch: oklch(0.580 0.160 212.8);
  --primary-hover: #007081;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #E5EFFF; /* oklch(0.950 0.035 258.8) */
  --accent-palette-1-strong: #2B5CA6; /* oklch(0.480 0.130 258.8) */
  --accent-palette-2-soft: #EAEDFF; /* oklch(0.950 0.035 276.8) */
  --accent-palette-2-strong: #4C53A5; /* oklch(0.480 0.130 276.8) */
  --accent-palette-3-soft: #F5E9FF; /* oklch(0.950 0.035 308.8) */
  --accent-palette-3-strong: #734594; /* oklch(0.480 0.130 308.8) */
  --accent-palette-4-soft: #FFE6F5; /* oklch(0.950 0.035 340.8) */
  --accent-palette-4-strong: #8C3B73; /* oklch(0.480 0.130 340.8) */
}
```

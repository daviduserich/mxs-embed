# Source Visual DNA & Design-Sommelier Dossier: `holz-susi`

- **Mandanten-Slug:** `holz-susi`
- **Ursprungs-URL:** `https://holz-susi.ch/`
- **Design-Modus:** `evolution`
- **Branche / Kontext:** Aus Seiteninhalt ermittelt
- **Gewaehlter Schweizer Meister-Archetyp:** **1. Warm Humanist Editorial (Praxis, Coaching, Therapie, Gesundheit, Paedagogik)**
- **Vorher-Kamera-Beweise:** `visual-dna/holz-susi/source_desktop.png` (`1440x900`) & `visual-dna/holz-susi/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers — Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.887`**<br>• `hero_luminance`: **`0.693`**<br>• Kamera-Pixel oben/Hero: `0.617` / `0.756`<br>• Gemessene Flaechen: Body `#FFFFFF`, Hero `#FFFFFF` | **Regel 1 (Polaritaets-Entscheid):**<br>LICHT-SPERRE AKTIV (#UI-16): Ursprungsseite ist im Gesamteindruck (body_luminance=0.887) und Hero (hero_luminance=0.693) hell/freundlich. Dunkle Startbuehnen sind strikt verboten (Sensor S-27 ueberwacht >= 0.45)! | • **`target_hero_polarity: "light"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`>= 0.45 Pflicht!`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#FFFFFF`<br>• Primaer-Farbton `H = 64.2deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #FEF9F5` (`oklch(0.985 0.008 64.2)`)<br>• `--bg-soft: #F8EEE5` (`oklch(0.955 0.016 64.2)`)<br>• `--text-main: #1E140A` (Kontrast **`17.31:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 1`**<br>• Gefundene Akzent-Cluster: `#A67B52` (`L=0.616, C=0.078, H=64.2deg`, Gewicht 316) | **Regel 3 (60-30-10 Marken-Harmonie):**<br>Klare, fokussierte Marken-Farbwelt (1 Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt. | • **10 % Primaer-CTA (`--primary`):** `#AF6600` (Original: `#A67B52`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Comfortaa`<br>• Body-Font: `Comfortaa`<br>• Gemessene Radien: `0px, 5px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Comfortaa / Comfortaa) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`warm_humanist_editorial`** (Helle, warme Tinted Neutrals, entschleunigte Lesbarkeit, hohe menschliche Naehe und Vertrauenswuerdigkeit ohne sterile Spital-Kaelte.) | • `--font-display: 'Lora', Georgia, serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`56`** (max. Breite: **`2000px`**)<br>• Hi-Res (`>=1100px`): `15` | Low-Res (`<900px`): `41`<br>• Hochformat-Anteil: `14 %` | **Regel 5 (Bild-Schutz-Regel):**<br>Hochaufloesendes Bildmaterial vorhanden (max. 2000px Breite). Sowohl "split_framed_card" (#UI-02) als auch architektonische Buehne ohne Verpixelung moeglich. | • **`recommended_hero_layout: "split_framed_card_or_architectural_stage"`**<br>• `forbid_fullscreen_bg_image: false`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>Standard-Sektionsabfolge (Hero -> Angebot -> Ueber uns -> Kontakt) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#A67B52` (`H=64.2deg`) | `#F8EEE5` (`oklch(0.955 0.016 64.2)`) | **`#AF6600`** (`oklch(0.580 0.160 64.2)`) |
| Slot 1 (`--accent-palette-1`) | `#957F0E` (`H=96.2deg`) | `#F5EFD5` (`oklch(0.950 0.035 96.2)`) | `#6E5D00` (`oklch(0.480 0.130 96.2)`) |
| Slot 2 (`--accent-palette-2`) | `#6B8D39` (`H=128.2deg`) | `#E8F3DB` (`oklch(0.950 0.035 128.2)`) | `#486A00` (`oklch(0.480 0.130 128.2)`) |
| Slot 3 (`--accent-palette-3`) | `#2A9667` (`H=160.2deg`) | `#DBF6E7` (`oklch(0.950 0.035 160.2)`) | `#007048` (`oklch(0.480 0.130 160.2)`) |
| Slot 4 (`--accent-palette-4`) | `#009390` (`H=192.2deg`) | `#D5F6F4` (`oklch(0.950 0.035 192.2)`) | `#006C6A` (`oklch(0.480 0.130 192.2)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_holz_susi_site.py`

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

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=64.2deg) === */
  --bg-page: #FEF9F5;
  --bg-page-oklch: oklch(0.985 0.008 64.2);
  --bg-soft: #F8EEE5;
  --bg-soft-oklch: oklch(0.955 0.016 64.2);
  --bg-elevated: #FFFFFF;
  --border-subtle: #E2D9D1;
  --border-subtle-oklch: oklch(0.890 0.014 64.2);
  --text-main: #1E140A;
  --text-main-oklch: oklch(0.200 0.025 64.2);
  --text-muted: #554B42;
  --text-muted-oklch: oklch(0.420 0.020 64.2);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #AF6600;
  --primary-brand-raw: #A67B52;
  --primary-oklch: oklch(0.580 0.160 64.2);
  --primary-hover: #8F5300;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #F5EFD5; /* oklch(0.950 0.035 96.2) */
  --accent-palette-1-strong: #6E5D00; /* oklch(0.480 0.130 96.2) */
  --accent-palette-2-soft: #E8F3DB; /* oklch(0.950 0.035 128.2) */
  --accent-palette-2-strong: #486A00; /* oklch(0.480 0.130 128.2) */
  --accent-palette-3-soft: #DBF6E7; /* oklch(0.950 0.035 160.2) */
  --accent-palette-3-strong: #007048; /* oklch(0.480 0.130 160.2) */
  --accent-palette-4-soft: #D5F6F4; /* oklch(0.950 0.035 192.2) */
  --accent-palette-4-strong: #006C6A; /* oklch(0.480 0.130 192.2) */
}
```

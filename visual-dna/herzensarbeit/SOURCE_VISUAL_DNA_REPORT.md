# Source Visual DNA & Design-Sommelier Dossier: `herzensarbeit`

- **Mandanten-Slug:** `herzensarbeit`
- **Ursprungs-URL:** `https://herzensarbeit.ch`
- **Design-Modus:** `evolution`
- **Branche / Kontext:** Paartherapie, Eheberatung, Trennungs- & Trauerbegleitung, Frauen-Workshops
- **Gewaehlter Schweizer Meister-Archetyp:** **1. Warm Humanist Editorial (Praxis, Coaching, Therapie, Gesundheit, Paedagogik)**
- **Vorher-Kamera-Beweise:** `visual-dna/herzensarbeit/source_desktop.png` (`1440x900`) & `visual-dna/herzensarbeit/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers — Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.963`**<br>• `hero_luminance`: **`0.753`**<br>• Kamera-Pixel oben/Hero: `0.926` / `0.611`<br>• Gemessene Flaechen: Body `#FFFFFF`, Hero `#FFFFFF` | **Regel 1 (Polaritaets-Entscheid):**<br>LICHT-SPERRE AKTIV (#UI-16): Ursprungsseite ist im Gesamteindruck (body_luminance=0.963) und Hero (hero_luminance=0.753) hell/freundlich. Dunkle Startbuehnen sind strikt verboten (Sensor S-27 ueberwacht >= 0.45)! | • **`target_hero_polarity: "light"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`>= 0.45 Pflicht!`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#FFFFFF`<br>• Primaer-Farbton `H = 14.7deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #FFF8F8` (`oklch(0.985 0.008 14.7)`)<br>• `--bg-soft: #FBECED` (`oklch(0.955 0.016 14.7)`)<br>• `--text-main: #201112` (Kontrast **`17.42:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 2`**<br>• Gefundene Akzent-Cluster: `#9A1536` (`L=0.446, C=0.165, H=14.7deg`, Gewicht 526), `#B08060` (`L=0.64, C=0.075, H=54.6deg`, Gewicht 80) | **Regel 3 (60-30-10 Marken-Harmonie):**<br>Klare, fokussierte Marken-Farbwelt (2 Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt. | • **10 % Primaer-CTA (`--primary`):** `#B4324A` (Original: `#9A1536`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Josefin Sans`<br>• Body-Font: `Josefin Sans`<br>• Gemessene Radien: `3px, 10px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Josefin Sans / Josefin Sans) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`warm_humanist_editorial`** (Helle, warme Tinted Neutrals, entschleunigte Lesbarkeit, hohe menschliche Naehe und Vertrauenswuerdigkeit ohne sterile Spital-Kaelte.) | • `--font-display: 'Lora', Georgia, serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`1`** (max. Breite: **`350px`**)<br>• Hi-Res (`>=1100px`): `0` | Low-Res (`<900px`): `1`<br>• Hochformat-Anteil: `0 %` | **Regel 5 (Bild-Schutz-Regel):**<br>BILD-SCHUTZ-SPERRE AKTIV: Maximale Originalbild-Breite (350px < 1000px) bzw. Hochformat-Anteil (0 %). Unscharfe Fullscreen-Hintergrundbilder sind verboten -> zwingend "split_framed_card" (links Typografie + Kennzahlen, rechts eingerahmte Bild-Karte mit Unterkanten-Buendigkeit #UI-02) bauen! | • **`recommended_hero_layout: "split_framed_card"`**<br>• `forbid_fullscreen_bg_image: true`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>Standard-Sektionsabfolge (Hero -> Angebot -> Ueber uns -> Kontakt) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#9A1536` (`H=14.7deg`) | `#FBECED` (`oklch(0.955 0.016 14.7)`) | **`#B4324A`** (`oklch(0.520 0.165 14.7)`) |
| Slot 1 (`--accent-palette-1`) | `#B08060` (`H=54.6deg`) | `#FFEADC` (`oklch(0.950 0.035 54.6)`) | `#8F4700` (`oklch(0.480 0.130 54.6)`) |
| Slot 2 (`--accent-palette-2`) | `#A67612` (`H=78.7deg`) | `#FCECD5` (`oklch(0.950 0.035 78.7)`) | `#7C5500` (`oklch(0.480 0.130 78.7)`) |
| Slot 3 (`--accent-palette-3`) | `#848620` (`H=110.7deg`) | `#EFF1D7` (`oklch(0.950 0.035 110.7)`) | `#616200` (`oklch(0.480 0.130 110.7)`) |
| Slot 4 (`--accent-palette-4`) | `#52924E` (`H=142.7deg`) | `#E2F5E0` (`oklch(0.950 0.035 142.7)`) | `#276F25` (`oklch(0.480 0.130 142.7)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_herzensarbeit_site.py`

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

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=14.7deg) === */
  --bg-page: #FFF8F8;
  --bg-page-oklch: oklch(0.985 0.008 14.7);
  --bg-soft: #FBECED;
  --bg-soft-oklch: oklch(0.955 0.016 14.7);
  --bg-elevated: #FFFFFF;
  --border-subtle: #E4D7D8;
  --border-subtle-oklch: oklch(0.890 0.014 14.7);
  --text-main: #201112;
  --text-main-oklch: oklch(0.200 0.025 14.7);
  --text-muted: #58494A;
  --text-muted-oklch: oklch(0.420 0.020 14.7);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #B4324A;
  --primary-brand-raw: #9A1536;
  --primary-oklch: oklch(0.520 0.165 14.7);
  --primary-hover: #9B1737;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #FFEADC; /* oklch(0.950 0.035 54.6) */
  --accent-palette-1-strong: #8F4700; /* oklch(0.480 0.130 54.6) */
  --accent-palette-2-soft: #FCECD5; /* oklch(0.950 0.035 78.7) */
  --accent-palette-2-strong: #7C5500; /* oklch(0.480 0.130 78.7) */
  --accent-palette-3-soft: #EFF1D7; /* oklch(0.950 0.035 110.7) */
  --accent-palette-3-strong: #616200; /* oklch(0.480 0.130 110.7) */
  --accent-palette-4-soft: #E2F5E0; /* oklch(0.950 0.035 142.7) */
  --accent-palette-4-strong: #276F25; /* oklch(0.480 0.130 142.7) */
}
```

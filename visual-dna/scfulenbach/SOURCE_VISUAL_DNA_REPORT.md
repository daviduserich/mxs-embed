# Source Visual DNA & Design-Sommelier Dossier: `scfulenbach`

- **Mandanten-Slug:** `scfulenbach`
- **Ursprungs-URL:** `https://www.scfulenbach.ch`
- **Design-Modus:** `redesign`
- **Branche / Kontext:** Fussballclub, Sportverein & Juniorenfoerderung
- **Gewaehlter Schweizer Meister-Archetyp:** **4. Dynamic Club & Community Spirit (Vereine, Verbaende, Teamsport, Sportfoerderung)**
- **Vorher-Kamera-Beweise:** `visual-dna/scfulenbach/source_desktop.png` (`1440x900`) & `visual-dna/scfulenbach/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers – Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.797`**<br>• `hero_luminance`: **`0.531`**<br>• Kamera-Pixel oben/Hero: `0.575` / `0.495`<br>• Gemessene Flaechen: Body `#FFFFFF`, Hero `#FFFFFF` | **Regel 1 (Polaritaets-Entscheid):**<br>Redesign-Modus gewaehlt: Startbuehne darf gezielt neu inszeniert werden (target_hero_polarity="dark"). | • **`target_hero_polarity: "dark"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`Dunkle Buehne erlaubt`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#FFFFFF`<br>• Primaer-Farbton `H = 233.4deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #F5FBFF` (`oklch(0.985 0.008 233.4)`)<br>• `--bg-soft: #E6F2F9` (`oklch(0.955 0.016 233.4)`)<br>• `--text-main: #0A1820` (Kontrast **`17.29:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 4`**<br>• Gefundene Akzent-Cluster: `#33B8F4` (`L=0.739, C=0.139, H=233.4deg`, Gewicht 469), `#2EAB66` (`L=0.657, C=0.149, H=154.1deg`, Gewicht 351), `#FF0000` (`L=0.628, C=0.258, H=29.2deg`, Gewicht 118), `#0000FF` (`L=0.452, C=0.313, H=264.1deg`, Gewicht 12) | **Regel 3 (Bunter-Kuchen-Zaehmung aktiv!):**<br>Marken-Seele = farbenfroh/vielseitig (4 verschiedene Farbtoene erkannt -> behalten!), aber Saettigungs-Chaos auf 60-30-10 reduzieren! 1 Primaer-CTA-Chef (10 %) + 3 OKLCH-normalisierte Pastell-/Akzent-Toene gleicher optischer Ruhe. | • **10 % Primaer-CTA (`--primary`):** `#0085B6` (Original: `#33B8F4`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Oswald`<br>• Body-Font: `Roboto`<br>• Gemessene Radien: `0px, 20px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Oswald / Roboto) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`dynamic_club_spirit`** (Stolze Vereinsfarben im 60-30-10-Raster, emotionale Vereins-Identitaet kombiniert mit aufgeraeumter Kader-, Spielplan- und Sponsoren-Struktur.) | • `--font-display: 'Montserrat', 'Plus Jakarta Sans', sans-serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`18`** (max. Breite: **`2437px`**)<br>• Hi-Res (`>=1100px`): `10` | Low-Res (`<900px`): `2`<br>• Hochformat-Anteil: `0 %` | **Regel 5 (Bild-Schutz-Regel):**<br>Hochaufloesendes Bildmaterial vorhanden (max. 2437px Breite). Sowohl "split_framed_card" (#UI-02) als auch architektonische Buehne ohne Verpixelung moeglich. | • **`recommended_hero_layout: "split_framed_card_or_architectural_stage"`**<br>• `forbid_fullscreen_bg_image: false`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>Standard-Sektionsabfolge (Hero -> Angebot -> Ueber uns -> Kontakt) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#33B8F4` (`H=233.4deg`) | `#E6F2F9` (`oklch(0.955 0.016 233.4)`) | **`#0085B6`** (`oklch(0.580 0.160 233.4)`) |
| Slot 1 (`--accent-palette-1`) | `#2EAB66` (`H=154.1deg`) | `#DDF6E4` (`oklch(0.950 0.035 154.1)`) | `#00713C` (`oklch(0.480 0.130 154.1)`) |
| Slot 2 (`--accent-palette-2`) | `#FF0000` (`H=29.2deg`) | `#FFE9E5` (`oklch(0.950 0.035 29.2)`) | `#993A2F` (`oklch(0.480 0.130 29.2)`) |
| Slot 3 (`--accent-palette-3`) | `#0000FF` (`H=264.1deg`) | `#E6EFFF` (`oklch(0.950 0.035 264.1)`) | `#3759A6` (`oklch(0.480 0.130 264.1)`) |
| Slot 4 (`--accent-palette-4`) | `#B95F7B` (`H=1.4deg`) | `#FFE7ED` (`oklch(0.950 0.035 1.4)`) | `#953859` (`oklch(0.480 0.130 1.4)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_scfulenbach_site.py`

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

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=233.4deg) === */
  --bg-page: #F5FBFF;
  --bg-page-oklch: oklch(0.985 0.008 233.4);
  --bg-soft: #E6F2F9;
  --bg-soft-oklch: oklch(0.955 0.016 233.4);
  --bg-elevated: #FFFFFF;
  --border-subtle: #D2DDE3;
  --border-subtle-oklch: oklch(0.890 0.014 233.4);
  --text-main: #0A1820;
  --text-main-oklch: oklch(0.200 0.025 233.4);
  --text-muted: #434F56;
  --text-muted-oklch: oklch(0.420 0.020 233.4);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #0085B6;
  --primary-brand-raw: #33B8F4;
  --primary-oklch: oklch(0.580 0.160 233.4);
  --primary-hover: #006C95;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #DDF6E4; /* oklch(0.950 0.035 154.1) */
  --accent-palette-1-strong: #00713C; /* oklch(0.480 0.130 154.1) */
  --accent-palette-2-soft: #FFE9E5; /* oklch(0.950 0.035 29.2) */
  --accent-palette-2-strong: #993A2F; /* oklch(0.480 0.130 29.2) */
  --accent-palette-3-soft: #E6EFFF; /* oklch(0.950 0.035 264.1) */
  --accent-palette-3-strong: #3759A6; /* oklch(0.480 0.130 264.1) */
  --accent-palette-4-soft: #FFE7ED; /* oklch(0.950 0.035 1.4) */
  --accent-palette-4-strong: #953859; /* oklch(0.480 0.130 1.4) */
}
```

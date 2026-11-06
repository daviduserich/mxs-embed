# Source Visual DNA & Design-Sommelier Dossier: `bunter-kuchen-test`

- **Mandanten-Slug:** `bunter-kuchen-test`
- **Ursprungs-URL:** `synthetic://raw-html`
- **Design-Modus:** `evolution`
- **Branche / Kontext:** Praxis, Coaching & Begleitung
- **Gewaehlter Schweizer Meister-Archetyp:** **1. Warm Humanist Editorial (Praxis, Coaching, Therapie, Gesundheit, Paedagogik)**
- **Vorher-Kamera-Beweise:** `visual-dna/bunter-kuchen-test/source_desktop.png` (`1440x900`) & `visual-dna/bunter-kuchen-test/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers — Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.972`**<br>• `hero_luminance`: **`0.912`**<br>• Kamera-Pixel oben/Hero: `0.943` / `0.887`<br>• Gemessene Flaechen: Body `#FFFFFF`, Hero `#FFF9F5` | **Regel 1 (Polaritaets-Entscheid):**<br>LICHT-SPERRE AKTIV (#UI-16): Ursprungsseite ist im Gesamteindruck (body_luminance=0.972) und Hero (hero_luminance=0.912) hell/freundlich. Dunkle Startbuehnen sind strikt verboten (Sensor S-27 ueberwacht >= 0.45)! | • **`target_hero_polarity: "light"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`>= 0.45 Pflicht!`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#FFFFFF`<br>• Primaer-Farbton `H = 17.6deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #FFF8F8` (`oklch(0.985 0.008 17.6)`)<br>• `--bg-soft: #FBECEC` (`oklch(0.955 0.016 17.6)`)<br>• `--text-main: #201112` (Kontrast **`17.42:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 5`**<br>• Gefundene Akzent-Cluster: `#E11D48` (`L=0.586, C=0.222, H=17.6deg`, Gewicht 95), `#16A34A` (`L=0.627, C=0.17, H=149.2deg`, Gewicht 80), `#2563EB` (`L=0.546, C=0.215, H=262.9deg`, Gewicht 80), `#D97706` (`L=0.666, C=0.157, H=58.3deg`, Gewicht 80), `#9333EA` (`L=0.558, C=0.252, H=302.3deg`, Gewicht 80) | **Regel 3 (Bunter-Kuchen-Zaehmung aktiv!):**<br>Marken-Seele = farbenfroh/vielseitig (5 verschiedene Farbtoene erkannt -> behalten!), aber Saettigungs-Chaos auf 60-30-10 reduzieren! 1 Primaer-CTA-Chef (10 %) + 4 OKLCH-normalisierte Pastell-/Akzent-Toene gleicher optischer Ruhe. | • **10 % Primaer-CTA (`--primary`):** `#D7314C` (Original: `#E11D48`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Times New Roman`<br>• Body-Font: `Arial`<br>• Gemessene Radien: `0px, 4px, 6px, 12px, 18px, 24px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Alte System-/Fallback-Schrift erkannt (Times New Roman / Arial) -> wird als handwerklicher Alt-Baufehler geheilt.<br>• Archetyp: **`warm_humanist_editorial`** (Helle, warme Tinted Neutrals, entschleunigte Lesbarkeit, hohe menschliche Naehe und Vertrauenswuerdigkeit ohne sterile Spital-Kaelte.) | • `--font-display: 'Lora', Georgia, serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`1`** (max. Breite: **`420px`**)<br>• Hi-Res (`>=1100px`): `0` | Low-Res (`<900px`): `1`<br>• Hochformat-Anteil: `100 %` | **Regel 5 (Bild-Schutz-Regel):**<br>BILD-SCHUTZ-SPERRE AKTIV: Maximale Originalbild-Breite (420px < 1000px) bzw. Hochformat-Anteil (100 %). Unscharfe Fullscreen-Hintergrundbilder sind verboten -> zwingend "split_framed_card" (links Typografie + Kennzahlen, rechts eingerahmte Bild-Karte mit Unterkanten-Buendigkeit #UI-02) bauen! | • **`recommended_hero_layout: "split_framed_card"`**<br>• `forbid_fullscreen_bg_image: true`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>1. `hero_stage` (Willkommen in unserer bunten Praxis fuer Coaching & Begleitu) -> 2. `content_section` (content_section) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#E11D48` (`H=17.6deg`) | `#FBECEC` (`oklch(0.955 0.016 17.6)`) | **`#D7314C`** (`oklch(0.580 0.200 17.6)`) |
| Slot 1 (`--accent-palette-1`) | `#16A34A` (`H=149.2deg`) | `#DFF6E2` (`oklch(0.950 0.035 149.2)`) | `#0C7131` (`oklch(0.480 0.130 149.2)`) |
| Slot 2 (`--accent-palette-2`) | `#2563EB` (`H=262.9deg`) | `#E6EFFF` (`oklch(0.950 0.035 262.9)`) | `#355AA6` (`oklch(0.480 0.130 262.9)`) |
| Slot 3 (`--accent-palette-3`) | `#D97706` (`H=58.3deg`) | `#FFEADB` (`oklch(0.950 0.035 58.3)`) | `#8C4A00` (`oklch(0.480 0.130 58.3)`) |
| Slot 4 (`--accent-palette-4`) | `#9333EA` (`H=302.3deg`) | `#F2EAFF` (`oklch(0.950 0.035 302.3)`) | `#6C4899` (`oklch(0.480 0.130 302.3)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_bunter_kuchen_test_site.py`

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

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=17.6deg) === */
  --bg-page: #FFF8F8;
  --bg-page-oklch: oklch(0.985 0.008 17.6);
  --bg-soft: #FBECEC;
  --bg-soft-oklch: oklch(0.955 0.016 17.6);
  --bg-elevated: #FFFFFF;
  --border-subtle: #E4D7D7;
  --border-subtle-oklch: oklch(0.890 0.014 17.6);
  --text-main: #201112;
  --text-main-oklch: oklch(0.200 0.025 17.6);
  --text-muted: #584949;
  --text-muted-oklch: oklch(0.420 0.020 17.6);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #D7314C;
  --primary-brand-raw: #E11D48;
  --primary-oklch: oklch(0.580 0.200 17.6);
  --primary-hover: #BA0136;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #DFF6E2; /* oklch(0.950 0.035 149.2) */
  --accent-palette-1-strong: #0C7131; /* oklch(0.480 0.130 149.2) */
  --accent-palette-2-soft: #E6EFFF; /* oklch(0.950 0.035 262.9) */
  --accent-palette-2-strong: #355AA6; /* oklch(0.480 0.130 262.9) */
  --accent-palette-3-soft: #FFEADB; /* oklch(0.950 0.035 58.3) */
  --accent-palette-3-strong: #8C4A00; /* oklch(0.480 0.130 58.3) */
  --accent-palette-4-soft: #F2EAFF; /* oklch(0.950 0.035 302.3) */
  --accent-palette-4-strong: #6C4899; /* oklch(0.480 0.130 302.3) */
}
```

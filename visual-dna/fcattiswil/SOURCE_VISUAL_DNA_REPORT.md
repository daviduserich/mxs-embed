# Source Visual DNA & Design-Sommelier Dossier: `fcattiswil`

- **Mandanten-Slug:** `fcattiswil`
- **Ursprungs-URL:** `file:///home/brainuser/workspaces/mxs-embed/preview-fcattiswil/index.html`
- **Design-Modus:** `evolution`
- **Branche / Kontext:** Fussballclub, Vereinsleben & Sportfoerderung
- **Gewaehlter Schweizer Meister-Archetyp:** **4. Dynamic Club & Community Spirit (Vereine, Verbaende, Teamsport, Sportfoerderung)**
- **Vorher-Kamera-Beweise:** `visual-dna/fcattiswil/source_desktop.png` (`1440x900`) & `visual-dna/fcattiswil/source_mobile.png` (`375x812`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers — Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• `body_luminance`: **`0.621`**<br>• `hero_luminance`: **`0.077`**<br>• Kamera-Pixel oben/Hero: `0.289` / `0.173`<br>• Gemessene Flaechen: Body `#F8FAFC`, Hero `#311522` | **Regel 1 (Polaritaets-Entscheid):**<br>Ursprungs-Startbuehne war nachweislich dunkel gestaltet (hero_luminance=0.077 < 0.42). Dunkler/kontrastreicher Hero ist im Evolution-Modus erlaubt. | • **`target_hero_polarity: "dark"`**<br>• **`target_page_polarity: "light"`**<br>• Sensor **`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)`** prueft bei jedem Build automatisch die Hero-Luminanz (`Dunkle Buehne erlaubt`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund `#F8FAFC`<br>• Primaer-Farbton `H = 27.6deg` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (`#FFFFFF`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (`Chroma 0.008–0.025`). | • `--bg-page: #FFF8F7` (`oklch(0.985 0.008 27.6)`)<br>• `--bg-soft: #FBECEA` (`oklch(0.955 0.016 27.6)`)<br>• `--text-main: #201210` (Kontrast **`17.32:1`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **`distinct_accent_hues_count = 5`**<br>• Gefundene Akzent-Cluster: `#C81E1E` (`L=0.535, C=0.203, H=27.6deg`, Gewicht 259), `#F59E0B` (`L=0.769, C=0.165, H=70.1deg`, Gewicht 137), `#60A020` (`L=0.638, C=0.168, H=133.3deg`, Gewicht 80), `#10B981` (`L=0.696, C=0.149, H=162.5deg`, Gewicht 18), `#FDE047` (`L=0.905, C=0.166, H=98.1deg`, Gewicht 8) | **Regel 3 (Bunter-Kuchen-Zaehmung aktiv!):**<br>Marken-Seele = farbenfroh/vielseitig (5 verschiedene Farbtoene erkannt -> behalten!), aber Saettigungs-Chaos auf 60-30-10 reduzieren! 1 Primaer-CTA-Chef (10 %) + 4 OKLCH-normalisierte Pastell-/Akzent-Toene gleicher optischer Ruhe. | • **10 % Primaer-CTA (`--primary`):** `#C72120` (Original: `#C81E1E`)<br>• **Sekundaer-Farben (`--accent-palette-1..4`):** In `OKLCH` auf exakt gleiche optische Ruhe (`L=0.95, C=0.035` Pastell & `L=0.48, C=0.13` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: `Montserrat`<br>• Body-Font: `Inter`<br>• Gemessene Radien: `0px, 4px, 8px` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>Bestehende Schrift-Gattung (Montserrat / Inter) wird typografisch im Schweizer Meister-Archetyp veredelt.<br>• Archetyp: **`dynamic_club_spirit`** (Stolze Vereinsfarben im 60-30-10-Raster, emotionale Vereins-Identitaet kombiniert mit aufgeraeumter Kader-, Spielplan- und Sponsoren-Struktur.) | • `--font-display: 'Montserrat', 'Plus Jakarta Sans', sans-serif`<br>• `--font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`<br>• Strikte 2-Radius-Architektur (`4px` Badges, `8px` Cards/Buttons, `1100px` Schweizer Fluchtlinie `#UI-02`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **`6`** (max. Breite: **`960px`**)<br>• Hi-Res (`>=1100px`): `0` | Low-Res (`<900px`): `4`<br>• Hochformat-Anteil: `17 %` | **Regel 5 (Bild-Schutz-Regel):**<br>BILD-SCHUTZ-SPERRE AKTIV: Maximale Originalbild-Breite (960px < 1000px) bzw. Hochformat-Anteil (17 %). Unscharfe Fullscreen-Hintergrundbilder sind verboten -> zwingend "split_framed_card" (links Typografie + Kennzahlen, rechts eingerahmte Bild-Karte mit Unterkanten-Buendigkeit #UI-02) bauen! | • **`recommended_hero_layout: "split_framed_card"`**<br>• `forbid_fullscreen_bg_image: true`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (`#UI-02`, Sensor `S-23`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>1. `hero_stage` (Fussballclub Attiswil — Herzblut auf dem Lindenrain.) -> 2. `references_or_trust` (Unsere 23 Sponsoren, der 300er Club & Gönner.) -> 3. `about_or_portrait` (Transparenter Vorschau-Entwurf: Welche Beispiel-Seiten berei) -> 4. `content_section` (content_section) | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (`social-media` & `blog`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + `data-section="social-media"` + `data-section="blog"`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (`60-30-10` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (`L=0.95, C=0.035`) | Veredelter Icon-/Badge-Akzent (`L=0.48, C=0.13`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | `#C81E1E` (`H=27.6deg`) | `#FBECEA` (`oklch(0.955 0.016 27.6)`) | **`#C72120`** (`oklch(0.535 0.200 27.6)`) |
| Slot 1 (`--accent-palette-1`) | `#F59E0B` (`H=70.1deg`) | `#FEEBD6` (`oklch(0.950 0.035 70.1)`) | `#825100` (`oklch(0.480 0.130 70.1)`) |
| Slot 2 (`--accent-palette-2`) | `#60A020` (`H=133.3deg`) | `#E5F4DC` (`oklch(0.950 0.035 133.3)`) | `#3E6C0C` (`oklch(0.480 0.130 133.3)`) |
| Slot 3 (`--accent-palette-3`) | `#10B981` (`H=162.5deg`) | `#DBF6E8` (`oklch(0.950 0.035 162.5)`) | `#006F4C` (`oklch(0.480 0.130 162.5)`) |
| Slot 4 (`--accent-palette-4`) | `#FDE047` (`H=98.1deg`) | `#F4EFD5` (`oklch(0.950 0.035 98.1)`) | `#6D5D00` (`oklch(0.480 0.130 98.1)`) |

---

## 3. Verbindlicher CSS `:root` Token-Block fuer `build_fcattiswil_site.py`

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

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=27.6deg) === */
  --bg-page: #FFF8F7;
  --bg-page-oklch: oklch(0.985 0.008 27.6);
  --bg-soft: #FBECEA;
  --bg-soft-oklch: oklch(0.955 0.016 27.6);
  --bg-elevated: #FFFFFF;
  --border-subtle: #E4D7D6;
  --border-subtle-oklch: oklch(0.890 0.014 27.6);
  --text-main: #201210;
  --text-main-oklch: oklch(0.200 0.025 27.6);
  --text-muted: #584947;
  --text-muted-oklch: oklch(0.420 0.020 27.6);

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: #C72120;
  --primary-brand-raw: #C81E1E;
  --primary-oklch: oklch(0.535 0.200 27.6);
  --primary-hover: #AB000B;

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: #FEEBD6; /* oklch(0.950 0.035 70.1) */
  --accent-palette-1-strong: #825100; /* oklch(0.480 0.130 70.1) */
  --accent-palette-2-soft: #E5F4DC; /* oklch(0.950 0.035 133.3) */
  --accent-palette-2-strong: #3E6C0C; /* oklch(0.480 0.130 133.3) */
  --accent-palette-3-soft: #DBF6E8; /* oklch(0.950 0.035 162.5) */
  --accent-palette-3-strong: #006F4C; /* oklch(0.480 0.130 162.5) */
  --accent-palette-4-soft: #F4EFD5; /* oklch(0.950 0.035 98.1) */
  --accent-palette-4-strong: #6D5D00; /* oklch(0.480 0.130 98.1) */
}
```

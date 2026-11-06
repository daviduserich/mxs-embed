#!/usr/bin/env node
/**
 * extract_source_visual_dna.mjs — 3-Stufen «Source Visual DNA & Design-Sommelier» Engine v1.0
 * ===========================================================================================
 * Verbindliches Vorab-Analyse- & Veredelungs-Werkzeug fuer WebPilot (#UI-01, #UI-02, #UI-14, #UI-16, #LANG-01).
 *
 * Warum dieses Werkzeug existiert:
 *   Zwischen dem optischen Messen einer bestehenden Kunden-Webseite (Stufe 1) und dem Bau der
 *   neuen WebPilot-Seite (Stufe 3) steht der deterministische «Design-Sommelier» (Stufe 2).
 *   Er bewahrt die wiedererkennbare Marken-Seele (Helligkeit, Atmosphaere, Farbcharakter)
 *   und veredelt gleichzeitig alte handwerkliche Baufehler (z. B. «bunter Kuchen aus 5 knalligen
 *   Farben», Arial/Times New Roman, fehlende Abstaende, verpixelte Mini-Bilder, schwache Kontraste)
 *   nach State-of-the-Art Design-Engineering-Prinzipien:
 *     - pbakaus/impeccable & Refactoring UI (Tinted Neutrals statt Spital-Weiss)
 *     - OKLCH Perceptual Color Space (gleiche empfundene Helligkeit L & Ruhe C ueber alle Farbtoene H)
 *     - 60-30-10 Farb-Gewichtung (Bunter-Kuchen-Zaehmung: 1 Primaer-CTA + harmonisierte Pastell-/Akzent-Palette)
 *     - 4 Schweizer Meister-Archetypen & Bild-Schutz-Regel (#UI-02 Split-Framed-Card bei < 1000px Fotos)
 *
 * Aufruf:
 *   node scripts/extract_source_visual_dna.mjs --url <https://...> --slug <slug> [--design-mode evolution|redesign] [--industry "..."]
 *   node scripts/extract_source_visual_dna.mjs --from-existing-site <preview-dir> --slug <slug>
 *   node scripts/extract_source_visual_dna.mjs --generate-all-profiles
 *   node scripts/extract_source_visual_dna.mjs --self-test
 */

import fs from 'fs';
import path from 'path';
import http from 'http';
import { fileURLToPath } from 'url';
import { createRequire } from 'module';

const require = createRequire('/home/brainuser/workspaces/ACP-Authentic-Content-Pilot-Pro0396/acp-app/package.json');
const { chromium } = require('playwright-core');

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const MXS_ROOT = fs.existsSync('/home/brainuser/workspaces/mxs-embed')
  ? '/home/brainuser/workspaces/mxs-embed'
  : path.resolve(__dirname, '..');
const VISUAL_DNA_ROOT = path.join(MXS_ROOT, 'visual-dna');

const CHROMIUM_PATHS = [
  '/home/brainuser/.cache/ms-playwright/chromium-1217/chrome-linux64/chrome',
  '/home/brainuser/.cache/ms-playwright/chromium-1217/chrome-linux/chrome',
  '/home/brainuser/.cache/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-linux64/chrome-headless-shell'
];

function getChromiumPath() {
  for (const p of CHROMIUM_PATHS) {
    if (fs.existsSync(p)) return p;
  }
  throw new Error('Playwright Chromium binary nicht gefunden.');
}

// ============================================================================
// MATHEMATISCHE FARBRAUM-FUNKTIONEN (sRGB <-> Linear RGB <-> OKLab <-> OKLCH)
// ============================================================================

function clamp(val, min, max) {
  return Math.max(min, Math.min(max, val));
}

function srgbChannelToLinear(v255) {
  const s = clamp(v255 / 255, 0, 1);
  return s <= 0.04045 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
}

function linearChannelToSrgb(lin) {
  const c = clamp(lin, 0, 1);
  const s = c <= 0.0031308 ? 12.92 * c : 1.055 * Math.pow(c, 1 / 2.4) - 0.055;
  return Math.round(clamp(s * 255, 0, 255));
}

export function relativeLuminanceRgb(r, g, b) {
  const rl = srgbChannelToLinear(r);
  const gl = srgbChannelToLinear(g);
  const bl = srgbChannelToLinear(b);
  return +(0.2126 * rl + 0.7152 * gl + 0.0722 * bl).toFixed(4);
}

export function wcagContrastRatio(rgb1, rgb2) {
  const l1 = relativeLuminanceRgb(rgb1[0], rgb1[1], rgb1[2]);
  const l2 = relativeLuminanceRgb(rgb2[0], rgb2[1], rgb2[2]);
  return +((Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05)).toFixed(2);
}

export function rgbToHex(r, g, b) {
  return (
    '#' +
    [r, g, b]
      .map(x => clamp(Math.round(x), 0, 255).toString(16).padStart(2, '0'))
      .join('')
      .toUpperCase()
  );
}

export function hexToRgb(hex) {
  const clean = String(hex || '').replace(/^#/, '').trim();
  if (clean.length === 3) {
    return [
      parseInt(clean[0] + clean[0], 16),
      parseInt(clean[1] + clean[1], 16),
      parseInt(clean[2] + clean[2], 16)
    ];
  }
  if (clean.length >= 6) {
    return [
      parseInt(clean.slice(0, 2), 16),
      parseInt(clean.slice(2, 4), 16),
      parseInt(clean.slice(4, 6), 16)
    ];
  }
  return [30, 41, 59];
}

export function rgbToOklch(r, g, b) {
  const rl = srgbChannelToLinear(r);
  const gl = srgbChannelToLinear(g);
  const bl = srgbChannelToLinear(b);

  const l = Math.cbrt(0.4122214708 * rl + 0.5363325363 * gl + 0.0514459929 * bl);
  const m = Math.cbrt(0.2119034982 * rl + 0.6806995451 * gl + 0.1073969566 * bl);
  const s = Math.cbrt(0.0883024619 * rl + 0.2817188376 * gl + 0.6299787005 * bl);

  const L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s;
  const A = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s;
  const B = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s;

  const C = Math.sqrt(A * A + B * B);
  let H = (Math.atan2(B, A) * 180) / Math.PI;
  if (H < 0) H += 360;
  if (C < 0.0005) H = 0;

  return {
    L: +clamp(L, 0, 1).toFixed(3),
    C: +clamp(C, 0, 0.4).toFixed(3),
    H: +H.toFixed(1)
  };
}

function oklchToLinearRgbUnclamped(L, C, H) {
  const hRad = ((H || 0) * Math.PI) / 180;
  const a = C * Math.cos(hRad);
  const b = C * Math.sin(hRad);

  const l_ = L + 0.3963377774 * a + 0.2158037573 * b;
  const m_ = L - 0.1055613458 * a - 0.0638541728 * b;
  const s_ = L - 0.0894841775 * a - 1.2914855480 * b;

  const l = l_ * l_ * l_;
  const m = m_ * m_ * m_;
  const s = s_ * s_ * s_;

  const r = +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s;
  const g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s;
  const bl = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s;
  return [r, g, bl];
}

export function oklchToRgb(L, C, H) {
  const targetL = clamp(L, 0, 1);
  let lowC = 0;
  let highC = Math.max(0, C);
  let bestLin = oklchToLinearRgbUnclamped(targetL, highC, H);

  const inGamut = lin =>
    lin[0] >= -0.0005 && lin[0] <= 1.0005 &&
    lin[1] >= -0.0005 && lin[1] <= 1.0005 &&
    lin[2] >= -0.0005 && lin[2] <= 1.0005;

  if (!inGamut(bestLin)) {
    for (let i = 0; i < 14; i++) {
      const midC = (lowC + highC) / 2;
      const cand = oklchToLinearRgbUnclamped(targetL, midC, H);
      if (inGamut(cand)) {
        lowC = midC;
        bestLin = cand;
      } else {
        highC = midC;
      }
    }
  }

  return [
    linearChannelToSrgb(bestLin[0]),
    linearChannelToSrgb(bestLin[1]),
    linearChannelToSrgb(bestLin[2])
  ];
}

export function oklchToHex(L, C, H) {
  const [r, g, b] = oklchToRgb(L, C, H);
  return rgbToHex(r, g, b);
}

export function formatOklchCss(L, C, H) {
  return `oklch(${Number(L).toFixed(3)} ${Number(C).toFixed(3)} ${Number(H).toFixed(1)})`;
}

function circularHueDistance(h1, h2) {
  const diff = Math.abs(h1 - h2) % 360;
  return diff > 180 ? 360 - diff : diff;
}

// ============================================================================
// SCHWEIZER MEISTER-ARCHETYPEN DEFINITION (#UI-01, #UI-02, #UI-16)
// ============================================================================

export const SWISS_MASTER_ARCHETYPES = {
  warm_humanist_editorial: {
    id: 'warm_humanist_editorial',
    label: '1. Warm Humanist Editorial (Praxis, Coaching, Therapie, Gesundheit, Paedagogik)',
    font_display: "'Lora', Georgia, serif",
    font_sans: "'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif",
    google_fonts_import: 'https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap',
    radius_card: '8px',
    radius_badge: '4px',
    grid_max_width: '1100px',
    default_polarity: 'light',
    character_note: 'Helle, warme Tinted Neutrals, entschleunigte Lesbarkeit, hohe menschliche Naehe und Vertrauenswuerdigkeit ohne sterile Spital-Kaelte.'
  },
  swiss_architectural_craft: {
    id: 'swiss_architectural_craft',
    label: '2. Swiss Architectural Craft (Handwerk, Solar, Schreinerei, Holzbau, Bau, Technik, Produktion)',
    font_display: "'Lexend', 'Plus Jakarta Sans', sans-serif",
    font_sans: "'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif",
    google_fonts_import: 'https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap',
    radius_card: '8px',
    radius_badge: '4px',
    grid_max_width: '1100px',
    default_polarity: 'light',
    character_note: 'Praezise 1100px Schweizer Fluchtlinien-Rasterung (#UI-02), messerscharfe 4px/8px Kanten, handwerkliche Substanz und klare Leistungs-Metriken.'
  },
  executive_authority: {
    id: 'executive_authority',
    label: '3. Executive Authority (Beratung, Fuehrung, Executive Coaching, Treuhand, IT, Recht)',
    font_display: "'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif",
    font_sans: "'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif",
    google_fonts_import: 'https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,600;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap',
    radius_card: '8px',
    radius_badge: '4px',
    grid_max_width: '1100px',
    default_polarity: 'light',
    character_note: 'Edles Warm-Alabaster (#F8F6F2), souveraene Typografie, ruhige Entscheidungs-Architektur fuer Geschaeftsleitung und Verwaltungsrat.'
  },
  dynamic_club_spirit: {
    id: 'dynamic_club_spirit',
    label: '4. Dynamic Club & Community Spirit (Vereine, Verbaende, Teamsport, Sportfoerderung)',
    font_display: "'Montserrat', 'Plus Jakarta Sans', sans-serif",
    font_sans: "'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif",
    google_fonts_import: 'https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap',
    radius_card: '8px',
    radius_badge: '4px',
    grid_max_width: '1100px',
    default_polarity: 'dark',
    character_note: 'Stolze Vereinsfarben im 60-30-10-Raster, emotionale Vereins-Identitaet kombiniert mit aufgeraeumter Kader-, Spielplan- und Sponsoren-Struktur.'
  }
};

function selectMasterArchetype({ slug = '', industry = '', title = '', hasSerifHeadings = false, heroLuminance = 0.75 }) {
  const haystack = `${slug} ${industry} ${title}`.toLowerCase();
  if (
    haystack.includes('textil') ||
    haystack.includes('frees') ||
    haystack.includes('stickerei')
  ) {
    return SWISS_MASTER_ARCHETYPES.swiss_architectural_craft;
  }
  if (
    haystack.includes('fussball') ||
    haystack.includes('fc ') ||
    haystack.includes('fcschlieren') ||
    haystack.includes('fcattiswil') ||
    haystack.includes('scfulenbach') ||
    haystack.includes('sportverein') ||
    haystack.includes('frauenfussball') ||
    haystack.includes('verein') ||
    haystack.includes('club') ||
    haystack.includes('her11')
  ) {
    return SWISS_MASTER_ARCHETYPES.dynamic_club_spirit;
  }
  if (
    haystack.includes('therapie') ||
    haystack.includes('paar') ||
    haystack.includes('herzensarbeit') ||
    haystack.includes('praxis') ||
    haystack.includes('psycholog') ||
    haystack.includes('gesundheit') ||
    haystack.includes('hebamme') ||
    haystack.includes('paedagog') ||
    haystack.includes('kinder') ||
    haystack.includes('begleitung')
  ) {
    return SWISS_MASTER_ARCHETYPES.warm_humanist_editorial;
  }
  if (
    haystack.includes('executive') ||
    haystack.includes('fuehrung') ||
    haystack.includes('führung') ||
    haystack.includes('innere-staerke') ||
    haystack.includes('innere stärke') ||
    haystack.includes('treuhand') ||
    haystack.includes('kanzlei') ||
    haystack.includes('recht') ||
    haystack.includes('consulting') ||
    haystack.includes('unternehmensberatung') ||
    haystack.includes('management')
  ) {
    return SWISS_MASTER_ARCHETYPES.executive_authority;
  }
  if (
    haystack.includes('solar') ||
    haystack.includes('joma') ||
    haystack.includes('schreiner') ||
    haystack.includes('holzbau') ||
    haystack.includes('hochuli') ||
    haystack.includes('hiltbrand') ||
    haystack.includes('birchmeier') ||
    haystack.includes('gebaeude') ||
    haystack.includes('gebäude') ||
    haystack.includes('textil') ||
    haystack.includes('frees') ||
    haystack.includes('imp-marketing') ||
    haystack.includes('handwerk') ||
    haystack.includes('technik') ||
    haystack.includes('bau')
  ) {
    return SWISS_MASTER_ARCHETYPES.swiss_architectural_craft;
  }
  if (hasSerifHeadings && heroLuminance >= 0.5) {
    return SWISS_MASTER_ARCHETYPES.warm_humanist_editorial;
  }
  return SWISS_MASTER_ARCHETYPES.swiss_architectural_craft;
}

// ============================================================================
// STUFE 1: FAKTEN MESSEN IM ECHTEN PLAYWRIGHT-BROWSER (3 VORHER-AUGEN)
// ============================================================================

async function measureScreenshotPixelFacts(helperPage, pngBuffer) {
  const b64 = pngBuffer.toString('base64');
  return await helperPage.evaluate(async b64Str => {
    const img = new Image();
    img.src = 'data:image/png;base64,' + b64Str;
    await new Promise((res, rej) => {
      img.onload = res;
      img.onerror = rej;
    });
    const c = document.createElement('canvas');
    c.width = img.width;
    c.height = img.height;
    const ctx = c.getContext('2d');
    ctx.drawImage(img, 0, 0);

    function relLum(r, g, b) {
      const a = [r, g, b].map(v => {
        const s = v / 255;
        return s <= 0.03928 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
      });
      return 0.2126 * a[0] + 0.7152 * a[1] + 0.0722 * a[2];
    }

    function avgRegion(y0, y1) {
      const h = Math.max(1, Math.min(img.height, y1) - Math.max(0, y0));
      const data = ctx.getImageData(0, Math.max(0, y0), img.width, h).data;
      let sum = 0;
      let count = 0;
      for (let i = 0; i < data.length; i += 16) {
        sum += relLum(data[i], data[i + 1], data[i + 2]);
        count++;
      }
      return count > 0 ? +(sum / count).toFixed(3) : 0.85;
    }

    // Sample dominant chromatic pixel clusters from the upper 700px (catches logo/banner colors)
    const sampleH = Math.min(img.height, 700);
    const imgData = ctx.getImageData(0, 0, img.width, sampleH).data;
    const buckets = new Map();
    for (let i = 0; i < imgData.length; i += 64) {
      const r = imgData[i];
      const g = imgData[i + 1];
      const b = imgData[i + 2];
      const maxC = Math.max(r, g, b);
      const minC = Math.min(r, g, b);
      if (maxC - minC < 38) continue; // skip achromatic pixels
      if (maxC < 35 || minC > 235) continue;
      // Quantize to 16-step RGB grid to group similar pixels
      const qr = Math.round(r / 16) * 16;
      const qg = Math.round(g / 16) * 16;
      const qb = Math.round(b / 16) * 16;
      const key = `${qr},${qg},${qb}`;
      buckets.set(key, (buckets.get(key) || 0) + 1);
    }
    const pixelColors = Array.from(buckets.entries())
      .sort((a, b) => b[1] - a[1])
      .slice(0, 6)
      .map(([k, count]) => {
        const [r, g, b] = k.split(',').map(Number);
        return { rgb: [r, g, b], count };
      });

    return {
      header_px_luminance: avgRegion(0, 105),
      hero_px_luminance: avgRegion(105, 620),
      lower_px_luminance: avgRegion(620, 900),
      overall_px_luminance: avgRegion(0, 900),
      pixel_chromatic_clusters: pixelColors
    };
  }, b64);
}

async function measureDomVisualFacts(page) {
  return await page.evaluate(() => {
    const VW = window.innerWidth;
    const VH = window.innerHeight;

    function isVisible(el) {
      if (!el || el.nodeType !== 1) return false;
      const cs = window.getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity || '1') < 0.1) return false;
      const r = el.getBoundingClientRect();
      return r.width > 2 && r.height > 2;
    }

    function parseRgbaList(str) {
      if (!str) return [];
      const out = [];
      const re = /rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)/g;
      let m;
      while ((m = re.exec(str)) !== null) {
        const a = m[4] !== undefined ? parseFloat(m[4]) : 1;
        if (a > 0.05) out.push([+m[1], +m[2], +m[3], a]);
      }
      return out;
    }

    function blendRgba(fgRgba, bgRgb) {
      const a = fgRgba[3];
      return [
        Math.round(fgRgba[0] * a + bgRgb[0] * (1 - a)),
        Math.round(fgRgba[1] * a + bgRgb[1] * (1 - a)),
        Math.round(fgRgba[2] * a + bgRgb[2] * (1 - a))
      ];
    }

    function getEffectiveBgRgb(el) {
      const layers = [];
      let cur = el;
      while (cur && cur !== document.documentElement) {
        const cs = window.getComputedStyle(cur);
        if (cs.backgroundImage && cs.backgroundImage.includes('gradient')) {
          const gcols = parseRgbaList(cs.backgroundImage);
          const opaqueStops = gcols.filter(c => c[3] >= 0.8);
          const stops = opaqueStops.length > 0 ? opaqueStops : gcols;
          if (stops.length >= 1) {
            const avg = [0, 0, 0, 0];
            stops.forEach(c => {
              avg[0] += c[0];
              avg[1] += c[1];
              avg[2] += c[2];
              avg[3] += c[3];
            });
            const layer = [avg[0] / stops.length, avg[1] / stops.length, avg[2] / stops.length, avg[3] / stops.length];
            layers.push(layer);
            if (layer[3] >= 0.95) break;
          }
        }
        const bgc = parseRgbaList(cs.backgroundColor);
        if (bgc.length > 0) {
          layers.push(bgc[0]);
          if (bgc[0][3] >= 0.95) break;
        }
        cur = cur.parentElement;
      }
      let base = [255, 255, 255];
      const bodyBg = parseRgbaList(window.getComputedStyle(document.body).backgroundColor);
      if (bodyBg.length > 0 && bodyBg[0][3] > 0.5) base = [bodyBg[0][0], bodyBg[0][1], bodyBg[0][2]];
      for (let i = layers.length - 1; i >= 0; i--) {
        base = blendRgba(layers[i], base);
      }
      return base;
    }

    function relLum(rgb) {
      const a = rgb.map(v => {
        const s = v / 255;
        return s <= 0.03928 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
      });
      return +(0.2126 * a[0] + 0.7152 * a[1] + 0.0722 * a[2]).toFixed(3);
    }

    function toHex(r, g, b) {
      return '#' + [r, g, b].map(x => Math.max(0, Math.min(255, Math.round(x))).toString(16).padStart(2, '0')).join('').toUpperCase();
    }

    const headerEl = document.querySelector('header, .site-header, .main-header, nav');
    const heroEl = document.querySelector('.hero-section, section.hero, .hero, .hero-wrap, [data-section="hero"], main > section:first-of-type, body > section:first-of-type');
    const footerEl = document.querySelector('footer, .site-footer');

    const bodyBgRgb = getEffectiveBgRgb(document.body);
    const headerBgRgb = headerEl ? getEffectiveBgRgb(headerEl) : bodyBgRgb;
    const heroBgRgb = heroEl ? getEffectiveBgRgb(heroEl) : bodyBgRgb;
    const footerBgRgb = footerEl ? getEffectiveBgRgb(footerEl) : bodyBgRgb;

    let heroHasExplicitCssBg = false;
    if (heroEl) {
      const hcs = window.getComputedStyle(heroEl);
      const bgs = parseRgbaList(hcs.backgroundColor);
      if ((bgs.length > 0 && bgs[0][3] > 0.3) || (hcs.backgroundImage && hcs.backgroundImage !== 'none')) {
        heroHasExplicitCssBg = true;
      }
    }

    // Collect visible colors with role weighting
    const colorMap = new Map();
    const textColors = new Map();
    const surfaceColors = new Map();
    const radiiSet = new Set();
    const containerWidths = [];

    const allEls = Array.from(document.querySelectorAll('*')).filter(isVisible);
    for (const el of allEls) {
      const r = el.getBoundingClientRect();
      if (r.width < 6 || r.height < 6 || r.top > 3200) continue;
      const cs = window.getComputedStyle(el);

      const isAction = el.matches('button, .btn, [class*="btn"], a[class*="btn"], a[class*="button"], [role="button"], input[type="submit"]');
      const isHeading = el.matches('h1, h2, h3, .hero-title, .section-title');
      const isNavOrHeader = Boolean(el.closest('header, nav'));
      const inUpperViewport = r.top < 850;

      const weight = (isAction ? 14 : isHeading ? 7 : isNavOrHeader ? 5 : 2) * (inUpperViewport ? 1.5 : 1);

      // Check border-radius on cards/buttons
      if (isAction || el.matches('.card, [class*="card"], [class*="box"], section > div')) {
        const br = parseFloat(cs.borderTopLeftRadius || '0');
        if (!Number.isNaN(br) && br >= 0 && br <= 100) {
          radiiSet.add(Math.round(br));
        }
      }

      // Check container max-width
      const mw = cs.maxWidth;
      if (mw && mw.endsWith('px')) {
        const mwVal = Math.round(parseFloat(mw));
        if (mwVal >= 900 && mwVal <= 1600) containerWidths.push(mwVal);
      }

      // Background & Gradient colors
      for (const prop of [cs.backgroundColor, cs.backgroundImage]) {
        for (const [cr, cg, cb, ca] of parseRgbaList(prop)) {
          if (ca < 0.2) continue;
          const hex = toHex(cr, cg, cb);
          if (r.width > 120 && r.height > 60) {
            surfaceColors.set(hex, (surfaceColors.get(hex) || 0) + Math.round((r.width * r.height) / 1000));
          }
          const role = isAction ? 'cta_button_bg' : 'surface_or_badge_bg';
          const prev = colorMap.get(hex) || { hex, rgb: [cr, cg, cb], weight: 0, roles: new Set() };
          prev.weight += weight * (isAction ? 1.8 : 1);
          prev.roles.add(role);
          colorMap.set(hex, prev);
        }
      }

      // Foreground / Text / Border / SVG colors
      for (const prop of [cs.color, cs.borderTopColor, cs.fill, cs.stroke]) {
        for (const [cr, cg, cb, ca] of parseRgbaList(prop)) {
          if (ca < 0.25) continue;
          const hex = toHex(cr, cg, cb);
          // Skip unstyled default browser link blue #0000EE unless it has a background
          if (hex === '#0000EE' && !isAction) continue;
          if (prop === cs.color) {
            textColors.set(hex, (textColors.get(hex) || 0) + 1);
          }
          const role = isAction ? 'cta_text_or_border' : isHeading ? 'heading_color' : 'accent_or_text';
          const prev = colorMap.get(hex) || { hex, rgb: [cr, cg, cb], weight: 0, roles: new Set() };
          prev.weight += weight * 0.8;
          prev.roles.add(role);
          colorMap.set(hex, prev);
        }
      }
    }

    // Typography inspection
    const h1El = document.querySelector('h1, .hero-title, h2');
    const bodyEl = document.querySelector('p, li, body') || document.body;
    const h1Cs = h1El ? window.getComputedStyle(h1El) : window.getComputedStyle(document.body);
    const bodyCs = window.getComputedStyle(bodyEl);

    const headingFontRaw = h1Cs.fontFamily || 'sans-serif';
    const bodyFontRaw = bodyCs.fontFamily || 'sans-serif';

    // Image inspection
    const imgs = Array.from(document.querySelectorAll('img'))
      .filter(im => isVisible(im))
      .map(im => {
        const r = im.getBoundingClientRect();
        const nw = im.naturalWidth || Math.round(r.width) || 0;
        const nh = im.naturalHeight || Math.round(r.height) || 0;
        return {
          src: (im.getAttribute('src') || '').slice(0, 120),
          naturalWidth: nw,
          naturalHeight: nh,
          renderedWidth: Math.round(r.width),
          renderedHeight: Math.round(r.height),
          isLogoOrIcon: nw < 180 && nh < 180
        };
      });

    const contentImgs = imgs.filter(im => !im.isLogoOrIcon && (im.naturalWidth >= 140 || im.renderedWidth >= 140));
    const maxImgW = contentImgs.length > 0 ? Math.max(...contentImgs.map(i => i.naturalWidth)) : 0;
    const hiResCount = contentImgs.filter(i => i.naturalWidth >= 1100).length;
    const lowResCount = contentImgs.filter(i => i.naturalWidth > 0 && i.naturalWidth < 900).length;
    const portraitCount = contentImgs.filter(i => i.naturalHeight > i.naturalWidth * 1.05).length;
    const landscapeCount = contentImgs.filter(i => i.naturalWidth >= i.naturalHeight * 0.95).length;

    // Section sequence discovery
    const rawSections = Array.from(document.querySelectorAll('main > section, body > section, .section, [data-section]')).filter(isVisible);
    const sectionSequence = rawSections.slice(0, 10).map((sec, idx) => {
      const ds = sec.getAttribute('data-section') || '';
      const id = sec.id || '';
      const cls = typeof sec.className === 'string' ? sec.className : '';
      const h = sec.querySelector('h1, h2, h3');
      const titleText = h ? h.textContent.replace(/\s+/g, ' ').trim().slice(0, 60) : '';
      const combined = `${ds} ${id} ${cls} ${titleText}`.toLowerCase();
      let type = 'content_section';
      if (idx === 0 || combined.includes('hero')) type = 'hero_stage';
      else if (combined.includes('leist') || combined.includes('angebot') || combined.includes('service') || combined.includes('workshop')) type = 'services_or_offers_grid';
      else if (combined.includes('ueber') || combined.includes('über') || combined.includes('team') || combined.includes('profil') || combined.includes('mich')) type = 'about_or_portrait';
      else if (combined.includes('referenz') || combined.includes('sponsor') || combined.includes('kunden') || combined.includes('stimmen')) type = 'references_or_trust';
      else if (combined.includes('faq') || combined.includes('fragen')) type = 'faq_accordion';
      else if (combined.includes('kontakt') || combined.includes('standort') || combined.includes('cta')) type = 'contact_or_cta';
      return { index: idx + 1, type, heading: titleText || type };
    });

    return {
      page_title: document.title || '',
      viewport: { width: VW, height: VH },
      dom_luminance: {
        body_luminance: relLum(bodyBgRgb),
        header_luminance: relLum(headerBgRgb),
        hero_luminance: relLum(heroBgRgb),
        footer_luminance: relLum(footerBgRgb),
        hero_has_explicit_css_bg: heroHasExplicitCssBg,
        body_bg_hex: toHex(...bodyBgRgb),
        header_bg_hex: toHex(...headerBgRgb),
        hero_bg_hex: toHex(...heroBgRgb)
      },
      raw_colors: Array.from(colorMap.values()).map(c => ({
        hex: c.hex,
        rgb: c.rgb,
        weight: Math.round(c.weight),
        roles: Array.from(c.roles)
      })),
      typography: {
        heading_font_family: headingFontRaw,
        body_font_family: bodyFontRaw,
        h1_font_size: h1Cs.fontSize || '',
        h1_line_height: h1Cs.lineHeight || '',
        body_font_size: bodyCs.fontSize || '',
        body_line_height: bodyCs.lineHeight || '',
        detected_border_radii_px: Array.from(radiiSet).sort((a, b) => a - b),
        detected_container_max_widths_px: Array.from(new Set(containerWidths)).sort((a, b) => a - b)
      },
      images: {
        total_visible_images: imgs.length,
        content_images_count: contentImgs.length,
        max_image_width_px: maxImgW,
        hi_res_images_count: hiResCount,
        low_res_images_count: lowResCount,
        portrait_images_count: portraitCount,
        landscape_images_count: landscapeCount,
        portrait_ratio_share: contentImgs.length > 0 ? +(portraitCount / contentImgs.length).toFixed(2) : 0
      },
      section_sequence: sectionSequence
    };
  });
}

// ============================================================================
// STUFE 2: DER «DESIGN-SOMMELIER» (ANALYSE & VEREDELUNG NACH IMPECCABLE + OKLCH)
// ============================================================================

export function runDesignSommelier({
  slug,
  sourceUrl,
  designMode = 'evolution',
  industry = '',
  fallbackBrandHex = '',
  domFacts,
  pixelFacts
}) {
  const mode = String(designMode || 'evolution').toLowerCase() === 'redesign' ? 'redesign' : 'evolution';

  // 1. Kombinierte Helligkeits-Messung (DOM + Kamera-Pixel)
  const domBodyLum = domFacts.dom_luminance.body_luminance;
  const domHeroLum = domFacts.dom_luminance.hero_luminance;
  const headerPxLum = pixelFacts.header_px_luminance;
  const heroPxLum = pixelFacts.hero_px_luminance;
  const overallPxLum = pixelFacts.overall_px_luminance;

  let effectiveHeroLuminance;
  if (domFacts.dom_luminance.hero_has_explicit_css_bg && domHeroLum < 0.42) {
    effectiveHeroLuminance = +(0.60 * domHeroLum + 0.40 * heroPxLum).toFixed(3);
  } else {
    effectiveHeroLuminance = +(0.55 * heroPxLum + 0.45 * headerPxLum).toFixed(3);
  }
  const effectiveBodyLuminance = +(0.50 * domBodyLum + 0.50 * Math.max(overallPxLum, headerPxLum)).toFixed(3);

  // 2. Farb-Extraktion & OKLCH Clustering (Zaehen der echten Akzent-Farbtoene)
  const combinedColorCandidates = [];
  for (const c of domFacts.raw_colors || []) {
    const ok = rgbToOklch(c.rgb[0], c.rgb[1], c.rgb[2]);
    // Ignore tiny social share default colors (#3B5998) when weight is low
    if (c.hex === '#3B5998' && c.weight < 18) continue;
    // Ignore standard Divi link blue (#2EA3F2) if another stronger brand color exists
    combinedColorCandidates.push({
      hex: c.hex,
      rgb: c.rgb,
      oklch: ok,
      weight: c.weight,
      roles: c.roles || [],
      source: 'dom'
    });
  }

  for (const pc of pixelFacts.pixel_chromatic_clusters || []) {
    const hex = rgbToHex(pc.rgb[0], pc.rgb[1], pc.rgb[2]);
    const ok = rgbToOklch(pc.rgb[0], pc.rgb[1], pc.rgb[2]);
    if (ok.C >= 0.055 && ok.L >= 0.18 && ok.L <= 0.88) {
      combinedColorCandidates.push({
        hex,
        rgb: pc.rgb,
        oklch: ok,
        weight: Math.min(40, Math.round(pc.count / 6)),
        roles: ['camera_pixel_cluster'],
        source: 'camera_pixels'
      });
    }
  }

  // Filter chromatic accent candidates (Chroma >= 0.045, Lightness 0.16..0.91)
  let chromaticCandidates = combinedColorCandidates
    .filter(c => c.oklch.C >= 0.045 && c.oklch.L >= 0.16 && c.oklch.L <= 0.91 && c.weight >= 8)
    .sort((a, b) => b.weight - a.weight);

  // If Divi default #2EA3F2 is present alongside a real brand color, demote #2EA3F2 unless it's the only color
  if (chromaticCandidates.length > 1 && chromaticCandidates.some(c => c.hex !== '#2EA3F2' && c.weight >= 25)) {
    chromaticCandidates = chromaticCandidates.filter(c => c.hex !== '#2EA3F2');
  }

  // Group into distinct Hue clusters (Delta H >= 25 degrees)
  const distinctHueClusters = [];
  for (const cand of chromaticCandidates) {
    const existing = distinctHueClusters.find(cl => circularHueDistance(cl.oklch.H, cand.oklch.H) < 25);
    if (!existing) {
      distinctHueClusters.push({
        representative_hex: cand.hex,
        rgb: cand.rgb,
        oklch: cand.oklch,
        total_weight: cand.weight,
        roles: Array.from(new Set(cand.roles))
      });
    } else {
      existing.total_weight += cand.weight;
      cand.roles.forEach(r => {
        if (!existing.roles.includes(r)) existing.roles.push(r);
      });
    }
  }

  distinctHueClusters.sort((a, b) => b.total_weight - a.total_weight);

  // Fallback brand color if page was purely monochrome or fallbackBrandHex provided
  if (distinctHueClusters.length === 0) {
    const fbRgb = hexToRgb(fallbackBrandHex || '#C88A36');
    const fbOk = rgbToOklch(fbRgb[0], fbRgb[1], fbRgb[2]);
    distinctHueClusters.push({
      representative_hex: rgbToHex(...fbRgb),
      rgb: fbRgb,
      oklch: fbOk,
      total_weight: 100,
      roles: ['fallback_brand_color']
    });
  } else if (fallbackBrandHex && distinctHueClusters[0].representative_hex === '#0000EE') {
    const fbRgb = hexToRgb(fallbackBrandHex);
    const fbOk = rgbToOklch(fbRgb[0], fbRgb[1], fbRgb[2]);
    distinctHueClusters.unshift({
      representative_hex: rgbToHex(...fbRgb),
      rgb: fbRgb,
      oklch: fbOk,
      total_weight: 120,
      roles: ['configured_brand_color']
    });
  }

  const distinctAccentHuesCount = distinctHueClusters.length;
  const primaryCluster = distinctHueClusters[0];
  const primaryHue = primaryCluster.oklch.H;

  // ==========================================================================
  // REGEL 1: HELLIGKEITS- & ATMOSPHAEREN-TREUE (polarity_decision)
  // ==========================================================================
  let targetHeroPolarity = 'light';
  let targetPagePolarity = 'light';
  let lightLockActive = true;
  let polarityReason = '';

  if (mode === 'redesign') {
    const archPreview = selectMasterArchetype({ slug, industry, title: domFacts.page_title });
    targetHeroPolarity = archPreview.default_polarity === 'dark' || effectiveHeroLuminance < 0.42 ? 'dark' : 'light';
    targetPagePolarity = 'light';
    lightLockActive = targetHeroPolarity === 'light';
    polarityReason = `Redesign-Modus gewaehlt: Startbuehne darf gezielt neu inszeniert werden (target_hero_polarity="${targetHeroPolarity}").`;
  } else {
    // Evolution-Modus (#UI-16)
    if (effectiveBodyLuminance >= 0.60 && effectiveHeroLuminance >= 0.50) {
      targetHeroPolarity = 'light';
      targetPagePolarity = 'light';
      lightLockActive = true;
      polarityReason = `LICHT-SPERRE AKTIV (#UI-16): Ursprungsseite ist im Gesamteindruck (body_luminance=${effectiveBodyLuminance}) und Hero (hero_luminance=${effectiveHeroLuminance}) hell/freundlich. Dunkle Startbuehnen sind strikt verboten (Sensor S-27 ueberwacht >= 0.45)!`;
    } else if (effectiveHeroLuminance < 0.42) {
      targetHeroPolarity = 'dark';
      targetPagePolarity = effectiveBodyLuminance >= 0.50 ? 'light' : 'dark';
      lightLockActive = false;
      polarityReason = `Ursprungs-Startbuehne war nachweislich dunkel gestaltet (hero_luminance=${effectiveHeroLuminance} < 0.42). Dunkler/kontrastreicher Hero ist im Evolution-Modus erlaubt.`;
    } else {
      targetHeroPolarity = 'light';
      targetPagePolarity = 'light';
      lightLockActive = true;
      polarityReason = `Evolution-Schutzregel (#UI-16): Mittlere Hero-Helligkeit (${effectiveHeroLuminance}) bei hellem Grundkoerper (${effectiveBodyLuminance}) -> Licht-Sperre target_hero_polarity="light" aktiv.`;
    }
  }

  // ==========================================================================
  // REGEL 2: «TINTED NEUTRALS» STATT KALTEM SPITAL-WEISS (impeccable / Refactoring UI)
  // ==========================================================================
  const bgPageOklch = { L: 0.985, C: 0.008, H: primaryHue };
  const bgSoftOklch = { L: 0.955, C: 0.016, H: primaryHue };
  const borderSubtleOklch = { L: 0.890, C: 0.014, H: primaryHue };
  const textMainOklch = { L: 0.200, C: 0.025, H: primaryHue };
  const textMutedOklch = { L: 0.420, C: 0.020, H: primaryHue };

  const bgPageHex = oklchToHex(bgPageOklch.L, bgPageOklch.C, bgPageOklch.H);
  const bgSoftHex = oklchToHex(bgSoftOklch.L, bgSoftOklch.C, bgSoftOklch.H);
  const borderSubtleHex = oklchToHex(borderSubtleOklch.L, borderSubtleOklch.C, borderSubtleOklch.H);
  const textMainHex = oklchToHex(textMainOklch.L, textMainOklch.C, textMainOklch.H);
  const textMutedHex = oklchToHex(textMutedOklch.L, textMutedOklch.C, textMutedOklch.H);

  const textContrastOnBg = wcagContrastRatio(hexToRgb(textMainHex), hexToRgb(bgPageHex));

  const tintedNeutrals = {
    brand_hue_deg: primaryHue,
    bg_page: {
      oklch: formatOklchCss(bgPageOklch.L, bgPageOklch.C, bgPageOklch.H),
      hex: bgPageHex,
      role: '60 % Haupt-Hintergrundflaeche mit feinem Marken-Hauch (Chroma 0.008)'
    },
    bg_soft: {
      oklch: formatOklchCss(bgSoftOklch.L, bgSoftOklch.C, bgSoftOklch.H),
      hex: bgSoftHex,
      role: '30 % Sekundaer-Sektionen & Karten-Flaechen (Chroma 0.016)'
    },
    bg_elevated: {
      oklch: 'oklch(1.000 0.000 0.0)',
      hex: '#FFFFFF',
      role: 'Erhabene Inhalts-Karten auf getoentem Canvas'
    },
    border_subtle: {
      oklch: formatOklchCss(borderSubtleOklch.L, borderSubtleOklch.C, borderSubtleOklch.H),
      hex: borderSubtleHex,
      role: 'Harmonische 1px Haarlinien-Rahmen im Marken-Farbton'
    },
    text_main: {
      oklch: formatOklchCss(textMainOklch.L, textMainOklch.C, textMainOklch.H),
      hex: textMainHex,
      contrast_vs_bg_page: `${textContrastOnBg}:1`,
      role: 'Tiefdunkle, mit Marken-Hue abgetoente Textfarbe (Kontrast >= 10:1)'
    },
    text_muted: {
      oklch: formatOklchCss(textMutedOklch.L, textMutedOklch.C, textMutedOklch.H),
      hex: textMutedHex,
      role: 'Ruhige Sekundaer-Textfarbe fuer Metadaten und Bildlegenden'
    }
  };

  // ==========================================================================
  // REGEL 3: DIE «BUNTER-KUCHEN-ZAEHMUNG» (60-30-10 + OKLCH MULTI-COLOR HARMONIZER)
  // ==========================================================================
  const isMulticolorChaos = distinctAccentHuesCount >= 3;
  const primaryHarmonizedL = clamp(primaryCluster.oklch.L, 0.52, 0.58);
  const primaryHarmonizedC = clamp(primaryCluster.oklch.C, 0.16, 0.20);
  const primaryHarmonizedHex = oklchToHex(primaryHarmonizedL, primaryHarmonizedC, primaryHue);
  const primaryHoverHex = oklchToHex(clamp(primaryHarmonizedL - 0.07, 0.40, 0.50), primaryHarmonizedC, primaryHue);

  // Build up to 4 secondary accent palette slots (from additional source hues or harmonic neighbors)
  const secondarySourceHues = distinctHueClusters.slice(1, 5).map(c => ({
    original_hex: c.representative_hex,
    original_oklch: c.oklch,
    hue: c.oklch.H
  }));

  while (secondarySourceHues.length < 4) {
    const idx = secondarySourceHues.length + 1;
    const synthHue = +((primaryHue + idx * 32) % 360).toFixed(1);
    secondarySourceHues.push({
      original_hex: oklchToHex(0.60, 0.12, synthHue),
      original_oklch: { L: 0.60, C: 0.12, H: synthHue },
      hue: synthHue,
      synthetic_extension: true
    });
  }

  const harmonizedAccentPalette = secondarySourceHues.map((item, idx) => {
    const h = item.hue;
    const pastelL = 0.950;
    const pastelC = 0.035;
    const strongL = 0.480;
    const strongC = 0.130;
    return {
      slot: idx + 1,
      token_prefix: `--accent-palette-${idx + 1}`,
      source_hex: item.original_hex,
      source_hue_deg: h,
      pastel_surface: {
        oklch: formatOklchCss(pastelL, pastelC, h),
        hex: oklchToHex(pastelL, pastelC, h),
        spec: 'L=0.95, C=0.035'
      },
      icon_accent: {
        oklch: formatOklchCss(strongL, strongC, h),
        hex: oklchToHex(strongL, strongC, h),
        spec: 'L=0.48, C=0.13'
      }
    };
  });

  const colorHarmonyDecision = {
    distinct_accent_hues_count: distinctAccentHuesCount,
    is_multicolor_chaos: isMulticolorChaos,
    sommelier_verdict: isMulticolorChaos
      ? `Marken-Seele = farbenfroh/vielseitig (${distinctAccentHuesCount} verschiedene Farbtoene erkannt -> behalten!), aber Saettigungs-Chaos auf 60-30-10 reduzieren! 1 Primaer-CTA-Chef (10 %) + ${Math.min(4, distinctAccentHuesCount - 1)} OKLCH-normalisierte Pastell-/Akzent-Toene gleicher optischer Ruhe.`
      : `Klare, fokussierte Marken-Farbwelt (${distinctAccentHuesCount} Haupt-Akzentton erkannt). Wird im 60-30-10-Verhaeltnis mit Tinted Neutrals veredelt.`,
    primary_10_percent_cta: {
      original_brand_hex: primaryCluster.representative_hex,
      original_oklch: primaryCluster.oklch,
      harmonized_oklch: formatOklchCss(primaryHarmonizedL, primaryHarmonizedC, primaryHue),
      harmonized_hex: primaryHarmonizedHex,
      hover_hex: primaryHoverHex
    },
    secondary_accent_palette: harmonizedAccentPalette
  };

  // ==========================================================================
  // REGEL 4: SCHRIFT- & ARCHETYP-VEREDELUNG (4 SCHWEIZER MEISTER-ARCHETYPEN)
  // ==========================================================================
  const rawFontString = `${domFacts.typography.heading_font_family} | ${domFacts.typography.body_font_family}`;
  const legacyFontRegex = /\b(Arial|Times New Roman|Times|Calibri|Comic Sans|Verdana|Tahoma|Trebuchet MS|Courier New|Lucida)\b/i;
  const primaryHeadingFontToken = (domFacts.typography.heading_font_family.split(',')[0] || '').replace(/['"]/g, '').trim();
  const primaryBodyFontToken = (domFacts.typography.body_font_family.split(',')[0] || '').replace(/['"]/g, '').trim();

  const usesCheapSystemPrimary =
    legacyFontRegex.test(primaryHeadingFontToken) ||
    legacyFontRegex.test(primaryBodyFontToken) ||
    primaryBodyFontToken.toLowerCase().includes('helvetica-w01');

  const hasSerifHeadings =
    /\b(serif|Lora|Playfair|Merriweather|Georgia|Cormorant|Newsreader|Times)\b/i.test(domFacts.typography.heading_font_family) &&
    !/\bsans-serif\b/i.test(primaryHeadingFontToken);

  const selectedArchetype = selectMasterArchetype({
    slug,
    industry,
    title: domFacts.page_title,
    hasSerifHeadings,
    heroLuminance: effectiveHeroLuminance
  });

  const typographyDecision = {
    measured_heading_font: primaryHeadingFontToken || 'System Standard',
    measured_body_font: primaryBodyFontToken || 'System Standard',
    heal_legacy_flaw: usesCheapSystemPrimary,
    legacy_flaw_diagnosis: usesCheapSystemPrimary
      ? `Alte System-/Fallback-Schrift erkannt (${primaryHeadingFontToken} / ${primaryBodyFontToken}) -> wird als handwerklicher Alt-Baufehler geheilt.`
      : `Bestehende Schrift-Gattung (${primaryHeadingFontToken} / ${primaryBodyFontToken}) wird typografisch im Schweizer Meister-Archetyp veredelt.`,
    selected_archetype: selectedArchetype
  };

  // ==========================================================================
  // REGEL 5: BILD-SCHUTZ-REGEL (image_layout_decision)
  // ==========================================================================
  const maxImgW = domFacts.images.max_image_width_px || 0;
  const portraitShare = domFacts.images.portrait_ratio_share || 0;
  const hasLowResOrPortraitConstraint = (maxImgW > 0 && maxImgW < 1000) || portraitShare >= 0.45;

  const imageLayoutDecision = {
    max_source_image_width_px: maxImgW,
    portrait_ratio_share: portraitShare,
    forbid_fullscreen_bg_image: hasLowResOrPortraitConstraint,
    recommended_hero_layout: hasLowResOrPortraitConstraint ? 'split_framed_card' : 'split_framed_card_or_architectural_stage',
    sommelier_verdict: hasLowResOrPortraitConstraint
      ? `BILD-SCHUTZ-SPERRE AKTIV: Maximale Originalbild-Breite (${maxImgW}px < 1000px) bzw. Hochformat-Anteil (${Math.round(portraitShare * 100)} %). Unscharfe Fullscreen-Hintergrundbilder sind verboten -> zwingend "split_framed_card" (links Typografie + Kennzahlen, rechts eingerahmte Bild-Karte mit Unterkanten-Buendigkeit #UI-02) bauen!`
      : `Hochaufloesendes Bildmaterial vorhanden (max. ${maxImgW}px Breite). Sowohl "split_framed_card" (#UI-02) als auch architektonische Buehne ohne Verpixelung moeglich.`
  };

  // ==========================================================================
  // STUFE 3: FIXFERTIGER CSS :root TOKEN-BLOCK GENERIEREN
  // ==========================================================================
  const p1 = harmonizedAccentPalette[0];
  const p2 = harmonizedAccentPalette[1];
  const p3 = harmonizedAccentPalette[2];
  const p4 = harmonizedAccentPalette[3];

  const cssRootBlock = `:root {
  /* === 1. Polaritaet & Schweizer Raster (#UI-02, #UI-16, Sensor S-27) === */
  --wp-expected-hero-polarity: "${targetHeroPolarity}";
  --wp-archetype: "${selectedArchetype.id}";
  --container-max: ${selectedArchetype.grid_max_width};
  --radius-card: ${selectedArchetype.radius_card};
  --radius-badge: ${selectedArchetype.radius_badge};

  /* === 2. Typografie (${selectedArchetype.id}) === */
  --font-display: ${selectedArchetype.font_display};
  --font-sans: ${selectedArchetype.font_sans};

  /* === 3. 60 % & 30 % Tinted Neutrals (impeccable / Refactoring UI, Hue=${primaryHue}deg) === */
  --bg-page: ${tintedNeutrals.bg_page.hex};
  --bg-page-oklch: ${tintedNeutrals.bg_page.oklch};
  --bg-soft: ${tintedNeutrals.bg_soft.hex};
  --bg-soft-oklch: ${tintedNeutrals.bg_soft.oklch};
  --bg-elevated: ${tintedNeutrals.bg_elevated.hex};
  --border-subtle: ${tintedNeutrals.border_subtle.hex};
  --border-subtle-oklch: ${tintedNeutrals.border_subtle.oklch};
  --text-main: ${tintedNeutrals.text_main.hex};
  --text-main-oklch: ${tintedNeutrals.text_main.oklch};
  --text-muted: ${tintedNeutrals.text_muted.hex};
  --text-muted-oklch: ${tintedNeutrals.text_muted.oklch};

  /* === 4. 10 % Primaer-CTA-Chef (Marken-Hauptfarbe) === */
  --primary: ${colorHarmonyDecision.primary_10_percent_cta.harmonized_hex};
  --primary-brand-raw: ${colorHarmonyDecision.primary_10_percent_cta.original_brand_hex};
  --primary-oklch: ${colorHarmonyDecision.primary_10_percent_cta.harmonized_oklch};
  --primary-hover: ${colorHarmonyDecision.primary_10_percent_cta.hover_hex};

  /* === 5. OKLCH-Harmonisierte Sekundaer-Palette (Bunter-Kuchen-Zaehmung: L=0.95/C=0.035 & L=0.48/C=0.13) === */
  --accent-palette-1-soft: ${p1.pastel_surface.hex}; /* ${p1.pastel_surface.oklch} */
  --accent-palette-1-strong: ${p1.icon_accent.hex}; /* ${p1.icon_accent.oklch} */
  --accent-palette-2-soft: ${p2.pastel_surface.hex}; /* ${p2.pastel_surface.oklch} */
  --accent-palette-2-strong: ${p2.icon_accent.hex}; /* ${p2.icon_accent.oklch} */
  --accent-palette-3-soft: ${p3.pastel_surface.hex}; /* ${p3.pastel_surface.oklch} */
  --accent-palette-3-strong: ${p3.icon_accent.hex}; /* ${p3.icon_accent.oklch} */
  --accent-palette-4-soft: ${p4.pastel_surface.hex}; /* ${p4.pastel_surface.oklch} */
  --accent-palette-4-strong: ${p4.icon_accent.hex}; /* ${p4.icon_accent.oklch} */
}`;

  return {
    schema_version: '1.0.0',
    generated_at: new Date().toISOString(),
    slug,
    source_url: sourceUrl || '',
    design_mode: mode,
    industry: industry || '',
    stage_1_measured_facts: {
      luminance: {
        body_luminance: effectiveBodyLuminance,
        hero_luminance: effectiveHeroLuminance,
        header_px_luminance: headerPxLum,
        hero_px_luminance: heroPxLum,
        lower_px_luminance: pixelFacts.lower_px_luminance,
        dom_body_luminance: domBodyLum,
        dom_hero_luminance: domHeroLum,
        body_bg_hex: domFacts.dom_luminance.body_bg_hex,
        header_bg_hex: domFacts.dom_luminance.header_bg_hex,
        hero_bg_hex: domFacts.dom_luminance.hero_bg_hex
      },
      colors: {
        distinct_accent_hues_count: distinctAccentHuesCount,
        primary_detected_hex: primaryCluster.representative_hex,
        primary_detected_oklch: primaryCluster.oklch,
        distinct_hue_clusters: distinctHueClusters
      },
      typography: domFacts.typography,
      images: domFacts.images,
      section_sequence: domFacts.section_sequence
    },
    sommelier_decisions: {
      polarity_decision: {
        design_mode: mode,
        target_hero_polarity: targetHeroPolarity,
        target_page_polarity: targetPagePolarity,
        light_lock_active: lightLockActive,
        s27_min_hero_luminance_threshold: targetHeroPolarity === 'light' ? 0.45 : 0.0,
        reason: polarityReason
      },
      tinted_neutrals: tintedNeutrals,
      color_harmony_60_30_10: colorHarmonyDecision,
      typography_and_archetype: typographyDecision,
      image_layout_decision: imageLayoutDecision
    },
    stage_3_blueprint: {
      css_root_tokens: cssRootBlock,
      recommended_hero_layout: imageLayoutDecision.recommended_hero_layout,
      target_hero_polarity: targetHeroPolarity,
      selected_archetype_id: selectedArchetype.id,
      google_fonts_import: selectedArchetype.google_fonts_import
    }
  };
}

// ============================================================================
// STUFE 3: MARKDOWN-DOSSIER GENERIEREN (SOURCE_VISUAL_DNA_REPORT.md)
// ============================================================================

export function renderVisualDnaReportMarkdown(dna) {
  const f = dna.stage_1_measured_facts;
  const s = dna.sommelier_decisions;
  const pol = s.polarity_decision;
  const tn = s.tinted_neutrals;
  const ch = s.color_harmony_60_30_10;
  const typo = s.typography_and_archetype;
  const img = s.image_layout_decision;

  const clusterListStr = f.colors.distinct_hue_clusters
    .slice(0, 6)
    .map(
      (c, i) =>
        `\`${c.representative_hex}\` (\`L=${c.oklch.L}, C=${c.oklch.C}, H=${c.oklch.H}deg\`, Gewicht ${c.total_weight})`
    )
    .join(', ');

  const secSeqStr =
    (f.section_sequence || [])
      .map(sec => `${sec.index}. \`${sec.type}\` (${sec.heading})`)
      .join(' -> ') || 'Standard-Sektionsabfolge (Hero -> Angebot -> Ueber uns -> Kontakt)';

  const secondaryRows = ch.secondary_accent_palette
    .map(
      p =>
        `| Slot ${p.slot} (\`${p.token_prefix}\`) | \`${p.source_hex}\` (\`H=${p.source_hue_deg}deg\`) | \`${p.pastel_surface.hex}\` (\`${p.pastel_surface.oklch}\`) | \`${p.icon_accent.hex}\` (\`${p.icon_accent.oklch}\`) |`
    )
    .join('\n');

  const report = `# Source Visual DNA & Design-Sommelier Dossier: \`${dna.slug}\`

- **Mandanten-Slug:** \`${dna.slug}\`
- **Ursprungs-URL:** \`${dna.source_url || 'Lokale Referenz / Neubau-Entwurf'}\`
- **Design-Modus:** \`${dna.design_mode}\`
- **Branche / Kontext:** ${dna.industry || 'Aus Seiteninhalt ermittelt'}
- **Gewaehlter Schweizer Meister-Archetyp:** **${typo.selected_archetype.label}**
- **Vorher-Kamera-Beweise:** \`visual-dna/${dna.slug}/source_desktop.png\` (\`1440x900\`) & \`visual-dna/${dna.slug}/source_mobile.png\` (\`375x812\`)

---

## 1. Die 3-Spalten-Entscheidungstabelle (Fakten messen -> Sommelier-Veredelung -> Bauplan)

| 1. Gemessener Fakt auf der Ursprungsseite (Stufe 1) | 2. Urteil des Design-Sommeliers — Seele behalten vs. Baufehler heilen (Stufe 2) | 3. Konkrete WebPilot-Bau-Anweisung & Pruef-Schranke (Stufe 3) |
|---|---|---|
| **Licht & Atmosphaere (Auge 2):**<br>• \`body_luminance\`: **\`${f.luminance.body_luminance}\`**<br>• \`hero_luminance\`: **\`${f.luminance.hero_luminance}\`**<br>• Kamera-Pixel oben/Hero: \`${f.luminance.header_px_luminance}\` / \`${f.luminance.hero_px_luminance}\`<br>• Gemessene Flaechen: Body \`${f.luminance.body_bg_hex}\`, Hero \`${f.luminance.hero_bg_hex}\` | **Regel 1 (Polaritaets-Entscheid):**<br>${pol.reason} | • **\`target_hero_polarity: "${pol.target_hero_polarity}"\`**<br>• **\`target_page_polarity: "${pol.target_page_polarity}"\`**<br>• Sensor **\`S-27 (P1_EVOLUTION_POLARITY_MISMATCH)\`** prueft bei jedem Build automatisch die Hero-Luminanz (\`${pol.target_hero_polarity === 'light' ? '>= 0.45 Pflicht!' : 'Dunkle Buehne erlaubt'}\`). |
| **Hintergrund-Toenung:**<br>• Ursprungs-Hintergrund \`${f.luminance.body_bg_hex}\`<br>• Primaer-Farbton \`H = ${tn.brand_hue_deg}deg\` | **Regel 2 (Tinted Neutrals nach *impeccable* & *Refactoring UI*):**<br>Statt kaltem Spital-Weiss (\`#FFFFFF\`) oder totem Grau erhalten alle Hintergrund- und Textflaechen einen feinen Hauch des Marken-Farbtons (\`Chroma 0.008–0.025\`). | • \`--bg-page: ${tn.bg_page.hex}\` (\`${tn.bg_page.oklch}\`)<br>• \`--bg-soft: ${tn.bg_soft.hex}\` (\`${tn.bg_soft.oklch}\`)<br>• \`--text-main: ${tn.text_main.hex}\` (Kontrast **\`${tn.text_main.contrast_vs_bg_page}\`** >= 10:1) |
| **Farb-Vielfalt & Harmonie:**<br>• **\`distinct_accent_hues_count = ${f.colors.distinct_accent_hues_count}\`**<br>• Gefundene Akzent-Cluster: ${clusterListStr} | **Regel 3 (${ch.is_multicolor_chaos ? 'Bunter-Kuchen-Zaehmung aktiv!' : '60-30-10 Marken-Harmonie'}):**<br>${ch.sommelier_verdict} | • **10 % Primaer-CTA (\`--primary\`):** \`${ch.primary_10_percent_cta.harmonized_hex}\` (Original: \`${ch.primary_10_percent_cta.original_brand_hex}\`)<br>• **Sekundaer-Farben (\`--accent-palette-1..4\`):** In \`OKLCH\` auf exakt gleiche optische Ruhe (\`L=0.95, C=0.035\` Pastell & \`L=0.48, C=0.13\` Akzent) normalisiert. |
| **Typografie & Geometrie (Auge 3):**<br>• Heading-Font: \`${typo.measured_heading_font}\`<br>• Body-Font: \`${typo.measured_body_font}\`<br>• Gemessene Radien: \`${(f.typography.detected_border_radii_px || []).join('px, ') || '0'}px\` | **Regel 4 (Schrift- & Archetyp-Veredelung):**<br>${typo.legacy_flaw_diagnosis}<br>• Archetyp: **\`${typo.selected_archetype.id}\`** (${typo.selected_archetype.character_note}) | • \`--font-display: ${typo.selected_archetype.font_display}\`<br>• \`--font-sans: ${typo.selected_archetype.font_sans}\`<br>• Strikte 2-Radius-Architektur (\`4px\` Badges, \`8px\` Cards/Buttons, \`1100px\` Schweizer Fluchtlinie \`#UI-02\`). |
| **Bildqualitaet & Aufloesung (Auge 3):**<br>• Inhalts-Bilder: **\`${f.images.content_images_count}\`** (max. Breite: **\`${f.images.max_image_width_px}px\`**)<br>• Hi-Res (\`>=1100px\`): \`${f.images.hi_res_images_count}\` \| Low-Res (\`<900px\`): \`${f.images.low_res_images_count}\`<br>• Hochformat-Anteil: \`${Math.round((f.images.portrait_ratio_share || 0) * 100)} %\` | **Regel 5 (Bild-Schutz-Regel):**<br>${img.sommelier_verdict} | • **\`recommended_hero_layout: "${img.recommended_hero_layout}"\`**<br>• \`forbid_fullscreen_bg_image: ${img.forbid_fullscreen_bg_image}\`<br>• Im 2-Spalten-Hero gilt zwingend **Bottom-Edge Baseline Lock (\`#UI-02\`, Sensor \`S-23\`)**. |
| **Sektions-Abfolge der Ursprungsseite:**<br>${secSeqStr} | **Struktur-Seele bewahren & mit ACP-Bruecken veredeln:**<br>Die vertraute Informations-Reihenfolge des Kunden bleibt erhalten und wird um die zwei verkaufspsychologischen ACP-Sektionen (\`social-media\` & \`blog\`) ergaenzt. | • Startseite folgt der gewachsenen Dramaturgie + \`data-section="social-media"\` + \`data-section="blog"\`. |

---

## 2. OKLCH Multi-Color Harmonizer Tabelle (\`60-30-10\` Farb-Architektur)

| Palette-Rolle | Ursprungs-Farbe (Gemessen) | Veredelte Pastell-Kachel (\`L=0.95, C=0.035\`) | Veredelter Icon-/Badge-Akzent (\`L=0.48, C=0.13\`) |
|---|---|---|---|
| **Primaer-Markenfarbe (10 % CTA-Chef)** | \`${ch.primary_10_percent_cta.original_brand_hex}\` (\`H=${ch.primary_10_percent_cta.original_oklch.H}deg\`) | \`${tn.bg_soft.hex}\` (\`${tn.bg_soft.oklch}\`) | **\`${ch.primary_10_percent_cta.harmonized_hex}\`** (\`${ch.primary_10_percent_cta.harmonized_oklch}\`) |
${secondaryRows}

---

## 3. Verbindlicher CSS \`:root\` Token-Block fuer \`build_${dna.slug.replace(/-/g, '_')}_site.py\`

\`\`\`css
/* Google Fonts Import fuer Archetyp "${typo.selected_archetype.id}":
   @import url('${typo.selected_archetype.google_fonts_import}');
*/
${dna.stage_3_blueprint.css_root_tokens}
\`\`\`
`;

  // #LANG-01 Guard: 0x Eszett
  return report.replace(/\u00df/g, 'ss').replace(/\u1e9e/g, 'SS');
}

// ============================================================================
// LOKALER FALLBACK-SERVER & PROFIL-KATALOG FUER BESTEHENDE SHOWCASES
// ============================================================================

const KNOWN_SHOWCASE_CATALOG = [
  {
    slug: 'herzensarbeit',
    url: 'https://herzensarbeit.ch',
    design_mode: 'evolution',
    industry: 'Paartherapie, Eheberatung, Trennungs- & Trauerbegleitung, Frauen-Workshops',
    fallback_brand_hex: '#9A1536'
  },
  {
    slug: 'joma',
    url: 'https://www.joma-solar.ch/',
    design_mode: 'evolution',
    industry: 'Solaranlagen, Photovoltaik, Batteriespeicher & Energietechnik',
    fallback_brand_hex: '#D64B13'
  },
  {
    slug: 'imp-marketing',
    url: '',
    design_mode: 'redesign',
    industry: 'Schreinerei, Holzbau & Digital-Marketing',
    fallback_brand_hex: '#C88A36'
  },
  {
    slug: 'frees',
    url: 'https://www.frees.ch',
    design_mode: 'evolution',
    industry: 'Textildruck, Stickerei, Arbeitskleidung & Teamsport',
    fallback_brand_hex: '#0284C7'
  },
  {
    slug: 'innere-staerke',
    url: 'https://www.innere-staerke.business',
    design_mode: 'evolution',
    industry: 'Executive Coaching, Fuehrungsentwicklung & Mentaltraining',
    fallback_brand_hex: '#D99B26'
  },
  {
    slug: 'fcschlieren',
    url: 'https://fcschlieren.ch',
    design_mode: 'evolution',
    industry: 'Fussballclub, Teamsport & Nachwuchsfoerderung',
    fallback_brand_hex: '#FFDA21'
  },
  {
    slug: 'fcattiswil',
    url: '',
    design_mode: 'evolution',
    industry: 'Fussballclub, Vereinsleben & Sportfoerderung',
    fallback_brand_hex: '#8A1538'
  },
  {
    slug: 'scfulenbach',
    url: 'https://www.scfulenbach.ch',
    design_mode: 'redesign',
    industry: 'Fussballclub, Sportverein & Juniorenfoerderung',
    fallback_brand_hex: '#1D4ED8'
  },
  {
    slug: 'her11',
    url: 'https://www.her11.ch',
    design_mode: 'redesign',
    industry: 'Sportfoerderung, Berufsbildung & Karrierebegleitung im Frauenfussball',
    fallback_brand_hex: '#0F2048'
  },
  {
    slug: 'hochuli',
    url: 'https://www.hochuli-gruppe.ch',
    design_mode: 'evolution',
    industry: 'Holzbau, Zimmerei, Elementbau & Bedachungen',
    fallback_brand_hex: '#B85D19'
  },
  {
    slug: 'hiltbrand',
    url: 'https://hiltbrand.swiss',
    design_mode: 'evolution',
    industry: 'Gebaeudehuellen, Dachdecker, Fassadenbau & Solar',
    fallback_brand_hex: '#D96B27'
  },
  {
    slug: 'birchmeier',
    url: 'https://birchmeier-hohler.ch',
    design_mode: 'evolution',
    industry: 'Sanitaer, Heizung, Haustechnik & Badumbau',
    fallback_brand_hex: '#0284C7'
  }
];

export async function analyzeSiteVisualDna({
  browser,
  url = '',
  slug = 'mandant',
  designMode = 'evolution',
  industry = '',
  fromExistingSite = '',
  rawHtml = '',
  fallbackBrandHex = ''
}) {
  const cleanSlug = String(slug || 'mandant')
    .replace(/^preview-/, '')
    .replace(/-(?:vollversion|vv|v1|v2)$/, '')
    .trim();

  // Read company.json if available to enrich industry/url/brand_color
  const previewDir = path.join(MXS_ROOT, `preview-${cleanSlug}`);
  const previewV2Dir = path.join(MXS_ROOT, `preview-${cleanSlug}-v2`);
  const companyJsonPath = path.join(previewDir, 'company.json');
  if (fs.existsSync(companyJsonPath)) {
    try {
      const cdata = JSON.parse(fs.readFileSync(companyJsonPath, 'utf-8'));
      if (!url && cdata.website) url = cdata.website;
      if (!url && cdata.source_url) url = cdata.source_url;
      if (!industry && cdata.industry) industry = cdata.industry;
      if (!fallbackBrandHex && (cdata.brand_color || cdata.primary_color)) {
        fallbackBrandHex = cdata.brand_color || cdata.primary_color;
      }
    } catch (_) {
      // ignore parse warnings
    }
  }

  const outDir = path.join(VISUAL_DNA_ROOT, cleanSlug);
  fs.mkdirSync(outDir, { recursive: true });

  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  const helperPage = await browser.newPage();

  let loadedTarget = '';
  let loadedOk = false;

  try {
    if (rawHtml) {
      await page.setContent(rawHtml, { waitUntil: 'domcontentloaded' });
      await page.waitForTimeout(200);
      loadedTarget = 'synthetic://raw-html';
      loadedOk = true;
    } else if (fromExistingSite) {
      const candidateHtml = fromExistingSite.endsWith('.html')
        ? path.resolve(fromExistingSite)
        : path.join(path.resolve(fromExistingSite), 'index.html');
      if (fs.existsSync(candidateHtml)) {
        await page.goto('file://' + candidateHtml, { waitUntil: 'domcontentloaded', timeout: 15000 });
        await page.waitForTimeout(300);
        loadedTarget = 'file://' + candidateHtml;
        loadedOk = true;
      }
    }

    if (!loadedOk && url && /^https?:\/\//i.test(url)) {
      try {
        await page.goto(url, { waitUntil: 'networkidle', timeout: 16000 }).catch(async () => {
          await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 12000 });
        });
        await page.waitForTimeout(600);
        loadedTarget = url;
        loadedOk = true;
      } catch (_) {
        loadedOk = false;
      }
    }

    if (!loadedOk) {
      const localIndex = fs.existsSync(path.join(previewDir, 'index.html'))
        ? path.join(previewDir, 'index.html')
        : path.join(previewV2Dir, 'index.html');
      if (fs.existsSync(localIndex)) {
        await page.goto('file://' + localIndex, { waitUntil: 'domcontentloaded', timeout: 12000 });
        await page.waitForTimeout(300);
        loadedTarget = 'file://' + localIndex;
        loadedOk = true;
      } else {
        await page.setContent(
          '<!doctype html><html><body style="background:#ffffff;color:#1e293b;font-family:sans-serif;"><section class="hero"><h1>Mandant Vorschau</h1></section></body></html>'
        );
        loadedTarget = 'fallback://blank';
      }
    }

    // Auge 1: Desktop Screenshot (1440x900)
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.waitForTimeout(120);
    const desktopPngPath = path.join(outDir, 'source_desktop.png');
    const desktopBuf = await page.screenshot({ path: desktopPngPath, type: 'png', fullPage: false });

    // Auge 2 & 3: DOM & Pixel Messung auf Desktop (1440x900)
    const pixelFacts = await measureScreenshotPixelFacts(helperPage, desktopBuf);
    const domFacts = await measureDomVisualFacts(page);

    // Auge 1b: Mobile Screenshot (375x812)
    await page.setViewportSize({ width: 375, height: 812 });
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.waitForTimeout(120);
    const mobilePngPath = path.join(outDir, 'source_mobile.png');
    await page.screenshot({ path: mobilePngPath, type: 'png', fullPage: false });

    // Stufe 2: Design-Sommelier
    const dnaResult = runDesignSommelier({
      slug: cleanSlug,
      sourceUrl: url || loadedTarget,
      designMode,
      industry,
      fallbackBrandHex,
      domFacts,
      pixelFacts
    });

    // Stufe 3: Speichern von source_visual_dna.json & SOURCE_VISUAL_DNA_REPORT.md
    const jsonStr = JSON.stringify(dnaResult, null, 2).replace(/\u00df/g, 'ss') + '\n';
    const jsonPath = path.join(outDir, 'source_visual_dna.json');
    fs.writeFileSync(jsonPath, jsonStr, 'utf-8');

    // Auch in preview-<slug>/ und preview-<slug>-v2/ ablegen, falls vorhanden
    if (fs.existsSync(previewDir) && fs.statSync(previewDir).isDirectory()) {
      fs.writeFileSync(path.join(previewDir, 'source_visual_dna.json'), jsonStr, 'utf-8');
    }
    if (fs.existsSync(previewV2Dir) && fs.statSync(previewV2Dir).isDirectory()) {
      fs.writeFileSync(path.join(previewV2Dir, 'source_visual_dna.json'), jsonStr, 'utf-8');
    }

    const reportMd = renderVisualDnaReportMarkdown(dnaResult);
    const reportPath = path.join(outDir, 'SOURCE_VISUAL_DNA_REPORT.md');
    fs.writeFileSync(reportPath, reportMd, 'utf-8');

    return {
      dna: dnaResult,
      paths: {
        outDir,
        desktopPngPath,
        mobilePngPath,
        jsonPath,
        reportPath
      }
    };
  } finally {
    await page.close();
    await helperPage.close();
  }
}

// ============================================================================
// SYNTHETISCHER SELBSTTEST («5-FARBEN-BUNTER-KUCHEN-TEST» + POLARITAETS-TESTS)
// ============================================================================

async function runSelfTest(browser) {
  const cakeHtml = `<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>Bunter Kuchen KMU Praxis & Coaching</title>
  <style>
    body { background: #FFFFFF; color: #222222; font-family: Arial, "Times New Roman", sans-serif; margin: 0; }
    header { background: #FFFDF9; padding: 20px 40px; border-bottom: 3px solid #E11D48; }
    .hero { background: #FFF9F5; padding: 60px 40px; }
    h1 { color: #E11D48; font-family: "Times New Roman", serif; font-size: 38px; }
    .btn-1 { display: inline-block; padding: 14px 24px; background: #E11D48; color: #FFFFFF; border-radius: 24px; }
    .btn-2 { display: inline-block; padding: 14px 24px; background: #16A34A; color: #FFFFFF; border-radius: 18px; }
    .btn-3 { display: inline-block; padding: 14px 24px; background: #2563EB; color: #FFFFFF; border-radius: 12px; }
    .btn-4 { display: inline-block; padding: 14px 24px; background: #D97706; color: #FFFFFF; border-radius: 6px; }
    .btn-5 { display: inline-block; padding: 14px 24px; background: #9333EA; color: #FFFFFF; border-radius: 4px; }
    .cards { display: flex; gap: 16px; padding: 30px 40px; }
    .card-a { background: #16A34A; color: #fff; padding: 24px; width: 220px; height: 140px; }
    .card-b { background: #2563EB; color: #fff; padding: 24px; width: 220px; height: 140px; }
    .card-c { background: #D97706; color: #fff; padding: 24px; width: 220px; height: 140px; }
    .card-d { background: #9333EA; color: #fff; padding: 24px; width: 220px; height: 140px; }
  </style>
</head>
<body>
  <header><strong>Praxis Bunter Kuchen</strong></header>
  <section class="hero">
    <h1>Willkommen in unserer bunten Praxis fuer Coaching & Begleitung</h1>
    <p>Wir helfen Ihnen im Alltag weiter.</p>
    <div>
      <a class="btn-1" href="#1">Termin buchen</a>
      <a class="btn-2" href="#2">Workshop Gruen</a>
      <a class="btn-3" href="#3">Kurs Blau</a>
      <a class="btn-4" href="#4">Seminar Orange</a>
      <a class="btn-5" href="#5">Coaching Violett</a>
    </div>
    <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='420' height='560'><rect width='420' height='560' fill='%23f3e8ee'/></svg>" width="420" height="560" alt="Portrait">
  </section>
  <section class="cards">
    <div class="card-a">Angebot 1</div>
    <div class="card-b">Angebot 2</div>
    <div class="card-c">Angebot 3</div>
    <div class="card-d">Angebot 4</div>
  </section>
</body>
</html>`;

  const cakeRes = await analyzeSiteVisualDna({
    browser,
    slug: 'bunter-kuchen-test',
    designMode: 'evolution',
    industry: 'Praxis, Coaching & Begleitung',
    rawHtml: cakeHtml
  });

  const d = cakeRes.dna;
  const ch = d.sommelier_decisions.color_harmony_60_30_10;
  const pol = d.sommelier_decisions.polarity_decision;
  const typo = d.sommelier_decisions.typography_and_archetype;
  const img = d.sommelier_decisions.image_layout_decision;

  const checks = [
    {
      name: '5-Farben-Bunter-Kuchen erkannt (distinct_accent_hues_count >= 5)',
      passed: ch.distinct_accent_hues_count >= 5 && ch.is_multicolor_chaos === true,
      detail: `distinct_accent_hues_count=${ch.distinct_accent_hues_count}, is_multicolor_chaos=${ch.is_multicolor_chaos}`
    },
    {
      name: '10 % Primaer-CTA festgelegt + 4 Nebenfarben in OKLCH harmonisiert (L=0.95/C=0.035 & L=0.48/C=0.13)',
      passed:
        Boolean(ch.primary_10_percent_cta.harmonized_hex) &&
        ch.secondary_accent_palette.length === 4 &&
        ch.secondary_accent_palette.every(
          p => p.pastel_surface.oklch.includes('0.950 0.035') && p.icon_accent.oklch.includes('0.480 0.130')
        ),
      detail: `primary=${ch.primary_10_percent_cta.harmonized_hex}, secondary_slots=${ch.secondary_accent_palette.length}`
    },
    {
      name: 'Regel 1 Licht-Sperre erkennt hellen Hero (target_hero_polarity === "light")',
      passed: pol.target_hero_polarity === 'light' && pol.light_lock_active === true,
      detail: `target_hero_polarity=${pol.target_hero_polarity}, hero_lum=${d.stage_1_measured_facts.luminance.hero_luminance}`
    },
    {
      name: 'Regel 4 erkennt Arial/Times New Roman als Alt-Baufehler & waehlt warm_humanist_editorial',
      passed: typo.heal_legacy_flaw === true && typo.selected_archetype.id === 'warm_humanist_editorial',
      detail: `heal_legacy_flaw=${typo.heal_legacy_flaw}, archetype=${typo.selected_archetype.id}`
    },
    {
      name: 'Regel 5 Bild-Schutz erzwingt split_framed_card bei kleinem Hochformat-Bild (420x560px)',
      passed: img.forbid_fullscreen_bg_image === true && img.recommended_hero_layout === 'split_framed_card',
      detail: `max_w=${img.max_source_image_width_px}px, layout=${img.recommended_hero_layout}`
    }
  ];

  const allPassed = checks.every(c => c.passed);
  return { ok: allPassed, checks, report_path: cakeRes.paths.reportPath, json_path: cakeRes.paths.jsonPath };
}

// ============================================================================
// CLI ENTRYPOINT
// ============================================================================

function getArgValue(flag, defaultVal = '') {
  const idx = process.argv.indexOf(flag);
  if (idx !== -1 && process.argv[idx + 1] && !process.argv[idx + 1].startsWith('--')) {
    return process.argv[idx + 1];
  }
  return defaultVal;
}

async function main() {
  const isSelfTest = process.argv.includes('--self-test');
  const isGenerateAll = process.argv.includes('--generate-all-profiles');
  const url = getArgValue('--url', '');
  const slug = getArgValue('--slug', '');
  const designMode = getArgValue('--design-mode', 'evolution');
  const industry = getArgValue('--industry', '');
  const fromExistingSite = getArgValue('--from-existing-site', '');

  const browser = await chromium.launch({ executablePath: getChromiumPath() });
  try {
    if (isSelfTest) {
      const selfRes = await runSelfTest(browser);
      console.log(JSON.stringify(selfRes, null, 2));
      if (!selfRes.ok) process.exit(1);
    }

    if (isGenerateAll) {
      const summary = [];
      for (const item of KNOWN_SHOWCASE_CATALOG) {
        const res = await analyzeSiteVisualDna({
          browser,
          url: item.url,
          slug: item.slug,
          designMode: item.design_mode,
          industry: item.industry,
          fallbackBrandHex: item.fallback_brand_hex
        });
        summary.push({
          slug: item.slug,
          target_hero_polarity: res.dna.sommelier_decisions.polarity_decision.target_hero_polarity,
          archetype: res.dna.sommelier_decisions.typography_and_archetype.selected_archetype.id,
          distinct_hues: res.dna.sommelier_decisions.color_harmony_60_30_10.distinct_accent_hues_count,
          multicolor_tamed: res.dna.sommelier_decisions.color_harmony_60_30_10.is_multicolor_chaos,
          primary_hex: res.dna.sommelier_decisions.color_harmony_60_30_10.primary_10_percent_cta.harmonized_hex,
          hero_layout: res.dna.sommelier_decisions.image_layout_decision.recommended_hero_layout,
          report: res.paths.reportPath
        });
      }
      console.log(JSON.stringify({ ok: true, generated_profiles: summary.length, profiles: summary }, null, 2));
      return;
    }

    if (slug || url || fromExistingSite) {
      const targetSlug = slug || (fromExistingSite ? path.basename(fromExistingSite) : 'mandant');
      const catalogHit = KNOWN_SHOWCASE_CATALOG.find(
        x => x.slug === targetSlug.replace(/^preview-/, '').replace(/-(?:vollversion|vv|v1|v2)$/, '')
      );
      const res = await analyzeSiteVisualDna({
        browser,
        url: url || (catalogHit ? catalogHit.url : ''),
        slug: targetSlug,
        designMode: designMode || (catalogHit ? catalogHit.design_mode : 'evolution'),
        industry: industry || (catalogHit ? catalogHit.industry : ''),
        fromExistingSite,
        fallbackBrandHex: catalogHit ? catalogHit.fallback_brand_hex : ''
      });
      console.log(
        JSON.stringify(
          {
            ok: true,
            slug: res.dna.slug,
            target_hero_polarity: res.dna.sommelier_decisions.polarity_decision.target_hero_polarity,
            target_page_polarity: res.dna.sommelier_decisions.polarity_decision.target_page_polarity,
            archetype: res.dna.sommelier_decisions.typography_and_archetype.selected_archetype.id,
            distinct_accent_hues_count: res.dna.sommelier_decisions.color_harmony_60_30_10.distinct_accent_hues_count,
            multicolor_taming_active: res.dna.sommelier_decisions.color_harmony_60_30_10.is_multicolor_chaos,
            primary_hex: res.dna.sommelier_decisions.color_harmony_60_30_10.primary_10_percent_cta.harmonized_hex,
            recommended_hero_layout: res.dna.sommelier_decisions.image_layout_decision.recommended_hero_layout,
            json_path: res.paths.jsonPath,
            report_path: res.paths.reportPath
          },
          null,
          2
        )
      );
      return;
    }

    if (!isSelfTest) {
      console.error(
        'Usage: node scripts/extract_source_visual_dna.mjs --url <https://...> --slug <slug> [--design-mode evolution|redesign] [--self-test] [--generate-all-profiles]'
      );
      process.exit(1);
    }
  } finally {
    await browser.close();
  }
}

if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch(err => {
    console.error('[FATAL] extract_source_visual_dna.mjs failed:', err);
    process.exit(1);
  });
}

#!/usr/bin/env node
/**
 * audit_webpilot_devices.mjs — Playwright 3-Zonen Device-Maschine & Doppel-Systemaugen (#UI-01, #UI-13, #UI-14)
 * Prueft preview-hochuli/* und webpilot/* ueber alle 3 Geraete-Zonen:
 *   - Zone 1 Smartphone: 375 x 667
 *   - Zone 2 Laptop:     1366 x 768
 *   - Zone 3 Desktop:    1440 x 900
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
const ROOT_DIR = path.resolve(__dirname, '..');

const CHROMIUM_PATHS = [
  '/home/brainuser/.cache/ms-playwright/chromium-1217/chrome-linux64/chrome',
  '/home/brainuser/.cache/ms-playwright/chromium-1217/chrome-linux/chrome',
  '/home/brainuser/.cache/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-linux64/chrome-headless-shell'
];

const PAGES = [
  'preview-hochuli/index.html',
  'preview-hochuli/team.html',
  'preview-hochuli/karriere.html',
  'preview-hochuli/kontakt.html',
  'webpilot/index.html',
  'webpilot/angebot.html',
  'webpilot/ueber-uns.html',
  'webpilot/technologie.html',
  'webpilot/kontakt.html'
];

const ZONES = [
  { name: 'mobile_375x667', width: 375, height: 667 },
  { name: 'laptop_1366x768', width: 1366, height: 768 },
  { name: 'desktop_1440x900', width: 1440, height: 900 }
];

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.woff2': 'font/woff2'
};

function startServer() {
  return new Promise((resolve, reject) => {
    const server = http.createServer((req, res) => {
      try {
        const parsed = new URL(req.url, 'http://127.0.0.1');
        let pathname = decodeURIComponent(parsed.pathname);
        const safePath = path.normalize(path.join(ROOT_DIR, pathname));
        if (!safePath.startsWith(ROOT_DIR) || !fs.existsSync(safePath) || fs.statSync(safePath).isDirectory()) {
          res.writeHead(404);
          res.end('Not found');
          return;
        }
        const ext = path.extname(safePath).toLowerCase();
        res.writeHead(200, {
          'Content-Type': MIME_TYPES[ext] || 'application/octet-stream',
          'Cache-Control': 'no-store'
        });
        fs.createReadStream(safePath).pipe(res);
      } catch (e) {
        res.writeHead(500);
        res.end(String(e));
      }
    });
    server.listen(0, '127.0.0.1', () => {
      resolve({ server, baseUrl: `http://127.0.0.1:${server.address().port}` });
    });
    server.on('error', reject);
  });
}

function getChromium() {
  for (const p of CHROMIUM_PATHS) {
    if (fs.existsSync(p)) return p;
  }
  throw new Error('Chromium binary not found');
}

async function auditPageZone(page, relPage, zone, screenshotDir) {
  await page.setViewportSize({ width: zone.width, height: zone.height });
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(60);

  if (screenshotDir && (relPage === 'preview-hochuli/index.html' || relPage === 'webpilot/index.html') && (zone.width === 375 || zone.width === 1440)) {
    fs.mkdirSync(screenshotDir, { recursive: true });
    const slug = relPage.replace(/\//g, '_').replace('.html', '') + '_' + zone.name + '.png';
    await page.screenshot({ path: path.join(screenshotDir, slug), fullPage: false });
  }

  return await page.evaluate(({ relPage, zone }) => {
    const VW = window.innerWidth;
    const VH = window.innerHeight;
    const findings = [];
    const seen = new Set();

    function addFinding(severity, code, element, selector, details) {
      const k = `${code}::${selector}::${element}`;
      if (seen.has(k)) return;
      seen.add(k);
      findings.push({ page: relPage, zone: zone.name, severity, code, element, selector, details });
    }

    function getCssPath(el) {
      if (!el || el.nodeType !== 1) return 'unknown';
      const parts = [];
      let cur = el;
      let d = 0;
      while (cur && cur.nodeType === 1 && cur !== document.body && d < 5) {
        let name = cur.tagName.toLowerCase();
        if (cur.id) {
          name += '#' + cur.id;
          parts.unshift(name);
          break;
        }
        if (cur.className && typeof cur.className === 'string') {
          const cls = cur.className.trim().split(/\s+/).slice(0, 2).join('.');
          if (cls) name += '.' + cls;
        }
        parts.unshift(name);
        cur = cur.parentElement;
        d++;
      }
      return parts.join(' > ');
    }

    function getLabel(el) {
      if (!el) return '';
      return (
        el.getAttribute('aria-label') ||
        el.innerText ||
        el.textContent ||
        el.getAttribute('placeholder') ||
        el.id ||
        el.tagName
      ).toString().replace(/\s+/g, ' ').trim().slice(0, 65);
    }

    function isVisible(el) {
      if (!el || el.nodeType !== 1) return false;
      if (el.hasAttribute('hidden')) return false;
      let cur = el;
      while (cur && cur.nodeType === 1) {
        const st = window.getComputedStyle(cur);
        if (st.display === 'none' || st.visibility === 'hidden' || parseFloat(st.opacity || '1') <= 0.05) {
          return false;
        }
        cur = cur.parentElement;
      }
      const r = el.getBoundingClientRect();
      return r.width > 2 && r.height > 2;
    }

    function findStickyOrFixedAncestor(node) {
      let cur = node;
      while (cur && cur.nodeType === 1 && cur !== document.body) {
        const st = window.getComputedStyle(cur);
        if (st.position === 'fixed' || st.position === 'sticky') return cur;
        cur = cur.parentElement;
      }
      return null;
    }

    // 1. P1_HORIZONTAL_OVERFLOW
    const docScrollW = document.documentElement.scrollWidth;
    if (docScrollW > VW) {
      addFinding('P1', 'P1_HORIZONTAL_OVERFLOW', 'document.documentElement', 'html', `scrollWidth=${docScrollW}px > innerWidth=${VW}px`);
    }

    // 2. Interactive elements check: P1_OFFSCREEN_X & P2_CRAMPED_MOBILE
    const interactiveEls = Array.from(document.querySelectorAll('a[href], button, input:not([type="hidden"]), select, textarea, [role="button"]')).filter(isVisible);
    for (const el of interactiveEls) {
      const r = el.getBoundingClientRect();
      const lbl = getLabel(el);
      const sel = getCssPath(el);

      if (r.left < 0 || r.right > VW) {
        addFinding('P1', 'P1_OFFSCREEN_X', lbl, sel, `left=${Math.round(r.left)}px, right=${Math.round(r.right)}px (VW=${VW}px)`);
      } else if (VW === 375 && el.closest('.mobile-thumb-bar, .thumb-bar')) {
        if (r.left < 8 || r.right > 367) {
          addFinding('P1', 'P1_OFFSCREEN_X', lbl, sel, `Mobile-Bar Button zu nah am Rand: left=${Math.round(r.left)}px, right=${Math.round(r.right)}px (Pflicht 8..367px)`);
        }
      }

      if (VW < 769) {
        if (r.width < 34 || r.height < 30) {
          addFinding('P2', 'P2_CRAMPED_MOBILE', lbl, sel, `Touch-Fläche zu klein auf Mobile: ${Math.round(r.width)}x${Math.round(r.height)}px (Pflicht >= 34x30px)`);
        }
      }
    }

    // 3. P1_ELEMENT_COLLISION
    const collisionItems = interactiveEls.map(el => ({
      el,
      rect: el.getBoundingClientRect(),
      stickyAnc: findStickyOrFixedAncestor(el)
    }));
    for (let i = 0; i < collisionItems.length; i++) {
      const A = collisionItems[i];
      for (let j = i + 1; j < collisionItems.length; j++) {
        const B = collisionItems[j];
        if (A.el.contains(B.el) || B.el.contains(A.el)) continue;
        if (A.stickyAnc !== B.stickyAnc) continue;
        const overlapW = Math.min(A.rect.right, B.rect.right) - Math.max(A.rect.left, B.rect.left);
        const overlapH = Math.min(A.rect.bottom, B.rect.bottom) - Math.max(A.rect.top, B.rect.top);
        if (overlapW > 4 && overlapH > 4) {
          addFinding('P1', 'P1_ELEMENT_COLLISION', `${getLabel(A.el)} vs ${getLabel(B.el)}`, getCssPath(A.el), `Overlap ${Math.round(overlapW)}x${Math.round(overlapH)}px`);
        }
      }
    }

    // 4. P1_MID_SCREEN_SCROLLBAR (Desktop / Laptop)
    if (VW >= 769) {
      const allEls = Array.from(document.body.querySelectorAll('*')).filter(isVisible);
      for (const el of allEls) {
        const st = window.getComputedStyle(el);
        if ((st.overflowY === 'auto' || st.overflowY === 'scroll') && el.scrollHeight > el.clientHeight + 4) {
          addFinding('P1', 'P1_MID_SCREEN_SCROLLBAR', getLabel(el), getCssPath(el), `scrollHeight=${el.scrollHeight} > clientHeight=${el.clientHeight}`);
        }
      }
    }

    // 5. P2_EMOJI_IN_UI & Checkmarks (✓, ✔, ❌, ✅, Unicode Emojis) + 2-Radius-Architektur (#UI-01)
    const emojiRe = /[\u{1F1E6}-\u{1F1FF}\u{1F300}-\u{1FAFF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}\u{231A}-\u{23F3}\u2713\u2714\u2717\u2718]/u;
    const allDom = Array.from(document.body.querySelectorAll('*')).filter(isVisible);
    for (const el of allDom) {
      if (el.tagName === 'SCRIPT' || el.tagName === 'STYLE' || el.tagName === 'SVG' || el.closest('svg')) continue;
      const directText = Array.from(el.childNodes)
        .filter(n => n.nodeType === 3)
        .map(n => n.nodeValue || '')
        .join(' ')
        .trim();
      if (directText && emojiRe.test(directText)) {
        const m = directText.match(emojiRe);
        addFinding('P2', 'P2_EMOJI_IN_UI', getLabel(el), getCssPath(el), `Unicode-Emoji/Checkmark "${m[0]}" im DOM gefunden`);
      }
      const beforeContent = window.getComputedStyle(el, '::before').content;
      if (beforeContent && beforeContent !== 'none' && emojiRe.test(beforeContent)) {
        const m = beforeContent.match(emojiRe);
        addFinding('P2', 'P2_EMOJI_IN_UI', getLabel(el), getCssPath(el) + '::before', `Unicode-Emoji/Checkmark "${m[0]}" in ::before gefunden`);
      }
      // Check border-radius architecture (#UI-01: only 0px, 4px, 8px)
      const br = window.getComputedStyle(el).borderTopLeftRadius;
      if (br && br !== '0px' && br !== '4px' && br !== '8px') {
        addFinding('P2', 'P2_BAD_RADIUS', getLabel(el), getCssPath(el), `Unerlaubter border-radius=${br} (Pflicht: 4px oder 8px nach #UI-01)`);
      }
    }

    // 6. P2_ROW_HEIGHT_MISMATCH & P2_RAGGED_RIGHT_EDGE in Grids
    const grids = Array.from(document.querySelectorAll('.pillar-cards, .vs-grid, .teaser-grid, .price-grid, .story-grid, .values-grid, .arch-grid, .sparten-filter-grid, .subservices-grid, .sparte-ref-row, .quiz-steps-grid, .social-grid, .blog-grid, .team-dept-grid, .timeline-list')).filter(isVisible);
    for (const g of grids) {
      const children = Array.from(g.children).filter(isVisible);
      if (children.length < 2) continue;
      const rows = [];
      for (const c of children) {
        const r = c.getBoundingClientRect();
        let row = rows.find(rw => Math.abs(rw.top - r.top) <= 10);
        if (!row) {
          row = { top: r.top, items: [] };
          rows.push(row);
        }
        row.items.push({ el: c, rect: r });
      }
      const gRect = g.getBoundingClientRect();
      const gPadR = parseFloat(window.getComputedStyle(g).paddingRight || '0') || 0;
      const expectedRight = gRect.right - gPadR;
      for (const rw of rows) {
        rw.items.sort((a, b) => a.rect.left - b.rect.left);
        const lastItem = rw.items[rw.items.length - 1];
        if (expectedRight - lastItem.rect.right > 14) {
          addFinding('P2', 'P2_RAGGED_RIGHT_EDGE', getCssPath(g), getCssPath(g), `Rechte Kante ausgefranst: last.right=${Math.round(lastItem.rect.right)}px vs container.right=${Math.round(expectedRight)}px`);
        }
        if (rw.items.length >= 2) {
          const heights = rw.items.map(i => i.rect.height);
          const maxH = Math.max(...heights);
          const minH = Math.min(...heights);
          if (maxH - minH > 4) {
            addFinding('P2', 'P2_ROW_HEIGHT_MISMATCH', getCssPath(g), getCssPath(g), `Karten in derselben Zeile haben ungleiche Höhe: min=${Math.round(minH)}px vs max=${Math.round(maxH)}px`);
          }
        }
      }
    }

    // 7. P1_STICKY_OCCLUDES_FOOTER & P1_PARTIALLY_OCCLUDED_BY_STICKY (Mobile)
    if (VW < 769) {
      const stickyBar = document.querySelector('.mobile-thumb-bar, .thumb-bar');
      const footer = document.querySelector('footer');
      if (stickyBar && isVisible(stickyBar) && footer && isVisible(footer)) {
        // Test default window.scrollTo(0, document.documentElement.scrollHeight) without instant to catch smooth-scroll traps
        window.scrollTo(0, document.documentElement.scrollHeight);
        const sRect = stickyBar.getBoundingClientRect();
        const fRect = footer.getBoundingClientRect();
        if (fRect.bottom > sRect.top - 4) {
          addFinding(
            'P1',
            'P1_STICKY_OCCLUDES_FOOTER',
            'footer',
            getCssPath(footer),
            `Footer wird am unteren Seitenende von Sticky-Bar verdeckt: footer.bottom=${Math.round(fRect.bottom)}px > sticky.top-4=${Math.round(sRect.top - 4)}px (scrollY=${Math.round(window.scrollY)})`
          );
        }
        // Also check lowest interactive element inside footer or page
        const footerLinks = Array.from(footer.querySelectorAll('a[href], button')).filter(isVisible);
        for (const fl of footerLinks) {
          const flr = fl.getBoundingClientRect();
          if (flr.bottom > sRect.top - 4) {
            addFinding(
              'P1',
              'P1_PARTIALLY_OCCLUDED_BY_STICKY',
              getLabel(fl),
              getCssPath(fl),
              `Footer-Link bei Max-Scroll unter Sticky-Bar: link.bottom=${Math.round(flr.bottom)}px > sticky.top-4=${Math.round(sRect.top - 4)}px`
            );
          }
        }
      }
      window.scrollTo(0, 0);
    }

    return findings;
  }, { relPage, zone });
}

async function main() {
  const { server, baseUrl } = await startServer();
  const browser = await chromium.launch({ executablePath: getChromium() });
  const page = await browser.newPage();
  const allFindings = [];
  const screenshotDir = process.argv.includes('--screenshots') ? '/tmp/webpilot_device_screenshots' : null;

  for (const relPage of PAGES) {
    await page.goto(`${baseUrl}/${relPage}`, { waitUntil: 'networkidle' });
    for (const zone of ZONES) {
      const f = await auditPageZone(page, relPage, zone, screenshotDir);
      allFindings.push(...f);
    }
  }

  await browser.close();
  server.close();

  const p1 = allFindings.filter(f => f.severity === 'P1');
  const p2 = allFindings.filter(f => f.severity === 'P2');
  console.log(`=== DEVICE-MASCHINE AUDIT: ${PAGES.length} Pages x ${ZONES.length} Zones (${PAGES.length * ZONES.length} Views) ===`);
  console.log(`P1 Findings: ${p1.length} | P2 Findings: ${p2.length}`);
  for (const f of allFindings) {
    console.log(`[${f.severity}] [${f.code}] ${f.page} (${f.zone}) :: ${f.selector} ("${f.element}") -> ${f.details}`);
  }
  if (p1.length > 0 || p2.length > 0) {
    process.exit(1);
  }
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});

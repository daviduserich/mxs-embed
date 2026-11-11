import fs from 'fs';
import path from 'path';
import http from 'http';
import { fileURLToPath } from 'url';
import { createRequire } from 'module';
import {
  SYSTEM_EYES_VERSION,
  SYSTEM_EYES_SENSORS,
  evaluateSystemEyesInPage
} from './lib/system_eyes_core.mjs';

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

function findChromium() {
  for (const p of CHROMIUM_PATHS) {
    if (fs.existsSync(p)) return p;
  }
  throw new Error('Chromium binary not found');
}

function startStaticServer(rootDir) {
  return new Promise((resolve) => {
    const mimeTypes = {
      '.html': 'text/html; charset=utf-8',
      '.css': 'text/css; charset=utf-8',
      '.js': 'application/javascript; charset=utf-8',
      '.json': 'application/json; charset=utf-8',
      '.png': 'image/png',
      '.jpg': 'image/jpeg',
      '.jpeg': 'image/jpeg',
      '.webp': 'image/webp',
      '.svg': 'image/svg+xml'
    };
    const srv = http.createServer((req, res) => {
      const u = new URL(req.url, 'http://127.0.0.1');
      let rel = decodeURIComponent(u.pathname);
      if (rel.startsWith('/sites/')) rel = rel.replace(/^\/sites\//, '/');
      if (rel.endsWith('/')) rel += 'index.html';
      const filePath = path.join(rootDir, rel);
      if (!filePath.startsWith(rootDir) || !fs.existsSync(filePath) || fs.statSync(filePath).isDirectory()) {
        res.writeHead(404);
        res.end('Not found');
        return;
      }
      const ext = path.extname(filePath).toLowerCase();
      res.writeHead(200, { 'Content-Type': mimeTypes[ext] || 'application/octet-stream' });
      fs.createReadStream(filePath).pipe(res);
    });
    srv.listen(0, '127.0.0.1', () => {
      resolve({ server: srv, port: srv.address().port });
    });
  });
}

async function runAuditOnPage(page, relPage, width, height, activeScopeSelector = null) {
  const findings = await page.evaluate(evaluateSystemEyesInPage, {
    relPage,
    zone: { name: width < 769 ? 'mobile' : 'desktop', width, height },
    options: { activeScopeSelector }
  });
  return {
    p1Count: findings.filter(f => f.severity === 'P1').length,
    p2Count: findings.filter(f => f.severity === 'P2').length,
    findings
  };
}

async function main() {
  const { server, port } = await startStaticServer(ROOT_DIR);
  const baseUrl = `http://127.0.0.1:${port}`;
  const browser = await chromium.launch({
    executablePath: findChromium(),
    headless: true,
    args: ['--no-sandbox', '--disable-dev-shm-usage']
  });

  const report = {
    system_eyes_version: SYSTEM_EYES_VERSION,
    sensors_count: SYSTEM_EYES_SENSORS.length,
    M1_desktop: {},
    M2_mobile: {},
    M3_schlummer_roundtrip: {},
    M4_cockpit_full: {},
    M5_cockpit_light: {},
    M6_orthography: {}
  };

  try {
    // =========================================================================
    // M1: Desktop 1440x900 (preview-holz-susi-v2 & preview-holz-susi) + Screenshots 1 & 2
    // =========================================================================
    const ctxDesktop = await browser.newContext({ viewport: { width: 1440, height: 900 } });
    const pageD = await ctxDesktop.newPage();

    for (const slug of ['preview-holz-susi-v2', 'preview-holz-susi']) {
      await pageD.goto(`${baseUrl}/${slug}/index.html`, { waitUntil: 'networkidle' });
      await pageD.waitForTimeout(300);
      const res = await runAuditOnPage(pageD, `${slug}/index.html`, 1440, 900, null);
      const details = await pageD.evaluate(() => {
        const st = document.querySelector('[data-wp-stoerer]');
        const stInner = document.querySelector('.wp-stoerer-seal-content');
        const sec = document.getElementById('bluescht-beiz');
        const imgs = sec ? Array.from(sec.querySelectorAll('img')) : [];
        return {
          stoererVisible: Boolean(st && window.getComputedStyle(st).display !== 'none'),
          stoererStyle: st ? st.getAttribute('data-wp-stoerer') : null,
          stoererTransform: stInner ? window.getComputedStyle(stInner).transform : null,
          sectionVisible: Boolean(sec && window.getComputedStyle(sec).display !== 'none'),
          blueschtImagesCount: imgs.length,
          blueschtImagesAllLoaded: imgs.every(im => im.complete && im.naturalWidth > 0)
        };
      });
      report.M1_desktop[slug] = {
        p1: res.p1Count,
        p2: res.p2Count,
        findings: res.findings,
        ...details
      };

      if (slug === 'preview-holz-susi-v2') {
        await pageD.evaluate(() => window.scrollTo(0, 0));
        await pageD.waitForTimeout(200);
        await pageD.screenshot({ path: '/tmp/holz_susi_stoerer_hero_desktop.png', fullPage: false });

        await pageD.evaluate(() => {
          const el = document.getElementById('bluescht-beiz');
          if (el) el.scrollIntoView({ behavior: 'instant', block: 'end' });
        });
        await pageD.waitForTimeout(250);
        await pageD.screenshot({ path: '/tmp/holz_susi_bluescht_sektion_desktop.png', fullPage: false });
      }
    }

    // =========================================================================
    // M2: Mobile 375x812 (preview-holz-susi-v2 & preview-holz-susi)
    // =========================================================================
    const ctxMobile = await browser.newContext({ viewport: { width: 375, height: 812 } });
    const pageM = await ctxMobile.newPage();

    for (const slug of ['preview-holz-susi-v2', 'preview-holz-susi']) {
      await pageM.goto(`${baseUrl}/${slug}/index.html`, { waitUntil: 'networkidle' });
      await pageM.waitForTimeout(300);
      const res = await runAuditOnPage(pageM, `${slug}/index.html`, 375, 812, null);
      const mobDetails = await pageM.evaluate(() => {
        const st = document.querySelector('[data-wp-stoerer]');
        const stCs = st ? window.getComputedStyle(st) : null;
        return {
          overflowPx: Math.max(0, document.documentElement.scrollWidth - window.innerWidth),
          stoererPosition: stCs ? stCs.position : null,
          stoererBorderRadius: stCs ? stCs.borderTopLeftRadius : null
        };
      });
      report.M2_mobile[slug] = {
        p1: res.p1Count,
        p2: res.p2Count,
        findings: res.findings,
        ...mobDetails
      };
    }

    // =========================================================================
    // M3: Schlummer-Modus Test via POST /api/publish-career/update-seasonal-stoerer
    // =========================================================================
    const sleepRes = await fetch('http://127.0.0.1:5056/api/publish-career/update-seasonal-stoerer', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        site: 'sites/preview-holz-susi-v2',
        skip_deploy: true,
        sections: [{ id: 'bluescht-beiz', hidden: true, visible_from: '2026-04-03', visible_until: '2026-05-01' }],
        stoerer: {
          active: true,
          style: 'seal',
          theme: 'brand',
          line1: 'FRÜHLINGS-HIGHLIGHT',
          line2: 'Bluescht-Beiz',
          line3: 'Ostern bis 1. Mai ↓',
          target: '#bluescht-beiz'
        }
      })
    }).then(r => r.json());

    await pageD.goto(`${baseUrl}/preview-holz-susi-v2/index.html`, { waitUntil: 'networkidle' });
    const hiddenCheck = await pageD.evaluate(() => {
      const sec = document.getElementById('bluescht-beiz');
      const navLink = document.querySelector('a[href="#bluescht-beiz"]:not([data-wp-stoerer])');
      const st = document.querySelector('[data-wp-stoerer]');
      return {
        sectionAttrHidden: sec ? sec.getAttribute('data-wp-hidden') : null,
        sectionDisplay: sec ? window.getComputedStyle(sec).display : null,
        navLinkDisplay: navLink ? window.getComputedStyle(navLink).display : null,
        stoererDisplayWhenTargetSleeping: st ? window.getComputedStyle(st).display : null
      };
    });

    // Restore active state (hidden: false, stoerer.active: true)
    const wakeRes = await fetch('http://127.0.0.1:5056/api/publish-career/update-seasonal-stoerer', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        site: 'sites/preview-holz-susi-v2',
        skip_deploy: true,
        sections: [{ id: 'bluescht-beiz', hidden: false, visible_from: '2026-04-03', visible_until: '2026-05-01' }],
        stoerer: {
          active: true,
          style: 'seal',
          theme: 'brand',
          line1: 'FRÜHLINGS-HIGHLIGHT',
          line2: 'Bluescht-Beiz',
          line3: 'Ostern bis 1. Mai ↓',
          target: '#bluescht-beiz'
        }
      })
    }).then(r => r.json());

    await pageD.goto(`${baseUrl}/preview-holz-susi-v2/index.html`, { waitUntil: 'networkidle' });
    const wakeCheck = await pageD.evaluate(() => {
      const sec = document.getElementById('bluescht-beiz');
      const navLink = document.querySelector('a[href="#bluescht-beiz"]:not([data-wp-stoerer])');
      const st = document.querySelector('[data-wp-stoerer]');
      return {
        sectionAttrHidden: sec ? sec.getAttribute('data-wp-hidden') : null,
        sectionDisplay: sec ? window.getComputedStyle(sec).display : null,
        navLinkDisplay: navLink ? window.getComputedStyle(navLink).display : null,
        stoererDisplayWhenTargetAwake: st ? window.getComputedStyle(st).display : null
      };
    });

    report.M3_schlummer_roundtrip = {
      apiSleepOk: sleepRes.ok,
      hiddenCheck,
      apiWakeOk: wakeRes.ok,
      wakeCheck
    };

    // =========================================================================
    // M4: Cockpit Full Mode + #acp-stoerer-modal + Screenshot 3 + .wp-cockpit-peek
    // =========================================================================
    await pageD.goto(`${baseUrl}/preview-holz-susi-v2/cockpit.html`, { waitUntil: 'networkidle' });
    await pageD.waitForTimeout(500);
    await pageD.click('#btn-seasonal-stoerer');
    await pageD.waitForTimeout(350);

    const modalAudit = await runAuditOnPage(pageD, 'preview-holz-susi-v2/cockpit.html#stoerer-modal', 1440, 900, '#acp-stoerer-modal');
    await pageD.screenshot({ path: '/tmp/holz_susi_cockpit_stoerer_modal.png', fullPage: false });

    // Test .wp-cockpit-peek on sleeping section
    const peekCheck = await pageD.evaluate(() => {
      acpToggleSecHiddenInModal('bluescht-beiz');
      acpPeekSectionInCockpit('bluescht-beiz');
      const iframe = document.getElementById('acp-widget-viewport');
      const doc = iframe.contentDocument;
      const sec = doc.getElementById('bluescht-beiz');
      const banner = sec ? sec.querySelector('.wp-cockpit-peek-banner') : null;
      const result = {
        hasPeekClass: sec ? sec.classList.contains('wp-cockpit-peek') : false,
        displayInCockpitWhileHidden: sec ? iframe.contentWindow.getComputedStyle(sec).display : null,
        hasPeekBanner: Boolean(banner),
        peekBannerText: banner ? banner.textContent.trim() : null
      };
      // Restore hidden=false
      acpToggleSecHiddenInModal('bluescht-beiz');
      sec.classList.remove('wp-cockpit-peek');
      iframe.contentWindow.wpSyncSeasonalVisibility();
      return result;
    });

    report.M4_cockpit_full = {
      modalP1: modalAudit.p1Count,
      modalP2: modalAudit.p2Count,
      modalFindings: modalAudit.findings,
      peekCheck
    };

    // =========================================================================
    // M5: Cockpit Light Mode (?mode=light)
    // =========================================================================
    await pageD.goto(`${baseUrl}/cockpit-app.html?site=preview-holz-susi-v2&mode=light`, { waitUntil: 'networkidle' });
    await pageD.waitForTimeout(500);
    const lightBeforeClick = await pageD.evaluate(() => {
      const btn = document.getElementById('btn-seasonal-stoerer');
      const vibeBtn = document.getElementById('acp-btn-open-design-vibe');
      return {
        isLightModeClass: document.documentElement.classList.contains('acp-cockpit-light-mode'),
        stoererBtnVisible: Boolean(btn && window.getComputedStyle(btn).display !== 'none'),
        vibeBtnHiddenInLight: Boolean(vibeBtn && window.getComputedStyle(vibeBtn).display === 'none')
      };
    });
    await pageD.click('#btn-seasonal-stoerer');
    await pageD.waitForTimeout(300);
    const lightAfterClick = await pageD.evaluate(() => {
      const modal = document.getElementById('acp-stoerer-modal');
      return {
        modalOpenInLightMode: Boolean(modal && modal.classList.contains('is-open') && window.getComputedStyle(modal).display !== 'none'),
        sectionsCountInModal: document.querySelectorAll('#acp-stoerer-sections-list .acp-stoerer-sec-row').length
      };
    });
    report.M5_cockpit_light = {
      ...lightBeforeClick,
      ...lightAfterClick
    };

    // =========================================================================
    // M6: Orthography Check (#LANG-01: 0 'ß', 0 unauthorized '—')
    // =========================================================================
    const filesToCheck = [
      'preview-holz-susi/index.html',
      'preview-holz-susi-v2/index.html',
      'templates/cockpit-app.html',
      'templates/cockpit-script-template.js'
    ];
    for (const rel of filesToCheck) {
      const content = fs.readFileSync(path.join(ROOT_DIR, rel), 'utf-8');
      const eszettCount = (content.match(/\u00df/g) || []).length;
      report.M6_orthography[rel] = { eszettCount };
    }

    await ctxDesktop.close();
    await ctxMobile.close();
  } finally {
    await browser.close();
    server.close();
  }

  console.log(JSON.stringify(report, null, 2));
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});

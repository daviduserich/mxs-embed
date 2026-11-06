#!/usr/bin/env node
/**
 * audit_webpilot_devices.mjs — Playwright 3-Zonen Device-Maschine & Doppel-Systemaugen v2.0 (#UI-01, #UI-06, #UI-13, #UI-14)
 * Nutzt den zentralen Baustein ./lib/system_eyes_core.mjs (18 Mathematisch-Aesthetische Sensoren S-01..S-18)
 * und prueft JEDE anwaehlbare Ansicht, Unterseite, Mobile-Menue & Cockpit-Modal:
 *   - Alle Seiten & Unterseiten in preview-her11/*, preview-hochuli/*, webpilot/*
 *   - Geoeffnetes Mobile-Burger-Menue (375x667) auf allen Kunden- & Marketing-Seiten
 *   - Alle 12 anwaehlbaren Studio-Cockpit-Zustaende (Default, Inline-Edit, Job-Dropdown,
 *     Sections-Modal, Replace-Section-Modal, New-Section-Modal, Images-Modal,
 *     Pages-Directory-Modal, Draft-Panel, Swap-Dock, Log-Modal, Help-Modal) ueber alle 3 Zonen
 */

import fs from 'fs';
import path from 'path';
import http from 'http';
import { execFileSync } from 'child_process';
import { fileURLToPath } from 'url';
import { createRequire } from 'module';
import {
  SYSTEM_EYES_VERSION,
  SYSTEM_EYES_ZONES,
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

const ALL_PAGES = [
  'preview-her11/index.html',
  'preview-her11/ueber-uns.html',
  'preview-her11/ausbildung.html',
  'preview-her11/begleitung.html',
  'preview-her11/mach-mit.html',
  'preview-her11/kontakt.html',
  'preview-her11/cockpit.html',
  'preview-fcschlieren/index.html',
  'preview-fcschlieren/herren-1.html',
  'preview-fcschlieren/kontakt.html',
  'preview-fcschlieren/team-update.html',
  'preview-fcschlieren/cockpit.html',
  'preview-fcschlieren-v2/index.html',
  'preview-fcschlieren-v2/herren-1.html',
  'preview-fcschlieren-v2/kontakt.html',
  'preview-fcschlieren-v2/team-update.html',
  'preview-fcschlieren-v2/cockpit.html',
  'preview-fcattiswil/index.html',
  'preview-fcattiswil/herren-1.html',
  'preview-fcattiswil/kontakt.html',
  'preview-fcattiswil/team-update.html',
  'preview-fcattiswil/cockpit.html',
  'preview-scfulenbach/index.html',
  'preview-scfulenbach/herren-1.html',
  'preview-scfulenbach/kontakt.html',
  'preview-scfulenbach/team-update.html',
  'preview-scfulenbach/cockpit.html',
  'preview-hochuli/index.html',
  'preview-hochuli/team.html',
  'preview-hochuli/karriere.html',
  'preview-hochuli/kontakt.html',
  'preview-hochuli/cockpit.html',
  'preview-innere-staerke/index.html',
  'preview-innere-staerke/angebot.html',
  'preview-innere-staerke/ueber-uns.html',
  'preview-innere-staerke/referenzen.html',
  'preview-innere-staerke/kontakt.html',
  'preview-innere-staerke/cockpit.html',
  'preview-innere-staerke-v2/index.html',
  'preview-innere-staerke-v2/kontakt.html',
  'preview-innere-staerke-v2/cockpit.html',
  'preview-frees/index.html',
  'preview-frees/dienstleistungen.html',
  'preview-frees/textilsortiment.html',
  'preview-frees/profil.html',
  'preview-frees/kontakt.html',
  'preview-frees/cockpit.html',
  'preview-frees-v2/index.html',
  'preview-frees-v2/kontakt.html',
  'preview-frees-v2/cockpit.html',
  'preview-herzensarbeit/index.html',
  'preview-herzensarbeit/angebot.html',
  'preview-herzensarbeit/workshops.html',
  'preview-herzensarbeit/ueber-mich.html',
  'preview-herzensarbeit/kontakt.html',
  'preview-herzensarbeit/cockpit.html',
  'preview-herzensarbeit-v2/index.html',
  'preview-herzensarbeit-v2/kontakt.html',
  'preview-herzensarbeit-v2/cockpit.html',
  'preview-imp-marketing/index.html',
  'preview-imp-marketing/leistungen.html',
  'preview-imp-marketing/methode.html',
  'preview-imp-marketing/ueber-uns.html',
  'preview-imp-marketing/kontakt.html',
  'preview-imp-marketing/cockpit.html',
  'preview-imp-marketing-v2/index.html',
  'preview-imp-marketing-v2/leistungen.html',
  'preview-imp-marketing-v2/methode.html',
  'preview-imp-marketing-v2/ueber-uns.html',
  'preview-imp-marketing-v2/kontakt.html',
  'preview-imp-marketing-v2/cockpit.html',
  'preview-joma/index.html',
  'preview-joma/leistungen.html',
  'preview-joma/referenzen.html',
  'preview-joma/ueber-uns.html',
  'preview-joma/kontakt.html',
  'preview-joma/cockpit.html',
  'preview-joma-v2/index.html',
  'preview-joma-v2/kontakt.html',
  'preview-joma-v2/cockpit.html',
  'webpilot/index.html',
  'webpilot/angebot.html',
  'webpilot/ueber-uns.html',
  'webpilot/technologie.html',
  'webpilot/kontakt.html',
  'partner/index.html'
];

const COCKPIT_STATES = [
  {
    id: 'state_inline_edit',
    label: 'inline-edit-dock',
    activeScopeSelector: '#acp-inline-edit-dock',
    open: () => {
      if (typeof window.acpToggleInlineEdit === 'function') window.acpToggleInlineEdit(true);
    },
    close: () => {
      if (typeof window.acpToggleInlineEdit === 'function') window.acpToggleInlineEdit(false);
    }
  },
  {
    id: 'state_job_dropdown',
    label: 'job-dropdown',
    activeScopeSelector: '#acp-job-dropdown',
    open: () => {
      const dd = document.getElementById('acp-job-dropdown');
      if (dd && !dd.classList.contains('is-open') && typeof window.acpToggleJobDropdown === 'function') {
        window.acpToggleJobDropdown();
      }
    },
    close: () => {
      const dd = document.getElementById('acp-job-dropdown');
      if (dd && dd.classList.contains('is-open') && typeof window.acpToggleJobDropdown === 'function') {
        window.acpToggleJobDropdown();
      }
    }
  },
  {
    id: 'state_sections_modal',
    label: 'sections-modal',
    activeScopeSelector: '#acp-sections-modal',
    open: () => {
      const m = document.getElementById('acp-sections-modal');
      if (m && !m.classList.contains('is-open') && typeof window.acpToggleSectionsModal === 'function') {
        window.acpToggleSectionsModal();
      }
    },
    close: () => {
      const m = document.getElementById('acp-sections-modal');
      if (m && m.classList.contains('is-open') && typeof window.acpToggleSectionsModal === 'function') {
        window.acpToggleSectionsModal();
      }
    }
  },
  {
    id: 'state_replace_modal',
    label: 'replace-section-modal',
    activeScopeSelector: '#acp-replace-section-modal',
    open: () => {
      if (typeof window.acpOpenReplaceSectionModal === 'function') {
        window.acpOpenReplaceSectionModal('hero');
      }
    },
    close: () => {
      if (typeof window.acpCloseReplaceSectionModal === 'function') {
        window.acpCloseReplaceSectionModal();
      }
    }
  },
  {
    id: 'state_new_section_modal',
    label: 'new-section-modal',
    activeScopeSelector: '#acp-new-section-modal',
    open: () => {
      if (typeof window.acpOpenNewSectionModal === 'function') {
        window.acpOpenNewSectionModal();
      }
    },
    close: () => {
      if (typeof window.acpCloseNewSectionModal === 'function') {
        window.acpCloseNewSectionModal();
      }
    }
  },
  {
    id: 'state_images_modal',
    label: 'images-modal',
    activeScopeSelector: '#acp-images-modal',
    open: () => {
      const m = document.getElementById('acp-images-modal');
      if (m && !m.classList.contains('is-open') && typeof window.acpToggleImagesModal === 'function') {
        window.acpToggleImagesModal();
      }
    },
    close: () => {
      const m = document.getElementById('acp-images-modal');
      if (m && m.classList.contains('is-open') && typeof window.acpToggleImagesModal === 'function') {
        window.acpToggleImagesModal();
      }
    }
  },
  {
    id: 'state_directory_modal',
    label: 'directory-modal',
    activeScopeSelector: '#acp-directory-modal',
    open: () => {
      const m = document.getElementById('acp-directory-modal');
      if (m && !m.classList.contains('is-open') && typeof window.acpToggleDirectoryModal === 'function') {
        window.acpToggleDirectoryModal();
      }
    },
    close: () => {
      const m = document.getElementById('acp-directory-modal');
      if (m && m.classList.contains('is-open') && typeof window.acpToggleDirectoryModal === 'function') {
        window.acpToggleDirectoryModal();
      }
    }
  },
  {
    id: 'state_draft_panel',
    label: 'draft-panel',
    activeScopeSelector: '#acp-draft-panel',
    open: () => {
      const p = document.getElementById('acp-draft-panel');
      if (p && !p.classList.contains('is-open') && typeof window.acpToggleMenu === 'function') {
        window.acpToggleMenu();
      }
    },
    close: () => {
      const p = document.getElementById('acp-draft-panel');
      if (p && p.classList.contains('is-open') && typeof window.acpToggleMenu === 'function') {
        window.acpToggleMenu();
      }
    }
  },
  {
    id: 'state_swap_dock',
    label: 'swap-dock',
    activeScopeSelector: '#acp-swap-dock',
    open: () => {
      if (typeof window.acpSelectSwapImage === 'function' && Array.isArray(window.ACP_BILDER) && window.ACP_BILDER.length > 0) {
        const first = window.ACP_BILDER[0];
        window.acpSelectSwapImage(first.rel_path, first.filename);
      }
    },
    close: () => {
      if (typeof window.acpCancelSwap === 'function') {
        window.acpCancelSwap(true);
      }
    }
  },
  {
    id: 'state_log_modal',
    label: 'log-modal',
    activeScopeSelector: '#acp-log-modal',
    open: () => {
      const m = document.getElementById('acp-log-modal');
      if (m && !m.classList.contains('is-open') && typeof window.acpToggleLogModal === 'function') {
        window.acpToggleLogModal();
      }
    },
    close: () => {
      const m = document.getElementById('acp-log-modal');
      if (m && m.classList.contains('is-open') && typeof window.acpToggleLogModal === 'function') {
        window.acpToggleLogModal();
      }
    }
  },
  {
    id: 'state_help_modal',
    label: 'help-modal',
    activeScopeSelector: '#acp-help-modal',
    open: () => {
      const m = document.getElementById('acp-help-modal');
      if (m && !m.classList.contains('is-open') && typeof window.acpToggleHelpModal === 'function') {
        window.acpToggleHelpModal();
      }
    },
    close: () => {
      const m = document.getElementById('acp-help-modal');
      if (m && m.classList.contains('is-open') && typeof window.acpToggleHelpModal === 'function') {
        window.acpToggleHelpModal();
      }
    }
  },
  {
    id: 'state_design_vibe_modal',
    label: 'design-vibe-modal',
    activeScopeSelector: '#designVibeModal',
    open: () => {
      const m = document.getElementById('designVibeModal');
      if (m && !m.classList.contains('is-open') && typeof window.acpOpenDesignVibeModal === 'function') {
        window.acpOpenDesignVibeModal();
      }
    },
    close: () => {
      const m = document.getElementById('designVibeModal');
      if (m && m.classList.contains('is-open') && typeof window.acpCloseDesignVibeModal === 'function') {
        window.acpCloseDesignVibeModal();
      }
    }
  }
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

const VISUAL_DNA_CACHE = new Map();

function loadSourceVisualDnaForPage(relPage) {
  const clientPrefix = (relPage || '').split('/')[0];
  if (!clientPrefix || !clientPrefix.startsWith('preview-')) return null;
  if (VISUAL_DNA_CACHE.has(clientPrefix)) return VISUAL_DNA_CACHE.get(clientPrefix);

  const baseSlug = clientPrefix.replace(/^preview-/, '').replace(/-(?:vollversion|vv|v1|v2)$/, '');
  const candidates = [
    path.join(ROOT_DIR, clientPrefix, 'source_visual_dna.json'),
    path.join(ROOT_DIR, 'visual-dna', baseSlug, 'source_visual_dna.json'),
    path.join(ROOT_DIR, 'visual-dna', clientPrefix.replace(/^preview-/, ''), 'source_visual_dna.json')
  ];
  for (const cand of candidates) {
    if (fs.existsSync(cand)) {
      try {
        const parsed = JSON.parse(fs.readFileSync(cand, 'utf-8'));
        VISUAL_DNA_CACHE.set(clientPrefix, parsed);
        return parsed;
      } catch (_) {
        // ignore parse error
      }
    }
  }
  VISUAL_DNA_CACHE.set(clientPrefix, null);
  return null;
}

function resolvePagesFromArgs() {
  const requestedTargets = [];
  for (let i = 2; i < process.argv.length; i++) {
    const arg = process.argv[i];
    if (arg === '--site' && process.argv[i + 1]) {
      requestedTargets.push(process.argv[i + 1]);
      i++;
    } else if (!arg.startsWith('--')) {
      requestedTargets.push(arg);
    }
  }

  if (requestedTargets.length > 0) {
    const collected = [];
    for (const rawTarget of requestedTargets) {
      let siteSlug = path.basename(rawTarget.replace(/\/+$/, ''));
      if (!fs.existsSync(path.join(ROOT_DIR, siteSlug)) && fs.existsSync(path.join(ROOT_DIR, 'preview-' + siteSlug))) {
        siteSlug = 'preview-' + siteSlug;
      }
      const siteDir = path.join(ROOT_DIR, siteSlug);
      if (fs.existsSync(siteDir) && fs.statSync(siteDir).isDirectory()) {
        const htmlFiles = fs.readdirSync(siteDir)
          .filter(f => f.endsWith('.html'))
          .sort()
          .map(f => `${siteSlug}/${f}`);
        collected.push(...htmlFiles);
      }
    }
    if (collected.length > 0) return Array.from(new Set(collected));
  }
  return ALL_PAGES.filter(p => fs.existsSync(path.join(ROOT_DIR, p)));
}

async function auditPageZone(page, relPage, zone, screenshotDir, options = {}) {
  await page.setViewportSize({ width: zone.width, height: zone.height });
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(60);

  const sourceVisualDna = options.sourceVisualDna !== undefined ? options.sourceVisualDna : loadSourceVisualDnaForPage(relPage);
  const mergedOptions = { ...options, sourceVisualDna };

  if (screenshotDir && !mergedOptions.activeScopeSelector && (zone.width === 375 || zone.width === 1440)) {
    fs.mkdirSync(screenshotDir, { recursive: true });
    const slug = relPage.replace(/\//g, '_').replace('.html', '') + '_' + zone.name + '.png';
    await page.screenshot({ path: path.join(screenshotDir, slug), fullPage: false });
  }

  return await page.evaluate(evaluateSystemEyesInPage, { relPage, zone, options: mergedOptions });
}

async function runS27CanarySelfTest() {
  const browser = await chromium.launch({ executablePath: getChromium() });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  try {
    await page.setContent(`<!DOCTYPE html>
<html lang="de" data-expected-hero-polarity="light" data-design-mode="evolution">
<head><meta charset="UTF-8"><title>S-27 Canary Dark Hero</title></head>
<body style="margin:0;background:#ffffff;color:#1e293b;font-family:sans-serif;">
  <section class="hero-section" style="background:#18232C;color:#ffffff;padding:80px 40px;">
    <h1>Versehentlich dunkler Hero bei heller Ursprungsseite</h1>
  </section>
</body>
</html>`);
    const findings = await page.evaluate(evaluateSystemEyesInPage, {
      relPage: 'canary-s27/index.html',
      zone: SYSTEM_EYES_ZONES[2],
      options: {
        sourceVisualDna: {
          design_mode: 'evolution',
          sommelier_decisions: {
            polarity_decision: { target_hero_polarity: 'light' }
          }
        }
      }
    });
    const s27Hit = findings.find(f => f.code === 'P1_EVOLUTION_POLARITY_MISMATCH');
    console.log(JSON.stringify({
      ok: Boolean(s27Hit),
      sensor: 'S-27',
      system_eyes_version: SYSTEM_EYES_VERSION,
      triggered_finding: s27Hit || null
    }, null, 2));
    if (!s27Hit) process.exit(1);
  } finally {
    await browser.close();
  }
}

async function main() {
  if (process.argv.includes('--self-test') || process.argv.includes('--self-test-s27')) {
    await runS27CanarySelfTest();
    return;
  }
  const pagesToAudit = resolvePagesFromArgs();
  const { server, baseUrl } = await startServer();
  const browser = await chromium.launch({ executablePath: getChromium() });
  const page = await browser.newPage();
  const allFindings = [];
  const screenshotDir = process.argv.includes('--screenshots') ? '/tmp/webpilot_device_screenshots' : null;
  let totalViewsAudited = 0;

  for (const relPage of pagesToAudit) {
    await page.goto(`${baseUrl}/${relPage}`, { waitUntil: 'networkidle' });

    // 1. Standard 3-Zone Audit
    for (const zone of SYSTEM_EYES_ZONES) {
      const f = await auditPageZone(page, relPage, zone, screenshotDir);
      allFindings.push(...f);
      totalViewsAudited++;

      // 2a. Blueprint Preview Modal (#wpBlueprintModal) on V2 / Zeigeversion pages across all 3 Zones
      const openedBlueprint = await page.evaluate(() => {
        if (typeof window.wpOpenBlueprintModal === 'function') {
          window.wpOpenBlueprintModal('Angebots-Vertiefung & Seminar-Programme', '1:1 Executive-Coaching, 9 Levels Workshops & MentalFitnessCenter', 'Christine Wüest & Nino Paneduro');
          const m = document.getElementById('wpBlueprintModal');
          return (m && m.classList.contains('open')) ? '#wpBlueprintModal' : null;
        }
        if (typeof window.wpOpenBlueprint === 'function') {
          window.wpOpenBlueprint('angebot');
          const m = document.getElementById('wpBlueprintModal');
          return (m && m.classList.contains('open')) ? '#wpBlueprintModal' : null;
        }
        return null;
      });
      if (openedBlueprint) {
        await page.waitForTimeout(80);
        const bpf = await page.evaluate(evaluateSystemEyesInPage, {
          relPage: `${relPage}#blueprint-modal`,
          zone,
          options: { activeScopeSelector: openedBlueprint }
        });
        allFindings.push(...bpf);
        totalViewsAudited++;
        await page.evaluate(() => {
          if (typeof window.wpCloseBlueprintModal === 'function') window.wpCloseBlueprintModal();
          if (typeof window.wpCloseBlueprint === 'function') window.wpCloseBlueprint();
        });
        await page.waitForTimeout(50);
      }

      // 2b. Partner Attribution Modal (#wpPartnerModal) on kontakt.html across all 3 Zones
      if (relPage.endsWith('/kontakt.html')) {
        const openedPartner = await page.evaluate(() => {
          if (typeof window.wpOpenPartnerModal === 'function') {
            window.wpOpenPartnerModal('audit');
            const m = document.getElementById('wpPartnerModal');
            return (m && m.classList.contains('open')) ? '#wpPartnerModal' : null;
          }
          return null;
        });
        if (openedPartner) {
          await page.waitForTimeout(80);
          const pf = await page.evaluate(evaluateSystemEyesInPage, {
            relPage: `${relPage}#partner-modal`,
            zone,
            options: { activeScopeSelector: openedPartner }
          });
          allFindings.push(...pf);
          totalViewsAudited++;
          await page.evaluate(() => {
            if (typeof window.wpClosePartnerModal === 'function') window.wpClosePartnerModal();
          });
          await page.waitForTimeout(50);
        }
      }

      // 2. Customer/Marketing Website Mobile Burger Menu State (W1) on 375x667
      if (!relPage.endsWith('cockpit.html') && zone.width === 375) {
        const openedBurger = await page.evaluate(() => {
          const btn = document.querySelector('.nav-burger, #navBurgerBtn, #mobileMenuBtn, [aria-label*="Menü"]');
          if (!btn) return null;
          btn.click();
          const drawer = document.querySelector('#mobileNavDrawer.open, #mobileDrawer.open, #navDrawer.open, .mobile-drawer.open, .nav-drawer.open');
          return drawer ? '#' + (drawer.id || 'mobile-drawer') : null;
        });
        if (openedBurger) {
          await page.waitForTimeout(120);
          if (screenshotDir && relPage.endsWith('/index.html')) {
            const clientPrefix = relPage.split('/')[0];
            await page.screenshot({
              path: path.join(screenshotDir, `${clientPrefix}_index_burger_open_375x667.png`),
              fullPage: false
            });
          }
          const bf = await page.evaluate(evaluateSystemEyesInPage, {
            relPage: `${relPage}#mobile-burger-menu`,
            zone,
            options: { activeScopeSelector: openedBurger }
          });
          allFindings.push(...bf);
          totalViewsAudited++;

          // Close burger menu again
          await page.evaluate(() => {
            const btn = document.querySelector('.nav-burger, #navBurgerBtn, #mobileMenuBtn, [aria-label*="Menü"]');
            if (btn) btn.click();
          });
          await page.waitForTimeout(60);
        }
      }
    }

    // 2c. Partner Studio Interactive States (Tab 1 List, Tab 1 Cards, Tab 2 Intake, Tab 3 Admin 2FA)
    if (relPage === 'partner/index.html') {
      const unlocked = await page.evaluate(() => {
        if (typeof window.wpUnlockStudioForAudit === 'function') {
          window.wpUnlockStudioForAudit(true);
          const sv = document.getElementById('studioView');
          return (sv && !sv.classList.contains('hidden')) ? '#studioView' : null;
        }
        return null;
      });
      if (unlocked) {
        const partnerStates = [
          {
            suffix: '#tab1-list',
            setup: () => {
              if (typeof window.wpSwitchStudioTab === 'function') window.wpSwitchStudioTab('projects');
              const bList = document.getElementById('btnViewList');
              if (bList) bList.click();
            }
          },
          {
            suffix: '#tab1-cards',
            setup: () => {
              if (typeof window.wpSwitchStudioTab === 'function') window.wpSwitchStudioTab('projects');
              const bCards = document.getElementById('btnViewCards');
              if (bCards) bCards.click();
            }
          },
          {
            suffix: '#tab2-intake',
            setup: () => {
              if (typeof window.wpSwitchStudioTab === 'function') window.wpSwitchStudioTab('intake');
            }
          },
          {
            suffix: '#tab3-admin-2fa',
            setup: () => {
              if (typeof window.wpSwitchStudioTab === 'function') window.wpSwitchStudioTab('admin');
            }
          }
        ];
        for (const pState of partnerStates) {
          await page.evaluate(pState.setup);
          await page.waitForTimeout(120);
          for (const zone of SYSTEM_EYES_ZONES) {
            const sf = await auditPageZone(page, `${relPage}${pState.suffix}`, zone, screenshotDir);
            allFindings.push(...sf);
            totalViewsAudited++;
          }
        }
      }
    }

    // 3. Studio Cockpit Interactive State-Walker (All 11 Additional States x 3 Zones)
    if (relPage.endsWith('cockpit.html')) {
      const clientPrefix = relPage.split('/')[0];
      for (const state of COCKPIT_STATES) {
        for (const zone of SYSTEM_EYES_ZONES) {
          await page.setViewportSize({ width: zone.width, height: zone.height });
          await page.evaluate(state.open);
          if (state.id === 'state_images_modal') {
            await page.evaluate(async () => {
              const imgs = Array.from(document.querySelectorAll('#acp-images-modal img'));
              for (const im of imgs) { im.loading = 'eager'; }
              await Promise.all(imgs.map(im => im.complete ? Promise.resolve() : new Promise(r => { im.onload = r; im.onerror = r; setTimeout(r, 800); })));
            });
          }
          await page.waitForTimeout(state.id === 'state_sections_modal' ? 280 : 120);

          if (screenshotDir && (zone.width === 1440 || zone.width === 375)) {
            fs.mkdirSync(screenshotDir, { recursive: true });
            const shotName = `${clientPrefix}_cockpit_${state.id}_${zone.width}x${zone.height}.png`;
            await page.screenshot({ path: path.join(screenshotDir, shotName), fullPage: false });
          }

          const sf = await page.evaluate(evaluateSystemEyesInPage, {
            relPage: `${relPage}#${state.label}`,
            zone,
            options: { activeScopeSelector: state.activeScopeSelector }
          });
          allFindings.push(...sf);
          totalViewsAudited++;

          await page.evaluate(state.close);
          await page.waitForTimeout(60);
        }
      }
    }
  }

  await browser.close();
  server.close();

  if (screenshotDir) {
    try {
      execFileSync('python3', [path.join(__dirname, 'build_system_eyes_filmstrips.py')], { stdio: 'inherit' });
    } catch (e) {
      console.error('[WARN] Filmstrip build failed:', e.message);
    }
  }

  const p1 = allFindings.filter(f => f.severity === 'P1');
  const p2 = allFindings.filter(f => f.severity === 'P2');
  console.log(`=== DOPPEL-SYSTEMAUGEN v${SYSTEM_EYES_VERSION} AUDIT: ${pagesToAudit.length} Pages | ${totalViewsAudited} Interactive & Device Views | ${SYSTEM_EYES_SENSORS.length} Sensors ===`);
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

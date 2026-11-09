#!/usr/bin/env node
/**
 * visual_section_inspector.mjs – Sektion-fuer-Sektion Grafik-, Fluchtlinien- & Proportions-Inspektor (#UI-02, #UI-14, #UI-16)
 * ============================================================================================================================
 * Vermisst fuer eine gegebene Webseite (--site <slug>) oder alle Showcases (--all) jede Seite
 * auf Desktop (1440x900 & 1366x768) und Mobile (375x667) in Playwright Sektion fuer Sektion
 * (<header>, <section>, <footer>) auf 6 Schweizer Grafik-Design-Kriterien:
 *
 *   1. NAV_SINGLE_LINE:
 *      Liegen im <header> auf Desktop (>= 1024px) alle Hauptmenue-Links exakt auf einer einzigen
 *      horizontalen Linie (maxTop - minTop <= 8px, keine 2-Zeilen-Umbrueche) und ohne klobigen Kasten?
 *   2. SPLIT_BOTTOM_BASELINE_LOCK:
 *      Schliessen in 2-Spalten-Sektionen (insb. Hero- & Split-Sektionen mit Text/Kacheln links und
 *      Bild-/Portrait-/Info-Karte rechts) die Unterkante der linken Spalte und die Unterkante der
 *      rechten Karte auf Desktop (>= 1024px) exakt buendig auf derselben Y-Koordinate
 *      (Math.abs(leftBottom - rightBottom) <= 4px) ab (keine 15-90px "Treppenstufe")?
 *   3. CTA_ROW_HARMONY:
 *      Stehen 2 nebeneinander gehoerende Action-Buttons in einer breiten Desktop-Spalte (>= 480px)
 *      sauber nebeneinander in einer Reihe statt unnoetig vertikal untereinander gestapelt?
 *   4. GRID_ROW_EQUAL_HEIGHT:
 *      Haben Karten (card, feature-card, service-card, stat-card, etc.), die in derselben Grid-Zeile
 *      nebeneinander stehen, auf den Pixel genau dieselbe Hoehe (Math.abs(heightA - heightB) <= 2px)
 *      und schliessen ihre Unterkanten buendig ab?
 *   5. CARD_INTERNAL_BALANCE:
 *      Ist in gleich hohen Karten der Inhalt sauber verteilt (kein > 90px grosses totes Loch am
 *      unteren Kartenrand ohne justify-content: space-between oder passenden Flex-Fueller)?
 *   6. SECTION_RHYTHM_AND_SYMMETRY:
 *      Haben aufeinanderfolgende Sektionen dieselbe linke Container-Fluchtlinie
 *      (Math.abs(containerLeftA - containerLeftB) <= 2px auf 1440px)?
 *
 * Flags:
 *   --site <slug>          Prueft einen einzelnen Showcase (z.B. preview-herzensarbeit)
 *   --all                  Prueft alle 9 WebPilot-Showcases (inkl. -v2 Varianten = 14 Verzeichnisse)
 *   --contact-sheet        Rendert visuelle Pruefboegen mit eingezeichneten gruenen/roten Fluchtlinien
 *   --out-dir <pfad>       Zielordner fuer Contact-Sheets (Standard: artifacts/section_inspector)
 */

import fs from "fs";
import path from "path";
import http from "http";
import { fileURLToPath } from "url";
import { createRequire } from "module";

const require = createRequire("/home/brainuser/workspaces/ACP-Authentic-Content-Pilot-Pro0396/acp-app/package.json");
const { chromium } = require("playwright-core");

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, "..");

const CHROMIUM_PATHS = [
  "/home/brainuser/.cache/ms-playwright/chromium-1217/chrome-linux64/chrome",
  "/home/brainuser/.cache/ms-playwright/chromium-1217/chrome-linux/chrome",
  "/home/brainuser/.cache/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-linux64/chrome-headless-shell"
];

export const SHOWCASE_DIRS = [
  "preview-herzensarbeit",
  "preview-herzensarbeit-v2",
  "preview-innere-staerke",
  "preview-innere-staerke-v2",
  "preview-frees",
  "preview-frees-v2",
  "preview-imp-marketing",
  "preview-imp-marketing-v2",
  "preview-joma",
  "preview-joma-v2",
  "preview-fcschlieren",
  "preview-fcschlieren-v2",
  "preview-scfulenbach",
  "preview-fcattiswil",
  "preview-her11",
  "preview-hochuli"
];

export const INSPECTOR_VIEWPORTS = [
  { name: "desktop_1440x900", width: 1440, height: 900 },
  { name: "laptop_1366x768", width: 1366, height: 768 },
  { name: "mobile_375x667", width: 375, height: 667 }
];

function findChromium() {
  for (const p of CHROMIUM_PATHS) {
    if (fs.existsSync(p)) return p;
  }
  throw new Error("Chromium binary not found in CHROMIUM_PATHS");
}

function startStaticServer(rootDir) {
  const mimeTypes = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".mjs": "application/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
    ".svg": "image/svg+xml",
    ".ico": "image/x-icon",
    ".woff2": "font/woff2",
    ".woff": "font/woff"
  };

  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      try {
        const cleanUrl = decodeURIComponent((req.url || "/").split("?")[0].split("#")[0]);
        let filePath = path.join(rootDir, cleanUrl);
        if (fs.existsSync(filePath) && fs.statSync(filePath).isDirectory()) {
          filePath = path.join(filePath, "index.html");
        }
        if (!fs.existsSync(filePath)) {
          res.writeHead(404);
          res.end("Not found");
          return;
        }
        const ext = path.extname(filePath).toLowerCase();
        res.writeHead(200, { "Content-Type": mimeTypes[ext] || "application/octet-stream" });
        fs.createReadStream(filePath).pipe(res);
      } catch (e) {
        res.writeHead(500);
        res.end(String(e));
      }
    });
    server.listen(0, "127.0.0.1", () => {
      resolve({ server, port: server.address().port });
    });
  });
}

function collectSitePages(siteSlug) {
  const dirPath = path.join(ROOT_DIR, siteSlug);
  if (!fs.existsSync(dirPath) || !fs.statSync(dirPath).isDirectory()) {
    return [];
  }
  const files = fs.readdirSync(dirPath)
    .filter(f => f.endsWith(".html") && f !== "cockpit.html" && !f.endsWith("-src.html"))
    .sort((a, b) => (a === "index.html" ? -1 : b === "index.html" ? 1 : a.localeCompare(b)));
  return files.map(f => `${siteSlug}/${f}`);
}

/**
 * Browser-side evaluation of all <header>, <section>, <footer> elements
 * across the 6 Swiss Graphic Design criteria.
 */
function inspectSectionsInPage({ relPage, viewport, drawOverlay }) {
  const VW = viewport.width;
  const VH = viewport.height;
  const isDesktop = VW >= 1024;
  const findings = [];
  const sectionSummaries = [];
  const overlayGuides = [];

  function isVisible(el) {
    if (!el || !(el instanceof Element)) return false;
    const cs = window.getComputedStyle(el);
    if (cs.display === "none" || cs.visibility === "hidden" || parseFloat(cs.opacity || "1") === 0) return false;
    const r = el.getBoundingClientRect();
    return r.width > 1 && r.height > 1;
  }

  function hasVisualSurface(el) {
    if (!el || !(el instanceof Element)) return false;
    const tag = el.tagName.toLowerCase();
    if (["img", "svg", "video", "iframe", "canvas", "hr", "input", "select", "textarea", "button"].includes(tag)) return true;
    const cs = window.getComputedStyle(el);
    const bg = cs.backgroundColor || "";
    const hasBg = bg !== "rgba(0, 0, 0, 0)" && bg !== "transparent";
    const hasBgImg = cs.backgroundImage && cs.backgroundImage !== "none";
    const hasBorder =
      (parseFloat(cs.borderTopWidth) > 0 && cs.borderTopStyle !== "none" && cs.borderTopColor !== "rgba(0, 0, 0, 0)") ||
      (parseFloat(cs.borderBottomWidth) > 0 && cs.borderBottomStyle !== "none" && cs.borderBottomColor !== "rgba(0, 0, 0, 0)") ||
      (parseFloat(cs.borderLeftWidth) > 0 && cs.borderLeftStyle !== "none" && cs.borderLeftColor !== "rgba(0, 0, 0, 0)") ||
      (parseFloat(cs.borderRightWidth) > 0 && cs.borderRightStyle !== "none" && cs.borderRightColor !== "rgba(0, 0, 0, 0)");
    const hasShadow = cs.boxShadow && cs.boxShadow !== "none";
    return Boolean(hasBg || hasBgImg || hasBorder || hasShadow);
  }

  function getVisualBottom(colEl) {
    const colRect = colEl.getBoundingClientRect();
    if (hasVisualSurface(colEl)) {
      return colRect.bottom;
    }
    const kids = Array.from(colEl.children).filter(c => {
      if (!isVisible(c)) return false;
      const cCs = window.getComputedStyle(c);
      return cCs.position !== "absolute" && cCs.position !== "fixed";
    });
    if (kids.length === 0) {
      return colRect.bottom;
    }
    return Math.max(...kids.map(k => getVisualBottom(k)));
  }

  function hasStickyColumn(colEl) {
    const cs = window.getComputedStyle(colEl);
    if (cs.position === "sticky") return true;
    return Array.from(colEl.querySelectorAll("*")).some(ch => window.getComputedStyle(ch).position === "sticky");
  }

  function getShortSelector(el) {
    if (!el) return "";
    const tag = el.tagName.toLowerCase();
    const id = el.id ? `#${el.id}` : "";
    const cls = (el.className && typeof el.className === "string")
      ? "." + el.className.trim().split(/\s+/).slice(0, 2).join(".")
      : "";
    return `${tag}${id}${cls}`;
  }

  function addDefect(criterion, sectionLabel, selector, details, guide) {
    findings.push({
      page: relPage,
      viewport: viewport.name,
      criterion,
      section: sectionLabel,
      selector,
      details
    });
    if (guide) overlayGuides.push({ ...guide, ok: false });
  }

  // ---------------------------------------------------------------------------
  // 1. NAV_SINGLE_LINE (<header>)
  // ---------------------------------------------------------------------------
  const header = document.querySelector("header");
  if (header && isVisible(header) && isDesktop) {
    const navContainer = header.querySelector("nav, .nav-links, .desktop-nav, .header-nav, ul");
    const allHeaderLinks = Array.from((navContainer || header).querySelectorAll("a, button")).filter(el => {
      if (!isVisible(el)) return false;
      if (el.closest(".mobile-menu, #mobileMenu, .nav-drawer, .burger-menu, [class*='mobile']")) return false;
      if (el.matches(".nav-burger, .burger, .menu-toggle, [aria-label*='Menü'], [aria-label*='Menu']")) return false;
      if (el.matches(".logo, .brand, .nav-logo, .header-logo, [class*='logo'], [class*='brand']")) return false;
      return true;
    });

    const regularLinks = allHeaderLinks.filter(el => {
      const cls = (el.className && typeof el.className === "string") ? el.className : "";
      if (/\b(btn|cta|nav-cta|header-cta|btn-primary|btn-accent|button)\b/i.test(cls)) return false;
      return true;
    });

    if (regularLinks.length >= 2) {
      const tops = regularLinks.map(el => el.getBoundingClientRect().top);
      const bottoms = regularLinks.map(el => el.getBoundingClientRect().bottom);
      const minTop = Math.min(...tops);
      const maxTop = Math.max(...tops);
      const topSpread = maxTop - minTop;

      if (topSpread > 8) {
        addDefect(
          "NAV_SINGLE_LINE",
          "header",
          getShortSelector(navContainer || header),
          `Hauptmenue-Links nicht auf einer Linie: maxTop - minTop = ${Math.round(topSpread)}px (Erlaubt: <= 8px)`,
          { type: "hline", y: minTop, x1: regularLinks[0].getBoundingClientRect().left, x2: regularLinks[regularLinks.length - 1].getBoundingClientRect().right, label: `✗ NAV WRAP Δ=${Math.round(topSpread)}px` }
        );
      } else {
        overlayGuides.push({
          type: "hline",
          ok: true,
          y: Math.round((Math.min(...bottoms) + Math.max(...bottoms)) / 2),
          x1: Math.round(regularLinks[0].getBoundingClientRect().left),
          x2: Math.round(regularLinks[regularLinks.length - 1].getBoundingClientRect().right),
          label: `✓ NAV 1-LINE (Δ=${Math.round(topSpread)}px)`
        });
      }

      for (const link of regularLinks) {
        const cs = window.getComputedStyle(link);
        const textNodes = Array.from(link.childNodes).filter(n => n.nodeType === Node.TEXT_NODE && n.nodeValue.trim().length > 0);
        for (const tn of textNodes) {
          const range = document.createRange();
          range.selectNodeContents(tn);
          const rects = range.getClientRects();
          if (rects.length > 1 && Math.abs(rects[rects.length - 1].top - rects[0].top) > 6) {
            addDefect(
              "NAV_SINGLE_LINE",
              "header",
              getShortSelector(link),
              `Menue-Link "${link.textContent.trim()}" bricht zweizeilig um (${rects.length} Zeilen)`
            );
          }
        }
        const bTop = parseFloat(cs.borderTopWidth) || 0;
        const bLeft = parseFloat(cs.borderLeftWidth) || 0;
        const bRight = parseFloat(cs.borderRightWidth) || 0;
        const bBottom = parseFloat(cs.borderBottomWidth) || 0;
        const hasFourSidedBorder = bTop >= 1 && bLeft >= 1 && bRight >= 1 && bBottom >= 1 &&
          cs.borderTopColor !== "rgba(0, 0, 0, 0)" && cs.borderLeftColor !== "rgba(0, 0, 0, 0)";
        const bg = cs.backgroundColor || "";
        const hasBoxBg = bg !== "rgba(0, 0, 0, 0)" && bg !== "transparent";
        if (hasFourSidedBorder || hasBoxBg) {
          addDefect(
            "NAV_SINGLE_LINE",
            "header",
            getShortSelector(link),
            `Menue-Link "${link.textContent.trim()}" hat klobigen Kasten/Hintergrund (bg=${bg}, border=${bTop}/${bRight}/${bBottom}/${bLeft}px) statt feiner Unterstreichung`
          );
        }
      }
    }
  }

  // ---------------------------------------------------------------------------
  // Collect all <section> and <footer> elements
  // ---------------------------------------------------------------------------
  const blocks = Array.from(document.querySelectorAll("header, main > section, body > section, section, footer")).filter(el => {
    if (!isVisible(el)) return false;
    if (el.tagName.toLowerCase() === "section" && el.parentElement && el.parentElement.closest("section")) return false;
    if (el.closest("[id*='Modal'], [id*='modal'], [id*='acp-'], .modal-backdrop")) return false;
    return true;
  });

  const sectionLeftFluchtlinien = [];

  blocks.forEach((block, idx) => {
    const tag = block.tagName.toLowerCase();
    const heading = block.querySelector("h1, h2, h3");
    const headingText = heading ? heading.textContent.trim().replace(/\s+/g, " ").slice(0, 38) : "";
    const sectionLabel = `${tag}#${idx + 1}${block.id ? `(${block.id})` : ""}${headingText ? ` "${headingText}"` : ""}`;
    const blockRect = block.getBoundingClientRect();

    let innerContainer = block.querySelector(".container, .section-inner, .nav-inner, .header-inner, .footer-inner, .hero-inner, .wrap, .wrapper");
    if (!innerContainer) {
      const directDivs = Array.from(block.children).filter(c => isVisible(c) && ["DIV", "NAV"].includes(c.tagName));
      if (directDivs.length === 1) innerContainer = directDivs[0];
    }

    if (innerContainer && isVisible(innerContainer) && tag === "section") {
      const icRect = innerContainer.getBoundingClientRect();
      const icCs = window.getComputedStyle(innerContainer);
      const padL = parseFloat(icCs.paddingLeft) || 0;
      const padR = parseFloat(icCs.paddingRight) || 0;
      const contentLeft = icRect.left + padL;
      const contentRight = icRect.right - padR;
      const maxW = parseFloat(icCs.maxWidth) || icRect.width;

      if (VW === 1440 && (maxW >= 1000 || icRect.width >= 980)) {
        sectionLeftFluchtlinien.push({
          sectionLabel,
          selector: getShortSelector(innerContainer),
          left: contentLeft,
          right: contentRight,
          top: blockRect.top + window.scrollY,
          bottom: blockRect.bottom + window.scrollY
        });
      }

      if (isDesktop) {
        const secHeader = innerContainer.querySelector(".section-header, .sec-header, .section-head");
        if (secHeader && isVisible(secHeader)) {
          const shCs = window.getComputedStyle(secHeader);
          const h2 = secHeader.querySelector("h2, h1");
          const h2Cs = h2 ? window.getComputedStyle(h2) : shCs;
          if (shCs.textAlign !== "center" && h2Cs.textAlign !== "center") {
            const shLeft = (h2 || secHeader).getBoundingClientRect().left;
            if (Math.abs(shLeft - contentLeft) > 4) {
              addDefect(
                "SECTION_RHYTHM_AND_SYMMETRY",
                sectionLabel,
                getShortSelector(secHeader),
                `Sektions-Header links versetzt zur Container-Fluchtlinie: headerLeft=${Math.round(shLeft)}px vs containerLeft=${Math.round(contentLeft)}px`
              );
            }
          }
        }
      }
    }

    // -------------------------------------------------------------------------
    // 2. SPLIT_BOTTOM_BASELINE_LOCK (2-Column Layouts in <section> on Desktop)
    // -------------------------------------------------------------------------
    if (isDesktop && tag === "section") {
      const candidates = [block, ...Array.from(block.querySelectorAll("div, main, article"))].filter(el => {
        if (!isVisible(el)) return false;
        const cs = window.getComputedStyle(el);
        if (cs.display !== "grid" && cs.display !== "flex") return false;
        const r = el.getBoundingClientRect();
        if (r.width < Math.min(720, VW * 0.65) || r.height < 140) return false;
        const cls = (el.className && typeof el.className === "string") ? el.className : "";
        if (/\b(sponsor-tier-header|blueprint-cut-top|assistant-hero-box|section-header|workspace-grid)\b/i.test(cls)) return false;
        const visChildren = Array.from(el.children).filter(c => {
          if (!isVisible(c)) return false;
          const cCs = window.getComputedStyle(c);
          return cCs.position !== "absolute" && cCs.position !== "fixed";
        });
        if (visChildren.length !== 2) return false;
        if (hasStickyColumn(visChildren[0]) || hasStickyColumn(visChildren[1])) return false;
        const r0 = visChildren[0].getBoundingClientRect();
        const r1 = visChildren[1].getBoundingClientRect();
        const sideBySide = Math.abs(r0.left - r1.left) > 140 && r0.right <= r1.left + 8 && Math.abs(r0.top - r1.top) < 120;
        return sideBySide && r0.width >= 200 && r1.width >= 200 && Math.min(r0.height, r1.height) >= 100;
      });

      for (const splitEl of candidates) {
        const visChildren = Array.from(splitEl.children).filter(c => {
          if (!isVisible(c)) return false;
          const cCs = window.getComputedStyle(c);
          return cCs.position !== "absolute" && cCs.position !== "fixed";
        });
        const [leftCol, rightCol] = visChildren;
        const leftVisualBottom = getVisualBottom(leftCol);
        const rightVisualBottom = getVisualBottom(rightCol);
        const bottomDiff = Math.abs(leftVisualBottom - rightVisualBottom);

        const rLeft = leftCol.getBoundingClientRect();
        const rRight = rightCol.getBoundingClientRect();

        if (bottomDiff > 4) {
          addDefect(
            "SPLIT_BOTTOM_BASELINE_LOCK",
            sectionLabel,
            getShortSelector(splitEl),
            `Treppenstufe an der Unterkante der 2-Spalten-Sektion: links=${Math.round(leftVisualBottom)}px vs rechts=${Math.round(rightVisualBottom)}px (Δ=${Math.round(bottomDiff)}px, erlaubt <= 4px)`,
            {
              type: "split_step",
              x1: Math.round(rLeft.left),
              xMid: Math.round((rLeft.right + rRight.left) / 2),
              x2: Math.round(rRight.right),
              yLeft: Math.round(leftVisualBottom + window.scrollY),
              yRight: Math.round(rightVisualBottom + window.scrollY),
              label: `✗ SPLIT STEP Δ=${Math.round(bottomDiff)}px`
            }
          );
        } else {
          overlayGuides.push({
            type: "hline",
            ok: true,
            y: Math.round(leftVisualBottom + window.scrollY),
            x1: Math.round(rLeft.left),
            x2: Math.round(rRight.right),
            label: `✓ SPLIT BASELINE LOCK (Δ=${Math.round(bottomDiff)}px)`
          });
        }
      }
    }

    // -------------------------------------------------------------------------
    // 3. CTA_ROW_HARMONY (2 Action-Buttons in wide Desktop column >= 480px)
    // -------------------------------------------------------------------------
    if (isDesktop && tag === "section") {
      const allContainers = Array.from(block.querySelectorAll("div, nav, p, form")).filter(isVisible);
      for (const c of allContainers) {
        const directBtns = Array.from(c.children).filter(ch => {
          if (!isVisible(ch)) return false;
          const t = ch.tagName.toLowerCase();
          if (t !== "a" && t !== "button") return false;
          const cls = (ch.className && typeof ch.className === "string") ? ch.className : "";
          const cs = window.getComputedStyle(ch);
          const hasBtnLook = /\b(btn|cta|button)\b/i.test(cls) ||
            (parseFloat(cs.paddingLeft) >= 12 && (cs.backgroundColor !== "rgba(0, 0, 0, 0)" || parseFloat(cs.borderTopWidth) >= 1));
          return hasBtnLook;
        });

        if (directBtns.length === 2) {
          const parentCol = c.closest(".hero-copy, .hero-left, .hero-content, .split-left, div") || c;
          const colRect = parentCol.getBoundingClientRect();
          const cRect = c.getBoundingClientRect();
          const availableWidth = Math.max(colRect.width, cRect.width);
          if (availableWidth >= 480) {
            const b0 = directBtns[0].getBoundingClientRect();
            const b1 = directBtns[1].getBoundingClientRect();
            if (Math.abs(b0.top - b1.top) > 10) {
              addDefect(
                "CTA_ROW_HARMONY",
                sectionLabel,
                getShortSelector(c),
                `2 Action-Buttons ("${directBtns[0].textContent.trim().slice(0, 22)}" & "${directBtns[1].textContent.trim().slice(0, 22)}") sind in einer ${Math.round(availableWidth)}px breiten Spalte vertikal gestapelt (top0=${Math.round(b0.top)}px vs top1=${Math.round(b1.top)}px)`
              );
            } else if (Math.abs(b0.height - b1.height) > 2) {
              addDefect(
                "CTA_ROW_HARMONY",
                sectionLabel,
                getShortSelector(c),
                `2 nebeneinanderliegende Action-Buttons haben ungleiche Hoehe: ${Math.round(b0.height)}px vs ${Math.round(b1.height)}px`
              );
            }
          }
        }
      }
    }

    // -------------------------------------------------------------------------
    // 4. GRID_ROW_EQUAL_HEIGHT & 5. CARD_INTERNAL_BALANCE
    // -------------------------------------------------------------------------
    if (tag === "section") {
      const gridParents = Array.from(block.querySelectorAll("div, ul")).filter(el => {
        if (!isVisible(el)) return false;
        const cs = window.getComputedStyle(el);
        return cs.display === "grid" || cs.display === "flex";
      });

      for (const gp of gridParents) {
        const gpCls = (gp.className && typeof gp.className === "string") ? gp.className : "";
        if (/\b(workspace-grid)\b/i.test(gpCls)) continue;

        const cardChildren = Array.from(gp.children).filter(ch => {
          if (!isVisible(ch)) return false;
          const cs = window.getComputedStyle(ch);
          if (cs.position === "absolute" || cs.position === "fixed" || cs.position === "sticky") return false;
          const cls = (ch.className && typeof ch.className === "string") ? ch.className : "";
          const isCardClass = /\b(card|feature-card|service-card|stat-card|kpi-card|offer-card|team-card|value-card|step-card|testimonial-card|review-card|price-card|pricing-card|tile|box|panel|item)\b/i.test(cls);
          return isCardClass || hasVisualSurface(ch);
        });

        if (cardChildren.length < 2) continue;

        const rows = [];
        for (const ch of cardChildren) {
          const r = ch.getBoundingClientRect();
          if (r.width < 80 || r.height < 42) continue;
          let row = rows.find(rw => Math.abs(rw.top - r.top) <= 16);
          if (!row) {
            row = { top: r.top, items: [] };
            rows.push(row);
          }
          row.items.push({ el: ch, rect: r });
        }

        for (const rw of rows) {
          if (rw.items.length < 2) continue;
          rw.items.sort((a, b) => a.rect.left - b.rect.left);
          const distinctX = rw.items.every((it, i) => i === 0 || it.rect.left >= rw.items[i - 1].rect.right - 4);
          if (!distinctX) continue;

          const heights = rw.items.map(i => i.rect.height);
          const bottoms = rw.items.map(i => i.rect.bottom);
          const maxH = Math.max(...heights);
          const minH = Math.min(...heights);
          const maxB = Math.max(...bottoms);
          const minB = Math.min(...bottoms);

          if (maxH - minH > 2 || maxB - minB > 2) {
            addDefect(
              "GRID_ROW_EQUAL_HEIGHT",
              sectionLabel,
              getShortSelector(gp),
              `Nachbar-Karten in derselben Zeile haben ungleiche Hoehe/Unterkante: minH=${Math.round(minH)}px vs maxH=${Math.round(maxH)}px (ΔH=${Math.round(maxH - minH)}px, ΔBottom=${Math.round(maxB - minB)}px)`,
              {
                type: "hline",
                y: Math.round(maxB + window.scrollY),
                x1: Math.round(rw.items[0].rect.left),
                x2: Math.round(rw.items[rw.items.length - 1].rect.right),
                label: `✗ CARD ROW Δ=${Math.round(maxH - minH)}px`
              }
            );
          } else if (isDesktop) {
            overlayGuides.push({
              type: "hline",
              ok: true,
              y: Math.round(maxB + window.scrollY),
              x1: Math.round(rw.items[0].rect.left),
              x2: Math.round(rw.items[rw.items.length - 1].rect.right),
              label: `✓ ROW EQUAL HEIGHT (${rw.items.length}x ${Math.round(maxH)}px)`
            });
          }

          for (const item of rw.items) {
            const cardEl = item.el;
            const cRect = item.rect;
            if (cRect.height < 140) continue;
            const cCs = window.getComputedStyle(cardEl);
            const padB = parseFloat(cCs.paddingBottom) || 0;
            const borderB = parseFloat(cCs.borderBottomWidth) || 0;
            const innerBottom = cRect.bottom - padB - borderB;

            const visKids = Array.from(cardEl.children).filter(k => {
              if (!isVisible(k)) return false;
              const kCs = window.getComputedStyle(k);
              return kCs.position !== "absolute" && kCs.position !== "fixed";
            });
            if (visKids.length === 0) continue;

            let lowestChildBottom = -Infinity;
            for (const k of visKids) {
              const kr = k.getBoundingClientRect();
              if (kr.bottom > lowestChildBottom) lowestChildBottom = kr.bottom;
            }
            const deadHole = innerBottom - lowestChildBottom;
            if (deadHole > 90) {
              addDefect(
                "CARD_INTERNAL_BALANCE",
                sectionLabel,
                getShortSelector(cardEl),
                `Karte hat unten ein ${Math.round(deadHole)}px grosses totes Loch (Erlaubt: <= 90px; fehlt flex-direction: column / justify-content: space-between / margin-top: auto)`
              );
            }
          }
        }
      }
    }

    sectionSummaries.push({
      section: sectionLabel,
      top: Math.round(blockRect.top + window.scrollY),
      height: Math.round(blockRect.height)
    });
  });

  // ---------------------------------------------------------------------------
  // 6. SECTION_RHYTHM_AND_SYMMETRY (Consecutive Sections Left Fluchtlinie on 1440px)
  // ---------------------------------------------------------------------------
  if (VW === 1440 && sectionLeftFluchtlinien.length >= 2) {
    const refLeft = sectionLeftFluchtlinien[0].left;
    const refRight = sectionLeftFluchtlinien[0].right;
    let allAligned = true;

    for (let i = 1; i < sectionLeftFluchtlinien.length; i++) {
      const prev = sectionLeftFluchtlinien[i - 1];
      const curr = sectionLeftFluchtlinien[i];
      const diffLeft = Math.abs(curr.left - prev.left);
      if (diffLeft > 2) {
        allAligned = false;
        addDefect(
          "SECTION_RHYTHM_AND_SYMMETRY",
          curr.sectionLabel,
          curr.selector,
          `Linke Container-Fluchtlinie springt gegenueber Vor-Sektion (${prev.sectionLabel}): ${Math.round(curr.left)}px vs ${Math.round(prev.left)}px (Δ=${Math.round(diffLeft)}px, erlaubt <= 2px)`
        );
      }
    }

    overlayGuides.push({
      type: "vline",
      ok: allAligned,
      x: Math.round(refLeft),
      label: allAligned ? `✓ FLUCHTLINIE L X=${Math.round(refLeft)}px` : `✗ FLUCHTLINIE L DRIFT`
    });
    overlayGuides.push({
      type: "vline",
      ok: allAligned,
      x: Math.round(refRight),
      label: allAligned ? `✓ FLUCHTLINIE R X=${Math.round(refRight)}px` : `✗ FLUCHTLINIE R DRIFT`
    });
  }

  // ---------------------------------------------------------------------------
  // Optional: Draw Visual SVG Overlay for Contact Sheet / Proof Screenshot
  // ---------------------------------------------------------------------------
  if (drawOverlay) {
    const old = document.getElementById("__visual_section_inspector_overlay");
    if (old) old.remove();

    const docH = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight, VH);
    const svgNS = "http://www.w3.org/2000/svg";
    const wrapper = document.createElement("div");
    wrapper.id = "__visual_section_inspector_overlay";
    wrapper.style.cssText = `position:absolute;top:0;left:0;width:${VW}px;height:${docH}px;pointer-events:none;z-index:2147483647;overflow:hidden;`;

    const svg = document.createElementNS(svgNS, "svg");
    svg.setAttribute("width", String(VW));
    svg.setAttribute("height", String(docH));
    svg.setAttribute("viewBox", `0 0 ${VW} ${docH}`);

    for (const g of overlayGuides) {
      const color = g.ok ? "#10b981" : "#ef4444";
      if (g.type === "vline") {
        const line = document.createElementNS(svgNS, "line");
        line.setAttribute("x1", String(g.x));
        line.setAttribute("y1", "0");
        line.setAttribute("x2", String(g.x));
        line.setAttribute("y2", String(docH));
        line.setAttribute("stroke", color);
        line.setAttribute("stroke-width", "2");
        line.setAttribute("stroke-dasharray", "6,4");
        svg.appendChild(line);

        const badge = document.createElementNS(svgNS, "rect");
        badge.setAttribute("x", String(Math.max(4, g.x - 75)));
        badge.setAttribute("y", "8");
        badge.setAttribute("width", "150");
        badge.setAttribute("height", "20");
        badge.setAttribute("rx", "4");
        badge.setAttribute("fill", color);
        svg.appendChild(badge);

        const txt = document.createElementNS(svgNS, "text");
        txt.setAttribute("x", String(Math.max(79, g.x)));
        txt.setAttribute("y", "22");
        txt.setAttribute("fill", "#ffffff");
        txt.setAttribute("font-size", "10");
        txt.setAttribute("font-family", "sans-serif");
        txt.setAttribute("font-weight", "bold");
        txt.setAttribute("text-anchor", "middle");
        txt.textContent = g.label;
        svg.appendChild(txt);
      } else if (g.type === "hline") {
        const line = document.createElementNS(svgNS, "line");
        line.setAttribute("x1", String(g.x1));
        line.setAttribute("y1", String(g.y));
        line.setAttribute("x2", String(g.x2));
        line.setAttribute("y2", String(g.y));
        line.setAttribute("stroke", color);
        line.setAttribute("stroke-width", "2.5");
        svg.appendChild(line);

        const midX = Math.round((g.x1 + g.x2) / 2);
        const bw = Math.max(170, g.label.length * 6.5);
        const badge = document.createElementNS(svgNS, "rect");
        badge.setAttribute("x", String(midX - bw / 2));
        badge.setAttribute("y", String(Math.max(2, g.y - 11)));
        badge.setAttribute("width", String(bw));
        badge.setAttribute("height", "20");
        badge.setAttribute("rx", "4");
        badge.setAttribute("fill", color);
        svg.appendChild(badge);

        const txt = document.createElementNS(svgNS, "text");
        txt.setAttribute("x", String(midX));
        txt.setAttribute("y", String(Math.max(15, g.y + 3)));
        txt.setAttribute("fill", "#ffffff");
        txt.setAttribute("font-size", "10");
        txt.setAttribute("font-family", "sans-serif");
        txt.setAttribute("font-weight", "bold");
        txt.setAttribute("text-anchor", "middle");
        txt.textContent = g.label;
        svg.appendChild(txt);
      } else if (g.type === "split_step") {
        const l1 = document.createElementNS(svgNS, "line");
        l1.setAttribute("x1", String(g.x1));
        l1.setAttribute("y1", String(g.yLeft));
        l1.setAttribute("x2", String(g.xMid));
        l1.setAttribute("y2", String(g.yLeft));
        l1.setAttribute("stroke", "#ef4444");
        l1.setAttribute("stroke-width", "3");
        svg.appendChild(l1);

        const l2 = document.createElementNS(svgNS, "line");
        l2.setAttribute("x1", String(g.xMid));
        l2.setAttribute("y1", String(g.yRight));
        l2.setAttribute("x2", String(g.x2));
        l2.setAttribute("y2", String(g.yRight));
        l2.setAttribute("stroke", "#ef4444");
        l2.setAttribute("stroke-width", "3");
        svg.appendChild(l2);

        const lStep = document.createElementNS(svgNS, "line");
        lStep.setAttribute("x1", String(g.xMid));
        lStep.setAttribute("y1", String(g.yLeft));
        lStep.setAttribute("x2", String(g.xMid));
        lStep.setAttribute("y2", String(g.yRight));
        lStep.setAttribute("stroke", "#ef4444");
        lStep.setAttribute("stroke-width", "3");
        lStep.setAttribute("stroke-dasharray", "4,3");
        svg.appendChild(lStep);
      }
    }

    wrapper.appendChild(svg);
    document.body.appendChild(wrapper);
  }

  return {
    page: relPage,
    viewport: viewport.name,
    sectionsCount: sectionSummaries.length,
    findings
  };
}

async function main() {
  const args = process.argv.slice(2);
  let siteArg = null;
  let runAll = false;
  let contactSheet = false;
  let contactSheetDir = path.join(ROOT_DIR, "artifacts", "section_inspector");

  for (let i = 0; i < args.length; i++) {
    if ((args[i] === "--site" || args[i] === "--slug") && args[i + 1]) {
      siteArg = args[++i];
    } else if (args[i] === "--all") {
      runAll = true;
    } else if (args[i] === "--contact-sheet") {
      contactSheet = true;
    } else if (args[i] === "--out-dir" && args[i + 1]) {
      contactSheetDir = path.resolve(args[++i]);
    }
  }

  if (!siteArg && !runAll) {
    console.error("Usage: node scripts/visual_section_inspector.mjs --site <slug> | --all [--contact-sheet]");
    process.exit(1);
  }

  const targetSites = [];
  if (runAll) {
    targetSites.push(...SHOWCASE_DIRS);
  } else if (siteArg) {
    let clean = siteArg.replace(/\/+$/, "");
    if (!fs.existsSync(path.join(ROOT_DIR, clean)) && fs.existsSync(path.join(ROOT_DIR, `preview-${clean}`))) {
      clean = `preview-${clean}`;
    }
    targetSites.push(clean);
  }

  const pagesToInspect = [];
  for (const s of targetSites) {
    pagesToInspect.push(...collectSitePages(s));
  }

  if (pagesToInspect.length === 0) {
    console.log(`[Visual-Section-Inspector] Keine Kunden-HTML-Seiten fuer ${targetSites.join(", ")} gefunden.`);
    process.exit(0);
  }

  const { server, port } = await startStaticServer(ROOT_DIR);
  const browser = await chromium.launch({
    executablePath: findChromium(),
    headless: true,
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
  });

  const context = await browser.newContext();
  const page = await context.newPage();

  const allFindings = [];
  let totalSectionsInspected = 0;
  let totalPageViews = 0;

  if (contactSheet) {
    fs.mkdirSync(contactSheetDir, { recursive: true });
  }

  for (const relPage of pagesToInspect) {
    const url = `http://127.0.0.1:${port}/${relPage}`;
    for (const vp of INSPECTOR_VIEWPORTS) {
      await page.setViewportSize({ width: vp.width, height: vp.height });
      await page.goto(url, { waitUntil: "load", timeout: 30000 });
      await page.evaluate(async () => {
        if (document.fonts && document.fonts.ready) {
          await document.fonts.ready;
        }
        const imgs = Array.from(document.querySelectorAll("img"));
        for (const im of imgs) im.loading = "eager";
        await Promise.all(
          imgs.map(im =>
            im.complete
              ? Promise.resolve()
              : new Promise(r => {
                  im.onload = r;
                  im.onerror = r;
                  setTimeout(r, 1200);
                })
          )
        );
      });
      await page.waitForTimeout(80);

      const drawOverlay = contactSheet && vp.width === 1440;
      const res = await page.evaluate(inspectSectionsInPage, { relPage, viewport: vp, drawOverlay });
      totalSectionsInspected += res.sectionsCount;
      totalPageViews++;
      allFindings.push(...res.findings);

      if (drawOverlay) {
        const safeName = relPage.replace(/[\/\\]/g, "__").replace(/\.html$/, "");
        const shotPath = path.join(contactSheetDir, `${safeName}__1440x900_sheet.png`);
        await page.screenshot({ path: shotPath, fullPage: true });
      }
    }
  }

  await browser.close();
  server.close();

  console.log(`=== VISUAL SECTION INSPECTOR (#UI-02 / #UI-16): ${targetSites.length} Sites | ${pagesToInspect.length} Pages | ${totalPageViews} Views | ${totalSectionsInspected} Sections Inspected ===`);
  console.log(`Grafik-Maengel gesamt: ${allFindings.length}`);

  if (allFindings.length > 0) {
    const byCrit = {};
    for (const f of allFindings) {
      byCrit[f.criterion] = (byCrit[f.criterion] || 0) + 1;
    }
    console.log("Nach Kriterium:", JSON.stringify(byCrit));
    for (const f of allFindings) {
      console.log(`  [GRAFIK-MANGEL] [${f.criterion}] ${f.page} (${f.viewport}) :: ${f.section} [${f.selector}] -> ${f.details}`);
    }
    process.exit(1);
  } else {
    console.log("✓ ALLE 6 SCHWEIZER GRAFIK-KRITERIEN BESTANDEN (0 Grafik-Maengel)!");
    process.exit(0);
  }
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});

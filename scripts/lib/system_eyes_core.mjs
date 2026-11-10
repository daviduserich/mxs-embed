/**
 * system_eyes_core.mjs – Zentraler Doppel-Systemaugen-Baustein v2.0.0 (#UI-01, #UI-06, #UI-13, #UI-14)
 * ====================================================================================================
 * Wiederverwendbares Kern-Modul fuer alle ACP- & WebPilot-Frontends:
 *   - mxs-embed (WebPilot Kunden-Webseiten & Studio-Cockpits v4.0)
 *   - acp-app (Cockpit, Erfassung, Admin)
 *   - acp-landing & acp-blog
 *   - magnet-xs-website
 *
 * Architektur:
 *   Auge 1 (Mathematisch-Aesthetische Sensoren S-01..S-18):
 *     Vermisst im echten Headless-Chromium ueber alle 3 Geraete-Zonen (375x667, 1366x768, 1440x900)
 *     jedes sichtbare DOM-Element, jedes Bild, jeden Button, jedes Grid und jedes geoeffnete Modal/Menue.
 *   Auge 2 (Visuelle Kamera-Filmstreifen):
 *     Erzeugt hochaufloesende Kontaktboegen (Filmstrips < 400 KB) aller Seiten, Unterseiten,
 *     Mobile-Menues und Cockpit-Modals zur verpflichtenden Sichtabnahme per read_file.
 */

export const SYSTEM_EYES_VERSION = '2.6.0';

export const SYSTEM_EYES_ZONES = [
  { name: 'mobile_375x667', width: 375, height: 667, label: 'Zone 1 Smartphone (375×667)' },
  { name: 'laptop_1366x768', width: 1366, height: 768, label: 'Zone 2 Laptop (1366×768)' },
  { name: 'desktop_1440x900', width: 1440, height: 900, label: 'Zone 3 Desktop (1440×900)' }
];

export const SYSTEM_EYES_SENSORS = [
  { id: 'S-01', code: 'P1_HORIZONTAL_OVERFLOW', severity: 'P1', rule: '#UI-13', desc: 'Dokument scrollWidth darf Viewport-Breite (VW) niemals ueberschreiten' },
  { id: 'S-02', code: 'P1_OFFSCREEN_X', severity: 'P1', rule: '#UI-13', desc: 'Interaktive Elemente muessen horizontal vollstaendig im Viewport (0..VW) liegen' },
  { id: 'S-03', code: 'P1_UNREACHABLE_OFFSCREEN', severity: 'P1', rule: '#UI-13', desc: 'Interaktive Elemente duerfen nicht in overflow:hidden Containern abgeschnitten sein' },
  { id: 'S-04', code: 'P1_ELEMENT_COLLISION', severity: 'P1', rule: '#UI-14', desc: 'Sichtbare interaktive Elemente derselben Schicht duerfen sich nicht ueberlappen (> 4x4px)' },
  { id: 'S-05', code: 'P1_MID_SCREEN_SCROLLBAR', severity: 'P1', rule: '#UI-14', desc: 'Auf Desktop/Laptop (>=769px) sind Teil-Scrollbalken mitten im Screen verboten (Ausnahme: Modals/Code)' },
  { id: 'S-06', code: 'P1_STICKY_OCCLUDES_FOOTER', severity: 'P1', rule: '#UI-13', desc: 'Auf Mobile (<769px) muss der Footer bei Max-Scroll komplett ueber der Sticky-Daumenzone liegen' },
  { id: 'S-07', code: 'P1_PARTIALLY_OCCLUDED_BY_STICKY', severity: 'P1', rule: '#UI-13', desc: 'Footer-Links und unterste CTAs duerfen bei Max-Scroll nicht von Sticky-Bars verdeckt werden' },
  { id: 'S-08', code: 'P1_SIDEBAR_OVERFLOW', severity: 'P1', rule: '#UI-14', desc: 'Globale Navigations-Seitenleiste darf im Ruhezustand nicht vertikal scrollen' },
  { id: 'S-09', code: 'P1_BROKEN_IMAGE', severity: 'P1', rule: '#UI-14', desc: 'Jedes sichtbare <img> muss vollstaendig geladen und dekodierbar sein (complete && naturalWidth > 0)' },
  { id: 'S-10', code: 'P2_CRAMPED_MOBILE', severity: 'P2', rule: '#UI-14', desc: 'Interaktive Touch-Ziele auf Mobile (<769px) muessen mindestens 34x30px gross sein' },
  { id: 'S-11', code: 'P2_EMOJI_IN_UI', severity: 'P2', rule: '#UI-01', desc: '100% Lucide-SVG-Pflicht: Keine Unicode-Emojis oder Text-Checkmarks (✓, ✔, ❌, ✅) im UI' },
  { id: 'S-12', code: 'P2_BAD_RADIUS', severity: 'P2', rule: '#UI-01', desc: 'Strikte 2-Radius-Architektur: Ausschliesslich 0px, 4px oder 8px erlaubt' },
  { id: 'S-13', code: 'P2_UNSTYLED_OR_EMPTY_BUTTON', severity: 'P2', rule: '#UI-01', desc: 'Keine ungestylten Browser-Buttons (buttonface/outset) und keine leeren Buttons ohne Text & SVG' },
  { id: 'S-14', code: 'P2_RAGGED_RIGHT_EDGE', severity: 'P2', rule: '#UI-14', desc: 'Mehrspaltige Karten-Grids muessen rechts buendig abschliessen (Toleranz <= 14px)' },
  { id: 'S-15', code: 'P2_ROW_HEIGHT_MISMATCH', severity: 'P2', rule: '#UI-14', desc: 'Karten in derselben Grid-Zeile muessen exakt gleich hoch sein (Toleranz <= 4px)' },
  { id: 'S-16', code: 'P2_SEVERE_TEXT_TRUNCATION', severity: 'P2', rule: '#UI-14', desc: 'Text mit text-overflow:ellipsis darf nicht unter 115px Restbreite abgeschnitten werden' },
  { id: 'S-17', code: 'P2_CLIENT_CODE_FONT_OR_SLASH', severity: 'P2', rule: '#UI-01', desc: 'Auf Kunden-Webseiten sind JetBrains Mono, //-Code-Striche und vorangestellte ::before-Striche in Kickern/Badges strikt verboten' },
  { id: 'S-18', code: 'P2_MODAL_OVERLAP_LEAK', severity: 'P2', rule: '#UI-06', desc: 'Bei geoeffnetem Modal darf kein Hintergrund-Widget (#acp-draft-widget) ueber das Modal ragen' },
  { id: 'S-19', code: 'P1_TEXT_BLEEDS_CONTAINER', severity: 'P1', rule: '#UI-14', desc: 'Kein Wort/Textknoten darf horizontal ueber den rechten/linken Rand seines Buttons, Badges oder seiner Karte hinausragen' },
  { id: 'S-20', code: 'P2_FORM_INPUT_MISALIGNMENT', severity: 'P2', rule: '#UI-02', desc: 'Nebeneinanderliegende Formular-Inputs in derselben Zeile muessen auf exakt gleicher vertikaler Hoehe (top) sitzen' },
  { id: 'S-21', code: 'P2_UGLY_MID_WORD_BREAK', severity: 'P2', rule: '#UI-14', desc: 'Einzelne Woerter (>= 4 Buchstaben ohne Bindestrich) duerfen in Buttons, Pillen oder schmalen Containern (< 180px) nicht mitten im Wort auf 2 Zeilen umbrechen' },
  { id: 'S-22', code: 'P1_NAV_MULTILINE_WRAP', severity: 'P1', rule: '#UI-02', desc: 'Hauptnavigation im Header darf auf Desktop/Laptop (>= 1024px) niemals zweizeilig umbrechen (maxTop - minTop <= 10px, linkHeight <= 46px)' },
  { id: 'S-23', code: 'P2_SPLIT_BOTTOM_STEP', severity: 'P2', rule: '#UI-02', desc: 'In 2-Spalten-Sektionen (.hero-grid, .split-grid, .two-col-grid) auf Desktop (>= 1024px) muessen linke und rechte Spalte unten buendig abschliessen (kein Treppen-Versatz 8..110px)' },
  { id: 'S-24', code: 'P2_HERO_CTA_STACKED_ON_DESKTOP', severity: 'P2', rule: '#UI-02', desc: 'Benachbarte Hero-Action-Buttons duerfen in breiten Desktop-Spalten (>= 480px) nicht unnoetig vertikal untereinander stapeln, wenn sie nebeneinander passen' },
  { id: 'S-25', code: 'P2_CARD_EXCESSIVE_DEAD_SPACE', severity: 'P2', rule: '#UI-02', desc: 'Gerahmte Karten (.card, .content-card, .hero-card, .hero-media-card) duerfen auf Desktop nicht > 90px leeren Totraum unter ihrem Inhalt aufweisen' },
  { id: 'S-26', code: 'P1_LOW_CONTRAST_GHOST', severity: 'P1', rule: '#UI-01', desc: 'Sichtbarer Text muss gegenueber seinem effektiven Hintergrund (inkl. RGBA-Alpha-Blending & CSS linear-/radial-gradient Farb-Stops) ein Kontrastverhaeltnis >= 2.2:1 aufweisen (kein Dunkel-auf-Dunkel oder Weiss-auf-Weiss)' },
  { id: 'S-27', code: 'P1_EVOLUTION_POLARITY_MISMATCH', severity: 'P1', rule: '#UI-16', desc: 'Im Evolution-Modus mit heller Ursprungsseite (target_hero_polarity === "light") darf die Startbuehne (.hero-section, .hero, main > section:first-of-type) niemals dunkel (< 0.45 Luminanz) gebaut werden' },
  { id: 'S-28', code: 'P2_MULTILINE_CELL_INDENT_DRIFT', severity: 'P2', rule: '#UI-02', desc: 'In mehrzeiligen Tabellenzellen, Listen-Spalten oder Flex/Grid-Zellen muessen untereinanderliegende Zeilen exakt auf derselben linken/rechten Fluchtlinie starten (kein margin-left-Versatz auf Zeile 2, Toleranz <= 2.5px)' },
  { id: 'S-29', code: 'P2_CROSS_ROW_RHYTHM_MISMATCH', severity: 'P2', rule: '#UI-02', desc: 'Aufeinanderfolgende Listen-Zeilen gleicher Signatur muessen in allen Spalten exakt fluchten (x-Abweichung <= 3px) und wiederkehrende Tags/Badges im selben Stockwerk (y-Rhythmus) fuehren' },
  { id: 'S-30', code: 'P2_TYPOGRAPHIC_PLENK_OR_ASCII_ORT', severity: 'P2', rule: '#LANG-01/#LANG-06', desc: 'Keine Leerzeichen vor Kommas (Plenk), keine unkorrigierten Schweizer ASCII-Umlaut-Ortsnamen (Zuerich etc.), kein englischer KI-Geviertstrich ((?<!\.)\u2014) sowie 0 Kunden-Klarnamen/Geheimnis-Begriffe (#LANG-06) auf oeffentlichen Produktseiten' },
  { id: 'S-31', code: 'P2_SIBLING_CARD_ANATOMY_DRIFT', severity: 'P2', rule: '#UI-02', desc: 'Nebeneinanderliegende Kacheln in 2er-/3er-/4er-Grids muessen sowohl aussen (2D-Spaltenflucht) als auch innen (Kicker-, Ueberschrift- und Textstart-Horizont) miteinander fluchten' }
];

/**
 * Browser-side evaluation function executed via page.evaluate(evaluateSystemEyesInPage, { relPage, zone, options })
 */
export function evaluateSystemEyesInPage({ relPage, zone, options = {} }) {
  const VW = window.innerWidth;
  const VH = window.innerHeight;
  const findings = [];
  const seen = new Set();
  const isCockpit = relPage.includes('cockpit.html') || Boolean(document.querySelector('.acp-cockpit-bar'));
  const activeScopeSelector = options.activeScopeSelector || null;
  const rawModals = Array.from(
    document.querySelectorAll(
      '[data-acp-modal-title], .modal-overlay.active, #formatSelectModal[style*="flex"], #historyModal[style*="flex"], #erfassungZenSidebar.open, #erfassungOnboardingIntroModal, [id$="Modal"][style*="flex"], [id*="Modal"][style*="fixed"][style*="flex"]'
    )
  ).filter(m => isVisible(m));
  const openModals = rawModals.filter(m => !rawModals.some(other => other !== m && other.contains(m)));
  const scopeRoot = activeScopeSelector
    ? document.querySelector(activeScopeSelector)
    : openModals.length > 0
      ? openModals[openModals.length - 1]
      : document.body;

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
      el.getAttribute('title') ||
      el.innerText ||
      el.textContent ||
      el.getAttribute('placeholder') ||
      el.getAttribute('alt') ||
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

  function getLayerContext(node) {
    let cur = node;
    while (cur && cur.nodeType === 1 && cur !== document.body) {
      if (
        cur.classList.contains('acp-modal-backdrop') ||
        cur.classList.contains('wp-partner-modal-backdrop') ||
        cur.id === 'wpPartnerModal' ||
        cur.id === 'acp-replace-section-modal' ||
        cur.id === 'acp-new-section-modal' ||
        cur.id === 'acp-job-dropdown' ||
        cur.id === 'acp-draft-panel' ||
        cur.id === 'acp-draft-widget' ||
        cur.id === 'acp-inline-edit-dock' ||
        cur.id === 'acp-swap-dock' ||
        cur.id === 'mobileNavDrawer' ||
        cur.id === 'mobileDrawer' ||
        cur.id === 'navDrawer'
      ) {
        return cur;
      }
      const st = window.getComputedStyle(cur);
      if (st.position === 'fixed' || st.position === 'sticky') return cur;
      cur = cur.parentElement;
    }
    return document.body;
  }

  if (activeScopeSelector && (!scopeRoot || !isVisible(scopeRoot))) {
    addFinding('P1', 'P1_UNREACHABLE_OFFSCREEN', activeScopeSelector, activeScopeSelector, `Angeforderte Ansicht/Modal (${activeScopeSelector}) ist nach dem Oeffnen nicht sichtbar!`);
    return findings;
  }

  const queryRoot = scopeRoot || document.body;

  // S-01: P1_HORIZONTAL_OVERFLOW
  const docScrollW = document.documentElement.scrollWidth;
  if (docScrollW > VW + 1) {
    addFinding('P1', 'P1_HORIZONTAL_OVERFLOW', 'document.documentElement', 'html', `scrollWidth=${docScrollW}px > innerWidth=${VW}px`);
  }

  // S-03b: Dialog Modal Bottom CTA Viewport Fit (#UI-14)
  if (activeScopeSelector === '#acp-replace-section-modal' || activeScopeSelector === '#acp-new-section-modal') {
    const dialogBtns = scopeRoot.querySelectorAll('.acp-btn-primary, .acp-btn-secondary');
    for (const btn of dialogBtns) {
      if (!isVisible(btn)) continue;
      const r = btn.getBoundingClientRect();
      if (r.bottom > VH - 2 || r.top < 2) {
        addFinding('P1', 'P1_UNREACHABLE_OFFSCREEN', selectorFor(btn), textOf(btn), `Dialog button clipped vertically in viewport (top=${Math.round(r.top)}px, bottom=${Math.round(r.bottom)}px vs VH=${VH}px)`);
      }
    }
  }

  // S-18: P2_MODAL_OVERLAP_LEAK (Floating Draft Widget visible while a modal or dock is open)
  if (isCockpit && activeScopeSelector && (activeScopeSelector.includes('modal') || activeScopeSelector.includes('dock'))) {
    const draftWidget = document.getElementById('acp-draft-widget');
    if (draftWidget && isVisible(draftWidget)) {
      addFinding('P2', 'P2_MODAL_OVERLAP_LEAK', 'acp-draft-widget', '#acp-draft-widget', `Schwebende Entwurf-Pille (#acp-draft-widget) bleibt ueber geoeffnetem Modal (${activeScopeSelector}) sichtbar`);
    }
  }

  // S-02, S-03, S-10, S-13: Interactive elements check
  const interactiveEls = Array.from(queryRoot.querySelectorAll('a[href], button, input:not([type="hidden"]), select, textarea, [role="button"]')).filter(isVisible);
  for (const el of interactiveEls) {
    const r = el.getBoundingClientRect();
    const lbl = getLabel(el);
    const sel = getCssPath(el);

    // Check if inside a horizontal scroll wrapper (e.g. .acp-jobs-table-wrap or .acp-filter-pills with overflow-x: auto)
    const hScrollAnc = el.closest('.acp-jobs-table-wrap, [data-allow-x-scroll="true"]');
    if (!hScrollAnc) {
      if (r.left < -1 || r.right > VW + 1) {
        addFinding('P1', 'P1_OFFSCREEN_X', lbl, sel, `left=${Math.round(r.left)}px, right=${Math.round(r.right)}px (VW=${VW}px)`);
      } else if (VW === 375 && el.closest('.mobile-thumb-bar, .thumb-bar')) {
        if (r.left < 8 || r.right > 367) {
          addFinding('P1', 'P1_OFFSCREEN_X', lbl, sel, `Mobile-Bar Button zu nah am Rand: left=${Math.round(r.left)}px, right=${Math.round(r.right)}px (Pflicht 8..367px)`);
        }
      }
    }

    if (VW < 769) {
      const isCheckOrRadio = el.tagName === 'INPUT' && (el.type === 'checkbox' || el.type === 'radio');
      const parentLabel = isCheckOrRadio ? el.closest('label') : null;
      const touchR = parentLabel ? parentLabel.getBoundingClientRect() : r;
      if (touchR.width < 34 || touchR.height < 30) {
        addFinding('P2', 'P2_CRAMPED_MOBILE', lbl, sel, `Touch-Flaeche zu klein auf Mobile: ${Math.round(touchR.width)}x${Math.round(touchR.height)}px (Pflicht >= 34x30px)`);
      }
    }

    if (el.tagName === 'BUTTON') {
      const hasText = (el.innerText || el.textContent || '').trim().length > 0;
      const hasIcon = Boolean(el.querySelector('svg, img, .acp-brand-signet'));
      if (!hasText && !hasIcon) {
        addFinding('P2', 'P2_UNSTYLED_OR_EMPTY_BUTTON', lbl || 'empty-button', sel, 'Button besitzt weder sichtbaren Text noch ein SVG-Icon (leerer Kasten)');
      }
    }
  }

  // S-04: P1_ELEMENT_COLLISION (Union Bounding-Box aus Element-Rect + unbeschnittener direkter Text-Range)
  const collisionItems = interactiveEls.map(el => {
    const r = el.getBoundingClientRect();
    let unionLeft = r.left;
    let unionRight = r.right;
    let unionTop = r.top;
    let unionBottom = r.bottom;
    const nCs = window.getComputedStyle(el);
    const parentEl = el.parentElement;
    const pCs = parentEl ? window.getComputedStyle(parentEl) : null;
    const isClippedX =
      nCs.overflowX === 'hidden' || nCs.overflowX === 'clip' || nCs.textOverflow === 'ellipsis' ||
      (pCs && (pCs.overflowX === 'hidden' || pCs.overflowX === 'clip'));
    if (!isClippedX) {
      for (let ch = el.firstChild; ch; ch = ch.nextSibling) {
        if (ch.nodeType === 3 && ch.nodeValue && ch.nodeValue.trim().length > 0) {
          const rng = document.createRange();
          rng.selectNodeContents(ch);
          const tr = rng.getBoundingClientRect();
          if (tr.width > 0 && tr.height > 0) {
            unionLeft = Math.min(unionLeft, tr.left);
            unionRight = Math.max(unionRight, tr.right);
            unionTop = Math.min(unionTop, tr.top);
            unionBottom = Math.max(unionBottom, tr.bottom);
          }
        }
      }
    }
    return {
      el,
      rect: {
        left: unionLeft,
        right: unionRight,
        top: unionTop,
        bottom: unionBottom,
        width: unionRight - unionLeft,
        height: unionBottom - unionTop
      },
      layerAnc: getLayerContext(el)
    };
  });
  for (let i = 0; i < collisionItems.length; i++) {
    const A = collisionItems[i];
    for (let j = i + 1; j < collisionItems.length; j++) {
      const B = collisionItems[j];
      if (A.el.contains(B.el) || B.el.contains(A.el)) continue;
      if (A.layerAnc !== B.layerAnc) continue;
      const overlapW = Math.min(A.rect.right, B.rect.right) - Math.max(A.rect.left, B.rect.left);
      const overlapH = Math.min(A.rect.bottom, B.rect.bottom) - Math.max(A.rect.top, B.rect.top);
      if (overlapW > 4 && overlapH > 4) {
        addFinding('P1', 'P1_ELEMENT_COLLISION', `${getLabel(A.el)} vs ${getLabel(B.el)}`, getCssPath(A.el), `Overlap ${Math.round(overlapW)}x${Math.round(overlapH)}px`);
      }
    }
  }

    // S-04b: Mobile Burger Drawer vs Sticky Header Collision
  if (activeScopeSelector && (activeScopeSelector.includes('Drawer') || activeScopeSelector.includes('drawer'))) {
    const headerEl = document.querySelector('header, .main-header, .site-header');
    if (headerEl && isVisible(headerEl)) {
      const hRect = headerEl.getBoundingClientRect();
      for (const el of interactiveEls) {
        const r = el.getBoundingClientRect();
        if (r.top < hRect.bottom - 2) {
          addFinding('P1', 'P1_ELEMENT_COLLISION', `${getLabel(el)} vs Sticky Header`, getCssPath(el), `Mobile-Drawer-Link (top=${Math.round(r.top)}px) wird vom Header (bottom=${Math.round(hRect.bottom)}px) ueberlappt`);
        }
      }
    }
  }

  // S-05: P1_MID_SCREEN_SCROLLBAR (Desktop / Laptop)
  if (VW >= 769) {
    const allEls = Array.from(queryRoot.querySelectorAll('*')).filter(isVisible);
    for (const el of allEls) {
      if (
        el.classList.contains('acp-modal-backdrop') ||
        el.classList.contains('acp-modal') ||
        el.classList.contains('acp-modal-body') ||
        el.id === 'acp-replace-section-modal' ||
        el.id === 'acp-new-section-modal' ||
        el.id === 'acp-dropdown-list' ||
        el.id === 'acp-log-console' ||
        el.classList.contains('acp-code-pre') ||
        el.tagName === 'TEXTAREA' ||
        el.hasAttribute('data-allow-scroll')
      ) {
        continue;
      }
      const st = window.getComputedStyle(el);
      if ((st.overflowY === 'auto' || st.overflowY === 'scroll') && el.scrollHeight > el.clientHeight + 4) {
        addFinding('P1', 'P1_MID_SCREEN_SCROLLBAR', getLabel(el), getCssPath(el), `scrollHeight=${el.scrollHeight} > clientHeight=${el.clientHeight}`);
      }
    }
  }

  // S-08: P1_SIDEBAR_OVERFLOW
  const sidebars = Array.from(queryRoot.querySelectorAll('#erfassungZenSidebar, .zen-sidebar')).filter(isVisible);
  for (const sb of sidebars) {
    if (sb.scrollHeight > sb.clientHeight + 4) {
      addFinding('P1', 'P1_SIDEBAR_OVERFLOW', getLabel(sb), getCssPath(sb), `Sidebar scrollt vertikal: scrollHeight=${sb.scrollHeight} > clientHeight=${sb.clientHeight}`);
    }
  }

  // S-09: P1_BROKEN_IMAGE
  const images = Array.from(queryRoot.querySelectorAll('img')).filter(isVisible);
  for (const img of images) {
    const src = img.getAttribute('src') || '';
    if (!src) continue;
    const r = img.getBoundingClientRect();
    const inViewport = r.top < VH && r.bottom > 0;
    if (img.loading === 'lazy' && !inViewport && !img.complete) continue;
    if (!img.complete || img.naturalWidth === 0) {
      addFinding('P1', 'P1_BROKEN_IMAGE', src, getCssPath(img), `Bild defekt oder nicht geladen (src="${src}", complete=${img.complete}, naturalWidth=${img.naturalWidth})`);
    }
  }

  // S-11, S-12, S-13, S-16, S-17: DOM Aesthetics & Typography
  const emojiRe = /[\u{1F1E6}-\u{1F1FF}\u{1F300}-\u{1FAFF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}\u{231A}-\u{23F3}\u2713\u2714\u2717\u2718]/u;
  const allDom = Array.from(queryRoot.querySelectorAll('*')).filter(isVisible);
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

    const cs = window.getComputedStyle(el);
    // S-12: 2-Radius-Architektur (#UI-01: only 0px, 4px, 8px)
    const br = cs.borderTopLeftRadius;
    if (br && br !== '0px' && br !== '4px' && br !== '8px') {
      addFinding('P2', 'P2_BAD_RADIUS', getLabel(el), getCssPath(el), `Unerlaubter border-radius=${br} (Pflicht: 4px oder 8px nach #UI-01)`);
    }

    // S-13: Unstyled browser default buttons
    if (el.tagName === 'BUTTON') {
      if (cs.borderTopStyle === 'outset' || cs.backgroundColor === 'rgb(239, 239, 239)' || cs.backgroundColor === 'buttonface') {
        addFinding('P2', 'P2_UNSTYLED_OR_EMPTY_BUTTON', getLabel(el), getCssPath(el), `Unstyled Browser-Standard-Button gefunden (bg=${cs.backgroundColor}, border=${cs.borderTopStyle})`);
      }
    }

    // S-16: Severe text truncation
    if (cs.textOverflow === 'ellipsis' && (cs.overflow === 'hidden' || cs.overflowX === 'hidden')) {
      const r = el.getBoundingClientRect();
      if (r.width < 110 && el.scrollWidth > el.clientWidth + 4) {
        addFinding('P2', 'P2_SEVERE_TEXT_TRUNCATION', getLabel(el), getCssPath(el), `Text auf ${Math.round(r.width)}px Breite mit Ellipsis abgeschnitten (scrollWidth=${el.scrollWidth}px)`);
      }
    }

    // S-17: Customer Website Typography Guard (#UI-01 Pt 4: No JetBrains Mono, // kickers, or ::before kicker lines on customer sites)
    const isClientSite = !isCockpit && !relPage.startsWith('webpilot/');
    if (isClientSite) {
      if (cs.fontFamily && cs.fontFamily.toLowerCase().includes('jetbrains mono')) {
        addFinding('P2', 'P2_CLIENT_CODE_FONT_OR_SLASH', getLabel(el), getCssPath(el), `Programmierer-Schriftart JetBrains Mono auf Kunden-Webseite verboten (#UI-01 Pt 4)`);
      }
      if (directText.startsWith('// ')) {
        addFinding('P2', 'P2_CLIENT_CODE_FONT_OR_SLASH', getLabel(el), getCssPath(el), `Code-Kommentar-Striche "// " in Kicker/Text auf Kunden-Webseite verboten (#UI-01 Pt 4)`);
      }
      if (el.matches('.section-kicker, .section-tag, .eyebrow, .kicker, .hero-kicker, .calc-kicker, .sub-kicker')) {
        const beforeCs = window.getComputedStyle(el, '::before');
        const bContent = (beforeCs.content || 'none').replace(/^["']|["']$/g, '').trim();
        const bWidth = parseFloat(beforeCs.width || '0');
        const bHeight = parseFloat(beforeCs.height || '0');
        const hasBeforeLine = Boolean(beforeCs.content && beforeCs.content !== 'none' && beforeCs.display !== 'none' && bWidth >= 6 && bHeight > 0 && bHeight <= 4);
        const hasBeforeDash = Boolean(beforeCs.content && beforeCs.content !== 'none' && beforeCs.display !== 'none' && (bContent === '\u2014' || bContent === '\u2013' || bContent === '-'));
        const hasLeadingTextDash = /^[\u2014\u2013]\s*/.test(directText);
        if (hasBeforeLine || hasBeforeDash || hasLeadingTextDash) {
          addFinding('P2', 'P2_CLIENT_CODE_FONT_OR_SLASH', getLabel(el), getCssPath(el), `Kicker hat vorangestellten KI-Strich ::before`);
        }
      }
    }
  }

  // S-14, S-15 & S-31: P2_ROW_HEIGHT_MISMATCH, P2_RAGGED_RIGHT_EDGE & P2_SIBLING_CARD_ANATOMY_DRIFT in Grids (inkl. Auto-Discovery)
  const explicitGridSelector = '.pillar-cards, .vs-grid, .teaser-grid, .price-grid, .story-grid, .values-grid, .arch-grid, .sparten-filter-grid, .subservices-grid, .sparte-ref-row, .quiz-steps-grid, .social-grid, .blog-grid, .team-dept-grid, .timeline-list, .partner-grid, .foerder-grid, .check-grid, .begleitung-grid, .testimonials-grid, .about-grid, .about-trust-bar, [data-acp-bento-grid], [data-eyes-card-grid="true"]';
  const explicitGrids = Array.from(queryRoot.querySelectorAll(explicitGridSelector)).filter(isVisible);
  const gridSet = new Set(explicitGrids);
  if (VW >= 769) {
    for (const cand of allDom) {
      if (gridSet.has(cand)) continue;
      if (cand.closest('nav, header, footer, table, .agenda-toolbar, .toolbar-primary-row, #erfassungZenSidebar, #acpSidebarDrawer, [data-ignore-card-anatomy="true"]')) continue;
      const cCs = window.getComputedStyle(cand);
      if (cCs.display !== 'grid' && cCs.display !== 'flex') continue;
      const visKids = Array.from(cand.children).filter(isVisible);
      if (visKids.length < 2 || visKids.length > 12) continue;
      const firstTag = visKids[0].tagName;
      const firstCls = (typeof visKids[0].className === 'string' ? visKids[0].className.trim().split(/\s+/)[0] : '') || '';
      const allSameType = visKids.every(k => {
        if (k.tagName !== firstTag) return false;
        const kCls = (typeof k.className === 'string' ? k.className.trim().split(/\s+/)[0] : '') || '';
        if (firstCls && kCls !== firstCls) return false;
        const kr = k.getBoundingClientRect();
        if (kr.width < 140 || kr.height < 72) return false;
        const kCs = window.getComputedStyle(k);
        const hasSurface =
          parseFloat(kCs.borderTopWidth || '0') > 0 ||
          parseFloat(kCs.borderLeftWidth || '0') > 0 ||
          (kCs.backgroundColor && kCs.backgroundColor !== 'rgba(0, 0, 0, 0)' && kCs.backgroundColor !== 'transparent') ||
          /\b(card|tile|item|bento|pillar|trust-item)\b/i.test(k.className || '');
        return hasSurface && Array.from(k.children).filter(isVisible).length >= 2;
      });
      if (allSameType) {
        gridSet.add(cand);
      }
    }
  }
  const grids = Array.from(gridSet);
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
    rows.sort((a, b) => a.top - b.top);
    const gRect = g.getBoundingClientRect();
    const gPadR = parseFloat(window.getComputedStyle(g).paddingRight || '0') || 0;
    const expectedRight = gRect.right - gPadR;
    const isExplicitGrid = g.matches(explicitGridSelector);
    for (const rw of rows) {
      rw.items.sort((a, b) => a.rect.left - b.rect.left);
      const lastItem = rw.items[rw.items.length - 1];
      if ((isExplicitGrid || rw.items.length >= 2) && rw.items.length === rows[0].items.length && expectedRight - lastItem.rect.right > 14) {
        addFinding('P2', 'P2_RAGGED_RIGHT_EDGE', getCssPath(g), getCssPath(g), `Rechte Kante ausgefranst: last.right=${Math.round(lastItem.rect.right)}px vs container.right=${Math.round(expectedRight)}px`);
      }
      if (rw.items.length >= 2) {
        const heights = rw.items.map(i => i.rect.height);
        const maxH = Math.max(...heights);
        const minH = Math.min(...heights);
        if (maxH - minH > 4) {
          addFinding('P2', 'P2_ROW_HEIGHT_MISMATCH', getCssPath(g), getCssPath(g), `Karten in derselben Zeile haben ungleiche Hoehe: min=${Math.round(minH)}px vs max=${Math.round(maxH)}px`);
        }
      }
    }

    // S-31a: 2D Multi-Row Column Alignment (z. B. 2x2 4-Kachel-Grid wie .about-grid oder gestapelte Kacheln)
    if (rows.length >= 2) {
      for (let ri = 1; ri < rows.length; ri++) {
        if (rows[ri].items.length !== rows[0].items.length) continue;
        for (let ci = 0; ci < rows[ri].items.length; ci++) {
          const topCard = rows[0].items[ci];
          const curCard = rows[ri].items[ci];
          const leftDiff = Math.abs(curCard.rect.left - topCard.rect.left);
          const widthDiff = Math.abs(curCard.rect.width - topCard.rect.width);
          if (leftDiff > 3 || widthDiff > 3) {
            addFinding(
              'P2',
              'P2_SIBLING_CARD_ANATOMY_DRIFT',
              getLabel(curCard.el),
              getCssPath(curCard.el),
              `2D-Kachel-Spaltenflucht zwischen Reihe 1 und Reihe ${ri + 1} (Spalte ${ci + 1}) verschoben: leftDiff=${leftDiff.toFixed(1)}px, widthDiff=${widthDiff.toFixed(1)}px (Pflicht <= 3px)`
            );
          }
        }
      }
    }

    // S-31b: Innen-Anatomie-Horizont nebeneinanderliegender Kacheln derselben Reihe
    for (let ri = 0; ri < rows.length; ri++) {
      const rw = rows[ri];
      if (rw.items.length < 2) continue;
      const baseCard = rw.items[0];
      const baseKids = Array.from(baseCard.el.children).filter(isVisible);
      if (baseKids.length < 2) continue;
      const getSig = kids =>
        kids
          .map(k => k.tagName + '.' + ((typeof k.className === 'string' ? k.className.trim().split(/\s+/)[0] : '') || ''))
          .join('>');
      const baseSig = getSig(baseKids);

      for (let ci = 1; ci < rw.items.length; ci++) {
        const curCard = rw.items[ci];
        const curKids = Array.from(curCard.el.children).filter(isVisible);
        if (curKids.length < 2 || getSig(curKids) !== baseSig) continue;

        // 1. Erstes sichtbares Kind (Kicker / Nummer / Icon / Heading)
        const r0A = baseKids[0].getBoundingClientRect();
        const r0B = curKids[0].getBoundingClientRect();
        const padLA = r0A.left - baseCard.rect.left;
        const padLB = r0B.left - curCard.rect.left;
        if (Math.abs(r0A.top - r0B.top) > 4 || Math.abs(padLA - padLB) > 3) {
          addFinding(
            'P2',
            'P2_SIBLING_CARD_ANATOMY_DRIFT',
            `${getLabel(baseCard.el)} vs ${getLabel(curCard.el)}`,
            getCssPath(curCard.el),
            `Kachel-Innen-Anatomie (1. Kind) in Reihe ${ri + 1} versetzt: topDiff=${Math.abs(r0A.top - r0B.top).toFixed(1)}px (Pflicht <= 4px), padLeftDiff=${Math.abs(padLA - padLB).toFixed(1)}px (Pflicht <= 3px)`
          );
        }

        // 2. Hauptueberschrift (h2, h3, h4, .card-title, strong:first-child)
        const headA = baseCard.el.querySelector('h2, h3, h4, .card-title, strong:first-child');
        const headB = curCard.el.querySelector('h2, h3, h4, .card-title, strong:first-child');
        if (headA && headB && isVisible(headA) && isVisible(headB)) {
          const rhA = headA.getBoundingClientRect();
          const rhB = headB.getBoundingClientRect();
          if (Math.abs(rhA.top - rhB.top) > 4) {
            addFinding(
              'P2',
              'P2_SIBLING_CARD_ANATOMY_DRIFT',
              `${getLabel(headA)} vs ${getLabel(headB)}`,
              getCssPath(curCard.el),
              `Ueberschriften-Horizont in Nachbar-Kacheln (Reihe ${ri + 1}) versetzt: topA=${Math.round(rhA.top)}px vs topB=${Math.round(rhB.top)}px (Diff=${Math.abs(rhA.top - rhB.top).toFixed(1)}px > 4px)`
            );
          }
        }

        // 3. Erster Fliesstext-Absatz (p / .about-card-sub / span) nach der Ueberschrift
        for (let ki = 1; ki < baseKids.length; ki++) {
          const kA = baseKids[ki];
          const kB = curKids[ki];
          if (!kA.matches('p, .about-card-sub, span')) continue;
          const rpA = kA.getBoundingClientRect();
          const rpB = kB.getBoundingClientRect();
          if (Math.abs(rpA.top - rpB.top) > 6) {
            addFinding(
              'P2',
              'P2_SIBLING_CARD_ANATOMY_DRIFT',
              `${getLabel(baseCard.el)} vs ${getLabel(curCard.el)}`,
              getCssPath(kB),
              `Textstart-Horizont in Nachbar-Kacheln (Reihe ${ri + 1}) versetzt: topA=${Math.round(rpA.top)}px vs topB=${Math.round(rpB.top)}px (Diff=${Math.abs(rpA.top - rpB.top).toFixed(1)}px > 6px)`
            );
            break;
          }
          if (kA.tagName === 'P' && !kA.classList.contains('about-card-sub')) {
            break;
          }
        }
      }
    }
  }

  // S-06 & S-07: P1_STICKY_OCCLUDES_FOOTER & P1_PARTIALLY_OCCLUDED_BY_STICKY (Mobile)
  if (VW < 769 && !activeScopeSelector) {
    const stickyBar = document.querySelector('.mobile-thumb-bar, .thumb-bar');
    const footer = document.querySelector('footer');
    if (stickyBar && isVisible(stickyBar) && footer && isVisible(footer)) {
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


  // S-19: P1_TEXT_BLEEDS_CONTAINER & S-21: P2_UGLY_MID_WORD_BREAK (Text node bleeds outside border or breaks mid-word)
  for (const el of allDom) {
    if (['SCRIPT', 'STYLE', 'SVG', 'PATH', 'HTML', 'BODY', 'TEXTAREA', 'INPUT', 'SELECT'].includes(el.tagName) || el.closest('svg')) continue;
    const textNodes = Array.from(el.childNodes).filter(n => n.nodeType === 3 && n.nodeValue.trim().length > 0);
    if (textNodes.length === 0) continue;
    const boxEl = el.closest('button, a, .role-pill, .topic-chip-btn, .zen-sb-mode-pill, [class*="badge"], [class*="pill"], [class*="btn"], [class*="card"], td, th, label') || el;
    const elCs = window.getComputedStyle(el);
    const boxCs = window.getComputedStyle(boxEl);
    const hasClip =
      elCs.overflowX === 'hidden' || elCs.overflowX === 'clip' || elCs.textOverflow === 'ellipsis' ||
      boxCs.overflowX === 'hidden' || boxCs.overflowX === 'clip' || boxCs.textOverflow === 'ellipsis';
    const bRect = boxEl.getBoundingClientRect();
    if (bRect.width < 16 || bRect.height < 12) continue;
    const isFramedPillOrBtn = boxEl.matches('button, .role-pill, .zen-sb-mode-pill, [class*="badge"], [class*="pill"], [class*="btn"]') &&
      (parseFloat(boxCs.borderLeftWidth) > 0 || parseFloat(boxCs.borderRightWidth) > 0 || (boxCs.backgroundColor && boxCs.backgroundColor !== 'rgba(0, 0, 0, 0)' && boxCs.backgroundColor !== 'transparent'));
    const fontSize = parseFloat(elCs.fontSize) || 13;
    const lineHeight = parseFloat(elCs.lineHeight) || (fontSize * 1.35);
    for (const tn of textNodes) {
      const range = document.createRange();
      range.selectNodeContents(tn);
      const rRect = range.getBoundingClientRect();
      if (rRect.width === 0 || rRect.height === 0) continue;
      if (!hasClip) {
        if (rRect.right > bRect.right + 1.5 || rRect.left < bRect.left - 1.5) {
          addFinding('P1', 'P1_TEXT_BLEEDS_CONTAINER', getLabel(boxEl), getCssPath(boxEl), `Text ragt ueber Element-Rahmen hinaus: textRight=${Math.round(rRect.right)}px > boxRight=${Math.round(bRect.right)}px`);
        } else if (isFramedPillOrBtn && tn.nodeValue.trim().length >= 4 && bRect.width >= 36 && bRect.width <= 180 && (bRect.right - rRect.right < 1.5 || rRect.left - bRect.left < 1.5)) {
          addFinding('P1', 'P1_TEXT_BLEEDS_CONTAINER', getLabel(boxEl), getCssPath(boxEl), `Text klebt ohne Innenabstand (< 1.5px) am Pillen-/Button-Rand: insetL=${(rRect.left - bRect.left).toFixed(1)}px, insetR=${(bRect.right - rRect.right).toFixed(1)}px`);
        }
      }
      if (rRect.height > lineHeight * 1.55 && bRect.width < 180) {
        const rawText = tn.nodeValue || '';
        const wordRegex = /[A-Za-zÄÖÜäöü]{4,}/g;
        let match;
        while ((match = wordRegex.exec(rawText)) !== null) {
          const startIdx = match.index;
          const endIdx = match.index + match[0].length;
          const firstRange = document.createRange();
          firstRange.setStart(tn, startIdx);
          firstRange.setEnd(tn, startIdx + 1);
          const lastRange = document.createRange();
          lastRange.setStart(tn, endIdx - 1);
          lastRange.setEnd(tn, endIdx);
          const fRect = firstRange.getBoundingClientRect();
          const lRect = lastRange.getBoundingClientRect();
          if (fRect.width > 0.5 && lRect.width > 0.5 && Math.abs(lRect.top - fRect.top) > lineHeight * 0.55) {
          const wRects = [fRect, lRect];
            addFinding('P2', 'P2_UGLY_MID_WORD_BREAK', getLabel(boxEl), getCssPath(boxEl), `Wort "${match[0]}" bricht mitten im Wort ohne Bindestrich auf ${wRects.length} Zeilen um (Container-Breite ${Math.round(bRect.width)}px)`);
            break;
          }
        }
      }
    }
  }

  // S-20: P2_FORM_INPUT_MISALIGNMENT (Sibling inputs in same form row must share exact same top coordinate)
  const formInputs = Array.from(queryRoot.querySelectorAll('input:not([type="hidden"]):not([type="checkbox"]):not([type="radio"]), select, textarea')).filter(isVisible);
  for (let i = 0; i < formInputs.length; i++) {
    for (let j = i + 1; j < formInputs.length; j++) {
      const A = formInputs[i], B = formInputs[j];
      const pA = A.parentElement, pB = B.parentElement;
      if (!pA || !pB || pA.parentElement !== pB.parentElement) continue;
      const rPA = pA.getBoundingClientRect(), rPB = pB.getBoundingClientRect();
      if (Math.abs(rPA.left - rPB.left) > 20 && Math.abs(rPA.top - rPB.top) <= 30) {
        const rA = A.getBoundingClientRect(), rB = B.getBoundingClientRect();
        if (Math.abs(rA.top - rB.top) > 2) {
          addFinding('P2', 'P2_FORM_INPUT_MISALIGNMENT', `${getLabel(A)} vs ${getLabel(B)}`, getCssPath(A), `Formular-Inputs in derselben Zeile vertikal versetzt: topA=${Math.round(rA.top)}px vs topB=${Math.round(rB.top)}px`);
        }
      }
    }
  }


  // S-22..S-25: Grafik- & Proportions-Harmonie-Sensoren auf Desktop/Laptop (VW >= 1024)
  if (VW >= 1024 && !isCockpit && !activeScopeSelector && !relPage.startsWith('partner/')) {
    // S-22: P1_NAV_MULTILINE_WRAP
    const navContainers = Array.from(queryRoot.querySelectorAll('header nav, .site-header nav, .main-header nav, .main-nav, .nav-links')).filter(
      el => isVisible(el) && !el.closest('.mobile-drawer, #mobileDrawer, #navDrawer, #mobileNavDrawer, footer, .site-footer')
    );
    for (const navEl of navContainers) {
      const navItems = Array.from(navEl.querySelectorAll('a, button')).filter(
        el => isVisible(el) && !el.closest('.dropdown-menu, .sub-menu, .mobile-drawer, #mobileDrawer, #navDrawer, #mobileNavDrawer')
      );
      if (navItems.length >= 2) {
        const rects = navItems.map(el => el.getBoundingClientRect());
        const tops = rects.map(r => r.top);
        const minTop = Math.min(...tops);
        const maxTop = Math.max(...tops);
        if (maxTop - minTop > 10) {
          addFinding(
            'P1',
            'P1_NAV_MULTILINE_WRAP',
            getLabel(navEl),
            getCssPath(navEl),
            `Hauptnavigation bricht auf Desktop (${VW}px) mehrzeilig um: maxTop-minTop=${Math.round(maxTop - minTop)}px (Pflicht <= 10px)`
          );
        }
        for (let idx = 0; idx < navItems.length; idx++) {
          const item = navItems[idx];
          const r = rects[idx];
          const itemCs = window.getComputedStyle(item);
          if (r.height > 46 && itemCs.flexDirection !== 'column') {
            addFinding(
              'P1',
              'P1_NAV_MULTILINE_WRAP',
              getLabel(item),
              getCssPath(item),
              `Hauptmenue-Link bricht auf Desktop (${VW}px) zweizeilig um: height=${Math.round(r.height)}px (Pflicht <= 46px)`
            );
          }
        }
      }
    }

    // S-23: P2_SPLIT_BOTTOM_STEP
    function getVisualColumnBottom(col) {
      const cRect = col.getBoundingClientRect();
      const cs = window.getComputedStyle(col);
      const hasFrame =
        parseFloat(cs.borderBottomWidth || '0') > 0 ||
        (cs.backgroundColor && cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && cs.backgroundColor !== 'transparent');
      const kids = Array.from(col.children).filter(isVisible);
      if (hasFrame || kids.length === 0) {
        return cRect.bottom;
      }
      return Math.max(...kids.map(k => getVisualColumnBottom(k)));
    }

    const splitGrids = Array.from(queryRoot.querySelectorAll('.hero-grid, .split-grid, .two-col-grid')).filter(isVisible);
    for (const sg of splitGrids) {
      const cols = Array.from(sg.children).filter(isVisible);
      if (cols.length !== 2) continue;
      const r0 = cols[0].getBoundingClientRect();
      const r1 = cols[1].getBoundingClientRect();
      const vOverlap = Math.min(r0.bottom, r1.bottom) - Math.max(r0.top, r1.top);
      if (r1.left < r0.right - 16 || vOverlap < 40) continue;
      const leftBottom = getVisualColumnBottom(cols[0]);
      const rightBottom = getVisualColumnBottom(cols[1]);
      const diff = Math.abs(leftBottom - rightBottom);
      if (diff > 8 && diff <= 110) {
        addFinding(
          'P2',
          'P2_SPLIT_BOTTOM_STEP',
          getCssPath(sg),
          getCssPath(sg),
          `Untere Grundlinien-Treppenstufe in 2-Spalten-Sektion: leftBottom=${Math.round(leftBottom)}px vs rightBottom=${Math.round(rightBottom)}px (Versatz=${Math.round(diff)}px, Pflicht <= 8px)`
        );
      }
    }

    // S-24: P2_HERO_CTA_STACKED_ON_DESKTOP
    const ctaContainers = Array.from(queryRoot.querySelectorAll('.hero-actions, .hero-cta, .hero-btns, .cta-actions')).filter(isVisible);
    for (const actEl of ctaContainers) {
      const pRect = actEl.getBoundingClientRect();
      if (pRect.width < 480) continue;
      const btns = Array.from(actEl.children).filter(c => isVisible(c) && c.matches('a, button, .btn, .btn-cta, [class*="btn"]'));
      if (btns.length >= 2) {
        const rA = btns[0].getBoundingClientRect();
        const rB = btns[1].getBoundingClientRect();
        if (rB.top > rA.top + 20 && (rA.width + rB.width <= pRect.width + 24)) {
          addFinding(
            'P2',
            'P2_HERO_CTA_STACKED_ON_DESKTOP',
            `${getLabel(btns[0])} + ${getLabel(btns[1])}`,
            getCssPath(actEl),
            `Action-Buttons in breiter Desktop-Spalte (${Math.round(pRect.width)}px) unnoetig vertikal gestapelt: topA=${Math.round(rA.top)}px, topB=${Math.round(rB.top)}px`
          );
        }
      }
    }

    // S-25: P2_CARD_EXCESSIVE_DEAD_SPACE
    const framedCards = Array.from(queryRoot.querySelectorAll('.card, .content-card, .hero-card, .hero-media-card')).filter(isVisible);
    for (const card of framedCards) {
      const cCs = window.getComputedStyle(card);
      if (cCs.justifyContent === 'space-between' || cCs.justifyContent === 'space-around' || cCs.justifyContent === 'center') continue;
      const kids = Array.from(card.children).filter(isVisible);
      if (kids.length === 0) continue;
      const cRect = card.getBoundingClientRect();
      const lastKidBottom = Math.max(...kids.map(k => k.getBoundingClientRect().bottom));
      const padB = parseFloat(cCs.paddingBottom || '0') || 0;
      const deadSpace = cRect.bottom - padB - lastKidBottom;
      if (deadSpace > 90) {
        addFinding(
          'P2',
          'P2_CARD_EXCESSIVE_DEAD_SPACE',
          getLabel(card),
          getCssPath(card),
          `Karte hat auf Desktop ${Math.round(deadSpace)}px leeren Totraum am unteren Rand (cardBottom=${Math.round(cRect.bottom)}px vs contentBottom=${Math.round(lastKidBottom)}px)`
        );
      }
    }
  }

  // S-26: P1_LOW_CONTRAST_GHOST (Alpha-blended backgroundColor + CSS linear/radial-gradient stop contrast)
  if (!isCockpit) {
    function parseRgbaStops(str) {
      if (!str) return [];
      const out = [];
      const re = /rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)/g;
      let m;
      while ((m = re.exec(str)) !== null) {
        const a = m[4] !== undefined ? parseFloat(m[4]) : 1;
        if (a > 0.01) out.push([+m[1], +m[2], +m[3], a]);
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
        if (cs.webkitBackgroundClip === 'text' || cs.backgroundClip === 'text') {
          cur = cur.parentElement;
          continue;
        }
        if (cs.backgroundImage && cs.backgroundImage.includes('gradient')) {
          const gcols = parseRgbaStops(cs.backgroundImage);
          const opaqueStops = gcols.filter(c => c[3] >= 0.85);
          const stops = opaqueStops.length > 0 ? opaqueStops : gcols;
          if (stops.length >= 1) {
            const avg = [0, 0, 0, 0];
            stops.forEach(c => { avg[0] += c[0]; avg[1] += c[1]; avg[2] += c[2]; avg[3] += c[3]; });
            const layer = [avg[0] / stops.length, avg[1] / stops.length, avg[2] / stops.length, avg[3] / stops.length];
            layers.push(layer);
            if (layer[3] >= 0.95) break;
          }
        }
        const bgc = parseRgbaStops(cs.backgroundColor);
        if (bgc.length > 0) {
          layers.push(bgc[0]);
          if (bgc[0][3] >= 0.95) break;
        }
        cur = cur.parentElement;
      }
      let base = [255, 255, 255];
      const bodyBg = parseRgbaStops(window.getComputedStyle(document.body).backgroundColor);
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
      return 0.2126 * a[0] + 0.7152 * a[1] + 0.0722 * a[2];
    }
    function contrastRatio(c1, c2) {
      const l1 = relLum(c1), l2 = relLum(c2);
      return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
    }
    for (const el of allDom) {
      if (['SCRIPT', 'STYLE', 'SVG', 'PATH', 'HTML', 'BODY', 'INPUT', 'SELECT', 'TEXTAREA'].includes(el.tagName) || el.closest('svg')) continue;
      const r = el.getBoundingClientRect();
      if (r.width < 10 || r.height < 10) continue;
      const cs = window.getComputedStyle(el);
      if (parseFloat(cs.opacity || '1') < 0.25 || cs.webkitTextFillColor === 'transparent') continue;
      let directText = '';
      for (const n of el.childNodes) {
        if (n.nodeType === 3) directText += n.textContent;
      }
      directText = directText.trim();
      if (!directText) continue;
      const fgRgba = parseRgbaStops(cs.color)[0];
      if (!fgRgba) continue;
      const bg = getEffectiveBgRgb(el);
      const fg = blendRgba(fgRgba, bg);
      // Exclude official WhatsApp brand green #25D366 (rgb 37,211,102) with white text (ratio 1.98)
      if ((bg[0] === 37 && bg[1] === 211 && bg[2] === 102) || (fg[0] === 37 && fg[1] === 211 && fg[2] === 102)) continue;
      const ratio = contrastRatio(fg, bg);
      if (ratio < 2.2) {
        addFinding(
          'P1',
          'P1_LOW_CONTRAST_GHOST',
          getLabel(el),
          getCssPath(el),
          `Unlesbarer Text-Kontrast ${ratio.toFixed(2)}:1 (fg=rgb(${fg.join(',')}) auf bg=rgb(${bg.join(',')}), Pflicht >= 2.2:1)`
        );
      }
    }

    // S-27: P1_EVOLUTION_POLARITY_MISMATCH (#UI-16 Evolution-Licht-Sperre fuer Startbuehne/Hero)
    if (!activeScopeSelector && !relPage.endsWith('onboarding.html')) {
      const expectedHeroPolarity =
        (options &&
          options.sourceVisualDna &&
          options.sourceVisualDna.sommelier_decisions &&
          options.sourceVisualDna.sommelier_decisions.polarity_decision &&
          options.sourceVisualDna.sommelier_decisions.polarity_decision.target_hero_polarity) ||
        (options && options.sourceVisualDna && options.sourceVisualDna.target_hero_polarity) ||
        (options && options.expectedHeroPolarity) ||
        window.__WP_EXPECTED_HERO_POLARITY ||
        document.documentElement.getAttribute('data-expected-hero-polarity') ||
        (document.body && document.body.getAttribute('data-expected-hero-polarity')) ||
        null;
      const designMode =
        (options && options.sourceVisualDna && options.sourceVisualDna.design_mode) ||
        document.documentElement.getAttribute('data-design-mode') ||
        'evolution';
      if (expectedHeroPolarity === 'light' && designMode !== 'redesign') {
        const heroCandidate = document.querySelector(
          '.hero-section, section.hero, .hero, .hero-wrap, [data-section="hero"], main > section:first-of-type, body > section:first-of-type'
        );
        if (heroCandidate && isVisible(heroCandidate)) {
          const heroBg = getEffectiveBgRgb(heroCandidate);
          const heroLum = relLum(heroBg);
          if (heroLum < 0.45) {
            addFinding(
              'P1',
              'P1_EVOLUTION_POLARITY_MISMATCH',
              getLabel(heroCandidate),
              getCssPath(heroCandidate),
              `Evolution-Licht-Sperre (#UI-16) verletzt: Ursprungsseite verlangt target_hero_polarity="light", aber gerenderte Startbuehne ist dunkel (Luminanz=${heroLum.toFixed(2)} < 0.45, bg=rgb(${heroBg.join(',')}), Pflicht >= 0.45)`
            );
          }
        }
      }
    }
  }

  // S-28: P2_MULTILINE_CELL_INDENT_DRIFT (Intra-Zellen-Fluchtlinie bei mehrzeiligen Zellen)
  const multilineCells = Array.from(
    queryRoot.querySelectorAll('.agenda-date, .agenda-badges, [data-eyes-cell="true"], [data-acp-multiline-cell="true"], [data-acp-path*="row"] > div')
  ).filter(isVisible);
  for (const cell of multilineCells) {
    if (cell.closest('[data-ignore-cell-indent="true"]')) continue;
    const cellCs = window.getComputedStyle(cell);
    const isRightAligned =
      cellCs.alignItems === 'flex-end' ||
      cellCs.alignItems === 'end' ||
      cellCs.textAlign === 'right' ||
      cellCs.textAlign === 'end';
    const isLeftAligned =
      !isRightAligned &&
      cellCs.alignItems !== 'center' &&
      cellCs.justifyContent !== 'center' &&
      cellCs.justifyContent !== 'flex-end' &&
      cellCs.justifyContent !== 'space-between' &&
      cellCs.textAlign !== 'center';
    if (!isLeftAligned && !isRightAligned) continue;

    const cellItems = [];
    for (const node of cell.childNodes) {
      if (node.nodeType === 3 && node.nodeValue && node.nodeValue.trim().length > 0) {
        const rng = document.createRange();
        rng.selectNodeContents(node);
        const rects = rng.getClientRects();
        if (rects.length > 0 && rects[0].width > 1 && rects[0].height > 1) {
          cellItems.push({ rect: rects[0], label: node.nodeValue.trim().slice(0, 30) });
        }
      } else if (node.nodeType === 1 && isVisible(node)) {
        let targetEl = node;
        const nCs = window.getComputedStyle(node);
        const hasOwnBox =
          parseFloat(nCs.borderLeftWidth || '0') > 0 ||
          parseFloat(nCs.paddingLeft || '0') > 0 ||
          (nCs.backgroundColor && nCs.backgroundColor !== 'rgba(0, 0, 0, 0)' && nCs.backgroundColor !== 'transparent');
        if (!hasOwnBox && node.children.length > 0) {
          const firstVisChild = Array.from(node.children).find(isVisible);
          if (firstVisChild) targetEl = firstVisChild;
        }
        const r = targetEl.getBoundingClientRect();
        const fullR = node.getBoundingClientRect();
        cellItems.push({
          rect: { left: r.left, right: fullR.right, top: fullR.top, bottom: fullR.bottom, width: fullR.width, height: fullR.height },
          label: getLabel(node)
        });
      }
    }
    if (cellItems.length < 2) continue;
    const cellLines = [];
    for (const it of cellItems) {
      let ln = cellLines.find(l => Math.abs(l.top - it.rect.top) <= 10);
      if (!ln) {
        ln = { top: it.rect.top, items: [] };
        cellLines.push(ln);
      }
      ln.items.push(it);
    }
    if (cellLines.length < 2) continue;
    cellLines.sort((a, b) => a.top - b.top);
    for (const ln of cellLines) {
      ln.items.sort((a, b) => a.rect.left - b.rect.left);
    }
    const row1First = cellLines[0].items[0];
    const row1Last = cellLines[0].items[cellLines[0].items.length - 1];
    for (let li = 1; li < cellLines.length; li++) {
      const rowNFirst = cellLines[li].items[0];
      const rowNLast = cellLines[li].items[cellLines[li].items.length - 1];
      if (isLeftAligned) {
        const driftL = Math.abs(rowNFirst.rect.left - row1First.rect.left);
        if (driftL > 2.5) {
          addFinding(
            'P2',
            'P2_MULTILINE_CELL_INDENT_DRIFT',
            getLabel(cell),
            getCssPath(cell),
            `Mehrzeilige Zelle fluchtet links nicht: Zeile 1 ("${row1First.label}") bei x=${row1First.rect.left.toFixed(1)}px vs Zeile ${li + 1} ("${rowNFirst.label}") bei x=${rowNFirst.rect.left.toFixed(1)}px (Versatz=${driftL.toFixed(1)}px > 2.5px)`
          );
          break;
        }
      } else if (isRightAligned) {
        const driftR = Math.abs(rowNLast.rect.right - row1Last.rect.right);
        if (driftR > 2.5) {
          addFinding(
            'P2',
            'P2_MULTILINE_CELL_INDENT_DRIFT',
            getLabel(cell),
            getCssPath(cell),
            `Rechtsbuendige mehrzeilige Zelle fluchtet rechts nicht: Zeile 1 bei right=${row1Last.rect.right.toFixed(1)}px vs Zeile ${li + 1} bei right=${rowNLast.rect.right.toFixed(1)}px (Versatz=${driftR.toFixed(1)}px > 2.5px)`
          );
          break;
        }
      }
    }
  }

  // S-29: P2_CROSS_ROW_RHYTHM_MISMATCH (Zeilenuebergreifender Mehrzeilen-Abgleich in Listen)
  const rowCandidates = Array.from(
    queryRoot.querySelectorAll('.agenda-row, [data-acp-path="1000-cockpit.zen.posts.row"], [data-acp-path="1000-cockpit.zen.stage.compact_row"], .list-row, [data-eyes-row="true"]')
  ).filter(isVisible);
  const rowsByParent = new Map();
  for (const rEl of rowCandidates) {
    const p = rEl.parentElement;
    if (!p) continue;
    const sig =
      rEl.tagName +
      '.' +
      ((typeof rEl.className === 'string' ? rEl.className.trim().split(/\s+/).slice(0, 2).join('.') : '') || '') +
      '|' +
      (rEl.getAttribute('data-acp-path') || '');
    if (!rowsByParent.has(p)) rowsByParent.set(p, new Map());
    const sigMap = rowsByParent.get(p);
    if (!sigMap.has(sig)) sigMap.set(sig, []);
    sigMap.get(sig).push(rEl);
  }
  for (const [, sigMap] of rowsByParent.entries()) {
    for (const [, rawRows] of sigMap.entries()) {
      if (rawRows.length < 2) continue;
      const stackedRows = rawRows
        .map(el => ({ el, rect: el.getBoundingClientRect(), cols: Array.from(el.children).filter(isVisible) }))
        .filter(r => r.rect.width >= 240 && r.cols.length >= 2);
      if (stackedRows.length < 2) continue;
      let isVerticallyStacked = true;
      for (let i = 0; i < stackedRows.length - 1; i++) {
        if (stackedRows[i + 1].rect.top < stackedRows[i].rect.bottom - 4) {
          isVerticallyStacked = false;
          break;
        }
      }
      if (!isVerticallyStacked) continue;

      const refRow = stackedRows[0];
      const refColCount = refRow.cols.length;
      const rowCs = window.getComputedStyle(refRow.el);
      const isSpaceBetweenFlex = rowCs.display === 'flex' && rowCs.justifyContent === 'space-between';

      // (a) Spalten-Fluchtlinie (x-Achse ueber alle Zeilen gleicher Spaltenanzahl)
      for (let ri = 1; ri < stackedRows.length; ri++) {
        const curRow = stackedRows[ri];
        if (curRow.cols.length !== refColCount) continue;
        for (let ci = 0; ci < refColCount; ci++) {
          const rRef = refRow.cols[ci].getBoundingClientRect();
          const rCur = curRow.cols[ci].getBoundingClientRect();
          if (isSpaceBetweenFlex && ci === refColCount - 1 && ci > 0) {
            const rightDiff = Math.abs(rCur.right - rRef.right);
            if (rightDiff > 3) {
              addFinding(
                'P2',
                'P2_CROSS_ROW_RHYTHM_MISMATCH',
                getLabel(curRow.cols[ci]),
                getCssPath(curRow.el),
                `Spalten-Fluchtlinie (rechts) zwischen Zeile 1 und Zeile ${ri + 1} gebrochen: col[${ci}].right=${Math.round(rCur.right)}px vs ${Math.round(rRef.right)}px (Diff=${rightDiff.toFixed(1)}px > 3px)`
              );
            }
          } else {
            const leftDiff = Math.abs(rCur.left - rRef.left);
            if (leftDiff > 3) {
              addFinding(
                'P2',
                'P2_CROSS_ROW_RHYTHM_MISMATCH',
                getLabel(curRow.cols[ci]),
                getCssPath(curRow.el),
                `Spalten-Fluchtlinie (links) zwischen Zeile 1 und Zeile ${ri + 1} gebrochen: col[${ci}].left=${Math.round(rCur.left)}px vs ${Math.round(rRef.left)}px (Diff=${leftDiff.toFixed(1)}px > 3px)`
              );
            }
          }
        }
      }

      // (b) Stockwerk-Paritaet wiederkehrender Tags/Badges (y-Rhythmus ueber alle Zeilen)
      for (let ci = 0; ci < refColCount; ci++) {
        let row1BesideRow = null;
        let row2BelowRow = null;
        for (let ri = 0; ri < stackedRows.length; ri++) {
          const curRow = stackedRows[ri];
          if (curRow.cols.length !== refColCount) continue;
          const colEl = curRow.cols[ci];
          const tagEl = colEl.querySelector('.agenda-kw-tag, .badge, [class*="kw-tag"], [data-eyes-rhythm-tag="true"]');
          if (!tagEl || !isVisible(tagEl)) continue;
          const colRect = colEl.getBoundingClientRect();
          const tagRect = tagEl.getBoundingClientRect();
          const relTop = tagRect.top - colRect.top;
          const relLeft = tagRect.left - colRect.left;
          if (relTop < 8 && relLeft > 25) {
            if (!row1BesideRow) row1BesideRow = { idx: ri + 1, label: getLabel(colEl), el: curRow.el };
          } else if (relTop >= 12) {
            if (!row2BelowRow) row2BelowRow = { idx: ri + 1, label: getLabel(colEl), el: curRow.el };
          }
        }
        if (row1BesideRow && row2BelowRow) {
          addFinding(
            'P2',
            'P2_CROSS_ROW_RHYTHM_MISMATCH',
            `${row1BesideRow.label} vs ${row2BelowRow.label}`,
            getCssPath(row2BelowRow.el),
            `Stockwerk-Zickzack in Spalte ${ci + 1}: Tag sitzt in Zeile ${row1BesideRow.idx} auf Zeile 1 neben dem Text ("${row1BesideRow.label}"), in Zeile ${row2BelowRow.idx} aber auf Zeile 2 unter dem Text ("${row2BelowRow.label}")!`
          );
        }
      }
    }
  }

  // S-30: P2_TYPOGRAPHIC_PLENK_OR_ASCII_ORT (Leerzeichen vor Komma, Schweizer ASCII-Ortsnamen, englischer KI-Geviertstrich \u2014 & #LANG-06 Klarnamen-/Geheimnis-Sperre)
  const plenkRe = /[A-Za-zÄÖÜäöü0-9)\]]\s+,/;
  const asciiOrtRe = /\b(?:Zuerich|Zuercher|Graubuenden|Duebendorf|Buelach|Kuesnacht|Kuessnacht)\b/;
  const emDashRe = /(?<!\.)\u2014/;
  const einserRe = /(?<![0-9:\.\-/])\b1\s+(?:Ansprechpartner(?:in|innen)?|System|Ziel|Beispiel-Team|Co-Sponsor|Haupt-Empf[aä]ngeradresse|St[uü]ck)\b/i;
  const isPublicProductPage =
    relPage.includes('webpilot/') ||
    relPage.includes('kmu-kalender') ||
    location.pathname.includes('/webpilot') ||
    location.hostname.includes('webpilot.') ||
    location.hostname.includes('kmu-kalender');
  const lang06LeakRe =
    /\b(?:Elias\s+Hiltbrand|Hiltbrand\s+(?:Gebäudehüllen|Bau)|Hochuli\s+Schlossrued|JOMA\s+Solar|Anne-Katrin\s+Koch|Herzensarbeit|Innere\s+Stärke|IMP\s+Marketing|FC\s+Schlieren|SC\s+Fulenbach|FC\s+Attiswil|Holz-Susi|Jenny\s+Ettle|JE-MI|Doppel-Systemaugen|OKLCH|60-30-10|Design-Sommelier|JSON-LD|FAQPage|llms\.txt)\b/i;
  for (const el of allDom) {
    if (['SCRIPT', 'STYLE', 'TEXTAREA', 'SVG', 'PATH', 'INPUT', 'SELECT'].includes(el.tagName)) continue;
    if (el.closest('textarea, svg, [data-user-content="true"], .post-preview-text, .acp-no-capture')) continue;
    const isCodeOrPre = ['PRE', 'CODE'].includes(el.tagName) || Boolean(el.closest('pre, code'));
    for (const n of el.childNodes) {
      if (n.nodeType !== 3) continue;
      const directText = (n.nodeValue || '').replace(/\s+/g, ' ').trim();
      if (!directText) continue;
      if (isPublicProductPage && lang06LeakRe.test(directText)) {
        const m = directText.match(lang06LeakRe);
        addFinding(
          'P2',
          'P2_TYPOGRAPHIC_PLENK_OR_ASCII_ORT',
          getLabel(el),
          getCssPath(el),
          `Verstoss gegen #LANG-06 (Kunden-Klarname oder internes Betriebsgeheimnis auf öffentlicher Produktseite gefunden: "${m[0]}")`
        );
      }
      if (isCodeOrPre) continue;
      if (plenkRe.test(directText)) {
        const m = directText.match(plenkRe);
        addFinding(
          'P2',
          'P2_TYPOGRAPHIC_PLENK_OR_ASCII_ORT',
          getLabel(el),
          getCssPath(el),
          `Typografischer Plenk (Leerzeichen vor Komma "${m[0]}") im sichtbaren Text gefunden`
        );
      }
      if (asciiOrtRe.test(directText)) {
        const m = directText.match(asciiOrtRe);
        addFinding(
          'P2',
          'P2_TYPOGRAPHIC_PLENK_OR_ASCII_ORT',
          getLabel(el),
          getCssPath(el),
          `Unkorrigierter Schweizer ASCII-Umlaut-Ortsname "${m[0]}" im sichtbaren UI-Text gefunden (#LANG-01)`
        );
      }
      if (einserRe.test(directText)) {
        const m = directText.match(einserRe);
        addFinding(
          'P2',
          'P2_TYPOGRAPHIC_PLENK_OR_ASCII_ORT',
          getLabel(el),
          getCssPath(el),
          `Nackte Ziffer 1 vor gebeugtem Substantiv ("${m[0]}") gefunden — gemaess #LANG-01 Einser-Ausschreibungs-Regel als Wort (Ein/Eine/Einem) ausschreiben`
        );
      }
      if (emDashRe.test(directText)) {
        addFinding(
          'P2',
          'P2_TYPOGRAPHIC_PLENK_OR_ASCII_ORT',
          getLabel(el),
          getCssPath(el),
          `Englischer KI-Geviertstrich (\u2014) gefunden \u2014 gem\u00e4ss #LANG-01 verboten, nur .\u2014 bei CHF erlaubt`
        );
      }
    }
  }

  return findings;
}

// Optional standalone CLI Self-Test (--self-test-only)
if (
  typeof process !== 'undefined' &&
  Array.isArray(process.argv) &&
  process.argv[1] &&
  process.argv[1].endsWith('system_eyes_core.mjs') &&
  process.argv.includes('--self-test-only')
) {
  (async () => {
    const { createRequire } = await import('module');
    const fs = await import('fs');
    const req = createRequire('/home/brainuser/workspaces/ACP-Authentic-Content-Pilot-Pro0396/acp-app/package.json');
    const { chromium } = req('playwright-core');
    const candidates = [
      '/home/brainuser/.cache/ms-playwright/chromium-1217/chrome-linux64/chrome',
      '/home/brainuser/.cache/ms-playwright/chromium-1217/chrome-linux/chrome',
      '/home/brainuser/.cache/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-linux64/chrome-headless-shell',
      '/home/brainuser/.cache/ms-playwright/chromium-1208/chrome-linux64/chrome'
    ];
    const executablePath = candidates.find(p => fs.existsSync(p));
    const browser = await chromium.launch({ executablePath });
    const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
    try {
      await page.setContent(`<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <style>
    .section-kicker { display: inline-flex; align-items: center; gap: 10px; }
    .section-kicker::before { content: ""; display: inline-block; width: 16px; height: 2px; background: #A84B2B; }
  </style>
</head>
<body>
  <span class="section-kicker">TEST KICKER MIT VORSTRICH</span>
  <p id="bad-em">Satz mit verbotenem KI-Gedankenstrich \u2014 mitten im Satz.</p>
  <p id="good-chf">Erlaubter Schweizer Frankenbetrag: CHF 35.\u2014 pro Monat.</p>
</body>
</html>`);
      const findings = await page.evaluate(evaluateSystemEyesInPage, {
        relPage: 'preview-canary/index.html',
        zone: SYSTEM_EYES_ZONES[2],
        options: {}
      });
      const s17Hit = findings.find(f => f.code === 'P2_CLIENT_CODE_FONT_OR_SLASH' && f.details.includes('::before'));
      const s30Hit = findings.find(f => f.code === 'P2_TYPOGRAPHIC_PLENK_OR_ASCII_ORT' && f.element.includes('verbotenem KI-Gedankenstrich'));
      const s30FalsePositive = findings.find(f => f.code === 'P2_TYPOGRAPHIC_PLENK_OR_ASCII_ORT' && f.element.includes('CHF 35.'));
      await page.setContent(`<!DOCTYPE html><html lang="de"><body><p>Wie bei Elias Hiltbrand und unseren Doppel-Systemaugen mit OKLCH.</p></body></html>`);
      const lang06Findings = await page.evaluate(evaluateSystemEyesInPage, {
        relPage: 'webpilot/index.html',
        zone: SYSTEM_EYES_ZONES[2],
        options: {}
      });
      const s30Lang06Hit = lang06Findings.find(f => f.code === 'P2_TYPOGRAPHIC_PLENK_OR_ASCII_ORT' && f.details.includes('Verstoss gegen #LANG-06'));
      const ok = Boolean(s17Hit && s30Hit && !s30FalsePositive && s30Lang06Hit);
      console.log(JSON.stringify({
        ok,
        system_eyes_version: SYSTEM_EYES_VERSION,
        sensors_count: SYSTEM_EYES_SENSORS.length,
        s17_kicker_before_caught: Boolean(s17Hit),
        s30_em_dash_caught: Boolean(s30Hit),
        s30_chf_price_allowed: !s30FalsePositive,
        s30_lang06_leak_caught: Boolean(s30Lang06Hit)
      }, null, 2));
      if (!ok) process.exit(1);
    } finally {
      await browser.close();
    }
  })();
}

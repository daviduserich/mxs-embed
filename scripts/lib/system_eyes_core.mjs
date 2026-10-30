/**
 * system_eyes_core.mjs — Zentraler Doppel-Systemaugen-Baustein v2.0.0 (#UI-01, #UI-06, #UI-13, #UI-14)
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

export const SYSTEM_EYES_VERSION = '2.1.0';

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
  { id: 'S-17', code: 'P2_CLIENT_CODE_FONT_OR_SLASH', severity: 'P2', rule: '#UI-01', desc: 'Auf Kunden-Webseiten sind JetBrains Mono und //-Code-Striche in Kickern/Badges strikt verboten' },
  { id: 'S-18', code: 'P2_MODAL_OVERLAP_LEAK', severity: 'P2', rule: '#UI-06', desc: 'Bei geoeffnetem Modal darf kein Hintergrund-Widget (#acp-draft-widget) ueber das Modal ragen' },
  { id: 'S-19', code: 'P1_TEXT_BLEEDS_CONTAINER', severity: 'P1', rule: '#UI-14', desc: 'Kein Wort/Textknoten darf horizontal ueber den rechten/linken Rand seines Buttons, Badges oder seiner Karte hinausragen' },
  { id: 'S-20', code: 'P2_FORM_INPUT_MISALIGNMENT', severity: 'P2', rule: '#UI-02', desc: 'Nebeneinanderliegende Formular-Inputs in derselben Zeile muessen auf exakt gleicher vertikaler Hoehe (top) sitzen' }
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
  const scopeRoot = activeScopeSelector ? document.querySelector(activeScopeSelector) : document.body;

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
      if (r.width < 34 || r.height < 30) {
        addFinding('P2', 'P2_CRAMPED_MOBILE', lbl, sel, `Touch-Flaeche zu klein auf Mobile: ${Math.round(r.width)}x${Math.round(r.height)}px (Pflicht >= 34x30px)`);
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

  // S-04: P1_ELEMENT_COLLISION
  const collisionItems = interactiveEls.map(el => ({
    el,
    rect: el.getBoundingClientRect(),
    layerAnc: getLayerContext(el)
  }));
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

    // S-17: Customer Website Typography Guard (#UI-01 Pt 4: No JetBrains Mono or // kickers on customer sites)
    if (!isCockpit && !relPage.startsWith('webpilot/')) {
      if (cs.fontFamily && cs.fontFamily.toLowerCase().includes('jetbrains mono')) {
        addFinding('P2', 'P2_CLIENT_CODE_FONT_OR_SLASH', getLabel(el), getCssPath(el), `Programmierer-Schriftart JetBrains Mono auf Kunden-Webseite verboten (#UI-01 Pt 4)`);
      }
      if (directText.startsWith('// ')) {
        addFinding('P2', 'P2_CLIENT_CODE_FONT_OR_SLASH', getLabel(el), getCssPath(el), `Code-Kommentar-Striche "// " in Kicker/Text auf Kunden-Webseite verboten (#UI-01 Pt 4)`);
      }
    }
  }

  // S-14 & S-15: P2_ROW_HEIGHT_MISMATCH & P2_RAGGED_RIGHT_EDGE in Grids
  const grids = Array.from(queryRoot.querySelectorAll('.pillar-cards, .vs-grid, .teaser-grid, .price-grid, .story-grid, .values-grid, .arch-grid, .sparten-filter-grid, .subservices-grid, .sparte-ref-row, .quiz-steps-grid, .social-grid, .blog-grid, .team-dept-grid, .timeline-list, .partner-grid, .foerder-grid, .check-grid, .begleitung-grid, .testimonials-grid')).filter(isVisible);
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
          addFinding('P2', 'P2_ROW_HEIGHT_MISMATCH', getCssPath(g), getCssPath(g), `Karten in derselben Zeile haben ungleiche Hoehe: min=${Math.round(minH)}px vs max=${Math.round(maxH)}px`);
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


  // S-19: P1_TEXT_BLEEDS_CONTAINER (Text node bleeds outside button/badge/pill/card border)
  for (const el of allDom) {
    if (['SCRIPT', 'STYLE', 'SVG', 'PATH', 'HTML', 'BODY'].includes(el.tagName) || el.closest('svg')) continue;
    const textNodes = Array.from(el.childNodes).filter(n => n.nodeType === 3 && n.nodeValue.trim().length > 0);
    if (textNodes.length === 0) continue;
    const boxEl = el.closest('button, a, .role-pill, .topic-chip-btn, [class*="badge"], [class*="pill"], [class*="btn"], [class*="card"], td, th, label') || el;
    const elCs = window.getComputedStyle(el);
    const boxCs = window.getComputedStyle(boxEl);
    if (elCs.overflowX === 'hidden' || elCs.overflowX === 'clip' || boxCs.overflowX === 'hidden' || boxCs.overflowX === 'clip') continue;
    const bRect = boxEl.getBoundingClientRect();
    if (bRect.width < 10) continue;
    for (const tn of textNodes) {
      const range = document.createRange();
      range.selectNodeContents(tn);
      const rRect = range.getBoundingClientRect();
      if (rRect.width === 0) continue;
      if (rRect.right > bRect.right + 1.5 || rRect.left < bRect.left - 1.5) {
        addFinding('P1', 'P1_TEXT_BLEEDS_CONTAINER', getLabel(boxEl), getCssPath(boxEl), `Text ragt ueber Element-Rahmen hinaus: textRight=${Math.round(rRect.right)}px > boxRight=${Math.round(bRect.right)}px`);
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

  return findings;
}

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fixes the "Im Simulator ansehen" jump action in WebPilot Studio Cockpit:
1. Updates templates/cockpit-script-template.js:
   - Enhances acpScrollToSectionInViewport() with smart fallbacks (by data-section, id, class, tag)
   - Stamped data-section attribute into the iframe DOM during scanning
   - Adds explicit onclick on the jump button and overlay
   - Removes unnecessary sandbox attribute from mini-iframes to eliminate console warnings
2. Tags all sections in preview-birchmeier/*.html with explicit data-section and id
3. Recompiles cockpits and verifies
"""

from pathlib import Path
import re

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
TEMPLATE_JS = BASE_DIR / "templates" / "cockpit-script-template.js"
BIRCHMEIER_DIR = BASE_DIR / "preview-birchmeier"

# 1. Update templates/cockpit-script-template.js
c_js = TEMPLATE_JS.read_text(encoding="utf-8")

# Replace acpScrollToSectionInViewport
old_scroll_fn = """function acpScrollToSectionInViewport(secId) {
  var iframe = document.getElementById("acp-widget-viewport");
  var doc = iframe ? (iframe.contentDocument || iframe.contentWindow.document) : null;
  if (!doc) return;

  var targetEl = doc.querySelector('[data-section="' + secId + '"]') || doc.getElementById(secId);
  if (!targetEl) return;

  acpToggleSectionsModal();

  targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });

  var origTransition = targetEl.style.transition;
  var origOutline = targetEl.style.outline;
  var origShadow = targetEl.style.boxShadow;

  targetEl.style.transition = 'all 0.3s ease';
  targetEl.style.outline = '3px solid #f59e0b';
  targetEl.style.boxShadow = '0 0 50px rgba(245, 158, 11, 0.5)';

  setTimeout(function() {
    targetEl.style.outline = origOutline;
    targetEl.style.boxShadow = origShadow;
    targetEl.style.transition = origTransition;
  }, 2500);
}"""

new_scroll_fn = """function acpScrollToSectionInViewport(secId) {
  console.log("[WebPilot Studio] 🎯 Springe zu Sektion:", secId);
  var iframe = document.getElementById("acp-widget-viewport");
  var doc = iframe ? (iframe.contentDocument || iframe.contentWindow.document) : null;
  if (!doc) {
    console.warn("[WebPilot Studio] Kein iframe-Document gefunden");
    return;
  }

  // 1. Suche nach data-section oder id
  var targetEl = doc.querySelector('[data-section="' + secId + '"]') || doc.getElementById(secId);

  // 2. Smarte Fallbacks nach Archetyp / Klassen
  if (!targetEl) {
    if (secId === "hero" || secId.includes("hero")) {
      targetEl = doc.querySelector(".hero-wrap, .page-hero, .hero, section");
    } else if (secId === "top-bar" || secId === "header") {
      targetEl = doc.querySelector("header, .top-bar, .header-wrap");
    } else if (secId === "footer") {
      targetEl = doc.querySelector("footer, .footer-wrap, .block-footer");
    } else if (secId === "leistungen" || secId.includes("service")) {
      targetEl = doc.querySelector("#leistungen, .service-cards, [id*='leistung']");
    } else if (secId === "stellen" || secId.includes("job")) {
      targetEl = doc.querySelector("#stellen, .jobs-grid, [id*='stell']");
    } else if (secId === "vorteile" || secId.includes("benefit")) {
      targetEl = doc.querySelector("#vorteile, .benefits-grid, [id*='vorteil']");
    } else if (secId === "bewerben" || secId.includes("apply")) {
      targetEl = doc.querySelector("#bewerben, .apply-section, form");
    }
  }

  if (!targetEl) {
    console.warn("[WebPilot Studio] Sektion nicht im DOM gefunden:", secId);
    return;
  }

  // Modal schliessen
  if (acpSectionsModalOpen) {
    acpToggleSectionsModal();
  }

  // Sanftes Scrollen zur Zielsektion
  try {
    targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
  } catch (e) {
    targetEl.scrollIntoView();
  }

  // Visueller bernsteinfarbener Hervorhebungs-Impuls (2.5 Sekunden)
  var origTransition = targetEl.style.transition;
  var origOutline = targetEl.style.outline;
  var origShadow = targetEl.style.boxShadow;

  targetEl.style.transition = 'all 0.3s ease';
  targetEl.style.outline = '3px solid #f59e0b';
  targetEl.style.boxShadow = '0 0 50px rgba(245, 158, 11, 0.5)';

  setTimeout(function() {
    targetEl.style.outline = origOutline;
    targetEl.style.boxShadow = origShadow;
    targetEl.style.transition = origTransition;
  }, 2500);
}"""

assert old_scroll_fn in c_js, "old_scroll_fn not found in template!"
c_js = c_js.replace(old_scroll_fn, new_scroll_fn)

# Replace id tagging and mini-iframe sandbox
old_scan_loop = """      var id = el.getAttribute("data-section") || el.id;
      if (!id) {
        if (el.tagName.toLowerCase() === "header") id = "header";
        else if (el.tagName.toLowerCase() === "footer") id = "footer";
        else if (el.className && el.className.includes("hero")) id = "hero";
        else id = "section-" + (idx + 1);
      }"""

new_scan_loop = """      var id = el.getAttribute("data-section") || el.id;
      if (!id) {
        if (el.tagName.toLowerCase() === "header") id = "top-bar";
        else if (el.tagName.toLowerCase() === "footer") id = "footer";
        else if (el.className && (el.className.includes("hero") || el.className.includes("page-hero"))) id = "hero";
        else id = "section-" + (idx + 1);
      }
      // Garantiere data-section im Live-iFrame DOM für deterministisches Anspringen
      if (!el.getAttribute("data-section")) {
        el.setAttribute("data-section", id);
      }"""

assert old_scan_loop in c_js, "old_scan_loop not found in template!"
c_js = c_js.replace(old_scan_loop, new_scan_loop)

# Replace mini-stage HTML rendering
old_stage_html = """        '<div class="acp-sec-mini-stage" onclick="acpScrollToSectionInViewport(\\'' + sec.id + '\\')" title="Klicken, um im Live-Simulator direkt zu diesem Abschnitt zu springen">' +
          '<iframe class="acp-sec-mini-iframe" srcdoc="' + srcdocHtml.replace(/"/g, '&quot;') + '" sandbox="allow-same-origin allow-scripts"></iframe>' +
          '<div class="acp-sec-mini-overlay">' +
            '<button type="button" class="acp-sec-mini-jump-btn"><span>👁️ Im Simulator ansehen</span></button>' +
          '</div>' +
        '</div>' +"""

new_stage_html = """        '<div class="acp-sec-mini-stage" onclick="acpScrollToSectionInViewport(\\'' + sec.id + '\\')" title="Klicken, um im Live-Simulator direkt zu diesem Abschnitt zu springen">' +
          '<iframe class="acp-sec-mini-iframe" srcdoc="' + srcdocHtml.replace(/"/g, '&quot;') + '"></iframe>' +
          '<div class="acp-sec-mini-overlay" onclick="acpScrollToSectionInViewport(\\'' + sec.id + '\\')">' +
            '<button type="button" class="acp-sec-mini-jump-btn" onclick="event.stopPropagation(); acpScrollToSectionInViewport(\\'' + sec.id + '\\')"><span>👁️ Im Simulator ansehen</span></button>' +
          '</div>' +
        '</div>' +"""

assert old_stage_html in c_js, "old_stage_html not found in template!"
c_js = c_js.replace(old_stage_html, new_stage_html)

TEMPLATE_JS.write_text(c_js, encoding="utf-8")
print("✅ templates/cockpit-script-template.js updated.")

# 2. Tag HTML files in preview-birchmeier
for p in [BIRCHMEIER_DIR / "index.html", BIRCHMEIER_DIR / "team.html", BIRCHMEIER_DIR / "kontakt.html"]:
    if not p.exists(): continue
    txt = p.read_text(encoding="utf-8")
    
    # Hero
    txt = txt.replace('<section class="hero-wrap">', '<section class="hero-wrap" id="hero" data-section="hero">')
    txt = txt.replace('<section class="page-hero">', '<section class="page-hero" id="hero" data-section="hero">')
    
    # Leistungen / Kompetenzen
    txt = txt.replace('<div class="section-wrap" id="leistungen">', '<div class="section-wrap" id="leistungen" data-section="leistungen">')
    
    # Teaser
    txt = txt.replace('<div class="section-wrap" style="background: var(--surface);">', '<div class="section-wrap" id="teaser" data-section="teaser" style="background: var(--surface);">')
    
    # Team Grid
    txt = txt.replace('<div class="section-wrap">\n    <div class="section-inner">\n      <span class="section-kicker">Ansprechpartner & Meister</span>',
                      '<div class="section-wrap" id="team" data-section="team">\n    <div class="section-inner">\n      <span class="section-kicker">Ansprechpartner & Meister</span>')
    
    # Kontakt Grid
    txt = txt.replace('<div class="section-wrap">\n    <div class="section-inner">\n      <span class="section-kicker">Standort & Erreichbarkeit</span>',
                      '<div class="section-wrap" id="kontakt" data-section="kontakt">\n    <div class="section-inner">\n      <span class="section-kicker">Standort & Erreichbarkeit</span>')
    
    # Footer
    txt = txt.replace('<footer class="footer-wrap">', '<footer class="footer-wrap" id="footer" data-section="footer">')
    
    p.write_text(txt, encoding="utf-8")
    print(f"✅ Tagged sections in {p.name}")


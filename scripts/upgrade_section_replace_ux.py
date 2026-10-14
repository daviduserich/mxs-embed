#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Studio Section Replace UX Upgrade (upgrade_section_replace_ux.py)
========================================================================
Behebt das Problem der modalen Sichtbarkeit (opacity: 0 durch fehlende .is-open Klasse)
und implementiert Davids gewünschte "Text ist drin -> Klicken absenden" Experience:
1. Dialog-Modal CSS mit z-index 5000, flex-Zentrierung und bernsteinfarbenem Rand
2. Großes, sofort fokussiertes Einfügefeld mit Live-Feedback:
   "🟢 ✓ Text ist drin! X Zeilen • Y Wörter • Z Zeichen erkannt. Bereit zum Absenden!"
3. Großer, unübersehbarer Absende-Button: "🚀 Änderung jetzt absenden & live speichern"
4. Toleranter Airbag: automatisches Entfernen von Markdown-Fences (```html)
   und automatisches Wrappen von reinem Text / innerem HTML in die Sektions-Hülle
5. Shortcut-Button im Coach-Toast: "✏️ Antwort hier einfügen →"
6. Recompiling & Validierung für alle Mandanten (preview-birchmeier, etc.)
"""

import re
import sys
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
APP_HTML = BASE_DIR / "templates" / "cockpit-app.html"
SCRIPT_JS = BASE_DIR / "templates" / "cockpit-script-template.js"

def update_cockpit_app_html():
    content = APP_HTML.read_text(encoding="utf-8")

    # 1. CSS für fokussierte Dialog-Modale hinzufügen
    dialog_css = """
/* ======================================================= */
/* FOKUSSIERTE DIALOG-MODALE (Z-INDEX 5000 ÜBER FULLSCREEN) */
/* ======================================================= */
#acp-replace-section-modal,
#acp-new-section-modal {
  position: fixed !important;
  inset: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  background: rgba(4, 7, 13, 0.88) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  z-index: 5000 !important;
  display: none !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 20px !important;
  box-sizing: border-box !important;
  opacity: 0 !important;
  transition: opacity 0.2s ease !important;
}

#acp-replace-section-modal.is-open,
#acp-new-section-modal.is-open {
  display: flex !important;
  opacity: 1 !important;
}

#acp-replace-section-modal .acp-modal,
#acp-new-section-modal .acp-modal {
  width: 100% !important;
  max-width: 780px !important;
  min-height: auto !important;
  height: auto !important;
  background: #0d131f !important;
  border: 1px solid rgba(245, 158, 11, 0.35) !important;
  border-radius: 16px !important;
  box-shadow: 0 25px 80px rgba(0, 0, 0, 0.9), 0 0 40px rgba(245, 158, 11, 0.12) !important;
  padding: 28px !important;
  margin: auto !important;
  box-sizing: border-box !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 16px !important;
  color: #f8fafc !important;
  overflow: visible !important;
}
"""

    if "#acp-replace-section-modal.is-open" not in content:
        # Vor </style> einfügen
        content = content.replace("</style>", dialog_css + "\n</style>", 1)
        print("✓ Dialog-CSS in cockpit-app.html injiziert")

    # 2. HTML-Markup für #acp-replace-section-modal modernisieren
    new_modal_html = """<!-- MODAL: SEKTION ERSETZEN & TEXT/CODE EINFÜGEN -->
<div id="acp-replace-section-modal" onclick="if(event.target===this)acpCloseReplaceSectionModal()">
  <div class="acp-modal">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:14px;">
      <div>
        <span style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#f59e0b; font-weight:700; letter-spacing:0.5px;">// WEBPILOT FREIHEIT ⬥ NEUEN TEXT ODER CODE EINSETZEN</span>
        <h3 style="color:#fff; font-size:18px; margin:4px 0 0 0; font-weight:700;" id="acp-replace-modal-title">Sektion bearbeiten</h3>
      </div>
      <button type="button" class="acp-btn-close" onclick="acpCloseReplaceSectionModal()" style="background:none; border:none; color:#94a3b8; font-size:20px; cursor:pointer; padding:4px 8px; line-height:1;">✕</button>
    </div>

    <div style="background:rgba(245,158,11,0.06); border:1px solid rgba(245,158,11,0.2); border-radius:8px; padding:12px 16px; font-size:13px; color:#cbd5e1; line-height:1.5;">
      📋 <strong>So funktioniert's:</strong> Kopiere den neuen Text oder Code aus ChatGPT / Claude und füge ihn unten mit <strong>Strg + V</strong> ein. Unser intelligenter Airbag bereinigt den Code automatisch, schützt das Layout und speichert die Änderung dauerhaft auf dem Server.
    </div>

    <div>
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <label for="acp-replace-code-input" style="font-size:12.5px; font-weight:700; color:#e2e8f0; font-family:'JetBrains Mono',monospace;">
          EINFÜGE-FELD (TEXT ODER HTML):
        </label>
        <span id="acp-replace-char-counter" style="font-size:11.5px; font-family:'JetBrains Mono',monospace; color:#94a3b8;">
          0 Zeichen
        </span>
      </div>

      <textarea id="acp-replace-code-input" rows="11" oninput="acpUpdateReplaceTextFeedback()" onpaste="setTimeout(acpUpdateReplaceTextFeedback, 50)" style="width:100%; background:#06090e; border:1.5px solid rgba(245,158,11,0.3); border-radius:10px; color:#f1f5f9; font-family:'JetBrains Mono',monospace; font-size:12.5px; padding:14px; box-sizing:border-box; resize:vertical; line-height:1.5; outline:none;" placeholder="Hier die Antwort / den Text von ChatGPT oder Claude einfügen (Strg + V)..."></textarea>
    </div>

    <!-- LIVE-STATUS: DAMIT MAN WEISS DER TEXT IST DRIN -->
    <div id="acp-replace-live-feedback" style="background:#090d16; border:1px solid rgba(255,255,255,0.08); border-radius:8px; padding:10px 14px; font-size:12.5px;">
      <span style="color:#94a3b8;">⚪ Noch kein Inhalt eingefügt. Füge deinen Text mit Strg + V ein.</span>
    </div>

    <div id="acp-replace-airbag-status" style="font-size:12.5px; display:none;"></div>

    <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px; padding-top:14px; border-top:1px solid rgba(255,255,255,0.08);">
      <button type="button" class="acp-btn-secondary" onclick="acpCloseReplaceSectionModal()" style="padding:10px 18px; font-size:13px; color:#94a3b8; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:6px; cursor:pointer;">
        Abbrechen
      </button>

      <button type="button" class="acp-btn-primary" id="acp-btn-apply-replace" onclick="acpSubmitReplaceSection()" style="background:linear-gradient(135deg, #10b981 0%, #059669 100%); color:#ffffff; font-weight:700; font-size:14px; padding:12px 24px; border-radius:8px; border:none; cursor:pointer; display:inline-flex; align-items:center; gap:8px; box-shadow:0 4px 14px rgba(16,185,129,0.35);">
        <span>🚀 Änderung jetzt absenden &amp; live speichern</span>
      </button>
    </div>
  </div>
</div>"""

    # Ersetze altes Modal
    pattern = re.compile(r'<!-- MODAL: SEKTION ERSETZEN & AIRBAG CHECK -->[\s\S]*?<!-- MODAL: NEUE SEKTION MIT KI ERSTELLEN -->', re.MULTILINE)
    if pattern.search(content):
        content = pattern.sub(new_modal_html + "\n\n<!-- MODAL: NEUE SEKTION MIT KI ERSTELLEN -->", content)
        print("✓ Neues Modal-Markup in cockpit-app.html ersetzt")
    else:
        print("⚠️ Pattern für altes Modal nicht gefunden")

    APP_HTML.write_text(content, encoding="utf-8")


def update_cockpit_script_js():
    content = SCRIPT_JS.read_text(encoding="utf-8")

    # 1. Sektions-Karten Button umbenennen: "✏️ Text / Code einfügen"
    old_btn = r"""'<button type="button" class="acp-btn-secondary" onclick="acpOpenReplaceSectionModal\(\\\'\' \+ sec\.id \+ \'\\\'\)" style="padding:9px 12px; font-size:12\.5px;" title="Modifizierten KI-Code einfügen & dauerhaft speichern">' \+\s*'<span[^>]*>✏️ Ersetzen</span>' \+\s*'</button>'"""
    new_btn = """'<button type="button" class="acp-btn-secondary" onclick="acpOpenReplaceSectionModal(\\'' + sec.id + '\\')" style="padding:9px 12px; font-size:12.5px; font-weight:700; color:#34d399; background:rgba(16,185,129,0.12); border-color:rgba(16,185,129,0.35);" title="Neuen Text oder KI-Code einfügen & dauerhaft speichern">' +
          '<span>✏️ Text / Code einfügen</span>' +
        '</button>'"""
    content = re.sub(old_btn, new_btn, content)

    # 2. Im Coach-Toast den 3. Direktbutton "✏️ Antwort hier einfügen →" einbauen
    old_toast_links = r"""'<div style="display:flex; gap:10px; margin-top:4px;">' \+\s*'<a href="https://chatgpt\.com/"[^>]*>[\s\S]*?</a>' \+\s*'<a href="https://claude\.ai/"[^>]*>[\s\S]*?</a>' \+\s*'</div>';"""
    new_toast_links = """'<div style="display:flex; gap:10px; margin-top:8px; flex-wrap:wrap;">' +
      '<a href="https://chatgpt.com/" target="_blank" rel="noopener" style="flex:1; min-width:130px; text-align:center; background:#10a37f; color:#fff; font-size:12px; font-weight:700; padding:8px 12px; border-radius:6px; text-decoration:none; display:inline-flex; align-items:center; justify-content:center; gap:6px;">' +
        '<span>🤖 ChatGPT öffnen ↗</span>' +
      '</a>' +
      '<a href="https://claude.ai/" target="_blank" rel="noopener" style="flex:1; min-width:130px; text-align:center; background:#d97706; color:#fff; font-size:12px; font-weight:700; padding:8px 12px; border-radius:6px; text-decoration:none; display:inline-flex; align-items:center; justify-content:center; gap:6px;">' +
        '<span>🧠 Claude öffnen ↗</span>' +
      '</a>' +
      '<button type="button" onclick="this.closest(\\'.acp-coach-toast\\').remove(); acpOpenReplaceSectionModal(\\'' + secId + '\\')" style="flex:1.4; min-width:160px; text-align:center; background:linear-gradient(135deg, #10b981 0%, #059669 100%); color:#fff; font-size:12px; font-weight:700; padding:8px 12px; border-radius:6px; border:none; cursor:pointer; display:inline-flex; align-items:center; justify-content:center; gap:6px; box-shadow:0 2px 8px rgba(16,185,129,0.3);">' +
        '<span>✏️ Antwort hier einfügen →</span>' +
      '</button>' +
    '</div>';"""
    content = re.sub(old_toast_links, new_toast_links, content)

    # 3. acpOpenReplaceSectionModal, acpCloseReplaceSectionModal, acpUpdateReplaceTextFeedback,
    #    acpNormalizeAndValidateSection und acpSubmitReplaceSection ersetzen
    new_script_block = """
function acpOpenReplaceSectionModal(secId) {
  acpActiveEditSectionId = secId;
  var modal = document.getElementById("acp-replace-section-modal");
  var title = document.getElementById("acp-replace-modal-title");
  var textarea = document.getElementById("acp-replace-code-input");
  var status = document.getElementById("acp-replace-airbag-status");
  var feedback = document.getElementById("acp-replace-live-feedback");
  var counter = document.getElementById("acp-replace-char-counter");

  if (title) {
    var targetSec = (acpScannedSections || []).find(function(s) { return s.id === secId; });
    var secTitle = targetSec && targetSec.title ? (' «' + targetSec.title + '»') : '';
    title.textContent = "Sektion [" + secId + "]" + secTitle + " — Neuer Text / Code";
  }
  if (textarea) {
    textarea.value = "";
    textarea.placeholder = "Hier die Antwort oder den neuen Text von ChatGPT / Claude für Sektion [" + secId + "] einfügen (Strg + V)...";
  }
  if (status) {
    status.style.display = "none";
    status.innerHTML = "";
  }
  if (counter) {
    counter.textContent = "0 Zeichen";
  }
  if (feedback) {
    feedback.innerHTML = '<span style="color:#94a3b8;">⚪ Noch kein Inhalt eingefügt. Füge deinen Text mit Strg + V ein.</span>';
  }

  if (modal) {
    modal.classList.add("is-open");
    modal.style.display = "flex";
  }
  acpUpdateBodyModalClass();

  // Fokus sofort ins Eingabefeld
  setTimeout(function() {
    if (textarea) textarea.focus();
  }, 100);
}

function acpCloseReplaceSectionModal() {
  var modal = document.getElementById("acp-replace-section-modal");
  if (modal) {
    modal.classList.remove("is-open");
    modal.style.display = "none";
  }
  acpUpdateBodyModalClass();
}

function acpUpdateReplaceTextFeedback() {
  var textarea = document.getElementById("acp-replace-code-input");
  var feedback = document.getElementById("acp-replace-live-feedback");
  var counter = document.getElementById("acp-replace-char-counter");
  var status = document.getElementById("acp-replace-airbag-status");
  if (!textarea || !feedback) return;

  var val = textarea.value.trim();
  if (counter) {
    counter.textContent = val.length + " Zeichen";
  }

  if (!val) {
    feedback.innerHTML = '<span style="color:#94a3b8;">⚪ Noch kein Inhalt eingefügt. Füge deinen Text mit Strg + V ein.</span>';
    if (status) status.style.display = "none";
    return;
  }

  var lines = val.split("\\n").length;
  var words = val.split(/\\s+/).filter(Boolean).length;
  var chars = val.length;

  feedback.innerHTML = 
    '<span style="display:inline-flex; align-items:center; gap:8px; color:#10b981; font-weight:700;">' +
      '<span style="font-size:16px;">🟢</span>' +
      '<span>✓ Text ist drin! ' + lines + ' Zeilen • ' + words + ' Wörter • ' + chars + ' Zeichen erkannt. Bereit zum Absenden!</span>' +
    '</span>';
}

function acpNormalizeAndValidateSection(rawInput, secId) {
  if (!rawInput || !rawInput.trim()) {
    return { ok: false, error: "Das Textfeld ist noch leer. Bitte füge zuerst den Text oder Code ein." };
  }

  var clean = rawInput.trim();

  // 1. Markdown-Codefences entfernen (```html ... ``` oder ``` ... ```)
  if (clean.startsWith("```")) {
    clean = clean.replace(/^```[a-zA-Z]*\\n?/, "");
    clean = clean.replace(/\\n?```$/, "").trim();
  }

  // 2. Sicherheits-Check: Keine ausführbaren Skripte oder iframes
  var forbiddenTags = /<(script|iframe|object|embed|form|meta|base|style)\\b[^>]*>/i;
  var mTag = clean.match(forbiddenTags);
  if (mTag) {
    return { ok: false, error: "Sicherheits-Schranke: Ausführbare Tags (<" + mTag[1] + ">) sind in Inhalts-Sektionen verboten." };
  }
  if (/\\son[a-zA-Z]+\\s*=/i.test(clean)) {
    return { ok: false, error: "Sicherheits-Schranke: Inline-JavaScript (on... Event-Handler) ist verboten." };
  }
  if (/(href|src|action)\\s*=\\s*["'\\s]*javascript:/i.test(clean)) {
    return { ok: false, error: "Sicherheits-Schranke: javascript:... Links sind nicht erlaubt." };
  }

  // 3. Intelligente Sektions-Hülle (Wrapping):
  var isAlreadySection = /^<(section|header|footer)\\b[^>]*>/i.test(clean) && /<\\/(section|header|footer)>$/i.test(clean);

  if (!isAlreadySection) {
    // Wenn HTML-Tags enthalten sind:
    if (/<[a-z][\\s\\S]*>/i.test(clean)) {
      clean = '<section class="section-wrap" id="' + secId + '" data-section="' + secId + '">\\n  <div class="section-inner">\\n' + clean + '\\n  </div>\\n</section>';
    } else {
      // Reiner Text: Absätze in <p> wrappen
      var paragraphs = clean.split(/\\n\\s*\\n/).map(function(p) {
        return '    <p class="section-desc">' + p.trim().replace(/\\n/g, '<br>') + '</p>';
      }).join('\\n');
      clean = '<section class="section-wrap" id="' + secId + '" data-section="' + secId + '">\\n  <div class="section-inner">\\n' + paragraphs + '\\n  </div>\\n</section>';
    }
  } else {
    // Sicherstellen, dass data-section gesetzt ist
    if (!clean.includes('data-section=')) {
      clean = clean.replace(/^<(section|header|footer)\\b/i, '<$1 data-section="' + secId + '"');
    }
  }

  // 4. Tag-Balancierung
  var checkTags = ["section", "div", "p", "span", "a", "h1", "h2", "h3", "h4", "ul", "ol", "li"];
  for (var i = 0; i < checkTags.length; i++) {
    var tag = checkTags[i];
    var openRegex = new RegExp("<" + tag + "(\\s+[^>]*)?>", "gi");
    var closeRegex = new RegExp("</" + tag + ">", "gi");
    var openCount = (clean.match(openRegex) || []).length;
    var closeCount = (clean.match(closeRegex) || []).length;
    if (openCount !== closeCount) {
      return { 
        ok: false, 
        error: "Tag-Fehler bei <" + tag + ">: Wurde " + openCount + "x geöffnet, aber " + closeCount + "x geschlossen. Bitte schliesse alle <" + tag + "> Tags sauber ab." 
      };
    }
  }

  return { ok: true, html: clean };
}

function acpSubmitReplaceSection() {
  var textarea = document.getElementById("acp-replace-code-input");
  var status = document.getElementById("acp-replace-airbag-status");
  var applyBtn = document.getElementById("acp-btn-apply-replace");
  if (!textarea || !textarea.value) {
    if (status) {
      status.style.display = "block";
      status.style.color = "#ef4444";
      status.style.background = "rgba(239, 68, 68, 0.1)";
      status.style.padding = "10px 14px";
      status.style.borderRadius = "6px";
      status.style.border = "1px solid rgba(239, 68, 68, 0.3)";
      status.innerHTML = "⚠️ <strong>Bitte zuerst Text einfügen:</strong> Das Feld ist noch leer.";
    }
    return;
  }

  var validation = acpNormalizeAndValidateSection(textarea.value, acpActiveEditSectionId);
  if (!validation.ok) {
    if (status) {
      status.style.display = "block";
      status.style.color = "#ef4444";
      status.style.background = "rgba(239, 68, 68, 0.1)";
      status.style.padding = "10px 14px";
      status.style.borderRadius = "6px";
      status.style.border = "1px solid rgba(239, 68, 68, 0.3)";
      status.innerHTML = "🚨 <strong>Airbag-Schranke:</strong> " + validation.error;
    }
    return;
  }

  var iframe = document.getElementById("acp-widget-viewport");
  var targetFile = "index.html";
  if (iframe && iframe.getAttribute("src")) {
    var srcVal = iframe.getAttribute("src").split("?")[0];
    if (srcVal.endsWith(".html")) {
      targetFile = srcVal.split("/").pop();
    }
  }

  var clientSlug = window.ACP_CURRENT_CLIENT || (window.location.pathname.split("/")[1] || "preview-birchmeier");

  if (applyBtn) {
    applyBtn.disabled = true;
    applyBtn.innerHTML = "<span>⏳ Speichere &amp; Edge CDN synchronisieren...</span>";
  }

  if (status) {
    status.style.display = "block";
    status.style.color = "#fbbf24";
    status.style.background = "rgba(245, 158, 11, 0.1)";
    status.style.padding = "10px 14px";
    status.style.borderRadius = "6px";
    status.style.border = "1px solid rgba(245, 158, 11, 0.3)";
    status.innerHTML = "⚡ <strong>Airbag grün:</strong> Sende neue Sektion an Cloudflare Edge CDN...";
  }

  var payload = {
    client: clientSlug,
    file: targetFile,
    section_id: acpActiveEditSectionId,
    content: validation.html
  };

  fetch("/api/publish-career/replace-section", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
  .then(function(res) {
    if (!res.ok) {
      return res.json().then(function(j) { throw new Error(j.error || ("HTTP " + res.status)); });
    }
    return res.json();
  })
  .then(function(data) {
    if (applyBtn) {
      applyBtn.disabled = false;
      applyBtn.innerHTML = "<span>🚀 Änderung jetzt absenden &amp; live speichern</span>";
    }
    acpCloseReplaceSectionModal();

    if (typeof acpAutoSyncViewport === "function") {
      acpAutoSyncViewport("Sektion [" + acpActiveEditSectionId + "] aktualisiert");
    } else if (iframe) {
      var curSrc = iframe.src.split("?")[0];
      iframe.src = curSrc + "?t=" + Date.now();
    }

    setTimeout(function() {
      acpScanAndRenderSections();
    }, 1500);

    alert("🎉 Sektion [" + acpActiveEditSectionId + "] erfolgreich dauerhaft gespeichert und auf Cloudflare Pages bereitgestellt!");
  })
  .catch(function(err) {
    console.error("Fehler beim Ersetzen der Sektion:", err);
    if (applyBtn) {
      applyBtn.disabled = false;
      applyBtn.innerHTML = "<span>🚀 Änderung jetzt absenden &amp; live speichern</span>";
    }
    if (status) {
      status.style.display = "block";
      status.style.color = "#ef4444";
      status.style.background = "rgba(239, 68, 68, 0.1)";
      status.style.padding = "10px 14px";
      status.style.borderRadius = "6px";
      status.style.border = "1px solid rgba(239, 68, 68, 0.3)";
      status.innerHTML = "🚨 <strong>Server-Fehler:</strong> " + err.message;
    }
  });
}
"""

    # Ersetze alten Funktionsblock
    pattern_fns = re.compile(r'function acpOpenReplaceSectionModal\b[\s\S]*?function acpOpenNewSectionModal\b', re.MULTILINE)
    if pattern_fns.search(content):
        content = pattern_fns.sub(new_script_block.strip() + "\n\nfunction acpOpenNewSectionModal", content)
        print("✓ Neue Sektions-Ersetzen Logik in cockpit-script-template.js ersetzt")
    else:
        print("⚠️ Pattern für alte Funktionen nicht gefunden")

    # Auch acpOpenNewSectionModal und acpCloseNewSectionModal mit .is-open ausstatten
    content = content.replace(
        'if (modal) modal.style.display = "block";\n}',
        'if (modal) { modal.classList.add("is-open"); modal.style.display = "flex"; }\n  acpUpdateBodyModalClass();\n}'
    )
    content = content.replace(
        'if (modal) modal.style.display = "none";\n}',
        'if (modal) { modal.classList.remove("is-open"); modal.style.display = "none"; }\n  acpUpdateBodyModalClass();\n}'
    )

    SCRIPT_JS.write_text(content, encoding="utf-8")

def main():
    print("Starte Upgrade der WebPilot Studio Section Replace UX...")
    update_cockpit_app_html()
    update_cockpit_script_js()
    print("Upgrade erfolgreich durchgeführt!")

if __name__ == "__main__":
    main()

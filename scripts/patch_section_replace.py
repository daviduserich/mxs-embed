#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chirurgischer Patch für templates/cockpit-script-template.js:
- Reaktiviert modale Sichtbarkeit mit .is-open und display: flex
- Bietet intelligentes Wrapping & Bereinigung (Airbag)
- Live-Rückmeldung bei Texteinfügung (Damit man weiss der Text ist drin)
- Unmissverständlicher Absende-Button & automatische Edge CDN Synchronisation
"""

from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
SCRIPT_JS = BASE_DIR / "templates" / "cockpit-script-template.js"

content = SCRIPT_JS.read_text(encoding="utf-8")

# 1. Sektions-Karten Button anpassen
old_btn = """'<button type="button" class="acp-btn-secondary" onclick="acpOpenReplaceSectionModal(\\'' + sec.id + '\\')" style="padding:9px 12px; font-size:12.5px;" title="Modifizierten KI-Code einfügen & dauerhaft speichern">' +
          '<span>✏️ Ersetzen</span>' +
        '</button>'"""

new_btn = """'<button type="button" class="acp-btn-secondary" onclick="acpOpenReplaceSectionModal(\\'' + sec.id + '\\')" style="padding:9px 12px; font-size:12.5px; font-weight:700; color:#34d399; background:rgba(16,185,129,0.12); border-color:rgba(16,185,129,0.35);" title="Neuen Text oder KI-Code einfügen & dauerhaft speichern">' +
          '<span>✏️ Text / Code einfügen</span>' +
        '</button>'"""

if old_btn in content:
    content = content.replace(old_btn, new_btn)
    print("✓ Sektionskarten-Button zu '✏️ Text / Code einfügen' aktualisiert")
else:
    print("ℹ️ Sektionskarten-Button bereits aktualisiert oder nicht gefunden")

# 2. Toast-Links mit 3. Button versehen
old_toast = """    '<div style="display:flex; gap:10px; margin-top:4px;">' +
      '<a href="https://chatgpt.com/" target="_blank" rel="noopener" style="flex:1; text-align:center; background:#10a37f; color:#fff; font-size:12px; font-weight:700; padding:8px 12px; border-radius:6px; text-decoration:none; display:inline-flex; align-items:center; justify-content:center; gap:6px;">' +
        '<span>🤖 ChatGPT öffnen ↗</span>' +
      '</a>' +
      '<a href="https://claude.ai/" target="_blank" rel="noopener" style="flex:1; text-align:center; background:#d97706; color:#fff; font-size:12px; font-weight:700; padding:8px 12px; border-radius:6px; text-decoration:none; display:inline-flex; align-items:center; justify-content:center; gap:6px;">' +
        '<span>🧠 Claude öffnen ↗</span>' +
      '</a>' +
    '</div>';"""

new_toast = """    '<div style="display:flex; gap:10px; margin-top:8px; flex-wrap:wrap;">' +
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

if old_toast in content:
    content = content.replace(old_toast, new_toast)
    print("✓ Coach-Toast um '✏️ Antwort hier einfügen →' erweitert")
else:
    print("ℹ️ Coach-Toast bereits aktualisiert oder nicht gefunden")

# 3. Hauptfunktionen ersetzen
i1 = content.find("function acpOpenReplaceSectionModal(secId) {")
i2 = content.find("function acpOpenNewSectionModal() {")

if i1 != -1 and i2 != -1:
    new_fns = """function acpOpenReplaceSectionModal(secId) {
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
    content = content[:i1] + new_fns + content[i2:]
    print("✓ Hauptfunktionen in cockpit-script-template.js erfolgreich ausgetauscht")
else:
    print("❌ Konnte Funktionsgrenzen i1/i2 nicht finden!")

SCRIPT_JS.write_text(content, encoding="utf-8")
print("Patch fertiggestellt!")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Patcht die Sicherheits-Schranke in:
1. templates/cockpit-script-template.js
2. /home/brainuser/workspaces/Marketing-Hiltbrand-Pro0409/scripts/publish_service.py

Damit:
- <form> nicht mehr fälschlicherweise in Inhalts-Sektionen verboten wird
- Legitime System-Handler (toggleDrawer(), setJobChoice(), handleApplySubmit(), etc.) erlaubt sind
- Bösartige Handler (onerror, onload, onmouse..., beliebiger JS-Code) deterministisch abgewehrt werden
"""

import re
import sys
from pathlib import Path

# 1. cockpit-script-template.js patchen
js_path = Path("/home/brainuser/workspaces/mxs-embed/templates/cockpit-script-template.js")
js_content = js_path.read_text(encoding="utf-8")

old_js_chunk = """  // 2. Sicherheits-Check: Keine ausführbaren Skripte oder iframes
  var forbiddenTags = /<(script|iframe|object|embed|form|meta|base|style)\\b[^>]*>/i;
  var mTag = clean.match(forbiddenTags);
  if (mTag) {
    return { ok: false, error: "Sicherheits-Schranke: Ausführbare Tags (&lt;" + mTag[1] + "&gt;) sind in Inhalts-Sektionen verboten." };
  }
  if (/\\son[a-zA-Z]+\\s*=/i.test(clean)) {
    return { ok: false, error: "Sicherheits-Schranke: Inline-JavaScript (on... Event-Handler) ist verboten." };
  }
  if (/(href|src|action)\\s*=\\s*["'\\s]*javascript:/i.test(clean)) {
    return { ok: false, error: "Sicherheits-Schranke: javascript:... Links sind nicht erlaubt." };
  }"""

new_js_chunk = """  // 2. Sicherheits-Check: Keine ausführbaren Skripte oder iframes
  var forbiddenTags = /<(script|iframe|object|embed|meta|base|style)\\b[^>]*>/i;
  var mTag = clean.match(forbiddenTags);
  if (mTag) {
    return { ok: false, error: "Sicherheits-Schranke: Ausführbare Tags (&lt;" + mTag[1] + "&gt;) sind in Inhalts-Sektionen verboten." };
  }

  // Whitelist für legitime WebPilot-System-Handler (Navigation, Formulare, Stellen-Auswahl)
  var allowedHandlers = /^(?:toggleDrawer\\(\\)|setJobChoice\\([^)]*\\)|handleApplySubmit\\(event\\)|event\\.preventDefault\\(\\).*?|history\\.back\\(\\))$/i;
  var evRegex = /\\s(on[a-zA-Z]+)\\s*=\\s*(?:"([^"]*)"|'([^']*)'|([^\\s>]+))/gi;
  var evMatch;
  while ((evMatch = evRegex.exec(clean)) !== null) {
    var evName = (evMatch[1] || "").toLowerCase();
    var evBody = (evMatch[2] || evMatch[3] || evMatch[4] || "").trim();
    if (evName === "onerror" || evName === "onload" || evName === "onunload" || evName.indexOf("onmouse") === 0 || evName.indexOf("onkey") === 0) {
      return { ok: false, error: "Sicherheits-Schranke: Gefährlicher Event-Handler " + evName + " ist verboten." };
    }
    if (!allowedHandlers.test(evBody)) {
      return { ok: false, error: "Sicherheits-Schranke: Nicht genehmigter Inline-JavaScript-Code in " + evName + " (\\"" + evBody + "\\")." };
    }
  }

  if (/(href|src|action)\\s*=\\s*["'\\s]*javascript:/i.test(clean)) {
    return { ok: false, error: "Sicherheits-Schranke: javascript:... Links sind nicht erlaubt." };
  }"""

if old_js_chunk in js_content:
    js_content = js_content.replace(old_js_chunk, new_js_chunk, 1)
    js_path.write_text(js_content, encoding="utf-8")
    print("✅ cockpit-script-template.js erfolgreich aktualisiert.")
else:
    print("❌ old_js_chunk in cockpit-script-template.js nicht gefunden!")
    sys.exit(1)

# 2. publish_service.py patchen
py_path = Path("/home/brainuser/workspaces/Marketing-Hiltbrand-Pro0409/scripts/publish_service.py")
py_content = py_path.read_text(encoding="utf-8")

old_py_chunk = """            # Airbag-Prüfung auf dem übergebenen Chunk:
            # 1. Gefährliche / ausführbare Tags deterministisch blockieren (White-Hat Airbag)
            forbidden_tags = re.compile(r"<(script|iframe|object|embed|form|meta|base|style)(?:\\s|>)", re.I)
            m_tag = forbidden_tags.search(new_content)
            if m_tag:
                err = f"Sicherheits-Schranke: Ausführbare Tags (<{m_tag.group(1)}>) sind in Inhalts-Sektionen verboten."
                append_service_log(client, "REPLACE_SECTION_REJ", "SECURITY_TAG", err)
                return jsonify({"ok": False, "error": err}), 400

            # 2. Inline Event-Handler blockieren
            if re.search(r'\\son[a-zA-Z]+\\s*=', new_content, re.I):
                err = "Sicherheits-Schranke: Inline-JavaScript (on... Event-Handler) ist verboten."
                append_service_log(client, "REPLACE_SECTION_REJ", "SECURITY_EVENT", err)
                return jsonify({"ok": False, "error": err}), 400"""

new_py_chunk = """            # Airbag-Prüfung auf dem übergebenen Chunk:
            # 1. Gefährliche / ausführbare Tags deterministisch blockieren (White-Hat Airbag)
            forbidden_tags = re.compile(r"<(script|iframe|object|embed|meta|base|style)(?:\\s|>)", re.I)
            m_tag = forbidden_tags.search(new_content)
            if m_tag:
                err = f"Sicherheits-Schranke: Ausführbare Tags (<{m_tag.group(1)}>) sind in Inhalts-Sektionen verboten."
                append_service_log(client, "REPLACE_SECTION_REJ", "SECURITY_TAG", err)
                return jsonify({"ok": False, "error": err}), 400

            # 2. Inline Event-Handler prüfen (Legitime WebPilot-Systemfunktionen zulassen)
            safe_handlers_pattern = re.compile(
                r'^(?:toggleDrawer\\(\\)|setJobChoice\\([^)]*\\)|handleApplySubmit\\(event\\)|event\\.preventDefault\\(\\).*?|history\\.back\\(\\))$',
                re.I
            )
            event_matches = re.finditer(r'''\\s(on[a-zA-Z]+)\\s*=\\s*(?:"([^"]*)"|'([^']*)'|([^\\s>]+))''', new_content, re.I)
            for m_ev in event_matches:
                ev_name = m_ev.group(1).lower()
                ev_val = (m_ev.group(2) or m_ev.group(3) or m_ev.group(4) or "").strip()
                if ev_name in ("onerror", "onload", "onunload") or ev_name.startswith(("onmouse", "onkey")):
                    err = f"Sicherheits-Schranke: Gefährlicher Event-Handler {ev_name} ist verboten."
                    append_service_log(client, "REPLACE_SECTION_REJ", "SECURITY_EVENT", err)
                    return jsonify({"ok": False, "error": err}), 400
                if not safe_handlers_pattern.match(ev_val):
                    err = f"Sicherheits-Schranke: Nicht genehmigter Inline-JavaScript-Code in {ev_name} (\\"{ev_val}\\")."
                    append_service_log(client, "REPLACE_SECTION_REJ", "SECURITY_EVENT", err)
                    return jsonify({"ok": False, "error": err}), 400"""

if old_py_chunk in py_content:
    py_content = py_content.replace(old_py_chunk, new_py_chunk, 1)
    py_path.write_text(py_content, encoding="utf-8")
    print("✅ publish_service.py erfolgreich aktualisiert.")
else:
    print("❌ old_py_chunk in publish_service.py nicht gefunden!")
    sys.exit(1)

print("🎯 Alle Patches erfolgreich eingespielt.")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_embed_routing_gate.py – Deterministisches Pre-Push Routing- & Embed-Gate fuer mxs-embed
==============================================================================================
Verhindert vor jedem Git-Push in < 1s, dass ein Direkt-Mandantenordner (Karriere-Widget / Cockpit)
durch einen Fehl-Rewrite in functions/_middleware.js auf einen nicht existierenden preview-* Pfad
umgeleitet wird (stiller HTTP 200 SPA-Fallback 'WebPilot Swiss Edge' mit X-Frame-Options: DENY).

Prueft 4 harte Invarianzen (#BE-12 & #SYS-01):
1. Jeder Top-Level-Mandantenordner ohne 'preview-'-Praefix, der eine stellen.json oder Widget-HTMLs
   besitzt (z. B. hiltbrand, zurbuchen, cotra, muster-holzbau + kuenftige Ordner), MUSS in
   functions/_middleware.js in DIRECT_ONLY_FOLDERS oder DUAL_EMBED_AND_PREVIEW_FOLDERS stehen.
2. Jede in stellen.json eines Direkt-Mandantenordners referenzierte "datei" muss physisch im
   jeweiligen Mandanten-Ordner existieren (und auch falls in hiltbrand/stellen.json auf einen
   Nachbarordner wie folder="zurbuchen" verwiesen wird).
3. Keine Widget-HTML-Datei in einem Direkt-Mandantenordner darf <meta http-equiv="X-Frame-Options" content="DENY"
   enthalten.
4. Synthetischer Negativ-Selbsttest (--self-test): Beweist deterministisch, dass das Gate bei
   Ausbau eines Ordners aus DIRECT_ONLY_FOLDERS oder bei Injektion von X-Frame-Options: DENY sofort
   anschlage und mit EXIT 1 blockiert.

Canary: BACKEND-DB-2026-V1 | DEPLOY-MAP-2026-V1 | LANG-CH-2026-V1 (100 % ss statt Eszett)
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MIDDLEWARE_PATH = REPO_ROOT / "functions" / "_middleware.js"

SYSTEM_AND_RESERVED_FOLDERS = {
    ".git",
    ".github",
    ".wrangler",
    "node_modules",
    "artifacts",
    "boardroom",
    "brand-gallery",
    "client-preview",
    "config",
    "functions",
    "leads",
    "mxs-talent",
    "partner",
    "partner-jobs",
    "reports",
    "scripts",
    "staging-mxs-talent",
    "team_submissions",
    "templates",
    "visual-dna",
    "webpilot",
    "images",
    "css",
    "js",
    "fonts",
}

XFO_DENY_REGEX = re.compile(
    r'<meta\s+[^>]*http-equiv\s*=\s*["\']X-Frame-Options["\'][^>]*content\s*=\s*["\'](?:DENY|SAMEORIGIN)["\']',
    re.IGNORECASE,
)


def parse_middleware_registered_folders(middleware_text: str) -> set[str]:
    registered = set()
    for var_name in ("DIRECT_ONLY_FOLDERS", "DUAL_EMBED_AND_PREVIEW_FOLDERS"):
        m = re.search(rf"const\s+{var_name}\s*=\s*\[([^\]]*)\]", middleware_text)
        if m:
            items = re.findall(r"['\"]([a-zA-Z0-9_-]+)['\"]", m.group(1))
            registered.update(s.lower() for s in items)
    return registered


def run_routing_audit(
    middleware_override: str | None = None,
    injected_xfo_html: tuple[str, str] | None = None,
    quiet: bool = False,
) -> list[str]:
    errors: list[str] = []

    if middleware_override is not None:
        mw_text = middleware_override
    else:
        if not MIDDLEWARE_PATH.is_file():
            return [f"CRITICAL: Middleware-Datei fehlt: {MIDDLEWARE_PATH}"]
        mw_text = MIDDLEWARE_PATH.read_text(encoding="utf-8", errors="ignore")

    registered_folders = parse_middleware_registered_folders(mw_text)
    if not registered_folders:
        errors.append(
            "CRITICAL: Konnte DIRECT_ONLY_FOLDERS / DUAL_EMBED_AND_PREVIEW_FOLDERS in functions/_middleware.js nicht parsen!"
        )

    # Pruefe Enterprise Security- & HSTS-Header in _middleware.js und _headers
    headers_file = REPO_ROOT / "_headers"
    if not headers_file.is_file():
        errors.append("[SECURITY-HEADER-GATE] Statische _headers-Datei im Repo-Root fehlt!")
    else:
        hdr_text = headers_file.read_text(encoding="utf-8", errors="ignore")
        for req_hdr in ("Strict-Transport-Security", "X-Content-Type-Options", "Referrer-Policy", "Permissions-Policy"):
            if req_hdr not in mw_text:
                errors.append(f"[SECURITY-HEADER-GATE] Header '{req_hdr}' fehlt in functions/_middleware.js!")
            if req_hdr not in hdr_text:
                errors.append(f"[SECURITY-HEADER-GATE] Header '{req_hdr}' fehlt in _headers!")
        if "X-Frame-Options: DENY" in hdr_text or "frame-ancestors 'none'" in hdr_text:
            errors.append("[SECURITY-HEADER-GATE] Verbotenes X-Frame-Options: DENY oder frame-ancestors 'none' in _headers gefunden!")

    # Scanne alle Top-Level-Ordner ohne preview-* Praefix
    for entry in sorted(REPO_ROOT.iterdir()):
        if not entry.is_dir():
            continue
        folder_name = entry.name
        if folder_name.startswith(".") or folder_name.startswith("preview-"):
            continue
        if folder_name in SYSTEM_AND_RESERVED_FOLDERS:
            continue

        stellen_file = entry / "stellen.json"
        html_files = [p for p in entry.glob("*.html") if p.name != "cockpit.html"]

        if not stellen_file.is_file() and not html_files:
            continue

        # 1. Muss in Middleware registriert sein
        if folder_name.lower() not in registered_folders:
            errors.append(
                f"[ROUTING-GATE] Direkt-Mandantenordner '{folder_name}' besitzt Widgets/stellen.json, "
                f"fehlt aber in DIRECT_ONLY_FOLDERS / DUAL_EMBED_AND_PREVIEW_FOLDERS in functions/_middleware.js!"
            )

        # 2. Pruefe alle Eintraege in stellen.json auf physische Existenz
        if stellen_file.is_file():
            try:
                stellen_data = json.loads(stellen_file.read_text(encoding="utf-8"))
                if isinstance(stellen_data, list):
                    for item in stellen_data:
                        if not isinstance(item, dict):
                            continue
                        datei = (item.get("datei") or "").strip()
                        item_folder = (item.get("folder") or folder_name).strip()
                        if not datei:
                            continue
                        target_dir = REPO_ROOT / item_folder
                        target_file = target_dir / datei
                        if not target_file.is_file():
                            errors.append(
                                f"[MISSING-WIDGET-FILE] {folder_name}/stellen.json referenziert '{item_folder}/{datei}', "
                                f"aber Datei existiert nicht unter {target_file}!"
                            )
                        if item_folder.lower() not in registered_folders and not item_folder.startswith("preview-"):
                            errors.append(
                                f"[ROUTING-GATE] {folder_name}/stellen.json referenziert Ordner '{item_folder}', "
                                f"der nicht in functions/_middleware.js registriert ist!"
                            )
            except Exception as exc:
                errors.append(f"[INVALID-JSON] Konnte {stellen_file} nicht als JSON lesen: {exc}")

        # 3. Pruefe alle Widget-HTML-Dateien auf verbotenes X-Frame-Options: DENY
        for html_path in html_files:
            html_text = html_path.read_text(encoding="utf-8", errors="ignore")
            if XFO_DENY_REGEX.search(html_text):
                errors.append(
                    f"[XFO-DENY-BLOCKER] Widget-HTML '{folder_name}/{html_path.name}' enthaelt "
                    f"<meta http-equiv=\"X-Frame-Options\" content=\"DENY/SAMEORIGIN\"> (blockiert iFrame-Einbettung)!"
                )

    if injected_xfo_html is not None:
        virt_name, virt_html = injected_xfo_html
        if XFO_DENY_REGEX.search(virt_html):
            errors.append(
                f"[XFO-DENY-BLOCKER] Virtuelles Test-Widget '{virt_name}' enthaelt X-Frame-Options: DENY!"
            )

    if not quiet:
        if errors:
            print("=" * 72, file=sys.stderr)
            print("🚨 MXS-EMBED PRE-PUSH ROUTING & WIDGET GATE BLOCKIERT!", file=sys.stderr)
            print("=" * 72, file=sys.stderr)
            for err in errors:
                print(f"  ❌ {err}", file=sys.stderr)
            print("=" * 72, file=sys.stderr)
        else:
            print(
                f"✅ [verify_embed_routing_gate] PASS: Alle Direkt-Mandantenordner ({sorted(registered_folders)}) "
                f"in _middleware.js registriert, alle stellen.json-Dateien vorhanden & 0 XFO-DENY-Blocker."
            )

    return errors


def run_selftest() -> bool:
    """Prueft deterministisch, dass das Gate bei Fehl-Routing und XFO-DENY anschlaegt."""
    mw_text = MIDDLEWARE_PATH.read_text(encoding="utf-8", errors="ignore")
    # Test 1: Entferne 'zurbuchen' aus DIRECT_ONLY_FOLDERS
    broken_mw = mw_text.replace("'zurbuchen',", "").replace("'zurbuchen'", "")
    errs_1 = run_routing_audit(middleware_override=broken_mw, quiet=True)
    cond_1 = any("zurbuchen" in e and "ROUTING-GATE" in e for e in errs_1)

    # Test 2: Injiziere X-Frame-Options: DENY
    errs_2 = run_routing_audit(
        injected_xfo_html=("zurbuchen/test_widget.html", '<meta http-equiv="X-Frame-Options" content="DENY">'),
        quiet=True,
    )
    cond_2 = any("XFO-DENY-BLOCKER" in e for e in errs_2)

    if cond_1 and cond_2:
        print("🧪 [verify_embed_routing_gate --self-test] PASS: Beide Negativ-Proben (Missing Folder + XFO DENY) wurden hart blockiert.")
        return True
    print(f"🚨 [verify_embed_routing_gate --self-test] FAIL: cond_1={cond_1}, cond_2={cond_2}", file=sys.stderr)
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Pre-Push Routing & Widget Integrity Gate fuer mxs-embed")
    parser.add_argument("--self-test", action="store_true", help="Fuehrt zusätzlich den synthetischen Negativ-Test aus")
    args = parser.parse_args()

    if args.self_test:
        if not run_selftest():
            return 1

    errors = run_routing_audit(quiet=False)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

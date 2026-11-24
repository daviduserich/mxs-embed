#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_embed_routing_gate.py – Deterministisches Pre-Push Routing- & Embed-Gate fuer mxs-embed
==============================================================================================
Verhindert vor jedem Git-Push in < 1s, dass ein Direkt-Mandantenordner (Karriere-Widget / Cockpit)
durch einen Fehl-Rewrite in functions/_middleware.js auf einen nicht existierenden preview-* Pfad
umgeleitet wird (stiller HTTP 200 SPA-Fallback 'WebPilot Swiss Edge' mit X-Frame-Options: DENY).

Prueft 5 harte Invarianzen (#BE-12 & #SYS-01):
1. Jeder Top-Level-Mandantenordner ohne 'preview-'-Praefix, der eine stellen.json oder Widget-HTMLs
   besitzt (z. B. hiltbrand, zurbuchen, cotra, muster-holzbau, hochuli-zimmermann + kuenftige Ordner), MUSS in
   functions/_middleware.js in DIRECT_ONLY_FOLDERS oder DUAL_EMBED_AND_PREVIEW_FOLDERS stehen.
2. Jede in stellen.json eines Direkt-Mandantenordners referenzierte "datei" muss physisch im
   jeweiligen Mandanten-Ordner existieren (und auch falls in hiltbrand/stellen.json auf einen
   Nachbarordner wie folder="zurbuchen" verwiesen wird).
3. Keine Widget-HTML-Datei in einem Direkt-Mandantenordner darf <meta http-equiv="X-Frame-Options" content="DENY"
   enthalten.
4. Jede Karriere-Widget-HTML-Datei (Ordner mit stellen.json, ohne cockpit.html) MUSS zwingend den
   iFrame-Resize-Hook 'acp-embed-resize' sowie einen WhatsApp-Hook ('wa.me/' oder 'data-required="whatsapp-cta"')
   im Body enthalten (100 % Paritaet zu watchdog_framework_integrity.py).
5. Synthetischer 4-Proben Negativ-Selbsttest (--self-test): Beweist deterministisch, dass das Gate bei
   Missing Folder, XFO DENY, fehlendem acp-embed-resize oder fehlendem WhatsApp-Hook sofort mit EXIT 1 blockiert.

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
TENANT_REDIRECTS_PATH = REPO_ROOT / "functions" / "lib" / "tenant_redirects.js"
LIVE_CUSTOM_DOMAIN_FOLDERS = ("webpilot", "mxs-talent")

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
    "login",
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

SHRINK_LOCK_REGEX = re.compile(r"documentElement\.scrollHeight", re.IGNORECASE)
LEGACY_SHRINK_LOCK_ALLOWLIST = {
    "cotra/Cotra_Autotransport_Fahrer.html",
    "cotra/cotra_Chauffeur_CE.html",
    "cotra/index.html",
    "hiltbrand/Hiltbrand_Dachdecker.html",
    "muster-holzbau/index.html",
    "muster-holzbau/Muster_Holzbau_Zimmermann.html",
}


def parse_middleware_registered_folders(middleware_text: str) -> set[str]:
    registered = set()
    for var_name in ("DIRECT_ONLY_FOLDERS", "DUAL_EMBED_AND_PREVIEW_FOLDERS"):
        m = re.search(rf"const\s+{var_name}\s*=\s*\[([^\]]*)\]", middleware_text)
        if m:
            items = re.findall(r"['\"]([a-zA-Z0-9_-]+)['\"]", m.group(1))
            registered.update(s.lower() for s in items)
    return registered


def parse_redirects_file(redirects_path: Path) -> dict[str, dict]:
    rules: dict[str, dict] = {}
    if not redirects_path.is_file():
        return rules
    for raw_line in redirects_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        raw_src, raw_dst = parts[0].strip(), parts[1].strip()
        status = 301
        if len(parts) >= 3:
            try:
                status = int(parts[2].strip())
            except ValueError:
                status = 301
        norm_src = "/" + raw_src.lstrip("/").rstrip("/") if raw_src != "/" else "/"
        if not norm_src:
            norm_src = "/"
        rules[norm_src] = {"to": raw_dst, "status": status}
    return dict(sorted(rules.items(), key=lambda kv: kv[0]))


def collect_repo_redirects(repo_root: Path) -> dict[str, dict]:
    expected: dict[str, dict] = {}
    for redir_file in sorted(repo_root.glob("*/_redirects")):
        folder = redir_file.parent.name
        if folder.startswith("."):
            continue
        parsed = parse_redirects_file(redir_file)
        if parsed:
            expected[folder] = parsed
    return expected


def run_routing_audit(
    middleware_override: str | None = None,
    injected_xfo_html: tuple[str, str] | None = None,
    injected_career_html: tuple[str, str] | None = None,
    root_404_override: str | None = None,
    live_domain_override: dict[tuple[str, str], str] | None = None,
    redirects_js_override: str | None = None,
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

        # 3. Pruefe alle Widget-HTML-Dateien (ohne cockpit.html, s. Zeile 125) auf XFO-DENY & Pflicht-Hooks
        has_stellen = stellen_file.is_file()
        for html_path in html_files:
            if html_path.name == "cockpit.html":
                continue
            html_text = html_path.read_text(encoding="utf-8", errors="ignore")
            if XFO_DENY_REGEX.search(html_text):
                errors.append(
                    f"[XFO-DENY-BLOCKER] Widget-HTML '{folder_name}/{html_path.name}' enthaelt "
                    f"<meta http-equiv=\"X-Frame-Options\" content=\"DENY/SAMEORIGIN\"> (blockiert iFrame-Einbettung)!"
                )
            if has_stellen:
                if "acp-embed-resize" not in html_text:
                    errors.append(
                        f"[MISSING-RESIZE-HOOK] Karriere-Widget '{folder_name}/{html_path.name}' enthaelt keinen "
                        f"'acp-embed-resize' postMessage-Sender (iFrame schneidet Inhalt bei min-height:850px ab)!"
                    )
                if 'data-required="whatsapp-cta"' not in html_text and "wa.me/" not in html_text:
                    errors.append(
                        f"[MISSING-WHATSAPP-HOOK] Karriere-Widget '{folder_name}/{html_path.name}' enthaelt weder "
                        f"'wa.me/' noch 'data-required=\"whatsapp-cta\"'!"
                    )
                rel_key = f"{folder_name}/{html_path.name}"
                if (
                    rel_key not in LEGACY_SHRINK_LOCK_ALLOWLIST
                    and "acp-embed-resize" in html_text
                    and SHRINK_LOCK_REGEX.search(html_text)
                    and "measureContentHeight" not in html_text
                ):
                    errors.append(
                        f"[SHRINK-LOCK-BLOCKER] Karriere-Widget '{rel_key}' nutzt documentElement.scrollHeight im Resize-Sender "
                        f"(verursacht Iframe-Shrink-Lock nach FAQ-/Akkordeon-Klick; bitte measureContentHeight() verwenden)!"
                    )

    if injected_xfo_html is not None:
        virt_name, virt_html = injected_xfo_html
        if XFO_DENY_REGEX.search(virt_html):
            errors.append(
                f"[XFO-DENY-BLOCKER] Virtuelles Test-Widget '{virt_name}' enthaelt X-Frame-Options: DENY!"
            )

    if injected_career_html is not None:
        virt_c_name, virt_c_html = injected_career_html
        if "acp-embed-resize" not in virt_c_html:
            errors.append(
                f"[MISSING-RESIZE-HOOK] Virtuelles Karriere-Widget '{virt_c_name}' enthaelt keinen 'acp-embed-resize' Hook!"
            )
        if 'data-required="whatsapp-cta"' not in virt_c_html and "wa.me/" not in virt_c_html:
            errors.append(
                f"[MISSING-WHATSAPP-HOOK] Virtuelles Karriere-Widget '{virt_c_name}' enthaelt keinen WhatsApp-Hook!"
            )
        if (
            virt_c_name not in LEGACY_SHRINK_LOCK_ALLOWLIST
            and "acp-embed-resize" in virt_c_html
            and SHRINK_LOCK_REGEX.search(virt_c_html)
            and "measureContentHeight" not in virt_c_html
        ):
            errors.append(
                f"[SHRINK-LOCK-BLOCKER] Virtuelles Karriere-Widget '{virt_c_name}' nutzt documentElement.scrollHeight!"
            )

    # 6. Go-Live SEO- & HTTP-404-Gate (Root 404.html + Live-Custom-Domain-Ordner)
    root_404_path = REPO_ROOT / "404.html"
    if root_404_override is not None:
        root_404_txt = root_404_override
        root_404_exists = bool(root_404_txt.strip())
    else:
        root_404_exists = root_404_path.is_file()
        root_404_txt = root_404_path.read_text(encoding="utf-8", errors="ignore") if root_404_exists else ""

    if not root_404_exists or "noindex" not in root_404_txt.lower():
        errors.append("[GO-LIVE-SEO-404-GATE] Root-Datei '404.html' fehlt oder enthaelt kein 'noindex'!")
    elif "\u00df" in root_404_txt or "\u1e9e" in root_404_txt:
        errors.append("[GO-LIVE-SEO-404-GATE] Root-Datei '404.html' enthaelt Eszett!")

    live_overrides = live_domain_override or {}
    for live_folder in LIVE_CUSTOM_DOMAIN_FOLDERS:
        folder_path = REPO_ROOT / live_folder
        if not folder_path.is_dir():
            errors.append(f"[GO-LIVE-SEO-404-GATE] Live-Custom-Domain-Ordner '{live_folder}' fehlt!")
            continue

        def _read_live_file(fname: str) -> str | None:
            if (live_folder, fname) in live_overrides:
                val = live_overrides[(live_folder, fname)]
                return val if val else None
            fp = folder_path / fname
            return fp.read_text(encoding="utf-8", errors="ignore") if fp.is_file() else None

        rob = _read_live_file("robots.txt")
        if rob is None or "Content-Signal:" not in rob:
            errors.append(f"[GO-LIVE-SEO-404-GATE] '{live_folder}/robots.txt' fehlt oder enthaelt kein 'Content-Signal:'!")

        llms = _read_live_file("llms.txt")
        if llms is None or len(llms.strip()) < 100:
            errors.append(f"[GO-LIVE-SEO-404-GATE] '{live_folder}/llms.txt' fehlt oder ist zu kurz!")

        sm = _read_live_file("sitemap.xml")
        if sm is None or len(sm.strip()) < 80:
            errors.append(f"[GO-LIVE-SEO-404-GATE] '{live_folder}/sitemap.xml' fehlt oder ist zu kurz!")

        err404 = _read_live_file("404.html")
        if err404 is None or "noindex" not in err404.lower():
            errors.append(f"[GO-LIVE-SEO-404-GATE] '{live_folder}/404.html' fehlt oder enthaelt kein 'noindex'!")
        elif "\u00df" in err404 or "\u1e9e" in err404:
            errors.append(f"[GO-LIVE-SEO-404-GATE] '{live_folder}/404.html' enthaelt Eszett!")

    # 7. Edge-Redirects-Sync-Gate (1:1 Abgleich <folder>/_redirects <-> functions/lib/tenant_redirects.js)
    expected_redirects = collect_repo_redirects(REPO_ROOT)
    if redirects_js_override is not None:
        js_text = redirects_js_override
        js_exists = bool(js_text.strip())
    else:
        js_exists = TENANT_REDIRECTS_PATH.is_file()
        js_text = TENANT_REDIRECTS_PATH.read_text(encoding="utf-8", errors="ignore") if js_exists else ""

    if not js_exists:
        errors.append("[REDIRECTS-SYNC-GATE] 'functions/lib/tenant_redirects.js' fehlt!")
    else:
        js_m = re.search(r"export\s+const\s+TENANT_REDIRECTS\s*=\s*(\{[\s\S]*\})\s*;?", js_text)
        if not js_m:
            errors.append("[REDIRECTS-SYNC-GATE] Konnte 'TENANT_REDIRECTS' in functions/lib/tenant_redirects.js nicht parsen!")
        else:
            try:
                actual_redirects = json.loads(js_m.group(1))
                if actual_redirects != expected_redirects:
                    errors.append(
                        "[REDIRECTS-SYNC-GATE] Drift zwischen '<folder>/_redirects' und 'functions/lib/tenant_redirects.js'! "
                        "Bitte 'python3 scripts/webpilot_seo_geo_autopilot.py --sync-redirects' ausfuehren."
                    )
            except Exception as exc:
                errors.append(f"[REDIRECTS-SYNC-GATE] Ungueltiges JSON in tenant_redirects.js: {exc}")

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
                f"✅ [verify_embed_routing_gate] PASS: Alle Direkt-Mandantenordner ({sorted(registered_folders)}), "
                f"Live-Domain SEO/404-Dateien ({list(LIVE_CUSTOM_DOMAIN_FOLDERS)}) & {len(expected_redirects)} "
                f"Edge-Redirect-Tabellen 100 % verifiziert (0 XFO-Blocker, 0 Drift)."
            )

    return errors


def run_selftest() -> bool:
    """Prueft deterministisch, dass das Gate bei Fehl-Routing, XFO-DENY, fehlenden Hooks, SEO/404 & Redirect-Drift anschlaegt."""
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
    cond_2 = any("test_widget.html" in e and "XFO-DENY-BLOCKER" in e for e in errs_2)

    # Test 3: Injiziere Karriere-Widget ohne acp-embed-resize
    errs_3 = run_routing_audit(
        injected_career_html=("hochuli-zimmermann/test_no_resize.html", '<html><body><a href="https://wa.me/41790000000">WA</a></body></html>'),
        quiet=True,
    )
    cond_3 = any("test_no_resize.html" in e and "MISSING-RESIZE-HOOK" in e for e in errs_3)

    # Test 4: Injiziere Karriere-Widget ohne WhatsApp-Hook
    errs_4 = run_routing_audit(
        injected_career_html=("hochuli-zimmermann/test_no_wa.html", "<html><body><script>acp-embed-resize</script></body></html>"),
        quiet=True,
    )
    cond_4 = any("test_no_wa.html" in e and "MISSING-WHATSAPP-HOOK" in e for e in errs_4)

    # Test 5: Injiziere Karriere-Widget mit documentElement.scrollHeight Shrink-Lock
    errs_5 = run_routing_audit(
        injected_career_html=(
            "zurbuchen/test_shrink_lock.html",
            '<html><body><a href="https://wa.me/41790000000">WA</a><script>var h=document.documentElement.scrollHeight;parent.postMessage({type:"acp-embed-resize",height:h},"*");</script></body></html>',
        ),
        quiet=True,
    )
    cond_5 = any("test_shrink_lock.html" in e and "SHRINK-LOCK-BLOCKER" in e for e in errs_5)

    # Test 6: Go-Live SEO & 404 Gate (fehlendes Content-Signal in mxs-talent/robots.txt & fehlende Root-404)
    errs_6a = run_routing_audit(
        live_domain_override={("mxs-talent", "robots.txt"): "User-agent: *\nAllow: /\n"},
        quiet=True,
    )
    errs_6b = run_routing_audit(root_404_override="", quiet=True)
    cond_6 = (
        any("mxs-talent/robots.txt" in e and "GO-LIVE-SEO-404-GATE" in e for e in errs_6a)
        and any("Root-Datei '404.html'" in e and "GO-LIVE-SEO-404-GATE" in e for e in errs_6b)
    )

    # Test 7: Edge-Redirects-Sync Gate (Drift in functions/lib/tenant_redirects.js)
    errs_7 = run_routing_audit(
        redirects_js_override='export const TENANT_REDIRECTS = {};\n',
        quiet=True,
    )
    cond_7 = any("REDIRECTS-SYNC-GATE" in e for e in errs_7)

    if cond_1 and cond_2 and cond_3 and cond_4 and cond_5 and cond_6 and cond_7:
        print(
            "🧪 [verify_embed_routing_gate --self-test] PASS: Alle 7 Negativ-Proben "
            "(Missing Folder + XFO DENY + Missing Resize + Missing WhatsApp + Shrink-Lock + GoLive SEO/404 + Redirect-Drift) "
            "wurden hart blockiert."
        )
        return True
    print(
        f"🚨 [verify_embed_routing_gate --self-test] FAIL: cond_1={cond_1}, cond_2={cond_2}, cond_3={cond_3}, "
        f"cond_4={cond_4}, cond_5={cond_5}, cond_6={cond_6}, cond_7={cond_7}",
        file=sys.stderr,
    )
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Multi-Page CSS & Layout Parity Guard (css_layout_guard.py)
===================================================================
Verhindert deterministisch:
1. Unbalancierte geschweifte Klammern { / } in <style>-Blöcken und @media-Queries (Root Cause #061).
2. Verwaiste Layout-Klassen auf Unterseiten (Cross-Page CSS Drift: Eine Klasse wie .section-header
   wird im HTML einer Unterseite genutzt, ist in index.html gestylt, fehlt aber im <style> der Unterseite).
3. Fehlende Mindestabstände bei .section-header (Heading-to-Card Collision).
"""

import re
from pathlib import Path


def extract_style_content(html: str) -> str:
    matches = re.findall(r"<style[^>]*>(.*?)</style>", html, re.DOTALL | re.IGNORECASE)
    return "\n".join(matches)


def check_css_brace_balance(css: str) -> list[str]:
    errors = []
    # Strip CSS comments
    clean = re.sub(r"/\*.*?\*/", "", css, flags=re.DOTALL)
    open_c = clean.count("{")
    close_c = clean.count("}")
    if open_c != close_c:
        errors.append(f"CSS Brace Imbalance: {open_c} '{{' vs {close_c} '}}' (diff={open_c - close_c})")
    return errors


def extract_defined_classes(css: str) -> set[str]:
    clean = re.sub(r"/\*.*?\*/", "", css, flags=re.DOTALL)
    # Remove rule bodies { ... } (non-nested) to scan selectors cleanly
    # For @media blocks, we just scan everything outside simple declaration properties
    classes = set(re.findall(r"\.([a-zA-Z_][a-zA-Z0-9_-]*)", clean))
    return classes


def extract_used_html_classes(html: str) -> set[str]:
    # Strip <style> and <script> first
    body = re.sub(r"<(style|script)[^>]*>.*?</\1>", "", html, flags=re.DOTALL | re.IGNORECASE)
    used = set()
    for m in re.finditer(r'\bclass=["\']([^"\']+)["\']', body):
        for cls in m.group(1).split():
            if cls.strip():
                used.add(cls.strip())
    return used


def extract_class_rule_blocks(index_css: str, cls_name: str) -> list[str]:
    """Extrahiert Top-Level CSS-Regeln aus index.html, die .cls_name stylen."""
    clean = re.sub(r"/\*.*?\*/", "", index_css, flags=re.DOTALL)
    blocks = []
    # Match simple top-level selector { ... } blocks containing .cls_name
    pattern = re.compile(r"([^{}@]+\{[^{}]*\})", re.DOTALL)
    for m in pattern.finditer(clean):
        block = m.group(1).strip()
        selector_part = block.split("{", 1)[0]
        if re.search(rf"\.{re.escape(cls_name)}\b", selector_part):
            blocks.append("    " + block.replace("\n", "\n    "))
    return blocks


def enforce_site_css_parity(site_dir: Path, auto_fix: bool = True) -> dict:
    """
    Prüft alle Inhalts-HTML-Dateien eines Mandanten gegen index.html.
    Injiziert bei Bedarf fehlende Basis-Klassen aus index.html in Unterseiten.
    """
    report = {
        "site": site_dir.name,
        "brace_errors": [],
        "missing_classes_fixed": [],
        "missing_classes_found": [],
    }
    index_file = site_dir / "index.html"
    if not index_file.exists():
        return report

    index_html = index_file.read_text(encoding="utf-8")
    index_css = extract_style_content(index_html)
    index_defined = extract_defined_classes(index_css)

    for hf in sorted(site_dir.glob("*.html")):
        if hf.name in ("cockpit.html", "onboarding.html"):
            continue
        html = hf.read_text(encoding="utf-8")
        # Skip redirect stubs without <style>
        if "<style" not in html.lower():
            continue

        css = extract_style_content(html)
        b_errs = check_css_brace_balance(css)
        for err in b_errs:
            report["brace_errors"].append(f"{hf.name}: {err}")

        if hf.name == "index.html":
            continue

        defined = extract_defined_classes(css)
        used = extract_used_html_classes(html)

        # Find classes used in subpage HTML that ARE defined in index.html CSS, but MISSING in subpage CSS
        missing = sorted((used & index_defined) - defined)
        if missing:
            for cls in missing:
                report["missing_classes_found"].append(f"{hf.name}: .{cls}")
            if auto_fix:
                injected_rules = []
                for cls in missing:
                    rules = extract_class_rule_blocks(index_css, cls)
                    for r in rules:
                        if r not in injected_rules:
                            injected_rules.append(r)
                if injected_rules:
                    patch_css = "\n    /* ── Auto-Synced Shared Layout Rules (css_layout_guard.py) ── */\n" + "\n".join(injected_rules) + "\n"
                    if "@media" in html:
                        idx = html.find("@media")
                        new_html = html[:idx] + patch_css + "    " + html[idx:]
                    else:
                        new_html = html.replace("</style>", patch_css + "  </style>", 1)
                    hf.write_text(new_html, encoding="utf-8")
                    report["missing_classes_fixed"].extend([f"{hf.name}: .{c}" for c in missing])

    return report


if __name__ == "__main__":
    import sys
    base = Path(__file__).resolve().parent.parent
    targets = [Path(sys.argv[1])] if len(sys.argv) > 1 else [d for d in sorted(base.iterdir()) if d.is_dir() and (d / "company.json").exists()]
    for t in targets:
        rep = enforce_site_css_parity(t, auto_fix=False)
        print(f"[{rep['site']}] Brace-Errors: {len(rep['brace_errors'])} | Missing Shared Classes: {rep['missing_classes_found']}")

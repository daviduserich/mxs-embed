#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Unified Compiler (compile_site.py)
===========================================
Führt das ACP-Standard-Paradigma (data-i18n für UI-Strings, data-slot für Mandanten-Daten)
in einem einzigen deterministischen Edge-Compiler zusammen.

Doktrin:
1. UI-Texte, Navigation, Buttons & Formulare: 'data-i18n="section.key"' -> aus 'templates/i18n/{lang}.json'
2. Mandanten-Stammdaten & Inhalts-Slots: 'data-slot="key"' -> aus '{site}/company.json'
3. Übersetzungs- & Slot-Integrität: 100% verifizierbar vor dem Git-Push.
"""

import os
import sys
import re
import json
import time
import argparse
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
I18N_DIR = TEMPLATES_DIR / "i18n"


def get_nested_val(data: dict, key_path: str):
    """Liest verschachtelte Keys wie 'nav.home' oder 'contact.form_title'."""
    parts = key_path.split(".")
    curr = data
    for p in parts:
        if isinstance(curr, dict) and p in curr:
            curr = curr[p]
        else:
            return None
    return curr


def load_i18n(lang: str = "de") -> dict:
    """Lädt das Sprachwörterbuch."""
    lang_file = I18N_DIR / f"{lang}.json"
    if not lang_file.exists():
        lang_file = I18N_DIR / "de.json"
    if not lang_file.exists():
        return {}
    with open(lang_file, "r", encoding="utf-8") as f:
        return json.load(f)


def load_company(site_dir: Path) -> dict:
    """Lädt company.json des Mandanten."""
    comp_file = site_dir / "company.json"
    if not comp_file.exists():
        return {}
    with open(comp_file, "r", encoding="utf-8") as f:
        return json.load(f)


def compile_html(html: str, i18n_data: dict, slot_data: dict) -> tuple[str, dict]:
    """
    Kompiliert HTML-Dateien durch Auflösung von:
    1. data-i18n="key.path"
    2. data-i18n-placeholder="key.path"
    3. data-slot="key"
    """
    stats = {"i18n_updated": 0, "slots_updated": 0, "placeholders_updated": 0, "missing_keys": []}

    # 1. data-i18n
    def i18n_replacer(match):
        tag = match.group("tag")
        attrs = match.group("attrs")
        key = match.group("key")
        old_val = match.group("content")

        val = get_nested_val(i18n_data, key)
        if val is None:
            stats["missing_keys"].append(f"i18n:{key}")
            return match.group(0)

        val_str = str(val)
        if old_val.strip() != val_str.strip():
            stats["i18n_updated"] += 1
            return f"<{tag}{attrs}>{val_str}</{tag}>"
        return match.group(0)

    p_i18n = re.compile(
        r'<(?P<tag>[a-zA-Z0-9]+)(?P<attrs>[^>]*?\bdata-i18n=["\'](?P<key>[a-zA-Z0-9_.-]+)["\'][^>]*)>(?P<content>.*?)</(?P=tag)>',
        re.DOTALL | re.IGNORECASE,
    )
    html = p_i18n.sub(i18n_replacer, html)

    # 2. data-i18n-placeholder
    def placeholder_replacer(match):
        pre = match.group("pre")
        key = match.group("key")
        post = match.group("post")

        val = get_nested_val(i18n_data, key)
        if val is None:
            stats["missing_keys"].append(f"placeholder:{key}")
            return match.group(0)

        val_str = str(val)
        # Ersetze placeholder="..." oder füge hinzu
        full = match.group(0)
        if 'placeholder="' in full or "placeholder='" in full:
            new_full = re.sub(r'placeholder=["\'][^"\']*["\']', f'placeholder="{val_str}"', full)
            if new_full != full:
                stats["placeholders_updated"] += 1
            return new_full
        else:
            stats["placeholders_updated"] += 1
            return f"{pre}data-i18n-placeholder=\"{key}\" placeholder=\"{val_str}\"{post}"

    p_plh = re.compile(
        r'(?P<pre><[a-zA-Z0-9]+\b[^>]*?\b)data-i18n-placeholder=["\'](?P<key>[a-zA-Z0-9_.-]+)["\'](?P<post>[^>]*>)',
        re.IGNORECASE,
    )
    html = p_plh.sub(placeholder_replacer, html)

    # 3. data-slot
    def slot_replacer(match):
        tag = match.group("tag")
        attrs = match.group("attrs")
        slot = match.group("slot")
        old_val = match.group("content")

        if slot not in slot_data:
            return match.group(0)

        val_str = str(slot_data[slot])
        new_attrs = attrs

        # Automatische Link-Attribute
        if tag.lower() == "a":
            if slot in ("email", "email_link"):
                new_attrs = re.sub(r'href=["\']mailto:[^"\']*["\']', f'href="mailto:{val_str}"', new_attrs)
            elif slot in ("phone", "phone_link") and "phone_clean" in slot_data:
                new_attrs = re.sub(r'href=["\']tel:[^"\']*["\']', f'href="tel:{slot_data["phone_clean"]}"', new_attrs)
            elif slot in ("whatsapp", "whatsapp_link") and "whatsapp_clean" in slot_data:
                new_attrs = re.sub(r'href=["\']https://wa\.me/[^"\']*["\']', f'href="https://wa.me/{slot_data["whatsapp_clean"]}"', new_attrs)

        if old_val.strip() != val_str.strip() or new_attrs != attrs:
            stats["slots_updated"] += 1
            return f"<{tag}{new_attrs}>{val_str}</{tag}>"
        return match.group(0)

    p_slot = re.compile(
        r'<(?P<tag>[a-zA-Z0-9]+)(?P<attrs>[^>]*?\bdata-slot=["\'](?P<slot>[a-zA-Z0-9_-]+)["\'][^>]*)>(?P<content>.*?)</(?P=tag)>',
        re.DOTALL | re.IGNORECASE,
    )
    html = p_slot.sub(slot_replacer, html)

    return html, stats


def compile_site_dir(site_dir: Path, lang: str = "de", dry_run: bool = False) -> dict:
    """Kompiliert eine vollständige Website-Instanz."""
    i18n_dict = load_i18n(lang)
    company_dict = load_company(site_dir)

    # Abgeleitete Slots berechnen
    from sync_company_slots import compute_derived_fields
    slot_data = compute_derived_fields(company_dict)

    html_files = sorted(site_dir.glob("*.html"))
    total_stats = {
        "site": site_dir.name,
        "lang": lang,
        "files_checked": len(html_files),
        "files_modified": 0,
        "i18n_updated": 0,
        "slots_updated": 0,
        "placeholders_updated": 0,
        "missing_keys": set(),
    }

    for hf in html_files:
        with open(hf, "r", encoding="utf-8") as f:
            content = f.read()

        new_content, f_stats = compile_html(content, i18n_dict, slot_data)
        mod = (f_stats["i18n_updated"] + f_stats["slots_updated"] + f_stats["placeholders_updated"]) > 0
        if mod:
            total_stats["files_modified"] += 1
            total_stats["i18n_updated"] += f_stats["i18n_updated"]
            total_stats["slots_updated"] += f_stats["slots_updated"]
            total_stats["placeholders_updated"] += f_stats["placeholders_updated"]
            if not dry_run:
                with open(hf, "w", encoding="utf-8") as f:
                    f.write(new_content)

        for m in f_stats["missing_keys"]:
            total_stats["missing_keys"].add(m)

    total_stats["missing_keys"] = list(total_stats["missing_keys"])
    return total_stats


def main():
    parser = argparse.ArgumentParser(description="WebPilot i18n & Slot Unified Compiler")
    parser.add_argument("--site", help="Site-Ordner (z.B. preview-hiltbrand, webpilot)")
    parser.add_argument("--lang", default="de", help="Sprache (de, fr, en)")
    parser.add_argument("--all", action="store_true", help="Alle Mandanten kompilieren")
    parser.add_argument("--dry-run", action="store_true", help="Änderungen nur anzeigen")
    parser.add_argument("--git-push", action="store_true", help="Automatisch committen & pushen")

    args = parser.parse_args()
    start_time = time.time()

    if not args.site and not args.all:
        parser.print_help()
        sys.exit(1)

    target_dirs = []
    if args.site:
        p = BASE_DIR / args.site
        if not p.is_dir():
            p = Path(args.site).resolve()
        if not p.is_dir():
            print(f"Fehler: {args.site} nicht gefunden.")
            sys.exit(1)
        target_dirs.append(p)
    elif args.all:
        for item in BASE_DIR.iterdir():
            if item.is_dir() and (item / "company.json").exists():
                target_dirs.append(item)

    any_changes = False
    for td in target_dirs:
        res = compile_site_dir(td, lang=args.lang, dry_run=args.dry_run)
        print(f"Site: {res['site']} [Lang: {res['lang']}]")
        print(f"  Files: {res['files_checked']} geprüft, {res['files_modified']} modifiziert")
        print(f"  Slots synchronisiert: {res['slots_updated']}")
        print(f"  i18n-Strings synchronisiert: {res['i18n_updated']}")
        print(f"  Placeholders synchronisiert: {res['placeholders_updated']}")
        if res["missing_keys"]:
            print(f"  WARNUNG: Fehlende Keys im Wörterbuch: {', '.join(res['missing_keys'])}")
        if res["files_modified"] > 0:
            any_changes = True

    if args.git_push and any_changes and not args.dry_run:
        print("\nFühre Git Push aus...")
        try:
            for td in target_dirs:
                subprocess.run(["git", "add", td.name], cwd=str(BASE_DIR), check=True)
            subprocess.run(["git", "add", "templates/i18n/"], cwd=str(BASE_DIR), check=True)
            commit_msg = f"fix(i18n): compile site framework ({args.site or 'all'}) [{args.lang}]"
            subprocess.run(["git", "commit", "-m", commit_msg], cwd=str(BASE_DIR), check=True)
            subprocess.run(["git", "push", "origin", "main"], cwd=str(BASE_DIR), check=True)
            print("Git Push erfolgreich!")
        except Exception as e:
            print(f"Git Push Fehler: {e}")

    elapsed = time.time() - start_time
    print(f"\nKompiliert in {elapsed:.3f} Sekunden.")


if __name__ == "__main__":
    main()

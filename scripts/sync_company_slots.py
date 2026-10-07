#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Metadata & Semantic Slot Compiler (sync_company_slots.py)
===================================================================
Zentraler Compiler zur blitzschnellen Aktualisierung von Firmen-, Kontakt-
und Footer-Metadaten über alle HTML-Dateien eines WebPilot-Mandanten.

Doktrin: Single Source of Truth
- Alle Stammdaten liegen exklusiv in 'company.json' im jeweiligen Mandanten-Ordner.
- HTML-Dateien markieren dynamische Stellen mit 'data-slot="<key>"'.
- Bei Änderungen wird nur company.json editiert (oder per CLI-Flag --set),
  der Compiler aktualisiert alle HTML-Dateien in < 1 Sekunde und committet optional direkt.

Verwendung:
  python3 sync_company_slots.py --site webpilot
  python3 sync_company_slots.py --site webpilot --set email="neu@magnet-xs.ch" --git-push
  python3 sync_company_slots.py --site webpilot --set street="Vordere Hauptgasse 104" --set city="Zofingen" --git-push
  python3 sync_company_slots.py --all
  python3 sync_company_slots.py --site webpilot --show
"""

import os
import sys
import re
import json
import time
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

# Basis-Verzeichnis ermitteln
BASE_DIR = Path(__file__).resolve().parent.parent


def compute_derived_fields(data: dict) -> dict:
    """Berechnet abgeleitete Standard-Slots, falls sie nicht explizit gesetzt sind."""
    d = dict(data)
    now_year = datetime.now().year

    # Bereinigte Telefon- & WhatsApp-Nummern für Links
    phone_raw = str(d.get("phone", ""))
    d["phone_clean"] = re.sub(r"[^\d+]", "", phone_raw)

    wa_raw = str(d.get("whatsapp", ""))
    d["whatsapp_clean"] = re.sub(r"[^\d]", "", wa_raw)

    # Standard Footer-Zeile: Straße • PLZ Ort • E-Mail
    street = d.get("street", "")
    zip_code = d.get("zip", "")
    city = d.get("city", "")
    email = d.get("email", "")
    legal_name = d.get("legal_name") or d.get("company_name", "")
    prod_name = d.get("product_name", "")

    # Auto-Footer-Zeile immer aus den Einzelteilen ableiten, ausser wenn 'footer_address_override' gesetzt ist
    if "footer_address_override" in d:
        d["footer_address"] = d["footer_address_override"]
    else:
        parts = []
        if street:
            parts.append(street)
        if zip_code or city:
            parts.append(f"{zip_code} {city}".strip())
        if email:
            parts.append(email)
        d["footer_address"] = " • ".join(parts)

    if "footer_brand" not in d and prod_name and legal_name:
        d["footer_brand"] = f"{prod_name} · Ein Produkt der {legal_name}"

    if "copyright" not in d and legal_name:
        d["copyright"] = f"© {now_year} {legal_name}, {city}."

    if "hosting_badge" not in d:
        d["hosting_badge"] = f"Gehostet in der Schweiz (ZRH / GVA) • Sub-50ms Server-Reaktionszeit • Version {now_year}"

    return d


def update_html_slots(html: str, data: dict) -> tuple[str, int, list]:
    """
    Ersetzt alle HTML-Tags mit data-slot="key" durch den entsprechenden Wert aus data.
    Aktualisiert bei <a> Tags auch automatisch href (mailto, tel, wa.me).
    """
    updated_slots = []

    def replacer(match):
        tag = match.group("tag")
        attrs = match.group("attrs")
        slot = match.group("slot")
        old_content = match.group("content")

        if slot not in data:
            return match.group(0)

        new_val = str(data[slot])
        new_attrs = attrs

        # Automatische href-Korrektur bei Links
        if tag.lower() == "a":
            if slot in ("email", "email_link"):
                if re.search(r'href=["\']mailto:[^"\']*["\']', new_attrs):
                    new_attrs = re.sub(r'href=["\']mailto:[^"\']*["\']', f'href="mailto:{new_val}"', new_attrs)
            elif slot in ("phone", "phone_link") and "phone_clean" in data:
                if re.search(r'href=["\']tel:[^"\']*["\']', new_attrs):
                    new_attrs = re.sub(r'href=["\']tel:[^"\']*["\']', f'href="tel:{data["phone_clean"]}"', new_attrs)
            elif slot in ("whatsapp", "whatsapp_link") and "whatsapp_clean" in data:
                if re.search(r'href=["\']https://wa\.me/[^"\']*["\']', new_attrs):
                    new_attrs = re.sub(r'href=["\']https://wa\.me/[^"\']*["\']', f'href="https://wa.me/{data["whatsapp_clean"]}"', new_attrs)

        # Prüfen ob Änderung stattgefunden hat (Leerräume normalisieren)
        if old_content.strip() != new_val.strip() or new_attrs != attrs:
            updated_slots.append(slot)
            return f"<{tag}{new_attrs}>{new_val}</{tag}>"

        return match.group(0)

    pattern = re.compile(
        r'<(?P<tag>[a-zA-Z0-9]+)(?P<attrs>[^>]*?\bdata-slot=["\'](?P<slot>[a-zA-Z0-9_-]+)["\'][^>]*)>(?P<content>.*?)</(?P=tag)>',
        re.DOTALL | re.IGNORECASE,
    )
    new_html = pattern.sub(replacer, html)
    return new_html, len(updated_slots), updated_slots


def sync_site(site_dir: Path, set_fields: dict = None, dry_run: bool = False) -> dict:
    """Synchronisiert eine einzelne WebPilot-Instanz."""
    config_file = site_dir / "company.json"
    if not config_file.exists():
        return {"success": False, "error": f"Keine company.json in {site_dir} gefunden."}

    try:
        with open(config_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return {"success": False, "error": f"Fehler beim Lesen von {config_file}: {e}"}

    # Falls --set übergeben wurde: Werte in company.json schreiben
    config_changed = False
    if set_fields:
        for k, v in set_fields.items():
            if data.get(k) != v:
                data[k] = v
                config_changed = True

        if config_changed and not dry_run:
            with open(config_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                f.write("\n")

    # Abgeleitete Werte berechnen
    enriched_data = compute_derived_fields(data)

    # Alle HTML-Dateien durchsuchen
    html_files = sorted(site_dir.glob("*.html"))
    total_files_changed = 0
    total_slots_changed = 0
    file_details = {}

    for hf in html_files:
        with open(hf, "r", encoding="utf-8") as f:
            content = f.read()

        new_content, count, slots = update_html_slots(content, enriched_data)
        if count > 0:
            total_files_changed += 1
            total_slots_changed += count
            file_details[hf.name] = slots
            if not dry_run:
                with open(hf, "w", encoding="utf-8") as f:
                    f.write(new_content)

    return {
        "success": True,
        "site": site_dir.name,
        "config_changed": config_changed,
        "files_changed": total_files_changed,
        "slots_changed": total_slots_changed,
        "details": file_details,
        "data": enriched_data,
    }


def main():
    parser = argparse.ArgumentParser(
        description="WebPilot Semantic Slot & Metadata Sync Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--site", help="Name des Site-Ordners (z.B. webpilot, preview-hiltbrand)")
    parser.add_argument("--all", action="store_true", help="Alle Seiten mit company.json synchronisieren")
    parser.add_argument("--show", action="store_true", help="Zeigt die aktuellen Stammdaten der Seite an")
    parser.add_argument("--set", action="append", help="Aktualisiert ein Feld in company.json (Format: key=value)")
    parser.add_argument("--dry-run", action="store_true", help="Zeigt Änderungen an, ohne Dateien zu schreiben")
    parser.add_argument("--git-push", action="store_true", help="Committet und pusht geänderte Dateien automatisch")

    args = parser.parse_args()
    start_time = time.time()

    if not args.site and not args.all:
        parser.print_help()
        sys.exit(1)

    # Key-Value Paare aus --set parsen
    set_fields = {}
    if args.set:
        for item in args.set:
            if "=" in item:
                k, v = item.split("=", 1)
                set_fields[k.strip()] = v.strip()
            else:
                print(f"Fehler: Ungültiges Format bei --set '{item}'. Erwartet: key=value")
                sys.exit(1)

    # Zielverzeichnisse bestimmen
    target_dirs = []
    if args.site:
        p = BASE_DIR / args.site
        if not p.is_dir():
            p = Path(args.site).resolve()
        if not p.is_dir():
            print(f"Fehler: Verzeichnis '{args.site}' nicht gefunden.")
            sys.exit(1)
        target_dirs.append(p)
    elif args.all:
        for item in BASE_DIR.iterdir():
            if item.is_dir() and (item / "company.json").exists():
                target_dirs.append(item)

    if not target_dirs:
        print("Keine Seiten mit company.json gefunden.")
        sys.exit(0)

    # Ausführen
    any_changes = False
    for tdir in target_dirs:
        if args.show:
            cfg = tdir / "company.json"
            if cfg.exists():
                with open(cfg, "r", encoding="utf-8") as f:
                    print(f"\n--- Stammdaten: {tdir.name} ({cfg}) ---")
                    print(json.dumps(json.load(f), indent=2, ensure_ascii=False))
            continue

        res = sync_site(tdir, set_fields=set_fields, dry_run=args.dry_run)
        if not res["success"]:
            print(f"Fehler bei {tdir.name}: {res['error']}")
            continue

        site_name = res["site"]
        print(f"Site: {site_name}")
        if res["config_changed"]:
            print("  -> company.json aktualisiert")
            any_changes = True

        if res["files_changed"] > 0:
            any_changes = True
            print(f"  -> {res['files_changed']} HTML-Dateien ({res['slots_changed']} Slots) aktualisiert:")
            for fname, slots in res["details"].items():
                print(f"     - {fname}: {', '.join(slots)}")
        else:
            print("  -> Alle HTML-Dateien sind 100% synchron mit company.json (0 Änderungen nötig).")

    # Optionaler Git Push
    if args.git_push and any_changes and not args.dry_run:
        print("\nFühre automatischen Git Push nach Cloudflare Pages Edge aus...")
        try:
            for tdir in target_dirs:
                subprocess.run(["git", "add", tdir.name], cwd=str(BASE_DIR), check=True)
            commit_msg = f"fix(metadata): sync company slots ({args.site or 'all sites'})"
            subprocess.run(["git", "commit", "-m", commit_msg], cwd=str(BASE_DIR), check=True)
            subprocess.run(["git", "push", "origin", "main"], cwd=str(BASE_DIR), check=True)
            print("Git Push erfolgreich abgeschlossen!")
        except Exception as e:
            print(f"Git Push Fehler / Warnung: {e}")

    elapsed = time.time() - start_time
    print(f"\nFertig in {elapsed:.3f} Sekunden.")


if __name__ == "__main__":
    main()

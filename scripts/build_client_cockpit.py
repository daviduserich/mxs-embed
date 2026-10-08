#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Client Cockpit Compiler (v3.4.1)
========================================
Generiert aus den Vorlagen templates/cockpit-app.html und templates/cockpit-script-template.js
ein vollständiges, voll funktionsfähiges WebPilot Studio Cockpit v{fw_version} für jeden Mandanten:
- Vollständige obere Studio-Leiste mit Magnet-XS Signet & Device Simulator (Desktop/Smartphone)
- Vollständiges Bilder-Pool Modal mit Drag & Drop Upload, dynamischer Sortierung und Löschfunktion
- Vollständiger 1-Klick Bildtausch Modus mit Spotlight & ESC-Abbruch
- Vollständige Einbettungscodes & CNAME-Anleitungen
- 100% autark und Cloudflare Edge-kompatibel
- Dynamisches Branchen- & Fachbegriffs-Profil (swiss_industry_catalog.json)
"""

import os
import sys
import re
import json
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

BASE_DIR = Path(__file__).resolve().parent.parent  # mxs-embed
TEMPLATES_DIR = BASE_DIR / "templates"
SCRIPTS_DIR = BASE_DIR / "scripts"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

try:
    import industry_resolver
except ImportError:
    industry_resolver = None

def get_image_info(path):
    """Liest Bilddimensionen und Dateigrösse aus."""
    import struct
    size_bytes = os.path.getsize(path)
    size_kb = round(size_bytes / 1024, 1)
    w, h = 0, 0
    try:
        with open(path, "rb") as f:
            data = f.read(64)
            if data[:8] == b"\x89PNG\r\n\x1a\n":
                w, h = struct.unpack(">II", data[16:24])
            elif data[:2] == b"\xff\xd8":
                f.seek(0)
                full = f.read()
                for i in range(len(full) - 9):
                    if full[i] == 0xFF and full[i+1] in (0xC0, 0xC2):
                        h, w = struct.unpack(">HH", full[i+5:i+9])
                        break
            elif data[:4] == b"RIFF" and data[8:12] == b"WEBP":
                f.seek(12)
                chunk = f.read(18)
                if chunk[:4] == b"VP8X":
                    w = int.from_bytes(chunk[12:15], "little") + 1
                    h = int.from_bytes(chunk[15:18], "little") + 1
    except Exception:
        pass
    dim = f"{w}x{h}" if (w and h) else "Unbekannt"
    return size_kb, dim

def get_client_profile(slug: str, client_dir: Path, name: str) -> dict:
    """Ermittelt das dynamische Branchen- und Mandantenprofil inkl. Fachtermini."""
    clean_slug = slug.replace("preview-", "")
    cfg_data = {}
    for cfg_candidate in [
        client_dir / "company.json",
        client_dir / "config.json",
        client_dir / "01-Company-Specs" / "company.json"
    ]:
        if cfg_candidate.exists():
            try:
                cfg_data = json.loads(cfg_candidate.read_text(encoding="utf-8"))
                break
            except Exception:
                pass

    industry_query = cfg_data.get("industry") or cfg_data.get("branche") or name
    if "hiltbrand" in clean_slug.lower():
        industry_query = "Bedachung"
    elif "birchmeier" in clean_slug.lower():
        industry_query = "Sanitär"

    industry_info = None
    if industry_resolver:
        try:
            industry_info = industry_resolver.resolve_industry(industry_query)
        except Exception:
            pass

    if industry_info:
        ind_id = industry_info.get("id", "generic")
        ind_name = industry_info.get("name", "Schweizer Unternehmen")
        fachvok = industry_info.get("fachvokabular", {})
        use_terms = fachvok.get("verwende", [])[:8]
        avoid_terms = fachvok.get("vermeide", [])[:8]
        efz_jobs = industry_info.get("berufsbezeichnungen_efz", [])[:4]
        verband = industry_info.get("verband_normen", {}).get("verband", "")

        if ind_id in ["bedachung_gebaeudehuelle", "schreinerei_innenausbau", "photovoltaik_solartechnik", "elektro_gebaeudetechnik", "sanitaer_heizung_haustechnik"]:
            work_label = "Baustelle & Projekte"
            industry_label = f"Schweizer {ind_name}-Meisterbetrieb"
        elif ind_id in ["treuhand_finanzen_kmu", "b2b_fuehrung_beratung"]:
            work_label = "Mandate & Einblicke"
            industry_label = f"Schweizer {ind_name}-Kanzlei"
        elif ind_id in ["architektur_bauingenieur"]:
            work_label = "Projekte & Bauwerke"
            industry_label = f"Schweizer {ind_name}-Büro"
        else:
            work_label = "Praxis & Projekte"
            industry_label = f"Schweizer {ind_name}"

        if cfg_data.get("work_category_label"):
            work_label = cfg_data.get("work_category_label")
        elif "hiltbrand" in clean_slug.lower():
            work_label = "Baustelle & Benefit"

        rules = []
        if verband:
            rules.append(f"- Branchen-Standard: {verband}.")
        if use_terms:
            rules.append(f"- Schweizer Fachvokabular (aktiv nutzen): {', '.join(use_terms)}.")
        if avoid_terms:
            rules.append(f"- Verbotenes Fremdvokabular (nie verwenden!): {', '.join(avoid_terms)}.")
        if efz_jobs:
            rules.append(f"- Offizielle Berufsbezeichnungen: {', '.join(efz_jobs)}.")
        rules.append("- Grunddoktrin: 'Leistungen' (nie 'Gewerke'), 'Offerte' (nie 'Kostenvoranschlag'), 'Ferien' (nie 'Urlaub'), 'Lernende' (nie 'Azubis').")
    else:
        ind_id = "universal_swiss_kmu"
        ind_name = "Schweizer KMU"
        industry_label = "Schweizer Unternehmens-Website"
        work_label = cfg_data.get("work_category_label") or ("Baustelle & Benefit" if "hiltbrand" in clean_slug.lower() else "Projekte & Einblicke")
        rules = [
            "- Sprache: Authentisches Schweizer Hochdeutsch (100% Verbot von 'ß', nutze 'ss').",
            "- Schweizer Geschäftsbegriffe: 'Leistungen' (nie 'Gewerke'), 'Fachspezialisten EFZ' (nie 'Gesellen'), 'Lernende' (nie 'Azubis'), 'Offerte' (nie 'Kostenvoranschlag'), 'Ferien' (nie 'Urlaub')."
        ]

    short_name = cfg_data.get("short_name") or (name.split()[0] if name else "Unternehmen")
    host_url = cfg_data.get("host_url") or f"https://embed.magnet-xs.ch/{slug}/cockpit"
    host_jobs_url = cfg_data.get("host_jobs_url") or f"https://embed.magnet-xs.ch/{slug}/"
    if clean_slug == "hiltbrand":
        host_jobs_url = "https://dachdecker-berneroberland.ch/jobs/"

    brand_title = cfg_data.get("studio_title") or ("KARRIERE-STUDIO" if clean_slug == "hiltbrand" else "WEBPILOT STUDIO")

    return {
        "slug": slug,
        "clean_slug": clean_slug,
        "name": name,
        "short_name": short_name,
        "industry_id": ind_id,
        "industry_name": ind_name,
        "industry_label": industry_label,
        "work_category_label": work_label,
        "brand_title": brand_title,
        "prompt_rules": rules,
        "host_url": host_url,
        "host_jobs_url": host_jobs_url
    }

def scan_images(client_dir: Path, slug: str, default_category: str = "Baustelle & Benefit"):
    """Scannt images/ Ordner und erzeugt bilder.json."""
    images_dir = client_dir / "images"
    bilder = []
    if not images_dir.exists():
        return bilder

    html_files = list(client_dir.glob("*.html"))
    html_contents = {f.name: f.read_text(encoding="utf-8", errors="ignore") for f in html_files if f.name != "cockpit.html"}

    for p in sorted(images_dir.glob("*")):
        if p.name.startswith(".") or p.is_dir():
            continue
        ext = p.suffix.lower()
        if ext not in [".jpg", ".jpeg", ".png", ".webp", ".svg", ".gif"]:
            continue
        
        size_kb, dim = get_image_info(p)
        mtime = int(p.stat().st_mtime)
        mtime_str = datetime.fromtimestamp(mtime).strftime("%d.%m.%Y %H:%M")
        
        rel_path = f"images/{p.name}"
        cdn_url = f"https://embed.magnet-xs.ch/{slug}/{rel_path}"
        
        category = default_category
        if "hero" in p.name.lower():
            category = "Hero & Header"
        elif "logo" in p.name.lower():
            category = "Logo & Icon"
        elif any(k in p.name.lower() for k in ["team", "michael", "stefan", "beat", "alain"]):
            category = "Team & Porträt"

        used_in = []
        for doc_name, content in html_contents.items():
            if rel_path in content or p.name in content:
                is_hero = ("hero" in p.name.lower() or "hero" in doc_name.lower())
                used_in.append({"datei": doc_name, "slot": "image", "is_hero": is_hero})
                
        img_id = re.sub(r'[^a-zA-Z0-9_]', '_', f"images_{p.name}")
        bilder.append({
            "id": img_id,
            "filename": p.name,
            "rel_path": rel_path,
            "folder": slug,
            "category": category,
            "dimensions": dim,
            "size_kb": size_kb,
            "mtime": mtime,
            "mtime_str": mtime_str,
            "cdn_url": cdn_url,
            "is_used": len(used_in) > 0,
            "used_in": used_in
        })

    with open(client_dir / "bilder.json", "w", encoding="utf-8") as f:
        json.dump(bilder, f, indent=2, ensure_ascii=False)
    return bilder

def scan_stellen(client_dir: Path, slug: str, name: str):
    """Scannt HTML-Dateien und erzeugt stellen.json."""
    html_files = [f for f in sorted(client_dir.glob("*.html")) if f.name != "cockpit.html"]
    stellen = []
    
    for f in html_files:
        content = f.read_text(encoding="utf-8", errors="ignore")
        title_m = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        title = title_m.group(1).split("·")[0].split("|")[0].strip() if title_m else f.stem
        
        edge_url = f"https://embed.magnet-xs.ch/{slug}/{f.name}"
        widget_code = (
            f'<iframe src="{edge_url}?embed=true" '
            f'style="width:100%; border:none; min-height:850px;" scrolling="no" id="acp-job-widget"></iframe>\n'
            f'<script>window.addEventListener("message",function(e){{'
            f'if(e.data&&e.data.type==="acp-embed-resize"){{'
            f'var el=document.getElementById("acp-job-widget");'
            f'if(el)el.style.height=e.data.height+"px";'
            f'}}'
            f'}});</script>'
        )
        
        stellen.append({
            "id": f.stem.lower(),
            "titel": title,
            "firma": name,
            "icon": "🏗️",
            "datei": f.name,
            "folder": slug,
            "edge_url": edge_url,
            "host_webseite": f"https://{slug}.ch",
            "host_label": f"{slug}.ch",
            "farb_akzent": "#d97706",
            "widget_code": widget_code,
            "is_live": True,
            "live_url": edge_url,
            "status": "Live auf Edge CDN",
            "status_badge": "🟢 LIVE"
        })

    with open(client_dir / "stellen.json", "w", encoding="utf-8") as f:
        json.dump(stellen, f, indent=2, ensure_ascii=False)
    return stellen

def get_framework_version() -> str:
    v_file = BASE_DIR / "VERSION"
    if v_file.exists():
        return v_file.read_text(encoding="utf-8").strip()
    return "3.4.1"

def build_cockpit(slug: str):
    """Kompiliert das vollwertige WebPilot Cockpit für den Mandanten."""
    client_dir = BASE_DIR / slug
    if not client_dir.exists():
        print(f"❌ Mandant {slug} nicht gefunden in {client_dir}")
        return False

    config_file = client_dir / "config.json"
    name = slug.replace("-", " ").title()
    if config_file.exists():
        try:
            cfg = json.loads(config_file.read_text(encoding="utf-8"))
            name = cfg.get("name", name)
        except Exception:
            pass

    clean_slug = slug.replace("preview-", "")
    profile = get_client_profile(slug, client_dir, name)
    name = profile["name"]
    short_name = profile["short_name"]
    host_url = profile["host_url"]
    host_jobs_url = profile["host_jobs_url"]
    clean_host_url = host_url.replace("https://", "").replace("http://", "")
    clean_jobs_domain = host_jobs_url.replace("https://", "").replace("http://", "")
    brand_title = profile["brand_title"]
    work_category_label = profile["work_category_label"]

    # 1. Bilder & Stellen scannen
    bilder = scan_images(client_dir, slug, default_category=work_category_label)
    stellen = scan_stellen(client_dir, slug, name)

    # 2. Viewport- und Dateivorgaben ermitteln
    default_viewport_file = "index.html"
    default_viewport_src = "index.html?embed=true"
    initial_job_title = "Aktive Stelle"

    if clean_slug == "hiltbrand" and (client_dir / "Hiltbrand_Dachdecker_Pragmatisch.html").exists():
        default_viewport_file = "Hiltbrand_Dachdecker_Pragmatisch.html"
        default_viewport_src = "Hiltbrand_Dachdecker_Pragmatisch.html?embed=true"
        initial_job_title = "Dachdecker EFZ (80–100%)"
    elif stellen:
        default_viewport_file = stellen[0].get("datei", "index.html")
        default_viewport_src = f"{default_viewport_file}?embed=true"
        initial_job_title = stellen[0].get("titel", "Aktive Stelle")

    sync_folder_name = "Hiltbrand-Karriere" if "hiltbrand" in clean_slug else f"{clean_slug}-web"

    # 3. Template einlesen
    cockpit_app_file = TEMPLATES_DIR / "cockpit-app.html"
    js_template_file = TEMPLATES_DIR / "cockpit-script-template.js"
    
    content = cockpit_app_file.read_text(encoding="utf-8")
    js_template_code = js_template_file.read_text(encoding="utf-8")

    # 4. Branding & Pfade anpassen
    fw_version = get_framework_version()
    now_build = datetime.now(ZoneInfo("Europe/Zurich")).strftime("%Y-%m-%d %H:%M")

    # Platzhalter ersetzen
    replacements = {
        "__CLIENT_NAME__": name,
        "__CLIENT_SHORT_NAME__": short_name,
        "__CLIENT_SLUG__": slug,
        "__CLIENT_STUDIO_TITLE__": brand_title,
        "__FRAMEWORK_VERSION__": fw_version,
        "__HOST_URL__": host_url,
        "__HOST_URL_CLEAN__": clean_host_url,
        "__HOST_JOBS_URL__": host_jobs_url,
        "__HOST_JOBS_DOMAIN__": clean_jobs_domain,
        "__WORK_CATEGORY_LABEL__": work_category_label,
        "__DEFAULT_VIEWPORT_SRC__": default_viewport_src,
        "__DEFAULT_VIEWPORT_FILE__": default_viewport_file,
        "__INITIAL_JOB_TITLE__": initial_job_title,
        "__SYNC_FOLDER_NAME__": sync_folder_name
    }
    for placeholder, val in replacements.items():
        content = content.replace(placeholder, str(val))

    # Regex-Absicherungen für Alt-Templates / Fallbacks
    content = re.sub(r'<title>.*?</title>', f'<title>{name} · WebPilot Studio · v{fw_version}</title>', content, flags=re.IGNORECASE)
    content = re.sub(r'<span class="acp-version-badge"[^>]*>.*?</span>', f'<span class="acp-version-badge" id="acp-version-badge" title="WebPilot Framework v{fw_version}">v{fw_version}</span>', content)
    content = content.replace('<span class="acp-brand-text" id="acp-brand-label">KARRIERE-STUDIO</span>', f'<span class="acp-brand-text" id="acp-brand-label">{brand_title}</span>')
    content = content.replace('Hiltbrand & Zurbuchen Karriere-Studio', f'{name} WebPilot Studio')
    content = content.replace('id="picker-current-firm">Hiltbrand<', f'id="picker-current-firm">{name}<')
    content = content.replace('id="acp-stage-client-pill">Hiltbrand Gebäudehüllen AG<', f'id="acp-stage-client-pill">{name}<')
    content = content.replace('https://embed.magnet-xs.ch/hiltbrand/cockpit', f'https://embed.magnet-xs.ch/{slug}/cockpit')
    content = content.replace('https://dachdecker-berneroberland.ch/jobs/', host_jobs_url if clean_slug == 'hiltbrand' else f'https://embed.magnet-xs.ch/{slug}/')
    content = content.replace('Hiltbrand-Karriere\\images\\', f'{sync_folder_name}\\images\\')

    # 5. JS Template füllen
    for s in stellen:
        if "widget_code" in s:
            s["widget_code"] = s["widget_code"].replace("</script>", "<\\/script>")

    stellen_json_str = json.dumps(stellen, ensure_ascii=False)
    bilder_json_str = json.dumps(bilder, ensure_ascii=False)
    profile_json_str = json.dumps(profile, indent=2, ensure_ascii=False)

    compiled_js = re.sub(r'var ACP_COCKPIT_VERSION = ".*?";', f'var ACP_COCKPIT_VERSION = "v{fw_version}";', js_template_code)
    compiled_js = re.sub(r'var ACP_COCKPIT_BUILD = ".*?";', f'var ACP_COCKPIT_BUILD = "{now_build}";', compiled_js)
    compiled_js = compiled_js.replace('Magnet-XS Karriere-Cockpit', f'{name} WebPilot Studio')
    compiled_js = compiled_js.replace("/* __BILDER_JSON__ */", bilder_json_str)
    compiled_js = compiled_js.replace("/* __STELLEN_JSON__ */", stellen_json_str)
    compiled_js = compiled_js.replace("/* __CLIENT_PROFILE_JSON__ */", profile_json_str)
    
    # Pfad-Ersetzungen im JS
    compiled_js = compiled_js.replace("https://embed.magnet-xs.ch/hiltbrand/", f"https://embed.magnet-xs.ch/{slug}/")
    compiled_js = compiled_js.replace("'hiltbrand'", f"'{slug}'")
    compiled_js = compiled_js.replace('"hiltbrand"', f'"{slug}"')

    # Script-Tag ersetzen
    new_script_tag = f'<script id="acp-studio-main-engine">\n{compiled_js}\n</script>'
    if '<script id="acp-studio-main-engine">' in content:
        content = re.sub(r'<script id="acp-studio-main-engine">.*?</script>', lambda m: new_script_tag, content, flags=re.DOTALL)
    else:
        last_idx = content.rfind("<script")
        if last_idx != -1:
            end_idx = content.find("</script>", last_idx) + len("</script>")
            content = content[:last_idx] + new_script_tag + content[end_idx:]

    target_cockpit = client_dir / "cockpit.html"
    target_cockpit.write_text(content, encoding="utf-8")
    print(f"✨ Vollwertiges WebPilot Studio Cockpit v{fw_version} für {name} ({slug}) generiert: {len(content)} Bytes")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build Client Cockpit v3.4.1")
    parser.add_argument("--slug", required=True, help="Mandanten-Slug (z. B. muster-holzbau)")
    args = parser.parse_args()
    build_cockpit(args.slug)

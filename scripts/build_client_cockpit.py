#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Client Cockpit Compiler (v3.3.0)
========================================
Generiert aus den Vorlagen templates/cockpit-app.html und templates/cockpit-script-template.js
ein vollständiges, voll funktionsfähiges WebPilot Studio Cockpit v{fw_version} für jeden Mandanten:
- Vollständige obere Studio-Leiste mit Magnet-XS Signet & Device Simulator (Desktop/Smartphone)
- Vollständiges Bilder-Pool Modal mit Drag & Drop Upload, dynamischer Sortierung und Löschfunktion
- Vollständiger 1-Klick Bildtausch Modus mit Spotlight & ESC-Abbruch
- Vollständige Einbettungscodes & CNAME-Anleitungen
- 100% autark und Cloudflare Edge-kompatibel
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

def scan_images(client_dir: Path, slug: str):
    """Scannt images/ Ordner und erzeugt bilder.json."""
    images_dir = client_dir / "images"
    bilder = []
    if not images_dir.exists():
        return bilder

    # Prüfe wo Bilder verwendet werden
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
        
        category = "Baustelle & Benefit"
        if "hero" in p.name.lower():
            category = "Hero & Header"
        elif "logo" in p.name.lower():
            category = "Logo & Icon"
        elif any(k in p.name.lower() for k in ["team", "michael", "stefan", "beat", "alain"]):
            category = "Team & Porträt"

        # Check used
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
    return "3.4.0"

def build_cockpit(slug: str):
    """Kompiliert das vollwertige WebPilot Cockpit v3.3.0 für den Mandanten."""
    client_dir = BASE_DIR / slug
    if not client_dir.exists():
        print(f"❌ Mandant {slug} nicht gefunden in {client_dir}")
        return False

    config_file = client_dir / "config.json"
    name = slug.replace("-", " ").title()
    if config_file.exists():
        cfg = json.loads(config_file.read_text(encoding="utf-8"))
        name = cfg.get("name", name)

    # 1. Bilder & Stellen scannen
    bilder = scan_images(client_dir, slug)
    stellen = scan_stellen(client_dir, slug, name)

    # 2. Template einlesen
    cockpit_app_file = TEMPLATES_DIR / "cockpit-app.html"
    js_template_file = TEMPLATES_DIR / "cockpit-script-template.js"
    
    content = cockpit_app_file.read_text(encoding="utf-8")
    js_template_code = js_template_file.read_text(encoding="utf-8")

    # 3. Branding & Pfade anpassen
    fw_version = get_framework_version()
    now_build = datetime.now(ZoneInfo("Europe/Zurich")).strftime("%Y-%m-%d %H:%M")

    content = re.sub(r'<title>.*?</title>', f'<title>{name} · WebPilot Studio · v{fw_version}</title>', content, flags=re.IGNORECASE)
    content = re.sub(r'<span class="acp-version-badge"[^>]*>.*?</span>', f'<span class="acp-version-badge" id="acp-version-badge" title="WebPilot Framework v{fw_version}">v{fw_version}</span>', content)
    brand_title = "WEBPILOT STUDIO" if slug != "hiltbrand" else "KARRIERE-STUDIO"
    content = content.replace('<span class="acp-brand-text" id="acp-brand-label">KARRIERE-STUDIO</span>', f'<span class="acp-brand-text" id="acp-brand-label">{brand_title}</span>')
    content = content.replace('Hiltbrand & Zurbuchen Karriere-Studio', f'{name} WebPilot Studio')
    content = content.replace('id="picker-current-firm">Hiltbrand<', f'id="picker-current-firm">{name}<')
    content = content.replace('id="acp-stage-client-pill">Hiltbrand Gebäudehüllen AG<', f'id="acp-stage-client-pill">{name}<')
    content = content.replace('https://embed.magnet-xs.ch/hiltbrand/cockpit', f'https://embed.magnet-xs.ch/{slug}/cockpit')
    content = content.replace('https://dachdecker-berneroberland.ch/jobs/', f'https://embed.magnet-xs.ch/{slug}/')
    content = content.replace('Hiltbrand-Karriere\\images\\', f'{slug}\\images\\')
    content = content.replace('Hiltbrand_Dachdecker_Pragmatisch.html?embed=true', 'index.html?embed=true')
    content = content.replace('src="Hiltbrand_Dachdecker_Pragmatisch.html?embed=true"', 'src="index.html?embed=true"')

    # 4. JS Template füllen
    for s in stellen:
        if "widget_code" in s:
            s["widget_code"] = s["widget_code"].replace("</script>", "<\\/script>")

    stellen_json_str = json.dumps(stellen, ensure_ascii=False)
    bilder_json_str = json.dumps(bilder, ensure_ascii=False)

    compiled_js = re.sub(r'var ACP_COCKPIT_VERSION = ".*?";', f'var ACP_COCKPIT_VERSION = "v{fw_version}";', js_template_code)
    compiled_js = re.sub(r'var ACP_COCKPIT_BUILD = ".*?";', f'var ACP_COCKPIT_BUILD = "{now_build}";', compiled_js)
    compiled_js = compiled_js.replace('Magnet-XS Karriere-Cockpit', f'{name} WebPilot Studio')
    compiled_js = compiled_js.replace("/* __BILDER_JSON__ */", bilder_json_str)
    compiled_js = compiled_js.replace("/* __STELLEN_JSON__ */", stellen_json_str)
    
    # Pfad-Ersetzungen im JS
    compiled_js = compiled_js.replace("https://embed.magnet-xs.ch/hiltbrand/", f"https://embed.magnet-xs.ch/{slug}/")
    compiled_js = compiled_js.replace("'hiltbrand'", f"'{slug}'")
    compiled_js = compiled_js.replace('"hiltbrand"', f'"{slug}"')

    # Script-Tag ersetzen
    new_script_tag = f"<script>\n{compiled_js}\n</script>"
    content = re.sub(r"<script>.*?</script>", lambda m: new_script_tag, content, flags=re.DOTALL)

    target_cockpit = client_dir / "cockpit.html"
    target_cockpit.write_text(content, encoding="utf-8")
    print(f"✨ Vollwertiges WebPilot Studio Cockpit v{fw_version} für {name} ({slug}) generiert: {len(content)} Bytes")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build Client Cockpit v3.3.0")
    parser.add_argument("--slug", required=True, help="Mandanten-Slug (z. B. muster-holzbau)")
    args = parser.parse_args()
    build_cockpit(args.slug)

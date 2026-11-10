#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Bilder- & Cloudflare-Asset-Katalog (webpilot_asset_catalog.py)
=======================================================================
Zentrales Katalog-, Kategorisierungs- und Namens-Standard-Modul für alle
WebPilot-Webseiten (/home/brainuser/workspaces/mxs-embed/).

Funktionen:
1. Verbindlicher Schweizer kebab-case Benennungs-Standard (normalize_upload_filename):
   - logo-<beschreibung>.<ext>     (Logo & Marken-Icon)
   - hero-<beschreibung>.<ext>     (Startbühne & Header)
   - team-<vorname-nachname>.<ext> (Team, Porträt & Kader)
   - sponsor-<firmenname>.<ext>    (Sponsor & Partner)
   - ref-<projekt-thema>.<ext>     (Referenz, Projekt & Angebot)
   - icon-<beschreibung>.<ext>     (Favicon & App-Icon)
   - video-<beschreibung>.<ext>    (Video & Bewegtbild)
2. Pro Webseite (alle 20 Ordner):
   - Aktualisiert bilder.json (inkl. Kategorie, Auflösung, KB, Format, Seiten-Einsatz,
     SEO/GEO-Alt-Text und kanonischer Cloudflare-URL).
   - Generiert BILDER_VERZEICHNIS.md mit Direkt-Links auf Cloudflare Edge.
3. Zentraler Master-Katalog über alle 20 Webseiten:
   - /home/brainuser/workspaces/mxs-embed/MASTER_ASSET_KATALOG.md
   - /home/brainuser/workspaces/mxs-embed/config/master_asset_inventory.json
   - /home/brainuser/vault-plain/10-Projects/WebPilot-Pro0416/03-Fulfillment/WEBPILOT-BILDER-UND-ASSET-KATALOG.md
"""

import os
import re
import sys
import json
import time
import struct
import shutil
import argparse
import unicodedata
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    from PIL import Image
except ImportError:
    Image = None

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
VAULT_CATALOG_PATH = Path(
    "/home/brainuser/vault-plain/10-Projects/WebPilot-Pro0416/03-Fulfillment/WEBPILOT-BILDER-UND-ASSET-KATALOG.md"
)
VAULT_SCRIPT_MIRROR_PATH = Path(
    "/home/brainuser/vault-plain/10-Projects/WebPilot-Pro0416/03-Fulfillment/webpilot_asset_catalog.py"
)
MASTER_CATALOG_MD = BASE_DIR / "MASTER_ASSET_KATALOG.md"
MASTER_INVENTORY_JSON = BASE_DIR / "config" / "master_asset_inventory.json"

ALLOWED_ASSET_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".svg", ".gif", ".mp4", ".webm", ".mov"}

CATEGORY_DEFINITIONS = {
    "logo": ("Logo & Marken-Icon", "logo-<beschreibung>.<ext>"),
    "hero": ("Startbühne & Header", "hero-<beschreibung>.<ext>"),
    "team": ("Team, Porträt & Kader", "team-<vorname-nachname>.<ext>"),
    "sponsor": ("Sponsor & Partner", "sponsor-<firmenname>.<ext>"),
    "ref": ("Referenz, Projekt & Angebot", "ref-<projekt-thema>.<ext>"),
    "icon": ("Favicon & App-Icon", "icon-<beschreibung>.<ext>"),
    "video": ("Video & Bewegtbild", "video-<beschreibung>.<ext>"),
}

# Kanonisches Cloudflare-Routing gemäss functions/_middleware.js
PUBLIC_CLOUDFLARE_SLUG_MAP = {
    "preview-mondocani": ("vorschau.magnet-xs.ch", "mondocani-vollversion"),
    "preview-mondocani-v2": ("vorschau.magnet-xs.ch", "mondocani-v2"),
    "preview-holz-susi": ("vorschau.magnet-xs.ch", "holz-susi-vollversion"),
    "preview-holz-susi-v2": ("vorschau.magnet-xs.ch", "holz-susi-v2"),
    "preview-joma": ("vorschau.magnet-xs.ch", "joma-vollversion"),
    "preview-joma-v2": ("vorschau.magnet-xs.ch", "joma-v2"),
    "preview-imp-marketing": ("vorschau.magnet-xs.ch", "imp-marketing-vollversion"),
    "preview-imp-marketing-v2": ("vorschau.magnet-xs.ch", "imp-marketing-v2"),
    "preview-herzensarbeit": ("vorschau.magnet-xs.ch", "herzensarbeit-vollversion"),
    "preview-herzensarbeit-v2": ("vorschau.magnet-xs.ch", "herzensarbeit-v2"),
    "preview-innere-staerke": ("vorschau.magnet-xs.ch", "innere-staerke-vollversion"),
    "preview-innere-staerke-v2": ("vorschau.magnet-xs.ch", "innere-staerke-v2"),
    "preview-frees": ("vorschau.magnet-xs.ch", "frees-vollversion"),
    "preview-frees-v2": ("vorschau.magnet-xs.ch", "frees-v2"),
    "preview-fcschlieren": ("vorschau.magnet-xs.ch", "fcschlieren-vollversion"),
    "preview-fcschlieren-v2": ("vorschau.magnet-xs.ch", "fcschlieren-v2"),
    "preview-scfulenbach": ("vorschau.magnet-xs.ch", "scfulenbach"),
    "preview-fcattiswil": ("vorschau.magnet-xs.ch", "fcattiswil"),
    "preview-her11": ("vorschau.magnet-xs.ch", "her11"),
    "preview-hochuli": ("vorschau.magnet-xs.ch", "hochuli"),
    "preview-hiltbrand": ("vorschau.magnet-xs.ch", "hiltbrand"),
    "preview-birchmeier": ("vorschau.magnet-xs.ch", "birchmeier"),
    "hiltbrand": ("embed.magnet-xs.ch", "hiltbrand"),
    "webpilot": ("vorschau.magnet-xs.ch", "webpilot"),
}

CURATED_COMPANY_NAMES = {
    "hiltbrand": ("Hiltbrand Gebäudehüllen AG (Karriere-Cockpit)", "Krattigen BE"),
    "preview-birchmeier": ("Birchmeier-Hohler GmbH", "Bremgarten AG"),
    "preview-fcattiswil": ("FC Attiswil", "Attiswil BE"),
    "preview-fcschlieren": ("FC Schlieren (Vollversion)", "Schlieren ZH"),
    "preview-fcschlieren-v2": ("FC Schlieren (Zeigeversion v2)", "Schlieren ZH"),
    "preview-frees": ("Free's · Studio für Textildesign & Stickerei (Vollversion)", "Niederrohrdorf AG"),
    "preview-frees-v2": ("Free's · Studio für Textildesign & Stickerei (Zeigeversion v2)", "Niederrohrdorf AG"),
    "preview-her11": ("HER11 · Frauenfussball-Förderung", "Zürich ZH"),
    "preview-herzensarbeit": ("Herzensarbeit · Anne-Katrin Koch (Vollversion)", "Härkingen SO"),
    "preview-herzensarbeit-v2": ("Herzensarbeit · Anne-Katrin Koch (Zeigeversion v2)", "Härkingen SO"),
    "preview-hiltbrand": ("Hiltbrand Gebäudehüllen AG (WebPilot)", "Krattigen BE"),
    "preview-hochuli": ("Hochuli Schlossrued AG", "Schlossrued AG"),
    "preview-mondocani": ("MONDOCANI · Die mobile Hundeschule (Vollversion)", "Flumenthal / Solothurn SO"),
    "preview-mondocani-v2": ("MONDOCANI · Die mobile Hundeschule (Zeigeversion v2)", "Flumenthal / Solothurn SO"),
    "preview-holz-susi": ("Holz-Susi GmbH · Susanne Schmid (Vollversion)", "Frick AG"),
    "preview-holz-susi-v2": ("Holz-Susi GmbH · Susanne Schmid (Zeigeversion v2)", "Frick AG"),
    "preview-imp-marketing": ("IMP GmbH · Matthias Iseli (Vollversion)", "Obersteckholz BE"),
    "preview-imp-marketing-v2": ("IMP GmbH · Matthias Iseli (Zeigeversion v2)", "Obersteckholz BE"),
    "preview-innere-staerke": ("Wüest + Paneduro · Innere Stärke (Vollversion)", "Sursee LU"),
    "preview-innere-staerke-v2": ("Wüest + Paneduro · Innere Stärke (Zeigeversion v2)", "Sursee LU"),
    "preview-joma": ("JOMA Solar GmbH (Vollversion)", "Wettingen AG"),
    "preview-joma-v2": ("JOMA Solar GmbH (Zeigeversion v2)", "Wettingen AG"),
    "preview-scfulenbach": ("SC Fulenbach", "Fulenbach SO"),
    "webpilot": ("WebPilot Plattform · magnet-Xs gmbh", "Zofingen AG"),
}

FALLBACK_JOB_META = {
    "hiltbrand": ("David Hügli (Magnet XS · Referenz)", "29.09.2026 · 15:31 Uhr"),
    "preview-hiltbrand": ("David Hügli (Magnet XS · Referenz)", "04.10.2026 · 11:02 Uhr"),
    "preview-birchmeier": ("David Hügli (Magnet XS · Referenz)", "04.10.2026 · 11:02 Uhr"),
    "preview-hochuli": ("David Hügli (Magnet XS · Referenz)", "29.10.2026 · 13:08 Uhr"),
    "webpilot": ("David Hügli (Magnet XS · Produktseite)", "02.10.2026 · 20:14 Uhr"),
    "preview-her11": ("Jenny Ettle (JE-MI)", "30.10.2026 · 16:00 Uhr"),
    "preview-fcschlieren": ("Jenny Ettle (JE-MI)", "02.11.2026 · 17:00 Uhr"),
    "preview-fcschlieren-v2": ("Jenny Ettle (JE-MI)", "02.11.2026 · 17:00 Uhr"),
    "preview-scfulenbach": ("Jenny Ettle (JE-MI)", "02.11.2026 · 17:20 Uhr"),
    "preview-fcattiswil": ("Jenny Ettle (JE-MI)", "02.11.2026 · 17:40 Uhr"),
    "preview-innere-staerke": ("Jenny Ettle (JE-MI)", "03.11.2026 · 18:30 Uhr"),
    "preview-innere-staerke-v2": ("Jenny Ettle (JE-MI)", "03.11.2026 · 18:30 Uhr"),
    "preview-frees": ("Jenny Ettle (JE-MI)", "03.11.2026 · 21:30 Uhr"),
    "preview-frees-v2": ("Jenny Ettle (JE-MI)", "03.11.2026 · 21:30 Uhr"),
    "preview-herzensarbeit": ("Jenny Ettle (JE-MI)", "05.11.2026 · 11:00 Uhr"),
    "preview-herzensarbeit-v2": ("Jenny Ettle (JE-MI)", "05.11.2026 · 11:00 Uhr"),
    "preview-imp-marketing": ("David Hügli (Magnet XS)", "05.11.2026 · 12:35 Uhr"),
    "preview-imp-marketing-v2": ("David Hügli (Magnet XS)", "05.11.2026 · 12:35 Uhr"),
    "preview-joma": ("Jenny Ettle (JE-MI)", "05.11.2026 · 20:54 Uhr"),
    "preview-joma-v2": ("Jenny Ettle (JE-MI)", "05.11.2026 · 20:54 Uhr"),
    "preview-mondocani": ("Jenny Ettle (JE-MI)", "10.11.2026 · 09:35 Uhr"),
    "preview-mondocani-v2": ("Jenny Ettle (JE-MI)", "10.11.2026 · 09:35 Uhr"),
    "preview-holz-susi": ("David Hügli (Magnet XS)", "09.11.2026 · 13:44 Uhr"),
    "preview-holz-susi-v2": ("David Hügli (Magnet XS)", "09.11.2026 · 13:44 Uhr"),
}


def _resolve_partner_and_submitted(folder: str) -> tuple[str, str]:
    base_slug = re.sub(r"-(?:vollversion|vv|v1|v2)$", "", folder.replace("preview-", ""))
    idx_file = BASE_DIR / "partner-jobs" / "index.json"
    if idx_file.exists():
        try:
            for j in json.loads(idx_file.read_text(encoding="utf-8")):
                jslug = str(j.get("slug") or "").strip().lower()
                if jslug == base_slug:
                    partner = str(j.get("created_by_name") or j.get("partner_name") or "").strip()
                    if base_slug == "imp-marketing" or str(j.get("created_by") or "").lower() == "david":
                        partner = "David Hügli (Magnet XS)"
                    elif not partner or "jenny" in partner.lower():
                        partner = "Jenny Ettle (JE-MI)"
                    raw_ts = str(j.get("created_at") or "").strip()
                    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})[T\s](\d{2}):(\d{2})", raw_ts)
                    if m:
                        yyyy, mm, dd, hh, mi = m.groups()
                        sub_str = f"{dd}.{mm}.{yyyy} · {hh}:{mi} Uhr"
                    else:
                        sub_str = raw_ts or FALLBACK_JOB_META.get(folder, ("Jenny Ettle (JE-MI)", "-"))[1]
                    return partner, sub_str
        except Exception:
            pass
    return FALLBACK_JOB_META.get(folder, ("Jenny Ettle (JE-MI)", "-"))


def _ss(text: str) -> str:
    """Erzwingt 100 % Schweizer Rechtschreibung (ss statt Eszett)."""
    if not text:
        return ""
    return str(text).replace("\u00df", "ss").replace("\u00df", "ss")


def normalize_upload_filename(raw_name: str, category_hint: str = "", slug: str = "") -> str:
    """
    Verbindlicher Schweizer kebab-case Benennungs-Standard für Bild-/Asset-Uploads:
    - Umlaute ä/ö/ü -> ae/oe/ue, Eszett -> ss
    - Kleinbuchstaben, Bindestriche statt Unterstriche/Leerzeichen
    - Optionales Kategorie-Präfix (logo-, hero-, team-, sponsor-, ref-, icon-, video-)
    """
    if not raw_name:
        raw_name = "bild.jpg"
    p = Path(str(raw_name).strip())
    ext = p.suffix.lower()
    if ext == ".jpeg":
        ext = ".jpg"
    if not ext:
        ext = ".jpg"

    stem = p.stem.lower()
    replacements = {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "\u00df": "ss",
        "\u00df": "ss",
        "é": "e",
        "è": "e",
        "ê": "e",
        "à": "a",
        "â": "a",
        "ç": "c",
    }
    for k, v in replacements.items():
        stem = stem.replace(k, v)

    stem = unicodedata.normalize("NFKD", stem).encode("ascii", "ignore").decode("ascii")
    stem = re.sub(r"[^a-z0-9]+", "-", stem).strip("-")
    stem = re.sub(r"-{2,}", "-", stem)
    if not stem:
        stem = "asset"

    cat = str(category_hint or "").strip().lower()
    cat_map = {
        "logo": "logo",
        "logo & icon": "logo",
        "logo & marken-icon": "logo",
        "hero": "hero",
        "hero & header": "hero",
        "startbühne & header": "hero",
        "team": "team",
        "team & porträt": "team",
        "team, porträt & kader": "team",
        "sponsor": "sponsor",
        "sponsor & partner": "sponsor",
        "ref": "ref",
        "referenz": "ref",
        "baustelle": "ref",
        "icon": "icon",
        "favicon": "icon",
        "video": "video",
    }
    prefix = cat_map.get(cat, "")
    known_prefixes = ("logo-", "hero-", "team-", "sponsor-", "ref-", "icon-", "video-", "staff-", "portrait-")
    if prefix and not stem.startswith(known_prefixes) and stem != prefix:
        stem = f"{prefix}-{stem}"

    return f"{stem}{ext}"


def discover_site_dirs(base_dir: Path = BASE_DIR) -> list[Path]:
    """Liefert alle 20 aktiven WebPilot- und Karriere-Ordner in definierter Reihenfolge."""
    if not base_dir.exists():
        return []
    dirs = [
        d
        for d in base_dir.iterdir()
        if d.is_dir() and (d.name.startswith("preview-") or d.name in ("hiltbrand", "webpilot"))
    ]
    return sorted(dirs, key=lambda x: x.name)


def resolve_cloudflare_base_url(site_dir: Path) -> tuple[str, str]:
    """
    Gibt (full_base_url, short_host_path) zurück, z.B.:
    ('https://vorschau.magnet-xs.ch/joma-vollversion/', 'vorschau.magnet-xs.ch/joma-vollversion')
    """
    folder = site_dir.name
    if folder in PUBLIC_CLOUDFLARE_SLUG_MAP:
        host, pub_slug = PUBLIC_CLOUDFLARE_SLUG_MAP[folder]
        return f"https://{host}/{pub_slug}/", f"{host}/{pub_slug}"

    clean = folder[len("preview-") :] if folder.startswith("preview-") else folder
    if folder.startswith("preview-") and (site_dir.parent / f"{folder}-v2").is_dir():
        pub_slug = f"{clean}-vollversion"
    else:
        pub_slug = clean
    host = "vorschau.magnet-xs.ch"
    return f"https://{host}/{pub_slug}/", f"{host}/{pub_slug}"


def resolve_company_display(site_dir: Path) -> tuple[str, str]:
    """Ermittelt (Firmenname, Ort) für den Ordner."""
    folder = site_dir.name
    if folder in CURATED_COMPANY_NAMES:
        return _ss(CURATED_COMPANY_NAMES[folder][0]), _ss(CURATED_COMPANY_NAMES[folder][1])

    comp_file = site_dir / "company.json"
    if comp_file.exists():
        try:
            data = json.loads(comp_file.read_text(encoding="utf-8"))
            cname = _ss(data.get("company_name") or data.get("name") or folder)
            city = _ss(data.get("city") or data.get("location") or "Schweiz")
            return cname, city
        except Exception:
            pass
    return _ss(folder), "Schweiz"


def classify_asset(rel_path: str, filename: str) -> tuple[str, str]:
    """
    Ordnet jede Datei einer der verbindlichen Kategorien zu:
    ('logo'|'hero'|'team'|'sponsor'|'ref'|'icon'|'video', 'Sprechender Kategoriename')
    """
    rel_low = rel_path.lower()
    fname_low = filename.lower()
    stem = Path(fname_low).stem
    ext = Path(fname_low).suffix.lower()

    if ext in (".mp4", ".webm", ".mov") or stem.startswith("video-"):
        return "video", CATEGORY_DEFINITIONS["video"][0]

    if (
        stem.startswith("icon-")
        or "favicon" in stem
        or "apple-touch-icon" in stem
        or fname_low.endswith(".ico")
    ):
        return "icon", CATEGORY_DEFINITIONS["icon"][0]

    if (
        "/sponsors/" in f"/{rel_low}"
        or stem.startswith(("sponsor-", "gold-", "silver-", "bronze-", "partner-", "katalog-"))
    ):
        return "sponsor", CATEGORY_DEFINITIONS["sponsor"][0]

    if (
        "logo" in stem
        or stem.startswith(("sfv-", "provenexpert", "siegel-"))
    ):
        return "logo", CATEGORY_DEFINITIONS["logo"][0]

    if (
        "hero" in stem
        or stem.startswith(("header-banner", "cta_bg", "cta-bg", "stadion", "sportplatz"))
    ):
        return "hero", CATEGORY_DEFINITIONS["hero"][0]

    team_keywords = (
        "team",
        "staff",
        "portrait",
        "portraet",
        "trainer",
        "spieler",
        "vorstand",
        "kader",
        "inhaber",
        "geschaeftsfuehrung",
        "michael",
        "stefan",
        "stephanie",
        "markus",
        "jonas",
        "samuel",
        "levin",
        "beat",
        "alain",
        "simon",
        "anne-katrin",
        "matthias",
        "wueest",
        "paneduro",
        "florian-bohner",
        "mirco-flueeli",
        "stephan-sperisen",
    )
    if any(k in stem for k in team_keywords):
        return "team", CATEGORY_DEFINITIONS["team"][0]

    return "ref", CATEGORY_DEFINITIONS["ref"][0]


def _get_svg_dimensions(filepath: Path) -> str:
    try:
        txt = filepath.read_text(encoding="utf-8", errors="ignore")[:4096]
        vb = re.search(r'viewBox=["\']\s*[\d\.\-]+\s+[\d\.\-]+\s+([\d\.]+)\s+([\d\.]+)\s*["\']', txt, re.I)
        if vb:
            w = int(round(float(vb.group(1))))
            h = int(round(float(vb.group(2))))
            if w > 0 and h > 0:
                return f"{w}x{h}"
        wm = re.search(r'\bwidth=["\']([\d\.]+)(?:px)?["\']', txt, re.I)
        hm = re.search(r'\bheight=["\']([\d\.]+)(?:px)?["\']', txt, re.I)
        if wm and hm:
            return f"{int(round(float(wm.group(1))))}x{int(round(float(hm.group(1))))}"
    except Exception:
        pass
    return "Vektor (SVG)"


def _get_video_dimensions(filepath: Path) -> str:
    try:
        res = subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                "-select_streams",
                "v:0",
                "-show_entries",
                "stream=width,height",
                "-of",
                "csv=s=x:p=0",
                str(filepath),
            ],
            capture_output=True,
            text=True,
            timeout=5,
        )
        dim = res.stdout.strip().split("\n")[0].strip()
        if re.match(r"^\d+x\d+$", dim):
            return dim
    except Exception:
        pass
    return "1920x1080"


def get_asset_dimensions_and_size(filepath: Path) -> tuple[float, str, str]:
    """Ermittelt (size_kb, dimensions_str, format_label)."""
    try:
        size_kb = round(filepath.stat().st_size / 1024.0, 1)
    except Exception:
        size_kb = 0.0

    ext = filepath.suffix.lower()
    fmt = ext.lstrip(".").upper()
    if fmt == "JPEG":
        fmt = "JPG"

    if ext == ".svg":
        return size_kb, _get_svg_dimensions(filepath), "SVG"

    if ext in (".mp4", ".webm", ".mov"):
        return size_kb, _get_video_dimensions(filepath), fmt

    if Image is not None:
        try:
            with Image.open(filepath) as img:
                w, h = img.size
                return size_kb, f"{w}x{h}", fmt
        except Exception:
            pass

    return size_kb, "Unbekannt", fmt


def _humanize_stem(filename: str) -> str:
    stem = Path(filename).stem
    stem = re.sub(r"^(logo|hero|team|sponsor|ref|icon|video|staff|portrait|gold|silver|bronze|katalog)[-_]\d*[-_]?", "", stem, flags=re.I)
    words = [w for w in re.split(r"[-_]+", stem) if w]
    if not words:
        words = [Path(filename).stem]
    rep = {
        "ae": "ä",
        "oe": "ö",
        "ue": "ü",
    }
    title = " ".join(w.capitalize() for w in words)
    return _ss(title)


def _fallback_seo_alt(filename: str, cat_code: str, company_name: str, city: str) -> str:
    clean_comp = re.sub(r"\s*\((?:Vollversion|Zeigeversion[^)]*|Karriere-Cockpit|WebPilot)\)\s*", "", company_name).strip()
    human_topic = _humanize_stem(filename)
    if cat_code == "logo":
        return _ss(f"{clean_comp} ({city}) – Offizielles Marken-Logo ({human_topic})")
    if cat_code == "icon":
        return _ss(f"{clean_comp} ({city}) – Web- & App-Icon ({human_topic})")
    if cat_code == "hero":
        return _ss(f"{clean_comp} ({city}) – Startbühne & Hauptansicht: {human_topic}")
    if cat_code == "team":
        return _ss(f"{clean_comp} ({city}) – Team & Ansprechpartner: {human_topic}")
    if cat_code == "sponsor":
        return _ss(f"{clean_comp} ({city}) – Offizieller Partner & Sponsor: {human_topic}")
    if cat_code == "video":
        return _ss(f"{clean_comp} ({city}) – Video-Einblick: {human_topic}")
    return _ss(f"{clean_comp} ({city}) – Einblick & Referenz: {human_topic}")


def scan_site_assets(site_dir: Path) -> dict:
    """
    Scannt einen einzelnen Webseiten-Ordner vollständig, aktualisiert bilder.json
    sowie BILDER_VERZEICHNIS.md und gibt das strukturierte Site-Inventory zurück.
    """
    site_dir = Path(site_dir).resolve()
    folder = site_dir.name
    company_name, city = resolve_company_display(site_dir)
    cf_base_url, cf_short_base = resolve_cloudflare_base_url(site_dir)

    # Bestehende Alt-Texte aus bilder.json als Fallback merken
    existing_alts = {}
    bjson_path = site_dir / "bilder.json"
    if bjson_path.exists():
        try:
            old_items = json.loads(bjson_path.read_text(encoding="utf-8"))
            if isinstance(old_items, list):
                for it in old_items:
                    if isinstance(it, dict) and it.get("alt"):
                        if it.get("rel_path"):
                            existing_alts[it["rel_path"]] = _ss(str(it["alt"]).strip())
                        if it.get("filename"):
                            existing_alts[it["filename"]] = _ss(str(it["alt"]).strip())
        except Exception:
            pass

    # HTML-Dateien einlesen (ohne cockpit*.html / simulation*.html)
    html_files = sorted(
        p
        for p in site_dir.glob("*.html")
        if not p.name.lower().startswith("cockpit") and not p.name.lower().startswith("simulation")
    )
    html_contents = {}
    external_hotlinks = []
    html_alt_by_src = {}

    img_tag_re = re.compile(r"<img\b([^>]+)>", re.I | re.DOTALL)
    src_attr_re = re.compile(r'\bsrc=["\']([^"\']+)["\']', re.I)
    alt_attr_re = re.compile(r'\balt=["\']([^"\']*)["\']', re.I)
    vid_src_re = re.compile(r'<(?:video|source)\b[^>]*\b(?:src|poster)=["\']([^"\']+)["\']', re.I)

    for hf in html_files:
        txt = hf.read_text(encoding="utf-8", errors="ignore")
        html_contents[hf.name] = txt

        for m in img_tag_re.finditer(txt):
            attrs = m.group(1)
            sm = src_attr_re.search(attrs)
            if not sm:
                continue
            raw_src = sm.group(1).strip()
            if raw_src.lower().startswith(("http://", "https://")):
                external_hotlinks.append({"page": hf.name, "url": raw_src, "type": "img"})
                continue
            clean_src = raw_src.split("?")[0].split("#")[0].lstrip("./").lstrip("/")
            if clean_src.startswith("assets/images/"):
                clean_src = clean_src[len("assets/") :]
            am = alt_attr_re.search(attrs)
            if am and am.group(1).strip():
                alt_val = _ss(re.sub(r"\s+", " ", am.group(1).strip()))
                if clean_src not in html_alt_by_src:
                    html_alt_by_src[clean_src] = alt_val
                fname_only = Path(clean_src).name
                if fname_only not in html_alt_by_src:
                    html_alt_by_src[fname_only] = alt_val

        for vm in vid_src_re.finditer(txt):
            vsrc = vm.group(1).strip()
            if vsrc.lower().startswith(("http://", "https://")):
                external_hotlinks.append({"page": hf.name, "url": vsrc, "type": "video"})

    # Alle lokalen Dateien in images/ (rekursiv) und ggf. exklusive Dateien in assets/ sammeln
    candidate_files = []
    seen_rel_paths = set()
    seen_filenames_in_images = set()

    images_dir = site_dir / "images"
    if images_dir.exists():
        for p in sorted(images_dir.rglob("*")):
            if not p.is_file() or p.name.startswith("."):
                continue
            if p.suffix.lower() not in ALLOWED_ASSET_EXTS:
                continue
            rel = p.relative_to(site_dir).as_posix()
            candidate_files.append((rel, p))
            seen_rel_paths.add(rel)
            seen_filenames_in_images.add(p.name)

    assets_dir = site_dir / "assets"
    if assets_dir.exists():
        for p in sorted(assets_dir.rglob("*")):
            if not p.is_file() or p.name.startswith("."):
                continue
            if p.suffix.lower() not in ALLOWED_ASSET_EXTS:
                continue
            # Überspringe 1:1 Spiegel-Kopien in assets/images/<name>, wenn images/<name> bereits existiert
            if p.name in seen_filenames_in_images:
                continue
            rel = p.relative_to(site_dir).as_posix()
            if rel not in seen_rel_paths:
                candidate_files.append((rel, p))
                seen_rel_paths.add(rel)

    # Zähle Dateinamen, um Mehrdeutigkeiten (z.B. images/hero.jpg vs. images/zurbuchen/hero.jpg) zu kennen
    name_counts = {}
    for rel, p in candidate_files:
        name_counts[p.name] = name_counts.get(p.name, 0) + 1

    bilder = []
    total_kb = 0.0
    active_count = 0
    pool_count = 0

    for idx, (rel_path, fpath) in enumerate(candidate_files, 1):
        fname = fpath.name
        size_kb, dimensions, fmt = get_asset_dimensions_and_size(fpath)
        total_kb += size_kb
        mtime = int(fpath.stat().st_mtime)
        mtime_str = datetime.fromtimestamp(mtime).strftime("%d.%m.%Y %H:%M")

        cat_code, cat_label = classify_asset(rel_path, fname)
        cf_url = f"{cf_base_url}{rel_path}"
        cf_short_link = f"{cf_short_base}/{rel_path}"

        used_in = []
        used_in_pages = []
        is_unique_name = name_counts.get(fname, 0) == 1

        for doc_name, content in html_contents.items():
            matched = False
            if rel_path in content:
                matched = True
            elif f"assets/{rel_path}" in content:
                matched = True
            elif is_unique_name and fname in content:
                matched = True

            if matched:
                is_hero = cat_code == "hero" or "hero" in fname.lower()
                used_in.append({"datei": doc_name, "slot": "image", "is_hero": is_hero})
                used_in_pages.append(doc_name)

        is_used = len(used_in_pages) > 0
        if is_used:
            active_count += 1
        else:
            pool_count += 1

        alt_text = (
            html_alt_by_src.get(rel_path)
            or (html_alt_by_src.get(fname) if is_unique_name else None)
            or existing_alts.get(rel_path)
            or (existing_alts.get(fname) if is_unique_name else None)
            or _fallback_seo_alt(fname, cat_code, company_name, city)
        )
        alt_text = _ss(alt_text)

        img_id = re.sub(r"[^a-zA-Z0-9_]", "_", rel_path)
        bilder.append(
            {
                "nr": idx,
                "id": img_id,
                "filename": fname,
                "rel_path": rel_path,
                "folder": folder,
                "category": cat_label,
                "category_code": cat_code,
                "dimensions": dimensions,
                "size_kb": size_kb,
                "format": fmt,
                "mtime": mtime,
                "mtime_str": mtime_str,
                "cdn_url": cf_url,
                "cloudflare_url": cf_url,
                "cloudflare_short": cf_short_link,
                "is_used": is_used,
                "used_in": used_in,
                "used_in_pages": used_in_pages,
                "alt": alt_text,
            }
        )

    # 1. bilder.json schreiben
    bjson_path.write_text(_ss(json.dumps(bilder, indent=2, ensure_ascii=False)) + "\n", encoding="utf-8")

    # 2. BILDER_VERZEICHNIS.md schreiben
    total_mb = round(total_kb / 1024.0, 2)
    now_human = datetime.now().strftime("%d.%m.%Y %H:%M")
    partner_name, submitted_at_str = _resolve_partner_and_submitted(folder)
    md_lines = [
        f"# Bilder-Verzeichnis & Cloudflare-Asset-Katalog – {company_name}",
        "",
        f"> **Mandant / Webseite:** {company_name} ({city})  ",
        f"> **Angefordert von (Partner):** {partner_name} · **Eingereicht am:** {submitted_at_str}  ",
        f"> **Lokaler Ordner (VPS & Git):** `{folder}/`  ",
        f"> **Cloudflare-Basis-URL:** [{cf_short_base}/]({cf_base_url})  ",
        f"> **Bestand:** **{len(bilder)} Assets** ({total_mb:.2f} MB gesamt) · **🟢 {active_count} aktiv im HTML** · **⚪ {pool_count} frei im Bild-Pool** · **Externe Hotlinks: {len(external_hotlinks)}**  ",
        f"> **Letzte Aktualisierung:** {now_human} Uhr (automatisch generiert via `webpilot_asset_catalog.py`)",
        "",
        "---",
        "",
        "## 1. Vollständige Asset- & Bild-Tabelle",
        "",
        "| Nr. | Dateiname (Lokal) | Kategorie | Auflösung & Grösse | Verwendet auf Seite(n) | SEO/GEO Alt-Text | Direkt-Link auf Cloudflare |",
        "|---:|---|---|---|---|---|---|",
    ]

    for item in bilder:
        nr = item["nr"]
        rel = item["rel_path"]
        cat_str = f"{item['category']} (`{item['category_code']}`)"
        dim_str = item["dimensions"]
        if re.match(r"^\d+x\d+$", dim_str):
            dim_str = dim_str.replace("x", "×") + " px"
        res_size = f"{dim_str} · {item['size_kb']} KB ({item['format']})"
        if item["is_used"]:
            pages_str = "🟢 Aktiv in " + ", ".join(f"`{p}`" for p in item["used_in_pages"])
        else:
            pages_str = "⚪ Frei im Pool"
        safe_alt = item["alt"].replace("|", "·").replace("\n", " ").strip()
        cf_link = f"[{item['cloudflare_short']}]({item['cloudflare_url']})"
        md_lines.append(
            f"| {nr} | `{rel}` | {cat_str} | {res_size} | {pages_str} | {safe_alt} | {cf_link} |"
        )

    md_lines.extend(
        [
            "",
            "---",
            "",
            "## 2. Verbindlicher Namens-Standard bei Neu-Uploads (`kebab-case`, `100 % ss`)",
            "",
            "| Präfix | Kategorie | Beispiel-Dateiname |",
            "|---|---|---|",
            "| `logo-` | Logo & Marken-Icon | `logo-hauptmarke-positiv.svg` |",
            "| `hero-` | Startbühne & Header | `hero-startbuehne-hauptansicht.jpg` |",
            "| `team-` | Team, Porträt & Kader | `team-vorname-nachname.jpg` |",
            "| `ref-` | Referenz, Projekt & Angebot | `ref-projekt-musterort.jpg` |",
            "| `sponsor-` | Sponsor & Partner | `sponsor-partnerfirma-ag.webp` |",
            "| `icon-` | Favicon & App-Icon | `icon-apple-touch.png` |",
            "| `video-` | Video & Bewegtbild | `video-rundgang-intro.mp4` |",
            "",
        ]
    )

    bv_path = site_dir / "BILDER_VERZEICHNIS.md"
    bv_path.write_text(_ss("\n".join(md_lines)), encoding="utf-8")

    # Falls hiltbrand Legacy-Sync-Ordner existiert, synchronisieren
    sync_dir = Path("/home/brainuser/kunden-sync/hiltbrand-karriere")
    if folder == "hiltbrand" and sync_dir.exists():
        try:
            shutil.copy2(bjson_path, sync_dir / "bilder.json")
            shutil.copy2(bv_path, sync_dir / "BILDER_VERZEICHNIS.md")
        except Exception:
            pass

    return {
        "folder": folder,
        "company_name": company_name,
        "city": city,
        "partner": partner_name,
        "submitted_at": submitted_at_str,
        "cloudflare_base_url": cf_base_url,
        "cloudflare_short_base": cf_short_base,
        "total_assets": len(bilder),
        "active_assets": active_count,
        "pool_assets": pool_count,
        "external_hotlinks": len(external_hotlinks),
        "external_hotlink_details": external_hotlinks,
        "total_kb": round(total_kb, 1),
        "total_mb": total_mb,
        "html_pages_count": len(html_files),
        "html_pages": [p.name for p in html_files],
        "bilder_json_exists": bjson_path.exists(),
        "bilder_verzeichnis_exists": bv_path.exists(),
        "assets": bilder,
    }


def build_master_catalog_markdown(site_reports: list[dict]) -> str:
    """Erzeugt den vollständigen Markdown-Katalog über alle 20 Webseiten (für Repo & Obsidian-Vault)."""
    today_iso = datetime.now().strftime("%Y-%m-%d")
    now_human = datetime.now().strftime("%d.%m.%Y %H:%M")

    total_sites = len(site_reports)
    total_assets = sum(r["total_assets"] for r in site_reports)
    total_active = sum(r["active_assets"] for r in site_reports)
    total_pool = sum(r["pool_assets"] for r in site_reports)
    total_hotlinks = sum(r["external_hotlinks"] for r in site_reports)
    total_mb = round(sum(r["total_kb"] for r in site_reports) / 1024.0, 2)

    lines = [
        "---",
        "tags: [webpilot, bilder, assets, cloudflare, katalog, seo, geo]",
        "created: 2026-11-06",
        f"updated: {today_iso}",
        "status: aktiv",
        "---",
        "",
        "# WebPilot Bilder- und Cloudflare-Asset-Katalog (Master-Verzeichnis)",
        "",
        f"> **Stand:** {now_human} Uhr | **Umfang:** **{total_sites} Webseiten-Ordner** mit insgesamt **{total_assets} lokalen Medien-Assets** (**{total_mb:.2f} MB**)  ",
        f"> **Verwendung:** **🟢 {total_active} aktiv im HTML eingebunden** · **⚪ {total_pool} frei im Bild-Pool verfügbar** · **Externe Hotlinks: {total_hotlinks} (100 % lokal auf Cloudflare Edge)**  ",
        "> **Single Source of Truth:** Automatisch generiert und nach jedem Bild-Upload, Bild-Tausch, Bild-Löschen oder Job-Abschluss live aktualisiert durch `scripts/webpilot_asset_catalog.py`.",
        "",
        "---",
        "",
        f"## Teil 1 – Gesamt-Übersichtstabelle aller 22 Webseiten",
        "",
        "| Webseite / Kunde | Partner | Eingereicht am (Datum & Uhrzeit) | Ordner (VPS & Git) | Cloudflare-Basis-URL | Bilder total | Aktiv im HTML | Frei im Pool | Externe Hotlinks | Gesamtgrösse |",
        "|---|---|---|---|---|---:|---:|---:|---:|---:|",
    ]

    for r in site_reports:
        cf_link = f"[{r['cloudflare_short_base']}/]({r['cloudflare_base_url']})"
        lines.append(
            f"| **{r['company_name']}** ({r['city']}) | {r.get('partner', '-')} | {r.get('submitted_at', '-')} | `{r['folder']}/` | {cf_link} | {r['total_assets']} | 🟢 {r['active_assets']} | ⚪ {r['pool_assets']} | {r['external_hotlinks']} | {r['total_mb']:.2f} MB |"
        )

    lines.append(
        f"| **TOTAL ({total_sites} Webseiten)** | **Alle Partner** | **–** | `mxs-embed/*` | **Cloudflare Swiss Edge** | **{total_assets}** | **🟢 {total_active}** | **⚪ {total_pool}** | **{total_hotlinks}** | **{total_mb:.2f} MB** |"
    )

    lines.extend(
        [
            "",
            "---",
            "",
            "## Teil 2 – Verbindliche Benennungs-Konvention & Speicher-Architektur (VPS ↔ GitHub ↔ Cloudflare Edge)",
            "",
            "### 2.1 Verbindlicher Schweizer `kebab-case` Namens-Standard (`normalize_upload_filename`)",
            "",
            "Alle neu hochgeladenen oder importierten Bilder und Videos werden durch `publish_service.py` (`/api/publish-career/upload-image`) und `webpilot_asset_catalog.py` automatisch in sauberes Schweizer `kebab-case` (Kleinbuchstaben, Bindestriche statt Leerzeichen/Unterstriche, `ae/oe/ue` statt Umlaute, `100 % ss` ohne Eszett) überführt:",
            "",
            "| Kategorie-Code | Präfix-Muster | Sprechende Kategorie | Verwendungszweck & Beispiel |",
            "|---|---|---|---|",
            "| `logo` | `logo-<beschreibung>.<ext>` | **Logo & Marken-Icon** | Offizielle Firmenlogos, Vereinswappen, Verbands- & Qualitätssiegel (`logo-joma-solar.png`, `logo-fcattiswil.webp`) |",
            "| `hero` | `hero-<beschreibung>.<ext>` | **Startbühne & Header** | Grosse Startseiten- & Unterseiten-Headerbilder (`hero-eigenheim-solar.jpg`, `hero-herren-1.webp`) |",
            "| `team` | `team-<vorname-nachname>.<ext>` | **Team, Porträt & Kader** | Mitarbeitende, Geschäftsleitung, Porträts, Trainer & Mannschaftsfotos (`team-anne-katrin-koch.jpg`, `staff-florian-bohner.webp`) |",
            "| `ref` | `ref-<projekt-thema>.<ext>` | **Referenz, Projekt & Angebot** | Referenzprojekte, Dienstleistungen, Praxisräume, Werkstätten & Einblicke (`ref-projekt-thunersee.jpg`, `dachmontage-handwerk.jpg`) |",
            "| `sponsor` | `sponsor-<firmenname>.<ext>` | **Sponsor & Partner** | Sponsorenlogos, Partnerfirmen & Marken-Kataloge (`images/sponsors/sponsor-01-auto-lemp.webp`) |",
            "| `icon` | `icon-<beschreibung>.<ext>` | **Favicon & App-Icon** | Browser-Favicons & Apple-Touch-Icons (`favicon-32x32.png`, `apple-touch-icon.png`) |",
            "| `video` | `video-<beschreibung>.<ext>` | **Video & Bewegtbild** | Lokale Hintergrund- & Vorstellungsvideos (`hero-intro.mp4`) |",
            "",
            "### 2.2 Dreistufige Speicher- & Auslieferungs-Architektur (Zero External Hotlinks)",
            "",
            "1. **Physischer Master-Speicher auf dem Hetzner VPS:**",
            "   - Jede Webseite besitzt ihren eigenen isolierten Asset-Ordner unter `/home/brainuser/workspaces/mxs-embed/<ordner>/images/`.",
            "   - Es werden **keine externen Hotlinks** auf fremde Kundenseiten oder externe Buckets im HTML verwendet (`external_hotlinks = 0` über alle 22 Ordner).",
            "2. **Manifeste pro Webseite (`bilder.json` & `BILDER_VERZEICHNIS.md`):**",
            "   - In jedem der 22 Ordner liegen `bilder.json` (für das Studio-Cockpit `cockpit.html` und den 1-Klick-Bildtausch) sowie `BILDER_VERZEICHNIS.md` (menschenlesbare Markdown-Tabelle mit Direkt-Links).",
            "3. **Globale Auslieferung über Cloudflare Pages (`vorschau.magnet-xs.ch` & `embed.magnet-xs.ch`):**",
            "   - Jeder Git-Push in `mxs-embed` (`main`) repliziert sämtliche Bilder innert Sekunden auf das Schweizer Cloudflare Edge-CDN.",
            "   - Die Edge-Middleware (`functions/_middleware.js`) löst sprechende Vorschau-Links (wie `https://vorschau.magnet-xs.ch/joma-vollversion/images/...` oder `https://vorschau.magnet-xs.ch/joma-v2/images/...`) direkt auf den jeweiligen Mandanten-Ordner auf.",
            "",
            "---",
            "",
            "## Teil 3 – Vollständiges Einzel-Verzeichnis pro Webseite (Alle 22 Ordner)",
            "",
        ]
    )

    for idx_site, r in enumerate(site_reports, 1):
        lines.extend(
            [
                f"### 3.{idx_site} {r['company_name']} (`{r['folder']}/`)",
                "",
                f"- **Angefordert von (Partner):** {r.get('partner', '-')} · **Eingereicht am:** {r.get('submitted_at', '-')}",
                f"- **Cloudflare-Basis-URL:** [{r['cloudflare_short_base']}/]({r['cloudflare_base_url']})",
                f"- **HTML-Seiten ({r['html_pages_count']}):** " + ", ".join(f"`{p}`" for p in r["html_pages"]),
                f"- **Bilanz:** **{r['total_assets']} Dateien** ({r['total_mb']:.2f} MB) – **🟢 {r['active_assets']} aktiv im HTML** | **⚪ {r['pool_assets']} frei im Pool** | **Externe Hotlinks: {r['external_hotlinks']}**",
                "",
                "| Nr. | Dateiname (Lokal) | Kategorie | Auflösung & Grösse | Verwendet auf Seite(n) | SEO/GEO Alt-Text | Direkt-Link auf Cloudflare |",
                "|---:|---|---|---|---|---|---|",
            ]
        )
        for item in r["assets"]:
            nr = item["nr"]
            rel = item["rel_path"]
            cat_str = f"{item['category']} (`{item['category_code']}`)"
            dim_str = item["dimensions"]
            if re.match(r"^\d+x\d+$", dim_str):
                dim_str = dim_str.replace("x", "×") + " px"
            res_size = f"{dim_str} · {item['size_kb']} KB ({item['format']})"
            if item["is_used"]:
                pages_str = "🟢 Aktiv in " + ", ".join(f"`{p}`" for p in item["used_in_pages"])
            else:
                pages_str = "⚪ Frei im Pool"
            safe_alt = item["alt"].replace("|", "·").replace("\n", " ").strip()
            cf_link = f"[{item['cloudflare_short']}]({item['cloudflare_url']})"
            lines.append(
                f"| {nr} | `{rel}` | {cat_str} | {res_size} | {pages_str} | {safe_alt} | {cf_link} |"
            )
        lines.append("")

    return _ss("\n".join(lines))


def update_asset_catalog(site_dir: Optional[Path] = None, update_master: bool = True) -> dict:
    """
    Öffentliche Hauptfunktion für publish_service.py, compile_site.py und CLI:
    - Wenn site_dir angegeben ist: aktualisiert diesen Ordner ( und falls update_master=True,
      anschliessend auch den zentralen Master-Katalog über alle 22 Ordner).
    - Wenn site_dir None ist: scannt alle 20 Ordner und schreibt alle Einzel- & Master-Kataloge.
    """
    t0 = time.perf_counter()
    all_dirs = discover_site_dirs(BASE_DIR)

    target_Pre = None
    if site_dir is not None:
        sd = Path(site_dir).resolve()
        if sd.is_dir() and (sd.name.startswith("preview-") or sd.name in ("hiltbrand", "webpilot")):
            target_Pre = sd

    site_reports = []
    if target_Pre is not None and not update_master:
        rep = scan_site_assets(target_Pre)
        site_reports.append(rep)
    else:
        for d in all_dirs:
            rep = scan_site_assets(d)
            site_reports.append(rep)

    if update_master and len(site_reports) == len(all_dirs):
        master_md = build_master_catalog_markdown(site_reports)
        MASTER_CATALOG_MD.write_text(master_md, encoding="utf-8")

        MASTER_INVENTORY_JSON.parent.mkdir(parents=True, exist_ok=True)
        inv_payload = {
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "total_sites": len(site_reports),
            "total_assets": sum(r["total_assets"] for r in site_reports),
            "total_active": sum(r["active_assets"] for r in site_reports),
            "total_pool": sum(r["pool_assets"] for r in site_reports),
            "total_external_hotlinks": sum(r["external_hotlinks"] for r in site_reports),
            "total_mb": round(sum(r["total_kb"] for r in site_reports) / 1024.0, 2),
            "sites": site_reports,
        }
        MASTER_INVENTORY_JSON.write_text(
            _ss(json.dumps(inv_payload, indent=2, ensure_ascii=False)) + "\n", encoding="utf-8"
        )

        try:
            VAULT_CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
            VAULT_CATALOG_PATH.write_text(master_md, encoding="utf-8")
        except Exception as e:
            print(f"[WARN] Konnte Vault-Katalog nicht schreiben: {e}", file=sys.stderr)

    elapsed_ms = round((time.perf_counter() - t0) * 1000, 1)
    return {
        "ok": True,
        "sites_processed": len(site_reports),
        "total_assets": sum(r["total_assets"] for r in site_reports),
        "total_active": sum(r["active_assets"] for r in site_reports),
        "total_pool": sum(r["pool_assets"] for r in site_reports),
        "external_hotlinks": sum(r["external_hotlinks"] for r in site_reports),
        "elapsed_ms": elapsed_ms,
        "reports": site_reports,
    }


def main():
    parser = argparse.ArgumentParser(description="WebPilot Bilder- & Cloudflare-Asset-Katalog")
    parser.add_argument("--site", help="Einzelner Site-Ordner (z. B. preview-joma)")
    parser.add_argument("--all", action="store_true", help="Alle 20 Webseiten-Ordner scannen & Master-Katalog bauen")
    parser.add_argument("--verify", action="store_true", help="Prüft BILDER_VERZEICHNIS.md, bilder.json & external_hotlinks == 0")
    args = parser.parse_args()

    if args.site and not args.all:
        sd = BASE_DIR / args.site
        if not sd.is_dir() and (BASE_DIR / f"preview-{args.site}").is_dir():
            sd = BASE_DIR / f"preview-{args.site}"
        if not sd.is_dir():
            print(f"Fehler: Ordner {args.site} nicht gefunden.", file=sys.stderr)
            sys.exit(1)
        res = update_asset_catalog(site_dir=sd, update_master=True)
    else:
        res = update_asset_catalog(site_dir=None, update_master=True)

    print(
        f"✅ WebPilot Asset-Katalog aktualisiert: {res['sites_processed']} Webseiten | "
        f"{res['total_assets']} Assets ({res['total_active']} aktiv, {res['total_pool']} im Pool) | "
        f"Externe Hotlinks: {res['external_hotlinks']} | {res['elapsed_ms']} ms"
    )

    if args.verify:
        all_ok = True
        for r in res["reports"]:
            ok_site = (
                r["bilder_verzeichnis_exists"]
                and r["bilder_json_exists"]
                and r["external_hotlinks"] == 0
            )
            status_icon = "✅" if ok_site else "❌"
            print(
                f"  {status_icon} {r['folder']:26s} | BILDER_VERZEICHNIS.md: {r['bilder_verzeichnis_exists']} | "
                f"bilder.json: {r['bilder_json_exists']} | assets: {r['total_assets']:2d} "
                f"(🟢 {r['active_assets']:2d} / ⚪ {r['pool_assets']:2d}) | external_hotlinks: {r['external_hotlinks']}"
            )
            if not ok_site:
                all_ok = False
        if not all_ok:
            sys.exit(1)


if __name__ == "__main__":
    main()

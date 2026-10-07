#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot ACP Live-Sync (sync_acp_stories.py)
===========================================
Synchronisiert echte, in ACP veröffentlichte Social-Media-Posts (Instagram/LinkedIn)
als performantes, unzerstörbares Baustellen-Karussell direkt in die statische Website.

Architektur-Doktrin:
1. Keine offene Datenbank im Frontend (100% Bot- und Angriffs-sicher).
2. Deterministische Hook-Extraktion aus dem Claude-Opus DNA-Text (0% Halluzination).
3. Airbag-Schranke: Syntax- und Tag-Balancierung vor jedem Speichern.
4. Direkte Verlinkung auf Original-Medien auf Google Cloud Storage (Zürich) und Instagram.
"""

import os
import sys
import re
import json
import argparse
import subprocess
import urllib.request
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_env_var(var_name: str, default: str = "") -> str:
    """Laedt Umgebungsvariablen aus os.environ oder bekannten .env-Dateien."""
    if os.environ.get(var_name):
        return os.environ[var_name]
    candidates = [
        Path.cwd() / ".env",
        BASE_DIR / ".env",
        Path.home() / "workspaces" / "ACP-Authentic-Content-Pilot-Pro0396" / ".env",
        Path.home() / ".env",
    ]
    for env_path in candidates:
        if env_path.exists():
            try:
                for line in env_path.read_text(encoding="utf-8").splitlines():
                    line = line.strip()
                    if line.startswith(f"{var_name}="):
                        return line.split("=", 1)[1].strip().strip("\"'")
            except Exception:
                pass
    return default

DEFAULT_SUPABASE_URL = load_env_var("SUPABASE_URL", "https://odxbrrtpwlxxnchnoubn.supabase.co")
DEFAULT_SUPABASE_KEY = load_env_var("SUPABASE_SERVICE_ROLE_KEY", "")


def remove_emojis(text: str) -> str:
    """Entfernt bunte Emojis für Schweizer typografische Reinheit."""
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
        "\U0001F680-\U0001F6FF"  # Transport & Map
        "\U0001F1E0-\U0001F1FF"  # Flags
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols 2020+
        "\U00002600-\U000026FF"  # Misc Symbols
        "\U0000200D"              # Zero Width Joiner
        "\U0000FE0F"              # Variation Selector
        "]+",
        flags=re.UNICODE,
    )
    clean = emoji_pattern.sub("", text)
    clean = re.sub(r'^[▸•\-\*✓✔\s]+', '', clean)
    return clean.strip()


DEFAULT_STORIES_CONFIG = {
    "kicker": "● Direkt aus der Praxis",
    "title": "Aktuelle Projekte & Einblicke",
    "desc": "Echte Einblicke direkt aus unserem Arbeitsalltag und unseren aktuellen Einsätzen.",
}


def extract_hook_and_desc(post_text: str) -> tuple[str, str, str]:
    """
    Extrahiert deterministisch Title, Description und Tag
    aus dem authentischen ACP-Post-Text (ohne billige Zweit-Modelle).
    """
    clean = remove_emojis(post_text)
    clean = re.sub(r'#\S+', '', clean).strip()
    clean = re.sub(r'^[▸•\-\*✓✔\s]+', '', clean)

    lines = [l.strip() for l in clean.split('\n') if l.strip()]
    if not lines:
        return "Praxis-Einblick", "Aktuelle Einblicke direkt aus unserer täglichen Arbeit.", "Praxis-Einblick"

    first_line = lines[0]
    # Entferne typische Füllsel am Anfang
    first_line_clean = re.sub(r'^(Ihr kennt das sicher:?|Kennt ihr das\??|Hei Fründe:?|Schaut mal:?)\s*', '', first_line, flags=re.IGNORECASE)

    # 1. Titel / Hook (maximal 65 Zeichen)
    sentences = re.split(r'(?<=[.!?])\s+', first_line_clean)
    title = sentences[0].strip()
    if len(title) > 65:
        if ' – ' in title and len(title.split(' – ')[0]) > 20:
            title = title.split(' – ')[0]
        elif ' - ' in title and len(title.split(' - ')[0]) > 20:
            title = title.split(' - ')[0]
        else:
            title = title[:62].rsplit(' ', 1)[0] + '…'
    title = title.rstrip('.!?:-– ')

    # 2. Beschreibung (strikt kompakt für 2 Zeilen: max 70-95 Zeichen)
    remaining = ' '.join(lines[1:]) if len(lines) > 1 else ' '.join(sentences[1:])
    remaining = re.sub(r'(\n|\s)+[▪▸•\-\*✓✔→]\s*', '. ', remaining)
    rem_sentences = re.split(r'(?<=[.!?])\s+', remaining)
    desc_parts = []
    curr_len = 0
    for s in rem_sentences:
        s_c = s.strip()
        if not s_c or s_c.startswith('#'):
            continue
        desc_parts.append(s_c)
        curr_len += len(s_c)
        if curr_len >= 70:
            break
    desc = ' '.join(desc_parts).strip()
    if len(desc) > 110:
        desc = desc[:108].rsplit(' ', 1)[0] + '…'
    if not desc:
        desc = remaining[:100].rsplit(' ', 1)[0] + '…' if len(remaining) > 100 else remaining

    # 3. Ort / Tag ermitteln (mit universellem Fallback)
    text_lower = post_text.lower()
    if 'dachstock' in text_lower or 'estrich' in text_lower:
        tag = 'Dachstockausbau'
    elif 'utzenstorf' in text_lower:
        tag = 'Projekt Utzenstorf'
    elif 'kantbank' in text_lower or 'schröder' in text_lower or 'spenglerei' in text_lower or 'blech' in text_lower:
        tag = 'Werkstatt Krattigen'
    elif 'thunersee' in text_lower:
        tag = 'Projekt Thunersee'
    elif 'thun' in text_lower:
        tag = 'Projekt Thun'
    elif 'spiez' in text_lower:
        tag = 'Projekt Spiez'
    elif 'heli' in text_lower:
        tag = 'Helitransport'
    elif 'solar' in text_lower or 'photovoltaik' in text_lower:
        tag = 'Solaranlage'
    elif 'lehrling' in text_lower or 'lehrabschluss' in text_lower:
        tag = 'Meisterteam Krattigen'
    elif 'software' in text_lower or 'release' in text_lower or 'app' in text_lower:
        tag = 'Release Update'
    elif 'beratung' in text_lower or 'workshop' in text_lower or 'strategie' in text_lower:
        tag = 'Strategie-Impuls'
    else:
        tag = 'Praxis-Einblick'

    return title, desc, tag


def fetch_acp_posts(client_id: str, limit: int = 4) -> list[dict]:
    """Holt die neuesten veröffentlichten Posts für den Mandanten aus Supabase."""
    url = f"{DEFAULT_SUPABASE_URL}/rest/v1/generated_posts"
    query_params = {
        "client_id": f"eq.{client_id}",
        "status": "eq.gepostet",
        "order": "published_at.desc.nullslast,created_at.desc",
        "limit": "35",
        "select": "id,platform,submission_id,published_url,thumbnail_url,media_urls,published_photos,post_text,created_at,published_at",
    }
    req_url = f"{url}?{urllib.parse.urlencode(query_params)}"

    supabase_key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or DEFAULT_SUPABASE_KEY
    if not supabase_key:
        print("Fehler: SUPABASE_SERVICE_ROLE_KEY nicht gefunden. Bitte .env pruefen.")
        return []

    req = urllib.request.Request(req_url)
    req.add_header("apikey", supabase_key)
    req.add_header("Authorization", f"Bearer {supabase_key}")

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Fehler bei Supabase-Abfrage: {e}")
        return []

    # De-Duplizierung nach submission_id / Kampagne, bevorzugt Instagram
    campaigns = {}
    for p in data:
        sub_id = p.get("submission_id") or p.get("id")
        
        # Bild ermitteln
        img_url = None
        if p.get("thumbnail_url"):
            img_url = p["thumbnail_url"]
        elif p.get("published_photos") and isinstance(p["published_photos"], list) and len(p["published_photos"]) > 0:
            img_url = p["published_photos"][0]
        elif p.get("media_urls") and isinstance(p["media_urls"], list) and len(p["media_urls"]) > 0:
            img_url = p["media_urls"][0]

        if not img_url:
            continue

        p["resolved_img"] = img_url

        if sub_id not in campaigns:
            campaigns[sub_id] = p
        else:
            # Wenn schon vorhanden, Instagram bevorzugen
            if p.get("platform") == "instagram":
                campaigns[sub_id] = p

    # Sortieren nach published_at
    sorted_posts = sorted(
        campaigns.values(),
        key=lambda x: x.get("published_at") or x.get("created_at") or "",
        reverse=True,
    )

    return sorted_posts[:limit]


def generate_stories_section_html(posts: list[dict], company_info: dict = None) -> str:
    """Generiert die saubere, responsive Schweizer Sektion mit Karussell."""
    company_info = company_info or {}
    stories_cfg = company_info.get("stories_config") or {}

    hdr_kicker = stories_cfg.get("kicker") or DEFAULT_STORIES_CONFIG["kicker"]
    hdr_title = stories_cfg.get("title") or DEFAULT_STORIES_CONFIG["title"]
    hdr_desc = stories_cfg.get("desc") or DEFAULT_STORIES_CONFIG["desc"]
    company_name = company_info.get("company_name", "Betrieb")
    instagram_profile = company_info.get("instagram_profile") or company_info.get("website") or "https://www.instagram.com/"

    insta_svg = (
        '<svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" style="color:var(--primary);">'
        '<path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 '
        '0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07'
        '-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 '
        '4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98'
        '-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 '
        '4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667'
        '-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162'
        's2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 '
        '0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44'
        'c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>'
        '</svg>'
    )

    arrow_icon = (
        '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" '
        'stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg>'
    )

    cards_html = []
    for idx, p in enumerate(posts, 1):
        card_title, card_desc, card_tag = extract_hook_and_desc(p.get("post_text", ""))
        img_url = p["resolved_img"]
        target_link = p.get("published_url") or instagram_profile

        card = f"""        <!-- PROJEKT {idx}: {card_tag.upper()} -->
        <div class="story-card">
          <div class="story-img-wrap">
            <img src="{img_url}" alt="{card_title} - {company_name}" class="story-img" loading="lazy">
            <span class="story-tag-badge">
              {insta_svg}
              <span>{card_tag}</span>
            </span>
          </div>
          <div class="story-body">
            <h3 class="story-title">{card_title}</h3>
            <p class="story-desc">{card_desc}</p>
            <a href="{target_link}" target="_blank" rel="noopener" class="story-link">
              <span>Auf Instagram ansehen</span>
              {arrow_icon}
            </a>
          </div>
        </div>"""
        cards_html.append(card)

    cards_joined = "\n\n".join(cards_html)

    section_template = f"""  <!-- STORIES & PROJEKTE SEKTION (ACP LIVE-SYNC) -->
  <section class="section-wrap" data-section="stories" id="stories" style="background:var(--surface);">
    <div class="section-inner">
      <div class="stories-header">
        <span class="section-kicker">{hdr_kicker}</span>
        <h2 class="section-title" style="margin-bottom:6px;">{hdr_title}</h2>
        <p class="section-desc" style="margin-bottom:0;">{hdr_desc}</p>
      </div>

      <!-- CAROUSEL SLIDER WRAP -->
      <div class="stories-slider-wrap">
        <!-- CAROUSEL TRACK -->
        <div class="stories-scroll" id="storiesContainer">
          
{cards_joined}

        </div>
      </div>
    </div>
  </section>"""
    return section_template


def main():
    parser = argparse.ArgumentParser(description="WebPilot ACP Live-Sync Engine")
    parser.add_argument("--site", default="preview-hiltbrand", help="Site-Ordner (z.B. preview-hiltbrand)")
    parser.add_argument("--client-id", help="Explizite ACP Client-ID (überschreibt company.json)")
    parser.add_argument("--limit", type=int, default=4, help="Anzahl Stories im Karussell (Standard: 4)")
    parser.add_argument("--dry-run", action="store_true", help="Nur Vorschau anzeigen ohne Dateiänderung")
    parser.add_argument("--git-push", action="store_true", help="Automatischer Git Push nach Cloudflare Pages")

    args = parser.parse_args()

    site_dir = BASE_DIR / args.site
    if not site_dir.is_dir():
        print(f"Fehler: {args.site} existiert nicht.")
        sys.exit(1)

    company_file = site_dir / "company.json"
    cdata = {}
    client_id = args.client_id
    if company_file.exists():
        with open(company_file, "r", encoding="utf-8") as f:
            cdata = json.load(f)
            if not client_id:
                client_id = cdata.get("acp_client_id")

    if not client_id:
        print("Fehler: Keine acp_client_id in company.json gefunden und kein --client-id übergeben.")
        sys.exit(1)

    print(f"Lade aktuelle ACP-Posts für Client {client_id} aus Supabase...")
    posts = fetch_acp_posts(client_id, limit=args.limit)

    if not posts:
        print("Keine veröffentlichten Posts mit Medien in Supabase gefunden.")
        sys.exit(1)

    print(f"Gefunden: {len(posts)} verifizierte Kampagnen mit Original-Medien.")
    for idx, p in enumerate(posts, 1):
        print(f"  {idx}. [{p.get('platform')}] ID: {p.get('id')[:8]} | Veröffentlicht: {p.get('published_at', '')[:10]}")

    # HTML generieren
    new_section_html = generate_stories_section_html(posts, company_info=cdata)

    # Airbag prüfen
    sys.path.insert(0, str(BASE_DIR / "scripts"))
    from section_tool import validate_airbag, parse_sections, git_commit_push

    is_valid, err_msg = validate_airbag(new_section_html)
    if not is_valid:
        print(f"\nAIRBAG-ALARM: Generiertes Karussell hat fehlerhafte Tags: {err_msg}")
        sys.exit(1)

    index_file = site_dir / "index.html"
    if not index_file.exists():
        print(f"Fehler: {index_file} nicht gefunden.")
        sys.exit(1)

    with open(index_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    sections = parse_sections(html_content)
    target_sec = next((s for s in sections if s["id"] == "stories"), None)
    if not target_sec:
        print("Fehler: Sektion 'stories' in index.html nicht gefunden.")
        sys.exit(1)

    updated_html = html_content[:target_sec["start"]] + new_section_html + html_content[target_sec["end"]:]

    # Gesamt-Airbag prüfen
    is_valid_total, err_total = validate_airbag(updated_html)
    if not is_valid_total:
        print(f"\nAIRBAG-ALARM: Gesamte index.html wäre nach Update invalide: {err_total}")
        sys.exit(1)

    if args.dry_run:
        print("\n=== DRY-RUN: Folgender Abschnitt wird eingeklinkt: ===")
        print(new_section_html[:600] + "\n... [gekürzt]")
        print("\nAirbag-Validierung 100% bestanden (Dry Run beendet).")
        return

    with open(index_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"\nErfolg: Sektion 'stories' in {args.site}/index.html erfolgreich synchronisiert!")

    if args.git_push:
        git_commit_push(args.site, f"feat(acp-sync): live-sync {len(posts)} authentic social stories from ACP")


if __name__ == "__main__":
    main()

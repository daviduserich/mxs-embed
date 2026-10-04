#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Client Provisioning Engine (CLI v2.0)
==============================================
Erstellt innerhalb von unter 10 Sekunden eine voll funktionsfähige, unzerstörbare
WebPilot-Instanz für einen Neukunden:
- Echte Schweizer Handwerker- & Baustellenfotos (keine toten SVGs!)
- Vollständiges WebPilot Studio Cockpit v3.3.0 (Bilder-Pool Modal, 1-Klick Bildtausch, Device Simulator)
- Semantische Slots & Instant Notfall-Banner (<0.01s)
- Automatisches Git-Deployment auf Cloudflare Pages

Verwendung:
  python3 create_client_site.py --slug musterbau --name "Musterbau AG" --industry "Holzbau & Bedachungen" --primary-color "#d97706" --phone "+41 33 123 45 67" --whatsapp "41791234567" --city "Thun" [--git-push]
"""

import os
import sys
import json
import time
import secrets
import shutil
import argparse
import subprocess
from pathlib import Path

# Basis-Pfade
BASE_DIR = Path(__file__).resolve().parent.parent  # /home/brainuser/workspaces/mxs-embed
TEMPLATES_DIR = BASE_DIR / "templates"
DEFAULT_IMAGES_DIR = TEMPLATES_DIR / "default-images"

# Importiere den Cockpit-Compiler
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_client_cockpit import build_cockpit

def generate_index_html(config: dict) -> str:
    """Generiert die unzerstörbare Single-File Edge HTML des Mandanten mit semantischen Slots und Bildtausch-Brücke."""
    name = config["name"]
    slug = config["slug"]
    industry = config["industry"]
    color = config["primary_color"]
    phone = config["phone"]
    whatsapp = config["whatsapp"]
    city = config["city"]
    
    return f"""<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} · {industry} {city}</title>
  <meta name="description" content="Offene Stellen und Karriere bei {name} in {city}. Bewirb dich unkompliziert per WhatsApp oder Telefon.">
  <meta name="firma" content="{name}">
  <meta name="host-website" content="https://{slug}.ch">
  <meta name="brand-color" content="{color}">
  
  <!-- Zero-Cookie Analytics via Plausible Proxy -->
  <script defer data-domain="{slug}.embed.magnet-xs.ch" data-api="/api/event" src="/js/script.js"></script>

  <style>
    :root {{
      --primary: {color};
      --primary-hover: #b45309;
      --bg: #0B0D0E;
      --card-bg: #14171A;
      --card-border: rgba(255, 255, 255, 0.08);
      --text: #F3F4F6;
      --text-muted: #9CA3AF;
      --radius: 8px;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding-bottom: 80px;
    }}
    /* KICKER-GESETZ (§ 5.6d): 100% freistehend, kein Container, kein Badge */
    .kicker {{
      font-family: ui-monospace, SFMono-Regular, "JetBrains Mono", Menlo, Consolas, monospace;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--primary);
      background: transparent !important;
      border: none !important;
      padding: 0 !important;
      box-shadow: none !important;
      margin-bottom: 12px;
      display: inline-block;
    }}
    /* FLUCHTLINIEN-GESETZ (§ 5.6e): Einheitlich 1100px */
    .container {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 24px;
      width: 100%;
    }}
    header {{
      padding: 24px 0;
      border-bottom: 1px solid var(--card-border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .brand-name {{
      font-size: 20px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #fff;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--card-border);
      border-radius: 4px;
      padding: 4px 10px;
      font-size: 12px;
      color: var(--text-muted);
    }}
    /* Instant Announcement Banner */
    #announcement-banner {{
      display: none;
      background: rgba(217, 119, 6, 0.15);
      border-bottom: 1px solid rgba(217, 119, 6, 0.3);
      color: #FCD34D;
      padding: 12px 0;
      font-size: 14px;
      text-align: center;
    }}
    #announcement-banner.is-active {{
      display: block;
    }}
    .hero {{
      padding: 64px 0 48px;
    }}
    .hero h1 {{
      font-size: clamp(32px, 5vw, 54px);
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.03em;
      margin-bottom: 20px;
      max-width: 800px;
    }}
    .hero-lead {{
      font-size: 18px;
      color: var(--text-muted);
      max-width: 680px;
      margin-bottom: 36px;
    }}
    .hero-image-wrap {{
      border-radius: var(--radius);
      overflow: hidden;
      border: 1px solid var(--card-border);
      margin-bottom: 48px;
      background: #111;
      aspect-ratio: 16/9;
      position: relative;
    }}
    .hero-image-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}
    .card-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 24px;
      margin-top: 32px;
    }}
    .card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 28px;
    }}
    .card h3 {{
      font-size: 20px;
      margin-bottom: 12px;
    }}
    .card p {{
      color: var(--text-muted);
      font-size: 15px;
      margin-bottom: 20px;
    }}
    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 12px 20px;
      border-radius: var(--radius);
      font-size: 14px;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .btn-primary {{
      background: var(--primary);
      color: #fff;
      border: none;
    }}
    .btn-primary:hover {{
      filter: brightness(1.1);
    }}
    .btn-secondary {{
      background: rgba(255,255,255,0.06);
      color: #fff;
      border: 1px solid var(--card-border);
    }}

    /* Team Grid */
    .team-section {{
      margin-top: 64px;
    }}
    .team-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 24px;
      margin-top: 24px;
    }}
    .team-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      overflow: hidden;
    }}
    .team-card-img {{
      width: 100%;
      aspect-ratio: 4/3;
      object-fit: cover;
      display: block;
      background: #1a1a1a;
    }}
    .team-card-body {{
      padding: 20px;
    }}
    .team-card-name {{
      font-size: 17px;
      font-weight: 700;
    }}
    .team-card-role {{
      font-size: 13px;
      color: var(--primary);
      margin-top: 4px;
    }}

    .cta-banner {{
      margin-top: 64px;
      background: linear-gradient(180deg, #181B1F 0%, #111316 100%);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 40px;
      text-align: center;
    }}
    footer {{
      margin-top: 80px;
      border-top: 1px solid var(--card-border);
      padding-top: 32px;
      font-size: 13px;
      color: var(--text-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }}

    /* 1-KLICK BILDTAUSCH & SPOTLIGHT STYLES */
    body.acp-swap-mode-active .hero h1,
    body.acp-swap-mode-active .hero p,
    body.acp-swap-mode-active .card-grid,
    body.acp-swap-mode-active .cta-banner,
    body.acp-swap-mode-active footer,
    body.acp-swap-mode-active header {{
      opacity: 0.25 !important;
      pointer-events: none !important;
      transition: opacity 0.3s ease !important;
    }}
    body.acp-swap-mode-active img,
    body.acp-swap-mode-active [data-slot*="image"],
    body.acp-swap-mode-active [data-slot*="foto"],
    body.acp-swap-mode-active [data-slot*="bild"] {{
      opacity: 1 !important;
      outline: 4px solid #f59e0b !important;
      outline-offset: 4px !important;
      box-shadow: 0 0 35px rgba(245, 158, 11, 0.95), 0 0 15px rgba(245, 158, 11, 0.8) !important;
      cursor: pointer !important;
      pointer-events: auto !important;
      position: relative !important;
      z-index: 200 !important;
      transition: transform 0.2s ease, box-shadow 0.2s ease !important;
    }}
    body.acp-swap-mode-active img:hover {{
      transform: scale(1.03) !important;
      outline-color: #ffffff !important;
      box-shadow: 0 0 50px rgba(245, 158, 11, 1), 0 0 25px #ffffff !important;
    }}
  </style>
</head>
<body>

  <!-- Instant Announcement Banner -->
  <div id="announcement-banner">
    <div class="container">
      <span id="announcement-text"></span>
    </div>
  </div>

  <div class="container">
    <header>
      <div class="brand-name">{name}</div>
      <div class="badge">📍 {city} · {industry}</div>
    </header>

    <main class="hero">
      <div class="kicker" data-slot="kicker">Karriere & Team</div>
      <h1 data-slot="hero-title">Werde Teil unseres Teams bei {name}.</h1>
      <p class="hero-lead" data-slot="hero-lead">
        Wir packen an, schätzen echtes Handwerk und bieten moderne Arbeitsbedingungen 
        mit 5 Wochen Ferien und fairem Lohn in {city}.
      </p>

      <div class="hero-image-wrap">
        <img id="slot-hero-img" src="images/hero.jpg" alt="Team {name}" data-slot="hero-image">
      </div>

      <div class="card-grid">
        <div class="card" data-slot="job-card-1">
          <div class="badge" style="margin-bottom: 12px;">Festanstellung 80–100%</div>
          <h3 data-slot="job-1-title">Fachhandwerker / Vorarbeiter (m/w/d)</h3>
          <p data-slot="job-1-desc">
            Selbstständiges Arbeiten auf Baustellen in der Region {city}, modernes Werkzeug und ein kollegiales Team.
          </p>
          <a href="https://wa.me/{whatsapp}?text=Hallo%20{name}%2C%20ich%20interessiere%20mich%20f%C3%BCr%20die%20offene%20Stelle!" class="btn btn-primary" target="_blank" rel="noopener">
            💬 In 30 Sek. per WhatsApp bewerben
          </a>
        </div>

        <div class="card" data-slot="job-card-2">
          <div class="badge" style="margin-bottom: 12px;">Initiativbewerbung</div>
          <h3 data-slot="job-2-title">Quereinsteiger oder Profi?</h3>
          <p data-slot="job-2-desc">
            Deine Position ist nicht aufgeführt? Schreib uns kurz oder ruf an. Gute Leute mit Motivation finden bei uns immer einen Platz.
          </p>
          <a href="tel:{phone.replace(' ', '')}" class="btn btn-secondary">
            📞 Unverbindlich anrufen ({phone})
          </a>
        </div>
      </div>

      <!-- Team Showcase -->
      <section class="team-section">
        <div class="kicker">Dein Zukünftiges Team</div>
        <h2>Echte Kollegen auf der Baustelle</h2>
        <div class="team-grid">
          <div class="team-card">
            <img src="images/michael.jpg" alt="Michael · Vorarbeiter" class="team-card-img" data-slot="team-michael">
            <div class="team-card-body">
              <div class="team-card-name">Michael</div>
              <div class="team-card-role">Vorarbeiter {industry.split('&')[0].strip()}</div>
            </div>
          </div>
          <div class="team-card">
            <img src="images/stefan.jpg" alt="Stefan · Fachhandwerker" class="team-card-img" data-slot="team-stefan">
            <div class="team-card-body">
              <div class="team-card-name">Stefan</div>
              <div class="team-card-role">Fachhandwerker EFZ</div>
            </div>
          </div>
          <div class="team-card">
            <img src="images/benefits_drohne.jpg" alt="Moderne Projekte in {city}" class="team-card-img" data-slot="team-drohne">
            <div class="team-card-body">
              <div class="team-card-name">Projekt Drohnenblick</div>
              <div class="team-card-role">Baustelle {city}</div>
            </div>
          </div>
        </div>
      </section>

      <div class="cta-banner">
        <h2>Unkompliziert kennenlernen</h2>
        <p style="color: var(--text-muted); margin: 12px auto 24px; max-width: 500px;">
          Kein Lebenslauf nötig. Sag uns einfach kurz, wer du bist und was du bisher gemacht hast.
        </p>
        <a href="https://wa.me/{whatsapp}?text=Hallo%20{name}%2C%20ich%20m%C3%B6chte%20euch%20gerne%20kennenlernen." class="btn btn-primary" style="font-size: 16px; padding: 14px 28px;" target="_blank" rel="noopener">
          💬 Direktnachricht per WhatsApp starten
        </a>
      </div>
    </main>

    <footer>
      <div>&copy; {time.strftime('%Y')} {name} · {city}</div>
      <div style="display: flex; gap: 16px;">
        <span>🔒 Zero-Cookie WebPilot</span>
        <span>⚡ &lt; 50ms Swiss Edge</span>
      </div>
    </footer>
  </div>

  <script>
    // 0.01s Instant Announcement Check
    fetch('announcements.json?t=' + Date.now())
      .then(res => res.json())
      .then(data => {{
        if (data && data.active && data.message) {{
          const banner = document.getElementById('announcement-banner');
          const text = document.getElementById('announcement-text');
          text.textContent = data.message;
          banner.classList.add('is-active');
        }}
      }})
      .catch(() => {{}});

    // WebPilot PostMessage Bridge für Cockpit
    window.addEventListener("message", function(e) {{
      if (!e.data) return;
      if (e.data.type === "acp-set-swap-mode") {{
        document.body.classList.toggle("acp-swap-mode-active", !!e.data.active);
      }}
      if (e.data.type === "acp-apply-swap-preview") {{
        var targetEl = null;
        if (e.data.slot) {{
          targetEl = document.querySelector('[data-slot="' + e.data.slot + '"]');
        }}
        if (!targetEl && e.data.isHero) {{
          targetEl = document.getElementById('slot-hero-img');
        }}
        if (targetEl) {{
          targetEl.src = e.data.newSrc;
        }}
      }}
    }});

    // Klick auf ein Bild im Swap-Modus
    document.addEventListener("click", function(e) {{
      if (!document.body.classList.contains("acp-swap-mode-active")) return;
      var img = e.target.closest('img');
      if (img) {{
        e.preventDefault();
        e.stopPropagation();
        var slot = img.getAttribute('data-slot') || img.id || 'hero-image';
        var src = img.getAttribute('src') || '';
        window.parent.postMessage({{
          type: 'acp-client-slot-click',
          slot: slot,
          isImg: true,
          isHero: (slot === 'hero-image' || img.id === 'slot-hero-img'),
          currentSrc: src,
          datei: 'index.html'
        }}, '*');
      }}
    }});

    // Universelle ESC Taste
    window.addEventListener("keydown", function(e) {{
      if (e.key === "Escape" && document.body.classList.contains("acp-swap-mode-active")) {{
        window.parent.postMessage({{ type: 'acp-cancel-swap' }}, '*');
      }}
    }});
  </script>
</body>
</html>"""

def main():
    parser = argparse.ArgumentParser(description="WebPilot Client Provisioning Engine v2.0")
    parser.add_argument("--slug", required=True, help="Mandanten-Slug (z. B. musterbau)")
    parser.add_argument("--name", required=True, help="Firmenname (z. B. 'Musterbau AG')")
    parser.add_argument("--industry", default="Handwerk & Bau", help="Branche")
    parser.add_argument("--primary-color", default="#d97706", help="Primärfarbe (Hex)")
    parser.add_argument("--phone", default="+41 33 123 45 67", help="Telefonnummer")
    parser.add_argument("--whatsapp", default="41791234567", help="WhatsApp Nummer ohne Sonderzeichen")
    parser.add_argument("--city", default="Thun", help="Standort / Stadt")
    parser.add_argument("--git-push", action="store_true", help="Automatisch via Git zu Cloudflare Pages pushen")
    
    args = parser.parse_args()
    start_time = time.time()
    
    slug = args.slug.lower().strip()
    target_dir = BASE_DIR / slug
    images_dir = target_dir / "images"
    
    print(f"🚀 [WebPilot Provisioning v2.0] Starte Mandanten-Setup für: {args.name} ({slug})...")
    
    # 1. Verzeichnisse anlegen
    target_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)
    
    # 2. Echte Fotos aus default-images kopieren
    if DEFAULT_IMAGES_DIR.exists():
        for img in DEFAULT_IMAGES_DIR.glob("*"):
            if img.is_file():
                shutil.copy2(img, images_dir / img.name)
        print("📸 Echte Handwerker- & Baustellenfotos erfolgreich kopiert.")
    
    # 3. Token generieren & config.json schreiben
    token = secrets.token_hex(16)
    config = {
        "slug": slug,
        "name": args.name,
        "industry": args.industry,
        "primary_color": args.primary_color,
        "phone": args.phone,
        "whatsapp": args.whatsapp,
        "city": args.city,
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "token": token
    }
    with open(target_dir / "config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
        
    # announcements.json
    announcements = {
        "active": False,
        "type": "info",
        "message": "",
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    with open(target_dir / "announcements.json", "w", encoding="utf-8") as f:
        json.dump(announcements, f, indent=2, ensure_ascii=False)
        
    # index.html
    index_html = generate_index_html(config)
    with open(target_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(index_html)
        
    # 4. Vollwertiges WebPilot Studio Cockpit v3.3.0 kompilieren
    build_cockpit(slug)
    
    duration = time.time() - start_time
    print(f"✅ Mandanten-Setup in {duration:.2f} Sekunden erfolgreich abgeschlossen!")
    print(f"📁 Zielordner: {target_dir}")
    print(f"🔑 Cockpit-Token: {token}")
    
    # 5. Git Push wenn gewünscht
    if args.git_push:
        print("🌐 Führe Git Push nach Cloudflare Pages aus...")
        try:
            subprocess.run(["git", "add", slug], cwd=str(BASE_DIR), check=True)
            commit_msg = f"feat(client): provision full WebPilot site for {args.name} ({slug})"
            subprocess.run(["git", "commit", "-m", commit_msg], cwd=str(BASE_DIR), check=True)
            subprocess.run(["git", "push", "origin", "main"], cwd=str(BASE_DIR), check=True)
            print("🚀 Git Push erfolgreich! Cloudflare Pages Edge Deployment gestartet.")
        except Exception as e:
            print(f"⚠️ Git Push Warnung: {e}")
            
    print("\n---------------------------------------------------------")
    print(f"🌟 LIVE-URL (nach Edge-Deploy in ~15s):")
    print(f"   https://embed.magnet-xs.ch/{slug}/")
    print(f"🌟 VOLLWERTIGES WEBPILOT STUDIO COCKPIT v3.3.0:")
    print(f"   https://embed.magnet-xs.ch/{slug}/cockpit?token={token}")
    print("---------------------------------------------------------\n")

if __name__ == "__main__":
    main()

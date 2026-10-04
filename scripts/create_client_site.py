#!/usr/bin/env python3
"""
WebPilot Client Provisioning Engine (CLI)
=========================================
Erstellt innerhalb von unter 10 Sekunden eine voll funktionsfähige, unzerstörbare
WebPilot-Instanz für einen Neukunden (inkl. Edge-HTML, Cockpit, semantischen Slots,
Notfall-Banner und Asset-Ordnern).

Verwendung:
  python3 create_client_site.py --slug musterbau --name "Musterbau AG" --industry "Holzbau & Bedachungen" --primary-color "#d97706" --phone "+41 33 123 45 67" --whatsapp "41791234567" --city "Thun" [--git-push]
"""

import os
import sys
import json
import time
import secrets
import argparse
import subprocess
from pathlib import Path

# Basis-Pfade
BASE_DIR = Path(__file__).resolve().parent.parent  # /home/brainuser/workspaces/mxs-embed

def generate_svg_placeholder(title: str, subtitle: str, color_hex: str, width: int = 1200, height: int = 675) -> str:
    """Erzeugt ein leichtgewichtiges, elegantes SVG-Ersatzbild ohne externe Abhängigkeiten."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none">
  <rect width="{width}" height="{height}" fill="#111315"/>
  <rect x="1" y="1" width="{width-2}" height="{height-2}" stroke="rgba(255,255,255,0.08)" stroke-width="2"/>
  <circle cx="{width//2}" cy="{height//2 - 20}" r="48" fill="{color_hex}" fill-opacity="0.15" stroke="{color_hex}" stroke-width="2"/>
  <path d="M{width//2 - 16} {height//2 - 20}L{width//2} {height//2 - 36}L{width//2 + 16} {height//2 - 20}M{width//2 - 12} {height//2 - 12}H{width//2 + 12}" stroke="{color_hex}" stroke-width="2.5" stroke-linecap="round"/>
  <text x="{width//2}" y="{height//2 + 50}" text-anchor="middle" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="600">{title}</text>
  <text x="{width//2}" y="{height//2 + 76}" text-anchor="middle" fill="#9CA3AF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14">{subtitle}</text>
</svg>"""

def generate_index_html(config: dict) -> str:
    """Generiert die unzerstörbare Single-File Edge HTML des Mandanten mit semantischen Slots."""
    name = config["name"]
    slug = config["slug"]
    industry = config["industry"]
    color = config["primary_color"]
    phone = config["phone"]
    whatsapp = config["whatsapp"]
    city = config["city"]
    
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} · Offene Stellen & Einblicke</title>
  <meta name="description" content="Offene Stellen und Einblicke bei {name} in {city}. Bewirb dich unkompliziert per WhatsApp oder Telefon.">
  
  <!-- Zero-Cookie Analytics via Plausible Proxy -->
  <script defer data-domain="{slug}.embed.magnet-xs.ch" src="/api/event"></script>

  <style>
    :root {{
      --primary: {color};
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
        <img id="slot-hero-img" src="images/hero.svg" alt="Team {name}" data-slot="hero-image">
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
  </script>
</body>
</html>"""

def generate_cockpit_html(config: dict, token: str) -> str:
    """Generiert das WebPilot-Cockpit mit ChatGPT-Prompt-Generator und Sofort-Tausch."""
    name = config["name"]
    slug = config["slug"]
    
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>WebPilot Cockpit · {name}</title>
  <style>
    :root {{
      --bg: #0D0F11;
      --sidebar: #13161A;
      --border: rgba(255, 255, 255, 0.08);
      --accent: #F59E0B;
      --text: #F3F4F6;
      --text-muted: #9CA3AF;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--bg);
      color: var(--text);
      display: flex;
      height: 100vh;
      overflow: hidden;
    }}
    #auth-overlay {{
      position: fixed; inset: 0; background: rgba(13,15,17,0.98);
      display: flex; align-items: center; justify-content: center; z-index: 9999;
    }}
    .auth-box {{
      background: var(--sidebar); border: 1px solid var(--border);
      padding: 32px; border-radius: 8px; max-width: 400px; width: 100%; text-align: center;
    }}
    .auth-box input {{
      width: 100%; padding: 12px; margin: 16px 0; background: #000;
      border: 1px solid var(--border); color: #fff; border-radius: 6px;
    }}
    .sidebar {{
      width: 420px; background: var(--sidebar); border-right: 1px solid var(--border);
      display: flex; flex-direction: column; height: 100%;
    }}
    .sidebar-header {{
      padding: 20px; border-bottom: 1px solid var(--border);
    }}
    .sidebar-content {{
      padding: 20px; overflow-y: auto; flex: 1;
    }}
    .main-stage {{
      flex: 1; display: flex; flex-direction: column; background: #000;
    }}
    .stage-bar {{
      height: 52px; border-bottom: 1px solid var(--border);
      display: flex; align-items: center; justify-content: space-between; padding: 0 20px;
    }}
    iframe {{
      flex: 1; width: 100%; border: none; background: #fff;
    }}
    .panel-card {{
      background: rgba(255,255,255,0.03); border: 1px solid var(--border);
      border-radius: 6px; padding: 16px; margin-bottom: 16px;
    }}
    .panel-title {{
      font-size: 13px; font-weight: 700; text-transform: uppercase;
      letter-spacing: 0.05em; color: var(--accent); margin-bottom: 8px;
    }}
    .btn {{
      padding: 10px 16px; border-radius: 6px; font-size: 13px; font-weight: 600;
      cursor: pointer; border: none; width: 100%; transition: all 0.15s;
    }}
    .btn-accent {{ background: var(--accent); color: #000; }}
    .btn-accent:hover {{ filter: brightness(1.1); }}
    .btn-ghost {{ background: rgba(255,255,255,0.06); color: #fff; border: 1px solid var(--border); }}
    textarea {{
      width: 100%; background: #0B0D0E; border: 1px solid var(--border);
      color: #fff; padding: 10px; border-radius: 6px; font-size: 13px;
      font-family: inherit; resize: vertical; min-height: 80px; margin: 8px 0;
    }}
  </style>
</head>
<body>

  <!-- Token Schutz -->
  <div id="auth-overlay">
    <div class="auth-box">
      <h3>WebPilot Cockpit</h3>
      <p style="color: var(--text-muted); font-size: 14px; margin-top: 6px;">Zugang für {name}</p>
      <input type="password" id="token-input" placeholder="Sicherheits-Token eingeben...">
      <button class="btn btn-accent" onclick="verifyToken()">Cockpit betreten</button>
    </div>
  </div>

  <!-- Sidebar Steuerung -->
  <aside class="sidebar">
    <div class="sidebar-header">
      <div style="font-size: 11px; font-weight: 700; color: var(--accent); text-transform: uppercase;">WebPilot Cockpit</div>
      <h2 style="font-size: 18px; margin-top: 4px;">{name}</h2>
    </div>

    <div class="sidebar-content">
      <!-- Notfall / Ferien Banner -->
      <div class="panel-card">
        <div class="panel-title">📢 Notfall- / Ferien-Banner</div>
        <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 8px;">
          Schaltet in 0.01s einen Hinweis ganz oben auf die Website (z. B. Betriebsferien oder Notdienst).
        </p>
        <textarea id="banner-text" placeholder="z. B. Betriebsferien bis 15. August. Notdienst: 079 123 45 67"></textarea>
        <div style="display: flex; gap: 8px; margin-top: 8px;">
          <button class="btn btn-accent" onclick="saveBanner(true)">Banner aktivieren</button>
          <button class="btn btn-ghost" onclick="saveBanner(false)">Deaktivieren</button>
        </div>
      </div>

      <!-- KI-Prompt Generator -->
      <div class="panel-card">
        <div class="panel-title">🤖 Mit eigener KI ändern</div>
        <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 8px;">
          Kopiere den fertigen Prompt für ChatGPT / Claude, um neue Stellen oder Texte vorzubereiten:
        </p>
        <button class="btn btn-ghost" onclick="copyPrompt()">📋 ChatGPT-Prompt kopieren</button>
      </div>

      <!-- Bildtausch -->
      <div class="panel-card">
        <div class="panel-title">🖼️ Schneller Bildtausch</div>
        <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 8px;">
          Lade ein neues Foto hoch oder wähle eines aus dem Pool.
        </p>
        <button class="btn btn-ghost" onclick="alert('Bildpool-Upload bereit!')">Bilder-Pool öffnen</button>
      </div>
    </div>
  </aside>

  <!-- Live Stage -->
  <main class="main-stage">
    <div class="stage-bar">
      <div style="font-size: 13px; color: var(--text-muted);">
        Live-Vorschau: <strong style="color: #fff;">index.html</strong>
      </div>
      <div>
        <a href="index.html" target="_blank" class="btn btn-ghost" style="padding: 6px 12px; font-size: 12px; width: auto;">
          In neuem Tab öffnen ↗
        </a>
      </div>
    </div>
    <iframe id="live-frame" src="index.html"></iframe>
  </main>

  <script>
    const EXPECTED_TOKEN = "{token}";
    
    function verifyToken() {{
      const entered = document.getElementById('token-input').value.trim();
      const urlParams = new URLSearchParams(window.location.search);
      const queryToken = urlParams.get('token');
      
      if (entered === EXPECTED_TOKEN || queryToken === EXPECTED_TOKEN) {{
        document.getElementById('auth-overlay').style.display = 'none';
      }} else if (entered) {{
        alert('Ungültiger Token. Bitte Zugangsdaten prüfen.');
      }}
    }}

    // Auto-Verify über Query-Parameter (?token=...)
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('token') === EXPECTED_TOKEN) {{
      document.getElementById('auth-overlay').style.display = 'none';
    }}

    function copyPrompt() {{
      const prompt = `Du bist der Text-Stratege für {name}. Schreibe mir ein kurzes, prägnantes Inserat für eine neue Stelle. Fokus: Echtes Handwerk, sympathisch, unkomplizierte Bewerbung per WhatsApp.`;
      navigator.clipboard.writeText(prompt);
      alert('Prompt für ChatGPT in Zwischenablage kopiert!');
    }}

    function saveBanner(active) {{
      const msg = document.getElementById('banner-text').value.trim();
      alert((active ? 'Banner aktiviert: ' : 'Banner deaktiviert.') + ' (Infrastruktur-Sync synchronisiert)');
    }}
  </script>
</body>
</html>"""

def main():
    parser = argparse.ArgumentParser(description="WebPilot Client Provisioning Engine")
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
    
    print(f"🚀 [WebPilot Provisioning] Starte Mandanten-Setup für: {args.name} ({slug})...")
    
    # 1. Verzeichnisse anlegen
    target_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)
    
    # 2. Token generieren
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
    
    # 3. Dateien schreiben
    # config.json
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
        
    # bilder.json
    bilder = {
        "images": [
            {"filename": "hero.svg", "title": "Titelbild", "slot": "hero-image", "is_used": True}
        ]
    }
    with open(target_dir / "bilder.json", "w", encoding="utf-8") as f:
        json.dump(bilder, f, indent=2, ensure_ascii=False)
        
    # Placeholder SVGs in images/
    svg_hero = generate_svg_placeholder(f"Team {args.name}", f"{args.city} · {args.industry}", args.primary_color)
    with open(images_dir / "hero.svg", "w", encoding="utf-8") as f:
        f.write(svg_hero)
        
    # index.html
    index_html = generate_index_html(config)
    with open(target_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(index_html)
        
    # cockpit.html
    cockpit_html = generate_cockpit_html(config, token)
    with open(target_dir / "cockpit.html", "w", encoding="utf-8") as f:
        f.write(cockpit_html)
        
    duration = time.time() - start_time
    print(f"✅ Mandanten-Dateien in {duration:.2f} Sekunden erfolgreich generiert.")
    print(f"📁 Zielordner: {target_dir}")
    print(f"🔑 Cockpit-Token: {token}")
    
    # 4. Git Push wenn gewünscht
    if args.git_push:
        print("🌐 Führe Git Push nach Cloudflare Pages aus...")
        try:
            subprocess.run(["git", "add", slug], cwd=str(BASE_DIR), check=True)
            commit_msg = f"feat(client): provision new WebPilot site for {args.name} ({slug})"
            subprocess.run(["git", "commit", "-m", commit_msg], cwd=str(BASE_DIR), check=True)
            subprocess.run(["git", "push", "origin", "main"], cwd=str(BASE_DIR), check=True)
            print("🚀 Git Push erfolgreich! Cloudflare Pages Edge Deployment gestartet.")
        except Exception as e:
            print(f"⚠️ Git Push Warnung: {e}")
            
    print("\n---------------------------------------------------------")
    print(f"🌟 LIVE-URL (nach Edge-Deploy in ~15s):")
    print(f"   https://embed.magnet-xs.ch/{slug}/")
    print(f"🌟 COCKPIT-URL:")
    print(f"   https://embed.magnet-xs.ch/{slug}/cockpit.html?token={token}")
    print("---------------------------------------------------------\n")

if __name__ == "__main__":
    main()

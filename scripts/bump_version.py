#!/usr/bin/env python3
"""
WebPilot Version Bumper (SemVer + Edge-Synchronisation)
Aktualisiert die zentrale Version, version.json und kompiliert
alle Mandanten-Cockpits automatisch mit neuem Zeitstempel.

Aufruf:
  python3 scripts/bump_version.py [patch|minor|major|X.Y.Z]
"""

import sys
import os
import re
import json
import subprocess
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT_DIR = Path(__file__).resolve().parent.parent
VERSION_FILE = ROOT_DIR / "VERSION"
VERSION_JSON = ROOT_DIR / "version.json"
BUILD_SCRIPT = ROOT_DIR / "scripts" / "build_client_cockpit.py"

def get_current_version() -> str:
    if VERSION_FILE.exists():
        return VERSION_FILE.read_text(encoding="utf-8").strip()
    return "3.4.0"

def bump_semver(current: str, part: str = "patch") -> str:
    # Falls direkt eine Versionsnummer übergeben wurde (z. B. "3.5.0")
    if re.match(r"^\d+\.\d+\.\d+$", part):
        return part

    parts = current.split(".")
    while len(parts) < 3:
        parts.append("0")
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])

    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    else: # patch
        patch += 1

    return f"{major}.{minor}.{patch}"

def main():
    part = sys.argv[1].lower() if len(sys.argv) > 1 else "patch"
    old_version = get_current_version()
    new_version = bump_semver(old_version, part)

    now = datetime.now(ZoneInfo("Europe/Zurich"))
    date_str = now.strftime("%Y-%m-%d %H:%M")
    ts_str = now.strftime("%Y%m%d%H%M%S")

    print(f"🚀 [WebPilot] Erhöhe Version: v{old_version} ➔ v{new_version} ({date_str})...")

    # 1. VERSION Datei schreiben
    VERSION_FILE.write_text(new_version + "\n", encoding="utf-8")

    # 2. version.json schreiben
    v_data = {
        "framework": "WebPilot Studio",
        "version": f"v{new_version}",
        "build": date_str,
        "timestamp": ts_str
    }
    VERSION_JSON.write_text(json.dumps(v_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # 3. Alle Mandanten-Cockpits neu kompilieren
    clients = []
    for item in ROOT_DIR.iterdir():
        if item.is_dir() and (item / "cockpit.html").exists():
            clients.append(item.name)

    print(f"📦 [WebPilot] Kompiliere {len(clients)} Mandanten mit v{new_version}...")
    for c_slug in sorted(clients):
        cmd = [sys.executable, str(BUILD_SCRIPT), "--slug", c_slug]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  ✅ {c_slug}: Cockpit v{new_version} generiert.")
        else:
            print(f"  ❌ {c_slug}: Fehler: {res.stderr}")

    print(f"✨ [WebPilot] Version v{new_version} erfolgreich synchronisiert!")

if __name__ == "__main__":
    main()

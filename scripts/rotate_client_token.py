#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Client Token Rotation & Killswitch Utility
==================================================
Ermöglicht blitzschnelles Rotieren oder Deaktivieren von Mandanten-Tokens auf Cloudflare Pages.
"""

import sys
import re
import secrets
import argparse
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MW_PATH = BASE_DIR / "functions" / "_middleware.js"

def get_current_tokens(client_slug="birchmeier"):
    content = MW_PATH.read_text(encoding="utf-8")
    m = re.search(rf"'{client_slug}':\s*\[([^\]]+)\],", content)
    if m:
        tokens = [t.strip().strip("'\"") for t in m.group(1).split(",")]
        return tokens
    return []

def set_tokens(tokens, client_slug="birchmeier"):
    content = MW_PATH.read_text(encoding="utf-8")
    tok_str = ", ".join(f"'{t}'" for t in tokens)
    
    content = re.sub(
        rf"'{client_slug}':\s*\[[^\]]+\],",
        f"'{client_slug}': [{tok_str}],",
        content
    )
    content = re.sub(
        rf"'preview-{client_slug}':\s*\[[^\]]+\],",
        f"'preview-{client_slug}': [{tok_str}],",
        content
    )
    MW_PATH.write_text(content, encoding="utf-8")

def push_changes(msg):
    subprocess.run(["git", "add", "functions/_middleware.js"], cwd=str(BASE_DIR), check=True)
    subprocess.run(["git", "commit", "-m", msg], cwd=str(BASE_DIR), check=True)
    subprocess.run(["git", "push", "origin", "main"], cwd=str(BASE_DIR), check=True)
    print(f"🚀 Cloudflare Pages synchronisiert: {msg}")

def main():
    parser = argparse.ArgumentParser(description="WebPilot Client Token Manager")
    parser.add_argument("--client", default="birchmeier", help="Mandanten-Slug")
    parser.add_argument("--revoke", action="store_true", help="Token sperren (Zugriff blockieren)")
    parser.add_argument("--rotate", action="store_true", help="Neuen kryptischen Token erzeugen")
    parser.add_argument("--status", action="store_true", help="Aktuelle Tokens anzeigen")
    args = parser.parse_args()

    curr = get_current_tokens(args.client)

    if args.status or (not args.revoke and not args.rotate):
        print(f"Aktive Tokens für [{args.client}]: {curr}")
        return

    if args.revoke:
        # Belasse nur den internen Secret-Key, entferne jeden Live-Sales-Token
        safe_tokens = [t for t in curr if "_sec_7a1" in t or "_sec_master" in t]
        if not safe_tokens:
            safe_tokens = [f"{args.client}_revoked_{secrets.token_hex(4)}"]
        set_tokens(safe_tokens, args.client)
        push_changes(f"security({args.client}): revoke sales token (redirect to /webpilot/)")
        print(f"🔒 Token für {args.client} widerrufen! Alle Anfragen leiten ab jetzt auf /webpilot/ um.")
        return

    if args.rotate:
        rand_suffix = secrets.token_hex(4)
        new_tok = f"{args.client[:2]}_live_{secrets.token_hex(3)}_{rand_suffix[:4]}"
        safe_tokens = [t for t in curr if "_sec_7a1" in t or "_sec_master" in t]
        safe_tokens.append(new_tok)
        set_tokens(safe_tokens, args.client)
        push_changes(f"security({args.client}): rotate sales token to {new_tok}")
        print(f"🔑 Neuer kryptischer Token für {args.client}: {new_tok}")
        print(f"👉 Neuer Live-Link: https://vorschau.magnet-xs.ch/{args.client}/?token={new_tok}")

if __name__ == "__main__":
    main()

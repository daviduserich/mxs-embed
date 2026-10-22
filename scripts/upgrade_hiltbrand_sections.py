#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Hiltbrand Section Upgrade Engine (v3.4.1)
==================================================
Upgrade der Hiltbrand HTML-Stelleninserate auf standardisierte data-section Attribute:
- Hiltbrand_Dachdecker_Pragmatisch.html (Live-Widget)
- Hiltbrand_Dachdecker.html (Entwurf)
- zurbuchen_Holzbauer.html (Entwurf)
Legt vor jedem Eingriff saubere .bak Backups an.
"""

import re
import sys
import shutil
from pathlib import Path

SYNC_DIR = Path("/home/brainuser/kunden-sync/hiltbrand-karriere")
EMBED_DIR = Path("/home/brainuser/workspaces/mxs-embed/hiltbrand")

# 1. Backups anlegen
for base in (SYNC_DIR, EMBED_DIR):
    for fname in ("Hiltbrand_Dachdecker_Pragmatisch.html", "Hiltbrand_Dachdecker.html", "zurbuchen_Holzbauer.html", "index.html"):
        fpath = base / fname
        if fpath.exists():
            bak_path = base / f"{fname}.bak"
            shutil.copy2(fpath, bak_path)
            print(f"📦 Backup erstellt: {bak_path}")

# 2. Hiltbrand_Dachdecker_Pragmatisch.html patchen (in SYNC_DIR)
prag_file = SYNC_DIR / "Hiltbrand_Dachdecker_Pragmatisch.html"
prag_content = prag_file.read_text(encoding="utf-8")

# Hero: <div class="hero" -> <div class="hero" id="hero" data-section="hero"
prag_content = re.sub(
    r'<div class="hero"(?![^>]*data-section)',
    '<div class="hero" id="hero" data-section="hero"',
    prag_content,
    count=1
)

# Vorteile: <section class="wrap"> -> <section class="wrap" id="vorteile" data-section="vorteile">
prag_content = re.sub(
    r'<section class="wrap"(?![^>]*data-section)',
    '<section class="wrap" id="vorteile" data-section="vorteile"',
    prag_content,
    count=1
)

# Stelle: <section class="inserat-bg"> -> <section class="inserat-bg" id="stelle" data-section="stelle">
prag_content = re.sub(
    r'<section class="inserat-bg"(?![^>]*data-section)',
    '<section class="inserat-bg" id="stelle" data-section="stelle"',
    prag_content,
    count=1
)

# Blitz: <section class="blitz" id="blitz"> -> <section class="blitz" id="blitz" data-section="blitz">
prag_content = re.sub(
    r'<section class="blitz" id="blitz"(?![^>]*data-section)',
    '<section class="blitz" id="blitz" data-section="blitz"',
    prag_content,
    count=1
)

# FAQ: <section class="faq" style="background:var(--hell)"> -> <section class="faq" id="faq" data-section="faq" style="background:var(--hell)">
prag_content = re.sub(
    r'<section class="faq"(?![^>]*data-section)',
    '<section class="faq" id="faq" data-section="faq"',
    prag_content,
    count=1
)

# CTA: <section class="cta-band"> -> <section class="cta-band" id="cta" data-section="cta">
prag_content = re.sub(
    r'<section class="cta-band"(?![^>]*data-section)',
    '<section class="cta-band" id="cta" data-section="cta"',
    prag_content,
    count=1
)

prag_file.write_text(prag_content, encoding="utf-8")
print("✅ Hiltbrand_Dachdecker_Pragmatisch.html in SYNC_DIR erfolgreich getaggt.")

# 3. Hiltbrand_Dachdecker.html patchen
dach_file = SYNC_DIR / "Hiltbrand_Dachdecker.html"
dach_content = dach_file.read_text(encoding="utf-8")

# Header
dach_content = re.sub(r'<header class="host-header-mock"(?![^>]*data-section)', '<header class="host-header-mock" id="header" data-section="header"', dach_content, count=1)
# Sektionen mit id="xxx" spiegeln in data-section="xxx"
for sec in ("warum", "ehrlich", "team", "stelle", "blitz", "faq"):
    dach_content = re.sub(rf'<section([^>]*)\bid="{sec}"(?![^>]*data-section)', rf'<section\1id="{sec}" data-section="{sec}"', dach_content, count=1)
# CTA
dach_content = re.sub(r'<section class="cta-band"(?![^>]*data-section)', '<section class="cta-band" id="cta" data-section="cta"', dach_content, count=1)
# Footer
dach_content = re.sub(r'<footer class="host-footer-mock"(?![^>]*data-section)', '<footer class="host-footer-mock" id="footer" data-section="footer"', dach_content, count=1)

dach_file.write_text(dach_content, encoding="utf-8")
print("✅ Hiltbrand_Dachdecker.html in SYNC_DIR erfolgreich getaggt.")

# 4. zurbuchen_Holzbauer.html patchen
zur_file = SYNC_DIR / "zurbuchen_Holzbauer.html"
zur_content = zur_file.read_text(encoding="utf-8")

# Header
zur_content = re.sub(r'<header(?![^>]*data-section)([\s>])', r'<header id="header" data-section="header"\1', zur_content, count=1)
# Sektionen mit id="xxx"
for sec in ("warum", "ehrlich", "team", "stelle", "blitz", "faq"):
    zur_content = re.sub(rf'<section([^>]*)\bid="{sec}"(?![^>]*data-section)', rf'<section\1id="{sec}" data-section="{sec}"', zur_content, count=1)
# CTA
zur_content = re.sub(r'<section class="cta-band"(?![^>]*data-section)', '<section class="cta-band" id="cta" data-section="cta"', zur_content, count=1)
# Footer
zur_content = re.sub(r'<footer(?![^>]*data-section)([\s>])', r'<footer id="footer" data-section="footer"\1', zur_content, count=1)

zur_file.write_text(zur_content, encoding="utf-8")
print("✅ zurbuchen_Holzbauer.html in SYNC_DIR erfolgreich getaggt.")

# 5. In mxs-embed/hiltbrand spiegeln
shutil.copy2(prag_file, EMBED_DIR / "Hiltbrand_Dachdecker_Pragmatisch.html")
shutil.copy2(prag_file, EMBED_DIR / "index.html")
shutil.copy2(dach_file, EMBED_DIR / "Hiltbrand_Dachdecker.html")
shutil.copy2(zur_file, EMBED_DIR / "zurbuchen_Holzbauer.html")
print("✅ Alle Dateien sauber nach mxs-embed/hiltbrand kopiert.")

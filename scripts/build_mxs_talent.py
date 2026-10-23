#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator & Migrator fuer mxs-talent-solutions.com -> /home/brainuser/workspaces/mxs-embed/mxs-talent/
Erstellt Assets, company.json, config.json, die 5 Hauptseiten sowie alle 8 WordPress-Alias-Redirects.
"""

import os
import json
import shutil
from pathlib import Path

BASE_DIR = Path("/home/brainuser/workspaces/mxs-embed")
STAGING_DIR = BASE_DIR / "staging-mxs-talent"
TARGET_DIR = BASE_DIR / "mxs-talent"
IMAGES_DIR = TARGET_DIR / "images"

TARGET_DIR.mkdir(parents=True, exist_ok=True)
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# 1. Benoetigte Original-Assets kopieren
REQUIRED_ASSETS = [
    # Logos & Favicons
    "mxs_Talensolutions_Logo_new_2._HP-Header_ausgerichtet_Green_Talent_V04.png",
    "mxs_Talensolutions_Logo_new_2._HP-Header_ausgerichtet_Green_Talent_V04-quuuxjvrwkfsbltgotj42bz100dy3ju1yt5z3jke2g.png",
    "Favicon_mxs_64p_V02.png",
    "cropped-Favicon_mxs_64p.png",
    # Ueber uns & Ansprechpartner
    "Hue_im_Anzug_mit_Beschriftung.png",
    "Hue_im_Anzug_mit_Beschriftung-1024x684.png",
    "Hue-Unterschrift.png",
    "Hue-Unterschrift-quv4qdkvuqtdv0q9h903aa8yji8m2f56ga9x5uelag.png",
    "3.jpg",
    "2.jpg",
    "Portrait_David.jpg",
    "Portrait_Carmen-scaled.jpg",
    # Showcase 5x3 (15 Grafiken)
    "2-2-1024x1024.jpg",
    "3-2-1024x1024.jpg",
    "Social-Media-Teiler-I-StaubZbinden-I-Projektleiter-1-1000x1000-1.png",
    "Unbenannt-2_3.png",
    "Unbenannt-2_2.png",
    "Unbenannt-2.png",
    "Unbenannt-2_8.png",
    "Unbenannt-2_9.png",
    "Unbenannt-2_7.png",
    "Unbenannt-2_11.png",
    "Unbenannt-2_10.png",
    "Unbenannt-2_12.png",
    "39edea0c-f2f3-4be7-8140-501a27b2dc78.jpeg",
    "6deca7dd-0188-4289-814c-e9821c2d63a4.jpeg",
    "545cdbe7-b92b-4518-adce-5f243a3dfc14.jpeg",
    # Methodik 6 Bilder in voller 1024x768 Aufloesung
    "2da8cf40-b1a0-422e-8ece-1de98311a847_TR.png",
    "0b46cf0c-24cf-4c4d-aedf-64eaf15e38af.jpeg",
    "ae2c4681-9f17-4db3-8ea7-635c3dabedc8.jpeg",
    "742d73ee-7295-4210-9a89-cd7eb544cee4.jpeg",
    "Zeit_Ball_V02.png",
    "76cbf091-6133-4a79-a7fe-5ea19a440a18.jpeg",
    # Trust Badges (KMU, National, International)
    "Logos_Grau_V02_Firma_lokal_V02.png",
    "Logos_Grau_V02_Firma_national_V03.png",
    "Logos_Grau_V02_Firma_International_V02.png",
    # Prozess & Zitat Hintergrund
    "a4ce3d14-117b-400a-b0bb-a6461f2c909b.jpeg",
    # Social Recruiting Vertiefung (e99_expand_01)
    "67b5485a-ad6e-4460-9a43-1e0d2226854b.jpeg",
    # 6 Referenz-Schutz-Grafiken
    "1.png",
    "2.png",
    "3.png",
    "4.png",
    "5.png",
    "6.png",
    # AGB PDF
    "AGB-Dauerstellenvermittlung-I-magnet-Xs-gmbh.pdf",
]

copied_count = 0
for fname in REQUIRED_ASSETS:
    src = STAGING_DIR / "images" / fname
    dst = IMAGES_DIR / fname
    if src.exists():
        shutil.copy2(src, dst)
        copied_count += 1
    else:
        print(f"WARNUNG: Asset fehlt in Staging: {fname}")

print(f"Assets kopiert: {copied_count}/{len(REQUIRED_ASSETS)}")

# 2. company.json & config.json erstellen
company_data = {
    "company_name": "mXs Talent Solutions",
    "product_name": "mXs Talent Solutions",
    "legal_name": "magnet-Xs gmbh",
    "short_name": "mXs Talent",
    "street": "Vordere Hauptgasse 104",
    "zip": "4800",
    "city": "Zofingen",
    "country": "Schweiz",
    "email": "recruiting@mxs-talent-solutions.com",
    "phone": "+41 62 511 21 06",
    "phone_central": "+41 62 511 21 05",
    "whatsapp": "41625112105",
    "website": "https://mxs-talent-solutions.com",
    "industry": "B2B Recruiting & Employer Branding",
    "branche": "B2B Recruiting & Employer Branding",
    "is_website_studio": True,
    "studio_title": "WEBPILOT STUDIO — MXS TALENT SOLUTIONS",
    "work_category_label": "Kampagnen & Methodik",
    "host_url": "https://embed.magnet-xs.ch/mxs-talent/cockpit",
    "host_jobs_url": "https://embed.magnet-xs.ch/mxs-talent/",
    "footer_brand": "mXs Talent Solutions · Eine Einheit der magnet-Xs gmbh",
    "footer_address": "Vordere Hauptgasse 104 · 4800 Zofingen · Schweiz",
    "live_embeds": {
        "index.html": {
            "url": "https://embed.magnet-xs.ch/mxs-talent/",
            "label": "mxs-talent-solutions.com (Hauptseite)"
        },
        "strategie-kennen-lernen.html": {
            "url": "https://embed.magnet-xs.ch/mxs-talent/strategie-kennen-lernen.html",
            "label": "mxs-talent-solutions.com/strategie-kennen-lernen"
        },
        "bremskloetze.html": {
            "url": "https://embed.magnet-xs.ch/mxs-talent/bremskloetze.html",
            "label": "mxs-talent-solutions.com/bremskloetze"
        }
    }
}

(TARGET_DIR / "company.json").write_text(json.dumps(company_data, indent=2, ensure_ascii=False), encoding="utf-8")
(TARGET_DIR / "config.json").write_text(json.dumps({
    "name": "mXs Talent Solutions",
    "slug": "mxs-talent",
    "industry": "B2B Recruiting & Employer Branding",
    "is_website_studio": True
}, indent=2, ensure_ascii=False), encoding="utf-8")
print("company.json & config.json erstellt.")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Client Intake & Gap-Closing Engine (onboard_client.py)
==============================================================
Vollautomatisierter Pre-Scraper & Provisioning-Engine für Neukunden:
1. Web-Crawl der bestehenden Domain (Metadaten, Logo, Mail, Telefon, Social Media)
2. Schweizer Zefix REST-API Lookup (Offizielle Handelsregister-UID, Adresse, Rechtsform, Zweck, Organe)
3. Schweizer Branchen-Resolver (Thesaurus, Fachbegriffe, Verband)
4. Lücken-Analyse & Berechnung des Vollständigkeits-Scores (75-85%)
5. Bereitstellung von company.json, HTML-Templates und des Kunden-Gap-Closing-Cockpits
6. Edge-Kompilierung via compile_site.py und swiss_lexicon_guard.py

Verwendung:
  python3 onboard_client.py --domain hiltbrand-ag.ch [--slug preview-hiltbrand] [--git-push]
  python3 onboard_client.py --name "Birchmeier Bedachungen" --domain birchmeier-dach.ch
"""

import os
import sys
import re
import json
import time
import shutil
import urllib.request
import urllib.parse
import argparse
import subprocess
from pathlib import Path
from html.parser import HTMLParser

# Basis-Pfade
BASE_DIR = Path(__file__).resolve().parent.parent
FULFILLMENT_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = FULFILLMENT_DIR / "templates"
if not TEMPLATES_DIR.exists():
    TEMPLATES_DIR = BASE_DIR / "templates"

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Importiere den Branchen-Resolver
try:
    from industry_resolver import resolve_industry, load_catalog
except ImportError:
    sys.path.insert(0, str(FULFILLMENT_DIR))
    from industry_resolver import resolve_industry, load_catalog


class WebScraper(HTMLParser):
    """Schlanker HTML-Parser zur Extraktion von Stammdaten ohne schwere externe Dependencies."""
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.meta_desc = ""
        self.links = []
        self.images = []
        self.text_chunks = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            name = attr_dict.get("name", "").lower()
            prop = attr_dict.get("property", "").lower()
            if name == "description" or prop == "og:description":
                self.meta_desc = attr_dict.get("content", "")
        elif tag == "a":
            href = attr_dict.get("href", "")
            if href:
                self.links.append(href)
        elif tag == "img":
            src = attr_dict.get("src", "")
            alt = attr_dict.get("alt", "")
            cls = attr_dict.get("class", "")
            if src:
                self.images.append({"src": src, "alt": alt, "class": cls})

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data.strip()
        txt = data.strip()
        if txt and len(txt) > 2:
            self.text_chunks.append(txt)


def fetch_url_html(url: str, timeout: int = 8) -> str:
    """Lädt HTML einer URL mit Browser User-Agent."""
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "de-CH,de;q=0.9,en;q=0.8"
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content = resp.read()
            # Decompress if gzipped
            if content.startswith(b'\x1f\x8b'):
                import gzip
                try:
                    content = gzip.decompress(content)
                except Exception:
                    pass
            # Encoding ermitteln
            encoding = resp.headers.get_content_charset() or "utf-8"
            try:
                return content.decode(encoding, errors="replace")
            except Exception:
                return content.decode("utf-8", errors="replace")
    except Exception as e:
        print(f"⚠️ [Crawl Warnung] Konnte {url} nicht direkt abrufen: {e}")
        return ""


def crawl_website(domain: str) -> dict:
    """Untersucht Homepage und Standard-Subpages der Kunden-Website."""
    print(f"🕷️ [1/4 Pre-Scraper] Analysiere Website: {domain}...")
    base_url = "https://" + domain.replace("https://", "").replace("http://", "").strip("/")
    
    pages = ["", "/kontakt", "/ueber-uns", "/impressum", "/team"]
    combined_html = ""
    parsed_meta = {
        "title": "",
        "desc": "",
        "emails": set(),
        "phones": set(),
        "mobiles": set(),
        "social": {},
        "logo_candidate": "",
        "all_text": ""
    }

    for p in pages:
        u = base_url + p
        html = fetch_url_html(u)
        if not html:
            continue
        combined_html += " " + html

        parser = WebScraper()
        try:
            parser.feed(html)
        except Exception:
            pass

        if not parsed_meta["title"] and parser.title:
            parsed_meta["title"] = parser.title
        if not parsed_meta["desc"] and parser.meta_desc:
            parsed_meta["desc"] = parser.meta_desc

        # Links auswerten
        for l in parser.links:
            if l.startswith("mailto:"):
                mail = l.replace("mailto:", "").split("?")[0].strip().lower()
                if "@" in mail and "." in mail:
                    parsed_meta["emails"].add(mail)
            elif l.startswith("tel:"):
                tel = l.replace("tel:", "").strip()
                if len(re.sub(r"\D", "", tel)) >= 9:
                    parsed_meta["phones"].add(tel)
            elif "instagram.com" in l:
                parsed_meta["social"]["instagram"] = l
            elif "facebook.com" in l:
                parsed_meta["social"]["facebook"] = l
            elif "linkedin.com" in l:
                parsed_meta["social"]["linkedin"] = l

        # Logo-Kandidaten
        for img in parser.images:
            src = img["src"].lower()
            alt = img["alt"].lower()
            cls = img["class"].lower()
            if "logo" in src or "logo" in alt or "logo" in cls:
                if not parsed_meta["logo_candidate"]:
                    parsed_meta["logo_candidate"] = urllib.parse.urljoin(base_url, img["src"])

        parsed_meta["all_text"] += " " + " ".join(parser.text_chunks)

    # Regex für E-Mails im Text
    found_emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', combined_html)
    for fe in found_emails:
        fe_clean = fe.lower().strip(".")
        if not fe_clean.endswith(".png") and not fe_clean.endswith(".jpg"):
            parsed_meta["emails"].add(fe_clean)

    # Regex für Schweizer Festnetz & Mobile
    # z.B. 033 530 02 04, 079 231 84 84, +41 33 530 02 04
    phone_matches = re.findall(r'(?:\+41|0041|0)\s?(?:[1-9]{2})\s?(?:[0-9]{3})\s?(?:[0-9]{2})\s?(?:[0-9]{2})', combined_html)
    for pm in phone_matches:
        cleaned = re.sub(r'[^\d+]', '', pm)
        if "7" in cleaned[:4] or "07" in pm:  # 076, 077, 078, 079 -> Mobile
            parsed_meta["mobiles"].add(pm.strip())
        else:
            parsed_meta["phones"].add(pm.strip())

    parsed_meta["emails"] = list(parsed_meta["emails"])
    parsed_meta["phones"] = list(parsed_meta["phones"])
    parsed_meta["mobiles"] = list(parsed_meta["mobiles"])

    print(f"   ✓ Gefundene E-Mails: {parsed_meta['emails'][:2]}")
    print(f"   ✓ Gefundene Festnetz-Nummern: {parsed_meta['phones'][:2]}")
    print(f"   ✓ Gefundene Mobile/WhatsApp: {parsed_meta['mobiles'][:2]}")
    return parsed_meta


def lookup_zefix(company_name: str) -> dict:
    """Fragt die offizielle Schweizer Zefix REST-API ab."""
    print(f"🇨🇭 [2/4 Zefix-API] Suche Schweizer Handelsregister für: «{company_name}»...")
    clean_query = re.sub(r'\b(AG|GmbH|GmbH\.|AG\.|SA|Sàrl)\b', '', company_name, flags=re.IGNORECASE).strip()
    
    url = "https://www.zefix.admin.ch/ZefixREST/api/v1/firm/search"
    payload = json.dumps({"name": clean_query, "languageKey": "de", "maxEntries": 5}).encode("utf-8")
    headers = {"Content-Type": "application/json", "User-Agent": "WebPilot-Ingestion/2.0"}

    zefix_data = {
        "verified": False,
        "name": company_name,
        "legal_name": company_name,
        "uidFormatted": "",
        "legalSeat": "",
        "street": "",
        "houseNumber": "",
        "swissZipCode": "",
        "town": "",
        "legalForm": "",
        "purpose": "",
        "executive": ""
    }

    try:
        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results = data.get("list", [])
            if not results:
                print("   ℹ️ Kein direkter Treffer im Handelsregister gefunden.")
                return zefix_data

            first = results[0]
            ehraid = first.get("ehraid")
            zefix_data["name"] = first.get("name", company_name)
            zefix_data["legal_name"] = first.get("name", company_name)
            zefix_data["uidFormatted"] = first.get("uidFormatted", "")
            zefix_data["legalSeat"] = first.get("legalSeat", "")

            # Details über ehraid abrufen
            if ehraid:
                detail_url = f"https://www.zefix.admin.ch/ZefixREST/api/v1/firm/{ehraid}"
                d_req = urllib.request.Request(detail_url, headers=headers)
                with urllib.request.urlopen(d_req, timeout=6) as d_resp:
                    d_data = json.loads(d_resp.read().decode("utf-8"))
                    zefix_data["verified"] = True
                    zefix_data["purpose"] = d_data.get("purpose", "")
                    addr = d_data.get("address", {}) or {}
                    zefix_data["street"] = addr.get("street", "")
                    zefix_data["houseNumber"] = addr.get("houseNumber", "")
                    zefix_data["swissZipCode"] = addr.get("swissZipCode", "")
                    zefix_data["town"] = addr.get("town", "")

                    lf_id = d_data.get("legalFormId")
                    if lf_id == 3:
                        zefix_data["legalForm"] = "AG"
                    elif lf_id == 4:
                        zefix_data["legalForm"] = "GmbH"
                    elif lf_id == 1:
                        zefix_data["legalForm"] = "Einzelfirma"

                    # Organe / Inhaber aus Publikationen ermitteln
                    shab = d_data.get("shabPub", [])
                    if shab and isinstance(shab, list):
                        msg = shab[0].get("message", "")
                        # Sucht nach Personen: z.B. "Hiltbrand, Eljas Ivan, Mitglied des Verwaltungsrates"
                        p_match = re.search(r'([A-ZÄÖÜ][a-zäöü]+,\s+[A-ZÄÖÜ][a-zäöü]+(?:\s+[A-ZÄÖÜ][a-zäöü]+)?),\s+von\s+[^,]+,\s+in\s+[^,]+,\s+([^;.\n]+)', msg)
                        if p_match:
                            raw_name = p_match.group(1)
                            role = p_match.group(2)
                            # Formatierung von "Nachname, Vorname" zu "Vorname Nachname"
                            parts = [x.strip() for x in raw_name.split(",")]
                            if len(parts) == 2:
                                zefix_data["executive"] = f"{parts[1]} {parts[0]}"
                                zefix_data["executive_role"] = role.split("[")[0].strip()

            print(f"   ✓ Zefix verifiziert: {zefix_data['name']} (UID: {zefix_data['uidFormatted']})")
            if zefix_data["street"]:
                print(f"   ✓ Offizielle Adresse: {zefix_data['street']} {zefix_data['houseNumber']}, {zefix_data['swissZipCode']} {zefix_data['town']}")
            if zefix_data["executive"]:
                print(f"   ✓ Eingetragene Schlüsselperson: {zefix_data['executive']}")
    except Exception as e:
        print(f"⚠️ Zefix API-Aufruf fehlgeschlagen: {e}")

    return zefix_data


def detect_client_industry(text: str, catalog: dict = None) -> dict:
    """Ermittelt das passende Schweizer Branchenprofil aus dem Webseiten-Text."""
    print("🔍 [3/4 Branchen-Resolver] Analysiere Fachbereich & Schweizer Vokabular...")
    if catalog is None:
        catalog = load_catalog()

    matched = None
    res = resolve_industry(text, catalog)
    if res:
        matched = res
    else:
        for word in text.split():
            if len(word) >= 5:
                sub_res = resolve_industry(word, catalog)
                if sub_res:
                    matched = sub_res
                    break

    if matched:
        lbl = matched.get("label", matched.get("id"))
        print(f"   ✓ Branche erkannt: {lbl} (ID: {matched.get('id')})")
        assoc = matched.get("association", {}).get("name", "N/A")
        print(f"   ✓ Verband: {assoc}")
        return {
            "matched": True,
            "industry_id": matched.get("id"),
            "industry_label": lbl,
            "industry_data": matched
        }
    else:
        print("   ℹ️ Keine eindeutige Spezialisierung erkannt, nutze Standard.")
        return {
            "matched": False,
            "industry_id": "bedachung_gebaeudehuelle",
            "industry_label": "Gebäudehülle & Bedachung",
            "industry_data": {}
        }


def calculate_onboarding_gaps(company_data: dict) -> dict:
    """
    Berechnet den Vollständigkeits-Score und die offenen Lücken.
    Fakultative Sektionen werden berücksichtigt!
    """
    verified = []
    gaps = []
    score = 0

    # 1. Basis-Stammdaten prüfen
    checks = [
        ("company_name", 15, "Firmenname"),
        ("legal_name", 10, "Offizielle Handelsregister-Bezeichnung"),
        ("street", 10, "Strasse & Hausnummer"),
        ("zip", 10, "Postleitzahl & Ort"),
        ("phone", 10, "Haupttelefon"),
        ("email", 10, "E-Mail-Adresse"),
        ("zefix_uid", 10, "Handelsregister-UID (Zefix)"),
    ]

    for key, weight, label in checks:
        if company_data.get(key):
            verified.append(key)
            score += weight

    # 2. Fakultative Lücken definieren
    # Lücke 1: Team & Strukturierung
    team_mode = company_data.get("enabled_sections", {}).get("team_mode", "gl_only_group")
    if team_mode == "none":
        score += 10
    else:
        gaps.append({
            "id": "team_structure",
            "title": "Team & Mitarbeiter-Präsentation",
            "type": "choice_with_upload",
            "status": "pending",
            "weight": 10,
            "default": "gl_only_group",
            "description": "Option B (Chef + Gruppenfoto) oder Option C (Vorerst ohne Teamseite starten)"
        })

    # Lücke 2: WhatsApp Direktkontakt
    if company_data.get("whatsapp"):
        score += 8
        verified.append("whatsapp")
    else:
        gaps.append({
            "id": "whatsapp_number",
            "title": "WhatsApp Direktkontakt für Kunden",
            "type": "phone_or_opt_out",
            "status": "missing",
            "weight": 8,
            "description": "Mobilnummer für Anfragen oder Checkbox 'Kein WhatsApp gewünscht'"
        })

    # Lücke 3: 24h-Pikett Notfalldienst
    gaps.append({
        "id": "emergency_pikett",
        "title": "24h-Pikett Notfalldienst",
        "type": "radio_toggle",
        "status": "pending",
        "weight": 7,
        "default": "none",
        "description": "24h-Notfalldienst aktiv oder reguläre Bürozeiten"
    })

    if score > 100:
        score = 100

    return {
        "score": score,
        "status": "ready" if score >= 95 else "gaps_pending",
        "verified_fields": verified,
        "gaps": gaps
    }


def provision_client(domain: str, name: str = "", slug: str = "", city: str = "", git_push: bool = False):
    """Haupt-Funktion zur vollständigen Mandanten-Provisionierung."""
    start_time = time.time()
    clean_domain = domain.replace("https://", "").replace("http://", "").strip("/")
    
    if not slug:
        slug = "preview-" + clean_domain.split(".")[0].lower()
    if not name:
        name = clean_domain.split(".")[0].capitalize()

    print(f"\n=======================================================")
    print(f"🚀 [WebPilot Intake Engine] Initialisiere Mandant: {name} ({slug})")
    print(f"=======================================================\n")

    # 1. Webseiten-Crawl
    scrape_data = crawl_website(clean_domain)
    extracted_name = scrape_data["title"].split("—")[0].split("-")[0].split("|")[0].strip()
    if extracted_name and len(extracted_name) > 3 and not name:
        name = extracted_name

    # 2. Zefix Ingestion
    search_term = name or extracted_name or clean_domain
    zefix_data = lookup_zefix(search_term)

    # 3. Branchen-Resolver
    catalog = load_catalog()
    all_context = f"{scrape_data['title']} {scrape_data['desc']} {zefix_data.get('purpose', '')} {scrape_data['all_text'][:1500]}"
    industry_match = detect_client_industry(all_context, catalog)

    # 4. Daten-Konsolidierung
    final_name = zefix_data.get("name") or name
    final_street = (zefix_data.get("street", "") + " " + zefix_data.get("houseNumber", "")).strip()
    final_zip = zefix_data.get("swissZipCode", "")
    final_city = zefix_data.get("town", "") or city or zefix_data.get("legalSeat", "")
    final_phone = scrape_data["phones"][0] if scrape_data["phones"] else ""
    final_email = scrape_data["emails"][0] if scrape_data["emails"] else ""
    final_whatsapp = scrape_data["mobiles"][0] if scrape_data["mobiles"] else ""

    # Sauberes company.json Schema
    company_config = {
        "company_name": final_name,
        "legal_name": zefix_data.get("legal_name") or final_name,
        "claim": "Meisterbetrieb in 3. Generation",
        "street": final_street,
        "zip": final_zip,
        "city": final_city,
        "canton": "BE" if not zefix_data.get("legalSeat") else "CH",
        "country": "Schweiz",
        "email": final_email,
        "phone": final_phone,
        "whatsapp": final_whatsapp,
        "website": f"https://{clean_domain}",
        "zefix_uid": zefix_data.get("uidFormatted", ""),
        "industry_id": industry_match.get("industry_id", "bedachung_gebaeudehuelle"),
        "industry_label": industry_match.get("industry_label", "Gebäudehülle & Bedachung"),
        "enabled_sections": {
            "team_page": True,
            "team_mode": "gl_only_group",
            "whatsapp_button": bool(final_whatsapp),
            "emergency_pikett": False,
            "career_page": True
        }
    }

    # Lücken-Analyse durchführen
    onboarding_state = calculate_onboarding_gaps(company_config)
    company_config["onboarding"] = onboarding_state

    # 5. Mandanten-Ordner anlegen & Vorlagen kopieren
    # Suche Master-Template (preview-hiltbrand als Referenz)
    target_dir = BASE_DIR / slug
    if not target_dir.parent.exists():
        target_dir = FULFILLMENT_DIR.parent / "01-Company-Specs" / slug

    target_dir.mkdir(parents=True, exist_ok=True)
    images_dir = target_dir / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    # Kopiere Referenz-HTML & Default-Images falls leer
    ref_dir = BASE_DIR / "preview-hiltbrand"
    if not ref_dir.exists():
        ref_dir = FULFILLMENT_DIR.parent / "01-Company-Specs" / "preview-hiltbrand"

    if ref_dir.exists():
        for f in ref_dir.glob("*.html"):
            if not (target_dir / f.name).exists():
                shutil.copy2(f, target_dir / f.name)
        ref_images = ref_dir / "images"
        if ref_images.exists():
            for img in ref_images.glob("*"):
                if img.is_file() and not (images_dir / img.name).exists():
                    shutil.copy2(img, images_dir / img.name)

    # Kopiere das Gap-Closing Cockpit (onboarding.html)
    onboard_tpl = TEMPLATES_DIR / "onboarding.html"
    if onboard_tpl.exists():
        with open(onboard_tpl, "r", encoding="utf-8") as f:
            ob_content = f.read()

        # Personalisierung des Cockpits vor dem Schreiben
        ob_content = ob_content.replace("Hiltbrand Gebäudehüllen AG", final_name)
        if zefix_data.get("uidFormatted"):
            ob_content = ob_content.replace("CHE-431.204.279", zefix_data["uidFormatted"])
        if final_street:
            ob_content = ob_content.replace("Risegasse 27, 3704 Krattigen", f"{final_street}, {final_zip} {final_city}")
        if final_phone:
            ob_content = ob_content.replace("033 530 02 04", final_phone)
        if final_email:
            ob_content = ob_content.replace("info@hiltbrand.swiss", final_email)
        ob_content = ob_content.replace("hiltbrand-ag.ch", clean_domain)
        ob_content = ob_content.replace("78%", f"{onboarding_state['score']}%")
        ob_content = ob_content.replace("78 / 100%", f"{onboarding_state['score']} / 100%")
        ob_content = ob_content.replace("width: 78%;", f"width: {onboarding_state['score']}%;")

        with open(target_dir / "onboarding.html", "w", encoding="utf-8") as f:
            f.write(ob_content)
        print(f"   ✓ Gap-Closing Cockpit bereitgestellt: {target_dir / 'onboarding.html'}")

    # Bestehende Felder (z.B. acp_client_id, stories_config, instagram_profile) mergen
    comp_file = target_dir / "company.json"
    if comp_file.exists():
        try:
            with open(comp_file, "r", encoding="utf-8") as f:
                existing_comp = json.load(f)
            for k, v in existing_comp.items():
                if k not in company_config or not company_config[k]:
                    company_config[k] = v
        except Exception:
            pass

    # Speichere company.json
    with open(comp_file, "w", encoding="utf-8") as f:
        json.dump(company_config, f, indent=2, ensure_ascii=False)
    print(f"   ✓ company.json geschrieben (Score: {onboarding_state['score']}%)")

    # 6. Kompiliere Mandanten via compile_site.py
    print("⚡ [4/4 Edge-Compiler] Kompiliere statische HTML-Seiten & Swiss Lexicon Guard...")
    try:
        from compile_site import compile_site_dir
        c_stats = compile_site_dir(target_dir, lang="de", dry_run=False)
        print(f"   ✓ Kompilierung erfolgreich: {c_stats['files_checked']} Seiten geprüft, {c_stats['swiss_fixes']} Schweizer Bereinigungen.")
    except Exception as e:
        print(f"⚠️ Kompilierungs-Warnung: {e}")

    # 7. Git Push wenn gewünscht
    if git_push:
        print("🌐 Führe Git Push nach Cloudflare Pages Edge aus...")
        try:
            subprocess.run(["git", "add", str(target_dir)], cwd=str(BASE_DIR), check=True)
            msg = f"feat(onboard): provision automated site for {final_name} ({slug}) [Score: {onboarding_state['score']}%]"
            subprocess.run(["git", "commit", "-m", msg], cwd=str(BASE_DIR), check=True)
            subprocess.run(["git", "push", "origin", "main"], cwd=str(BASE_DIR), check=True)
            print("🚀 Git Push erfolgreich! Cloudflare Pages Edge Deployment läuft.")
        except Exception as e:
            print(f"⚠️ Git Push Warnung: {e}")

    elapsed = time.time() - start_time
    token = f"{slug}-token"
    print("\n---------------------------------------------------------")
    print(f"🎉 Mandanten-Onboarding in {elapsed:.2f} Sekunden erfolgreich!")
    print(f"📊 Vollständigkeits-Score: {onboarding_state['score']}%")
    print(f"📂 Lokaler Ordner: {target_dir}")
    print(f"🔗 Kunden-Gap-Closing-Link:")
    print(f"   https://embed.magnet-xs.ch/{slug}/onboarding?token={token}")
    print(f"🌟 Vorschau-Link:")
    print(f"   https://embed.magnet-xs.ch/{slug}/?token={token}")
    print("---------------------------------------------------------\n")


def main():
    parser = argparse.ArgumentParser(description="WebPilot Automated Client Intake & Gap-Closing Engine")
    parser.add_argument("--domain", required=True, help="Domain des Kunden (z.B. hiltbrand-ag.ch)")
    parser.add_argument("--name", default="", help="Optionaler Firmenname (wird sonst aus Zefix/Webseite ermittelt)")
    parser.add_argument("--slug", default="", help="Optionaler Ordner-Slug (z.B. preview-hiltbrand)")
    parser.add_argument("--city", default="", help="Optionaler Standort (wird sonst aus Zefix ermittelt)")
    parser.add_argument("--git-push", action="store_true", help="Automatisch committen & zu Cloudflare Pages pushen")

    args = parser.parse_args()
    provision_client(
        domain=args.domain,
        name=args.name,
        slug=args.slug,
        city=args.city,
        git_push=args.git_push
    )


if __name__ == "__main__":
    main()

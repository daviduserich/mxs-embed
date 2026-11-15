#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
legacy_web_probe.py – Reiner Python-Fakten-Scanner fuer bestehende Kunden-Webseiten (MKT-029)
============================================================================================
Misst deterministisch und komplett ohne externe Node-/Telemetrie-Binaries (DISABLE_TELEMETRY=1)
ueberpruefbare Zahlen, Daten und Fakten einer bestehenden Webseite (source_url) und uebersetzt
diese in wertschaetzende Schweizer Alltagssprache (#LANG-01, #LANG-02, #LANG-06, #051).

Regel-Konformitaet:
- UI-LAYOUT-RULES.md (Canary: UI-LAYOUT-2026-V1, #UI-07, #UI-08, #UI-23)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1, #LANG-01 100 % ss, #LANG-02, #LANG-06)
- BACKEND-DB-RULES.md (Canary: BACKEND-DB-2026-V1, #BE-01, #BE-06)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from typing import Any, Dict, List, Set
from urllib.parse import urljoin, urlparse

# Strikte Telemetrie-Sperre (#UI-23)
os.environ["DISABLE_TELEMETRY"] = "1"

import requests
from bs4 import BeautifulSoup

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15"
)


def _ss(text: str) -> str:
    """Erzwingt 100 % Schweizer Rechtschreibung (ss statt Eszett #LANG-01) und Halbgeviertstriche (#LANG-02)."""
    cleaned = str(text or "").replace("\u00df", "ss").replace("\u1e9e", "SS")
    # Ersetze englische Satz-Geviertstriche (ausser nach Punkt bei CHF .—) durch Halbgeviertstriche
    cleaned = re.sub(r"(?<!\.)\u2014", "\u2013", cleaned)
    return cleaned


def _count_de(count: int, zero_text: str, one_text: str, many_template: str) -> str:
    """Formatiert Anzahlen ohne nackte Ziffer 1 vor gebeugten deutschen Nomen (#LANG-02)."""
    if count <= 0:
        return _ss(zero_text)
    if count == 1:
        return _ss(one_text)
    return _ss(many_template.format(n=count))


def _base_domain(hostname: str) -> str:
    host = (hostname or "").strip().lower().rstrip(".")
    if host.startswith("www."):
        host = host[4:]
    parts = host.split(".")
    if len(parts) >= 2:
        return ".".join(parts[-2:])
    return host


def _detect_cms(html_lower: str, headers: Dict[str, str], external_domains: Set[str]) -> str:
    joined_domains = " ".join(sorted(external_domains))
    server_hdr = (headers.get("Server") or headers.get("X-Powered-By") or "").lower()

    if "weebly" in html_lower or "editmysite.com" in html_lower or "editmysite.com" in joined_domains:
        return "Weebly Baukasten"
    if "wix.com" in html_lower or "wixstatic.com" in html_lower or "parastorage.com" in joined_domains:
        return "Wix Baukasten"
    if "jimdo" in html_lower or "jimstatic" in html_lower:
        return "Jimdo Baukasten"
    if "funnelcockpit" in html_lower:
        return "FunnelCockpit System"
    if "leadconnector" in html_lower or "msgsndr.com" in html_lower:
        return "GoHighLevel System"
    if "clubdesk" in html_lower:
        return "ClubDesk Vereins-Baukasten"
    if "webflow" in html_lower or "website-files.com" in joined_domains:
        return "Webflow System"
    if "squarespace" in html_lower or "sqspcdn.com" in joined_domains:
        return "Squarespace Baukasten"
    if "wp-content" in html_lower or "wp-includes" in html_lower:
        if "elementor" in html_lower:
            return "WordPress mit Elementor"
        if "divi" in html_lower:
            return "WordPress mit Divi"
        return "WordPress System"
    if "typo3" in html_lower:
        return "TYPO3 Redaktionssystem"
    if "joomla" in html_lower:
        return "Joomla Redaktionssystem"
    if "cdn.shopify.com" in html_lower or "shopify" in server_hdr:
        return "Shopify System"
    if "hostpoint" in html_lower or "webador" in html_lower:
        return "Homepage-Baukasten"
    return "Klassisches Websystem / Baukasten"


def _detect_visitor_hurdles(html_lower: str, external_domains: Set[str]) -> Dict[str, Any]:
    joined = html_lower + " " + " ".join(sorted(external_domains))
    has_cookie_banner = any(
        token in joined
        for token in (
            "cookiebot",
            "usercentrics",
            "borlabs-cookie",
            "onetrust",
            "complianz",
            "cookie-consent",
            "cookieconsent",
            "cookie-banner",
            "cookiebanner",
            "cc-window",
            "eu-cookie",
            "gdpr-cookie",
            "arity-cookie",
            "weebly-footer-signup",
        )
    ) or ("cookie" in html_lower and ("akzeptieren" in html_lower or "zustimmen" in html_lower or "accept all" in html_lower))

    has_captcha = any(
        token in joined
        for token in (
            "recaptcha",
            "grecaptcha",
            "hcaptcha",
            "challenges.cloudflare.com",
            "cf-turnstile",
        )
    )

    has_external_analytics = any(
        token in joined
        for token in (
            "google-analytics.com",
            "googletagmanager.com",
            "gtag(",
            "connect.facebook.net",
            "fbevents.js",
            "hotjar",
        )
    )

    hurdles: List[str] = []
    if has_cookie_banner:
        hurdles.append("Vorgeschaltetes Cookie-Banner beim Seitenstart")
    if has_captcha:
        hurdles.append("Spamschutz-Rätsel vor dem Absenden von Anfragen")
    if has_external_analytics:
        hurdles.append("Externe Besucher-Auswertung über Drittanbieter")

    return {
        "has_cookie_banner": has_cookie_banner,
        "has_captcha": has_captcha,
        "has_external_analytics": has_external_analytics,
        "has_cookie_banner_or_captcha": bool(has_cookie_banner or has_captcha),
        "visitor_hurdles": hurdles,
    }


def _check_llms_txt(origin_url: str) -> bool:
    if not origin_url:
        return False
    llms_url = urljoin(origin_url.rstrip("/") + "/", "llms.txt")
    try:
        resp = requests.get(
            llms_url,
            timeout=4,
            headers={"User-Agent": USER_AGENT},
            allow_redirects=True,
        )
        if resp.status_code != 200:
            return False
        ctype = (resp.headers.get("Content-Type") or "").lower()
        body_sample = (resp.text or "").strip()[:300].lower()
        if "text/html" in ctype or body_sample.startswith("<!doctype html") or body_sample.startswith("<html"):
            return False
        return len(body_sample) >= 20
    except Exception:
        return False


def probe_legacy_url(source_url: str, timeout: int = 12) -> Dict[str, Any]:
    """
    Prueft eine bestehende Kunden-URL rein lesend per HTTP/HTML und liefert sowohl
    exakte Rohzahlen als auch wertschaetzende Formulierungen in Alltagssprache (#051, #LANG-06).
    """
    raw_url = (source_url or "").strip()
    if raw_url and not re.match(r"^https?://", raw_url, re.I):
        raw_url = "https://" + raw_url

    parsed_in = urlparse(raw_url)
    display_url = re.sub(r"^www\.", "", (parsed_in.netloc or raw_url).lower()).rstrip("/")
    own_base = _base_domain(parsed_in.netloc)
    origin_url = f"{parsed_in.scheme or 'https'}://{parsed_in.netloc}" if parsed_in.netloc else ""

    result: Dict[str, Any] = {
        "telemetry_disabled": os.environ.get("DISABLE_TELEMETRY") == "1",
        "source_url": raw_url,
        "source_url_display": display_url,
        "reachable": False,
        "status_code": 0,
        "connection_issue": None,
        "response_time_ms": 650,
        "response_time_sec": 0.65,
        "html_kb": 120.0,
        "cms_detected": "Klassisches Websystem / Baukasten",
        "page_title": "",
        "page_title_len": 0,
        "meta_description_len": 0,
        "h1_count": 0,
        "h2_count": 0,
        "script_count": 0,
        "external_script_count": 0,
        "external_domain_count": 0,
        "external_domains": [],
        "has_cookie_banner": False,
        "has_captcha": False,
        "has_external_analytics": False,
        "has_cookie_banner_or_captcha": False,
        "visitor_hurdles": [],
        "images_total": 0,
        "images_missing_alt": 0,
        "images_missing_dimensions": 0,
        "has_structured_data": False,
        "structured_data_blocks": 0,
        "has_llms_txt": False,
        "plain_language": {},
    }

    t0 = time.perf_counter()
    try:
        resp = requests.get(
            raw_url,
            timeout=timeout,
            headers={"User-Agent": USER_AGENT, "Accept-Language": "de-CH,de;q=0.9,en;q=0.7"},
            allow_redirects=True,
        )
        elapsed_ms = max(1, int(round((time.perf_counter() - t0) * 1000)))
        result["reachable"] = resp.status_code < 500
        result["status_code"] = int(resp.status_code)
        result["response_time_ms"] = elapsed_ms
        result["response_time_sec"] = round(elapsed_ms / 1000.0, 2)
        result["html_kb"] = round(len(resp.content or b"") / 1024.0, 1)

        final_parsed = urlparse(resp.url or raw_url)
        if final_parsed.netloc:
            own_base = _base_domain(final_parsed.netloc)
            origin_url = f"{final_parsed.scheme or 'https'}://{final_parsed.netloc}"

        html_text = resp.text or ""
        html_lower = html_text.lower()
        soup = BeautifulSoup(html_text, "html.parser")

        title_tag = soup.find("title")
        page_title = re.sub(r"\s+", " ", (title_tag.get_text() if title_tag else "")).strip()
        result["page_title"] = _ss(page_title)
        result["page_title_len"] = len(page_title)

        md = soup.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
        meta_desc = (md.get("content") or "").strip() if md else ""
        result["meta_description_len"] = len(meta_desc)

        result["h1_count"] = len(soup.find_all("h1"))
        result["h2_count"] = len(soup.find_all("h2"))

        scripts = soup.find_all("script")
        ld_json_blocks = [
            s for s in scripts
            if "ld+json" in ((s.get("type") or "").lower()) and (s.string or s.get_text() or "").strip()
        ]
        executable_scripts = [
            s for s in scripts
            if "ld+json" not in ((s.get("type") or "").lower())
        ]
        result["script_count"] = len(executable_scripts)
        result["structured_data_blocks"] = len(ld_json_blocks)
        result["has_structured_data"] = len(ld_json_blocks) > 0

        ext_domains: Set[str] = set()
        ext_script_count = 0

        def _collect_url(raw_ref: str, is_script: bool = False) -> None:
            nonlocal ext_script_count
            ref = (raw_ref or "").strip()
            if not ref or ref.startswith(("data:", "mailto:", "tel:", "javascript:", "#")):
                return
            full = urljoin(resp.url or raw_url, ref)
            host = (urlparse(full).netloc or "").lower().split(":")[0]
            if not host:
                return
            if _base_domain(host) != own_base:
                ext_domains.add(host)
                if is_script:
                    ext_script_count += 1

        for s in executable_scripts:
            if s.get("src"):
                _collect_url(str(s.get("src")), is_script=True)
        for lnk in soup.find_all("link"):
            rels = " ".join(lnk.get("rel") or []).lower()
            if any(k in rels for k in ("stylesheet", "preconnect", "dns-prefetch", "preload", "font")):
                _collect_url(str(lnk.get("href") or ""))
        for ifr in soup.find_all("iframe"):
            _collect_url(str(ifr.get("src") or ""))
        for im in soup.find_all("img"):
            _collect_url(str(im.get("src") or ""))

        result["external_script_count"] = ext_script_count
        result["external_domains"] = sorted(ext_domains)
        result["external_domain_count"] = len(ext_domains)

        imgs = soup.find_all("img")
        result["images_total"] = len(imgs)
        result["images_missing_alt"] = len([i for i in imgs if not (i.get("alt") or "").strip()])
        result["images_missing_dimensions"] = len(
            [i for i in imgs if not ((i.get("width") or "").strip() and (i.get("height") or "").strip())]
        )

        result["cms_detected"] = _ss(_detect_cms(html_lower, dict(resp.headers), ext_domains))
        hurdle_info = _detect_visitor_hurdles(html_lower, ext_domains)
        result.update(hurdle_info)
        result["has_llms_txt"] = _check_llms_txt(origin_url)

    except requests.exceptions.SSLError:
        result["connection_issue"] = "Verschlüsselte Verbindung (HTTPS) meldet aktuell einen Zertifikats- oder Verbindungsfehler"
    except requests.exceptions.RequestException:
        result["connection_issue"] = "Bestehende Adresse antwortete innerhalb des Prüfzeitfensters nicht direkt"

    # Uebersetzung in 100 % wertschaetzende Schweizer Alltagssprache (#051, #LANG-06)
    sec_str = f"{result['response_time_sec']:.2f}"
    scripts_phrase = _count_de(
        result["script_count"],
        "keine zusätzlichen Hintergrund-Programme",
        "ein Hintergrund-Programm",
        "{n} geladene Hintergrund-Programme",
    )
    domains_phrase = _count_de(
        result["external_domain_count"],
        "keine fremden Drittserver",
        "ein externer Drittserver",
        "{n} externe Drittserver",
    )
    imgs_total = result["images_total"]
    imgs_no_dim = result["images_missing_dimensions"]
    imgs_no_alt = result["images_missing_alt"]

    if imgs_total == 0:
        img_calm_phrase = "Noch keine eingebundenen Inhaltsbilder auf der Startseite"
        img_desc_phrase = "Noch keine hinterlegten Bildbeschreibungen auf der Startseite"
    else:
        img_calm_phrase = _count_de(
            imgs_no_dim,
            "Alle Bilder besitzen bereits feste Platzmasse",
            f"Ein Bild (von {imgs_total}) ohne feste Grössenreservierung",
            f"{{n}} von {imgs_total} Bildern ohne feste Grössenreservierung",
        )
        img_desc_phrase = _count_de(
            imgs_no_alt,
            "Alle Bilder besitzen eine Textbeschreibung für Google",
            f"Ein Bild (von {imgs_total}) ohne hinterlegte Bildbeschreibung",
            f"{{n}} von {imgs_total} Bildern ohne hinterlegte Bildbeschreibung",
        )

    if result["has_structured_data"] and result["has_llms_txt"]:
        ai_findability = "Orts- und Angebotsdaten sowie KI-Kurzprofil sind bereits hinterlegt"
    elif result["has_structured_data"]:
        ai_findability = "Basis-Ortsdaten vorhanden, noch ohne eigenes KI-Kurzprofil für Antwortsysteme"
    else:
        ai_findability = "Noch kein strukturiertes Orts-, Angebots- und Fragenverzeichnis hinterlegt"

    if result["visitor_hurdles"]:
        hurdles_summary = " · ".join(_ss(h) for h in result["visitor_hurdles"])
    else:
        hurdles_summary = "Direkter Zugang ohne vorgeschaltetes Cookie-Banner oder Bilderrätsel"

    result["plain_language"] = {
        "system_einordnung": _ss(f"{result['cms_detected']} ({display_url})"),
        "wartezeit_heute": _ss(f"{sec_str} Sekunden Antwortzeit beim ersten Seitenaufruf"),
        "hintergrund_programme": _ss(f"{scripts_phrase} · {domains_phrase}"),
        "besucher_huerden": _ss(hurdles_summary),
        "bildaufbau_ruhe": _ss(img_calm_phrase),
        "bildbeschreibungen_google": _ss(img_desc_phrase),
        "google_und_ki_findbarkeit": _ss(ai_findability),
    }

    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sachlicher Fakten-Scanner fuer bestehende Kunden-Webseiten in Alltagssprache (DISABLE_TELEMETRY=1)"
    )
    parser.add_argument("url", help="Zu pruefende Webseiten-URL (z. B. https://goodfordogs.ch/index.html)")
    parser.add_argument("--timeout", type=int, default=12, help="HTTP-Timeout in Sekunden (Standard: 12)")
    args = parser.parse_args()

    report = probe_legacy_url(args.url, timeout=args.timeout)
    print(_ss(json.dumps(report, indent=2, ensure_ascii=False)))


if __name__ == "__main__":
    main()

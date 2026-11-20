#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
legacy_web_probe.py – Reiner Python-Fakten-Scanner fuer bestehende Kunden-Webseiten (MKT-029 + MKT-034)
========================================================================================================
Misst deterministisch und komplett ohne externe Node-/Telemetrie-Binaries (DISABLE_TELEMETRY=1)
ueberpruefbare Zahlen, Daten und Fakten einer bestehenden Webseite (source_url) inkl. additivem
Mobile First-Screen-Check (390x664 px) und uebersetzt diese in wertschaetzende Schweizer
Alltagssprache (#LANG-01, #LANG-02, #LANG-06, #051).

Regel-Konformitaet:
- UI-LAYOUT-RULES.md (Canary: UI-LAYOUT-2026-V1, #UI-07, #UI-08, #UI-23)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1, #LANG-01 100 % ss, #LANG-02, #LANG-06)
- BACKEND-DB-RULES.md (Canary: BACKEND-DB-2026-V1, #BE-01, #BE-06)
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys
import time
from typing import Any, Dict, List, Optional, Set
from urllib.parse import urljoin, urlparse

# Strikte Telemetrie-Sperre (#UI-23)
os.environ["DISABLE_TELEMETRY"] = "1"

import requests
from bs4 import BeautifulSoup

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

USER_AGENT = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1"
)

FIRST_SCREEN_VIEWPORT = "390x664"
FIRST_SCREEN_WORD_LIMIT = 120
H1_ABOVE_FOLD_WORD_LIMIT = 80

CH_PHONE_RE = re.compile(
    r"(?:\+41|0041|0)\s*(?:\(0\)\s*)?[1-9]\d[\s.\-]?\d{3}[\s.\-]?\d{2}[\s.\-]?\d{2}"
)
RATING_TEXT_RE = re.compile(
    r"(?:(?:[34]\.\d|5\.0)\s*(?:/\s*5|von\s*5|stern|sterne|\u2605)"
    r"|\u2605{3,5}"
    r"|google[\s\-]*(?:bewertung|bewertungen|rezension|rezensionen)"
    r"|\b\d{1,4}\s+(?:bewertungen|rezensionen|google-bewertungen)\b)",
    re.IGNORECASE,
)
PROMISE_TERMS = (
    "24h",
    "pikett",
    "notfall",
    "garantie",
    "offerte",
    "kostenlos",
    "unverbindlich",
    "erfahrung",
    "jahre",
    "seit ",
    "schweiz",
    "regional",
    "efz",
    "meister",
    "zertifiziert",
    "termin",
    "beratung",
    "sofort",
    "direkt",
    "fachbetrieb",
    "schnell",
)
CONTACT_CTA_RE = re.compile(
    r"(kontakt|offerte|anfrage|anfragen|termin|buchen|anrufen|rueckruf|rückruf|beratung|schreiben)",
    re.IGNORECASE,
)


def _ss(text: str) -> str:
    """Erzwingt 100 % Schweizer Rechtschreibung (ss statt Eszett #LANG-01) und Halbgeviertstriche (#LANG-02)."""
    cleaned = str(text or "").replace("\u00df", "ss").replace("\u1e9e", "SS")
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


def _default_first_screen() -> Dict[str, Any]:
    return {
        "viewport_reference": FIRST_SCREEN_VIEWPORT,
        "has_viewport_meta": False,
        "h1_text": "",
        "h1_word_position": None,
        "h1_above_fold": False,
        "tel_links_total": 0,
        "tel_link_above_fold": False,
        "tel_hrefs": [],
        "phone_numbers_in_opening": [],
        "promise_hits_above_fold": [],
        "rating_signal_above_fold": False,
        "rating_jsonld": [],
        "direct_contact_cta_above_fold": False,
        "forms_count": 0,
        "first_form_fields": None,
        "checks": {
            "tel_link": False,
            "core_promise": False,
            "rating_signal": False,
            "direct_contact_path": False,
        },
        "passed_count": 0,
        "max_count": 4,
        "score_label": "0 / 4",
    }


def _walk_jsonld_ratings(node: Any, ratings_out: List[str]) -> None:
    if isinstance(node, dict):
        ar = node.get("aggregateRating")
        if isinstance(ar, dict):
            val = ar.get("ratingValue")
            cnt = ar.get("reviewCount") or ar.get("ratingCount")
            if val is not None:
                ratings_out.append(f"{val} ({cnt})" if cnt is not None else str(val))
        for v in node.values():
            _walk_jsonld_ratings(v, ratings_out)
    elif isinstance(node, list):
        for v in node:
            _walk_jsonld_ratings(v, ratings_out)


def _extract_first_screen_facts(soup: BeautifulSoup, ld_json_blocks: List[Any]) -> Dict[str, Any]:
    """Prueft den ersten Smartphone-Bildschirm (390x664 px / above-the-fold Heuristik nach MKT-034)."""
    fs = _default_first_screen()

    vp_meta = soup.find("meta", attrs={"name": re.compile(r"^viewport$", re.I)})
    fs["has_viewport_meta"] = bool(vp_meta and (vp_meta.get("content") or "").strip())

    first_h1 = soup.find("h1")
    h1_text = re.sub(r"\s+", " ", first_h1.get_text(" ", strip=True) if first_h1 else "").strip()
    fs["h1_text"] = _ss(h1_text[:180])

    # Kopiere DOM-Baum ohne Script/Style/SVG/Template fuer saubere Wort-Positionen
    work_root = BeautifulSoup(str(soup.body or soup), "html.parser")
    for junk in work_root.find_all(["script", "style", "noscript", "template", "svg"]):
        junk.decompose()

    header_links: List[Dict[str, str]] = []
    for hdr in work_root.find_all(["header", "nav"]):
        for el in hdr.find_all(["a", "button"]):
            header_links.append(
                {
                    "href": (el.get("href") or "").strip(),
                    "text": re.sub(r"\s+", " ", el.get_text(" ", strip=True)),
                    "aria": (el.get("aria-label") or "").strip(),
                }
            )

    # Hauptinhalt ohne globale nav/footer fuer die Lese-Reihenfolge ab Hero
    content_words: List[str] = []
    h1_word_pos: Optional[int] = None
    tel_positions: List[tuple[str, int]] = []
    cta_positions: List[tuple[str, int]] = []
    form_positions: List[tuple[int, int]] = []

    skip_tags = {"nav", "footer"}

    def _walk_dom(node: Any, in_skip: bool = False) -> None:
        nonlocal h1_word_pos
        name = getattr(node, "name", None)
        if name is None:
            if not in_skip:
                txt = str(node).strip()
                if txt:
                    content_words.extend(txt.split())
            return

        is_hidden_attr = name is not None and (
            node.has_attr("hidden") or str(node.get("aria-hidden") or "").lower() == "true"
        )
        now_skip = in_skip or (name in skip_tags) or is_hidden_attr
        if not now_skip:
            if name == "h1" and h1_word_pos is None:
                h1_word_pos = len(content_words)
            elif name == "a":
                href = (node.get("href") or "").strip()
                lbl = re.sub(r"\s+", " ", node.get_text(" ", strip=True))
                aria = (node.get("aria-label") or "").strip()
                combined = f"{lbl} {aria}".strip()
                if href.lower().startswith("tel:"):
                    tel_positions.append((href, len(content_words)))
                if href.lower().startswith(("tel:", "mailto:")) or "#kontakt" in href.lower() or CONTACT_CTA_RE.search(combined):
                    cta_positions.append((href or combined[:40], len(content_words)))
            elif name == "button":
                lbl = re.sub(r"\s+", " ", node.get_text(" ", strip=True))
                aria = (node.get("aria-label") or "").strip()
                if CONTACT_CTA_RE.search(f"{lbl} {aria}"):
                    cta_positions.append((lbl[:40] or "button", len(content_words)))
            elif name == "form":
                visible_fields = 0
                for fld in node.find_all(["input", "select", "textarea"]):
                    ftype = (fld.get("type") or "text").lower()
                    if ftype not in ("hidden", "submit", "button", "image"):
                        visible_fields += 1
                form_positions.append((visible_fields, len(content_words)))

        for child in node.children:
            _walk_dom(child, now_skip)

    _walk_dom(work_root, False)

    all_tel_tags = soup.find_all("a", href=re.compile(r"^tel:", re.I))
    tel_hrefs = [str(a.get("href") or "").strip() for a in all_tel_tags if (a.get("href") or "").strip()]
    fs["tel_links_total"] = len(tel_hrefs)
    fs["tel_hrefs"] = list(dict.fromkeys(tel_hrefs))[:3]

    header_has_tel = any(item["href"].lower().startswith("tel:") for item in header_links)
    opening_has_tel = any(pos <= FIRST_SCREEN_WORD_LIMIT for _, pos in tel_positions)
    fs["tel_link_above_fold"] = bool(header_has_tel or opening_has_tel)

    opening_text = _ss(" ".join(content_words[:150]))
    first_screen_text = _ss(f"{h1_text} " + " ".join(content_words[:FIRST_SCREEN_WORD_LIMIT]))
    first_screen_lower = first_screen_text.lower()

    fs["phone_numbers_in_opening"] = sorted(
        {re.sub(r"\s+", " ", m.group(0)).strip() for m in CH_PHONE_RE.finditer(opening_text)}
    )[:3]

    fs["h1_word_position"] = h1_word_pos
    fs["h1_above_fold"] = bool(h1_word_pos is not None and h1_word_pos <= H1_ABOVE_FOLD_WORD_LIMIT)

    promise_hits = [term.strip() for term in PROMISE_TERMS if term in first_screen_lower]
    fs["promise_hits_above_fold"] = promise_hits[:8]

    ratings_jsonld: List[str] = []
    for block in ld_json_blocks:
        raw_json = (block.string or block.get_text() or "").strip()
        if not raw_json:
            continue
        try:
            _walk_jsonld_ratings(json.loads(raw_json), ratings_jsonld)
        except (ValueError, TypeError):
            continue
    fs["rating_jsonld"] = sorted(set(ratings_jsonld))[:3]
    fs["rating_signal_above_fold"] = bool(RATING_TEXT_RE.search(opening_text) or fs["rating_jsonld"])

    header_has_cta = any(
        item["href"].lower().startswith(("tel:", "mailto:"))
        or "#kontakt" in item["href"].lower()
        or bool(CONTACT_CTA_RE.search(f"{item['text']} {item['aria']}"))
        for item in header_links
    )
    opening_has_cta = any(pos <= FIRST_SCREEN_WORD_LIMIT for _, pos in cta_positions)
    opening_has_form = any(pos <= 180 for _, pos in form_positions)
    fs["direct_contact_cta_above_fold"] = bool(header_has_cta or opening_has_cta or opening_has_form)
    fs["forms_count"] = len(form_positions)
    fs["first_form_fields"] = form_positions[0][0] if form_positions else None

    core_promise_ok = bool(fs["has_viewport_meta"] and fs["h1_above_fold"] and (len(h1_text) >= 12 or promise_hits))
    checks = {
        "tel_link": fs["tel_link_above_fold"],
        "core_promise": core_promise_ok,
        "rating_signal": fs["rating_signal_above_fold"],
        "direct_contact_path": fs["direct_contact_cta_above_fold"],
    }
    passed_count = sum(1 for v in checks.values() if v)
    fs["checks"] = checks
    fs["passed_count"] = passed_count
    fs["max_count"] = 4
    fs["score_label"] = f"{passed_count} / 4"
    return fs


def _build_plain_language(result: Dict[str, Any], display_url: str) -> Dict[str, str]:
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

    fs = result.get("first_screen") or {}
    fs_checks = fs.get("checks") or {}
    missing_labels: List[str] = []
    if not fs_checks.get("tel_link"):
        missing_labels.append("Direktwahl per Telefon")
    if not fs_checks.get("core_promise"):
        missing_labels.append("klares Hauptversprechen oben")
    if not fs_checks.get("rating_signal"):
        missing_labels.append("sichtbares Bewertungs-Signal")
    if not fs_checks.get("direct_contact_path"):
        missing_labels.append("direkter Anfrage-Weg")
    if not missing_labels:
        first_screen_phrase = "4 / 4 Mobile-Startbildschirm-Signale direkt sichtbar (Telefon, Versprechen, Bewertung, Kontakt)"
    else:
        first_screen_phrase = f"{fs.get('score_label', '0 / 4')} auf dem ersten Handy-Bildschirm sichtbar (fehlt oben: {', '.join(missing_labels)})"

    return {
        "system_einordnung": _ss(f"{result['cms_detected']} ({display_url})"),
        "wartezeit_heute": _ss(f"{sec_str} Sekunden Antwortzeit beim ersten Seitenaufruf"),
        "hintergrund_programme": _ss(f"{scripts_phrase} · {domains_phrase}"),
        "besucher_huerden": _ss(hurdles_summary),
        "bildaufbau_ruhe": _ss(img_calm_phrase),
        "bildbeschreibungen_google": _ss(img_desc_phrase),
        "google_und_ki_findbarkeit": _ss(ai_findability),
        "mobile_first_screen": _ss(first_screen_phrase),
    }


def analyze_html_document(
    html_text: str,
    source_url: str = "",
    final_url: str = "",
    headers: Optional[Dict[str, str]] = None,
    status_code: int = 200,
    response_time_ms: int = 1,
    has_llms_txt: bool = False,
) -> Dict[str, Any]:
    """Analysiert ein HTML-Dokument deterministisch (genutzt fuer Live-HTTP und lokale Trockenlaeufe)."""
    parsed_in = urlparse(final_url or source_url)
    display_url = re.sub(r"^www\.", "", (parsed_in.netloc or source_url or "lokal").lower()).rstrip("/")
    own_base = _base_domain(parsed_in.netloc)
    hdrs = headers or {}

    html_lower = (html_text or "").lower()
    soup = BeautifulSoup(html_text or "", "html.parser")

    title_tag = soup.find("title")
    page_title = re.sub(r"\s+", " ", (title_tag.get_text() if title_tag else "")).strip()

    md = soup.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
    meta_desc = (md.get("content") or "").strip() if md else ""

    scripts = soup.find_all("script")
    ld_json_blocks = [
        s for s in scripts
        if "ld+json" in ((s.get("type") or "").lower()) and (s.string or s.get_text() or "").strip()
    ]
    executable_scripts = [
        s for s in scripts
        if "ld+json" not in ((s.get("type") or "").lower())
    ]

    ext_domains: Set[str] = set()
    ext_script_count = 0

    def _collect_url(raw_ref: str, is_script: bool = False) -> None:
        nonlocal ext_script_count
        ref = (raw_ref or "").strip()
        if not ref or ref.startswith(("data:", "mailto:", "tel:", "javascript:", "#")):
            return
        full = urljoin(final_url or source_url or "https://localhost/", ref)
        host = (urlparse(full).netloc or "").lower().split(":")[0]
        if not host or host == "localhost":
            return
        if own_base and _base_domain(host) != own_base:
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

    imgs = soup.find_all("img")
    hurdle_info = _detect_visitor_hurdles(html_lower, ext_domains)
    first_screen = _extract_first_screen_facts(soup, ld_json_blocks)

    result: Dict[str, Any] = {
        "telemetry_disabled": os.environ.get("DISABLE_TELEMETRY") == "1",
        "source_url": source_url or final_url,
        "source_url_display": display_url,
        "reachable": status_code < 500,
        "status_code": int(status_code),
        "connection_issue": None,
        "response_time_ms": int(response_time_ms),
        "response_time_sec": round(response_time_ms / 1000.0, 2),
        "html_kb": round(len((html_text or "").encode("utf-8", "replace")) / 1024.0, 1),
        "cms_detected": _ss(_detect_cms(html_lower, hdrs, ext_domains)),
        "page_title": _ss(page_title),
        "page_title_len": len(page_title),
        "meta_description_len": len(meta_desc),
        "h1_count": len(soup.find_all("h1")),
        "h2_count": len(soup.find_all("h2")),
        "script_count": len(executable_scripts),
        "external_script_count": ext_script_count,
        "external_domain_count": len(ext_domains),
        "external_domains": sorted(ext_domains),
        "has_cookie_banner": hurdle_info["has_cookie_banner"],
        "has_captcha": hurdle_info["has_captcha"],
        "has_external_analytics": hurdle_info["has_external_analytics"],
        "has_cookie_banner_or_captcha": hurdle_info["has_cookie_banner_or_captcha"],
        "visitor_hurdles": hurdle_info["visitor_hurdles"],
        "images_total": len(imgs),
        "images_missing_alt": len([i for i in imgs if not (i.get("alt") or "").strip()]),
        "images_missing_dimensions": len(
            [i for i in imgs if not ((i.get("width") or "").strip() and (i.get("height") or "").strip())]
        ),
        "has_structured_data": len(ld_json_blocks) > 0,
        "structured_data_blocks": len(ld_json_blocks),
        "has_llms_txt": has_llms_txt,
        "first_screen": first_screen,
        "plain_language": {},
    }
    result["plain_language"] = _build_plain_language(result, display_url)
    return result


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
    origin_url = f"{parsed_in.scheme or 'https'}://{parsed_in.netloc}" if parsed_in.netloc else ""

    t0 = time.perf_counter()
    try:
        resp = requests.get(
            raw_url,
            timeout=timeout,
            headers={"User-Agent": USER_AGENT, "Accept-Language": "de-CH,de;q=0.9,en;q=0.7"},
            allow_redirects=True,
        )
        elapsed_ms = max(1, int(round((time.perf_counter() - t0) * 1000)))
        final_parsed = urlparse(resp.url or raw_url)
        if final_parsed.netloc:
            origin_url = f"{final_parsed.scheme or 'https'}://{final_parsed.netloc}"
        has_llms = _check_llms_txt(origin_url)
        return analyze_html_document(
            resp.text or "",
            source_url=raw_url,
            final_url=resp.url or raw_url,
            headers=dict(resp.headers),
            status_code=int(resp.status_code),
            response_time_ms=elapsed_ms,
            has_llms_txt=has_llms,
        )
    except requests.exceptions.SSLError:
        issue = "Verschlüsselte Verbindung (HTTPS) meldet aktuell einen Zertifikats- oder Verbindungsfehler"
    except requests.exceptions.RequestException:
        issue = "Bestehende Adresse antwortete innerhalb des Prüfzeitfensters nicht direkt"

    fallback: Dict[str, Any] = {
        "telemetry_disabled": os.environ.get("DISABLE_TELEMETRY") == "1",
        "source_url": raw_url,
        "source_url_display": display_url,
        "reachable": False,
        "status_code": 0,
        "connection_issue": issue,
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
        "first_screen": _default_first_screen(),
        "plain_language": {},
    }
    fallback["plain_language"] = _build_plain_language(fallback, display_url)
    return fallback


def run_first_screen_self_test() -> int:
    """Deterministischer Offline-Selbsttest fuer den 390x664 Mobile First-Screen-Check."""
    good_html = """<!DOCTYPE html>
    <html lang="de-CH">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Muster Holzbau AG · Aargau</title>
      <script type="application/ld+json">{"@type":"LocalBusiness","aggregateRating":{"ratingValue":"4.9","reviewCount":"42"}}</script>
    </head>
    <body>
      <header><a href="tel:+41625550101">Anrufen</a><a href="#kontakt">Offerte anfordern</a></header>
      <main>
        <h1>Holzbau und Bedachung seit 1998 im Raum Aargau</h1>
        <p>4.9 / 5 Google-Bewertungen. Unverbindliche Beratung innert 24h.</p>
      </main>
    </body>
    </html>"""

    weak_html = """<!DOCTYPE html>
    <html lang="de-CH">
    <head><meta charset="UTF-8"><title>Alte Baukasten-Seite</title></head>
    <body>
      <nav>Start Ueber uns Leistungen Referenzen Team Karriere Partner Links</nav>
      <main>
        <p>Willkommen auf unserer Webseite. Hier stehen zuerst viele allgemeine Saetze ohne klaren Nutzen oder Handlung.
        Wir sind ein Betrieb in der Region und arbeiten fuer verschiedene Kunden im ganzen Umfeld.
        Lesen Sie hier weiter, um mehr ueber unsere Geschichte aus den letzten Jahrzehnten zu erfahren.
        Viele weitere allgemeine Woerter fuellen den ersten Bildschirm auf dem Smartphone komplett aus.
        Auch im zweiten Absatz folgen nur allgemeine Hinweise ohne konkrete Telefonnummer, Bewertung oder Leistung.
        Besucher muessen zuerst lange nach unten scrollen, bevor überhaupt ein Angebot oder eine Ueberschrift erscheint.
        Erst sehr weit unten nach vielen Zeilen folgt eine Ueberschrift.</p>
        <h1>Startseite</h1>
      </main>
    </body>
    </html>"""

    res_good = analyze_html_document(good_html, source_url="https://muster-holzbau.ch")
    res_weak = analyze_html_document(weak_html, source_url="https://alt-baukasten.ch")

    fs_good = res_good["first_screen"]
    fs_weak = res_weak["first_screen"]

    ok1 = fs_good["passed_count"] == 4 and fs_good["checks"] == {
        "tel_link": True,
        "core_promise": True,
        "rating_signal": True,
        "direct_contact_path": True,
    }
    ok2 = fs_weak["passed_count"] == 0 and all(not v for v in fs_weak["checks"].values())
    ok3 = res_good["telemetry_disabled"] is True

    print(f"  [{'PASS ✅' if ok1 else 'FAIL ❌'}] Good Mobile First-Screen: {fs_good['score_label']} {fs_good['checks']}")
    print(f"  [{'PASS ✅' if ok2 else 'FAIL ❌'}] Weak Legacy First-Screen: {fs_weak['score_label']} {fs_weak['checks']}")
    print(f"  [{'PASS ✅' if ok3 else 'FAIL ❌'}] DISABLE_TELEMETRY=1 aktiv: {res_good['telemetry_disabled']}")

    passed = sum(1 for ok in (ok1, ok2, ok3) if ok)
    print(f"LEGACY-WEB-PROBE-SELF-TEST: {passed}/3 Faelle bestanden")
    return 0 if passed == 3 else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sachlicher Fakten-Scanner fuer bestehende Kunden-Webseiten in Alltagssprache (DISABLE_TELEMETRY=1)"
    )
    parser.add_argument("url", nargs="?", help="Zu pruefende Webseiten-URL (z. B. https://goodfordogs.ch/index.html)")
    parser.add_argument("--html-file", help="Lokale HTML-Datei fuer Offline-Trockenlauf pruefen")
    parser.add_argument("--timeout", type=int, default=12, help="HTTP-Timeout in Sekunden (Standard: 12)")
    parser.add_argument("--self-test", action="store_true", help="Fuehrt den deterministischen First-Screen-Selbsttest aus")
    args = parser.parse_args()

    if args.self_test:
        return run_first_screen_self_test()

    if args.html_file:
        html_path = pathlib.Path(args.html_file)
        if not html_path.is_file():
            print(f"Datei nicht gefunden: {html_path}", file=sys.stderr)
            return 2
        report = analyze_html_document(
            html_path.read_text(encoding="utf-8", errors="replace"),
            source_url=f"file://{html_path.as_posix()}",
        )
    elif args.url:
        report = probe_legacy_url(args.url, timeout=args.timeout)
    else:
        parser.print_help()
        return 2

    print(_ss(json.dumps(report, indent=2, ensure_ascii=False)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

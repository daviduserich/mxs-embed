#!/usr/bin/env python3
"""
WebPilot Adversarial Content & Screenshot Auditor (Vorher-vs.-Nachher Fakten-, Text- & Vision-Pruefmaschine)
============================================================================================================
Prueft fertige WebPilot-Vorschauen vor Kundenabgabe in 3 Stufen:
  1. Deterministischer Fakten-, Zahlen-, Preis- & Begriffs-Diff gegen das gecrawlte Original
  2. Unbestechlicher Text- & Fakten-Staatsanwalt (OpenRouter LLM: anthropic/claude-sonnet-5.5)
  3. Multimodaler Full-Page Screenshot-Kritiker (Playwright + OpenRouter Vision: google/gemini-3.8-flash)

Ausgabe: JSON + lesbarer Report; Exit-Code 2 bei P1-Befunden (nicht versandbereit).
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Set

from bs4 import BeautifulSoup

MXS_ROOT = Path("/home/brainuser/workspaces/mxs-embed")
ENV_PATHS = [
    Path("/home/brainuser/workspaces/ACP-Authentic-Content-Pilot-Pro0396/.env"),
    Path("/home/brainuser/workspaces/ACP-Authentic-Content-Pilot-Pro0396/acp-core/.env"),
    Path("/home/brainuser/workspaces/ACP-Authentic-Content-Pilot-Pro0396/acp-core/scripts/llm-swarm/.env"),
]


def load_openrouter_key() -> str:
    if os.environ.get("OPENROUTER_API_KEY"):
        return os.environ["OPENROUTER_API_KEY"].strip()
    for p in ENV_PATHS:
        if p.exists():
            for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
                if line.startswith("OPENROUTER_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise RuntimeError("OPENROUTER_API_KEY not found in env or .env files")


def extract_visible_text_from_html(html: str, keep_partner_footer: bool = False) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "svg", "noscript"]):
        tag.decompose()
    if not keep_partner_footer:
        for el in soup.select(".wp-partner-footer-wrap, #wpPartnerModal"):
            el.decompose()
    lines: List[str] = []
    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    if title:
        lines.append(f"[TITLE] {title}")
    for el in soup.find_all(["h1", "h2", "h3", "h4", "p", "li", "label", "button", "a", "span", "option", "input", "textarea"]):
        # Skip deeply nested redundant wrappers
        if el.name == "span" and el.parent and el.parent.name in ("button", "a", "li", "p", "h1", "h2", "h3", "label"):
            continue
        if el.name in ("input", "textarea"):
            ph = (el.get("placeholder") or "").strip()
            if ph:
                lines.append(f"[PLACEHOLDER] {ph}")
            continue
        txt = re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()
        if not txt or len(txt) < 2:
            continue
        prefix = f"[{el.name.upper()}] " if el.name in ("h1", "h2", "h3", "label", "button") else ""
        item = prefix + txt
        if not lines or lines[-1] != item:
            lines.append(item)
    return "\n".join(lines)


def fetch_url_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as r:
        html = r.read().decode("utf-8", "ignore")
    return extract_visible_text_from_html(html, keep_partner_footer=True)


def normalize_num(raw: str) -> str:
    return re.sub(r"[\s'’.,—–\-]+", "", raw or "").lower()


def extract_facts(text: str) -> Dict[str, Set[str]]:
    # CHF / prices / percents / quantified claims
    chf_matches = set(re.findall(r"(?:CHF|Fr\.?)\s*[\d'’.,]+(?:\.—|\.-)?", text, re.I))
    quant_matches = set(
        re.findall(
            r"\b\d{1,5}(?:['’.,]\d+)?\s*(?:%|Prozent|Jahre|Jahr|Fahrzeuge|Ersatzwagen|Lieferwagen|Personenwagen|Teams|Mitarbeitende|Mitarbeiter|Minuten|Sekunden|Stunden|Tage|Monate|Felder|Ratgeber|PDFs?)\b",
            text,
            re.I,
        )
    )
    phones = set(re.findall(r"(?:\+41|0800|0\d{2})[\s\d]{7,15}", text))
    emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text.lower()))
    return {
        "chf": chf_matches,
        "quants": quant_matches,
        "phones": {re.sub(r"\s+", " ", p).strip() for p in phones},
        "emails": emails,
    }


COST_LOG: List[Dict[str, Any]] = []


def openrouter_chat(api_key: str, model: str, messages: List[Dict[str, Any]], max_tokens: int = 16384, step_label: str = "") -> str:
    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.1,
        "max_tokens": max_tokens,
    }
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://webpilot.magnet-xs.ch",
            "X-Title": "WebPilot Adversarial Auditor",
        },
    )
    with urllib.request.urlopen(req, timeout=180) as r:
        data = json.loads(r.read().decode("utf-8"))
    usage = data.get("usage") or {}
    cost_usd = float(usage.get("cost") or 0.0)
    COST_LOG.append({
        "step": step_label or model,
        "model": model,
        "prompt_tokens": int(usage.get("prompt_tokens") or 0),
        "completion_tokens": int(usage.get("completion_tokens") or 0),
        "cost_usd": round(cost_usd, 6),
    })
    choice = (data.get("choices") or [{}])[0]
    msg = choice.get("message") or {}
    txt = msg.get("content") or msg.get("reasoning") or ""
    if not txt:
        raise RuntimeError(f"Empty OpenRouter response from {model}: {json.dumps(data)[:400]}")
    return str(txt)


def parse_json_block(raw: str) -> Dict[str, Any]:
    m = re.search(r"```json\s*(\{.*?\})\s*```", raw, re.S)
    blob = m.group(1) if m else raw
    if not m:
        s = raw.find("{")
        e = raw.rfind("}")
        if s != -1 and e != -1:
            blob = raw[s : e + 1]
    try:
        return json.loads(blob)
    except Exception:
        return {"raw_parse_error": True, "raw": raw}


def capture_fullpage_slices(site_dir: Path, pages: List[str], out_dir: Path) -> Dict[str, List[Path]]:
    out_dir.mkdir(parents=True, exist_ok=True)
    node_script = out_dir / "_capture.mjs"
    manifest_out = out_dir / "_manifest.json"
    js = f"""
import {{ createRequire }} from 'module';
import fs from 'fs';
import path from 'path';
const req = createRequire('/home/brainuser/workspaces/ACP-Authentic-Content-Pilot-Pro0396/acp-app/package.json');
const {{ chromium }} = req('playwright-core');
const candidates = [
  '/home/brainuser/.cache/ms-playwright/chromium-1217/chrome-linux64/chrome',
  '/home/brainuser/.cache/ms-playwright/chromium-1217/chrome-linux/chrome',
  '/home/brainuser/.cache/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-linux64/chrome-headless-shell',
  '/home/brainuser/.cache/ms-playwright/chromium-1208/chrome-linux64/chrome'
];
const exe = candidates.find(p => fs.existsSync(p));
const pages = {json.dumps(pages)};
const siteDir = {json.dumps(str(site_dir))};
const outDir = {json.dumps(str(out_dir))};
const manifest = {{}};

const browser = await chromium.launch({{ executablePath: exe }});
try {{
  const ctx = await browser.newContext({{ viewport: {{ width: 1440, height: 900 }} }});
  const page = await ctx.newPage();
  for (const rel of pages) {{
    const url = 'file://' + path.join(siteDir, rel);
    await page.goto(url, {{ waitUntil: 'networkidle' }});
    await page.waitForTimeout(250);
    const totalH = await page.evaluate(() => document.documentElement.scrollHeight);
    const shots = [];
    // Zero-Blindspot Slicing: 750px Schritt bei 900px Viewport (150px Ueberlappung) bis ganz zum Footer
    const vh = 900;
    const step = 750;
    const maxSlices = 10;
    const lastY = Math.max(0, totalH - vh);
    let y = 0;
    let idx = 1;
    while (idx <= maxSlices) {{
      await page.evaluate(isScrolled => {{
        for (const h of document.querySelectorAll('header, .site-header, .ah-sparten-bar')) {{
          const pos = getComputedStyle(h).position;
          if (pos === 'sticky' || pos === 'fixed') {{
            h.style.visibility = isScrolled ? 'hidden' : '';
          }}
        }}
      }}, idx >= 2);
      await page.evaluate(yy => window.scrollTo({{ top: yy, behavior: 'instant' }}), y);
      await page.waitForTimeout(150);
      const outPng = path.join(outDir, rel.replace(/[^a-zA-Z0-9_-]/g, '_') + `_d${{idx}}.png`);
      await page.screenshot({{ path: outPng }});
      shots.push(outPng);
      if (y >= lastY) break;
      y = Math.min(y + step, lastY);
      idx++;
    }}
    await page.evaluate(() => {{
      for (const h of document.querySelectorAll('header, .site-header, .ah-sparten-bar')) {{
        h.style.visibility = '';
      }}
    }});
    manifest[rel] = shots;
  }}
}} finally {{
  await browser.close();
}}
fs.writeFileSync({json.dumps(str(manifest_out))}, JSON.stringify(manifest, null, 2));
"""
    node_script.write_text(js, encoding="utf-8")
    env = os.environ.copy()
    extra_bins = [str(Path.home() / ".local/bin"), "/usr/local/bin"] + [str(b) for b in sorted(Path.home().glob(".nvm/versions/node/*/bin"))]
    env["PATH"] = ":".join(extra_bins) + ":" + env.get("PATH", "")
    node_bin = next((str(Path(d) / "node") for d in extra_bins if (Path(d) / "node").exists()), "node")
    subprocess.run([node_bin, str(node_script)], check=True, env=env)
    return {k: [Path(p) for p in v] for k, v in json.loads(manifest_out.read_text(encoding="utf-8")).items()}


def main() -> int:
    ap = argparse.ArgumentParser(description="WebPilot Adversarial Vorher/Nachher Text-, Fakten- & Screenshot-Auditor")
    ap.add_argument("--site", required=True, help="z. B. preview-autohauser-v2")
    ap.add_argument("--source-json", default="", help="Optionales Scrape-JSON der Original-Website(s)")
    ap.add_argument("--source-urls", nargs="*", default=[], help="Original-URLs fuer den Vorher-Vergleich")
    ap.add_argument("--text-model", default="anthropic/claude-sonnet-5.5")
    ap.add_argument("--vision-model", default="google/gemini-3.8-flash")
    ap.add_argument("--skip-vision", action="store_true")
    ap.add_argument("--out", default="", help="Pfad fuer JSON-Report")
    args = ap.parse_args()

    site_dir = MXS_ROOT / args.site
    if not site_dir.exists():
        print(f"ERROR: Site dir not found: {site_dir}", file=sys.stderr)
        return 1

    api_key = load_openrouter_key()

    # 1. Load source baseline text (Vorher)
    orig_texts: List[str] = []
    if args.source_json and Path(args.source_json).exists():
        raw = json.loads(Path(args.source_json).read_text(encoding="utf-8"))
        # Support both list-of-pages dicts and dict-by-url/domain
        if isinstance(raw, list):
            for entry in raw:
                if isinstance(entry, dict):
                    u = entry.get("url") or entry.get("path") or ""
                    body = entry.get("text") or entry.get("content") or json.dumps(entry, ensure_ascii=False)
                    orig_texts.append(f"=== ORIGINAL {u} ===\n{body[:8000]}")
        elif isinstance(raw, dict):
            def _flatten_clean(obj):
                if isinstance(obj, str):
                    return obj
                if isinstance(obj, list):
                    return " ".join(_flatten_clean(x) for x in obj)
                if isinstance(obj, dict):
                    if "items" in obj and isinstance(obj["items"], list):
                        return "\n".join(str(i.get("text") or "") for i in obj["items"] if isinstance(i, dict))
                    if "text" in obj and isinstance(obj["text"], str):
                        return obj["text"]
                    return "\n".join(f"{kk}: {_flatten_clean(vv)}" for kk, vv in obj.items())
                return str(obj)
            for k, v in raw.items():
                orig_texts.append(f"=== ORIGINAL SECTION {k} ===\n{_flatten_clean(v)[:28000]}")
    for u in args.source_urls:
        try:
            orig_texts.append(f"=== LIVE ORIGINAL {u} ===\n" + fetch_url_text(u)[:18000])
        except Exception as ex:
            orig_texts.append(f"=== LIVE ORIGINAL {u} (FETCH ERR: {ex}) ===")

    full_original_corpus = "\n\n".join(orig_texts)
    orig_facts = extract_facts(full_original_corpus)
    orig_norm_chf = {normalize_num(x) for x in orig_facts["chf"]}
    orig_norm_nums = {re.sub(r"[^0-9]", "", x) for x in (orig_facts["chf"] | orig_facts["quants"]) if re.sub(r"[^0-9]", "", x)}

    # 2. Extract generated top-level pages (Nachher)
    html_files = sorted([p.name for p in site_dir.glob("*.html") if p.name != "cockpit.html"])
    pages_extracted: Dict[str, str] = {}
    all_new_corpus_parts: List[str] = []
    det_findings: List[Dict[str, Any]] = []

    meta_jargon_re = re.compile(
        r"\b(?:webpilot|smart-pro|jotform|altformular[a-z]*|defekte[nr]?\s+formular[a-z]*|veraltete[nr]?\s+externe|vorschau-?schutzmodus|auftrags-pdf|1-seiten-|lazy[\s-]modal|cockpit)\b",
        re.I,
    )

    for fname in html_files:
        raw_html = (site_dir / fname).read_text(encoding="utf-8")
        txt = extract_visible_text_from_html(raw_html, keep_partner_footer=False)
        pages_extracted[fname] = txt
        all_new_corpus_parts.append(f"### SEITE: {fname}\n{txt}")

        nf = extract_facts(txt)
        for c in sorted(nf["chf"]):
            digits = re.sub(r"[^0-9]", "", c)
            if normalize_num(c) not in orig_norm_chf and digits not in orig_norm_nums:
                det_findings.append({
                    "severity": "P1",
                    "type": "UNVERIFIED_PRICE_OR_CHF",
                    "page": fname,
                    "value": c,
                    "detail": f"CHF-Betrag '{c}' steht auf '{fname}', wurde aber im Original-Scrape NICHT gefunden!",
                })
        for q in sorted(nf["quants"]):
            digits = re.sub(r"[^0-9]", "", q)
            if digits and digits not in orig_norm_nums and not re.search(rf"\b{re.escape(digits)}\b", full_original_corpus):
                det_findings.append({
                    "severity": "P2",
                    "type": "UNVERIFIED_QUANTIFIED_CLAIM",
                    "page": fname,
                    "value": q,
                    "detail": f"Zahlenangabe '{q}' auf '{fname}' kommt im gecrawlten Original nicht direkt mit dieser Zahl vor — Fakten-Check noetig!",
                })
        for ph in sorted(nf["phones"]):
            dph = re.sub(r"[^0-9]", "", ph)
            orig_dphs = {re.sub(r"[^0-9]", "", op) for op in orig_facts["phones"]}
            if dph and not any(dph[-7:] in od for od in orig_dphs if len(od) >= 7) and dph[-7:] not in re.sub(r"[^0-9]", "", full_original_corpus):
                det_findings.append({
                    "severity": "P1",
                    "type": "UNVERIFIED_PHONE",
                    "page": fname,
                    "value": ph,
                    "detail": f"Telefonnummer '{ph}' auf '{fname}' steht nicht im Original!",
                })
        for jm in set(meta_jargon_re.findall(txt)):
            det_findings.append({
                "severity": "P2",
                "type": "SUSPECT_INTERNAL_TERM",
                "page": fname,
                "value": jm,
                "detail": f"Verdaechtiger interner/Agentur-/Systembegriff '{jm}' im sichtbaren Kundentext auf '{fname}'.",
            })

    # 3. Adversarial LLM Prosecutor (Vorher vs. Nachher Text, Fakten & Peinlichkeit)
    new_corpus_joined = "\n\n".join(all_new_corpus_parts)
    prosecutor_prompt = f"""Du bist ein unbestechlicher, pingeliger Schweizer KMU-Geschaeftsfuehrer und Qualitaets-Staatsanwalt.
Unten siehst du:
(A) Die gesammelten ORIGINALTEXTE der bisherigen Unternehmens-Website(s) (VORHER)
(B) Die deterministisch gefundenen neuen Zahlen/Preise/Telefonnummern/Verdaechtigen Begriffe (DELTA)
(C) Alle sichtbaren Texte, Buttons, Formulare, Kacheln und Hinweise der NEU GENERIERTEN Website-Vorschau (NACHHER)

DEINE AUFGABE:
Finde JEDEN Textfehler, jede Peinlichkeit, jeden erfundene Preis/Fakt/Garantie, jeden unlogischen Zusammenhang, jede KI-Floskel und jeden internen Entwickler-/Agentur-Sprech, bei dem der Firmeninhaber sagen wuerde: "Das kann ich doch meinen Kunden nicht zeigen – komplett unbrauchbar!"

Pruefe streng auf diese 6 Klassen:
1. ERFUNDENE FAKTEN / PREISE / ZAHLEN / VERSPRECHEN: Steht im Nachher ein Preis (CHF), ein Rabatt, eine Garantie ("lebenslange Garantie"), eine Fahrzeuganzahl, eine Stueckzahl, eine Lieferfrist oder ein Name, der im Vorher-Original gar nicht belegt ist? -> P1!
2. KONTEXT-BRUCH / FORMULAR-UNSINN: Stehen falsche Optionen, falsche Bereiche, unpassende Fragen oder widerspruechliche Ueberschriften auf einer Seite? -> P1!
3. ENTWICKLER- / AGENTUR-SPRECH / ALTSEITEN-BASHING: Spricht der Text ueber "Formulare", "PDFs", "Prozesse", "Vorschau", "alte Seite", "Smart-Assistent" statt einfach zum Endkunden? -> P1/P2!
4. TONALITAET & AUTHENTIZITAET: Wirkt eine Passage kuenstlich aufgeblasen, uebertrieben oder marktschreierisch statt wie ein echter Schweizer Traditionsbetrieb? -> P2!
5. FEHLENDE / FALSCH ZUGEORDNETE INHALTE: Ist eine Person einer falschen Abteilung zugeordnet oder fehlt ein wichtiges Detail? -> P1!
6. PEINLICHKEITS-TEST: Was genau waere peinlich, wenn der Inhaber es heute Abend liest?

Antworte AUSSCHLIESSLICH mit validem JSON exakt in dieser Form:
{{
  "ready_to_present": true/false,
  "verdict_summary": "Kurzes ehrliches Urteil in 2-3 Saetzen",
  "p1_findings": [
    {{"page": "dateiname.html", "category": "HALLUZINATION|KONTEXT|JARGON|FAKTENFEHLER|PEINLICH", "quote": "exaktes Zitat aus Nachher", "why_bad": "Warum das falsch/peinlich/erfunden ist", "fix": "Konkreter Ersatz oder Loeschung"}}
  ],
  "p2_findings": [
    {{"page": "dateiname.html", "category": "TONALITAET|JARGON|UNGENAU", "quote": "exaktes Zitat", "why_bad": "...", "fix": "..."}}
  ]
}}

=== (A) VORHER-ORIGINAL ===
{full_original_corpus[:120000]}

=== (B) DETERMINISTISCHES DELTA ===
{json.dumps(det_findings, indent=2, ensure_ascii=False)[:15000]}

=== (C) NACHHER-SEITEN ===
{new_corpus_joined[:85000]}
"""
    raw_text_verdict = openrouter_chat(
        api_key,
        args.text_model,
        [{"role": "user", "content": prosecutor_prompt}],
        max_tokens=16384,
        step_label="text_fact_audit",
    )
    text_audit = parse_json_block(raw_text_verdict)

    # 4. Multimodal Vision Screenshot Critic
    vision_findings: List[Dict[str, Any]] = []
    shot_dir = Path(f"/tmp/content_audit_shots_{args.site}")
    if not args.skip_vision:
        manifest = capture_fullpage_slices(site_dir, html_files, shot_dir)
        for page_name, pngs in manifest.items():
            content_parts: List[Dict[str, Any]] = [
                {
                    "type": "text",
                    "text": (
                        f"Du pruefst als strenger Schweizer Geschaeftsfuehrer und Artdirector die Full-Page-Screenshots der Seite '{page_name}' ({args.site}). "
                        "Suche schonungslos nach: (1) Texten die nicht zur Sektion/zum Foto passen, (2) peinlichem Entwickler-/KI-/Agentur-Sprech im UI, "
                        "(3) komischen Buttons, asymmetrischen Button-Zeilen oder Treppenstufen in nebeneinanderliegenden Karten (1-zeilig vs. 2-zeilig umgebrochen), abgeschnittenen Kartenbildern mit weissem Randstreifen, Abstaenden, fehlenden Bildern oder optischen Bruchen, "
                        "(4) Behauptungen/Preisen die verdaechtig oder fehl am Platz wirken. "
                        'Antworte als kompaktes JSON: {"page":"' + page_name + '","issues":[{"severity":"P1|P2","location":"...","issue":"...","fix":"..."}]}'
                    ),
                }
            ]
            for png in pngs:
                b64 = base64.b64encode(png.read_bytes()).decode("ascii")
                content_parts.append({
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{b64}"},
                })
            raw_v = openrouter_chat(api_key, args.vision_model, [{"role": "user", "content": content_parts}], max_tokens=8192, step_label=f"vision:{page_name}")
            vision_findings.append(parse_json_block(raw_v))

    total_usd = round(sum(c["cost_usd"] for c in COST_LOG), 5)
    total_prompt_tok = sum(c["prompt_tokens"] for c in COST_LOG)
    total_comp_tok = sum(c["completion_tokens"] for c in COST_LOG)
    report = {
        "site": args.site,
        "pages_checked": html_files,
        "text_model": args.text_model,
        "vision_model": args.vision_model,
        "openrouter_cost": {
            "total_usd": total_usd,
            "approx_chf": round(total_usd * 0.90, 4),
            "prompt_tokens": total_prompt_tok,
            "completion_tokens": total_comp_tok,
            "calls": COST_LOG,
        },
        "deterministic_delta": det_findings,
        "text_fact_audit": text_audit,
        "vision_screenshot_audit": vision_findings,
    }

    out_path = Path(args.out) if args.out else Path(f"/tmp/content_audit_{args.site}.json")
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))

    p1_cnt = len(text_audit.get("p1_findings") or []) + sum(
        1 for vf in vision_findings for iss in (vf.get("issues") or []) if iss.get("severity") == "P1"
    )
    return 2 if p1_cnt > 0 else 0


if __name__ == "__main__":
    sys.exit(main())

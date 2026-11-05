#!/usr/bin/env python3
"""
WebPilot — Kunden- & URL-Zentrale (Google Sheets Live-Sync)
===========================================================
Synchronisiert alle WebPilot-Vorschauen (Zeigeversion -v2, Vollversion -vollversion,
Studio Cockpit v4.0, Original-Webseite & Kontext, Partner, Status & Datum) mit der
zentralen Google-Tabelle fuer Jenny Ettle (JE-MI) & David Huegli (Magnet XS).

Regel-Konformitaet:
- BACKEND-DB-RULES.md (Canary: BACKEND-DB-2026-V1, #BE-07 Retry & Zero-Silent-Failure)
- LANG-KODEX-CH.md (Canary: LANG-CH-2026-V1, 100 % ss statt Eszett)
"""

from __future__ import annotations

import argparse
import json
import os
import time
import urllib.parse
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests
from google.auth.transport.requests import Request
from google.oauth2 import service_account

DEFAULT_SPREADSHEET_ID = "1O3EqOCqGS5HbE5rWxIBoTk8lLA0a2Pz30F7yKiEbRms"
DEFAULT_SPREADSHEET_URL = f"https://docs.google.com/spreadsheets/d/{DEFAULT_SPREADSHEET_ID}/edit"
DEFAULT_TAB_TITLE = "Kunden & URL-Zentrale"

SA_PATHS = [
    "/home/brainuser/.config/gcloud/legacy_credentials/pro-0396-acp-authen-cont-pilot@appspot.gserviceaccount.com/adc.json",
    r"C:\Users\Daviduserich\AppData\Roaming\gcloud\legacy_credentials\pro-0396-acp-authen-cont-pilot@appspot.gserviceaccount.com\adc.json",
]

PARTNER_CONFIG_PATHS = [
    Path("/home/brainuser/vault-plain/10-Projects/WebPilot-Pro0416/03-Fulfillment/partner_config.json"),
    Path("/home/brainuser/workspaces/mxs-embed/config/partner_config.json"),
]

HEADERS = [
    "Aktiv",
    "Firma / Verein",
    "Zeigeversion (-v2 für Kunden)",
    "Vollversion (-vollversion für uns)",
    "Studio Cockpit v4.0",
    "Original-Webseite & Kontext",
    "Partner",
    "Status & Datum",
]

SEED_PROJECTS = [
    {
        "slug": "herzensarbeit",
        "active": True,
        "company": "Herzensarbeit — Anne-Katrin Koch (Härkingen SO)",
        "v2_url": "https://vorschau.magnet-xs.ch/herzensarbeit-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/herzensarbeit-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/herzensarbeit-vollversion/cockpit?token=herzensarbeit2026",
        "source_context": "https://herzensarbeit.ch/ — Paartherapie, Trennungsberatung, Trauerbegleitung & Frauen-Workshops in Härkingen SO",
        "partner": "Jenny Ettle (JE-MI)",
        "status": "🟢 Bereit zum Zeigen (05.11.2026)",
    },
    {
        "slug": "frees",
        "active": True,
        "company": "Free's Stefan Fritschi (Niederrohrdorf)",
        "v2_url": "https://vorschau.magnet-xs.ch/frees-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/frees-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/frees-vollversion/cockpit?token=frees2026",
        "source_context": "https://www.frees.ch/ — Studio für Textildesign, Textildruck, Stickerei, Teamsport & Promowear in Niederrohrdorf AG",
        "partner": "Jenny Ettle (JE-MI)",
        "status": "🟢 Bereit zum Zeigen (04.11.2026)",
    },
    {
        "slug": "innere-staerke",
        "active": True,
        "company": "Wüest + Paneduro — Innere Stärke (Sursee)",
        "v2_url": "https://vorschau.magnet-xs.ch/innere-staerke-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/innere-staerke-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/innere-staerke-vollversion/cockpit?token=innerestaerke2026",
        "source_context": "https://www.innere-staerke.business/ — Führungskräfte-Training, Resilienz & Persönlichkeitsentwicklung in Sursee LU",
        "partner": "Jenny Ettle (JE-MI)",
        "status": "🟢 Bereit zum Zeigen (04.11.2026)",
    },
    {
        "slug": "fcschlieren",
        "active": True,
        "company": "FC Schlieren (33 Teams)",
        "v2_url": "https://vorschau.magnet-xs.ch/fcschlieren-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/fcschlieren-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/fcschlieren-vollversion/cockpit?token=fcschlieren2026",
        "source_context": "https://www.fcschlieren.ch/ — Fussballclub Schlieren ZH (33 Teams, Sponsoren-Matrix & Team-Hub)",
        "partner": "Jenny Ettle (JE-MI)",
        "status": "🟢 Bereit zum Zeigen (04.11.2026)",
    },
    {
        "slug": "scfulenbach",
        "active": True,
        "company": "SC Fulenbach (14 Teams)",
        "v2_url": "https://vorschau.magnet-xs.ch/scfulenbach-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/scfulenbach-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/scfulenbach-vollversion/cockpit?token=scfulenbach2026",
        "source_context": "https://www.scfulenbach.ch/ — Sportclub Fulenbach SO (14 Teams, Vereinsleben & Sponsoren)",
        "partner": "Jenny Ettle (JE-MI)",
        "status": "🟢 Bereit zum Zeigen (04.11.2026)",
    },
    {
        "slug": "fcattiswil",
        "active": True,
        "company": "FC Attiswil (14 Teams)",
        "v2_url": "https://vorschau.magnet-xs.ch/fcattiswil-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/fcattiswil-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/fcattiswil-vollversion/cockpit?token=fcattiswil2026",
        "source_context": "https://www.fcattiswil.ch/ — Fussballclub Attiswil BE (14 Teams, Junioren & Sponsoren)",
        "partner": "Jenny Ettle (JE-MI)",
        "status": "🟢 Bereit zum Zeigen (04.11.2026)",
    },
    {
        "slug": "her11",
        "active": True,
        "company": "HER11 (Jenny Ettle)",
        "v2_url": "https://vorschau.magnet-xs.ch/her11-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/her11-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/her11-vollversion/cockpit?token=her112026",
        "source_context": "https://www.her11.ch/ — HER11 Frauenfussball & Sport-Marketing (Jenny Ettle / JE-MI)",
        "partner": "Jenny Ettle (JE-MI)",
        "status": "🟢 Bereit zum Zeigen (30.10.2026)",
    },
    {
        "slug": "hochuli",
        "active": True,
        "company": "Hochuli Schlossrued AG (5 Sparten)",
        "v2_url": "https://vorschau.magnet-xs.ch/hochuli-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/hochuli-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/hochuli-vollversion/cockpit?token=hochuli2026",
        "source_context": "https://www.hochuli-gruppe.ch/ — Bauunternehmung Schlossrued AG (5 Sparten: Hoch-/Tiefbau, Holzbau, Bedachungen, Immobilien, Mulden)",
        "partner": "David Hügli (Magnet XS)",
        "status": "🟢 Bereit zum Zeigen (29.10.2026)",
    },
    {
        "slug": "hiltbrand",
        "active": True,
        "company": "Hiltbrand Gebäudehüllen AG (Zweisimmen)",
        "v2_url": "https://vorschau.magnet-xs.ch/hiltbrand-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/hiltbrand-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/hiltbrand-vollversion/cockpit?token=hb2026",
        "source_context": "https://dachdecker-berneroberland.ch/ — Steildach, Flachdach, Fassadenbau & Spenglerei in Zweisimmen BE",
        "partner": "David Hügli (Magnet XS)",
        "status": "🟢 Bereit zum Zeigen (29.10.2026)",
    },
    {
        "slug": "birchmeier",
        "active": True,
        "company": "Birchmeier Haustechnik (Sarmenstorf)",
        "v2_url": "https://vorschau.magnet-xs.ch/birchmeier-v2/",
        "vollversion_url": "https://vorschau.magnet-xs.ch/birchmeier-vollversion/",
        "cockpit_url": "https://vorschau.magnet-xs.ch/birchmeier-vollversion/cockpit?token=bi_live_ea3776_a1ef",
        "source_context": "https://www.birchmeier-hohler.ch/ — Sanitär, Heizung, Badumbau & 24h-Pikettdienst in Sarmenstorf AG",
        "partner": "David Hügli (Magnet XS)",
        "status": "🟢 Bereit zum Zeigen (29.10.2026)",
    },
]


def get_sheet_config() -> Dict[str, str]:
    for p in PARTNER_CONFIG_PATHS:
        if p.exists():
            try:
                cfg = json.loads(p.read_text(encoding="utf-8"))
                sid = str(cfg.get("google_sheet_id") or DEFAULT_SPREADSHEET_ID).strip()
                surl = str(cfg.get("google_sheet_url") or f"https://docs.google.com/spreadsheets/d/{sid}/edit").strip()
                return {"spreadsheet_id": sid, "spreadsheet_url": surl}
            except Exception:
                pass
    return {"spreadsheet_id": DEFAULT_SPREADSHEET_ID, "spreadsheet_url": DEFAULT_SPREADSHEET_URL}


def _get_auth_headers() -> Dict[str, str]:
    for sa_path in SA_PATHS:
        if os.path.exists(sa_path):
            creds = service_account.Credentials.from_service_account_file(
                sa_path,
                scopes=["https://www.googleapis.com/auth/spreadsheets"],
            )
            creds.refresh(Request())
            return {
                "Authorization": f"Bearer {creds.token}",
                "Content-Type": "application/json",
            }
    raise RuntimeError("Keine Google Service-Account-Credentials (adc.json) gefunden.")


def _request_with_retry(method: str, url: str, **kwargs) -> requests.Response:
    """Adaptive Retry-Schleife gemaess #BE-07."""
    last_exc = None
    for attempt in range(3):
        try:
            headers = _get_auth_headers()
            r = requests.request(method, url, headers=headers, timeout=25, **kwargs)
            if r.status_code < 500 and r.status_code != 429:
                return r
            last_exc = RuntimeError(f"HTTP {r.status_code}: {r.text[:300]}")
        except Exception as exc:
            last_exc = exc
        time.sleep(1.2 * (attempt + 1))
    if last_exc:
        raise last_exc
    raise RuntimeError("Request fehlgeschlagen.")


def _get_first_sheet_meta(spreadsheet_id: str) -> Dict[str, Any]:
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}"
    r = _request_with_retry("GET", url, params={"fields": "properties.title,sheets.properties(sheetId,title)"})
    r.raise_for_status()
    data = r.json()
    sheets = data.get("sheets") or []
    if not sheets:
        raise RuntimeError("Keine Tabellenblaetter im Spreadsheet gefunden.")
    return sheets[0]["properties"]


def apply_sheet_formatting(spreadsheet_id: str, sheet_id: int, current_title: str, total_rows: int = 100) -> None:
    """Wendet Header-Fixierung, Auto-Filter, echte BOOLEAN-Checkboxen, bedingte Formatierung & Spaltenbreiten an."""
    requests_list: List[Dict[str, Any]] = []

    # 1. Tab-Name auf 'Kunden & URL-Zentrale' setzen + Zeile 1 fixieren
    requests_list.append({
        "updateSheetProperties": {
            "properties": {
                "sheetId": sheet_id,
                "title": DEFAULT_TAB_TITLE,
                "gridProperties": {
                    "frozenRowCount": 1,
                },
            },
            "fields": "title,gridProperties.frozenRowCount",
        }
    })

    # 2. Header-Zeile (Zeile 1): Dunkles Slate (#0F172A), weisse fette Schrift
    requests_list.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 0,
                "endColumnIndex": 8,
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.059, "green": 0.090, "blue": 0.165},
                    "textFormat": {
                        "bold": True,
                        "fontSize": 10,
                        "foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0},
                    },
                    "horizontalAlignment": "LEFT",
                    "verticalAlignment": "MIDDLE",
                    "wrapStrategy": "WRAP",
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,wrapStrategy)",
        }
    })

    # Header-Zeilenhoehe 38px
    requests_list.append({
        "updateDimensionProperties": {
            "range": {
                "sheetId": sheet_id,
                "dimension": "ROWS",
                "startIndex": 0,
                "endIndex": 1,
            },
            "properties": {"pixelSize": 38},
            "fields": "pixelSize",
        }
    })

    # 3. Daten-Zeilen (A2:H100): Sauberer Textumbruch & vertikale Zentrierung
    requests_list.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 1,
                "endRowIndex": max(total_rows, 100),
                "startColumnIndex": 0,
                "endColumnIndex": 8,
            },
            "cell": {
                "userEnteredFormat": {
                    "verticalAlignment": "MIDDLE",
                    "wrapStrategy": "WRAP",
                    "textFormat": {"fontSize": 10},
                }
            },
            "fields": "userEnteredFormat(verticalAlignment,wrapStrategy,textFormat.fontSize)",
        }
    })

    # 4a. Leere Checkboxen unterhalb der belegten Zeilen bereinigen
    requests_list.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": max(2, total_rows),
                "endRowIndex": 200,
                "startColumnIndex": 0,
                "endColumnIndex": 1,
            },
            "cell": {
                "dataValidation": None,
            },
            "fields": "dataValidation",
        }
    })

    # 4b. Echte interaktive Google-Sheets-Checkboxen exakt auf den belegten Zeilen in Spalte A
    requests_list.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 1,
                "endRowIndex": max(2, total_rows),
                "startColumnIndex": 0,
                "endColumnIndex": 1,
            },
            "cell": {
                "dataValidation": {
                    "condition": {"type": "BOOLEAN"},
                    "showCustomUi": True,
                },
                "userEnteredFormat": {
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE",
                },
            },
            "fields": "dataValidation,userEnteredFormat(horizontalAlignment,verticalAlignment)",
        }
    })

    # 5. Spalte B (Firma / Verein) fett formatieren
    requests_list.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 1,
                "endRowIndex": max(total_rows, 100),
                "startColumnIndex": 1,
                "endColumnIndex": 2,
            },
            "cell": {
                "userEnteredFormat": {
                    "textFormat": {"bold": True, "fontSize": 10},
                }
            },
            "fields": "userEnteredFormat.textFormat(bold,fontSize)",
        }
    })

    # 6. Auto-Filter (BasicFilter) ueber A1:H100 aktivieren
    requests_list.append({
        "setBasicFilter": {
            "filter": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": 0,
                    "endRowIndex": max(total_rows, 100),
                    "startColumnIndex": 0,
                    "endColumnIndex": 8,
                }
            }
        }
    })

    # 7. Optimale Spaltenbreiten (A bis H)
    col_widths = [
        (0, 1, 75),    # A: Aktiv
        (1, 2, 285),   # B: Firma / Verein
        (2, 3, 330),   # C: Zeigeversion (-v2)
        (3, 4, 350),   # D: Vollversion (-vollversion)
        (4, 5, 420),   # E: Studio Cockpit v4.0
        (5, 6, 390),   # F: Original-Webseite & Kontext
        (6, 7, 185),   # G: Partner
        (7, 8, 235),   # H: Status & Datum
    ]
    for start_col, end_col, px in col_widths:
        requests_list.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": sheet_id,
                    "dimension": "COLUMNS",
                    "startIndex": start_col,
                    "endIndex": end_col,
                },
                "properties": {"pixelSize": px},
                "fields": "pixelSize",
            }
        })

    # 8. Bedingte Formatierung: Wenn Spalte A (Aktiv) = FALSE -> Zeile dezent ausgrauen
    # Zuerst bestehende ConditionalFormatRules abfragen, um Duplikate zu vermeiden
    meta_url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}"
    r_cf = _request_with_retry("GET", meta_url, params={"fields": "sheets(properties.sheetId,conditionalFormats)"})
    if r_cf.status_code == 200:
        for sh in r_cf.json().get("sheets", []):
            if sh.get("properties", {}).get("sheetId") == sheet_id:
                existing_rules = sh.get("conditionalFormats") or []
                for idx in range(len(existing_rules) - 1, -1, -1):
                    requests_list.append({
                        "deleteConditionalFormatRule": {
                            "sheetId": sheet_id,
                            "index": idx,
                        }
                    })

    requests_list.append({
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [
                    {
                        "sheetId": sheet_id,
                        "startRowIndex": 1,
                        "endRowIndex": max(total_rows, 100),
                        "startColumnIndex": 0,
                        "endColumnIndex": 8,
                    }
                ],
                "booleanRule": {
                    "condition": {
                        "type": "CUSTOM_FORMULA",
                        "values": [{"userEnteredValue": "=$A2=FALSE"}],
                    },
                    "format": {
                        "backgroundColor": {"red": 0.945, "green": 0.961, "blue": 0.976},
                        "textFormat": {
                            "foregroundColor": {"red": 0.580, "green": 0.639, "blue": 0.722},
                        },
                    },
                },
            },
            "index": 0,
        }
    })

    batch_url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}:batchUpdate"
    r_batch = _request_with_retry("POST", batch_url, json={"requests": requests_list})
    r_batch.raise_for_status()


def get_all_rows(spreadsheet_id: str, tab_title: str) -> List[List[str]]:
    safe_range = urllib.parse.quote(f"'{tab_title}'!A1:H200")
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{safe_range}"
    r = _request_with_retry("GET", url)
    r.raise_for_status()
    return r.json().get("values") or []


def _normalize_partner_label(raw_partner: str) -> str:
    s = (raw_partner or "").strip()
    low = s.lower()
    if "jenny" in low or "je-mi" in low or "ettle" in low:
        return "Jenny Ettle (JE-MI)"
    if "david" in low or "huegli" in low or "hügli" in low or "magnet" in low:
        return "David Hügli (Magnet XS)"
    return s or "Jenny Ettle (JE-MI)"


def init_and_seed_sheet() -> Dict[str, Any]:
    cfg = get_sheet_config()
    spreadsheet_id = cfg["spreadsheet_id"]
    props = _get_first_sheet_meta(spreadsheet_id)
    sheet_id = props["sheetId"]
    current_title = props["title"]

    # Formatierung & Umbenennung auf DEFAULT_TAB_TITLE
    apply_sheet_formatting(spreadsheet_id, sheet_id, current_title, total_rows=100)
    tab_title = DEFAULT_TAB_TITLE

    existing_rows = get_all_rows(spreadsheet_id, tab_title)
    # Map bestehender Aktiv-Werte anhand Slug oder Firmenname
    active_by_slug: Dict[str, bool] = {}
    for row in existing_rows[1:]:
        if len(row) >= 3:
            raw_active = str(row[0]).strip().upper()
            is_act = False if raw_active == "FALSE" else True
            row_text = " ".join(row).lower()
            for item in SEED_PROJECTS:
                if item["slug"] in row_text or item["company"].lower() in row_text:
                    active_by_slug[item["slug"]] = is_act

    values_matrix: List[List[Any]] = [HEADERS]
    for item in SEED_PROJECTS:
        slug = item["slug"]
        is_active = active_by_slug.get(slug, item.get("active", True))
        values_matrix.append([
            is_active,
            item["company"],
            item["v2_url"],
            item["vollversion_url"],
            item["cockpit_url"],
            item["source_context"],
            item["partner"],
            item["status"],
        ])

    # Behalte zusaetzliche dynamische Zeilen, die nicht in SEED_PROJECTS sind
    seed_slugs = {item["slug"] for item in SEED_PROJECTS}
    for row in existing_rows[1:]:
        if len(row) >= 2 and str(row[1]).strip():
            row_joined = " ".join(row).lower()
            if not any(s in row_joined for s in seed_slugs):
                padded = list(row) + [""] * (8 - len(row))
                padded[0] = False if str(padded[0]).strip().upper() == "FALSE" else True
                values_matrix.append(padded[:8])

    safe_range = urllib.parse.quote(f"'{tab_title}'!A1:H{len(values_matrix)}")
    put_url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{safe_range}"
    r_put = _request_with_retry(
        "PUT",
        put_url,
        params={"valueInputOption": "USER_ENTERED"},
        json={"values": values_matrix},
    )
    r_put.raise_for_status()

    # Formatierung & Checkboxen nochmals exakt ueber alle Zeilen legen
    apply_sheet_formatting(spreadsheet_id, sheet_id, tab_title, total_rows=len(values_matrix))

    return {
        "ok": True,
        "spreadsheet_id": spreadsheet_id,
        "spreadsheet_url": cfg["spreadsheet_url"],
        "tab_title": tab_title,
        "rows_written": len(values_matrix) - 1,
    }


def upsert_webpilot_sheet_row(
    slug: str,
    company_name: str,
    v2_url: str = "",
    vollversion_url: str = "",
    cockpit_url: str = "",
    source_context: str = "",
    partner: str = "Jenny Ettle (JE-MI)",
    status_text: str = "",
    active: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    Aktualisiert eine bestehende Zeile im Google Sheet (anhand Slug oder Firmenname)
    oder fuegt eine neue Zeile hinzu. Bewahrt bestehende Checkbox-Zustaende (Aktiv).
    """
    cfg = get_sheet_config()
    spreadsheet_id = cfg["spreadsheet_id"]
    props = _get_first_sheet_meta(spreadsheet_id)
    sheet_id = props["sheetId"]
    tab_title = props["title"]

    rows = get_all_rows(spreadsheet_id, tab_title)
    if not rows or rows[0] != HEADERS:
        init_and_seed_sheet()
        tab_title = DEFAULT_TAB_TITLE
        rows = get_all_rows(spreadsheet_id, tab_title)

    clean_slug = (slug or "").strip().lower().replace("preview-", "")
    for suffix in ("-vollversion", "-vv", "-v2", "-v1"):
        if clean_slug.endswith(suffix):
            clean_slug = clean_slug[: -len(suffix)]

    today_str = datetime.now().strftime("%d.%m.%Y")
    if not status_text:
        status_text = f"🟢 Bereit zum Zeigen ({today_str})" if v2_url else f"⏳ In Arbeit ({today_str})"

    partner_norm = _normalize_partner_label(partner)

    target_row_idx: Optional[int] = None
    existing_row: List[str] = []

    for idx, r in enumerate(rows):
        if idx == 0:
            continue
        row_str = " ".join(r).lower()
        comp_cell = (r[1] if len(r) > 1 else "").strip().lower()
        if (clean_slug and f"/{clean_slug}" in row_str) or (
            company_name and company_name.strip().lower() in comp_cell
        ) or (comp_cell and comp_cell in company_name.strip().lower()):
            target_row_idx = idx + 1  # 1-basiert
            existing_row = r
            break

    if target_row_idx is not None:
        prev_active = False if (len(existing_row) > 0 and str(existing_row[0]).strip().upper() == "FALSE") else True
        row_active = prev_active if active is None else bool(active)
        final_company = company_name.strip() or (existing_row[1] if len(existing_row) > 1 else clean_slug)
        final_v2 = v2_url.strip() if v2_url is not None and v2_url != "" else (existing_row[2] if len(existing_row) > 2 else "")
        final_voll = vollversion_url.strip() if vollversion_url is not None and vollversion_url != "" else (existing_row[3] if len(existing_row) > 3 else "")
        final_cockpit = cockpit_url.strip() if cockpit_url is not None and cockpit_url != "" else (existing_row[4] if len(existing_row) > 4 else "")
        final_source = source_context.strip() if source_context else (existing_row[5] if len(existing_row) > 5 else "")
        final_partner = partner_norm if partner else (existing_row[6] if len(existing_row) > 6 else "Jenny Ettle (JE-MI)")
        final_status = status_text.strip() if status_text else (existing_row[7] if len(existing_row) > 7 else "")

        row_values = [
            row_active,
            final_company,
            final_v2,
            final_voll,
            final_cockpit,
            final_source,
            final_partner,
            final_status,
        ]
        safe_range = urllib.parse.quote(f"'{tab_title}'!A{target_row_idx}:H{target_row_idx}")
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{safe_range}"
        r_put = _request_with_retry(
            "PUT",
            url,
            params={"valueInputOption": "USER_ENTERED"},
            json={"values": [row_values]},
        )
        r_put.raise_for_status()
        return {
            "ok": True,
            "action": "updated",
            "row": target_row_idx,
            "spreadsheet_url": cfg["spreadsheet_url"],
            "values": row_values,
        }
    else:
        row_active = True if active is None else bool(active)
        row_values = [
            row_active,
            company_name.strip() or clean_slug,
            v2_url.strip(),
            vollversion_url.strip(),
            cockpit_url.strip(),
            source_context.strip(),
            partner_norm,
            status_text.strip(),
        ]
        new_row_idx = len(rows) + 1
        safe_range = urllib.parse.quote(f"'{tab_title}'!A{new_row_idx}:H{new_row_idx}")
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{safe_range}"
        r_put = _request_with_retry(
            "PUT",
            url,
            params={"valueInputOption": "USER_ENTERED"},
            json={"values": [row_values]},
        )
        r_put.raise_for_status()
        apply_sheet_formatting(spreadsheet_id, sheet_id, tab_title, total_rows=new_row_idx)
        return {
            "ok": True,
            "action": "inserted",
            "row": new_row_idx,
            "spreadsheet_url": cfg["spreadsheet_url"],
            "values": row_values,
        }


def verify_sheet() -> Dict[str, Any]:
    cfg = get_sheet_config()
    spreadsheet_id = cfg["spreadsheet_id"]
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}"
    r = _request_with_retry(
        "GET",
        url,
        params={
            "includeGridData": "true",
            "ranges": f"'{DEFAULT_TAB_TITLE}'!A1:H20",
            "fields": "properties.title,sheets(properties(sheetId,title,gridProperties.frozenRowCount),basicFilter,conditionalFormats,data.rowData.values(userEnteredValue,dataValidation))",
        },
    )
    r.raise_for_status()
    meta = r.json()
    sh = (meta.get("sheets") or [{}])[0]
    row_data = ((sh.get("data") or [{}])[0]).get("rowData") or []
    checkbox_count = 0
    for r_idx, r_obj in enumerate(row_data[1:], start=2):
        vals = r_obj.get("values") or []
        if vals and (vals[0].get("dataValidation") or {}).get("condition", {}).get("type") == "BOOLEAN":
            checkbox_count += 1

    # Public HTTP check
    pub_r = requests.get(cfg["spreadsheet_url"], timeout=15)
    return {
        "ok": True,
        "title": meta.get("properties", {}).get("title"),
        "tab_title": sh.get("properties", {}).get("title"),
        "frozen_rows": sh.get("properties", {}).get("gridProperties", {}).get("frozenRowCount"),
        "has_basic_filter": bool(sh.get("basicFilter")),
        "conditional_format_rules": len(sh.get("conditionalFormats") or []),
        "total_rows": len(row_data) - 1,
        "verified_boolean_checkboxes": checkbox_count,
        "public_http_status": pub_r.status_code,
        "spreadsheet_url": cfg["spreadsheet_url"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WebPilot Google Sheets Sync")
    parser.add_argument("--init", action="store_true", help="Initialisiert & befuellt das Google Sheet")
    parser.add_argument("--verify", action="store_true", help="Prueft Checkboxen, Filter & Public Access")
    parser.add_argument("--upsert", action="store_true", help="Fuegt eine Zeile ein oder aktualisiert sie")
    parser.add_argument("--slug", type=str, default="", help="Mandanten-Slug")
    parser.add_argument("--company", type=str, default="", help="Firma / Verein")
    parser.add_argument("--v2-url", type=str, default="", help="Zeigeversion (-v2) URL")
    parser.add_argument("--voll-url", type=str, default="", help="Vollversion (-vollversion) URL")
    parser.add_argument("--cockpit-url", type=str, default="", help="Studio Cockpit v4.0 URL")
    parser.add_argument("--source", type=str, default="", help="Original-Webseite & Kontext")
    parser.add_argument("--partner", type=str, default="Jenny Ettle (JE-MI)", help="Partner")
    parser.add_argument("--status", type=str, default="", help="Status & Datum")
    args = parser.parse_args()

    if args.init:
        print(json.dumps(init_and_seed_sheet(), indent=2, ensure_ascii=False))
    elif args.verify:
        print(json.dumps(verify_sheet(), indent=2, ensure_ascii=False))
    elif args.upsert:
        res = upsert_webpilot_sheet_row(
            slug=args.slug,
            company_name=args.company,
            v2_url=args.v2_url,
            vollversion_url=args.voll_url,
            cockpit_url=args.cockpit_url,
            source_context=args.source,
            partner=args.partner,
            status_text=args.status,
        )
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print(json.dumps(verify_sheet(), indent=2, ensure_ascii=False))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
webpilot_lead_engine.py — WebPilot Smart-Anfrage & Dual-Delivery Engine
=======================================================================
Verarbeitet eingehende 3-Schritte Smart-Anfragen (preview-hochuli, preview-her11, etc.),
erzeugt das 1-seitige A4-Auftrags-PDF («Monika-&-Monteur-Blatt») via lead_pdf_generator.py
und loest die Dual-Delivery (HTML-E-Mail + PDF-Anhang & WhatsApp-Sofortmeldung) aus.
"""

import os
import re
import time
import json
import secrets
import smtplib
import urllib.parse
from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from email.message import EmailMessage
import requests

from lead_pdf_generator import generate_lead_pdf, _normalize_e164

EMBED_DIR = Path("/home/brainuser/workspaces/mxs-embed")
LEADS_DIR = EMBED_DIR / "leads"
LEAD_ROUTING_FILE = EMBED_DIR / "config" / "lead_routing.json"

def _load_supabase_creds() -> tuple[str, str]:
    url = os.environ.get("SUPABASE_URL", "https://odxbrrtpwlxxnchnoubn.supabase.co")
    key = os.environ.get("SUPABASE_KEY", "")
    if not key:
        try:
            ps = Path("/home/brainuser/workspaces/Marketing-Hiltbrand-Pro0409/scripts/publish_service.py").read_text(encoding="utf-8")
            m = re.search(r"SUPABASE_KEY\s*=\s*os\.environ\.get\([^,]+,\s*.([^\x22\x27]+).", ps)
            if m:
                key = m.group(1)
        except Exception:
            pass
    return url, key

SUPABASE_URL, SUPABASE_KEY = _load_supabase_creds()

_lead_rate_limits = {}
_smtp_cfg_cache = {"data": None, "ts": 0}


def get_smtp_config() -> dict:
    """Laedt SMTP- & E-Mail-Konfiguration inkl. Backup-SMTP aus Supabase system_config (300s Cache)."""
    now_ts = time.time()
    if _smtp_cfg_cache["data"] and (now_ts - _smtp_cfg_cache["ts"] < 300):
        return _smtp_cfg_cache["data"]
    try:
        keys = (
            "smtp_host,smtp_port,smtp_user,smtp_pass,smtp_from,"
            "smtp_backup_host,smtp_backup_port,smtp_backup_user,smtp_backup_pass,smtp_backup_from,"
            "notify_email,resend_api_key"
        )
        url = f"{SUPABASE_URL}/rest/v1/system_config?key=in.({keys})&select=key,value"
        headers = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"}
        res = requests.get(url, headers=headers, timeout=6)
        if res.status_code == 200:
            cfg = {row["key"]: str(row["value"]).strip() for row in res.json() if row.get("value") is not None}
            _smtp_cfg_cache["data"] = cfg
            _smtp_cfg_cache["ts"] = now_ts
            return cfg
    except Exception:
        pass
    return _smtp_cfg_cache["data"] or {}


def load_lead_routing() -> dict:
    if LEAD_ROUTING_FILE.exists():
        try:
            return json.loads(LEAD_ROUTING_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def compute_callback_window(urgency: str, callback_pref: str = "") -> str:
    """Berechnet ein uhrzeitabhaengiges, verbindliches Rueckruf-Versprechen (Europe/Zurich)."""
    now_ch = datetime.now(ZoneInfo("Europe/Zurich"))
    u = (urgency or "").lower()
    if "notfall" in u or "sofort" in u or "pikett" in u:
        return "Sofort-Rückruf innert 15–30 Minuten (24h-Pikett Bereitschaft)"

    weekday = now_ch.weekday()  # 0=Mo .. 6=So
    hour = now_ch.hour + now_ch.minute / 60.0

    if weekday <= 4 and 7.0 <= hour < 16.0:
        target = now_ch + timedelta(hours=2)
        mins = ((target.minute // 15) + 1) * 15
        if mins >= 60:
            target = target.replace(minute=0) + timedelta(hours=1)
        else:
            target = target.replace(minute=mins)
        return f"Heute verbindlich bis {target.strftime('%H:%M')} Uhr"

    if weekday <= 4 and 16.0 <= hour < 20.0 and ("heute" in u or "dringend" in u):
        return "Heute Abend noch bis 20:30 Uhr (Dringend-Priorität)"

    if weekday == 4 and hour >= 16.0:
        day_label = "Am Montagvormittag"
    elif weekday in (5, 6):
        day_label = "Am Montagvormittag"
    elif hour < 7.0:
        day_label = "Heute Vormittag"
    else:
        day_label = "Morgen Vormittag"

    if callback_pref and "nachmittag" in callback_pref.lower():
        return f"{day_label.replace('Vormittag', 'Nachmittag').replace('vormittag', 'nachmittag')} zwischen 13:30 und 16:00 Uhr"
    return f"{day_label} zwischen 07:30 und 10:00 Uhr"


def resolve_lead_routing_for_request(slug: str, category: str, sparte: str, urgency: str, plz: str) -> tuple[dict, dict, bool]:
    """Ermittelt Mandanten-Brand-Config, den zustaendigen Ansprechpartner und den PLZ-Einzugsgebiets-Status."""
    all_routing = load_lead_routing()
    clean_slug = re.sub(r"^preview-", "", (slug or "hochuli").strip().lower())
    client_cfg = all_routing.get(clean_slug) or all_routing.get("hochuli") or {}

    routes = client_cfg.get("routes") or {}
    default_assignee = client_cfg.get("default_assignee") or {
        "name": "Zentrale Projektleitung",
        "role": "Kundenberatung",
        "department": sparte or category or "Allgemein",
        "phone": client_cfg.get("default_phone", ""),
        "email": client_cfg.get("default_email", ""),
    }

    u_low = (urgency or "").lower()
    c_low = (category or "").lower()
    selected = None

    if clean_slug == "hochuli" and ("notfall" in u_low or "sofort" in u_low or "notfall" in c_low or "pikett" in c_low):
        pikett_route = routes.get("Notfall / Pikett") or default_assignee
        sparte_route = routes.get(sparte)
        if sparte_route and sparte != "Notfall / Pikett":
            selected = {
                "name": f"{pikett_route.get('name')} & {sparte_route.get('name')}",
                "role": f"24h-Pikett & {sparte_route.get('role')}",
                "department": f"Notfall / {sparte}",
                "phone": pikett_route.get("phone") or "062 726 11 46",
                "email": sparte_route.get("email") or client_cfg.get("default_email", ""),
            }
        else:
            selected = dict(pikett_route)
    else:
        for key_candidate in [sparte, category]:
            if key_candidate and key_candidate in routes:
                selected = dict(routes[key_candidate])
                break
        if not selected:
            for rk, rv in routes.items():
                if (sparte and rk.lower() in sparte.lower()) or (category and rk.lower() in category.lower()):
                    selected = dict(rv)
                    break
        if not selected:
            selected = dict(default_assignee)

    plz_clean = re.sub(r"\D", "", str(plz or ""))[:4]
    prefixes = client_cfg.get("service_area_plz_prefixes") or []
    if not plz_clean or not prefixes:
        in_area = True
    else:
        in_area = any(plz_clean.startswith(pref) for pref in prefixes)

    return client_cfg, selected, in_area


def _smtp_deliver_message(host: str, port: int, user: str, password: str, msg: EmailMessage, to_addrs: list[str] | None = None) -> None:
    """Versendet EmailMessage mit Dual-TLS-Weiche: Port 465 = Implicit TLS (SMTP_SSL), sonst STARTTLS."""
    port_int = int(port or 587)
    if port_int == 465:
        with smtplib.SMTP_SSL(host, port_int, timeout=15) as server:
            server.ehlo()
            server.login(user, password)
            server.send_message(msg, to_addrs=to_addrs)
    else:
        with smtplib.SMTP(host, port_int, timeout=15) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(user, password)
            server.send_message(msg, to_addrs=to_addrs)


def send_lead_email_with_pdf(
    to_emails: list[str],
    reply_to: str,
    subject: str,
    html_body: str,
    text_body: str,
    pdf_path: Path,
    pdf_filename: str,
    log_fn=None,
    company_name: str = "WebPilot",
    cc_email: str = "",
) -> tuple[bool, str]:
    """Versendet die strukturierte HTML-E-Mail samt angehaengtem 1-Seiten-PDF (Dual-TLS 465/587 + Kasserver-Fallback #BE-07)."""
    smtp_cfg = get_smtp_config()
    smtp_host = smtp_cfg.get("smtp_host") or os.environ.get("SMTP_HOST") or "w01b7af4.kasserver.com"
    smtp_port = int(smtp_cfg.get("smtp_port") or os.environ.get("SMTP_PORT") or 587)
    smtp_user = smtp_cfg.get("smtp_user") or os.environ.get("SMTP_USER") or ""
    smtp_pass = smtp_cfg.get("smtp_pass") or os.environ.get("SMTP_PASS") or ""
    smtp_from = smtp_cfg.get("smtp_from") or os.environ.get("SMTP_FROM") or "david.huegli@acp-authentic-content-pilot.com"
    fallback_notify = smtp_cfg.get("notify_email") or "david.huegli@magnet-xs.com"

    backup_host = smtp_cfg.get("smtp_backup_host") or os.environ.get("SMTP_BACKUP_HOST") or "w01b7af4.kasserver.com"
    backup_port = int(smtp_cfg.get("smtp_backup_port") or os.environ.get("SMTP_BACKUP_PORT") or 587)
    backup_user = smtp_cfg.get("smtp_backup_user") or os.environ.get("SMTP_BACKUP_USER") or "m07d99e5"
    backup_pass = smtp_cfg.get("smtp_backup_pass") or os.environ.get("SMTP_BACKUP_PASS") or ""
    backup_from = smtp_cfg.get("smtp_backup_from") or os.environ.get("SMTP_BACKUP_FROM") or smtp_from

    real_recipients = []
    for em in (to_emails or []):
        em_clean = str(em or "").strip()
        if not em_clean or "@" not in em_clean:
            continue
        dom = em_clean.split("@", 1)[1].lower()
        if dom in ("example.com", "example.ch", "example.org", "test.ch", "test.local", "invalid", "localhost"):
            if fallback_notify not in real_recipients:
                real_recipients.append(fallback_notify)
        else:
            if em_clean not in real_recipients:
                real_recipients.append(em_clean)

    if not real_recipients:
        real_recipients = [fallback_notify]

    if (not smtp_user or not smtp_pass) and (not backup_user or not backup_pass):
        return False, "missing_smtp_credentials"

    clean_company = (
        str(company_name or "WebPilot")
        .replace("\r", " ")
        .replace("\n", " ")
        .replace('"', "")
        .replace("\u00df", "ss")
        .strip()
        or "WebPilot"
    )

    cc_recipients = []
    if cc_email:
        raw_ccs = cc_email if isinstance(cc_email, list) else str(cc_email).split(",")
        for ce in raw_ccs:
            ce_clean = str(ce or "").strip()
            if not ce_clean or "@" not in ce_clean:
                continue
            dom = ce_clean.split("@", 1)[1].lower()
            if dom not in ("example.com", "example.ch", "example.org", "test.ch", "test.local", "invalid", "localhost"):
                if ce_clean not in cc_recipients:
                    cc_recipients.append(ce_clean)

    envelope_recipients = list(real_recipients)
    for ce in cc_recipients:
        if ce not in envelope_recipients:
            envelope_recipients.append(ce)

    msg = EmailMessage()
    msg["Subject"] = subject.replace("\u00df", "ss")
    msg["From"] = f"{clean_company} — Smart-Anfrage <{smtp_from}>"
    msg["To"] = ", ".join(real_recipients)
    if cc_recipients:
        msg["Cc"] = ", ".join(cc_recipients)
    if reply_to and "@" in reply_to:
        msg["Reply-To"] = reply_to

    msg.set_content(text_body.replace("\u00df", "ss"))
    msg.add_alternative(html_body.replace("\u00df", "ss"), subtype="html")

    if pdf_path and pdf_path.exists():
        pdf_bytes = pdf_path.read_bytes()
        msg.add_attachment(
            pdf_bytes,
            maintype="application",
            subtype="pdf",
            filename=pdf_filename,
        )

    last_err = ""
    if smtp_user and smtp_pass:
        for attempt in range(2):
            try:
                _smtp_deliver_message(smtp_host, smtp_port, smtp_user, smtp_pass, msg, to_addrs=envelope_recipients)
                if log_fn:
                    log_fn("webpilot-lead", "EMAIL_OK", "SENT", f"via={smtp_host}:{smtp_port} from={clean_company} to={real_recipients} cc={cc_recipients} pdf={pdf_filename}")
                return True, "sent_smtp"
            except Exception as ex:
                last_err = str(ex)
                time.sleep(1.0 * (attempt + 1))

    # Automatischer Fallback auf Kasserver-SMTP (w01b7af4.kasserver.com:587)
    if backup_host and backup_user and backup_pass and (backup_host != smtp_host or backup_port != smtp_port or backup_user != smtp_user):
        try:
            msg.replace_header("From", f"{clean_company} — Smart-Anfrage <{backup_from}>")
            _smtp_deliver_message(backup_host, backup_port, backup_user, backup_pass, msg, to_addrs=envelope_recipients)
            if log_fn:
                log_fn("webpilot-lead", "EMAIL_FALLBACK_OK", "WARN", f"primary_err={last_err} fallback={backup_host}:{backup_port} to={real_recipients} cc={cc_recipients}")
            return True, "sent_smtp_fallback"
        except Exception as fb_ex:
            last_err = f"primary({smtp_host}:{smtp_port}): {last_err} | fallback({backup_host}:{backup_port}): {fb_ex}"

    if log_fn:
        log_fn("webpilot-lead", "EMAIL_ERR", "FAIL", f"to={real_recipients} err={last_err}")
    return False, last_err


def format_lead_whatsapp_message(lead_data: dict, brand_cfg: dict) -> str:
    """Erstellt den praegnanten WhatsApp-Sofortmeldungs-Text inkl. Direktlink zum 1-Seiten-PDF & wa.me Antwortlink."""
    company_name = brand_cfg.get("company_name") or "WebPilot"
    ref_code = lead_data.get("ref_code") or "#WP-2026"
    urgency = lead_data.get("urgency") or "Planbar"
    sparte = lead_data.get("sparte") or lead_data.get("category") or "Allgemein"
    category = lead_data.get("category") or "Anfrage"
    assigned_to = lead_data.get("assigned_to") or "Projektleitung"
    visitor_name = lead_data.get("name") or "Kunde"
    visitor_company = lead_data.get("company") or ""
    visitor_phone = lead_data.get("phone") or ""
    plz_city = f"{lead_data.get('plz', '')} {lead_data.get('city', '')}".strip() or "Schweiz"
    in_area = lead_data.get("in_service_area", True)
    area_txt = "Im Einzugsgebiet" if in_area else "Standort prüfen"
    callback_window = lead_data.get("callback_window") or "Zeitnah"
    msg_short = re.sub(r"\s+", " ", str(lead_data.get("message") or "Keine Zusatznotiz")).strip()
    if len(msg_short) > 160:
        msg_short = msg_short[:157] + "..."
    photo_count = int(lead_data.get("photo_count") or 0)
    pdf_url = lead_data.get("pdf_url") or ""

    e164_digits = re.sub(r"\D", "", _normalize_e164(visitor_phone))
    reply_prefill = urllib.parse.quote(
        f"Guten Tag {visitor_name}, vielen Dank für Ihre Anfrage ({ref_code}) bei {company_name}. Wir haben Ihr Auftragsblatt erhalten und melden uns wie versprochen ({callback_window})."
    )
    wa_reply_url = f"https://wa.me/{e164_digits}?text={reply_prefill}"

    lines = [
        f"🔔 *NEUE SMART-ANFRAGE ({ref_code})*",
        f"🏢 *Mandant:* {company_name}",
        f"⚡ *Dringlichkeit:* {urgency}",
        f"📍 *Ort:* {plz_city} ({area_txt})",
        f"🧭 *Zuständig:* {assigned_to}",
        f"🔧 *Bereich:* {sparte} ({category})",
        "━━━━━━━━━━━━━━━━━━━━",
        f"👤 *Kunde:* {visitor_name}" + (f" ({visitor_company})" if visitor_company else ""),
        f"📞 *Telefon:* {visitor_phone}",
        f"🕒 *Rückruf-Garantie:* {callback_window}",
        f"📷 *Fotos im PDF:* {photo_count} Aufnahme(n) eingebettet",
        f"💬 *Nachricht:* «{msg_short}»",
        "━━━━━━━━━━━━━━━━━━━━",
        f"📄 *1-Seiten-Auftrags-PDF (mit QR-Codes & Fotos) öffnen:*",
        f"{pdf_url}",
        "",
        f"👉 *1-Klick WhatsApp-Antwort an Kunde:*",
        f"{wa_reply_url}",
    ]
    return "\n".join(lines).replace("\u00df", "ss")


def build_lead_email_html(lead_data: dict, brand_cfg: dict) -> tuple[str, str]:
    """Erzeugt HTML- & Plaintext-Body fuer die Auftrags-E-Mail."""
    company_name = brand_cfg.get("company_name") or "WebPilot"
    primary_rgb = brand_cfg.get("primary_color") or [227, 6, 19]
    dark_rgb = brand_cfg.get("dark_color") or [15, 23, 42]
    primary_hex = "#{:02x}{:02x}{:02x}".format(*primary_rgb)
    dark_hex = "#{:02x}{:02x}{:02x}".format(*dark_rgb)

    ref_code = lead_data.get("ref_code")
    assigned_to = lead_data.get("assigned_to")
    sparte = lead_data.get("sparte") or lead_data.get("category")
    category = lead_data.get("category")
    urgency = lead_data.get("urgency")
    callback_window = lead_data.get("callback_window")
    name = lead_data.get("name")
    company = lead_data.get("company") or "–"
    phone = lead_data.get("phone")
    email = lead_data.get("email") or "–"
    street = lead_data.get("street") or "–"
    plz_city = f"{lead_data.get('plz', '')} {lead_data.get('city', '')}".strip() or "–"
    msg_txt = lead_data.get("message") or "–"
    pdf_url = lead_data.get("pdf_url")
    photo_count = int(lead_data.get("photo_count") or 0)

    extra_rows_html = ""
    extra_fields = lead_data.get("extra_fields") or {}
    if isinstance(extra_fields, dict):
        for ek, ev in extra_fields.items():
            if ev and str(ev).strip():
                extra_rows_html += (
                    f'<tr><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#475569;font-weight:600;width:38%;">{ek}</td>'
                    f'<td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#0f172a;">{ev}</td></tr>'
                )

    html_body = f"""<!DOCTYPE html>
<html lang="de-CH">
<body style="margin:0;padding:20px;background:#f1f5f9;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:#0f172a;">
  <div style="max-width:640px;margin:0 auto;background:#ffffff;border-radius:8px;overflow:hidden;border:1px solid #cbd5e1;">
    <div style="background:{dark_hex};color:#ffffff;padding:20px 24px;border-bottom:4px solid {primary_hex};">
      <div style="font-size:11px;text-transform:uppercase;letter-spacing:0.08em;color:#cbd5e1;font-weight:700;">STRUKTURIERTES AUFTRAGS- &amp; ANFRAGE-DOSSIER · {ref_code}</div>
      <h1 style="margin:6px 0 4px 0;font-size:20px;color:#ffffff;">{company_name}</h1>
      <div style="font-size:13px;color:#e2e8f0;">Zuständig: <strong>{assigned_to}</strong> ({sparte})</div>
    </div>
    <div style="padding:20px 24px;">
      <div style="margin-bottom:16px;">
        <span style="display:inline-block;background:{primary_hex};color:#ffffff;padding:4px 10px;border-radius:4px;font-size:12px;font-weight:700;margin-right:6px;">Dringlichkeit: {urgency}</span>
        <span style="display:inline-block;background:#059669;color:#ffffff;padding:4px 10px;border-radius:4px;font-size:12px;font-weight:700;margin-right:6px;">PLZ/Ort: {plz_city}</span>
        <span style="display:inline-block;background:#0f172a;color:#ffffff;padding:4px 10px;border-radius:4px;font-size:12px;font-weight:700;">Fotos im PDF: {photo_count}</span>
      </div>
      <p style="margin:0 0 16px 0;font-size:14px;line-height:1.5;color:#334155;">
        Das druckfertige <strong>1-Seiten-Auftrags-PDF («Monika-&amp;-Monteur-Blatt»)</strong> inklusive eingebetteter Kundenfotos und 2 scannbaren Praxis-QR-Codes (Direkt-Anruf &amp; Google Maps Route) befindet sich direkt im Anhang dieser E-Mail.
      </p>
      <table style="width:100%;border-collapse:collapse;font-size:13.5px;margin-bottom:18px;border:1px solid #e2e8f0;">
        <tr style="background:#f8fafc;">
          <td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#475569;font-weight:600;width:38%;">Kontaktperson</td>
          <td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#0f172a;font-weight:700;">{name}</td>
        </tr>
        <tr>
          <td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#475569;font-weight:600;">Firma / Verein</td>
          <td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#0f172a;">{company}</td>
        </tr>
        <tr style="background:#f8fafc;">
          <td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#475569;font-weight:600;">Telefon / Mobil</td>
          <td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#0f172a;font-weight:700;"><a href="tel:{_normalize_e164(phone)}" style="color:{primary_hex};text-decoration:none;">{phone}</a></td>
        </tr>
        <tr>
          <td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#475569;font-weight:600;">E-Mail-Adresse</td>
          <td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#0f172a;">{email}</td>
        </tr>
        <tr style="background:#f8fafc;">
          <td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#475569;font-weight:600;">Objekt-Adresse</td>
          <td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#0f172a;">{street}, {plz_city}</td>
        </tr>
        <tr>
          <td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#475569;font-weight:600;">Anliegen &amp; Bereich</td>
          <td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#0f172a;font-weight:700;">{category} · {sparte}</td>
        </tr>
        <tr style="background:#f8fafc;">
          <td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#475569;font-weight:600;">Rückruf-Versprechen</td>
          <td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#059669;font-weight:700;">{callback_window}</td>
        </tr>
        {extra_rows_html}
      </table>
      <div style="background:#f8fafc;border-left:4px solid {primary_hex};padding:12px 14px;border-radius:4px;margin-bottom:18px;">
        <div style="font-size:11px;font-weight:700;text-transform:uppercase;color:#475569;margin-bottom:4px;">Kundennachricht / Beschreibung</div>
        <div style="font-size:13.5px;color:#0f172a;white-space:pre-line;">{msg_txt}</div>
      </div>
      <div style="text-align:center;margin:20px 0 8px 0;">
        <a href="{pdf_url}" style="display:inline-block;background:{primary_hex};color:#ffffff;text-decoration:none;font-weight:700;font-size:14px;padding:12px 22px;border-radius:8px;">1-Seiten-Auftrags-PDF direkt öffnen</a>
      </div>
    </div>
  </div>
</body>
</html>"""

    text_body = (
        f"STRUKTURIERTES AUFTRAGS- & ANFRAGE-BLATT ({ref_code})\n"
        f"Mandant: {company_name}\n"
        f"Zuständig: {assigned_to} ({sparte})\n"
        f"Dringlichkeit: {urgency}\n"
        f"Kunde: {name} ({company})\n"
        f"Telefon: {phone} | E-Mail: {email}\n"
        f"Adresse: {street}, {plz_city}\n"
        f"Rückruf-Versprechen: {callback_window}\n\n"
        f"Nachricht:\n{msg_txt}\n\n"
        f"Direktlink zum 1-Seiten-PDF:\n{pdf_url}\n"
    )
    return html_body, text_body


def process_lead_submission(data: dict, client_ip: str, referer: str, resolve_client_dir_fn, send_partner_whatsapp_fn, log_fn) -> tuple[dict, int]:
    """Haupt-Controller fuer POST /api/lead-submit."""
    if str(data.get("website_url") or data.get("_hp") or "").strip():
        return {"ok": True, "spam_ignored": True}, 200

    now_ts = time.time()
    ip_hist = [t for t in _lead_rate_limits.get(client_ip, []) if now_ts - t < 900]
    if len(ip_hist) >= 25:
        return {"ok": False, "error": "Zu viele Anfragen in kurzer Zeit. Bitte kurz warten."}, 429
    ip_hist.append(now_ts)
    _lead_rate_limits[client_ip] = ip_hist

    raw_slug = str(data.get("client") or data.get("client_slug") or data.get("slug") or "").strip().lower()
    if not raw_slug:
        _, raw_slug, _ = resolve_client_dir_fn(None, referer)
    clean_slug = re.sub(r"^preview-", "", raw_slug or "hochuli")

    cust = data.get("customer") if isinstance(data.get("customer"), dict) else {}
    category = str(data.get("category") or data.get("role") or data.get("type") or "Anfrage").strip()
    sparte = str(data.get("sparte") or data.get("department") or data.get("topic") or category).strip()
    urgency = str(data.get("urgency") or "Planbar / Nach Absprache").strip()
    name = str(data.get("name") or cust.get("name") or "").strip()
    company = str(data.get("company") or cust.get("company") or "").strip()
    street = str(data.get("street") or cust.get("street") or "").strip()
    plz = str(data.get("plz") or cust.get("plz") or cust.get("plz_city") or "").strip()
    city = str(data.get("city") or cust.get("city") or "").strip()
    if plz and not city and " " in plz:
        parts = plz.split(None, 1)
        if re.match(r"^\d{4,5}$", parts[0]):
            plz, city = parts[0], parts[1]
    email = str(data.get("email") or cust.get("email") or "").strip()
    phone = str(data.get("phone") or cust.get("phone") or "").strip()
    callback_pref = str(data.get("callback_pref") or cust.get("callback_pref") or "").strip()
    message = str(data.get("message") or data.get("description") or "").strip()
    raw_extra = data.get("extra_fields") if isinstance(data.get("extra_fields"), dict) else (data.get("details") if isinstance(data.get("details"), dict) else {})
    extra_fields = dict(raw_extra)
    raw_photos = data.get("photos") if isinstance(data.get("photos"), list) else (data.get("photos_base64") if isinstance(data.get("photos_base64"), list) else [])
    photos = list(raw_photos)

    if not name or (not phone and not email):
        return {"ok": False, "error": "Bitte Name sowie Telefonnummer oder E-Mail-Adresse angeben."}, 400

    brand_cfg, route_target, in_service_area = resolve_lead_routing_for_request(
        clean_slug, category, sparte, urgency, plz
    )
    assigned_person = route_target.get("name") or "Zentrale Disposition"
    assigned_role = route_target.get("role") or ""
    assigned_full = f"{assigned_person} — {assigned_role}" if assigned_role else assigned_person
    callback_window = compute_callback_window(urgency, callback_pref)

    now_ch = datetime.now(ZoneInfo("Europe/Zurich"))
    rand_num = secrets.randbelow(9000) + 1000
    ref_code = f"#WP-2026-{rand_num}"
    lead_id = f"lead_{clean_slug}_{now_ch.strftime('%Y%m%d_%H%M%S')}_{rand_num}"
    sec_token = secrets.token_hex(8)

    public_origin = "https://vorschau.magnet-xs.ch"
    pdf_url = f"{public_origin}/api/lead-pdf/{lead_id}.pdf?t={sec_token}"

    lead_record = {
        "lead_id": lead_id,
        "ref_code": ref_code,
        "token": sec_token,
        "client_slug": clean_slug,
        "created_at": now_ch.isoformat(),
        "created_at_display": now_ch.strftime("%d.%m.%Y, %H:%M Uhr"),
        "category": category,
        "sparte": sparte,
        "urgency": urgency,
        "assigned_to": assigned_person,
        "assigned_role": assigned_role,
        "assigned_full": assigned_full,
        "name": name,
        "company": company,
        "street": street,
        "plz": plz,
        "city": city,
        "in_service_area": in_service_area,
        "email": email,
        "phone": phone,
        "callback_pref": callback_pref,
        "callback_window": callback_window,
        "message": message,
        "extra_fields": extra_fields,
        "photo_count": min(len(photos), 3),
        "pdf_url": pdf_url,
    }

    LEADS_DIR.mkdir(parents=True, exist_ok=True)
    pdf_path = LEADS_DIR / f"{lead_id}.pdf"
    meta_path = LEADS_DIR / f"{lead_id}.json"

    pdf_input = dict(lead_record)
    pdf_input["photos"] = photos[:3]
    generate_lead_pdf(pdf_input, brand_cfg, pdf_path)
    meta_path.write_text(json.dumps(lead_record, indent=2, ensure_ascii=False), encoding="utf-8")

    whatsapp_preview_text = format_lead_whatsapp_message(lead_record, brand_cfg)

    route_email = str(route_target.get("email") or "").strip()
    cc_email = str(route_target.get("cc_email") or data.get("cc_email") or "").strip()
    lead_record["assigned_email"] = route_email
    lead_record["cc_email"] = cc_email
    meta_path.write_text(json.dumps(lead_record, indent=2, ensure_ascii=False), encoding="utf-8")

    target_emails = []
    if clean_slug == "webpilot_partner" and route_email and "@" in route_email:
        if data.get("self_test_mode"):
            target_emails.append(cc_email or "david.huegli@magnet-xs.ch")
        else:
            target_emails.append(route_email)
    if email and "@" in email and email not in target_emails:
        target_emails.append(email)

    html_body, text_body = build_lead_email_html(lead_record, brand_cfg)
    pdf_filename = f"Auftrag_{ref_code.lstrip('#')}_{clean_slug.upper()}.pdf"
    subj = f"[{urgency.upper()}] Neue Smart-Anfrage {ref_code} · {brand_cfg.get('company_name', clean_slug)} ({sparte})"
    email_sent, email_status = send_lead_email_with_pdf(
        to_emails=target_emails,
        reply_to=email or route_email,
        subject=subj,
        html_body=html_body,
        text_body=text_body,
        pdf_path=pdf_path,
        pdf_filename=pdf_filename,
        log_fn=log_fn,
        company_name=brand_cfg.get("company_name") or clean_slug.upper(),
        cc_email=cc_email,
    )

    whatsapp_sent = False
    whatsapp_status = "skipped_no_mobile"
    digits_only = re.sub(r"\D", "", _normalize_e164(phone))
    is_synthetic_phone = any(pat in digits_only for pat in ("00000", "123456", "999999", "111111"))
    is_swiss_mobile = digits_only.startswith(("4175", "4176", "4177", "4178", "4179")) and len(digits_only) == 11
    is_intl_mobile = len(digits_only) >= 10 and not digits_only.startswith("4162") and not is_synthetic_phone

    if (is_swiss_mobile or is_intl_mobile) and not is_synthetic_phone and not data.get("skip_whatsapp_live"):
        wa_res = send_partner_whatsapp_fn([phone], whatsapp_preview_text)
        whatsapp_sent = bool(wa_res.get("whatsapp_delivered") or wa_res.get("ok"))
        whatsapp_status = "sent_evolution" if whatsapp_sent else str(wa_res.get("error") or "failed")
    elif is_synthetic_phone:
        whatsapp_status = "simulated_test_number"

    try:
        sb_payload = {
            "lead_id": lead_id,
            "lead_ref": ref_code,
            "client_slug": clean_slug,
            "source_page": str(data.get("source_page") or "kontakt.html"),
            "category_key": re.sub(r"[^a-z0-9_]+", "_", category.lower()).strip("_") or "anfrage",
            "category_label": category,
            "sparte_label": sparte,
            "urgency": urgency,
            "assigned_person": assigned_full,
            "visitor_name": name,
            "visitor_company": company,
            "visitor_phone": phone,
            "visitor_email": email,
            "visitor_plz": plz,
            "visitor_city": city,
            "visitor_street": street,
            "in_service_area": in_service_area,
            "callback_window_pref": callback_pref,
            "promised_callback_text": callback_window,
            "description": message,
            "extra_fields": extra_fields,
            "photo_count": min(len(photos), 3),
            "pdf_url": pdf_url,
            "email_delivery_status": email_status,
            "whatsapp_delivery_status": whatsapp_status,
            "is_preview_test": True,
        }
        requests.post(
            f"{SUPABASE_URL}/rest/v1/webpilot_leads",
            headers={
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "application/json",
            },
            json=sb_payload,
            timeout=5,
        )
    except Exception as ex:
        if log_fn:
            log_fn(clean_slug, "LEAD_DB_WARN", "WARN", str(ex))

    if log_fn:
        log_fn(clean_slug, "LEAD_SUBMIT", "OK", f"ref={ref_code} to={assigned_person} email={email_sent} wa={whatsapp_sent}")

    return {
        "ok": True,
        "lead_id": lead_id,
        "ref_code": ref_code,
        "pdf_url": pdf_url,
        "assigned_to": assigned_full,
        "assigned_person": assigned_person,
        "assigned_role": assigned_role,
        "assigned_email": route_email,
        "cc_email": cc_email,
        "in_service_area": in_service_area,
        "callback_window": callback_window,
        "email_sent": email_sent,
        "email_status": email_status,
        "whatsapp_sent": whatsapp_sent,
        "whatsapp_status": whatsapp_status,
        "whatsapp_preview_text": whatsapp_preview_text,
    }, 200


TEAM_SUBMISSIONS_DIR = EMBED_DIR / "team_submissions"


def _slugify_filename_part(val: str) -> str:
    s = str(val or "").strip().lower()
    for k, v in [("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("é", "e"), ("è", "e"), ("ê", "e"), ("à", "a"), ("á", "a"), ("ç", "c")]:
        s = s.replace(k, v)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "unbekannt"


def process_team_submission(
    data: dict,
    client_ip: str = "unknown",
    referer: str = "",
    log_fn=None,
) -> tuple[dict, int]:
    """
    Verarbeitet eine Mannschafts-Daten & Kader-Einreichung (POST /api/team-submit).
    Speichert zeitgestempelte JSON-Datei + latest_<site_id>_<team_slug>.json unter team_submissions/.
    """
    if not isinstance(data, dict):
        return {"ok": False, "error": "Ungueltiges JSON-Payload."}, 400

    rights_confirmed = bool(data.get("rights_confirmed"))
    if not rights_confirmed:
        return {
            "ok": False,
            "error": "Bitte bestaetigen Sie die Nutzungsrechte und das Einverstaendnis der abgebildeten Personen.",
        }, 400

    raw_site = str(data.get("site_id") or data.get("client_slug") or "scfulenbach").strip().lower()
    site_id = re.sub(r"^preview-", "", raw_site)
    site_id = re.sub(r"[^a-z0-9_-]", "", site_id) or "scfulenbach"

    club_name = str(data.get("club_name") or site_id.upper()).strip()
    raw_team_slug = str(data.get("team_slug") or data.get("team_name") or "1-mannschaft").strip()
    team_slug = _slugify_filename_part(raw_team_slug)
    team_name = str(data.get("team_name") or team_slug).strip()
    league = str(data.get("league") or "").strip()
    sfv_link = str(data.get("sfv_link") or "").strip()
    team_motto = str(data.get("team_motto") or "").strip()
    training_times = str(data.get("training_times") or "").strip()
    pitch_location = str(data.get("pitch_location") or "").strip()
    winter_note = str(data.get("winter_note") or "").strip()
    team_sponsor = str(data.get("team_sponsor") or "").strip()
    submitter_name = str(data.get("submitter_name") or "").strip()
    submitter_contact = str(data.get("submitter_email_or_phone") or data.get("submitter_contact") or "").strip()

    team_photo_meta = data.get("team_photo_meta") if isinstance(data.get("team_photo_meta"), dict) else {}
    target_team_photo = str(
        team_photo_meta.get("target_filename")
        or f"{site_id}_{team_slug}_teamfoto.webp"
    ).strip()
    team_photo_meta["target_filename"] = target_team_photo

    raw_staff = data.get("staff") if isinstance(data.get("staff"), list) else []
    clean_staff = []
    auto_renamed_files = []

    if team_photo_meta.get("has_new_upload") or team_photo_meta.get("original_filename") or team_photo_meta.get("preview_src"):
        auto_renamed_files.append(target_team_photo)

    for idx, st in enumerate(raw_staff[:12]):
        if not isinstance(st, dict):
            continue
        role = str(st.get("role") or "Trainer").strip()
        name = str(st.get("name") or "").strip()
        if not name:
            continue
        phone = str(st.get("phone") or "").strip()
        email = str(st.get("email") or "").strip()
        orig_fn = str(st.get("original_filename") or "").strip()
        role_slug = _slugify_filename_part(role)
        name_slug = _slugify_filename_part(name)
        target_fn = str(st.get("target_filename") or f"{site_id}_{team_slug}_{role_slug}_{name_slug}.webp").strip()
        has_photo = bool(st.get("has_photo") or orig_fn or st.get("photo"))
        if has_photo and target_fn not in auto_renamed_files:
            auto_renamed_files.append(target_fn)
        clean_staff.append({
            "role": role,
            "name": name,
            "phone": phone,
            "email": email,
            "has_photo": has_photo,
            "original_filename": orig_fn,
            "target_filename": target_fn,
        })

    raw_players = data.get("players") if isinstance(data.get("players"), list) else []
    clean_players = []
    for idx, pl in enumerate(raw_players[:60]):
        if not isinstance(pl, dict):
            continue
        num_raw = str(pl.get("number") or "").strip()
        name = str(pl.get("name") or "").strip()
        if not name and not num_raw:
            continue
        pos = str(pl.get("position") or "").strip()
        orig_fn = str(pl.get("original_filename") or "").strip()
        num_slug = num_raw.zfill(2) if num_raw.isdigit() else (_slugify_filename_part(num_raw) if num_raw else f"{idx+1:02d}")
        name_slug = _slugify_filename_part(name or f"spieler-{num_slug}")
        target_fn = str(pl.get("target_filename") or f"{site_id}_{team_slug}_{num_slug}_{name_slug}.webp").strip()
        has_photo = bool(pl.get("has_photo") or orig_fn)
        if (has_photo or idx < 5) and target_fn not in auto_renamed_files:
            auto_renamed_files.append(target_fn)
        clean_players.append({
            "number": num_raw,
            "name": name,
            "position": pos,
            "has_photo": has_photo,
            "parsed_from_filename": bool(pl.get("parsed_from_filename")),
            "original_filename": orig_fn,
            "target_filename": target_fn,
        })

    now_ch = datetime.now(ZoneInfo("Europe/Zurich"))
    ts_str = now_ch.strftime("%Y%m%d_%H%M%S")
    submission_id = f"TEAM-{ts_str}-{secrets.token_hex(2).upper()}"

    TEAM_SUBMISSIONS_DIR.mkdir(parents=True, exist_ok=True)
    ts_filename = f"{site_id}_{team_slug}_{ts_str}.json"
    latest_filename = f"latest_{site_id}_{team_slug}.json"
    ts_path = TEAM_SUBMISSIONS_DIR / ts_filename
    latest_path = TEAM_SUBMISSIONS_DIR / latest_filename

    record = {
        "submission_id": submission_id,
        "timestamp": now_ch.isoformat(),
        "site_id": site_id,
        "club_name": club_name,
        "team_slug": team_slug,
        "team_name": team_name,
        "league": league,
        "sfv_link": sfv_link,
        "team_motto": team_motto,
        "training_times": training_times,
        "pitch_location": pitch_location,
        "winter_note": winter_note,
        "team_photo_meta": team_photo_meta,
        "staff": clean_staff,
        "staff_count": len(clean_staff),
        "players": clean_players,
        "player_count": len(clean_players),
        "team_sponsor": team_sponsor,
        "submitter_name": submitter_name,
        "submitter_email_or_phone": submitter_contact,
        "rights_confirmed": True,
        "auto_renamed_files": auto_renamed_files,
        "partner_name": "Jenny Ettle (JE-MI)",
        "client_ip": client_ip,
        "referer": referer,
    }

    payload_json = json.dumps(record, indent=2, ensure_ascii=False)
    ts_path.write_text(payload_json, encoding="utf-8")
    latest_path.write_text(payload_json, encoding="utf-8")

    if log_fn:
        log_fn(
            site_id,
            "TEAM_SUBMIT",
            "OK",
            f"id={submission_id} team={team_slug} staff={len(clean_staff)} players={len(clean_players)}",
        )

    return {
        "ok": True,
        "submission_id": submission_id,
        "site_id": site_id,
        "club_name": club_name,
        "team_slug": team_slug,
        "team_name": team_name,
        "staff_count": len(clean_staff),
        "player_count": len(clean_players),
        "auto_renamed_files": auto_renamed_files,
        "saved_file": f"team_submissions/{ts_filename}",
        "latest_file": f"team_submissions/{latest_filename}",
        "partner_name": "Jenny Ettle (JE-MI)",
        "timestamp": now_ch.isoformat(),
    }, 200

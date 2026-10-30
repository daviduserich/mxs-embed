#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lead_pdf_generator.py — WebPilot 1-Seiten-A4-PDF-Generator («Das Monika-&-Monteur-Blatt»)
=========================================================================================
Erzeugt in < 150 ms ein druckfertiges, exakt 1-seitiges A4-Auftrags- & Anfrage-Blatt
im jeweiligen Mandanten-Markendesign (Hochuli / HER11 / WebPilot) mit:
- Mandanten-Logo, Referenz-ID (#WP-2026-XXXX) & Eingangszeitstempel
- 3 farbigen Status-Badges (Dringlichkeit, Einzugsgebiet, Zustaendigkeit/Routing)
- 2-spaltigem Kunden- & Fach-Steckbrief + Kundennachricht
- Bis zu 3 direkt auf derselben A4-Seite eingebetteten Kundenfotos (Typenschild/Schaden/Raum)
- 2 scannbaren Praxis-QR-Codes unten rechts (QR 1: Direkt-Anruf tel:..., QR 2: Google Maps Route)
- Buero-/Monteur-Checkliste unten links
"""

import io
import os
import re
import base64
import tempfile
import urllib.parse
from datetime import datetime
from pathlib import Path
from fpdf import FPDF
from PIL import Image, ImageOps
import qrcode


def _pdf_safe(text: str) -> str:
    """Konvertiert beliebigen UTF-8 Text sicher in CP1252/Latin-1 fuer FPDF Core-Fonts (100% ss)."""
    if text is None:
        return ""
    s = str(text).replace("\u00df", "ss").replace("\u1e9e", "SS")
    replacements = {
        "\u2014": " - ",
        "\u2013": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2022": "·",
        "\u2026": "...",
        "\u2192": "->",
        "\u2713": "[x]",
        "\u2714": "[x]",
        "\u2705": "[OK]",
        "\u26a1": "",
        "\U0001f6a8": "[!]",
        "\U0001f527": "",
        "\U0001f4d0": "",
        "\U0001f6e1": "",
        "\ufe0f": "",
    }
    for k, v in replacements.items():
        s = s.replace(k, v)
    # Entferne sonstige Emojis / Nicht-Latin-1 Zeichen sauber
    out = []
    for ch in s:
        try:
            ch.encode("latin-1")
            out.append(ch)
        except UnicodeEncodeError:
            out.append(" ")
    return re.sub(r"[ \t]+", " ", "".join(out)).strip()


def _truncate(text: str, max_len: int = 80) -> str:
    s = _pdf_safe(text)
    if len(s) <= max_len:
        return s
    return s[: max_len - 3].rstrip() + "..."


def _normalize_e164(phone: str) -> str:
    raw = re.sub(r"[^\d+]", "", str(phone or ""))
    digits = re.sub(r"\D", "", raw)
    if not digits:
        return "+41627390020"
    if digits.startswith("00"):
        digits = digits[2:]
    elif digits.startswith("0") and len(digits) == 10:
        digits = "41" + digits[1:]
    elif not digits.startswith("41") and len(digits) == 9:
        digits = "41" + digits
    return "+" + digits


def _urgency_badge_style(urgency: str) -> tuple[str, tuple[int, int, int], tuple[int, int, int]]:
    u = (urgency or "").lower()
    if "notfall" in u or "sofort" in u or "pikett" in u:
        return "[NOTFALL / SOFORT]", (220, 38, 38), (255, 255, 255)
    if "heute" in u or "dringend" in u:
        return "[DRINGEND: HEUTE]", (234, 88, 12), (255, 255, 255)
    if "woche" in u or "zeitnah" in u:
        return "[DIESE WOCHE]", (2, 132, 199), (255, 255, 255)
    return "[PLANBAR / OFFERTE]", (5, 150, 105), (255, 255, 255)


def _decode_and_prepare_photo(photo_item, dst_path: Path) -> tuple[bool, str]:
    """Dekodiert ein Base64-Bild (oder Dateipfad), korrigiert EXIF und speichert ein kompaktes RGB-JPEG."""
    try:
        raw_bytes = None
        label = "Kundenfoto"
        if isinstance(photo_item, dict):
            label = str(photo_item.get("name") or photo_item.get("label") or "Kundenfoto")
            b64 = str(photo_item.get("data") or photo_item.get("data_url") or photo_item.get("base64") or "")
        else:
            b64 = str(photo_item or "")

        if not b64:
            return False, label

        if os.path.isfile(b64):
            im = Image.open(b64)
        else:
            if "," in b64:
                b64 = b64.split(",", 1)[1]
            raw_bytes = base64.b64decode(b64)
            im = Image.open(io.BytesIO(raw_bytes))

        im = ImageOps.exif_transpose(im)
        if im.mode in ("RGBA", "LA", "P"):
            bg = Image.new("RGB", im.size, (255, 255, 255))
            if im.mode == "P":
                im = im.convert("RGBA")
            bg.paste(im, mask=im.split()[-1] if im.mode in ("RGBA", "LA") else None)
            im = bg
        elif im.mode != "RGB":
            im = im.convert("RGB")

        im.thumbnail((900, 675), Image.Resampling.LANCZOS)
        im.save(str(dst_path), format="JPEG", quality=84, optimize=True)
        return True, _truncate(label, 28)
    except Exception:
        return False, "Foto"


def _make_qr_image(data_str: str, dst_path: Path, fill_rgb: tuple[int, int, int] = (15, 23, 42)):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=8,
        border=1,
    )
    qr.add_data(data_str)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_rgb, back_color="white").convert("RGB")
    img.save(str(dst_path), format="PNG")


def generate_lead_pdf(lead_data: dict, brand_cfg: dict, output_pdf_path: str | Path) -> Path:
    """
    Erzeugt das exakt 1-seitige A4-Auftragsblatt und speichert es unter output_pdf_path.
    """
    out_path = Path(output_pdf_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    primary_rgb = tuple(brand_cfg.get("primary_color") or [227, 6, 19])
    dark_rgb = tuple(brand_cfg.get("dark_color") or [15, 23, 42])
    company_name = _pdf_safe(brand_cfg.get("company_name") or "WebPilot Mandant")
    brand_subtitle = _pdf_safe(brand_cfg.get("brand_subtitle") or "Strukturierter Kundenauftrag")
    logo_path = brand_cfg.get("logo_path") or ""
    logo_white_bg = bool(brand_cfg.get("logo_white_bg", True))

    ref_code = _pdf_safe(lead_data.get("ref_code") or "#WP-2026-0001")
    created_at_str = _pdf_safe(lead_data.get("created_at_display") or datetime.now().strftime("%d.%m.%Y, %H:%M Uhr"))

    urgency_raw = str(lead_data.get("urgency") or "Planbar / Nach Absprache")
    urg_text, urg_bg, urg_fg = _urgency_badge_style(urgency_raw)

    in_area = bool(lead_data.get("in_service_area", True))
    area_badge_text = _pdf_safe(
        "[IM EINZUGSGEBIET]" if in_area else "[STANDORT PRÜFEN]"
    )
    area_bg = (5, 150, 105) if in_area else (217, 119, 6)

    assigned_to = _pdf_safe(lead_data.get("assigned_to") or "Zentrale Disposition")
    assigned_role = _pdf_safe(lead_data.get("assigned_role") or "")
    sparte_label = _pdf_safe(lead_data.get("sparte") or lead_data.get("department") or "Allgemein")
    category_label = _pdf_safe(lead_data.get("category") or lead_data.get("role") or "Anfrage")

    visitor_name = _pdf_safe(lead_data.get("name") or "Kunde")
    visitor_company = _pdf_safe(lead_data.get("company") or "-")
    visitor_phone = _pdf_safe(lead_data.get("phone") or "-")
    visitor_email = _pdf_safe(lead_data.get("email") or "-")
    visitor_street = _pdf_safe(lead_data.get("street") or "-")
    visitor_plz = _pdf_safe(lead_data.get("plz") or "")
    visitor_city = _pdf_safe(lead_data.get("city") or "")
    plz_city = f"{visitor_plz} {visitor_city}".strip() or "-"
    callback_window = _pdf_safe(lead_data.get("callback_window") or "Zeitnah")
    message_text = _pdf_safe(lead_data.get("message") or "Keine zusätzliche Nachricht angegeben.")
    extra_fields = lead_data.get("extra_fields") or {}

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_margins(12, 10, 12)
    pdf.set_auto_page_break(False)
    pdf.add_page()

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        # ── 1. KOPFZEILE (0..33mm) ──────────────────────────────────────────────
        pdf.set_fill_color(*dark_rgb)
        pdf.rect(0, 0, 210, 32, "F")
        pdf.set_fill_color(*primary_rgb)
        pdf.rect(0, 32, 210, 2.2, "F")

        text_start_x = 12.0
        if logo_path and os.path.isfile(logo_path):
            try:
                logo_im = Image.open(logo_path)
                lw, lh = logo_im.size
                if logo_white_bg:
                    pdf.set_fill_color(255, 255, 255)
                    pdf.rect(12, 6, 42, 20, "F")
                    # Fit inside 38x16
                    ratio = min(38.0 / lw, 16.0 / lh)
                    draw_w = lw * ratio
                    draw_h = lh * ratio
                    dx = 12 + (42 - draw_w) / 2.0
                    dy = 6 + (20 - draw_h) / 2.0
                    pdf.image(logo_path, x=dx, y=dy, w=draw_w, h=draw_h)
                    text_start_x = 58.0
                else:
                    ratio = min(20.0 / lw, 20.0 / lh)
                    draw_w = lw * ratio
                    draw_h = lh * ratio
                    pdf.image(logo_path, x=12, y=6 + (20 - draw_h) / 2.0, w=draw_w, h=draw_h)
                    text_start_x = 36.0
            except Exception:
                text_start_x = 12.0

        # Titel & Mandant links neben Logo
        pdf.set_xy(text_start_x, 6.5)
        pdf.set_font("helvetica", "B", 12.5)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(95, 6, _truncate(company_name, 46), border=0)

        pdf.set_xy(text_start_x, 13.0)
        pdf.set_font("helvetica", "B", 9.5)
        pdf.set_text_color(255, 190, 140) if primary_rgb[0] > 200 and primary_rgb[2] < 50 else pdf.set_text_color(255, 140, 190)
        pdf.cell(95, 5, "STRUKTURIERTES AUFTRAGS- & ANFRAGE-BLATT", border=0)

        pdf.set_xy(text_start_x, 19.0)
        pdf.set_font("helvetica", "", 8)
        pdf.set_text_color(203, 213, 225)
        pdf.cell(95, 4.5, _truncate(brand_subtitle, 62), border=0)

        # Referenz-ID & Zeitstempel rechtsbündig
        pdf.set_xy(142, 6.5)
        pdf.set_font("helvetica", "B", 11)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(56, 6, f"REF: {ref_code}", border=0, align="R")

        pdf.set_xy(142, 13.0)
        pdf.set_font("helvetica", "", 8.5)
        pdf.set_text_color(226, 232, 240)
        pdf.cell(56, 5, f"Eingang: {created_at_str}", border=0, align="R")

        pdf.set_xy(142, 18.8)
        pdf.set_font("helvetica", "B", 7.5)
        pdf.set_text_color(148, 163, 184)
        pdf.cell(56, 4.5, "Quelle: WebPilot Smart-Anfrage", border=0, align="R")

        # ── 2. STATUS-BADGES ZEILE (y = 38..46mm) ───────────────────────────────
        y_badge = 38.0
        # Badge 1: Urgency
        pdf.set_font("helvetica", "B", 8.2)
        w1 = max(38.0, pdf.get_string_width(urg_text) + 7.0)
        pdf.set_fill_color(*urg_bg)
        pdf.set_text_color(*urg_fg)
        pdf.rect(12, y_badge, w1, 7.2, "F")
        pdf.set_xy(12, y_badge + 1.1)
        pdf.cell(w1, 5, urg_text, align="C")

        # Badge 2: Einzugsgebiet
        x2 = 12 + w1 + 3.0
        w2 = max(38.0, pdf.get_string_width(area_badge_text) + 7.0)
        pdf.set_fill_color(*area_bg)
        pdf.set_text_color(255, 255, 255)
        pdf.rect(x2, y_badge, w2, 7.2, "F")
        pdf.set_xy(x2, y_badge + 1.1)
        pdf.cell(w2, 5, area_badge_text, align="C")

        # Badge 3: Zuständigkeit / Abteilungs-Routing
        x3 = x2 + w2 + 3.0
        w3 = 198.0 - x3
        routing_text = _truncate(f"Zuständig: {assigned_to} · {sparte_label}", 56)
        pdf.set_fill_color(241, 245, 249)
        pdf.set_draw_color(203, 213, 225)
        pdf.rect(x3, y_badge, w3, 7.2, "FD")
        pdf.set_text_color(*dark_rgb)
        pdf.set_xy(x3 + 2.5, y_badge + 1.1)
        pdf.cell(w3 - 5.0, 5, routing_text, align="L")

        # ── 3. ZWEISPALTIGER STECKBRIEF (y = 49..114mm) ─────────────────────────
        y_box = 49.0
        box_h = 64.0
        col_w = 91.0

        # Linke Box: Kundendaten
        pdf.set_fill_color(248, 250, 252)
        pdf.set_draw_color(226, 232, 240)
        pdf.rect(12, y_box, col_w, box_h, "FD")
        pdf.set_fill_color(*dark_rgb)
        pdf.rect(12, y_box, col_w, 7.0, "F")
        pdf.set_xy(15, y_box + 1.2)
        pdf.set_font("helvetica", "B", 8.5)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(col_w - 6, 4.6, "1. KUNDEN- & STANDORT-ANGABEN")

        left_rows = [
            ("Kontaktperson:", _truncate(visitor_name, 38)),
            ("Firma / Verein:", _truncate(visitor_company, 38)),
            ("Telefon / Mobil:", _truncate(visitor_phone, 38)),
            ("E-Mail-Adresse:", _truncate(visitor_email, 38)),
            ("Strasse & Nr.:", _truncate(visitor_street, 38)),
            ("PLZ & Ort:", _truncate(plz_city, 38)),
            ("Einzugsgebiet:", "Ja - Direkt-Einzugsgebiet" if in_area else "Ausserhalb Kerngebiet"),
        ]
        ry = y_box + 9.2
        for lbl, val in left_rows:
            pdf.set_xy(15, ry)
            pdf.set_font("helvetica", "B", 8.0)
            pdf.set_text_color(71, 85, 105)
            pdf.cell(28, 6.5, lbl)
            pdf.set_font("helvetica", "B" if lbl in ("Kontaktperson:", "Telefon / Mobil:") else "", 8.3)
            pdf.set_text_color(15, 23, 42)
            pdf.cell(col_w - 33, 6.5, val)
            pdf.set_draw_color(226, 232, 240)
            pdf.line(15, ry + 6.5, 12 + col_w - 3, ry + 6.5)
            ry += 7.4

        # Rechte Box: Fachliche Angaben & Routing
        rx = 107.0
        pdf.set_fill_color(248, 250, 252)
        pdf.set_draw_color(226, 232, 240)
        pdf.rect(rx, y_box, col_w, box_h, "FD")
        pdf.set_fill_color(*primary_rgb)
        pdf.rect(rx, y_box, col_w, 7.0, "F")
        pdf.set_xy(rx + 3, y_box + 1.2)
        pdf.set_font("helvetica", "B", 8.5)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(col_w - 6, 4.6, "2. AUFTRAGS-DETAILS & ZUSTÄNDIGKEIT")

        extra_items = []
        if isinstance(extra_fields, dict):
            for ek, ev in extra_fields.items():
                if ev and str(ev).strip():
                    extra_items.append(f"{_pdf_safe(ek)}: {_pdf_safe(ev)}")
        extra_summary = " | ".join(extra_items) if extra_items else "Standard-Erfassung"

        right_rows = [
            ("Anliegen-Art:", _truncate(category_label, 36)),
            ("Sparte / Thema:", _truncate(sparte_label, 36)),
            ("Zeit-Horizont:", _truncate(urgency_raw, 36)),
            ("Zuständig:", _truncate(assigned_to, 36)),
            ("Funktion:", _truncate(assigned_role or sparte_label, 36)),
            ("Rückruf-Ziel:", _truncate(callback_window, 36)),
            ("Zusatz-Angaben:", _truncate(extra_summary, 36)),
        ]
        ry = y_box + 9.2
        for lbl, val in right_rows:
            pdf.set_xy(rx + 3, ry)
            pdf.set_font("helvetica", "B", 8.0)
            pdf.set_text_color(71, 85, 105)
            pdf.cell(28, 6.5, lbl)
            pdf.set_font("helvetica", "B" if lbl in ("Zuständig:", "Rückruf-Ziel:") else "", 8.3)
            pdf.set_text_color(15, 23, 42)
            pdf.cell(col_w - 33, 6.5, val)
            pdf.set_draw_color(226, 232, 240)
            pdf.line(rx + 3, ry + 6.5, rx + col_w - 3, ry + 6.5)
            ry += 7.4

        # ── 4. KUNDENNACHRICHT & SPEZIFISCHE ANGABEN (y = 116..151mm) ───────────
        y_msg = 116.5
        msg_h = 34.0
        pdf.set_fill_color(255, 255, 255)
        pdf.set_draw_color(203, 213, 225)
        pdf.rect(12, y_msg, 186, msg_h, "FD")
        pdf.set_fill_color(241, 245, 249)
        pdf.rect(12, y_msg, 186, 6.5, "F")
        pdf.set_xy(15, y_msg + 1.0)
        pdf.set_font("helvetica", "B", 8.2)
        pdf.set_text_color(*dark_rgb)
        pdf.cell(180, 4.5, "3. BESCHREIBUNG DES ANLIEGENS / KUNDENNACHRICHT")

        full_msg = message_text
        if extra_items:
            full_msg = f"[Spezifische Angaben: {' · '.join(extra_items)}]\n" + full_msg
        full_msg = _truncate(full_msg, 460)

        pdf.set_xy(15, y_msg + 8.2)
        pdf.set_font("helvetica", "", 8.6)
        pdf.set_text_color(30, 41, 59)
        pdf.multi_cell(180, 4.6, full_msg)

        # ── 5. EINGEBETTETE KUNDEN-FOTOS (MAX. 3 BILDER, y = 154..220mm) ────────
        y_photos = 154.0
        photos_h = 65.0
        pdf.set_fill_color(248, 250, 252)
        pdf.set_draw_color(226, 232, 240)
        pdf.rect(12, y_photos, 186, photos_h, "FD")
        pdf.set_fill_color(241, 245, 249)
        pdf.rect(12, y_photos, 186, 6.5, "F")

        raw_photos = lead_data.get("photos") or []
        valid_photos = []
        for idx, p_item in enumerate(raw_photos[:3]):
            p_file = tmp / f"photo_{idx}.jpg"
            ok_img, lbl_img = _decode_and_prepare_photo(p_item, p_file)
            if ok_img and p_file.exists():
                valid_photos.append((p_file, lbl_img))

        pdf.set_xy(15, y_photos + 1.0)
        pdf.set_font("helvetica", "B", 8.2)
        pdf.set_text_color(*dark_rgb)
        pdf.cell(
            180,
            4.5,
            f"4. EINGEREICHTE FOTOS & DOKUMENTATION ({len(valid_photos)} / 3 AUFNAHMEN DIREKT EINGEBETTET)",
        )

        if valid_photos:
            slot_w = 57.0
            slot_h = 46.0
            gap = 4.5
            start_x = 15.0
            img_y = y_photos + 9.0
            for idx, (p_file, lbl_img) in enumerate(valid_photos):
                sx = start_x + idx * (slot_w + gap)
                pdf.set_fill_color(255, 255, 255)
                pdf.set_draw_color(203, 213, 225)
                pdf.rect(sx, img_y, slot_w, slot_h, "FD")
                try:
                    with Image.open(p_file) as pim:
                        pw, ph = pim.size
                    ratio = min((slot_w - 3.0) / pw, (slot_h - 3.0) / ph)
                    dw = pw * ratio
                    dh = ph * ratio
                    dx = sx + (slot_w - dw) / 2.0
                    dy = img_y + (slot_h - dh) / 2.0
                    pdf.image(str(p_file), x=dx, y=dy, w=dw, h=dh)
                except Exception:
                    pass
                pdf.set_xy(sx, img_y + slot_h + 1.0)
                pdf.set_font("helvetica", "B", 7.3)
                pdf.set_text_color(71, 85, 105)
                pdf.cell(slot_w, 4.0, _truncate(f"Foto {idx + 1}: {lbl_img}", 32), align="C")
        else:
            pdf.set_xy(15, y_photos + 26.0)
            pdf.set_font("helvetica", "I", 8.8)
            pdf.set_text_color(100, 116, 139)
            pdf.cell(
                180,
                6.0,
                "Keine Fotos im Formular beigefügt (Tipp: Im Smart-Anfrage-Assistenten können bis zu 3 Fotos direkt hochgeladen werden).",
                align="C",
            )

        # ── 6. UNTERER PRAXIS-BLOCK: CHECKLISTE LINKS + 2 QR-CODES RECHTS (y = 223..281mm) ──
        y_bot = 222.5
        bot_h = 58.0

        # Links: Büro- & Monteur-Notizfeld (x = 12..114mm, w = 102mm)
        pdf.set_fill_color(255, 255, 255)
        pdf.set_draw_color(203, 213, 225)
        pdf.rect(12, y_bot, 102, bot_h, "FD")
        pdf.set_fill_color(241, 245, 249)
        pdf.rect(12, y_bot, 102, 6.5, "F")
        pdf.set_xy(15, y_bot + 1.0)
        pdf.set_font("helvetica", "B", 8.0)
        pdf.set_text_color(*dark_rgb)
        pdf.cell(96, 4.5, "5. INTERNER BEARBEITUNGS- & MONTEUR-VERMERK")

        checks = [
            "Kunde kontaktiert am: ________________   Visum: ________",
            "Termin / Besichtigung: _______________   Monteur: ______",
            "Offerte / Auftrag erledigt am: _________________________",
        ]
        cy = y_bot + 9.5
        pdf.set_font("helvetica", "", 8.0)
        pdf.set_text_color(30, 41, 59)
        for line_txt in checks:
            pdf.set_draw_color(100, 116, 139)
            pdf.rect(15.5, cy + 0.8, 3.6, 3.6, "D")
            pdf.set_xy(21.0, cy)
            pdf.cell(90, 5.2, line_txt)
            cy += 7.5

        pdf.set_xy(15, cy + 1.0)
        pdf.set_font("helvetica", "B", 7.5)
        pdf.set_text_color(100, 116, 139)
        pdf.cell(90, 4.5, "Handschriftliche Notizen / Material / Masse:")
        pdf.set_draw_color(203, 213, 225)
        pdf.line(15, cy + 11.5, 110, cy + 11.5)
        pdf.line(15, cy + 18.5, 110, cy + 18.5)
        pdf.line(15, cy + 25.5, 110, cy + 25.5)

        # Rechts: 2 Praxis-QR-Codes (x = 117..198mm, w = 81mm)
        qx = 117.0
        qw = 81.0
        pdf.set_fill_color(248, 250, 252)
        pdf.set_draw_color(*primary_rgb)
        pdf.rect(qx, y_bot, qw, bot_h, "FD")
        pdf.set_fill_color(*dark_rgb)
        pdf.rect(qx, y_bot, qw, 6.5, "F")
        pdf.set_xy(qx + 3, y_bot + 1.0)
        pdf.set_font("helvetica", "B", 8.0)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(qw - 6, 4.5, "6. PRAXIS-QR-CODES (DIREKT-AKTION)")

        e164_phone = _normalize_e164(visitor_phone)
        tel_uri = f"tel:{e164_phone}"
        maps_query_raw = ", ".join(
            [p for p in [visitor_street if visitor_street != "-" else "", plz_city if plz_city != "-" else "Schweiz"] if p]
        )
        maps_uri = f"https://maps.google.com/?q={urllib.parse.quote(maps_query_raw)}"

        qr1_path = tmp / "qr_call.png"
        qr2_path = tmp / "qr_maps.png"
        _make_qr_image(tel_uri, qr1_path, fill_rgb=dark_rgb)
        _make_qr_image(maps_uri, qr2_path, fill_rgb=dark_rgb)

        # QR 1 Card (Kunde direkt anrufen)
        c1_x = qx + 3.5
        c2_x = qx + 42.0
        c_y = y_bot + 8.5
        c_w = 35.5
        c_h = 46.5

        for card_x, qr_img, title_lbl, sub1, sub2 in [
            (c1_x, qr1_path, "KUNDE ANRUFEN", _truncate(visitor_phone, 18), "Scan startet Anruf"),
            (c2_x, qr2_path, "ROUTE / MAPS", _truncate(plz_city, 18), "Google Maps Route"),
        ]:
            pdf.set_fill_color(255, 255, 255)
            pdf.set_draw_color(226, 232, 240)
            pdf.rect(card_x, c_y, c_w, c_h, "FD")
            pdf.set_xy(card_x, c_y + 1.5)
            pdf.set_font("helvetica", "B", 6.8)
            pdf.set_text_color(*primary_rgb)
            pdf.cell(c_w, 3.8, title_lbl, align="C")

            if qr_img.exists():
                pdf.image(str(qr_img), x=card_x + 3.75, y=c_y + 6.0, w=28.0, h=28.0)

            pdf.set_xy(card_x + 1, c_y + 35.0)
            pdf.set_font("helvetica", "B", 6.8)
            pdf.set_text_color(15, 23, 42)
            pdf.cell(c_w - 2, 3.8, sub1, align="C")

            pdf.set_xy(card_x + 1, c_y + 39.2)
            pdf.set_font("helvetica", "", 6.3)
            pdf.set_text_color(100, 116, 139)
            pdf.cell(c_w - 2, 3.5, sub2, align="C")

        # ── 7. FUSSZEILE (y = 284..291mm) ───────────────────────────────────────
        pdf.set_draw_color(226, 232, 240)
        pdf.line(12, 284.0, 198, 284.0)
        pdf.set_xy(12, 285.2)
        pdf.set_font("helvetica", "", 7.2)
        pdf.set_text_color(100, 116, 139)
        pdf.cell(
            120,
            4.0,
            _pdf_safe(f"{company_name} · Automatisch generiert durch WebPilot Smart-Anfrage & Dual-Delivery Engine"),
            align="L",
        )
        pdf.set_xy(132, 285.2)
        pdf.set_font("helvetica", "B", 7.2)
        pdf.cell(66, 4.0, f"Referenz {ref_code} · Seite 1 von 1", align="R")

        pdf.output(str(out_path))

    return out_path


if __name__ == "__main__":
    import json
    import time

    routing_cfg = json.loads(
        Path("/home/brainuser/workspaces/mxs-embed/config/lead_routing.json").read_text(encoding="utf-8")
    )
    t0 = time.perf_counter()
    sample_lead = {
        "ref_code": "#WP-2026-8421",
        "created_at_display": "30.10.2026, 20:35 Uhr",
        "category": "Reparatur / Stoerung",
        "sparte": "Heizung & Waermepumpen",
        "urgency": "Heute (Dringend)",
        "assigned_to": "Thomas Bertschi",
        "assigned_role": "Bereichsleiter Heizung & Waermepumpen",
        "name": "Hanspeter Mueller",
        "company": "Mueller Immobilien GmbH",
        "phone": "+41 79 412 34 56",
        "email": "hp.mueller@bluewin.ch",
        "street": "Muehlethalstrasse 42",
        "plz": "4800",
        "city": "Zofingen",
        "in_service_area": True,
        "callback_window": "Heute bis 21:30 Uhr (verbindlich)",
        "message": "Beim Warmwasserboiler im Keller tropft seit heute Morgen regelmaessig Wasser aus dem Sicherheitsventil. Typenschild und Ventil habe ich direkt fotografiert.",
        "extra_fields": {"Objekt-Typ": "Einfamilienhaus", "Baujahr Heizung": "ca. 2011"},
        "photos": [
            "/home/brainuser/workspaces/mxs-embed/preview-hochuli/images/ref-heizung-waermepumpe.jpg",
            "/home/brainuser/workspaces/mxs-embed/preview-hochuli/images/ref-sanitaer-badumbau.jpg",
        ],
    }
    out = generate_lead_pdf(
        sample_lead,
        routing_cfg["hochuli"],
        "/tmp/test_hochuli_lead.pdf",
    )
    dt_ms = (time.perf_counter() - t0) * 1000
    print(f"Generated {out} ({out.stat().st_size} bytes) in {dt_ms:.1f} ms")

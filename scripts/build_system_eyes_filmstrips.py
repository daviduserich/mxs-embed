#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_system_eyes_filmstrips.py — Baut die 4 visuellen Doppel-Systemaugen Kontaktboegen (< 400 KB)
aus den Einzel-Screenshots in /tmp/webpilot_device_screenshots/.
"""
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SHOT_DIR = Path("/tmp/webpilot_device_screenshots")


def make_grid_filmstrip(title: str, items: list, out_path: Path, cols: int = 3, thumb_w: int = 440, thumb_h: int = 290):
    valid = [(label, SHOT_DIR / fname) for label, fname in items if (SHOT_DIR / fname).exists()]
    if not valid:
        print(f"[WARN] Keine Frames fuer {out_path.name} gefunden.")
        return

    rows = (len(valid) + cols - 1) // cols
    pad = 16
    header_h = 48
    label_h = 28
    cell_w = thumb_w + pad
    cell_h = thumb_h + label_h + pad

    canvas_w = pad + cols * cell_w
    canvas_h = header_h + pad + rows * cell_h

    canvas = Image.new("RGB", (canvas_w, canvas_h), (7, 9, 14))
    draw = ImageDraw.Draw(canvas)

    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
        font_lbl = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 13)
    except Exception:
        font_title = ImageFont.load_default()
        font_lbl = ImageFont.load_default()

    # Header bar
    draw.rectangle([0, 0, canvas_w, header_h], fill=(15, 20, 32))
    draw.line([0, header_h - 1, canvas_w, header_h - 1], fill=(240, 133, 45), width=2)
    draw.text((18, 14), title, fill=(255, 255, 255), font=font_title)

    for idx, (label, img_path) in enumerate(valid):
        r = idx // cols
        c = idx % cols
        x0 = pad + c * cell_w
        y0 = header_h + pad + r * cell_h

        # Label bar
        draw.rectangle([x0, y0, x0 + thumb_w, y0 + label_h], fill=(22, 28, 42))
        draw.text((x0 + 8, y0 + 6), f"#{idx+1:02d}  {label}", fill=(255, 168, 88), font=font_lbl)

        # Frame area
        box_y = y0 + label_h
        draw.rectangle([x0, box_y, x0 + thumb_w, box_y + thumb_h], fill=(12, 16, 24), outline=(45, 55, 72), width=1)

        try:
            with Image.open(img_path) as im:
                im_rgb = im.convert("RGB")
                im_rgb.thumbnail((thumb_w - 4, thumb_h - 4), Image.Resampling.LANCZOS)
                ox = x0 + (thumb_w - im_rgb.width) // 2
                oy = box_y + (thumb_h - im_rgb.height) // 2
                canvas.paste(im_rgb, (ox, oy))
        except Exception as e:
            draw.text((x0 + 12, box_y + 20), f"Error: {e}", fill=(239, 68, 68), font=font_lbl)

    # Save with adaptive JPEG quality to stay < 380 KB
    for q in (82, 74, 66, 58, 50):
        canvas.save(out_path, "JPEG", quality=q, optimize=True)
        if out_path.stat().st_size <= 385 * 1024:
            break
    print(f"[OK] {out_path.name} ({len(valid)} Frames, {out_path.stat().st_size // 1024} KB)")


def main():
    if not SHOT_DIR.exists():
        return

    # 1. HER11 Pages Desktop + Mobile + Burger Menu
    her11_items = [
        ("HER11 index (Desktop 1440)", "preview-her11_index_desktop_1440x900.png"),
        ("HER11 ueber-uns (Desktop 1440)", "preview-her11_ueber-uns_desktop_1440x900.png"),
        ("HER11 ausbildung (Desktop 1440)", "preview-her11_ausbildung_desktop_1440x900.png"),
        ("HER11 begleitung (Desktop 1440)", "preview-her11_begleitung_desktop_1440x900.png"),
        ("HER11 mach-mit (Desktop 1440)", "preview-her11_mach-mit_desktop_1440x900.png"),
        ("HER11 kontakt (Desktop 1440)", "preview-her11_kontakt_desktop_1440x900.png"),
        ("HER11 index (Mobile 375)", "preview-her11_index_mobile_375x667.png"),
        ("HER11 Mobile Burger-Menue (375)", "preview-her11_index_burger_open_375x667.png"),
        ("HER11 ueber-uns (Mobile 375)", "preview-her11_ueber-uns_mobile_375x667.png"),
        ("HER11 ausbildung (Mobile 375)", "preview-her11_ausbildung_mobile_375x667.png"),
        ("HER11 begleitung (Mobile 375)", "preview-her11_begleitung_mobile_375x667.png"),
        ("HER11 mach-mit (Mobile 375)", "preview-her11_mach-mit_mobile_375x667.png"),
        ("HER11 kontakt (Mobile 375)", "preview-her11_kontakt_mobile_375x667.png"),
    ]
    make_grid_filmstrip(
        "DOPPEL-SYSTEMAUGEN FILMSTRIP 01: HER11 ALLE 6 SEITEN (DESKTOP + MOBILE + BURGER-MENUE)",
        her11_items,
        SHOT_DIR / "filmstrip_01_her11_pages_desktop_mobile.jpg",
        cols=4,
        thumb_w=360,
        thumb_h=240,
    )

    # 2. Cockpit All 12 States on Desktop (1440x900)
    cockpit_desktop_items = [
        ("C01 Default Stage (1440)", "preview-her11_cockpit_desktop_1440x900.png"),
        ("C02 Direkt-Bearbeitung aktiv (1440)", "preview-her11_cockpit_state_inline_edit_1440x900.png"),
        ("C03 Seiten-Dropdown offen (1440)", "preview-her11_cockpit_state_job_dropdown_1440x900.png"),
        ("C04 Sektionen & KI Modal (1440)", "preview-her11_cockpit_state_sections_modal_1440x900.png"),
        ("C05 Text/Code einfuegen Modal (1440)", "preview-her11_cockpit_state_replace_modal_1440x900.png"),
        ("C06 Neue Sektion erstellen Modal (1440)", "preview-her11_cockpit_state_new_section_modal_1440x900.png"),
        ("C07 Bilder-Pool & Galerie Modal (1440)", "preview-her11_cockpit_state_images_modal_1440x900.png"),
        ("C08 Seiten-Uebersicht & Code Modal (1440)", "preview-her11_cockpit_state_directory_modal_1440x900.png"),
        ("C09 Entwurf- & Scharfstell-Panel (1440)", "preview-her11_cockpit_state_draft_panel_1440x900.png"),
        ("C10 Bild-Tausch-Dock aktiv (1440)", "preview-her11_cockpit_state_swap_dock_1440x900.png"),
        ("C11 Aktivitaets-Protokoll Modal (1440)", "preview-her11_cockpit_state_log_modal_1440x900.png"),
        ("C12 Hilfe & Schnellstart Modal (1440)", "preview-her11_cockpit_state_help_modal_1440x900.png"),
    ]
    make_grid_filmstrip(
        "DOPPEL-SYSTEMAUGEN FILMSTRIP 02: COCKPIT v4.0 ALLE 12 ANSICHTEN & MODALS (DESKTOP 1440x900)",
        cockpit_desktop_items,
        SHOT_DIR / "filmstrip_02_cockpit_views_desktop.jpg",
        cols=4,
        thumb_w=380,
        thumb_h=245,
    )

    # 3. Cockpit All 12 States on Mobile (375x667)
    cockpit_mobile_items = [
        ("C01 Default Stage (375)", "preview-her11_cockpit_mobile_375x667.png"),
        ("C02 Direkt-Bearbeitung aktiv (375)", "preview-her11_cockpit_state_inline_edit_375x667.png"),
        ("C03 Seiten-Dropdown offen (375)", "preview-her11_cockpit_state_job_dropdown_375x667.png"),
        ("C04 Sektionen & KI Modal (375)", "preview-her11_cockpit_state_sections_modal_375x667.png"),
        ("C05 Text/Code einfuegen Modal (375)", "preview-her11_cockpit_state_replace_modal_375x667.png"),
        ("C06 Neue Sektion erstellen Modal (375)", "preview-her11_cockpit_state_new_section_modal_375x667.png"),
        ("C07 Bilder-Pool & Galerie Modal (375)", "preview-her11_cockpit_state_images_modal_375x667.png"),
        ("C08 Seiten-Uebersicht & Code Modal (375)", "preview-her11_cockpit_state_directory_modal_375x667.png"),
        ("C09 Entwurf- & Scharfstell-Panel (375)", "preview-her11_cockpit_state_draft_panel_375x667.png"),
        ("C10 Bild-Tausch-Dock aktiv (375)", "preview-her11_cockpit_state_swap_dock_375x667.png"),
        ("C11 Aktivitaets-Protokoll Modal (375)", "preview-her11_cockpit_state_log_modal_375x667.png"),
        ("C12 Hilfe & Schnellstart Modal (375)", "preview-her11_cockpit_state_help_modal_375x667.png"),
    ]
    make_grid_filmstrip(
        "DOPPEL-SYSTEMAUGEN FILMSTRIP 03: COCKPIT v4.0 ALLE 12 ANSICHTEN & MODALS (MOBILE 375x667)",
        cockpit_mobile_items,
        SHOT_DIR / "filmstrip_03_cockpit_views_mobile.jpg",
        cols=4,
        thumb_w=260,
        thumb_h=440,
    )

    # 4. Hochuli Pages Desktop + Mobile + Burger Menu + Cockpit
    hochuli_items = [
        ("Hochuli index (Desktop 1440)", "preview-hochuli_index_desktop_1440x900.png"),
        ("Hochuli team (Desktop 1440)", "preview-hochuli_team_desktop_1440x900.png"),
        ("Hochuli karriere (Desktop 1440)", "preview-hochuli_karriere_desktop_1440x900.png"),
        ("Hochuli kontakt (Desktop 1440)", "preview-hochuli_kontakt_desktop_1440x900.png"),
        ("Hochuli index (Mobile 375)", "preview-hochuli_index_mobile_375x667.png"),
        ("Hochuli Mobile Burger-Menue (375)", "preview-hochuli_index_burger_open_375x667.png"),
        ("Hochuli team (Mobile 375)", "preview-hochuli_team_mobile_375x667.png"),
        ("Hochuli karriere (Mobile 375)", "preview-hochuli_karriere_mobile_375x667.png"),
        ("Hochuli kontakt (Mobile 375)", "preview-hochuli_kontakt_mobile_375x667.png"),
        ("Hochuli Cockpit Default (1440)", "preview-hochuli_cockpit_desktop_1440x900.png"),
        ("Hochuli Sektionen-Modal (1440)", "preview-hochuli_cockpit_state_sections_modal_1440x900.png"),
        ("Hochuli Seiten-Modal (375)", "preview-hochuli_cockpit_state_directory_modal_375x667.png"),
    ]
    make_grid_filmstrip(
        "DOPPEL-SYSTEMAUGEN FILMSTRIP 04: HOCHULI ALLE SEITEN + BURGER-MENUE + COCKPIT",
        hochuli_items,
        SHOT_DIR / "filmstrip_04_hochuli_pages_desktop_mobile.jpg",
        cols=4,
        thumb_w=360,
        thumb_h=250,
    )


if __name__ == "__main__":
    main()

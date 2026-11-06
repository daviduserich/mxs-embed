#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_before_after_report.py — Kanonischer CLI-Entrypoint fuer den WebPilot Vorher/Nachher-PDF-Report
Delegiert direkt an build_webpilot_audit_pdf.py (HTML + A4-PDF + 27-Sensoren Systemaugen-Pruefung).
"""
import os
import sys
import subprocess
from pathlib import Path

if __name__ == "__main__":
    target_script = Path(__file__).resolve().parent / "build_webpilot_audit_pdf.py"
    rc = subprocess.call([sys.executable, str(target_script)] + sys.argv[1:])
    sys.exit(rc)

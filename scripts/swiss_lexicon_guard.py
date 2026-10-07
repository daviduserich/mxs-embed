#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Swiss Lexicon Guard (swiss_lexicon_guard.py)
======================================================
Automatisierter helvetischer Sprachwächter und Linter für das WebPilot-Framework.

Doktrin:
1. Reines Schweizer Hochdeutsch: 100% Verbot von bundesdeutschem Vokabular
   («Gewerke» -> «Leistungen», «Geselle» -> «Handwerker EFZ», «Notdienst» -> «24h-Pikett»,
    «Urlaub» -> «Ferien», «Kostenvoranschlag» -> «Offerte», etc.).
2. Absolute 0-Toleranz für Eszett («ß» -> «ss»).
3. Deterministischer Airbag: Wird automatisch in compile_site.py und
   create_client_site.py vor jedem Commit / Edge-Deploy ausgeführt.
"""

import os
import sys
import re
from pathlib import Path
from typing import Tuple, List, Dict, Any

# Wörterbuch mit strengen helvetischen Ersetzungsregeln
# Format: (Regex-Muster, Ersatzbegriff, Beschreibung/Kontext)
SWISS_REPLACEMENTS = [
    # 1. Bundesdeutsche Handwerks- & Branchenbegriffe
    (r"\bStartseite\s*&\s*Gewerke\b", "Startseite & Leistungen", "Navigation: Schweizer Handwerks-Standard"),
    (r"\bGewerke\b", "Leistungen", "Handwerk: Gewerke existiert in der Schweiz nicht"),
    (r"\bGewerk\b", "Leistung", "Handwerk: Gewerk -> Leistung / Fachbereich"),
    (r"\bGesellen\b", "Handwerker EFZ und Fachmonteure", "Berufsbezeichnung: In CH gilt EFZ"),
    (r"\bGeselle\b", "Handwerker EFZ", "Berufsbezeichnung: Geselle -> Handwerker EFZ"),
    (r"\bAzubis\b", "Lernende", "Bildung: Azubis -> Lernende"),
    (r"\bAzubi\b", "Lernende", "Bildung: Azubi -> Lernende"),
    (r"\bAuszubildende\b", "Lernende", "Bildung: Auszubildende -> Lernende"),
    (r"\bAuszubildender\b", "Lernender", "Bildung: Auszubildender -> Lernender"),
    (r"\bAuszubildenden\b", "Lernenden", "Bildung: Auszubildenden -> Lernenden"),
    (r"\bLehrling\b", "Lernende", "Bildung: Moderner Schweizer Standard ist Lernende"),
    (r"\bLehrlinge\b", "Lernende", "Bildung: Moderner Schweizer Standard ist Lernende"),
    
    # 2. Notdienst & Pikett
    (r"\b24h\s+Notdienst\s*&\s*Pikett\b", "24h-Pikett & Notfallkontakt", "Notfall: Schweizer Begriff ist Pikett"),
    (r"\b24h\s+Notfall-Pikett\b", "24h-Pikett", "Notfall: Schweizer Standard 24h-Pikett"),
    (r"\b24h\s+Notdienst\b", "24h-Pikett", "Notfall: Notdienst -> 24h-Pikett"),
    (r"\b24h-Notdienst\b", "24h-Pikett", "Notfall: Notdienst -> 24h-Pikett"),
    (r"\bSturm-Notdienst\b", "Sturm-Pikett", "Notfall: Sturm-Notdienst -> Sturm-Pikett"),
    (r"\bSanitärnotdienst\b", "Sanitär-Pikett", "Notfall: Sanitärnotdienst -> Sanitär-Pikett"),
    (r"\bSanitär-Notdienst\b", "Sanitär-Pikett", "Notfall: Sanitär-Notdienst -> Sanitär-Pikett"),
    (r"\bNotdienst\s*&\s*Büro\b", "24h-Pikett & Büro", "Notfall: Notdienst -> Pikett"),
    (r"\bKontakt\s*&\s*Notdienst\b", "Kontakt & 24h-Pikett", "Notfall: Notdienst -> Pikett"),
    (r"\bSanitär\s*&\s*Notdienst\b", "Sanitär & 24h-Pikett", "Notfall: Notdienst -> Pikett"),
    (r"\bNotdienste\b", "Pikettdienste", "Notfall: Notdienste -> Pikettdienste"),
    (r"\bNotdienstes\b", "Pikettdienstes", "Notfall: Notdienstes -> Pikettdienstes"),
    (r"\bNotdienst\b", "24h-Pikett", "Notfall: Notdienst -> 24h-Pikett"),

    # 3. Offerten & Finanzen
    (r"\bKostenvoranschlag\b", "Offerte", "Kaufmännisch: Kostenvoranschlag -> Offerte"),
    (r"\bKostenvoranschlags\b", "Offerte", "Kaufmännisch: Kostenvoranschlags -> Offerte"),
    (r"\bKostenvoranschläge\b", "Offerten", "Kaufmännisch: Kostenvoranschläge -> Offerten"),
    (r"\bKostenvoranschlägen\b", "Offerten", "Kaufmännisch: Kostenvoranschlägen -> Offerten"),
    (r"\bAngebot\s+einholen\b", "Offerte anfordern", "CTA: Angebot einholen -> Offerte anfordern"),
    (r"\bAngebot\s+anfordern\b", "Offerte anfordern", "CTA: Angebot anfordern -> Offerte anfordern"),
    (r"\bMwSt\.?\b", "MWST", "Steuern: Schweizer Standard ist MWST (ohne Punkt)"),
    (r"\bMehrwertsteuer\b", "MWST", "Steuern: MWST"),

    # 4. Ferien & HR
    (r"\bUrlaubsplanung\b", "Ferienplanung", "HR: Urlaubsplanung -> Ferienplanung"),
    (r"\bUrlaubsanspruch\b", "Ferienanspruch", "HR: Urlaubsanspruch -> Ferienanspruch"),
    (r"\bBetriebsurlaub\b", "Betriebsferien", "HR: Betriebsurlaub -> Betriebsferien"),
    (r"\bUrlaubstage\b", "Ferientage", "HR: Urlaubstage -> Ferientage"),
    (r"\bUrlaub\b", "Ferien", "HR: Urlaub -> Ferien"),

    # 5. Bau- & Gebäude-Fachausdrücke
    (r"\bGauben\b", "Lukarnen", "Architektur: Gauben -> Lukarnen"),
    (r"\bGaube\b", "Lukarne", "Architektur: Gaube -> Lukarne"),
    (r"\bDachböden\b", "Dachstöcke", "Architektur: Dachböden -> Dachstöcke"),
    (r"\bDachboden\b", "Dachstock", "Architektur: Dachboden -> Dachstock"),
    (r"\bDachbodenausbau\b", "Dachstockausbau", "Architektur: Dachbodenausbau -> Dachstockausbau"),
    (r"\bSchornsteine\b", "Kamine", "Architektur: Schornsteine -> Kamine"),
    (r"\bSchornstein\b", "Kamin", "Architektur: Schornstein -> Kamin"),
    (r"\bFördermittel\b", "Fördergelder", "Behörden: Fördermittel -> Fördergelder"),
    (r"\bTÜV\b", "SUVA / MFK", "Prüfung: TÜV existiert in der Schweiz nicht"),

    # 6. Mobilität & Alltag
    (r"\bBürgersteig\b", "Trottoir", "Alltag: Bürgersteig -> Trottoir"),
    (r"\bGehweg\b", "Trottoir", "Alltag: Gehweg -> Trottoir"),
    (r"\bFahrräder\b", "Velos", "Alltag: Fahrräder -> Velos"),
    (r"\bFahrrad\b", "Velo", "Alltag: Fahrrad -> Velo"),
    (r"\bParkplätze\b", "Parkplätze", "Alltag: Parkplätze"),
]

# Eszett-Normalisierung
RE_ESZETT = re.compile(r"ß")


def enforce_swiss_standards(content: str) -> Tuple[str, List[Dict[str, Any]]]:
    """
    Normalisiert einen Text/HTML-Inhalt nach Schweizer Sprachstandards.
    Gibt (bereinigter_inhalt, liste_der_korrekturen) zurück.
    """
    fixes = []
    new_content = content

    # 1. Eszett restlos tilgen
    eszett_matches = len(RE_ESZETT.findall(new_content))
    if eszett_matches > 0:
        new_content = RE_ESZETT.sub("ss", new_content)
        fixes.append({
            "type": "eszett",
            "matches": eszett_matches,
            "description": f"{eszett_matches}x Eszett ('ß') durch 'ss' ersetzt."
        })

    # 2. Vokabular prüfen und ersetzen
    for pattern, replacement, desc in SWISS_REPLACEMENTS:
        # Regex mit Case-Insensitive Flag, aber Match-Replacement
        regex = re.compile(pattern, re.IGNORECASE)
        matches = regex.findall(new_content)
        if matches:
            # Case-preserving oder Standard-Ersatz
            def repl_func(match):
                txt = match.group(0)
                # Wenn kompletter Grossbuchstabe
                if txt.isupper():
                    return replacement.upper()
                # Wenn Gross am Anfang
                if txt[0].isupper():
                    return replacement[0].upper() + replacement[1:]
                return replacement.lower()

            new_content = regex.sub(repl_func, new_content)
            fixes.append({
                "type": "vocabulary",
                "term": pattern,
                "replacement": replacement,
                "count": len(matches),
                "description": f"{len(matches)}x '{pattern}' -> '{replacement}' ({desc})"
            })

    return new_content, fixes


def audit_swiss_standards(content: str) -> List[Dict[str, Any]]:
    """
    Prüft einen Text/HTML-Inhalt auf unschweizerische Ausdrücke ohne ihn zu modifizieren.
    Gibt eine Liste aller gefundenen Verstösse zurück.
    """
    violations = []

    # 1. Eszett Check
    eszett_matches = len(RE_ESZETT.findall(content))
    if eszett_matches > 0:
        violations.append({
            "term": "ß (Eszett)",
            "count": eszett_matches,
            "recommendation": "Durch 'ss' ersetzen."
        })

    # 2. Vokabular Check
    for pattern, replacement, desc in SWISS_REPLACEMENTS:
        regex = re.compile(pattern, re.IGNORECASE)
        matches = regex.findall(content)
        if matches:
            violations.append({
                "term": pattern,
                "count": len(matches),
                "recommendation": f"Ersetzen durch '{replacement}' ({desc})"
            })

    return violations


def process_file(file_path: Path, fix: bool = False) -> Dict[str, Any]:
    """Prüft oder repariert eine einzelne Datei."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return {"file": str(file_path), "error": str(e)}

    if fix:
        sanitized, fixes = enforce_swiss_standards(content)
        if fixes:
            file_path.write_text(sanitized, encoding="utf-8")
        return {"file": str(file_path), "fixes": fixes, "modified": len(fixes) > 0}
    else:
        violations = audit_swiss_standards(content)
        return {"file": str(file_path), "violations": violations, "has_issues": len(violations) > 0}


def main():
    import argparse
    parser = argparse.ArgumentParser(description="WebPilot Swiss Lexicon Guard & Linter")
    parser.add_argument("--audit", help="Datei oder Verzeichnis auditieren")
    parser.add_argument("--fix", help="Datei oder Verzeichnis automatisch reparieren")
    parser.add_argument("--all", action="store_true", help="Alle Mandanten & Templates scannen/reparieren")
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent.parent

    target_paths = []
    do_fix = bool(args.fix or args.all)

    if args.audit:
        target_paths.append(Path(args.audit).resolve())
    elif args.fix:
        target_paths.append(Path(args.fix).resolve())
    elif args.all:
        target_paths.append(base_dir)
    else:
        parser.print_help()
        sys.exit(0)

    total_files = 0
    total_issues = 0

    for tp in target_paths:
        if tp.is_file():
            files = [tp]
        elif tp.is_dir():
            files = sorted([p for p in tp.rglob("*") if p.suffix.lower() in [".html", ".json", ".js"] and not ".git" in p.parts and not "node_modules" in p.parts])
        else:
            print(f"Pfad nicht gefunden: {tp}")
            continue

        for f in files:
            res = process_file(f, fix=do_fix)
            total_files += 1
            if do_fix:
                if res.get("modified"):
                    total_issues += len(res["fixes"])
                    print(f" [GEFIXT] {f.relative_to(base_dir) if f.is_relative_to(base_dir) else f}")
                    for fix in res["fixes"]:
                        print(f"   -> {fix['description']}")
            else:
                if res.get("has_issues"):
                    total_issues += len(res["violations"])
                    print(f" [VERSTOSS] {f.relative_to(base_dir) if f.is_relative_to(base_dir) else f}")
                    for v in res["violations"]:
                        print(f"   -> {v['count']}x '{v['term']}': {v['recommendation']}")

    if do_fix:
        print(f"\nFertig: {total_files} Dateien geprüft, {total_issues} helvetische Anpassungen vorgenommen.")
    else:
        print(f"\nAudit beendet: {total_files} Dateien geprüft, {total_issues} Sprach-Verstösse identifiziert.")
        if total_issues > 0:
            sys.exit(1)


if __name__ == "__main__":
    main()

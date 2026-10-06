#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Section Surgery Engine (section_tool.py)
=================================================
Chirurgisches Werkzeug zur isolierten Verwaltung, Bearbeitung und Erweiterung
von WebPilot-Sektionen, ohne den Rest der HTML-Seite zu berühren.

Doktrin:
- Jede Sektion trägt das Attribut data-section="<id>"
- Kein schweres WordPress-CMS, sondern deterministische Build-Time-Chirurgie
- Ein-Klick Prompt-Generierung für LLMs
- Airbag-Schutz: Prüfung auf Tag-Balancierung vor jedem Schreibvorgang

Befehle:
  python3 section_tool.py --site hiltbrand --page index.html --list
  python3 section_tool.py --site hiltbrand --page index.html --export ratgeber [--prompt]
  python3 section_tool.py --site hiltbrand --page index.html --replace ratgeber --file neu.html [--git-push]
  python3 section_tool.py --site hiltbrand --page index.html --insert-after services --file faq.html [--git-push]
  python3 section_tool.py --site hiltbrand --page index.html --insert-before contact --file partner.html [--git-push]
  python3 section_tool.py --site hiltbrand --page index.html --remove ratgeber [--git-push]
"""

import os
import sys
import re
import argparse
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def find_tag_span(html: str, start_pos: int, tag_name: str) -> tuple[int, int]:
    """Findet den exakten Start- und End-Index eines HTML-Tags unter Berücksichtigung von Nesting."""
    gt_pos = html.find(">", start_pos)
    if gt_pos == -1:
        return -1, -1

    depth = 1
    curr = gt_pos + 1
    combined_regex = re.compile(rf"(<{tag_name}\b[^>]*>)|(</{tag_name}>)", re.IGNORECASE)

    for m in combined_regex.finditer(html, curr):
        if m.group(1):
            depth += 1
        elif m.group(2):
            depth -= 1
            if depth == 0:
                return start_pos, m.end()

    return -1, -1


def parse_sections(html: str) -> list[dict]:
    """Findet alle Elemente mit data-section='...' auf der Seite."""
    sections = []
    # Matcht <section ... data-section="xyz" ...> oder div/header/footer
    pattern = re.compile(
        r'<(?P<tag>section|div|header|footer)\b(?P<attrs>[^>]*?\bdata-section=["\'](?P<id>[a-zA-Z0-9_-]+)["\'][^>]*)>',
        re.IGNORECASE,
    )

    for m in pattern.finditer(html):
        start_idx = m.start()
        tag = m.group("tag").lower()
        sec_id = m.group("id")
        attrs = m.group("attrs")

        # Ende finden
        s_pos, e_pos = find_tag_span(html, start_idx, tag)
        if s_pos != -1 and e_pos != -1:
            content = html[s_pos:e_pos]
            start_line = html.count("\n", 0, s_pos) + 1
            end_line = html.count("\n", 0, e_pos) + 1

            # Titel / Überschrift extrahieren für hübsche Anzeige
            h_match = re.search(r'<h[1-4][^>]*>(.*?)</h[1-4]>', content, re.DOTALL | re.IGNORECASE)
            title = ""
            if h_match:
                title = re.sub(r'<[^>]+>', '', h_match.group(1)).strip()

            k_match = re.search(r'class=["\'][^"\']*section-kicker[^"\']*["\'][^>]*>(.*?)<', content, re.IGNORECASE)
            kicker = k_match.group(1).strip() if k_match else ""

            sections.append({
                "id": sec_id,
                "tag": tag,
                "start": s_pos,
                "end": e_pos,
                "start_line": start_line,
                "end_line": end_line,
                "lines": end_line - start_line + 1,
                "title": title,
                "kicker": kicker,
                "raw": content,
            })

    return sections


def validate_airbag(html_chunk: str) -> tuple[bool, str]:
    """Prüft die syntaktische Unversehrtheit des HTML-Chunks (Airbag)."""
    tags_to_check = ["div", "section", "p", "span", "a", "h1", "h2", "h3", "h4", "ul", "ol", "li", "form"]
    for t in tags_to_check:
        opens = len(re.findall(rf'<{t}\b[^>]*>', html_chunk, re.IGNORECASE))
        closes = len(re.findall(rf'</{t}>', html_chunk, re.IGNORECASE))
        if opens != closes:
            return False, f"Airbag-Fehler: Ungleiche Anzahl von <{t}> ({opens}) und </{t}> ({closes})."

    return True, "OK"


def git_commit_push(site_name: str, message: str):
    """Führt einen deterministischen Git Commit und Push aus."""
    print("Führe automatischen Git-Push nach Cloudflare Pages aus...")
    try:
        subprocess.run(["git", "add", site_name], cwd=str(BASE_DIR), check=True)
        subprocess.run(["git", "commit", "-m", message], cwd=str(BASE_DIR), check=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=str(BASE_DIR), check=True)
        print("Git Push erfolgreich abgeschlossen!")
    except Exception as e:
        print(f"Git Push Warnung / Fehler: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="WebPilot Section Surgery Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--site", required=True, help="Site-Ordner (z.B. preview-hiltbrand, webpilot)")
    parser.add_argument("--page", default="index.html", help="HTML-Datei (Standard: index.html)")
    parser.add_argument("--list", action="store_true", help="Listet alle Sektionen der Seite auf")
    parser.add_argument("--export", help="Exportiert eine bestimmte Sektion (ID)")
    parser.add_argument("--prompt", action="store_true", help="Generiert zusammen mit --export einen KI-Prompt")
    parser.add_argument("--replace", help="Ersetzt eine Sektion (ID)")
    parser.add_argument("--insert-after", help="Fügt eine neue Sektion NACH dieser Sektion ein")
    parser.add_argument("--insert-before", help="Fügt eine neue Sektion VOR dieser Sektion ein")
    parser.add_argument("--remove", help="Entfernt eine Sektion (ID)")
    parser.add_argument("--file", help="Datei mit dem neuen Sektions-HTML")
    parser.add_argument("--content", help="Direkter HTML-String für replace/insert")
    parser.add_argument("--out", help="Zieldatei für den Export")
    parser.add_argument("--git-push", action="store_true", help="Automatisch committen & pushen")

    args = parser.parse_args()

    # Pfade auflösen
    site_dir = BASE_DIR / args.site
    if not site_dir.is_dir():
        site_dir = Path(args.site).resolve()
    if not site_dir.is_dir():
        print(f"Fehler: Site '{args.site}' nicht gefunden.")
        sys.exit(1)

    page_file = site_dir / args.page
    if not page_file.is_file():
        print(f"Fehler: Seite '{page_file}' nicht gefunden.")
        sys.exit(1)

    with open(page_file, "r", encoding="utf-8") as f:
        html = f.read()

    sections = parse_sections(html)

    # 1. LIST
    if args.list:
        print(f"\nSektionen in {args.site}/{args.page} ({len(sections)} gefunden):")
        print("-" * 75)
        for i, s in enumerate(sections, 1):
            title_disp = f" - \"{s['title']}\"" if s["title"] else ""
            kicker_disp = f" [{s['kicker']}]" if s["kicker"] else ""
            print(f"{i:2d}. [{s['id']:<18}] <{s['tag']}> {s['lines']:3d} Zeilen (Z.{s['start_line']}–{s['end_line']}){kicker_disp}{title_disp}")
        print("-" * 75)
        return

    # 2. EXPORT
    if args.export:
        sec = next((s for s in sections if s["id"] == args.export), None)
        if not sec:
            print(f"Fehler: Sektion '{args.export}' nicht gefunden.")
            sys.exit(1)

        raw = sec["raw"]
        if args.prompt:
            prompt_text = f"""Du bist Web-Designer für Schweizer KMUs und Handwerksbetriebe.
Hier ist der isolierte HTML-Code der Sektion '{args.export}' von {args.site}:

```html
{raw}
```

Aufgabe:
[Deine Anweisungen hier eingeben]

WICHTIGE REGELN:
1. Behalte alle CSS-Klassen und Attribute (insbesondere data-section="{args.export}") exakt bei.
2. Schliesse alle Tags sauber ab (keine offenen divs).
3. Antworte AUSSCHLIESSLICH mit dem vollständigen, fertigen HTML-Codeblock für <{sec['tag']} data-section="{args.export}">...</{sec['tag']}> ohne einleitendes Geplänkel.
"""
            raw = prompt_text

        if args.out:
            with open(args.out, "w", encoding="utf-8") as out_f:
                out_f.write(raw)
            print(f"Sektion '{args.export}' erfolgreich nach '{args.out}' exportiert.")
        else:
            print(f"\n--- Sektion: {args.export} ({sec['lines']} Zeilen) ---\n")
            print(raw)
        return

    # HTML-Chunk für Insertion/Replacement laden
    new_chunk = None
    if args.file:
        with open(args.file, "r", encoding="utf-8") as in_f:
            new_chunk = in_f.read().strip()
    elif args.content:
        new_chunk = args.content.strip()

    # 3. REPLACE
    if args.replace:
        if not new_chunk:
            print("Fehler: Für --replace wird --file oder --content benötigt.")
            sys.exit(1)

        sec = next((s for s in sections if s["id"] == args.replace), None)
        if not sec:
            print(f"Fehler: Sektion '{args.replace}' nicht gefunden.")
            sys.exit(1)

        # Airbag-Prüfung
        valid, err = validate_airbag(new_chunk)
        if not valid:
            print(f"AIRBAG ABBRUCH: {err}")
            sys.exit(1)

        # Ersetzen
        new_html = html[:sec["start"]] + new_chunk + html[sec["end"]:]
        with open(page_file, "w", encoding="utf-8") as f:
            f.write(new_html)

        print(f"Sektion '{args.replace}' erfolgreich ausgetauscht ({sec['lines']} Zeilen ersetzt).")

        if args.git_push:
            git_commit_push(site_dir.name, f"feat(section): update section '{args.replace}' in {args.page}")
        return

    # 4. INSERT AFTER
    if args.insert_after:
        if not new_chunk:
            print("Fehler: Für --insert-after wird --file oder --content benötigt.")
            sys.exit(1)

        sec = next((s for s in sections if s["id"] == args.insert_after), None)
        if not sec:
            print(f"Fehler: Bezugs-Sektion '{args.insert_after}' nicht gefunden.")
            sys.exit(1)

        valid, err = validate_airbag(new_chunk)
        if not valid:
            print(f"AIRBAG ABBRUCH: {err}")
            sys.exit(1)

        insert_pos = sec["end"]
        new_html = html[:insert_pos] + "\n\n  " + new_chunk + html[insert_pos:]
        with open(page_file, "w", encoding="utf-8") as f:
            f.write(new_html)

        print(f"Neue Sektion erfolgreich NACH '{args.insert_after}' eingefügt.")
        if args.git_push:
            git_commit_push(site_dir.name, f"feat(section): insert section after '{args.insert_after}' in {args.page}")
        return

    # 5. INSERT BEFORE
    if args.insert_before:
        if not new_chunk:
            print("Fehler: Für --insert-before wird --file oder --content benötigt.")
            sys.exit(1)

        sec = next((s for s in sections if s["id"] == args.insert_before), None)
        if not sec:
            print(f"Fehler: Bezugs-Sektion '{args.insert_before}' nicht gefunden.")
            sys.exit(1)

        valid, err = validate_airbag(new_chunk)
        if not valid:
            print(f"AIRBAG ABBRUCH: {err}")
            sys.exit(1)

        insert_pos = sec["start"]
        new_html = html[:insert_pos] + new_chunk + "\n\n  " + html[insert_pos:]
        with open(page_file, "w", encoding="utf-8") as f:
            f.write(new_html)

        print(f"Neue Sektion erfolgreich VOR '{args.insert_before}' eingefügt.")
        if args.git_push:
            git_commit_push(site_dir.name, f"feat(section): insert section before '{args.insert_before}' in {args.page}")
        return

    # 6. REMOVE
    if args.remove:
        sec = next((s for s in sections if s["id"] == args.remove), None)
        if not sec:
            print(f"Fehler: Sektion '{args.remove}' nicht gefunden.")
            sys.exit(1)

        new_html = html[:sec["start"]] + html[sec["end"]:]
        with open(page_file, "w", encoding="utf-8") as f:
            f.write(new_html)

        print(f"Sektion '{args.remove}' erfolgreich entfernt ({sec['lines']} Zeilen gelöscht).")
        if args.git_push:
            git_commit_push(site_dir.name, f"feat(section): remove section '{args.remove}' from {args.page}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()

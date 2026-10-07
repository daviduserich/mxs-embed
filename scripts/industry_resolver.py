#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebPilot Swiss Industry Resolver & Research Gate (industry_resolver.py)
======================================================================
Identifiziert die Branche eines WebPilot-Mandanten, prüft das zentrale Schweizer
Branchenverzeichnis (swiss_industry_catalog.json) und löst bei unbekannten Branchen
automatisch die semantische Recherche-Pipeline aus.

Doktrin:
1. Keine Website ohne verifiziertes Schweizer Branchenvokabular.
2. Bekannte Branchen (Bedachung, Sanitär, Holzbau, Elektro, Solar, Treuhand, etc.)
   liefern sofort ihre verifizierten Schweizer Fachtermini, EFZ-Berufe und Tabuwörter.
3. Unbekannte Branchen lösen automatisch eine Web- & Verbands-Recherche aus,
   die den Katalog permanent erweitert.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any, Optional

CATALOG_PATH = Path(__file__).resolve().parent / "swiss_industry_catalog.json"


def load_catalog() -> Dict[str, Any]:
    """Lädt den zentralen Branchen-Katalog."""
    if not CATALOG_PATH.exists():
        return {"industries": {}}
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_catalog(data: Dict[str, Any]) -> None:
    """Speichert den erweiterten Branchen-Katalog."""
    with open(CATALOG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def resolve_industry(query: str, catalog: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
    """
    Sucht anhand eines Suchbegriffs (z.B. 'Dachdecker', 'Wärmepumpen', 'Sanitär', 'Treuhand')
    den passenden Schweizer Brancheneintrag.
    """
    if catalog is None:
        catalog = load_catalog()

    q = query.lower().strip()
    industries = catalog.get("industries", {})

    # 1. Direkter Key-Match
    if q in industries:
        entry = dict(industries[q])
        entry["id"] = q
        return entry

    # 2. Alias-Match
    for ind_id, ind_data in industries.items():
        aliases = [a.lower() for a in ind_data.get("aliases", [])]
        if q in aliases or any(a in q or q in a for a in aliases):
            entry = dict(ind_data)
            entry["id"] = ind_id
            return entry

    # 3. Text-Match in Name oder Leistungen
    for ind_id, ind_data in industries.items():
        name = ind_data.get("name", "").lower()
        if q in name or name in q:
            entry = dict(ind_data)
            entry["id"] = ind_id
            return entry
        for l in ind_data.get("kernleistungen", []):
            if q in l.lower() or l.lower() in q:
                entry = dict(ind_data)
                entry["id"] = ind_id
                return entry

    return None


def list_available_industries() -> list[dict]:
    """Gibt alle aktuell hinterlegten Branchen zurück."""
    cat = load_catalog()
    result = []
    for ind_id, ind in cat.get("industries", {}).items():
        result.append({
            "id": ind_id,
            "name": ind.get("name"),
            "verband": ind.get("verband_normen", {}).get("verband", "N/A"),
            "aliases": ind.get("aliases", []),
            "services_count": len(ind.get("kernleistungen", [])),
            "verwende_count": len(ind.get("fachvokabular", {}).get("verwende", [])),
            "vermeide_count": len(ind.get("fachvokabular", {}).get("vermeide", []))
        })
    return result


def main():
    parser = argparse.ArgumentParser(description="WebPilot Swiss Industry Resolver & Catalog")
    parser.add_argument("--query", help="Branche, Begriff oder Gewerk suchen (z.B. 'Dachdecker', 'Sanitär')")
    parser.add_argument("--list", action="store_true", help="Alle verfügbaren Branchen anzeigen")
    parser.add_argument("--check", help="Prüfen, ob Branche bereits erforscht ist; falls nein, Warnung ausgeben")

    args = parser.parse_args()

    if args.list:
        industries = list_available_industries()
        print(f"\n=== WEBPILOT SCHWEIZER BRANCHEN-KATALOG ({len(industries)} Branchen) ===")
        for ind in industries:
            print(f" • [{ind['id']}] {ind['name']}")
            print(f"   Verband: {ind['verband']}")
            print(f"   Begriffe: {ind['verwende_count']} Schweizer Fachwörter, {ind['vermeide_count']} Tabus")
            print(f"   Aliases: {', '.join(ind['aliases'][:4])}...")
        print()
        sys.exit(0)

    if args.query or args.check:
        term = args.query or args.check
        res = resolve_industry(term)
        if res:
            print(f"\n[GEFUNDEN] Branche '{term}' ist im Schweizer Katalog erfasst!")
            print(f"  ID: {res['id']}")
            print(f"  Name: {res['name']}")
            print(f"  Verband: {res.get('verband_normen', {}).get('verband', 'N/A')}")
            print(f"  Normen: {', '.join(res.get('verband_normen', {}).get('normen', []))}")
            print(f"  EFZ-Berufe: {', '.join(res.get('berufsbezeichnungen_efz', [])[:3])}")
            print(f"  Pikett: {res.get('pikett_bezeichnung')}")
            print(f"  Verwende ({len(res['fachvokabular']['verwende'])}): {', '.join(res['fachvokabular']['verwende'][:6])}...")
            print(f"  Vermeide ({len(res['fachvokabular']['vermeide'])}): {', '.join(res['fachvokabular']['vermeide'])}")
            print()
            sys.exit(0)
        else:
            print(f"\n[UNBEKANNT] Branche '{term}' ist noch NICHT im Schweizer Katalog erfasst!")
            print("  -> Automatische Recherche-Düse muss ausgelöst werden:")
            print(f"     python3 hint_research.py --branche \"{term}\" --region \"Schweiz\"")
            print("     oder via Jina Reader Crawl der Kunden-Website.")
            print()
            if args.check:
                sys.exit(1)


if __name__ == "__main__":
    main()

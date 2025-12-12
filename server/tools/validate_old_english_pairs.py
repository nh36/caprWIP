#!/usr/bin/env python3
"""Ensure every English entry has a matching Old English row in the TSV."""
from __future__ import annotations
import argparse
import csv
from collections import defaultdict
from pathlib import Path

PLACEHOLDER = "TODO: replace with attested Old English form"


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader)


def key_for(row: dict[str, str]) -> tuple[str, str]:
    return (row.get("CONCEPT", "").strip(), row.get("PROTO", "").strip())


def validate(path: Path) -> int:
    rows = load_rows(path)
    english = defaultdict(list)
    old_english = defaultdict(list)
    for row in rows:
        doc = row.get("DOCULECT")
        key = key_for(row)
        if doc == "English":
            english[key].append(row)
        elif doc == "Old_English":
            old_english[key].append(row)
    exit_code = 0
    missing = sorted(k for k in english if k not in old_english)
    if missing:
        exit_code = 1
        print(f"[ERROR] {len(missing)} English concepts lack Old English rows in {path}")
        for concept, proto in missing[:10]:
            print(f"    - {concept} ({proto})")
        if len(missing) > 10:
            print("    …")
    extra = sorted(k for k in old_english if k not in english)
    if extra:
        exit_code = 1
        print(f"[ERROR] {len(extra)} Old English rows lack matching English entries in {path}")
    placeholders = [row for row in rows if row.get("DOCULECT") == "Old_English" and row.get("NOTE", "").startswith(PLACEHOLDER)]
    if placeholders:
        print(f"[WARN] {len(placeholders)} Old English rows still carry placeholder notes in {path}")
    else:
        print(f"[OK] All Old English notes populated in {path}")
    duplicates = [key for key, entries in old_english.items() if len(entries) > 1]
    if duplicates:
        print(f"[WARN] {len(duplicates)} concepts have multiple Old English rows; expected 1:1")
    if not missing and not extra:
        print(f"[OK] Old English coverage matches English entries in {path}")
    return exit_code


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    exit_code = 0
    for path in args.paths:
        exit_code = max(exit_code, validate(path))
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()

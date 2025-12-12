#!/usr/bin/env python3
"""Duplicate English rows as Old English placeholders in a TSV."""
from __future__ import annotations
import argparse
import csv
from pathlib import Path

DEFAULT_NOTE = "TODO: replace with attested Old English form"


def load_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames is None:
            raise SystemExit(f"Missing header in {path}")
        rows = list(reader)
    return reader.fieldnames, rows

def write_rows(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    with tmp_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    tmp_path.replace(path)

def duplicate_english_rows(rows: list[dict[str, str]], note_suffix: str) -> tuple[list[dict[str, str]], int]:
    existing_oe = [row for row in rows if row.get("DOCULECT") == "Old_English"]
    if existing_oe:
        raise SystemExit("File already contains Old_English rows; aborting to prevent duplicates.")
    english_rows = [row for row in rows if row.get("DOCULECT") == "English"]
    if not english_rows:
        raise SystemExit("No English rows found—nothing to duplicate.")
    try:
        max_id = max(int(row["ID"]) for row in rows if row.get("ID"))
    except ValueError as exc:
        raise SystemExit(f"Failed to determine max ID: {exc}")
    next_id = max_id + 1
    result: list[dict[str, str]] = []
    added = 0
    for row in rows:
        result.append(row)
        if row.get("DOCULECT") != "English":
            continue
        clone = row.copy()
        clone["ID"] = str(next_id)
        next_id += 1
        clone["DOCULECT"] = "Old_English"
        note = (clone.get("NOTE") or "").strip()
        clone["NOTE"] = note_suffix if not note else f"{note} | {note_suffix}"
        clone.setdefault("COUNTERPART", row.get("COUNTERPART", ""))
        clone.setdefault("IPA", row.get("IPA", ""))
        clone.setdefault("TOKENS", row.get("TOKENS", ""))
        result.append(clone)
        added += 1
    return result, added

def add_old_english_rows(tsv: Path, note_suffix: str = DEFAULT_NOTE) -> int:
    fieldnames, rows = load_rows(tsv)
    updated_rows, added = duplicate_english_rows(rows, note_suffix)
    write_rows(tsv, fieldnames, updated_rows)
    return added


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tsv", type=Path, help="Path to germanic-aligned TSV")
    parser.add_argument(
        "--note",
        default=DEFAULT_NOTE,
        help="Note appended to each placeholder row",
    )
    args = parser.parse_args()
    added = add_old_english_rows(args.tsv, args.note)
    print(f"Added {added} Old English placeholder rows to {args.tsv}.")

if __name__ == "__main__":
    main()

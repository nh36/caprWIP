#!/usr/bin/env python3
"""Update Old English rows with attested forms from Wiktionary's Swadesh list."""
from __future__ import annotations
import argparse
import csv
import re
import unicodedata
from pathlib import Path
from typing import Iterable

DATA_ROOT = Path(__file__).resolve().parents[1] / "data"
SWADESH_PATH = DATA_ROOT / "old_english_swadesh.tsv"
WIKTIONARY_PATH = DATA_ROOT / "old_english_wiktionary.tsv"
SWADESH_NOTE = "Source: Wiktionary Old English Swadesh list (retrieved 2025-12-12)"
WIKTIONARY_NOTE_TEMPLATE = "Source: Wiktionary etymology ({detail})"
COMBINING_MARKS = {"Mn", "Me", "Mc"}
TIE_BARS = {"\u0361", "\u035C"}
LENGTH_MARKS = {"\u02D0", "\u02D1"}


def normalize_label(label: str) -> str:
    label = label.lower().strip()
    label = re.sub(r"\([^)]*\)", "", label)
    label = label.replace("_", " ")
    label = re.sub(r"[^a-z0-9]+", " ", label)
    return label.strip()


def pick_first(value: str) -> str:
    value = re.sub(r"\([^)]*\)", "", value)
    for delimiter in [",", ";", "/", " or ", "=" ]:
        if delimiter in value:
            value = value.split(delimiter)[0]
            break
    return value.strip()


def clean_ipa(raw: str) -> str:
    choices = re.findall(r"/([^/]+)/", raw)
    token = choices[0] if choices else raw.strip()
    token = token.strip().strip("/")
    token = token.replace(" ", "")
    return token


def ipa_to_tokens(ipa: str) -> list[str]:
    tokens: list[str] = []
    current = ""
    tie_active = False
    for ch in ipa:
        if ch.isspace():
            continue
        if ch in {"/", "[", "]"}:
            continue
        cat = unicodedata.category(ch)
        if ch in LENGTH_MARKS or cat in COMBINING_MARKS:
            if not current:
                current = ch
            else:
                current += ch
            continue
        if ch in TIE_BARS:
            if not current:
                current = ch
            else:
                current += ch
            tie_active = True
            continue
        if tie_active:
            current += ch
            tie_active = False
            continue
        if current:
            tokens.append(current)
        current = ch
    if current:
        tokens.append(current)
    return tokens


def load_swadesh_mapping() -> dict[str, dict[str, str]]:
    mapping: dict[str, dict[str, str]] = {}
    with SWADESH_PATH.open() as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            english = row["ENGLISH"].strip()
            key = normalize_label(english)
            oe_form = pick_first(row["OLD_ENGLISH"]).replace("·", "")
            ipa = clean_ipa(row["IPA_RAW"])
            if not oe_form:
                continue
            tokens = ipa_to_tokens(ipa) if ipa else []
            mapping[key] = {
                "english": english,
                "oe_form": oe_form,
                "ipa": ipa,
                "tokens": tokens,
                "note": SWADESH_NOTE,
            }
    return mapping


def orth_tokens(lemma: str) -> list[str]:
    tokens: list[str] = []
    for ch in lemma:
        if ch.isspace() or ch in {"-", "·"}:
            continue
        tokens.append(ch)
    return tokens


def load_wiktionary_mapping() -> dict[str, dict[str, str]]:
    mapping: dict[str, dict[str, str]] = {}
    if not WIKTIONARY_PATH.exists():
        return mapping
    with WIKTIONARY_PATH.open() as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            english = row.get("ENGLISH", "").strip()
            oe_form = row.get("OE_FORM", "").strip()
            if not english or not oe_form:
                continue
            key = normalize_label(english)
            detail = row.get("DETAIL", "").strip() or row.get("SOURCE", "").strip()
            note = WIKTIONARY_NOTE_TEMPLATE.format(detail=detail or "template")
            tokens = orth_tokens(oe_form)
            mapping[key] = {
                "english": english,
                "oe_form": oe_form,
                "ipa": "",
                "tokens": tokens,
                "note": note,
            }
    return mapping


def load_mapping() -> dict[str, dict[str, str]]:
    mapping: dict[str, dict[str, str]] = {}
    for source in (load_swadesh_mapping(), load_wiktionary_mapping()):
        for key, entry in source.items():
            mapping[key] = entry
    return mapping


def load_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames is None:
            raise RuntimeError(f"Missing header in {path}")
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


def update_rows(rows: Iterable[dict[str, str]], mapping: dict[str, dict[str, str]]) -> int:
    updated = 0
    for row in rows:
        if row.get("DOCULECT") != "Old_English":
            continue
        counterpart_key = normalize_label(row.get("COUNTERPART", ""))
        concept_key = normalize_label(row.get("CONCEPT", ""))
        entry = mapping.get(counterpart_key) or mapping.get(concept_key)
        if not entry:
            continue
        row["COUNTERPART"] = entry["oe_form"]
        if entry.get("ipa"):
            row["IPA"] = entry["ipa"]
        if entry.get("tokens"):
            row["TOKENS"] = " ".join(entry["tokens"])
        note = (row.get("NOTE") or "").strip()
        if note.startswith("TODO: replace with attested Old English form"):
            note = ""
        entry_note = entry.get("note", SWADESH_NOTE)
        row["NOTE"] = entry_note if not note else f"{note} | {entry_note}"
        updated += 1
    return updated


def process_file(path: Path, mapping: dict[str, dict[str, str]]) -> int:
    fieldnames, rows = load_rows(path)
    updated = update_rows(rows, mapping)
    write_rows(path, fieldnames, rows)
    return updated


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="TSV files to update")
    args = parser.parse_args()
    mapping = load_mapping()
    total = 0
    for path in args.paths:
        updated = process_file(path, mapping)
        total += updated
        print(f"Updated {updated} Old English rows in {path}")
    if not total:
        print("No rows updated; verify concept labels overlap with the Swadesh list")


if __name__ == "__main__":
    main()

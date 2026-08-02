#!/usr/bin/env python3
"""Exact assembled-Markdown occurrence parity for explicit .iv/.pred spans."""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "tools"))

from index_verborum_emission import classify_emission, load_model_entry_headings

FORMS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_forms.tsv"
PRINT_MAIN_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_main.tsv"
PRINT_EXCLUDED_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_excluded.tsv"
DEFAULT_BOOK_MD = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.md"

EXPLICIT_TAG_RE = re.compile(r"\[(?P<content>[^\]]+)\]\{(?P<attrs>[^}]*)\}")
NESTED_RECON_IV_RE = re.compile(r"\[\[(?P<form>[^\]]+)\]\{\.recon\}(?P<tail>.*?)\]\{(?P<attrs>[^}]*)\}")


def parse_attr_string(raw: str) -> dict[str, str]:
    attrs: dict[str, str] = {}
    for key, value in re.findall(r'([A-Za-z0-9_:-]+)\s*=\s*"([^"]*)"', raw):
        attrs[key] = value
    for key, value in re.findall(r"([A-Za-z0-9_:-]+)\s*=\s*([^\s}]+)", raw):
        attrs.setdefault(key, value)
    return attrs


def has_tag_class(raw_attrs: str, cls: str) -> bool:
    return re.search(rf"(^|\s)\.{re.escape(cls)}(?=\s|$)", raw_attrs) is not None


def normalize_form(text: str) -> str:
    value = text.strip()
    if value.startswith("`") and value.endswith("`"):
        value = value[1:-1]
    if value.startswith("_") and value.endswith("_") and len(value) > 2:
        value = value[1:-1]
    value = value.replace(r"\*", "*")
    if value.startswith("*") and value.endswith("*") and len(value) > 2:
        value = value[1:-1]
    return value.strip()


def normalize_display(text: str) -> str:
    value = text.strip()
    if value.startswith("_") and value.endswith("_") and len(value) > 2:
        value = value[1:-1]
    if value.startswith("`") and value.endswith("`") and len(value) > 2:
        value = value[1:-1]
    value = re.sub(r"(\*[^`\s|<>]*-?)\*$", r"\1", value)
    return value.strip()


def extract_spans_from_book(book_md: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line_no, line in enumerate(book_md.read_text(encoding="utf-8").splitlines(), start=1):
        line_counter = 0
        nested_spans = [(m.start(), m.end()) for m in NESTED_RECON_IV_RE.finditer(line)]
        for m in NESTED_RECON_IV_RE.finditer(line):
            attrs_raw = m.group("attrs")
            if not (has_tag_class(attrs_raw, "iv") or has_tag_class(attrs_raw, "pred")):
                continue
            line_counter += 1
            attrs = parse_attr_string(attrs_raw)
            rows.append(
                {
                    "occurrence_id": (attrs.get("occ_id") or "").strip(),
                    "source_ref": (attrs.get("source_ref") or "").strip(),
                    "language": (attrs.get("lang") or "").strip(),
                    "form_role": (attrs.get("role") or "evidence_form").strip(),
                    "variety": (attrs.get("variety") or "").strip(),
                    "sort_key": (attrs.get("sort") or normalize_form(m.group("form"))).strip(),
                    "display": normalize_display((attrs.get("display") or f"*{normalize_form(m.group('form'))}").strip()),
                    "normalized_visible_form": normalize_form(m.group("form")),
                    "reconstruction_status": "1",
                    "span_class": "pred" if has_tag_class(attrs_raw, "pred") else "iv",
                    "line_span_ordinal": str(line_counter),
                    "line_no": str(line_no),
                }
            )
        scrubbed = list(line)
        for s, e in nested_spans:
            for i in range(s, e):
                scrubbed[i] = " "
        scrubbed_line = "".join(scrubbed)
        for m in EXPLICIT_TAG_RE.finditer(scrubbed_line):
            attrs_raw = m.group("attrs")
            if not (has_tag_class(attrs_raw, "iv") or has_tag_class(attrs_raw, "pred")):
                continue
            line_counter += 1
            attrs = parse_attr_string(attrs_raw)
            content = normalize_form(m.group("content"))
            is_recon = has_tag_class(attrs_raw, "recon")
            rows.append(
                {
                    "occurrence_id": (attrs.get("occ_id") or "").strip(),
                    "source_ref": (attrs.get("source_ref") or "").strip(),
                    "language": (attrs.get("lang") or "").strip(),
                    "form_role": (attrs.get("role") or "evidence_form").strip(),
                    "variety": (attrs.get("variety") or "").strip(),
                    "sort_key": (attrs.get("sort") or content).strip(),
                    "display": normalize_display((attrs.get("display") or (f"*{content}" if is_recon else content)).strip()),
                    "normalized_visible_form": content,
                    "reconstruction_status": "1" if is_recon else "0",
                    "span_class": "pred" if has_tag_class(attrs_raw, "pred") else "iv",
                    "line_span_ordinal": str(line_counter),
                    "line_no": str(line_no),
                }
            )
    return rows


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def explicit_in_book(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    headings = load_model_entry_headings()
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        if (row.get("source_scope") or "").strip() != "explicit_tag":
            continue
        occ_id = (row.get("occurrence_id") or "").strip()
        if not occ_id:
            continue
        if not classify_emission(row, headings).in_book:
            continue
        out[occ_id] = row
    return out


def _suffix_ordinal(occ_id: str) -> str:
    if ":" not in occ_id:
        return ""
    tail = occ_id.rsplit(":", 1)[1]
    return tail if tail.isdigit() else ""


def check_parity(book_md: Path) -> None:
    forms = load_rows(FORMS_PATH)
    main = load_rows(PRINT_MAIN_PATH)
    excluded = load_rows(PRINT_EXCLUDED_PATH)

    in_book_forms = explicit_in_book(forms)
    in_book_main = explicit_in_book(main)
    in_book_excluded = explicit_in_book(excluded)

    expected_all = set(in_book_forms)
    expected_printable = set(in_book_main)
    expected_excluded = set(in_book_excluded)

    if expected_printable | expected_excluded != expected_all:
        raise AssertionError("in-book explicit IDs do not partition into printable ⊎ excluded")
    if expected_printable & expected_excluded:
        raise AssertionError("printable/excluded in-book explicit ID sets overlap")

    spans = [
        s for s in extract_spans_from_book(book_md)
        if s["span_class"] in {"iv", "pred"}
        and (s.get("language") or "").strip()
        and ">" not in (s.get("normalized_visible_form") or "")
    ]
    occ_ids = [s["occurrence_id"] for s in spans if s["occurrence_id"]]
    actual_counter = Counter(occ_ids)

    unknown = sorted({oid for oid in occ_ids if oid not in expected_all})
    missing = sorted(oid for oid in expected_all if oid not in actual_counter)
    duplicates = sorted(oid for oid, c in actual_counter.items() if c > 1)

    semantic_mismatch: list[str] = []
    swapped_ordinal: list[str] = []
    for span in spans:
        occ_id = span["occurrence_id"]
        if not occ_id or occ_id not in expected_all:
            continue
        row = in_book_forms[occ_id]
        checks = {
            "source_ref": (row.get("source_ref") or "").strip(),
            "language": (row.get("language") or "").strip(),
            "form_role": (row.get("form_role") or "evidence_form").strip(),
            "variety": (row.get("variety") or "").strip(),
            "sort_key": (row.get("sort_key") or "").strip(),
            "display": (row.get("display") or "").strip(),
            "normalized_visible_form": (row.get("form") or "").strip(),
        }
        for key, exp in checks.items():
            if (span.get(key) or "").strip() != exp:
                semantic_mismatch.append(f"{occ_id}:{key}:expected={exp!r}:actual={(span.get(key) or '').strip()!r}")
                break
        ordinal = _suffix_ordinal(occ_id)
        if ordinal and span["line_span_ordinal"] != ordinal:
            swapped_ordinal.append(f"{occ_id} line={span['line_no']} seen_ordinal={span['line_span_ordinal']}")

    printables_seen = sum(1 for oid in occ_ids if oid in expected_printable)
    excluded_seen = sum(1 for oid in occ_ids if oid in expected_excluded)
    pred_seen = sum(1 for s in spans if s["span_class"] == "pred")
    print(
        "assembled explicit parity: "
        f"printable={printables_seen} excluded={excluded_seen} pred={pred_seen} "
        f"unknown={len(unknown)} duplicate={len(duplicates)} missing={len(missing)} "
        f"semantic_mismatch={len(semantic_mismatch)}"
    )

    errors: list[str] = []
    if unknown:
        errors.append(f"unknown occ_id count={len(unknown)} first={unknown[:5]}")
    if duplicates:
        errors.append(f"duplicate occ_id count={len(duplicates)} first={duplicates[:5]}")
    if missing:
        errors.append(f"missing expected occ_id count={len(missing)} first={missing[:5]}")
    if semantic_mismatch:
        errors.append(f"semantic mismatches count={len(semantic_mismatch)} first={semantic_mismatch[:5]}")
    if swapped_ordinal:
        errors.append(f"line-ordinal/occ_id suffix mismatches count={len(swapped_ordinal)} first={swapped_ordinal[:5]}")
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book-md", type=Path, default=DEFAULT_BOOK_MD)
    args = parser.parse_args()
    check_parity(args.book_md)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact assembled-Markdown occurrence parity for explicit .iv/.pred spans."""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "tools"))

from index_verborum_explicit_plan import (
    explicit_in_book,
    load_rows,
    book_source_paths,
    scan_explicit_spans,
)

FORMS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_forms.tsv"
PRINT_MAIN_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_main.tsv"
PRINT_EXCLUDED_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_excluded.tsv"
DEFAULT_BOOK_MD = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.md"

def _suffix_ordinal(occ_id: str) -> str:
    if ":" not in occ_id:
        return ""
    tail = occ_id.rsplit(":", 1)[1]
    return tail if tail.isdigit() else ""


def check_parity(book_md: Path) -> None:
    forms = load_rows(FORMS_PATH)
    main = load_rows(PRINT_MAIN_PATH)
    excluded = load_rows(PRINT_EXCLUDED_PATH)

    source_paths = book_source_paths()
    in_book_forms = explicit_in_book(forms, source_paths)
    in_book_main = explicit_in_book(main, source_paths)
    in_book_excluded = explicit_in_book(excluded, source_paths)

    expected_all = set(in_book_forms)
    expected_printable = set(in_book_main)
    expected_excluded = set(in_book_excluded)

    if expected_printable | expected_excluded != expected_all:
        raise AssertionError("in-book explicit IDs do not partition into printable ⊎ excluded")
    if expected_printable & expected_excluded:
        raise AssertionError("printable/excluded in-book explicit ID sets overlap")

    # Derivation-chain spans (those with ">" in the visible form) are excluded
    # from plan membership because they represent multi-form chains.  Exactly 1
    # such span is expected in the assembled book; see inventory_spans() for the
    # canonical assertion.
    spans = [
        s for s in scan_explicit_spans(book_md.read_text(encoding="utf-8"))
        if s["span_class"] == "iv"
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
    print(
        "assembled explicit parity: "
        f"printable={printables_seen} excluded={excluded_seen} "
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

#!/usr/bin/env python3
"""check_book_occ_id_parity.py — Exact occurrence-level parity check.

Verifies that every explicit_tag occurrence in index_verborum_book_main.tsv
has exactly one corresponding span with a matching occ_id attribute in the
assembled capr_book_draft_alpha_01.md.

This proves that every explicit-tag printable occurrence is represented in
the assembled book exactly once — no missing and no duplicated occurrences.

For heading/line-injected rows, the existing command-level parity check in
check_book_draft_tex_indexes.py applies.

Exit codes:
  0  — parity verified
  1  — parity failure (missing or duplicate occ_ids)
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BOOK_MAIN_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_book_main.tsv"
DEFAULT_BOOK_MD = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.md"


def _load_book_main_occ_ids(path: Path) -> Counter[str]:
    rows = list(csv.DictReader(path.open(encoding="utf-8"), delimiter="\t"))
    explicit = [
        r for r in rows
        if (r.get("source_scope") or "").strip() == "explicit_tag"
        and (r.get("occurrence_id") or "").strip()
    ]
    return Counter(r["occurrence_id"] for r in explicit)


def _extract_occ_ids_from_md(text: str) -> Counter[str]:
    return Counter(re.findall(r'occ_id="([^"]+)"', text))


def check_parity(book_md_path: Path, book_main_path: Path) -> None:
    if not book_main_path.exists():
        print(
            f"book_main.tsv not found at {book_main_path}; "
            "run build_index_verborum.py and index_verborum_emission.py first.",
            file=sys.stderr,
        )
        sys.exit(1)

    expected: Counter[str] = _load_book_main_occ_ids(book_main_path)
    book_text = book_md_path.read_text(encoding="utf-8")
    actual: Counter[str] = _extract_occ_ids_from_md(book_text)

    errors: list[str] = []

    # 1. No duplicate occ_ids in the assembled book.
    duplicates = {k: v for k, v in actual.items() if v > 1}
    if duplicates:
        errors.append(
            f"{len(duplicates)} occ_id(s) appear more than once in assembled book "
            f"(duplicate occurrence markers):\n"
            + "\n".join(f"  {k}: {v}" for k, v in sorted(duplicates.items())[:5])
        )

    # 2. Every expected explicit occ_id appears at least once in the assembled book.
    missing = {k: v for k, v in expected.items() if k not in actual}
    if missing:
        errors.append(
            f"{len(missing)} expected explicit_tag occ_id(s) missing from assembled book:\n"
            + "\n".join(
                f"  {k} (expected={expected[k]})"
                for k in sorted(missing)[:5]
            )
        )

    # 3. Report extras for information (excluded occurrences — not a failure).
    extras = {k: v for k, v in actual.items() if k not in expected}

    if errors:
        print("FAIL: occurrence-level parity errors:", file=sys.stderr)
        for err in errors:
            print(err, file=sys.stderr)
        sys.exit(1)

    print(
        f"occurrence-level parity: {sum(expected.values())} expected explicit "
        f"occ_ids, {sum(actual.values())} in assembled book "
        f"({len(extras)} excluded/non-printable spans present but not expected — OK)"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book-md", type=Path, default=DEFAULT_BOOK_MD)
    parser.add_argument("--book-main", type=Path, default=BOOK_MAIN_PATH)
    args = parser.parse_args()
    check_parity(args.book_md, args.book_main)


if __name__ == "__main__":
    main()

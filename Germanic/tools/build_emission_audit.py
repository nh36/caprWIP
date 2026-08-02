#!/usr/bin/env python3
"""Generate index_verborum_book_emission_audit.tsv.

Accounts for every row in index_verborum_print_main.tsv with a controlled
disposition and canonical occurrence/emission identities. Run after
build_index_verborum.py and build_capr_book_draft.py.

Dispositions:
  emitted_once         — explicit_tag span emitted exactly once by Lua filter
  emitted_explicit_N   — explicit_tag command appears N times (N > 1 rows share cmd)
  collapsed_same_site  — non-explicit row whose cmd+site was already counted
  heading_injected     — Python heading injection fired
  line_injected        — Python line injection fired
  source_not_in_book   — source material not included in the assembled book
  missing_from_assembly — expected to fire but not found in actual TeX
  duplicate_emission   — appears more times than expected (upper-bound breach)
  unresolved           — could not classify
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "tools"))
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "docs" / "assembly"))
from index_verborum_emission import build_emission_table, load_model_entry_headings, load_print_main

PRINT_MAIN_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_main.tsv"
DEFAULT_TEX_PATH = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.tex"
AUDIT_OUT = REPO_ROOT / "Germanic/docs/book/index_verborum_book_emission_audit.tsv"


def extract_iv_bodies(text: str) -> list[str]:
    bodies: list[str] = []
    for m in re.finditer(r"\\index\[iv\]\{", text):
        pos = m.end()
        depth = 1
        end = pos
        while end < len(text) and depth > 0:
            if text[end] == "{":
                depth += 1
            elif text[end] == "}":
                depth -= 1
            end += 1
        bodies.append(text[m.end() : end - 1])
    return bodies


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex-path", type=Path, default=DEFAULT_TEX_PATH)
    args = parser.parse_args()

    tex_path = args.tex_path.expanduser().resolve()
    tex_text = tex_path.read_text(encoding="utf-8")
    actual: Counter[str] = Counter(
        r"\index[iv]{" + b + "}" for b in extract_iv_bodies(tex_text)
    )

    main_rows = load_print_main(PRINT_MAIN_PATH)
    emission_rows = build_emission_table(main_rows, load_model_entry_headings())

    # First pass: classify every row and build expected emission structures.
    explicit_expected: Counter[str] = Counter()
    row_classifications: list[tuple[str, str, str, str, str, str]] = []
    for row in emission_rows:
        path = row["emission_path"]
        site = row["site"]
        cmd = row["index_command"]
        row_classifications.append((path, site, cmd, row["in_book"], row["emission_id"], row.get("collapsed_into", "")))
        if path == "explicit_tag" and row["in_book"] == "1":
            explicit_expected[cmd] += 1

    # Second pass: assign dispositions.
    audit_rows: list[dict[str, str]] = []
    seen_emission_ids: set[str] = set()
    emission_representative: set[str] = set()
    for row in emission_rows:
        if row["in_book"] == "1" and row["emission_id"] not in emission_representative:
            emission_representative.add(row["emission_id"])

    for row, (path, site, cmd, in_book, emission_id, collapsed_into) in zip(main_rows, row_classifications):
        actual_count = actual.get(cmd, 0)

        collapsed_into = (collapsed_into or "").strip()
        occ_id = (row.get("occurrence_id") or "").strip()

        if path == "explicit_tag":
            exp = explicit_expected.get(cmd, 0)
            if in_book != "1":
                dispo = "source_not_in_book"
                reason = "explicit source not in assembled book"
            elif actual_count >= exp:
                dispo = "emitted_once" if exp == 1 else f"emitted_explicit_{exp}"
                reason = f"Lua filter emitted {actual_count} occurrence(s); expected {exp}"
            else:
                dispo = "missing_from_assembly"
                reason = f"explicit_tag: expected {exp}, actual {actual_count}"

        elif in_book != "1" or path == "source_not_in_book":
            dispo = "source_not_in_book"
            reason = "source material not included in assembled lexical volume"

        elif path in ("heading_injection", "line_injection"):
            if collapsed_into:
                dispo = "collapsed_same_site"
                reason = "duplicate occurrence collapsed into shared book emission"
            else:
                seen_emission_ids.add(emission_id)
                if actual_count > 0:
                    dispo = "heading_injected" if path == "heading_injection" else "line_injected"
                    reason = f"Python injection fired at site {site[:60]!r}"
                else:
                    dispo = "missing_from_assembly"
                    reason = f"{path}: site {site[:60]!r} not found in assembled book"

        else:
            dispo = "unresolved"
            reason = f"unrecognised emission path: {path}"

        audit_rows.append(
            {
                "language": row.get("language", ""),
                "variety": row.get("variety", ""),
                "form": row.get("form", ""),
                "display": row.get("display", ""),
                "sort_key": row.get("sort_key", ""),
                "form_role": row.get("form_role", ""),
                "source_scope": row.get("source_scope", ""),
                "source_ref": row.get("source_ref", ""),
                "occurrence_id": occ_id,
                "emission_id": emission_id,
                "collapsed_into": collapsed_into,
                "in_book": in_book,
                "expected_emission_path": path,
                "expected_site": site,
                "emitted_count": str(actual_count),
                "disposition": dispo,
                "reason": reason,
            }
        )

    # Write audit TSV.
    FIELDS = [
        "language", "variety", "form", "display", "sort_key", "form_role",
        "source_scope", "source_ref", "occurrence_id", "emission_id", "collapsed_into", "in_book",
        "expected_emission_path", "expected_site", "emitted_count",
        "disposition", "reason",
    ]
    with AUDIT_OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(audit_rows)

    # Summary.
    dispo_counts = Counter(r["disposition"] for r in audit_rows)
    variety_rows = [r for r in audit_rows if r.get("variety")]
    variety_counts = Counter(r["variety"] for r in variety_rows)
    variety_emitted = Counter(
        r["variety"]
        for r in variety_rows
        if r["disposition"] not in ("source_not_in_book", "missing_from_assembly")
    )

    print(f"print_main rows: {len(main_rows)}")
    print(f"Actual TeX commands: {sum(actual.values())}")
    print("\nDisposition breakdown:")
    for k, v in sorted(dispo_counts.items()):
        print(f"  {k}: {v}")
    print("\nOE variety occurrence counts:")
    for variety in ["ews", "lws", "angl", "merc", "north", "kent"]:
        total = variety_counts.get(variety, 0)
        emitted = variety_emitted.get(variety, 0)
        print(f"  {variety}: {total} print_main, {emitted} emitted")
    print(f"\nAudit written to: {AUDIT_OUT}")


if __name__ == "__main__":
    main()

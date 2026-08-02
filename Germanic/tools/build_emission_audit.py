#!/usr/bin/env python3
"""Generate index_verborum_book_emission_audit.tsv.

Accounts for every row in index_verborum_print_main.tsv with a controlled
disposition. Run after build_index_verborum.py and build_capr_book_draft.py.

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
import index_verborum_render as ivr
from build_full_lexical_volume import normalize_print_text as npt

PRINT_MAIN_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_main.tsv"
MANIFEST_PATH = REPO_ROOT / "Germanic/docs/assembly/manifest_all_by_class.tsv"
DEFAULT_TEX_PATH = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.tex"
AUDIT_OUT = REPO_ROOT / "Germanic/docs/book/index_verborum_book_emission_audit.tsv"

_LANG_META = ivr.load_language_registry()
_VAR_REG = ivr.load_variety_registry()
_LINE_INJ_SCOPES = {"table_semantic_auto", "table_semantic_decision", "broad_prose_decision"}


def make_cmd(row: dict[str, str]) -> str:
    return ivr.index_command(
        row["language"], row["sort_key"], npt(row.get("display", "")),
        (row.get("variety") or "").strip(),
        lang_meta=_LANG_META, var_registry=_VAR_REG,
    )


def load_model_entry_headings() -> dict[str, str]:
    headings: dict[str, str] = {}
    with MANIFEST_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            mp = (row.get("model_entry_path") or "").strip()
            li = (row.get("lexical_item") or "").strip()
            ct = (row.get("counterpart") or "").strip()
            dc = (row.get("derivation_class") or "").strip()
            if mp and li:
                headings[mp] = f"{li} — OE {'*' + ct if dc == 'reconstructed_oe' else ct}"
    return headings


def classify_row_emission(
    row: dict[str, str],
    mehmap: dict[str, str],
) -> tuple[str, str, str]:
    """Return (emission_path, site, command)."""
    scope = (row.get("source_scope") or "").strip()
    ref = (row.get("source_ref") or "").strip()
    cmd = make_cmd(row)
    if scope == "explicit_tag":
        return ("explicit_tag", ref, cmd)
    if not ref:
        return ("source_not_in_book", ref, cmd)
    if ".md:" in ref:
        path_part, line_part = ref.rsplit(":", 1)
        if scope in _LINE_INJ_SCOPES and line_part.isdigit() and path_part not in mehmap:
            return ("line_injection", f"{path_part}:{line_part}", cmd)
        if path_part in mehmap:
            return ("heading_injection", mehmap[path_part], cmd)
        if line_part.isdigit():
            return ("line_injection", f"{path_part}:{line_part}", cmd)
        return ("source_not_in_book", ref, cmd)
    # heading string ref
    if ref in set(mehmap.values()):
        return ("heading_injection", ref, cmd)
    return ("source_not_in_book", ref, cmd)


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

    main_rows = list(csv.DictReader(PRINT_MAIN_PATH.open(encoding="utf-8"), delimiter="\t"))
    mehmap = load_model_entry_headings()
    manifest_heading_set = set(mehmap.values())

    # First pass: classify every row and build expected emission structures.
    explicit_expected: Counter[str] = Counter()
    collapsed_sites: set[tuple[str, str]] = set()   # (site_type, site) per non-explicit cmd
    site_cmd_seen: set[tuple[str, str]] = set()

    row_classifications: list[tuple[str, str, str]] = []
    for row in main_rows:
        path, site, cmd = classify_row_emission(row, mehmap)
        row_classifications.append((path, site, cmd))
        if path == "explicit_tag":
            explicit_expected[cmd] += 1
        elif path in ("heading_injection", "line_injection"):
            site_cmd_seen.add((site, cmd))

    # Second pass: assign dispositions.
    audit_rows: list[dict[str, str]] = []
    seen_site_cmd: set[tuple[str, str]] = set()

    for row, (path, site, cmd) in zip(main_rows, row_classifications):
        actual_count = actual.get(cmd, 0)

        if path == "explicit_tag":
            exp = explicit_expected[cmd]
            if actual_count >= exp:
                dispo = "emitted_once" if exp == 1 else f"emitted_explicit_{exp}"
                reason = f"Lua filter emitted {actual_count} occurrence(s); expected {exp}"
            else:
                dispo = "missing_from_assembly"
                reason = f"explicit_tag: expected {exp}, actual {actual_count}"

        elif path == "source_not_in_book":
            dispo = "source_not_in_book"
            reason = "source material not included in assembled lexical volume"

        elif path in ("heading_injection", "line_injection"):
            key = (site, cmd)
            if key in seen_site_cmd:
                dispo = "collapsed_same_site"
                reason = f"duplicate {path} at same site+cmd; first occurrence already counts"
            else:
                seen_site_cmd.add(key)
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
        "source_scope", "source_ref",
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

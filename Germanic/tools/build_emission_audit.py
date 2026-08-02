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

Exit nonzero if any invariant fails.
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


def validate_command_counts(
    emission_rows: list[dict[str, str]],
    actual: Counter[str],
) -> list[str]:
    """Validate that every in-book emission fires the expected number of times.

    Constructs expected_commands from canonical in-book emission plan:
      expected_commands[cmd] = count of distinct in-book emission_ids with that cmd

    Compares with actual TeX commands extracted from the final build.

    Returns a list of error messages. Empty list means all counts match.
    """
    # Unique in-book emission_ids and their command
    seen: set[str] = set()
    expected: Counter[str] = Counter()
    rep_by_cmd: defaultdict[str, list[str]] = defaultdict(list)
    for row in emission_rows:
        if row["in_book"] != "1":
            continue
        eid = row["emission_id"]
        if eid in seen:
            continue
        seen.add(eid)
        cmd = row["index_command"]
        expected[cmd] += 1
        rep_occ = row["occurrence_id"] if not (row.get("collapsed_into") or "").strip() else None
        if rep_occ:
            rep_by_cmd[cmd].append(f"emission={eid[:20]},rep={rep_occ[:40]}")

    errors: list[str] = []
    all_cmds = set(expected) | set(actual)
    for cmd in all_cmds:
        exp = expected.get(cmd, 0)
        act = actual.get(cmd, 0)
        if act < exp:
            errors.append(
                f"MISSING emission: expected={exp} actual={act}\n"
                f"  cmd: {cmd[:120]}\n"
                f"  sources: {rep_by_cmd.get(cmd, [])[:3]}"
            )
        elif act > exp:
            errors.append(
                f"DUPLICATE emission: expected={exp} actual={act}\n"
                f"  cmd: {cmd[:120]}"
            )
    return errors


def validate_audit(
    main_rows: list[dict[str, str]],
    audit_rows: list[dict[str, str]],
    emission_rows: list[dict[str, str]],
    actual: Counter[str] | None = None,
) -> None:
    """Fail-closed runtime validation of the generated audit.

    Raises AssertionError on any invariant violation.
    """
    errors: list[str] = []

    # 1. Exact occurrence coverage.
    pm_ids = Counter((r.get("occurrence_id") or "").strip() for r in main_rows)
    audit_ids = Counter((r.get("occurrence_id") or "").strip() for r in audit_rows)
    if "" in pm_ids:
        errors.append(f"print_main has {pm_ids['']} rows with blank occurrence_id")
    if "" in audit_ids:
        errors.append(f"audit has {audit_ids['']} rows with blank occurrence_id")
    pm_ids.pop("", None)
    audit_ids.pop("", None)
    if pm_ids != audit_ids:
        missing = sorted(k for k in pm_ids if pm_ids[k] != audit_ids.get(k, 0))
        extra = sorted(k for k in audit_ids if audit_ids[k] != pm_ids.get(k, 0))
        errors.append(
            f"Audit occurrence_id coverage mismatch: "
            f"{len(missing)} missing, {len(extra)} extra"
            + (f"\n  missing examples: {missing[:3]}" if missing else "")
            + (f"\n  extra examples: {extra[:3]}" if extra else "")
        )

    # 2. Build exact structures for representative and emission validation.
    in_book_by_emission: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    for row in emission_rows:
        if row["in_book"] == "1":
            in_book_by_emission[row["emission_id"]].append(row)

    representatives_by_emission: dict[str, list[dict[str, str]]] = {
        eid: [r for r in rows if not (r.get("collapsed_into") or "").strip()]
        for eid, rows in in_book_by_emission.items()
    }

    audit_by_emission: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    for row in audit_rows:
        if (row.get("in_book") or "").strip() == "1":
            audit_by_emission[(row.get("emission_id") or "").strip()].append(row)

    # 3. Per-emission invariants.
    for eid, et_rows in in_book_by_emission.items():
        reps = representatives_by_emission[eid]
        is_explicit = all(r.get("source_scope") == "explicit_tag" for r in et_rows)
        is_shared = len(et_rows) > 1

        # Every emission must have exactly one representative.
        if len(reps) != 1:
            errors.append(
                f"Emission {eid[:30]}: expected 1 representative, "
                f"got {len(reps)} (collapsed_into=='' rows)"
            )

        # Explicit emissions must have exactly one occurrence and no collapse.
        if is_explicit and len(et_rows) != 1:
            errors.append(f"Explicit emission {eid[:30]} has {len(et_rows)} occurrences; expected 1")
        if is_explicit and et_rows and (et_rows[0].get("collapsed_into") or "").strip():
            errors.append(f"Explicit emission {eid[:30]} has nonblank collapsed_into")

        # Non-explicit collapsing: all non-representative rows must point to emission_id.
        for row in et_rows:
            ci = (row.get("collapsed_into") or "").strip()
            is_rep = not ci
            if not is_rep and ci != eid:
                errors.append(
                    f"Emission {eid[:30]}: collapsed occurrence {row['occurrence_id'][:40]} "
                    f"has collapsed_into={ci!r} != emission_id={eid[:30]!r}"
                )

        # Audit disposition pattern for shared non-explicit emissions.
        if is_shared and not is_explicit:
            a_rows = audit_by_emission.get(eid, [])
            injected = [r for r in a_rows if r.get("disposition") in ("heading_injected", "line_injected")]
            collapsed = [r for r in a_rows if r.get("disposition") == "collapsed_same_site"]
            expected_path = et_rows[0].get("emission_path", "")
            expected_dispo = "heading_injected" if expected_path == "heading_injection" else "line_injected"
            if len(injected) != 1:
                errors.append(
                    f"Shared emission {eid[:30]}: expected 1 injected audit row, "
                    f"got {len(injected)}"
                )
            if len(collapsed) != len(et_rows) - 1:
                errors.append(
                    f"Shared emission {eid[:30]}: expected {len(et_rows)-1} collapsed rows, "
                    f"got {len(collapsed)}"
                )
            for r in injected:
                if r.get("disposition") != expected_dispo:
                    errors.append(
                        f"Shared emission {eid[:30]}: injected row has disposition "
                        f"{r.get('disposition')!r}, expected {expected_dispo!r}"
                    )

        # Audit disposition pattern for singleton non-explicit emissions.
        if not is_shared and not is_explicit:
            a_rows = audit_by_emission.get(eid, [])
            if len(a_rows) != 1:
                errors.append(f"Singleton emission {eid[:30]} has {len(a_rows)} audit rows; expected 1")
            for r in a_rows:
                if r.get("disposition") not in ("heading_injected", "line_injected"):
                    errors.append(
                        f"Singleton emission {eid[:30]}: wrong disposition {r.get('disposition')!r}"
                    )
                if (r.get("collapsed_into") or "").strip():
                    errors.append(f"Singleton emission {eid[:30]}: nonblank collapsed_into")

    # 4. Collapsed audit rows point to existing emissions with one representative.
    for row in audit_rows:
        ci = (row.get("collapsed_into") or "").strip()
        eid = (row.get("emission_id") or "").strip()
        dispo = (row.get("disposition") or "").strip()
        if not ci:
            continue
        if dispo != "collapsed_same_site":
            errors.append(f"collapsed row has wrong disposition {dispo!r}: {row.get('occurrence_id')}")
        if eid not in representatives_by_emission:
            errors.append(f"collapsed row points to nonexistent emission {eid!r}: {row.get('occurrence_id')}")
        elif len(representatives_by_emission.get(eid, [])) != 1:
            errors.append(f"collapsed row's emission {eid!r} has multiple representatives")
        if ci != eid:
            errors.append(f"collapsed_into={ci!r} != emission_id={eid!r}: {row.get('occurrence_id')}")

    # 5. Book/emission consistency for non-book rows.
    for r in audit_rows:
        in_bk = (r.get("in_book") or "").strip()
        dispo = (r.get("disposition") or "").strip()
        eid = (r.get("emission_id") or "").strip()
        if in_bk == "1" and not eid:
            errors.append(f"in_book audit row has blank emission_id: {r.get('occurrence_id')}")
        if in_bk != "1" and dispo != "source_not_in_book":
            errors.append(f"non-book row has wrong disposition {dispo!r}: {r.get('occurrence_id')}")
        if dispo == "source_not_in_book" and in_bk == "1":
            errors.append(f"source_not_in_book row claims in_book=1: {r.get('occurrence_id')}")

    # 6. Command-count validation (if actual TeX commands provided).
    if actual is not None:
        cmd_errors = validate_command_counts(emission_rows, actual)
        errors.extend(cmd_errors)

    # 7. No forbidden dispositions.
    BAD_DISPOSITIONS = {"missing_from_assembly", "unresolved", "duplicate_emission"}
    bad = [(r.get("occurrence_id"), r.get("disposition")) for r in audit_rows
           if (r.get("disposition") or "") in BAD_DISPOSITIONS]
    if bad:
        errors.append(
            f"Audit contains {len(bad)} forbidden disposition(s) "
            f"({sorted({d for _, d in bad})}):\n  "
            + "\n  ".join(f"{occ}: {dispo}" for occ, dispo in bad[:5])
        )

    if errors:
        print("AUDIT VALIDATION FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        raise AssertionError(f"Audit validation failed with {len(errors)} error(s)")


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

    # Fail-closed validation before writing.
    try:
        validate_audit(main_rows, audit_rows, emission_rows, actual)
    except AssertionError as e:
        sys.exit(str(e))

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

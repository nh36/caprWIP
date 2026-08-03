#!/usr/bin/env python3
"""Stage 3B explicit-plan production checker.

Verifies that the production explicit plan is valid and that running pandoc
in plan mode with completeness enforcement produces the expected output.
"""
from __future__ import annotations

import csv
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BOOK = REPO_ROOT / "Germanic/docs/book"
ASSEMBLY_MD = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.md"
FILTER_LUA = REPO_ROOT / "Germanic/tools/index_verborum_filter.lua"

EXPLICIT_PLAN = BOOK / "index_verborum_book_explicit_plan.tsv"
BOOK_EMISSIONS = BOOK / "index_verborum_book_emissions.tsv"
PRINT_EXCLUDED = BOOK / "index_verborum_print_excluded.tsv"

EXPECTED_PLAN_ROWS = 1496
EXPECTED_EMIT = 1417
EXPECTED_SUPPRESS = 79
EXPECTED_TOTAL_CMDS = 1865
EXPECTED_UNIQUE_CMDS = 828

sys.path.insert(0, str(REPO_ROOT / "Germanic" / "tools"))
from index_verborum_explicit_plan import scan_explicit_spans


def _pandoc_available() -> bool:
    return subprocess.run(["pandoc", "--version"], capture_output=True).returncode == 0


def _load_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def _extract_iv_commands(text: str) -> list[str]:
    cmds = []
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
        cmds.append(r"\index[iv]{" + text[m.end() : end - 1] + "}")
    return cmds


def _narrow_tex_normalize(tex: str) -> str:
    raw_lines = [ln.rstrip() for ln in tex.splitlines()]
    norm: list[str] = []
    i = 0
    n = len(raw_lines)
    cmd_re = re.compile(r"^\\index\[iv\]\{.*\}$")
    while i < n:
        line = raw_lines[i]
        if cmd_re.match(line):
            while norm and norm[-1] == "":
                norm.pop()
            norm.append(line)
            j = i + 1
            while j < n and raw_lines[j] == "":
                j += 1
            if j < n:
                norm.append("")
            i = j
            continue
        norm.append(line)
        i += 1
    return "\n".join(norm)


def _run_pandoc(md_text: str, *, require_completeness: bool = True) -> str:
    env = dict(os.environ)
    env.update(
        {
            "CAPR_IV_BOOK_EMISSIONS_TSV": str(BOOK_EMISSIONS),
            "CAPR_IV_EXPLICIT_PLAN_TSV": str(EXPLICIT_PLAN),
            "CAPR_IV_REQUIRE_EXPLICIT_COMPLETENESS": "1" if require_completeness else "0",
        }
    )
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "plan.md"
        src.write_text(md_text, encoding="utf-8")
        proc = subprocess.run(
            ["pandoc", str(src), "--from", "markdown+raw_tex", "--to", "latex", "--lua-filter", str(FILTER_LUA)],
            capture_output=True,
            text=True,
            cwd=str(REPO_ROOT),
            env=env,
        )
        if proc.returncode != 0:
            raise AssertionError(f"pandoc failed:\n{proc.stderr[:800]}")
        return proc.stdout


def check(
    *,
    plan_rows_override: list[dict[str, str]] | None = None,
    markdown_override: str | None = None,
) -> None:
    errors: list[str] = []
    plan_rows = plan_rows_override if plan_rows_override is not None else _load_tsv(EXPLICIT_PLAN)
    emissions = _load_tsv(BOOK_EMISSIONS)
    excluded = _load_tsv(PRINT_EXCLUDED)
    md_text = markdown_override if markdown_override is not None else ASSEMBLY_MD.read_text(encoding="utf-8")

    # A. plan partition
    plan_counts = Counter((r.get("disposition") or "").strip() for r in plan_rows)
    if len(plan_rows) != EXPECTED_PLAN_ROWS:
        errors.append(f"A: rows={len(plan_rows)} != {EXPECTED_PLAN_ROWS}")
    if plan_counts.get("emit", 0) != EXPECTED_EMIT:
        errors.append(f"A: emit={plan_counts.get('emit', 0)} != {EXPECTED_EMIT}")
    if plan_counts.get("suppress", 0) != EXPECTED_SUPPRESS:
        errors.append(f"A: suppress={plan_counts.get('suppress', 0)} != {EXPECTED_SUPPRESS}")
    dup_plan = [k for k, v in Counter((r.get("occurrence_id") or "").strip() for r in plan_rows).items() if v > 1]
    if dup_plan:
        errors.append(f"A: duplicate occurrence_id in plan ({len(dup_plan)})")
    unsupported_disp = [k for k in plan_counts if k not in {"emit", "suppress"}]
    if unsupported_disp:
        errors.append(f"A: unsupported dispositions in plan: {unsupported_disp}")

    # B. assembled coverage + order
    spans = [
        s
        for s in scan_explicit_spans(md_text)
        if s["span_class"] == "iv"
        and (s.get("language") or "").strip()
        and ">" not in (s.get("normalized_visible_form") or "")
    ]
    span_ids = [s["occurrence_id"] for s in spans]
    if len(span_ids) != EXPECTED_PLAN_ROWS:
        errors.append(f"B: assembled explicit spans={len(span_ids)} != {EXPECTED_PLAN_ROWS}")
    if any(not oid for oid in span_ids):
        errors.append("B: assembled .iv span missing occ_id")
    dup_md = [k for k, v in Counter(span_ids).items() if v > 1]
    if dup_md:
        errors.append(f"B: duplicate occ_id in assembled Markdown ({len(dup_md)})")
    plan_ids = [(r.get("occurrence_id") or "").strip() for r in plan_rows]
    if plan_ids != span_ids:
        errors.append("B: assembled explicit occurrence_id order != explicit plan order")
    if set(plan_ids) != set(span_ids):
        errors.append("B: assembled/plan occurrence-id sets differ")

    # C. emit join validation
    em_by_id = {(r.get("emission_id") or "").strip(): r for r in emissions if (r.get("emission_id") or "").strip()}
    explicit_em_by_occ = {
        (r.get("representative_occurrence_id") or "").strip(): r
        for r in emissions
        if (r.get("emission_path") or "").strip() == "explicit_tag"
    }
    for row in plan_rows:
        if (row.get("disposition") or "").strip() != "emit":
            continue
        occ = (row.get("occurrence_id") or "").strip()
        eid = (row.get("emission_id") or "").strip()
        em = em_by_id.get(eid)
        if not em:
            errors.append(f"C: emit row missing emission: {occ}")
            continue
        if (em.get("emission_path") or "").strip() != "explicit_tag":
            errors.append(f"C: emit row non-explicit emission_path: {occ}")
        if (em.get("representative_occurrence_id") or "").strip() != occ:
            errors.append(f"C: representative mismatch: {occ}")
        if (em.get("source_occurrence_count") or "").strip() != "1":
            errors.append(f"C: source_occurrence_count!=1 for {occ}")
        if (em.get("source_occurrence_ids") or "").strip() != occ:
            errors.append(f"C: source_occurrence_ids mismatch for {occ}")
        if (em.get("index_command") or "").strip() != (row.get("index_command") or "").strip():
            errors.append(f"C: index_command mismatch for {occ}")

    # D. suppress join validation
    excluded_by_occ = {
        (r.get("occurrence_id") or "").strip(): r
        for r in excluded
        if (r.get("source_scope") or "").strip() == "explicit_tag"
    }
    for row in plan_rows:
        if (row.get("disposition") or "").strip() != "suppress":
            continue
        occ = (row.get("occurrence_id") or "").strip()
        reason = (row.get("exclusion_reason") or "").strip()
        ex = excluded_by_occ.get(occ)
        if not ex:
            errors.append(f"D: suppress row missing in print_excluded: {occ}")
            continue
        if (ex.get("exclusion_reason") or "").strip() != reason:
            errors.append(f"D: suppress exclusion_reason mismatch: {occ}")
        if occ in explicit_em_by_occ:
            errors.append(f"D: suppress row unexpectedly has explicit emission: {occ}")

    # E. Plan mode with completeness enforcement (single production run)
    try:
        plan_tex = _run_pandoc(md_text, require_completeness=True)
        plan_cmds = _extract_iv_commands(plan_tex)
        if len(plan_cmds) != EXPECTED_TOTAL_CMDS:
            errors.append(f"E: total commands={len(plan_cmds)} != {EXPECTED_TOTAL_CMDS}")
        if len(set(plan_cmds)) != EXPECTED_UNIQUE_CMDS:
            errors.append(f"E: unique commands={len(set(plan_cmds))} != {EXPECTED_UNIQUE_CMDS}")
    except AssertionError as exc:
        errors.append(f"E: pandoc plan+completeness run failed: {exc}")

    if errors:
        print("EXPLICIT PLAN PRODUCTION CHECK FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        raise SystemExit(1)

    print(
        "explicit plan production check passed:\n"
        f"  A: plan rows={len(plan_rows)} emit={plan_counts.get('emit', 0)} suppress={plan_counts.get('suppress', 0)}\n"
        f"  B: assembled explicit spans={len(span_ids)} order/coverage exact\n"
        f"  C: emit joins validated ({EXPECTED_EMIT})\n"
        f"  D: suppress joins validated ({EXPECTED_SUPPRESS})\n"
        f"  E: plan+completeness=1 commands={EXPECTED_TOTAL_CMDS} total, {EXPECTED_UNIQUE_CMDS} unique"
    )


def main() -> None:
    if not _pandoc_available():
        print("pandoc not found; cannot run explicit plan production check.", file=sys.stderr)
        raise SystemExit(127)
    check()


if __name__ == "__main__":
    main()

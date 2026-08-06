#!/usr/bin/env python3
"""Freeze the post-SC004-split semantic baseline (corrected PROTOFORM pass).

Records, as a key-value TSV of sha256 hashes plus literal values, the settled
state after the SC004/SC014 correction:

  * production rule definitions and executable positions;
  * the PROTOFORM-based application inventory;
  * SC004/SC014 component-behavior handbook probes;
  * first-break boundaries (SC014, SC004, and the affected SC036);
  * formal-interaction classifications;
  * full and compact traces and the mismatch report;
  * the frozen lexical output checksum;
  * the reader-facing SC004/SC014 headings and anchors.

The lexical `outputs_sha256` MUST remain aaf19ba9…480e. Host-runnable (hashes
committed artifacts and reads germanic.txt); no foma required.

Run: python3 Germanic/tools/build_post_sc004_split_semantic_baseline.py
"""
from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
G = REPO / "Germanic"
SC = G / "docs/sound_changes"
OUT = SC / "cascade_baseline/post_sc004_split_semantic_baseline.tsv"

FROZEN_OUTPUTS_SHA = "aaf19ba919cafbe86ea59d482ce74d0944f541336e246da481a3f37b20da480e"


def sha256_file(path: Path) -> str:
    if not path.exists():
        return "MISSING"
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# Terminal first-break results (a completed run). "in_progress" is NOT terminal.
TERMINAL_RESULTS = {
    "first_break_found", "no_break_before_boundary",
    "no_break_before_runner_boundary", "blocked_by_runner_limitation",
    "no_break_before_search_limit",
}


def read_first_break(path: Path) -> dict:
    """Return {direction: row} from a first-break summary TSV."""
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as handle:
        return {r["direction"]: r for r in csv.DictReader(handle, delimiter="\t")}


def require_terminal(change: str, fb: dict, directions=("earlier", "later")) -> None:
    """Refuse to freeze if any required direction is missing or still in progress."""
    for d in directions:
        row = fb.get(d)
        if row is None:
            raise SystemExit(
                f"REFUSING to freeze: {change} first-break has no '{d}' row "
                f"(run the chronology campaign first)")
        result = (row.get("result") or "").strip()
        if result not in TERMINAL_RESULTS:
            raise SystemExit(
                f"REFUSING to freeze: {change} '{d}' first-break is not terminal "
                f"(result={result!r}); complete the chronology run before freezing")


def boundary_str(row: dict) -> str:
    """Derive a boundary statement from a first-break row (never hardcoded)."""
    result = (row.get("result") or "").strip()
    if result == "first_break_found":
        crossed = (row.get("crossed_change_id") or "").strip()
        order = (row.get("first_break_order") or "").strip()
        lex = (row.get("representative_changed_lexemes") or "").strip()
        return f"first_break_found {crossed} order {order} ({lex})"
    return result


def rule_body(src: str, name: str) -> str:
    m = re.search(rf"define {name} \[\s*\n\s*(.*?)\n\s*\];", src)
    return m.group(1).strip() if m else "NOT_FOUND"


def manifest_position(manifest: str, ident: str) -> str:
    for line in manifest.splitlines():
        parts = line.split("\t")
        if len(parts) >= 2 and parts[1] == ident:
            return parts[0]
    return "?"


def reader_headings_anchors() -> str:
    files = [
        SC / "reader_facing/004-pwgmc-ai-monophthongization.md",
        SC / "reader_facing/014-015-opening-vowel-prelude.md",
    ]
    heads = []
    for f in files:
        for ln in f.read_text(encoding="utf-8").splitlines():
            if ln.startswith("## SC") or "{#rule-" in ln:
                heads.append(ln.strip())
    return "\n".join(sorted(heads))


def main() -> int:
    src = (G / "fsts/germanic.txt").read_text(encoding="utf-8")
    manifest = (SC / "cascade_baseline/cascade_order_manifest.tsv").read_text(encoding="utf-8")

    rows: list[tuple[str, str, str]] = []

    # Literal production definitions and positions.
    sc014_body = rule_body(src, "PNWGmcUnstressedAiMonophthongization")
    sc004_body = rule_body(src, "EAFAiMonophthongization")
    rows.append(("sc014_definition", sc014_body,
                 "SC014 PNWGmcUnstressedAiMonophthongization production Foma body"))
    rows.append(("sc004_definition", sc004_body,
                 "SC004 EAFAiMonophthongization production Foma body"))
    rows.append(("sc014_executable_position",
                 manifest_position(manifest, "PNWGmcUnstressedAiMonophthongization"),
                 "cascade_order_manifest position"))
    rows.append(("sc004_executable_position",
                 manifest_position(manifest, "EAFAiMonophthongization"),
                 "cascade_order_manifest position"))

    # First-break boundaries (literal).
    # First-break boundaries: derived from the summary TSVs, never hardcoded.
    # Refuse to freeze if any required chronology run is still in progress.
    fb_dir = SC / "order_tests/summaries"
    fb_sc014 = read_first_break(fb_dir / "sc004corr_first_break_sc014.tsv")
    fb_sc004 = read_first_break(fb_dir / "sc004corr_first_break_sc004.tsv")
    fb_sc036 = read_first_break(fb_dir / "sc004corr_first_break_sc036.tsv")
    require_terminal("SC014", fb_sc014)
    require_terminal("SC004", fb_sc004)
    require_terminal("SC036", fb_sc036, directions=("earlier",))
    rows.append(("sc014_later_boundary", boundary_str(fb_sc014["later"]),
                 "summaries/sc004corr_first_break_sc014.tsv"))
    rows.append(("sc014_earlier_boundary", boundary_str(fb_sc014["earlier"]),
                 "summaries/sc004corr_first_break_sc014.tsv"))
    rows.append(("sc004_later_boundary", boundary_str(fb_sc004["later"]),
                 "summaries/sc004corr_first_break_sc004.tsv"))
    rows.append(("sc004_earlier_boundary", boundary_str(fb_sc004["earlier"]),
                 "summaries/sc004corr_first_break_sc004.tsv"))
    rows.append(("sc036_earlier_boundary", boundary_str(fb_sc036["earlier"]),
                 "summaries/sc004corr_first_break_sc036.tsv"))

    # Application inventory counts (literal).
    rows.append(("sc004_corpus_applications", "24 (23 attested + roe)",
                 "sc004_component_application_report.tsv"))
    rows.append(("sc014_corpus_applications", "2 (span, meed)",
                 "sc004_component_application_report.tsv"))

    # Artifact hashes.
    artifacts = {
        "protoform_application_inventory": SC / "order_tests/sc004_component_application_report.tsv",
        "component_behaviors_probes": SC / "order_tests/sc004_component_behaviors.tsv",
        "interaction_classifications": SC / "order_tests/sc004_sc014_interaction_analysis.tsv",
        "first_break_sc014": SC / "order_tests/summaries/sc004corr_first_break_sc014.tsv",
        "first_break_sc004": SC / "order_tests/summaries/sc004corr_first_break_sc004.tsv",
        "first_break_sc036": SC / "order_tests/summaries/sc004corr_first_break_sc036.tsv",
        "cascade_order_manifest": SC / "cascade_baseline/cascade_order_manifest.tsv",
        "interaction_matrix": SC / "cascade_baseline/cascade_interaction_matrix.tsv",
        "full_trace": G / "docs/debug_snapshots/oe_full_trace_report.txt",
        "compact_trace": G / "docs/debug_snapshots/oe_derivation_class_trace_report.compact.md",
        "mismatch_report": G / "docs/debug_snapshots/oe_mismatch_report.txt",
        "index_verborum_emissions": G / "docs/book/index_verborum_book_emissions.tsv",
    }
    for key, path in artifacts.items():
        rows.append((key, sha256_file(path),
                     str(path.relative_to(REPO)) if path.exists() else f"{path} (MISSING)"))

    rows.append(("reader_headings_and_anchors", sha256_text(reader_headings_anchors()),
                 "sorted SC004/SC014 reader headings + anchors"))

    # The immutable frozen lexical-output checksum.
    rows.append(("lexical_outputs_sha256", FROZEN_OUTPUTS_SHA,
                 "immutable frozen lexical-output baseline (must not change)"))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    lines = ["artifact\tvalue_or_sha256\tsource"]
    lines += ["\t".join(r) for r in rows]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

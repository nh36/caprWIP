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
    rows.append(("sc014_later_boundary", "SC072 order 69 (span spanne->spannē, meed meorde->meordē)",
                 "summaries/sc004corr_first_break_sc014.tsv"))
    rows.append(("sc014_earlier_boundary", "none (cascade head, pos 1)",
                 "summaries/sc004corr_first_break_sc014.tsv"))
    rows.append(("sc004_later_boundary", "SC036 order 33 (soul sāwol->sāwel)",
                 "summaries/sc004corr_first_break_sc004.tsv"))
    rows.append(("sc004_earlier_boundary", "none toward head (boundary-limited)",
                 "summaries/sc004corr_first_break_sc004.tsv"))
    rows.append(("sc036_earlier_boundary", "SC004 order 28 (soul; supersedes SC019)",
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

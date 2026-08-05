#!/usr/bin/env python3
"""Freeze / verify the post-relabelling semantic baseline.

Records SHA-256 fingerprints of the canonical post-rename artifacts so future
changes are detectable. This is a *reporting* baseline: it does NOT replace the
frozen lexical-output baseline (cascade_baseline_summary.json /
cascade_order_manifest_frozen.tsv), which remains immutable. The lexical
outputs_sha256 must stay `aaf19ba9…480e`.

Artifacts fingerprinted:
  canonical_rule_identifiers  – sorted canonical Foma identifiers of migrated rules
  full_trace                  – oe_full_trace_report.txt
  compact_trace               – oe_derivation_class_trace_report.compact.md
  mismatch_report             – oe_mismatch_report.txt
  book_headings_and_anchors   – sorted rule headings+anchors from reader section 19
  index_verborum_emissions    – index_verborum_book_emissions.tsv

Usage:
  build_post_rename_semantic_baseline.py            # write the baseline TSV
  build_post_rename_semantic_baseline.py --check    # verify current == frozen
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
G = REPO / "Germanic"
OUT = G / "docs/sound_changes/cascade_baseline/post_rename_semantic_baseline.tsv"

FULL_TRACE = G / "docs/debug_snapshots/oe_full_trace_report.txt"
COMPACT_TRACE = G / "docs/debug_snapshots/oe_derivation_class_trace_report.compact.md"
MISMATCH = G / "docs/debug_snapshots/oe_mismatch_report.txt"
SECTION19 = G / "docs/sound_changes/reader_facing/reader_facing_local_section_19.md"
EMISSIONS = G / "docs/book/index_verborum_book_emissions.tsv"
MANIFEST = G / "docs/sound_changes/cascade_baseline/rename_migration_manifest.tsv"
BASELINE_SUMMARY = G / "docs/sound_changes/cascade_baseline/cascade_baseline_summary.json"

FROZEN_OUTPUTS_SHA256 = "aaf19ba919cafbe86ea59d482ce74d0944f541336e246da481a3f37b20da480e"

RULE_HEADING_RE = re.compile(r"^##\s+(SC\d{3})\.\s+(.*?)\s+\(`([^`]+)`\)\s+\{#(rule-[^}]+)\}\s*$")


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def canonical_identifiers() -> str:
    ids = []
    with MANIFEST.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["migration_status"] == "completed":
                ids.append(row["canonical_foma_identifier"])
    return "\n".join(sorted(ids)) + "\n"


def book_headings_and_anchors() -> str:
    lines = []
    for ln in SECTION19.read_text(encoding="utf-8").splitlines():
        m = RULE_HEADING_RE.match(ln.strip())
        if m:
            lines.append(f"{m.group(1)}\t{m.group(3)}\t{m.group(4)}")
    return "\n".join(sorted(lines)) + "\n"


def fingerprints() -> list[tuple[str, str, str]]:
    return [
        ("canonical_rule_identifiers", _sha(canonical_identifiers()),
         "sorted canonical Foma identifiers of the 18 migrated rules"),
        ("full_trace", _sha(FULL_TRACE.read_text(encoding="utf-8")),
         FULL_TRACE.relative_to(REPO).as_posix()),
        ("compact_trace", _sha(COMPACT_TRACE.read_text(encoding="utf-8")),
         COMPACT_TRACE.relative_to(REPO).as_posix()),
        ("mismatch_report", _sha(MISMATCH.read_text(encoding="utf-8")),
         MISMATCH.relative_to(REPO).as_posix()),
        ("book_headings_and_anchors", _sha(book_headings_and_anchors()),
         "sorted rule headings + anchors from " + SECTION19.relative_to(REPO).as_posix()),
        ("index_verborum_emissions", _sha(EMISSIONS.read_text(encoding="utf-8")),
         EMISSIONS.relative_to(REPO).as_posix()),
        ("lexical_outputs_sha256", FROZEN_OUTPUTS_SHA256,
         "immutable frozen lexical-output baseline (must not change)"),
    ]


def write_baseline() -> int:
    rows = fingerprints()
    with OUT.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["artifact", "sha256", "source"])
        w.writerows(rows)
    print(f"wrote {OUT} ({len(rows)} artifacts)")
    return 0


def check() -> int:
    if not OUT.exists():
        print("no frozen baseline to check", file=sys.stderr)
        return 1
    frozen = {r["artifact"]: r["sha256"]
              for r in csv.DictReader(OUT.open(encoding="utf-8"), delimiter="\t")}
    drift = []
    for artifact, sha, _ in fingerprints():
        if frozen.get(artifact) != sha:
            drift.append((artifact, frozen.get(artifact), sha))
    if frozen.get("lexical_outputs_sha256") != FROZEN_OUTPUTS_SHA256:
        drift.append(("lexical_outputs_sha256", frozen.get("lexical_outputs_sha256"), FROZEN_OUTPUTS_SHA256))
    if drift:
        print("POST-RENAME SEMANTIC BASELINE DRIFT:")
        for a, f, c in drift:
            print(f"  {a}: frozen={f} now={c}")
        return 1
    print("post-rename semantic baseline: all artifacts match frozen fingerprints")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="verify current == frozen instead of writing")
    args = ap.parse_args()
    return check() if args.check else write_baseline()


if __name__ == "__main__":
    raise SystemExit(main())

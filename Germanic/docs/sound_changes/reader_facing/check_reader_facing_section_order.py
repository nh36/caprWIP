#!/usr/bin/env python3
"""Require exact individual executable-order parity in sources and both books."""
from __future__ import annotations

import argparse
import csv
import io
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
SC_DIR = ROOT.parent
sys.path.insert(0, str(ROOT.parents[3] / "Germanic/tools"))
import generate_registry_views as registry
import oe_pipeline
from reader_facing_check_utils import mask_fenced_code

DEFAULT_MANIFEST = SC_DIR / "registry/reader_manifest.tsv"


def read_tsv_text(text: str) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO("\n".join(
        line for line in text.splitlines() if line and not line.startswith("#"))),
        delimiter="\t"))


def section_sequence(text: str) -> list[str]:
    headings = re.findall(r"^#{2,3}\s+(?:\\CAPRRuleHeading\{)?(SC\d{3})\.",
                          mask_fenced_code(text), re.M)
    return [sc for i, sc in enumerate(headings) if i == 0 or headings[i - 1] != sc]


def verify(manifest: Path) -> tuple[list[str], list[str], list[str]]:
    reg = registry.read_tsv(registry.SC_REGISTRY)
    expected_manifest = registry.build_reader_manifest(reg, registry.read_reader_sources())
    actual_rows = read_tsv_text(manifest.read_text(encoding="utf-8"))
    if actual_rows != read_tsv_text(expected_manifest):
        raise ValueError(f"{manifest}: stale or reordered individual reader manifest; "
                         "run python3 Germanic/tools/adjudicate.py --refresh")
    eligible = {r["fst_identifier"]: r["sc_id"] for r in reg
                if r["lifecycle_status"] == "active"
                and r["include_in_volume"] == r["is_reader_facing"] == "yes"}
    expected = [eligible[s.foma_identifier] for s in oe_pipeline.named_stages()
                if s.foma_identifier in eligible]
    files = [r["reader_file"] for r in actual_rows]
    source_sequence = [sc for name in files
                       for sc in section_sequence((ROOT / name).read_text(encoding="utf-8"))]
    observations = {
        "manifest": [r["sc_id"] for r in actual_rows],
        "reader sources": source_sequence,
        "assembled reader": section_sequence(
            (ROOT / "reader_facing_local_section_20.md").read_text(encoding="utf-8")),
        "combined manuscript": section_sequence(
            (ROOT.parents[2] / "docs/assembly/capr_book_draft_alpha_01.md").read_text(encoding="utf-8")),
    }
    for label, actual in observations.items():
        if actual != expected:
            raise ValueError(f"{label}: complete SC sequence differs from canonical "
                             f"oe_pipeline order:\nactual={actual}\nexpected={expected}\n"
                             "Refresh generated outputs; never manually reorder them.")
    return files, source_sequence, expected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    args = parser.parse_args()
    files, _, sequence = verify(args.manifest.resolve())
    print(f"Exact executable-order parity: {len(sequence)} identities, {len(files)} sources, "
          "manifest, reader and combined manuscript.")
    print("SC order: " + ", ".join(sequence))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

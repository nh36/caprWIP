#!/usr/bin/env python3
"""Mechanically sync chronology_card_index.tsv executable positions.

The ``cascade_position`` column (formerly ``current_order``) is a DERIVED
projection: the registry owns ``change_id -> fst_identifier`` and the
executable model (oe_pipeline, parsed from fsts/germanic.txt) owns
``fst_identifier -> cascade_position``.  This builder joins the two and
rewrites that one column only — it never reads a cached human-entered
position.  Every other column (earliest_safe_order, latest_safe_order,
*_boundary_order, ...) records the ARCHIVAL first-break experiment results
in the original chronology-test order space and is deliberately left
untouched.

Retired changes get the literal value ``retired``; active changes without a
cascade position get ``-``.

Usage:
    python3 Germanic/tools/sync_chronology_card_positions.py [--check]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import oe_pipeline  # noqa: E402
from generate_registry_views import SC_REGISTRY, read_tsv  # noqa: E402

CARD_INDEX = (SC_REGISTRY.parents[1] / "order_tests" / "chronology_cards"
              / "chronology_card_index.tsv")


def _derived_position(row: dict[str, str]) -> str:
    if row["lifecycle_status"] == "retired":
        return "retired"
    ident = row["fst_identifier"]
    if not ident:
        return "-"
    try:
        pos = oe_pipeline.cascade_position(ident)
    except KeyError:
        return "-"
    return "-" if pos is None else str(pos)


def synced_text() -> str:
    registry = {r["sc_id"]: r for r in read_tsv(SC_REGISTRY)}
    lines = CARD_INDEX.read_text(encoding="utf-8").splitlines()
    header = lines[0].split("\t")
    if header[0] != "change_id":
        raise SystemExit(f"unexpected card index header: {header[:3]}")
    if header[2] == "current_order":
        header[2] = "cascade_position"
    if header[2] != "cascade_position":
        raise SystemExit(f"unexpected position column: {header[2]!r}")
    out = ["\t".join(header)]
    for line in lines[1:]:
        if not line.strip():
            continue
        fields = line.split("\t")
        sc_id = fields[0]
        row = registry.get(sc_id)
        if row is None:
            raise SystemExit(f"card index change_id {sc_id} not in sc_registry.tsv")
        fields[2] = _derived_position(row)
        out.append("\t".join(fields))
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="verify the committed file is in sync; write nothing")
    args = parser.parse_args()
    text = synced_text()
    current = CARD_INDEX.read_text(encoding="utf-8")
    if args.check:
        if text != current:
            print(f"STALE: {CARD_INDEX} cascade_position column is out of sync "
                  "with sc_registry.tsv; run "
                  "python3 Germanic/tools/sync_chronology_card_positions.py",
                  file=sys.stderr)
            return 1
        print(f"in sync: {CARD_INDEX}")
        return 0
    if text != current:
        CARD_INDEX.write_text(text, encoding="utf-8")
        print(f"updated {CARD_INDEX}")
    else:
        print(f"already in sync: {CARD_INDEX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

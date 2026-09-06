#!/usr/bin/env python3
"""Mechanically sync sc_registry.tsv ``cascade_position`` from the executable model.

Authority architecture:

    sc_registry.tsv (SOURCE, hand-edited)   owns  sc_id -> fst_identifier
    oe_pipeline (executable model)          owns  fst_identifier -> cascade_position

``cascade_position`` is therefore DERIVED, retained in the registry only as a
physical compatibility column. Moving an FST rule in germanic.txt must never
require hand-typing the new position: run this tool (or
``adjudicate.py SCNNN --finalize``, which runs it) and the column is rewritten
from the model. ``--check`` fails when any derived value differs.

Rows that are not active, have no fst_identifier, or whose identifier lies
outside the SC cascade-position space (prelude/surface stages) get an empty
value.

Usage:
    python3 Germanic/tools/sync_registry_cascade_positions.py [--check]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import oe_pipeline  # noqa: E402
from generate_registry_views import SC_REGISTRY  # noqa: E402


def derived_position(lifecycle_status: str, fst_identifier: str) -> str:
    if lifecycle_status != "active" or not fst_identifier:
        return ""
    try:
        pos = oe_pipeline.cascade_position(fst_identifier)
    except KeyError:
        return ""
    return "" if pos is None else str(pos)


def synced_text() -> str:
    lines = SC_REGISTRY.read_text(encoding="utf-8").splitlines()
    header: list[str] | None = None
    col = status_col = ident_col = None
    out: list[str] = []
    for line in lines:
        if line.startswith("#") or not line.strip():
            out.append(line)
            continue
        fields = line.split("\t")
        if header is None:
            header = fields
            col = header.index("cascade_position")
            status_col = header.index("lifecycle_status")
            ident_col = header.index("fst_identifier")
            out.append(line)
            continue
        fields[col] = derived_position(fields[status_col], fields[ident_col])
        out.append("\t".join(fields))
    if header is None:
        raise SystemExit(f"no header row found in {SC_REGISTRY}")
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="verify the committed column is in sync; write nothing")
    args = parser.parse_args()
    text = synced_text()
    current = SC_REGISTRY.read_text(encoding="utf-8")
    if args.check:
        if text != current:
            print(f"STALE: {SC_REGISTRY} cascade_position column is out of sync "
                  "with the executable model (oe_pipeline); run "
                  "python3 Germanic/tools/sync_registry_cascade_positions.py",
                  file=sys.stderr)
            return 1
        print(f"in sync: {SC_REGISTRY}")
        return 0
    if text != current:
        SC_REGISTRY.write_text(text, encoding="utf-8")
        print(f"updated {SC_REGISTRY}")
    else:
        print(f"already in sync: {SC_REGISTRY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

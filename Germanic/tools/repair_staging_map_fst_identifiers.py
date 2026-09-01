#!/usr/bin/env python3
"""Synchronize executable columns of the historical staging map.

The staging map (``sound_change_historical_staging_map.tsv``) is the reader-facing
SC-level registry. Its ``fst_identifier`` column was populated with SC labels
(``SC004``, ``SC049`` …) rather than the actual Foma identifiers used in
``germanic.txt``. This tool replaces each ``fst_identifier`` value with the real
Foma identifier, taken from the authoritative per-rule anchor in
``sound_change_inventory.tsv`` (``rule_source_anchor`` = ``define <Ident> (line N)``).

The tool is idempotent: re-running it on an already-repaired map makes no change.
Run with ``--check`` to verify the committed map is up to date without writing.

Comments, header, row order, all other columns, and LF endings are preserved.
"""
from __future__ import annotations

import argparse
import csv
import io
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
STAGING_MAP = SC_DIR / "sound_change_historical_staging_map.tsv"
INVENTORY = SC_DIR / "sound_change_inventory.tsv"
MANIFEST = SC_DIR / "cascade_baseline" / "cascade_order_manifest.tsv"

_DEFINE_RE = re.compile(r"define\s+([A-Za-z][A-Za-z0-9_]*)")


def load_sc_to_foma(inventory_path: Path) -> dict[str, str]:
    """Return {change_id: foma_identifier} from the inventory rule anchors."""
    mapping: dict[str, str] = {}
    with inventory_path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            change_id = (row.get("change_id") or "").strip()
            anchor = row.get("rule_source_anchor") or ""
            match = _DEFINE_RE.search(anchor)
            if not change_id or not match:
                continue
            mapping[change_id] = match.group(1)
    return mapping


def load_foma_to_position(manifest_path: Path) -> dict[str, str]:
    with manifest_path.open(encoding="utf-8") as handle:
        return {
            row["foma_identifier"]: row["position"]
            for row in csv.DictReader(handle, delimiter="\t")
        }


def repair_lines(
    staging_text: str,
    sc_to_foma: dict[str, str],
    foma_to_position: dict[str, str] | None = None,
) -> tuple[list[str], int]:
    """Return repaired lines and the count of changed rows."""
    raw_lines = staging_text.splitlines()
    comment_lines = [ln for ln in raw_lines if ln.startswith("#")]
    data_lines = [ln for ln in raw_lines if not ln.startswith("#")]

    reader = csv.reader(io.StringIO("\n".join(data_lines)), delimiter="\t")
    records = list(reader)
    header = records[0]
    sc_idx = header.index("sc_id")
    fst_idx = header.index("fst_identifier")
    pos_idx = header.index("cascade_position")

    changed = 0
    out_rows = [header]
    for row in records[1:]:
        if not row:
            continue
        sc_id = row[sc_idx].strip()
        if sc_id not in sc_to_foma:
            raise ValueError(f"staging row {sc_id!r} has no inventory Foma identifier")
        foma = sc_to_foma[sc_id]
        if row[fst_idx] != foma:
            row[fst_idx] = foma
            changed += 1
        if foma_to_position is not None:
            if foma not in foma_to_position:
                raise ValueError(
                    f"staging row {sc_id!r} Foma identifier {foma!r} is absent "
                    "from the executable order manifest"
                )
            if row[pos_idx] != foma_to_position[foma]:
                row[pos_idx] = foma_to_position[foma]
                changed += 1
        out_rows.append(row)

    buffer = io.StringIO()
    writer = csv.writer(buffer, delimiter="\t", lineterminator="\n")
    writer.writerows(out_rows)
    repaired = comment_lines + buffer.getvalue().splitlines()
    return repaired, changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staging", type=Path, default=STAGING_MAP)
    parser.add_argument("--inventory", type=Path, default=INVENTORY)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--check", action="store_true",
                        help="Verify the map is already repaired; exit 1 if not")
    args = parser.parse_args()

    sc_to_foma = load_sc_to_foma(args.inventory)
    foma_to_position = load_foma_to_position(args.manifest)
    original = args.staging.read_text(encoding="utf-8")
    repaired_lines, changed = repair_lines(
        original, sc_to_foma, foma_to_position
    )
    repaired_text = "\n".join(repaired_lines) + "\n"

    if args.check:
        if repaired_text != original:
            print(f"staging map is STALE: {changed} fst_identifier value(s) need repair")
            return 1
        print("staging map fst_identifier column is up to date")
        return 0

    if repaired_text == original:
        print("staging map already repaired; no change")
        return 0
    args.staging.write_text(repaired_text, encoding="utf-8")
    print(f"repaired {changed} fst_identifier value(s) in {args.staging}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Record every selected checkpoint before/after the authorized SC015 adoption."""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, "/usr/app/tools")
import anglo_frisian_experiments as experiments
import oe_pipeline
from capr_runtime import check_build_manifest, layout

OLD_FST = "6c33b3c723150b61de4a41c89e228f32eeceb8280114b573e182eb8baf6ff51f"
OLD_CORPUS = "1fd8ec257581a54603b59835a46ca764ee2ba0f438c9b497b874a58ee2fe8f73"
TARGETS = {"2095": "leornian", "2313": "leorna", "2314": "leornaþ"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("before", "after"))
    parser.add_argument("output", type=Path)
    parser.add_argument("--before", type=Path)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("refusing to overwrite an adoption receipt")
    rt = layout()
    if not rt.is_container:
        parser.error("checkpoint capture requires the backend container")
    baseline_dir = rt.docs_dir / "sound_changes/cascade_baseline"
    with (baseline_dir / "cascade_baseline_outputs.tsv").open() as handle:
        records = list(csv.DictReader(handle, delimiter="\t"))
    if len(records) != 387 or len({r["row_id"] for r in records}) != 387:
        raise RuntimeError("selected population changed")
    manifest = json.loads(rt.build_manifest.read_text())
    if args.phase == "before":
        # Source edits have begun, but these are the freshly rebuilt incumbent
        # bins. Their manifest must still identify the preserved starting pair.
        if (manifest["sources"]["germanic.txt"] != OLD_FST
                or manifest["sources"]["germanic-aligned-final.tsv"] != OLD_CORPUS):
            raise RuntimeError("incumbent build no longer available")
    else:
        errors = check_build_manifest(
            ["old_english.bin", *oe_pipeline.expected_snapshot_bins()], rt)
        if errors:
            raise RuntimeError("; ".join(errors))
        if args.before is None:
            parser.error("--before is required for after capture")
    forms = [r["fst_input"] for r in records]
    checkpoints = {}
    for stage in oe_pipeline.stages():
        if stage.kind != "inline":
            checkpoints[stage.foma_identifier] = experiments.batch_apply_down(
                rt.bin_dir / stage.snapshot_bin, forms)
    outputs = experiments.batch_apply_down(rt.bin_dir / "old_english.bin", forms)
    if any(len(result) != 1 for result in outputs):
        raise RuntimeError("rejected or ambiguous selected input")
    rows = {
        row["row_id"]: {
            "record": row, "outputs": final,
            "checkpoints": {name: values[i] for name, values in checkpoints.items()},
        }
        for i, (row, final) in enumerate(zip(records, outputs))
    }
    protected = {
        str(path.relative_to(baseline_dir)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in baseline_dir.iterdir()
        if path.is_file() and (
            "_pre_" in path.name or "_legacy380" in path.name
            or path.name.startswith("approved_") and path.name != "approved_input_migrations.tsv"
        )
    }
    receipt = {"phase": args.phase, "build_manifest": manifest,
               "rows": rows, "protected_archives": protected}
    if args.phase == "before":
        if any(row["outputs"] != row["record"]["outputs"].split("|") for row in rows.values()):
            raise RuntimeError("incumbent bins differ from active baseline")
    else:
        previous = json.loads(gzip.decompress(args.before.read_bytes()))
        if previous["protected_archives"] != protected:
            raise RuntimeError("pre-existing archive or approval changed")
        final_deltas = {
            identifier: {"before": old["outputs"], "after": rows[identifier]["outputs"]}
            for identifier, old in previous["rows"].items()
            if old["outputs"] != rows[identifier]["outputs"]
        }
        if set(final_deltas) != set(TARGETS) or any(
                rows[identifier]["outputs"] != [target] for identifier, target in TARGETS.items()):
            raise RuntimeError(f"unexpected final deltas: {final_deltas}")
        intermediate_deltas = {
            identifier: {
                name: {"before": values, "after": rows[identifier]["checkpoints"][name]}
                for name, values in old["checkpoints"].items()
                if rows[identifier]["checkpoints"][name] != values
            }
            for identifier, old in previous["rows"].items()
        }
        intermediate_deltas = {k: v for k, v in intermediate_deltas.items() if v}
        if set(intermediate_deltas) != {*TARGETS, "2250"}:
            raise RuntimeError(f"unexpected intermediate identities: {list(intermediate_deltas)}")
        state1 = sum(r["record"]["counterpart"] in r["outputs"] for r in previous["rows"].values())
        state2 = sum(r["record"]["counterpart"] in r["outputs"] for r in rows.values())
        state3 = sum(TARGETS.get(i, r["record"]["counterpart"]) in r["outputs"]
                     for i, r in rows.items())
        if (state1, state2, state3) != (379, 376, 379):
            raise RuntimeError(f"unexpected three-state comparison: {state1,state2,state3}")
        receipt.update(final_deltas=final_deltas, intermediate_deltas=intermediate_deltas,
                       matched_three_states=[state1, state2, state3])
    args.output.write_bytes(gzip.compress(
        (json.dumps(receipt, ensure_ascii=False, indent=2) + "\n").encode(), mtime=0))
    print(f"{args.phase}: {len(rows)} selections, {len(checkpoints)} checkpoints")
    if args.phase == "after":
        print(json.dumps({k: receipt[k] for k in ("matched_three_states", "final_deltas")},
                         ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

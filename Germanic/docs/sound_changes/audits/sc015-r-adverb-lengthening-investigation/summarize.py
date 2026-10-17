#!/usr/bin/env python3
"""Summarize completed isolated receipts without running or interpreting Foma."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(path):
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as handle:
        return json.load(handle)


def first_common_difference(left, right):
    """Align named events, not numerical positions shifted by inserted rules."""
    by_event = {state["event"]: state for state in right}
    for state in left:
        other = by_event.get(state["event"])
        if other is not None and state["after"] != other["after"]:
            return {
                "event": state["event"], "left_index": state["index"],
                "right_index": other["index"],
                "left": state["after"], "right": other["after"],
            }
    return None


def compare(left, right):
    require(set(left["outputs"]) == set(right["outputs"]), "selected IDs differ")
    lp = {probe["id"]: probe for probe in left["probes"]}
    rp = {probe["id"]: probe for probe in right["probes"]}
    require(set(lp) == set(rp), "supplementary probe IDs differ")
    selected = []
    for identifier in left["outputs"]:
        difference = first_common_difference(
            left["traces"][identifier], right["traces"][identifier])
        a, b = left["outputs"][identifier], right["outputs"][identifier]
        if difference or a != b:
            selected.append({
                "id": identifier, "first_common_event_difference": difference,
                "left_output": a, "right_output": b, "final_differs": a != b,
            })
    probes = []
    for identifier, probe in lp.items():
        other = rp[identifier]
        require(probe["evaluation_input"] == other["evaluation_input"]
                and probe.get("entry_stage") == other.get("entry_stage")
                and probe.get("side", "before") == other.get("side", "before"),
                f"probe input/stage differs: {identifier}")
        difference = first_common_difference(probe["trace"], other["trace"])
        if difference or probe["outputs"] != other["outputs"]:
            probes.append({
                "id": identifier, "first_common_event_difference": difference,
                "left_output": probe["outputs"], "right_output": other["outputs"],
                "final_differs": probe["outputs"] != other["outputs"],
            })
    return {
        "left": left["recipe"]["id"], "right": right["recipe"]["id"],
        "selected_intermediate_or_final_differences": selected,
        "selected_final_difference_count": sum(item["final_differs"] for item in selected),
        "probe_intermediate_or_final_differences": probes,
        "probe_final_difference_count": sum(item["final_differs"] for item in probes),
        "left_only_events": [event for event in left["order"] if event not in right["order"]],
        "right_only_events": [event for event in right["order"] if event not in left["order"]],
    }


def summarize(receipts):
    require(bool(receipts), "at least one receipt required")
    base = None
    models = {}
    receipt_pins = []
    rows = None
    for path in receipts:
        report = load(path)
        require(report["status"] == "complete" and report["protected_unchanged"],
                f"incomplete or protection-failed receipt: {path}")
        baseline = report["baseline"]
        if base is None:
            base, rows = baseline, report["rows"]
        else:
            require(report["rows"] == rows and baseline["outputs"] == base["outputs"]
                    and baseline["traces"] == base["traces"]
                    and baseline["probes"] == base["probes"],
                    "batch identities or baseline traces differ")
        receipt_pins.append({
            "file": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "driver_sha256": report["driver_sha256"],
            "source_pins": report["specification"]["pins"],
            "witness_sha256": report["specification"]["witness_sha256"],
        })
        for model in report["models"]:
            name = model["recipe"]["id"]
            require(name not in models, f"duplicate model: {name}")
            models[name] = model
    targets = {row["id"]: row["counterpart"] for row in rows}
    summaries = []
    for name, model in models.items():
        differences = compare(base, model)
        summaries.append({
            "id": name, "architecture": model["recipe"]["architecture"],
            "representation": model["recipe"]["representation"],
            "selected_count": len(targets),
            "selected_matches": sum(output == [targets[key]]
                                    for key, output in model["outputs"].items()),
            "selected_final_deltas": model["deltas"],
            "selected_intermediate_differences": differences[
                "selected_intermediate_or_final_differences"],
            "rejected_ids": model["rejected_ids"],
            "ambiguous_ids": model["ambiguous_ids"],
            "rejected_probes": model["rejected_probes"],
            "ambiguous_probes": model["ambiguous_probes"],
            "probes": [{key: probe[key] for key in (
                "id", "evaluation_input", "kind", "evidence", "historical_stage",
                "reconstruction_level", "outputs", "firing_events")}
                for probe in model["probes"]],
            "experimental_and_lowering_census": [
                event for event in model["census"]
                if event["event"].startswith("XR") or event["event"] == "PNWGmcILowering"],
        })
    return {
        "schema_version": 1,
        "interpretation": (
            "Mechanical comparison only. First differences align common named events, "
            "not historical stages; event-only lists identify unaligned operations. "
            "A changed intermediate/final string is not by itself a chronology edge."
        ),
        "receipts": receipt_pins,
        "baseline": {
            "selected_count": len(targets),
            "selected_matches": sum(output == [targets[key]]
                                    for key, output in base["outputs"].items()),
            "mismatches": [{"id": key, "outputs": output, "target": targets[key]}
                           for key, output in base["outputs"].items()
                           if output != [targets[key]]],
            "lowering_census": [event for event in base["census"]
                                if event["event"] == "PNWGmcILowering"],
            "probes": [{key: probe[key] for key in ("id", "outputs")}
                       for probe in base["probes"]],
        },
        "models": summaries,
        "pairwise": [compare(left, right)
                     for left, right in itertools.combinations(models.values(), 2)],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipts", type=Path, nargs="+")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = summarize(args.receipts)
    require(not args.output.exists() and args.output.parent.is_dir(),
            "output must be a new file in an existing directory")
    with args.output.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(json.dumps({"models": len(result["models"]), "pairs": len(result["pairwise"]),
                      "output": str(args.output)}))


if __name__ == "__main__":
    main()

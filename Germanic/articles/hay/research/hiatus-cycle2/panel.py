#!/usr/bin/env python3
"""Extend the pinned historical panel and replay it on the common substrate."""

import argparse
from collections import Counter
import json
from pathlib import Path
import subprocess
import tempfile
import unicodedata

from reproduce_stress import DELETION, run, verify
from stress_repairs import FOOT_DEFINITION


HERE = Path(__file__).resolve().parent


class Foot:
    RULES = ("StFoot",)

    @staticmethod
    def definitions():
        return FOOT_DEFINITION


def inventory():
    inherited_file = run.HERE / "historical.tsv"
    inherited = run.dsv(inherited_file)
    extension = run.dsv(HERE / "panel.tsv")
    all_ids = {row["id"] for row in inherited + extension}
    verify(len(all_ids), len(inherited) + len(extension), "distinct panel identities")
    for row in extension:
        if (row["parent"] and row["parent"] not in all_ids
                or not row["source"] or not row["preceding_history_and_limits"]
                or (row["entry"] == "none") != (not row["input"])
                or (row["entry"] == "none" and row["grade"] == "synthetic")):
            raise RuntimeError(f"Incomplete evidence row: {row}")
    return inherited, extension


def batches_for(order, inherited, extension, archive):
    batches = {order[0]: {row["id"]: unicodedata.normalize("NFC", row["submit"])
                          for row in inherited if row["submit"]}}
    for row in extension:
        start, grade, form = row["entry"], row["grade"], row["input"]
        if start == "none" or (grade == "synthetic" and "*⊕" in form):
            continue  # Explicit boundary probes need a boundary-aware stack.
        if start == "archive":
            recorded = archive[f"active:{form}"]
            verify(recorded["concept"], row["family"], f"{row['id']} archived concept")
            form = recorded["fst_input"]
        start = order[0] if start in ("full", "archive") else start
        batches.setdefault(start, {})[row["id"]] = form
    return batches


def replay(order, paths, batches):
    traces = {}
    for start, batch in batches.items():
        suffix = order[order.index(start):]
        for key, trace in run.evaluate(suffix, paths, batch, set(suffix)).items():
            traces[key] = {"start": start, **trace}
    return traces


def count_status(ids, anchor, traces):
    return dict(Counter(
        "not submitted" if key not in traces else
        "admitted" if traces[key]["anchors"][anchor][1] else "rejected"
        for key in sorted(ids)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    prior = json.loads((run.HERE / "baseline.json").read_text(encoding="utf-8"))
    archive_path = run.HERE / "joint-corpus.json"
    archive = json.loads(archive_path.read_text(encoding="utf-8"))
    inherited, extension = inventory()
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    verify(orders, prior["orders"], "ordered components")
    verify(run.frozen.sha(source), prior["source_sha256"], "frozen source")
    paths = run.cached_stages(args.stage_cache, source, definitions, orders)
    models = {}
    with tempfile.TemporaryDirectory(prefix="hay-panel-") as directory:
        foot = run.compile_candidates(source, args.stage_cache, Path(directory), Foot)
        repaired = paths | {f"component:{DELETION}": foot["component:StFoot"]}
        for model, order in orders.items():
            batches = batches_for(order, inherited, extension, archive["models"][model]["baseline"])
            original = replay(order, paths, batches)
            traces = replay(order, repaired, batches)
            inherited_ids = {row["id"] for row in inherited}
            new_full = [row["id"] for row in extension if row["entry"] in ("full", "archive")]
            for key, historic in prior["models"][model]["traces"].items():
                verify({item: original[key][item] for item in ("input", "changes", "output")},
                       {item: historic[item] for item in ("input", "changes", "output")},
                       f"{model}/{key} frozen baseline")
            changes = {key: {"S0": original[key], "S1": trace} for key, trace in traces.items()
                       if trace != original[key]}
            verify(set(changes) - {"call-past-late", "call-pres", "call-ptc"}, set(),
                   f"{model} independent stress control invariance")
            models[model] = {
                "inherited_full_counts": count_status(inherited_ids, order[0], traces),
                "extension_full_counts": count_status(new_full, order[0], traces),
                "trace_count": len(traces), "s1_changes": changes, "traces": traces,
            }
    print(json.dumps({
        "base": run.BASE, "orders": orders,
        "source_sha256": run.frozen.sha(source),
        "historical_sha256": run.frozen.sha(run.HERE / "historical.tsv"),
        "supplement_sha256": run.frozen.sha(HERE / "panel.tsv"),
        "archive_sha256": run.frozen.sha(archive_path),
        "runner_sha256": run.frozen.sha(Path(__file__)),
        "foma": subprocess.check_output(["foma", "-v"], text=True).strip(),
        "historical": inherited, "supplement": extension, "models": models,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Replay a frozen unscored benchmark and inspect all wide-panel firings."""

import argparse
from collections import Counter
import json
from pathlib import Path
import subprocess
import tempfile

from matched import trial
from panel import inventory
from reproduce_stress import DELETION, run, verify
from stacks import Components, dahl_inputs, panel, plans


FREEZE = "1bcd080eae0ca82e08bd6d55e2e4c522bbe3eb6b"
FREEZE_SHA = "2731b6567b484929a955606de9f1c5a1a2fb2d8adb082cb96139595b4ec17980"
COMPARE = {"OEPalatalFricativeMerger", "OldEnglishOrthography", DELETION}


def corpus_run(order, paths, inputs, placements):
    execution = run.overlay_order(order, placements)
    return run.evaluate(execution, paths, inputs, COMPARE | {rule for _, rule in placements})


def audit_delta(report, control):
    affected = {}
    counts = Counter()
    for key, trace in report.items():
        initial = control[key]
        fired = {stage: [before, after] for stage, (before, after) in trace["anchors"].items()
                 if before != after and stage not in COMPARE}
        counts.update(fired.keys())
        if (trace["changes"] != initial["changes"]
                or trace["output"] != initial["output"]
                or any(trace["anchors"][stage] != initial["anchors"][stage] for stage in COMPARE)):
            affected[key] = {"firings": fired, **trace}
    return {
        "audited": len(report), "stage_firings": dict(counts),
        "surface_changes": [key for key, result in affected.items()
                            if result["output"] != control[key]["output"]],
        "internal_only_changes": [key for key, result in affected.items()
                                  if result["output"] == control[key]["output"]],
        "affected": affected,
    }


def benchmark_traces(order, paths, full_panel, spec, placements):
    selected = {}
    untraced = {}
    by_id = {key: (entry, form) for entry, batch in full_panel.items()
             for key, form in batch.items()}
    for row in spec:
        entry, ident, form = row["entry"], row["id"], row["input"]
        if row["provenance"] == "panel":
            if entry not in by_id:
                untraced[ident] = "not the same historical input in this arm"
                continue
            entry, form = by_id[entry]
        if row["provenance"] == "observation":
            untraced[ident] = "written variant only; no independent phonological input"
        else:
            selected.setdefault(entry, {})[ident] = form
    return {"traces": trial(order, paths, selected, placements), "untraced": untraced}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    base = json.loads((run.HERE / "baseline.json").read_text(encoding="utf-8"))
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    verify(orders, base["orders"], "ordered components")
    verify(run.frozen.sha(source), base["source_sha256"], "frozen source")
    archive_path = run.HERE / "joint-corpus.json"
    archive = json.loads(archive_path.read_text(encoding="utf-8"))
    benchmark_path = Path(__file__).with_name("benchmark.tsv")
    verify(run.frozen.sha(benchmark_path), FREEZE_SHA, "frozen benchmark")
    benchmark = run.dsv(benchmark_path)
    verify(len({row["id"] for row in benchmark}), len(benchmark), "benchmark identities")
    verify({row["grade"] for row in benchmark},
           {"established", "qualified", "disputed", "variant", "local", "synthetic"},
           "disjoint evidence grades")
    inherited, extension = inventory()
    frozen = run.cached_stages(args.stage_cache, source, definitions, orders)
    models = {}
    with tempfile.TemporaryDirectory(prefix="hay-audit-") as directory:
        paths = frozen | run.compile_candidates(source, args.stage_cache, Path(directory), Components)
        repaired = paths | {f"component:{DELETION}": paths["component:StFoot"]}
        _, _, dahl = dahl_inputs(paths)
        for model, order in orders.items():
            rows = archive["models"][model]["baseline"]
            verify(Counter(key.split(":")[0] for key in rows),
                   Counter({"archived": 394, "active": 396}), f"{model} panel coverage")
            inputs = {key: row["fst_input"] for key, row in rows.items()}
            control = corpus_run(order, frozen, inputs, ())
            verify({key: tr["output"] for key, tr in control.items()},
                   {key: row["output"] for key, row in rows.items()}, f"{model} frozen outputs")
            model_data = {"baseline": control, "arms": {}}
            for name, placements in plans(order).items():
                substrate = frozen if name == "T0" else repaired
                full_panel = panel(order, inherited, extension, rows, dahl, name == "TD")
                report = control if name == "T0" else corpus_run(order, substrate, inputs, placements)
                delta = audit_delta(report, control)
                model_data["arms"][name] = {
                    "placements": placements, "wide": delta,
                    "benchmark": benchmark_traces(order, substrate, full_panel, benchmark, placements),
                }
                if name in {"T0", "T1"}:
                    verify(delta["affected"], {}, f"{model}/{name} prior stress census")
            models[model] = model_data

    print(json.dumps({
        "base": run.BASE, "orders": orders, "source_sha256": run.frozen.sha(source),
        "archive_sha256": run.frozen.sha(archive_path), "benchmark_freeze": FREEZE,
        "benchmark_sha256": run.frozen.sha(benchmark_path), "benchmark": benchmark,
        "runner_sha256": run.frozen.sha(Path(__file__)), "definitions": Components.definitions(),
        "foma": subprocess.check_output(["foma", "-v"], text=True).strip(),
        "models": models,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

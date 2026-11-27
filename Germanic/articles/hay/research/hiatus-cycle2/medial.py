#!/usr/bin/env python3
"""Replay only T5 with independently limited intervocalic hw reduction."""

import argparse
import json
from pathlib import Path
import tempfile

from audit import audit_delta, benchmark_traces, corpus_run, FREEZE_SHA
from matched import trial
from panel import inventory
from reproduce_stress import DELETION, run, verify
from stacks import Components as Integrated, panel, plans


class Components:
    RULES = (*Integrated.RULES, "HwMed")

    @staticmethod
    def definitions():
        return (Integrated.definitions() +
                "define HwMed [{*w} -> 0 || EnglishStarVocalic {*x} _ EnglishStarVocalic];\n")


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
    inherited, extension = inventory()
    frozen = run.cached_stages(args.stage_cache, source, definitions, orders)
    models = {}
    with tempfile.TemporaryDirectory(prefix="hay-medial-") as directory:
        paths = frozen | run.compile_candidates(source, args.stage_cache, Path(directory), Components)
        paths[f"component:{DELETION}"] = paths["component:StFoot"]
        probes = {"initial": ["*x*w*a"], "medial": ["*e*x*w*a"], "nonprevocalic": ["*e*x*w*t"]}
        domains = {rule: run.frozen.apply_stage(paths[f"component:{rule}"], probes)
                   for rule in ("HwRed", "HwMed")}
        verify(domains["HwMed"], probes | {"medial": ["*e*x*a"]}, "intervocalic-only scope")
        for model, order in orders.items():
            rows = archive["models"][model]["baseline"]
            inputs = {key: row["fst_input"] for key, row in rows.items()}
            verify(len(inputs), 790, f"{model} panel coverage")
            control = corpus_run(order, frozen, inputs, ())
            verify({key: tr["output"] for key, tr in control.items()},
                   {key: row["output"] for key, row in rows.items()}, f"{model} frozen outputs")
            placements = tuple((anchor, "HwMed" if rule == "HwRed" else rule)
                               for anchor, rule in plans(order)["T5"])
            report = corpus_run(order, paths, inputs, placements)
            delta = audit_delta(report, control)
            verify(delta["surface_changes"], [], f"{model} keeps all frozen surface forms")
            full_panel = panel(order, inherited, extension, rows, {}, False)
            traces = trial(order, paths, full_panel, placements)
            verify(traces["source:see-inf"]["output"], ["sēon"], f"{model} medial see")
            models[model] = {
                "placements": placements, "wide": delta, "panel": traces,
                "benchmark": benchmark_traces(
                    order, paths, full_panel, run.dsv(benchmark_path), placements),
            }

    print(json.dumps({
        "base": run.BASE, "orders": orders, "source_sha256": run.frozen.sha(source),
        "archive_sha256": run.frozen.sha(archive_path), "benchmark_sha256": FREEZE_SHA,
        "runner_sha256": run.frozen.sha(Path(__file__)), "definitions": Components.definitions(),
        "controls": domains, "models": models,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

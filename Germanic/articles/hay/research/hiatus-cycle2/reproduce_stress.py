#!/usr/bin/env python3
"""Verify the frozen root-stress regression and its stage-local counterfactual."""

import argparse
import json
from pathlib import Path
import subprocess
import sys

sys.path.insert(0, str(Path(sys.argv[1]) / "Germanic/articles/hay/research/hiatus"))
import run

DELETION = "OEUnstressedEIContraction"
ANCHORS = {
    "EnglishProtoInput", "SC047ProtoInput", "OEStressFootContext", "EAFBrightening",
    "OEIUmlaut", "OEWLossBeforeI", DELETION, "OEHLoss",
}


def verify(actual, expected, label):
    if actual != expected:
        raise RuntimeError(f"{label}: expected {expected!r}, got {actual!r}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    previous = run.HERE / "baseline.json"
    baseline = json.loads(previous.read_text(encoding="utf-8"))
    verify(run.frozen.sha(source), baseline["source_sha256"], "frozen source")
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    verify(orders, baseline["orders"], "ordered components")
    paths = run.cached_stages(args.stage_cache, source, definitions, orders)
    inputs = {key: baseline["models"]["A"]["traces"][key]["input"]
              for key in ("call-pres", "call-ptc", "call-past")}
    models = {}
    for model, order in orders.items():
        traces = run.evaluate(order, paths, inputs, ANCHORS)
        reference = baseline["models"][model]["traces"]
        for key, trace in traces.items():
            for field in ("input", "changes", "output"):
                verify(trace[field], reference[key][field], f"{model}/{key}/{field}")
        suffix = order[order.index(DELETION) + 1:]
        bypass = run.evaluate(suffix, paths, {
            key: traces[key]["anchors"][DELETION][0][0]
            for key in ("call-pres", "call-ptc")
        }, ANCHORS)
        if model in ("A", "B2"):
            for key, tail, ending in (("call-pres", "*θ", "þ"), ("call-ptc", "*d", "d")):
                anchors = traces[key]["anchors"]
                verify(anchors["EAFBrightening"], [
                    [f"*ᶠ*g*æ*k*á*w*i{tail}"], [f"*ᶠ*g*æ*k*æ*w*i{tail}"],
                ], f"{model}/{key}/brightening")
                verify(anchors["OEIUmlaut"][1], [f"*ᶠ*ʝ*i*k*e*w*i{tail}"], f"{model}/{key}/umlaut")
                verify(anchors["OEWLossBeforeI"][1], [f"*ᶠ*ʝ*i*k*e*i{tail}"], f"{model}/{key}/w-loss")
                verify(anchors[DELETION][1], [f"*ᶠ*ʝ*e*k*i{tail}"], f"{model}/{key}/deletion")
                verify(anchors["OEHLoss"][1], [f"*ʝ*e*k*i{tail}"], f"{model}/{key}/foot cleanup")
                verify(bypass[key]["output"], [f"ġecei{ending}"], f"{model}/{key}/deletion bypass")
        else:
            for key in bypass:
                verify(bypass[key]["output"], traces[key]["output"], f"{model}/{key}/canonical bypass")
        models[model] = {"frozen": traces, "deletion_bypassed": bypass}

    probes = {
        "root-plain": ["*ᶠ*ʝ*e*k*e*i*d"],
        "root-marked": ["*ᶠ*ʝ*e*k*é*i*d"],
        "unprefixed": ["*k*e*i*d"],
        "posttonic-weak": ["*á*k*e*i*d"],
        "pretonic-weak": ["*ʝ*e*i*k*á*d"],
        "marked-prefix": ["*ʝ*é*k*e*i*d"],
    }
    results = run.frozen.apply_stage(paths[f"component:{DELETION}"], probes)
    verify(results, probes | {
        "root-plain": ["*ᶠ*ʝ*e*k*i*d"],
        "posttonic-weak": ["*á*k*i*d"],
        "marked-prefix": ["*ʝ*é*k*i*d"],
    }, "synthetic deletion contrasts")
    print(json.dumps({
        "base": run.BASE, "source_sha256": run.frozen.sha(source),
        "prior_receipt_sha256": run.frozen.sha(previous),
        "runner_sha256": run.frozen.sha(Path(__file__)),
        "foma": subprocess.check_output(["foma", "-v"], text=True).strip(),
        "orders": orders, "models": models, "synthetic": {"inputs": probes, "outputs": results},
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

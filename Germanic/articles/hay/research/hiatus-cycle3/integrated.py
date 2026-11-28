#!/usr/bin/env python3
"""Compare T5m-derived front-hiatus mechanisms on one pinned substrate."""

import argparse
import gzip
import json
from pathlib import Path
import subprocess
import sys
import tempfile


SNAPSHOT = Path(sys.argv[1])
CYCLE2 = SNAPSHOT / "Germanic/articles/hay/research/hiatus-cycle2"
sys.path.insert(0, str(CYCLE2))

from matched import apply, trial
from medial import Components
from panel import inventory
from reproduce_stress import DELETION, run, verify
from sources import AFTER_H
from stacks import panel, plans


FRONT = {
    DELETION: ("NuDN", "NuEd", "NuPv", "NaDN"),
    AFTER_H: ("NuDN", "NaDN"),
}
MECHANISMS = {"D": ("DcDN",), "J": ("GlDN", "GaDN"), "N": ("NuDN", "NaDN")}
EDGE = {"D": "Dc", "J": "Gl", "N": "Nu"}


def reference(order):
    return tuple((anchor, "HwMed" if rule == "HwRed" else rule)
                 for anchor, rule in plans(order)["T5"])


def common(order):
    return tuple((anchor, rule) for anchor, rule in reference(order)
                 if rule not in FRONT.get(anchor, ()))


def stack(order, mechanism, edge=False):
    steps = MECHANISMS.get(mechanism, ())
    additions = {DELETION: steps, AFTER_H: tuple(step + "PostH" for step in steps)}
    if edge:
        additions[DELETION] += (EDGE[mechanism] + "Ed",)
    placements = common(order)
    return tuple((anchor, rule) for anchor in order
                 for rule in additions.get(anchor, ()) +
                 tuple(rule for site, rule in placements if site == anchor))


def boundary(paths):
    probes = {row["id"]: row["form"] for row in run.dsv(run.HERE / "compound.tsv")}
    outcomes = {mechanism: {
        policy: apply(paths, (prefix + suffix,), probes)[prefix + suffix]
        for policy, suffix in (("absolute-only", "Ed"), ("member-enabled", "Me"))
    } for mechanism, prefix in EDGE.items()}
    for mechanism, policies in outcomes.items():
        verify(policies["absolute-only"]["short-member"], [probes["short-member"]],
               f"{mechanism} absolute edge must not reach first member")
        verify(policies["member-enabled"]["short-internal"], [probes["short-internal"]],
               f"{mechanism} ordinary medial adjacency outside member scope")
        if policies["member-enabled"]["short-member"] == [probes["short-member"]]:
            raise RuntimeError(f"{mechanism} marked first member did not resolve")
    return {"inputs": probes, "policies": outcomes}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    baseline = json.loads((run.HERE / "baseline.json").read_text(encoding="utf-8"))
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    verify(orders, baseline["orders"], "frozen orders")
    verify(run.frozen.sha(source), baseline["source_sha256"], "frozen source")
    archive_path = run.HERE / "joint-corpus.json"
    archive = json.loads(archive_path.read_text(encoding="utf-8"))
    reference_path = CYCLE2 / "medial-traces.json.gz"
    with gzip.open(reference_path, "rt", encoding="utf-8") as handle:
        accepted = json.load(handle)
    inherited, extension = inventory()
    frozen = run.cached_stages(args.stage_cache, source, definitions, orders)
    models = {}
    with tempfile.TemporaryDirectory(prefix="hay3-integrated-") as work:
        paths = frozen | run.compile_candidates(source, args.stage_cache, Path(work), Components)
        paths[f"component:{DELETION}"] = paths["component:StFoot"]
        for steps in MECHANISMS.values():
            for step in steps:
                paths[f"component:{step}PostH"] = paths[f"component:{step}"]
        isolated = boundary(paths)
        for model, order in orders.items():
            batches = panel(order, inherited, extension, archive["models"][model]["baseline"], {}, False)
            placements = {"T5m-reference": reference(order), "T5m-0": stack(order, "0")}
            for mechanism in MECHANISMS:
                placements[f"T5m-{mechanism}"] = stack(order, mechanism)
                placements[f"T5m-{mechanism}-edge"] = stack(order, mechanism, edge=True)
            models[model] = {}
            for name, sites in placements.items():
                traces = trial(order, paths, batches, sites)
                models[model][name] = {"placements": sites, "traces": traces}
                if name == "T5m-reference":
                    verify(traces, accepted["models"][model]["panel"], f"{model} accepted T5m")
                for key in ("source:claw", "source:knee-pl", "source:tree-pl",
                            "source:see-inf", "key-edge", "key-protected"):
                    verify(traces[key]["output"], accepted["models"][model]["panel"][key]["output"],
                           f"{model}/{name}/{key} shared control")

    print(json.dumps({
        "base": run.BASE, "orders": orders, "source_sha256": run.frozen.sha(source),
        "archive_sha256": run.frozen.sha(archive_path),
        "reference_sha256": run.frozen.sha(reference_path),
        "runner_sha256": run.frozen.sha(Path(__file__)),
        "foma": subprocess.check_output(["foma", "-v"], text=True).strip(),
        "definitions": Components.definitions(), "boundary": isolated, "models": models,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

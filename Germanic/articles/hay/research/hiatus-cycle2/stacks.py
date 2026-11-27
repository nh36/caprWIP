#!/usr/bin/env python3
"""Replay a small family of integrated phonological stacks."""

import argparse
import json
from pathlib import Path
import tempfile

from matched import apply, trial
from panel import batches_for, inventory
from reproduce_stress import DELETION, run, verify
from sources import AFTER_H, ARMS as SOURCES, Components as SourceComponents, FULL, LOCAL


TD_ENTRY = "OELatePalatalDiphthong"


class Components:
    dahl = run.continental.RULES | {
        "TdMid": "[{*ǣo} -> {*ē} || _ {*j}]",
        "TdHigh": "[{*ǣo} -> {*īe} || _ {*j}]",
        "TdWeak": "[{*a} -> {*æ} || {*j} _ {*s} .#.]",
    }
    RULES = (*SourceComponents.RULES, *dahl)

    @classmethod
    def definitions(cls):
        return SourceComponents.definitions() + "".join(f"define {name} {rule};\n"
                                                         for name, rule in cls.dahl.items())


def plans(order):
    early = order[order.index("OEWLossBeforeI") + 1]
    late = "OEJLossAfterHeavy"
    pre_h = DELETION
    return {
        "T0": (),
        "T1": (),
        "T2": ((early, "DcDN"),),
        "T2-late": ((late, "DcDN"),),
        "T3": ((early, "GlDN"), (early, "GlEd"), (early, "GlPv"), (late, "GaDN")),
        "T3N": ((early, "NuDN"), (early, "NuEd"), (early, "NuPv"), (late, "NaDN")),
        "T4": ((early, "GlEd"), (late, "HiPostLength"), (late, "AbsHigh")),
        "T5": (SOURCES["back-diphthong"] + SOURCES["cluster"] +
               ((pre_h, "NuDN"), (pre_h, "NuEd"), (pre_h, "NuPv"), (pre_h, "NaDN"),
                (AFTER_H, "NuDN"), (AFTER_H, "NaDN"),
                (AFTER_H, "HLBroken"), (AFTER_H, "HLBack"), (AFTER_H, "AbsHigh"))),
        "TD": (("OEPalatalFricativeMerger", "DaFinalJ"),),
    }


def dahl_inputs(paths):
    raw = {row["id"]: row["form"] for row in run.dsv(run.HERE / "continental.tsv")
           if row["id"] in {"hay-diph-direct", "hay-diph-protected", "district-diph"}}
    receipts = {}
    entries = {}
    for region, mutation in (("anglian", "TdMid"), ("west-saxon", "TdHigh")):
        receipts[region] = apply(paths, ("DaDiffer", "DaLowLoss", mutation, "TdWeak"), raw)
        for key, result in receipts[region]["TdWeak"].items():
            if len(result) != 1:
                raise RuntimeError(f"{region}/{key}: ambiguous Dahl stage entry")
            form = result[0]
            if form.startswith("*x"):
                form = "*ç" + form[2:]
            elif form.startswith("*g"):
                form = "*ʝ" + form[2:]
            entries[f"dahl:{region}:{key}"] = form
    return raw, receipts, entries


def panel(order, inherited, extension, archive, dahl, include_dahl):
    batches = batches_for(order, inherited, extension, archive)
    batches[order[0]].update({f"source:{key}": val for key, val in FULL.items()})
    for entry, forms in LOCAL.items():
        batches.setdefault(entry, {}).update({f"source:{key}": val for key, val in forms.items()})
    if include_dahl:
        batches.setdefault(TD_ENTRY, {}).update(dahl)
        for key in ("hay-dir", "hay-gen", "hay-dat", "district-direct", "district-protected"):
            del batches[order[0]][key]
    return batches


def boundary_trial(paths, name, placements):
    inputs = {row["id"]: row["form"] for row in run.dsv(run.HERE / "compound.tsv")}
    permitted = Components.RULES
    rules = [step for _, step in placements if step in permitted]
    edge = {"T3": "GlEd", "T3N": "NuEd", "T4": "GlEd", "T5": "NuEd",
            "TD": "DaFinalJ"}.get(name)
    member = {"GlEd": "GlMe", "NuEd": "NuMe", "DaFinalJ": "DaMemberLoss"}.get(edge)
    return {"absolute": apply(paths, rules, inputs),
            "member": apply(paths, [member if step == edge else step for step in rules], inputs)
            if member else {}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    base = json.loads((run.HERE / "baseline.json").read_text(encoding="utf-8"))
    verify(orders, base["orders"], "ordered components")
    verify(run.frozen.sha(source), base["source_sha256"], "frozen source")
    archive_path = run.HERE / "joint-corpus.json"
    archive = json.loads(archive_path.read_text(encoding="utf-8"))
    inherited, extension = inventory()
    frozen = run.cached_stages(args.stage_cache, source, definitions, orders)
    models = {}
    with tempfile.TemporaryDirectory(prefix="hay-stacks-") as directory:
        paths = frozen | run.compile_candidates(source, args.stage_cache, Path(directory), Components)
        repaired = paths | {f"component:{DELETION}": paths["component:StFoot"]}
        dahl_raw, dahl_trace, dahl = dahl_inputs(paths)
        for model, order in orders.items():
            models[model] = {}
            for name, sites in plans(order).items():
                batches = panel(order, inherited, extension, archive["models"][model]["baseline"],
                                dahl, name == "TD")
                traces = trial(order, paths if name == "T0" else repaired, batches, sites)
                models[model][name] = {
                    "placements": sites, "traces": traces,
                    "boundary": boundary_trial(repaired, name, sites),
                }
            verify(models[model]["TD"]["traces"]["key-edge"]["output"], ["cǣ"],
                   f"{model} preserves independent Dahl counterevidence")
            verify(models[model]["TD"]["traces"]["key-protected"]["output"], ["cǣġe"],
                   f"{model} protected key")
        for key, expected in {
            "source:see-inf": "sēon", "source:tree-pl": "trēo", "source:knee-pl": "cnēo",
            "source:claw": "clēa", "flock-late": "ēde", "couch-acc": "strēne",
        }.items():
            verify(models["A"]["T5"]["traces"][key]["output"], [expected], f"T5/{key}")

    print(json.dumps({
        "base": run.BASE, "orders": orders, "source_sha256": run.frozen.sha(source),
        "archive_sha256": run.frozen.sha(archive_path),
        "runners_sha256": {name: run.frozen.sha(Path(__file__).with_name(name))
                           for name in ("stacks.py", "sources.py", "matched.py", "panel.py",
                                        "quantity.py", "panel.tsv")},
        "definitions": Components.definitions(),
        "dahl_inputs": dahl_raw, "dahl_history": dahl_trace, "models": models,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Replay origin-controlled front hiatus and census changes from the frozen corpus."""

import argparse
from collections import Counter
import json
from pathlib import Path
import subprocess
import tempfile

from back_vowels import Components as Back, ENTRIES as BACK
from audit import audit_delta, corpus_run, FREEZE_SHA
from chronology import LOCAL as CHRONOLOGY, timing
from integrated import apply, common
from later_h import Components as Later, LOCAL as LATER
from matched import rule, trial
from panel import inventory
from reproduce_stress import DELETION, run, verify
from sources import AFTER_H, CLUSTER
from stacks import panel


HOLDOUT = "23c9621af57672fa1d5486eadad00322099194e3"
HOLDOUT_SHA = "426cfd361c51152e7462b49efe78c024433aa920b3177470fc2b091b2a5574ae"
DN = "[{*d}|{*θ}|{*ð}|{*n}]"
WIDE = {
    "D": ("RvD",), "J": ("RvJ", "RvGa"), "N": ("RvN", "RvNa"),
}
EDGE = {"D": ("DcEd",), "J": ("GlEd",), "N": ("RvNE", "RvPrint")}


def consume(plain, acute, scope):
    return (f"[{plain} -> {{*ē}} || _ {scope}] .o. "
            f"[{acute} -> {{*ḗ}} || _ {scope}]")


class Components:
    extra = {
        "RvD": rule(("e", "i"), ("ē",), DN),
        "RvJ": rule(("e", "i"), ("e", "j", "ʲ"), DN),
        "RvGa": consume("{*e} {*j} {*ʲ}", "{*é} {*j} {*ʲ}", DN),
        "RvN": ("[{*é} {*i} -> {*éi} || _ " + DN + "] .o. "
                "[{*e} {*i} -> {*ėi} || HiHeadContext _ " + DN + "]"),
        "RvNa": consume("{*ėi}", "{*éi}", DN),
        "RvNE": ("[{*é} {*i} -> {*éi} || _ .#.] .o. "
                 "[{*e} {*i} -> {*ėi} || HiHeadContext _ .#.]"),
        "RvPrint": "[{*ėi} -> {*ei}, {*éi} -> {*ei}]",
    }
    back_rules = {key: Back.definitions_by_name[key] for key in ("BkIu", "BkIo", "BkAe")}
    RULES = (*Later.RULES, *back_rules, *extra)

    @classmethod
    def definitions(cls):
        return Later.definitions() + "".join(
            f"define {key} {body};\n" for key, body in (cls.back_rules | cls.extra).items())


def plans(order):
    sites = timing(order)
    if sites["after-hvd"] == AFTER_H or order.index(sites["after-hvd"]) >= order.index(AFTER_H):
        raise RuntimeError("HVD and h-loss windows are not distinct")
    shared = common(order) + ((AFTER_H, "HbFront"), (AFTER_H, "HbIden"))
    key = lambda placement: order.index(placement[0])
    yield "common", tuple(sorted(shared, key=key))
    for mechanism, components in WIDE.items():
        post = tuple((AFTER_H, component + "H") for component in components)
        early = tuple((sites["after-hvd"], component) for component in components)
        for label, sequence in (
            ("late", post), ("two-window", early + post),
            ("late-edge", post + tuple((AFTER_H, step) for step in EDGE[mechanism])),
        ):
            yield f"{label}-{mechanism}", tuple(sorted(shared + sequence, key=key))
    realization = (("OEAuBrightening", "BkIu"), ("OEDiphthongLeveling", "BkIo"))
    yield "back-realization-probe", tuple(sorted(shared + realization, key=key))
    yield "back-bridge-probe", tuple(sorted(shared + (("OEEwLongDiphthong", "BkAe"),), key=key))


def batches(order, inherited, extension, rows, old_spec, spec):
    entries = panel(order, inherited, extension, rows, {}, False)
    by_id = {key: (start, value) for start, forms in entries.items() for key, value in forms.items()}
    untraced = {}
    for prefix, rows in (("benchmark", old_spec), ("holdout", spec)):
        for row in rows:
            key = prefix + ":" + row["id"]
            if row["provenance"] == "observation":
                untraced[key] = "written evidence only"
                continue
            if row["provenance"] == "panel" and row["entry"] not in by_id:
                untraced[key] = "no runnable stage input"
                continue
            site, value = (by_id[row["entry"]] if row["provenance"] == "panel"
                           else (row["entry"], row["input"]))
            entries.setdefault(site, {})[key] = value
    for prefix, controls in (("timeline", CHRONOLOGY), ("back", BACK), ("h", LATER)):
        for site, values in controls.items():
            site = order[0] if site == CLUSTER else site
            entries.setdefault(site, {}).update({f"{prefix}:{key}": val for key, val in values.items()})
    entries[order[0]].update({
        "initial:whale": "xwálaz", "initial:while": "xwīlō", "initial:whine": "xwīnaną",
        "initial:who": "xwáz", "initial:where": "xwār",
    })
    return entries, untraced


def guards(paths):
    inputs = {
        "plain": "*t*e*i*d", "acute": "*t*é*i*d", "old-atom": "*t*ei*d",
        "old-j": "*t*e*j*d", "secondary": "*t*e*ʝ*d", "weak": "*t*á*k*e*i*d",
    }
    traces = {label: apply(paths, steps, inputs) for label, steps in WIDE.items()}
    for key, rules in WIDE.items():
        verify(traces[key][rules[-1]], {name: [value] for name, value in
               (inputs | {"plain": "*t*ē*d", "acute": "*t*ḗ*d"}).items()}, key)
    verify(traces["J"]["RvJ"]["acute"], ["*t*é*j*ʲ*d"], "explicit consonantal intermediate")
    verify(traces["N"]["RvN"]["acute"], ["*t*éi*d"], "explicit accented nuclear intermediate")
    weak_inputs = inputs | {
        "prefixed-root": "*ᶠ*ʝ*e*k*e*i*θ", "prefixed-weak": "*ᶠ*ʝ*e*k*e*l*e*i*θ",
        "strew": "*s*t*r*e*i*d*e",
    }
    weak = {name: apply(paths, (name,), weak_inputs)[name]
            for name in (DELETION, "StFoot")}
    verify(weak["StFoot"], {key: [val] for key, val in
           (weak_inputs | {"weak": "*t*á*k*i*d",
                           "prefixed-weak": "*ᶠ*ʝ*e*k*e*l*i*θ"}).items()},
           "foot guard retains weak contraction without deleting or atomizing the stressed root")
    return {"inputs": inputs, "traces": traces, "weak_inputs": weak_inputs, "weak": weak}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    prior = args.snapshot / "Germanic/articles/hay/research/hiatus-cycle2/benchmark.tsv"
    spec_path = Path(__file__).with_name("holdouts-v1.tsv")
    verify(run.frozen.sha(prior), FREEZE_SHA, "prior benchmark unchanged")
    verify(run.frozen.sha(spec_path), HOLDOUT_SHA, "new holdouts frozen before execution")
    spec = run.dsv(spec_path)
    old_spec = run.dsv(prior)
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    archive_path = run.HERE / "joint-corpus.json"
    archive = json.loads(archive_path.read_text(encoding="utf-8"))
    base = json.loads((run.HERE / "baseline.json").read_text(encoding="utf-8"))
    verify(run.frozen.sha(source), base["source_sha256"], "frozen source")
    verify(orders, base["orders"], "frozen orders")
    inherited, extension = inventory()
    frozen = run.cached_stages(args.stage_cache, source, definitions, orders)
    models = {}
    with tempfile.TemporaryDirectory(prefix="hay3-revised-") as work:
        paths = frozen | run.compile_candidates(source, args.stage_cache, Path(work), Components)
        guards_receipt = guards(paths)
        paths[f"component:{DELETION}"] = paths["component:StFoot"]
        for steps in WIDE.values():
            for step in steps:
                paths[f"component:{step}H"] = paths[f"component:{step}"]
        for model, order in orders.items():
            rows = archive["models"][model]["baseline"]
            verify(Counter(key.split(":")[0] for key in rows),
                   Counter({"archived": 394, "active": 396}), f"{model} wide identity coverage")
            inputs = {key: row["fst_input"] for key, row in rows.items()}
            baseline = corpus_run(order, frozen, inputs, ())
            verify({key: record["output"] for key, record in baseline.items()},
                   {key: row["output"] for key, row in rows.items()}, f"{model} frozen outputs")
            panel_inputs, untraced = batches(order, inherited, extension, rows, old_spec, spec)
            models[model] = {"untraced_holdouts": untraced, "wide_frozen": baseline, "arms": {}}
            match = None
            for name, placements in plans(order):
                traces = trial(order, paths, panel_inputs, placements)
                wide = corpus_run(order, paths, inputs, placements)
                if match is None:
                    match = wide
                models[model]["arms"][name] = {
                    "placements": placements, "traces": traces,
                    "from_frozen": audit_delta(wide, baseline),
                    "from_common": audit_delta(wide, match),
                }
                for key, out in (("key-edge", "cǣġ"), ("key-protected", "cǣġe"),
                                 ("h:wealth-dative", "fēo"), ("source:see-inf", "sēon")):
                    verify(traces[key]["output"], [out], f"{model}/{name}/{key}")
                for key in panel_inputs[order[0]]:
                    if key.startswith("initial:"):
                        out = traces[key]["output"]
                        if not out or not all(text.startswith("hw") for text in out):
                            raise RuntimeError(f"{model}/{name} lost initial hw in {key}: {out}")
                if name.startswith(("late-", "two-window-")):
                    verify(traces["timeline:flock-short"]["output"], ["ēde"], f"{model}/{name} HVD")
                    verify(traces["h:strike-raised"]["output"], ["slēþ"], f"{model}/{name} late dental")
    print(json.dumps({
        "base": run.BASE, "orders": orders, "source_sha256": run.frozen.sha(source),
        "archive_sha256": run.frozen.sha(archive_path), "prior_holdout_sha256": FREEZE_SHA,
        "holdout_freeze": HOLDOUT, "holdout_sha256": HOLDOUT_SHA, "holdouts": spec,
        "runner_sha256": {name: run.frozen.sha(Path(__file__).with_name(name))
                          for name in ("revised.py", "integrated.py", "chronology.py",
                                       "later_h.py", "back_vowels.py")},
        "foma": subprocess.check_output(["foma", "-v"], text=True).strip(),
        "definitions": Components.definitions(), "guards": guards_receipt, "models": models,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

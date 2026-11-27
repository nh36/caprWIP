#!/usr/bin/env python3
"""Compare matched consonantal, nuclear and direct resolution with private Foma components."""

import argparse
import json
from pathlib import Path
import subprocess
import tempfile

from panel import batches_for, inventory, replay
from reproduce_stress import DELETION, run, verify
from stress_repairs import FOOT_DEFINITION


CLASSES = {
    "DS": "t d", "ST": "p b t d k g", "DO": "t d θ ð",
    "DN": "d θ ð n", "CO": "t d θ ð s z n l r", "CX": None,
}
MECHANISMS = ("direct", "glide", "nuclear")
STEPS = {"direct": ("Dc",), "glide": ("Gl", "Ga"), "nuclear": ("Nu", "Na")}
BOUNDARY = "{*⊕}"


def rule(src, dst, right):
    return run.joint.rewrite(src, dst, f" {right}" if right else "")


def atomic(right):
    return f"[{{*ei}} -> {{*ē}} || _ {right}] .o. [{{*éi}} -> {{*ḗ}} || _ {right}]"


def make_rules():
    rules = {}
    for label, phones in CLASSES.items():
        right = "OEAnyConsonant" if phones is None else (
            "[" + " | ".join(run.candidates.segment(x) for x in phones.split()) + "]")
        for prefix, before, after in (
            ("Dc", ("e", "i"), ("ē",)), ("Gl", ("e", "i"), ("e", "j")),
            ("Ga", ("e", "j"), ("ē",)), ("Nu", ("e", "i"), ("ei",)),
        ):
            rules[prefix + label] = rule(before, after, right)
        rules["Na" + label] = atomic(right)
    for label, right in {"Ed": ".#.", "Me": f"[.#. | {BOUNDARY}]",
                         "Pv": "EnglishStarVocalic"}.items():
        for prefix, output in (("Dc", ("ē",)), ("Gl", ("e", "j")), ("Nu", ("ei",))):
            rules[prefix + label] = rule(("e", "i"), output, right)
    dn = "[{*d}|{*θ}|{*ð}|{*n}]"
    rules.update({
        "FrDN": rule(("e", "ʝ"), ("ē",), dn),
        "ApNU": rule(("e", "j"), ("ei",), dn),
        "FrNU": rule(("e", "ʝ"), ("ei",), dn),
        "FrBr": rule(("e", "ʝ"), ("ei", "ʝ"), dn),
        "DaFinalJ": run.palatal.RULES["DaFinalJ"],
        "DaMemberLoss": run.compound.RULES["DaMemberLoss"],
    })
    return rules


class Components:
    definitions_by_name = make_rules()
    RULES = (*definitions_by_name, "StFoot")

    @classmethod
    def definitions(cls):
        return (run.candidates.PREFIX + FOOT_DEFINITION + "\n"
                + "".join(f"define {name} {body};\n"
                          for name, body in cls.definitions_by_name.items()))


def apply(paths, stages, inputs):
    states = {key: [form] for key, form in inputs.items()}
    receipt = {}
    for stage in stages:
        states = run.frozen.apply_stage(paths[f"component:{stage}"], states)
        receipt[stage] = states
    return receipt


def diagnostics(paths):
    phones = "t d θ ð n k p b g s z l r m w"
    probes = {phone: "*t*e*i*" + phone for phone in phones.split()}
    probes |= {"edge": "*t*e*i", "vowel": "*t*e*i*a", "long": "*t*ē*i*n",
               "weak": "*t*á*k*e*i*n", "prefixed": "*ᶠ*t*i*k*e*i*n",
               "inherited-j": "*t*e*j*n", "secondary-fricative": "*t*e*ʝ*n",
               "atomic": "*t*ei*n", "inherited-ai": "*t*ai*n",
               "breaking-retained": "*t*ei*ʝ*n"}
    compounds = {row["id"]: row["form"] for row in run.dsv(run.HERE / "compound.tsv")}
    medial = {}
    for label, domain in CLASSES.items():
        medial[label] = {}
        for mechanism, steps in STEPS.items():
            trial = apply(paths, [step + label for step in steps], probes)
            final = list(trial.values())[-1]
            actual = {phone for phone in phones.split()
                      if final[phone] != [probes[phone]]}
            expected = set(phones.split() if domain is None else domain.split()) & probes.keys()
            verify(actual, expected, f"{label}/{mechanism} matched control environment")
            for phone in expected:
                verify(final[phone], ["*t*ē*" + phone], f"{label}/{mechanism}/{phone}")
            medial[label][mechanism] = trial
    contexts = {}
    for label in ("Ed", "Me", "Pv"):
        contexts[label] = {}
        for step in ("Dc", "Gl", "Nu"):
            trial = apply(paths, [step + label], probes | compounds)
            contexts[label][step] = trial[step + label]
    verify(contexts["Ed"]["Gl"]["short-member"], [compounds["short-member"]], "word edge")
    verify(contexts["Me"]["Gl"]["short-member"], ["*ç*e*j*⊕*w*e*g"], "first member edge")
    verify(contexts["Me"]["Gl"]["short-internal"], [compounds["short-internal"]], "non-boundary")
    verify(contexts["Me"]["Gl"]["short-last"], [compounds["short-last"]], "weak last member")
    verify(contexts["Me"]["Gl"]["short-last-acute"], ["*s*ū*θ*⊕*ʝ*é*j"], "marked last member")
    origins = {
        "hiatus": ("NuDN", "NaDN"), "approximant": ("ApNU", "NaDN"),
        "fricative": ("FrNU", "NaDN"), "breaking": ("FrBr", "NaDN"),
        "direct-fricative": ("FrDN",),
        "merge-first": ("OEPalatalFricativeMerger", "GaDN"),
        "lose-first": ("GaDN", "OEPalatalFricativeMerger"),
    }
    return {
        "inputs": probes, "compound_inputs": compounds, "matched": medial, "edge": contexts,
        "origins": {label: apply(paths, stages, probes) for label, stages in origins.items()},
    }


def arms(order):
    early = order[order.index("OEWLossBeforeI") + 1]
    for label in CLASSES:
        for mechanism, steps in STEPS.items():
            yield f"{label}-{mechanism}", tuple((early, step + label) for step in steps)
    # Keep word-edge and prevocalic policies independent of medial scope.
    for context in ("Ed", "Pv"):
        for mechanism, steps in STEPS.items():
            for placement in (early, "OEContraction"):
                yield f"{context}-{mechanism}-{placement}", ((placement, steps[0] + context),)
    for label, steps in {
        "separated-glide": ((early, "GlDN"), ("OEJLossAfterHeavy", "GaDN")),
        "separated-nuclear": ((early, "NuDN"), ("OEJLossAfterHeavy", "NaDN")),
        "before-merger": ((early, "GlDN"), ("OEPalatalFricativeMerger", "GaDN")),
        "after-merger": ((early, "GlDN"), ("OECjCleanup", "GaDN")),
    }.items():
        yield label, steps


def trial(order, paths, batches, placements):
    traces = {}
    for start, batch in batches.items():
        suffix = order[order.index(start):]
        selected = tuple(pair for pair in placements if pair[0] in suffix)
        execution = run.overlay_order(suffix, selected)
        for key, trace in run.evaluate(execution, paths, batch, set(execution)).items():
            traces[key] = {"start": start, **trace}
    return traces


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
    frozen_paths = run.cached_stages(args.stage_cache, source, definitions, orders)
    models = {}
    with tempfile.TemporaryDirectory(prefix="hay-matched-") as directory:
        components = run.compile_candidates(source, args.stage_cache, Path(directory), Components)
        paths = frozen_paths | components | {f"component:{DELETION}": components["component:StFoot"]}
        isolated = diagnostics(paths)
        for model, order in orders.items():
            batches = batches_for(order, inherited, extension, archive["models"][model]["baseline"])
            h0 = replay(order, paths, batches)
            models[model] = {"H0": h0, "arms": {
                arm: {"placements": placements, "traces": trial(order, paths, batches, placements)}
                for arm, placements in arms(order)
            }}
    print(json.dumps({
        "base": run.BASE, "orders": orders, "source_sha256": run.frozen.sha(source),
        "sources": {name: run.frozen.sha(path) for name, path in {
            "panel": Path(__file__).with_name("panel.tsv"),
            "inventory": Path(__file__).with_name("panel.py"),
            "runner": Path(__file__), "archive": archive_path,
        }.items()},
        "foma": subprocess.check_output(["foma", "-v"], text=True).strip(),
        "definitions": Components.definitions(), "classes": CLASSES,
        "standalone": isolated, "models": models,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

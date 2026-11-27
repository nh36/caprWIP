#!/usr/bin/env python3
"""Replay reconstructed 'couch' cells without changing frozen admission."""

import argparse
import json
from pathlib import Path
import subprocess
import tempfile

from reproduce_stress import DELETION, run, verify
from stress_repairs import FOOT_DEFINITION


EARLY = "EAFBrighteningUnstressed"
PRE_HVD = "OEHighVowelApocope"
NUCLEAR = "JoHiOff"
MONO = "JoMerge"


class Components:
    RULES = (*run.joint.RULES, "StFoot", "CoRoot", "CoStem", "CoTail", "CoRaw", "CoNasal")

    @staticmethod
    def definitions():
        return run.joint.definitions() + FOOT_DEFINITION + """
define CoRoot PGCellRoot;
define CoStem PGCellRoot PGCellStem;
define CoTail PGCellEnd;
define CoRaw PGCellRaw;
define CoNasal [PGCellRoot PGCellStem* u:{*u}];
"""


def starred(form):
    return "".join(f"*{segment}" for segment in form)


CELLS = {
    # Pre-OE endings from Hogg–Fulk §2.39; not PGmc parser strings.
    "nom": (EARLY, starred("strawinu")),
    "acc": (EARLY, starred("strawina")),
    "gen": (EARLY, starred("strawinō")),
    "dat": (EARLY, starred(("s", "t", "r", "a", "w", "i", "n", "ai"))),
    "dat-pl": (EARLY, starred("strawinum")),
    # Conditional alternatives, not additional witness identifications.
    "long-i-acc": (EARLY, starred("strawīna")),
    "nn-acc": (EARLY, starred("strawinna")),
    "bede-w-acc": ("OELatePalatalDiphthong",
                   starred(("s", "t", "r", "eo", "w", "i", "n", "a"))),
    "bede-w-heavy": ("OELatePalatalDiphthong",
                     starred(("s", "t", "r", "ēo", "w", "i", "n", "ǣ"))),
}

FULL_CELLS = {
    # Conditional projections using Hogg–Fulk §2.38 and the frozen long-vowel
    # tail encoding; an accepted spelling is not evidence of PGmc inheritance.
    "nom-pg": "strawinō", "acc-pg": "strawinǭ", "gen-pg": "strawinōz",
    "dat-pg": "strawinai", "dat-pl-early": "strawinum",
}


def arms(frozen_model):
    early = run.candidates.placements("H1-early", frozen_model)[0][0]
    return {
        "H0": (),
        "direct-early": ((early, "HiContract"),),
        "direct-pre-HVD": ((PRE_HVD, "HiContract"),),
        "direct-post-HVD": (("OEMedialSyncope", "HiContract"),),
        "dental-stop": ((early, "HiDentalStop"),),
        "dental-obstruent": ((early, "HiDentalObstruent"),),
        "coronal": ((early, "HiCoronal"),),
        "glide-only": ((early, "HiGlide"),),
        "glide-loss": ((early, "HiGlide"), ("OEJLossAfterHeavy", "HiLoss")),
        "glide-loss-early": ((early, "HiGlide"), (early, "HiLoss")),
        "nuclear-mono": ((early, NUCLEAR), ("OEJLossAfterHeavy", MONO)),
        "nuclear-mono-early": ((early, NUCLEAR), (early, MONO)),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    baseline_path = run.HERE / "baseline.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    verify(run.frozen.sha(source), baseline["source_sha256"], "frozen source")
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    verify(orders, baseline["orders"], "ordered components")
    frozen_paths = run.cached_stages(args.stage_cache, source, definitions, orders)
    models = {}
    with tempfile.TemporaryDirectory(prefix="hay-couch-") as directory:
        paths = frozen_paths | run.compile_candidates(
            source, args.stage_cache, Path(directory), Components)
        probes = {form: [form] for form in (
            "strawinu", "stráwinu", "strawina", "stráwina", "strawinō", "strawinǭ",
            "strawinai", "strawinum", "strawinōz", "straw", "strawin", "u", "a")}
        admission = {name: run.frozen.apply_stage(paths[f"component:{name}"], probes)
                     for name in ("EnglishProtoInput", "SC047ProtoInput", "CoRoot", "CoStem",
                                  "CoTail", "CoRaw", "CoNasal")}
        for gate in ("EnglishProtoInput", "SC047ProtoInput", "CoRaw"):
            for form in ("strawinu", "stráwinu"):
                verify(admission[gate][form], [], f"{gate}/{form}")
        verify(admission["CoStem"]["strawin"], [starred("strawin")], "segmentable stem")
        verify(admission["CoTail"]["u"], [], "no bare final u branch")
        verify(admission["CoNasal"]["strawinu"], [starred("strawinu")], "tail distinction")

        for model, order in orders.items():
            native = run.evaluate(order, paths, {form: form for form in probes if
                                  form.startswith(("strawin", "stráwin"))}, set(order))
            for substrate in ("S0", "S1"):
                key = f"{model}/{substrate}"
                use_paths = paths if substrate == "S0" else paths | {
                    f"component:{DELETION}": paths["component:StFoot"]}
                trials = {}
                for arm, placements in arms(model).items():
                    if substrate == "S0" and arm != "H0":
                        continue
                    records = {}
                    for start in dict.fromkeys(start for start, _ in CELLS.values()):
                        suffix = order[order.index(start):]
                        selected = tuple(pair for pair in placements if pair[0] in suffix)
                        execution = run.overlay_order(suffix, selected)
                        batch = {cell: form for cell, (entry, form) in CELLS.items()
                                 if entry == start}
                        records.update(run.evaluate(execution, use_paths, batch, set(execution)))
                    trials[arm] = {"placements": placements, "traces": records,
                                   "full": run.evaluate(
                                       run.overlay_order(order, placements), use_paths, FULL_CELLS,
                                       set(order) | {component for _, component in placements})}
                models[key] = {"local": trials}
                if substrate == "S0":
                    models[key]["parser_to_surface"] = native

        for model in orders:
            s0 = models[f"{model}/S0"]["local"]["H0"]
            s1 = models[f"{model}/S1"]["local"]
            verify(s1["H0"], s0, f"{model} stress guard invariance for simplex cells")
            for arm, expected in {
                "H0": ("streinu", "streina"),
                "direct-early": ("strēn", "strēna"),
                "direct-post-HVD": ("strēnu", "strēna"),
                "dental-stop": ("streinu", "streina"),
                "dental-obstruent": ("streinu", "streina"),
                "glide-only": ("streġn", "streġna"),
                "glide-loss": ("strēn", "strēna"),
                "nuclear-mono": ("strēn", "strēna"),
            }.items():
                verify([s1[arm]["traces"][cell]["output"] for cell in ("nom", "acc")],
                       [[form] for form in expected], f"{model}/{arm}/local endpoints")
            target = "strīene" if model == "canonical" else "strēne"
            for arm in ("direct-early", "glide-loss", "nuclear-mono"):
                verify(s1[arm]["full"]["acc-pg"]["output"], [target],
                       f"{model}/{arm}/full accusative endpoint")

    print(json.dumps({
        "base": run.BASE, "source_sha256": run.frozen.sha(source),
        "baseline_sha256": run.frozen.sha(baseline_path),
        "runner_sha256": run.frozen.sha(Path(__file__)),
        "foma": subprocess.check_output(["foma", "-v"], text=True).strip(),
        "orders": orders, "local_cells": CELLS, "admission": admission, "models": models,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

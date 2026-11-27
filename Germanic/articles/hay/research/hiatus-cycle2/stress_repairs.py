#!/usr/bin/env python3
"""Compare a foot guard and a persistent head tier on frozen stress controls."""

import argparse
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import unicodedata
from unittest.mock import patch

sys.path.insert(0, str(Path(sys.argv[1]) / "Germanic/articles/hay/research/hiatus"))
import run

from reproduce_stress import ANCHORS, DELETION, verify

HEAD = "*⌃"
SECONDARY = "*⌄"
TAG = "[{*⌃}|{*⌄}]"
TAGS = re.compile(r"\*[⌃⌄]")
VOWELS = "aeiouyæœø"
PRIMARY = set("á é í ó ú ḯ ḗ ái áu éu íu".split())
GRAVE = set("à è ì ò ù ỳ ǽ".split())
ORTHOGRAPHY = "OldEnglishOrthography"
EARLY = "OEWLossBeforeI"
FOOT_DEFINITION = "define StFoot FootCtx(OEUnstressedEIContraction);"


def untag(form):
    return TAGS.sub("", form)


def annotate(form):
    def tag(match):
        symbol = match[1]
        prefix = HEAD if symbol in PRIMARY else SECONDARY if symbol in GRAVE else ""
        return prefix + match[0]
    return re.sub(r"\*([^*]+)", tag, form)


def valid(form, tags):
    if TAGS.findall(form) != tags:
        return False
    return all(
        re.match(r"\*(?![⌃⌄])", form[tag.end():])
        and len(form) > tag.end() + 1
        and unicodedata.normalize("NFD", form[tag.end() + 1])[0] in VOWELS
        for tag in TAGS.finditer(form)
    )


def compile_repairs(source, cache, directory, orders, frozen_definitions):
    stages = sorted({stage for order in orders.values()
                     for stage in order[1:order.index(ORTHOGRAPHY)]} - {DELETION})
    lifts = {stage: f"St{index:03d}" for index, stage in enumerate(stages)}
    definitions = [
        frozen_definitions,
        FOOT_DEFINITION,
        "define StGuard [{*e} -> 0 || EnglishStarVocalic "
        "[EnglishStarConsonant|EnglishPalatalConsonant]+ _ {*i}];",
        *(f"define {name} [{stage} / {TAG}];" for stage, name in lifts.items()),
    ]
    for ending, plain, accented in (("Con", ("ē",), ("ḗ",)), ("Gl", ("e", "j"), ("é", "j")),
                                    ("Nuc", ("ei",), ("ei",))):
        definitions.append(
            f"define StP{ending} "
            f"[{{*e}} {{*i}} -> {run.candidates.sequence(plain)} || {TAG} _] .o. "
            f"[{{*é}} {{*i}} -> {run.candidates.sequence(accented)} || {TAG} _];")
    definitions += [
        run.candidates.PREFIX,
        "define StFCon " + run.candidates.rewrite("ei", "ē") + ";",
        "define StFGl " + run.candidates.rewrite("ei", "ej") + ";",
        "define StFNuc [{*e} {*i} -> {*ei} || HiHeadContext _] "
        ".o. [{*é} {*i} -> {*ei}];",
        "define StPrint [{*ei} -> {*e} {*i}];",
    ]
    names = [*lifts.values(), "StFoot", "StGuard", "StFCon", "StFGl", "StFNuc",
             "StPCon", "StPGl", "StPNuc", "StPrint"]
    recipe = {"definitions": "\n".join(definitions), "replace": {}, "insert_rule": None,
              "insert_after": None, "component_checks": [{"component": name} for name in names]}
    image = cache / "defined.bin"
    with patch.dict(os.environ, {"CAPR_FOMA_DEFINITION_IMAGE": str(image)}):
        if not run.frozen.compiler.definition_image_source(
                source.read_text(encoding="utf-8"), directory).startswith("load defined "):
            raise RuntimeError("Repair compilation requires an exact frozen image")
        bins = run.frozen.compiler.compile_isolated(
            source, recipe, [], directory, components_only=True)
    return lifts, bins


def evaluate(order, paths, lifts, rows, arm, extra=None):
    marked = arm == "S2"
    records = {row["id"]: {"input": row["input"], "changes": [], "anchors": {}, "issues": []}
               for row in rows}
    for start in dict.fromkeys(row["entry"] for row in rows):
        index = 0 if start == "full" else order.index(start)
        states = {}
        for row in rows:
            if row["entry"] == start:
                form = row["input"]
                if marked and start != "full":
                    if row["id"] == "root-plain":
                        form = form.replace("*k*e", "*k*⌃*e")
                    form = form if TAGS.search(form) else annotate(form)
                states[row["id"]] = [form if marked else untag(form)]
        for stage in order[index:]:
            if stage == ORTHOGRAPHY:
                for key, forms in states.items():
                    records[key]["preorthographic"] = forms
                states = {key: sorted(set(map(untag, forms))) for key, forms in states.items()}
                if extra and extra[1].endswith("Nuc"):
                    states = run.frozen.apply_stage(paths["component:StPrint"], states)
            if extra and stage == extra[0]:
                states = lookup(paths, extra[1], states, records, marked)
            name = stage
            if stage == DELETION:
                name = {"S0": stage, "S1": "StFoot", "S2": "StGuard"}[arm]
            elif marked:
                name = lifts.get(stage, stage)
            if marked and stage in lifts:
                plain = {key: sorted(set(map(untag, forms))) for key, forms in states.items()}
                projected = run.frozen.apply_stage(paths[f"component:{stage}"], plain)
                changing = {key: forms for key, forms in states.items() if plain[key] != projected[key]}
                after = states | lookup(paths, name, changing, records, True, label=stage)
                for key in changing:
                    if sorted(set(map(untag, after[key]))) != projected[key]:
                        records[key]["issues"].append([stage, "projection-differs", projected[key]])
            else:
                after = lookup(paths, name, states, records, False, label=stage)
            if marked and stage == order[0]:
                after = {key: list(map(annotate, forms)) for key, forms in after.items()}
            for key, forms in after.items():
                if stage in ANCHORS:
                    records[key]["anchors"][stage] = [states[key], forms]
                if states[key] != forms:
                    records[key]["changes"].append([stage, forms])
            states = after
        for key, forms in states.items():
            records[key]["output"] = forms
    return records


def lookup(paths, stage, states, records, marked, label=None):
    after = run.frozen.apply_stage(paths[f"component:{stage}"], states)
    if marked:
        for key, forms in after.items():
            tags = TAGS.findall(states[key][0]) if states[key] else []
            accepted = [form for form in forms if valid(form, tags)]
            if len(accepted) != len(forms):
                records[key]["issues"].append([label or stage, "invalid-alignment",
                                               sorted(set(forms) - set(accepted))])
            if len({tuple(m.start() for m in TAGS.finditer(x)) for x in accepted}) > 1:
                records[key]["issues"].append([label or stage, "ambiguous-alignment", accepted])
            after[key] = accepted
    if label is None:
        for key, forms in after.items():
            if states[key] != forms:
                records[key]["changes"].append([stage, forms])
    return after


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    paths = run.cached_stages(args.stage_cache, source, definitions, orders)
    panel = Path(__file__).with_name("stress-panel.tsv")
    rows = run.dsv(panel)
    with tempfile.TemporaryDirectory(prefix="hay-stress-repairs-") as directory:
        lifts, bins = compile_repairs(source, args.stage_cache, Path(directory), orders, definitions)
        paths |= bins
        models = {}
        for model, order in orders.items():
            arms = {arm: evaluate(order, paths, lifts, rows, arm) for arm in ("S0", "S1", "S2")}
            for repair, letter, late in (("S1", "F", "OEHLoss"), ("S2", "P", "OEContraction")):
                for position, anchor in (("early", order[order.index(EARLY) + 1]), ("late", late)):
                    for kind in ("Con", "Gl", "Nuc"):
                        arms[f"{repair}-H-{kind}-{position}"] = evaluate(
                            order, paths, lifts, rows, repair, (anchor, f"St{letter}{kind}"))
            models[model] = arms
        for model in ("A", "B2"):
            for key, tail in (("call-present", "þ"), ("call-participle", "d")):
                for arm in ("S1", "S2"):
                    trace = models[model][arm][key]
                    verify(trace["output"], [f"ġecei{tail}"],
                           f"{model}/{arm}/{key}: {trace}")
                    for position in ("early", "late"):
                        verify(models[model][f"{arm}-H-Con-{position}"][key]["output"],
                               [f"ġecē{tail}"], f"{model}/{arm}/{position}/{key}")
        for model, arms in models.items():
            for key, expected in (("weak-posttonic", "*á*k*i*d"),
                                  ("weak-after-root", "*ᶠ*ʝ*e*k*é*t*i*d"),
                                  ("weak-prefix-stressed", "*ʝ*é*k*i*d"),
                                  ("weak-prefix", "*ʝ*e*i*k*á*d")):
                for arm in ("S0", "S1", "S2"):
                    weak = arms[arm][key]["anchors"][DELETION][1]
                    verify(list(map(untag, weak)), [expected], f"{model}/{arm}/{key}")
            for key in ("believe", "world", "call-simplex"):
                verify(arms["S1"][key]["output"], arms["S0"][key]["output"], f"{model}/S1/{key}")
        print(json.dumps({"base": run.BASE, "source_sha256": run.frozen.sha(source),
                          "runner_sha256": run.frozen.sha(Path(__file__)),
                          "panel_sha256": run.frozen.sha(panel), "models": models},
                         ensure_ascii=False))


if __name__ == "__main__":
    main()

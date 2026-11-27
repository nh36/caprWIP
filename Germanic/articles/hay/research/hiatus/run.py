#!/usr/bin/env python3
"""Batch trace research inputs against a private copy of the frozen cascade."""

import csv
import argparse
import gzip
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unicodedata
from unittest.mock import patch

import candidates
import compound
import palatal

BASE = "113101ac5f169b589e1a9647cdf24d32cdd4d919"
ROOT = Path(sys.argv[1]).resolve()
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "Germanic/tools"))

import sc047_models as frozen


def read_json(path):
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def evaluate(order, paths, inputs, anchors):
    states = {key: [form] for key, form in inputs.items()}
    records = {key: {"input": form, "changes": [], "anchors": {}}
               for key, form in inputs.items()}
    for stage in order:
        after = frozen.apply_stage(paths[f"component:{stage}"], states)
        for key, result in after.items():
            record = records[key]
            if states[key] != result:
                record["changes"].append([stage, result])
            if stage in anchors:
                record["anchors"][stage] = [states[key], result]
        states = after
    for key, result in states.items():
        records[key]["output"] = result
    return records


def compile_stages(source, definitions, orders, directory):
    compiler = frozen.compiler
    image = compiler.prepare_definition_image(source, directory)
    if image is None:
        raise RuntimeError("Missing common definition image")
    recipe = {"definitions": definitions, "replace": {}, "insert_rule": None,
              "insert_after": None, "component_checks": [
                  {"component": stage} for stage in sorted(set().union(*orders.values()))
              ]}
    with patch.dict(os.environ, {"CAPR_FOMA_DEFINITION_IMAGE": str(image)}):
        return compiler.compile_isolated(source, recipe, [], directory, components_only=True)


def dsv(path):
    with path.open(encoding="utf-8") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def local_diagnostics(orders, paths):
    rows = dsv(HERE / "local.tsv")
    results = {}
    for model, order in orders.items():
        traces = {}
        for start in dict.fromkeys(row["start"] for row in rows):
            batch = {row["id"]: row["form"] for row in rows if row["start"] == start}
            suffix = order[order.index(start):]
            traces.update(evaluate(suffix, paths, batch, set(suffix)))
        results[model] = traces
    return results


def cached_stages(directory, source, definitions, orders):
    names = sorted(set().union(*orders.values()))
    identity = {
        "source": frozen.sha(source),
        "definition": frozen.compiler._definition_identity(
            source.read_text(encoding="utf-8"), directory),
        "orders": orders,
        "definitions": definitions,
    }
    receipt = directory / "stages.json"
    if not receipt.exists():
        paths = compile_stages(source, definitions, orders, directory)
        receipt.write_text(json.dumps({"identity": identity, "hashes": {
            stage: frozen.sha(path) for stage, path in paths.items()}}), encoding="utf-8")
        return paths
    recorded = json.loads(receipt.read_text(encoding="utf-8"))
    paths = {f"component:{name}": directory / f"af_component_{index:02d}.bin"
             for index, name in enumerate(names)}
    if recorded != {"identity": identity, "hashes": {
        stage: frozen.sha(path) for stage, path in paths.items()
    }}:
        raise RuntimeError("Stage cache does not match frozen source, environment or bins")
    return paths


def compile_candidates(source, cache, directory, overlay=candidates):
    image = cache / "defined.bin"
    if not frozen.compiler.definition_image_source(
            source.read_text(encoding="utf-8"), directory, image).startswith("load defined "):
        raise RuntimeError("Candidate compilation requires the matching frozen definition image")
    recipe = {"definitions": overlay.definitions(), "replace": {}, "insert_rule": None,
              "insert_after": None, "component_checks": [
                  {"component": name} for name in overlay.RULES
              ]}
    with patch.dict(os.environ, {"CAPR_FOMA_DEFINITION_IMAGE": str(image)}):
        return frozen.compiler.compile_isolated(
            source, recipe, [], directory, components_only=True)


def overlay_order(order, placements):
    for anchor, component in placements:
        index = order.index(anchor)
        order = order[:index] + [component] + order[index:]
    return order


def synthetic_components(paths):
    probes = {row["id"]: row["form"] for row in dsv(HERE / "synthetic.tsv")}
    standalone = {name: frozen.apply_stage(
        paths[f"component:{name}"], {key: [form] for key, form in probes.items()})
        for name in candidates.RULES}
    dental_stops = {"d", "t", "plain", "prefix-root", "marked-root", "no-boundary"}
    dental = dental_stops | {"thorn", "eth"}
    coronal = dental | {"n", "s", "l", "r"}
    preconsonantal = coronal | {"k", "p", "m"}
    edge = {"edge", "compound", "weak-context"}
    eligible = preconsonantal | edge | {"vowel"}
    expected = {
        "HiContract": eligible, "HiGlide": eligible, "HiPreLength": eligible,
        "HiEdgeGlide": edge, "HiCGlide": preconsonantal,
        "HiAcute": eligible - {"compound", "weak-context", "plain", "prefix-root"},
        "HiStop": dental_stops | {"k", "p"}, "HiDentalStop": dental_stops,
        "HiDentalObstruent": dental, "HiCoronal": coronal,
        "HiConsonant": preconsonantal, "HiLoss": {"inherited-j"},
        "HiLongGlide": {"long-first"}, "HiPostLength": {"inherited-j", "existing-final-j"},
    }
    if standalone.keys() != expected.keys():
        raise RuntimeError("Synthetic expectations do not cover the defined components")
    for component, results in standalone.items():
        actual = {key for key, output in results.items() if output != [probes[key]]}
        if actual != expected[component] or any(len(output) != 1 for output in results.values()):
            raise RuntimeError(
                f"{component} synthetic domain violates the manifest: {sorted(actual ^ expected[component])}")
    for component, probe, outcome in [
        ("HiContract", "d", "*t*ḗ*d"),
        ("HiContract", "prefix-root", "*ᶠ*t*i*k*ē*d"),
        ("HiGlide", "vowel", "*t*é*j*a"),
        ("HiEdgeGlide", "edge", "*t*é*j"),
        ("HiLoss", "inherited-j", "*t*ḗ*d"),
        ("HiPreLength", "edge", "*t*ḗ*i"),
        ("HiLongGlide", "long-first", "*t*ḗ*j*d"),
        ("HiPostLength", "existing-final-j", "*t*ḗ*j"),
    ]:
        if standalone[component][probe] != [outcome]:
            raise RuntimeError(f"Incorrect immediate output: {component}/{probe}")
    return probes, standalone


def synthetic_trials(order, paths):
    probes, standalone = synthetic_components(paths)
    starts = {candidates.EARLY, *candidates.ORDERINGS.values()}
    controls = {start: evaluate(order[order.index(start):], paths, probes, set())
                for start in sorted(starts)}
    arms = {}
    for arm in candidates.ARMS:
        placements = candidates.placements(arm, "A")
        if not placements:
            continue
        start = placements[0][0]
        suffix = overlay_order(order[order.index(start):], placements)
        traces = evaluate(suffix, paths, probes, {component for _, component in placements})
        arms[arm] = {"start": start, "placements": placements, "traces": traces}
    return {"standalone": standalone, "controls": controls, "arms": arms}


def compare_arms(model, order, paths, batches, selected, extra=None):
    results = {}
    for arm in selected:
        placements = extra[arm] if extra and arm in extra else candidates.placements(arm, model)
        records = {}
        for start, inputs in batches.items():
            index = order.index(start)
            suffix_placements = tuple((anchor, component) for anchor, component in placements
                                      if order.index(anchor) >= index)
            suffix = overlay_order(order[index:], suffix_placements)
            records.update(evaluate(suffix, paths, inputs,
                                    {component for _, component in suffix_placements}))
        results[arm] = {"placements": placements, "traces": records}
    return results


def district_trials(orders, paths, inputs):
    rows = dsv(HERE / "district.tsv")
    extra = {"Dahl-final": (("OEJLossAfterHeavy", "DaFinalJ"),)}
    arms = ("H0", "H1-early", "H2-early", "H5-glide-first", "H6-final-only", *extra)
    results = {}
    for model, order in orders.items():
        batches = {}
        for row in rows:
            start = order[0] if row["start"] == "full" else row["start"]
            form = row["form"]
            batches.setdefault(start, {})[row["id"]] = (
                inputs[form[1:]] if form.startswith("@") else form
            )
        results[model] = compare_arms(model, order, paths, batches, arms, extra)
    return results


def historical_trials(orders, paths, inputs):
    local = {}
    for row in dsv(HERE / "local.tsv"):
        local.setdefault(row["start"], {})["local:" + row["id"]] = row["form"]
    return {model: compare_arms(model, order, paths, {order[0]: inputs, **local}, candidates.ARMS)
            for model, order in orders.items()}


def palatal_trials(orders, paths, inputs):
    rows = dsv(HERE / "palatal.tsv")
    results = {}
    for model, order in orders.items():
        arms = {}
        for arm, anchor in {"H0": None, **palatal.POSITIONS}.items():
            records = {}
            for entry in dict.fromkeys(row["start"] for row in rows):
                start = order[0] if entry == "full" else entry
                batch = {row["id"]: inputs[row["form"][1:]] if row["form"].startswith("@")
                         else row["form"] for row in rows if row["start"] == entry}
                suffix = order[order.index(start):]
                if anchor in suffix:
                    suffix = overlay_order(suffix, ((anchor, "DaFinalJ"),))
                records.update(evaluate(suffix, paths, batch, {
                    "DaFinalJ", "OEIUmlaut", "OEWLossBeforeI", "OEHighVowelApocope",
                    "OEJLossAfterHeavy", "OEJStrengtheningAfterFrontDiphthong",
                    "OEIntervocalicJVocalization",
                    "OEPalatalFricativeMerger", "OldEnglishOrthography",
                }))
            arms[arm] = records
        results[model] = arms
    return results


CORPUS_ARMS = (
    "H0", "H1-acute", "H1-early", "H1-late", "H2-early", "H2-late",
    "H3-stop-retain", "H3-dental_stop-retain", "H3-dental_obstruent-glide",
    "H3-coronal-glide", "H3-consonant-glide", "H4-pre-loss", "H4-post-loss",
    "H4-post-merger", "H5-length-first", "H5-glide-first", "H6-final-only",
    "H6-nonfinal-only",
)


def corpus_trials(orders, paths, archive, capture):
    results = {}
    for model, order in orders.items():
        archived = archive["corpus"] if model == "canonical" else capture["models"][model]["corpus"]
        active = capture["models"]["A" if model == "canonical" else model]["active_corpus"]
        rows = {f"{panel}:{row['row_id']}": row for panel, items in
                (("archived", archived), ("active", active)) for row in items}
        inputs = {key: row["fst_input"] for key, row in rows.items()}
        arms = compare_arms(model, order, paths, {order[0]: inputs}, CORPUS_ARMS)
        base = arms.pop("H0")["traces"]
        baseline = {}
        for key, row in rows.items():
            panel = key.split(":")[0]
            expected = (row["identity" if model == "canonical" else "diagnostic_outputs"]
                        if panel == "archived" else row["outputs"] if model != "canonical" else None)
            output = base[key]["output"]
            if expected is not None and output != expected:
                raise RuntimeError(f"Corpus H0 does not reproduce {model}/{key}")
            baseline[key] = {field: row[field] for field in
                             ("concept", "proto", "fst_input", "word_stress",
                              "phonological_finality", "counterpart")}
            baseline[key]["output"] = output
        comparison = {}
        for arm, details in arms.items():
            affected = {}
            for key, tr in details["traces"].items():
                firings = {stage: [before, after] for stage, (before, after)
                           in tr["anchors"].items() if before != after}
                if firings or tr["output"] != base[key]["output"]:
                    affected[key] = {
                        "firings": firings,
                        "baseline_changes": base[key]["changes"],
                        "changes": tr["changes"],
                        "output": tr["output"],
                    }
            comparison[arm] = {"placements": details["placements"], "affected": affected}
        results[model] = {"baseline": baseline, "arms": comparison}
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("mode", choices=("baseline", "local", "synthetic", "historical", "corpus",
                                        "palatal", "district", "compound"),
                        nargs="?", default="baseline")
    parser.add_argument("--stage-cache", type=Path)
    args = parser.parse_args()
    source = ROOT / "Germanic/fsts/germanic.txt"
    archive = read_json(frozen.FROZEN)
    capture_path = frozen.DOCS / "models/sc047/captures/sc047-adoption-v1.json.gz"
    capture = read_json(capture_path)
    if (frozen.sha(frozen.FROZEN) != frozen.FROZEN_SHA
            or frozen.sha(source) != archive["inputs_sha256"]["germanic.txt"]
            or frozen.sha(source) != capture["fst_sha256"]
            or frozen.sha(frozen.CELLS) != capture["cells_sha256"]):
        raise RuntimeError("Frozen sources do not match the capture")
    inventory = HERE / "historical.tsv"
    with inventory.open(encoding="utf-8") as stream:
        inputs = {r["id"]: unicodedata.normalize("NFC", r["submit"])
                  for r in csv.DictReader(stream, delimiter="\t") if r["submit"]}
    canonical, orders, definitions = frozen.model_sources(source)
    orders = {"canonical": canonical, **orders}
    if args.mode != "baseline":
        if args.stage_cache is None:
            parser.error("research trials require a private --stage-cache")
        paths = cached_stages(args.stage_cache, source, definitions, orders)
        data = {"base": BASE, "source_sha256": frozen.sha(source)}
        if args.mode == "local":
            data.update(local_sha256=frozen.sha(HERE / "local.tsv"),
                        models=local_diagnostics(orders, paths))
        else:
            with tempfile.TemporaryDirectory(prefix="hay-candidates-") as tmp:
                overlay = {"palatal": palatal, "compound": compound}.get(args.mode, candidates)
                bins = compile_candidates(source, args.stage_cache, Path(tmp), overlay)
                data.update(candidates_sha256=frozen.sha(HERE / f"{overlay.__name__}.py"),
                            foma=subprocess.check_output(["foma", "-v"], text=True).strip(),
                            component_sha256={key: frozen.sha(path) for key, path in bins.items()})
                if args.mode == "compound":
                    probes = {row["id"]: [row["form"]] for row in dsv(HERE / "compound.tsv")}
                    data.update(panel_sha256=frozen.sha(HERE / "compound.tsv"),
                                inputs=probes, outputs={
                                    name: frozen.apply_stage(bins[f"component:{name}"], probes)
                                    for name in overlay.RULES
                                })
                elif args.mode == "district":
                    with tempfile.TemporaryDirectory(prefix="hay-palatal-") as palatal_dir:
                        palatal_bins = compile_candidates(source, args.stage_cache,
                                                          Path(palatal_dir), palatal)
                        data.update(inventory_sha256=frozen.sha(inventory),
                                    panel_sha256=frozen.sha(HERE / "district.tsv"),
                                    palatal_sha256=frozen.sha(HERE / "palatal.py"),
                                    palatal_component_sha256={
                                        key: frozen.sha(path) for key, path in palatal_bins.items()
                                    },
                                    models=district_trials(orders, paths | bins | palatal_bins, inputs))
                elif args.mode == "synthetic":
                    data.update(synthetic_sha256=frozen.sha(HERE / "synthetic.tsv"),
                                **synthetic_trials(orders["A"], paths | bins))
                elif args.mode == "historical":
                    data.update(inventory_sha256=frozen.sha(inventory),
                                local_sha256=frozen.sha(HERE / "local.tsv"),
                                models=historical_trials(orders, paths | bins, inputs))
                elif args.mode == "corpus":
                    _, predictions = synthetic_components(paths | bins)
                    data.update(archived_sha256=frozen.sha(frozen.FROZEN),
                                active_capture_sha256=frozen.sha(capture_path),
                                synthetic_sha256=frozen.sha(HERE / "synthetic.tsv"),
                                synthetic_component_outputs=predictions,
                                models=corpus_trials(orders, paths | bins, archive, capture))
                else:
                    data.update(inventory_sha256=frozen.sha(inventory),
                                panel_sha256=frozen.sha(HERE / "palatal.tsv"),
                                placements=palatal.POSITIONS,
                                models=palatal_trials(orders, paths | bins, inputs))
        print(json.dumps(data, ensure_ascii=False))
        return
    anchors = {"OEWLossBeforeI", "SC047FinalIi", "OEHighVowelApocope",
               "OEMedUnstressedILowering1", "OEMedUnstressedILowering",
               "OEUnstressedEIContraction", "OEHLoss", "OEContraction",
               "OldEnglishOrthography", "OldEnglishSurface"}
    reference = {f'row:{r["row_id"]}': r for r in archive["corpus"]}
    corpus = {key: row["fst_input"] for key, row in reference.items()}
    results = {}
    with tempfile.TemporaryDirectory(prefix="hay-build-") as tmp:
        paths = compile_stages(source, definitions, orders, Path(tmp))
        for model, order in orders.items():
            expected = ({key: row["identity"] for key, row in reference.items()}
                        if model == "canonical" else
                        {f'row:{row["row_id"]}': row["diagnostic_outputs"]
                         for row in capture["models"][model]["corpus"]})
            selected = {key: corpus[key] for key in expected}
            actual = evaluate(order, paths, inputs | selected, anchors | {order[0]})
            if any(actual[key]["output"] != output for key, output in expected.items()):
                raise RuntimeError(f"{model} does not reproduce the frozen corpus")
            results[model] = {"reference_rows_reproduced": len(expected),
                              "traces": {key: actual[key] for key in inputs}}
    data = {"base": BASE, "source_sha256": frozen.sha(source),
            "inventory_sha256": frozen.sha(inventory),
            "foma": subprocess.check_output(["foma", "-v"], text=True).strip(),
            "orders": orders, "models": results}
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

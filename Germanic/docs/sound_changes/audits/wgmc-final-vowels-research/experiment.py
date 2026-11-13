"""Unadopted final-vowel research; all Foma execution is container-only."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import zipfile


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def prepare(root):
    sys.path.insert(0, str(root / "Germanic/tools"))
    import anglo_frisian_experiments as af
    import experiment_snapshot as snapshots
    from executable_facts import parse_defines

    work = root / ".capr-work/wgmc-final-vowels-research"
    research = Path(__file__).resolve().parent
    parent = snapshots.Snapshot(root / ".capr-work/experiments/sc042-baseline-20261111")
    parent.verify()
    original = parent.input_path("germanic_fst")
    production = root / "Germanic/fsts/germanic.txt"
    old, current = parse_defines(original.read_text()), parse_defines(production.read_text())
    differences = sorted(name for name in old if old[name].body != current[name].body)
    assert set(old) == set(current) and differences == ["EAFFinalZDeletion"], differences
    inherited_rows = root / ".capr-work/sc042-final-verification/rows.json"
    rows = [{**row, "id": row["row_id"]} for row in json.loads(inherited_rows.read_text())]
    rows_path = work / "research-rows.json"
    write_json(rows_path, rows)
    assert len(rows) == 394
    assert sum(row["baseline_outputs"] == [row["counterpart"]] for row in rows) == 386
    high = "[{*i}|{*í}|{*ì}|{*ī}]"
    stop = current["OEVelarPalatalizationStops"].body
    assert stop.count("{*g} -> {*ʤ} || _ EnglishStarFrontVowel,") == 1
    stop = stop.replace("{*g} -> {*ʤ} || _ EnglishStarFrontVowel,",
                        "{*g} -> {*ʤ} || _ " + high + ",")
    merger = current["PWGmcSurvivingBimoricOUnrounding"].body
    assert merger.count("{*ō} -> {*ā}") == 1
    merger = merger.replace("{*ō} -> {*ā}", "[{*ō}|{*ǭ}] -> {*ā}")
    repair = "define AF20 [" + current["EAFFinalZDeletion"].body + "];\n"
    noop = "define AF0 [?*];\n"
    sources = [{"key": "RingeTaylor2014", "pages": "58-60,192-193,203-209,299-300,314"},
               {"key": "HoggGrammar2011", "pages": "254-260,271-275"}]
    pure = {"id": "identity", "description": "Required schema identity; not replayed.",
            "definitions": "", "insert_after": "", "insert_rule": "", "replace": {},
            "sources": [], "assumptions": "Historical cached-image identity only.",
            "limitations": "Not the current-source identity; use current-identity."}
    identity = {**pure, "id": "current-identity",
                "description": "Exact current definitions using authenticated prior image.",
                "definitions": repair + noop, "insert_after": "NWGmcInStemNLoss",
                "insert_rule": "AF0", "replace": {"EAFFinalZDeletion": "AF20"},
                "sources": [{"key": "RingeTaylor2014", "pages": "44-45"}],
                "assumptions": "Only cached-source definition difference is the repaired SC020.",
                "limitations": "Neutral insertion; no production intervention."}
    models = []
    for name in ("model-b", "model-c"):
        eligibility = stop
        if name == "model-c":
            eligibility += (
                "\n.o. [{*k} -> {*ʧ} || " + high + " [{*n}|{*ŋ}] _,,"
                "\n{*g} -> {*ʤ} || " + high + " [{*n}|{*ŋ}] _]"
            )
        definitions = (
            repair + noop + "define AF42N [" + merger + "];\n"
            "define AFG [Ctx([OEGFricativePalatal .o. (" + eligibility + ")])];\n"
            "define AFH [FootCtx([[{*x}|{*ç}] -> 0 || "
            "EnglishStarVocalic _ EnglishStarVocalic])];\n"
        )
        models.append({
            "id": name, "description": "Early merger and independently sourced consonant comparison.",
            "definitions": definitions, "insert_after": "NWGmcInStemNLoss",
            "insert_rule": "AF42N",
            "replace": {"EAFFinalZDeletion": "AF20",
                        "PWGmcSurvivingBimoricOUnrounding": "AF0",
                        "OEVelarPalatalization": "AFG", "OEHLoss": "AFH"},
            "sources": sources,
            "assumptions": "Pre-experiment memorandum; C adds Hogg's nasal-mediated eligibility.",
            "limitations": "No production adoption; singleton intervocalic posttonic h only; "
                           "before-r unrounding and full alternative fronting chronology untested.",
        })
    packet = {"schema_version": 1, "recipes": [pure, identity, *models],
              "probes": [{"id": "unrounded", "stage": "$inserted", "side": "after"}]}
    recipes = work / "research-recipes.json"
    write_json(recipes, packet)
    af.load_recipes(recipes)
    controls = [
        ("oral", "AF42N", "*r*á*t*ō", "*r*á*t*ā"),
        ("nasal", "AF42N", "*r*á*t*ǭ", "*r*á*t*ā"),
        ("trimoric", "AF42N", "*r*á*t*ô", "*r*á*t*ô"),
        ("monosyllable", "AF42N", "*t*ō", "*t*ō"),
        ("consonant_protected", "AF42N", "*r*á*t*ō*n", "*r*á*t*ō*n"),
        ("nasal_short", "AF42N", "*r*á*t*ą", "*r*á*t*ą"),
        ("low_front_ng", "AFG", "*t*u*n*g*ǣ", "*t*u*n*g*ǣ"),
        ("original_high_ng", "AFG", "*l*a*n*g*ī", "*l*a*n*ʤ*ī"),
        ("singleton_g", "AFG", "*b*e*g*e", "*b*e*ʝ*e"),
        ("initial_g", "AFG", "*g*æ", "*ʝ*æ"),
        ("velar_h", "AFH", "*w*l*ō*x*u*m", "*w*l*ō*u*m"),
        ("palatal_h", "AFH", "*θ*ō*ç*æ", "*θ*ō*æ"),
        ("geminate_velar_h", "AFH", "*a*x*x*a", "*a*x*x*a"),
        ("geminate_palatal_h", "AFH", "*a*ç*ç*a", "*a*ç*ç*a"),
        ("initial_h", "AFH", "*x*a", "*x*a"),
        ("protected_h", "AFH", "*a*x*t*a", "*a*x*t*a"),
        ("pretonic_h", "AFH", "*ᶠ*b*i*x*í*n*d*a*n", "*ᶠ*b*i*x*í*n*d*a*n"),
    ]
    predictions = {
        "component_controls": [{"id": i, "stage": s, "input": f, "expected": e}
                               for i, s, f, e in controls],
        "nasal_mediated": {"input": "*x*r*i*n*g", "model-b": "*x*r*i*n*g",
                          "model-c": "*x*r*i*n*ʤ"},
        "raw_controls": ["rátōz", "rátǭ", "gébōz", "gébǭ", "gébôz", "námô",
                         "θánxōn", "táixōn"],
        "expected_model_finals": [["ræte"], ["ræte"], ["ġiefe"], ["ġiefe"],
                                 ["ġiefa"], ["nama"], ["þō"], ["tā"]],
        "expected_lexical": {"flask": "flæsċe", "nightmare": "mære",
                             "toe": "tā", "tongue": "tunge"},
        "weak_witnesses": [row["id"] for row in rows if row["proto_norm"].endswith("ōn")],
        "source_definition_differences": differences,
        "strict_certification": "Not requested or claimed for unadopted experiments.",
    }
    predictions_path = work / "research-predictions.json"
    write_json(predictions_path, predictions)
    identifier = "wgmc-final-vowels-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    snapshot = snapshots.create_snapshot(
        identifier, "Source-grounded unadopted final-vowel and consonant comparisons.",
        {"source": original, "current_source": production, "recipes": recipes,
         "rows": rows_path, "predictions": predictions_path, "driver": Path(__file__).resolve(),
         "research_memorandum": research / "research-memorandum.md",
         "held_out_witnesses": research / "held-out-witnesses.tsv"},
        variants={recipe["id"]: json.dumps(recipe, ensure_ascii=False, sort_keys=True)
                  for recipe in packet["recipes"]},
        probes=packet["probes"], expected_outcomes=predictions,
        negative_controls=[control[0] for control in controls[2:]],
    )
    write_json(work / "research-snapshot.json", {"snapshot": str(snapshot.root)})
    print(json.dumps({"snapshot": str(snapshot.root), "weak_witnesses": predictions["weak_witnesses"],
                      "source_differences": differences}, ensure_ascii=False))


def run_container(source, recipes, rows_path, predictions_path, output):
    if not Path("/usr/app/tools").is_dir():
        raise RuntimeError("Foma experiments must execute inside the backend container")
    sys.path.insert(0, "/usr/app/tools")
    import anglo_frisian_experiments as af
    from sound_change_order_sensitivity import batch_apply_down

    image = Path("/tmp/capr-sc042-counterfactuals-20261111/image/defined.bin")
    os.environ["CAPR_FOMA_DEFINITION_IMAGE"] = str(image)
    packet, rows = af.load_recipes(recipes), json.loads(rows_path.read_text())
    predictions = json.loads(predictions_path.read_text())
    runtime = af.layout()
    live = af.corpus_rows(runtime.corpus_tsv)
    assert [(r["id"], r["fst_input"], r["counterpart"]) for r in rows] == [
        (r["id"], af.oe_pipeline.evaluation_input(r), r["counterpart"]) for r in live
    ], "Frozen population no longer equals production selections"
    protected = [runtime.germanic_fst, runtime.corpus_tsv, runtime.build_manifest,
                 runtime.bin_dir / "old_english.bin"]
    protected += sorted((runtime.docs_dir / "sound_changes/cascade_baseline").glob("*"))
    protected += sorted((runtime.docs_dir / "sound_changes/registry").glob("*.tsv"))
    before = {str(p): af.digest(p) for p in protected if p.is_file()}
    result = {"source_sha256": af.digest(source), "recipes_sha256": af.digest(recipes),
              "rows_sha256": af.digest(rows_path), "predictions_sha256": af.digest(predictions_path),
              "definition_image": json.loads(image.with_suffix(".json").read_text()),
              "protected_before": before, "predictions": predictions, "variants": {}}
    population_forms = [r["fst_input"] for r in rows]
    raw = predictions["raw_controls"]
    forms = population_forms + raw
    for recipe in packet["recipes"]:
        if recipe["id"] == "identity":
            continue
        directory = output.parent / recipe["id"]
        directory.mkdir()
        assert af.definition_image_source(source.read_text(), directory).startswith("load defined ")
        order, _ = af.context_lifted_order(recipe, af.complete_variant_order(recipe))
        bins = af.compile_isolated(source, recipe, [], directory, diagnostic_stages=order)
        finals = batch_apply_down(bins["final"], forms)
        stages, states = [], [[f] for f in forms]
        component_results = []
        by_stage = {stage: bins["diagnostic:" + str(i)] for i, stage in enumerate(order)}
        if recipe["id"] != "current-identity":
            for check in predictions["component_controls"]:
                values = batch_apply_down(by_stage[check["stage"]], [check["input"]])[0]
                component_results.append({**check, "outputs": values,
                                          "passed": values == [check["expected"]]})
            expected = predictions["nasal_mediated"][recipe["id"]]
            values = batch_apply_down(by_stage["AFG"], [predictions["nasal_mediated"]["input"]])[0]
            component_results.append({"id": "nasal_mediated", "outputs": values,
                                      "expected": expected, "passed": values == [expected]})
        for index, stage in enumerate(order):
            flattened = [f for state in states for f in state]
            applied = iter(batch_apply_down(bins["diagnostic:" + str(index)], flattened))
            states = [sorted({value for _ in state for value in next(applied)}) for state in states]
            stages.append({"stage": stage, "outputs": states})
        assert states == finals, "Serial component derivations differ from complete composition"
        record = {
            "order": order, "components": component_results,
            "matches": sum(v == [r["counterpart"]] for r, v in zip(rows, finals)),
            "missing": [r["id"] for r, v in zip(rows, finals) if not v],
            "multiple": [r["id"] for r, v in zip(rows, finals) if len(v) > 1],
            "rows": [{**r, "outputs": v, "changed": v != r["baseline_outputs"],
                      "derivation": [{"stage": s["stage"], "outputs": s["outputs"][i]} for s in stages]}
                     for i, (r, v) in enumerate(zip(rows, finals))],
            "raw_controls": [{"input": f, "outputs": finals[len(rows) + i],
                              "derivation": [{"stage": s["stage"], "outputs": s["outputs"][len(rows) + i]}
                                             for s in stages]} for i, f in enumerate(raw)],
            "binary_sha256": {key: af.digest(path) for key, path in bins.items()},
        }
        record["changed"] = [r["id"] for r in record["rows"] if r["changed"]]
        if recipe["id"] == "current-identity":
            assert not record["changed"] and record["matches"] == 386
        else:
            start = order.index("AF42N")
            record["all_subsequent_merger_equal"] = all(
                stage["outputs"][len(rows)] == stage["outputs"][len(rows) + 1]
                and stage["outputs"][len(rows) + 2] == stage["outputs"][len(rows) + 3]
                for stage in stages[start:]
            )
            record["raw_predictions_passed"] = finals[len(rows):] == predictions["expected_model_finals"]
        result["variants"][recipe["id"]] = record
        write_json(output, result)
        print(recipe["id"], json.dumps({key: record[key] for key in
              ("matches", "changed", "missing", "multiple")}), flush=True)
    after = {str(p): af.digest(Path(p)) for p in before}
    result["protected_after"] = after
    result["canonical_artifacts_unchanged"] = before == after
    write_json(output, result)
    assert before == after, "Experiment altered a protected canonical artifact"


def execute(root):
    sys.path.insert(0, str(root / "Germanic/tools"))
    import adjudication_control as control
    import experiment_snapshot as snapshots

    work = root / ".capr-work/wgmc-final-vowels-research"
    snapshot = snapshots.Snapshot(Path(json.loads((work / "research-snapshot.json").read_text())["snapshot"]))
    snapshot.verify()
    with control.runtime_lock("Unadopted West Germanic final-vowel research"):
        container = snapshot.stage_in_container()
        arguments = [container + "/" + snapshot.input_path(key).name
                     for key in ("source", "recipes", "rows", "predictions")]
        output = container + "/observations.json"
        receipt = control.run_logged(
            ["docker", "compose", "exec", "-T", "backend", "python3", "-u",
             container + "/" + snapshot.input_path("driver").name,
             "run", *arguments, output],
            label="wgmc-final-vowels-unadopted", cwd=root, log_dir=work / "validation",
        )
        subprocess.run(["docker", "compose", "cp", "backend:" + output,
                        str(work / "research-observations.json")], check=True)
    snapshot.complete("passed" if receipt["ok"] else "failed",
                      "Authentic execution status; hypothesis predictions assessed separately.",
                      [receipt])
    write_json(work / "research-receipt.json", receipt)
    print(Path(receipt["stdout_log"]).read_text())
    print(Path(receipt["stderr_log"]).read_text())
    raise SystemExit(receipt["returncode"])


def bundle(root):
    work = root / ".capr-work/wgmc-final-vowels-research"
    target = Path(__file__).resolve().parent
    receipt = json.loads((work / "research-receipt.json").read_text())
    files = {name: work / name for name in
             ("research-observations.json", "research-predictions.json",
              "research-recipes.json", "research-rows.json", "research-receipt.json",
              "supplement-observations.json", "supplement-predictions.json", "supplement-receipt.json",
              "clay-observations.json", "clay-predictions.json", "clay-receipt.json")}
    for label in ("research", "supplement", "clay"):
        command = json.loads((work / (label + "-receipt.json")).read_text())
        for key in ("stdout_log", "stderr_log"):
            path = Path(command[key])
            files["validation/" + path.name] = path
    snapshot = Path(json.loads((work / "research-snapshot.json").read_text())["snapshot"])
    snapshot_roots = [snapshot, root / ".capr-work/experiments/wgmc-final-vowels-controls-20261113",
                      root / ".capr-work/experiments/wgmc-final-vowels-controls-20261113-clay"]
    for index, directory in enumerate(snapshot_roots):
        for path in sorted(directory.rglob("*")):
            if path.is_file():
                files[f"snapshots/{index}/" + str(path.relative_to(directory))] = path
    members = {name: {"sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
                      "size": p.stat().st_size} for name, p in files.items()}
    archive = target / "experiments.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as capsule:
        for name, path in files.items():
            capsule.write(path, name)
    write_json(target / "manifest.json", {
        "archive_sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
        "members": members, "base_commit": "7604cdb1b7e4432ef1f7b4bae1fa5b91aa134d9d",
        "status": "unadopted research", "receipt": receipt,
    })


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("prepare", "execute", "run", "bundle"))
    parser.add_argument("paths", nargs="*", type=Path)
    args = parser.parse_args()
    if args.command == "run":
        run_container(*args.paths)
    else:
        {"prepare": prepare, "execute": execute, "bundle": bundle}[args.command](Path.cwd())

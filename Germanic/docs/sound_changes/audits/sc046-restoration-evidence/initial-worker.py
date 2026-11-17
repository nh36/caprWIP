#!/usr/bin/env python3
"""Pinned finite-input SC046 comparisons; no shared-bin writes or rebuilds."""
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import tempfile
import threading
import time
from unittest.mock import patch
import uuid


ROOT = (Path("/usr/app") if Path("/usr/app/tools").is_dir()
        else Path(__file__).resolve().parents[5])
TOOLS = ROOT / "Germanic/tools"
sys.path.insert(0, "/usr/app/tools" if Path("/usr/app/tools").is_dir() else str(TOOLS))

SELECTED = ["1934", "1938", "1981", "1985", "2016", "2141", "2148",
            "2240", "2266", "2336", "2090"]
HELPERS = ["anglo_frisian_experiments.py", "oe_pipeline.py", "capr_runtime.py",
           "sound_change_order_sensitivity.py", "executable_facts.py"]
LOCAL = {
    "crabba-schema": "*k*r*æ*b*b*ô",
    "racca-schema": "*r*æ*k*k*ô",
    "secondary-schema": "*g*e*b*ǽ*k*ō",
}


def variants(text):
    from executable_facts import parse_defines
    body = parse_defines(text)["OEARestoration"].body
    assert body.count("|| _") == body.count("{*æ} -> {*a}") == 1
    primary = body.replace("|| _", "|| .#. OEAnyConsonant* _")
    secondary = body.replace("{*æ} -> {*a}", "{*ǽ} -> {*à}")
    return {
        "stress": f"define AF46S [{primary}] .o. [{secondary}];",
        "no_geminate": (
            "define AF46C [EnglishStarConsonant | {*s} EnglishStarConsonant"
            " | {*f} EnglishStarConsonant];\n"
            "define AF46G " + body.replace("OEARestorationIntervening", "AF46C") + ";"),
    }


def worker(snapshot):
    import anglo_frisian_experiments as compiler
    from capr_runtime import check_build_manifest, layout
    import oe_pipeline
    from sound_change_order_sensitivity import batch_apply_down

    begun = time.perf_counter()
    runtime = layout()
    source = snapshot / "source.txt"
    plan = json.loads((snapshot / "plan.json").read_text())
    assert source.read_bytes() == runtime.germanic_fst.read_bytes()
    assert (snapshot / "corpus.tsv").read_bytes() == runtime.corpus_tsv.read_bytes()
    for name, digest in plan["helpers"].items():
        assert hashlib.sha256((runtime.tools_dir / name).read_bytes()).hexdigest() == digest
    problems = check_build_manifest(oe_pipeline.expected_snapshot_bins() + ["old_english.bin"])
    if problems:
        raise ValueError(problems)
    all_rows = oe_pipeline.load_rows(runtime.corpus_tsv)
    selected = {row["row_id"]: row for row in all_rows}
    absent = set(plan["selected"]) - selected.keys()
    if absent:
        raise ValueError(f"unknown selected rows: {sorted(absent)}")
    rows = all_rows if plan["full_corpus"] else [selected[key] for key in plan["selected"]]
    raw = [row["fst_input"] for row in rows]
    stages = oe_pipeline.stages()
    names = [stage.foma_identifier for stage in stages]
    at = names.index("OEARestoration")
    assert names[at:at + 3] == [
        "OEARestoration", "OEHeavySyllableNasalApocope", "OESecondaryNasalization"]
    after = names[at + 1:]
    syncope = after.index("OENonHighSyn")
    checkpoints = ["PWGmcFinalBareALoss", "EAFBrighteningUnstressed",
                   "EAFBrightening", "OEVelarFricativePalatalization",
                   "OEARestoration", "OESecondaryNasalization", "OENonHighSyn"]
    live = {name: batch_apply_down(
        runtime.bin_dir / oe_pipeline.stage_for(name).snapshot_bin, raw)
        for name in checkpoints}
    endpoints = batch_apply_down(runtime.bin_dir / "old_english.bin", raw)
    incoming = live["OEVelarFricativePalatalization"]
    if any(len(value) != 1 for value in incoming):
        raise ValueError("the independently staged comparison needs one incoming state per row")
    forms = [value[0] for value in incoming]
    local_inputs = list(dict.fromkeys(forms + list(LOCAL.values())))
    position = {row["row_id"]: index for index, row in enumerate(rows)}
    compounds = [forms[position[key]] for key in ("2148", "2336")]
    order_inputs = [forms[position[key]] for key in ("1934", "2266")]
    queries = {}
    for label, relation in (("current", "OEARestoration"),
                            ("stress", "AF46S"), ("no_geminate", "AF46G")):
        queries[label + ":local"] = ([relation], local_inputs)
    queries["46_then_48:local"] = (names[at:at + 3], order_inputs)
    reverse = ["OESecondaryNasalization", "OEHeavySyllableNasalApocope", "OEARestoration"]
    queries["48_then_46:local"] = (reverse, order_inputs)
    queries["48_then_46:final"] = (reverse + names[at + 3:], order_inputs)
    queries["stress:syncope"] = (["AF46S"] + after[:syncope + 1], compounds)
    queries["stress:final"] = (["AF46S"] + after, compounds)
    if plan["full_corpus"]:
        for label, relation in (("stress", "AF46S"), ("no_geminate", "AF46G")):
            queries[label + ":corpus"] = ([relation] + after, forms)
    definitions = list(plan["variants"].values())
    labels = {}
    for index, (label, (members, inputs)) in enumerate(queries.items()):
        name = "AF46Q" + str(index)
        definitions.append("define " + name + " [" + compiler.foma_domain(inputs)
                           + " .o. " + " .o. ".join(members) + "];")
        labels[label] = name
    recipe = {"definitions": "\n".join(definitions), "replace": {},
              "insert_rule": None, "insert_after": None,
              "component_checks": [{"component": name} for name in labels.values()]}
    memory = []

    def measured_compile(script, directory):
        with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
            started = time.perf_counter()
            process = subprocess.Popen(
                ["foma", "-q", "-f", script.name], cwd=directory,
                stdout=stdout, stderr=stderr)
            deadline = threading.Timer(600, process.kill)
            deadline.start()
            try:
                _, status, usage = os.wait4(process.pid, 0)
            finally:
                deadline.cancel()
            process.returncode = os.waitstatus_to_exitcode(status)
            memory.append({"seconds": time.perf_counter() - started,
                           "peak_rss_kib": usage.ru_maxrss,
                           "returncode": process.returncode})
            stdout.seek(0)
            stderr.seek(0)
            log = stdout.read().decode() + "\n" + stderr.read().decode()
            if process.returncode or re.search(r"(?im)\b(error|syntax error|not defined)\b", log):
                raise RuntimeError("SC046 isolated compilation failed:\n" + log[-6000:])

    with tempfile.TemporaryDirectory(prefix="capr_sc046_") as temporary:
        directory = Path(temporary)
        with patch.object(compiler, "_compile_foma", measured_compile):
            compiled = compiler.compile_isolated(
                source, recipe, [], directory, components_only=True,
                use_definition_image=bool(os.environ.get("CAPR_FOMA_DEFINITION_IMAGE")))
        sent = (directory / "experiment.foma").read_text()
        outputs = {
            label: batch_apply_down(compiled["component:" + name], queries[label][1])
            for label, name in labels.items()}
    records = [
        {"row_id": row["row_id"], "concept": row["concept"], "input": row["proto_norm"],
         "fst_input": row["fst_input"], "target": row["counterpart"],
         "before": forms[index], "baseline": endpoints[index],
         "live": {stage: values[index] for stage, values in live.items()}}
        for index, row in enumerate(rows)]
    corpus = {}
    for label in ("stress", "no_geminate"):
        if label + ":corpus" not in outputs:
            continue
        comparison = []
        for row, values in zip(records, outputs[label + ":corpus"]):
            comparison.append({
                **row, "outputs": values,
                "changed": set(values) != set(row["baseline"]),
                "rejected": not values, "ambiguous": len(values) > 1})
        corpus[label] = {
            "rows": comparison, "changed": sum(row["changed"] for row in comparison),
            "rejected": sum(row["rejected"] for row in comparison),
            "ambiguous": sum(row["ambiguous"] for row in comparison),
            "matches": sum(row["target"] in row["outputs"] for row in comparison)}
    return {
        "rows": records, "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "entry": {"stage": "OEARestoration", "side": "before"},
        "local_schemas": LOCAL, "corpus": corpus,
        "queries": {label: {"members": members, "inputs": inputs, "outputs": outputs[label]}
                    for label, (members, inputs) in queries.items()},
        "compiler_appendix": recipe["definitions"],
        "cost": {"variants": 3, "networks": len(queries), "compiler_calls": len(memory),
                 "foma_processes": memory, "image_loaded": sent.startswith("load defined "),
                 "definition_preparation_calls": 0, "seconds": time.perf_counter() - begun},
    }


def capture(prefix, root=ROOT, *, full_corpus=False, journal=None):
    from adjudication_control import run_logged
    from capr_runtime import container_command
    from experiment_snapshot import create_snapshot

    source = root / "Germanic/fsts/germanic.txt"
    out = root / ".capr-work/sc046"
    out.mkdir(parents=True, exist_ok=True)
    plan = {
        "full_corpus": full_corpus, "selected": SELECTED,
        "variants": variants(source.read_text()),
        "helpers": {name: hashlib.sha256((root / "Germanic/tools" / name).read_bytes()).hexdigest()
                    for name in HELPERS},
        "predictions": {
            "oral_nasal": "bake retracts; bast does not",
            "SC041": "day and craft lost the trigger and remain front",
            "local_order": "46 before 48 retains a; reversed retains ae; SC047 remains in its slot",
            "geminates": "no-geminate retains taepp- but contradicts crabba/racca root positives",
            "stress": "unstressed compound linkers remain front; follow syncope and final, do not infer",
            "secondary": "explicit secondary-stressed ae is eligible; unstressed linker is not",
        },
    }
    plan_path = out / "plan.json"
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2))
    snapshot = create_snapshot(
        "sc046-restoration-" + uuid.uuid4().hex[:8],
        "Separate target stress, trigger quality, geminates and model-local 46/48 ordering",
        {"source": source, "corpus": root / "Germanic/data/germanic-aligned-final.tsv",
         "worker": Path(__file__), "plan": plan_path,
         "assessment": root / "Germanic/docs/sound_changes/literature_dossiers/sc046-a-restoration/04-source-assessment.md",
         **{Path(name).stem: root / "Germanic/tools" / name for name in HELPERS}},
        variants=plan["variants"], probes=SELECTED + list(LOCAL.values()),
        expected_outcomes=plan["predictions"],
        negative_controls=["bast", "day", "craft", "mære", "unstressed compound linker"])
    container = snapshot.stage_in_container()
    if journal is not None:
        journal.complete_stage("SNAPSHOT", evidence={"snapshot_root": str(snapshot.root)})
    receipt = run_logged(
        container_command("cd /usr/app && " + prefix + "python3 "
                          + shlex.quote(container + "/worker.py") + " --worker "
                          + shlex.quote(container)),
        label="sc046-full" if full_corpus else "sc046-focused",
        log_dir=snapshot.staging_dir)
    snapshot.complete("passed" if receipt["ok"] else "failed",
                      "Manifest-validated cumulative entries and finite-domain comparisons",
                      [receipt])
    if not receipt["ok"]:
        raise RuntimeError((snapshot.results_dir / Path(receipt["stderr_log"]).name).read_text())
    result = json.loads((snapshot.results_dir / Path(receipt["stdout_log"]).name).read_text())
    (out / ("full-latest.json" if full_corpus else "focused-latest.json")).write_text(
        json.dumps({"snapshot_root": str(snapshot.root), "result": result},
                   ensure_ascii=False, indent=2))
    return result


if __name__ == "__main__":
    if sys.argv[1:2] == ["--worker"]:
        print(json.dumps(worker(Path(sys.argv[2])), ensure_ascii=False))
    elif sys.argv[1:] == ["--capture-full"]:
        from adjudication_run import load
        journal = load("SC046")
        result = capture("", full_corpus=True,
                         journal=journal if journal.frontier() == "SNAPSHOT" else None)
        print(json.dumps({"cost": result["cost"],
                          "corpus": {name: {key: value for key, value in data.items() if key != "rows"}
                                     for name, data in result["corpus"].items()}}, indent=2))
    else:
        raise SystemExit("use --capture-full on the host; pytest supplies the shared session image")

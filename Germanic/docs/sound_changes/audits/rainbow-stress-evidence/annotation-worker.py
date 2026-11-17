#!/usr/bin/env python3
"""Opt-in, finite-input SC046/SC059 comparisons against one pinned source."""
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import tempfile
import time
from unittest.mock import patch
import uuid


ROOT = (Path("/usr/app") if Path("/usr/app/tools").is_dir()
        else Path(__file__).resolve().parents[5])
sys.path.insert(0, "/usr/app/tools" if Path("/usr/app/tools").is_dir()
                else str(ROOT / "Germanic/tools"))
HELPERS = ["anglo_frisian_experiments.py", "oe_pipeline.py", "capr_runtime.py",
           "sound_change_order_sensitivity.py", "executable_facts.py"]
SELECTED = ["1934", "2266", "1963", "2068", "2174", "2148", "2302", "2336"]
SCHEMAS = ["régna-bàkô", "régna-bakô"]
LOCAL = ["*æ*l*u", "*s*t*æ*ð*u*l", "*g*e*b*ǽ*b*u",
         "*g*e*b*æ*b*u", "*g*e*b*è*b*u", "*g*e*b*e*b*u"]


def variants(text):
    from executable_facts import parse_defines
    body = parse_defines(text)["OEARestoration"].body
    assert body.count("|| _") == body.count("{*æ} -> {*a}") == 1
    primary = body.replace("|| _", "|| .#. OEAnyConsonant* _")
    secondary = body.replace("{*æ} -> {*a}", "{*ǽ} -> {*à}")
    return {
        "RB46": f"define RB46 [{primary}] .o. [{secondary}];",
        "RB59": """define RB59 FootCtx([
    {*e} -> {*eo} || .#. OEAnyConsonant* _ [EnglishStarLabial | EnglishStarLiquid] {*u},
    {*æ} -> {*ea} || .#. OEAnyConsonant* _ [EnglishStarLabial | EnglishStarLiquid] EnglishBackMutationTrigger
]) .o. Ctx([
    {*é} -> {*éo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u},
    {*è} -> {*eo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u},
    {*ǽ} -> {*ea} || _ [EnglishStarLabial | EnglishStarLiquid] EnglishBackMutationTrigger
]);""",
    }


def codec_variants(text):
    from executable_facts import parse_defines
    facts = parse_defines(text)
    result = variants(text)
    body = facts["OEBreaking"].body
    decoder = ".o. [{*ǽ} -> {*æ}, {*à} -> {*a}, {*è} -> {*e}]"
    assert body.count(decoder) == 1
    result["RB44"] = "define RB44 " + body.replace(decoder, "") + ";"
    body = facts["OEARestoration"].body
    result["RB46C"] = ("define RB46C [" + body + "] .o. ["
                      + body.replace("{*æ} -> {*a}", "{*ǽ} -> {*à}") + "];")
    body = facts["OEIUmlautFronting"].body
    anchor = "{*a} -> {*æ} || _ EnglishIUmlautThroughU EnglishIUmlautTrigger,"
    assert body.count(anchor) == 1
    body = body.replace(anchor, anchor + """
    {*à} -> {*ǽ} || _ EnglishIUmlautThroughU EnglishIUmlautTrigger,
    {*è} -> {*i} || _ EnglishIUmlautThroughU EnglishIUmlautTrigger,""")
    result["RBIF"] = "define RBIF " + body + ";"
    body = facts["OEIUmlautRaising"].body
    result["RBIR"] = ("define RBIR [" + body + "] .o. ["
                     + body.replace("{*æ} -> {*e}", "{*ǽ} -> {*è}") + "];")
    result["RBI"] = "define RBI FootCtx(RBIF .o. RBIR .o. OEIUmlautDiphthong);"
    body = facts["OESecondaryNasalization"].body
    result["RBN"] = ("define RBN [" + body + "] .o. ["
                    + body.replace("{*a} -> {*ą}", "{*à} -> {*ą}") + "];")
    result["RBD"] = "define RBD Ctx([{*ǽ} -> {*æ}, {*à} -> {*a}, {*è} -> {*e}]);"
    body = facts["OEBackMutation"].body
    result["RB59C"] = "define RB59C [" + body + """] .o. Ctx([
    {*è} -> {*eo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u},
    {*ǽ} -> {*ea} || _ [EnglishStarLabial | EnglishStarLiquid] EnglishBackMutationTrigger
]) .o. RBD;"""
    result["RB59D"] = "define RB59D RB59 .o. RBD;"
    return result


def worker(snapshot):
    import anglo_frisian_experiments as compiler
    from capr_runtime import check_build_manifest, layout
    import oe_pipeline
    from sound_change_order_sensitivity import batch_apply_down

    begun = time.perf_counter()
    runtime = layout()
    plan = json.loads((snapshot / "plan.json").read_text())
    source = snapshot / "source.txt"
    assert source.read_bytes() == runtime.germanic_fst.read_bytes()
    assert (snapshot / "corpus.tsv").read_bytes() == runtime.corpus_tsv.read_bytes()
    for name, digest in plan["helpers"].items():
        assert hashlib.sha256((runtime.tools_dir / name).read_bytes()).hexdigest() == digest
    problems = check_build_manifest(oe_pipeline.expected_snapshot_bins() + ["old_english.bin"])
    if problems:
        raise ValueError(problems)
    rows = oe_pipeline.load_rows(runtime.corpus_tsv)
    by_id = {row["row_id"]: row for row in rows}
    selected = [by_id[key] for key in SELECTED]
    raw = [row["fst_input"] for row in rows]
    names = [stage.foma_identifier for stage in oe_pipeline.stages()]
    codec = plan.get("codec", False)
    at = names.index("OEBreaking" if codec else "OEARestoration")
    before = names[at - 1]
    checkpoint_names = [
        "PNWGmcULowering", "OEStripSecondaryStress", "EAFBrightening",
        before, "OEARestoration", "OEJClusterCoalescence",
        "OEBackMutation", "OENonHighSyn", "PGmcBAllophony"]
    live = {name: batch_apply_down(
        runtime.bin_dir / oe_pipeline.stage_for(name).snapshot_bin, raw)
        for name in checkpoint_names}
    final = batch_apply_down(runtime.bin_dir / "old_english.bin", raw)
    if any(len(value) != 1 for value in live[before]):
        raise ValueError("the common entry requires one state per selected row")
    incoming = [value[0] for value in live[before]]
    position = {row["row_id"]: i for i, row in enumerate(rows)}
    compounds = [incoming[position[key]] for key in ("2148", "2336")]
    schemas = (["régna-bàkaną", "régna-bakaną", "régna-xèbun", "régna-xebun",
                "gabákaną", "gasébun"] if codec else SCHEMAS)
    definitions = list(plan["variants"].values())
    queries = {}
    configurations = [
            ("baseline", {}), ("restoration", {"OEARestoration": "RB46"}),
            ("back_mutation", {"OEBackMutation": "RB59"}),
            ("joint", {"OEARestoration": "RB46", "OEBackMutation": "RB59"})]
    if codec:
        common = {"OEBreaking": "RB44", "OEARestoration": "RB46C",
                  "OESecondaryNasalization": "RBN", "OEIUmlaut": "RBI",
                  "OEBackMutation": "RB59C"}
        configurations = [("baseline", {}), ("annotation", common),
                          ("restoration", {**common, "OEARestoration": "RB46"}),
                          ("back_mutation", {**common, "OEBackMutation": "RB59D"}),
                          ("joint", {**common, "OEARestoration": "RB46",
                                     "OEBackMutation": "RB59D"})]
    for variant, replacements in configurations:
        order = [replacements.get(name, name) for name in names]
        for stop in ("OEARestoration", "OEJClusterCoalescence",
                     "OEBackMutation", "OENonHighSyn", "PGmcBAllophony"):
            queries[f"{variant}:{stop}"] = (order[at:names.index(stop) + 1], compounds)
        queries[f"{variant}:raw_final"] = (
            order, [row["fst_input"] for row in selected] + schemas)
        if variant != "baseline":
            queries[f"{variant}:corpus"] = (order[at:], incoming)
    for stage in ("EAFBrightening", "OEBreaking"):
        queries["schema:" + stage] = (names[:names.index(stage) + 1], schemas)
    if codec:
        for variant, replacements in configurations[1:]:
            order = [replacements.get(name, name) for name in names]
            for stage in ("OEBreaking", "OEARestoration", "OEBackMutation"):
                queries[f"{variant}:schema:{stage}"] = (
                    order[:names.index(stage) + 1], schemas)
    for label, relation in (("current46", "OEARestoration"), ("stress46", "RB46"),
                            ("current59", "OEBackMutation"), ("stress59", "RB59")):
        queries[label + ":local"] = ([relation], LOCAL)
    labels = {}
    for index, (label, (members, inputs)) in enumerate(queries.items()):
        name = "RBQ" + str(index)
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
            _, status, usage = os.wait4(process.pid, 0)
            process.returncode = os.waitstatus_to_exitcode(status)
            memory.append({"seconds": time.perf_counter() - started,
                           "peak_rss_kib": usage.ru_maxrss,
                           "returncode": process.returncode})
            stdout.seek(0)
            stderr.seek(0)
            log = stdout.read().decode() + "\n" + stderr.read().decode()
            if process.returncode or re.search(r"(?im)\b(error|syntax error|not defined)\b", log):
                raise RuntimeError("rainbow isolated compilation failed:\n" + log[-6000:])

    with tempfile.TemporaryDirectory(prefix="capr_rainbow_") as temporary:
        directory = Path(temporary)
        with patch.object(compiler, "_compile_foma", measured_compile):
            compiled = compiler.compile_isolated(
                source, recipe, [], directory, components_only=True,
                use_definition_image=bool(os.environ.get("CAPR_FOMA_DEFINITION_IMAGE")))
        sent = (directory / "experiment.foma").read_text()
        outputs = {label: batch_apply_down(compiled["component:" + name], queries[label][1])
                   for label, name in labels.items()}
    records = [
        {**row, "baseline": final[i],
         "live": {stage: values[i] for stage, values in live.items()}}
        for i, row in enumerate(rows)]
    corpus = {}
    for label in (["annotation"] if codec else []) + ["restoration", "back_mutation", "joint"]:
        comparison = [
            {"row_id": row["row_id"], "concept": row["concept"],
             "baseline": final[i], "outputs": values,
             "changed": set(values) != set(final[i]), "rejected": not values,
             "ambiguous": len(values) > 1}
            for i, (row, values) in enumerate(zip(rows, outputs[label + ":corpus"]))]
        corpus[label] = {
            "rows": comparison, "changed": sum(row["changed"] for row in comparison),
            "rejected": sum(row["rejected"] for row in comparison),
            "ambiguous": sum(row["ambiguous"] for row in comparison),
            "matches": sum(row["counterpart"] in values
                           for row, values in zip(rows, outputs[label + ":corpus"]))}
    return {
        "rows": records, "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "entry": {"stage": names[at], "side": "before"},
        "corpus": corpus,
        "queries": {label: {"members": members, "inputs": inputs, "outputs": outputs[label]}
                    for label, (members, inputs) in queries.items()},
        "compiler_appendix": recipe["definitions"],
        "cost": {"variants": len(configurations), "networks": len(queries), "compiler_calls": len(memory),
                 "foma_processes": memory, "image_loaded": sent.startswith("load defined "),
                 "definition_preparation_calls": 0, "seconds": time.perf_counter() - begun},
    }


def capture(*, codec=False):
    from adjudication_control import run_logged
    import adjudication_run
    from capr_runtime import container_command
    from experiment_snapshot import create_snapshot

    source = ROOT / "Germanic/fsts/germanic.txt"
    assessment = ROOT / (
        "Germanic/docs/sound_changes/literature_dossiers/"
        "rainbow-stress-domains/01-source-assessment.md")
    out = ROOT / ".capr-work/rainbow"
    plan = {
        "variants": (codec_variants if codec else variants)(source.read_text()),
        "selected": SELECTED, "codec": codec,
        "helpers": {name: hashlib.sha256((ROOT / "Germanic/tools" / name).read_bytes()).hexdigest()
                    for name in HELPERS},
        "predictions": assessment.read_text(),
    }
    plan_path = out / "plan.json"
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2))
    snapshot = create_snapshot(
        "rainbow-stress-" + uuid.uuid4().hex[:8],
        "Separate linker stress domains and test inherited syncope against controls",
        {"source": source, "corpus": ROOT / "Germanic/data/germanic-aligned-final.tsv",
         "worker": Path(__file__), "plan": plan_path, "assessment": assessment,
         **{Path(name).stem: ROOT / "Germanic/tools" / name for name in HELPERS}},
        variants=plan["variants"], probes=SELECTED + SCHEMAS + LOCAL,
        expected_outcomes={"assessment": plan["predictions"]},
        negative_controls=["unstressed compound linker", "dental outside labial/liquid proxy"])
    container = snapshot.stage_in_container()
    run = adjudication_run.load("SC059")
    if not codec:
        run.complete_stage("SNAPSHOT", evidence={"snapshot_root": str(snapshot.root)})
    receipt = run_logged(
        container_command("cd /usr/app && python3 " + shlex.quote(container + "/worker.py")
                          + " --worker " + shlex.quote(container)),
        label="rainbow-four-way", log_dir=snapshot.root / "execution")
    if receipt["ok"]:
        (snapshot.staging_dir / "observed.json").write_bytes(Path(receipt["stdout_log"]).read_bytes())
    snapshot.complete("passed" if receipt["ok"] else "failed",
                      "Executed comparisons; scientific acceptance is assessed separately", [receipt])
    if not receipt["ok"]:
        raise RuntimeError(Path(receipt["stderr_log"]).read_text())
    (out / ("codec-latest.json" if codec else "latest.json")).write_text(json.dumps({"snapshot_root": str(snapshot.root),
                                                "receipt": receipt}, indent=2))
    print(snapshot.root)


if __name__ == "__main__":
    if sys.argv[1:2] == ["--worker"]:
        print(json.dumps(worker(Path(sys.argv[2])), ensure_ascii=False))
    elif sys.argv[1:] == ["--capture"]:
        capture()
    elif sys.argv[1:] == ["--capture-codec"]:
        capture(codec=True)
    else:
        raise SystemExit("use --capture or --worker SNAPSHOT")

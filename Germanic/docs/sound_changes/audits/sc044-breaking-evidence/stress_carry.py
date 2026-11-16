#!/usr/bin/env python3
"""Preserve subordinate low/front stress until its breaking consumer."""
import hashlib
import json
import os
from pathlib import Path
import sys
import uuid

import experiment as original

ROOT, HERE = original.ROOT, original.HERE


def candidate(source):
    from executable_facts import parse_defines

    def replace(name, body):
        nonlocal source
        source = original.replace_definition(source, name, "define " + name + " " + body + ";")

    for name in ("PGmcStarVowel", "PGmcStarFrontVowel", "PGmcStarGraveVowel",
                 "EnglishStarShortVowel"):
        body = parse_defines(source)[name].body
        replace(name, "[" + body + " | {*ǽ}]")
    replace("OEStripSecondaryStress", "Ctx([{*ò} -> {*o}])")
    body = parse_defines(source)["OELHWeakRaising"].body
    replace("OELHWeakRaising", body.replace("{*a} -> {*u}", "[{*a}|{*à}] -> {*u}"))
    body = parse_defines(source)["EAFBrighteningStressed"].body
    replace("EAFBrighteningStressed", body + """ .o. [
    {*à} -> {*ǽ} || _ [EnglishStarConsonant - EnglishStarNasal | .#.]
]""")
    body = parse_defines(source)["OEBreakingA"].body
    replace("OEBreakingA", body + """ .o. [
    {*ǽ} -> {*ea} || _ EnglishBreakingRContext,
    {*ǽ} -> {*ea} || _ EnglishBreakingLContext,
    {*ǽ} -> {*ea} || _ EnglishBreakingHContext
]""")
    body = parse_defines(source)["OEBreakingE"].body
    replace("OEBreakingE", body + """ .o. [
    {*è} -> {*eo} || _ EnglishBreakingRContext,
    {*è} -> {*eo} || _ EnglishBreakingHContext,
    {*è} -> {*eo} || _ EnglishBreakingWContext,
    {*è} -> {*eo} || _ EnglishBreakingLContextE,
    {*è} -> {*eo} || {*s} _ {*l} {*k}
]""")
    replace("OEBreaking", """FootCtx(OEBreakingA
    .o. OEBreakingE .o. OEBreakingI .o. OEBreakingLong
    .o. [{*ǽ} -> {*æ}, {*à} -> {*a}, {*è} -> {*e}])""")
    return source


def worker(snapshot, directory):
    from anglo_frisian_experiments import compile_isolated, prepare_definition_image
    from cascade_baseline import build_baseline
    from oe_pipeline import normalize_proto
    from sound_change_order_sensitivity import batch_apply_down

    plan = json.loads((snapshot / "plan.json").read_text())
    source = snapshot / "candidate.txt"
    directory.mkdir()
    image = os.environ.get("CAPR_FOMA_DEFINITION_IMAGE") or prepare_definition_image(source, directory)
    if not image:
        raise RuntimeError("The new annotation alphabet needs its own definition image")
    os.environ["CAPR_FOMA_DEFINITION_IMAGE"] = str(image)
    probes = [dict(id=name, stage=name, side="after") for name in (
        "OEStripSecondaryStress", "EAFBrightening", "OEBreaking",
        "OEIUmlaut", "OEHLoss", "OEContraction")]
    recipe = dict(definitions="", replace={}, insert_rule=None, insert_after=None,
                  component_checks=[{"component": name} for name in (
                      "OEBreaking", "OEStripSecondaryStress", "EAFBrightening")])
    (directory / "bins").mkdir()
    bins = compile_isolated(source, recipe, probes, directory / "bins")
    inputs = [p["input"] for p in plan["probes"]]
    ids = [p["id"] for p in plan["probes"]]
    result = {
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "components": {name: dict(zip(ids, batch_apply_down(path, inputs)))
                       for name, path in bins.items() if name.startswith("component:")},
        "corpus": build_baseline(snapshot / "corpus.tsv", bins["final"]),
        "raw": [{"id": label, "input": raw,
                 "outputs": batch_apply_down(bins["final"], [normalize_proto(raw)])[0],
                 "trace": {p["id"]: batch_apply_down(
                     bins[p["id"]], [normalize_proto(raw)])[0] for p in probes}}
                for label, raw in plan["raw"]],
    }
    observed = result["components"]["component:OEBreaking"]
    for probe in plan["probes"]:
        if "expected" in probe:
            assert observed[probe["id"]] == probe["expected"], (
                probe["id"], observed[probe["id"]])
    assert result["corpus"]["records"] == plan["control_records"]
    raw = {r["id"]: r["outputs"] for r in result["raw"]}
    assert all(raw["compound-" + str(i)] == ["seleweard"] for i in range(3))
    print(json.dumps(result, ensure_ascii=False))


def host():
    import experiment_snapshot
    from adjudication_control import run_logged

    work = ROOT / ".capr-work/sc044/stress-carry"
    work.mkdir(parents=True, exist_ok=True)
    source = (ROOT / "Germanic/fsts/germanic.txt").read_text()
    proposed = candidate(source)
    (work / "candidate.txt").write_text(proposed)
    old = json.loads((HERE / "observed.json").read_text())
    expected = old["adopted"]["components"]["component:OEBreaking"]
    probes = [dict(p, expected=expected[p["id"]]) for p in original.cases()]
    probes += [
        dict(id="secondary-ae", input="*s*æ*l*ì*w*ǽ*r*d",
             expected=["*s*æ*l*io*w*ea*r*d"]),
        dict(id="secondary-e", input="*x*á*m*è*r*d", expected=["*x*á*m*eo*r*d"]),
        dict(id="secondary-rj", input="*x*á*m*ǽ*r*j*a",
             expected=["*x*á*m*æ*r*j*a"]),
        dict(id="secondary-unfronted", input="*x*á*m*à*n",
             expected=["*x*á*m*a*n"]),
    ]
    raw = [(r["id"], r["input"]) for r in old["adopted"]["raw"]]
    raw += [("compound-" + str(i), form) for i, form in enumerate(
        ("sáli-wàrðaz", "sáli-wàrðuz", "sáli-wàrðą"))]
    plan = dict(probes=probes, raw=raw, control_records=json.loads(
        (ROOT / ".capr-work/sc044/control-result.json").read_text())["corpus"]["records"])
    (work / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2))
    snap = experiment_snapshot.create_snapshot(
        "sc044-secondary-carry-" + uuid.uuid4().hex[:8],
        "Repair the full strict suite's conditional-compound regression without admitting weak breaking",
        {"candidate": work / "candidate.txt", "plan": work / "plan.json",
         "worker": Path(__file__), "experiment": HERE / "experiment.py",
         "corpus": ROOT / "Germanic/data/germanic-aligned-final.tsv",
         "entry_context_metadata": ROOT / "Germanic/data/entry_context_metadata.tsv"},
        variants={"candidate": proposed}, probes=probes, expected_outcomes=plan,
        negative_controls=["all previous weak controls", "secondary rj", "unfronted nasal"])
    import adjudication_run
    adjudication_run.load("SC044").complete_stage(
        "SNAPSHOT", note="Secondary-stress repair follows the recorded strict-suite failure.",
        evidence={"snapshot_root": str(snap.root)})
    print("SNAPSHOT", snap.root, flush=True)
    container = snap.stage_in_container()
    image_args = (["-e", "CAPR_FOMA_DEFINITION_IMAGE=" + os.environ["SC044_CARRY_IMAGE"]]
                  if os.environ.get("SC044_CARRY_IMAGE") else [])
    receipt = run_logged(
        ["docker", "compose", "exec", "-T", *image_args, "backend", "python3",
         container + "/worker.py", "--worker", container,
         "/tmp/capr-sc044-secondary-" + uuid.uuid4().hex[:8]],
        label="sc044-secondary-carry", log_dir=snap.staging_dir)
    snap.complete("passed" if receipt["ok"] else "failed",
                  "Compound, weak-vowel and complete selected-record controls", [receipt])
    if not receipt["ok"]:
        raise RuntimeError(Path(snap.results_dir / Path(receipt["stderr_log"]).name).read_text())
    result = json.loads((snap.results_dir / Path(receipt["stdout_log"]).name).read_text())
    (work / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(result["corpus"]["summary"], flush=True)


if __name__ == "__main__":
    if sys.argv[1:2] == ["--worker"]:
        worker(Path(sys.argv[2]), Path(sys.argv[3]))
    else:
        host()

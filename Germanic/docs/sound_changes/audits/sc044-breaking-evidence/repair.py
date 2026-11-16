#!/usr/bin/env python3
"""Follow up the independently observed mixed-context stress failure."""
import argparse
import hashlib
import json
import re
import sys
import uuid
from pathlib import Path

import experiment as original

ROOT, HERE = original.ROOT, original.HERE


def stress_grouping(source):
    from executable_facts import parse_defines

    for name in ("OEBreakingA", "OEBreakingE"):
        plain, marked = [], []
        for line in parse_defines(source)[name].body.splitlines():
            if "->" not in line:
                continue
            clause = line.strip().rstrip(",")
            if re.match(r"\{\*(?:a|æ|e)\}", clause):
                clause = clause.replace("|| ", "|| .#. OEAnyConsonant* ", 1)
                plain.append(clause)
            else:
                marked.append(clause)
        groups = ["[\n    " + ",\n    ".join(group) + "\n]"
                  for group in (plain, marked) if group]
        source = original.replace_definition(
            source, name, "define " + name + " " + " .o. ".join(groups) + ";")
    return source


def long_grouping(source):
    return original.replace_definition(source, "OEBreaking", """define OEBreakingLong [
    {*ǣ} -> {*ēa} || .#. OEAnyConsonant* _ EnglishBreakingHContext,
    {*ē} -> {*ēo} || .#. OEAnyConsonant* _ EnglishBreakingHContext,
    {*ī} -> {*īo} || .#. OEAnyConsonant* _ EnglishBreakingHContext
] .o. [
    {*ḗ} -> {*ḗo} || _ EnglishBreakingHContext,
    {*ḯ} -> {*īo} || _ EnglishBreakingHContext
];
define OEBreaking FootCtx(OEBreakingA
    .o. OEBreakingE .o. OEBreakingI .o. OEBreakingLong);""")


def i_lateral(source):
    from executable_facts import parse_defines

    lines = []
    for line in parse_defines(source)["OEBreakingI"].body.splitlines():
        lines.append(line)
        if "->" in line and "EnglishBreakingHContext" in line:
            lines.append(line.replace("EnglishBreakingHContext", "EnglishBreakingLContextI"))
    return original.replace_definition(
        source, "OEBreakingI",
        "define EnglishBreakingLContextI [{*l} {*x}];\n"
        "define OEBreakingI " + "\n".join(lines) + ";")


def candidate(source):
    return i_lateral(long_grouping(stress_grouping(
        original.palatal_l_only(original.lateral_only(original.front_only(source))))))


def overrides(base, source):
    from executable_facts import parse_defines

    before, after = parse_defines(base), parse_defines(source)
    components = ["OEBreakingA", "OEBreakingE", "OEBreakingI",
                  "OEBreakingLong", "OEBreaking"]
    changed = [name for name in after if name not in components
               and (name not in before or after[name].body != before[name].body)]
    return "\n".join(after[name].definition_raw
                     for name in changed + components if name in after)


def worker(snapshot, directory, variant):
    from anglo_frisian_experiments import compile_isolated
    from cascade_baseline import build_baseline
    from sound_change_order_sensitivity import batch_apply_down
    from oe_pipeline import normalize_proto

    plan = json.loads((snapshot / "plan.json").read_text())
    for name, expected in plan["helper_sha256"].items():
        assert hashlib.sha256((Path("/usr/app/tools") / name).read_bytes()).hexdigest() == expected, name
    base = (snapshot / "control.txt").read_text()
    source = (snapshot / (variant + ".txt")).read_text()
    spec = original.recipe()
    spec["definitions"] = overrides(base, source)
    moved = variant in ("before043", "after045", "front-before043")
    if moved:
        spec.update(
            definitions=spec["definitions"] + "\ndefine AFMoved OEBreaking;\ndefine AFSkip [?*];",
            insert_rule="AFMoved",
            insert_after=("OEVelarFricativePalatalization" if variant == "after045"
                          else "EAFBrighteningUnstressed"),
            replace={"OEBreaking": "AFSkip"})
    spec["definitions"] += """
define AFFront [{*á} -> {*æ}];
define AFMut [{*æ} -> {*e} || _ EnglishIUmlautIntervening {*j}];
define AFEarlyA [{*æ} -> {*ea} || _ EnglishBreakingRContext];
define AFEarlyE [{*e} -> {*eo} || _ EnglishBreakingRContext];
define AFMutEA [{*ea} -> {*e} || _ EnglishIUmlautIntervening {*j}];
define AFLateA [{*a} -> {*ea} || _ {*r} [{*d}|{*ð}|{*m}|{*b}]];
define AFLateE [{*e} -> {*eo} || _ {*r} {*m}];
define AFRivalFront [{*á} -> {*æ} || _ EnglishIUmlautIntervening {*j}];
define AFConventional AFFront .o. AFEarlyA .o. AFEarlyE .o. AFMutEA .o. AFMut;
define AFLate AFRivalFront .o. AFMut .o. [{*á} -> {*a}] .o. AFLateE .o. AFLateA;
"""
    spec["component_checks"] += [{"component": name} for name in ("AFConventional", "AFLate")]
    full = variant == "candidate" or moved
    probes = [dict(id=name, stage=name, side="after") for name in (
        "EAFBrighteningUnstressed", "EAFBrightening", "EAFBrighteningLongFinal",
        "OEBreaking", "OEVelarFricativePalatalization", "OEARestoration",
        "OEIUmlaut", "OEHLoss", "OEContraction")] if full else []
    directory.mkdir()
    bins = compile_isolated(snapshot / "control.txt", spec, probes, directory,
                            components_only=not full)
    forms = [p["input"] for p in plan["probes"]]
    ids = [p["id"] for p in plan["probes"]]
    result = {
        "variant": variant, "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "components": {name: dict(zip(ids, batch_apply_down(path, forms)))
                       for name, path in bins.items() if name.startswith("component:")},
    }
    if full:
        if moved:
            records = []
            controls = plan["control_records"]
            values = batch_apply_down(bins["final"], [r["fst_input"] for r in controls])
            for old, outs in zip(controls, values):
                records.append({
                    **old, "accepted": str(int(bool(outs))), "output_count": str(len(outs)),
                    "match": str(int(old["counterpart"] in outs)), "outputs": "|".join(outs)})
            result["corpus"] = {"records": records, "summary": {
                "total_lexemes": len(records),
                "accepted": sum(r["accepted"] == "1" for r in records),
                "rejected": sum(r["accepted"] == "0" for r in records),
                "matched": sum(r["match"] == "1" for r in records),
                "mismatched": sum(r["match"] == "0" for r in records),
                "ambiguous_outputs": sum(int(r["output_count"]) > 1 for r in records),
                "purpose": "counterfactual observation, not an accepted baseline"}}
        else:
            result["corpus"] = build_baseline(snapshot / "corpus.tsv", bins["final"])
        result["checkpoints"] = {
            p["id"]: dict(zip(
                [r["row_id"] for r in plan["control_records"]],
                batch_apply_down(bins[p["id"]], [r["fst_input"] for r in plan["control_records"]])))
            for p in probes}
        result["raw"] = []
        for label, raw, warrant in plan["raw"]:
            form = normalize_proto(raw)
            result["raw"].append({
                "id": label, "input": form, "warrant": warrant,
                "outputs": batch_apply_down(bins["final"], [form])[0],
                "trace": {p["id"]: batch_apply_down(bins[p["id"]], [form])[0] for p in probes},
            })
    if variant == "candidate":
        expected_unchanged = ("weak-a", "weak-ae", "weak-e", "weak-selk",
                              "fulwiht-weak", "nawiht-weak", "weak-i-no-w",
                              "w-before-i", "w-before-j", "erian-rj", "long-not-weak")
        observed = result["components"]["component:OEBreaking"]
        inputs = {p["id"]: p["input"] for p in plan["probes"]}
        for identifier in expected_unchanged:
            assert observed[identifier] == [inputs[identifier]], (identifier, observed[identifier])
        assert observed["filhith-short-i"] == ["*f*ío*l*x*i*θ"]
        assert {r["id"]: r["outputs"] for r in result["raw"]}["sell"] == ["sellan"]
    print(json.dumps(result, ensure_ascii=False))


def host(image):
    import subprocess
    import experiment_snapshot
    from adjudication_control import run_logged

    work = ROOT / ".capr-work/sc044/repair"
    work.mkdir(parents=True, exist_ok=True)
    base = subprocess.check_output(
        ["git", "show", original.BASE + ":Germanic/fsts/germanic.txt"], cwd=ROOT, text=True)
    variants = dict(stress_grouping=stress_grouping(base), long_grouping=long_grouping(base),
                    i_lateral=i_lateral(base), candidate=candidate(base),
                    before043=base, after045=base,
                    **{"front-before043": original.front_only(base)})
    extra = [
        dict(id="tar-consonantal-w", input="*t*e*r*w*u", kind="stage diagnostic",
             question="retained consonantal w versus the attested spelling teru",
             warrant="Hogg §5.22 n.6; Versloot §5.4; premise about w must be stated"),
        dict(id="tar-vocalized-w", input="*t*e*r*u", kind="stage diagnostic",
             question="w already vocalized; not a covered-r environment",
             warrant="Same historical comparison with a contrasting timing premise"),
        dict(id="farmjan", input="*f*á*r*m*j*a*n", kind="reconstructed finite history",
             question="mutation-created e at late breaking",
             warrant="Pheifer p.22 no.402; Versloot §5.4"),
        dict(id="germantlab", input="*g*e*r*m*a*n*t*l*æ*β", kind="qualified reconstruction",
             question="original-front e comparison",
             warrant="Pheifer no.656 and p.103; complete etymology uncertain"),
    ]
    plan = dict(base_commit=original.BASE, probes=original.cases() + extra,
                helper_sha256=json.loads(
                    (ROOT / ".capr-work/sc044/plan.json").read_text())["helper_sha256"],
                control_records=json.loads(
                    (ROOT / ".capr-work/sc044/control-result.json").read_text())["corpus"]["records"],
                raw=[(label, "*nḗxwaz" if label == "near" else form, warrant)
                     for label, form, warrant in original.RAW])
    (work / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2))
    inputs = {
        "plan": work / "plan.json", "worker": Path(__file__),
        "experiment": HERE / "experiment.py",
        "control": ROOT / ".capr-work/sc044/control.txt",
        "corpus": ROOT / "Germanic/data/germanic-aligned-final.tsv",
        "entry_context_metadata": ROOT / "Germanic/data/entry_context_metadata.tsv",
    }
    for name, source in variants.items():
        path = work / (name + ".txt")
        path.write_text(source)
        inputs[name] = path
    snap = experiment_snapshot.create_snapshot(
        "sc044-stress-repair-" + uuid.uuid4().hex[:8],
        "Repair failed weak-E/long-vowel contexts and the independently sourced I-before-lx gap",
        inputs, variants=variants, probes=plan["probes"], expected_outcomes=plan,
        negative_controls=["weak medial A/E/I", "following i/j", "rj", "weak long vowel"])
    print("SNAPSHOT", snap.root, flush=True)
    container = snap.stage_in_container()
    receipts = []
    if not image:
        raise ValueError("Supply the freshly prepared, compiler-validated --image from the main experiment")
    for name in variants:
        receipt = run_logged(
            ["docker", "compose", "exec", "-T", "-e", "CAPR_FOMA_DEFINITION_IMAGE=" + image,
             "backend", "python3", container + "/worker.py", "--worker", container,
             "/tmp/capr-sc044-repair-" + uuid.uuid4().hex[:8], name],
            label="sc044-repair-" + name, log_dir=snap.staging_dir)
        receipts.append(receipt)
        if not receipt["ok"]:
            snap.complete("failed", name + " failed execution or required controls", receipts)
            raise RuntimeError(Path(receipt["stderr_log"]).read_text())
        result = json.loads(Path(receipt["stdout_log"]).read_text())
        (work / (name + "-result.json")).write_text(json.dumps(result, ensure_ascii=False, indent=2))
        print("COMPLETE", name, flush=True)
    snap.complete("passed", "Required stress negatives and the I/lx positive passed", receipts)


if __name__ == "__main__":
    if sys.argv[1:2] == ["--worker"]:
        worker(Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4])
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument("--image", required=True)
        host(parser.parse_args().image)

#!/usr/bin/env python3
"""Pinned SC044 research using the existing isolated Foma compiler."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

BASE = "54b15a2d3a764d5ac92c9ce0c1ecaf398aed878f"
HERE = Path(__file__).resolve().parent
ROOT = Path("/usr/app") if Path("/usr/app/tools").is_dir() else HERE.parents[4]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
if Path("/usr/app/tools").is_dir():
    sys.path.insert(0, "/usr/app/tools")


def replace_definition(text, name, definition):
    from executable_facts import _blank_comments

    scan = _blank_comments(text)
    match = re.search(r"\bdefine\s+" + re.escape(name) + r"\b", scan)
    if match is None:
        raise ValueError(name)
    depth = 0
    for end in range(match.end(), len(scan)):
        if scan[end] in "([":
            depth += 1
        elif scan[end] in ")]":
            depth -= 1
        elif scan[end] == ";" and depth == 0:
            return text[:match.start()] + definition + text[end + 1:]
    raise ValueError("unterminated " + name)


def front_only(source):
    from executable_facts import parse_defines

    body = parse_defines(source)["OEBreakingA"].body
    clauses = [line.strip().rstrip(",") for line in body.splitlines()
               if "->" in line and "{*æ}" in line]
    return replace_definition(
        source, "OEBreakingA", "define OEBreakingA [\n    "
        + ",\n    ".join(clauses) + "\n];")


def lateral_only(source):
    source = replace_definition(
        source, "EnglishBreakingLContextE",
        "define EnglishBreakingLContextE [{*l} [{*x} | {*w}]];")
    from executable_facts import parse_defines

    body = parse_defines(source)["OEBreakingE"].body
    return replace_definition(source, "OEBreakingE",
                              "define OEBreakingE " + body + " .o. [\n"
                              "    {*e} -> {*eo} || {*s} _ {*l} {*k},\n"
                              "    {*é} -> {*éo} || {*s} _ {*l} {*k}\n];")


def stress_only(source):
    from executable_facts import parse_defines

    for name in ("OEBreakingA", "OEBreakingE"):
        body = parse_defines(source)[name].body
        body = re.sub(r"(\{\*(?:a|æ|e)\} -> \{\*[^}]+\} \|\|) ",
                      r"\1 .#. OEAnyConsonant* ", body)
        source = replace_definition(source, name, f"define {name} {body};")
    return source


def palatal_l_only(source):
    return replace_definition(source, "EnglishBreakingLContext", """define EnglishBreakingLContext [
    {*l} [EnglishStarConsonant - [{*l}|{*j}]] |
    {*l} {*l} [[ContextSegments - {*j}] | .#.]
];""")


def long_only(source):
    definition = """define OEBreakingLong [
    {*ǣ} -> {*ēa} || .#. OEAnyConsonant* _ EnglishBreakingHContext,
    {*ē} -> {*ēo} || .#. OEAnyConsonant* _ EnglishBreakingHContext,
    {*ī} -> {*īo} || .#. OEAnyConsonant* _ EnglishBreakingHContext,
    {*ḗ} -> {*ḗo} || _ EnglishBreakingHContext,
    {*ḯ} -> {*īo} || _ EnglishBreakingHContext
];
define OEBreaking FootCtx(OEBreakingA
    .o. OEBreakingE .o. OEBreakingI .o. OEBreakingLong);"""
    return replace_definition(source, "OEBreaking", definition)


def candidate(source):
    return long_only(stress_only(palatal_l_only(lateral_only(front_only(source)))))


def cases():
    rows = []

    def add(identifier, form, question, warrant, kind="stage diagnostic"):
        rows.append(dict(id=identifier, input=form, question=question,
                         warrant=warrant, kind=kind))

    for identifier, form in (
        ("seal-lx", "*s*é*l*x"), ("elk-lx", "*é*l*x"),
        ("languish-selk", "*s*é*l*k*a*n"), ("milk-melk", "*m*é*l*k*a*n"),
        ("unwitnessed-elg", "*b*é*l*g*a*n"),
        ("yellow-lw", "*g*é*l*w*æ"), ("meal-lw", "*m*é*l*w*æ*s"),
        ("self-ws", "*s*é*l*f"), ("dig-lf", "*d*é*l*f*a*n"),
    ):
        add(identifier, form, "short E before a covered lateral",
            "Campbell §§146–147; Hogg §5.22 and notes; Ringe–Taylor pp.186–188")
    for identifier, form in (
        ("southern-all", "*æ*l*l"), ("southern-half", "*x*æ*l*f"),
        ("anglian-back-all", "*a*l*l"), ("palatal-sellan", "*s*æ*l*l*j*a*n"),
        ("palatal-hell", "*x*æ*l*l*j*ō"), ("erian-rj", "*æ*r*j*a*n"),
    ):
        add(identifier, form, "low-vowel input and palatalized liquid contrast",
            "Campbell §139 n.3, §§143–145; Hogg §§5.15–16; Ringe–Taylor pp.181,184–186")
    for vowel in ("a", "á", "æ"):
        for tail in ("", "*t", "*a*n*ą", "*i", "*u", "*é", "*j*a*n*ą"):
            add(f"x-{vowel}-{tail or 'bare'}", "*s*l*" + vowel + "*x" + tail,
                "short input quantity; bare x versus consonant and contrasting tails",
                "Hogg §§5.16,5.20; Campbell §§145,234; Fulk pp.74–75")
    for identifier, form in (
        ("meox-primary-i", "*m*í*x*s"), ("meox-unmarked-i", "*m*i*x*s"),
        ("picts-short-i", "*p*í*x*t*a*s"),
        ("fulwiht-weak", "*f*u*l*w*i*x*t"),
        ("nawiht-weak", "*n*ā*w*i*x*t"),
        ("weak-i-no-w", "*x*á*m*i*x*t"),
        ("explicit-secondary-i", "*x*á*m*w*ì*x*t"),
        ("primary-i-medial", "*b*e*m*í*x*s"),
        ("weak-a", "*x*á*m*a*r*d"),
        ("weak-ae", "*x*á*m*æ*r*d"),
        ("weak-e", "*x*á*m*e*r*d"),
        ("weak-selk", "*x*á*m*s*e*l*k"),
        ("secondary-ae-representation-gap", "*x*á*m*æ*r*d"),
        ("filhith-short-i", "*f*í*l*x*i*θ"),
        ("primary-e-medial", "*b*e*m*é*r*d"),
        ("knee-short", "*k*n*é*w*ē"),
        ("w-before-i", "*k*n*é*w*i"),
        ("w-before-j", "*k*n*é*w*j*a"),
        ("near-long", "*n*ǣ*x"),
        ("light-weight-long", "*l*ḯ*x*t"),
        ("nonws-near-long", "*n*ē*x"),
        ("long-not-rC", "*b*ḯ*r*d"),
        ("long-not-weak", "*x*á*m*ī*x*t"),
    ):
        add(identifier, form, "stress, quantity and w exclusion",
            "Hogg §§5.21–25,6.7–8; Campbell §§148–154; Fulk §§4.13–14")
    return rows


RAW = [
    ("slay", "*sláxaną", "PGmc; selected inherited infinitive"),
    ("seal", "*sélxaz", "PNWGmc selhaz, Ringe–Taylor p.187; x notation"),
    ("milk", "*mélkaną", "constructed infinitive of the melcan comparison"),
    ("meox", "*míxs", "PWGmc mihs, Ringe–Taylor p.178; later-stage input"),
    ("hell", "*xáljō", "PGmc haljo, Ringe–Taylor p.185; x notation"),
    ("sell", "*sáljaną", "PGmc saljana, Ringe–Taylor p.185"),
    ("near", "*nēxwaz", "PGmc long ē1, conventional neah comparison"),
    ("light-weight", "*línxtaz", "PGmc linhtaz, Ringe–Taylor p.178; x notation"),
    ("flask-nompl", "*fláskōniz", "adopted inherited nominative plural"),
    ("flask-datsg", "*fláskōni", "independently attested inherited dative singular"),
    ("maere", "*márōn", "adopted final-nasal control"),
]


def recipe():
    return dict(definitions="", insert_after="", insert_rule="", replace={},
                component_checks=[{"component": name} for name in (
                    "OEBreaking", "OEBreakingA", "OEBreakingE", "OEBreakingI",
                    "EnglishBreakingXContextNonWeakA",
                    "EnglishBreakingXContextWeakTail", "OEBackMutation",
                    "OEIUmlaut", "EAFBrightening", "OEVelarFricativePalatalization")],
                staged_checks=[dict(id="rest-of-cascade", stage="OEBreaking",
                                    side="before")])


def worker(snapshot_dir, output, variant):
    from anglo_frisian_experiments import compile_isolated, corpus_rows
    from capr_runtime import layout
    from sound_change_order_sensitivity import batch_apply_down
    import oe_pipeline
    from cascade_baseline import build_baseline

    pins = json.loads((snapshot_dir / "plan.json").read_text())
    source = snapshot_dir / (variant + ".txt")
    for name, expected in pins["helper_sha256"].items():
        assert hashlib.sha256((Path("/usr/app/tools") / name).read_bytes()).hexdigest() == expected, name
    probes = pins["probes"]
    rt = layout()
    if not rt.is_container:
        raise RuntimeError("Foma execution requires the backend container")
    output.mkdir()
    spec = recipe()
    from executable_facts import parse_defines
    before = parse_defines((snapshot_dir / "control.txt").read_text())
    after = parse_defines(source.read_text())
    components = ["OEBreakingA", "OEBreakingE", "OEBreakingI",
                  "OEBreakingLong", "OEBreaking"]
    changed = [name for name in after if name not in components
               and (name not in before or after[name].body != before[name].body)]
    # Rebind composed networks after overriding their constituent definitions.
    spec["definitions"] = "\n".join(
        after[name].definition_raw for name in changed + components if name in after)
    if variant in ("before043", "after045", "front-before043"):
        spec.update(
            definitions=spec["definitions"] + "\ndefine AFMoved OEBreaking;\ndefine AFSkip [?*];",
            insert_rule="AFMoved",
            insert_after=("OEVelarFricativePalatalization" if variant == "after045"
                          else "EAFBrighteningUnstressed"),
            replace={"OEBreaking": "AFSkip"})
    checkpoints = ("EAFBrighteningUnstressed", "EAFBrightening",
                   "EAFBrighteningLongFinal", "OEBreaking",
                   "OEVelarFricativePalatalization", "OEARestoration",
                   "OEIUmlaut", "OEHLoss", "OEContraction")
    available = {stage.foma_identifier for stage in oe_pipeline.stages()}
    prefix_probes = [dict(id=name, stage=name, side="after")
                     for name in checkpoints if name in available]
    diagnostic_only = variant not in (
        "control", "candidate", "before043", "after045", "front-before043")
    bins = compile_isolated(snapshot_dir / "control.txt", spec,
                            [] if diagnostic_only else prefix_probes, output,
                            components_only=diagnostic_only)
    result = dict(variant=variant, source_sha256=hashlib.sha256(source.read_bytes()).hexdigest())
    inputs = [p["input"] for p in probes]
    result["components"] = {
        name: dict(zip([p["id"] for p in probes], batch_apply_down(path, inputs)))
        for name, path in bins.items() if name.startswith("component:")
    }
    result["stage_finals"] = (
        {} if diagnostic_only else dict(zip([p["id"] for p in probes],
        batch_apply_down(bins["staged:rest-of-cascade"], inputs))))
    x_forms = ["*x" + tail for tail in ("", "*t", "*a*n*ą", "*i", "*u", "*é", "*j*a*n*ą")]
    result["x_languages"] = {
        name: dict(zip(x_forms, batch_apply_down(bins["component:" + name], x_forms)))
        for name in ("EnglishBreakingXContextNonWeakA", "EnglishBreakingXContextWeakTail")
    }
    raw = [] if diagnostic_only else [(label, oe_pipeline.normalize_proto(form), warrant)
           for label, form, warrant in pins["raw"]]
    result["raw"] = [
        dict(id=label, normalized=form, warrant=warrant,
             outputs=batch_apply_down(bins["final"], [form])[0],
             trace={name: batch_apply_down(bins[name], [form])[0]
                    for name in (p["id"] for p in prefix_probes)})
        for label, form, warrant in raw
    ]
    corpus_path = snapshot_dir / "corpus.tsv"
    corpus = [] if diagnostic_only else corpus_rows(corpus_path)
    result["corpus"] = None if diagnostic_only else build_baseline(corpus_path, bins["final"])
    forms = [oe_pipeline.evaluation_input(row) for row in corpus]
    result["checkpoints"] = {
        p["id"]: dict(zip([r["id"] for r in corpus],
                         batch_apply_down(bins[p["id"]], forms)))
        for p in ([] if diagnostic_only else prefix_probes)
    }
    if variant != "control":
        print(json.dumps(result, ensure_ascii=False))
        return
    # A finite contrast of *farmjan- histories, not a second dialect-wide cascade.
    rm = "{*r} {*m}"
    definitions = """
define AFFront [{*á} -> {*æ}];
define AFMut [{*æ} -> {*e} || _ EnglishIUmlautIntervening {*j}];
define AFEarlyA [{*æ} -> {*ea} || _ EnglishBreakingRContext];
define AFEarlyE [{*e} -> {*eo} || _ EnglishBreakingRContext];
define AFMutEA [{*ea} -> {*e} || _ EnglishIUmlautIntervening {*j}];
define AFLateA [{*a} -> {*ea} || _ {*r} [{*d}|{*ð}|{*m}|{*b}]];
define AFLateE [{*e} -> {*eo} || _ """ + rm + """];
define AFRivalFront [{*á} -> {*æ} || _ EnglishIUmlautIntervening {*j}];
define AFConventional AFFront .o. AFEarlyA .o. AFEarlyE .o. AFMutEA .o. AFMut;
define AFLate AFRivalFront .o. AFMut .o. [{*á} -> {*a}] .o. AFLateE .o. AFLateA;
"""
    rival = recipe()
    rival.update(definitions=definitions,
                 component_checks=[{"component": n}
                                   for n in ("AFConventional", "AFLate")])
    rival_dir = output / "rival"
    rival_dir.mkdir()
    rival_bins = compile_isolated(snapshot_dir / "control.txt", rival, [], rival_dir, components_only=True)
    rival_forms = ("*f*á*r*m*j*a*n", "*g*e*r*m*a*n*t*l*æ*β",
                   "*w*e*r*k*i", "*s*m*e*r*w*i", "*t*e*r*u",
                   "*g*a*r*d", "*g*á*r*d", "*g*æ*r*d", "*x*æ*l*d")
    result["rival"] = {
        name: dict(zip(rival_forms, batch_apply_down(path, list(rival_forms))))
        for name, path in rival_bins.items()
    }
    print(json.dumps(result, ensure_ascii=False))


def smoke(snapshot_dir, output):
    from anglo_frisian_experiments import compile_isolated
    from sound_change_order_sensitivity import batch_apply_down

    output.mkdir()
    spec = recipe()
    spec.update(definitions="define AFProbeLang EnglishStarAlphabet*;",
                component_checks=[{"component": name}
                                  for name in ("AFProbeLang", "OEBreaking")])
    bins = compile_isolated(snapshot_dir / "control.txt", spec, [], output,
                            components_only=True)
    probes = json.loads((snapshot_dir / "plan.json").read_text())["probes"]
    forms = [p["input"] for p in probes]
    admitted = batch_apply_down(bins["component:AFProbeLang"], forms)
    observed = batch_apply_down(bins["component:OEBreaking"], forms)
    assert admitted == [[form] for form in forms], [
        p for p, values in zip(probes, admitted) if not values]
    assert all(observed), [p for p, values in zip(probes, observed) if not values]
    print(json.dumps({"admitted_probes": len(forms), "nonempty_rule_results": len(observed)}))


def host():
    import experiment_snapshot
    from adjudication_control import run_logged

    work = ROOT / ".capr-work/sc044"
    work.mkdir(parents=True, exist_ok=True)
    base = subprocess.run(["git", "show", BASE + ":Germanic/fsts/germanic.txt"],
                          cwd=ROOT, check=True, capture_output=True, text=True).stdout
    variants = dict(control=base, front_only=front_only(base),
                    lateral_only=lateral_only(base), stress_only=stress_only(base),
                    long_only=long_only(base), palatal_l_only=palatal_l_only(base),
                    candidate=candidate(base),
                    before043=base, after045=base,
                    **{"front-before043": front_only(base)})
    helpers = ("anglo_frisian_experiments.py", "oe_pipeline.py",
               "sound_change_order_sensitivity.py", "cascade_baseline.py")
    plan = dict(base_commit=BASE, probes=cases(), raw=RAW,
                helper_sha256={name: hashlib.sha256(
                    (ROOT / "Germanic/tools" / name).read_bytes()).hexdigest()
                    for name in helpers},
                prediction="Each clause is compiled separately; see the pre-run prediction ledger.")
    (work / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2))
    inputs = {"plan": work / "plan.json", "worker": Path(__file__),
              "corpus": ROOT / "Germanic/data/germanic-aligned-final.tsv",
              "entry_context_metadata": ROOT / "Germanic/data/entry_context_metadata.tsv"}
    for name, text in variants.items():
        path = work / (name + ".txt")
        path.write_text(text)
        inputs[name] = path
    snap = experiment_snapshot.create_snapshot(
        "sc044-breaking-" + __import__("uuid").uuid4().hex[:8],
        "Independent clause diagnostics and witness-specific displacement at integrated update",
        inputs, variants=variants, probes=cases(),
        expected_outcomes=plan,
        negative_controls=["melcan", "hell/sellan", "rj", "fulwiht/nawiht",
                           "weak medial A/E", "following i/j"])
    print("SNAPSHOT", snap.root, flush=True)
    container = snap.stage_in_container()
    collected = {}
    receipts = []
    image_dir = "/tmp/capr-sc044-image-" + __import__("uuid").uuid4().hex[:8]
    code = (
        "import sys;from pathlib import Path;sys.path.insert(0,'/usr/app/tools');"
        "from anglo_frisian_experiments import prepare_definition_image;"
        "out=Path(sys.argv[2]);out.mkdir();"
        "image=prepare_definition_image(Path(sys.argv[1]),out);"
        "assert image is not None;print(image)")
    preparation = run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", "-c", code,
         container + "/control.txt", image_dir],
        label="sc044-definition-image", log_dir=snap.staging_dir)
    receipts.append(preparation)
    if not preparation["ok"]:
        snap.complete("failed", "Definition-image preparation failed", receipts)
        raise RuntimeError(Path(preparation["stderr_log"]).read_text())
    image = Path(preparation["stdout_log"]).read_text().strip()
    command = ["docker", "compose", "exec", "-T", "-e",
               "CAPR_FOMA_DEFINITION_IMAGE=" + image, "backend", "python3",
               container + "/worker.py"]
    preflight = run_logged(
        command + ["--smoke", container, image_dir + "/smoke"],
        label="sc044-probe-language", log_dir=snap.staging_dir)
    receipts.append(preflight)
    if not preflight["ok"]:
        snap.complete("failed", "Probe-language preflight failed", receipts)
        raise RuntimeError(Path(preflight["stderr_log"]).read_text())
    for name in variants:
        print("RUNNING", name, flush=True)
        receipt = run_logged(
            command + ["--worker", container,
             "/tmp/capr-sc044-" + name + "-" + __import__("uuid").uuid4().hex[:8], name],
            label="sc044-" + name, log_dir=snap.staging_dir)
        receipts.append(receipt)
        if not receipt["ok"]:
            print(Path(receipt["stderr_log"]).read_text(), flush=True)
            snap.complete("failed", name + " did not execute", receipts)
            raise SystemExit(1)
        result = json.loads(Path(receipt["stdout_log"]).read_text())
        collected[name] = result
        (work / (name + "-result.json")).write_text(json.dumps(result, ensure_ascii=False, indent=2))
        print(name, result["corpus"]["summary"] if result["corpus"] else "independent components",
              flush=True)
    snap.complete("passed", "All planned experiments executed; historical success is assessed separately",
                  receipts, evidence={"variants": list(variants)})
    print("COMPLETE", snap.root, flush=True)


if __name__ == "__main__":
    if sys.argv[1:2] == ["--worker"]:
        worker(Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4])
    elif sys.argv[1:2] == ["--smoke"]:
        smoke(Path(sys.argv[2]), Path(sys.argv[3]))
    else:
        host()

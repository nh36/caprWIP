#!/usr/bin/env python3
"""Immutable research-only complete lexical-cell and local syncope comparisons."""
from __future__ import annotations

import argparse
import csv
import gzip
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
GERMANIC = HERE.parents[3]
ROOT = GERMANIC.parent
sys.path.insert(0, str(GERMANIC / "tools"))
OLD_PATH = HERE.parent / "soul-syncope-resolution/experiment.py"
spec = importlib.util.spec_from_file_location("syncope_resolution", OLD_PATH)
resolution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(resolution)
prior = resolution.prior
BASE = "1fb0223ba4b308afe4b72a0dc9cad805ca7f786c"
EXTRA = """
define RCellEnd [
    SCellEnd|a:{*a}|ą:{*ą}|{ai}:{*ai}|i:{*i}|0
];
define RProductive [
    [pgrmStrongPlainHeavy|pgrmStrongPlainHeavyPrefixed] SCellStem* RCellEnd
];
define RPrevious [EnglishProtoInput|RProductive];
define RInput [
    EnglishProtoInput|[[RProductive.u - EnglishProtoInput.u] .o. RProductive]
];
define RLocal Ctx([
    SNonHigh -> 0 || EnglishStarVocalic SCon+ _ SFollowing .#.
]);
define RPosttonic FootCtx([
    SNonHigh -> 0 ||
        .#. SCon* EnglishStarVocalic [SCon+ EnglishStarVocalic]* SCon+
        _ SFollowing .#.
]);
"""


def models(original):
    sequences = resolution.models(original)
    names = ("A-production", "A-coverage", "B-no-proxy", "C-nonhigh",
             "G-light-nonhigh")
    answer = {name: ["RInput" if s == "TInput" else s for s in sequences[name]]
              for name in names}
    for name, rule in (("H-local-nonhigh", "RLocal"),
                       ("K-stress-aware", "RPosttonic"),
                       ("J-open-medial", "STradSyn")):
        answer[name] = [rule if s == "TNonHigh" else s
                        for s in answer["G-light-nonhigh"]]
    return answer


def controls():
    extra = json.loads((HERE.parent / "soul-syncope-resolution/controls.json").read_text())
    answer = {**prior.CONTROLS, **{
        c["id"]: (c["input"], c["expected"].replace(" ", "")) for c in extra}}
    answer.update({
        "prefixed-soul-heavy": ("gesāwalǭ", "gesāwlǭ"),
        "prefixed-soul-light": ("gesāwalu", "gesāwalu"),
        "prefixed-light-root": ("geawælæs", "geawlæs"),
        "internal-closed-medial": ("gesāwalkǭ", "gesāwalkǭ"),
        "internal-stressed-medial": ("gesāwálǭ", "gesāwálǭ"),
        "internal-long-medial": ("gesāwālǭ", "gesāwālǭ"),
        "summer-closed-final": ("sumar", "sumar"),
        "water-closed-final": ("wætær", "wætær"),
        "over-closed-final": ("oβær", "oβær"),
        "marked-prefix-heavy": ("ᶠgesāwalǭ", "ᶠgesāwlǭ"),
        "marked-prefix-light": ("ᶠgesāwalu", "ᶠgesāwalu"),
        "marked-primary-root": ("ᶠgegedæs", "ᶠgegedæs"),
        "longer-posttonic-domain": ("tādanalǭ", "tādanlǭ"),
    })
    return answer


def worker(output):
    import oe_pipeline
    from anglo_frisian_experiments import compile_isolated, prepare_definition_image
    from capr_runtime import RuntimeLayout
    from sound_change_order_sensitivity import batch_apply_down

    if not Path("/.dockerenv").exists() or GERMANIC == Path("/usr/app"):
        raise RuntimeError("Requires container-private frozen sources")
    canonical = RuntimeLayout(Path("/usr/app"), Path("/usr/app"), Path("/usr/app"), True)
    paths = [*canonical.fsts_dir.rglob("*"), *canonical.data_dir.rglob("*"),
             *canonical.docs_dir.rglob("*"), *canonical.tools_dir.glob("*.py"),
             *canonical.bin_dir.glob("*.bin"), canonical.build_manifest]
    protected = {str(p): resolution.sha(p) for p in paths if p.is_file()}
    for relative in ("fsts/germanic.txt", "data/germanic-aligned-final.tsv"):
        if resolution.sha(GERMANIC / relative) != resolution.sha(Path("/usr/app") / relative):
            raise RuntimeError("Canonical scientific baseline drift")
    rows = oe_pipeline.load_rows(GERMANIC / "data/germanic-aligned-final.tsv")
    with (GERMANIC / "docs/sound_changes/cascade_baseline/"
          "cascade_baseline_outputs_legacy380.tsv").open() as handle:
        legacy = list(csv.DictReader(handle, delimiter="\t"))
    candidates = json.loads((HERE / "candidates.json").read_text())
    inputs = [oe_pipeline.evaluation_input(row) for row in rows + legacy]
    inputs += [oe_pipeline.evaluation_input(
        {"proto_norm": oe_pipeline.normalize_proto(c["input"])}) for c in candidates]
    original = [s.foma_identifier if s.kind == "named" else s.inline_text
                for s in oe_pipeline.stages()]
    sequences = models(original)
    definitions = prior.DEFINITIONS + resolution.EXTRA + EXTRA
    kernels = ("SNonHighSyn", "TNonHigh", "RLocal", "RPosttonic", "STradSyn")
    names = sorted({s for seq in sequences.values() for s in seq}
                   | set(kernels) | {"RPrevious", "RProductive"}
                   | {"RWhole" + str(i) for i in range(len(sequences))})
    recipe = dict(definitions=definitions, insert_after="", insert_rule="", replace={},
                  component_checks=[dict(component=name) for name in names])
    results, formal = {}, {}
    with tempfile.TemporaryDirectory(prefix="capr_lexical_") as temporary:
        directory = Path(temporary)
        image = prepare_definition_image(GERMANIC / "fsts/germanic.txt", directory)
        if image:
            os.environ["CAPR_FOMA_DEFINITION_IMAGE"] = str(image)
        parser_recipe = dict(recipe, component_checks=[
            dict(component=name) for name in ("RPrevious", "RInput")])
        bins = compile_isolated(GERMANIC / "fsts/germanic.txt", parser_recipe, [], directory,
                                components_only=True)
        previous_parses = batch_apply_down(bins["component:RPrevious"], inputs)
        repaired_parses = batch_apply_down(bins["component:RInput"], inputs)
        parser_evidence = dict(
            previous_ambiguities=[dict(index=i, input=inputs[i], outputs=values)
                                  for i, values in enumerate(previous_parses) if len(values) > 1],
            repaired_ambiguities=[dict(index=i, input=inputs[i], outputs=values)
                                  for i, values in enumerate(repaired_parses) if len(values) > 1])
        if parser_evidence["repaired_ambiguities"]:
            print(json.dumps(parser_evidence, ensure_ascii=False), file=sys.stderr, flush=True)
            raise RuntimeError("Productive parser remains ambiguous")
        for i, sequence in enumerate(sequences.values()):
            definitions += "\ndefine RWhole" + str(i) + " [" + " .o. ".join(sequence) + "];\n"
        recipe["definitions"] = definitions
        bins = compile_isolated(GERMANIC / "fsts/germanic.txt", recipe, [], directory,
                                components_only=True)
        production = batch_apply_down(canonical.bin_dir / "old_english.bin", inputs[:len(rows)])
        for i, (name, sequence) in enumerate(sequences.items()):
            print("model " + name, file=sys.stderr, flush=True)
            final, steps = prior.trace(sequence, bins, inputs)
            if final != batch_apply_down(bins["component:RWhole" + str(i)], inputs):
                raise RuntimeError("Whole/component disagreement: " + name)
            if i == 0:
                identity = final
                if final[:len(rows)] != production:
                    raise RuntimeError("Production/identity disagreement")
            offset = len(rows) + len(legacy)
            results[name] = dict(
                order=sequence, final=final,
                matched=sum(row["counterpart"] in values for row, values in zip(rows, final)),
                deltas=[dict(row_id=row["row_id"], concept=row["concept"], old=a, new=b)
                        for row, a, b in zip(rows, identity, final) if a != b],
                immutable380_deltas=[
                    dict(concept=row["concept"], input=row["proto_norm"], old=a, new=b)
                    for row, a, b in zip(legacy, identity[len(rows):offset],
                                         final[len(rows):offset]) if a != b],
                candidates={c["id"]: dict(**c, final=final[index])
                            for index, c in enumerate(candidates, offset)},
                transitions=[dict(stage=s["stage"], changes=[
                    dict(index=j, before=a, after=b)
                    for j, (a, b) in enumerate(zip(s["before"], s["after"])) if a != b])
                    for s in steps],
                candidate_traces={c["id"]: [
                    dict(stage=s["stage"], before=s["before"][j], after=s["after"][j])
                    for s in steps] for j, c in enumerate(candidates, offset)},
                composed_crosscheck=True,
                finite_ambiguity=[j for j, values in enumerate(final) if len(values) > 1])
        pairs = controls()
        component = {rule: dict(zip(pairs, batch_apply_down(
            bins["component:" + rule], [prior.star(p[0]) for p in pairs.values()])))
            for rule in kernels}
        for rule in (*kernels, *("RWhole" + str(i) for i in range(len(sequences)))):
            result = subprocess.run(
                ["foma", "-q", "-e", "load stack " + bins["component:" + rule].name,
                 "-e", "test functional", "-e", "quit"], cwd=directory,
                text=True, capture_output=True, check=True, timeout=120)
            formal[rule] = dict(stdout=result.stdout, stderr=result.stderr)
    after = {str(p): resolution.sha(p) for p in paths if p.is_file()}
    if protected != after:
        raise RuntimeError("Canonical files changed during experiment")
    report = dict(base=BASE, definitions=definitions, rows=rows, immutable380=legacy,
                  input_order=inputs, candidates=candidates, controls=pairs, models=results,
                  component=component, formal=formal, production_unchanged=True,
                  parser_evidence=parser_evidence,
                  protected_before=protected, protected_after=after,
                  runtime=subprocess.check_output(["foma", "-v"], text=True).strip())
    with gzip.open(output, "wt", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, sort_keys=True)


def launch(experiment_id):
    from adjudication_control import run_logged
    from experiment_snapshot import create_snapshot

    paths = sorted(set(
        list((GERMANIC / "tools").glob("*.py"))
        + list((GERMANIC / "data").glob("*.tsv"))
        + list((GERMANIC / "docs/sound_changes/cascade_baseline").glob("*.tsv"))
        + list((GERMANIC / "docs/sound_changes/cascade_baseline").glob("*.json"))
        + [GERMANIC / "fsts/germanic.txt", GERMANIC / "fsts/old_english_sandbox.txt",
           ROOT / "backend/oe_input_context.py", ROOT / "backend/compare_fst.py",
           Path(__file__), OLD_PATH, prior.HERE / "experiment.py",
           OLD_PATH.parent / "controls.json", HERE / "candidates.json",
           HERE / "preregistration.md"]))
    mapping = {f"file{i:03d}": str(p.relative_to(ROOT)) for i, p in enumerate(paths)}
    manifest = ROOT / ".capr-work/lexical-layout.json"
    manifest.write_text(json.dumps(mapping))
    inputs = {label: ROOT / relative for label, relative in mapping.items()}
    inputs["layout"] = manifest
    snapshot = create_snapshot(
        experiment_id, "Independently attested lexical cells and local nonhigh syncope",
        inputs, variants={"definitions": prior.DEFINITIONS + resolution.EXTRA + EXTRA},
        expected_outcomes={"question": "Classify all complete candidates and corpus deltas",
                           "preregistration": resolution.sha(HERE / "preregistration.md")},
        negative_controls=[key for key, (a, b) in controls().items() if a == b],
        environment={"runner": "private capr-soul-lexical backend", "base": BASE})
    evidence = ROOT / ".capr-work/lexical-snapshot.json"
    evidence.write_text(json.dumps({"snapshot_root": str(snapshot.root)}))
    subprocess.run([sys.executable, str(GERMANIC / "tools/adjudicate.py"),
                    "SC065", "--run", "advance", "SNAPSHOT", "--evidence", str(evidence)],
                   check=True)
    container = snapshot.stage_in_container()
    bootstrap = """
import json,shutil,sys,tempfile,subprocess
from pathlib import Path
src=Path(sys.argv[1]); layout=json.loads((src/'layout.json').read_text())
root=Path(tempfile.mkdtemp(prefix='capr_lexical_source_'))
try:
    for label,relative in layout.items():
        files=list(src.glob(label+'.*'))
        if len(files)!=1: raise RuntimeError(label)
        dest=root/relative; dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(files[0],dest)
    for name in ('compare_fst.py','oe_input_context.py'):
        shutil.copyfile(root/'backend'/name,root/'Germanic'/name)
    worker=root/'Germanic/docs/sound_changes/audits/soul-lexical-reassessment/experiment.py'
    subprocess.run(['python3',str(worker),'--worker','--output',sys.argv[2]],check=True)
finally:
    shutil.rmtree(root)
"""
    destination = container + "/../" + experiment_id + "-results.json.gz"
    receipt = run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", "-c",
         bootstrap, container, destination], label="lexical-comparison",
        log_dir=snapshot.staging_dir)
    if receipt["ok"]:
        subprocess.run(["docker", "compose", "cp", "backend:" + destination,
                        str(snapshot.staging_dir / "results.json.gz")], check=True)
    snapshot.complete("passed" if receipt["ok"] else "failed",
                      "Execution only; not scientific adoption",
                      command_receipts=[receipt])
    (snapshot.root / "staging").symlink_to("results", target_is_directory=True)
    print(snapshot.root)
    if not receipt["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--experiment-id")
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.worker:
        worker(args.output)
    elif args.experiment_id:
        launch(args.experiment_id)
    else:
        parser.error("--experiment-id or --worker is required")

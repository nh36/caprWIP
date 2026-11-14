"""Test whether the apparent genitive-plural success depends on a vowel-class gap."""
import ast
import json
from pathlib import Path
import subprocess
import sys


def main():
    root = Path.cwd()
    sys.path.insert(0, str(root / "Germanic/tools"))
    import experiment_snapshot
    from adjudication_control import run_logged
    from executable_facts import parse_defines

    previous = experiment_snapshot.Snapshot(
        root / ".capr-work/experiments/flask-genpl-77f314bf-v1")
    previous.verify()
    payload = json.loads(previous.input_path("payload").read_text())
    source = previous.input_path("source")
    body = parse_defines(source.read_text())["OENonHighSyn"].body
    old = "_ OEAnyConsonant EnglishStarVocalic\n"
    assert body.count(old) == 1
    repaired = body.replace(old, "_ OEAnyConsonant [EnglishStarVocalic|{*ô}]\n")
    order = list(payload["order"])
    order[order.index("OENonHighSyn")] = "GPNHS"
    payload["order"] = order
    payload["variant"] = "recognize-following-trimoric-carrier"
    for label, value in (("flask", "flaskana"), ("tongue", "tungana"), ("guma", "gumana")):
        payload["probes"].append({
            "id": label + "-analogical-ana-after-syncope",
            "entry": "*" + "*".join(value), "before": "OEEarlyOShortening",
            "status": "Explicit post-syncope restoration diagnostic; supplying -ana presupposes analogy, not a regular inherited derivation.",
            "source": "RingeTaylor2014 pp153–154; later -ana > -ena is Campbell1959 pp158–159 §385, not independently dated by this model-boundary run.",
        })
    base_driver = previous.input_path("driver")
    worker = next(ast.literal_eval(n.value) for n in ast.parse(base_driver.read_text()).body
                  if isinstance(n, ast.Assign) and any(
                      isinstance(t, ast.Name) and t.id == "WORKER" for t in n.targets))
    worker = worker.replace("assert finals==canonical", "assert len(finals)==len(canonical)")
    worker = worker.replace(
        'assert sum(f==[r["counterpart"]] for r,f in zip(p["rows"],finals))==385',
        'matches=sum(f==[r["counterpart"]] for r,f in zip(p["rows"],finals))')
    worker = worker.replace(
        'result={"reference_sha":p["reference_sha"],"order":order,',
        'result={"reference_sha":p["reference_sha"],"order":order,"matches":matches,'
        '"changed":[{"id":r["id"],"concept":r["concept"],"before":b,"after":f}'
        ' for r,b,f in zip(p["rows"],canonical,finals) if b!=f],')
    ast.parse(worker)
    work = root / ".capr-work/flask-genitive-plural-77f314bf/syncope-carrier"
    work.mkdir(exist_ok=True)
    recipe = {"id": "genitive-plural-carrier", "replace": {}, "insert_rule": None,
              "insert_after": None, "definitions": "define GPNHS " + repaired + ";",
              "component_checks": [{"component": s} for s in dict.fromkeys(order)]}
    for name, value in (("recipe.json", recipe), ("payload.json", payload)):
        (work / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    snapshot = experiment_snapshot.create_snapshot(
        "flask-genpl-carrier-77f314bf-v1",
        "Sensitivity test: a trimoric origin carrier must count as the following vowel in ordinary syncope; not a new historical SC114 adjudication.",
        {"source": source, "driver": Path(__file__).resolve(), "base_driver": base_driver,
         "recipe": work / "recipe.json", "payload": work / "payload.json",
         "pipeline": previous.input_path("pipeline"),
         "compiler": previous.input_path("compiler"),
         "corpus": previous.input_path("corpus"),
         "contexts": previous.input_path("contexts")},
        variants={"recognize-following-trimoric-carrier": " .o. ".join(order)},
        probes=payload["probes"],
        expected_outcomes={"measure": "All394 delta and genitive-plural sensitivity; do not assume target agreement."},
        negative_controls=["guma", "tunge", "No production adoption or baseline migration"])
    compiled = snapshot.compile_isolated("source", "recipe", components_only=True)
    output = compiled["container_output"] + "/carrier-results.json"
    execution = run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", "-u", "-c",
         worker, compiled["container_source"] + "/" + snapshot.input_path("payload").name,
         json.dumps(compiled["bins"]), output],
        label="genitive-plural-trimoric-syncope", log_dir=snapshot.staging_dir)
    if not execution["ok"]:
        raise RuntimeError(Path(execution["stderr_log"]).read_text())
    stdout = Path(execution["stdout_log"]).read_text()
    subprocess.run(["docker", "compose", "cp", "backend:" + output,
                    str(snapshot.staging_dir / "observed.json")], check=True)
    snapshot.complete("passed", "Actual diagnostic sensitivity and complete394 delta measured; no production adoption.",
                      [compiled["receipt"], execution])
    (work / "observed.json").write_text((snapshot.results_dir / "observed.json").read_text())
    observed = json.loads((work / "observed.json").read_text())
    print("MATCHES", observed["matches"], "CORPUS DELTA", observed["changed"])
    print(stdout)


if __name__ == "__main__":
    main()

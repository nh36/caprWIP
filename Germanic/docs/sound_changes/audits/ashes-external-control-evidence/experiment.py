"""Two external nouns, three root treatments, unchanged SC051 timing."""
import json
from pathlib import Path
import subprocess
import sys

REFERENCE = "5df7b9daef1a4da88abba30f0c9681c8e91d9a36"
PREDICTIONS = {
    "class_assumption": (
        "EWA supplies *askōn-, not a complete nominative. *áskōn is CAPR's "
        "weak-feminine citation encoding, parallel to selected *fláskōn; "
        "the shared later *-ā follows the class hypothesis, not a quoted EWA form."
    ),
    "categorical_narrow_rule": (
        "Both roots must remain/become a before *sk plus final *ā. "
        "A secure front-root nominative in that environment requires a further account."
    ),
    "wright_section_57": (
        "The published back-vowel condition includes sc, st and certain geminates; "
        "it explicitly acknowledges æsce beside asce. Do not equate it with "
        "an exception-free assertion that no front-root ashes form exists."
    ),
    "levelling": (
        "Back-root obliques can supply donors, but their existence alone does not "
        "establish direction; front-root inflected æscan must also be accounted for."
    ),
    "controls": (
        "Original production SC051 and its timing are identical in all trials. "
        "No context guard, early palatalization, corpus change or analogy is added."
    ),
}
WORKER = r'''
import hashlib,json,sys
from pathlib import Path
sys.path.insert(0,"/usr/app/tools")
from sound_change_order_sensitivity import batch_apply_down
from oe_pipeline import normalize_proto
p=json.loads(Path(sys.argv[1]).read_text())
bins={k.removeprefix("component:"):Path(v) for k,v in json.loads(sys.argv[2]).items()}
def trace(order,form):
    states=[form];history=[]
    for stage in order:
        after=sorted({y for xs in batch_apply_down(bins[stage],states) for y in xs})
        history.append({"stage":stage,"before":states,"after":after})
        states=after
        if not states or states==["+?"]:
            break
    return {"output":states,"trace":history}
result={"reference_sha":p["reference_sha"],"predictions":p["predictions"],
        "binary_sha256":{k:hashlib.sha256(v.read_bytes()).hexdigest() for k,v in bins.items()},
        "variants":{}}
for variant,order in p["orders"].items():
    result["variants"][variant]={}
    for noun,raw,tokenized in [
        ("ashes","*áskōn","*á*s*k*ō*n"),
        ("flask","*fláskōn","*f*l*á*s*k*ō*n")]:
        normalized=normalize_proto(raw)
        normal=trace(order,normalized)
        diagnostic=trace(order[1:],tokenized)
        assert all(len(s["after"])==1 and s["after"]!=["+?"] for s in diagnostic["trace"])
        if normal["output"]:
            assert normal["output"]==diagnostic["output"]
        result["variants"][variant][noun]={
            "raw":raw,"normalized_raw_input":normalized,"normal_entry":normal,
            "diagnostic_entry":"immediately after EnglishProtoInput",
            "tokenized_input":tokenized,"post_tokenization_diagnostic":diagnostic}
Path(sys.argv[3]).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({v:{n:{"normal":d["normal_entry"]["output"],
    "diagnostic":d["post_tokenization_diagnostic"]["output"]} for n,d in ns.items()}
    for v,ns in result["variants"].items()},ensure_ascii=False,indent=2))
'''


def main():
    root = Path.cwd()
    sys.path.insert(0, str(root / "Germanic/tools"))
    import experiment_snapshot
    from adjudication_control import run_logged
    import oe_pipeline
    work = root / ".capr-work/ashes-control-5df7b9da"
    work.mkdir(parents=True, exist_ok=True)
    source = work / "reference.txt"
    source.write_bytes(subprocess.check_output([
        "git", "show", REFERENCE + ":Germanic/fsts/germanic.txt"]))
    assert source.read_bytes() == (root / "Germanic/fsts/germanic.txt").read_bytes()
    original = [s.inline_text if s.kind == "inline" else s.foma_identifier
                for s in oe_pipeline.stages()]
    pipeline = root / "Germanic/tools/oe_pipeline.py"
    assert pipeline.read_bytes() == subprocess.check_output([
        "git", "show", REFERENCE + ":Germanic/tools/oe_pipeline.py"])
    assert original[0] == "EnglishProtoInput"
    orders = {"baseline": original}
    retain = list(original)
    retain[retain.index("EAFBrightening")] = "AGHold"
    orders["retain"] = retain
    retract = list(original)
    retract.insert(retract.index("EAFBrighteningLongFinal"), "AGRet")
    orders["retract"] = retract
    recipe = {
        "id": "ashes-root-only", "replace": {}, "insert_rule": None, "insert_after": None,
        "definitions": (
            "define AGHold Ctx([[{*á} -> {*a} || _ {*s} {*k} {*ā} .#.] "
            ".o. EAFBrighteningStressed]);\n"
            "define AGRet FootCtx([{*æ} -> {*a} || _ {*s} {*k} {*ā} .#.]);"
        ),
        "component_checks": [{"component": s} for s in dict.fromkeys(
            s for order in orders.values() for s in order)],
    }
    payload = {"reference_sha": REFERENCE, "orders": orders, "predictions": PREDICTIONS}
    for name, value in (("recipe.json", recipe), ("payload.json", payload)):
        (work / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    snapshot = experiment_snapshot.create_snapshot(
        "ashes-root-only-5df7b9da-v3",
        "External ashes control: raw entry and labelled post-tokenization diagnostics; fixed SC051.",
        {"source": source, "driver": Path(__file__).resolve(), "recipe": work / "recipe.json",
         "payload": work / "payload.json", "pipeline": root / "Germanic/tools/oe_pipeline.py",
         "compiler": root / "Germanic/tools/anglo_frisian_experiments.py"},
        variants={k: " .o. ".join(v) for k, v in orders.items()},
        probes=[{"id": "ashes", "input": "*áskōn"}, {"id": "flask", "input": "*fláskōn"}],
        expected_outcomes=PREDICTIONS, negative_controls=["unchanged SC051 and timing"])
    prior_root = root / ".capr-work/experiments/ashes-root-only-5df7b9da"
    if prior_root.is_dir():
        prior = experiment_snapshot.load_snapshot("ashes-root-only-5df7b9da")
        prior.verify()
        for label in ("source", "recipe", "payload", "pipeline", "compiler"):
            assert prior.input_path(label).read_bytes() == snapshot.input_path(label).read_bytes()
        receipt_root = prior.results_dir if prior.is_complete() else prior.staging_dir
        compile_receipt = json.loads(next(receipt_root.glob("isolated-compile-*.receipt.json")).read_text())
        assert compile_receipt["ok"]
        log = next(receipt_root.glob("isolated-compile-*.stdout.log"))
        import hashlib
        assert hashlib.sha256(log.read_bytes()).hexdigest() == compile_receipt["stdout_sha256"]
        bins = json.loads(log.read_text())
        if not prior.is_complete():
            prior.complete("failed", "Harness confused an empty rejection with an accepted raw form.")
        compiled = {"receipt": compile_receipt, "bins": bins,
                    "container_source": snapshot.stage_in_container(),
                    "container_output": str(Path(next(iter(bins.values()))).parent)}
    else:
        compiled = snapshot.compile_isolated("source", "recipe", components_only=True)
    output = compiled["container_output"] + "/observed.json"
    receipt = run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", "-u", "-c", WORKER,
         compiled["container_source"] + "/" + snapshot.input_path("payload").name,
         json.dumps(compiled["bins"]), output],
        label="ashes-three-root-treatments", log_dir=snapshot.staging_dir)
    if not receipt["ok"]:
        raise RuntimeError(Path(receipt["stderr_log"]).read_text())
    subprocess.run(["docker", "compose", "cp", "backend:" + output,
                    str(snapshot.staging_dir / "observed.json")], check=True)
    stdout = Path(receipt["stdout_log"]).read_text()
    snapshot.complete("passed", "Measured external probes only; no production adoption.",
                      [compiled["receipt"], receipt])
    target = Path(__file__).resolve().parent
    observed = json.loads((snapshot.results_dir / "observed.json").read_text())
    checkpoints = {
        "EnglishProtoInput", "PNWGmcNStemNLoss", "PWGmcSurvivingBimoricOUnrounding",
        "EAFBrightening", "AGHold", "AGRet", "EAFBrighteningLongFinal",
        "OEARestoration", "OESkPalatalization",
    }
    for nouns in observed["variants"].values():
        for noun in nouns.values():
            for entry in ("normal_entry", "post_tokenization_diagnostic"):
                history = noun[entry]["trace"]
                noun[entry]["trace"] = [
                    s for s in history
                    if s["stage"] in checkpoints or s["before"] != s["after"] or s is history[-1]]
    observed["trace_policy"] = "Changed relations plus named checkpoints and final; full history in sealed snapshot."
    (target / "observed.json").write_text(json.dumps(observed, ensure_ascii=False, indent=2) + "\n")
    print(stdout)


if __name__ == "__main__":
    main()

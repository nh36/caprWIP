"""Compare attested genitive plurals without changing the reference cascade."""
import json
from pathlib import Path
import subprocess
import sys

REFERENCE = "77f314bf85035c23706b6b09b3a1855aa23c0620"
WORKER = r'''
import hashlib,json,sys
from pathlib import Path
sys.path.insert(0,"/usr/app/tools")
from sound_change_order_sensitivity import batch_apply_down
from capr_runtime import layout,check_build_manifest
import oe_pipeline
p=json.loads(Path(sys.argv[1]).read_text())
bins={k.removeprefix("component:"):Path(v) for k,v in json.loads(sys.argv[2]).items()}
out=Path(sys.argv[3])
rt=layout()
assert not check_build_manifest(oe_pipeline.expected_snapshot_bins()+["old_english.bin"])
protected=[rt.germanic_fst,rt.corpus_tsv,rt.build_manifest]
protected.extend(q for q in (rt.docs_dir/"sound_changes/cascade_baseline").iterdir() if q.is_file())
before={str(q):hashlib.sha256(q.read_bytes()).hexdigest() for q in protected}
def trace(order,forms):
    states=[[f] for f in forms];histories=[[] for _ in forms]
    for stage in order:
        flat=[x for group in states for x in group]
        applied=iter(batch_apply_down(bins[stage],flat) if flat else [])
        result=[]
        for i,group in enumerate(states):
            after=sorted({x for _ in group for x in next(applied)})
            histories[i].append({"stage":stage,"before":group,"after":after})
            result.append(after)
        states=result
    return states,histories
order=p["order"]
forms=[r["fst_input"] for r in p["rows"]]
finals,histories=trace(order,forms)
canonical=batch_apply_down(rt.bin_dir/"old_english.bin",forms)
assert finals==canonical
assert len(finals)==394 and all(len(s["after"])==1 for h in histories for s in h)
assert sum(f==[r["counterpart"]] for r,f in zip(p["rows"],finals))==385
result={"reference_sha":p["reference_sha"],"order":order,
        "corpus":[{**r,"output":f} for r,f in zip(p["rows"],finals)],
        "protected_before":before,"probes":[]}
for probe in p["probes"]:
    q=dict(probe)
    if "raw" in q:
        f,h=trace(order,[q["raw"]])
        assert f[0]==batch_apply_down(rt.bin_dir/"old_english.bin",[q["raw"]])[0]
        q["raw_output"],q["raw_trace"]=f[0],h[0]
    if "entry" in q:
        f,h=trace(order[order.index(q["before"]):],[q["entry"]])
        q["diagnostic_output"],q["diagnostic_trace"]=f[0],h[0]
        q["diagnostic_singleton"]=all(len(s["after"])==1 for s in h[0])
    result["probes"].append(q)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(q["id"],"raw",q.get("raw_output"),"diagnostic",q.get("diagnostic_output"),flush=True)
after={q:hashlib.sha256(Path(q).read_bytes()).hexdigest() for q in before}
assert before==after
result["protected_after"]=after
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
'''


def main():
    root = Path.cwd()
    sys.path.insert(0, str(root / "Germanic/tools"))
    import experiment_snapshot
    from adjudication_control import run_logged
    from anglo_frisian_experiments import corpus_rows
    from executable_facts import parse_defines
    import oe_pipeline

    work = root / ".capr-work/flask-genitive-plural-77f314bf"
    work.mkdir(exist_ok=True)
    source = work / "reference.txt"
    source.write_bytes(subprocess.check_output([
        "git", "show", REFERENCE + ":Germanic/fsts/germanic.txt"]))
    frozen_defines = parse_defines(source.read_text())
    current_defines = parse_defines((root / "Germanic/fsts/germanic.txt").read_text())
    assert {k: v.body for k, v in frozen_defines.items()} == {
        k: v.body for k, v in current_defines.items()}
    for path in ("Germanic/tools/oe_pipeline.py",
                 "Germanic/tools/anglo_frisian_experiments.py",
                 "Germanic/data/germanic-aligned-final.tsv",
                 "Germanic/data/entry_context_metadata.tsv"):
        assert (root / path).read_bytes() == subprocess.check_output([
            "git", "show", REFERENCE + ":" + path]), path
    order = [s.inline_text if s.kind == "inline" else s.foma_identifier
             for s in oe_pipeline.stages()]
    probes = []
    for label, stem in [
        ("flask-inherited-feminine", "fláskōn"),
        ("tongue-inherited-feminine", "túngōn"),
        ("guma-inherited-masculine", "gúman"),
        ("flask-masculine-source", "fláskan"),
        ("tongue-masculine-source", "túngan"),
    ]:
        probes.append({
            "id": label + "-nasal-trimoric-raw",
            "raw": stem + "ǭ\u0304",
            "status": "Complete nasal trimoric gen.pl.; no unsupported multi-codepoint Foma token is invented.",
            "source": "Ringe2017 p313; replacing feminine stem vowel is the explicit masculine-source hypothesis.",
        })
        for ending, tag in [("ô", "trimoric-shadow"), ("ō", "literal-pwgmc-long-o")]:
            value = stem + ending
            probes.append({
                "id": label + "-" + tag,
                "raw": value,
                "entry": "*" + "*".join(value),
                "before": "PWGmcSurvivingBimoricOUnrounding",
                "status": (
                    "Named-boundary diagnostic, not inherited raw-entry success. "
                    + ("ô preserves inherited trimoric origin after denasalization; this is a quantity-shadow encoding, not literal PWGmc phonetics."
                       if ending == "ô" else
                       "Literal PWGmc ō spelling; tests loss of inherited quantity provenance at the early merger.")
                ),
                "source": "RingeTaylor2014 pp59,153–154; flask forms are class extrapolations.",
            })
        value = stem + "ô"
        probes.append({
            "id": label + "-trimoric-after-tokenizer",
            "entry": "*" + "*".join(value),
            "before": "PGmcGmSimplification",
            "status": "Post-tokenizer quantity-shadow diagnostic; supplying denasalized ô is not a full PGmc nasal-vowel derivation.",
            "source": "Ringe2017 p313; RingeTaylor2014 p59.",
        })
    for label, value in [
        ("flask-fronted-medial", "flaskæna"),
        ("tongue-fronted-medial", "tungæna"),
        ("guma-fronted-medial", "gumæna"),
        ("flask-restored-a", "flaskana"),
        ("tongue-restored-a", "tungana"),
        ("guma-restored-a", "gumana"),
    ]:
        probes.append({
            "id": label,
            "entry": "*" + "*".join(value),
            "before": "OEWeightMarkers",
            "status": "Late-intermediate diagnostic: not a transponent adoption or complete inherited derivation.",
            "source": "RingeTaylor2014 pp153–154: regular medial æ, syncope, analogical -ana and later -ena; flask is a class extrapolation.",
        })
    payload = {"reference_sha": REFERENCE, "order": order, "probes": probes,
               "rows": corpus_rows(root / "Germanic/data/germanic-aligned-final.tsv")}
    recipe = {"id": "flask-genitive-plural", "replace": {}, "insert_rule": None,
              "insert_after": None, "definitions": "",
              "component_checks": [{"component": s} for s in dict.fromkeys(order)]}
    for name, value in (("recipe.json", recipe), ("payload.json", payload)):
        (work / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    snapshot = experiment_snapshot.create_snapshot(
        "flask-genpl-77f314bf-v1",
        "After completed SC051 comparison, distinguish inherited feminine genitive plural from the masculine-source ending with tunge and inherited guma controls.",
        {"source": source, "driver": Path(__file__).resolve(),
         "recipe": work / "recipe.json", "payload": work / "payload.json",
         "corpus": root / "Germanic/data/germanic-aligned-final.tsv",
         "contexts": root / "Germanic/data/entry_context_metadata.tsv",
         "pipeline": root / "Germanic/tools/oe_pipeline.py",
         "compiler": root / "Germanic/tools/anglo_frisian_experiments.py"},
        variants={"reference": " .o. ".join(order)}, probes=probes,
        expected_outcomes={"measure": "Do not assume genitive-plural success; preserve all394 reference outputs."},
        negative_controls=["No nasal bimoric/trimoric conflation", "No gender-conditioned sound law",
                           "No production input, comparator, baseline or SC051 adoption"])
    compiled = snapshot.compile_isolated("source", "recipe", components_only=True)
    output = compiled["container_output"] + "/genpl-results.json"
    execution = run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", "-u", "-c",
         WORKER, compiled["container_source"] + "/" + snapshot.input_path("payload").name,
         json.dumps(compiled["bins"]), output],
        label="flask-genitive-plural", log_dir=snapshot.staging_dir)
    if not execution["ok"]:
        raise RuntimeError(Path(execution["stderr_log"]).read_text())
    stdout = Path(execution["stdout_log"]).read_text()
    subprocess.run(["docker", "compose", "cp", "backend:" + output,
                    str(snapshot.staging_dir / "observed.json")], check=True)
    snapshot.complete("passed", "All actual inherited and late diagnostic results measured; no production adoption.",
                      [compiled["receipt"], execution])
    (work / "observed.json").write_text((snapshot.results_dir / "observed.json").read_text())
    print(stdout)


if __name__ == "__main__":
    main()

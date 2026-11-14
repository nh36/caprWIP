"""Attested Flask cells and a phonological final-n late-shortening test."""
import argparse
import csv
import json
from pathlib import Path
import runpy
import subprocess
import sys

REFERENCE = "a829dfcb4a80eac9113ac473e06258edd7285002"
RAW = {
    "flask_nomsg": "*fláskōn",
    "flask_nompl": "*fláskōniz",
    "flask_accsg": "*fláskōnų",
    "flask_datsg": "*fláskōni",
    "flask_accpl_inherited": "*fláskōnunz",
    "flask_datpl_unattested": "*fláskōmaz",
    "tongue_nompl": "*túngōniz",
    "tongue_nomsg": "*túngōn",
    "tongue_accsg": "*túngōnų",
    "tongue_accpl_inherited": "*túngōnunz",
    "tongue_datpl": "*túngōmaz",
    "do_secondary_n": "*dōną",
    "bears_late_mechanism": "*búrōθi",
    "foldu_accsg_conditional": "*fúldōnų",
    "eorthu_accsg_conditional": "*érθōnų",
}
EXTRA = """
define FLEarly Ctx([
    {*ō} -> {*a} ||
    EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _
    [{*m} | {*n} ContextSegments]
]);
"""
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
        if not states:break
        assert len(states)==1 and states!=["+?"], (stage,states)
    return {"output":states,"trace":history}
result={"reference_sha":p["reference_sha"],"orders":p["orders"],
        "binary_sha256":{k:hashlib.sha256(v.read_bytes()).hexdigest() for k,v in bins.items()},
        "production":dict(p["reused_production"]),"variants":{},"stage_entries":{}}
for name,raw in p["raw"].items():
    if name not in result["production"]:
        normal=trace(p["orders"]["production"],normalize_proto(raw))
        record={"raw":raw,"normal_entry":normal,"provenance":"fresh"}
        if not normal["output"]:
            record["after_gateway_diagnostic"]=trace(
                p["orders"]["production"][1:],"*"+"*".join(normalize_proto(raw)))
        result["production"][name]=record
for variant,order in p["orders"].items():
    if variant=="production":continue
    result["variants"][variant]={}
    for name,raw in p["raw"].items():
        normal=trace(order,normalize_proto(raw))
        assert normal["trace"][0]["after"]==["*"+"*".join(normalize_proto(raw))]
        result["variants"][variant][name]={"raw":raw,"normal_entry":normal}
    result["stage_entries"][variant]={}
    for name,form in p["raised_entries"].items():
        tail=order[order.index("OEMedLongShort"):]
        result["stage_entries"][variant][name]={
            "entry":form,"before":"OEMedLongShort",
            "status":"Post-raising diagnostic, not PGmc normal entry.",
            **trace(tail,form)}
assert result["variants"]["protected_n"]["flask_nompl"]["normal_entry"]["output"]==["flascen"]
Path(sys.argv[3]).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({v:{n:r["normal_entry"]["output"] for n,r in rs.items()}
                 for v,rs in result["variants"].items()},ensure_ascii=False))
'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot-id", default="flask-cells-a829dfcb-v1")
    args = parser.parse_args()
    root = Path.cwd()
    sys.path.insert(0, str(root / "Germanic/tools"))
    import experiment_snapshot
    import oe_pipeline
    from adjudication_control import run_logged

    audits = Path(__file__).resolve().parent.parent
    previous_driver = audits / "flask-nominative-plural-evidence/experiment.py"
    previous = runpy.run_path(str(previous_driver))
    old_evidence = audits / "flask-nominative-plural-evidence/observed.json"
    old = json.loads(old_evidence.read_text())
    source_path = root / "Germanic/fsts/germanic.txt"
    pipeline = root / "Germanic/tools/oe_pipeline.py"
    for sha in (REFERENCE, old["reference_sha"]):
        for path in (source_path, pipeline):
            assert path.read_bytes() == subprocess.check_output(
                ["git", "show", sha + ":" + str(path.relative_to(root))])
    # Older cell ledgers differ only in a dated, non-executable comment.
    for path in (source_path, pipeline):
        earlier = subprocess.check_output(
            ["git", "show", "77f314bf:" + str(path.relative_to(root))], text=True)
        without_comments = lambda text: "\n".join(
            line for line in text.splitlines() if not line.lstrip().startswith("#"))
        assert without_comments(earlier) == without_comments(path.read_text())

    original = [s.inline_text if s.kind == "inline" else s.foma_identifier
                for s in oe_pipeline.stages()]
    protected = list(original)
    protected[0] = "FPGateway"
    protected.remove("PNWGmcNStemNLoss")
    protected.insert(protected.index("PWGmcEarlyIApocope"), "PNWGmcNStemNLoss")
    late = ["FLEarly" if s == "OEEarlyOShortening" else s for s in protected]
    orders = {"production": original, "protected_n": protected, "late_final_n": late}
    definitions = previous["DEFINITIONS"].replace(
        "define FPTails [",
        "define FPTails [ ō:{*ō} n:{*n} u:{*u} n:{*n} z:{*z} |") + EXTRA
    reused = {}
    for name in RAW:
        if name in old["variants"]["production"]:
            reused[name] = {**old["variants"]["production"][name],
                            "provenance": str(old_evidence.relative_to(root)),
                            "tested_reference": old["reference_sha"]}
    original_dir = audits / "flask-inherited-paradigm-evidence"
    original_probes = list(csv.DictReader(
        (original_dir / "probes.tsv").read_text().splitlines(), delimiter="\t"))
    original_traces = list(csv.DictReader(
        (original_dir / "stage_traces.tsv").read_text().splitlines(), delimiter="\t"))
    for name, label in (("flask_datsg", "flásk-datsg"),
                        ("flask_datpl_unattested", "flásk-datpl")):
        row = next(r for r in original_probes if r["variant"] == "identity" and r["probe"] == label)
        history = [{"stage":r["stage"],"before":r["before"].split(" | ") if r["before"] else [],
                    "after":r["after"].split(" | ") if r["after"] else []}
                   for r in original_traces if r["variant"] == "identity"
                   and r["probe"] == label and r["route"] == "diagnostic"]
        reused[name] = {
            "raw":RAW[name],"normal_entry":{"output":[]},
            "after_gateway_diagnostic":{"output":[row["diagnostic_output"]],"trace":history},
            "provenance":str((original_dir / "probes.tsv").relative_to(root)),
            "tested_reference":"2805d98ae5ecf7df33c65dc0caf7d9df2ed22077"}

    payload = {"reference_sha":REFERENCE,"orders":orders,"raw":RAW,
               "reused_production":reused,
               "raised_entries":{"foldu":"*f*ó*l*d*ū*n*ų","eorthu":"*éo*r*θ*ū*n*ų"}}
    components = list(dict.fromkeys(s for order in orders.values() for s in order))
    recipe = {"id":"flask-cells","replace":{},"insert_rule":None,"insert_after":None,
              "definitions":definitions,
              "component_checks":[{"component":s} for s in components]}
    work = root / ".capr-work/flask-cells-a829dfcb"
    work.mkdir(parents=True, exist_ok=True)
    for name, value in (("payload.json", payload), ("recipe.json", recipe)):
        (work / name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+"\n")
    snapshot = experiment_snapshot.create_snapshot(
        args.snapshot_id, "Attested cells and final-n exemption from early shortening.",
        {"source":source_path,"pipeline":pipeline,"driver":Path(__file__).resolve(),
         "previous_driver":previous_driver,"reused_evidence":old_evidence,
         "old_probes":original_dir / "probes.tsv","old_traces":original_dir / "stage_traces.tsv",
         "payload":work / "payload.json","recipe":work / "recipe.json",
         "predictions":audits / "flask-attested-cells-late-ending.md"},
        variants={k:" .o. ".join(v) for k,v in orders.items()},
        probes=[{"id":k,"input":v} for k,v in RAW.items()],
        expected_outcomes={"control":"flascen","hypothesis":"late ō > o > a"},
        negative_controls=["tunge","dōn","pre-m raising distinct","SC051 fixed"])
    compiled = snapshot.compile_isolated("source","recipe",components_only=True)
    output = compiled["container_output"] + "/observed.json"
    receipt = run_logged(
        ["docker","compose","exec","-T","backend","python3","-u","-c",WORKER,
         compiled["container_source"]+"/"+snapshot.input_path("payload").name,
         json.dumps(compiled["bins"]),output],
        label="flask-cells-focused",log_dir=snapshot.staging_dir)
    if not receipt["ok"]:
        snapshot.complete("failed","Focused worker failed.",[compiled["receipt"],receipt])
        raise RuntimeError("Inspect the sealed focused-worker stderr log.")
    subprocess.run(["docker","compose","cp","backend:"+output,
                    str(snapshot.staging_dir / "observed.json")],check=True)
    snapshot.complete("passed","Measured cell and late-route experiments; no adoption.",
                      [compiled["receipt"],receipt])
    result = json.loads((snapshot.results_dir / "observed.json").read_text())
    (Path(__file__).resolve().parent / "observed.json").write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print((snapshot.results_dir / Path(receipt["stdout_log"]).name).read_text())


if __name__ == "__main__":
    main()

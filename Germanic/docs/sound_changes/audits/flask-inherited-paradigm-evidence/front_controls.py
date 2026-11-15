"""Attested medial-sk structures, not asserted PGmc whole-word reconstructions."""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import adjudication_control as control
import experiment_snapshot

WORKER = r'''
import hashlib,json,sys
from pathlib import Path
sys.path.insert(0,"/usr/app/tools")
from sound_change_order_sensitivity import batch_apply_down
bins={k.removeprefix("component:"):Path(v) for k,v in json.loads(sys.argv[1]).items()}
payload=json.loads(sys.argv[2])
controls=[("*w*a*s*k*e","wasċe"),("*θ*e*r*s*k*e","þersċe"),
          ("*d*i*s*k*e*s","disċes"),("*d*i*s*k*a*s","discas")]
before={k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in bins.items()}
result={"reference_sha":payload["reference_sha"],
        "status":"Post-fronting structural diagnostics; no inherited-cell or early-e claim",
        "controls":{},"bin_hashes":before}
for variant,order in payload["orders"].items():
    stage=("AFSkF" if "AFSkF" in order else
           "OESkPalatalization" if variant=="whole_sk_negative" else
           "EAFBrighteningLongFinal")
    values=[x[0] for x in controls];traces=[[] for x in controls]
    for rule in order[order.index(stage):]:
        after=batch_apply_down(bins[rule],values)
        assert all(len(x)==1 and x[0]!="+?" for x in after),(variant,rule,after)
        for i,x in enumerate(after):
            traces[i].append({"stage":rule,"before":values[i],"after":x[0]})
        values=[x[0] for x in after]
    result["controls"][variant]=[
        {"input":x,"expected":e,"observed":v,"agrees":v==e,
         "before":stage,"trace":t}
        for (x,e),v,t in zip(controls,values,traces)]
assert before=={k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in bins.items()}
Path(sys.argv[3]).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({k:[(x["expected"],x["observed"]) for x in v]
                  for k,v in result["controls"].items()},ensure_ascii=False))
'''

work = ROOT / ".capr-work/flask-research"
compiled = json.loads((work / "compile.json").read_text())
payload = json.loads((work / "payload.json").read_text())
payload = {k: payload[k] for k in ("reference_sha", "orders")}
snapshot = experiment_snapshot.create_snapshot(
    "flask-front-controls-2805d98a-v3",
    "Source-backed medial structures distinguish low-front triggers and back-vowel negatives.",
    {"driver": Path(__file__).resolve(), "compiled": work / "compile.json",
     "payload": work / "payload.json", "source": ROOT / "Germanic/fsts/germanic.txt"},
    variants={k: " .o. ".join(v) for k, v in payload["orders"].items()},
    probes=["wasċe", "þersċe", "disċes", "discas"],
    expected_outcomes={"phonological_targets": ["wasċe", "þersċe", "disċes", "discas"]},
    negative_controls=["high-only trigger", "discas before back a"])
output = compiled["container_output"] + "/front-controls.json"
receipt = control.run_logged(
    ["docker", "compose", "exec", "-T", "backend", "python3", "-c", WORKER,
     json.dumps(compiled["bins"]), json.dumps(payload), output],
    label="flask-front-controls", log_dir=snapshot.staging_dir)
if not receipt["ok"]:
    raise RuntimeError(Path(receipt["stderr_log"]).read_text())
subprocess.run(["docker", "compose", "cp", "backend:" + output,
                str(snapshot.staging_dir / "observed.json")], check=True)
stdout = Path(receipt["stdout_log"]).read_text()
snapshot.complete("passed", "Observed agreements and counterexamples preserved without promotion.",
                  [receipt])
(work / "front-controls.json").write_text(
    (snapshot.results_dir / "observed.json").read_text())
print(stdout)

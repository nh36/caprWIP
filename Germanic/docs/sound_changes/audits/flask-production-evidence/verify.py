"""Verify freshly compiled production against the frozen Flask experiment."""
import json
from pathlib import Path
import shlex
import sys

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from adjudication_control import runtime_lock
from capr_runtime import run_in_runner

WORKER = r'''
import hashlib,json,sys
from pathlib import Path
sys.path.insert(0,"/usr/app/tools")
from capr_runtime import check_build_manifest,layout
from cascade_baseline import build_baseline
from oe_pipeline import stages
from sound_change_order_sensitivity import batch_apply_down
p=json.load(sys.stdin)
rt=layout()
ss=stages()
assert not check_build_manifest([s.snapshot_bin for s in ss]+["old_english.bin"])
baseline=build_baseline(rt.corpus_tsv,rt.bin_dir/"old_english.bin")
records=baseline["records"]
assert len(records)==394
expected=p["variants"]["selected"]
assert {r["row_id"] for r in records}==set(expected)
for r in records:
    e=expected[r["row_id"]]
    assert (r["fst_input"],r["counterpart"],r["outputs"].split("|"),r["match"]=="1")==(
        e["input"],e["counterpart"],e["output"],e["match"]),r
controls=p["controls"]["late_final_n"]
keys=list(controls)
forms=[r["fst_input"] for r in records]+[controls[k]["input"] for k in keys]
traces={k:[] for k in keys}
hashes={}
for stage in ss:
    path=rt.bin_dir/stage.snapshot_bin
    hashes[stage.foma_identifier]=hashlib.sha256(path.read_bytes()).hexdigest()
    observed=batch_apply_down(path,forms)
    assert len(observed)==len(forms)
    assert all(len(v)==1 for v in observed),stage.foma_identifier
    if stage.foma_identifier=="EnglishProtoInput":
        assert observed[394:]==[controls[k]["gateway"] for k in keys]
    for k,out in zip(keys,observed[394:]):
        traces[k].append({"stage":stage.foma_identifier,"outputs":out})
finals=batch_apply_down(rt.bin_dir/"old_english.bin",forms)
assert finals[394:]==[controls[k]["output"] for k in keys]
assert finals[:394]==[r["outputs"].split("|") for r in records]
diff=[]
for r in records:
    old=p["variants"]["production"][r["row_id"]]
    now={"input":r["fst_input"],"counterpart":r["counterpart"],
         "output":r["outputs"].split("|"),"match":r["match"]=="1",
         "admitted":r["accepted"]=="1"}
    changed=[k for k in now if old[k]!=now[k]]
    if changed:diff.append({"row_id":r["row_id"],"changed":changed,
                           "before":{k:old[k] for k in now},"after":now})
assert [r["row_id"] for r in diff]==["2016"]
print(json.dumps({"frozen_reference":p["reference_sha"],
    "frozen_recipe":p["recipe_sha256"],"summary":baseline["summary"],
    "records":records,"frozen_reference_diff":diff,
    "controls":{k:{"input":controls[k]["input"],"output":out,
                  "trace":traces[k]} for k,out in zip(keys,finals[394:])},
    "stage_binary_sha256":hashes,"intermediate_ambiguities":0,
    "production_binary_sha256":hashlib.sha256(
        (rt.bin_dir/"old_english.bin").read_bytes()).hexdigest()},
    ensure_ascii=False,indent=2))
'''


def main():
    here = Path(__file__).resolve().parent
    frozen = json.loads((here.parent / "flask-late-final-n-evidence/observed.json").read_text())
    with runtime_lock("Flask fresh production 394-row and 15-control verification"):
        result = run_in_runner(
            "python3 -c " + shlex.quote(WORKER),
            input=json.dumps(frozen), text=True, capture_output=True, timeout=1800)
    if result.returncode:
        raise RuntimeError(result.stderr)
    observed = json.loads(result.stdout)
    (here / "observed.json").write_text(
        json.dumps(observed, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: observed[k] for k in (
        "summary", "frozen_reference_diff", "intermediate_ambiguities")}, indent=2,
        ensure_ascii=False))


if __name__ == "__main__":
    main()

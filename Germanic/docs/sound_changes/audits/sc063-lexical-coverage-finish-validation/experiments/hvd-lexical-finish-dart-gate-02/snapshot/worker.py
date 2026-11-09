"""Pinned canonical traces and single-component historically wrong alternatives."""
import csv
import json
import os
from pathlib import Path
import shutil
import sys

sys.path.insert(0, "/usr/app/tools")
import oe_pipeline
from anglo_frisian_experiments import (
    compile_isolated, complete_variant_order, corpus_rows, prepare_definition_image,
)
from oe_input_context import METADATA_FILENAME
from sound_change_order_sensitivity import batch_apply_down

root = Path(sys.argv[1])
source = root / "fst.txt"
shutil.copyfile(root / "context.tsv", root / METADATA_FILENAME)
oe_pipeline.stages = lambda: oe_pipeline.parse_stages(source)
rows = corpus_rows(root / "corpus.tsv")
assert len(rows) == 392
definitions = """
define LxHv [OEHighVowelApocope .o. FootCtx([
    [{*i}|{*u}|{*y}|{*ų}] -> 0 ||
    .#. OEAnyConsonant* HvH _ OEAnyConsonant EnglishStarVocalic
])];
define LxL Ctx([
    {*i} -> 0 || [EnglishStarShortVowel|EnglishStarShortDiphthong]
    [OEAnyConsonant - [{*d}|{*θ}|{*f}]] _ {*l}
]);
define LxSh [OEMedLongShort .o. FootCtx([
    {*ī} -> {*i} || EnglishStarVocalic OEAnyConsonant+ _ .#.
])];
define LxWv Ctx([{*w} -> 0 || EnglishStarVocalic _ [{*i}|{*ī}]]);
define LxWi Ctx([
    {*w} -> 0 || EnglishStarVocalic EnglishStarConsonant* _ {*i}
]);
define LxWAll Ctx([
    {*w} -> 0 || EnglishStarVocalic EnglishStarConsonant* _ EnglishStarVocalic
]);
define LxNAll Ctx([
    {*n} -> 0 || [EnglishStarShortVowel|EnglishStarLongVowel] _ .#.
]);
define LxHap [OEHighVowelApocope .o. FootCtx([
    [{*i}|{*u}|{*y}|{*ų}] -> 0 ||
    .#. OEAnyConsonant* HvH EnglishStarVocalic OEAnyConsonant+ _ .#.
])];
define LxNat _unambpart(EnglishProtoNative);
define LxEnd [PGCellEnd | a:{*a} n:{*n} z:{*z}];
define LxPlain [PGCellRoot PGCellStem* LxEnd];
define LxPrefix [pgrmPrefix PGCellRoot PGCellStem* LxEnd];
define LxRaw [LxPlain | LxPrefix];
define LxGate [
    LxNat | _unambpart([[LxRaw.u - EnglishProtoNative.u] .o. LxRaw])
];
"""
foils = {
    "closed-pre-l-overdeletion": ("OELAdjacentSyncope", "LxL"),
}
recipe = {
    "id": "current", "definitions": definitions,
    "insert_rule": None, "insert_after": None, "replace": {},
    "component_checks": [{"component": name} for name in (
        *[name for _, name in foils.values()],
        "EnglishProtoNative", "PGCellRaw", "PGCellCanonical", "LxNat", "LxRaw", "LxGate")],
}
out = root / "output"
out.mkdir()
image = prepare_definition_image(source, out)
if image:
    os.environ["CAPR_FOMA_DEFINITION_IMAGE"] = str(image)
order = complete_variant_order(recipe)
directory = out / "current"
directory.mkdir()
print("Compiling pinned current cascade and component foils", flush=True)
bins = compile_isolated(source, recipe, [], directory, diagnostic_stages=order)
native = [
    ("dart-nom", "skútilaz"),
    ("dart-acc", "skútilą"),
    ("general-anz-kettle", "kátilanz"),
    ("general-anz-dart", "skútilanz"),
    ("malformed-double-z", "lūtilanzz"),
    ("malformed-double-n", "lūtilannz"),
    ("malformed-ending-stack", "lūtilanzai"),
]
inputs = [row["fst_input"] for row in rows] + [value for _, value in native]
baseline = {
    row["row_id"]: row for row in csv.DictReader(
        (root / "baseline.tsv").open(), delimiter="\t")
}
original = batch_apply_down(bins["final"], inputs)
for row, values in zip(rows, original):
    assert values == baseline[row["id"]]["outputs"].split("|"), row["id"]


def evaluate(replacement=None, initial=None, start=0):
    states = list(inputs if initial is None else initial)
    trace = []
    for index in range(start, len(order)):
        stage = order[index]
        path = bins[f"diagnostic:{index}"]
        if replacement and stage == replacement[0]:
            path = bins[f"component:{replacement[1]}"]
        before = list(states)
        active = [i for i, value in enumerate(states) if value is not None]
        values = [[] for _ in states]
        for i, value in zip(active, batch_apply_down(path, [states[i] for i in active])):
            if len(value) > 1:
                raise AssertionError((stage, replacement, i, value))
            values[i] = [] if value == ["+?"] else value
        if initial is None and replacement is None:
            assert all(len(value) == 1 for value in values[:len(rows)]), stage
        states = [value[0] if value else None for value in values]
        trace.append({"stage": stage, "before": before, "after": states})
    return states, trace


current, trace = evaluate()
assert original == [[value] if value is not None else [] for value in current]
report = {
    "rows": rows, "native": native, "current": current,
    "trace": trace, "foils": {}, "staged": {},
}
report["proto_gate_components"] = {
    name: batch_apply_down(bins["component:" + name], [value for _, value in native])
    for name in ("EnglishProtoNative", "PGCellRaw", "PGCellCanonical", "LxNat", "LxRaw", "LxGate")
}
report["rejected_candidates"] = {
    name: next(item["stage"] for item in trace
               if item["after"][len(rows) + i] is None)
    for i, (name, _) in enumerate(native) if current[len(rows) + i] is None
}
for name, replacement in foils.items():
    values, _ = evaluate(replacement)
    changed = [
        {"id": row["id"], "concept": row["concept"], "before": old, "after": new}
        for row, old, new in zip(rows, current, values) if old != new
    ]
    report["foils"][name] = {
        "changed_selected": changed,
        "native": dict(zip([name for name, _ in native], values[len(rows):])),
    }
    print(name, "changed selected:", changed, "; native:",
          report["foils"][name]["native"], flush=True)
print("Current native:", dict(zip([name for name, _ in native], current[len(rows):])),
      flush=True)
(out / "report.json").write_text(json.dumps(report, ensure_ascii=False))

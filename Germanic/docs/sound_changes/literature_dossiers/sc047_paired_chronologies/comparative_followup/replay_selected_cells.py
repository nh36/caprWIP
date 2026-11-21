"""Replay two corrected cells and the existing labial intervention in Docker."""

import csv
import gzip
import json
import os
from pathlib import Path
import tempfile
from unittest.mock import patch

import run_parallel as parallel


def run():
    import anglo_frisian_experiments as compiler
    from capr_runtime import check_build_manifest, layout
    from oe_pipeline import CITATION_CONTEXT, expected_snapshot_bins, stage_for, stages
    from sound_change_order_sensitivity import batch_apply_down

    runtime = layout()
    source = runtime.germanic_fst
    error = check_build_manifest(expected_snapshot_bins() + ["old_english.bin"])
    if error:
        raise RuntimeError(error)
    plan = json.loads(parallel.CONTROL.read_text())
    frozen_file = parallel.BASE / "parallel/observations.json.gz"
    frozen = json.loads(gzip.decompress(frozen_file.read_bytes()))
    canonical = [stage.foma_identifier for stage in stages()]
    assert parallel.digest(source) == frozen["inputs_sha256"]["germanic.txt"]
    assert parallel.digest(parallel.CONTROL) == frozen["inputs_sha256"]["plan.json"]
    archived_variant = parallel.CONTROL.parent / "selected-outputs.tsv"
    with archived_variant.open() as stream:
        old_b2 = {row["row_id"]: row for row in csv.DictReader(stream, delimiter="\t")}
    rows = frozen["corpus"]
    assert len({row["row_id"] for row in rows}) == len(old_b2) == len(rows) == 394
    replacements = {"2069": ("xágjaz", "xágjō"), "2152": ("rástōz", "rástǭ")}
    inputs = []
    for row in rows:
        before, after = replacements.get(row["row_id"], (row["fst_input"], row["fst_input"]))
        assert row["fst_input"] == before
        inputs.append(after)
    arms = {"canonical": canonical, **frozen["configurations"],
            "B2": parallel.order_for(canonical, plan["configurations"]["split_geminate_only"])}
    variants, _, _ = parallel.recipe()
    for name, operations in variants.items():
        assert arms[name] == parallel.order_for(canonical, operations)
    assert ["FNG" if stage == "FNU" else stage for stage in arms["B"]] == arms["B2"]
    probes = {
        "hay.direct": "xáwją", "hay.gen": "xáwjas", "hay.pl": "xáwjō",
        "hue.direct": "xíwją", "hue.gen": "xíwjas", "hue.pl": "xíwjō",
        "glee.direct": "glíwją", "glee.gen": "glíwjas",
        "new.direct": "níwjaz", "new.gen": "níwjas",
        "sew": "síwjaną", "strew": "stráwjaną", "net": "nátją",
    }
    probes = {name: CITATION_CONTEXT.encode(form) for name, form in probes.items()}
    probes.update({f"selected.{row['concept']}.{row['row_id']}": row["fst_input"]
                   for row in rows if row["concept"] in
                   {"believe", "straw", "show", "sew", "strew", "door", "there", "where", "dill"}})
    checkpoints = {"PWGmcJGemination", "FNU", "FNG", "OEAwwjResolution",
                   "OEEwLongDiphthong", "OEWLossBeforeI", parallel.LAST}
    definitions = [plan["definitions"][name] for name in ("FW", "FNU", "FON", "FNG")]
    queries = {}

    def add(key, forms, members):
        symbol = f"CPX{len(queries)}"
        definitions.append(f"define {symbol} {compiler.foma_domain(forms)} .o. "
                           + " .o. ".join(members) + ";")
        queries[key] = (symbol, forms)

    first = canonical.index(parallel.FIRST) + 1
    indices = [i for i, row in enumerate(rows) if row["row_id"] in replacements]
    incoming = batch_apply_down(runtime.bin_dir / stage_for(parallel.FIRST).snapshot_bin,
                                [inputs[i] for i in indices])
    assert all(len(out) == 1 for out in incoming), incoming
    for arm, order in arms.items():
        assert order[:first] == canonical[:first]
        add(f"{arm}:cells", [out[0] for out in incoming], order[first:])
        for stop, stage in enumerate(order):
            if stage in checkpoints:
                add(f"{arm}:{stage}", list(probes.values()), order[:stop + 1])

    with tempfile.TemporaryDirectory(prefix="capr-sc047-corrected-") as tmp:
        work = Path(tmp)
        image = compiler.prepare_definition_image(source, work)
        if image is None:
            raise RuntimeError("Could not prepare the pinned definition image")
        with patch.dict(os.environ, {"CAPR_FOMA_DEFINITION_IMAGE": str(image)}):
            bins = compiler.compile_isolated(source, {
                "definitions": "\n".join(definitions), "replace": {},
                "insert_rule": None, "insert_after": None,
                "component_checks": [{"component": name} for name, _ in queries.values()],
            }, [], work, components_only=True)
        values = {key: batch_apply_down(bins[f"component:{name}"], forms)
                  for key, (name, forms) in queries.items()}
    assert all(all(outputs) for outputs in values.values())
    corpus = []
    for i, row in enumerate(rows):
        item = {key: row[key] for key in ("row_id", "concept", "counterpart")}
        item["original_input"], item["corrected_input"] = row["fst_input"], inputs[i]
        for arm in arms:
            original = (old_b2[row["row_id"]]["split_geminate_only"].split("|") if arm == "B2"
                        else row["identity" if arm == "canonical" else arm])
            item[arm] = original
            if i in indices:
                item[arm] = values[f"{arm}:cells"][indices.index(i)]
                item[f"original_{arm}"] = original
        corpus.append(item)
    return {
        "id": "SC047-corrected-cells-v1",
        "sha256": {str(path.relative_to(parallel.BASE.parent)): parallel.digest(path) for path in (
            frozen_file, archived_variant, parallel.CONTROL, Path(__file__).resolve())},
        "fst_sha256": parallel.digest(source),
        "compiler_sha256": parallel.digest(Path(compiler.__file__)),
        "orders": arms, "corpus": corpus, "probe_inputs": probes,
        "traces": {key: dict(zip(probes, value)) for key, value in values.items()
                   if not key.endswith(":cells")},
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, separators=(",", ":")))

"""Verify archive equivalence and export exact corpus and diagnostic differences."""

import csv
import gzip
import hashlib
import json
import sys
from pathlib import Path


def write_table(path, columns, rows):
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(columns)
        writer.writerows(rows)


def cell(outputs):
    return " | ".join(outputs) if outputs else "<rejected>"


def firings(result, arm, stage):
    queries = result["queries"]
    prefix = f"{arm}:census:{stage}"
    before, after = (queries[f"{prefix}:{side}"]["outputs"] for side in ("before", "after"))
    return {
        row["row_id"]: (a, b)
        for row, a, b in zip(result["rows"], before, after, strict=True) if a != b
    }


def diagnostic_changes(result, plan):
    queries = result["queries"]
    for arm, order in result["configurations"].items():
        previous = {}
        aliases = {stage: name for name, stage in plan["aliases"][arm].items()}
        for stage in order:
            name = aliases.get(stage, stage)
            query = queries.get(f"{arm}:cell:{name}")
            if query is None:
                continue
            for probe, form, output in zip(
                plan["probe_ids"], query["inputs"], query["outputs"], strict=True
            ):
                before = previous.get(probe)
                if before != output or stage == "OldEnglishSurface":
                    yield arm, stage, probe, form, cell(before) if before is not None else "", cell(output)
                previous[probe] = output


def read_capture(snapshot):
    raw = (snapshot / "results/observed.json").read_bytes()
    sha = lambda data: hashlib.sha256(data).hexdigest()
    completion_path = snapshot / "completion.json"
    completion = json.loads(completion_path.read_bytes())
    receipt = json.loads((snapshot / "receipt.json").read_bytes())
    assert completion["outcome"] == "passed"
    assert completion["result_hashes"]["observed.json"] == sha(raw)
    assert completion["source_identity_sha256"] == receipt["source_identity"]["identity_sha256"]
    result = json.loads(raw)
    command = completion["command_receipts"][0]
    assert command["ok"] and command["stdout_sha256"] == sha(raw)
    assert command["source_identity_sha256"] == completion["source_identity_sha256"]
    pinned = {entry["snapshot_name"]: entry["sha256"] for entry in receipt["inputs"].values()}
    for name, digest in pinned.items():
        assert sha((snapshot / "snapshot" / name).read_bytes()) == digest, name
    plan = json.loads((snapshot / "snapshot/plan.json").read_bytes())
    assert all(pinned[name] == digest for name, digest in plan["helpers"].items())
    assert result["source_sha256"] == pinned["source.txt"]
    assert result["corpus_sha256"] == pinned["corpus.tsv"]
    provenance = {
        "snapshot": snapshot.name,
        "capture_head": receipt["source_identity"]["head_commit"],
        "capture_identity_sha256": completion["source_identity_sha256"],
        "completed_at": completion["completed_at"],
        "completion_receipt_sha256": sha(completion_path.read_bytes()),
        "execution_start": command["started_at"],
        "execution_finish": command["finished_at"],
        "worktree_identity_changed_during_run": command["source_changed"],
        "fst_sha256": result["source_sha256"],
        "corpus_sha256": result["corpus_sha256"],
        "worker_sha256": pinned["worker.py"],
        "pinned_plan_sha256": pinned["plan.json"],
        "pinned_inputs": pinned,
        "raw_observations_sha256": sha(raw),
        "cost": result["cost"],
    }
    return result, plan, raw, provenance


def write_archive(path, raw, provenance):
    frozen = gzip.compress(raw, mtime=0)
    path.write_bytes(frozen)
    provenance["frozen_observations_sha256"] = hashlib.sha256(frozen).hexdigest()


def main():
    destination = Path(__file__).resolve().parent
    result, plan, raw, provenance = read_capture(Path(sys.argv[1]))
    comparison = destination.parent / "labial_review" / "observations.json.gz"
    archived = json.loads(gzip.decompress(comparison.read_bytes()))
    arms = list(result["corpus"])
    for new, old in [
        ("identity", "identity"), ("A", "early"), ("B", "split"),
        ("B_geminate_only", "split_geminate_only"),
    ]:
        assert result["corpus"][new] == archived["corpus"][old], new

    reference = result["corpus"]["identity"]["rows"]
    assert len(reference) == 394
    assert all(result["corpus"][arm]["rejected"] == 0 for arm in arms)
    assert all(result["corpus"][arm]["ambiguous"] == 0 for arm in arms)
    for arm in arms:
        low = "PNWGmcULowering"
        r = "PNWGmcMonosyllabicFinalRLengthening"
        assert len(firings(result, arm, low)) == 40
        assert firings(result, arm, low).keys() == firings(result, "identity", low).keys()
        assert firings(result, arm, r) == firings(result, "identity", r)
        for row in result["corpus"][arm]["rows"]:
            if row["concept"] in {"door", "there", "where", "deer"}:
                assert row["baseline"] == row["outputs"], (arm, row)

    local = result["queries"]["contraction.local"]["outputs"]
    assert local == [[form] for form in [
        "*p*ḯ", "*p*í*í", "*p*i*i", "*p*í*ī", "*p*ḯ*i", "*p*ḯ*n",
    ]]
    placement_controls = {
        "B_geminate_only": "B", "B_consumers_before_loss": "B",
        "C_consumers_before_loss": "C_northern_order",
        "A_contraction": "A", "A_late_contraction": "A",
        "A_singleton_aw": "A", "live_singleton_aw": "identity",
    }
    write_table(
        destination / "factor-differences.tsv",
        ["arm", "control", "row_id", "concept", "control_output", "arm_output"],
        ([arm, control, row["row_id"], row["concept"], cell(other["outputs"]), cell(row["outputs"])]
         for arm, control in placement_controls.items()
         for row, other in zip(result["corpus"][arm]["rows"],
                               result["corpus"][control]["rows"], strict=True)
         if row["outputs"] != other["outputs"]),
    )
    write_table(
        destination / "outputs.tsv", ["row_id", "concept", "input", "target", *arms],
        ([row["row_id"], row["concept"], row["fst_input"], row["counterpart"],
          *(cell(result["corpus"][arm]["rows"][index]["outputs"]) for arm in arms)]
         for index, row in enumerate(reference)),
    )
    write_table(
        destination / "diagnostics.tsv",
        ["arm", "checkpoint", "probe", "input", "previous_checked_output", "output"],
        diagnostic_changes(result, plan),
    )
    provenance = {
        "production_reference": "1468c4ac0a6b4d4ca4997a28f82e88353f33c7a0",
        "discussion_base": "489f7d424942cea22844925f599b95c120f4a079",
        **provenance,
    }
    write_archive(destination / "observations.json.gz", raw, provenance)
    if len(sys.argv) > 2:
        placement, _, placement_raw, placement_provenance = read_capture(Path(sys.argv[2]))
        assert {name: digest for name, digest in placement_provenance["pinned_inputs"].items()
                if name != "plan.json"} == {
            name: digest for name, digest in provenance["pinned_inputs"].items()
            if name != "plan.json"
        }
        for arm, summary in placement["corpus"].items():
            assert summary == result["corpus"][arm], arm
            assert placement["configurations"][arm] == result["configurations"][arm], arm
            assert firings(placement, arm, "PWGmcEndinglessAw") == firings(
                result, arm, "PWGmcEndinglessAw"
            ), arm
        assert placement["witness_row_ids"] == ["1944", "2224"]
        write_archive(
            destination / "placement-traces.json.gz", placement_raw, placement_provenance
        )
        provenance["placement_trace"] = placement_provenance
    (destination / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    for arm, summary in result["corpus"].items():
        changes = [(row["concept"], cell(row["outputs"])) for row in summary["rows"]
                   if row["outputs"] != row["baseline"]]
        print(arm, summary["matches"], changes)


if __name__ == "__main__":
    main()

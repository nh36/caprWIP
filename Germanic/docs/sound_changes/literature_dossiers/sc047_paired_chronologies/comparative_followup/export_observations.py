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


def main():
    snapshot = Path(sys.argv[1])
    destination = Path(__file__).resolve().parent
    raw = (snapshot / "results/observed.json").read_bytes()
    result = json.loads(raw)
    plan_bytes = (snapshot / "snapshot/plan.json").read_bytes()
    plan = json.loads(plan_bytes)
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

    write_table(
        destination / "outputs.tsv", ["row_id", "concept", "input", "target", *arms],
        ([row["row_id"], row["concept"], row["fst_input"], row["counterpart"],
          *(cell(result["corpus"][arm]["rows"][index]["outputs"]) for arm in arms)]
         for index, row in enumerate(reference)),
    )
    write_table(
        destination / "diagnostics.tsv", ["arm", "checkpoint", "probe", "input", "output"],
        ([arm, stage, name, input_form, cell(output)]
         for query, data in result["queries"].items() if ":cell:" in query
         for arm, _, stage in [query.partition(":cell:")]
         for name, input_form, output in zip(
             plan["probe_ids"], data["inputs"], data["outputs"], strict=True)),
    )
    (destination / "observations.json.gz").write_bytes(gzip.compress(raw, mtime=0))
    sha = lambda data: hashlib.sha256(data).hexdigest()
    provenance = {
        "production_reference": "1468c4ac0a6b4d4ca4997a28f82e88353f33c7a0",
        "discussion_base": "489f7d424942cea22844925f599b95c120f4a079",
        "snapshot": snapshot.name,
        "fst_sha256": result["source_sha256"],
        "corpus_sha256": result["corpus_sha256"],
        "worker_sha256": sha((snapshot / "snapshot/worker.py").read_bytes()),
        "pinned_plan_sha256": sha(plan_bytes),
        "raw_observations_sha256": sha(raw),
        "frozen_observations_sha256": sha((destination / "observations.json.gz").read_bytes()),
        "cost": result["cost"],
    }
    (destination / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    for arm, summary in result["corpus"].items():
        changes = [(row["concept"], cell(row["outputs"])) for row in summary["rows"]
                   if row["outputs"] != row["baseline"]]
        print(arm, summary["matches"], changes)


if __name__ == "__main__":
    main()

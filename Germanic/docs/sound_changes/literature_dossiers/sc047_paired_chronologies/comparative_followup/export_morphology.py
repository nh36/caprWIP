"""Export the unscored morphology and hiatus round without changing prior evidence."""

import gzip
import json
import sys
from pathlib import Path

from export_observations import cell, diagnostic_changes, read_capture, write_archive, write_table


def main(snapshot):
    base = Path(__file__).resolve().parent
    destination = base / "morphology"
    result, plan, raw, provenance = read_capture(snapshot)
    reference_path = base / "source_integration" / "observations.json.gz"
    reference = json.loads(gzip.decompress(reference_path.read_bytes()))
    assert list(result["corpus"]) == ["identity", "A", "B", "C_northern_order"]
    for arm, corpus in result["corpus"].items():
        assert corpus == reference["corpus"][arm], arm
        assert result["configurations"][arm] == reference["configurations"][arm], arm

    identity = result["corpus"]["identity"]
    assert (len(identity["rows"]), identity["matches"], identity["rejected"],
            identity["ambiguous"]) == (394, 386, 0, 0)
    queries = result["queries"]
    for arm in result["corpus"]:
        expected = ("fene", "wede", "wefe") if arm == "A" else ("fen", "wedd", "webb")
        outputs = queries[f"{arm}:cell:OldEnglishSurface"]["outputs"]
        assert outputs[::3] == [[form] for form in expected], arm
        assert [cell(form) for i, form in enumerate(outputs) if i % 3] == [
            "fennes", "fenne", "weddes", "wedde", "webbes", "webbe",
        ], arm
    comparison = {name.removeprefix("hiatus:"): query for name, query in queries.items()
                  if name.startswith("hiatus:")}
    assert len(comparison) == 5
    loss = comparison["loss"]
    assert all(query["inputs"] == loss["inputs"] for query in comparison.values())
    assert comparison["fusion_hvd"]["outputs"][:3] == comparison["lengthening_hvd"]["outputs"][:3]

    destination.mkdir(exist_ok=True)
    write_table(destination / "diagnostics.tsv",
                ["arm", "checkpoint", "probe", "input", "previous_checkpoint", "output"],
                diagnostic_changes(result, plan))
    write_table(destination / "hiatus.tsv", ["input", *comparison],
                ([form, *(cell(query["outputs"][i]) for query in comparison.values())]
                 for i, form in enumerate(loss["inputs"])))
    write_archive(destination / "observations.json.gz", raw, provenance)
    provenance["frozen_comparison"] = str(reference_path.relative_to(base))
    (destination / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")


if __name__ == "__main__":
    main(Path(sys.argv[1]))

"""Export the source-integration assay separately from the earlier archive."""

import gzip
import json
import sys
from pathlib import Path

from export_observations import (
    cell, diagnostic_changes, firings, read_capture, write_archive, write_table,
)


def main(snapshot):
    previous = Path(__file__).resolve().parent
    destination = previous / "source_integration"
    result, plan, raw, provenance = read_capture(snapshot)
    prior = json.loads(gzip.decompress((previous / "observations.json.gz").read_bytes()))
    corpus = result["corpus"]
    identity = corpus["identity"]["rows"]
    queries = result["queries"]
    configurations = result["configurations"]
    for arm in corpus.keys() & prior["corpus"].keys():
        assert corpus[arm] == prior["corpus"][arm], arm
        assert configurations[arm] == prior["configurations"][arm], arm

    assert len(identity) == 394 and corpus["identity"]["matches"] == 386
    picked = {row_id: i for i, row_id in enumerate(result["witness_row_ids"])}
    lowering = "PNWGmcULowering"
    lengthening = "PNWGmcMonosyllabicFinalRLengthening"
    labial_control = "PWGmcEndinglessAw"
    door = next(i for i, row in enumerate(identity) if row["concept"] == "door")
    divergences = []
    for arm, summary in corpus.items():
        assert not summary["rejected"] and not summary["ambiguous"], arm
        lowers = firings(result, arm, lowering)
        assert len(lowers) == 40 and lowers.keys() == firings(result, "identity", lowering).keys()
        assert firings(result, arm, lengthening) == firings(result, "identity", lengthening)
        assert {key: after for key, (_, after) in firings(result, arm, labial_control).items()} == {
            "2224": ["*s*t*r*áu"]
        }
        before = queries[f"{arm}:census:{lengthening}:before"]["outputs"][door]
        assert before == ["*d*ó*r*ą"], (arm, before)
        aliases = {actual: nominal for nominal, actual in plan["aliases"][arm].items()}
        for row in summary["rows"]:
            if row["concept"] in {"door", "there", "where", "deer"}:
                assert row["baseline"] == row["outputs"], (arm, row)
            if row["baseline"] == row["outputs"]:
                continue
            i = picked[row["row_id"]]
            first = True
            for stage in configurations[arm]:
                test = queries.get(f"{arm}:all:{stage}")
                live = queries.get(f"identity:all:{aliases.get(stage, stage)}")
                if test is not None and live is not None:
                    old, new = live["outputs"][i], test["outputs"][i]
                    if old != new:
                        divergences.append((arm, row["row_id"], row["concept"], stage,
                                            "first" if first else "", cell(old), cell(new)))
                        first = False
            assert not first, (arm, row)

    local = queries["contraction.local"]["outputs"]
    assert local == [[form] for form in (
        "*p*ḯ", "*p*í*í", "*p*i*i", "*p*í*ī", "*p*ḯ*i", "*p*ḯ*n",
    )]
    assert queries["erdmann.gemination.local"]["outputs"] == [[form] for form in (
        "*d*á*n*i*j*ō", "*d*á*n*n*j*ō", "*w*í*n*i*j*ō", "*w*í*n*n*j*ō",
    )]

    def diagnostic(arm, stage="OldEnglishSurface"):
        return dict(zip(plan["probe_ids"], queries[f"{arm}:cell:{stage}"]["outputs"],
                        strict=True))

    first = diagnostic("A_contraction")
    for arm in ("A_presyncope_contraction", "A_late_contraction"):
        assert diagnostic(arm) == first and corpus[arm] == corpus["A_contraction"], arm
    for probe, expected in (
        ("hue.direct", "hī"), ("glee.direct", "glī"), ("new.oral_direct", "nī"),
        ("hue.gen.sg", "hīewes"), ("glee.protected", "glīewes"),
        ("new.protected", "nīewes"), ("sea.direct", "sǣ"),
    ):
        assert first[probe] == [expected], probe
    for arm, direct in (("A_matched", "cyne"), ("B_matched", "cyn"),
                        ("C_northern_order_matched", "cyn")):
        assert diagnostic(arm)["cynn.direct"] == [direct], arm
        assert diagnostic(arm)["cynn.gen.sg"] == ["cynnes"], arm
        assert diagnostic(arm)["cynn.dat.sg"] == ["cynne"], arm

    destination.mkdir(exist_ok=True)
    write_table(
        destination / "outputs.tsv", ["row_id", "concept", "input", "target", *corpus],
        ([row["row_id"], row["concept"], row["fst_input"], row["counterpart"],
          *(cell(corpus[arm]["rows"][i]["outputs"]) for arm in corpus)]
         for i, row in enumerate(identity)),
    )
    write_table(
        destination / "changed-stages.tsv",
        ["arm", "row_id", "concept", "stage", "first_shared_checkpoint", "live", "candidate"],
        divergences,
    )
    write_table(
        destination / "diagnostics.tsv",
        ["arm", "checkpoint", "probe", "input", "previous_checked_output", "output"],
        diagnostic_changes(result, plan),
    )
    write_archive(destination / "observations.json.gz", raw, provenance)
    (destination / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    for arm, summary in corpus.items():
        print(arm, summary["matches"], [(row["concept"], cell(row["outputs"]))
              for row in summary["rows"] if row["outputs"] != row["baseline"]])


if __name__ == "__main__":
    main(Path(sys.argv[1]))

"""Export reviewable tables from the paired run, without invoking Foma."""

import argparse
import csv
import gzip
import json
from pathlib import Path

from run_parallel import FIRST, LAST

NASAL = "OEHeavySyllableNasalApocope"
GEMINATION = "PWGmcJGemination"


def tables(report):
    corpus = report["corpus"]
    orders = report["configurations"]
    traces = report["traces"]
    changed = [["ID", "concept", "input", "target", "canonical", "A", "B"]]
    for row in corpus:
        if row["identity"] != row["A"] or row["identity"] != row["B"]:
            changed.append([row[key] for key in ("row_id", "concept", "proto", "counterpart")]
                           + [display(row[key]) for key in ("identity", "A", "B")])
    cells = [["cell_or_id", "FST_input", "shared_after_oral_vocalization",
              "A_first_block_step", "A_after_nasal_loss_and_vocalization", "A_after_SC010",
              "B_first_block_step", "B_after_nasal_loss_and_vocalization", "B_after_SC010",
              "first_unequal_block_step", "A_final", "B_final"]]
    index = {row["row_id"]: row for row in corpus}
    probes = list(report["cells"].items()) + [
        (key, index[key]["fst_input"]) for key in report["controls"]]
    blocks = {label: order[order.index("FON") + 1:order.index("FON") + 4]
              for label, order in orders.items()}
    assert blocks == {"A": [NASAL, "FNU", GEMINATION],
                      "B": [GEMINATION, NASAL, "FNU"]}
    for i, (cell, form) in enumerate(probes):
        def at(label, stage):
            return display(traces[f"{label}:{stage}"][i])

        assert at("A", "FON") == at("B", "FON")
        fork = next((str(step) for step, (a, b) in enumerate(zip(*blocks.values()), 1)
                     if at("A", a) != at("B", b)), "none")
        cells.append([cell, form, at("A", "FON"), at("A", NASAL), at("A", "FNU"),
                      at("A", GEMINATION), at("B", GEMINATION), at("B", "FNU"),
                      at("B", GEMINATION), fork, at("A", LAST), at("B", LAST)])
    return {"changed-outputs.tsv": changed, "matched-cells.tsv": cells}


def display(forms):
    return " | ".join(forms) or "∅"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("observation", type=Path)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    data = args.observation.read_bytes()
    report = json.loads(gzip.decompress(data) if data.startswith(b"\x1f\x8b") else data)
    assert report["prefix"] == FIRST
    args.out.mkdir(exist_ok=True, parents=True)
    for file, rows in tables(report).items():
        with (args.out / file).open("w", encoding="utf-8", newline="") as handle:
            csv.writer(handle, delimiter="\t", lineterminator="\n").writerows(rows)
    for label in ("identity", "A", "B"):
        rows = report["corpus"]
        print(label, {
            "matches": sum(row["counterpart"] in row[label] for row in rows),
            "changed": sum(row[label] != row["identity"] for row in rows),
            "rejected": sum(not row[label] for row in rows),
            "ambiguous": sum(len(row[label]) > 1 for row in rows),
        })


if __name__ == "__main__":
    main()

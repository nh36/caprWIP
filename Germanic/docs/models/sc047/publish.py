"""Generate separate catalogues, derivations and discrepancy inventories."""

import argparse
import csv
import gzip
import json
import os
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
GERMANIC = HERE.parents[2]
ASSEMBLY = GERMANIC / "docs/assembly"
FIELDS = ("row_id", "concept", "headword", "proto", "fst_input", "counterpart", "canonical_outputs",
          "diagnostic_outputs", "selection_status", "selected_cell", "selected_input", "selected_target",
          "selected_outputs", "frozen_input_decision", "published_class", "assessment")


def display(outputs):
    return " / ".join(outputs) if outputs else "(rejected)"


def assessment(model, row, known):
    target = row["selected_target"]
    if target in row["selected_outputs"]:
        if row["selected_input"] != row["fst_input"] or target != row["counterpart"]:
            return ("protected attested cell; proposed transfer is not a sound change"
                    if model == "A" and row["row_id"] in {"2138", "2332"}
                    else "common source-backed stem or cell correction")
        return "same evaluated form as frozen diagnostic"
    if row["row_id"] == "2061" and model == "A":
        return "inherited singleton prediction; no independently verified protected target"
    if row["canonical_outputs"] == row["selected_outputs"] and row["proto"] in known:
        return "inherited mismatch: " + known[row["proto"]]["category"]
    if row["proto"] in known:
        return "changed inherited mismatch; independently review " + known[row["proto"]]["category"]
    return "unresolved; no replacement attestation assigned"


def trace_text(start, trace):
    return " → ".join([f"`{start}`"] + [
        f"`{display(outputs)}` ({stage})" for stage, outputs in trace])


def first_different_events(left, right):
    for index, (a, b) in enumerate(zip(left, right)):
        if a != b:
            return [a, b]
    index = min(len(left), len(right))
    return [left[index] if index < len(left) else None,
            right[index] if index < len(right) else None]


def lexical_metadata():
    with (ASSEMBLY / "manifest_all_by_class.tsv").open(encoding="utf-8") as stream:
        headings = {}
        classes = {}
        for row in csv.DictReader(stream, delimiter="\t"):
            path = row["model_entry_path"]
            classes[row["row_id"]] = row["derivation_class"]
            if not path:
                continue
            with (GERMANIC.parent / path).open(encoding="utf-8") as entry:
                heading = entry.readline()
            _, separator, headword = heading.strip().partition(" — OE ")
            if separator:
                headings[row["row_id"]] = headword
    # The frozen hay row has no assembled lexical dossier.
    headings["2061"] = "hīeġ"
    with (GERMANIC / "data/entry_stage_metadata.tsv").open(encoding="utf-8") as stream:
        decisions = {row["row_id"]: row["decision_type"]
                     for row in csv.DictReader(stream, delimiter="\t")}
    return headings, classes, decisions


def expansion_entries(model, paradigms):
    cells = {(row["lexeme"], row["cell"]): row for row in paradigms}
    with (HERE / "expansions.tsv").open(encoding="utf-8") as stream:
        proposals = list(csv.DictReader(stream, delimiter="\t"))
    if len({row["id"] for row in proposals}) != len(proposals):
        raise ValueError("Duplicate research lexical identity")
    for row in proposals:
        if not row["id"].startswith("sc047-"):
            raise ValueError(f"Not a research lexical identity: {row['id']}")
        label = row[f"{model}_cell"]
        cell = cells.get((row["lexeme"], label)) if label else None
        target = row.get(f"{model}_target")
        if cell and target:
            cell = {**cell, "target": target}
        if label and (not cell or not cell["target"] or cell["target"] not in cell["outputs"]):
            raise ValueError(f"Research proposal lacks a matching attested cell: {row['id']} {model}")
        yield row, cell


def publish(result, directory):
    directory.mkdir(parents=True, exist_ok=True)
    with (GERMANIC / "data/oe_known_problems.tsv").open(encoding="utf-8") as stream:
        known = {row["proto"]: row for row in csv.DictReader(stream, delimiter="\t")}
    headings, classes, decisions = lexical_metadata()
    if all("active_corpus" in value for value in result["models"].values()):
        return publish_active(result, directory, headings)
    chapter_lines = (ASSEMBLY / "sc047_preview/chronologies.md").read_text(encoding="utf-8").splitlines()
    chapter = "\n".join("#" + line if line.startswith("# ") else line for line in chapter_lines)
    summary = {}
    for model, value in result["models"].items():
        rows = value["corpus"]
        if len({row["row_id"] for row in rows}) != 394 or len(rows) != 394:
            raise ValueError("Expected all 394 lexical identities exactly once")
        md = [f"# CAPR Germanic: Model {model}", "",
              f"Research implementation `{result['version']}`. The frozen diagnostic is a separate "
              "comparison, not the selected lexical catalogue.", "",
              chapter, "",
              "## Lexical catalogue", "",
              "Headwords are shown where the shared dossiers supply them. An unresolved comparison "
              "is not a certified selected cell; its original target is retained for visibility.", "",
              "| ID | Lexeme / OE headword | Cell | Input | Target | Regular output |",
              "|---|---|---|---|---|---|"]
        traces = [f"# Model {model}: complete derivations", "",
                  "Only stages that change the form are listed. The complete stage order is in the "
                  "technical appendix of the model volume.", ""]
        summary[model] = {
            "diagnostic": sum(row["counterpart"] in row["diagnostic_outputs"] for row in rows),
            "selected_slots": sum(row["selection_status"] != "unresolved comparison" for row in rows),
            "matches": sum(row["selected_target"] in row["selected_outputs"] and
                           row["selection_status"] != "unresolved comparison" for row in rows),
            "unmatched": [],
        }
        derived_fields = {"assessment", "headword", "published_class", "frozen_input_decision"}
        with (directory / f"{model}-inventory.tsv").open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, FIELDS, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            for row in rows:
                status = assessment(model, row, known)
                cell_label = row["selected_cell"] or row["selection_status"]
                headword = headings.get(row["row_id"], "")
                label = f"{row['concept']} / *{headword}*" if headword else row["concept"]
                md.append(f"| {row['row_id']} | {label} | {cell_label} "
                          f"| `*{row['selected_input']}` | *{row['selected_target']}* "
                          f"| `{display(row['selected_outputs'])}` |")
                leaf = {key: row[key] for key in FIELDS if key not in derived_fields}
                for key in ("canonical_outputs", "diagnostic_outputs", "selected_outputs"):
                    leaf[key] = " | ".join(leaf[key])
                writer.writerow({**leaf, "headword": headword, "assessment": status,
                                 "frozen_input_decision": decisions.get(row["row_id"], ""),
                                 "published_class": classes.get(row["row_id"], "")})
                if row["selected_target"] not in row["selected_outputs"]:
                    entry = {"id": row["row_id"], "lexeme": row["concept"], "diagnosis": status,
                             "input": row["selected_input"], "target": row["selected_target"],
                             "outputs": row["selected_outputs"]}
                    if row["proto"] in known:
                        entry["legacy_reason"] = known[row["proto"]]["reason"]
                    summary[model]["unmatched"].append(entry)
                traces.extend((f"## {row['row_id']} — {row['concept']}", "",
                               "Frozen input: " + trace_text(row["fst_input"], row["diagnostic_trace"]), ""))
                if row["diagnostic_outputs"] != row["canonical_outputs"]:
                    entry = first_different_events(row["canonical_trace"], row["diagnostic_trace"])
                    summary[model].setdefault("changed_diagnostics", []).append({
                        "id": row["row_id"], "lexeme": row["concept"], "input": row["fst_input"],
                        "canonical": row["canonical_outputs"], "active": row["diagnostic_outputs"],
                        "first_different_trace_events": entry,
                    })
                    traces.extend(("Canonical: " + trace_text(row["fst_input"], row["canonical_trace"]), ""))
                if row["selected_trace"] is not None:
                    traces.extend((f"Selected {row['selected_cell']}: "
                                   + trace_text(row["selected_input"], row["selected_trace"]), ""))
        entries = list(expansion_entries(model, value["paradigms"]))
        md.extend(("", "## Proposed catalogue additions", "",
                   "These entries have separate research identities and do not enter either benchmark score.", ""))
        fields = ("id", "lexeme", "headword", "cell", "input", "target", "outputs", "status")
        with (directory / f"{model}-expansions.tsv").open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fields, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            for row, cell in entries:
                md.extend(("", f"### {row['lexeme'].capitalize()} — *{row['headword']}*", ""))
                publication = {key: row[key] for key in ("id", "lexeme", "headword")}
                if cell:
                    publication.update({key: cell[key] for key in ("cell", "input", "target")})
                    publication.update(status="proposed selection", outputs=display(cell["outputs"]))
                    md.extend((f"Proposed {cell['cell']}: `*{cell['input']}` yields *{cell['target']}*.", ""))
                    traces.extend((f"## {row['id']} — selected {cell['cell']}", "",
                                   trace_text(cell["input"], cell["trace"]), ""))
                else:
                    publication["status"] = "pending selection"
                    md.extend(("Selection pending; see the paradigm evidence below.", ""))
                writer.writerow(publication)
                md.append((HERE / "lexemes" / f"{row['id']}.md").read_text(encoding="utf-8"))
        md.extend(("", "## Technical appendix", "",
                   f"Frozen matches: {summary[model]['diagnostic']}/394. "
                   f"Selected matches: {summary[model]['matches']}/{summary[model]['selected_slots']}.",
                   "",
                   "Executable order: " + ", ".join(f"`{stage}`" for stage in value["order"]),
                   "", "### Paradigms and unselected cells", "",
                   "| Lexeme | Cell | Reconstructed input | Regular output | Comparison target | Witness and limits |",
                   "|---|---|---|---|---|---|"))
        for cell in value["paradigms"]:
            md.append(f"| {cell['lexeme']} | {cell['cell']} | `*{cell['input']}` "
                      f"| `{display(cell['outputs'])}` | {cell['target']} | {cell['evidence']} |")
            traces.extend((f"## {cell['lexeme']} — {cell['cell']}", "",
                           trace_text(cell["input"], cell["trace"]), ""))
        for probe in value["queries"]:
            traces.extend((f"## Exploratory input — {probe['input']}", "",
                           trace_text(probe["input"], probe["trace"]), ""))
        md.extend(("", "### Unmatched forms and unresolved comparisons", ""))
        for item in summary[model]["unmatched"]:
            md.append(f"- {item['lexeme']} ({item['id']}), `*{item['input']}`: "
                      f"`{display(item['outputs'])}` vs *{item['target']}* — {item['diagnosis']}.")
        (directory / f"{model}-volume.md").write_text("\n".join(md) + "\n", encoding="utf-8")
        (directory / f"{model}-derivations.md").write_text("\n".join(traces) + "\n", encoding="utf-8")
    if set(result["models"]) == {"A", "B2"}:
        rows_a = result["models"]["A"]["corpus"]
        rows_b = {row["row_id"]: row for row in result["models"]["B2"]["corpus"]}
        lines = ["# Frozen-input differences between A and B2", "",
                 "| ID | Lexeme | Frozen input | A | B2 | Target |",
                 "|---|---|---|---|---|---|"]
        for a in rows_a:
            b = rows_b[a["row_id"]]
            if (a["fst_input"], a["counterpart"]) != (b["fst_input"], b["counterpart"]):
                raise ValueError(f"Models disagree on frozen inputs: {a['row_id']}")
            if a["diagnostic_outputs"] != b["diagnostic_outputs"]:
                lines.append(f"| {a['row_id']} | {a['concept']} | `*{a['fst_input']}` "
                             f"| `{display(a['diagnostic_outputs'])}` | `{display(b['diagnostic_outputs'])}` "
                             f"| *{a['counterpart']}* |")
        (directory / "comparison.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (directory / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
                                            encoding="utf-8")


COMMON_CELLS = {
    "2138": "dat.sg", "2332": "gen.sg", "2340": "dat.sg", "2341": "gen.sg",
    "2069": "nom.sg.fem", "2152": "acc.sg",
}


def publish_active(result, directory, headings):
    summary = {}
    shared = None
    for model, value in result["models"].items():
        frozen = {row["row_id"]: row for row in value["corpus"]}
        active = {row["row_id"]: row for row in value["active_corpus"]}
        if len(active) != len(value["active_corpus"]):
            raise ValueError("Duplicate active lexical identity")
        identity = {key: (row["fst_input"], row["counterpart"]) for key, row in active.items()}
        if shared is not None and identity != shared:
            raise ValueError("Active model catalogues disagree on selected evidence")
        shared = identity
        volume = [f"# CAPR Germanic: Model {model}", "",
                  "This is the derivation companion to the common indexed lexical catalogue. "
                  "The archived selected-form comparisons do not enter this score.", "",
                  "| ID | Lexeme / headword | Input | Target | Regular output |",
                  "|---|---|---|---|---|"]
        traces = [f"# Model {model}: complete derivations", "",
                  "Order: " + ", ".join(f"`{stage}`" for stage in value["order"]), ""]
        changed = {}
        for key, row in active.items():
            old = frozen.get(key)
            proto, target = identity[key]
            headword = headings.get(key)
            label = f"{row['concept']} / *{headword}*" if headword else row["concept"]
            volume.append(f"| {key} | {label} | `*{proto}` | *{target}* | `{display(row['outputs'])}` |")
            traces.extend((f"## {key} — {label}", "", trace_text(proto, row["trace"]), ""))
            if old is None or (old["fst_input"], old["counterpart"]) != identity[key]:
                changed[key] = {"before": [old["fst_input"], old["counterpart"]] if old else None,
                                "after": [proto, target], "outputs": row["outputs"]}
        for probe in (*value["paradigms"], *value["queries"]):
            label = f"{probe['lexeme']} — {probe['cell']}" if "cell" in probe else probe["input"]
            traces.extend((f"## Unscored — {label}", "",
                           trace_text(probe["input"], probe["trace"]), ""))
        missing = {key: [row["counterpart"], row["outputs"]] for key, row in active.items()
                   if row["counterpart"] not in row["outputs"]}
        frozen_missing = {key: [row["counterpart"], row["diagnostic_outputs"]]
                          for key, row in frozen.items()
                          if row["counterpart"] not in row["diagnostic_outputs"]}
        common = {key: {"cell": cell, "input": active[key]["fst_input"],
                        "target": active[key]["counterpart"], "outputs": active[key]["outputs"]}
                  for key, cell in COMMON_CELLS.items()}
        summary[model] = {
            "frozen": {"matches": len(frozen) - len(frozen_missing), "rows": len(frozen),
                       "unmatched": frozen_missing,
                       "changed_outputs": {key: row["diagnostic_outputs"] for key, row in frozen.items()
                                           if row["diagnostic_outputs"] != row["canonical_outputs"]}},
            "active": {"matches": len(active) - len(missing), "rows": len(active), "unmatched": missing,
                       "changed_selections": changed, "removed": sorted(frozen.keys() - active.keys())},
            "common": {"matches": sum(item["target"] in item["outputs"] for item in common.values()),
                       "rows": len(common), "cells": common},
        }
        volume.extend(("", "## Technical appendix", "",
                       f"Active selected matches: {len(active) - len(missing)}/{len(active)}. "
                       f"Historical frozen matches: {len(frozen) - len(frozen_missing)}/{len(frozen)}.", "",
                       "Hay remains a direct comparison in both denominators. Model A has "
                       "no verified protected selection.", "", "### Unmatched active forms", ""))
        volume.extend(f"- {key}: *{target}* versus `{display(outputs)}`."
                      for key, (target, outputs) in missing.items())
        (directory / f"{model}-volume.md").write_text("\n".join(volume) + "\n", encoding="utf-8")
        (directory / f"{model}-derivations.md").write_text("\n".join(traces) + "\n", encoding="utf-8")
    (directory / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
                                            encoding="utf-8")


def render(directory, models):
    for model in models:
        volume = directory / f"{model}-volume.md"
        subprocess.run([
            "pandoc", str(volume), "--pdf-engine=xelatex", "--toc", "--citeproc",
            "--bibliography", str(GERMANIC.parent / "docs/refs.bib"),
            "--bibliography", str(ASSEMBLY / "sc047_preview/supplement.bib"),
            "-V", "mainfont=Noto Serif",
            "-V", f"monofont={os.environ.get('SC047_PREVIEW_MONOFONT', 'Noto Sans Mono')}",
            "-V", "geometry:margin=24mm", "-o", str(volume.with_suffix(".pdf")),
        ], check=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("result", type=Path)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--pdf", action="store_true", help="render each model volume with Pandoc and XeLaTeX")
    args = parser.parse_args()
    read = gzip.open if args.result.suffix == ".gz" else open
    with read(args.result, "rt", encoding="utf-8") as stream:
        result = json.load(stream)
    publish(result, args.directory)
    if args.pdf:
        render(args.directory, result["models"])

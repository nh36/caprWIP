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
          "selected_outputs", "assessment")


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


def headwords():
    with (ASSEMBLY / "manifest_all_by_class.tsv").open(encoding="utf-8") as stream:
        result = {}
        for row in csv.DictReader(stream, delimiter="\t"):
            path = row["model_entry_path"]
            if not path:
                continue
            with (GERMANIC.parent / path).open(encoding="utf-8") as entry:
                heading = entry.readline()
            _, separator, headword = heading.strip().partition(" — OE ")
            if separator:
                result[row["row_id"]] = headword
    # The frozen hay row has no assembled lexical dossier.
    result["2061"] = "hīeġ"
    return result


def publish(result, directory):
    directory.mkdir(parents=True, exist_ok=True)
    with (GERMANIC / "data/oe_known_problems.tsv").open(encoding="utf-8") as stream:
        known = {row["proto"]: row for row in csv.DictReader(stream, delimiter="\t")}
    headings = headwords()
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
                leaf = {key: row[key] for key in FIELDS if key not in ("assessment", "headword")}
                for key in ("canonical_outputs", "diagnostic_outputs", "selected_outputs"):
                    leaf[key] = " | ".join(leaf[key])
                writer.writerow({**leaf, "headword": headword, "assessment": status})
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
        md.extend(("", "## Technical appendix", "",
                   "Executable order: " + ", ".join(f"`{stage}`" for stage in value["order"]),
                   "", "### Paradigms and unselected cells", "",
                   "| Lexeme | Cell | Reconstructed input | Regular output | Comparison target | Witness and limits |",
                   "|---|---|---|---|---|---|"))
        for cell in value["paradigms"]:
            md.append(f"| {cell['lexeme']} | {cell['cell']} | `*{cell['input']}` "
                      f"| `{display(cell['outputs'])}` | {cell['target']} | {cell['evidence']} |")
            traces.extend((f"## {cell['lexeme']} — {cell['cell']}", "",
                           trace_text(cell["input"], cell["trace"]), ""))
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

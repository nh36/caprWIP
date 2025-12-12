#!/usr/bin/env python3
"""Compare PGmc inputs pushed through EnglishSandboxProtoToOE vs. attested Old English forms."""
from __future__ import annotations

import argparse
import csv
import re
import subprocess
from pathlib import Path
from typing import Dict, List

DEFAULT_TSV = Path(__file__).resolve().parents[1] / "data" / "germanic-aligned-final.tsv"
DEFAULT_BIN = Path(__file__).resolve().parents[1] / "english_sandbox_after_proto_to_oe.bin"

STRIP_CHARS = "{}* \t"
BREVE_MAP = str.maketrans({"ă": "a", "Ą": "a", "ą": "a", "Ă": "a"})


PROTO_STRIP_RE = re.compile(r"[{}*\s\-/()]")

def normalize_proto(proto: str) -> str:
    return PROTO_STRIP_RE.sub("", proto or "")


def normalize_output(raw: str) -> str:
    cleaned = "".join(ch for ch in raw if ch not in STRIP_CHARS)
    return cleaned.translate(BREVE_MAP)


def normalize_target(raw: str) -> str:
    return raw.strip().translate(BREVE_MAP)


def run_stage(bin_path: Path, proto: str) -> List[str]:
    proc = subprocess.run(
        ["flookup", "-i", str(bin_path)],
        input=f"{proto}\n",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )
    outputs: List[str] = []
    for line in proc.stdout.splitlines():
        if "\t" not in line:
            continue
        _, out = line.split("\t", 1)
        out = out.strip()
        if out and out != "+?":
            outputs.append(out)
    return outputs


def load_oe_rows(tsv_path: Path) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    with tsv_path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if row.get("DOCULECT") != "Old_English":
                continue
            proto = normalize_proto(row.get("PROTO", ""))
            counterpart = row.get("COUNTERPART", "").strip()
            if not proto or not counterpart:
                continue
            rows.append({
                "concept": row.get("CONCEPT", ""),
                "proto": proto,
                "counterpart": counterpart,
            })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tsv", default=str(DEFAULT_TSV), help="Aligned TSV with Old English rows")
    parser.add_argument("--bin", default=str(DEFAULT_BIN), help="Path to english_sandbox_after_proto_to_oe.bin")
    parser.add_argument("--sample", type=int, default=15, help="How many mismatches to print")
    args = parser.parse_args()

    tsv_path = Path(args.tsv).expanduser().resolve()
    bin_path = Path(args.bin).expanduser().resolve()

    rows = load_oe_rows(tsv_path)
    total = len(rows)
    matches = 0
    no_output = 0
    mismatch_examples: List[Dict[str, str]] = []
    issue_counts = {"final_z": 0, "breve": 0, "lost_suffix": 0}

    for row in rows:
        outputs = run_stage(bin_path, row["proto"])
        if not outputs:
            no_output += 1
            row["outputs"] = []
            mismatch_examples.append(row)
            continue
        normalized = [normalize_output(out) for out in outputs]
        target = normalize_target(row["counterpart"])
        row["outputs"] = normalized
        if target in normalized:
            matches += 1
        else:
            mismatch_examples.append(row)
            for out in normalized:
                if out.endswith("z"):
                    issue_counts["final_z"] += 1
                if "ă" in out or "ą" in out:
                    issue_counts["breve"] += 1
                if out.endswith("a") and not target.endswith("a"):
                    issue_counts["lost_suffix"] += 1

    print(f"Total Old English rows: {total}")
    print(f"Matches (stage output equals counterpart): {matches}")
    print(f"No stage output: {no_output}")
    print(f"Mismatches: {total - matches - no_output}")
    if mismatch_examples:
        print("\nSample mismatches:")
        for row in mismatch_examples[: args.sample]:
            outs = ", ".join(row["outputs"]) or "+?"
            print(
                f"- {row['concept']}: proto {row['proto']} => stage {outs} | expected {row['counterpart']}"
            )
    print("\nCommon issues (counts across stage outputs, heuristic):")
    for key, value in issue_counts.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()

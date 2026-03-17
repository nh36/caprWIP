#!/usr/bin/env python3
"""Export Old English sandbox analyzer outputs to JSON."""

import argparse
import csv
import json
import subprocess
from pathlib import Path
from typing import Dict, List

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_TSV = SCRIPT_DIR.parent / "data" / "germanic-aligned-final.tsv"
DEFAULT_OUTPUT = SCRIPT_DIR.parent / "tmp" / "old_english_sandbox_results_current.json"
ANALYZER = "old_english.bin"


def analyze_surface(surface: str, bin_dir: Path) -> List[str]:
    proc = subprocess.run(
        ["flookup", str(bin_dir / ANALYZER)],
        input=f"{surface}\n",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )
    if proc.stderr:
        print(proc.stderr, end="")
    outputs: List[str] = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split("\t", 1)
        proto = parts[1] if len(parts) == 2 else ""
        if proto and proto != "+?":
            outputs.append(proto)
    return outputs


def load_rows(tsv_path: Path) -> List[Dict[str, str]]:
    with tsv_path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        rows = [row for row in reader if row.get("DOCULECT") == "Old_English"]
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Export Old English analyzer results to JSON")
    parser.add_argument("--tsv", default=DEFAULT_TSV, help="Aligned TSV (default: %(default)s)")
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="Destination JSON path (default: %(default)s)",
    )
    parser.add_argument(
        "--bin-dir",
        default=SCRIPT_DIR.parent,
        help="Directory containing old_english.bin (default: %(default)s)",
    )
    args = parser.parse_args()

    tsv_path = Path(args.tsv).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    bin_dir = Path(args.bin_dir).expanduser().resolve()

    rows = load_rows(tsv_path)
    results: List[Dict[str, object]] = []
    success = 0
    for row in rows:
        surface = row.get("COUNTERPART", "").strip()
        if not surface:
            continue
        outputs = analyze_surface(surface, bin_dir)
        if outputs:
            success += 1
        results.append(
            {
                "concept": row.get("CONCEPT", ""),
                "proto": row.get("PROTO", ""),
                "counterpart": surface,
                "doculect": row.get("DOCULECT", ""),
                "outputs": outputs,
            }
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    total = len(results)
    print(f"Wrote {total} entries to {output_path}")
    print(f"Analyzer successes: {success}/{total}")


if __name__ == "__main__":
    main()

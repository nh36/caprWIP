#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
INVENTORY_PATH = ROOT.parent / "sound_change_inventory.tsv"


def load_inventory_order() -> dict[str, int]:
    with INVENTORY_PATH.open(encoding="utf-8") as handle:
        rows = csv.DictReader(handle, delimiter="\t")
        return {
            (row["change_id"] or "").strip(): int((row["current_order"] or "").strip())
            for row in rows
            if (row.get("change_id") or "").strip() and (row.get("current_order") or "").strip()
        }


def parse_chapter_files(build_script: Path) -> list[str]:
    text = build_script.read_text(encoding="utf-8")
    match = re.search(r"chapter_files\s*=\s*(\[[^\]]*\])", text, re.S)
    if not match:
        raise ValueError(f"Could not find chapter_files list in {build_script}")
    return list(ast.literal_eval(match.group(1)))


def chapter_sc_numbers(path: Path) -> list[str]:
    numbers: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"##\s+SC(\d{3})\.\s", line)
        if match:
            numbers.append(f"SC{match.group(1)}")
    if not numbers:
        raise ValueError(f"No SC-numbered rule headings found in {path}")
    return numbers


def verify(build_script: Path) -> tuple[list[str], list[str], list[str]]:
    inventory_order = load_inventory_order()
    chapter_files = parse_chapter_files(build_script)
    flattened: list[str] = []

    for name in chapter_files:
        chapter_path = ROOT / name
        if not chapter_path.exists():
            raise FileNotFoundError(f"Missing chapter file in build list: {chapter_path}")
        numbers = chapter_sc_numbers(chapter_path)
        missing = [change_id for change_id in numbers if change_id not in inventory_order]
        if missing:
            raise ValueError(f"Unknown SC id(s) in {name}: {missing}")
        chapter_expected = sorted(numbers, key=lambda change_id: inventory_order[change_id])
        if numbers != chapter_expected:
            raise ValueError(f"Internal SC order mismatch in {name}: {numbers} vs {chapter_expected}")
        flattened.extend(numbers)

    current_orders = [inventory_order[change_id] for change_id in flattened]
    if current_orders != sorted(current_orders):
        raise ValueError(f"Chapter order mismatch: {flattened} vs nondecreasing current_order expectation")

    unique_flattened: list[str] = []
    seen_nonadjacent: set[str] = set()
    for change_id in flattened:
        if unique_flattened and unique_flattened[-1] == change_id:
            continue
        if change_id in seen_nonadjacent:
            raise ValueError(f"Non-adjacent repeated SC id in build order: {change_id}")
        unique_flattened.append(change_id)
        seen_nonadjacent.add(change_id)

    unique_orders = [inventory_order[change_id] for change_id in unique_flattened]
    if unique_orders != sorted(unique_orders):
        raise ValueError(f"Unique SC order mismatch: {unique_flattened} vs sorted current_order expectation")

    return chapter_files, flattened, unique_flattened


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify reader-facing chapter order against the canonical sound-change inventory.")
    parser.add_argument(
        "--build-script",
        type=Path,
        default=ROOT / "build_reader_facing_local_section_02_docker.sh",
        help="Build script whose chapter_files list should be checked.",
    )
    args = parser.parse_args()

    chapter_files, flattened, unique_flattened = verify(args.build_script.resolve())
    print(f"Verified reader-facing order for {args.build_script}")
    print("Chapters:")
    for chapter in chapter_files:
        print(f"  - {chapter}")
    print("SC order:")
    print("  " + ", ".join(flattened))
    print("Unique SC order:")
    print("  " + ", ".join(unique_flattened))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

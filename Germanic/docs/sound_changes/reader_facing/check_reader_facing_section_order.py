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


def verify(build_script: Path) -> tuple[list[str], list[str]]:
    inventory_order = load_inventory_order()
    chapter_files = parse_chapter_files(build_script)
    flattened: list[str] = []

    for name in chapter_files:
        chapter_path = ROOT / name
        if not chapter_path.exists():
            raise FileNotFoundError(f"Missing chapter file in build list: {chapter_path}")
        numbers = chapter_sc_numbers(chapter_path)
        chapter_expected = sorted(numbers, key=lambda change_id: inventory_order[change_id])
        if numbers != chapter_expected:
            raise ValueError(f"Internal SC order mismatch in {name}: {numbers} vs {chapter_expected}")
        flattened.extend(numbers)

    current_orders = [inventory_order[change_id] for change_id in flattened]
    if current_orders != sorted(current_orders):
        raise ValueError(f"Chapter order mismatch: {flattened} vs nondecreasing current_order expectation")

    unique_flattened: list[str] = []
    for change_id in flattened:
        if not unique_flattened or unique_flattened[-1] != change_id:
            unique_flattened.append(change_id)

    unique_orders = [inventory_order[change_id] for change_id in unique_flattened]
    if unique_orders[0] != 49 or unique_orders[-1] != 61:
        raise ValueError(f"Expected local section to span SC049..SC061, got orders {unique_orders[0]}..{unique_orders[-1]}")
    if unique_orders != list(range(49, 62)):
        raise ValueError(f"Expected contiguous unique current_order range 49..61, got {unique_orders}")

    return chapter_files, flattened


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify reader-facing chapter order against the canonical sound-change inventory.")
    parser.add_argument(
        "--build-script",
        type=Path,
        default=ROOT / "build_reader_facing_local_section_02_docker.sh",
        help="Build script whose chapter_files list should be checked.",
    )
    args = parser.parse_args()

    chapter_files, flattened = verify(args.build_script.resolve())
    print(f"Verified reader-facing order for {args.build_script}")
    print("Chapters:")
    for chapter in chapter_files:
        print(f"  - {chapter}")
    print("SC order:")
    print("  " + ", ".join(flattened))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

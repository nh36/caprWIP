"""API regression harness for CAPR pipelines.

Run this script against a live backend (e.g. ``docker compose up -d``) to
exercise ``/new-board`` and ``/compare-fst`` for the Burmish and Germanic
pipelines. The goal is an early warning if syllable parsing or correspondence
generation regresses.

Example::

    python server/tools/api_regression.py

Pass ``--base-url`` if the API is reachable somewhere else.
"""

from __future__ import annotations

import argparse
import sys
import time
from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence, Tuple

import requests


@dataclass
class CompareSpec:
    pipeline: str
    data_path: str
    transducer_name: str
    pairs: Sequence[Tuple[str, str]]
    expected_missing: Sequence[str]


SPECS: Sequence[CompareSpec] = (
    CompareSpec(
        pipeline="burmish",
        data_path="burmish-aligned-final.tsv",
        transducer_name="burmish.txt",
        pairs=(("Atsi", "Maru"),),
        expected_missing=("Rangoon",),
    ),
    CompareSpec(
        pipeline="germanic",
        data_path="germanic-aligned-final.tsv",
        transducer_name="germanic.txt",
        pairs=(("English", "German"),),
        expected_missing=(),
    ),
)


def fetch_json(method: str, url: str, **kwargs) -> Dict:
    response = requests.request(method, url, timeout=30, **kwargs)
    response.raise_for_status()
    return response.json()


def validate_syllables(board: Dict) -> Tuple[bool, str]:
    words = board.get("words", {})
    if not words:
        return False, "Board payload is missing 'words'"

    missing = []
    for word in words.values():
        syllables: List = word.get("syllables", [])
        parsed: List = word.get("syllables_parsed", [])
        if syllables and (len(syllables) != len(parsed) or not parsed):
            missing.append(word.get("id", "<unknown>"))
            if len(missing) >= 5:
                break

    if missing:
        preview = ", ".join(missing)
        return False, f"Parsed syllables missing or length mismatch (examples: {preview})"

    return True, ""


def validate_chapters(chapters: Dict, langs: Sequence[str]) -> Tuple[bool, str]:
    total_rows = 0
    for sections in chapters.values():
        for section in sections:
            if isinstance(section, dict):
                total_rows += len(section.get("rows", []))
    if total_rows == 0:
        return False, "No correspondence rows returned"

    return True, ""


def run_spec(base_url: str, spec: CompareSpec) -> Tuple[bool, List[str]]:
    errors: List[str] = []

    board = fetch_json(
        "POST",
        f"{base_url}/new-board",
        json={"dataPath": spec.data_path, "transducer": "internal"},
    )

    ok, message = validate_syllables(board)
    if not ok:
        errors.append(f"[{spec.pipeline}] {message}")

    transducer = fetch_json(
        "POST", f"{base_url}/get-transducers", json={"name": spec.transducer_name}
    )["transducer"]

    for pair in spec.pairs:
        langs = list(pair)
        compare = fetch_json(
            "POST",
            f"{base_url}/compare-fst",
            json={
                "langsUnderStudy": langs,
                "oldTransducer": transducer,
                "newTransducer": transducer,
                "board": board,
            },
        )

        missing = set(compare.get("missing_transducers", []))
        unexpected_missing = missing.difference(spec.expected_missing)
        if unexpected_missing:
            errors.append(
                f"[{spec.pipeline} {pair}] unexpected missing transducers: {sorted(unexpected_missing)}"
            )

        ok, message = validate_chapters(compare.get("chapters", {}), langs)
        if not ok:
            errors.append(f"[{spec.pipeline} {pair}] {message}")

    return not errors, errors


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="CAPR API regression harness")
    parser.add_argument(
        "--base-url",
        default="http://127.0.0.1:5001",
        help="Root URL of the CAPR backend (default: http://127.0.0.1:5001)",
    )
    args = parser.parse_args(argv)

    base_url: str = args.base_url.rstrip("/")

    start = time.time()
    overall_errors: List[str] = []

    try:
        for spec in SPECS:
            ok, errors = run_spec(base_url, spec)
            if errors:
                overall_errors.extend(errors)
            label = f"{spec.pipeline} ({spec.data_path})"
            status = "PASS" if ok else "FAIL"
            print(f"{status:<5} {label}")

        duration = time.time() - start
        print(f"\nCompleted in {duration:.1f}s")

        if overall_errors:
            print("\nIssues detected:")
            for err in overall_errors:
                print(f" - {err}")
            return 1

        return 0
    except requests.RequestException as exc:
        print(f"Error communicating with {base_url}: {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main())

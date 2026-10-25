#!/usr/bin/env python3
"""Verify the corrective acquisition manifest, locally or in a clean checkout."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
from pathlib import Path
import re
import unicodedata


RECORD = Path("docs/references/ga_prefix_2026-10-25")


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def best_span(reference: str, text: str) -> tuple[int, str, int]:
    def normal(value: str) -> str:
        return re.sub(r"\s+", " ", unicodedata.normalize("NFC", value)).strip()

    reference, text = normal(reference), normal(text)
    previous, starts = [0] * (len(text) + 1), list(range(len(text) + 1))
    for i, letter in enumerate(reference, 1):
        current, next_starts = [i], [0]
        for j, other in enumerate(text, 1):
            cost, start = min(
                (previous[j - 1] + (letter != other), starts[j - 1]),
                (previous[j] + 1, starts[j]),
                (current[j - 1] + 1, next_starts[j - 1]),
            )
            current.append(cost)
            next_starts.append(start)
        previous, starts = current, next_starts
    end = min(range(len(previous)), key=lambda j: previous[j])
    return previous[end], text[starts[end]:end], len(reference)


def check_ocr(root: Path) -> None:
    results = []
    for sample_id, sample in enumerate(rows(root / RECORD / "ocr_reference_sample.tsv"), 1):
        for method in ["native", "tesseract", "vision"]:
            candidate = root / "docs/references/local/ga-prefix/ocr-comparison" / (
                f"{sample['source']}-{int(sample['pdf_sheet']):03}.{method}.txt"
            )
            distance, observed, length = best_span(sample["reference"], candidate.read_text())
            results.append(dict(
                sample_id=sample_id, source=sample["source"], pdf_sheet=sample["pdf_sheet"],
                category=sample["category"], method=method, reference=sample["reference"],
                observed=observed, edit_distance=distance, reference_characters=length,
            ))
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=list(results[0]), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(results)
    if output.getvalue() != (root / RECORD / "ocr_comparison.tsv").read_text():
        raise ValueError("OCR comparison differs from the recorded checked sample")
    print(f"PASS: {len(results)} reproducible sample/method comparisons")


def verify(root: Path, require_local: bool) -> None:
    holdings = rows(root / RECORD / "holdings.tsv")
    if len(holdings) != 12 or len({row["text_path"] for row in holdings}) != 12:
        raise ValueError("Expected 12 distinct canonical text holdings")
    keys = re.findall(r"(?m)^@\w+\s*\{\s*([^,\s]+)", (root / "docs/refs.bib").read_text())
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate bibliography keys")
    missing, checked, pdfs = [], 0, 0
    for holding in holdings:
        if holding["citation_key"] not in keys:
            raise ValueError(f"Unknown citation key: {holding['citation_key']}")
        pdf, text_path = root / holding["pdf_path"], root / holding["text_path"]
        if pdf.exists():
            if digest(pdf) != holding["pdf_sha256"]:
                raise ValueError(f"PDF checksum mismatch: {pdf}")
            pdfs += 1
        else:
            missing.append(holding["pdf_path"])
        if not text_path.exists():
            if holding["access"] == "public_domain_git":
                raise ValueError(f"Missing public text: {text_path}")
            missing.append(holding["text_path"])
            continue
        if digest(text_path) != holding["text_sha256"]:
            raise ValueError(f"Text checksum mismatch: {text_path}")
        text = text_path.read_text()
        if holding["pdf_sha256"] not in text:
            raise ValueError(f"Missing source identity: {text_path}")
        mapping = rows(root / holding["page_map"])
        if holding["map_id"] == "WrightWuelcker1884II":
            expected = [(int(row["pdf_sheet"]), row["publication_page"]) for row in mapping]
        else:
            expected = [
                (int(row["pdf_sheet"]), row["publication_page_or_slide"])
                for row in mapping if row["intake_id"] == holding["map_id"]
            ]
        markers = [(int(n), label) for n, label in re.findall(
            r"^=== PDF sheet (\d+); page (.+) ===$", text, re.M
        )]
        if markers != expected or [n for n, _ in markers] != list(range(1, int(holding["pdf_sheets"]) + 1)):
            raise ValueError(f"Page marker mismatch: {text_path}")
        checked += 1
    print(f"PASS: {checked}/12 canonical texts; {pdfs}/12 canonical PDF hashes")
    if missing:
        print("UNAVAILABLE IN THIS CHECKOUT: " + ", ".join(missing))
        if require_local:
            raise ValueError("Authorised local holding restoration is incomplete")
    else:
        print("PASS: all 1,108 sheet markers and complete authorised local holdings")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--require-local", action="store_true")
    parser.add_argument("--check-ocr", action="store_true")
    args = parser.parse_args()
    try:
        verify(args.root, args.require_local)
        if args.check_ocr:
            check_ocr(args.root)
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"FAIL: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Prepare and verify the locally supplied world/prosody reference intake."""
import argparse
import csv
import hashlib
import io
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
RECORD = Path(__file__).resolve().parent
LOCAL = ROOT / "docs/references/local/world-2026-10-26"
HOLDINGS = [
    ("Fulk2010", "fulk_2010_high_vowel_deletion", 19, 1, 19, 126),
    ("Fulk2022", "fulk_2022_metre_editorial_concern", 8, 1, 8, 11),
    ("Britton1996", "britton_1996_english_historical_linguistics", 412, 1, 412, None),
    ("Hogg1996", "britton_1996_english_historical_linguistics", 412, 12, 21, 3),
    ("Minkova1996", "britton_1996_english_historical_linguistics", 412, 22, 47, 13),
    ("Goering2023", "goering_2023_heafudu_problem", 28, 1, 28, None),
    ("Cermak2005", "cermak_2005_obscured_compounds", 12, 1, 12, None),
    ("Sauer1992", "sauer_1992_nominalkomposita", 768, 1, 768, None),
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def prepared():
    texts, maps, holdings = {}, [], []
    for key, stem, extent, first, last, first_page in HOLDINGS:
        pdf = ROOT / "docs/references" / (stem + ".pdf")
        pdf_hash = digest(pdf.read_bytes())
        if stem not in texts:
            result = subprocess.run(
                ["pdftotext", "-layout", str(pdf), "-"],
                capture_output=True, check=True)
            if result.stderr:
                diagnostics = result.stderr.decode().splitlines()
                warnings = sorted(set(diagnostics))
                print(f"{stem}: {len(diagnostics)} extraction diagnostics "
                      f"({len(warnings)} distinct): {'; '.join(warnings)}",
                      file=sys.stderr)
            native = result.stdout
            pages = native.decode().split("\f")
            if pages[-1].strip():
                raise ValueError("Missing final PDF page break: " + stem)
            pages.pop()
            if len(pages) != extent:
                raise ValueError(f"Unexpected sheet count: {stem}: {len(pages)}")
            texts[stem] = pages
        pages = texts[stem]
        chunks = [f"Source: {key}\nPDF SHA256: {pdf_hash}\n"
                  "Local-only searchable navigation; PDF glyphs remain authoritative.\n"]
        current = 52
        for sheet in range(first, last + 1):
            page = pages[sheet - 1]
            if key == "Goering2023":
                anchors = [int(n) for n in re.findall(r"\bp\.\s*(\d+)", page)]
                labels = sorted({current, *anchors})
                label = ",".join(map(str, labels)) if sheet <= 25 else "endnotes"
                if anchors:
                    current = anchors[-1]
                basis = "publisher reflow; in-text print-page anchors, not facsimile sheets"
            elif key == "Cermak2005":
                label = "unnumbered (blank)" if sheet == 1 else str(sheet + 33)
                basis = "blank opening sheet; printed35--45 on sheets2--12"
            elif key == "Sauer1992":
                front = "V VI VII VIII IX X XI XII XIII XIV XV XVI XVII XVIII XIX XX XXI XXII XXIII XXIV XXV XXVI XXVII XXVIII".split()
                label = (str(sheet - 28) if sheet >= 29 else
                         front[sheet - 5] if sheet >= 5 else "unnumbered")
                basis = "frontmatter separated; printed page = PDF sheet minus28"
            elif key == "Britton1996":
                if sheet < 10:
                    label = {6: "v", 7: "vi", 8: "vii", 9: "viii"}.get(sheet, "unnumbered")
                else:
                    label = str(sheet - 9)
                basis = "sequence; selected article boundaries and running folios checked"
            else:
                label = str(first_page + sheet - first)
                basis = "printed article pagination; sequential within supplied PDF"
            maps.append(dict(
                citation_key=key, pdf_sheet=sheet, printed_page_or_range=label,
                mapping_basis=basis))
            chunks.append(f"=== PDF sheet {sheet:03}; page {label} ===\n{page.rstrip()}\n")
        text = "\n\f\n".join(chunks).encode()
        path = LOCAL / (key + ".txt")
        holdings.append(dict(
            citation_key=key, pdf_path=str(pdf.relative_to(ROOT)),
            pdf_sha256=pdf_hash, pdf_sheets=extent,
            first_sheet=first, last_sheet=last,
            text_path=str(path.relative_to(ROOT)), text_sha256=digest(text),
            access="local_only", extraction="pdftotext -layout"))
        yield path, text
    for filename, records in [("holdings.tsv", holdings), ("page_map.tsv", maps)]:
        stream = io.StringIO()
        writer = csv.DictWriter(stream, fieldnames=list(records[0]),
                                delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)
        yield RECORD / filename, stream.getvalue().encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        LOCAL.mkdir(parents=True, exist_ok=True)
    count = 0
    for path, content in prepared():
        if args.check:
            if not path.exists() or path.read_bytes() != content:
                raise ValueError("Absent or stale holding/page map: " + str(path))
        else:
            path.write_bytes(content)
        count += 1
    print(f"PASS: {count - 2} complete searchable holdings and exact page-map/hash records")


if __name__ == "__main__":
    main()

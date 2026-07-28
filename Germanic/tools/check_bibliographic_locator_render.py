#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


TEX_CITEPROC_LOCATOR_RE = re.compile(
    r"\\citeproc\{[^{}]+\}\{[^{}]*\bsects?\.?\s+[0-9]",
    re.IGNORECASE,
)
PDF_LOCATOR_RE = re.compile(r"\bsects?\.?\s+[0-9]", re.IGNORECASE)


def count_tex_locators(tex_path: Path) -> int:
    text = tex_path.read_text(encoding="utf-8")
    return len(TEX_CITEPROC_LOCATOR_RE.findall(text))


def count_pdf_locators(pdf_path: Path) -> int:
    proc = subprocess.run(
        ["pdftotext", str(pdf_path), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    return len(PDF_LOCATOR_RE.findall(proc.stdout))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex-path", type=Path, required=True)
    parser.add_argument("--pdf-path", type=Path, required=True)
    args = parser.parse_args()

    tex_path = args.tex_path.expanduser().resolve()
    pdf_path = args.pdf_path.expanduser().resolve()

    tex_remaining = count_tex_locators(tex_path)
    pdf_remaining = count_pdf_locators(pdf_path)

    print("Bibliographic locator check:")
    print(f"  sect/sects citation locators remaining in TeX: {tex_remaining}")
    print(f"  sect/sects citation locators remaining in PDF: {pdf_remaining}")

    if tex_remaining != 0 or pdf_remaining != 0:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

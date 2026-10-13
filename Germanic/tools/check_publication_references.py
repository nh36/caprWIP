#!/usr/bin/env python3
"""Check rendered LaTeX destinations and the actual PDF build's warnings."""
from __future__ import annotations

import argparse
from pathlib import Path
import re


def problems(tex: str, log: str) -> list[str]:
    destinations = set(re.findall(r"\\(?:label|hypertarget)\{([^{}]+)\}", tex))
    references = set(re.findall(
        r"\\(?:hyperlink|(?:page|eq|auto|name)?ref)\*?\{([^{}]+)\}", tex))
    references.update(re.findall(r"\\hyperref\[([^\]]+)\]", tex))
    errors = [f"undefined internal destination: {name}"
              for name in sorted(references - destinations)]
    if re.search(r"(?:Hyper reference|Reference|Citation)\b[\s\S]{0,400}?\bundefined\b"
                 r"|There were undefined references|destination.*does not exist", log):
        errors.append("PDF build reported undefined references or citations")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex-path", type=Path, required=True)
    parser.add_argument("--log-path", type=Path, required=True)
    parser.add_argument("--pdf-path", type=Path, required=True)
    args = parser.parse_args()
    errors = problems(args.tex_path.read_text(), args.log_path.read_text())
    if not args.pdf_path.read_bytes().startswith(b"%PDF-"):
        errors.append("rendered PDF missing or invalid")
    for error in errors:
        print(error)
    if errors:
        return 1
    print("Publication references: zero unresolved internal references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

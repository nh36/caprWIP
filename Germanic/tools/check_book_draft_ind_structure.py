#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ASSEMBLY_DIR = REPO_ROOT / "Germanic/docs/assembly"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--assembly-dir", type=Path, default=DEFAULT_ASSEMBLY_DIR)
    args = parser.parse_args()

    assembly_dir = args.assembly_dir.expanduser().resolve()

    ind_files = sorted(assembly_dir.glob("*.ind"))
    assert len(ind_files) == 1, f"Expected exactly one unified .ind file; found: {[p.name for p in ind_files]}"
    ind_path = ind_files[0]

    assert ind_path.stem == "iv", f"Unified index stream should be iv.ind; found {ind_path.name}"
    legacy_streams = [p for p in assembly_dir.glob("*.ind") if p.stem != "iv"]
    assert not legacy_streams, f"Legacy per-language .ind streams found: {[p.name for p in legacy_streams]}"

    text = ind_path.read_text(encoding="utf-8")
    heading_re = re.compile(r"\\item\s+\\ivlangheader\{([^}]+)\}")
    headings = list(heading_re.finditer(text))
    heading_titles = [match.group(1).strip() for match in headings]

    idx_path = assembly_dir / "iv.idx"
    assert idx_path.exists(), f"Missing iv.idx source stream for unified index: {idx_path.name}"
    idx_text = idx_path.read_text(encoding="utf-8")
    idx_groups = re.findall(r"([0-9]{2}[a-z0-9_]+)@\\ivlangheader\{([^}]+)\}\{[^}]*\}!", idx_text)
    assert idx_groups, "iv.idx contains no unified language-group index entries."

    prefix_to_title: dict[str, str] = {}
    for prefix, title in idx_groups:
        prefix_to_title.setdefault(prefix, title.strip())
    expected_titles = [prefix_to_title[prefix] for prefix in sorted(prefix_to_title)]

    assert heading_titles, "Unified .ind contains no language headings."
    assert len(heading_titles) == len(set(heading_titles)), f"Language headings are duplicated: {heading_titles}"
    assert heading_titles == expected_titles, (
        "Language heading order/content mismatch.\n"
        f"Expected: {expected_titles}\n"
        f"Actual:   {heading_titles}"
    )

    for idx, heading in enumerate(headings):
        start = heading.end()
        end = headings[idx + 1].start() if idx + 1 < len(headings) else len(text)
        block = text[start:end]
        assert r"\subitem " in block, f"Language heading has no form entries: {heading.group(1)!r}"

    ilg_path = ind_path.with_suffix(".ilg")
    assert ilg_path.exists(), f"Missing MakeIndex log for unified stream: {ilg_path.name}"
    ilg_text = ilg_path.read_text(encoding="utf-8")

    accepted_match = re.search(r"(\d+)\s+(?:entries\s+)?accepted", ilg_text)
    assert accepted_match is not None, "Could not parse 'entries accepted' from MakeIndex log."
    assert int(accepted_match.group(1)) > 0, "MakeIndex accepted zero entries for the unified index."

    rejected_match = re.search(r"(\d+)\s+(?:entries\s+)?rejected", ilg_text)
    assert rejected_match is not None, "Could not parse 'entries rejected' from MakeIndex log."
    assert int(rejected_match.group(1)) == 0, "MakeIndex rejected one or more index entries."

    print("book draft .ind structure checks passed")


if __name__ == "__main__":
    main()

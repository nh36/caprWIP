#!/usr/bin/env python3
"""Stage 4A shadow checker for broad-prose passage-adjacent placement."""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BOOK_DIR = REPO_ROOT / "Germanic/docs/book"
ASSEMBLY_DIR = REPO_ROOT / "Germanic/docs/assembly"
TOOLS_DIR = REPO_ROOT / "Germanic/tools"

sys.path.insert(0, str(TOOLS_DIR))
sys.path.insert(0, str(ASSEMBLY_DIR))

from build_full_lexical_volume import build_lexical_volume
from build_capr_book_draft import build_book_markdown, BookEmission
from index_verborum_broad_prose_placement import (
    load_broad_prose_inventory,
    build_passage_anchor_requests,
)

FILTER_LUA = TOOLS_DIR / "index_verborum_filter.lua"
BOOK_EMISSIONS_TSV = BOOK_DIR / "index_verborum_book_emissions.tsv"
EXPLICIT_PLAN_TSV = BOOK_DIR / "index_verborum_book_explicit_plan.tsv"
CANONICAL_LEXICAL_MD = ASSEMBLY_DIR / "lexical_volume_alpha_01.md"
CANONICAL_BOOK_MD = ASSEMBLY_DIR / "capr_book_draft_alpha_01.md"


def _load_tsv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def _extract_anchor_ids(md_text: str) -> list[str]:
    return re.findall(
        r':::\s*\{[^}]*\.iv-anchor[^}]*emission_id="([^"]+)"[^}]*\}\s*\n:::',
        md_text,
    )


def _strip_shadow_anchors_exact(shadow_text: str, anchor_ids: list[str]) -> str:
    result = shadow_text
    for eid in anchor_ids:
        safe = eid.replace('"', '&quot;')
        bare = f'::: {{.iv-anchor emission_id="{safe}"}}\n:::'
        result = result.replace(bare, '')
    return re.sub(r"\n{3,}", "\n\n", result)


def _strip_anchor_blocks(md_text: str) -> str:
    return _strip_shadow_anchors_exact(md_text, _extract_anchor_ids(md_text))


def _extract_iv_commands(tex_text: str) -> list[str]:
    out: list[str] = []
    prefix = r"\index[iv]{"
    i = 0
    n = len(tex_text)
    while i < n:
        j = tex_text.find(prefix, i)
        if j < 0:
            break
        k = j + len(prefix)
        depth = 1
        while k < n and depth > 0:
            ch = tex_text[k]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            k += 1
        if depth != 0:
            raise ValueError("unbalanced \\index[iv]{...} in TeX output")
        out.append(tex_text[j : k])
        i = k
    return out


def _strip_iv_commands_from_line(line: str) -> str:
    prefix = r"\index[iv]{"
    result: list[str] = []
    i = 0
    while i < len(line):
        j = line.find(prefix, i)
        if j < 0:
            result.append(line[i:])
            break
        result.append(line[i:j])
        k = j + len(prefix)
        depth = 1
        while k < len(line) and depth > 0:
            if line[k] == "{":
                depth += 1
            elif line[k] == "}":
                depth -= 1
            k += 1
        if depth != 0:
            raise ValueError("unbalanced \\index[iv]{...} in TeX output")
        i = k
    return "".join(result)


def _remove_iv_commands_narrow(tex_text: str) -> str:
    prefix = r"\index[iv]{"
    lines_info: list[tuple[str, bool]] = []
    for line in tex_text.split("\n"):
        if prefix not in line:
            lines_info.append((line, False))
            continue
        cleaned = _strip_iv_commands_from_line(line)
        created_by_removal = line.strip() != "" and cleaned.strip() == ""
        lines_info.append((cleaned, created_by_removal))

    output: list[str] = []
    i = 0
    while i < len(lines_info):
        line, _ = lines_info[i]
        if line == "":
            run_removals: list[bool] = []
            j = i
            while j < len(lines_info) and lines_info[j][0] == "":
                run_removals.append(lines_info[j][1])
                j += 1
            if any(run_removals):
                output.append("")
            else:
                output.extend([""] * len(run_removals))
            i = j
            continue
        output.append(line)
        i += 1
    return "\n".join(output)


def _remove_iv_commands_from_line(line: str) -> str:
    """Remove all \index[iv]{...} commands from a single line."""
    return _strip_iv_commands_from_line(line)


def _parse_makeindex_output(output: str, filename: str = "") -> tuple[int, int]:
    """Parse MakeIndex stdout/stderr for accepted/rejected counts."""
    accepted = None
    rejected = None
    for line in output.splitlines():
        m_acc = re.search(r"(\d+)\s+entries accepted", line)
        m_rej = re.search(r"(\d+)\s+rejected", line)
        if m_acc:
            accepted = int(m_acc.group(1))
        if m_rej:
            rejected = int(m_rej.group(1))
    label = f" in {filename}" if filename else ""
    if accepted is None:
        raise ValueError(f"makeindex output missing 'entries accepted' line{label}: {output[:200]!r}")
    if rejected is None:
        raise ValueError(f"makeindex output missing 'rejected' line{label}: {output[:200]!r}")
    return accepted, rejected


def _parse_idx_entries(idx_text: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    prefix = r"\indexentry{"
    i = 0
    while i < len(idx_text):
        j = idx_text.find(prefix, i)
        if j < 0:
            break
        k = j + len(prefix)
        depth = 1
        while k < len(idx_text) and depth > 0:
            if idx_text[k] == "{":
                depth += 1
            elif idx_text[k] == "}":
                depth -= 1
            k += 1
        if depth != 0:
            raise ValueError(r"unbalanced \indexentry{...} in IDX output")
        command = idx_text[j + len(prefix) : k - 1]
        if k >= len(idx_text) or idx_text[k] != "{":
            raise ValueError("missing page-number brace in IDX output")
        page_start = k + 1
        depth = 1
        k = page_start
        while k < len(idx_text) and depth > 0:
            if idx_text[k] == "{":
                depth += 1
            elif idx_text[k] == "}":
                depth -= 1
            k += 1
        if depth != 0:
            raise ValueError("unbalanced page-number brace in IDX output")
        # Strip |pagespec suffix added by hyperref (e.g., |hyperpage)
        # This is always at the top level of the key, not inside nested braces
        canonical_key = command.rsplit("|", 1)[0] if "|" in command else command
        entries.append({"key": canonical_key, "page": idx_text[page_start : k - 1]})
        i = k
    return entries


def _load_canonical_iv_commands() -> list[str]:
    rows = _load_tsv_rows(BOOK_EMISSIONS_TSV)
    return [
        (row.get("index_command") or "").strip()
        for row in rows
        if (row.get("index_command") or "").strip()
    ]


def _extract_index_key(index_command: str) -> str:
    """Extract the complete key from \\index[iv]{...} using balanced-brace parsing."""
    prefix = r"\index[iv]{"
    if not index_command.startswith(prefix):
        raise ValueError(f"not an \\index[iv]{{...}} command: {index_command!r}")
    i = len(prefix)
    depth = 1
    while i < len(index_command) and depth > 0:
        if index_command[i] == "{":
            depth += 1
        elif index_command[i] == "}":
            depth -= 1
        i += 1
    if depth != 0:
        raise ValueError(f"unbalanced braces in index command: {index_command!r}")
    return index_command[len(prefix) : i - 1]


def _idx_page_impact_analysis(
    prod_idx_text: str,
    shadow_idx_text: str,
    canonical_commands: list[str],
    movable_emission_ids: list[str],
    movable_records: list,  # list of PlacementRecord
) -> dict[str, object]:
    """Compare production vs shadow iv.idx using exact complete keys.

    Returns summary dict with corrected counts based on complete canonical keys
    (not display-only IND keys).
    """
    expected_keys = Counter(
        _extract_index_key(cmd) for cmd in canonical_commands
    )
    expected_key_set = set(expected_keys.keys())
    expected_total = len(canonical_commands)
    expected_unique = len(expected_key_set)

    # Parse both IDX files
    prod_entries = _parse_idx_entries(prod_idx_text)
    shadow_entries = _parse_idx_entries(shadow_idx_text)

    # Build key → page-label lists
    def _build_page_map(entries: list[dict[str, str]]) -> dict[str, list[str]]:
        pages: dict[str, list[str]] = {}
        for e in entries:
            key = e["key"]
            pages.setdefault(key, []).append(e["page"])
        return pages

    prod_pages = _build_page_map(prod_entries)
    shad_pages = _build_page_map(shadow_entries)

    prod_key_set = set(prod_pages.keys())
    shad_key_set = set(shad_pages.keys())

    # Build emission_id → canonical key mapping via PlacementRecord
    emission_to_key: dict[str, str] = {}
    for rec in movable_records:
        if rec.canonical_index_key:
            emission_to_key[rec.emission_id] = rec.canonical_index_key

    # Compare by exact key
    all_keys = prod_key_set | shad_key_set
    unchanged = changed = 0
    pages_added_count = pages_removed_count = 0
    changed_entries: list[dict[str, object]] = []
    changed_key_emission_ids: set[str] = set()

    for key in sorted(all_keys):
        prod_list = prod_pages.get(key, [])
        shad_list = shad_pages.get(key, [])
        if sorted(set(prod_list)) == sorted(set(shad_list)):
            unchanged += 1
        else:
            changed += 1
            prod_set = set(prod_list)
            shad_set = set(shad_list)
            added = sorted(shad_set - prod_set)
            removed = sorted(prod_set - shad_set)
            pages_added_count += len(added)
            pages_removed_count += len(removed)
            # Find associated movable emission IDs
            assoc_ids = [eid for eid, k in emission_to_key.items() if k == key]
            changed_key_emission_ids.update(assoc_ids)
            changed_entries.append({
                "key": key,
                "prod_pages": prod_list,
                "shadow_pages": shad_list,
                "pages_added": added,
                "pages_removed": removed,
                "moved_emission_ids": assoc_ids,
            })

    return {
        "expected_total_commands": expected_total,
        "expected_unique_keys": expected_unique,
        "prod_idx_total": len(prod_entries),
        "shadow_idx_total": len(shadow_entries),
        "prod_unique_keys": len(prod_key_set),
        "shadow_unique_keys": len(shad_key_set),
        "total_exact_entries": len(all_keys),
        "unchanged": unchanged,
        "changed": changed,
        "pages_added_count": pages_added_count,
        "pages_removed_count": pages_removed_count,
        "changed_entries": changed_entries[:20],
        "changed_key_emission_ids": sorted(changed_key_emission_ids),
        "prod_idx_matches_canonical_count": len(prod_entries) == expected_total,
        "prod_idx_matches_canonical_keys": prod_key_set == expected_key_set,
        "shadow_idx_matches_canonical_keys": shad_key_set == expected_key_set,
    }


def _split_pdf_text(pdf_text: str, label: str) -> tuple[str, str]:
    """Split PDF text into body and Index Verborum sections.

    Uses 'Index verborum' heading on its own page as the split boundary.
    The Table of Contents also contains "Index verborum" but it appears
    inline in a multi-entry page. The actual index starts on its own page
    where "Index verborum" is the first non-whitespace content.
    Raises if the boundary cannot be identified uniquely.
    """
    # Split on form-feed page boundaries
    pages = pdf_text.split("\f")
    iv_page_indices = []
    for i, page in enumerate(pages):
        stripped = page.strip()
        # The actual IV index page starts with "Index verborum" as its first content
        # The TOC page has it as an entry within other content
        if stripped.startswith("Index verborum") or stripped.startswith("Index Verborum"):
            iv_page_indices.append(i)

    if not iv_page_indices:
        # Fall back to first occurrence anywhere (handles TOC-only match)
        for i, page in enumerate(pages):
            if "Index verborum" in page or "Index Verborum" in page:
                iv_page_indices.append(i)
                break

    if not iv_page_indices:
        raise AssertionError(f"{label}: PDF text missing 'Index verborum' heading")
    if len(iv_page_indices) > 1:
        raise AssertionError(
            f"{label}: multiple Index Verborum page boundaries found ({len(iv_page_indices)} pages)"
        )

    split_page = iv_page_indices[0]
    body = "\f".join(pages[:split_page])
    index_section = "\f".join(pages[split_page:])
    return body, index_section


def _run_pandoc(md_text: str, *, label: str) -> str:
    env = dict(os.environ)
    env.update(
        {
            "CAPR_IV_BOOK_EMISSIONS_TSV": str(BOOK_EMISSIONS_TSV),
            "CAPR_IV_EXPLICIT_PLAN_TSV": str(EXPLICIT_PLAN_TSV),
            "CAPR_IV_REQUIRE_EXPLICIT_COMPLETENESS": "1",
        }
    )
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / f"{label}.md"
        src.write_text(md_text, encoding="utf-8")
        proc = subprocess.run(
            [
                "pandoc",
                str(src),
                "--from",
                "markdown+raw_tex",
                "--to",
                "latex",
                "--lua-filter",
                str(FILTER_LUA),
            ],
            capture_output=True,
            text=True,
            cwd=str(REPO_ROOT),
            env=env,
        )
    if proc.returncode != 0:
        raise AssertionError(f"pandoc failed for {label}: {proc.stderr[:400]}")
    return proc.stdout


def _nonexplicit_ids_from_book_emissions() -> list[str]:
    rows = _load_tsv_rows(BOOK_EMISSIONS_TSV)
    return [
        (r.get("emission_id") or "").strip()
        for r in rows
        if (r.get("emission_path") or "").strip() in {"heading_injection", "line_injection"}
    ]


def _parse_ind_page_lists(ind_text: str) -> dict[str, list[int]]:
    """Parse a MakeIndex IND file into {entry_identity: [page, ...]} mapping.

    Extracts \\hyperpage{N} references from \\item and \\subitem blocks.
    Entry identity is taken from \\iventry{form}{} or \\ivlangheader{lang}{}.
    """
    entry_re = re.compile(r"\\(?:iventry|ivlangheader)\{([^}]*)\}")
    page_re = re.compile(r"\\hyperpage\{(\d+)\}")
    pagerange_re = re.compile(r"\\hyperpagerange\{(\d+)\}\{(\d+)\}")

    pages: dict[str, list[int]] = {}
    current_key: str | None = None

    for line in ind_text.splitlines():
        stripped = line.strip()
        if stripped.startswith(r"\item") or stripped.startswith(r"\subitem"):
            m = entry_re.search(stripped)
            if m:
                current_key = m.group(1)
                if current_key not in pages:
                    pages[current_key] = []
        if current_key:
            for m in pagerange_re.finditer(stripped):
                for p in range(int(m.group(1)), int(m.group(2)) + 1):
                    if p not in pages[current_key]:
                        pages[current_key].append(p)
            for m in page_re.finditer(stripped):
                p = int(m.group(1))
                if p not in pages[current_key]:
                    pages[current_key].append(p)
    return {k: sorted(v) for k, v in pages.items()}


def _page_impact_summary(prod_pages: dict[str, list[int]], shadow_pages: dict[str, list[int]]) -> dict[str, object]:
    """Compare production and shadow IND page lists; return summary dict."""
    all_keys = set(prod_pages) | set(shadow_pages)
    unchanged = changed = 0
    pages_added: list[int] = []
    pages_removed: list[int] = []
    changed_entries: list[dict[str, object]] = []

    for key in sorted(all_keys):
        prod_list = prod_pages.get(key, [])
        shad_list = shadow_pages.get(key, [])
        if prod_list == shad_list:
            unchanged += 1
        else:
            changed += 1
            added = sorted(set(shad_list) - set(prod_list))
            removed = sorted(set(prod_list) - set(shad_list))
            pages_added.extend(added)
            pages_removed.extend(removed)
            changed_entries.append({"entry": key, "prod": prod_list, "shadow": shad_list})

    return {
        "total_entries": len(all_keys),
        "unchanged": unchanged,
        "changed": changed,
        "pages_added": len(pages_added),
        "pages_removed": len(pages_removed),
        "changed_entries": changed_entries[:20],  # limit for report
    }


_PANDOC_COMMON_ARGS = [
    "--standalone",
    "--from",
    "markdown+raw_tex+citations",
    "--to",
    "latex",
    "--top-level-division=chapter",
    "--number-sections",
    "--table-of-contents",
    "--toc-depth=1",
]


def _pandoc_filter_args() -> list[str]:
    return [
        "--lua-filter", str(TOOLS_DIR / "paragraph_gloss_validator.lua"),
        "--lua-filter", str(FILTER_LUA),
        "--lua-filter", str(TOOLS_DIR / "predicted_form_filter.lua"),
        "--lua-filter", str(TOOLS_DIR / "reconstructed_form_filter.lua"),
        "--lua-filter", str(TOOLS_DIR / "lex_form_filter.lua"),
        "--lua-filter", str(REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_foma.lua"),
        "--include-in-header", str(ASSEMBLY_DIR / "book_draft_pdf_header.tex"),
        "--include-in-header", str(ASSEMBLY_DIR / "book_draft_index_registry.tex"),
        "--include-in-header", str(REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_pdf_header.tex"),
        "--metadata-file", str(ASSEMBLY_DIR / "book_draft_metadata.yaml"),
        "--bibliography", str(REPO_ROOT / "docs/refs.bib"),
        "--citeproc",
    ]


def _run_full_impact_local(production_md: str, shadow_md: str, inventory: dict[str, object] | None = None) -> dict[str, object]:
    """Local 3-pass converged full-impact build (requires pandoc, xelatex, makeindex, pdftotext)."""
    env = dict(os.environ)
    env.update({
        "CAPR_IV_BOOK_EMISSIONS_TSV": str(BOOK_EMISSIONS_TSV),
        "CAPR_IV_EXPLICIT_PLAN_TSV": str(EXPLICIT_PLAN_TSV),
        "CAPR_IV_REQUIRE_EXPLICIT_COMPLETENESS": "1",
    })
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        result: dict[str, object] = {}

        for label, md_text in (("prod", production_md), ("shadow", shadow_md)):
            run_dir = tmp_path / label
            run_dir.mkdir()
            src_md = run_dir / f"{label}.md"
            src_tex = run_dir / f"{label}.tex"
            src_md.write_text(md_text, encoding="utf-8")

            # Pandoc
            proc = subprocess.run(
                ["pandoc", str(src_md), *_PANDOC_COMMON_ARGS, *_pandoc_filter_args(), "-o", str(src_tex)],
                capture_output=True, text=True, cwd=str(REPO_ROOT), env=env,
            )
            if proc.returncode != 0:
                raise AssertionError(f"--full-impact pandoc failed for {label}: {proc.stderr[:400]}")

            # normalize_citeproc_section_locators.py
            norm_proc = subprocess.run(
                [sys.executable, str(TOOLS_DIR / "normalize_citeproc_section_locators.py"), "--tex-path", str(src_tex)],
                capture_output=True, text=True, cwd=str(REPO_ROOT),
            )
            if norm_proc.returncode != 0:
                raise AssertionError(f"--full-impact normalize_citeproc failed for {label}: {norm_proc.stderr[:300]}")

            # XeLaTeX 3 passes with MakeIndex on iv.idx after pass 1
            for _pass in range(1, 4):
                xe = subprocess.run(
                    ["xelatex", "-interaction=nonstopmode", "-halt-on-error", src_tex.name],
                    cwd=str(run_dir), capture_output=True, text=True,
                )
                if xe.returncode != 0:
                    raise AssertionError(f"--full-impact xelatex pass {_pass} failed for {label}")
                if _pass == 1:
                    iv_idx = run_dir / "iv.idx"
                    if not iv_idx.exists():
                        raise AssertionError(f"--full-impact iv.idx not found after XeLaTeX pass 1 for {label}")
                    iv_ind = run_dir / "iv.ind"
                    iv_ilg = run_dir / "iv.ilg"
                    mk = subprocess.run(
                        ["makeindex", "-o", iv_ind.name, "-t", iv_ilg.name, iv_idx.name],
                        cwd=str(run_dir), capture_output=True, text=True,
                    )
                    if mk.returncode != 0:
                        raise AssertionError(f"--full-impact makeindex failed for {label}: {mk.stderr[:300]}")
                    mk_acc, mk_rej = _parse_makeindex_output(mk.stdout + "\n" + mk.stderr + "\n" + (iv_ilg.read_text() if iv_ilg.exists() else ""))
                    result[f"{label}_accepted"] = mk_acc
                    result[f"{label}_rejected"] = mk_rej
                    result[f"{label}_iv_idx"] = iv_idx.read_text(encoding="utf-8")

            # PDF page count (always try pdfinfo)
            pdf_path = run_dir / f"{label}.pdf"
            if pdf_path.exists():
                if shutil.which("pdfinfo"):
                    pi = subprocess.run(["pdfinfo", str(pdf_path)], capture_output=True, text=True)
                    m = re.search(r"Pages:\s+(\d+)", pi.stdout)
                    result[f"{label}_pdf_pages"] = int(m.group(1)) if m else 0
                if shutil.which("pdftotext"):
                    pt = subprocess.run(
                        ["pdftotext", "-layout", str(pdf_path), "-"],
                        capture_output=True, text=True,
                    )
                    result[f"{label}_pdf_text"] = pt.stdout

        # IDX-based page impact using exact complete keys
        if "prod_iv_idx" in result and "shadow_iv_idx" in result:
            canonical_commands = _load_canonical_iv_commands()
            movable_ids = inventory["movable_emission_ids"] if inventory else []
            movable_records = [r for r in inventory["records"] if r.proposed_status == "passage_shadow"] if inventory else []
            result["idx_page_impact"] = _idx_page_impact_analysis(
                result["prod_iv_idx"],
                result["shadow_iv_idx"],
                canonical_commands,
                movable_ids,
                movable_records,
            )

        return result


def _run_full_impact_docker(production_md: str, shadow_md: str, inventory: dict[str, object] | None = None) -> dict[str, object]:
    """Production-equivalent converged 3-pass TeX build inside Docker.

    Runs: Pandoc → normalize_citeproc → XeLaTeX×1 → MakeIndex → XeLaTeX×2 → XeLaTeX×3.
    Parses MakeIndex counts via Python (not sed) to avoid greedy last-digit-group capture.
    Returns rich dict including page-impact data.
    """
    if shutil.which("docker") is None:
        raise AssertionError("--full-impact requires xelatex/makeindex locally or Docker")
    with tempfile.TemporaryDirectory(dir=str(REPO_ROOT)) as tmp:
        tmp_path = Path(tmp)
        prod_md = tmp_path / "prod.md"
        shad_md = tmp_path / "shadow.md"
        prod_md.write_text(production_md, encoding="utf-8")
        shad_md.write_text(shadow_md, encoding="utf-8")
        # Write Python helper scripts to files (inline -c scripts have newline issues in Docker)
        (tmp_path / "mkparse.py").write_text(
            "import re, os, sys\n"
            "def parse(txt):\n"
            "    acc = rej = 0\n"
            "    for l in txt.splitlines():\n"
            "        m = re.search(r'(\\d+)\\s+entries accepted', l)\n"
            "        if m: acc = int(m.group(1))\n"
            "        m = re.search(r'(\\d+)\\s+rejected', l)\n"
            "        if m: rej = int(m.group(1))\n"
            "    return acc, rej\n"
            "for b in ('prod', 'shadow'):\n"
            "    ilg_path = b + '/iv.ilg'\n"
            "    if not os.path.exists(ilg_path):\n"
            "        print('ERROR: missing ' + ilg_path, file=sys.stderr)\n"
            "        sys.exit(1)\n"
            "    txt = open(ilg_path).read()\n"
            "    a, r = parse(txt)\n"
            "    print('MK_' + b.upper() + '_ACCEPTED=' + str(a))\n"
            "    print('MK_' + b.upper() + '_REJECTED=' + str(r))\n",
            encoding="utf-8",
        )
        (tmp_path / "indparse.py").write_text(
            "import glob\n"
            "for b in ('prod', 'shadow'):\n"
            "    inds = glob.glob(b + '/*.ind')\n"
            "    iv = [f for f in inds if 'iv' in f.lower()]\n"
            "    f = iv[0] if iv else (inds[0] if inds else None)\n"
            "    if f:\n"
            "        try: txt = open(f).read()\n"
            "        except: txt = ''\n"
            "        print('IND_' + b.upper() + '_BEGIN')\n"
            "        print(txt)\n"
            "        print('IND_' + b.upper() + '_END')\n",
            encoding="utf-8",
        )
        rel_tmp = tmp_path.relative_to(REPO_ROOT).as_posix()
        script = f"""
set -e
apk add --no-cache font-noto python3 >/dev/null 2>&1
apk add --no-cache poppler-utils >/dev/null 2>&1
tlmgr option repository https://ftp.fau.de/ctan/systems/texlive/tlnet >/dev/null
kpsewhich fvextra.sty >/dev/null 2>&1 || (tlmgr update --self >/dev/null && tlmgr install fvextra >/dev/null)
kpsewhich imakeidx.sty >/dev/null 2>&1 || tlmgr install imakeidx >/dev/null
kpsewhich morewrites.sty >/dev/null 2>&1 || tlmgr install morewrites >/dev/null
kpsewhich xkeyval.sty >/dev/null 2>&1 || tlmgr install xkeyval >/dev/null
cd /data/{rel_tmp}
mkdir -p prod shadow
cp prod.md prod/prod.md
cp shadow.md shadow/shadow.md
for base in prod shadow; do
  cd /data/{rel_tmp}/"$base"
  CAPR_IV_BOOK_EMISSIONS_TSV=/data/Germanic/docs/book/index_verborum_book_emissions.tsv \
  CAPR_IV_EXPLICIT_PLAN_TSV=/data/Germanic/docs/book/index_verborum_book_explicit_plan.tsv \
  CAPR_IV_REQUIRE_EXPLICIT_COMPLETENESS=1 \
  pandoc "$base.md" --standalone --from=markdown+raw_tex+citations --to=latex \
    --top-level-division=chapter --number-sections --table-of-contents --toc-depth=1 \
    --lua-filter=/data/Germanic/tools/paragraph_gloss_validator.lua \
    --lua-filter=/data/Germanic/tools/index_verborum_filter.lua \
    --lua-filter=/data/Germanic/tools/predicted_form_filter.lua \
    --lua-filter=/data/Germanic/tools/reconstructed_form_filter.lua \
    --lua-filter=/data/Germanic/tools/lex_form_filter.lua \
    --lua-filter=/data/Germanic/docs/sound_changes/reader_facing/reader_facing_foma.lua \
    --include-in-header=/data/Germanic/docs/assembly/book_draft_pdf_header.tex \
    --include-in-header=/data/Germanic/docs/assembly/book_draft_index_registry.tex \
    --include-in-header=/data/Germanic/docs/sound_changes/reader_facing/reader_facing_pdf_header.tex \
    --metadata-file=/data/Germanic/docs/assembly/book_draft_metadata.yaml \
    --bibliography=/data/docs/refs.bib --citeproc -o "$base.tex"
  python3 /data/Germanic/tools/normalize_citeproc_section_locators.py --tex-path "$base.tex"
  xelatex -interaction=nonstopmode -halt-on-error "$base.tex" >/dev/null
  [ -f iv.idx ] || {{ echo "missing iv.idx for $base" >&2; exit 1; }}
  makeindex -o iv.ind -t iv.ilg iv.idx
  [ -f iv.ind ] || {{ echo "missing iv.ind for $base" >&2; exit 1; }}
  [ -f iv.ilg ] || {{ echo "missing iv.ilg for $base" >&2; exit 1; }}
  xelatex -interaction=nonstopmode -halt-on-error "$base.tex" >/dev/null
  xelatex -interaction=nonstopmode -halt-on-error "$base.tex" >/dev/null
  [ -f "$base.pdf" ] || {{ echo "missing PDF for $base" >&2; exit 1; }}
  pdfinfo "$base.pdf" | grep "^Pages:" | grep -o '[0-9]*' > pages.txt
  pdftotext -layout "$base.pdf" "$base.pdf.txt"
  cd /data/{rel_tmp}
done
cd /data/{rel_tmp}
python3 mkparse.py
"""
        proc = subprocess.run(
            [
                "docker", "run", "--rm", "--platform", "linux/amd64",
                "--entrypoint", "/bin/sh",
                "-v", f"{REPO_ROOT}:/data",
                "-w", "/data",
                "pandoc/latex:latest", "-c", script,
            ],
            capture_output=True, text=True, cwd=str(REPO_ROOT),
        )
        if proc.returncode != 0:
            raise AssertionError(
                f"--full-impact docker run failed (rc={proc.returncode})\n"
                f"stderr (last 2000): {proc.stderr[-2000:]}\n"
                f"stdout (last 500): {proc.stdout[-500:]}"
            )
        output = proc.stdout

        # Parse MakeIndex counts from Python helper (reads iv.ilg)
        result: dict[str, object] = {}
        for key in ("prod", "shadow"):
            m_acc = re.search(rf"MK_{key.upper()}_ACCEPTED=(\d+)", output)
            m_rej = re.search(rf"MK_{key.upper()}_REJECTED=(\d+)", output)
            result[f"{key}_accepted"] = int(m_acc.group(1)) if m_acc else 0
            result[f"{key}_rejected"] = int(m_rej.group(1)) if m_rej else 0

        # Read result files from the mounted filesystem (not stdout)
        for key in ("prod", "shadow"):
            # PDF page count
            pages_file = tmp_path / key / "pages.txt"
            if pages_file.exists():
                pages_txt = pages_file.read_text(encoding="utf-8").strip()
                if pages_txt.isdigit():
                    result[f"{key}_pdf_pages"] = int(pages_txt)
            # PDF text
            pdf_txt_file = tmp_path / key / f"{key}.pdf.txt"
            if pdf_txt_file.exists():
                result[f"{key}_pdf_text"] = pdf_txt_file.read_text(encoding="utf-8")
            # iv.idx content (for IDX-based page impact)
            idx_file = tmp_path / key / "iv.idx"
            if idx_file.exists():
                result[f"{key}_iv_idx"] = idx_file.read_text(encoding="utf-8")
            # iv.ilg content (for structural verification)
            ilg_file = tmp_path / key / "iv.ilg"
            if ilg_file.exists():
                result[f"{key}_iv_ilg"] = ilg_file.read_text(encoding="utf-8")

        # IDX-based page impact (exact complete keys)
        if "prod_iv_idx" in result and "shadow_iv_idx" in result:
            canonical_commands = _load_canonical_iv_commands()
            inv = inventory or {}
            inv_movable_ids = inv.get("movable_emission_ids", [])
            inv_movable_records = [r for r in inv.get("records", []) if r.proposed_status == "passage_shadow"]
            result["idx_page_impact"] = _idx_page_impact_analysis(
                result["prod_iv_idx"],
                result["shadow_iv_idx"],
                canonical_commands,
                inv_movable_ids,
                inv_movable_records,
            )

        return result


def _run_full_impact(production_md: str, shadow_md: str, inventory: dict[str, object] | None = None) -> dict[str, object]:
    if all(shutil.which(tool) for tool in ("pandoc", "xelatex", "makeindex")):
        return _run_full_impact_local(production_md, shadow_md, inventory)
    return _run_full_impact_docker(production_md, shadow_md, inventory)


def check(*, full_impact: bool = False, verbose: bool = False) -> bool:
    errors: list[str] = []
    inventory = load_broad_prose_inventory()
    records = inventory["records"]
    movable_ids = inventory["movable_emission_ids"]
    retained_ids = sorted(
        set(inventory["retained_mixed_emission_ids"]) | set(inventory["retained_unresolved_emission_ids"])
    )

    ordinary_lexical = build_lexical_volume()
    canonical_lexical = CANONICAL_LEXICAL_MD.read_text(encoding="utf-8")
    if ordinary_lexical != canonical_lexical:
        errors.append("production lexical build is not byte-identical to tracked lexical volume")

    ordinary_book = build_book_markdown(render_mode="anchor")
    canonical_book = CANONICAL_BOOK_MD.read_text(encoding="utf-8")
    if ordinary_book != canonical_book:
        errors.append("production book build is not byte-identical to tracked book draft markdown")

    requests = build_passage_anchor_requests(records)
    shadow_lexical = build_lexical_volume(passage_anchor_requests=requests)
    shadow_anchor_ids = _extract_anchor_ids(shadow_lexical)
    shadow_anchor_counter = Counter(shadow_anchor_ids)
    duplicate_shadow = [eid for eid, count in shadow_anchor_counter.items() if count > 1]
    if duplicate_shadow:
        errors.append(f"shadow lexical has duplicate passage anchors: {duplicate_shadow[:5]}")
    missing_movable = [eid for eid in movable_ids if shadow_anchor_counter.get(eid, 0) != 1]
    if missing_movable:
        errors.append(f"shadow lexical missing movable anchors: {missing_movable[:5]}")
    retained_present = [eid for eid in retained_ids if shadow_anchor_counter.get(eid, 0) > 0]
    if retained_present:
        errors.append(f"retained heading IDs appeared in passage placement: {retained_present[:5]}")
    stripped_shadow_lexical = _strip_shadow_anchors_exact(shadow_lexical, movable_ids)
    if stripped_shadow_lexical != ordinary_lexical:
        errors.append("shadow lexical differs from ordinary lexical after stripping only generated anchor blocks")

    trace: list[BookEmission] = []
    shadow_book = build_book_markdown(
        render_mode="anchor",
        emission_trace=trace,
        lexical_markdown_override=shadow_lexical,
        preplaced_nonexplicit_emission_ids=set(movable_ids),
    )
    prod_anchor_ids = _extract_anchor_ids(ordinary_book)
    shad_anchor_ids = _extract_anchor_ids(shadow_book)
    prod_counter = Counter(prod_anchor_ids)
    shad_counter = Counter(shad_anchor_ids)
    if set(prod_anchor_ids) != set(shad_anchor_ids):
        errors.append("production vs shadow non-explicit anchor ID sets differ")
    if any(prod_counter[eid] != 1 for eid in prod_counter):
        errors.append("production book has duplicate/missing non-explicit anchor IDs")
    if any(shad_counter[eid] != 1 for eid in shad_counter):
        errors.append("shadow book has duplicate/missing non-explicit anchor IDs")

    trace_ids = [e.emission_id for e in trace]
    if any(eid in trace_ids for eid in movable_ids):
        errors.append("preplaced movable IDs were not fully suppressed from heading injection")

    nonexplicit_ids = _nonexplicit_ids_from_book_emissions()
    if set(nonexplicit_ids) != set(prod_anchor_ids):
        errors.append("production markdown non-explicit anchor IDs do not match canonical book_emissions plan")

    if shutil.which("pandoc") is None:
        errors.append("pandoc is required for shadow checker")
    else:
        prod_tex = _run_pandoc(ordinary_book, label="prod")
        shad_tex = _run_pandoc(shadow_book, label="shadow")
        prod_cmds = _extract_iv_commands(prod_tex)
        shad_cmds = _extract_iv_commands(shad_tex)
        prod_counter_cmd = Counter(prod_cmds)
        shad_counter_cmd = Counter(shad_cmds)
        if len(prod_cmds) != len(shad_cmds):
            errors.append(f"command totals differ: prod={len(prod_cmds)} shadow={len(shad_cmds)}")
        if len(prod_counter_cmd) != len(shad_counter_cmd):
            errors.append(
                f"unique command totals differ: prod={len(prod_counter_cmd)} shadow={len(shad_counter_cmd)}"
            )
        if prod_counter_cmd != shad_counter_cmd:
            errors.append("index command multiset differs between production and shadow")

        first_change = None
        last_change = None
        for idx, (a, b) in enumerate(zip(prod_cmds, shad_cmds), start=1):
            if a != b:
                if first_change is None:
                    first_change = idx
                last_change = idx
        if verbose:
            changed = sum(1 for i in range(min(len(prod_cmds), len(shad_cmds))) if prod_cmds[i] != shad_cmds[i])
            print(
                f"command order movement: changed={changed} first_changed={first_change} last_changed={last_change}"
            )

        prod_no_index = _remove_iv_commands_narrow(prod_tex)
        shad_no_index = _remove_iv_commands_narrow(shad_tex)
        if prod_no_index != shad_no_index:
            errors.append("non-index TeX differs after removing only \\index[iv]{...} commands")

    full_impact_result = None
    if full_impact and not errors:
        full_impact_result = _run_full_impact(ordinary_book, shadow_book, inventory=inventory)
        if full_impact_result["prod_rejected"] != 0 or full_impact_result["shadow_rejected"] != 0:
            errors.append(
                "makeindex rejected entries in full-impact mode: "
                f"prod={full_impact_result['prod_rejected']} shadow={full_impact_result['shadow_rejected']}"
            )
        if full_impact_result["prod_accepted"] == 0 or full_impact_result["shadow_accepted"] == 0:
            errors.append(
                "makeindex accepted totals were zero in full-impact mode; index extraction did not run as expected"
            )
        if full_impact_result["prod_accepted"] != full_impact_result["shadow_accepted"]:
            errors.append(
                "makeindex accepted totals differ in full-impact mode: "
                f"prod={full_impact_result['prod_accepted']} shadow={full_impact_result['shadow_accepted']}"
            )
        # IDX-based canonical key validation
        if "idx_page_impact" in full_impact_result:
            ipi = full_impact_result["idx_page_impact"]
            if not ipi.get("prod_idx_matches_canonical_count", True):
                errors.append(
                    f"prod iv.idx total ({ipi.get('prod_idx_total')}) != expected commands "
                    f"({ipi.get('expected_total_commands')})"
                )
            if not ipi.get("prod_idx_matches_canonical_keys", True):
                errors.append("prod iv.idx complete-key set does not match canonical book_emissions keys")
            if not ipi.get("shadow_idx_matches_canonical_keys", True):
                errors.append("shadow iv.idx complete-key set does not match canonical book_emissions keys")
            # Verify that changed keys are all associated with moved emissions
            changed_entries = ipi.get("changed_entries", [])
            for entry in changed_entries:
                if not entry.get("moved_emission_ids"):
                    errors.append(
                        f"index key changed without associated movable emission: {entry.get('key', '')[:80]}"
                    )
        # PDF body/index separation
        if "prod_pdf_text" in full_impact_result and "shadow_pdf_text" in full_impact_result:
            try:
                prod_body, prod_index = _split_pdf_text(full_impact_result["prod_pdf_text"], "prod")
                shad_body, shad_index = _split_pdf_text(full_impact_result["shadow_pdf_text"], "shadow")
                if prod_body != shad_body:
                    errors.append("PDF body text differs between production and shadow")
            except AssertionError as exc:
                errors.append(str(exc))

    if errors:
        print("Stage 4A shadow checker: FAILED", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return False

    summary = inventory["summary"]
    print("Stage 4A shadow checker: PASS")
    print(f"  movable_emissions={len(movable_ids)} retained_emissions={len(retained_ids)}")
    print(f"  group_classes={summary.get('group_classes')}")
    print(f"  resolved_block_kinds={summary.get('resolved_block_kinds')}")
    if full_impact_result:
        print(
            "  full-impact makeindex accepted/rejected: "
            f"prod={full_impact_result['prod_accepted']}/{full_impact_result['prod_rejected']} "
            f"shadow={full_impact_result['shadow_accepted']}/{full_impact_result['shadow_rejected']}"
        )
        if "idx_page_impact" in full_impact_result:
            ipi = full_impact_result["idx_page_impact"]
            print(
                f"  idx-page-impact (exact keys): total={ipi.get('total_exact_entries')} "
                f"unchanged={ipi.get('unchanged')} changed={ipi.get('changed')} "
                f"refs_added={ipi.get('pages_added_count')} refs_removed={ipi.get('pages_removed_count')}"
            )
            print(
                f"  prod/shadow idx: {ipi.get('prod_idx_total')}/{ipi.get('shadow_idx_total')} entries "
                f"({ipi.get('prod_unique_keys')}/{ipi.get('shadow_unique_keys')} unique keys)"
            )
        if verbose and full_impact_result:
            prod_pages_count = full_impact_result.get("prod_pdf_pages")
            shad_pages_count = full_impact_result.get("shadow_pdf_pages")
            if prod_pages_count is not None or shad_pages_count is not None:
                print(f"  pdf pages: prod={prod_pages_count} shadow={shad_pages_count}")
            prod_text = full_impact_result.get("prod_pdf_text", "")
            shad_text = full_impact_result.get("shadow_pdf_text", "")
            if prod_text and shad_text:
                try:
                    prod_body, prod_idx_text = _split_pdf_text(prod_text, "prod")
                    shad_body, shad_idx_text = _split_pdf_text(shad_text, "shadow")
                    body_eq = (prod_body == shad_body)
                    print(f"  pdf body text: {'identical' if body_eq else 'DIFFERS'}")
                    if not body_eq:
                        print("  WARNING: body text differs — investigate before proceeding")
                    print(f"  pdf index text: {'identical' if prod_idx_text == shad_idx_text else 'differs (expected: page refs changed)'}")
                except AssertionError as exc:
                    print(f"  pdf split: {exc}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full-impact", action="store_true", help="Run optional full compile/index impact mode")
    parser.add_argument("--verbose", action="store_true", help="Print additional movement diagnostics")
    args = parser.parse_args()
    return 0 if check(full_impact=args.full_impact, verbose=args.verbose) else 1


if __name__ == "__main__":
    raise SystemExit(main())

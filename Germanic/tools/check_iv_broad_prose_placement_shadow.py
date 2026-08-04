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
        entries.append({"command": command, "page": idx_text[page_start : k - 1]})
        i = k
    return entries


def _load_canonical_iv_commands() -> list[str]:
    rows = _load_tsv_rows(BOOK_EMISSIONS_TSV)
    return [
        (row.get("index_command") or "").strip()
        for row in rows
        if (row.get("index_command") or "").strip()
    ]


def _split_pdf_text(pdf_text: str, label: str) -> tuple[str, str]:
    marker = "Index verborum"
    idx = pdf_text.find(marker)
    if idx < 0:
        raise AssertionError(f"{label} PDF text missing '{marker}' heading")
    return pdf_text[:idx], pdf_text[idx:]


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


def _run_full_impact_local(production_md: str, shadow_md: str) -> dict[str, object]:
    """Local 3-pass converged full-impact build (requires pandoc, xelatex, makeindex)."""
    env = dict(os.environ)
    env.update({
        "CAPR_IV_BOOK_EMISSIONS_TSV": str(BOOK_EMISSIONS_TSV),
        "CAPR_IV_EXPLICIT_PLAN_TSV": str(EXPLICIT_PLAN_TSV),
        "CAPR_IV_REQUIRE_EXPLICIT_COMPLETENESS": "1",
    })
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        result: dict[str, object] = {}
        ind_contents: dict[str, str] = {}

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

            # XeLaTeX pass 1
            for _pass in range(1, 4):
                xe = subprocess.run(
                    ["xelatex", "-interaction=nonstopmode", "-halt-on-error", src_tex.name],
                    cwd=str(run_dir), capture_output=True, text=True,
                )
                if xe.returncode != 0:
                    raise AssertionError(f"--full-impact xelatex pass {_pass} failed for {label}")
                if _pass == 1:
                    # MakeIndex after pass 1
                    acc = rej = 0
                    for idx in run_dir.glob("*.idx"):
                        ind = idx.with_suffix(".ind")
                        mk = subprocess.run(
                            ["makeindex", "-o", ind.name, idx.name],
                            cwd=str(run_dir), capture_output=True, text=True,
                        )
                        if mk.returncode != 0:
                            raise AssertionError(f"--full-impact makeindex failed for {idx.name}")
                        mk_acc, mk_rej = _parse_makeindex_output(mk.stdout + "\n" + mk.stderr)
                        acc += mk_acc
                        rej += mk_rej
                    result[f"{label}_accepted"] = acc
                    result[f"{label}_rejected"] = rej
                    # Save IND content for page-impact analysis
                    iv_ind = next((run_dir / idx.stem).with_suffix(".ind")
                                  for idx in run_dir.glob("*.idx") if "iv" in idx.stem.lower()
                                  if (run_dir / idx.stem).with_suffix(".ind").exists()), None
                    if iv_ind is None:
                        iv_inds = list(run_dir.glob("*.ind"))
                        iv_ind = iv_inds[0] if iv_inds else None
                    if iv_ind and iv_ind.exists():
                        ind_contents[label] = iv_ind.read_text(encoding="utf-8", errors="replace")

            # PDF page count via pdftotext or pdfinfo
            pdf_path = run_dir / f"{label}.pdf"
            if pdf_path.exists() and shutil.which("pdftotext"):
                pt = subprocess.run(
                    ["pdftotext", "-layout", str(pdf_path), "-"],
                    capture_output=True, text=True,
                )
                result[f"{label}_pdf_text"] = pt.stdout
            elif pdf_path.exists() and shutil.which("pdfinfo"):
                pi = subprocess.run(["pdfinfo", str(pdf_path)], capture_output=True, text=True)
                m = re.search(r"Pages:\s+(\d+)", pi.stdout)
                result[f"{label}_pdf_pages"] = int(m.group(1)) if m else 0

        # Page-impact analysis
        if "prod" in ind_contents and "shadow" in ind_contents:
            prod_pages = _parse_ind_page_lists(ind_contents["prod"])
            shad_pages = _parse_ind_page_lists(ind_contents["shadow"])
            result["page_impact"] = _page_impact_summary(prod_pages, shad_pages)
            result["prod_iv_ind"] = ind_contents["prod"]
            result["shadow_iv_ind"] = ind_contents["shadow"]

        return result


def _run_full_impact_docker(production_md: str, shadow_md: str) -> dict[str, object]:
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
            "import re, glob\n"
            "def parse(txt):\n"
            "    acc = rej = 0\n"
            "    for l in txt.splitlines():\n"
            "        m = re.search(r'(\\d+)\\s+entries accepted', l)\n"
            "        if m: acc = int(m.group(1))\n"
            "        m = re.search(r'(\\d+)\\s+rejected', l)\n"
            "        if m: rej = int(m.group(1))\n"
            "    return acc, rej\n"
            "for b in ('prod', 'shadow'):\n"
            "    total_a = total_r = 0\n"
            "    for f in glob.glob(b + '/*.ilg'):\n"
            "        try: txt = open(f).read()\n"
            "        except: txt = ''\n"
            "        a, r = parse(txt)\n"
            "        total_a += a; total_r += r\n"
            "    print('MK_' + b.upper() + '_ACCEPTED=' + str(total_a))\n"
            "    print('MK_' + b.upper() + '_REJECTED=' + str(total_r))\n",
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
  makeindex -o iv.ind -t iv.ilg iv.idx >/dev/null 2>&1
  xelatex -interaction=nonstopmode -halt-on-error "$base.tex" >/dev/null
  xelatex -interaction=nonstopmode -halt-on-error "$base.tex" >/dev/null
  pg=unknown
  command -v pdfinfo >/dev/null 2>&1 && pg=$(pdfinfo "$base.pdf" 2>/dev/null | grep "^Pages:" | grep -o '[0-9]*' | head -1) || true
  echo "PDF_${{base}}_PAGES=$pg"
  command -v pdftotext >/dev/null 2>&1 && pdftotext -layout "$base.pdf" - >"$base.pdf.txt" 2>/dev/null || true
  cd /data/{rel_tmp}
done
cd /data/{rel_tmp}
python3 mkparse.py
python3 indparse.py
for base in prod shadow; do
  if [ -f "$base/$base.pdf.txt" ]; then
    echo "PDFTEXT_${{base}}_BEGIN"
    cat "$base/$base.pdf.txt"
    echo "PDFTEXT_${{base}}_END"
  fi
done
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
            # Show more stderr to aid diagnosis, but truncate to keep output manageable
            raise AssertionError(
                f"--full-impact docker run failed (rc={proc.returncode})\n"
                f"stderr (last 2000): {proc.stderr[-2000:]}\n"
                f"stdout (last 500): {proc.stdout[-500:]}"
            )
        output = proc.stdout

        # Parse MakeIndex counts
        result: dict[str, object] = {}
        for key in ("prod", "shadow"):
            m_acc = re.search(rf"MK_{key.upper()}_ACCEPTED=(\d+)", output)
            m_rej = re.search(rf"MK_{key.upper()}_REJECTED=(\d+)", output)
            result[f"{key}_accepted"] = int(m_acc.group(1)) if m_acc else 0
            result[f"{key}_rejected"] = int(m_rej.group(1)) if m_rej else 0

        # Parse page counts (format: PDF_prod_PAGES=N)
        for key in ("prod", "shadow"):
            m = re.search(rf"PDF_{key}_PAGES=(\d+)", output)
            if m:
                result[f"{key}_pdf_pages"] = int(m.group(1))

        # Parse IND content for page-impact analysis
        ind_contents: dict[str, str] = {}
        for key in ("prod", "shadow"):
            block = re.search(
                rf"IND_{key.upper()}_BEGIN\n(.*?)IND_{key.upper()}_END",
                output, re.DOTALL
            )
            if block:
                ind_contents[key] = block.group(1)

        if "prod" in ind_contents and "shadow" in ind_contents:
            prod_pages = _parse_ind_page_lists(ind_contents["prod"])
            shad_pages = _parse_ind_page_lists(ind_contents["shadow"])
            result["page_impact"] = _page_impact_summary(prod_pages, shad_pages)

        # Parse PDF text
        for key in ("prod", "shadow"):
            block = re.search(
                rf"PDFTEXT_{key}_BEGIN\n(.*?)PDFTEXT_{key}_END",
                output, re.DOTALL
            )
            if block:
                result[f"{key}_pdf_text"] = block.group(1)

        return result


def _run_full_impact(production_md: str, shadow_md: str) -> dict[str, object]:
    if all(shutil.which(tool) for tool in ("pandoc", "xelatex", "makeindex")):
        return _run_full_impact_local(production_md, shadow_md)
    return _run_full_impact_docker(production_md, shadow_md)


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
        full_impact_result = _run_full_impact(ordinary_book, shadow_book)
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
        # Page-impact report
        if verbose and full_impact_result and "page_impact" in full_impact_result:
            pi = full_impact_result["page_impact"]
            print(f"  page-impact: total_entries={pi.get('total_entries',0)} "
                  f"unchanged={pi.get('unchanged',0)} changed={pi.get('changed',0)} "
                  f"pages_added={pi.get('pages_added',0)} pages_removed={pi.get('pages_removed',0)}")
        if verbose and full_impact_result:
            prod_pages = full_impact_result.get("prod_pdf_pages")
            shad_pages = full_impact_result.get("shadow_pdf_pages")
            if prod_pages is not None or shad_pages is not None:
                print(f"  pdf pages: prod={prod_pages} shadow={shad_pages}")
            # PDF text comparison
            prod_text = full_impact_result.get("prod_pdf_text", "")
            shad_text = full_impact_result.get("shadow_pdf_text", "")
            if prod_text and shad_text:
                if prod_text == shad_text:
                    print("  pdf body text: identical")
                else:
                    print("  pdf body text: differs (pagination/placement change observed)")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full-impact", action="store_true", help="Run optional full compile/index impact mode")
    parser.add_argument("--verbose", action="store_true", help="Print additional movement diagnostics")
    args = parser.parse_args()
    return 0 if check(full_impact=args.full_impact, verbose=args.verbose) else 1


if __name__ == "__main__":
    raise SystemExit(main())

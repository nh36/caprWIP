#!/usr/bin/env python3
"""Stage 4A shadow checker for broad-prose passage-adjacent placement."""
from __future__ import annotations

import argparse
import csv
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


def _strip_anchor_blocks(md_text: str) -> str:
    stripped = re.sub(
        r"\n?:::\s*\{[^}]*\.iv-anchor[^}]*emission_id=\"[^\"]+\"[^}]*\}\s*\n:::\n?",
        "\n",
        md_text,
    )
    return re.sub(r"\n{3,}", "\n\n", stripped).rstrip() + "\n"


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


def _remove_iv_commands_and_normalize(tex_text: str) -> str:
    prefix = r"\index[iv]{"
    i = 0
    n = len(tex_text)
    parts: list[str] = []
    while i < n:
        j = tex_text.find(prefix, i)
        if j < 0:
            parts.append(tex_text[i:])
            break
        parts.append(tex_text[i:j])
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
        parts.append("\n")
        i = k
    merged = "".join(parts)
    merged = re.sub(r"[ \t]+\n", "\n", merged)
    merged = re.sub(r"\n{3,}", "\n\n", merged)
    return merged.rstrip()


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


def _run_full_impact_local(production_md: str, shadow_md: str) -> dict[str, int]:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        prod_md = tmp_path / "prod.md"
        shad_md = tmp_path / "shadow.md"
        prod_tex = tmp_path / "prod.tex"
        shad_tex = tmp_path / "shadow.tex"
        prod_md.write_text(production_md, encoding="utf-8")
        shad_md.write_text(shadow_md, encoding="utf-8")
        common_args = [
            "--standalone",
            "--from",
            "markdown+raw_tex+citations",
            "--to",
            "latex",
            "--top-level-division=chapter",
            "--number-sections",
            "--table-of-contents",
            "--toc-depth=1",
            "--lua-filter",
            str(TOOLS_DIR / "paragraph_gloss_validator.lua"),
            "--lua-filter",
            str(FILTER_LUA),
            "--lua-filter",
            str(TOOLS_DIR / "predicted_form_filter.lua"),
            "--lua-filter",
            str(TOOLS_DIR / "reconstructed_form_filter.lua"),
            "--lua-filter",
            str(TOOLS_DIR / "lex_form_filter.lua"),
            "--lua-filter",
            str(REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_foma.lua"),
            "--include-in-header",
            str(ASSEMBLY_DIR / "book_draft_pdf_header.tex"),
            "--include-in-header",
            str(ASSEMBLY_DIR / "book_draft_index_registry.tex"),
            "--include-in-header",
            str(REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_pdf_header.tex"),
            "--metadata-file",
            str(ASSEMBLY_DIR / "book_draft_metadata.yaml"),
            "--bibliography",
            str(REPO_ROOT / "docs/refs.bib"),
            "--citeproc",
        ]
        env = dict(os.environ)
        env.update(
            {
                "CAPR_IV_BOOK_EMISSIONS_TSV": str(BOOK_EMISSIONS_TSV),
                "CAPR_IV_EXPLICIT_PLAN_TSV": str(EXPLICIT_PLAN_TSV),
                "CAPR_IV_REQUIRE_EXPLICIT_COMPLETENESS": "1",
            }
        )
        for md, tex in ((prod_md, prod_tex), (shad_md, shad_tex)):
            proc = subprocess.run(
                ["pandoc", str(md), *common_args, "-o", str(tex)],
                capture_output=True,
                text=True,
                cwd=str(REPO_ROOT),
                env=env,
            )
            if proc.returncode != 0:
                raise AssertionError(f"--full-impact pandoc failed for {md.name}: {proc.stderr[:400]}")

        accepted = {}
        rejected = {}
        for tex_base in ("prod", "shadow"):
            tex_file = tmp_path / f"{tex_base}.tex"
            run_dir = tmp_path / tex_base
            run_dir.mkdir(exist_ok=True)
            run_tex = run_dir / tex_file.name
            run_tex.write_text(tex_file.read_text(encoding="utf-8"), encoding="utf-8")
            run_xe = subprocess.run(
                ["xelatex", "-interaction=nonstopmode", "-halt-on-error", run_tex.name],
                cwd=str(run_dir),
                capture_output=True,
                text=True,
            )
            if run_xe.returncode != 0:
                raise AssertionError(f"--full-impact xelatex failed for {tex_base}: {run_xe.stderr[:300]}")
            idx_files = list(run_dir.glob("*.idx"))
            acc = rej = 0
            for idx in idx_files:
                out = idx.with_suffix(".ind")
                mk = subprocess.run(
                    ["makeindex", "-o", out.name, idx.name],
                    cwd=str(run_dir),
                    capture_output=True,
                    text=True,
                )
                if mk.returncode != 0:
                    raise AssertionError(f"--full-impact makeindex failed for {idx.name}: {mk.stderr[:300]}")
                m_acc = re.search(r"(\d+)\s+entries accepted", mk.stdout)
                m_rej = re.search(r"(\d+)\s+entries rejected", mk.stdout)
                acc += int(m_acc.group(1)) if m_acc else 0
                rej += int(m_rej.group(1)) if m_rej else 0
            accepted[tex_base] = acc
            rejected[tex_base] = rej
        return {
            "prod_accepted": accepted.get("prod", 0),
            "shadow_accepted": accepted.get("shadow", 0),
            "prod_rejected": rejected.get("prod", 0),
            "shadow_rejected": rejected.get("shadow", 0),
        }


def _run_full_impact_docker(production_md: str, shadow_md: str) -> dict[str, int]:
    if shutil.which("docker") is None:
        raise AssertionError("--full-impact requires xelatex/makeindex locally or Docker")
    with tempfile.TemporaryDirectory(dir=str(REPO_ROOT)) as tmp:
        tmp_path = Path(tmp)
        prod_md = tmp_path / "prod.md"
        shad_md = tmp_path / "shadow.md"
        prod_md.write_text(production_md, encoding="utf-8")
        shad_md.write_text(shadow_md, encoding="utf-8")
        rel_tmp = tmp_path.relative_to(REPO_ROOT).as_posix()
        script = f"""
set -e
apk add --no-cache font-noto python3 >/dev/null
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
  xelatex -interaction=nonstopmode -halt-on-error "$base.tex" >/dev/null
  acc=0
  rej=0
  saw_idx=0
  for idx in *.idx; do
    [ -e "$idx" ] || continue
    saw_idx=1
    out="$(makeindex -o "${{idx%.idx}}.ind" "$idx" 2>&1)"
    a="$(printf '%s' "$out" | sed -n 's/.*\\([0-9][0-9]*\\) entries accepted.*/\\1/p' | head -n1)"
    r="$(printf '%s' "$out" | sed -n 's/.*\\([0-9][0-9]*\\) entries rejected.*/\\1/p' | head -n1)"
    [ -n "$a" ] || a=0
    [ -n "$r" ] || r=0
    acc=$((acc + a))
    rej=$((rej + r))
  done
  if [ "$saw_idx" -eq 0 ]; then
    echo "FULL_IMPACT_${{base}}_ERROR=no_idx_files"
    exit 14
  fi
  cd /data/{rel_tmp}
  echo "FULL_IMPACT_${{base}}_ACCEPTED=$acc"
  echo "FULL_IMPACT_${{base}}_REJECTED=$rej"
done
"""
        proc = subprocess.run(
            [
                "docker",
                "run",
                "--rm",
                "--platform",
                "linux/amd64",
                "--entrypoint",
                "/bin/sh",
                "-v",
                f"{REPO_ROOT}:/data",
                "-w",
                "/data",
                "pandoc/latex:latest",
                "-c",
                script,
            ],
            capture_output=True,
            text=True,
            cwd=str(REPO_ROOT),
        )
        if proc.returncode != 0:
            raise AssertionError(f"--full-impact docker run failed: {proc.stderr[:500]}")
        values = {}
        for key in ("prod", "shadow"):
            m_acc = re.search(rf"FULL_IMPACT_{key}_ACCEPTED=(\d+)", proc.stdout)
            m_rej = re.search(rf"FULL_IMPACT_{key}_REJECTED=(\d+)", proc.stdout)
            if not m_acc or not m_rej:
                raise AssertionError(f"--full-impact docker output missing totals for {key}")
            values[f"{key}_accepted"] = int(m_acc.group(1))
            values[f"{key}_rejected"] = int(m_rej.group(1))
        return {
            "prod_accepted": values["prod_accepted"],
            "shadow_accepted": values["shadow_accepted"],
            "prod_rejected": values["prod_rejected"],
            "shadow_rejected": values["shadow_rejected"],
        }


def _run_full_impact(production_md: str, shadow_md: str) -> dict[str, int]:
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
    stripped_shadow_lexical = _strip_anchor_blocks(shadow_lexical)
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

        prod_no_index = _remove_iv_commands_and_normalize(prod_tex)
        shad_no_index = _remove_iv_commands_and_normalize(shad_tex)
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
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full-impact", action="store_true", help="Run optional full compile/index impact mode")
    parser.add_argument("--verbose", action="store_true", help="Print additional movement diagnostics")
    args = parser.parse_args()
    return 0 if check(full_impact=args.full_impact, verbose=args.verbose) else 1


if __name__ == "__main__":
    raise SystemExit(main())

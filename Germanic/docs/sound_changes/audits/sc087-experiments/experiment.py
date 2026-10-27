#!/usr/bin/env python3
"""SC087 counterfactual experiments (run inside the backend container).

Compares the production OE cascade against three Barrack-derived
counterfactual variants of the r-metathesis law, applied to every
selected Old English corpus row:

  broad_s   -- Barrack 459.1 restricted to the sibilant branch: rV -> Vr
               before any *s (dropping CAPR's *st cluster requirement).
  broad_sn  -- Barrack 459.1 core matrix: rV -> Vr before *s or *n.
  broad_sn_ae -- broad_sn with the vowel set extended to the fronted
               vowels *ae and *y present at the rule's cascade site
               (Barrack's matrix constrains only accent and length).
  broad_sn_noleft -- broad_sn_ae without CAPR's protective left
               consonant context (Barrack's matrix has no left-hand
               consonant requirement, so word-initial *r qualifies).
  regressive_459_3 -- Barrack 459.3: accented short V + r -> r + V
               before *xt, composed immediately after OERMetathesis.

A production control compiled through the identical truncation path
must match the canonical old_english.bin on every row before any
variant comparison is trusted.

Usage (from the repository root on the host):
  docker compose exec -T backend python3 \
    /usr/app/docs/sound_changes/audits/sc087-experiments/experiment.py
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, "/usr/app/tools")
from capr_runtime import layout  # noqa: E402
from oe_pipeline import apply_down, display_form, evaluation_input, load_rows  # noqa: E402

EXPERIMENT_DIR = Path(__file__).resolve().parent
TRUNCATION_MARK = "save stack old_english.bin"
METATHESIS_BLOCK = re.compile(r"define OERMetathesis \[.*?\];", re.DOTALL)
COMPOSE_LINE = "    .o. OERMetathesis"

SHORT_VOWELS = ("*a", "*á", "*à", "*æ", "*e", "*é", "*è", "*i", "*í", "*ì",
                "*o", "*ó", "*ò", "*u", "*ú", "*ù", "*y")

REGRESSIVE_DEFINE = "define OERRegressiveMetathesis [\n" + ",\n".join(
    f"    {{{v}}} {{*r}} -> {{*r}} {{{v}}} || _ {{*x}} {{*t}}"
    for v in SHORT_VOWELS) + "\n];\n"


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def broadened_block(block: str, context: str) -> str:
    out = block.replace("{*s} {*t}", context)
    if out == block:
        raise RuntimeError("no {*s} {*t} contexts found to broaden")
    return out


def extended_vowel_block(block: str) -> str:
    extra = ",\n".join(
        f"    {{*r}} {{{v}}} -> {{{v}}} {{*r}} "
        "|| EnglishStarConsonant _ [{*s}|{*n}]"
        for v in ("*æ", "*y"))
    return block.replace("\n];", ",\n" + extra + "\n];")


def variant_sources(source: Path) -> dict[str, str]:
    text = source.read_text(encoding="utf-8")
    cut = text.find(TRUNCATION_MARK)
    if cut < 0:
        raise RuntimeError(f"missing truncation mark: {TRUNCATION_MARK}")
    text = text[: cut + len(TRUNCATION_MARK)] + "\nquit\n"
    block = METATHESIS_BLOCK.search(text)
    if not block:
        raise RuntimeError("OERMetathesis define not found")
    blk = block.group(0)
    broad_sn = broadened_block(blk, "[{*s}|{*n}]")
    broad_sn_ae = extended_vowel_block(broad_sn)
    variants = {
        "production_control": text,
        "broad_s": text.replace(blk, broadened_block(blk, "{*s}")),
        "broad_sn": text.replace(blk, broad_sn),
        "broad_sn_ae": text.replace(blk, broad_sn_ae),
        "broad_sn_noleft": text.replace(
            blk, broad_sn_ae.replace("|| EnglishStarConsonant _", "|| _")),
    }
    regressive = text.replace(blk, blk + "\n" + REGRESSIVE_DEFINE)
    if COMPOSE_LINE not in regressive:
        raise RuntimeError("pipeline composition line not found")
    variants["regressive_459_3"] = regressive.replace(
        COMPOSE_LINE, COMPOSE_LINE + "\n    .o. OERRegressiveMetathesis", 1)
    return variants


def compile_variant(name: str, text: str, workdir: Path) -> Path:
    directory = workdir / name
    directory.mkdir()
    script = directory / "variant.foma"
    script.write_text(text, encoding="utf-8")
    result = subprocess.run(["foma", "-q", "-f", script.name], cwd=directory,
                            capture_output=True, text=True, timeout=1800)
    log = result.stdout + "\n" + result.stderr
    if result.returncode or re.search(r"(?im)^\*\*\*|syntax error|not defined", log):
        raise RuntimeError(f"{name}: compilation failed:\n{log[-4000:]}")
    bin_path = directory / "old_english.bin"
    if not bin_path.is_file() or bin_path.stat().st_size == 0:
        raise RuntimeError(f"{name}: old_english.bin missing or empty")
    return bin_path


def main() -> int:
    rt = layout()
    source = rt.fsts_dir / "germanic.txt"
    canonical = rt.bin_dir / "old_english.bin"
    rows = load_rows(rt.corpus_tsv)
    report = {
        "experiment": "sc087-counterfactuals",
        "generated": time.strftime("%Y-%m-%d %H:%M:%S"),
        "germanic.txt_sha256": sha256_of(source),
        "corpus_sha256": sha256_of(rt.corpus_tsv),
        "selected_rows": len(rows),
        "variants": {},
    }
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        bins = {name: compile_variant(name, text, workdir)
                for name, text in variant_sources(source).items()}

        canonical_out = {r["row_id"]: apply_down(canonical, evaluation_input(r))
                         for r in rows}
        control_out = {r["row_id"]: apply_down(bins["production_control"],
                                               evaluation_input(r))
                       for r in rows}
        mismatched = [rid for rid in canonical_out
                      if canonical_out[rid] != control_out[rid]]
        if mismatched:
            raise RuntimeError(
                f"control does not match canonical bin on rows: {mismatched}")
        report["control_matches_canonical"] = True

        for name in ("broad_s", "broad_sn", "broad_sn_ae",
                     "broad_sn_noleft", "regressive_459_3"):
            changed = []
            for r in rows:
                out = apply_down(bins[name], evaluation_input(r))
                if out != control_out[r["row_id"]]:
                    changed.append({
                        "row_id": r["row_id"],
                        "proto": r["proto"],
                        "attested": r["counterpart"],
                        "production": [display_form(f)
                                       for f in control_out[r["row_id"]]],
                        "variant": [display_form(f) for f in out],
                    })
            report["variants"][name] = {
                "rows_changed": len(changed),
                "changes": changed,
            }

    receipt = EXPERIMENT_DIR / "receipt.json"
    receipt.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

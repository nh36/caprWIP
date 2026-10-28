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

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
from capr_runtime import layout  # noqa: E402
from oe_pipeline import (apply_down, display_form, evaluation_input, load_rows,
                         named_stages, normalize_proto)  # noqa: E402
from sound_change_order_sensitivity import batch_apply_down  # noqa: E402

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


def extended_vowel_block(block: str, context: str = "[{*s}|{*n}]") -> str:
    extra = ",\n".join(
        f"    {{*r}} {{{v}}} -> {{{v}}} {{*r}} "
        f"|| EnglishStarConsonant _ {context}"
        for v in ("*æ", "*y"))
    return block.replace("\n];", ",\n" + extra + "\n];")


def variant_sources(source: Path, *, controlled: bool = False) -> dict[str, str]:
    text = source.read_text(encoding="utf-8")
    cut = text.find(TRUNCATION_MARK)
    if cut < 0:
        raise RuntimeError(f"missing truncation mark: {TRUNCATION_MARK}")
    text = text[: cut + len(TRUNCATION_MARK)] + "\nquit\n"
    block = METATHESIS_BLOCK.search(text)
    if not block:
        raise RuntimeError("OERMetathesis define not found")
    blk = block.group(0)
    if controlled:
        extended = extended_vowel_block(blk, "{*s} {*t}")
        return {
            "A": text,
            "B": text.replace(blk, broadened_block(blk, "{*s}")),
            "C": text.replace(blk, extended),
            "D": text.replace(blk, broadened_block(extended, "{*s}")),
        }
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


def controlled_comparison(rt, source: Path, rows: list[dict]) -> dict:
    sources = variant_sources(source, controlled=True)
    forms = [evaluation_input(r) for r in rows]
    pre_bin = rt.bin_dir / "old_english_sandbox_after_oe_contraction.bin"
    before = batch_apply_down(pre_bin, forms)
    report = {
        "experiment": "sc087-s-versus-st-factorial",
        "germanic.txt_sha256": sha256_of(source),
        "corpus_sha256": sha256_of(rt.corpus_tsv),
        "context_metadata_sha256": sha256_of(rt.data_dir / "entry_context_metadata.tsv"),
        "selected_rows": len(rows),
        "selected_inputs_sha256": hashlib.sha256(
            json.dumps(rows, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
        "production_control": "A",
        "variants": {},
        "comparisons": {},
    }
    # These are source-backed reconstruction families, not admitted corpus
    # selections. Acute stress is CAPR notation; neither ending is adjudicated.
    probes = [
        {"id": "cress-n-stem", "input": "*krásjōn",
         "basis": "Bülbring 1902 §493 (*krasjon); ending/cell unresolved"},
        {"id": "cress-jo-stem", "input": "*krásjō",
         "basis": "Kluge–Seebold 2011 s.v. Kresse (*krasjō); cell unresolved"},
    ]
    probe_forms = [evaluation_input({"proto_norm": normalize_proto(p["input"])})
                   for p in probes]
    probe_pre = batch_apply_down(pre_bin, probe_forms)
    canonical = batch_apply_down(rt.bin_dir / "old_english.bin", forms)
    outputs = {}
    with tempfile.TemporaryDirectory() as tmp:
        for name, text in sources.items():
            print(f"Compiling controlled variant {name}", flush=True)
            directory = Path(tmp)
            bin_path = compile_variant(name, text.replace(
                "\nquit\n", "\nclear stack\nregex OERMetathesis;\n"
                "save stack component.bin\nquit\n"), directory)
            outputs[name] = batch_apply_down(bin_path, forms)
            block = METATHESIS_BLOCK.search(text).group(0)
            component = bin_path.parent / "component.bin"
            report["variants"][name] = {
                "definition": block,
                "source_sha256": hashlib.sha256(text.encode()).hexdigest(),
                "environment": "st" if name in ("A", "C") else "s",
                "vowels": "existing" if name in ("A", "B") else "existing_plus_æ_y",
                "cress_probes": [
                    {**p, "fst_input": form, "pre_sc087": pre,
                     "post_sc087": [apply_down(component, f) for f in pre],
                     "outputs": out, "status": "unresolved_input_and_cell"}
                    for p, form, pre, out in zip(
                        probes, probe_forms, probe_pre,
                        batch_apply_down(bin_path, probe_forms))
                ],
            }
    report["control_matches_canonical"] = outputs["A"] == canonical
    if not report["control_matches_canonical"]:
        raise RuntimeError("factorial control A differs from canonical production")
    for left, right in (("A", "B"), ("A", "C"), ("C", "D"), ("B", "D")):
        changed = []
        for row, pre, old, new in zip(rows, before, outputs[left], outputs[right]):
            if old == new:
                continue
            alternative = row["row_id"] == "2045" and new == ["gærs"]
            changed.append({
                "row_id": row["row_id"], "proto": row["proto"],
                "fst_input": evaluation_input(row), "pre_sc087": pre,
                "selected_target": row["counterpart"],
                "left_outputs": old, "right_outputs": new,
                "left_matches_selected": old == [row["counterpart"]],
                "right_matches_selected": new == [row["counterpart"]],
                "assessment": ("attested_alternative_not_selected" if alternative
                               else "unresolved_attestation"),
                "attested_alternatives": ([
                    {"form": "gærs", "reference":
                     "Campbell 1959 p.184 §459; Hogg 2011 p.297 §7.94"}
                ] if alternative else []),
            })
        report["comparisons"][f"{left}_vs_{right}"] = {
            "rows_changed": len(changed), "changes": changed,
        }
    report["implications"] = {
        "A_vs_B": "Tests s/st with the original eight-vowel enumeration.",
        "A_vs_C": "Isolates vowel expansion while retaining st and the left consonant.",
        "C_vs_D": "Isolates removal of t with the same expanded vowel class.",
        "historical_limit": "Selected-target differences do not establish which "
        "conditioning was productive within a specific dialect and period; an "
        "attested alternative is not an unattested or intrinsically erroneous form.",
    }
    return report


def cress_comparison(rt, source: Path) -> dict:
    """Local component evidence is not an authenticated inherited derivation."""
    sources = variant_sources(source, controlled=True)
    definitions = {name: METATHESIS_BLOCK.search(text).group(0)
                   for name, text in sources.items()}
    text = source.read_text(encoding="utf-8")
    consonants = re.search(
        r"define PGmcStarConsonant \[.*?\];", text, re.DOTALL).group(0)
    local_forms = ["*k*r*e*s*s*e", "*k*r*æ*s*s*e"]
    report = {
        "experiment": "sc087-cress-out-of-sample",
        "germanic.txt_sha256": sha256_of(source),
        "corpus_sha256": sha256_of(rt.corpus_tsv),
        "source_basis": {
            "e_variant": "Campbell 1959 pp.184,190 §§459,476; "
                         "Hogg 2011 p.288 §7.80: cresse > *cersse > cerse",
            "æ_variant": "Ringe–Taylor 2014 p.263: cærse < *cræsse",
            "inherited_family": "Bülbring 1902 p.198 §493: *krasjōn; "
                                "Kluge–Seebold 2011 p.540: WG *krasjō f.",
        },
        "inherited_probes": [],
        "local_components": {},
        "admitted": False,
    }
    for form in ("*krásjōn", "*krásjō"):
        encoded = evaluation_input({"proto_norm": normalize_proto(form)})
        previous = [encoded]
        for stage in named_stages():
            outputs = apply_down(rt.bin_dir / stage.snapshot_bin, encoded)
            if not outputs:
                report["inherited_probes"].append({
                    "input": form, "fst_input": encoded,
                    "first_rejecting_stage": stage.foma_identifier,
                    "previous_outputs": previous,
                    "status": "not_a_live_sc087_witness",
                })
                break
            previous = outputs
        else:
            raise RuntimeError(f"expected diagnostic rejection no longer holds: {form}")
    script = consonants + "\ndefine EnglishStarConsonant PGmcStarConsonant;\n"
    for name, definition in definitions.items():
        script += (definition + f"\nclear stack\nregex OERMetathesis;\n"
                   f"save stack {name}.bin\n")
    with tempfile.TemporaryDirectory() as tmp:
        directory = Path(tmp)
        path = directory / "components.foma"
        path.write_text(script + "quit\n", encoding="utf-8")
        compiled = subprocess.run(["foma", "-q", "-f", path.name], cwd=directory,
                                  capture_output=True, text=True, timeout=60)
        if compiled.returncode or re.search(
                r"(?im)^\*\*\*|syntax error|not defined",
                compiled.stdout + compiled.stderr):
            raise RuntimeError(compiled.stdout + compiled.stderr)
        for name, definition in definitions.items():
            outputs = batch_apply_down(directory / f"{name}.bin", local_forms)
            report["local_components"][name] = {
                "definition": definition,
                "probes": [{"pre_sc087": form, "post_sc087": out,
                            "status": "literature_based_stage_probe_not_corpus_input"}
                           for form, out in zip(local_forms, outputs)],
            }
    report["admission_limit"] = (
        "Both source-based inherited families are rejected before SC087. "
        "Do not change the input gate or earlier laws in this cleanup; the "
        "late-stage probes demonstrate distinct predictions, not a complete "
        "selected reconstruction, attested cell or dialect.")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--controlled", action="store_true",
                       help="run the A–D factorial comparison and local cress probes")
    modes.add_argument("--cress", action="store_true",
                       help="check inherited-family rejection and local stage probes")
    args = parser.parse_args()
    rt = layout()
    if not rt.is_container:
        parser.error("run this Foma experiment inside the backend container")
    source = rt.fsts_dir / "germanic.txt"
    canonical = rt.bin_dir / "old_english.bin"
    rows = load_rows(rt.corpus_tsv)
    if args.controlled or args.cress:
        report = (controlled_comparison(rt, source, rows) if args.controlled
                  else cress_comparison(rt, source))
        receipt = EXPERIMENT_DIR / (
            "controlled_receipt.json" if args.controlled else "cress_receipt.json")
        receipt.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                           encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
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

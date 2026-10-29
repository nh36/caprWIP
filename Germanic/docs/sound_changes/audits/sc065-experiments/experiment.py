#!/usr/bin/env python3
"""SC065 (OEMedialSyncope) counterfactual experiments (backend container).

SC065 currently fires on zero selected corpus rows. These experiments
establish (a) that the zero-firing census is a corpus coverage gap, not a
vacuous rule; (b) how the executable pre-dental formulation relates to the
weight-conditioned high-vowel syncope of the handbooks (R/T §6.7.3,
Campbell §§388-393, 589.6, Luick §306, Bülbring §§431-439); and (c) which
chronological placements are compatible with the attested *-iþō abstracts.

Variants compiled through the identical truncation path:

  production_control    -- unmodified cascade; must match canonical
                           old_english.bin on every selected row.
  retired               -- SC065 replaced by identity. Zero changes
                           demonstrate the zero live firings directly.
  u_extension           -- targets *u as well as *i (handbook laws treat
                           both high vowels). Expected: corrupts hēafod.
  any_consonant         -- drops the pre-dental restriction (deletes *i
                           after a heavy syllable before any consonant).
                           Expected: corrupts hierfest and collides with
                           SC066's l-adjacent domain.
  open_syllable_insitu  -- the handbook weight law (both high vowels, open
                           medial syllable only) at SC065's current
                           cascade site, i.e. after high-vowel apocope.
  open_syllable_pre_apocope -- the same handbook law composed BEFORE
                           OEHighVowelApocope, approximating the
                           handbooks' relative chronology.
  early_pre_umlaut      -- the current pre-dental rule composed BEFORE
                           OEIUmlaut. Witness probes show *-iþō abstracts
                           lose their umlaut trigger (*fūliþō → fūlþ,
                           unattested), evidencing umlaut < syncope.

Witness probes (source-backed reconstruction families, NOT admitted
corpus selections unless separately admitted): *fūliþō 'filth',
*xáiliþō 'health', *θéubiþō 'theft', *wármiþō 'warmth', *strángiþō
'strength', *lángiþō 'length'.

Usage (from the repository root on the host):
  docker compose exec -T backend python3 \
    /usr/app/docs/sound_changes/audits/sc065-experiments/experiment.py
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

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
from capr_runtime import layout  # noqa: E402
from oe_pipeline import (apply_down, evaluation_input, load_rows,
                         named_stages, normalize_proto)  # noqa: E402
from sound_change_order_sensitivity import batch_apply_down  # noqa: E402

EXPERIMENT_DIR = Path(__file__).resolve().parent
TRUNCATION_MARK = "save stack old_english.bin"
SYNCOPE_BLOCK = re.compile(r"define OEMedialSyncope FootCtx\(\[.*?\]\);",
                           re.DOTALL)
COMPOSE_LINE = "    .o. OEMedialSyncope\n"
APOCOPE_LINE = "    .o. OEHighVowelApocope\n"
UMLAUT_LINE = "    .o. OEIUmlaut\n"
PRE_STAGE_BIN = "old_english_sandbox_after_nwgmc_in_stem_n_loss.bin"
DENTALS = "[{*θ}|{*ð}|{*d}|{*t}]"

OPEN_SYLLABLE_BLOCK = """define OEMedialSyncope FootCtx([
    [{*i}|{*u}] -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ OEAnyConsonant EnglishStarVocalic,
    [{*i}|{*u}] -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ OEAnyConsonant EnglishStarVocalic,
    [{*i}|{*u}] -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ OEAnyConsonant EnglishStarVocalic
]);"""

# Source-backed reconstruction families (acute = CAPR stress notation).
WITNESS_PROBES = [
    {"id": "filth", "input": "*fūliþō", "attested": "fȳlþ",
     "basis": "Kroonen 2013:158 *fūla- (OS fulitha f. 'filth'); "
              "BT s.v. FÝLÞ; Clark Hall 1960:125; Campbell §589.6"},
    {"id": "health", "input": "*xáiliþō", "attested": "hǣlþ",
     "basis": "Campbell §589.6 class; BT s.v. hǣlþ"},
    {"id": "theft", "input": "*θéubiþō", "attested": "þīefþ",
     "basis": "Orel 2003 *þeubiþō (ON þýf, OE ðīfð, OFris thiūfthe, OS thiubda)"},
    {"id": "warmth", "input": "*wármiþō", "attested": "wiermþ",
     "basis": "Campbell §589.6 class (wiermþu)"},
    {"id": "strength", "input": "*strángiþō", "attested": "strengþu",
     "basis": "Campbell §589.6; palatalization chronology unresolved in CAPR"},
    {"id": "length", "input": "*lángiþō", "attested": "lengþu",
     "basis": "Campbell §589.6 (leng §589.7); palatalization unresolved"},
]


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def variant_sources(source: Path) -> dict[str, str]:
    text = source.read_text(encoding="utf-8")
    cut = text.find(TRUNCATION_MARK)
    if cut < 0:
        raise RuntimeError(f"missing truncation mark: {TRUNCATION_MARK}")
    text = text[: cut + len(TRUNCATION_MARK)] + "\nquit\n"
    match = SYNCOPE_BLOCK.search(text)
    if not match:
        raise RuntimeError("OEMedialSyncope define not found")
    blk = match.group(0)
    for anchor in (COMPOSE_LINE, APOCOPE_LINE, UMLAUT_LINE):
        if text.count(anchor) != 1:
            raise RuntimeError(f"composition anchor not unique: {anchor!r}")
    variants = {
        "production_control": text,
        "retired": text.replace(blk, "define OEMedialSyncope ?*;"),
        "u_extension": text.replace(
            blk, blk.replace("{*i} -> 0", "[{*i}|{*u}] -> 0")),
        "any_consonant": text.replace(
            blk, blk.replace(DENTALS, "OEAnyConsonant")),
        "open_syllable_insitu": text.replace(blk, OPEN_SYLLABLE_BLOCK),
        "open_syllable_pre_apocope": text.replace(blk, OPEN_SYLLABLE_BLOCK)
        .replace(COMPOSE_LINE, "")
        .replace(APOCOPE_LINE, COMPOSE_LINE + APOCOPE_LINE),
        "early_pre_umlaut": text
        .replace(COMPOSE_LINE, "")
        .replace(UMLAUT_LINE, COMPOSE_LINE + UMLAUT_LINE),
    }
    for name, variant in variants.items():
        if name != "production_control" and variant == text:
            raise RuntimeError(f"variant {name} is identical to control")
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


def classify(row: dict, old: list[str], new: list[str]) -> str:
    target = [row["counterpart"]]
    if old == target and new != target:
        return "corrupts_previously_correct_prediction"
    if old != target and new == target:
        return "repairs_previous_mismatch"
    if old != target and new != target:
        return "alters_existing_mismatch"
    return "unexpected"


def canonical_trace(rt, fst_input: str) -> list[dict]:
    trace, previous = [], [fst_input]
    for stage in named_stages():
        outputs = apply_down(rt.bin_dir / stage.snapshot_bin, fst_input)
        if not outputs:
            trace.append({"stage": stage.foma_identifier,
                          "status": "rejected", "previous": previous})
            break
        if outputs != previous:
            trace.append({"stage": stage.foma_identifier, "outputs": outputs})
            previous = outputs
    return trace


def main() -> int:
    rt = layout()
    if not rt.is_container:
        print("run this Foma experiment inside the backend container",
              file=sys.stderr)
        return 2
    source = rt.fsts_dir / "germanic.txt"
    rows = load_rows(rt.corpus_tsv)
    forms = [evaluation_input(r) for r in rows]
    pre_bin = rt.bin_dir / PRE_STAGE_BIN
    before = batch_apply_down(pre_bin, forms)
    canonical = batch_apply_down(rt.bin_dir / "old_english.bin", forms)
    probe_forms = [evaluation_input({"proto_norm": normalize_proto(p["input"])})
                   for p in WITNESS_PROBES]
    sources = variant_sources(source)
    report = {
        "experiment": "sc065-counterfactuals",
        "generated": time.strftime("%Y-%m-%d %H:%M:%S"),
        "germanic.txt_sha256": sha256_of(source),
        "corpus_sha256": sha256_of(rt.corpus_tsv),
        "selected_rows": len(rows),
        "selected_inputs_sha256": hashlib.sha256(
            json.dumps(rows, ensure_ascii=False, sort_keys=True)
            .encode()).hexdigest(),
        "pre_stage_bin": PRE_STAGE_BIN,
        "filth_canonical_trace": canonical_trace(rt, probe_forms[0]),
        "variants": {},
    }
    outputs = {}
    with tempfile.TemporaryDirectory() as tmp:
        for name, text in sources.items():
            print(f"Compiling variant {name}", flush=True)
            bin_path = compile_variant(name, text, Path(tmp))
            outputs[name] = batch_apply_down(bin_path, forms)
            block = SYNCOPE_BLOCK.search(text)
            report["variants"][name] = {
                "definition": (block.group(0) if block
                               else "define OEMedialSyncope ?*;"),
                "source_sha256": hashlib.sha256(text.encode()).hexdigest(),
                "composition_site": (
                    "before OEIUmlaut" if name == "early_pre_umlaut"
                    else "before OEHighVowelApocope"
                    if name == "open_syllable_pre_apocope"
                    else "canonical (after NWGmcInStemNLoss)"),
                "witness_probes": [
                    {**p, "fst_input": form, "outputs": out,
                     "matches_attested": out == [p["attested"]]}
                    for p, form, out in zip(WITNESS_PROBES, probe_forms,
                                            batch_apply_down(bin_path,
                                                             probe_forms))
                ],
            }
    if outputs["production_control"] != canonical:
        raise RuntimeError("production control differs from canonical bin")
    report["control_matches_canonical"] = True
    for name in sources:
        if name == "production_control":
            continue
        changed = []
        for row, pre, old, new in zip(rows, before,
                                      outputs["production_control"],
                                      outputs[name]):
            if old == new:
                continue
            changed.append({
                "row_id": row["row_id"], "proto": row["proto"],
                "fst_input": evaluation_input(row), "pre_sc065": pre,
                "selected_target": row["counterpart"],
                "control_outputs": old, "variant_outputs": new,
                "control_matches_selected": old == [row["counterpart"]],
                "variant_matches_selected": new == [row["counterpart"]],
                "assessment": classify(row, old, new),
            })
        report["variants"][name]["rows_changed"] = len(changed)
        report["variants"][name]["changes"] = changed
    receipt = EXPERIMENT_DIR / "counterfactual_receipt.json"
    receipt.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8")
    print(f"receipt written: {receipt}")
    for name, data in report["variants"].items():
        probes = {p["id"]: (p["outputs"], p["matches_attested"])
                  for p in data["witness_probes"]}
        print(f"\n{name}: rows_changed={data.get('rows_changed', 0)}")
        for pid, (out, ok) in probes.items():
            print(f"  {pid}: {out} {'OK' if ok else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

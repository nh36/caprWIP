#!/usr/bin/env python3
"""Phase 1/2: emit the adjudicated name/position/granularity audit table.

This is the core adjudication artifact. Mechanical `current_*` fields are loaded
from the registry (staging map + inventory) and the real executable-order
manifest; the judgement fields (`proposed_*`, statuses, action, sources,
conflicts, open questions) are hand-adjudicated from the CAPR research archive
and encoded in ADJUDICATION below, each with a source citation.

Reading trail (files consulted per contested rule) is recorded in
`historical_audit_evidence_inventory.tsv`; the specific source pages/sections
appear in the `existing_capr_sources` column here.

Controlled vocabularies (task spec):
  name_status / position_status : right | wrong | partly_right | unresolved
  granularity_status            : one_historical_change | possibly_conflated |
                                  definitely_conflated | unresolved
  required_action               : no_change | rename_only | move_only |
                                  rename_and_move | metadata_or_prose_only |
                                  split_rule | combine_rules |
                                  revise_implementation | defer_unresolved
"""
from __future__ import annotations

import argparse
import csv
import io
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
STAGING_MAP = SC_DIR / "sound_change_historical_staging_map.tsv"
INVENTORY = SC_DIR / "sound_change_inventory.tsv"
ORDER_MANIFEST = SC_DIR / "cascade_baseline/cascade_order_manifest.tsv"
DEFAULT_OUT = SC_DIR / "cascade_baseline/historical_audit_table.tsv"

TARGETS = [f"SC{n:03d}" for n in range(3, 29)] + ["SC041", "SC042", "SC049", "SC050", "SC064"]

# Default adjudication for the routine, source-clean rules (verified: reader-facing
# prose agrees with the registry stage/scope and FST name). Overridden per-rule below.
def _clean(stage_word: str, source: str) -> dict:
    return {
        "proposed_canonical_name": "",   # "" => keep current
        "proposed_hist_stage": "",
        "proposed_hist_scope": "",
        "supported_earlier_relations": "",
        "supported_later_relations": "",
        "confidence": "A",
        "name_status": "right",
        "position_status": "right",
        "granularity_status": "one_historical_change",
        "required_action": "no_change",
        "existing_capr_sources": source,
        "source_agreement_or_conflict": "agreement",
        "open_questions": "",
    }


ADJUDICATION: dict[str, dict] = {
    # ---- Routine PWGmc rules (reader-facing agrees pan-WGmc) ----
    "SC006": _clean("pwgmc", "006-pwgmc-early-i-apocope.dossier.md; reader 006"),
    "SC007": _clean("pwgmc", "007-pwgmc-final-or-lowering.dossier.md; reader 007"),
    "SC008": _clean("pwgmc", "008-pwgmc-coronal-w-assimilation.dossier.md; reader 008"),
    "SC009": _clean("pwgmc", "009-pwgmc-ij-contraction.dossier.md; reader 009"),
    "SC010": {**_clean("pwgmc", "010-pwgmc-j-gemination.dossier.md; R/T vol.2 p.50"),
              "supported_later_relations": "SC011 (SC010<SC011, fst+historical, A: nett)"},
    "SC011": {**_clean("pwgmc", "011-pwgmc-syllabic-j.dossier.md"),
              "supported_earlier_relations": "SC010 (SC010<SC011, A)"},
    "SC013": _clean("pwgmc", "013-pwgmc-dental-hardening.dossier.md; reader 013"),
    # ---- Routine NWGmc rules (reader-facing agrees Northwest Germanic) ----
    "SC005": {**_clean("nwgmc", "005-nwgmc-a-to-u-before-m.dossier.md; Campbell §331(6)"),
              "supported_later_relations": "SC017 (SC005<SC017, historical+fst, A: shoulders root vowel)"},
    "SC014": _clean("nwgmc", "014-015-opening-vowel-prelude.dossier.md; R/T pp.37-41"),
    "SC015": _clean("nwgmc", "014-015-opening-vowel-prelude.dossier.md; R/T pp.37-41"),
    "SC017": {**_clean("nwgmc", "017-nwgmc-u-lowering.md; Campbell §115; Fulk §4.3"),
              "supported_earlier_relations": "SC005 (SC005<SC017, A); SC016 (SC016<SC017, fst dependency, A: geoc)"},
    "SC018": {**_clean("nwgmc", "018-stressed-monosyllable-o-raising; Campbell §122"),
              "confidence": "B", "position_status": "unresolved",
              "open_questions": "R/T boundary-limited; thin positive local chronology (staging B)"},
    "SC019": {**_clean("nwgmc", "019-nwgmc-final-long-o-raising.dossier.md; R/T pp.30-31"),
              "supported_later_relations": "SC020 (SC019<SC020, A: raste)"},
    "SC021": {
        "proposed_canonical_name": "retired",
        "proposed_hist_stage": "retired",
        "proposed_hist_scope": "retired",
        "supported_earlier_relations": "",
        "supported_later_relations": "SC071 OELateOShortening; SC099 OEMedUnstressedORaising; SC100 OEFinalUnstressedOLowering",
        "confidence": "A",
        "name_status": "wrong",
        "position_status": "wrong",
        "granularity_status": "definitely_conflated",
        "required_action": "retired",
        "existing_capr_sources": "sc021-adjudication.md; reader 021 retirement note",
        "source_agreement_or_conflict": "retired: former PNWGmcUnstressedORaising is unsupported and has no live FST definition, inventory row, staging row, chapter candidacy, or chronology node",
        "open_questions": "Successor analysis is SC071 shortening plus SC099/SC100 medial/final split; do not reactivate SC021 or reuse its identifier.",
    },
    "SC022": {
        "proposed_canonical_name": "",
        "proposed_hist_stage": "pgmc",
        "proposed_hist_scope": "pan_germanic",
        "supported_earlier_relations": "",
        "supported_later_relations": "",
        "confidence": "B",
        "name_status": "partly_right",
        "position_status": "unresolved",
        "granularity_status": "one_historical_change",
        "required_action": "metadata_or_prose_only",
        "existing_capr_sources": "dossier-sc022-mn-dissimilation-2026.md §21; Fulk 2018 p.121 §6.11; Polomé 1967 pp.818-819",
        "source_agreement_or_conflict": "historical stage corrected: Fulk places the change among Common-Germanic developments and Polomé calls -mn- > -bn- older Germanic; stable PNWGmc Foma identifier is not a stage claim",
        "open_questions": "No positive local ordering: first-break result is boundary-limited both sides. NWGmc/OE paradigm leveling and secondary bn > mn are later, separate developments.",
    },
    "SC023": {
        "proposed_canonical_name": "Proto-Germanic Word-Final N Loss",
        "proposed_hist_stage": "pgmc",
        "proposed_hist_scope": "pan_germanic",
        "supported_earlier_relations": "",
        "supported_later_relations": "SC047 OEHeavySyllableNasalApocope (counterfeeding, stage-entailed: OE don retains secondary final -n; Ringe 2017:101-103); SC069 OEEarlyOShortening (17 in-domain weak-noun witnesses)",
        "confidence": "A",
        "name_status": "partly_right",
        "position_status": "right",
        "granularity_status": "one_historical_change",
        "required_action": "metadata_or_prose_only",
        "existing_capr_sources": "sc023-adjudication.md; Ringe 2017 pp.90,101-103,163,168-169; R/T 2014 pp.54-55,58-59; Fulk 2018 pp.170-171 §7.31",
        "source_agreement_or_conflict": "historical stage corrected: general (pre-)PGmc loss of word-final *-n with nasalization (Gothic tuggo shares it), not a NWGmc n-stem rule; the {*o-n} restriction is a deliberate citation-form proxy (numerals sebun/nigun/tehun retained -un by analogy); stable PNWGmc Foma identifier is not a stage claim",
        "open_questions": "None material: firing population is exactly the 17 weak-noun citation stems; do is a counterfeeding (negative) witness only.",
    },
    "SC024": {
        "proposed_canonical_name": "Long E Lowering with Anglo-Frisian Fronting",
        "proposed_hist_stage": "eaf",
        "proposed_hist_scope": "anglo_frisian",
        "supported_earlier_relations": "",
        "supported_later_relations": "SC056 OEWsPalatalDiphthongization (independently demonstrated: WS diphthongization operated on already-fronted ae — sceap, gear; Campbell §185, R/T 2014 p.216)",
        "confidence": "A",
        "name_status": "partly_right",
        "position_status": "right",
        "granularity_status": "one_historical_change",
        "required_action": "metadata_or_prose_only",
        "existing_capr_sources": "sc024-adjudication.md; R/T 2014 pp.11-14,142-153,169-170,216; Campbell 1959 §§127-132,185",
        "source_agreement_or_conflict": "historical stage/scope corrected: the rule telescopes pan-NWGmc *e1 > *a (runic makija, 2nd c. AD) plus Anglo-Frisian fronting of non-nasalized *a > ae (OS/OHG/ON keep a), so the fronted outcome is Anglo-Frisian, not pan-NWGmc; the one-step *e > *ae proxy deliberately keeps *e1 reflexes disjoint from a < *ai (stan, ham; Campbell §132 ordering encoded by symbol separation); stable PNWGmc Foma identifier is not a stage claim",
        "open_questions": "The *a-detour vs. direct-retention dispute (Campbell §129 agnostic; R/T pp.13-14 accept the detour) is recorded, not resolved — the proxy is compatible with both. 5 of 18 firings (father, mother, sister, have, live) are unstressed selected-input proxies, not witnesses of the stressed law.",
    },
    "SC025": {**_clean("nwgmc", "025-nwgmc-long-e-nasal-rounding.dossier.md"), "confidence": "B"},
    "SC028": _clean("nwgmc", "028-nwgmc-preconsonantal-x-loss; Campbell §417; R/T pp.156-158"),

    # ---- Contested / adjudicated rules ----
    "SC003": {
        "proposed_canonical_name": "WGmcRhotacism",
        "proposed_hist_stage": "wgmc", "proposed_hist_scope": "pan_wgmc",
        "supported_earlier_relations": "final-*z* losses (Crist2002 §6; R/T vol.2 p.87: rhotacism at the end of the z-loss sequence; enforced by cascade ordering — EAFRhotacism composed after MonosyllabicFinalZLoss; B)",
        "supported_later_relations": "SC044 OEBreaking (terminus ante quem, lexical A: liznojana>liornian, mizdai>meorde)",
        "confidence": "A",
        "name_status": "wrong", "position_status": "partly_right",
        "granularity_status": "one_historical_change",
        "required_action": "rename_only",
        "existing_capr_sources": "reader 003-west-germanic-rhotacism.md; change_reports/full/003; R/T pp.52,87,98,102; Crist2001 pp.104-106, Crist2002 pp.1,4; Hogg p.37",
        "source_agreement_or_conflict": "agreement (reader+registry both: WGmc, not PGmc); FST name is the sole legacy error",
        "open_questions": "Implementation broader than intervocalic (retains medial VzC); relation to the final-z rules now enforced by genuine cascade ordering (2026 rhotacism-position correction)",
    },
    "SC004": {
        "proposed_canonical_name": "",  # defer until split decided
        "proposed_hist_stage": "pnwgmc (word-final *e component) / uncertain (nonfinal *a generalization)",
        "proposed_hist_scope": "pan_nwgmc (word-final) / uncertain (nonfinal)",
        "supported_earlier_relations": "",
        "supported_later_relations": "OEInterStressRaising (lexical A: saiwalo>sawol; monophthongization precedes interstress raising)",
        "confidence": "B",
        "name_status": "partly_right", "position_status": "partly_right",
        "granularity_status": "definitely_conflated",
        "required_action": "split_rule",
        "existing_capr_sources": "reader 004-pwgmc-ai-monophthongization.md; change_reports/full/004; R/T pp.40-41",
        "source_agreement_or_conflict": "conflict: FST composes word-final *ai>*e (early NWGmc, well-supported) + nonfinal *ai>*a (generalization 'stated more sharply than handbooks'); registry labels whole as pnwgmc_pwgmc_transition",
        "open_questions": "Should the two sub-rewrites be split? Word-final merger is early NWGmc; nonfinal *ai>*a dating uncertain. Split decision precedes any rename.",
    },
    "SC012": {
        "proposed_canonical_name": "NorthWGmcLThVoicing",
        "proposed_hist_stage": "wgmc", "proposed_hist_scope": "north_wgmc",
        "supported_earlier_relations": "", "supported_later_relations": "",
        "confidence": "B",
        "name_status": "partly_right", "position_status": "right",
        "granularity_status": "one_historical_change",
        "required_action": "metadata_or_prose_only",
        "existing_capr_sources": "reader 012-lth-voicing.md; change_reports/full/012; dossier 012; R/T pp.170-171 (northern WGmc); Campbell §414",
        "source_agreement_or_conflict": "CONFLICT: registry says pan_wgmc/confidence A/'no staging issue'; reader+change-report+dossier all say northern WGmc and explicitly reject unqualified pan-PWGmc",
        "open_questions": "Narrow scope to north_wgmc and downgrade confidence A->B; chronology boundary-only both sides (no positive local seam)",
    },
    "SC016": {
        "proposed_canonical_name": "", "proposed_hist_stage": "", "proposed_hist_scope": "",
        "supported_earlier_relations": "",
        "supported_later_relations": "SC017 PNWGmcULowering (fst/technical dependency, A: juka>geoc requires glide before u-lowering)",
        "confidence": "B",
        "name_status": "right", "position_status": "partly_right",
        "granularity_status": "one_historical_change",
        "required_action": "metadata_or_prose_only",
        "existing_capr_sources": "reader 016-west-saxon-palatal-glide.md; Campbell §44",
        "source_agreement_or_conflict": "agreement: OE West Saxon rule; name/stage already accurate",
        "open_questions": "Cascade position (pos 13, before many NWGmc rules) is an FST dependency, not a historical claim; trace/prose must show stage(OE-WS) != position",
    },
    "SC020": {
        "proposed_canonical_name": "WGmcFinalZDeletion",
        "proposed_hist_stage": "wgmc", "proposed_hist_scope": "pan_wgmc (vs Ingvaeonic: open)",
        "supported_earlier_relations": "SC019 PNWGmcFinalLongORaising (lexical A: rastoz>raste)",
        "supported_later_relations": "SC040 OEMedUnstressedULowering (lexical A: bebruz>befer)",
        "confidence": "A (position) / B (scope)",
        "name_status": "wrong", "position_status": "right",
        "granularity_status": "one_historical_change",
        "required_action": "rename_only",
        "existing_capr_sources": "reader 020-wgmc-final-z-deletion.md; dossier 020; Hogg p.37; Crist2002 p.1",
        "source_agreement_or_conflict": "agreement (reader+registry: WGmc pan-WGmc, not PGmc); FST name is legacy error",
        "open_questions": "Scope all-WGmc vs Ingvaeonic unresolved; exact relation to SC003 rhotacism (bleeding of final vs medial *z) to confirm jointly",
    },
    "SC026": {
        "proposed_canonical_name": "NSGNasalSpirantLengthening",
        "proposed_hist_stage": "ingvaeonic", "proposed_hist_scope": "north_sea_germanic",
        "supported_earlier_relations": "", "supported_later_relations": "SC027 (SC026<SC027, lexical A: fist/goose/youth corridor)",
        "confidence": "B",
        "name_status": "wrong", "position_status": "right",
        "granularity_status": "one_historical_change",
        "required_action": "rename_only",
        "existing_capr_sources": "change_reports/full/026-027; Campbell §121; Fulk §4.11; Luick §§299,301.1; Sievers-Brunner §186.1; R/T pp.140-141",
        "source_agreement_or_conflict": "agreement (registry already ingvaeonic/north_sea_germanic); FST name NWGmc* is wrong; pair is one development split for modeling",
        "open_questions": "SC026+SC027 = one historical development split into two model rules; keep split (defended) but correct names; earlier boundary runner-limited",
    },
    "SC027": {
        "proposed_canonical_name": "NSGNasalSpirantLoss",
        "proposed_hist_stage": "ingvaeonic", "proposed_hist_scope": "north_sea_germanic",
        "supported_earlier_relations": "SC026 (SC026<SC027, lexical A)", "supported_later_relations": "",
        "confidence": "B",
        "name_status": "wrong", "position_status": "right",
        "granularity_status": "one_historical_change",
        "required_action": "rename_only",
        "existing_capr_sources": "change_reports/full/026-027; Fulk §4.11; Luick §301.1; R/T pp.140-141",
        "source_agreement_or_conflict": "agreement (registry ingvaeonic); FST name NWGmc* wrong; later half of the modeled corridor",
        "open_questions": "Later boundary no-break through order 86 (no positive later seam)",
    },
    "SC041": {
        "proposed_canonical_name": "", "proposed_hist_stage": "", "proposed_hist_scope": "",
        "supported_earlier_relations": "", "supported_later_relations": "",
        "confidence": "B",
        "name_status": "right", "position_status": "right",
        "granularity_status": "one_historical_change",
        "required_action": "no_change",
        "existing_capr_sources": "change_reports/full/041; Campbell §341; R/T pp.60-61 (already PWGmc)",
        "source_agreement_or_conflict": "agreement: R/T date final short-low-vowel loss to PWGmc; name accurate",
        "open_questions": "Chronology broader than the local widow pair; singleton hinge, no tight local seam",
    },
    "SC042": {
        "proposed_canonical_name": "", "proposed_hist_stage": "", "proposed_hist_scope": "",
        "supported_earlier_relations": "", "supported_later_relations": "SC043 EAFBrightening (feeder, fst dependency)",
        "confidence": "B",
        "name_status": "partly_right", "position_status": "right",
        "granularity_status": "one_historical_change",
        "required_action": "metadata_or_prose_only",
        "existing_capr_sources": "change_reports/full/042; Campbell §§131,157-158; Hogg pp.101,119; R/T pp.157-158,189-190",
        "source_agreement_or_conflict": "agreement but label is model-shaped (narrow feeder behind rest), not a standard named law",
        "open_questions": "Present as narrow model feeder, not a coequal chapter",
    },
    "SC049": {
        "proposed_canonical_name": "", "proposed_hist_stage": "", "proposed_hist_scope": "",
        "supported_earlier_relations": "SC010 PWGmcJGemination (fst dependency, A: b-allophony must follow gemination so [B] surfaces only on singleton *b)",
        "supported_later_relations": "",
        "confidence": "A",
        "name_status": "right", "position_status": "partly_right",
        "granularity_status": "one_historical_change",
        "required_action": "metadata_or_prose_only",
        "existing_capr_sources": "change_reports/full/049-050; Hogg pp.101-102; R/T p.121; Luick p.107",
        "source_agreement_or_conflict": "agreement: PGmc/PWGmc *b stop/fricative allophony is a real inherited distribution; late cascade pos 46 is a documented FST dependency",
        "open_questions": "Stage(pgmc) != cascade position(46); divergence already documented, keep; ensure trace/prose explain the computational placement",
    },
    "SC050": {
        "proposed_canonical_name": "", "proposed_hist_stage": "", "proposed_hist_scope": "",
        "supported_earlier_relations": "",
        "supported_later_relations": "SC051 OESkPalatalization / SC052 OEVelarPalatalization (feeder, fst dependency)",
        "confidence": "B",
        "name_status": "right", "position_status": "partly_right",
        "granularity_status": "one_historical_change",
        "required_action": "metadata_or_prose_only",
        "existing_capr_sources": "change_reports/full/049-050; Adamczyk2001; Fulk §6.15; R/T vol.2 p.157",
        "source_agreement_or_conflict": "agreement: Sievers' Law is real PWGmc/PGmc material; placed late as palatalization feeder",
        "open_questions": "Stage(pwgmc) earlier than cascade pos 47; the late placement is a modeling feeder role, document it",
    },
    "SC064": {
        "proposed_canonical_name": "", "proposed_hist_stage": "unresolved", "proposed_hist_scope": "unresolved",
        "supported_earlier_relations": "OEHighVowelApocope (cross-source A: *-n-after-*i loss follows OE high-V apocope; R/T vol.2 pp.71-72; Campbell §§472-473; Brunner §280; Fulk §7.34; Bammesberger §7.3.4)",
        "supported_later_relations": "",
        "confidence": "C",
        "name_status": "unresolved", "position_status": "right",
        "granularity_status": "one_historical_change",
        "required_action": "defer_unresolved",
        "existing_capr_sources": "change_reports/full/064-065; Kroonen p.201 (*furht-); R/T §§6.7.3-6.8.4",
        "source_agreement_or_conflict": "CONFLICT within registry: hist_stage=nwgmc but v1_chapter=4 (OE); rule operates in OE post-apocope tail; name NWGmc* likely wrong; confidence C",
        "open_questions": "Genuinely unresolved stage: narrow witness-driven *n-loss after *i; chronologically OE-adjacent though phenomenon may be older. Defer stage/name until adjudicated.",
    },
}


def _read_tsv_skip_comments(path: Path) -> dict:
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines() if not ln.startswith("#")]
    return {r["sc_id"]: r for r in csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t")}


FIELDS = [
    "sc_id", "current_foma_identifier", "implemented_transformation",
    "current_cascade_position", "current_reader_name", "current_book_chapter",
    "current_hist_stage", "current_hist_scope",
    "proposed_canonical_name", "proposed_hist_stage", "proposed_hist_scope",
    "supported_earlier_relations", "supported_later_relations", "confidence",
    "name_status", "position_status", "granularity_status", "required_action",
    "existing_capr_sources", "source_agreement_or_conflict", "open_questions",
]


def build_rows() -> list[dict[str, str]]:
    staging = _read_tsv_skip_comments(STAGING_MAP)
    inv_lines = [ln for ln in INVENTORY.read_text(encoding="utf-8").splitlines() if not ln.startswith("#")]
    inv = {r["change_id"]: r for r in csv.DictReader(io.StringIO("\n".join(inv_lines)), delimiter="\t")}
    with ORDER_MANIFEST.open(encoding="utf-8") as handle:
        pos = {r["foma_identifier"]: r["position"] for r in csv.DictReader(handle, delimiter="\t")}

    rows: list[dict[str, str]] = []
    for sc in TARGETS:
        s = staging.get(sc, {})
        i = inv.get(sc, {})
        adj = ADJUDICATION.get(sc)
        if adj is None:
            raise ValueError(f"no adjudication encoded for {sc}")
        foma = s.get("fst_identifier", "")
        cascade_pos = pos.get(foma, "pre-pipeline (support rule)")
        row = {
            "sc_id": sc,
            "current_foma_identifier": foma,
            "implemented_transformation": (i.get("foma_definition_raw", "") or "").strip(),
            "current_cascade_position": cascade_pos,
            "current_reader_name": s.get("display_name", ""),
            "current_book_chapter": s.get("v1_chapter", ""),
            "current_hist_stage": s.get("hist_stage", ""),
            "current_hist_scope": s.get("hist_scope", ""),
        }
        row.update({k: adj.get(k, "") for k in FIELDS if k not in row})
        rows.append(row)
    return rows


def write_table(rows: list[dict[str, str]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    rows = build_rows()
    write_table(rows, args.out)
    print(f"wrote {args.out} ({len(rows)} rules)")
    if args.summary:
        from collections import Counter
        for col in ("name_status", "position_status", "granularity_status", "required_action"):
            print(f"  {col}: {dict(Counter(r[col] for r in rows))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

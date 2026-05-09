---
row_id: 1941
concept: beaver
counterpart: befer
proto: *bébruz
protoform: *bébruz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1941 beaver / befer

## Current row state

- CONCEPT: `beaver`
- COUNTERPART: `befer`
- PROTO: `*bébruz`
- PROTOFORM: `*bébruz`
- DERIVATION_CLASS: `regular`
- The live Old English TSV row is stable and uncomplicated at metadata level: row `1941` currently reads `beaver / befer / *bébruz`, with `PROTO = PROTOFORM` and `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:36-36].
- `oe_known_problems.tsv` has no row-specific entry for `*bébruz`; current exception tracking does not classify the lexeme as a known analogical or wontfix problem [Germanic/data/oe_known_problems.tsv:1-8].
- No row-matching packet or research memo is currently recorded for this lexeme. `coverage_audit.md` still lists row `1941` as `none`, with no linked report infrastructure to reuse [Germanic/docs/lexeme_reports/coverage_audit.md:197-197].
- The current published derivation trace already reaches the attested target without workaround: `Proto Input: *bébruz` > `PGmc Final Z Deletion: *bébru` > `PGmc B Allophony: *béβru` > `OE High Vowel Apocope: *béβr` > `OE Epenthetic Vowel: *béβer` > orthographic `befer` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:126-145].

## Development-note summary

DEV_NOTES support for row `1941` is substantial enough to preserve real project history, but it is mixed: part of it is **current shared philology**, and part of it is **superseded debugging chronology**. The most important current philological passage is the Campbell quotation that explicitly names `befer` as a West Saxon back-mutation form: DEV_NOTES quotes Campbell §210 as saying that in West Saxon “u-umlaut is general before labials and liquids” and gives `befer` among the examples [Germanic/docs/DEV_NOTES.md:33855-33855]. That matters because it shows that the row's target is not merely whatever the current FST happens to emit; DEV_NOTES preserves an explicit source claim that `befer` is the kind of form OE phonology is supposed to produce.

The implementation history in DEV_NOTES is also unusually clear. An earlier consonant-bucket audit still had the row failing as `*bebruz → beber (expected befer)`, under the heading `intervocalic_voicing_missing` [Germanic/docs/DEV_NOTES.md:1569-1576]. Later OE diagnostics then caught a different failure mode: the grammar was still leaving final high vowels in place, and `bebru` appears in the sample bad outputs [Germanic/docs/DEV_NOTES.md:2481-2484]. The subsequent high-vowel apocope repair explicitly used `bebruz` as a verification probe and says that `balluz/balgiz/bebruz` now yield “a **single** output at each stage, with apocope firing deterministically in heavy contexts” [Germanic/docs/DEV_NOTES.md:2509-2520].

After that, DEV_NOTES records a more specific regression in the `*-uz` chronology work. Once `PGmcFinalZDeletion` had been moved too low in the pipeline, `*bébruz` became one of the eight new `*CVCuz` failures: `befro` instead of `befer` [Germanic/docs/DEV_NOTES.md:24443-24464]. The note is explicit about the mechanism: at `OEMedUnstressedULowering`, the form was still effectively `*bebruz`, so the final `u` looked medial because `z` still stood to its right; it therefore lowered to `o`, and the pipeline “cannot reach the attested *befer” because the high vowel needed for the normal apocope/syncope path had already been destroyed [Germanic/docs/DEV_NOTES.md:24466-24489]. The immediately following subsection then proposes moving z-loss back up after raising, and the next status line says that §17.10.24 + §17.10.25 were applied and committed, with Case 3 chronology work closed [Germanic/docs/DEV_NOTES.md:24513-24567].

Taken together, these fragments support a precise working note. The target `befer` has direct source support in DEV_NOTES via Campbell; the current derivation trace now succeeds; and the note history preserves three distinct superseded failure stages (`beber`, `bebru`, `befro`) that should not be mistaken for rival lexical analyses. They are debugging states from different moments in the pipeline, not alternative counterpart choices for row `1941` [Germanic/docs/DEV_NOTES.md:1569-1576,2481-2484,24443-24567; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:126-145].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-33855-33855

- Source heading: back-mutation discussion citing Campbell §210
- Source line or section hint: `line 33855`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `back_mutation`; `campbell_quote`; `target_support`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the strongest current DEV_NOTES support for the row because it mentions the OE form directly. DEV_NOTES quotes Campbell as follows: “(1) In W-S u-umlaut is general **before labials and liquids**, e.g. heofon heaven, eofor boar, ... but also with suffix containing front vowel, hefen, **befer**, and hence with suffix mixture hefon, befor, efor” [Germanic/docs/DEV_NOTES.md:33855-33855]. For row `1941`, the practical point is narrow but important: `befer` is preserved inside DEV_NOTES as an explicit source-backed West Saxon form, so the row's target has direct philological support and should not be treated as a mere placeholder output.

### DEV_NOTES:line-1569-1576

- Source heading: consonant mismatch bucket audit
- Source line or section hint: `lines 1569-1576`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `early_failure_state`; `intervocalic_fricativization`; `beber_output`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This is the earliest explicit DEV_NOTES mention of the lexeme as a mismatch. Under `intervocalic_voicing_missing`, DEV_NOTES lists `*bebruz → beber (expected befer)` beside `*drībăną → drīban (expected drīfan)` [Germanic/docs/DEV_NOTES.md:1575-1576]. The label is slightly misleading by later terminology, but the preserved substance is still useful: at this stage the row's problem was understood as failure to surface the expected fricative/orthographic `f`. That `beber` output is superseded and should be retained only as early diagnostic history.

### DEV_NOTES:line-2481-2484

- Source heading: `Ending diagnostics (old_english.bin)`
- Source line or section hint: `lines 2481-2484`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `final_high_vowel`; `tail_diagnostics`; `bebru_output`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This fragment preserves a later but different failure mode. DEV_NOTES says: “Sample `-i/-u` outputs: `ballu` (ball), `bebru` (beaver), `balgi` (belly), `crafti` (craft), `bugu` (bough)” [Germanic/docs/DEV_NOTES.md:2484-2484]. For row `1941`, this shows that before the heavy-syllable apocope cleanup, the pipeline was still leaving final high vowel `-u` in place. `bebru` is therefore not an alternative historical form; it is a tail-diagnostic output from an earlier broken stage of the OE cascade.

### DEV_NOTES:line-2509-2520

- Source heading: `High-vowel loss debug (2025-12-21)`
- Source line or section hint: `lines 2509-2520`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `high_vowel_apocope`; `deterministic_fix`; `shared_probe`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the main current implementation-side fragment for the row's tail behavior. DEV_NOTES says the weight-marker rule had been nondeterministic, “yielding both apocopated and non-apocopated outputs,” and then reports the repair: `balluz/balgiz/bebruz` now yield “a **single** output at each stage, with apocope firing deterministically in heavy contexts” [Germanic/docs/DEV_NOTES.md:2509-2520]. For `*bébruz`, the fragment does not by itself explain the whole derivation, but it does preserve one key current claim: final high-vowel loss was explicitly debugged with `bebruz` as a probe, and that part of the pathway is now meant to be stable rather than optional.

### DEV_NOTES:line-24443-24510

- Source heading: `§17.10.25 — Case 3 Option δ post-reorder: *-uz cluster regression`
- Source line or section hint: `lines 24443-24510`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `final_z_deletion`; `u_lowering`; `befro_output`; `rule_ordering`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This is the most detailed lexeme-specific debugging note for row `1941`, even though it is no longer current output state. DEV_NOTES lists `*bébruz | befro | befer` among the eight new `*CVCuz` mismatches after a z-loss reorder [Germanic/docs/DEV_NOTES.md:24451-24464]. It then gives an explicit causal explanation: “in forms like *bébruz, at the `OEMedUnstressedULowering` stage the form is still *bebruz — the *u has a real *z to its right, satisfying the `_ C` context — and it lowers to *bebroz. Then, finally, z-loss fires, yielding *bebro. From there the OE pipeline cannot reach the attested *befer (the *u would have had to survive as a word-final high vowel to drive the expected apocope and syncope pattern)” [Germanic/docs/DEV_NOTES.md:24480-24486]. This fragment is exactly the kind of detailed replacement-note material worth preserving: it records not just that `befro` was wrong, but why that temporary rule ordering made `befer` impossible.

### DEV_NOTES:line-24513-24567

- Source heading: `§17.10.25` expected outcome and `§17.10.26` closure status
- Source line or section hint: `lines 24513-24567`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `fix_rationale`; `chronology_closure`; `shared_-uz_problem`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

The value of this follow-on fragment is that it preserves the intended repair and the project's statement that the chronology issue was closed. DEV_NOTES says z-loss should fire “**immediately after raising**” so that OE-stage rules run against “a z-free input” [Germanic/docs/DEV_NOTES.md:24513-24524]. In the expected-outcome list it adds that “All eight `*-uz` regressions dissolve” once z-loss is moved back above `OEMedUnstressedULowering` [Germanic/docs/DEV_NOTES.md:24539-24551]. The next section then records the status update: “§17.10.24 + §17.10.25 applied and committed as `45f7db7`. Mismatch count 37. Case 3 chronology work is **closed**” [Germanic/docs/DEV_NOTES.md:24564-24567]. For row `1941`, that is the bridge from the stale `befro` regression to the current successful trace.

## Superseded or diagnostic material

- DEV_NOTES preserves three different obsolete bad outputs for this row, and they belong to three different debugging moments: `beber` (fricativization/consonant bucket), `bebru` (final high-vowel retention), and `befro` (late z-loss causing bad `u > o`) [Germanic/docs/DEV_NOTES.md:1575-1576,2484-2484,24451-24486].
- The alternation between `*bebruz` and `*bébruz` in DEV_NOTES should not be overread. In the passages relevant here, it functions as notation drift across sessions, not as evidence for different lexical inputs; the live row and current trace both use `*bébruz` [Germanic/data/germanic-aligned-final.tsv:36-36; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:126-145].
- No surviving row-specific packet or memo currently supersedes this slice. Until such infrastructure exists, this file has to carry both the current source-backed target support (`befer` in Campbell via DEV_NOTES) and the condensed debugging chronology [Germanic/docs/lexeme_reports/coverage_audit.md:197-197; Germanic/docs/DEV_NOTES.md:33855-33855,24443-24567].

## Open questions for later work

- If a full packet is later built for row `1941`, decide whether the opening emphasis should be philological (`befer` as an explicit Campbell back-mutation example) or implementation-historical (the `*-uz` chronology regression and repair) [Germanic/docs/DEV_NOTES.md:33855-33855,24443-24567].
- Decide whether the row is strong enough for eventual `index.tsv` inclusion on the basis of the current material alone. The case is better than a thin shared-note row because DEV_NOTES contains both a direct source-backed mention of `befer` and a detailed row-specific regression analysis, but the supporting dossier is still concentrated in shared chronology/debug sections rather than in a dedicated beaver memo.
- If later work revisits OE epenthetic-vowel conditioning, recheck whether the current trace's `*béβr > *béβer > befer` pathway continues to align with the Campbell-style back-mutation framing preserved in DEV_NOTES [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:139-145; Germanic/docs/DEV_NOTES.md:33855-33855].

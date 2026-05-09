---
row_id: 1960
concept: bough
counterpart: bōg
proto: *bōguz
protoform: *bōguz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1960 bough / bōg

## Current row state

- The live Old English row reads `CONCEPT = bough`, `COUNTERPART = bōg`, `PROTO = *bōguz`, `PROTOFORM = *bōguz`, and `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:110-112].
- `coverage_audit.md` still marks row 1960 as having no packet, no research memo, no linked dossier/analysis file, and overall status `none`, so the metadata links in this slice remain blank [Germanic/docs/lexeme_reports/coverage_audit.md:206-206].
- The published derivation trace already matches the live target without workaround: `# bough`, `PROTO: *bōguz`, `EXPECTED: bōg`, `OUTPUTS: bōg`, with the chain `*bōguz > *bōgu > bōg` via PGmc final `-z` deletion and OE high-vowel apocope [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:429-448].
- `oe_known_problems.tsv` currently lists several OE exception buckets, including unrelated `u`-lowering exceptions such as `*búkkaz`, `*fúglaz`, and `*wúlfaz`, but it does not list `*bōguz` or `bōg`; row 1960 is therefore not presently being tracked as an open OE problem entry [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

DEV_NOTES support for row 1960 is real but mostly **shared rather than row-local**. No standalone `bough / bōg` dossier survives in the live DEV_NOTES file. Instead, the row appears in three materially relevant places: a shared long-vowel triage note, a shared word-final `g ~ h` spelling-policy discussion, and a later diagnostic regression table. The replacement slice should preserve that thin-but-direct support honestly rather than inflating it into a lexeme-specific controversy [Germanic/docs/DEV_NOTES.md:1760-1766,10909-11024,24436-24485].

The earliest directly relevant statement is phonological and uncomplicated: “**OE ō before velars should stay long** → move `EnglishVelarShortening` out of the OE block (OE keeps `bōc/bōg`)” [Germanic/docs/DEV_NOTES.md:1760-1766]. For this row, that is the cleanest project-level claim about vowel quantity. It means the long `ō` of `bōg` is not an accident, not a target-side patch, and not something that should be sacrificed to an overbroad OE velar-shortening rule. In row terms, `PROTO` and `PROTOFORM` both remain `*bōguz`, and the live `COUNTERPART` `bōg` is the expected long-vowel outcome in precisely this environment [Germanic/data/germanic-aligned-final.tsv:111-111; Germanic/docs/DEV_NOTES.md:1760-1766].

The more substantial DEV_NOTES material comes from the later `Word-Final *g Spirantization Research (2026-03-15)` section. That note records that an attempted final-spirantization rule immediately broke row 1960: “`*bōguz` → `bōh` (expected `bōg`)” [Germanic/docs/DEV_NOTES.md:10913-10916]. This matters because it shows that `bōg` was not the form needing rescue; it was one of the forms used to prove the proposed OE-final-`g > h` rule was too aggressive for the repo's chosen normalization. DEV_NOTES then quotes Campbell on the chronology and spelling distribution of final `ɣ`: “for final ɣ there is an increasing use of the symbol `h` after Alfred's time,” but the same discussion also stresses that the alternation was “not categorical” and that `h` and `g` spellings coexisted, even with “inverted spellings” using `g` where `h` might be expected [Germanic/docs/DEV_NOTES.md:10920-10937].

That background leads directly to the row-relevant policy decision. DEV_NOTES says the TSV had become inconsistent because `lēah, troh` followed a Late West Saxon `-h` convention while `bōg, dāg` followed an earlier/northern `-g` convention [Germanic/docs/DEV_NOTES.md:10959-10961]. After considering four options, the note adopts “**Option D with `-g` convention (early/Northern spelling)**,” explicitly because this avoids adding a new sound-change rule and “reflects the more conservative spelling attested across multiple dialects” [Germanic/docs/DEV_NOTES.md:10990-11024]. For row 1960, that is the controlling current explanation: `bōg` is the retained dataset target because the project chose a shared normalization policy that keeps final `-g` where attestation and conservative spelling practice support it. Nothing in that section suggests changing `PROTO` or `PROTOFORM`; the row remained regular, and the proposed change was rejected at the rule/policy level instead [Germanic/docs/DEV_NOTES.md:10909-11024].

The much later `*-uz cluster regression` note should be kept, but only as **diagnostic history**. There the row appears in a mismatch table as `*bōguz | bōgo | bōg`, after a reordering that let late `z`-deletion interfere with the environment for `OEMedUnstressedULowering` [Germanic/docs/DEV_NOTES.md:24436-24485]. This is not a philological argument about the lexeme itself. It is implementation archaeology showing that if final `-z` is deleted too late, `*CVCuz` nouns can be misread as though they still had a medial consonant after `u`, yielding bad outputs like `bōgo`. Since the published live trace again gives `bōg`, the value of this passage is purely diagnostic: it records one way the grammar temporarily broke a regular row, not a live reason to doubt the row [Germanic/docs/DEV_NOTES.md:24453-24485; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:429-448].

## Relevant DEV_NOTES fragments

### Germanic/docs/DEV_NOTES.md:1760-1766

- Source heading: `Next actionable targets (carryover)` / `Long-vowel missing`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `long_vowel_preservation`; `shared_rule_support`; `ō_before_velar`; `regular_reflex`
- Recommended next use: `cite_in_final_report`

This is the clearest direct phonological support for row 1960. DEV_NOTES says: “**OE ō before velars should stay long** → move `EnglishVelarShortening` out of the OE block (OE keeps `bōc/bōg`)” [Germanic/docs/DEV_NOTES.md:1760-1766]. For `*bōguz > bōg`, the passage matters because it states exactly the row's expected quantity outcome: OE `ō` is supposed to survive before the velar, and `bōg` is named explicitly as a control example.

### Germanic/docs/DEV_NOTES.md:10909-10917

- Source heading: `Word-Final *g Spirantization Research (2026-03-15)` / `The mismatch report shows`
- Fragment type: `shared_problem_definition_with_row_specific_regression`
- Status: `diagnostic_but_still_useful`
- Issue tags: `g_vs_h`; `failed_rule`; `row_as_regression_control`; `target_policy`
- Recommended next use: `use_to_explain_why_no_final_h_rule_was_added`

This fragment preserves the immediate row-specific failure that made the proposed rule unacceptable. DEV_NOTES first lists the original mismatch set `*laugō → lēag (expected lēah)` and `*trugą → trog (expected troh)`, then records the regression caused by the attempted rule: “`*bōguz` → `bōh` (expected `bōg`)” and “`*daigăz` → `dāh` (expected `dāg`)” [Germanic/docs/DEV_NOTES.md:10909-10917]. For row 1960, this is crucial project history: `bōg` functioned as evidence against the candidate final-spirantization rule, not as a lexeme awaiting correction.

### Germanic/docs/DEV_NOTES.md:10920-10937

- Source heading: `Source Research`
- Fragment type: `shared_phonology_and_spelling_background`
- Status: `current`
- Issue tags: `Campbell`; `final_spirant`; `spelling_variation`; `g_h_alternation`
- Recommended next use: `cite_in_final_report`

This shared background is materially relevant because it explains why the row can remain `bōg` without denying that `-h` spellings existed elsewhere. DEV_NOTES quotes Campbell §446: “for final ɣ there is an increasing use of the symbol `h` after Alfred's time,” and Campbell §447: “The interchange of `h` and `g` ...” with “inverted spellings” as well [Germanic/docs/DEV_NOTES.md:10920-10937]. The note's own conclusion is that the alternation was “not categorical” [Germanic/docs/DEV_NOTES.md:10936-10937]. For row 1960, that shared framework is the reason `bōg` can be kept as a normalized target under a conservative `-g` convention rather than treated as a mistake.

### Germanic/docs/DEV_NOTES.md:10959-11024

- Source heading: `Analysis`; `Options`; `Decision: Use -g Spelling Convention (2026-03-15)`
- Fragment type: `current_row_policy_in_shared_section`
- Status: `current`
- Issue tags: `live_row_policy`; `target_normalization`; `no_new_rule`; `shared_decision`
- Recommended next use: `primary_index_anchor_if_needed`

This is the controlling current fragment for the live row. DEV_NOTES states the inconsistency plainly: “`lēah`, `troh` use the Late WS `h` convention” while “`bōg`, `dāg` use the earlier/Northumbrian `g` convention” [Germanic/docs/DEV_NOTES.md:10959-10961]. It then chooses “**Option D with `-g` convention (early/Northern spelling)**,” explicitly rejects adding a final-spirantization rule, and implements only the row changes `lēah → lēag` and `troh → trog` [Germanic/docs/DEV_NOTES.md:10990-11024]. For row 1960, the point is that `bōg` is not superseded: it is one of the forms that remain correct under the adopted project-wide spelling policy.

### Germanic/docs/DEV_NOTES.md:24436-24485

- Source heading: `§17.10.25 — Case 3 Option δ post-reorder: *-uz cluster regression`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `z_loss_order`; `cvcuz_regression`; `temporary_bad_output`; `implementation_history`
- Recommended next use: `preserve_as_diagnostic_history_only`

This later fragment is worth keeping only as implementation history. DEV_NOTES records a transient regression table with `*bōguz | bōgo | bōg` among eight new `*CVCuz` mismatches and then explains that moving `PGmcFinalZDeletion` too late let `OEMedUnstressedULowering` misread final `-uz` forms as though the `u` were still medial before a consonant [Germanic/docs/DEV_NOTES.md:24451-24485]. For row 1960, this does not challenge the live lexeme analysis; it simply explains one temporary way the FST could derail a normally regular derivation.

## Superseded or diagnostic material

- No standalone lexeme-specific DEV_NOTES narrative for `bough / bōg / *bōguz` was located. The absence should remain visible: current support is shared-policy and shared-rule material, not a bespoke `bōg` research memo embedded in DEV_NOTES [Germanic/docs/DEV_NOTES.md:1760-1766,10909-11024].
- The proposed final-spirantization fix `"{*g} -> h || EnglishStarVocalic _ .#."` is superseded for this row. DEV_NOTES records it only as a failed attempt because it produced the regression `*bōguz → bōh` [Germanic/docs/DEV_NOTES.md:10913-10917].
- The `*bōguz → bōgo` table in §17.10.25 is diagnostic only. Its importance is procedural: it shows that late `z`-deletion can create false `*CVCuz` lowering behavior, not that `bōg` itself is a disputed target [Germanic/docs/DEV_NOTES.md:24453-24485].
- `coverage_audit.md` and the live derivation trace are both supportive but non-DEV_NOTES materials. They matter here only to show the current repo state: no auxiliary packet/memo infrastructure exists, and the live cascade already returns `bōg` regularly [Germanic/docs/lexeme_reports/coverage_audit.md:206-206; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:429-448].

## Open questions for later work

- If row 1960 is ever considered for `index.tsv`, decide whether the explicit `bōg` mentions in the shared `ō before velars` and `g ~ h` policy sections are strong enough to count as index-worthy support, or whether the row should stay no-index because it still lacks a true lexeme-local dossier.
- If later DEV_NOTES work expands the final `g/h` normalization discussion, attach row 1960 more explicitly alongside `trog`, `lēag`, and `dāg`, so later extraction work does not have to infer `bōg`'s status from a regression example plus a shared policy choice [Germanic/docs/DEV_NOTES.md:10909-11024].
- If a later literature-facing memo is wanted, the likely task is not phonological repair but source-audit enrichment: gather direct lexicographic citations for OE `bōg` itself rather than relying mainly on shared DEV_NOTES policy text. The present DEV_NOTES support is enough for a conservative working note, but still comparatively thin.

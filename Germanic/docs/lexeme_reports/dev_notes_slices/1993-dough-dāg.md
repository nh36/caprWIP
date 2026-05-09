---
row_id: 1993
concept: dough
counterpart: dāg
proto: *dáigaz
protoform: *dáigaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1993 dough / dāg

## Current row state

- The live row reads `CONCEPT = dough`, `COUNTERPART = dāg`, `PROTO = *dáigaz`, `PROTOFORM = *dáigaz`, and `DERIVATION_CLASS = regular`; the row-local `NOTE` field is empty, while the `HISTORY` cell still contains duplicated inherited-etymology placeholders rather than a bespoke lexeme note [Germanic/data/germanic-aligned-final.tsv:242-242].
- `coverage_audit.md` still lists row 1993 as `regular | no | - | - | - | none`, so no packet, research memo, dossier, or analysis file is currently linked for this lexeme and the metadata links in this slice remain blank [Germanic/docs/lexeme_reports/coverage_audit.md:225-225].
- The required `oe_known_problems.tsv` check finds no entry for `*dáigaz`, `dāg`, or `dough`; row 1993 is therefore not being tracked as a live OE exception bucket there [Germanic/data/oe_known_problems.tsv:1-8].
- The published derivation trace already matches the live row with no workaround: `PROTO: *dáigaz`, `EXPECTED: dāg`, `OUTPUTS: dāg`, with the compact pathway `*dáigaz > *dāgaz > *dāga > dāg` via ai-monophthongization, final `-z` deletion, and final bare `-a` loss [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md:1067-1086].

## Development-note summary

DEV_NOTES support for row 1993 is real but mostly **shared-policy and diagnostic material rather than a dedicated lexeme dossier**. No long `dough / dāg` section was found. Instead, the lexeme surfaces inside the shared `Word-Final *g Spirantization Research (2026-03-15)` discussion and later inside a separate note on overbroad OE `g`-palatalisation [Germanic/docs/DEV_NOTES.md:10905-11030,43176-43185]. The slice therefore needs to preserve that support conservatively and state explicitly that row-local DEV_NOTES coverage is comparatively thin.

The first materially relevant DEV_NOTES passage is the failed attempt to add a blanket final-spirantization rule. DEV_NOTES records that the proposed rule `{*g} -> h || EnglishStarVocalic _ .#.` created regressions, including the row-local one: “`*daigăz` → `dāh` (expected `dāg`)” [Germanic/docs/DEV_NOTES.md:10913-10917]. For row 1993, this is important because it shows that `dāg` was not a target awaiting correction. It was one of the forms used to demonstrate that a universal OE final `g > h` rule would overgenerate.

The surrounding source discussion explains why that regression mattered. DEV_NOTES quotes Campbell that “for final `ɣ` there is an increasing use of the symbol `h` after Alfred's time,” then immediately summarizes that early texts mostly use `g`, Late West Saxon uses `h` increasingly, and northern material uses `h` only rarely [Germanic/docs/DEV_NOTES.md:10920-10937]. It then preserves the stronger normalization argument from Bülbring: “even in younger texts the spellings with `g` predominate ... in some (e.g. in the Vespasian Psalter and Rushworth) forms with `h` are completely absent” [Germanic/docs/DEV_NOTES.md:10998-11006]. That shared evidence directly bears on row 1993 because `dāg` is one of the dataset forms retained under the conservative `-g` convention.

DEV_NOTES states the policy conflict plainly: “`lēah`, `troh` use the Late WS `h` convention” while “`bōg`, `dāg` use the earlier/Northumbrian `g` convention” [Germanic/docs/DEV_NOTES.md:10959-10961]. The note considers four options, including changing `dāg → dāh` under a Late West Saxon normalization and a speculative vowel-quality-conditioned split, but it rejects new rule-making and adopts “**Option D with `-g` convention (early/Northern spelling)**” instead [Germanic/docs/DEV_NOTES.md:10963-11024]. For row 1993, that is the controlling current DEV_NOTES outcome: `PROTO` and `PROTOFORM` stay `*dáigaz`; `COUNTERPART = dāg` is retained as the chosen OE normalization under the repo-wide conservative spelling policy, not because the lexeme lacks `-h` comparanda in principle.

A later DEV_NOTES fragment matters as a guardrail against misclassification. In the note about over-application of OE `g`-palatalisation, the row is mentioned explicitly: “`*dáigaz → dāg` 'dough' — a long-vowel root; `*g` is in coda after a diphthong, behaviour governed by other rules” [Germanic/docs/DEV_NOTES.md:43176-43185]. That does not reopen the spelling-policy debate; instead it says that row 1993 should not be treated as evidence for the separate `nigon`-type palatalisation bug. This later note is therefore current diagnostic support that `dāg` belongs with the already-regular long-vowel/coda group, not with the front-vowel intervocalic-palatalisation problem.

## Relevant DEV_NOTES fragments

### Germanic/docs/DEV_NOTES.md:10905-10917

- Source heading: `Word-Final *g Spirantization Research (2026-03-15)` / `The Problem`
- Fragment type: `shared_problem_definition_with_row_specific_regression`
- Status: `diagnostic_but_still_useful`
- Issue tags: `g_vs_h`; `failed_rule`; `row_as_regression_control`; `not_proto_change`
- Recommended next use: `use_to_explain_why_no_final_h_rule_was_added`

This fragment preserves the exact row-local regression that blocked the proposed final-`g > h` rule. DEV_NOTES first lists the original mismatch set `*laugō → lēag (expected lēah)` and `*trugą → trog (expected troh)`, then records that the attempted repair also produced “`*daigăz` → `dāh` (expected `dāg`)” [Germanic/docs/DEV_NOTES.md:10909-10917]. For row 1993, the force of the passage is procedural but real: `dāg` is treated as a control showing that an across-the-board final spirantization rule would damage already acceptable outputs.

### Germanic/docs/DEV_NOTES.md:10920-11024

- Source heading: `Source Research`; `Analysis`; `Options`; `Decision: Use -g Spelling Convention (2026-03-15)`
- Fragment type: `current_row_policy_in_shared_section`
- Status: `current`
- Issue tags: `Campbell`; `Bulbring`; `g_h_alternation`; `target_normalization`; `no_new_rule`
- Recommended next use: `primary_index_anchor_if_shared_policy_counts`

This is the controlling current fragment for the live row. DEV_NOTES quotes Campbell on the increasing late use of final `h`, stresses that the alternation was “not categorical,” notes that the TSV mixed conventions, and then chooses `-g` as the repo's normalization standard [Germanic/docs/DEV_NOTES.md:10920-10937,10959-11024]. The most directly row-relevant lines are the explicit contrast “`bōg`, `dāg` use the earlier/Northumbrian `g` convention” and the later decision text adopting “**Option D with `-g` convention (early/Northern spelling)**” [Germanic/docs/DEV_NOTES.md:10959-10961,10990-11024]. The Bülbring quotation preserved here is also worth carrying forward because it gives the strongest source-backed rationale for retaining `dāg`: “even in younger texts the spellings with `g` predominate ... forms with `h` are completely absent” in some witnesses [Germanic/docs/DEV_NOTES.md:10998-11006].

### Germanic/docs/DEV_NOTES.md:43176-43185

- Source heading: `Empirical scope of the bug`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `palatalisation_scope`; `long_vowel_root`; `coda_g`; `guardrail`
- Recommended next use: `cite_as_current_diagnostic_constraint`

This later fragment is short but materially relevant because it names the row directly in a different rule-governance context. DEV_NOTES says: “`*dáigaz → dāg` 'dough' — a long-vowel root; `*g` is in coda after a diphthong, behaviour governed by other rules” [Germanic/docs/DEV_NOTES.md:43179-43180]. For row 1993, the passage functions as a current guardrail: even when front-vowel `g`-palatalisation was being tightened elsewhere, `dāg` was explicitly set aside as belonging to another already-regular pattern.

## Superseded or diagnostic material

- The superseded proposal for this row is the blanket final-spirantization rule `{*g} -> h || EnglishStarVocalic _ .#.`. DEV_NOTES preserves it only as a failed attempt because it would have turned `dāg` into `dāh` and thereby overgenerated against the live target [Germanic/docs/DEV_NOTES.md:10913-10917].
- Option A and Option C in the shared `g ~ h` note are useful only as labelled diagnostics now. Option A would have normalized the row to `dāh`, while Option C floated a vowel-quality-conditioned split `*ō/ai + g + u/ă → g (bōg, dāg)` but explicitly says the note had not found evidence for that conditioning [Germanic/docs/DEV_NOTES.md:10965-10982]. Neither proposal is current row policy.
- The later palatalisation note is current as a diagnostic constraint but not as a full lexeme audit. It says what row 1993 is **not** part of; it does not provide a standalone philological dossier for `dāg` [Germanic/docs/DEV_NOTES.md:43176-43185].
- DEV_NOTES support is therefore present but thin. The live row is well supported as current project policy, yet the support comes from shared-rule and shared-normalization notes rather than from a dedicated `dough / dāg` research section [Germanic/docs/DEV_NOTES.md:10905-11024,43176-43185].

## Open questions for later work

- If `dev_notes_slices/index.tsv` is revisited later, the strongest available anchor is the shared-policy block at [Germanic/docs/DEV_NOTES.md:10920-11024], but the row probably still belongs in the **shared-policy / thin-support** category rather than among rows with true lexeme-local dossiers.
- If a fuller lexeme report is ever wanted, the next useful task is not rule repair but source-audit enrichment: gather direct dictionary or grammar attestations for OE `dāg` itself, so the row does not rely almost entirely on shared `g ~ h` normalization discussion.
- If later DEV_NOTES work expands the final `g/h` normalization cluster, row 1993 should be named alongside `bōg`, `trog`, and `lēag` more explicitly, since current extraction has to infer much of `dāg`'s status from one regression example, one shared policy decision, and one later diagnostic guardrail [Germanic/docs/DEV_NOTES.md:10909-11024,43176-43185].

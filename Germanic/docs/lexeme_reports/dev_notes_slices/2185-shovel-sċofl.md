---
row_id: 2185
concept: shovel
counterpart: sċofl
proto: *skúflō
protoform: *skúflō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2185 shovel / sċofl

## Current row state

- CONCEPT: `shovel` [Germanic/data/germanic-aligned-final.tsv:989-989]
- COUNTERPART: `sċofl` [Germanic/data/germanic-aligned-final.tsv:989-989]
- PROTO: `*skúflō` [Germanic/data/germanic-aligned-final.tsv:989-989]
- PROTOFORM: `*skúflō` [Germanic/data/germanic-aligned-final.tsv:989-989]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:989-989]
- Live TSV row `2185` already records the key local editorial claim in its row note: `Proto corrected: Kroonen *skublō-/*skuflō with short u (not long ū). Palatal marker normalized.` The live row therefore treats the OE-facing input as a short-vowel form even though the TSV spelling is `*skúflō`; within this row's surviving project record, `*skúflō` is the stress-marked project notation used in the TSV/debug traces, while rejected `*skūflō` with macron is the older long-vowel policy explicitly targeted by the DEV_NOTES repair note [Germanic/data/germanic-aligned-final.tsv:989-989; Germanic/docs/DEV_NOTES.md:11037-11038,11071-11073; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4143-4155].
- The current published derivation trace already reaches the live target with no analogy flag or exception machinery: `Proto Input: *skúflō`, `NWGmc U Lowering: *skóflō`, `NWGmc Final Long O Raising: *skóflu`, `OE Sk Palatalization: *ʃóflu`, `OE High Vowel Apocope: *ʃófl`, orthographic `sċ*ófl`, outcome `sċofl` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4143-4162].
- The same row has no row-local problem entry in `oe_known_problems.tsv`, and coverage infrastructure still lists it as undocumented: `| 2185 | shovel | sċofl | regular | no | - | - | - | none |` [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:349-349].
- Source-facing OE attestation and project normalization must be kept apart. DEV_NOTES explicitly says `Normalize target: scofl → sċofl (palatal marker for consistency)`, while Campbell and Wright preserve unpointed `scofl` in lexical/glossarial material; those spellings support the lexeme but do not by themselves argue for dropping the project's normalized `sċ-` in the TSV [Germanic/docs/DEV_NOTES.md:11071-11075; docs/references/campbell_old_english_grammar.txt:11564-11564; docs/references/anglosaxonoldeng00wrig.txt:2357-2357].

## Development-note summary

Row `2185` does have a genuine row-specific DEV_NOTES block, but it has to be read in layers rather than lifted wholesale. The decisive row-level repair is the opening March note `## *skuflō 'Shovel' Reconstruction (2026-03-15)`. It starts from an older mismatch state, `*skūflō → sċūfl (expected scofl)`, and identifies two concrete problems: the older project proto used long `ū`, and the target spelling was inconsistently unpalatalized `sc` rather than the normalized `sċ` used elsewhere in the dataset [Germanic/docs/DEV_NOTES.md:11035-11040]. The part of that note that still governs the row is narrow and practical: Orel is quoted with `*skuflō sb.f.` and `OE scofl`, Kluge-Seebold is quoted with `Aus vd. *skūflō f. Daneben mit Vokalkürze ae. scofl, mndd. schuf(f)el, mndl. schuffel`, and Campbell is cited for direct OE `scofl` attestation [Germanic/docs/DEV_NOTES.md:11047-11061; docs/references/orel_handbook_germanic_etymology.vision.txt:38705-38708; docs/references/kluge_seebold_etymologisches_woerterbuch.txt:80188-80190; docs/references/campbell_old_english_grammar.txt:11564-11564]. Read conservatively, that is enough to support the project's present OE-directed claim: whatever wider West Germanic prehistory is chosen, the Old English row must be modeled with a short-vowel input that can lower to `o` before final non-high `*ō`, and its normalized target in the dataset is `sċofl` rather than raw-source `scofl` [Germanic/docs/DEV_NOTES.md:11070-11075].

The row's live notation now needs explicit disentangling. `PROTO` and `PROTOFORM` in the TSV are both written `*skúflō`, but that does not mean the row has reverted to the rejected long-vowel reconstruction `*skūflō`. For this row's local dossier, `*skúflō` in the TSV and trace is best treated as the project's stressed-vowel spelling for the same OE-facing short-vowel input that DEV_NOTES prose elsewhere writes as `*skuflō`; by contrast, `*skūflō` with macron is the specifically rejected long-vowel form from the old mismatch state [Germanic/data/germanic-aligned-final.tsv:989-989; Germanic/docs/DEV_NOTES.md:11037-11038,11071-11075; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4143-4155]. The same distinction applies on the output side: source quotations and glossaries mostly preserve `scofl`, but live row policy normalizes palatal `sċofl`. Those are notation or editorial-layer differences, not different OE targets [Germanic/docs/DEV_NOTES.md:11071-11075; docs/references/campbell_old_english_grammar.txt:11564-11564; docs/references/anglosaxonoldeng00wrig.txt:2357-2357].

Later DEV_NOTES work changes the implementation story more than the lexeme decision. The broad chronology audit around the `*núsō / *skúflō / *súrgō` cluster shows that row `2185` is now one of the controls fixing cascade order: if `NWGmcFinalLongORaising` were moved ahead of `NWGmcULowering`, the row would regress from `sċofl` back toward an unlowered `u` outcome [Germanic/docs/DEV_NOTES.md:24257-24308,24402-24410,24541-24545,39799-39804]. The current published trace mirrors exactly that audited order: lowering first (`*skóflō`), then final `ō > u` (`*skóflu`), then palatalization and apocope to `sċofl` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4151-4162]. So the row's present `regular` classification is not just a label in the TSV. It reflects the current project view that, once the OE-facing short-vowel input is chosen, the rest of the development is ordinary sound change rather than analogical repair [Germanic/data/germanic-aligned-final.tsv:989-989; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4143-4162].

What does **not** survive as stable row authority is the March note's broader historical theorizing. The middle of that note ventures beyond the safe OE-facing claim into explanations about Ingvaeonic versus Continental West Germanic, possible shortening versus possible lengthening, and Kroonen 2011's `*skóblō-` o-grade instrumental [Germanic/docs/DEV_NOTES.md:11077-11134]. The note then immediately corrects itself, saying the sources do **not** establish which variant is original, whether the change was Continental lengthening or Ingvaeonic shortening, or what the mechanism was [Germanic/docs/DEV_NOTES.md:11136-11167]. Repo-local reference files reinforce the need for caution: Orel clearly gives short-vowel `*skuflō`, Kluge-Seebold clearly contrasts continental `*skūflō` with short-vowel `ae. scofl`, but the local OCR of Kroonen's main dictionary entry currently reads `OHG scufla, scubla ... <*skūblō-`, not the short-vowel form reported in DEV_NOTES and in the TSV note [docs/references/orel_handbook_germanic_etymology.vision.txt:38705-38708; docs/references/kluge_seebold_etymologisches_woerterbuch.txt:80188-80190; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23035-23036]. That leaves the OE-facing row policy clear enough for a slice, but it makes the deeper comparative reconstruction too unstable to index without qualification.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-11035-11075

- Source heading: `## *skuflō 'Shovel' Reconstruction (2026-03-15)`
- Source line or section hint: `lines 11035-11075`
- Fragment type: `lexeme_specific`
- Status: `current_with_notational_cleanup`
- Issue tags: `proto_vs_protoform`; `vowel_quantity`; `palatal_marker`; `u_lowering`
- Recommended next use: `cite_in_final_report_with_caution`
- Shared with row IDs:

This is the main row-specific repair fragment. It preserves the exact old failure state, `*skūflō → sċūfl (expected scofl)`, and the exact repair package, namely: reject long-vowel `*skūflō`, normalize `scofl` to dataset `sċofl`, and let `NWGmcULowering` apply because the OE-facing input has short `u` before non-high `*ō` [Germanic/docs/DEV_NOTES.md:11037-11040,11070-11075]. The same fragment also preserves the dense source substance that later work still needs: Orel's `*skuflō sb.f.` with `OE scofl`, Kluge-Seebold's `Daneben mit Vokalkürze ae. scofl`, and Campbell's glossarial `scofl` [Germanic/docs/DEV_NOTES.md:11047-11061; docs/references/orel_handbook_germanic_etymology.vision.txt:38705-38708; docs/references/kluge_seebold_etymologisches_woerterbuch.txt:80188-80190; docs/references/campbell_old_english_grammar.txt:11564-11564]. For replacement-note purposes, this fragment is usable only if the notation layers are made explicit: live `*skúflō` is the row's stress-marked project spelling for the short-vowel input, not a return to the rejected macronized `*skūflō`.

### DEV_NOTES:line-11136-11167

- Source heading: `CORRECTION - What the sources actually say (2026-03-15)`
- Source line or section hint: `lines 11136-11167`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `source_limits`; `comparative_uncertainty`; `oe_facing_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This self-correction is the most important cautionary fragment in the whole dossier. DEV_NOTES retracts its own earlier overstatement and narrows the claim to what the sources actually support: continental material shows long-vowel `*skūflō`, Ingvaeonic reflexes show short-vowel `*skuflō`, the variation is real, but the sources do not tell us which side is original, whether lengthening or shortening happened, or what mechanism produced the split [Germanic/docs/DEV_NOTES.md:11136-11167]. The fragment ends with the policy statement that matters for the OE row: “For our FST: We use short *skuflō for OE because that's what the Ingvaeonic reflexes require” [Germanic/docs/DEV_NOTES.md:11165-11167]. That is stronger and cleaner than the surrounding speculation, and it is the best reason to treat the live row as OE-directed rather than as a full comparative verdict on all West Germanic.

### DEV_NOTES:line-24257-24308-and-24402-24410

- Source heading: `Regression cluster` / `Root-cause: U-lowering has been bled`
- Source line or section hint: `lines 24257-24308 and 24402-24410`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `chronology`; `u_lowering`; `final_ō_raising`; `shared_regression_cluster`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2143,2200`

This is the controlling current implementation fragment for row `2185`. DEV_NOTES first names `*skúflō → sċofl` as one of the three `root *u + final *-ō` rows that regressed together when the cascade order was wrong [Germanic/docs/DEV_NOTES.md:24257-24265]. It then explains why: if final long-`ō` raising applies first, the relevant non-high environment disappears and root `u` no longer lowers; the correct order is the opposite one, restoring `*skúflō → sċofl` along the same pattern as `*núsō → nosu` and `*súrgō → sorg` [Germanic/docs/DEV_NOTES.md:24275-24308,24402-24410]. The current published trace confirms that this is not stale prose but the live derivation now shipping in the repo [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4151-4162].

### DEV_NOTES:line-39799-39804

- Source heading: `Q4 finding — lautgesetz status (cell-switch, not wontfix)`
- Source line or section hint: `lines 39799-39804`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `regression_guard`; `chronology_lock`; `shared_control_row`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `2143,2200`

This later audit shows that row `2185` has become part of the project's regression guardrail set. DEV_NOTES says explicitly that reordering `NWGmcFinalLongORaising` ahead of `NWGmcULowering` would regress rows `2143`, `2200`, and `2185`, all of which attest the lowered-plus-apocopated outcome [Germanic/docs/DEV_NOTES.md:39799-39804]. For `2185`, this fragment is not primary philology, but it is valuable because it shows the row's current regular behavior is now constraining later rule work elsewhere.

### DEV_NOTES:line-11077-11134

- Source heading: `Further analysis: Why the vowel length difference?` / `Additional sources (2026-03-15)`
- Source line or section hint: `lines 11077-11134`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `misleading_if_uncontextualized`
- Issue tags: `overreach`; `comparative_theory`; `o_grade`; `diagnostic_only`
- Recommended next use: `use_only_to_explain_project_history`
- Shared with row IDs:

This material is useful only if it is fenced off as project history. It is where DEV_NOTES proposed that the base verb had e-grade and long zero-grade variants, that Ingvaeonic used a short-vowel line for the instrumental noun, and that Kroonen 2011's `*skóblō-` might align with the OE form [Germanic/docs/DEV_NOTES.md:11079-11134]. None of that is row-safe as a current conclusion on its own, because the very next correction block retracts the strongest historical claims and limits the secure result to descriptive coexistence of long-vowel continental and short-vowel Ingvaeonic evidence [Germanic/docs/DEV_NOTES.md:11136-11167]. This fragment should therefore survive only as an explanation of how the row's repair note briefly overinterpreted the comparative literature before narrowing back down.

## Superseded or diagnostic material

- The row's real superseded state is the older long-vowel analysis `*skūflō → sċūfl`, which DEV_NOTES itself marks as the mismatch being repaired [Germanic/docs/DEV_NOTES.md:11037-11040]. Any later writeup should treat that form as obsolete row history, not as a live alternative `PROTOFORM`.
- The broadest March historical explanation is also diagnostic rather than authoritative. DEV_NOTES first entertained scenarios such as Continental later lengthening, Ingvaeonic retention of an original short vowel, or separate ablaut-grade selection; the same note then explicitly says the available sources do **not** decide between those possibilities [Germanic/docs/DEV_NOTES.md:11097-11103,11131-11134,11136-11167].
- The Kroonen citation needs quarantine until someone checks the page image or a cleaner OCR. DEV_NOTES and the TSV note report Kroonen short-vowel `*skublō-`, but the repo-local OCR currently reads `OHG scufla, scubla ... <*skūblō-` [Germanic/data/germanic-aligned-final.tsv:989-989; Germanic/docs/DEV_NOTES.md:11043-11045,11141-11142; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23035-23036]. That inconsistency does not undo the OE-facing row policy, because Orel and Kluge-Seebold already support short-vowel OE `scofl`, but it does mean the Kroonen piece should not yet be indexed as a clean direct quotation.
- Luick's doublet material is useful background, not row authority. DEV_NOTES cites `*scufel ... neben scofel` as part of a broader `u/o` alternation discussion [Germanic/docs/DEV_NOTES.md:122-128], and the local Luick text indeed gives `*scufel ... neben scofel Schaufel` [docs/references/luick_historische_grammatik.txt:6119-6122]. That helps explain why project notes were alert to instability in this lexical family, but it does not by itself choose the live row's comparative reconstruction or its exact cascade ordering.

## Open questions for later work

- Check the page image or a better OCR for Kroonen p. 445 before turning any Kroonen-based sentence into indexed boilerplate. The row can presently be defended from Orel + Kluge-Seebold + OE attestation, but the Kroonen wording is not stable enough in repo-local form [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23035-23036; docs/references/orel_handbook_germanic_etymology.vision.txt:38705-38708; docs/references/kluge_seebold_etymologisches_woerterbuch.txt:80188-80190].
- Decide whether any future final report should split comparative and OE-facing notation explicitly in one sentence, e.g. “comparative literature shows mixed `*skūflō / *skublō / *skóblō` proposals, but the OE-directed project input is short-vowel `*skuflō` (TSV spelling `*skúflō`) because only that path yields `sċofl` under the live cascade” [Germanic/docs/DEV_NOTES.md:11070-11075,11136-11167; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4151-4162].
- If `dev_notes_slices/index.tsv` is ever reconsidered for this row, index only after separating the safe current anchors from the unstable comparative material: the safe anchors are the row-repair note's narrow resolution (`11035-11075`), the self-correction on source limits (`11136-11167`), and the shared chronology audit (`24257-24308`, `39799-39804`).

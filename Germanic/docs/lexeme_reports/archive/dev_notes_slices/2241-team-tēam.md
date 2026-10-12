---
row_id: 2241
concept: team
counterpart: tēam
proto: *táugmaz
protoform: *táugmaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2241 team / tēam

## Current row state

- The live OE row reads `2241\ttēam\tPROTO *táugmaz\tCOUNTERPART tēam\tDERIVATION_CLASS regular`, and the same row still has `PROTOFORM = *táugmaz` rather than a separate OE-facing substitute input [Germanic/data/germanic-aligned-final.tsv:1206-1206].
- `PROTO`, `PROTOFORM`, and `COUNTERPART` therefore need to stay sharply separated in later writeups: the comparative label is `*táugmaz`, the derivational input currently fed to the grammar is also `*táugmaz`, and the OE target selected by the row is `tēam` [Germanic/data/germanic-aligned-final.tsv:1206-1206].
- `oe_known_problems.tsv` currently has no entry for row `2241`, for `team`, for `tēam`, or for `*táugmaz`, so the row is not being tracked as a live unresolved OE exception [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation trace is an exact match and shows the live chain now in force: `PROTO: *táugmaz`, `Gm Simplification: *táumaz`, then `PGmc Final Z Deletion: *táuma`, `OE Au Fronting: *táeuma`, `OE Diphthong Leveling: *tēama`, `PWGmc Final Bare A Loss: *tēam`, with final `Outcome: tēam` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5088-5108].
- No reusable packet or research-memo stem turned up for this row, and the coverage audit still lists row `2241` with no linked packet, memo, or report (`| 2241 | team | tēam | regular | no | - | - | - | none |`) [Germanic/docs/lexeme_reports/coverage_audit.md:386-386].

## Detailed development-note summary

This row now has a genuinely row-specific DEV_NOTES dossier, but that dossier preserves two different project moments that must not be collapsed. The **current** row policy is the live TSV state and live derivation trace: `PROTO = PROTOFORM = *táugmaz`, `COUNTERPART = tēam`, and the grammar itself performs the `*gm > *m` simplification before the later `*au > ēa` and final-vowel steps [Germanic/data/germanic-aligned-final.tsv:1206-1206; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5088-5108]. The slice therefore needs to function as a replacement working note for the current earlier-stage, morphologically transparent input `*táugmaz`, not as a recap of the older mismatch state.

The philological starting point preserved in DEV_NOTES is still useful and should be carried forward explicitly. DEV_NOTES quotes Kroonen's headword `*tauma-` and preserves the crucial sentence: “The original form was `*taugma-`, which like `*drauma- < *draugma-` lost its `*g`” [Germanic/docs/DEV_NOTES.md:16031-16040; @Kroonen2013, p. 511]. The same note also preserves Orel's different practice: `"*tauxmaz sb.m.: ON taumr 'bridle, rein', OE teám 'tie, offspring, family, children' ..."`, i.e. a pre-loss form written with spirant `x` for `team`, while the same work gives `*draumaz` for `dream` [Germanic/docs/DEV_NOTES.md:16053-16067; @Orel2003, pp. 75, 403]. Those quotations matter because the row's present policy is deliberately neither a simple adoption of Kroonen's post-loss citation form `*tauma-` nor a retention of the older project spelling `*tauxmăz`. The project now keeps the earlier derivational stage but writes it with Verner-voiced `*g`.

The decisive current note is the later DEV_NOTES correction from the same day. That correction reverses the earlier tentative recommendation to normalize the TSV to post-loss `*taumăz` and instead states: “Implement as FST sound change rule (Option B with refinement)” [Germanic/docs/DEV_NOTES.md:16167-16223]. The note's core claim is that the relevant consonant is **voiced** `*g`, not voiceless `*x`, because Kroonen marks both `*tauma-` and `*drauma-` as **(DRV)**, i.e. Verner-derived [Germanic/docs/DEV_NOTES.md:16175-16185; @Kroonen2013, pp. 101, 511]. DEV_NOTES then spells out the intended chain as `PIE *deuk-mó- > *teux-mo- > *teug-mo- > *taugma- > *tauma-`, and the live derivation trace now embodies that choice in operational form via `Gm Simplification: *táumaz` before the regular OE vocalic history [Germanic/docs/DEV_NOTES.md:16180-16215; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5095-5108].

That distinction is the main thing later report work must preserve. `PROTO *táugmaz` is the row's present comparative/project reconstruction; `PROTOFORM *táugmaz` is the identical OE-facing input because no workaround form is currently needed; and `COUNTERPART tēam` is the regular OE outcome after `*gm > *m`, final-`z` loss, `*au > ēa`, and final bare-`a` loss [Germanic/data/germanic-aligned-final.tsv:1206-1206; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5088-5108]. The important superseded alternatives are also clear and should stay named as superseded alternatives: the stale mismatch input `*tauxmăz`, and the briefly recommended but rejected normalization to post-loss `*taumăz` [Germanic/docs/DEV_NOTES.md:16005-16018,16095-16166].

Because this row has a dedicated lexeme-addressed DEV_NOTES entry with direct source quotations and a final project decision, the support here is stronger than the thin shared-support slices. The slice can therefore stand as a replacement working note and is a plausible indexing candidate, provided any later index entry distinguishes the **current** Verner-voiced/FST-handled resolution from the earlier `*tauxmăz` mismatch and the superseded `*taumăz` recommendation.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-16029-16067

- Source heading: `Source Research: Reconstruction Forms`
- Source line or section hint: `lines 16029-16067`
- Fragment type: `copied_row_specific_fragment`
- Status: `current`
- Issue tags: `source_reconstructions`; `kroonen`; `orel`; `gm_loss`; `verners_law_context`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment preserves the source-facing reconstruction dispute that still matters for row `2241`. Kroonen's wording should be carried forward nearly verbatim because it is the cleanest statement of the relation between citation form and earlier derivational stage: `"A mo-stem created to the root of *teuhan- (q.v.). The original form was *taugma-, which like *drauma- < *draugma- lost its *g."` [Germanic/docs/DEV_NOTES.md:16031-16040; @Kroonen2013, p. 511]. The same passage also records the daughter set including `OE téam`, so it directly addresses the row rather than merely shared sound-change background.

The Orel quotation in the same fragment is worth preserving because it explains the stale project detour. DEV_NOTES records `"*tauxmaz sb.m.: ON taumr 'bridle, rein', OE teám 'tie, offspring, family, children' ..."` for `team`, but `*draumaz` for `dream`, and explicitly notes the inconsistency within Orel's own treatment [Germanic/docs/DEV_NOTES.md:16053-16067; @Orel2003, pp. 75, 403]. For row `2241`, this fragment is current not because Orel's literal reconstruction was adopted, but because it documents why the project had to choose among three distinct possibilities: post-loss `*tauma-`, pre-loss voiceless `*tauxmăz`, and pre-loss Verner-voiced `*táugmaz`.

### DEV_NOTES:line-16167-16223

- Source heading: `Fix Applied (2026-04-09)`
- Source line or section hint: `lines 16167-16223`
- Fragment type: `copied_row_specific_fragment`
- Status: `current`
- Issue tags: `fst_decision`; `gm_simplification`; `verners_law`; `current_row_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: 1995

This is the fragment that states the live project decision for `tēam`. DEV_NOTES explicitly says the change should be handled “by the transducer rather than by ad hoc TSV adjustments,” and then identifies the consonant as `*g` rather than `*x` because the derivation is Verner-voiced [Germanic/docs/DEV_NOTES.md:16169-16185]. The note's derivational chain `*deuk-mó- > *teux-mo- > *teug-mo- > *taugma- > *tauma-` is exactly the justification for the live row's present `PROTO = PROTOFORM = *táugmaz` instead of either `*tauxmăz` or `*taumăz` [Germanic/docs/DEV_NOTES.md:16180-16185; @Kroonen2013, pp. 101, 511].

The same fragment also records the project-level implementation result: row `2241` was updated from `*tauxmăz` to `*taugmăz`, and the grammar gained the rule that deletes `*g` before `*m`, after which `*taugmăz` yields `tēam` successfully [Germanic/docs/DEV_NOTES.md:16187-16223]. The live published trace now shows the same policy in stable operational form, albeit with the acute-accent project spelling `*táugmaz` and a visible `Gm Simplification` stage [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5088-5108].

## Superseded or diagnostic material

### DEV_NOTES:line-16001-16018

- Source heading: `OE tēam 'team, offspring': *gm Cluster Analysis (opening mismatch)`
- Source line or section hint: `lines 16001-16018`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `stale_mismatch`; `old_protoform`; `teahm_output`; `project_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This opening fragment is useful only for explaining why the dossier exists. It records the now-superseded mismatch `*tauxmăz -> tēahm (expected tēam)` and frames the original question as whether to change the TSV to a post-loss form or add a rule for `*gm -> *m` [Germanic/docs/DEV_NOTES.md:16005-16018]. That mismatch no longer reflects the live row state, because the row now uses `*táugmaz` and derives `tēam` exactly [Germanic/data/germanic-aligned-final.tsv:1206-1206; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5088-5108].

### DEV_NOTES:line-16093-16166

- Source heading: `Analysis: Which Approach is Better?` / `Recommendation`
- Source line or section hint: `lines 16093-16166`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `option_a`; `tauma_normalization`; `stale_row_state`; `project_reversal`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: 1995

This fragment should be kept because it preserves a real project detour, but it is no longer current policy. DEV_NOTES first argued for `Option A`, i.e. normalize the TSV to post-loss `*taumăz`, largely on the grounds of consistency with earlier `drēam` handling and Kroonen's headword practice, and it even called the row's older `*tauxmăz` state a probable data-entry error [Germanic/docs/DEV_NOTES.md:16095-16166; @Kroonen2013, pp. 101, 511]. That recommendation is superseded by the immediately following fix note, which instead adopted FST-handled `*gm > *m` plus Verner-voiced `*g` and updated the row to `*taugmăz`/`*táugmaz` [Germanic/docs/DEV_NOTES.md:16167-16223].

For later writers, the important point is not merely that Option A was rejected, but why it was rejected: the project decided that keeping the earlier derivational stage in `PROTO/PROTOFORM` made the morphology and Verner history more explicit, while the grammar could handle the simplification transparently. This fragment is therefore valuable project chronology, not present row authority.

## Open questions for later work

- If a later packet or report is written, keep the row's three layers explicit in the opening lines: comparative/project `PROTO *táugmaz`, identical OE-facing `PROTOFORM *táugmaz`, and regular OE `COUNTERPART tēam` from the live exact-match derivation [Germanic/data/germanic-aligned-final.tsv:1206-1206; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5088-5108].
- If later prose cites Kroonen's dictionary headword `*tauma-`, it should state explicitly that this is Kroonen's post-loss citation form, whereas the current project row intentionally keeps the earlier Verner-voiced derivational stage `*táugmaz` and lets the grammar perform `*gm > *m` [Germanic/docs/DEV_NOTES.md:16031-16040,16167-16223; @Kroonen2013, p. 511].
- If `dev_notes_slices/index.tsv` is updated later, the strongest candidate additions are the current source-reconstruction fragment `DEV_NOTES:line-16029-16067` and the current decision fragment `DEV_NOTES:line-16167-16223`; the opening mismatch `DEV_NOTES:line-16001-16018` and the Option A recommendation `DEV_NOTES:line-16093-16166` should be indexed, if at all, only as diagnostic/project-history material.

---
row_id: 2163
concept: rye
counterpart: ryġe
proto: *rúgiz
protoform: *rúgiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2163 rye / ryġe

## Current row state

- CONCEPT: `rye` [Germanic/data/germanic-aligned-final.tsv:903-903]
- COUNTERPART: `ryġe` [Germanic/data/germanic-aligned-final.tsv:903-903]
- PROTO: `*rúgiz` [Germanic/data/germanic-aligned-final.tsv:903-903]
- PROTOFORM: `*rúgiz` [Germanic/data/germanic-aligned-final.tsv:903-903]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:903-903]
- Live row sourcing is minimal rather than row-analytical: the row carries duplicated `Wiktionary etymology (template:inh)` source strings, and `Germanic/data/old_english_wiktionary.tsv` likewise maps English `rye` to OE `ryġe` [Germanic/data/germanic-aligned-final.tsv:903-903; Germanic/data/old_english_wiktionary.tsv:224-224].
- `oe_known_problems.tsv` currently has no entry for `2163`, `*rúgiz`, `rye`, or `ryġe`, so the row is not being managed as a live exception bucket there [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

No securely attachable **current** row-specific closure note for row 2163 survives in `Germanic/docs/DEV_NOTES.md`. The usable DEV_NOTES material is older diagnostic material from the December 2025 / January 2026 OE umlaut investigations, where the lexeme appears explicitly as one of the very small number of "clean" i-mutation failures: `*rugiz` was expected to yield `ryġe`, but the stack was outputting `rūġ` instead [Germanic/docs/DEV_NOTES.md:2581-2586,2588-2593,2595-2604]. That older spelling without the accent mark (`*rugiz`) is the same row-level proto lexeme as the live TSV's `*rúgiz`; the important row-level distinction is not between two protoforms, but between the inherited input `*rúgiz/*rugiz` and the OE target `ryġe` [Germanic/data/germanic-aligned-final.tsv:903-903; Germanic/docs/DEV_NOTES.md:2583,2591,2604].

Those DEV_NOTES fragments establish three concrete things. First, they preserve the exact earlier mismatch, so later review does not have to guess what was once broken: the row's failure mode was not some vague "rye problem," but specifically `*rugiz → rūġ` where OE `ryġe` was expected [Germanic/docs/DEV_NOTES.md:2583,2591,2604]. Second, the notes narrow the diagnosis. The December 2025 "palatalization vs fronting/umlaut" section says these cases were **not** true palatalization-rule failures; for this row the front-vowel context required to support the expected umlauted outcome was missing upstream, so the bug belonged with fronting/umlaut rather than consonant handling [Germanic/docs/DEV_NOTES.md:2588-2593]. Third, the January 2026 subgrouping confirms that rye stayed in the tiny `iumlaut_trigger_only` set even after other cleanup, alongside only two other examples, so the project at that stage still regarded this row as a high-value diagnostic for genuine i-mutation behavior rather than as a noisy mixed-case mismatch [Germanic/docs/DEV_NOTES.md:2595-2604].

What DEV_NOTES does **not** preserve is just as important for replacement-note purposes. There is no later rye-specific entry saying exactly which change repaired `*rugiz → rūġ`, no dedicated row-2163 status update, and no later note moving the lexeme into `oe_known_problems.tsv` or classing it as an enduring exception. The live TSV has since been normalized to `regular`, and the known-problems file is silent [Germanic/data/germanic-aligned-final.tsv:903-903; Germanic/data/oe_known_problems.tsv:1-8]. So the conservative current reading is: row 2163 is now treated as a regular match whose older row-local DEV_NOTES material survives only as debugging history. The slice should therefore preserve the earlier mismatch wording in detail, but it should **not** re-promote that historical bug report into current row policy.

## Relevant DEV_NOTES fragments

### DEV_NOTES:no-later-rye-closure-note

- Source heading: no later dedicated `rye / ryġe / *rugiz` closure note survives in `DEV_NOTES.md`
- Source line or section hint: exact row-local hits are limited to `2581-2604`
- Fragment type: `unclear_needs_human_review`
- Status: `uncertain`
- Issue tags: `missing_current_authority`; `negative_result`; `row_history_only`; `no_closure_note`
- Recommended next use: `check_against_literature`
- Shared with row IDs:

This negative result is the main current fact to preserve. `DEV_NOTES.md` does name the lexeme in the early umlaut diagnostics, but a direct review does **not** turn up a later rye-specific repair note, no project-status closure for row `2163`, and no discussion recasting `ryġe` as a documented exception. Because the live TSV now marks the row `regular`, later report work must keep the chronology explicit: the row had an earlier recorded mismatch, but the surviving DEV_NOTES dossier is incomplete on the exact moment and mechanism of its repair [Germanic/data/germanic-aligned-final.tsv:903-903; Germanic/docs/DEV_NOTES.md:2581-2604].

### DEV_NOTES:line-2581-2586

- Source heading: `OE i‑umlaut deep dive (2025-12-23)`
- Source line or section hint: `lines 2581-2586`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `exact_old_mismatch`; `i_umlaut`; `u_umlaut_miss`; `row_specific_debug_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs: `2308`

This is the earliest exact-hit fragment and the clearest statement of the old row failure. DEV_NOTES says there were only three suspected true i-umlaut failures in the targeted scan, and it names rye directly: ``*rugiz`` → expected **`ryġe`**, output **`rūġ`** [Germanic/docs/DEV_NOTES.md:2582-2583]. That wording preserves the concrete mismatch shape: missing mutated `y` in the root and a shortened/incorrect final shape instead of `-e`. The note's label `u-umlaut miss` is best preserved as historical bucket terminology, not as a complete final explanation, because later adjacent DEV_NOTES fragments refine the diagnosis into an upstream fronting/umlaut-context problem rather than a settled standalone rule name [Germanic/docs/DEV_NOTES.md:2583,2588-2593].

### DEV_NOTES:line-2588-2593

- Source heading: `OE palatalization vs fronting/umlaut split (2025-12-23)`
- Source line or section hint: `lines 2588-2593`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `front_vowel_context`; `not_palatalization`; `true_i_umlaut_miss`; `shared_bucket_analysis`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `1942`

This shared diagnostic note matters because it explains what the earlier mismatch was **not**. DEV_NOTES says the apparent palatalization failures in the bucket were upstream vowel-context failures: "palatalization never triggers because the **front-vowel context is missing**," and then adds that there was only one strict true i-umlaut miss, namely ``*rugiz → ryġe`` expected, output `rūġ` [Germanic/docs/DEV_NOTES.md:2590-2591]. For row 2163, that is the key interpretive limit on the old bug report. The note does not say that consonant handling for `ġ` was broken; it says the derivation failed before the expected fronted/umlauted vowel environment was established, so rye belonged to the genuine i-mutation problem set rather than to a separate palatalization defect [Germanic/docs/DEV_NOTES.md:2590-2593].

### DEV_NOTES:line-2595-2604

- Source heading: `OE i‑umlaut/fronting bucket diagnostics (2026-01-01)`
- Source line or section hint: `lines 2595-2604`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `iumlaut_trigger_only`; `subgroup_trace`; `old_priority_case`; `regression_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `1942,2151,2308`

This fragment shows that rye remained a tracked high-confidence i-mutation problem even after the next round of cleanup. DEV_NOTES groups the broader bucket and says only three items fell into `iumlaut_trigger_only`, then gives staged-trace examples including ``*rugiz → rūġ (expected ryġe)`` [Germanic/docs/DEV_NOTES.md:2600-2604]. For row 2163, the value is chronological and diagnostic: the project was still using rye as one of the clearest controls for genuine umlaut-trigger behavior on 2026-01-01. What the fragment does **not** supply is a later success state; it ends at the diagnostic stage rather than recording the eventual change that made the live row regular [Germanic/docs/DEV_NOTES.md:2597-2604; Germanic/data/germanic-aligned-final.tsv:903-903].

## Superseded or diagnostic material

- All directly attachable DEV_NOTES material for this row is early debugging history. None of the surviving rye-specific notes says that `ryġe` is still an exception, and none should be cited as though it overrides the live TSV's current `regular` status [Germanic/docs/DEV_NOTES.md:2581-2604; Germanic/data/germanic-aligned-final.tsv:903-903].
- The older DEV_NOTES spelling `*rugiz` should not be misread as a competing protoform. In current row metadata, `PROTO` and `PROTOFORM` are both `*rúgiz`; the accent difference is not the meaningful distinction for this slice [Germanic/data/germanic-aligned-final.tsv:903-903; Germanic/docs/DEV_NOTES.md:2583,2591,2604].
- The row currently has no `oe_known_problems.tsv` entry, so later writeups should avoid turning these old diagnostic fragments into an implied live exception classification [Germanic/data/oe_known_problems.tsv:1-8].

## Open questions for later work

- If a later final report needs a positive derivation narrative, identify which later OE umlaut/fronting repair actually turned the older `*rugiz → rūġ` mismatch into the current regular row; the surviving rye-specific DEV_NOTES fragments do not name that repair.
- If index integration is attempted, keep it conservative and explicit that the attachable DEV_NOTES material is diagnostic history, not a current row-policy note.
- If later review wants stronger authority than the live Wiktionary-based row sourcing, gather it from literature or a dedicated memo rather than from these December 2025 / January 2026 bug-bucket notes alone.

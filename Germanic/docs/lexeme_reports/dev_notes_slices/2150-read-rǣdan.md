---
row_id: 2150
concept: read
counterpart: rǣdan
proto: *rḗdaną
protoform: *rḗdaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2150 read / rǣdan

## Current row state

- CONCEPT: `read` [Germanic/data/germanic-aligned-final.tsv:855].
- COUNTERPART: `rǣdan` [Germanic/data/germanic-aligned-final.tsv:855].
- PROTO: `*rḗdaną` [Germanic/data/germanic-aligned-final.tsv:855].
- PROTOFORM: `*rḗdaną` [Germanic/data/germanic-aligned-final.tsv:855].
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:855].
- `oe_known_problems.tsv` currently has no row-local entry for `2150`, `*rḗdaną`, or `rǣdan`, so the project is not tracking this lexeme as a live exception bucket item [Germanic/data/oe_known_problems.tsv:1-8].
- The current derivation trace is fully regular and already matches the row target: `PROTO: *rḗdaną`, `EXPECTED: rǣdan`, `OUTPUTS: rǣdan`. The published trace spells the path out as Proto Input `*rḗdaną`, then `NWGmc Long E Lowering: *rǣdaną`, then OE `Heavy Syllable Nasal Apocope: *rǣdan`, `Secondary Nasalization: *rǣdąn`, and `Weak Tail Reduction: *rǣdan`, with final `Outcome: rǣdan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3610-3629].

## Development-note summary

No surviving row-2150 DEV_NOTES subsection functions as a dedicated lexeme dossier. The securely attachable DEV_NOTES material for this row is instead the shared April 2026 stress-tier refactor in §17.49, where `*rḗdaną → rǣdan` is used as one of the explicit verification samples after the project retrofits stressed long `*ḗ` throughout the cascade [Germanic/docs/DEV_NOTES.md:42679-42750]. That matters because the current row spelling is not just decorative orthography: `PROTO = *rḗdaną` and `PROTOFORM = *rḗdaną` now encode that the inherited long `ē` belongs to the stressed root syllable, not to the unstressed long-`*ē` class targeted by later shortening machinery [Germanic/docs/DEV_NOTES.md:42683-42692, 42722-42725, 42741-42749].

For this lexeme, the practical consequence is straightforward but worth stating explicitly. §17.49 says 16 lemmas were promoted in the TSV from plain `*ē` to stressed `*ḗ`, and then reports that probe outputs were invariant across the whole refactor, giving `*rḗdaną → rǣdan` as one of the named samples [Germanic/docs/DEV_NOTES.md:42727-42739]. The row should therefore be read as a control witness for the stress-tier distinction: the root vowel is stressed `*ḗ` at input, it lowers by the ordinary NWGmc long-`ē` rule to `*ǣ`, and the OE target remains regular `rǣdan`, not a lexeme requiring paradigm-cell rescue, exception labelling, or target-side correction [Germanic/docs/DEV_NOTES.md:42713-42719, 42735-42739; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3610-3629].

The row-level distinction among PROTO, PROTOFORM, and OE target still needs to stay explicit even though PROTO and PROTOFORM currently coincide. `PROTO = *rḗdaną` is the comparative/project lexeme label now carried in the live TSV; `PROTOFORM = *rḗdaną` is the actual stress-marked input the current grammar consumes; and the OE target is normalized infinitive `rǣdan`, reached only after NWGmc lowering and later OE weak-tail handling [Germanic/data/germanic-aligned-final.tsv:855; Germanic/docs/DEV_NOTES.md:42713-42719, 42741-42749; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3610-3629]. This distinction is especially important here because §17.49 expressly says the whole point of the new symbol is to keep stressed root `*ḗ` separate from unstressed suffixal `*ē` for `OEUnstressedLongVowelShortening2` [Germanic/docs/DEV_NOTES.md:42741-42749].

In other words, this slice is mostly an infrastructure note, but it is still a real replacement working note for row 2150. What DEV_NOTES currently establishes for `read / rǣdan` is not a bespoke philological controversy; it is the opposite. The row is a named sample proving that the stressed-long-`ē` refactor did not disturb a regular inherited pathway, and the live trace confirms the expected ordinary development `*rḗdaną > *rǣdaną > rǣdan` under the current grammar [Germanic/docs/DEV_NOTES.md:42727-42739; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3610-3629].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-42679-42692

- Source heading: `§17.49 Stressed long-ē tier (*ḗ) — extending the §17.46 stress-tier convention`
- Source line or section hint: `lines 42679-42692`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `protoform_notation`; `stress_tier`; `root_syllable`; `shared_row_support`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1987`, `2004`, `2093`, `2129`, `2131`, `2150`

This is the main current DEV_NOTES anchor for row 2150. The section explains why the project introduced stressed long `*ḗ` at all: after earlier work had already introduced stressed long diphthongs, the cascade was inconsistent because the stressed long monophthong `*ḗ` was still unrepresented even though the TSV contained about 16 lexemes with stressed root-syllable long `ē`, explicitly including `*rēdaną` in the motivating list [Germanic/docs/DEV_NOTES.md:42683-42692]. For row 2150, that establishes that the live `*rḗdaną` spelling is deliberate current policy rather than incidental diacritics.

### DEV_NOTES:line-42713-42719

- Source heading: `§17.49 rule-by-rule parallel plumbing`
- Source line or section hint: `lines 42713-42719`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `NWGmc_long_e_lowering`; `stress_drop_on_output`; `regular_pathway`; `shared_phonology`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `1987`, `2004`, `2093`, `2129`, `2131`, `2150`

This fragment gives the specific rule-side fact that makes `rǣdan` unsurprising under the new notation. DEV_NOTES says `NWGmcLongELowering` was extended by adding `{*ḗ} -> {*ǣ}` and notes that stress is dropped on the output side because this branch does not yet carry a separate stressed `*ǣ́` tier [Germanic/docs/DEV_NOTES.md:42713-42719]. For row 2150, this is the exact shared phonological statement behind the trace step `NWGmc Long E Lowering: *rǣdaną` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3621-3623].

### DEV_NOTES:line-42727-42739

- Source heading: `§17.49 TSV root-syllable promotion and verification`
- Source line or section hint: `lines 42727-42739`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `tsv_promotion`; `verification_sample`; `current_output`; `row_control_case`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1987`, `2004`, `2093`, `2129`, `2131`, `2150`

This is the most concrete row-shaped DEV_NOTES fragment. DEV_NOTES states that Phase 5 promoted 16 lemmas from `*ē` to `*ḗ` in the TSV and then reports: `Probe outputs invariant across the refactor (sample: *dḗdiz → dǣd*, *lḗtaną → lǣtan*, *rḗdaną → rǣdan* ...)` [Germanic/docs/DEV_NOTES.md:42727-42739]. For row 2150 that sentence does real work: it shows both that the older plain-`*ē` row state is superseded and that the current grammar was explicitly regression-tested on this exact lexeme after the promotion.

### DEV_NOTES:line-42741-42749

- Source heading: `§17.49 stress-on-output convention`
- Source line or section hint: `lines 42741-42749`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `stressed_vs_unstressed_long_e`; `OEUnstressedLongVowelShortening2`; `proto_vs_target`; `notation_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1987`, `2004`, `2093`, `2129`, `2131`, `2150`

This fragment explains why the notation difference matters for later interpretation of the row. DEV_NOTES states that stress is only preserved where the receiving long-vowel tier exists and that, in the current branch, stress information is used specifically to distinguish unstressed `*ē` from stressed `*ḗ` so that `OEUnstressedLongVowelShortening2` can apply to suffix `*ē` but not to root `*ḗ` [Germanic/docs/DEV_NOTES.md:42741-42749]. For `*rḗdaną`, that means the row should be read as a stress-marked root-vowel control case, not collapsed back into the unstressed-`*ē` bucket.

## Superseded or diagnostic material

- The superseded background relevant to row 2150 is the pre-§17.49 plain-`*ē` notation that the refactor explicitly replaced. DEV_NOTES says 16 lemmas were promoted from `*ē` to `*ḗ` in `PROTOFORM` and `PROTO`, and then cites `*rḗdaną → rǣdan` as a verification sample [Germanic/docs/DEV_NOTES.md:42727-42739]. For later work, the important limit is that older plain-`*rēdaną` spellings are now only diagnostic project history, not current row authority.
- The live project state gives no evidence that row 2150 is an unresolved exception. It is absent from `oe_known_problems.tsv`, and the published derivation trace already returns the expected target `rǣdan` [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3610-3629]. Any later write-up should therefore avoid treating this slice as if it documented a mismatch dossier.
- The surviving DEV_NOTES material is shared infrastructure/support material, not a long row-local philological essay. That is not a defect in the slice; it is the securely current state of the evidence. The row is presently important because it is a named regression-proof sample inside the `*ḗ` refactor, not because DEV_NOTES preserves a bespoke controversy around `rǣdan` [Germanic/docs/DEV_NOTES.md:42679-42750].

## Open questions for later work

- If a packet or research memo is created later, copy in the current row-local trace `*rḗdaną > *rǣdaną > rǣdan` explicitly so future review does not have to reconstruct the regular pathway from the shared §17.49 infrastructure note plus the debug snapshot [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3610-3629; Germanic/docs/DEV_NOTES.md:42713-42719].
- If future stress-tier work adds output-side stressed vowels such as `*ǣ́`, revisit whether this row should preserve stress marking beyond NWGmc lowering. §17.49 currently says the branch drops stress when `*ḗ` lowers to `*ǣ` because no downstream rule consumes stress on `*ǣ` yet [Germanic/docs/DEV_NOTES.md:42741-42749].
- If `dev_notes_slices/index.tsv` is updated later, index this slice as a **current shared-support/control-case note** for the stressed-long-`ē` refactor, not as a row-specific mismatch or exception dossier [Germanic/docs/DEV_NOTES.md:42727-42739].

---
row_id: 2225
concept: stream
counterpart: strēam
proto: *stráumaz
protoform: *stráumaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2225 stream / strēam

## Current row state

- The live OE row reads `2225	strēam	PROTO *stráumaz	COUNTERPART strēam	DERIVATION_CLASS regular`, with `PROTO = PROTOFORM = *stráumaz` and no row-local explanatory note beyond duplicated Wiktionary inheritance sourcing [Germanic/data/germanic-aligned-final.tsv:1145-1145].
- `PROTO` and `PROTOFORM` are therefore not split for this row. The comparative proto label and the OE-facing derivational input are both `*stráumaz`, and the OE target remains `COUNTERPART = strēam` rather than some oblique or analogically repaired substitute [Germanic/data/germanic-aligned-final.tsv:1145-1145].
- `old_english_wiktionary.tsv` independently maps English `stream` to OE `strēam`, so the lexical-source layer agrees with the live row state [Germanic/data/old_english_wiktionary.tsv:285-285].
- `oe_known_problems.tsv` currently has no entry for row `2225`, for `stream`, for `strēam`, or for `*stráumaz`, so the row is not being managed as a live OE exception or unresolved mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- The current published OE derivation trace is an exact match: `PROTO: *stráumaz`, `EXPECTED: strēam`, `OUTPUTS: strēam`, with the staged path `PGmc Final Z Deletion: *stráuma`, `OE Au Fronting: *stráeuma`, `OE Diphthong Leveling: *strēama`, `PWGmc Final Bare A Loss: *strēam` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4827-4845].
- No reusable packet or research-memo stem was found for this row during this pass, and `coverage_audit.md` still shows row `2225` with no linked packet, memo, or report (`| 2225 | stream | strēam | regular | no | - | - | - | none |`) [Germanic/docs/lexeme_reports/coverage_audit.md:377-377].

## Detailed development-note summary

No dedicated `stream / strēam / *stráumaz` memorandum currently survives in `DEV_NOTES.md`. The row therefore has to be documented from shared current sound-change notes plus the live exact-match derivation trace, not from a lexeme-specific DEV_NOTES dossier. That is still enough for a replacement working note, because the live grammar already derives the target cleanly as `*stráumaz > *stráuma > *stráeuma > *strēama > strēam`, and the surviving shared DEV_NOTES material explains both the `*-az > -a > Ø` chronology and the `*au > ēa` vocalic development [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4827-4845; Germanic/docs/DEV_NOTES.md:21436-21446,26754-26770,35059-35070; @RingeTaylor2014, pp. 59-61; @RingeTaylor2014, §6.6.3].

The most important positive point is that the row's long `ēa` is not a row-local repair. DEV_NOTES says explicitly that the existing `OEAuFronting (*au → *aeu)` plus `OEDiphthongLeveling (*aeu → *ēa)` rules “handle `*au → *ēa` generally” and that, for project purposes, “`*au` always becomes `*ēa` in the FST” [Germanic/docs/DEV_NOTES.md:26765-26769]. A separate DEV_NOTES quotation from Ringe & Taylor adds that “most examples of the long diphthong reflected PWGmc `*au`” [Germanic/docs/DEV_NOTES.md:35061-35062; @RingeTaylor2014, §6.6.3]. Read against the live trace, those statements support the concrete row-level conclusion that OE `strēam` is the regular long-`ēa` outcome of `*stráumaz`, not evidence that `PROTOFORM` should diverge from `PROTO` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4835-4845].

The final-vowel side of the derivation is likewise regular and should stay explicit in any later report. DEV_NOTES quotes Ringe & Taylor: “Another sweeping sound change that characterizes all WGmc languages is the loss of unstressed `*a` and `*ą` word-finally and before final `*-z`,” then restates the chronology as `(1)` loss of `*-z` after unstressed vowels and `(2)` loss of word-final `*-a` and `*-ą`, both already PWGmc [Germanic/docs/DEV_NOTES.md:21436-21443; @RingeTaylor2014, pp. 59-61]. That shared chronology maps directly onto the row trace's `*stráumaz > *stráuma ... > *strēam` sequence [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4839-4845]. For row policy, the important distinction remains simple but must still be stated outright: `PROTO = *stráumaz`, `PROTOFORM = *stráumaz`, `COUNTERPART = strēam`, and the row succeeds without any special exception handling.

The main caution is evidentiary rather than philological. Because the surviving DEV_NOTES support is shared and not lexeme-addressed, later writers should not overstate the note base. This row is well supported as a regular outcome, but its support comes from shared rule-history prose and the live exact-match trace rather than from a dedicated stream-specific investigation. That makes the slice useful as a replacement working note, but still a no-index-leaning one unless a later packet, memo, or philological note adds genuinely row-local material.

## Relevant DEV_NOTES fragments

No securely attachable current row-specific DEV_NOTES fragment survives for `2225`. The fragments below are the shared current notes that materially support the live row.

### DEV_NOTES:line-21436-21446

- Source heading: `Historical reality (R/T vol.2 §3.1.2, pp.59-61)`
- Source line or section hint: `lines 21436-21446`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `final_z_loss`; `final_a_loss`; `relative_chronology`; `shared_row_support`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the clearest current DEV_NOTES support for the non-lexical ending of the row. DEV_NOTES quotes Ringe & Taylor that “the loss of unstressed `*a` and `*ą` word-finally and before final `*-z`” was a WGmc-wide change and then restates the chronology as `(1)` loss of `*-z` after unstressed vowels and `(2)` loss of word-final `*-a` and `*-ą` [Germanic/docs/DEV_NOTES.md:21436-21443; @RingeTaylor2014, pp. 59-61]. For `2225`, that directly supports the trace's first and last non-OE steps: `*stráumaz > *stráuma` by final-`z` loss, and later `*strēama > *strēam` by final bare-`a` loss [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4839-4845].

### DEV_NOTES:line-26754-26770

- Source heading: `STAGE 3 — *au → *éa (existing breaking machinery)`
- Source line or section hint: `lines 26754-26770`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `au_fronting`; `diphthong_leveling`; `long_diphthong`; `regular_pathway`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment is the most direct current DEV_NOTES statement about the row's main vowel development. After discussing another lexical environment, DEV_NOTES says explicitly that the existing `OEAuFronting (*au → *aeu)` plus `OEDiphthongLeveling (*aeu → *ēa)` rules “handle `*au → *ēa` generally” and that, in the current project grammar, “`*au` always becomes `*ēa` in the FST” [Germanic/docs/DEV_NOTES.md:26765-26769]. For row `2225`, this is the shared note that explains the middle of the live derivation trace: `*stráuma > *stráeuma > *strēama` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4839-4840].

The fragment should still be used with proper scope. It is shared sound-change background, not a dedicated stream memo. Its value is that it preserves the project's present-tense statement that OE long `ēa` from proto `*au` is a regular rule outcome rather than a row-specific patch.

### DEV_NOTES:line-35059-35070

- Source heading: `§17.22.13.2.2 Ringe & Taylor (2014), A Linguistic History of English, vol. 2: The Development of Old English`
- Source line or section hint: `lines 35059-35070`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `ringe_taylor`; `long_ea`; `pwgmc_au`; `shared_row_support`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the best current DEV_NOTES quotation tying the row's long OE diphthong directly to handbook literature. DEV_NOTES preserves Ringe & Taylor's statement that “most examples of the long diphthong reflected PWGmc `*au`” [Germanic/docs/DEV_NOTES.md:35061-35062; @RingeTaylor2014, §6.6.3]. The local DEV_NOTES context there concerns i-umlaut of diphthongs, not `stream` specifically, but the quoted handbook generalization is directly relevant to `*stráumaz > strēam`.

For this row, the fragment establishes a literature-backed reason that the target should contain long `ēa`. `strēam` is exactly the sort of lexeme the quotation is talking about: an OE long diphthong traced back to PWGmc/PGmc `*au`, without any need for analogy, paradigm-cell substitution, or exception status [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4827-4845; @RingeTaylor2014, §6.6.3].

## Superseded or diagnostic material

### DEV_NOTES:line-1760-1765

- Source heading: `Next actionable targets (carryover)` / `Long-vowel-missing deep dive`
- Source line or section hint: `lines 1760-1765`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `long_vowel_missing`; `au_to_ea`; `project_history`; `rule_implementation`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This older note is useful only as project history. DEV_NOTES records an early “Long-vowel missing” bucket and says one of the “biggest actionable sources” was “PGmc `*au` not lengthened” and that the project should change `*aeu -> *ēa` or add a dedicated long-diphthong step [Germanic/docs/DEV_NOTES.md:1760-1765]. That matters to row `2225` because `strēam` is exactly the sort of output that would have been wrong before the `*au > *ēa` pathway was stabilized.

But this is not the best current authority for the row; it is only a breadcrumb explaining the implementation history behind the now-regular trace. Use it only if later reporting needs to explain why current DEV_NOTES passages treat `*au > *ēa` as an already-working general rule [Germanic/docs/DEV_NOTES.md:26765-26769].

- No dedicated superseded `stream` memorandum has been found in `DEV_NOTES.md`. The thinness here is not that the row was heavily revised and lost its dossier; it is that the row seems never to have acquired one, presumably because the current derivation is straightforward and exact-match.

## Open questions for later work

- If a packet or research memo is later created, keep the row's three layers explicit near the top: comparative `PROTO *stráumaz`, identical OE-facing `PROTOFORM *stráumaz`, and regular OE target `strēam` from the live exact-match derivation [Germanic/data/germanic-aligned-final.tsv:1145-1145; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4827-4845].
- If later report prose wants lexeme-specific philological support beyond the shared DEV_NOTES rule notes, fresh source canvassing would still be needed. The present slice securely preserves the shared current rule support and chronology, but it should not imply that `DEV_NOTES.md` already contains a dedicated row-numbered stream essay.
- If `dev_notes_slices/index.tsv` is reconsidered later, the only securely attachable current anchors are the shared chronology note (`DEV_NOTES:line-21436-21446`), the general `*au → *ēa` rule statement (`DEV_NOTES:line-26754-26770`), and the Ringe & Taylor quotation linking long OE `ēa` to PWGmc `*au` (`DEV_NOTES:line-35059-35070`). On present evidence they are better treated as shared support than as grounds for making row `2225` indexable.

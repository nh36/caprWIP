---
row_id: 2143
concept: nose
counterpart: nosu
proto: *nasō
protoform: *núsō
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2143-nose-nosu.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2143-nose-nosu.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2143 nose / nosu

## Current row state

- CONCEPT: `nose`
- COUNTERPART: `nosu`
- PROTO: `*nasō`
- PROTOFORM: `*núsō`
- DERIVATION_CLASS: `early_analogy`
- Live TSV row `2143` already encodes the crucial three-way distinction: comparative `PROTO *nasō`, row-level `PROTOFORM *núsō`, and OE target `nosu`; the row itself carries no explanatory note beyond its source trail [Germanic/data/germanic-aligned-final.tsv:827-827].
- The packet's compact derivation trace is current and matches the live row: `*núsō > *nósō > *nósu > nosu`; the packet also records `_None_` for `oe_known_problems.tsv` and no manifest entry for this row [Germanic/docs/lexeme_reports/packets/2143-nose-nosu.md:11-13,17-40,42-44].
- The research memo's settled recommendation is to keep the same split now shown in the TSV: `*nasō` as cognate-set proto, `*núsō` as the remodeled zero-grade/project input, and `nosu` as the OE target, while treating older `*nasō -> nosu` prose as superseded project history [Germanic/docs/lexeme_reports/research_memos/2143-nose-nosu.md:13-23,55-72,86-104,111-123].
- Repo-local philological checks support the row's present framing rather than a rollback. Campbell explicitly gives `OE nosu < *nusō`; Kroonen gives the Germanic ablaut pair `*nasō- ~ *nusō-`; Ringe-Taylor list `nosu` among the few surviving early OE feminine u-stems; Clark Hall gives `nosu f. gds. nosa`; Bosworth-Toller preserves a `nosu` entry while also showing `nasu` material, which fits DEV_NOTES' warning that full-grade and zero-grade histories should not be silently collapsed [docs/references/campbell_old_english_grammar.txt:3796-3797,16072-16075; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:20131-20147; docs/references/ringe_taylor_linguistic_history_vol2.txt:21756-21760; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29345-29345,30045-30045; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:104248-104249,105656-105662].

## Development-note summary

Current row-specific DEV_NOTES authority **does** survive for row `2143`, but it survives in two layers that must be kept separate. The first, and philologically decisive, layer is the `§15.3` correction note: the old row state paired expected OE `nosu` with `PROTOFORM *násō`, but DEV_NOTES concludes that this was inconsistent because the FST quite properly gave `nasu` from full-grade `*nasō`; the row therefore had to adopt zero-grade `*núsō` instead [Germanic/docs/DEV_NOTES.md:19774-19858]. The second, and implementation-decisive, layer is the later chronology audit: `*núsō > nosu` works only if `NWGmcULowering` sees the original final `*-ō` before `NWGmcFinalLongORaising` rewrites it to `*-u`, hence the current ordered chain `*núsō > *nósō > *nósu > nosu` [Germanic/docs/DEV_NOTES.md:24287-24308,24402-24407].

That means the slice must keep **PROTO**, **PROTOFORM**, and **OE target** sharply distinct. `PROTO *nasō` is the broader cognate-set/full-grade headword, still useful because Kroonen explicitly reconstructs the pair `*nasō- ~ *nusō-` and ties OE `nosu` to the latter, not the former [Germanic/docs/DEV_NOTES.md:19794-19807; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:20131-20147]. `PROTOFORM *núsō` is the row-level input actually fed into the OE cascade; DEV_NOTES quotes Campbell's wording, "We find o before Prim. Gmc. -ō, which has become -u in OE, e.g. OE nosu < *nusō," and treats that as the direct reason to rewrite the row's project input without erasing the broader etymological `*nasō` headword [Germanic/docs/DEV_NOTES.md:19789-19792,19846-19858; docs/references/campbell_old_english_grammar.txt:3796-3797]. OE target `nosu` is the attested Old English noun the row is meant to generate, and Ringe-Taylor's classification of `nosu` as one of the relic feminine u-stems helps explain why OE `-u` belongs to the lexeme's stable historical profile rather than being a late ad hoc repair [Germanic/docs/DEV_NOTES.md:934-934; docs/references/ringe_taylor_linguistic_history_vol2.txt:21756-21760].

The best current row-level narrative is therefore: comparative Germanic preserved both a full-grade `*nasō-` line and a remodeled zero-grade `*nusō-` line; the OE row deliberately models the second one. Under the current cascade `*núsō` undergoes NWGmc u-lowering first, giving `*nósō`, then final long `*ō` raises to `*u`, giving `*nósu`, and the remainder of the pipeline leaves `nosu` intact [Germanic/docs/DEV_NOTES.md:24295-24304,24402-24407; Germanic/docs/lexeme_reports/packets/2143-nose-nosu.md:27-39]. The row's `early_analogy` classification remains appropriate because the special move is upstream stem/ablaut selection—choosing the remodeled zero-grade input that the OE lexeme continues—not a late OE paradigm-cell workaround of the `*nahti > niht` or `*xémonų > heofon` type [Germanic/data/germanic-aligned-final.tsv:827-827; Germanic/docs/lexeme_reports/research_memos/2143-nose-nosu.md:57-63,93-103,117-123].

At the same time, the slice must not flatten away the project history. DEV_NOTES also preserves an older explanatory phase in which `*núsō > nosu` was described as though final `*ō` raising happened first and the resulting medial `*u` then lowered before `*u`; the nearby `§15.4` "Why *násō Worked Differently" block repeats that now-outdated order [Germanic/docs/DEV_NOTES.md:19809-19816,19919-19928]. That material remains useful only as diagnostic history showing how the row was first repaired before the later chronology audit made the ordering stricter. It should no longer be cited as current sound-change authority, because the later audit explicitly says that putting `NWGmcFinalLongORaising` before `NWGmcULowering` would regress row `2143` and other rows that need the lowered-plus-raised sequence [Germanic/docs/DEV_NOTES.md:24287-24308,39799-39804].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-19774-19858

- Source heading: `§15.3 TSV Correction: OE nosu 'nose' — Ablaut *nasō ~ *nusō (2026-04-15)`
- Source line or section hint: `lines 19774-19858`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `proto_vs_protoform`; `ablaut`; `zero_grade`; `row_correction`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the core current row-specific fragment because it preserves both the mismatch and the source-backed fix. DEV_NOTES states the bad old state plainly: ``*násō -> nasu (expected nosu)`` and then says the FST was right to return `nasu` from full-grade `*nasō` [Germanic/docs/DEV_NOTES.md:19776-19785]. The note then copies the two quotations that still govern the row. First, Campbell: `"We find o before Prim. Gmc. -ō, which has become -u in OE, e.g. OE nosu < *nusō"` [Germanic/docs/DEV_NOTES.md:19789-19792; docs/references/campbell_old_english_grammar.txt:3796-3797]. Second, Kroonen: `*nasō- ~ *nusō- f. 'nose'`, followed by the explicit statement that the origin of Germanic `*nasō-` versus `*nusō-` is unclear but that `*nus-` is "likely to have arisen as a secondary zero grade following a remodeling of the original paradigm" [Germanic/docs/DEV_NOTES.md:19794-19803; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:20131-20147]. The fragment's decision is therefore still current: keep comparative `*nasō` in view, but change the row-level OE input from `*násō` to `*núsō` because that is the PGmc shape that actually yields OE `nosu` [Germanic/docs/DEV_NOTES.md:19805-19858].

### DEV_NOTES:line-934-934

- Source heading: `Source analysis`
- Source line or section hint: `line 934`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `u_stem`; `OE_philology`; `lexeme_identity`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1992`

This shared fragment is short but still worth indexing because it supplies the synchronically OE-facing classification that the ablaut note by itself does not. DEV_NOTES copies Ringe-Taylor's statement that the surviving early OE u-stems include feminine `hand`, `nosu`, and `duru`, with `duru` specially noted as a shifted root noun [Germanic/docs/DEV_NOTES.md:932-934; docs/references/ringe_taylor_linguistic_history_vol2.txt:21756-21760]. For row `2143`, the practical value is that `nosu` is not merely a reconstructed phonological endpoint. It is a real OE noun belonging to the small residual u-stem class, and that helps explain why the row's OE target remains `nosu` after the `*nasō / *núsō` correction rather than being rewritten toward some different citation form [Germanic/data/germanic-aligned-final.tsv:827-827; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:30045-30045].

### DEV_NOTES:line-24287-24308

- Source heading: `3. Root-cause: U-lowering has been bled`
- Source line or section hint: `lines 24287-24308`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `chronology`; `u_lowering`; `final_ō_raising`; `implementation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2185,2200`

This later chronology fragment is the controlling current implementation authority for the row. DEV_NOTES says that when final long `*ō` raising fired first, `*núsō` became `*núsu`, so u-lowering then saw only a high-vowel sequence and "correctly by its own rule, [did] nothing"; the root `*u` consequently surfaced as `u`, not `o` [Germanic/docs/DEV_NOTES.md:24287-24291]. The note then contrasts the wrong and correct orders explicitly: wrong order `*núsō → *núsu`; correct order `NWGmcULowering: *núsō → *nósō`, then `NWGmcFinalLongORaising: *nósō → *nósu` [Germanic/docs/DEV_NOTES.md:24295-24304]. For row `2143`, this fragment supersedes any earlier wording that made `nosu` depend on a later "medial `u > o` before `u`" step. The live compact trace in the packet follows the later audited order, not the older provisional explanation [Germanic/docs/lexeme_reports/packets/2143-nose-nosu.md:27-39].

### DEV_NOTES:line-39799-39804

- Source heading: `Q4 finding — lautgesetz status (cell-switch, not wontfix)`
- Source line or section hint: `lines 39799-39804`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `regression_guard`; `chronology`; `shared_rule_dependency`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `2185,2200`

This shared late audit is not where row `2143` was first solved, but it is useful because it shows that the `*núsō > nosu` chronology stayed live after later re-analysis elsewhere. DEV_NOTES warns that reordering `NWGmcFinalLongORaising` before `NWGmcULowering` would regress rows `2143 (*núsō → nosu)`, `2200 (*súrgō → sorg)`, and `2185 (*skúflō → sċofl)` [Germanic/docs/DEV_NOTES.md:39799-39804]. For row `2143`, this is best used as a regression-guard fragment rather than as primary philology: it confirms that the row is now part of the data blocking a bad chronology change, but the row's own ablaut correction and ordered derivation still come from the earlier fragments [Germanic/docs/DEV_NOTES.md:19774-19858,24287-24308].

### DEV_NOTES:line-19809-19816-and-19919-19928

- Source heading: `The Sound Change Pathway` / `Why *násō Worked Differently`
- Source line or section hint: `lines 19809-19816 and 19919-19928`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `misleading_if_uncontextualized`
- Issue tags: `outdated_chronology`; `project_history`; `diagnostic_only`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This material should be preserved, but only with an explicit warning label. In the same April note that correctly fixed the row's `PROTOFORM`, DEV_NOTES still described the path as `*nusō > *nusu > *nosu > nosu`, i.e. final `*ō` raising first and then a later medial lowering of `u` to `o` before `u` [Germanic/docs/DEV_NOTES.md:19809-19816]. The nearby `§15.4` block then reused the same order when explaining why `*násō` had "worked differently" [Germanic/docs/DEV_NOTES.md:19919-19928]. Later DEV_NOTES work explicitly replaced that chronology with the audit preserved at lines `24287-24308`, and the packet's current derivation likewise uses `*núsō > *nósō > *nósu > nosu` instead [Germanic/docs/DEV_NOTES.md:24287-24308; Germanic/docs/lexeme_reports/packets/2143-nose-nosu.md:27-39]. This fragment is therefore valuable as project history, but misleading if quoted as the row's present sound-change account.

## Superseded or diagnostic material

- The main superseded row history is the older project state in which `nosu` was still expected from `PROTOFORM *násō`. DEV_NOTES now preserves that state only in order to show why the correction was necessary: `*nasō` regularly gives `nasu`, not `nosu` [Germanic/docs/DEV_NOTES.md:19776-19785,19846-19858].
- A second superseded layer is the first explanation of the corrected row, which still used the wrong chronology `*núsō > *núsu > *nosu`. That wording should remain visible only to explain why later chronology debugging had to revisit an already-correct TSV fix [Germanic/docs/DEV_NOTES.md:19809-19816,19919-19928,24287-24308].
- Philological dictionary material should also be handled carefully. Clark Hall normalizes `nasu=nosu` but gives the live headword as `nosu`, while Bosworth-Toller preserves both a `nosu` entry and `nasu` material; those are useful for showing OE variation/background, not for undoing the row's present `*nasō / *núsō / nosu` split [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29345-29345,30045-30045; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:104248-104249,105656-105662].

## Open questions for later work

- If a final lexeme report is drafted, keep the distinction explicit in one sentence near the top: cognate-set `*nasō`, OE-directed input `*núsō`, target `nosu`; the memo correctly identifies that as the non-negotiable framing for this row [Germanic/docs/lexeme_reports/research_memos/2143-nose-nosu.md:57-63,111-123].
- Decide whether later final prose should mention OE `nasu` explicitly as parallel/background evidence or relegate it to a short source-audit note. The repo has enough evidence to say it exists, but the current row is specifically about `nosu`, not about neutralizing the two ablaut lines [Germanic/docs/DEV_NOTES.md:19840-19844; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:29345-29345; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:104248-104249].
- If `DEV_NOTES.md` is ever cleaned up, annotate the old `*núsō > *núsu > *nosu` wording so future packeting does not surface it as though it were still the current chronology [Germanic/docs/DEV_NOTES.md:19809-19816,19919-19928,24287-24308].

---
row_id: 2307
concept: yoke
counterpart: ġeoc
proto: *júką
protoform: *júką
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2307 yoke / ġeoc

## Current row state

- The live OE row is currently regular and already aligned across the proto fields: `CONCEPT = yoke`, `COUNTERPART = ġeoc`, `PROTO = *júką`, `PROTOFORM = *júką`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1464-1464].
- `PROTO` and `PROTOFORM` are identical here. The comparative proto label and the OE-facing derivational input are therefore the same form `*júką`; the attested OE counterpart remains the distinct surface target `ġeoc` [Germanic/data/germanic-aligned-final.tsv:1464-1464].
- The support infrastructure around the live row is thin but clean: `oe_known_problems.tsv` has no `*júką` entry; `coverage_audit.md` lists row `2307` as `regular` with `NOTE? no`; and `report_manifest.tsv` still has no manifest-backed report entry for the row [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:423-423; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The current published derivation trace is exact-match and should be treated as the present pipeline state: `PROTO: *júką`, `EXPECTED: ġeoc`, `OUTPUTS: ġeoc`, with the trace `*júką` → `*jéuką` by `OE Ws Palatal Glide`, `*jéuką` → `*jéoką` by `OE Diphthong Leveling`, `*jéoką` → `*jéok` by `OE Heavy Syllable Nasal Apocope`, then orthographic `ġeoc` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6147-6167].

## Development-note summary

Unlike `year / ġēar`, this row does preserve a dedicated row-local DEV_NOTES block. The section `OE ġeoc 'yoke' — Palatal Glide before Back Vowel (not breaking)` was written to explain why older output `ġoc` was wrong and why `ġeoc` should not be analysed as an ordinary breaking reflex [Germanic/docs/DEV_NOTES.md:11363-11420]. Its enduring core claim is still the key row-local point: the `eo` of `ġeoc` is not evidence for breaking but for a palatal-glide development after inherited initial `*j` before a back vowel [Germanic/docs/DEV_NOTES.md:11369-11398].

That row-local note is now best read together with the later shared research section `Palatal Glide Orthography: Comprehensive Research (2026-04-09)`. The later section partly supersedes the earlier implementation diagnosis: it says the phonology was already inserting the glide correctly, while the remaining defect was orthographic failure to render glide+`u` as standard West-Saxon `eo`; it also preserves the best compact statement of the normalized analysis, including Campbell's spelling evidence and Ringe & Taylor's interpretation of `geoc` as `/jok/` [Germanic/docs/DEV_NOTES.md:15691-15735,15823-15835,15863-15905].

Taken together, the surviving DEV_NOTES material supports a careful three-way distinction that should stay explicit in this slice. `PROTO = *júką` is the comparative and derivational input; `PROTOFORM = *júką` is identical rather than a surrogate repair form; and the attested OE target is `COUNTERPART = ġeoc` [Germanic/data/germanic-aligned-final.tsv:1464-1464]. The notes do not support treating OE `eo` here as the same kind of genuine diphthong found in `ġēar`; instead they repeatedly place `ġeoc` in the initial-palatal-plus-back-vowel class where the written `e/eo` reflects a palatal glide or its orthographic residue [Germanic/docs/DEV_NOTES.md:11371-11398,15724-15735,15827-15835].

The live debug trace shows that the present cascade now encodes exactly that interpretation. The rule chain no longer relies on a vague “breaking missing” label: it explicitly applies `OE Ws Palatal Glide`, then `OE Diphthong Leveling`, then heavy-syllable apocope, and reaches exact `ġeoc` with no row-local exception flag [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6147-6167; Germanic/data/oe_known_problems.tsv:1-8]. The safest current characterization is therefore: **regular row with strong row-local DEV_NOTES support on palatal-glide analysis, plus later shared background clarifying that the surviving `eo` spelling is orthographic/phonological glide material rather than breaking** [Germanic/docs/DEV_NOTES.md:11363-11545,15687-15905].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-11363-11545

- Source heading: `OE ġeoc 'yoke' — Palatal Glide before Back Vowel (not breaking)`
- Source line hint: `lines 11363-11545`
- Fragment type: `row_local_analysis_with_historical_fix_context`
- Status: `current core analysis with superseded mismatch framing`
- Issue tags: `yoke`; `palatal_glide`; `not_breaking`; `initial_j`; `historical_fix`
- Recommended next use: `cite_when_explaining_why_ġeoc_has_eo_without_breaking`
- Shared-with rows if relevant: `2308 youth / ġeoguþ`; more broadly initial-palatal + back-vowel rows, but this section itself is row-local to `ġeoc`

This is the most important surviving row-local DEV_NOTES material. It opens with the mismatch statement `*juką` → `ġoc` vs. expected `ġeoc`, then explicitly rejects the earlier classifier label: “the `eo` in `ġeoc` is NOT from breaking” [Germanic/docs/DEV_NOTES.md:11365-11373]. That sentence should be carried forward as the row's main analytical warning.

The section then records the Campbell evidence in a form worth preserving verbatim: “In W-S the glide is written with considerable regularity... for Prim. Gmc. initial *jū we find iū (gū), giū, geū... e.g. iung, giong, geong young, iugup, giogup, geogup youth, **iuc, gioc, geoc yoke**” [Germanic/docs/DEV_NOTES.md:11377-11382]. The note's own interpretation is similarly useful and still accurate at a high level: “The `e/eo` is a **palatal glide** that develops to facilitate the transition from a palatalized consonant to a following back vowel” [Germanic/docs/DEV_NOTES.md:11383-11389].

The four-step sequence in the row-local note remains a good shorthand for the historical intuition even though later notes refine the implementation details: palatalization of initial `*j`, development of a glide vowel before `*u`, later lowering/leveling of the back vowel, and final orthographic `ġeoc` [Germanic/docs/DEV_NOTES.md:11386-11389]. The note also preserves a concise contrast that is still worth quoting: “**Breaking**: front vowel → diphthong before r/l/h + consonant” versus “**Palatal glide**: glide vowel inserted after palatal consonant, before back vowel” [Germanic/docs/DEV_NOTES.md:11391-11397].

What should not be carried forward unqualified is the old `Status: NEEDS NEW RULE` framing. The same section reports a fix implemented on 2026-03-17 and says `*juką` → `ġeoc` succeeds after adding `OEWsPalatalGlide` [Germanic/docs/DEV_NOTES.md:11399-11420]. That historical implementation narrative is useful, but only as project history; the live row is no longer a mismatch and now uses stressed `*júką` in both proto fields [Germanic/data/germanic-aligned-final.tsv:1464-1464].

### DEV_NOTES:line-15687-15905

- Source heading: `Palatal Glide Orthography: Comprehensive Research (2026-04-09)`
- Source line hint: `lines 15687-15905`
- Fragment type: `shared_background_directly_probative`
- Status: `current`
- Issue tags: `palatal_glide_orthography`; `eo_spelling`; `ringe_taylor`; `campbell`; `not_breaking`
- Recommended next use: `cite_for_the_best_current_account_of_why_ġeoc_spells_glide_plus_back_vowel_as_eo`
- Shared-with rows if relevant: `2308 youth / ġeoguþ`; `young`-type initial-`j` rows; more broadly the palatal-glide orthography cohort

This is a shared section, not a row-local memorandum, but it is directly probative for row `2307` because it reopens exactly the `ġeoc/ġeoguþ` problem. The issue summary says that for `*juką` the phonology was already right and that the remaining defect was orthography: “The phonology is correct (glide *e is inserted), but the orthography layer fails to convert glide+u to the standard WS digraph `eo`” [Germanic/docs/DEV_NOTES.md:15691-15695]. That refinement matters because it narrows the row's current analysis from a broad “missing glide” story to a more precise “orthographic representation of glide+u” story.

The section preserves the key Campbell quotation in a more explicit orthography-focused form: “The glide is usually written e, but sometimes i. **In W-S and Kt., glide+u is usually written eo or io, probably to avoid the multiplication of graphs**” [Germanic/docs/DEV_NOTES.md:15722-15727]. It then repeats the lexeme set with `**geoc** yoke` among the normalized West-Saxon spellings [Germanic/docs/DEV_NOTES.md:15729-15735]. For this row, those lines are stronger than a stray search hit because they tie `ġeoc` directly to a documented spelling convention for initial `j` plus back vowel.

The most important compact interpretive quotation is from Ringe & Taylor: “After word-initial /j/ followed by a back vowel that practice was universal. Thus *geara* 'long ago' is /ja:ra/, *geomor* 'lamentation' is /jo:mor/, **geoc 'yoke' is /jok/** ... On the other hand, *géar* 'year' ... contain genuine diphthongs” [Germanic/docs/DEV_NOTES.md:15827-15831]. For row `2307`, this is the clearest surviving statement that `ġeoc` belongs to the orthographic-glide class rather than the genuine-diphthong class.

The later subsection `Why U-Lowering Does Not Apply` is also worth preserving because it prevents an easy misreading of the live trace. DEV_NOTES says: “This is phonologically CORRECT: the `eo` in `geoc` is orthographic, not the result of phonological lowering. R/T explicitly transcribe geoc as /jok/” [Germanic/docs/DEV_NOTES.md:15876-15877]. The proposed rule `OEGlideUToEO` is implementation history, but its analytical point remains current: once the glide is present, West-Saxon `eo` spelling is a representation choice for glide+`u`, not a sign that the row should be filed under ordinary breaking [Germanic/docs/DEV_NOTES.md:15879-15905].

## Superseded or diagnostic material

### DEV_NOTES mismatch framing inside the row-local block

The opening lines of the row-local note are now partly superseded as project-state reporting. `Mismatch: *juką → FST ġoc | Expected ġeoc` and `Status: NEEDS NEW RULE — Palatal glide insertion` were accurate when written, but they no longer describe the live row, which now derives exactly from stressed `*júką` to `ġeoc` [Germanic/docs/DEV_NOTES.md:11365-11367; Germanic/data/germanic-aligned-final.tsv:1464-1464; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6147-6167]. These lines should therefore be used only as historical debugging context, not as current row state.

### DEV_NOTES issue-summary language in the later shared section

The comprehensive research section also contains superseded project-state prose. Its opening sentence says the FST produced `ġeuc` for PGmc `*juką` and that `ġeoc` was only the expected output [Germanic/docs/DEV_NOTES.md:15691-15694]. That is valuable diagnostic history because it explains why the orthography-focused investigation was opened, but it should not be copied as if it were still true of row `2307` after the live exact-match trace [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6147-6167].

### Shared diagnostic material outside DEV_NOTES

The final-vowel apocope investigation is relevant but should stay secondary to the dedicated DEV_NOTES sections. It lists `*juką → ġeoc` among the cases where a proto form that looks light becomes heavy in OE after vowel changes: “`*juką → ġeoc` - *u → eo (diphthong!) = HEAVY in OE” [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:153-159]. That observation helps explain why the live trace now includes `OE Heavy Syllable Nasal Apocope`, but it is diagnostic shared background rather than row-local lexical authority [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6160-6167].

The archived heavy-syllable apocope DEV_NOTES note is similar: useful for rule history, not for primary row-local semantics. It documents the empirical discovery and implementation of `OldEnglishHeavySyllableNasalApocope` as a broad pattern over heavy stems, including proto `*-ą` [Germanic/docs/DEV_NOTES.md:1591-1622]. For `2307`, that material explains why the live derivation ends `*jéoką` → `*jéok`, but it should remain explicitly classed as shared diagnostic support rather than as the main reason `ġeoc` is spelled with `eo` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6160-6167].

## Open questions for later work

- If this row later receives a full packet or memo, the top-level distinction should stay explicit: `PROTO = *júką`, `PROTOFORM = *júką`, and attested OE `COUNTERPART = ġeoc`; the row is regular, but its `eo` must still be explained as palatal-glide material rather than as a genuine diphthong or ordinary breaking reflex [Germanic/data/germanic-aligned-final.tsv:1464-1464; Germanic/docs/DEV_NOTES.md:15827-15835].
- The live trace uses both `OE Ws Palatal Glide` and `OE Diphthong Leveling`, while the later orthography note emphasizes that normalized West-Saxon `eo` can be orthographic even where Ringe & Taylor read `/jok/`. A future memo could spell out more explicitly which part of the present chain is meant as phonological history and which part as orthographic normalization [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6160-6167; Germanic/docs/DEV_NOTES.md:15691-15695,15827-15905].
- If later indexing work distinguishes slice-only rows from rows worth explicit index treatment, `2307` has a stronger claim than a pure shared-background row because it preserves a dedicated lexeme heading in DEV_NOTES (`OE ġeoc 'yoke'`) plus later shared corroboration; however, any future index entry should make clear that the mismatch-state prose is historical and that the live row is now regular [Germanic/docs/DEV_NOTES.md:11363-11545,15687-15905; Germanic/docs/lexeme_reports/coverage_audit.md:423-423].

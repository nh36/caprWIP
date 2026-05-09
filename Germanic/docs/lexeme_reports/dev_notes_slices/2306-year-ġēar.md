---
row_id: 2306
concept: year
counterpart: ġēar
proto: *jḗrą
protoform: *jḗrą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2306 year / ġēar

## Current row state

- The live OE row is now fully regular and already uses the stressed-long-vowel spelling in both proto fields: `CONCEPT = year`, `COUNTERPART = ġēar`, `PROTO = *jḗrą`, `PROTOFORM = *jḗrą`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1460-1460].
- `PROTO` and `PROTOFORM` are identical here. This row is therefore not using a surrogate input, alternate paradigm cell, or repair preform; the comparative proto label and the OE-facing derivational input are the same stressed form `*jḗrą` [Germanic/data/germanic-aligned-final.tsv:1460-1460].
- Current support infrastructure is deliberately thin. `oe_known_problems.tsv` has no entry for row `2306`, for `year`, for `ġēar`, or for `*jḗrą`; `coverage_audit.md` lists the row as `regular` with `NOTE? no` and no linked report path; and `report_manifest.tsv` contains no manifest-backed report entry for this row [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:422-422; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The current published derivation trace is an exact match and gives the live rule chain now underwriting the row: `*jḗrą` → `*jǣrą` by `NWGmc Long E Lowering`, then `*jǣr` by `OE Heavy Syllable Nasal Apocope`, then `*jēar` by `OE Ws Palatal Diphthongization`, surfacing orthographically as `ġēar` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6126-6146].
- Older diagnostic material still shows why this row once mattered for apocope work: the final-vowel investigation explicitly listed `*jērą` among the long-vowel heavy stems and recorded the pre-fix mismatch `*jērą → ġēra (exp. ġēar)` [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:148-150,287-288]. That material is useful as project history, but the live row now reflects the repaired state with stressed `*jḗrą` and exact output `ġēar` [Germanic/data/germanic-aligned-final.tsv:1460-1460; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6126-6146].

## Development-note summary

No dedicated row-local `year / ġēar / *jḗrą` block survives in `DEV_NOTES.md`. The replacement note therefore has to be conservative: it must be built from the best surviving shared material plus the current exact-match derivation trace, not from a lost lexeme-specific memorandum [Germanic/docs/DEV_NOTES.md:15687-15835,42679-42749; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6126-6146].

The most important surviving DEV_NOTES substance is the explicit contrast between **glide orthography after initial palatals** and **genuine diphthongs**. In the palatal-glide research dossier, DEV_NOTES quotes Ringe & Taylor: “After word-initial /j/ followed by a back vowel that practice was universal. Thus *geara* 'long ago' is /ja:ra/, *geomor* 'lamentation' is /jo:mor/, **geoc 'yoke' is /jok/** … On the other hand, *géar* 'year', *geolu* 'yellow', *georne* 'gladly', etc. contain genuine diphthongs” [Germanic/docs/DEV_NOTES.md:15827-15831]. For row `2306`, that means `ġēar` must not be treated like `ġeoc` or `ġeoguþ`, where `eo` can be largely orthographic/glide-driven. The row belongs on the “genuine diphthong” side of the contrast [Germanic/docs/DEV_NOTES.md:15691-15694,15724-15734,15827-15835].

The second durable point is that the live row's stressed proto spelling is intentional and current, not a stray normalization. DEV_NOTES' stressed-long-`ē` refactor says that a dedicated `*ḗ` tier was added so root-syllable long `ē` would be represented explicitly, that 16 lemmas were promoted in both `PROTOFORM` and `PROTO` columns, and that verification probes remained stable, including `*jḗrą → ġēar` [Germanic/docs/DEV_NOTES.md:42679-42749]. For this row, that note is the closest surviving row-specific DEV_NOTES support. It does not replace a philological lexeme essay, but it does establish that the present row state—`PROTO = PROTOFORM = *jḗrą`, exact output `ġēar`—is the intended current configuration rather than a silent transcription accident [Germanic/data/germanic-aligned-final.tsv:1460-1460; Germanic/docs/DEV_NOTES.md:42679-42749].

The third point is methodological. The live derivation trace already supplies the row-local chronology that DEV_NOTES no longer spells out in one place: stressed long `*ḗ` lowers in NWGmc to `*ǣ`, heavy-syllable apocope removes final nasal `*ą`, and West-Saxon palatal diphthongization yields `ēa` after initial `j`, giving `ġēar` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6133-6146]. Because that exact chain succeeds with no exception flag and no row-local known-problems entry, the safest present characterization is: **regular row, no surviving row-specific DEV_NOTES block, supported by shared current notes plus the live exact-match trace** [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:422-422].

## Relevant DEV_NOTES fragments

No standalone row-specific DEV_NOTES block for `2306 year / ġēar` survives. The fragments below are the surviving material that most directly bears on the row.

### DEV_NOTES:line-15687-15835

- Source heading: `Palatal Glide Orthography: Comprehensive Research (2026-04-09)`
- Source line hint: `lines 15687-15835`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `initial_j`; `palatal_glide`; `genuine_diphthong`; `year_vs_yoke`
- Recommended next use: `cite_when_distinguishing_true_diphthong_from_glide_spelling`
- Shared-with rows if relevant: `2307 yoke / ġeoc`; `2308 youth / ġeoguþ`; more broadly other initial-`j` OE rows

Although the section was opened to fix `ġeoc` and `ġeoguþ`, it preserves the most useful surviving DEV_NOTES quotation for `ġēar`. Campbell is first used to show that after Proto-Germanic initial `*j`, West Saxon often developed a written glide before back vowels and that glide+`u` was commonly written `eo/io` [Germanic/docs/DEV_NOTES.md:15702-15734]. Brunner and Luick then describe the same initial-palatal environment as producing `iu`, `eo`, and `ea` spellings/diphthongs in various lexical sets, with Luick's note that `io, eo, i für iu` point to `iu`, while `ea` beside `eo` points to a different vowel history [Germanic/docs/DEV_NOTES.md:15768-15821].

The row-specific value comes from the Ringe-Taylor quotation embedded in that dossier: “**geoc 'yoke' is /jok/** … On the other hand, **`géar` 'year' … contain genuine diphthongs**” [Germanic/docs/DEV_NOTES.md:15827-15831]. That sentence is doing real classificatory work for row `2306`. It says that `year` is not merely another member of the `geoc`-type orthographic `eo` set. So for this row the fragment should be treated as **shared-background-only but directly probative**: it survives from a shared initial-`j` discussion, yet it explicitly preserves the “year” side of the contrast and justifies treating `ġēar` as a true diphthong outcome in the current row analysis [Germanic/docs/DEV_NOTES.md:15823-15835].

### DEV_NOTES:line-42679-42749

- Source heading: `§17.49 Stressed long-ē tier (\`*ḗ\`) — extending the §17.46 stress-tier convention`
- Source line hint: `lines 42679-42749`
- Fragment type: `row_specific_verification_inside_shared_refactor`
- Status: `current`
- Issue tags: `stressed_long_e`; `proto_vs_protoform`; `current_row_state`; `verification`
- Recommended next use: `cite_for_current_proto_spelling_and_live_configuration`
- Shared-with rows if relevant: other rows promoted to stressed `*ḗ`, but `2306` is one of the explicitly named probe items

This is the closest thing to a surviving row-specific DEV_NOTES mention. The section documents a branch-wide refactor that introduced explicit stressed long `*ḗ` into the cascade, explains that root-syllable long `ē` lemmas were promoted in both `PROTOFORM` and `PROTO`, and then lists invariant verification probes, including `*jḗrą → ġēar` [Germanic/docs/DEV_NOTES.md:42679-42749]. For row `2306`, this matters more than a bare search hit: it proves that the present stressed spelling in the TSV is intentional project policy, not just later editorial normalization.

The fragment is still **shared** rather than a lexeme dossier, so it does not by itself explain why `ġēar` has `ēa`. What it does secure is the row's present input state and the distinction between older search-noise forms like `*jērą` and the live row's deliberately stressed `*jḗrą` [Germanic/docs/DEV_NOTES.md:42727-42739; Germanic/data/germanic-aligned-final.tsv:1460-1460]. It should therefore be used whenever later work needs to justify the exact current row fields rather than only the general phonology.

## Superseded or diagnostic material

### DEV_NOTES:line-1591-1622

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line hint: `lines 1591-1622`
- Fragment type: `diagnostic_support`
- Status: `archived_but_still_reflected_in_live_trace`
- Issue tags: `heavy_syllable`; `final_ą_loss`; `apocope_history`
- Recommended next use: `use_for_rule_history_only`
- Shared-with rows if relevant: broad heavy-stem `*-ą` cohort

This archived note is not a row-specific authority, but it still explains why the live trace contains `OE Heavy Syllable Nasal Apocope`. DEV_NOTES records that an empirical rule deleting proto `*ą` after heavy syllables was added, that heavy stems were disproportionately represented among the spurious-final-vowel cases, and that the rule was implemented as `OldEnglishHeavySyllableNasalApocope` [Germanic/docs/DEV_NOTES.md:1595-1622]. The live row trace still uses exactly that rule name in `*jǣrą > *jǣr` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6137-6140].

For `2306`, this material is therefore **diagnostic, not primary**. It helps explain the rule history behind the current exact derivation, and the companion investigation file explicitly includes `*jērą` among the heavy long-vowel cases and shows the older mismatch `*jērą → ġēra (exp. ġēar)` [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:148-150,287-288]. But because the DEV_NOTES section is explicitly archived and statistical, it should not be mistaken for a current row-local memorandum [Germanic/docs/DEV_NOTES.md:1591-1622].

### DEV_NOTES:line-11252-11255

- Source heading: `Risks / What to Check` within the `sċēaþ` rule-order note
- Source line hint: `lines 11252-11255`
- Fragment type: `superseded_or_inexact_example`
- Status: `diagnostic_only`
- Issue tags: `search_false_friend`; `older_proto_notation`; `do_not_copy_verbatim`
- Recommended next use: `ignore_as_row_authority`
- Shared-with rows if relevant: none

This is the one surviving place where DEV_NOTES casually mentions `*jērą`, but it should **not** be used as authoritative row prose. The line says “Forms like `*gēbanan → giefan`, `*jērą → géar`. These have short `*e` that undergoes WS palatal diphthongization to ie” [Germanic/docs/DEV_NOTES.md:11252-11255]. For row `2306`, that wording is inexact on multiple fronts: the live row uses stressed long `*jḗrą`, not plain `*jērą`; the current target is `ġēar`, not `géar`; and the row's published trace goes through `NWGmc Long E Lowering` plus `OE Ws Palatal Diphthongization`, not a short-`e` → `ie` pathway [Germanic/data/germanic-aligned-final.tsv:1460-1460; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6133-6146].

Treat this passage as a **diagnostic false friend** created by literal searching. It shows that the lexeme was in the developer's mind during an unrelated rule-order discussion, but it is superseded by the later stressed-`*ḗ` refactor and by the live exact-match trace [Germanic/docs/DEV_NOTES.md:42679-42749].

## Open questions for later work

- If a packet or memo is later created for row `2306`, it should keep the three live layers explicit at the top: comparative `PROTO`, identical OE-facing `PROTOFORM`, and attested OE `COUNTERPART = ġēar`, all now aligned under the exact-match derivation `*jḗrą > *jǣrą > *jǣr > *jēar > ġēar` [Germanic/data/germanic-aligned-final.tsv:1460-1460; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6126-6146].
- A current non-archived note on heavy-syllable `*-ą` loss would still be useful. Row `2306` now derives correctly, but one of its crucial steps is still documented mainly in archived empirical prose plus the separate investigation file rather than in a fresh stabilized DEV_NOTES section [Germanic/docs/DEV_NOTES.md:1591-1622; Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:133-160].
- If later slice indexing is expanded, the safest anchors are the palatal-glide/genuine-diphthong contrast (`15687-15835`) and the stressed-`*ḗ` refactor (`42679-42749`); the short-`*e` throwaway example at `11252-11255` should remain excluded from any authoritative row index [Germanic/docs/DEV_NOTES.md:11252-11255,15687-15835,42679-42749].

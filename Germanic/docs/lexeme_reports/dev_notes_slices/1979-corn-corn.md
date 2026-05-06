---
row_id: 1979
concept: corn
counterpart: corn
proto: *kúrną
protoform: *kúrną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/1979-corn-corn.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/1979-corn-corn.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1979 corn / corn

## Current row state

- CONCEPT: `corn`
- COUNTERPART: `corn`
- PROTO: `*kúrną`
- PROTOFORM: `*kúrną`
- DERIVATION_CLASS: `regular`
- Live TSV note: `Proto: oblique *kurnăn→*kurną (n. a-stem nom.sg.; Kroonen)`
- `oe_known_problems.tsv`: no entry for `*kúrną`, `*kurnăn`, or `corn`.
- Packet / manifest state: the packet reports `_No manifest entry._`
- Packet derivation trace: `*kúrną -> *kórną -> *kórn -> corn`, i.e. NWGmc u-lowering followed by OE heavy-syllable nasal apocope.

## Development-note summary

No securely attachable **current** row-specific DEV_NOTES authority survives for row 1979. The only direct DEV_NOTES hit that actually names the lexeme is an early mismatch-bucket note recording `*kurnăn -> cornan` as an over-inflected debugging path [DEV_NOTES:line-1569-1572]. That fragment is still worth preserving, but only as superseded project chronology. It does **not** challenge the live row's present analysis, and it should not be promoted into evidence for attested OE `cornan`.

The current row instead depends on keeping three levels separate. First, comparative dictionaries use lemma-style headwords such as `*kurna-` and `*kurnan` for the cognate set, with OE `corn` among the reflexes [@Kroonen2013, s.v. "*kurna-"; @Orel2003, s.v. "*kurnan"]. Second, the live TSV row deliberately feeds the singular FST input `*kúrną`, not the note's oblique `*kurnăn`. Third, the OE target is the ordinary attested noun `corn`, directly supported in the repo's lexical materials; Bright's glossary is especially useful because it also preserves the paradigm background `corn, n., corn, grain : gs. cornes` [@ClarkHall1960, s.v. "corn"; @BosworthToller1898, s.v. "corn"; @BrightCassidyRingler1971, glossary s.v. "corn"].

For working-note purposes, the row-level conclusion is therefore simple but needs to be said explicitly: row 1979 is a **regular** derivation from `*kúrną` to `corn`. The packet's compact trace is consistent with that state: NWGmc u-lowering gives `*kórną`, and OE heavy-syllable nasal apocope yields `*kórn`, surfacing as `corn`. The TSV note's `*kurnăn→*kurną` should be carried only as comparative/paradigmatic background explaining why oblique forms exist in the literature; it is not a competing live `PROTOFORM`, not a hidden paradigm-cell requirement, and not an unresolved modelling failure.

The packet also needs one hygiene warning preserved in the slice itself. Its other DEV_NOTES hit at `DEV_NOTES.md:6123` is a false positive on `Corn` = **Cornish** inside the adder discussion, not evidence for OE `corn` [DEV_NOTES:line-6119-6125]. Since row 1979 has so little genuine DEV_NOTES material, this false positive is exactly the kind of noise later writers might accidentally recycle unless the slice records the rejection explicitly.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1569-1572

- Source heading: `Consonant Mismatch Bucket Refinement (2026-02-07)`
- Source line or section hint: `lines 1569-1572`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `inflectional_suffix_extra`; `wrong_input_form`; `debug_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs: `1954`

This is the only securely attachable row-specific DEV_NOTES fragment, and it is preserved solely as stale chronology. DEV_NOTES classifies `*kurnăn -> cornan` under `inflectional_suffix_extra` and glosses such examples as `"Likely TSV data issues (wrong inflectional form selected)"` [DEV_NOTES:line-1569-1572]. For row 1979, the fragment therefore documents one abandoned project state very precisely: an oblique-style input with extra nasal material produced suffixed `cornan` instead of citation-form `corn`. It should be cited only to explain why the project no longer feeds `*kurnăn` into the row, not as evidence that OE `cornan` is the target and not as a sign that the current `regular` row still lacks a working derivation.

### DEV_NOTES:line-6119-6125

- Source heading: `Orel (2003) p.279, s.v. *naþraz`
- Source line or section hint: `lines 6119-6125`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `keyword_collision`; `cornish_false_positive`; `packet_hygiene`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This range is included only because the packet surfaced it as an "exact COUNTERPART" hit. The match is false: `Corn nader id.` at line 6123 means **Cornish** `nader`, not OE `corn`, and the surrounding note belongs entirely to the adder etymology [DEV_NOTES:line-6119-6125]. Later report work should keep this rejection explicit so that the row's thin DEV_NOTES footprint does not get padded with unrelated `Corn`/`corn.` collisions.

## Superseded or diagnostic material

The main diagnostic point is negative rather than constructive. DEV_NOTES does **not** currently preserve a live row-level argument for `corn` comparable to the long analytical notes written for harder lexemes. What survives is only (a) the old bucket entry showing why `*kurnăn -> cornan` was discarded and (b) a reviewed false positive on `Corn` = Cornish. Later workflow should therefore treat the live TSV row, the packet's compact derivation trace, and the checked lexicographic / comparative sources as the real current authority, while keeping the DEV_NOTES material in its narrower role as debugging history and search-noise control.

## Open questions for later work

- If the TSV `NOTE` is ever rewritten, clarify that `*kurnăn` is comparative stem/paradigm background and **not** the live derivational input for row 1979.
- If a future final report wants paradigm context, use attested OE `cornes` as background for the noun's inflectional profile without replacing the row target `corn`.
- Unless additional row-local DEV_NOTES material turns up later, keep index integration conservative: preserve the stale bucket note and the rejected Cornish false positive, but do not imply that row 1979 has a richer DEV_NOTES dossier than it actually does.

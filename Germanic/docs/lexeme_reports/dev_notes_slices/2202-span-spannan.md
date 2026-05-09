---
row_id: 2202
concept: span
counterpart: spannan
proto: *spánnaną
protoform: *spánnaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2202-span-spannan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2202-span-spannan.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2202 span / spannan

## Current row state

- The live OE row reads `2202	span	spannan	*spánnaną	*spánnaną	regular`, with TSV note `OE target: spann→spannan (inf. of str.v. class VII; noun 'spann' in *spannō row)` [Germanic/data/germanic-aligned-final.tsv:1055-1055].
- For this row, `PROTO` and `PROTOFORM` are the same verbal form `*spánnaną`. They are not a noun comparator, not a paradigm-cell substitute, and not a repair input borrowed from another row. The OE `COUNTERPART` represented by the row is the infinitive `spannan` [Germanic/data/germanic-aligned-final.tsv:1055-1055].
- The packet's compact derivation already matches the live row exactly: `PROTO: *spánnaną`, `EXPECTED: spannan`, `OUTPUTS: spannan`, ending with `Outcome: spannan` and repeating the same TSV note [Germanic/docs/lexeme_reports/packets/2202-span-spannan.md:17-42].
- `oe_known_problems.tsv` has no row-local exception entry for `2202`; the ledger currently lists unrelated items only, so the repository is not treating `*spánnaną → spannan` as a live unresolved mismatch [Germanic/data/oe_known_problems.tsv:1-8].

## Detailed development-note summary

Direct DEV_NOTES support for the **verb** row is thin, and that fact needs to stay explicit. The packet for row 2202 records `DEV_NOTES hits` as `_None_` for the row proper [Germanic/docs/lexeme_reports/packets/2202-span-spannan.md:48-60]. Broader `span` searches do recover DEV_NOTES material, but all of it turns out to be about the separate feminine ō-stem noun row now represented by `spanne`, plus generic project-history logging for that noun fix [Germanic/docs/DEV_NOTES.md:10394-10394,13645-14040,28072-28124]. This slice therefore has to function as a replacement working note: the live TSV row, the packet, the research memo, and local reference works carry the present argument more reliably than any row-2202 DEV_NOTES section does.

The present row itself is straightforward. Kroonen gives Proto-Germanic `*spannan-` and explicitly lists OE `spannan` among the reflexes [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:24007-24015; @Kroonen2013, p. 465]. Clark Hall keeps the noun and verb apart in exactly the way the row now needs: `spann I. f. 'span' (measure)` and separate `spannan "to join, link, clasp, fasten, attach"` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:37372-37376; @ClarkHall1960]. Brunner likewise indexes `sponnan, spannan stv.` and notes a later present `spannan`, so the repository's class-VII-infinitive reading is philologically ordinary rather than a special rescue analysis [docs/references/brunner_1965_altenglische_grammatik.vision.txt:15982-15984,16204-16207,28062-28065; @SieversBrunner1965, §392 Anm. 4; @SieversBrunner1965, §396.1].

What *is* row-local here is the documentation problem. The live note still says `spann→spannan`, which is useful only as shorthand for “this row is the verb, not the noun,” but it can be misread as if the row once genuinely targeted `spann`. The research memo already isolates the real issue: “The live derivation is not the problem here: `*spánnaną -> spannan` already works and the row remains correctly labelled `regular`. The real project problem is **documentation drift**” [Germanic/docs/lexeme_reports/research_memos/2202-span-spannan.md:56-64]. The same memo therefore recommends keeping row 2202 as the regular infinitive mapping while tightening the note so it distinguishes the verb from noun row 2203 without repeating stale noun-target wording [Germanic/docs/lexeme_reports/research_memos/2202-span-spannan.md:60-64,76-84].

That distinction also has to remain explicit at the notation level. For row 2202, `PROTO = *spánnaną` is the verbal cognate-set headword, `PROTOFORM = *spánnaną` is the row's actual derivational input, and `COUNTERPART = spannan` is the OE infinitive target [Germanic/data/germanic-aligned-final.tsv:1055-1055]. By contrast, the surviving DEV_NOTES `span` material is about a different lexeme and a different cell: the noun row's dative singular `*spannai/*spánnai → spanne`, discussed under the NWGmc treatment of unstressed word-final `*ai` [Germanic/docs/DEV_NOTES.md:13850-14040,28072-28124; @RingeTaylor2014, §6.1.5]. Nothing in the current evidence supports importing that noun-row paradigm-cell machinery into row 2202.

For later report work, the safest concise formulation is therefore: regular comparator `*spánnaną`, regular OE infinitive target `spannan`, stale note shorthand `spann→spannan`, and separate noun history confined to row 2203 `spanne`. On present evidence this row should remain a **no-index** slice, not because the verbal analysis is weak, but because the surviving DEV_NOTES prose is either absent for the verb or shared noun-row history that should not be indexed as if it were row-2202 authority [Germanic/docs/lexeme_reports/packets/2202-span-spannan.md:48-60; Germanic/docs/DEV_NOTES.md:13807-14040,28072-28124].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-10394-10394

- Source heading: `Mismatch Progress Log (2026-04-05)`
- Source line or section hint: `line 10394`
- Status: `diagnostic_only`
- Issue tags: `project_history`; `shared_span_material`; `noun_row_2203`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2203`

This is only a chronology marker: `span fix (feminine ō-stem dat.sg.)` [Germanic/docs/DEV_NOTES.md:10394-10394]. It is useful for showing when the noun-row repair landed, but it does not discuss `*spánnaną`, `spannan`, or any verbal class-VII problem. For row 2202 it should stay diagnostic only.

### DEV_NOTES:line-13645-13800

- Source heading: `Paradigm-cell approach for geminate-stem words`
- Source line or section hint: `lines 13645-13800`
- Status: `diagnostic_only`
- Issue tags: `geminate_background`; `shared_span_material`; `noun_row_2203`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2203`

This background note explains why older project history grouped `span` with other geminate problems. It states that if universal word-final degemination is modelled, targets like `mann`, `bann`, `spann` become “orthographic mismatches,” and it proposes paradigm-cell matching for nouns with medial geminates [Germanic/docs/DEV_NOTES.md:13605-13622,13663-13725]. The row table inside the same fragment lists `2203 | span | *spannō | span | spann | word-final degemination`, then immediately says: “For span (fem. ō-stem), different paradigm — investigate separately” [Germanic/docs/DEV_NOTES.md:13786-13800]. That is useful shared background for understanding why the old row-2202 note mentioned noun `spann`, but it is not evidence that row 2202 itself ever needed a verbal paradigm-cell workaround.

### DEV_NOTES:line-13807-14040

- Source heading: `Fem. ō-stem gen.sg. paradigm-cell for span (2026-04-06)`
- Source line or section hint: `lines 13807-14040`
- Status: `diagnostic_only`
- Issue tags: `noun_row_solution`; `shared_span_material`; `paradigm_cell`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2203`

This is the main surviving `span` DEV_NOTES discussion, and it is explicitly about the noun row, not the verb. It opens: “For `*spannō → span` (expected `spann`), we want to use a paradigm-cell approach similar to what we did for masc. a-stems” [Germanic/docs/DEV_NOTES.md:13811-13812]. The note then rejects the gen.sg. route for fem. ō-stems, proposes the dative singular instead, and states: “Use `*spannai → spanne` for the paradigm-cell mapping” [Germanic/docs/DEV_NOTES.md:13850-13866]. The later implementation block confirms that the target under discussion is noun `spanne`, not verbal `spannan`: “Updated TSV row 2203 (span): Proto: `*spannăi` ... Target: `spanne`” [Germanic/docs/DEV_NOTES.md:14032-14039]. For row 2202 the fragment matters only as evidence that shared `span` history has to be filtered carefully.

### DEV_NOTES:line-28072-28124

- Source heading: `§17.12.1-4 word-final *ai / spanne verification`
- Source line or section hint: `lines 28072-28124`
- Status: `diagnostic_only`
- Issue tags: `later_correction`; `noun_row_solution`; `shared_span_material`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2203`

This later correction still concerns the noun-row `spanne` solution only. It says: “Only one TSV form carries this marker: row 1057 `*spánnăi` (OE dat.sg. `spanne`). No other form in the corpus has a word-final `*ai` at any point in the cascade” [Germanic/docs/DEV_NOTES.md:28072-28074]. The implementation then removes the breve notation and verifies `*spánnai → spanne` [Germanic/docs/DEV_NOTES.md:28097-28124]. Even the stale row number inside the fragment is a reminder that this is project-history residue around the noun repair, not stable authority for the verb row.

## Superseded or diagnostic material

The main row-local diagnostic artifact is the TSV note itself. `OE target: spann→spannan` should not be read as a real derivational sequence inside the live pipeline or as a sign that the row currently wavers between noun and verb targets. The actual derivation is already exact from `*spánnaną` to `spannan` [Germanic/data/germanic-aligned-final.tsv:1055-1055; Germanic/docs/lexeme_reports/packets/2202-span-spannan.md:17-42].

The other diagnostic trap is noun-shaped lexical noise. The packet's only local lexical-table hit is `span | spann`, and the research memo correctly warns that this is “noun/citation-form orientation only, not evidence that the verbal target here should be `spann`” [Germanic/docs/lexeme_reports/packets/2202-span-spannan.md:66-73; Germanic/docs/lexeme_reports/research_memos/2202-span-spannan.md:18-20,50-54]. Clark Hall's separate entries for noun `spann` and verb `spannan` are the safer guide [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:37372-37376; @ClarkHall1960].

No superseded verbal `PROTOFORM` is actually preserved for row 2202. Forms such as `*spannai`, `*spannăi`, or `*spánnai` belong to the noun-row `spanne` history summarized above, not to this verbal infinitive row [Germanic/docs/DEV_NOTES.md:13850-14040,28097-28124].

## Open questions for later work

- If the TSV note is revised in a future task, the safest wording should name `spannan` directly as the OE infinitive and say only that row 2202 is distinct from noun row 2203 `spanne`.
- If a later final report wants one concise external citation for the distinction, Clark Hall is the clearest local source because it gives both noun `spann` and verb `spannan` side by side [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:37372-37376; @ClarkHall1960].
- `index.tsv` should remain untouched for now. Row 2202 has a stable analysis, but the surviving DEV_NOTES material is either absent for the verb or shared noun-row history, so there is still no clean row-2202 fragment worth indexing as current authority.

---
row_id: 2214
concept: starve
counterpart: steorfan
proto: *stérbaną
protoform: *stérbaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2214 starve / steorfan

## Current row state

- Live `Germanic/data/germanic-aligned-final.tsv` line `1102` gives row `2214` as `CONCEPT starve`, `COUNTERPART steorfan`, `PROTO *stérbaną`, `PROTOFORM *stérbaną`, and `DERIVATION_CLASS regular`; the row has no row-local explanatory note beyond duplicated Wiktionary inheritance provenance [Germanic/data/germanic-aligned-final.tsv:1102-1102].
- For this row, `PROTO` and `PROTOFORM` are currently the same string, but they still do different jobs: `PROTO` is the comparative cognate-set headword `*stérbaną`, while `PROTOFORM` is the specific FST input the OE derivation consumes. The `COUNTERPART` is the infinitive `steorfan`, not a finite present form or a prefixed derivative [Germanic/data/germanic-aligned-final.tsv:1102-1102].
- `Germanic/data/old_english_wiktionary.tsv` independently aligns English `starve` with OE `steorfan`, so the lexical-source layer agrees with the live row's present target [Germanic/data/old_english_wiktionary.tsv:274-274].
- `Germanic/data/oe_known_problems.tsv` has no entry for row `2214`, `steorfan`, or `*stérbaną`, which fits the row's current `regular` classification but does not itself supply any philological argument [Germanic/data/oe_known_problems.tsv:1-8].
- `Germanic/docs/lexeme_reports/coverage_audit.md` lists row `2214` with packet, memo, and report coverage all `none`, so no reusable packet or research-memo stem was available and the canonical row-based filename is appropriate here [Germanic/docs/lexeme_reports/coverage_audit.md:369-369].
- The published OE derivation trace is an exact match: `PROTO: *stérbaną`, `EXPECTED: steorfan`, `OUTPUTS: steorfan`. The trace shows ordinary OE breaking plus routine later clean-up, not a bespoke exception path: `OE Breaking: *stéorbaną`, then `OE Heavy Syllable Nasal Apocope`, `OE Secondary Nasalization`, `PGmc B Allophony`, and `OE Weak Tail Reduction`, ending in surface `steorfan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4646-4665].

## Detailed development-note summary

Direct DEV_NOTES support for row `2214` is effectively absent. No surviving DEV_NOTES passage currently discusses `steorfan` as a problem row, proposes a different OE target, or records any special repair to `*stérbaną`. The replacement working note therefore has to preserve the absence itself: the live TSV row is regular, the derivation trace already lands exactly on `steorfan`, and there is no surviving DEV_NOTES dossier that overrides that state [Germanic/data/germanic-aligned-final.tsv:1102-1102; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4646-4665].

The comparative evidence that does survive outside DEV_NOTES is straightforward and consistent with the live row. Kroonen's entry reads: `*sterban- s.v. 'to become stiff, die' OE steorfan s.v. 'to die' ... Du. sterven ... OHG sterban ... G sterben` [@Kroonen2013, p. 477]. Orel likewise has: `*sterbanan str.vb.: OE steorfan 'to die', OFris sterva id., OS sterban id., OHG sterban id.` [@Orel2003, p. 375]. Clark Hall's dictionary gives the ordinary OE verbal entry `steorfan³ to die, H. ['starve"]` [@ClarkHall1960, p. 291]. Those citations do not create a DEV_NOTES argument that is no longer present, but they do confirm that the live row's `PROTO = *stérbaną`, `PROTOFORM = *stérbaną`, and `COUNTERPART = steorfan` are philologically ordinary rather than ad hoc.

The phonological path is also ordinary. Campbell states that `e is broken to eo with very great regularity ... before x and r followed by a consonant`, citing forms such as `weorpan` and `weorðan` [@Campbell1959, §146]. The derivation trace's `*stéorbaną` stage fits that same breaking environment before `rb`, so the row's `steorfan` outcome is exactly what the regular OE pipeline should produce from `*stérbaną` [@Campbell1959, §146; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4655-4659]. Campbell also lists `steorfan die` among the verbs similar to `weorpan`, i.e. among the regular class-III broken-vowel comparators rather than among exceptional repairs [@Campbell1959, §741].

The present project conclusion should therefore stay conservative. This row now has a usable replacement working note, but it is still thin as DEV_NOTES slicing evidence. The note to preserve is not “DEV_NOTES solved a starve-specific problem”; it is “no starve-specific DEV_NOTES problem currently survives, and every live comparative signal still supports the regular row.” That makes the row stable enough to keep as `regular`, but still too weakly documented to justify aggressive indexing from DEV_NOTES alone.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-39913-39915

- Source heading: `shoulder diagnosis false-positive search hit`
- Source line or section hint: `lines 39913-39915`
- Fragment type: `diagnostic_only_search_trap`
- Status: `diagnostic_only`
- Issue tags: `false_positive`; `not_row_local`; `do_not_index`
- Recommended next use: `use_as_project_history_only`

This is the only literal `starves` hit found in the live DEV_NOTES file, and it is **not** evidence for row `2214`. The sentence belongs to a shoulder-row diagnosis: `The R/T reconstruction *skuldru (high-vowel suffix) starves NWGmcULowering of its trigger ...` [Germanic/docs/DEV_NOTES.md:39913-39915]. Its value for row `2214` is purely diagnostic: a plain-text search for English `starve` currently lands on an unrelated analytic verb in another lexeme's prose, not on a `steorfan` note. This fragment should not be indexed as row-local support.

No additional line-based `steorfan` or `*stérbaną` fragment survives in the current DEV_NOTES file. That absence is the main row-specific DEV_NOTES fact this slice needs to preserve: there is no surviving project-historical note that changes the live regular analysis, and no fragment rich enough to warrant index attachment on its own.

## Superseded or diagnostic material

- No superseded row-local target survives in DEV_NOTES for this lexeme. There is no preserved proposal that row `2214` should target anything other than `steorfan`, and no surviving note that distinguishes a different `PROTOFORM` from the present `PROTO` string.
- The only DEV_NOTES material recovered in this pass is diagnostic-only false-positive material from another lexeme's discussion, so later work should resist treating a successful plain-text `starve` search as evidence that row `2214` has genuine DEV_NOTES coverage [Germanic/docs/DEV_NOTES.md:39913-39915].
- The substantive support presently comes from the live row, the exact derivation trace, and ordinary reference works rather than from DEV_NOTES chronology. That is enough to keep the row regular, but it is not the same thing as having a row-specific memo or note dossier [@Kroonen2013, p. 477; @Orel2003, p. 375; @ClarkHall1960, p. 291; @Campbell1959, §§146, 741].

## Open questions for later work

- If the row is ever to become cleanly indexable from DEV_NOTES infrastructure, it will probably need a genuine row-local packet, memo, or later literature note; the current slice mainly records the absence of such material.
- A later report pass could add fuller strong-verb paradigm evidence for `steorfan` if needed, but nothing in the current live material suggests any need to retarget the row or change its derivation class.
- If broader lexeme-report work later wants a richer philological note, the most useful next citations would probably be a fuller class-III strong-verb discussion and direct dictionary attestational evidence, not another DEV_NOTES search.

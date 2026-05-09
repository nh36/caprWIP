---
row_id: 2196
concept: sleep
counterpart: slǣpan
proto: *slḗpaną
protoform: *slḗpaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2196-sleep-slǣpan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2196-sleep-slǣpan.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2196 sleep / slǣpan

## Current row state

- The live OE row reads `CONCEPT = sleep`, `COUNTERPART = slǣpan`, `PROTO = *slḗpaną`, `PROTOFORM = *slḗpaną`, `DERIVATION_CLASS = regular`, with TSV note `OE target: slǣp→slǣpan (inf. of str.v. class VII 'to sleep')` [Germanic/data/germanic-aligned-final.tsv:1031-1031].
- `PROTO` and `PROTOFORM` are identical in the live TSV, so the row is not currently using a substitute paradigm cell, an OE-stage rescue form, or a distinct editorial `PROTOFORM` layer. The stored project input is the infinitive-shaped PGmc form `*slḗpaną`; the attested OE target represented by the row is the infinitive `slǣpan`, not the noun/headword string `slǣp` embedded in the note shorthand [Germanic/data/germanic-aligned-final.tsv:1031-1031].
- `oe_known_problems.tsv` contains no row-local entry for `2196`, `sleep`, `slǣpan`, or `*slḗpaną`; the ledger currently lists unrelated exception and wontfix items only [Germanic/data/oe_known_problems.tsv:1-8].
- `coverage_audit.md` still flags the row as needing coverage because of its non-empty TSV note: `| 2196 | sleep | slǣpan | regular | yes | - | - | - | NOTE |` [Germanic/docs/lexeme_reports/coverage_audit.md:135-135].
- The published derivation traces are exact matches. The compact report gives `PROTO: *slḗpaną`, `EXPECTED: slǣpan`, `OUTPUTS: slǣpan`, with the active developments `NWGmc Long E Lowering: *slǣpaną`, `OE Heavy Syllable Nasal Apocope: *slǣpan`, `OE Secondary Nasalization: *slǣpąn`, and `OE Weak Tail Reduction: *slǣpan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4346-4359]. The full trace shows the same row in expanded rule order and surfaces `slǣpan` without any special repair stage [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29467-29504,29530-29531,29561-29580].
- Local reference works support the verbal target and keep the paradigm distinct from noun or preterite material. Clark Hall gives `slæpan ... pret. 3 sg. slēp, slēap` and cross-references `slēpan`; Bright lists `slæpan (slāpan), slēp slēpon slēpen`; Brunner treats West Saxon `slāpan/slæpan` beside Anglian/Kentish `slēpan`; Bülbring likewise contrasts `slāpan` with analogical `slæpan`; Kroonen gives comparative PGmc `*slēpan-`; Fulk cites root `*slēb-` behind `Go. slēpan, OE slæpan, OS slāpan, OHG slāfan` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:36698-36699,36877-36879; @ClarkHall1960; docs/references/bright_anglo_saxon_reader.vision.txt:25046-25050; @BrightCassidyRingler1971; docs/references/brunner_1965_altenglische_grammatik.vision.txt:16172-16185,27872-27894; @SieversBrunner1965; docs/references/bulbring_altenglisches_elementarbuch.txt:3066-3067,14431-14432; @Bulbring1902; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23445-23447; @Kroonen2013; docs/references/fulk_comparative_grammar_early_germanic.vision.txt:6397-6398,16316-16316; @Fulk2018].

## Development-note summary

No attachable row-specific DEV_NOTES fragment currently survives for row `2196`. Searchable DEV_NOTES material does **not** preserve a `sleep / slǣpan / *slḗpaną` problem note, a target-correction narrative, or a paradigm-cell workaround. The only literal sleep-adjacent DEV_NOTES hit recovered during slice preparation is an A-restoration source quotation listing unrelated `*hnappian* fall asleep` among example words; that passage concerns a different lexeme and different phenomenon and cannot be used as row authority for `slǣpan` [Germanic/docs/DEV_NOTES.md:30391-30402]. This slice is therefore a replacement working note built from the live row state, the current trace, and local reference works, not a compression of an existing DEV_NOTES dossier.

The most important distinction to preserve is between three different layers that the surviving repo material can blur. First, the live project input is `PROTO = PROTOFORM = *slḗpaną`, written in the repository's current accented PGmc infinitive notation [Germanic/data/germanic-aligned-final.tsv:1031-1031]. Second, comparative reference works often cite the same lexeme as dictionary headword `*slēpan-` or root `*slēb-`; those are comparative notation/stage labels, not rival live-row policies [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23445-23447; @Kroonen2013; docs/references/fulk_comparative_grammar_early_germanic.vision.txt:6397-6398; @Fulk2018]. Third, the OE target is the verbal infinitive `slǣpan`, with dialectal/headword variants such as `slæpan`, `slāpan`, and `slēpan` in the local handbooks [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:36698-36699,36877-36879; @ClarkHall1960; docs/references/brunner_1965_altenglische_grammatik.vision.txt:16172-16185,27872-27894; @SieversBrunner1965]. Nothing in the surviving evidence suggests that `PROTO` and `PROTOFORM` should diverge or that the row should be retargeted to a different paradigm cell.

The live derivation is fully regular and should be spelled out explicitly because there is no DEV_NOTES narrative to do it elsewhere. The full trace shows unchanged passage through Proto-Germanic and Proto-West-Germanic stages, then `NWGmcLongELowering: *s*l*ǣ*p*a*n*ą`, then the ordinary OE tail steps `OEHeavySyllableNasalApocope`, `OESecondaryNasalization`, and `OEWeakTailReduction`, finally `OldEnglishRemoveStars: slǣpan` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29468-29504,29530-29531,29561-29580]. That matters because it confirms that row `2196` is not an exception currently hidden by a note: the present pipeline already derives the infinitive exactly, and `oe_known_problems.tsv` does not reserve the lexeme as a known unresolved case [Germanic/data/oe_known_problems.tsv:1-8].

The real surviving problem is lexical framing, not phonology. The TSV note's `slǣp→slǣpan` shorthand and the local lexical tables can tempt later writers to collapse the verb with a noun/headword lookup. `source_inventory.md` explicitly warns that `old_english_wiktionary.tsv` is only a supplementary lookup table and that `old_english_swadesh.tsv` is low-authority lexical support, while local reference texts in `docs/references/` are the primary external evidence base [Germanic/docs/lexeme_reports/source_inventory.md:25-39,108-117,186-186]. That ranking matters here because the supplementary tables split: Wiktionary gives `sleep -> slǣp`, while Swadesh gives `to sleep -> slǣpan` [Germanic/data/old_english_wiktionary.tsv:257-257; Germanic/data/old_english_swadesh.tsv:108-108]. The handbooks resolve the ambiguity in favor of the verb: Clark Hall and Bright cite the infinitive `slæpan/slǣpan`, while `slēp` and `slēap` are preterite forms and `slǣp` is a separate noun/headword string, not the verbal citation form [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:36698-36699,36806-36806,36877-36879; @ClarkHall1960; docs/references/bright_anglo_saxon_reader.vision.txt:25046-25050; @BrightCassidyRingler1971].

Because the surviving DEV_NOTES evidence is absent rather than merely terse, this row presently belongs in the no-index category. There is enough evidence to justify the live row and to explain why the note shorthand is misleading, but there is no reusable DEV_NOTES fragment to index. If the row is indexed later, that should follow a future DEV_NOTES entry or some other explicitly citable internal rationale text, not this absence case.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-30391-30402

- Source heading: `§158 (the consonant-environment statement — the relevant statement, ref. line 4727ff.)`
- Source line or section hint: `lines 30391-30402`
- Fragment type: `unrelated_search_hit`
- Status: `not_row_relevant`
- Issue tags: `search_negative`; `unrelated_lexeme`; `no_row_specific_note`
- Recommended next use: `do_not_index`
- Shared with row IDs:

This is the only sleep-adjacent DEV_NOTES text recovered during slice preparation, and it is not usable row evidence. The passage is a quoted A-restoration example list ending with `*hnappian* fall asleep`, alongside unrelated forms such as `*faran*`, `*bacan*`, `*crabba*`, and `*racca*` [Germanic/docs/DEV_NOTES.md:30393-30398]. It says nothing about row `2196`, nothing about `slǣpan`, nothing about class-VII ablaut, and nothing about a `PROTO`/`PROTOFORM` distinction. Its only value here is negative: it confirms that literal overlap with the English gloss `sleep` exists in DEV_NOTES, but only in an unrelated quotation block, so there is still no attachable DEV_NOTES fragment for the row itself.

## Superseded or diagnostic material

The main diagnostic material is the row note itself. `OE target: slǣp→slǣpan` should not be read as a real derivational sequence from an OE noun to an OE infinitive or as evidence that the live row once targeted `slǣp`; it is compressed shorthand that blurs lemma type, paradigm cell, and row target [Germanic/data/germanic-aligned-final.tsv:1031-1031]. The current exact-match trace shows that the row actually derives straight from PGmc `*slḗpaną` to OE `slǣpan`, with no intermediate OE `slǣp` stage in the pipeline [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29468-29504,29530-29531,29561-29580].

The low-authority lexical-table split is also diagnostic rather than policy-setting. `old_english_wiktionary.tsv` gives `sleep -> slǣp`, while `old_english_swadesh.tsv` gives `to sleep -> slǣpan`; source-inventory policy explicitly says those tables are supplementary only and must not outrank better local reference works [Germanic/data/old_english_wiktionary.tsv:257-257; Germanic/data/old_english_swadesh.tsv:108-108; Germanic/docs/lexeme_reports/source_inventory.md:37-39,108-117,186-186]. For this row the dictionaries/readers are decisive: `slæpan/slǣpan/slēpan` is the verb; `slēp/slēap` are preterite forms; `slǣp/slæp` is separate noun/headword material [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:36698-36699,36751-36757,36806-36806,36877-36879; @ClarkHall1960; docs/references/bright_anglo_saxon_reader.vision.txt:25044-25050; @BrightCassidyRingler1971].

There is no preserved superseded project-state note comparable to rows where DEV_NOTES logs a former mismatch, wrong target, or abandoned paradigm-cell rescue. The absence itself is the point: the row looks stable in the live system, but the internal rationale never received a dedicated DEV_NOTES write-up.

## Open questions for later work

- If the TSV note is ever revised in a future task, the safest wording should name the OE target directly as the infinitive `slǣpan` and avoid `slǣp→slǣpan` shorthand, which currently invites confusion between the verb and noun/headword noise [Germanic/data/germanic-aligned-final.tsv:1031-1031; Germanic/data/old_english_wiktionary.tsv:257-257; Germanic/data/old_english_swadesh.tsv:108-108].
- If a later internal note is added, it should keep the notation layers explicit: live project input `*slḗpaną`, comparative headword/root notation `*slēpan-` / `*slēb-`, and OE target `slǣpan` [Germanic/data/germanic-aligned-final.tsv:1031-1031; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23445-23447; @Kroonen2013; docs/references/fulk_comparative_grammar_early_germanic.vision.txt:6397-6398; @Fulk2018].
- `index.tsv` should remain untouched for now. Until there is a real attachable DEV_NOTES fragment, row `2196` is better treated as a no-index slice whose purpose is to preserve the current evidence bundle and the warning about misleading `slǣp` shorthand.

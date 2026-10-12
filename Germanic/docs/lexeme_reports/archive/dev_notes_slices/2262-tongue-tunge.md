---
row_id: 2262
concept: tongue
counterpart: tunge
proto: "*túngōn"
protoform: "*túngōn"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2262 tongue / tunge

## Current row state

- The live OE row gives `CONCEPT = tongue`, `COUNTERPART = tunge`, `PROTO = *túngōn`, `PROTOFORM = *túngōn`, and `DERIVATION_CLASS = regular`, with only source-provenance material in the `NOTE` field rather than a project-authored lexical warning or exception note [Germanic/data/germanic-aligned-final.tsv:1288-1288].
- `PROTO` and `PROTOFORM` are **not** split in the current row, but they still name different roles. `PROTO` is the comparative proto headword used for the cognate set, `PROTOFORM` is the OE-facing derivational input the project is testing, and `COUNTERPART` is the attested OE output `tunge` [Germanic/data/germanic-aligned-final.tsv:1288-1288]. The fact that both proto fields currently contain the same string should not be mistaken for a collapse of those roles.
- The row's provenance is thin but consistent: `old_english_wiktionary.tsv` records `tongue / tunge` as an inherited item (`template:inh`), matching the TSV note's duplicated Wiktionary sourcing [Germanic/data/old_english_wiktionary.tsv:321-321; Germanic/data/germanic-aligned-final.tsv:1288-1288].
- `coverage_audit.md` still lists row `2262` with `packet no`, `memo -`, `report -`, and `links none`, so there is no existing row-specific packet, research memo, pilot report, or clearly row-local analysis file to reuse here [Germanic/docs/lexeme_reports/coverage_audit.md:398-398].
- The current derivation harness already produces the expected OE form from the row's input: the compact trace snapshot shows `PROTO: *túngōn`, `EXPECTED: tunge`, `OUTPUTS: tunge`, with the path `NWGmc N Stem N Loss: *túngǭ` then `OE Unstressed Long Vowel Shortening: *túngæ` and `OE Unstressed AE Merger: *túnge` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:6338-6356].

## Detailed development-note summary

This row is one of the clearest examples of a regular OE weak-feminine outcome in the surviving development notes, but the evidence is still mostly **shared infrastructure** rather than a tongue-only dossier. `DEV_NOTES.md` repeatedly uses `tunge` as the example for how feminine n-stem nominative singular `*-ōn` ends up as OE `-e`; the file does **not** preserve a separate row-specific dispute over analogical repair, paradigm-cell substitution, or a competing proto input [Germanic/docs/DEV_NOTES.md:2726-2739,3580-3583,20490-20520,23682-23690].

The central derivational claim is stated explicitly and should be preserved verbatim because later rows in the same class depend on it. DEV_NOTES gives the chain `fem. n-stem nom.sg. *tungōn → *tungō̃ (after n-loss, nasalized) → PWGmc *tunga → OE tunge`, then immediately explains the implementation policy: `For fem. n-stems, modelled by NWGmcNStemNLoss: {*ō}{*n} → {*ǭ} word-finally, then {*ǭ} → {*æ} → OE -e` [Germanic/docs/DEV_NOTES.md:2734-2739]. That is the repository's clearest statement of why row `2262` is still classed `regular`: the OE output is supposed to fall out of the ordinary weak-noun pipeline, not from a lexeme-specific override.

The distinction among the row fields remains important even though the live row happens to show the same string in both proto fields. `PROTO = *túngōn` is the row's comparative etymological label; `PROTOFORM = *túngōn` is the same lexical item considered as the project's OE-facing input; `COUNTERPART = tunge` is the attested Old English target [Germanic/data/germanic-aligned-final.tsv:1288-1288]. DEV_NOTES usually writes the proto stage without an acute, as `*tungōn`, and sometimes refers instead to the post-n-loss stage `PWGmc *tunga` [Germanic/docs/DEV_NOTES.md:2734-2735,23688-23690]. For this slice, the conservative reading is that these are notation/staging differences inside one derivational account, not evidence that the live row should split `PROTO` from `PROTOFORM` or abandon the current target.

The supporting handbook citations are unusually strong for such a short row. DEV_NOTES quotes Campbell §331.5: `But in all areas *ō > *a when a nasal had followed, e.g. OE a.s. giefe < *-æ < *-a < *-ōm, and so n.s.f. of weak nouns, tunge < *-ōn. This indicates that at the time of shortening the vowel was nasalized by influence of the lost nasal` [Germanic/docs/DEV_NOTES.md:20509-20514; docs/references/campbell_old_english_grammar.txt:9279-9284; @Campbell1959, §331.5]. It then quotes Campbell §333: `Except before nasals, unaccented *a > *æ (later e, §369), e.g. n.s.f. and n. of weak nouns, OE tunge, éage` [Germanic/docs/DEV_NOTES.md:20516-20520,20718-20725; docs/references/campbell_old_english_grammar.txt:9387-9390; @Campbell1959, §333]. Those are exactly the two phonological steps the row needs: early shortening in the nasal environment, then ordinary fronting of unstressed `a` to `æ > e` once the nasal is gone.

Ringe-Taylor is used in DEV_NOTES the same way: not as a row-specific tongue essay, but as confirmation that this ending type is being treated as fully regular. DEV_NOTES summarizes their position as the same paragraph that derives `a-stem dat.sg. -e < PWGmc *-ē` and `fem. n-stem nom.sg. tunge < PWGmc *tunga`, then concludes: `R/T treat all three as lautgesetzlich outcomes` [Germanic/docs/DEV_NOTES.md:23685-23690; @RingeTaylor2014, §6.8.3]. The OCR reference file preserves the same comparative claim in nearly lexical form: `PNWGmc nom. sg. *tung@ 'tongue' ... > PWGmc *tunga ... > OE tunge` and later `fem., neut. n-stem nom. sg. -e < ... PWGmc *-a, e.g. in tunge 'tongue'` [docs/references/ringe_taylor_linguistic_history_vol2.txt:4064-4067,17235-17237]. For this row, that matters because it shows the project is not depending only on an internal implementation note.

There is also a concise sanity-check table in DEV_NOTES that names the lexeme directly. In the mora-class comparison table, `*tungōn (fem. n-stem)` is assigned the pipeline `NWGmcNStemNLoss: {*ō}{*n}→{*ǭ}; shortening → {*æ} → -e`, with OE output `tunge` and a correctness mark `✓` [Germanic/docs/DEV_NOTES.md:3578-3583]. This passage is not richer than the main derivational note, but it is useful because it shows the project has already checked `tunge` against the same mora-sensitive framework used for other final-vowel problems.

The one later DEV_NOTES passage that names `tunge` again is incidental but still worth keeping. Inside the `tang/tange` discussion, DEV_NOTES says that a weak `ōn`-stem nominative singular would yield OE `-e`, `like *tunge* < *tungōn-, *sunne* < *sunnōn-` [Germanic/docs/DEV_NOTES.md:32289-32295]. That is not dedicated row-2262 analysis, but it is still a direct, explicit statement that the repository continues to treat `tunge` as the textbook weak-feminine reflex of `*tungōn-`.

Overall, the row looks stable. The documentary weakness is not that the derivation is doubtful; it is that most of the evidence is shared class evidence reused across many weak feminine rows. For future work, this slice should therefore function as the row's replacement working note: regular feminine n-stem, no live `PROTO/PROTOFORM` split despite the conceptual distinction, no sign of an exception bucket, and strong handbook support for the ordinary `*-ōn > -e` development [Germanic/data/germanic-aligned-final.tsv:1288-1288; Germanic/docs/DEV_NOTES.md:2726-2739,23682-23690; @Campbell1959, §§331.5, 333; @RingeTaylor2014, §6.8.3].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2726-2739

- Source heading: `final long ō outcomes; shared feminine n-stem derivation note`
- Source line or section hint: `lines 2726-2739`
- Fragment type: `shared_sound_change_support`
- Status: `current_but_shared`
- Issue tags: `feminine_n_stem`; `final_ōn`; `n_loss`; `regular_oe_e`
- Recommended next use: `primary_index_anchor_if_any`
- Shared with row IDs: `2231`; other weak feminine rows in `*-ōn`

This is the strongest surviving DEV_NOTES anchor for row `2262`. It gives the lexeme itself as the worked example: `fem. n-stem nom.sg. *tungōn → *tungō̃ (after n-loss, nasalized) → PWGmc *tunga → OE tunge`, then states the exact FST abstraction `NWGmcNStemNLoss: {*ō}{*n} → {*ǭ} ... then {*ǭ} → {*æ} → OE -e` [Germanic/docs/DEV_NOTES.md:2734-2739]. The fragment is shared rather than row-local, but unlike many shared notes it names the lexeme directly and provides both the historical claim and the current implementation path. It is the best candidate if the row is ever indexed from DEV_NOTES material.

### DEV_NOTES:line-3578-3583

- Source heading: `mora-class comparison table`
- Source line or section hint: `lines 3578-3583`
- Fragment type: `pipeline_sanity_check`
- Status: `current`
- Issue tags: `bimoraic_ōn`; `table_check`; `tunge_example`
- Recommended next use: `cite_as_compact_confirmation`
- Shared with row IDs: rows discussed in the same final-vowel table

This table row is compact but useful because it checks exactly the item at issue: `*tungōn (fem. n-stem) | Bimoraic *-ōn | NWGmcNStemNLoss ... | tunge | ✓` [Germanic/docs/DEV_NOTES.md:3583-3583]. Unlike the prose note, it makes the mora assignment explicit and shows that the project considered the outcome correct under the final-vowel framework. It should not replace the fuller 2726-2739 fragment, but it is a good corroborating citation when later notes need a one-line confirmation.

### DEV_NOTES:line-20490-20520

- Source heading: `Campbell-based early shortening and fronting note`
- Source line or section hint: `lines 20490-20520`
- Fragment type: `source_quote_with_project_gloss`
- Status: `current`
- Issue tags: `Campbell`; `early_shortening`; `nasal_context`; `unstressed_fronting`
- Recommended next use: `cite_for_phonological_justification`
- Shared with row IDs: weak feminine and other unstressed-final-vowel rows

This is the strongest handbook-facing fragment because it preserves the quotations that make `tunge` a regular phonological outcome rather than merely an implementation convention. DEV_NOTES quotes Campbell §331.5 on `tunge < *-ōn` after nasal-conditioned shortening and Campbell §333 on `OE tunge, éage` after unstressed fronting [Germanic/docs/DEV_NOTES.md:20509-20520]. For row `2262`, the fragment is valuable precisely because it spells out both chronological pieces of the derivation that the live transducer trace abbreviates [docs/references/campbell_old_english_grammar.txt:9279-9284,9387-9390; @Campbell1959, §§331.5, 333].

### DEV_NOTES:line-23682-23690

- Source heading: `Ringe-Taylor on regular -e outcomes`
- Source line or section hint: `lines 23682-23690`
- Fragment type: `shared_source_claim`
- Status: `current_but_shared`
- Issue tags: `RingeTaylor`; `lautgesetzlich`; `weak_feminine_nom_sg`
- Recommended next use: `use_as_handbook_support`
- Shared with row IDs: `2231`; other rows using the same final-vowel account

This fragment matters because it records DEV_NOTES's interpretive conclusion from Ringe-Taylor: `fem. n-stem nom.sg. tunge < PWGmc *tunga` is treated in the same paragraph as other regular `-e` outcomes, and `R/T treat all three as lautgesetzlich outcomes` [Germanic/docs/DEV_NOTES.md:23688-23690]. The point is not that Ringe-Taylor provide a tongue-only discussion, but that they support the repository's classification of the row as regular rather than analogical [docs/references/ringe_taylor_linguistic_history_vol2.txt:4064-4067,17235-17237; @RingeTaylor2014, §6.8.3].

### DEV_NOTES:line-32289-32295

- Source heading: `tang/tange discussion; weak ōn-stem comparison`
- Source line or section hint: `lines 32289-32295`
- Fragment type: `direct_lexeme_mention_in_shared_note`
- Status: `current_but_incidental`
- Issue tags: `tunge_example`; `weak_ōn_stem`; `comparison_passage`
- Recommended next use: `keep_as_secondary_hook`
- Shared with row IDs: `2231`; `2261`; comparable weak-feminine comparator rows

This fragment is not row-local, but it does preserve a later direct mention of the lexeme in a way that aligns with the live row policy. DEV_NOTES says a weak `ōn`-stem hypothesis would yield OE `-e`, `like *tunge* < *tungōn-, *sunne* < *sunnōn-` [Germanic/docs/DEV_NOTES.md:32293-32294]. The value of the fragment is therefore confirmatory: long after the main final-vowel note, the project is still using `tunge` as a standard example of the regular weak-feminine outcome.

## Superseded or diagnostic material

- No row-specific superseded proposal was found for `tongue / tunge`. The surviving notes do not preserve an abandoned rival counterpart, a failed analogical fix, or a competing derivation class for this row.
- The main caution is documentary rather than phonological: most of the evidence is shared class evidence. Even the strongest fragment is a general final-vowel note that happens to use `tunge` as its flagship example, not a dedicated row-2262 mini-dossier [Germanic/docs/DEV_NOTES.md:2726-2739].
- The spelling difference between live-row `*túngōn` and DEV_NOTES's more common `*tungōn` should presently be treated conservatively as notation/stress-marking variation, not as evidence for a different lexical reconstruction or for a required `PROTO/PROTOFORM` split [Germanic/data/germanic-aligned-final.tsv:1288-1288; Germanic/docs/DEV_NOTES.md:2734-2735].
- DEV_NOTES line 2885 is mildly diagnostic but not row authority: it uses `*tungōn` only to note that root `*u` does not trigger Anglo-Frisian Brightening, so a hypothetical restoration issue does not arise here [Germanic/docs/DEV_NOTES.md:2885-2888]. That observation is compatible with the row, but it is too implementation-local to function as the main lexeme anchor.

## Open questions for later work

- If a later final report is written, add direct dictionary-entry citations for OE `tunge` rather than relying almost entirely on phonological handbook discussion plus Wiktionary provenance.
- If more weak feminine `*-ōn` rows are sliced, consider whether `tunge` should become the canonical cluster example for that entire class, since DEV_NOTES already uses it that way.
- If `index.tsv` is revisited later, keep the indexing conservative: row `2262` has strong shared support and direct lexeme mentions, but it still lacks a bespoke tongue-only dossier or memo.

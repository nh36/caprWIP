---
row_id: 2289
concept: wield
counterpart: wealdan
proto: *wáldaną
protoform: *wáldaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2289 wield / wealdan

## Current row state

- The live OE row reads `CONCEPT = wield`, `COUNTERPART = wealdan`, `PROTO = *wáldaną`, `PROTOFORM = *wáldaną`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1393-1393].
- The row's inherited source-note field is still only the duplicated placeholder `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)`; for future report work that field should be treated as a carry-over provenance marker, not as the real analytical authority for the row [Germanic/data/germanic-aligned-final.tsv:1393-1393].
- No obvious row-specific packet, research memo, pilot file, or clearly row-specific dossier/analysis file was found under the required support locations during slice preparation. This file therefore has to preserve the usable DEV_NOTES and handbook evidence directly instead of outsourcing the row history to parallel documentation.

## Development-note summary

The surviving DEV_NOTES material for row 2289 is genuine but very thin. There is no dedicated long-form row dossier for `*wáldaną > wealdan`. What survives instead are two short but still useful anchors: one comparative-source note preserving the proto lemma from Ringe-Taylor, and one later row-inventory line classifying the OE outcome simply as **breaking** [Germanic/docs/DEV_NOTES.md:7365-7366,30604-30638]. That means this slice should be conservative. It should not pretend that DEV_NOTES contains a bespoke dispute or repair sequence for `wealdan`. It does not. The row looks stable precisely because it never became a large project problem.

The basic three-way distinction is still worth spelling out. In the live row, `PROTO = *wáldaną` is the comparative proto label attached to the cognate set in the aligned TSV [Germanic/data/germanic-aligned-final.tsv:1393-1393]. `PROTOFORM = *wáldaną` is, in this row, the same string again, but now understood as the actual project input form used for derivation; there is no separate engineering surrogate, no special paradigm-cell retargeting, and no mismatch-driven respelling recorded in DEV_NOTES. `COUNTERPART = wealdan` is the Old English output selected for the row. Even where `PROTO` and `PROTOFORM` coincide orthographically, they should not be conflated with `COUNTERPART`: the first two are proto-side inputs, while `wealdan` is the OE reflex after the ordinary OE developments, above all West-Saxon breaking before `l + consonant`.

The comparative dictionaries line up cleanly enough to support that reading. DEV_NOTES preserves Ringe-Taylor's wording "`PGmc *waldaŋ 'to control, to rule'`" [Germanic/docs/DEV_NOTES.md:7365-7366; @RingeTaylor2014, p. 232]. Orel likewise gives `*walđanan` with OE `wealdan`, and Kroonen gives `*waldan-` with OE `wealdan` and Modern English `to wield` [docs/references/orel_handbook_germanic_etymology.vision.txt:48863-48868; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28877-28882; @Orel2003, s.v. *walđanan; @Kroonen2013, s.v. *waldan-]. For this row, then, the comparative side is not the unstable part: the uncertainty is not about whether the verb exists or whether OE `wealdan` belongs here, but only about how much row-specific DEV_NOTES prose was ever written down.

What little project-internal analysis survives points in one direction only. In the `*-aCl-* / *-aCr-*` cluster inventory, DEV_NOTES lists row `2289` explicitly as `*wáldaną | wealdan | breaking` [Germanic/docs/DEV_NOTES.md:30604-30638]. That line matters because it places `wealdan` in the same ordinary OE environment as rows such as `*fálθaną > fealdan`, `*xáldaną > healdan`, `*sáltą > sealt`, and `*sálbō > sealf`, all of which are treated as routine breaking outcomes rather than as special repairs [Germanic/docs/DEV_NOTES.md:30618-30623,30631-30639]. In other words, the row's current `regular` status is not a guess added in the TSV; it matches the later DEV_NOTES inventory of exactly the relevant phonological shape.

The external handbooks support that ordinary classification. Campbell's discussion of West-Saxon spellings gives the canonical `a + lC` breaking set explicitly: "`Examples in normal W-S spelling are eall all, healdan hold, healf`" [docs/references/campbell_old_english_grammar.txt:4441-4445; @Campbell1959, §§133-141]. Ringe-Taylor present the same environment in derivational form for the closely parallel verb `*haldana`: `PGmc *haldana ... > *heldan > WS, Kent. OE healdan` [docs/references/ringe_taylor_linguistic_history_vol2.txt:10729-10731; @RingeTaylor2014, §6.2]. `Wealdan` is not quoted there in the same worked line, but it belongs to the same structural class: stressed `a` before `ld` with a following non-high vowel in the infinitive tail. That is exactly the class DEV_NOTES is invoking when it tags row 2289 as `breaking`.

Because the row is so simple, it is also easy to overstate the evidence. DEV_NOTES does **not** appear to preserve a dedicated discussion of whether the acute accent in `*wáldaną` is merely project encoding, whether OE `wealdan` should be prioritized over other West-Germanic reflexes, or whether any paradigm-cell distinction was considered. Nor does the surviving note say more than "`breaking`" about the OE mechanism. Future work should therefore avoid embellishing the row into a faux controversy. The conservative claim is enough: the live row uses `*wáldaną` / `*wáldaną` as proto-side input, expects OE `wealdan` as the regular West-Saxon reflex, and the only explicit in-repo phonological label attached to that expectation is breaking before `l + consonant` [Germanic/docs/DEV_NOTES.md:30638-30638].

The old comparative-source fragment at lines `7365-7366` is also worth preserving with the right label. It is not a row policy note, but it does show that the project once audited `*waldaną` in a cluster of verbs where medial `d` could otherwise invite questions about Verner-type history. Here the note simply quotes Ringe-Taylor's proto entry and moves on [Germanic/docs/DEV_NOTES.md:7349-7367]. That makes the fragment useful background for the proto lemma, but not a sufficient anchor for `index.tsv` by itself. The stronger row-local statement remains the later inventory line `30638`.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-30604-30638

- Source heading: `Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail`
- Source line or section hint: `lines 30604-30638`
- Fragment type: `shared_row_classification_inventory`
- Status: `current`
- Issue tags: `breaking`; `row_shape`; `regular_target`; `shared_context`
- Recommended next use: `best_available_index_anchor`
- Shared with row IDs: `1975; 2025; 2077; 2118; 2166; 2167; 2289; 2297`

This is the strongest surviving DEV_NOTES anchor for row 2289 because it is the only place where the row is named directly in its later, already-classified form. The relevant line reads: `| 2289 | *wáldaną | wealdan | breaking |` [Germanic/docs/DEV_NOTES.md:30638-30638]. The surrounding inventory is also useful, not merely decorative, because it shows that the row was reviewed alongside the other `a + liquid-cluster` items and not isolated as an exception. For future work, this fragment supports only the modest but solid claim that the row belongs to the ordinary OE breaking class.

### DEV_NOTES:line-7365-7366

- Source heading: `Evidence from Ringe/Taylor vol.2`
- Source line or section hint: `lines 7365-7366`
- Fragment type: `comparative_source_preservation`
- Status: `background`
- Issue tags: `proto_lemma`; `source_quote`; `comparative_support`
- Recommended next use: `cite_as_background_only`
- Shared with row IDs: not row-specific; part of a broader source audit

This fragment is brief, but it preserves the direct comparative wording that still fits the live row: `PGmc *waldaŋ 'to control, to rule'` [Germanic/docs/DEV_NOTES.md:7365-7366]. Its value is mainly lexical and bibliographic. It confirms that the project explicitly checked the Ringe-Taylor proto entry for this verb and accepted the ordinary `*wald-` reconstruction. What it does **not** do is explain the OE reflex in any detail. For that reason it should be cited only as background support for the proto-side lemma, not as the primary row anchor.

## Superseded or diagnostic material

- No row-specific superseded implementation note was located for `*wáldaną > wealdan`. That absence is itself worth recording: unlike many more difficult rows, 2289 does not presently carry visible project archaeology involving a replaced `PROTOFORM`, a failed probe, or a withdrawn exception analysis.
- The main diagnostic risk is over-reading the row from shared evidence. Campbell's and Ringe-Taylor's examples more often illustrate the parallel verb `healdan` than `wealdan` itself [docs/references/campbell_old_english_grammar.txt:4441-4445; docs/references/ringe_taylor_linguistic_history_vol2.txt:10729-10731]. They are still relevant because the phonological shape is the same, but they should be cited as class evidence, not misquoted as direct `wealdan` quotations.
- The duplicated Wiktionary source note in the TSV should likewise be treated as inherited scaffolding, not as a substitute for the actual row analysis [Germanic/data/germanic-aligned-final.tsv:1393-1393].

## Open questions for later work

- If a later final lexeme report is written, decide whether it should quote the comparative dictionaries together (`Ringe-Taylor`, `Orel`, `Kroonen`) to make the proto/OE pairing explicit, or whether the single row-inventory anchor plus one handbook citation is enough [Germanic/docs/DEV_NOTES.md:7365-7366,30638-30638; docs/references/orel_handbook_germanic_etymology.vision.txt:48863-48868; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28877-28882].
- If indexing is reconsidered later, keep the evidence hierarchy explicit: `DEV_NOTES:line-30604-30638` is the only strong in-repo row anchor, while `DEV_NOTES:line-7365-7366` is real but background-only.
- A later cleanup could add a more direct in-repo quotation for `a + lC` breaking if one is wanted for row 2289 specifically; at present the clearest handbook wording survives outside DEV_NOTES in Campbell's `eall / healdan / healf` example set [docs/references/campbell_old_english_grammar.txt:4441-4445; @Campbell1959, §§133-141].

---
row_id: 2204
concept: spar
counterpart: spearra
proto: "*spárrô"
protoform: "*spárrô"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2204-spar-spearra.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2204-spar-spearra.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2204 spar / spearra

## Current row state

- CONCEPT: `spar` [Germanic/data/germanic-aligned-final.tsv:1062-1062]
- COUNTERPART: `spearra` [Germanic/data/germanic-aligned-final.tsv:1062-1062]
- PROTO: `*spárrô` [Germanic/data/germanic-aligned-final.tsv:1062-1062]
- PROTOFORM: `*spárrô` [Germanic/data/germanic-aligned-final.tsv:1062-1062]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:1062-1062]
- Live TSV note: `Kroonen *sparran- m. 'rafter, spar' → OE spearra m.; sperran is the verb 'to bar'` [Germanic/data/germanic-aligned-final.tsv:1062-1062]. The note already points to the main lexical-hygiene issue: Kroonen's etymological headword is the noun `*spar(r)an- m. ‘bar, beam, rafter’`, while `sperran` is a different OE verb and must not be imported into this noun row just because English glosses overlap [@Kroonen2013, p. 466].
- `oe_known_problems.tsv` currently has no entry for row `2204`, `*spárrô`, `spearra`, or the noun concept `spar`, which is consistent with the row's live regular status [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

The live row is already stable and regular: `PROTO = PROTOFORM = *spárrô`, `COUNTERPART = spearra`, and `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1062-1062]. The important distinction is not between the two row-local proto columns, which currently agree, but between those row fields and the comparative etymological headword. Kroonen's dictionary entry is `*spar(r)an- m. ‘bar, beam, rafter’`, with cognates including Old Saxon `sparro` and Old High German `sparro`; the row's OE noun belongs with that nominal set [@Kroonen2013, p. 466]. The TSV `PROTO`/`PROTOFORM` `*spárrô` should therefore be read as the project's OE-facing input form for this row, not as a claim that Kroonen's headword itself is spelled `*spárrô`. `COUNTERPART` remains the OE noun `spearra`, distinct both from the verb `sperran` and from row 2205 `sparian` [Germanic/data/germanic-aligned-final.tsv:1062-1062].

Secure DEV_NOTES support is thin but usable. The only clean current DEV_NOTES line that names this row directly is the cluster-inventory entry `| 2204 | *spárrô | spearra | breaking + geminate *rr* |` [Germanic/docs/DEV_NOTES.md:30633-30633]. That line matters because it records the current project classification explicitly: row 2204 is not being treated as an exception, a paradigm-cell workaround, or an A-restoration problem item, but as a regular breaking-conditioned row whose environment includes geminate `*rr` [Germanic/docs/DEV_NOTES.md:30604-30634]. Repo-local derivation tracing agrees, giving `*spárrô > *spærrô > *spearrô > spearra` and glossing the result as `breaking before geminate *rr* (Luick §161.2 exclusion)` [Germanic/docs/analysis/arestoration_r_l_research.md:530-531; Germanic/docs/analysis/arestoration_r_l_research.md:741-741; @Luick1914, §161.2]. Since the live TSV row still matches that pathway, there is no row-level repair to recommend.

The later DEV_NOTES stability audit supplies the other current fragment. DEV_NOTES says: `For breaking-conditioned rows (*xármaz, *márkō, *kálbaz, *fállaną* etc., 21 rows total), A-restoration is bled by breaking; unaffected.` [Germanic/docs/DEV_NOTES.md:36628-36629]. Row 2204 is not re-listed in that sentence, but the earlier inventory entry had already placed `*spárrô -> spearra` inside the same class [Germanic/docs/DEV_NOTES.md:30633-30633]. For replacement-note purposes, the practical conclusion should be stated plainly: later A-restoration cleanup is not a reason to reopen `spearra`; the row is preserved as a stable breaking-before-geminate case, in line with the cluster taxonomy invoked elsewhere in the project [Germanic/docs/DEV_NOTES.md:36561-36568; @Campbell1959, §158; @Luick1914, §161.2].

The only real row-local hazard is source contamination. DEV_NOTES also contains a later verb-only block beginning `Mismatch row: TSV 2205 *spárēną → sparian` and then listing `Dossiers: Germanic/docs/dossier-spar-2025.md, Germanic/docs/dossier-spar-apocope-2025.md` [Germanic/docs/DEV_NOTES.md:37757-37760]. The same block immediately labels itself `Authority survey for the *spar- verb`, and later says that `Two deep-research dossiers were prepared` for that verb [Germanic/docs/DEV_NOTES.md:37807-37810; Germanic/docs/DEV_NOTES.md:37852-37859]. Those lines explain why packet extraction can over-associate `spar`-named files with row 2204, but they are not current lexical evidence for the noun `spearra`. The conservative project reading is therefore: keep row 2204 as regular noun `*spárrô -> spearra`, preserve the Kroonen nominal linkage, and quarantine row-2205 verbal material as separate.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-30604-30634

- Source heading: `Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail`
- Source line or section hint: `lines 30604-30634`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `breaking`; `regular_row`; `a_restoration_scope`; `geminate_rr`; `protoform_vs_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1975,2008,2025,2077,2118,2166,2167,2271`

This is the main securely attachable DEV_NOTES fragment for row 2204. The note is an audit inventory rather than a dedicated `spearra` memorandum, but it names the row directly and preserves the core classification later work needs to keep: `| 2204 | *spárrô | spearra | breaking + geminate *rr* |` [Germanic/docs/DEV_NOTES.md:30633-30633]. In context, DEV_NOTES is reviewing which `*aCl`/`*aCr` rows might matter for an A-restoration cleanup elsewhere in the project [Germanic/docs/DEV_NOTES.md:30604-30634]. By tagging row 2204 as `breaking + geminate *rr*`, the note establishes two concrete things: the row belongs with the ordinary breaking-conditioned control set, and geminate `*rr` is part of the reason the environment is being tracked separately from single-consonant restoration cases. Later reporting should cite this fragment when it needs the project's internal classification, but should not pretend that the source preserves a longer row-2204 argument than it actually does.

### DEV_NOTES:line-36625-36629

- Source heading: `side-effect audit after the A-restoration cleanup`
- Source line or section hint: `lines 36625-36629`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `breaking`; `a_restoration`; `stability_after_fix`; `shared_row_class`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1975,2008,2025,2077,2118,2166,2167,2271`

This later audit is short, but it is the clearest surviving statement of why row 2204 stayed stable during the subsequent cleanup pass. DEV_NOTES says: `For breaking-conditioned rows (*xármaz, *márkō, *kálbaz, *fállaną* etc., 21 rows total), A-restoration is bled by breaking; unaffected.` [Germanic/docs/DEV_NOTES.md:36628-36629]. Row 2204 is attached to that generalization because the earlier inventory had already classified `*spárrô -> spearra` as a breaking-conditioned row with geminate `*rr*` [Germanic/docs/DEV_NOTES.md:30633-30633]. For replacement-note purposes, the important takeaway is procedural: later work should not reopen `spearra` as an A-restoration casualty or treat its `ea` as a regression from cleanup work, because DEV_NOTES explicitly places rows of this class outside that danger zone.

## Superseded or diagnostic material

### DEV_NOTES:line-37757-37760

- Status: `diagnostic_only`
- Why it is not current for row 2204: the note explicitly identifies `Mismatch row: TSV 2205 *spárēną -> sparian` before naming the `dossier-spar-2025.md` and `dossier-spar-apocope-2025.md` files [Germanic/docs/DEV_NOTES.md:37757-37760]. Those dossiers belong to the verb row, not to the noun `spearra`.

This fragment is still worth preserving because it explains a recurrent packet-level false positive. The English gloss `spar` lets verb-only material leak into row-2204 evidence gathering, but DEV_NOTES itself labels the block as row 2205 before any dossier is named [Germanic/docs/DEV_NOTES.md:37757-37760]. Later writers should treat that labelling as decisive and keep the verb dossiers out of the noun row's main evidence stack.

### DEV_NOTES:line-37807-37810 and DEV_NOTES:line-37852-37859

- Status: `diagnostic_only`
- Why it is not current for row 2204: the first fragment is headed `Authority survey for the *spar- verb`, and the second says `Two deep-research dossiers were prepared` for that same verb [Germanic/docs/DEV_NOTES.md:37807-37810; Germanic/docs/DEV_NOTES.md:37852-37859].

These fragments should not be silently deleted from working memory, because they document why row 2204 is vulnerable to scope bleed from nearby verbal research. Even so, they do not alter the noun row's current policy. Nothing in them challenges the live regular noun derivation `*spárrô -> spearra`; they are relevant only as a warning against conflating the noun with row 2205 `sparian`.

## Open questions for later work

- If a final lexeme report is drafted, decide whether to add one short source note explaining explicitly that Kroonen's comparative headword `*spar(r)an-` and the TSV row input `*spárrô` are compatible but not identical levels of reconstruction, so `PROTO`, `PROTOFORM`, and etymological headword do not get collapsed [Germanic/data/germanic-aligned-final.tsv:1062-1062; @Kroonen2013, p. 466].
- Decide whether any future final report needs manuscript-level OE attestation support for `spearra` beyond the current Kroonen-based etymological linkage and repo-internal derivation trace, or whether the row can remain a short regular-note item without that extra philological build-out [@Kroonen2013, p. 466; Germanic/docs/analysis/arestoration_r_l_research.md:530-531].
- If `dev_notes_slices/index.tsv` is later updated, decide conservatively whether the two shared current fragments above are strong enough to justify indexing or whether row 2204 should remain no-index until a dedicated noun-specific DEV_NOTES passage exists [Germanic/docs/DEV_NOTES.md:30604-30634; Germanic/docs/DEV_NOTES.md:36625-36629].

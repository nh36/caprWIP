---
row_id: 2140
concept: night
counterpart: niht
proto: *náxtz
protoform: *náxti
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2140-night-niht.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2140-night-niht.md
linked_dossier_or_analysis_files: Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md; Germanic/docs/analysis/cow_root_noun_investigation.md; Germanic/docs/analysis/compound_archaism_inventory.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2140 night / niht

## Current row state

- CONCEPT: `night`
- COUNTERPART: `niht`
- PROTO: `*náxtz`
- PROTOFORM: `*náxti`
- DERIVATION_CLASS: `late_analogy`
- Live TSV note: `R/T vol.2 13912-15: OE niht < dat.sg. *nahti (i-umlaut); nom.sg. *nahts > neaht`; the row is therefore already encoded as a deliberate contrast between cognate-set headword `*náxtz` and selected dative-singular test cell `*náxti`, not as a simple one-form citation derivation [Germanic/data/germanic-aligned-final.tsv:815-815].
- Packet status: the compact derivation trace already runs `*náxti` through brightening, breaking, i-umlaut, West Saxon palatal umlaut, and apocope to `niht`, and the packet reports `_None_` for `oe_known_problems.tsv` plus `_No manifest entry._` for this row [Germanic/docs/lexeme_reports/packets/2140-night-niht.md:13-47].
- Memo status: the research memo explicitly treats the row as a paradigm-cell case, finds no dedicated prior lexeme report or dossier, and identifies the live TSV plus `DEV_NOTES` discussions of endingless datives and palatal umlaut as the strongest current evidence [Germanic/docs/lexeme_reports/research_memos/2140-night-niht.md:13-23,25-39].
- Repo-local philological background checked for this slice: Ringe-Taylor's discussion of endingless datives from `niht < *nahti`, Campbell and Brunner on `niht` versus plural `neahtas/cneohtas`-type environments, and the dialect summary `neaht / niht` vs. `næht / neht` [docs/references/ringe_taylor_linguistic_history_vol2.txt:21494-21518; docs/references/campbell_old_english_grammar.txt:4526-4530,8767-8775; docs/references/brunner_1965_altenglische_grammatik.txt:5066-5070; Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:709-710].

## Development-note summary

Current row-specific authority does survive for row 2140, but it survives in **content fragments**, not in a single dedicated `DEV_NOTES` night dossier. The securely current core is the cluster that says Old English `niht` continues dative-singular `*nahti`, that this endingless dative became an analogical model for other nouns, that palatal umlaut regularly yields `niht` before `ht` when no following back vowel blocks it, and that the present FST still treats `*náxti → niht` as a successful preserved-`*xt` control case [Germanic/docs/DEV_NOTES.md:6211-6223,6341-6343,15478-15502,39278-39284]. That is enough to support the live row as a replacement working note.

The three-way distinction must remain explicit. `PROTO = *náxtz` is the cognate-set or nominative-like root-noun headword reflected by the non-umlauted side of the paradigm; `PROTOFORM = *náxti` is the selected **dat.sg.** cell that the project actually feeds to the FST; OE target `niht` is the attested palatal-umlauted output of that oblique cell [Germanic/data/germanic-aligned-final.tsv:815-815; Germanic/docs/lexeme_reports/packets/2140-night-niht.md:19-42; Germanic/docs/lexeme_reports/research_memos/2140-night-niht.md:42-53]. The memo's explicit comparison remains the right operational gloss: citation-form `*náxtz` leads to `neaht`, while selected dat.sg. `*náxti` leads to `niht`; `PROTOFORM` is therefore a chosen paradigm cell, not a rival lexeme-level reconstruction [Germanic/docs/lexeme_reports/research_memos/2140-night-niht.md:48-53,65-78].

The OE philology also has to stay uncompressed. `niht` is not the only historically relevant OE form. Campbell's wording, preserved in `DEV_NOTES`, states that palatal umlaut occurs "regularly in niht ... but not in the plurals neahtas, &c.," and Brunner states the same conditioning in terms of `cniht` versus `cneohtas` before `ht/hs` when a following back vowel is or is not present [Germanic/docs/DEV_NOTES.md:15480-15502; docs/references/campbell_old_english_grammar.txt:8767-8775; docs/references/brunner_1965_altenglische_grammatik.txt:5066-5070]. The dialect summary checked for this slice likewise preserves West Saxon `neaht / niht` against Anglian `næht / neht`, so later reporting must not flatten the row into the claim that only `niht` existed in OE [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:709-710].

The main danger is stale project history. `DEV_NOTES` line 25307 still says row 2140 is `spanne`, which the packet and memo both identify as an old row-number state rather than live evidence for night [Germanic/docs/DEV_NOTES.md:25306-25310; Germanic/docs/lexeme_reports/packets/2140-night-niht.md:51-61; Germanic/docs/lexeme_reports/research_memos/2140-night-niht.md:21-23]. That fragment should be kept only to explain indexing noise and old project chronology. It must not compete with the current authorities above.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-6211-6223

- Source heading: `R/T vol.2 pp.379-380 (§7.2.2): Endingless datives`
- Source line or section hint: `lines 6211-6223`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `endingless_dative`; `paradigm_cell`; `late_analogy`; `protoform_vs_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2013`

This is the strongest row-specific `DEV_NOTES` authority because it preserves the key quotation in directly usable form: `"The dat. sg. dæg ... can owe its lack of ending to lexical analogy with dat. sg. niht < PWGmc, PGmc *nahti."` `DEV_NOTES` then immediately paraphrases the project consequence: the endingless dative pattern spread from `niht (< *nahti)` to nouns such as `dæg`, `morgen`, `ǣfen`, and `hām`, and this was a **later analogical development** after regular sound change had deleted the ending [Germanic/docs/DEV_NOTES.md:6213-6223; docs/references/ringe_taylor_linguistic_history_vol2.txt:21494-21518]. For row 2140 this fragment securely supports all of the live metadata at once: the OE target is specifically the dative-derived form `niht`, the selected `PROTOFORM` must be the oblique cell `*náxti/*nahti`, and `late_analogy` belongs to the later paradigmatic spread of this endingless pattern rather than to a phonological failure in the current FST [Germanic/data/germanic-aligned-final.tsv:815-815].

### DEV_NOTES:line-6341-6343

- Source heading: `Attestation of endingless dative`
- Source line or section hint: `lines 6341-6343`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `endingless_dative`; `productivity`; `morphological_background`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2013`

This short follow-up is worth indexing separately because it turns the long Ringe-Taylor quotation into a project-level inference: endingless datives spread from `niht (< *nahti)` and were a productive early OE pattern [Germanic/docs/DEV_NOTES.md:6341-6343]. It does not by itself prove the row setup, but it clarifies why row 2140 should be read as a stable paradigm-cell solution rather than a one-off curiosity. If later final-report prose needs a compact sentence explaining why `niht` matters beyond its own lexeme, this is the fragment to quote.

### DEV_NOTES:line-15478-15502

- Source heading: `Campbell on Palatal Umlaut (§305–308)`
- Source line or section hint: `lines 15478-15502`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `palatal_umlaut`; `plural_contrast`; `OE_philology`; `dialect_variation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2086`

This fragment preserves the handbook wording that makes the row's OE target philologically defensible without overclaiming. Campbell says palatal umlaut has taken place `"regularly in niht ... but not in the plurals neahtas, &c."`, while the immediately following Brunner quotation explains the same pattern through the presence or absence of a following back vowel before `ht/hs` [Germanic/docs/DEV_NOTES.md:15480-15502; docs/references/campbell_old_english_grammar.txt:8767-8775; docs/references/brunner_1965_altenglische_grammatik.txt:5066-5070]. This matters for row 2140 because it shows why `niht` is a valid OE target from the oblique cell while `neaht` and `neahtas` remain equally real comparators on the non-umlauted side of the paradigm. The row should therefore be written as a selected OE paradigm member, not as the only historically relevant Old English form [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:709-710].

### DEV_NOTES:line-39278-39284

- Source heading: `Corpus rows that depend on the current loss rule`
- Source line or section hint: `lines 39278-39284`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `xt_cluster`; `verification_history`; `successful_derivation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2086,2102,2125,2291`

This shared verification list is not the main philological argument, but it is valuable as a current control-state witness. `DEV_NOTES` explicitly lists `2140 *náxti → niht` among the rows that rely on the present preserved-`*xt` handling, beside `*knéxtaz → cniht`, `*máxtiz → miht`, and `*wéxtiz → wiht` [Germanic/docs/DEV_NOTES.md:39278-39284]. That means the row is not merely theoretically defendable; under the current pipeline it is already one of the working examples that confirm the relevant rule scope.

### DEV_NOTES:line-3167-3208

- Source heading: `Background: A-restoration and paradigmatic leveling` / `Proposed resolution — oblique form approach`
- Source line or section hint: `lines 3167-3208`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `background`
- Issue tags: `paradigm_cell`; `methodology`; `protoform_vs_proto`; `project_history`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `1980,2013,2053,2152`

This is shared methodology rather than fresh night evidence, but it still deserves preservation because it states the project's working rule in a form later notes reuse: two A-restoration cases require the same "oblique form" approach already used for `fire, cow, night`, and the ræst note then spells that precedent out as `night (*naxti → niht, dat.sg.)` [Germanic/docs/DEV_NOTES.md:3167-3208]. For row 2140 the fragment should be cited only as background confirming that night became an established project precedent for paradigm-cell targeting. It is not as strong as the dedicated `niht < *nahti` and `niht ~ neahtas` fragments, because it compresses the argument and does not itself discuss the dialect and paradigm contrasts in detail.

### DEV_NOTES:line-25306-25310

- Source heading: `Path α — paradigm-cell PROTOFORM (Lautgesetzlich via Campbell's own account)`
- Source line or section hint: `lines 25306-25310`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `misleading_if_uncontextualized`
- Issue tags: `stale_row_number`; `indexing_noise`; `project_history`; `diagnostic_only`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs: `2119,2140,2152`

This fragment must be marked aggressively as stale. It says the methodology matches precedents including `spanne (row 2140, dat.sg. *spannăi)`, which is incompatible with the live TSV where row 2140 is `night / niht` [Germanic/docs/DEV_NOTES.md:25306-25310; Germanic/data/germanic-aligned-final.tsv:815-815]. The packet and memo are therefore right to keep it only as diagnostic evidence for an older row-number state, not as current authority about night [Germanic/docs/lexeme_reports/packets/2140-night-niht.md:51-61; Germanic/docs/lexeme_reports/research_memos/2140-night-niht.md:21-23]. Later indexing or report work should preserve the fragment only so readers understand why raw `2140` searches can surface irrelevant `spanne` material.

## Superseded or diagnostic material

- The stale `row 2140 = spanne` hit is the main diagnostic hazard and should never be cited as live evidence for night; it belongs to older table numbering, not the current row [Germanic/docs/DEV_NOTES.md:25306-25310; Germanic/docs/lexeme_reports/research_memos/2140-night-niht.md:21-23].
- Generic keyword hits in unrelated analysis files are likewise not row-specific authority. The memo already flags the broad `i-umlaut` / chronology hits outside the dedicated night materials as potentially misleading if weighed alongside the actual `niht < *nahti` and palatal-umlaut discussions [Germanic/docs/lexeme_reports/research_memos/2140-night-niht.md:23-38].
- Shared methodology references such as `night (*naxti → niht, dat.sg.)` in the ræst discussion remain useful, but only as compressed project history or method background. They should not replace the row-specific authorities that explicitly mention `*nahti`, endingless datives, and the `niht` versus `neahtas` contrast [Germanic/docs/DEV_NOTES.md:3167-3208,6211-6223,15478-15502].

## Open questions for later work

- If a final lexeme report is written, include a small explicit probe table contrasting at minimum `nom.sg. *náxtz → neaht` with `dat.sg. *náxti → niht`; the memo already identifies this as the decisive paradigm-cell contrast for the row [Germanic/docs/lexeme_reports/research_memos/2140-night-niht.md:48-53,71-78].
- Decide whether later report prose should mention lexical headword `niht` together with the broader West Saxon / Anglian alternation `neaht / niht` and `næht / neht`, so the selected row target is not mistaken for the whole OE paradigm [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:709-710; Germanic/docs/lexeme_reports/research_memos/2140-night-niht.md:55-63].
- If `DEV_NOTES.md` itself is later cleaned up, annotate or rewrite the stale line 25307 row-number reference so future packets do not continue surfacing `spanne` as if it were live row-2140 evidence [Germanic/docs/DEV_NOTES.md:25306-25310; Germanic/docs/lexeme_reports/research_memos/2140-night-niht.md:84-92].

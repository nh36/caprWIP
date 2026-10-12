---
row_id: 2133
concept: navel
counterpart: nafola
proto: *nablô
protoform: *nábulô
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2133-navel-nafola.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2133-navel-nafola.md
linked_dossier_or_analysis_files: Germanic/docs/analysis/arestoration_r_l_research.md; Germanic/docs/analysis/unstressed_e_o_before_r.md; Germanic/docs/dossiers/un-to-on-chronology.md; Germanic/docs/dossiers/widuwe-u-preservation.md; Germanic/docs/analysis/compound_archaism_inventory.md; Germanic/docs/analysis/mismatch_dossier_mizdo.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2133 navel / nafola

## Current row state

- CONCEPT: `navel`
- COUNTERPART: `nafola`
- PROTO: `*nablô`
- PROTOFORM: `*nábulô`
- DERIVATION_CLASS: `early_analogy`
- Live TSV state: row 2133 already embodies the split now endorsed in the navel dossier: comparative/cognate-set `PROTO=*nablô`, row-local derivational `PROTOFORM=*nábulô`, and OE target `nafola`; the live note explicitly says Kroonen's headword shape stays in `PROTO` while Ringe-Taylor's pre-syncope shape is used as FST input [Germanic/data/germanic-aligned-final.tsv:788-788].
- Live packet state: the compact derivation trace now runs cleanly from `*nábulô` to `nafola` with no remaining row-level mismatch, passing through OE unstressed-`u` lowering, Anglo-Frisian brightening, A-restoration, `b` allophony, and final weak-tail shortening [Germanic/docs/lexeme_reports/packets/2133-navel-nafola.md:17-41].
- Attached support state: the packet records no separate `oe_known_problems.tsv` entry for this row, and the research memo's broader audit reaches the same conclusion while also confirming that the row is now a replacement-note problem, not an unresolved derivational mismatch [Germanic/docs/lexeme_reports/packets/2133-navel-nafola.md:44-46; Germanic/docs/lexeme_reports/research_memos/2133-navel-nafola.md:15-28,34-35,81-93].
- OE attestation baseline: repo-local lexical data includes `nafola` as an attested OE form, so the row target is not a project-internal invention [Germanic/data/old_english_wiktionary.tsv:194-194].

## Development-note summary

Secure current row-specific DEV_NOTES authority **does survive** for row 2133, and it survives in unusually explicit form. The live project position is that three levels must be kept separate: **PROTO** `*nablô` as the cross-Germanic / Kroonen-style etymological lemma, **PROTOFORM** `*nábulô` as the row-local derivational input needed by the FST, and **OE target** `nafola` as the nominative singular form represented by this row [Germanic/data/germanic-aligned-final.tsv:788-788; Germanic/docs/DEV_NOTES.md:30160-30258,30695-30844,30973-30997; Germanic/docs/lexeme_reports/research_memos/2133-navel-nafola.md:57-71].

That split is not cosmetic. DEV_NOTES preserves Kroonen's syncopated lemma — "`*nablan-` m. 'navel' ... OE `nafela` ... OHG `nabalo, nabulo`" — but also preserves Ringe-Taylor's explicit derivation, twice quoted, "PNWGmc `*nabulō` 'navel' ... > `*næbula` > OE `nafola`," with the word-index entry `nafola ~ -ela` [Germanic/docs/DEV_NOTES.md:30186-30199,30238-30258]. The row therefore does **not** rest on choosing between "Kroonen right" and "R/T right" tout court; the current authority says Kroonen is right for the comparative headword convention, while R/T are right for the phonologically present input form used in derivation [Germanic/docs/DEV_NOTES.md:30781-30812,30992-30997,31714-31728].

The phonological consequence is equally explicit. DEV_NOTES rejects any attempt to rescue `nafola` by widening A-restoration across a `bl` cluster, because under the endorsed input there is no relevant `bl` cluster at the restoration stage: `*næbulō > *nabulō` is an intervocalic-singleton environment, not a `Cl` environment [Germanic/docs/DEV_NOTES.md:30481-30508]. The larger chronology note then treats `nafola`, `nafela`, and Corpus `nabula` as successive OE spellings of the same lexical history: inherited/present medial `u`, then lowering or harmony to `o`, then later reduction/merger to `e` [Germanic/docs/DEV_NOTES.md:30565-30575,30834-30844; Germanic/docs/analysis/unstressed_e_o_before_r.md:27-34,124-139]. This is why the live packet can derive `nafola` regularly from `*nábulô` without any rule rewrite [Germanic/docs/lexeme_reports/packets/2133-navel-nafola.md:17-41].

The secure current note also separates row policy from project history. DEV_NOTES considered but rejected a paradigm-cell switch to oblique forms such as `nafolan` or `nafolum`; the current view is that the navel problem was solved at the **input-form** level, not by changing the target cell [Germanic/docs/DEV_NOTES.md:30762-30779]. The row's live `DERIVATION_CLASS=early_analogy` should therefore be treated cautiously inside the slice: it is the current TSV label, but the surviving DEV_NOTES authority repeatedly describes `nafola` as the clean, regular outcome from chosen input `*nábulô`, with later `nafela` as the more reduced WS majority spelling [Germanic/docs/DEV_NOTES.md:30781-30844; Germanic/docs/lexeme_reports/research_memos/2133-navel-nafola.md:111-120].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2995-2997

- Source heading: `Proto-form notes`
- Source line or section hint: `lines 2995-2997`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `protoform`; `medial_u`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This is the earliest short note that recognised the core row problem before the later dossier was written. It states that for `*nablô` "Competing reconstructions" are in play and that "For A-restoration to fire correctly in the pipeline, `*nabulô` may be needed," because R/T place epenthesis later than retraction [Germanic/docs/DEV_NOTES.md:2995-2997]. That observation is still historically useful, but it is no longer current authority: row 2133 already uses `*nábulô` as `PROTOFORM`, and the later §17.19 / §17.19.10 material replaces this tentative wording with a much firmer split between comparative `PROTO` and derivational `PROTOFORM` [Germanic/data/germanic-aligned-final.tsv:788-788; Germanic/docs/DEV_NOTES.md:30695-30844,30973-30997].

### DEV_NOTES:section-17.19-source-canvass-lines-30158-30258

- Source heading: `§17.19  PGmc 'navel' (*nablô / *nabulō → OE *nafola*) — proto-form choice and the *Cl A-restoration question`
- Source line or section hint: `lines 30158-30258`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `proto_vs_protoform`; `kroonen`; `ringe_taylor`; `attestation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the foundational row-specific DEV_NOTES fragment. It opens by recording the live mismatch state — `*náblô` yielded `næfla` instead of `nafola` because both A-restoration and the medial vowel were missing from the derivation — and then immediately anchors the problem in competing scholarly conventions rather than in an arbitrary project preference [Germanic/docs/DEV_NOTES.md:30160-30169]. Kroonen is quoted as lemmatising "`*nablan-` m. 'navel' ... OE `nafela` ... OHG `nabalo, nabulo`" [Germanic/docs/DEV_NOTES.md:30186-30199]. R/T are then quoted twice with the exact pathway needed by the row: "PNWGmc `*nabulō` 'navel' (ON `nafli`, OHG `nabalo`) > `*næbula` > OE `nafola`" and again "PWGmc `*nabulō` ... > `*næbula` > OE `nafola`," followed by the index entry `nafola ~ -ela` [Germanic/docs/DEV_NOTES.md:30221-30258]. The current slice should keep those quotations because they are the clearest explanation of why `PROTO` and `PROTOFORM` must diverge here while still referring to the same cognate set.

### DEV_NOTES:section-17.19-phonology-lines-30481-30580

- Source heading: `§17.19.2 Empirical check: does A-restoration fail before *l?` plus `§17.19.3 Chronology`
- Source line or section hint: `lines 30481-30580`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `a_restoration`; `chronology`; `single_consonant`; `unstressed_vowel_history`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2130`

This fragment contains the main phonological reason the row now counts as regular from the chosen input. DEV_NOTES stresses that R/T's rule applies after a stressed `æ` followed by "a single or geminate consonant or sC-cluster," and then spells out why `nafola` is **not** a counterexample involving `Cl`: under `*nabulō`, "the rule applies in the **intervocalic-singleton** case, not in a cluster case" [Germanic/docs/DEV_NOTES.md:30481-30490]. The inventory table then lists `nafola (V-b-ul-V)` explicitly as a **single**-consonant restoration case [Germanic/docs/DEV_NOTES.md:30497-30508]. The chronology note is equally important for row prose: after brightening to `*næbulō`, A-restoration returns `*nabulō`; later unstressed-vowel developments produce attested `nafela`, `nafola`, and Corpus `nabula`, with final OE nominative singular `-a` from the n-stem tail [Germanic/docs/DEV_NOTES.md:30553-30580]. The same point is reinforced in the dedicated liquid/restoration dossier, which quotes R/T's list of single-`l` examples headed by `*nabulē > *næbula > OE nafola` and concludes that R/T "does not anywhere identify *r/*l as a blocker" [Germanic/docs/analysis/arestoration_r_l_research.md:149-160].

### DEV_NOTES:section-17.19.5-recommendation-lines-30695-30844

- Source heading: `§17.19.5  Recommendation`
- Source line or section hint: `lines 30695-30844`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `row_policy`; `proto_vs_protoform`; `target_selection`; `paradigm_cell`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2130`

This is the operative row-policy fragment. DEV_NOTES weighs four options and then chooses Option A: change only the row-local proto-input, not the sound rule and not the target cell [Germanic/docs/DEV_NOTES.md:30695-30780]. The recommendation is explicit: "Option A is the most defensible philologically and the most surgical for the FST," because it "exactly tracks R/T §6.3.1 ... and §6.7.x, which twice cite `*nabulō > næbula > nafola` as the canonical derivation" [Germanic/docs/DEV_NOTES.md:30781-30797]. It also states the concrete row policy still visible in the TSV: `PROTOFORM` becomes `*nábulô`, `PROTO` may remain `*nablô`, and `TOKENS, COUNTERPART, ALIGNMENT, IPA` stay unchanged [Germanic/docs/DEV_NOTES.md:30802-30812; Germanic/data/germanic-aligned-final.tsv:788-788]. The attached note on doublets must be carried forward nearly verbatim because it is still accurate: OE shows `nafela` "(WS, majority)," `nafola` "(matches R/T's chosen output and the TSV target)," and `nabula` "(Cp., preserving the original *u)" [Germanic/docs/DEV_NOTES.md:30834-30844].

### DEV_NOTES:section-17.19.10-appendix-lines-30973-31310

- Source heading: `§17.19.10  Origin and chronology of the medial *u in *nabulō: a survey of the literature`
- Source line or section hint: `lines 30973-31310`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `medial_u`; `literature_split`; `inherited_vs_epenthetic`; `proto_vs_protoform`
- Recommended next use: `check_against_literature`
- Shared with row IDs:

This appendix is the best current authority on what the project **does not** need to overclaim. Its own conclusion is already the row's best formulation: "R/T's `*nabulō` is right *as the FST input*, but ... Kroonen's `*nablan-` is right *as the cross-Germanic etymological lemma*" [Germanic/docs/DEV_NOTES.md:30973-30997]. The appendix then preserves the real literature split over the medial vowel's origin instead of suppressing it. Camp 1 (Streitberg / Ringe) treats the `u` as inherited via syllabic-resonant resolution, with `*l̥ > *ul` producing the relevant shape before OE [Germanic/docs/DEV_NOTES.md:31152-31183]. Camp 2 (EWA / Brunner / Luick / Kroonen-style lemmatisation) treats the vowel as a **Sekundärvokal** or other epenthetic development at some prehistory stage [Germanic/docs/DEV_NOTES.md:31184-31310]. For row 2133, the usable present-tense conclusion is conservative: the slice should preserve the dispute, but the row does not depend on resolving it, because both camps still leave a medial vowel in place by the PNWGmc/WGmc stage required for `*nábulô → nafola` [Germanic/docs/DEV_NOTES.md:30973-30997; Germanic/docs/lexeme_reports/research_memos/2133-navel-nafola.md:66-71].

## Superseded or diagnostic material

- The old §17.19 status line "research complete; awaiting Option-selection by user" is now stale project history, not current authority, because the row already shows the Option A split in live TSV state and the packet confirms successful derivation from `*nábulô` [Germanic/docs/DEV_NOTES.md:30160-30169; Germanic/data/germanic-aligned-final.tsv:788-788; Germanic/docs/lexeme_reports/packets/2133-navel-nafola.md:17-41].
- The short proto-form note at lines 2995-2997 should likewise be read only as an early diagnostic precursor. It correctly anticipated the need for a medial vowel, but it predates the later source canvass, recommendation, and appendix that now provide the row's secure authority [Germanic/docs/DEV_NOTES.md:2995-2997,30158-30258,30695-30844,30973-30997].
- `compound_archaism_inventory.md` is useful only as project history here. Its Case 5 table calls the item a "strong ō-stem" while also speaking of n-stem obliques and therefore mixes stem-class and paradigm descriptions in a way that should not be reused as final row phrasing [Germanic/docs/analysis/compound_archaism_inventory.md:126-140].
- `mismatch_dossier_mizdo.md` is only a methodological cross-reference and appears to point to the wrong DEV_NOTES section for this lexeme; it should be ignored unless debugging dossier cross-links [Germanic/docs/analysis/mismatch_dossier_mizdo.md:20-24; Germanic/docs/lexeme_reports/research_memos/2133-navel-nafola.md:22-28,119-120].

## Open questions for later work

- If a later full lexeme report is written, decide whether to leave `DERIVATION_CLASS=early_analogy` untouched as an administrative label or to align it with the surviving note tradition, which treats `nafola` as regular from selected input `*nábulô` [Germanic/data/germanic-aligned-final.tsv:788-788; Germanic/docs/DEV_NOTES.md:30781-30844].
- If stronger manuscript or dialect wording is ever desired for `nafola` versus `nafela` versus `nabula`, check external literature directly; the current repo evidence securely supports the earlier/less-reduced versus later/majority distinction, but not a much sharper distributional claim [Germanic/docs/DEV_NOTES.md:30565-30575,30834-30844; docs/references/campbell_old_english_grammar.txt:10379-10380; docs/references/ringe_taylor_linguistic_history_vol2.txt:37733-37733].
- If future indexing wants the literature-survey material split more finely, keep the appendix's two-camp structure (`inherited *u` versus `Sekundärvokal`) attached to row 2133, because that is the key reason the row must continue to distinguish `PROTO` from `PROTOFORM` even though the derivation itself is no longer in doubt [Germanic/docs/DEV_NOTES.md:30973-30997,31152-31310].

---
row_id: 2077
concept: hold
counterpart: healdan
proto: *xáldaną
protoform: *xáldaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2077-hold-healdan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2077-hold-healdan.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md
  - Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2077 hold / healdan

## Current row state

- CONCEPT: `hold`
- COUNTERPART: `healdan`
- PROTO: `*xáldaną`
- PROTOFORM: `*xáldaną`
- DERIVATION_CLASS: `regular`
- Live TSV note: `R/T vol.2 10729: PGmc *haldaną > WS OE healdan (with breaking)` [Germanic/data/germanic-aligned-final.tsv:570].
- Packet status: the live cascade already derives the row correctly. The compact trace starts from `PROTO: *xáldaną`, applies Anglo-Frisian brightening and OE breaking, and surfaces `OUTPUTS: healdan`, so there is no current derivational mismatch to repair [Germanic/docs/lexeme_reports/packets/2077-hold-healdan.md:17-43].
- `oe_known_problems.tsv`: no row-specific entry survives; the packet records `Matching oe_known_problems.tsv entries` as `_None_`, and the memo repeats that row 2077 is not currently managed as an OE exception [Germanic/docs/lexeme_reports/packets/2077-hold-healdan.md:45-47; Germanic/docs/lexeme_reports/research_memos/2077-hold-healdan.md:49-50,82-91].
- Memo status: the row is regular, but the memo says the real documentation task is to state the dialect choice explicitly. The row targets West-Saxon/Kentish `healdan`, while Anglian/Mercian `haldan` is a genuine comparator doublet rather than a correction to the row [Germanic/docs/lexeme_reports/research_memos/2077-hold-healdan.md:19-29,63-79,86-101].
- Current DEV_NOTES authority does **not** exist as a dedicated row-specific discussion. The only securely attachable DEV_NOTES material is the shared classification line `| 2077 | *xáldaną | healdan | breaking |` and the later verification row `*xaldaną → healdan ✓`; both are useful, but neither is a prose dossier governing target choice on its own [Germanic/docs/lexeme_reports/packets/2077-hold-healdan.md:49-61,143-151; Germanic/docs/lexeme_reports/research_memos/2077-hold-healdan.md:23-29].

## Development-note summary

No securely attachable **row-specific** DEV_NOTES note survives for row 2077. That needs to be said explicitly. The packet's only exact DEV_NOTES hit is a one-line shared classification table, and the only other direct match the memo endorses is a verification row showing the current FST output. The memo therefore treats row 2077 as a case where current policy comes primarily from the live TSV row plus packet/memo source audit, not from a dedicated DEV_NOTES repair narrative [Germanic/docs/lexeme_reports/packets/2077-hold-healdan.md:49-61,143-151; Germanic/docs/lexeme_reports/research_memos/2077-hold-healdan.md:23-29,80-91].

The three lexical levels still need to stay distinct. Comparative sources in the repo cite the cognate set as PGmc `*haldaną/*haldana`, the live project row uses encoded input `*xáldaną` for both `PROTO` and `PROTOFORM`, and the OE target represented by the row is the citation infinitive `healdan`, not a hidden paradigm cell and not the non-WS doublet `haldan` [Germanic/data/germanic-aligned-final.tsv:570; Germanic/docs/lexeme_reports/research_memos/2077-hold-healdan.md:61-67,95-101]. Campbell's wording is the most compact statement of the dialect split and is worth preserving directly: “Examples in normal W-S spelling are eall all, **healdan** hold, healf half ... the corresponding Angl. forms are all, **haldan**, &c.” [docs/references/campbell_old_english_grammar.txt:4445-4468]. The repo's dialect note restates the same contrast as a reusable project rule: under `æ + lC`, “Angl. `ald, all, haldan ...`; WS `eald, eall, healdan ...`” [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:400-405,696-700].

The sound-change side is currently ordinary and should not be overdramatized. The packet's derivation trace gives the live sequence `*xáldaną` > brightened `*xældaną` > broken `*xealdaną` > `healdan`, and DEV_NOTES later re-checks the same lexical input with the verification line `*xaldaną         → healdan  healdan    ✓` [Germanic/docs/lexeme_reports/packets/2077-hold-healdan.md:19-43; Germanic/docs/DEV_NOTES.md:10553-10566]. The shared A-restoration audit also lists row 2077 simply as `breaking`, which is useful because it shows the row is being treated as a normal member of the `*a + lC` OE breaking set rather than as a special-case repair target [Germanic/docs/DEV_NOTES.md:30604-30647; Germanic/docs/analysis/arestoration_r_l_research.md:730-738].

The main row-level risk is source hygiene. The packet's lexical tables give two conflicting OE prompts: `old_english_wiktionary.tsv` has `hold -> hold`, but `old_english_swadesh.tsv` has `to hold -> healdan` [Germanic/docs/lexeme_reports/packets/2077-hold-healdan.md:367-379; Germanic/data/old_english_wiktionary.tsv:140; Germanic/data/old_english_swadesh.tsv:130]. The memo is explicit that `hold` is misleading here and must not outweigh the handbook-backed WS headword. For positive philological support, the repo already has Bright's strong-verb paradigm `healdan, ... heold, ... heoldon, ... healden`, which confirms that the row is about the ordinary citation infinitive and that any paradigm detail is only background, not a reason to probe a different cell [Germanic/docs/lexeme_reports/research_memos/2077-hold-healdan.md:35-39,71-79,93-101; docs/references/bright_anglo_saxon_reader.txt:2815-2821].

## Relevant DEV_NOTES fragments

No securely attachable **current row-specific** DEV_NOTES prose survives. The two items below are the only safe carry-forwards, and both are shared or diagnostic rather than controlling row policy.

### DEV_NOTES:line-30623

- Source heading: `Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail`
- Source line or section hint: `lines 30604-30647, especially 30623`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `background`
- Issue tags: `breaking`; `shared_row_inventory`; `a_plus_lc`; `row_classification`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `1975, 2025, 2052, 2118, 2166, 2167, 2289, 2297`

This fragment is worth preserving, but only as shared classification material. Inside a broader scan of TSV rows shaped like `*aCl`/`*aCr` before a back-vowel tail, DEV_NOTES lists row 2077 as `| 2077 | *xáldaną | healdan | breaking |`, alongside other ordinary breaking items [Germanic/docs/DEV_NOTES.md:30609-30640]. That matters because it shows later DEV_NOTES did **not** treat `healdan` as an A-restoration failure, a target-side anomaly, or a row needing bespoke repair prose. The memo accordingly classifies this hit only as a current internal label, useful for saying that 2077 belongs to the normal `*a + lC` breaking set, but not as the authority that chooses WS `healdan` over Anglian/Mercian `haldan` [Germanic/docs/lexeme_reports/research_memos/2077-hold-healdan.md:25-29,82-91].

### DEV_NOTES:line-10561

- Source heading: `Verification`
- Source line or section hint: `lines 10553-10566, especially 10561`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `verification`; `infinitive_output`; `fst_stability`; `project_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This is a useful verification checkpoint, not a row-policy note. The DEV_NOTES table records `*xaldaną         → healdan  healdan    ✓` as one of the tested derivations in a discussion about syllable-structure-sensitive handling of infinitives versus participles [Germanic/docs/DEV_NOTES.md:10553-10566]. For row 2077 the value of that line is narrow but real: it confirms that the current cascade continued to produce `healdan` when the surrounding rule mechanics were being checked. It does **not** by itself justify the lexical target, dialect choice, or philological interpretation; those still come from the row metadata and the packet/memo source audit [Germanic/docs/lexeme_reports/packets/2077-hold-healdan.md:143-151; Germanic/docs/lexeme_reports/research_memos/2077-hold-healdan.md:25-29,82-91].

## Superseded or diagnostic material

### Packet/source-audit: `hold -> hold` lexical-table false positive

- Source heading: `old_english_wiktionary.tsv` hit versus `old_english_swadesh.tsv` and handbook-backed WS evidence
- Source line or section hint: `packet lines 367-379; data lines old_english_wiktionary.tsv:140 and old_english_swadesh.tsv:130`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `misleading_if_uncontextualized`
- Issue tags: `false_positive`; `source_ranking`; `hold_vs_healdan`; `lexical_table_noise`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This is the main non-DEV_NOTES item that must be preserved so later work does not repeat the same mistake. The packet surfaces `old_english_wiktionary.tsv` as `hold | hold`, but `old_english_swadesh.tsv` gives `to hold | healdan`, and the memo explicitly warns that the `hold` hit is misleading for row 2077 [Germanic/docs/lexeme_reports/packets/2077-hold-healdan.md:367-379; Germanic/data/old_english_wiktionary.tsv:140; Germanic/data/old_english_swadesh.tsv:130; Germanic/docs/lexeme_reports/research_memos/2077-hold-healdan.md:35-39,78-91]. The reason is lexical and dialectal at once: this row is specifically the WS/Kentish strong-verb infinitive `healdan`, while `hold` is merely a low-authority lexical-table collision. Later report writing should therefore keep the source ranking explicit: TSV row + packet trace + handbook-backed dialect discussion outrank the stray `hold` table entry.

### Packet/DEV_NOTES search residue: unrelated `*habja-` / `*habē-` “to hold, to have” material

- Source heading: `Concept-name collisions on “hold” in DEV_NOTES packet search`
- Source line or section hint: `packet lines 409-429`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `misleading_if_uncontextualized`
- Issue tags: `concept_name_collision`; `wrong_lexeme_family`; `search_residue`; `diagnostic_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

The packet intentionally preserves two DEV_NOTES hits that mention “to hold,” but they belong to the `*habjan-/*habē-` family behind `habban`, not to row 2077's `*xáldaną` [Germanic/docs/lexeme_reports/packets/2077-hold-healdan.md:409-429]. One quotation is Ringe-Taylor's “PGmc `*habja- ~ *habai- 'to hold, to have'` ... OE `habban`,” and the other is a Kroonen-side remark that related entries confirm a `*-j-` variant [Germanic/docs/lexeme_reports/packets/2077-hold-healdan.md:414-428]. These hits should stay in the slice only as checked diagnostic residue showing what was screened out. They are not comparator evidence for `healdan`, and carrying them forward without warning would blur two different Germanic verb families.

## Open questions for later work

- If the live TSV note is ever rewritten, make the dialect choice fully explicit: row 2077 targets **WS/Kentish `healdan`**, while **Anglian/Mercian `haldan`** is the real comparator doublet; do not frame `haldan` as a correction to the row [Germanic/docs/lexeme_reports/research_memos/2077-hold-healdan.md:86-109; Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:696-700].
- If later index integration records fragment status, mark row 2077 as having **no row-specific current DEV_NOTES authority**, only a shared background classification fragment (`30623`) and a diagnostic verification fragment (`10561`) [Germanic/docs/lexeme_reports/packets/2077-hold-healdan.md:49-61,143-151; Germanic/docs/lexeme_reports/research_memos/2077-hold-healdan.md:23-29].
- If a final lexeme report wants paradigm detail, Bright's `healdan / heold / heoldon / healden` can be quoted as background for the ordinary strong-verb paradigm, but that material should remain philological color rather than evidence for a paradigm-cell workaround [docs/references/bright_anglo_saxon_reader.txt:2815-2821; Germanic/docs/lexeme_reports/research_memos/2077-hold-healdan.md:93-101].
- If source-audit cleanup later revisits OE lexical tables, keep the present ranking explicit: `old_english_wiktionary.tsv`'s `hold` is diagnostic only, whereas the live row, the packet trace, `old_english_swadesh.tsv`, and the handbook-backed WS/Anglian contrast all support `healdan` as the row's intended OE target [Germanic/docs/lexeme_reports/packets/2077-hold-healdan.md:17-43,367-379; Germanic/docs/lexeme_reports/research_memos/2077-hold-healdan.md:71-79,86-109].

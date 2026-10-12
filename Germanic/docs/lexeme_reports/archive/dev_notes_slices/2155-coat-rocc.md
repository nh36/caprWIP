---
row_id: 2155
concept: coat
counterpart: rocc
proto: *rúkkaz
protoform: *rúkkaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2155-coat-rocc.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2155-coat-rocc.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2155 coat / rocc

## Current row state

- CONCEPT: `coat`; COUNTERPART: `rocc`; PROTO: `*rúkkaz`; PROTOFORM: `*rúkkaz`; DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:873-873].
- Live row note: `Garment word: OE rocc 'tunic' (brēostrocc, pistolrocc etc.), from PGmc *rukkăz (a-stem).` Live row history: `Previous entry conflated stone and garment etymologies.` [Germanic/data/germanic-aligned-final.tsv:873-873]
- `oe_known_problems.tsv` has no entry for this lexeme or row; the current problem state is therefore documentary/etymological clarification, not an open exception bucket in that file [Germanic/data/oe_known_problems.tsv:1-8].
- Existing lexeme-report scaffolding already uses the same stem `2155-coat-rocc` for both the packet and the research memo, so this slice can link to them directly without renaming anything [Germanic/docs/lexeme_reports/packets/2155-coat-rocc.md:1-60; Germanic/docs/lexeme_reports/research_memos/2155-coat-rocc.md:1-84].

## Development-note summary

The securely relevant DEV_NOTES material for row `2155` is concentrated in one compact but important section: `Cognate set 379 "rock" → corrected to "coat" (*rukkăz)` [Germanic/docs/DEV_NOTES.md:3001-3045]. That section is the row's authoritative project-history explanation, because it records exactly what had gone wrong and exactly what the project decided to keep. DEV_NOTES says the old cognate set had been glossed `rock` and paired with PGmc `*rukkiz` plus OE `rocc`, German `Ruck`, Dutch `ruk`, and English `rock`; it then states bluntly, `This set was a mess: three different etymologies had been conflated` [Germanic/docs/DEV_NOTES.md:3008-3016]. For replacement working notes, that sentence matters because it is not just colorful wording: it defines the row-level danger that later reviewers must keep in view.

DEV_NOTES then separates the three etymologies explicitly. First comes the row that is now intended: `OE rocc "garment/tunic"`, from PGmc `*rukkaz` as a masculine a-stem, with German `Rock` and Dutch `rok` as the relevant continental comparanda, and with OE compound evidence (`brēostrocc, pistolrocc, bisċoprocc etc.`) cited to show that the garment word is a real OE lexeme rather than a project-side reconstruction [Germanic/docs/DEV_NOTES.md:3017-3019]. Second comes a different OE `*rocc` for `rock formation`, said to be attested only in `stānrocc` and to have uncertain, possibly non-native etymology via Medieval Latin `rocca`; DEV_NOTES adds that ModE `rock` in the stone sense is partly from this OE item and partly from Anglo-Norman `roque` [Germanic/docs/DEV_NOTES.md:3021-3024]. Third comes German `Ruck` / Dutch `ruk` `jerk, jolt, pull`, which DEV_NOTES derives from MHG/OHG material related to `rücken` and labels `a completely different root, unrelated to the garment word` [Germanic/docs/DEV_NOTES.md:3026-3028].

The resolution block is equally row-specific and should be carried over almost verbatim in substance. DEV_NOTES says the project `Replaced the cognate set with the garment word`, then gives the new set: PGmc `*rukkăz` (masc. a-stem), OE `rocc "upper garment, tunic"`, German `Rock`, Dutch `rok`, and English `rock` in an archaic garment sense [Germanic/docs/DEV_NOTES.md:3030-3038]. It then states the two decisive row-policy changes in explicit terms: `Concept changed from "rock" (stone) to "coat" (garment)` and `Proto-form changed from *rukkiz (i-stem, wrong) to *rukkăz (a-stem, correct)` [Germanic/docs/DEV_NOTES.md:3038-3040]. For the slice, that means the row-level distinction must stay sharp: the live row's `PROTO` and `PROTOFORM` are both the project's current garment-word input `*rúkkaz`, while the OE target is the garment noun `rocc`; neither the stone lexeme nor the `Ruck/ruk` set belongs inside the row's present lexical scope [Germanic/data/germanic-aligned-final.tsv:873-873; Germanic/docs/DEV_NOTES.md:3030-3040].

DEV_NOTES also gives a compact sound-change rationale that is still useful for review. Because the corrected protoform is an a-stem nominative singular in `*-ăz`, there is no following `*-i-` trigger; DEV_NOTES therefore notes `No i-umlaut`, `No palatalization of *kk (no following front vowel)`, and `PGmc *u stays as *u, lowered to OE o by NWGmc u-lowering`, ending with `Pipeline output: rocc ✓` [Germanic/docs/DEV_NOTES.md:3042-3045]. This is important for row `2155` because it shows that the correction was not only lexical but derivational: the project is not merely relabeling a troublesome row, it is explicitly asserting that the garment-word input belongs to the ordinary derivational path that yields `rocc`.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3015-3028

- Source heading: `Cognate set 379 "rock" → corrected to "coat" (*rukkăz)` / `### The problem`
- Source line or section hint: `lines 3015-3028`
- fragment_type: `lexeme_specific`
- current_status: `current`
- Issue tags: `lexical_disambiguation`; `conflated_etymologies`; `garment_vs_stone`; `counterpart_scope`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling disambiguation fragment. DEV_NOTES does not merely say that the old gloss was a little off; it says, `This set was a mess: three different etymologies had been conflated` [Germanic/docs/DEV_NOTES.md:3015-3015]. It then identifies each branch separately: the intended branch is `OE rocc "garment/tunic"` with cognates German `Rock` and Dutch `rok`, and with OE compounds such as `brēostrocc`, `pistolrocc`, and `bisċoprocc` showing that the garment lexeme is well established in OE usage [Germanic/docs/DEV_NOTES.md:3017-3019]. The two excluded branches are equally important for row policy: the stone word belongs only to `stānrocc` and may be a non-native item, while German `Ruck` / Dutch `ruk` belong to a different root tied to `rücken` [Germanic/docs/DEV_NOTES.md:3021-3028]. For row `2155`, this fragment establishes the lexical fence around the row.

### DEV_NOTES:line-3030-3045

- Source heading: `Cognate set 379 "rock" → corrected to "coat" (*rukkăz)` / `### Resolution`
- Source line or section hint: `lines 3030-3045`
- fragment_type: `lexeme_specific`
- current_status: `current`
- Issue tags: `row_policy`; `protoform_vs_proto`; `a_stem`; `sound_law_path`; `derivational_validation`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

This fragment is the row's current project policy in compact form. DEV_NOTES says the set was replaced with the garment word and then lists the corrected comparative set headed by PGmc `*rukkăz` and OE `rocc "upper garment, tunic"` [Germanic/docs/DEV_NOTES.md:3032-3038]. It also records the decisive row rewrite in exact terms: `Concept changed from "rock" (stone) to "coat" (garment)` and `Proto-form changed from *rukkiz (i-stem, wrong) to *rukkăz (a-stem, correct)` [Germanic/docs/DEV_NOTES.md:3038-3040]. The closing sound-law bullets are part of the same authority: because the corrected form is an a-stem in `*-ăz`, there is no `i`-trigger for umlaut or palatalization, and the cascade now reaches `rocc` as intended [Germanic/docs/DEV_NOTES.md:3042-3045]. For row `2155`, this fragment is the one to cite when explaining both why the live `PROTO`/`PROTOFORM` are now garment-word forms and why the derivation is still classified `regular`.

## Superseded or diagnostic material

- The old pre-fix set itself should be preserved only as diagnostic history. DEV_NOTES says cognate set 379 had been glossed `rock` and combined PGmc `*rukkiz` with OE `rocc`, German `Ruck`, Dutch `ruk`, and English `rock` [Germanic/docs/DEV_NOTES.md:3008-3013]. That configuration is superseded. Its value now is to document the exact mistaken bundle that later editors must **not** recreate.
- The row's live history field already agrees with DEV_NOTES about the nature of the mistake: `Previous entry conflated stone and garment etymologies` [Germanic/data/germanic-aligned-final.tsv:873-873]. That history line is still worth preserving because it ties the current row directly to the DEV_NOTES repair, but it should not be expanded back into a live mixed-etymology account.
- DEV_NOTES' comparative shorthand is useful but compact. It names the corrected proto as `*rukkăz` and also cites Kroonen in h-initial form inside the garment-word discussion [Germanic/docs/DEV_NOTES.md:3017-3018,3034-3034]. For present row policy that shorthand is good enough, but any later literature-heavy final report should verify exactly how much of that comparative-source nuance needs to be spelled out, rather than silently flattening all source traditions into a single uncontested proto citation.

## Open questions for later work

- If a later final report wants more than project-internal row policy, verify whether the Kroonen citation named in DEV_NOTES should be quoted more exactly and explain how it relates to the live row's `PROTO`/`PROTOFORM` `*rúkkaz` [Germanic/docs/DEV_NOTES.md:3017-3018,3034-3034; Germanic/data/germanic-aligned-final.tsv:873-873].
- If later report prose discusses OE attestation in more detail, keep the lexical boundary explicit: row `2155` is the garment noun `rocc`; the stone item from `stānrocc` belongs only in a contrast paragraph, not in the row's main evidentiary narrative [Germanic/docs/DEV_NOTES.md:3017-3024].
- If `Germanic/docs/lexeme_reports/dev_notes_slices/index.tsv` is updated later, index this row under the current disambiguation fragment (`3015-3028`) and the current resolution/derivation fragment (`3030-3045`); the earlier `3008-3013` bundle is best indexed only as superseded project history.

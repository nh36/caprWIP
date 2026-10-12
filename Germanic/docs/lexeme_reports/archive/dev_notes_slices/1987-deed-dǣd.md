---
row_id: 1987
concept: deed
counterpart: dǣd
proto: *dḗdiz
protoform: *dḗdiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/1987-deed-dǣd.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/1987-deed-dǣd.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1987 deed / dǣd

## Current row state

- CONCEPT: `deed`
- COUNTERPART: `dǣd`
- PROTO: `*dḗdiz`
- PROTOFORM: `*dḗdiz`
- DERIVATION_CLASS: `regular`
- Live TSV note: `R/T vol.2 13823: PGmc *dēdiz > WS OE dǣd (not Anglian dēd)`.
- `oe_known_problems.tsv`: no row-specific entry.
- `report_manifest.tsv`: no manifest entry for row 1987.
- Working caution carried forward from the packet and memo: comparative handbooks and lexical tables may cite undifferentiated or non-WS `dēd`, but the live row is intentionally **West Saxon** `dǣd`; the stress-marked `*dḗdiz` is the project's modelling input, not a claim that comparative etymology has abandoned ordinary `*dēdiz` / `*dédiz` style citation forms [DEV_NOTES:line-42683-42739; @Campbell1959, §128; @SieversBrunner1965].

## Development-note summary

Row 1987 has a notably thin DEV_NOTES footprint. No long lexeme-specific debate survives there about morphology, paradigm choice, or whether OE really had the noun. The securely attachable current DEV_NOTES authority is instead the stressed-long-`ē` refactor that regularized how the project marks **stressed root-syllable inherited long `ē`**. That note says the codebase had already introduced stress-tier symbols for other long vowels, but still lacked a parallel symbol for stressed long `ē`; it therefore retrofitted `*ḗ` across the cascade and explicitly listed `*dēdiz*` among the root-syllable long-`ē` lemmas that needed promotion [DEV_NOTES:line-42683-42728]. For this row, the important consequence is narrow but decisive: the live project input is now `*dḗdiz`, not plain `*dēdiz`, because the cascade needs to distinguish stressed inherited long `ē` from unstressed `ē` in suffixes and other weak-tail positions [DEV_NOTES:line-42683-42728].

That DEV_NOTES material does **not** by itself create the WS target `dǣd`; rather, it explains why the project can now model that target cleanly and consistently. The live row note and the linked memo preserve the philological distinction that matters: comparative Proto-Germanic is ordinarily cited as `*dēdiz` / `*dédiz`, while Old English shows a dialect split in which **West Saxon `dǣd`** stands against **Anglian / non-WS `dēd`** [@Campbell1959, §128; @SieversBrunner1965]. The project decision is therefore two-layered and should stay explicit in later work: keep the comparative etymology in the background, but feed the FST the stress-marked modelling form `*dḗdiz` so that the inherited stressed long vowel follows the encoded lowering path to WS `dǣd` [DEV_NOTES:line-42683-42739].

The verification lines are worth preserving almost verbatim because they are the only row-local DEV_NOTES place where the present derivation is actually shown in running project prose. DEV_NOTES reports that mismatch totals stayed stable through the refactor and gives the sample output list `"*dḗdiz → dǣd*, *lḗtaną → lǣtan*, *rḗdaną → rǣdan* ..."` [DEV_NOTES:line-42735-42739]. That quotation matters for workflow purposes: it shows that row 1987 was not a speculative future target when `*ḗ` was introduced, but one of the explicit proof cases used to verify that the refactor preserved expected outputs.

Just as important is what DEV_NOTES does **not** preserve. It does not retain a securely attachable row-specific argument for an older `dēd` target, nor a dedicated discussion reweighing WS against Anglian forms. The linked research memo shows that earlier debug snapshots still produced or expected `dēd`, but that chronology lives outside DEV_NOTES proper. The honest replacement working note therefore has to say this plainly: inside `DEV_NOTES.md`, current authority for row 1987 begins with the stressed-`*ḗ` refactor, while the fuller dialectological framing (`WS dǣd` versus `Anglian dēd`) comes from the live TSV note plus handbook background already assembled in the packet and memo [DEV_NOTES:line-42683-42739; @Campbell1959, §128; @SieversBrunner1965].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-42683-42728

- Source heading: `stressed long-ē refactor motivation and row promotion`
- Source line or section hint: `lines 42683-42728`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `stress_marking`; `protoform_vs_proto`; `shared_sound_change`; `row_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the main surviving DEV_NOTES authority for row 1987. The note explains that the project had already created stress-tier symbols for other long vowels and now needed an equivalent symbol for stressed inherited long `ē`; it therefore introduced `*ḗ` as a parallel symbol and says that about sixteen root-syllable long-`ē` lemmas were promoted from `*ē` to `*ḗ` in both `PROTOFORM` and `PROTO` [DEV_NOTES:line-42683-42728]. `*dēdiz*` is named explicitly in the motivating list of such lemmas, so this fragment is the clearest row-local evidence that live `*dḗdiz` is an intentional modelling convention rather than an accidental respelling. For later report work, the key use is to keep the distinction explicit: comparative proto is still cited in ordinary scholarship without the project-only stress mark, but the row's live FST input now requires stressed `*ḗ` in order to derive the selected WS target consistently.

### DEV_NOTES:line-42735-42739

- Source heading: `verification sample after stressed long-ē refactor`
- Source line or section hint: `lines 42735-42739`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `verification`; `stress_marking`; `output_check`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This short verification fragment is worth keeping separately because it is the only place where row 1987 appears in explicit before/after project verification prose. DEV_NOTES says mismatch count remained stable and quotes the sample outputs as `"*dḗdiz → dǣd*, *lḗtaną → lǣtan*, *rḗdaną → rǣdan* ..."` [DEV_NOTES:line-42735-42739]. For this slice, that line does two jobs at once: it confirms that `dǣd` is the intended live output under the new notation, and it marks the row as a checked success case of the stressed-`*ḗ` refactor rather than a lexeme still awaiting cleanup.

## Superseded or diagnostic material

No securely attachable **row-specific superseded DEV_NOTES fragment** survives for the older `dēd`-target stage. That absence needs to stay explicit so later workflow does not force a false connection. The older project chronology is real — the linked research memo records earlier debug snapshots with `dēd` — but it is preserved in snapshot files and memo reconstruction, not in a dedicated DEV_NOTES passage that can be indexed here as current row authority.

The practical consequence is conservative indexing and reporting. For row 1987, DEV_NOTES should be used mainly to document the stressed-`*ḗ` modelling decision and the verified output `*dḗdiz → dǣd`. The broader dialectological explanation (`WS dǣd`, Anglian `dēd`) belongs in the slice because it is essential working context, but it comes from the live row note and handbook background rather than from a fuller surviving DEV_NOTES dossier [@Campbell1959, §128; @SieversBrunner1965].

## Open questions for later work

- If a final lexeme report is written, decide whether the opening sentence should foreground the dialect choice (`WS dǣd` versus Anglian `dēd`) before introducing the project-only input notation `*dḗdiz`.
- If the live TSV note is ever expanded, consider making the two-level formulation fully explicit: comparative proto `*dēdiz` / `*dédiz`; project modelling input `*dḗdiz`; selected OE target `dǣd`.
- If supporting lexical tables elsewhere in the repo still cite bare `dēd`, decide whether they need dialect labelling so they are less likely to be mistaken for evidence against the live WS row.

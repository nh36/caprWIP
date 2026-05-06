---
row_id: 2100
concept: lid
counterpart: hlid
proto: *xlídą
protoform: *xlídą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2100-lid-hlid.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2100-lid-hlid.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/notable_findings.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2100 lid / hlid

## Current row state

- CONCEPT: `lid`
- COUNTERPART: `hlid`
- PROTO: `*xlídą`
- PROTOFORM: `*xlídą`
- DERIVATION_CLASS: `regular`
- Live TSV note (quoted closely): `Proto: *liθuz → *xlidą (Wiktionary *hlidą 'lid, cover')`. The checked memo is explicit that the earlier `*liθuz` stage is background etymology only, while the live row-level modelling input remains `*xlídą`; for this row `PROTO` and `PROTOFORM` are intentionally the same, and neither should be collapsed into the OE target `hlid` [Germanic/data/germanic-aligned-final.tsv:658; Germanic/docs/lexeme_reports/research_memos/2100-lid-hlid.md:39-46].
- `oe_known_problems.tsv`: no row-local entry survives. The packet records `Matching oe_known_problems.tsv entries` as `_None_`, and the memo repeats that there is no row-specific known-problems item for `hlid` [Germanic/docs/lexeme_reports/packets/2100-lid-hlid.md:45-47; Germanic/docs/lexeme_reports/research_memos/2100-lid-hlid.md:21-27].
- Packet status: the compact derivation trace and orthography block already align with the live row, giving `PROTO: *xlídą`, `EXPECTED: hlid`, `OUTPUTS: hlid`, and `Outcome: hlid`; the packet therefore preserves current resolved state as well as the older `hled` debugging history [Germanic/docs/lexeme_reports/packets/2100-lid-hlid.md:17-42].
- Manifest status: the packet records `_No manifest entry_`, so this slice has to function as the working replacement note rather than as a pointer to a pilot or full report [Germanic/docs/lexeme_reports/packets/2100-lid-hlid.md:11-13].
- Current row-specific DEV_NOTES authority **does exist**, but it is not a standalone lexeme dossier. The packet's exact-hit section says `_None_`, yet its supporting/background extraction preserves the real row-relevant material: the shared `i`-lowering/onset-velar block where `lid` is named directly in the regression table, Lloyd quotation, test cases, and results [Germanic/docs/lexeme_reports/packets/2100-lid-hlid.md:49-52,59-130].

## Development-note summary

Current authority for row 2100 is real but narrow. The row is not unstable at the lexeme level: the live TSV, packet trace, and memo all agree that the project currently models OE `hlid` from `*xlídą`, with `regular` derivation class and no row-local `oe_known_problems.tsv` warning [Germanic/data/germanic-aligned-final.tsv:658; Germanic/docs/lexeme_reports/packets/2100-lid-hlid.md:17-47; Germanic/docs/lexeme_reports/research_memos/2100-lid-hlid.md:12-17,54-65]. The note burden exists because the row still needs an explanation for retained `i`, not because the current OE target is in doubt.

The most securely attachable literature-facing point is Lloyd's retention set. DEV_NOTES quotes Lloyd's list of forms that keep `*i` across dialects: `"OE fisc, OHG, OS fisk, ON fiskr; OE, OS witan, ON vita, OHG wizzan; ON hliþó, OE hlid (Eng. lid), OHG (h)lit"`; the same passage then states that the `lid` case shows retention of `*i` in OE, OHG, and ON, with initial velar `*x` in `*xlidą` [Germanic/docs/DEV_NOTES.md:5653-5656]. That is current source audit for the row, and it supports the attested target `hlid`; it does **not** by itself license a claim that scholarship explicitly recognizes an Old English onset-velar blocking law [Germanic/docs/DEV_NOTES.md:5658-5660; Germanic/docs/lexeme_reports/research_memos/2100-lid-hlid.md:14-17,47-53].

The current project explanation is the shared onset-velar blocking hypothesis, but DEV_NOTES is clear that this is a project inference, not a textbook OE rule. In the assessment block, DEV_NOTES states: `No source explicitly claims onset-velar blocking for Old English`; Cercignani's claim is specific to Old Icelandic, Lloyd instead argues for the non-regularity of `i`-lowering, and the extension to OE is described as `our own hypothesis` supported by the empirical success of the rule [Germanic/docs/DEV_NOTES.md:5673-5708]. The memo repeats exactly that hierarchy: keep `*xlídą` as live modelling input, keep `hlid` as OE target, and describe onset-velar blocking as the repo's successful but cautiously framed explanation rather than as inherited consensus [Germanic/docs/lexeme_reports/research_memos/2100-lid-hlid.md:54-65,74-87].

What DEV_NOTES does authorize strongly is the row's project-history resolution. Before the repair, the FST produced `hled`; after onset-velar blocking was implemented, the test table and result table record `*xlidą | hled | hlid | hlid | ✓ Fixed (onset *x blocks)`, and the packet's compact derivation trace now shows the repaired output `hlid` [Germanic/docs/DEV_NOTES.md:5627-5634,5740-5792; Germanic/docs/lexeme_reports/packets/2100-lid-hlid.md:17-42]. That implementation success is current row authority. The stronger line immediately following it — that the result `confirms` onset-velar blocking as a `real phenomenon in Old English` — is not the best current wording and should be treated only as over-strong project history in light of the caution preserved earlier in the same DEV_NOTES block and repeated in the memo [Germanic/docs/DEV_NOTES.md:5683-5708,5794-5805; Germanic/docs/lexeme_reports/research_memos/2100-lid-hlid.md:14-17,64-65].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-5651-5660

- Source heading: `Lloyd (1966): OE hlid retains *i, but why?`
- Source line or section hint: `lines 5651-5660`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `retained_i`; `source_audit`; `cross_dialect`; `attested_target`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the most directly row-attached literature fragment now in DEV_NOTES. It quotes Lloyd's cross-dialect retention set in full, including `ON hliþó, OE hlid (Eng. lid), OHG (h)lit`, and then glosses the row-level consequence: the `lid` set preserves `*i` in OE, OHG, and ON while the proto-form under discussion is `*xlidą` with initial velar `*x` [Germanic/docs/DEV_NOTES.md:5653-5656]. Its authority is therefore lexical and comparative: it secures `hlid` as the sort of retained-`i` case the row is meant to model. The same fragment also limits itself, because DEV_NOTES immediately adds that Lloyd does **not** explain the outcome through onset-velar blocking but through a broader anti-regular-lowering position, so later prose should quote this fragment for retention/attestation, not as proof that the OE blocking mechanism is already established in the literature [Germanic/docs/DEV_NOTES.md:5658-5660; Germanic/docs/lexeme_reports/research_memos/2100-lid-hlid.md:47-53].

### DEV_NOTES:line-5673-5708

- Source heading: `Assessment: Is onset-velar blocking attested for OE?`
- Source line or section hint: `lines 5673-5708`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `onset_velar_blocking`; `literature_scope`; `novel_extension`; `current_caution`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2034`

This is the controlling caution fragment for row 2100. DEV_NOTES tabulates the literature positions, then states flatly: `No source explicitly claims onset-velar blocking for Old English`; Cercignani's onset-velar statement is for Old Icelandic, not OHG, Lloyd explains retention differently, and the OE application is therefore `a novel extension of the literature, supported by the data (OE hlid retains *i) but not explicitly attested in prior scholarship` [Germanic/docs/DEV_NOTES.md:5677-5687]. The later re-examination and direct-source verification keep exactly the same row policy while firming up the source chain behind the Old Icelandic premise: Gutenbrunner really does say `i zu e ... und nicht nach k, g`, but DEV_NOTES still concludes that `The extension to OE remains our own novel claim` [Germanic/docs/DEV_NOTES.md:5689-5708]. For row 2100 this is securely current authority, because it tells later writers exactly how far to press the argument and exactly where to stop [Germanic/docs/lexeme_reports/research_memos/2100-lid-hlid.md:14-17,54-65,84-87].

### DEV_NOTES:line-5738-5792

- Source heading: `Test cases` and `Results`
- Source line or section hint: `lines 5738-5792`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `implementation_result`; `row_resolution`; `shared_rule_context`; `retained_i_output`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2034`

This fragment is the current project-side proof that the repaired cascade now handles the row as intended. In the test-case table `lid` is explicitly listed with `Velar before? Yes (*x)` and predicted outcome `Block`, actual OE `hlid`; the results table then gives the full before/after comparison `*xlidą | hled | hlid | hlid | ✓ Fixed (onset *x blocks)` and includes the net gain line `+2 matches (lid, fright fixed; no regressions)` [Germanic/docs/DEV_NOTES.md:5740-5792]. This is shared with the companion onset-velar debugging history for `fright`, but for row 2100 the key point is narrow: the current cascade's resolved output is `hlid`, not `hled`, exactly as the packet's compact derivation trace and memo summary also now report [Germanic/docs/lexeme_reports/packets/2100-lid-hlid.md:17-42; Germanic/docs/lexeme_reports/research_memos/2100-lid-hlid.md:14-17,54-65]. Because the fragment is an implementation-success record rather than a source-origin argument, it should be paired with the Lloyd and caution fragments above when cited.

## Superseded or diagnostic material

### DEV_NOTES:line-5621-5634

- Source heading: `Refined analysis: onset velars also block i-lowering (2026-03-09 continued)` plus `The regressions`
- Source line or section hint: `lines 5621-5634`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `old_output`; `hled_regression`; `debugging_history`; `pre_fix_state`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2034`

This fragment is worth preserving because it records the exact pre-fix failure state for the row: after another rule refinement, `lid` appeared in the regression table as `*xlidą | hled | hlid`, with the note that `*i lowered incorrectly`; DEV_NOTES then diagnoses both `lid` and `fright` as words containing velar `*x` somewhere before the relevant `*i` [Germanic/docs/DEV_NOTES.md:5621-5634]. For row 2100 that is diagnostic history only. It should not be cited as current row state, but it is still the clearest explanation of why `lid` re-entered DEV_NOTES at all and why the later onset-velar repair was framed as a regression fix rather than as a fresh lexeme discovery [Germanic/docs/lexeme_reports/packets/2100-lid-hlid.md:61-71; Germanic/docs/lexeme_reports/research_memos/2100-lid-hlid.md:14-17,54-57].

### DEV_NOTES:line-5794-5805

- Source heading: `Theoretical significance`
- Source line or section hint: `lines 5794-5805`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `misleading_if_uncontextualized`
- Issue tags: `overstrong_claim`; `literature_scope`; `novel_extension`; `caution_override`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs: `2034`

This wording should be retained only with an explicit warning label. Immediately after the successful result table, DEV_NOTES says the outcome `confirms that onset-velar blocking is a real phenomenon in Old English` and treats the implementation as a potentially novel finding [Germanic/docs/DEV_NOTES.md:5794-5805]. Taken alone, that sentence overstates current row authority, because the earlier assessment in the same note had already said that no source explicitly claims this for OE and that the OE extension is the project's own hypothesis, and the later memo repeats that more careful position [Germanic/docs/DEV_NOTES.md:5683-5708; Germanic/docs/lexeme_reports/research_memos/2100-lid-hlid.md:14-17,64-65]. Use this fragment only to document an earlier stronger phrasing in repo history, not as the current description of why row 2100 works.

## Open questions for later work

- If later report prose wants a short attestation sentence, decide whether to quote only the Lloyd retention line or to add the memo's dictionary-based clarification that OE `hlid` is an attested noun distinct from unrelated topographic `hlið`; the current slice already preserves the safer minimum, but a full report may want the lexical distinction made explicit [Germanic/docs/lexeme_reports/research_memos/2100-lid-hlid.md:47-53].
- If the TSV note is ever revised elsewhere, keep the present slice's distinction intact: earlier `*liθuz` is background etymology, live modelling input is `*xlídą`, and OE target is `hlid`; the current TSV note compresses those levels more tightly than the memo recommends [Germanic/data/germanic-aligned-final.tsv:658; Germanic/docs/lexeme_reports/research_memos/2100-lid-hlid.md:39-46,80-86].
- If row summaries are indexed later, describe current DEV_NOTES authority as `shared onset-velar/i-lowering block with explicit caution that the OE extension is project-specific`; do not promote the `real phenomenon in Old English` sentence as standalone current authority [Germanic/docs/DEV_NOTES.md:5683-5708,5794-5805].

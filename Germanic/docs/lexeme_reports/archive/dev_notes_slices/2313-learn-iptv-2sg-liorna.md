---
row_id: 2313
concept: "learn (iptv.2sg)"
counterpart: liorna
proto: "*liznōjaną"
protoform: "*líznô"
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2313-learn-(iptv.2sg)-liorna.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2313-learn-(iptv.2sg)-liorna.md
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current_cell_specific_trace_plus_shared_learn_family_background
needs_literature_agent: no
---

# DEV_NOTES material — 2313 learn (iptv.2sg) / liorna

## Current row state

- The live OE row is `2313 | learn (iptv.2sg) | liorna | PROTO *liznōjaną | PROTOFORM *líznô | DERIVATION_CLASS late_analogy`, with the row note `Northumbrian iptv.2sg. Uses io from regular breaking; WS leorna has leveled eo.` The `PROTO`/`PROTOFORM` split is therefore already explicit in the TSV: `*liznōjaną` is the learn-family comparative/project label, while `*líznô` is the imperative-cell input for this row [Germanic/data/germanic-aligned-final.tsv:1474-1474].
- This row is a **non-lemma paradigm-cell companion**, not the learn-family citation-form row. The aligned lemma row remains `2095 | learn | liornian | *líznōjaną | regular`, and the adjacent 3sg cell remains `2314 | learn (3sg) | liornaþ | *líznōθi | late_analogy`; the existing `2095` slice already treats rows `2313` and `2314` as shared-family companions rather than independent lexeme decisions [Germanic/data/germanic-aligned-final.tsv:639-639,1474-1475; Germanic/docs/lexeme_reports/dev_notes_slices/2095-learn-liornian.md:29-41,59-81].
- The current cell-level derivation is clean in the published trace and in the row packet: `PROTO: *líznô`, `EXPECTED: liorna`, `OUTPUTS: liorna`, with the traced steps `Rhotacism: *lírnô`, `OE Breaking: *líornô`, and `OE Unstressed Long Vowel Shortening: *líorna`, ending in `Outcome: liorna` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7256-7276; Germanic/docs/lexeme_reports/packets/2313-learn-(iptv.2sg)-liorna.md:17-43].
- Audit state is quiet but relevant: `coverage_audit.md` flags row `2313` because it has a note and a non-`regular` derivation class, `report_manifest.tsv` has no row-local entry, and `oe_known_problems.tsv` has no corresponding learn-family exception entry [Germanic/docs/lexeme_reports/coverage_audit.md:182-182; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14; Germanic/data/oe_known_problems.tsv:1-8].
- The row memo adds one useful non-DEV_NOTES caution that should remain explicit here: repo-local dictionary-style material still defaults to lemma `leornian`, while Brunner is the best repo-local support for the finite Northumbrian comparator, explicitly giving `leornian, nordh. auch liorna`. That supports calling `liorna` a Northumbrian finite form, but not a dictionary headword [Germanic/docs/lexeme_reports/research_memos/2313-learn-(iptv.2sg)-liorna.md:40-43,64-67].

## Development-note summary

The most important replacement-note fact is negative: row `2313` has **no securely attachable current row-specific DEV_NOTES acceptance block** comparable to the make-family imperative row. The only DEV_NOTES lines that name row `2313` directly are from the abandoned West-Saxon-oriented rewrite `*liznô → *leznô → leorna`; those lines are row-specific, but they are no longer current authority for the live row [Germanic/docs/DEV_NOTES.md:14830-14854; Germanic/docs/lexeme_reports/packets/2313-learn-(iptv.2sg)-liorna.md:49-73].

What is current is instead **shared learn-family support**. Later DEV_NOTES work changed the family diagnosis away from “force WS `leorn-`” and toward “accept Northumbrian `liorn-` as the regular phonological output from the inherited `*lizn-` family, while treating WS `leorn-` as levelled.” The key family statements are that Ringe-Taylor allows `liornian` without an i-umlauting environment, Campbell explains WS `eo` as levelled through, and the project therefore recommends Northumbrian `liornian` as the regular target for the live learn-family row [Germanic/docs/DEV_NOTES.md:15131-15228,15305-15421]. For row `2313`, however, that remains **inherited lexeme/family support**, not a DEV_NOTES sentence written specifically about the imperative 2sg cell.

That distinction matters because this row is a paradigm cell. The current **cell-specific** proof that `*líznô` works as row input comes from the live trace/packet, not from a dedicated DEV_NOTES imperative subsection: the trace shows `*líznô → liorna`, and the memo explicitly frames the decisive contrast as `*líznô -> liorna` versus superseded `*leznô -> leorna` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7256-7276; Germanic/docs/lexeme_reports/research_memos/2313-learn-(iptv.2sg)-liorna.md:84-104].

The safest way to read the row is therefore layered. First, keep `PROTO *liznōjaną` as the learn-family comparator, in line with the current shared transponent policy and the aligned `2095` slice [Germanic/docs/DEV_NOTES.md:37888-37898; Germanic/docs/lexeme_reports/dev_notes_slices/2095-learn-liornian.md:31-41,45-69]. Second, keep `PROTOFORM *líznô` and OE `COUNTERPART liorna` as the row-local imperative selection because the live trace now derives them cleanly [Germanic/data/germanic-aligned-final.tsv:1474-1474; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7256-7276]. Third, treat WS `leorna` and all `*lezn-` material as comparator background or superseded history rather than as hidden current authority for this cell [Germanic/docs/DEV_NOTES.md:14748-14854,15305-15421].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-37888-37898

- Source heading: `§17.32.7 The choice: very-early vs very-late analogy`
- Source line or section hint: `lines 37888-37898`
- Fragment type: `current_shared_learn_family_policy`
- Status: `current`
- Issue tags: `transponent_policy`; `learn_family`; `proto_vs_protoform`; `shared_not_cell_specific`
- Recommended next use: `cite_to_keep_row_2313_aligned_with_row_2095`
- Shared with row IDs: `2095, 2314`

This is the clearest current DEV_NOTES policy fragment that still bears on row `2313`, but it is **family-level**, not imperative-cell-specific. DEV_NOTES says the class-III→II refashioning is taken at the `(West-)Germanic → pre-OE` stage, that the TSV `PROTOFORM` is a `transponent in the strict sense`, and that the FST already derives verbs such as `líznōjaną → liornian` regularly from that shape [Germanic/docs/DEV_NOTES.md:37888-37898]. For this row, the fragment matters because it supports keeping the learn family under `*lizn-` rather than reviving the old `*lezn-` rewrite; but it does **not** by itself prove that the imperative 2sg cell should be `liorna`. That last step still comes from the row trace and memo [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7256-7276; Germanic/docs/lexeme_reports/research_memos/2313-learn-(iptv.2sg)-liorna.md:84-104].

> `... the FST now produces 'sparian' by regular sound change from this shape, exactly as it does for the other class-III→II refashioned verbs already in the TSV ('búrōjaną → borian', 'líznōjaną → liornian', ...)` [Germanic/docs/DEV_NOTES.md:37894-37898]

### DEV_NOTES:line-15129-15421

- Source heading: ``The `leornian` problem revisited`` / `The *leornian* Problem (Campbell §154.3 footnote 3)`
- Source line or section hint: `lines 15129-15421`
- Fragment type: `current_shared_background_for_northumbrian_targeting`
- Status: `current_background`
- Issue tags: `northumbrian_vs_ws`; `breaking_of_i`; `ws_leveling`; `inherited_family_support`
- Recommended next use: `cite_to_explain_why_liorna_is_inherited_regular_support_not_unique_cell_note`
- Shared with row IDs: `2095, 2314`

This is the most important current DEV_NOTES reasoning for the live family posture. DEV_NOTES says that, for the learn family, Ringe-Taylor gives `Northumbrian liornian` as the regular output with **no i-umlaut**, while West-Saxon `leornian` requires paradigmatic leveling and the later `io/eo` merger; the section then explicitly recommends using the Northumbrian target rather than trying to force the levelled WS form as if it were the direct phonological output [Germanic/docs/DEV_NOTES.md:15131-15228,15305-15421].

For row `2313`, this fragment is crucial but inherited. It tells later readers **why** a Northumbrian `liorn-` row family is now acceptable and why West-Saxon `leorn-` should be demoted to comparator status. It does **not** directly discuss the imperative 2sg cell `liorna`; instead it supplies the family-level phonological backdrop that makes the row note `Uses io from regular breaking; WS leorna has leveled eo` intelligible [Germanic/data/germanic-aligned-final.tsv:1474-1474].

> `This is NOT a regular phonological development — it involves morphological leveling. Our FST cannot model this.` [Germanic/docs/DEV_NOTES.md:15149-15150]

> `eo would appear to have been levelled through, and then mutated before -i-, giving rise to eW-S liornian, North. liornta` [Germanic/docs/DEV_NOTES.md:15305-15308]

> `TSV update: Change the target for *liznōjăną variants from WS leornian (analogical) to Northumbrian liornian (regular phonological outcome).` [Germanic/docs/DEV_NOTES.md:15420-15421]

### DEV_NOTES:line-14863-14916

- Source heading: `Extended Research (2026-04-07)`
- Source line or section hint: `lines 14863-14916`
- Fragment type: `background_source_audit_for_learn_family`
- Status: `background`
- Issue tags: `source_audit`; `lizn_not_lezn`; `io_eo_variation`; `useful_direct_quotes`
- Recommended next use: `cite_for_exact_family-level quotations_only`
- Shared with row IDs: `2095, 2314`

This fragment is not a current row policy block, but it preserves the best exact quotations for the learn family. It records that Kroonen reconstructs only `*liznōn-`, that Ringe-Taylor likewise use `*lizn-` forms, and that Campbell explicitly recognizes Northumbrian `io` beside West-Saxon `eo` [Germanic/docs/DEV_NOTES.md:14863-14916]. Those quotations are worth preserving in this slice because they keep later writers from overstating `*lezn-` as the comparative default or from pretending that `liorna` lacks any family-level philological context.

For row `2313`, the strongest retained quotation is Campbell's dialect warning: `Beside leornian, forms with io are found in North.` The second key quotation is §202's statement that `the mutation of eo was io ... and never have ie`, which is exactly the sort of precise wording later prose may need when distinguishing regular Northumbrian `liorn-` from levelled West-Saxon `leorn-` [Germanic/docs/DEV_NOTES.md:14889-14916].

> `Beside leornian, forms with io are found in North., where original eo and io are well distinguished, and reflect a Prim. OE variation of e and i.` [Germanic/docs/DEV_NOTES.md:14890-14892]

> `the mutation of eo was io ... and never have ie` [Germanic/docs/DEV_NOTES.md:14906-14912]

### DEV_NOTES:line-14748-14854

- Source heading: `Analysis options` / `Decision` / `Recommendation` / `Solution (2026-04-07)`
- Source line or section hint: `lines 14748-14854`
- Fragment type: `row_specific_superseded_rewrite`
- Status: `superseded`
- Issue tags: `ws_retargeting`; `e_grade_workaround`; `explicit_row_2313_history`
- Recommended next use: `use_only_to_explain_old_row_history`
- Shared with row IDs: `2095, 2314`

This is the only DEV_NOTES fragment that speaks to row `2313` **directly by row number**, and it is precisely why later users can be misled if the slice is not explicit. DEV_NOTES first recommends `Row 2313: Change *liznô to *leznō`, then the solution table records `2313 | *liznô | *leznô | leorna` [Germanic/docs/DEV_NOTES.md:14830-14854]. That material has real historical value because it documents the earlier West-Saxon-targeting phase. But it is no longer current: the live TSV now keeps `*líznô` and targets Northumbrian `liorna`, while the aligned `2095` slice already classifies this whole block as superseded learn-family history [Germanic/data/germanic-aligned-final.tsv:1474-1474; Germanic/docs/lexeme_reports/dev_notes_slices/2095-learn-liornian.md:71-81].

> `- Row 2313: Change *liznô to *leznō (iptv.2sg uses stem + *-ō)` [Germanic/docs/DEV_NOTES.md:14830-14833]

> `| 2313 | *liznô | *leznô | leorna |` [Germanic/docs/DEV_NOTES.md:14849-14854]

## Superseded or diagnostic material

- The earliest direct imperative-cell diagnostic survives at `DEV_NOTES.md:2950-2979`: the results table records `liznô | lierna | leorna | ✗`, and the following subsection labels the issue `Stressed vowel ie vs eo (*liznô → lierna vs leorna)` [Germanic/docs/DEV_NOTES.md:2950-2979]. This is useful only as pre-retargeting project history. It documents the original mismatch against West-Saxon `leorna`, not the current live Northumbrian row `liorna`.
- The packet's row-ID hits at `14832` and `14853` should never be quoted without a superseded label. They are exact row-local hits, but they preserve the abandoned `*leznô / leorna` phase rather than the live row state [Germanic/docs/lexeme_reports/packets/2313-learn-(iptv.2sg)-liorna.md:49-73].
- Generic learn-family discussion of `leornian` in DEV_NOTES is relevant only when clearly marked as **shared**. Because row `2313` is a finite cell, lemma-level reasoning about `liornian/leornian` cannot automatically be promoted to cell-specific imperative evidence without saying so explicitly [Germanic/docs/DEV_NOTES.md:15131-15228,15305-15421; Germanic/docs/lexeme_reports/research_memos/2313-learn-(iptv.2sg)-liorna.md:69-80].
- The current row should stay aligned with the existing `2095` slice's family classification: one current shared policy fragment, one current/background Northumbrian-targeting correction trail, one background source-audit fragment, and one superseded `*lezn-` rewrite block. Reopening `2313` as if it had its own independent current DEV_NOTES decision would break that alignment [Germanic/docs/lexeme_reports/dev_notes_slices/2095-learn-liornian.md:45-81].

## Open questions for later work

- If `dev_notes_slices/index.tsv` is revised later, should row `2313` get its own entry, or should the learn family stay indexed primarily under row `2095` with row `2313` treated as a slice-only companion that inherits shared fragments plus row-local diagnostics [Germanic/docs/lexeme_reports/dev_notes_slices/2095-learn-liornian.md:45-81; Germanic/docs/lexeme_reports/coverage_audit.md:182-182]?
- If a future dossier is assembled for the finite learn forms, add direct manuscript/grammar support for `liorna` itself rather than relying on the current memo-level Brunner note and the family-level Campbell quotations [Germanic/docs/lexeme_reports/research_memos/2313-learn-(iptv.2sg)-liorna.md:40-43,64-67].
- If DEV_NOTES cleanup happens later, mark the old `2956` diagnostic and the `14832/14853` row-local rewrite more explicitly as superseded WS-phase history so later slice drafting does not mistake them for live authority [Germanic/docs/DEV_NOTES.md:2950-2979,14830-14854].

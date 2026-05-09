---
row_id: 2116
concept: lye
counterpart: lēag
proto: *láugō
protoform: *láugō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/dossier-leek-2026.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2116 lye / lēag

## Current row state

- The live Old English row now has `COUNTERPART = lēag`, `PROTO = *láugō`, `PROTOFORM = *láugō`, and `DERIVATION_CLASS = regular`; the row note is already explicit about the normalization logic: `Normalizing to -g spelling per Bülbring §489; both leag/læg attested` [Germanic/data/germanic-aligned-final.tsv:721-721].
- `PROTO` and `PROTOFORM` are **not split** here. `*láugō` is both the comparative proto headword and the actual derivational input for the OE cascade; the only historically disputed part of the row was the target-side OE spelling convention (`lēah` vs. `lēag`), not the proto reconstruction [Germanic/data/germanic-aligned-final.tsv:721-721; Germanic/docs/DEV_NOTES.md:10909-10917,10990-11024].
- `coverage_audit.md` still shows no packet, no research memo, no linked dossier/analysis file, and overall status `none`, so this slice is replacing direct DEV_NOTES consultation without any separate lexeme packet infrastructure [Germanic/docs/lexeme_reports/coverage_audit.md:303-303].
- The published derivation trace already matches the live target without workaround: `PROTO: *láugō`, `EXPECTED: lēag`, `OUTPUTS: lēag`, with the chain `*láugō > *láugu > *láeugu > *lēagu > *lēag` via NWGmc final long-`ō` raising, OE `au` fronting, OE diphthong leveling, and OE high-vowel apocope [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3064-3083].
- The inherited Wiktionary support file still gives `lye    lēah`, so the repo continues to preserve evidence of the older target convention even though the live row has moved to `lēag` [Germanic/data/old_english_wiktionary.tsv:177-177].

## Development-note summary

No standalone row-specific `DEV_NOTES` block for `lye / lēag / *láugō` survives. The usable material is concentrated in one shared `Word-Final *g Spirantization Research (2026-03-15)` cluster plus one later narrow diagnostic table. That shared cluster nevertheless contains the essential row history: the mismatch was recorded as ``*laugō` → `lēag` (expected `lēah`)`, meaning the transducer was already producing `lēag`; the dispute was whether the dataset should normalize this word-final reflex to Late West Saxon `-h` or keep attested/conservative `-g` [Germanic/docs/DEV_NOTES.md:10905-10917].

The strongest surviving **row-specific** support inside that shared note is Bülbring-based attestation. DEV_NOTES first warns that `§514 index: "leag 'log'"` is actually the preterite of *lie* and therefore irrelevant for this noun, then gives the directly relevant statement: `Bülbring footnote mentions "leag 'Lauge' (læg Erf., Corp.)" — confirming both leag and læg spellings for 'lye'` [Germanic/docs/DEV_NOTES.md:11008-11011]. That is the best in-DEV_NOTES lexeme-level support for the current target.

The rest of the section is mostly **shared-background-only but still controlling**. DEV_NOTES quotes Campbell that for final `ɣ` “there is an increasing use of the symbol `h` after Alfred's time,” then stresses that the `h/g` alternation was “not categorical” and even allowed “inverted spellings” with `g` for expected `h` [Germanic/docs/DEV_NOTES.md:10920-10937]. On that basis the note judges the TSV inconsistent by convention, not by reconstruction, and chooses `Option D with -g convention`, implementing `lēah → lēag` and `troh → trog` while explicitly **not** adding a new final-spirantization rule [Germanic/docs/DEV_NOTES.md:10959-11030]. For this row, that shared policy decision is the controlling current explanation.

Outside `DEV_NOTES`, one repo-local supporting file is genuinely useful but should be labeled **shared background rather than row-local DEV_NOTES evidence**: the leek dossier preserves Campbell §225, including `"The smoothing of éa has still not taken place in a number of forms preserved in Ep.: léag lye, fléah flea ..."` [Germanic/docs/dossier-leek-2026.md:71-80]. This supports the reality of an unsmoothed `léag`/`lēag` type in OE evidence, but it is not the note that drove the repo's target update.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-10905-10917

- Source heading: `Word-Final *g Spirantization Research (2026-03-15)` / `The Problem`
- Source line or section hint: `lines 10905-10917`
- Fragment type: `shared_problem_definition_with_row_specific_example`
- Status: `diagnostic_but_still_useful`
- Issue tags: `g_vs_h`; `target_history`; `not_proto_change`; `row_pair_with_2265`
- Recommended next use: `use_to_explain_why_target_changed_without_reconstructing_a_new_protoform`
- Shared with row IDs: `2265`

This is the cleanest statement of the original row problem. DEV_NOTES says: `The mismatch report shows two cons_mismatch__g_vs_h__word_final errors: - *laugō → lēag (expected lēah) - *trugą → trog (expected troh)` [Germanic/docs/DEV_NOTES.md:10909-10911]. For row 2116 the force of that wording is exact: the FST output was already `lēag`; the then-current expected target was `lēah`. So the surviving issue is not a problem with `PROTO = *láugō`, not a problem with `PROTOFORM = *láugō`, and not evidence that a special derivational workaround was needed. It is a spelling-normalization conflict at the OE endpoint.

### DEV_NOTES:line-10920-10937

- Source heading: `Source Research`
- Source line or section hint: `lines 10920-10937`
- Fragment type: `shared_phonology_and_spelling_background`
- Status: `current_shared_background_only`
- Issue tags: `Campbell`; `final_ɣ`; `orthographic_variation`; `late_ws_vs_early_g`
- Recommended next use: `cite_when_explaining_why_both_lēah_and_lēag_can_be_real`
- Shared with row IDs: `1960, 1993, 2265`

This fragment is not specific to `lye`, but it is the shared historical frame that makes the row intelligible. DEV_NOTES quotes Campbell §446: `"The voicing of medial spirants was followed by the unvoicing of final spirants ... but for final ɣ there is an increasing use of the symbol h after Alfred's time."` It then adds Campbell §447: `"The interchange of h and g in forms like burh—burge ... There are also inverted spellings like mearg, burg ..."` and summarizes that the alternation was `not categorical` [Germanic/docs/DEV_NOTES.md:10920-10937]. For row 2116, this should be used only as **shared-background-only** support: it explains why `lēah` can be a real late spelling without forcing the project to abandon `lēag` as the normalized target.

### DEV_NOTES:line-10996-11011

- Source heading: `Research confirming -g spellings are attested`
- Source line or section hint: `lines 10996-11011`
- Fragment type: `row_specific_attestation_note_inside_shared_policy_section`
- Status: `current`
- Issue tags: `Bülbring`; `attestation`; `lēag`; `læg`; `false_friend_warning`
- Recommended next use: `primary_row_level_attestation_anchor`
- Shared with row IDs:

This is the most important surviving lexeme-level DEV_NOTES passage. It first warns against a misleading hit: `"lēag 'lye': Attested in Bülbring (§514 index: 'leag 'log'') — note this is the preterite 'lied', not 'lye', but shows the spelling convention."` That warning matters because it prevents accidental citation of the wrong lexeme [Germanic/docs/DEV_NOTES.md:11008-11009]. The row-specific substance follows immediately: `"More directly: Bülbring footnote mentions 'leag 'Lauge' (læg Erf., Corp.)' — confirming both leag and læg spellings for 'lye'."` [Germanic/docs/DEV_NOTES.md:11010-11011]. For this row, that sentence is the best surviving in-DEV_NOTES evidence that the dataset's `-g` normalization is tied to actual lexical attestation, not merely to transducer convenience.

### DEV_NOTES:line-10959-11030

- Source heading: `Analysis`; `Options`; `Decision: Use -g Spelling Convention (2026-03-15)`
- Source line or section hint: `lines 10959-11030`
- Fragment type: `current_row_policy_in_shared_section`
- Status: `current`
- Issue tags: `live_row_policy`; `target_normalization`; `no_new_rule`; `shared_decision`
- Recommended next use: `controlling_anchor_for_current_row_state`
- Shared with row IDs: `2265`

This is the controlling current fragment. DEV_NOTES states the inconsistency explicitly: ``lēah`, `troh` use the Late WS `h` convention` while ``bōg`, `dāg` use the earlier/Northumbrian `g` convention` [Germanic/docs/DEV_NOTES.md:10959-10961]. It then selects `"Option D with -g convention (early/Northern spelling)"`, says this avoids adding a sound-change rule, and records the actual implementation step `Update TSV targets: lēah → lēag, troh → trog` [Germanic/docs/DEV_NOTES.md:10990-11024]. For row 2116 this is decisive and current, but it should be described accurately as **shared policy with direct row impact**, not as a bespoke lye-only phonological study.

## Superseded or diagnostic material

- The superseded material is the **older target convention** `lēah`, not the proto reconstruction. The inherited support file still has `lēah`, and the original mismatch note still shows `*laugō → lēag (expected lēah)`; DEV_NOTES later supersedes that target by choosing `-g` normalization and explicitly updating `lēah → lēag` [Germanic/data/old_english_wiktionary.tsv:177-177; Germanic/docs/DEV_NOTES.md:10909-10917,10990-11024].
- The later `*aw+j` risk audit is **diagnostic only** for this row. It lists `2116 *láugō lēag lēag ✓ no *j present` and the regression-risk table classifies `Other *Vw *dáwwō, *láugō — no *j present` as `NONE` [Germanic/docs/DEV_NOTES.md:26619-26629,26678-26685]. That material does not explain why `lēag` is chosen; it only marks row 2116 as a safe non-target when testing narrow `*aw+j` interventions elsewhere.
- No standalone row-specific DEV_NOTES dossier survives for `lye / lēag`. The replacement slice therefore has to be conservative: the attestation note at `11008-11011` is row-specific, but most remaining support is shared spelling-policy background rather than a dedicated lexeme memorandum [Germanic/docs/DEV_NOTES.md:10920-11030].
- The non-DEV_NOTES Campbell §225 quotation preserved in `dossier-leek-2026.md` is supportive but should stay secondary. It is useful as shared lexical background for unsmoothed `léag lye`, yet it did not drive the repository's actual `lēah → lēag` decision [Germanic/docs/dossier-leek-2026.md:71-80].

## Open questions for later work

- If row 2116 ever needs an `index.tsv` anchor, decide whether the shared policy block plus the short Bülbring attestation note are sufficient, or whether a fuller direct source extract for `leag/læg 'Lauge'` should be added to the repo.
- If later literature work revisits this row, verify the exact witness and dialect status behind DEV_NOTES' `"leag 'Lauge' (læg Erf., Corp.)"` shorthand, since that line is currently doing most of the row-specific attestation work [Germanic/docs/DEV_NOTES.md:11010-11011].
- Keep the distinctions fixed in future edits: `PROTO = *láugō` and `PROTOFORM = *láugō` are stable; the historically moving part was the OE target convention (`lēah` inherited from older source import vs. `lēag` adopted as current normalization) [Germanic/data/germanic-aligned-final.tsv:721-721; Germanic/docs/DEV_NOTES.md:10909-11024].

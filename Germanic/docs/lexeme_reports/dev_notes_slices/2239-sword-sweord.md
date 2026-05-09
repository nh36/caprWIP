---
row_id: 2239
concept: sword
counterpart: sweord
proto: "*swérdą"
protoform: "*swérdą"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/mismatch_dossier_mizdo.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2239 sword / sweord

## Current row state

- The live OE row now reads `CONCEPT = sword`, `COUNTERPART = sweord`, `PROTO = *swérdą`, `PROTOFORM = *swérdą`, and `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1198-1198].
- `PROTO` and `PROTOFORM` are currently identical, so the row is not using a substitute paradigm cell, a repaired stage-form, or a special OE-facing input. `COUNTERPART` remains separately the OE citation form `sweord` [Germanic/data/germanic-aligned-final.tsv:1198-1198; @ClarkHall1960, s.v. "sweord"].
- The published derivation trace is an exact match and gives the row's active regular pathway explicitly: `Proto Input: *swérdą`, `OE Breaking: *swéordą`, `OE Heavy Syllable Nasal Apocope: *swéord`, `Outcome: sweord` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5077-5087].
- `oe_known_problems.tsv` has no entry naming row `2239`, `sword`, `sweord`, or `*swérdą`, which is consistent with the row's present regular status rather than an exception-classification workflow [Germanic/data/oe_known_problems.tsv:1-8].

## Detailed development-note summary

The surviving DEV_NOTES support for row 2239 is thin and mostly shared, but it is still coherent enough to serve as a replacement working note. DEV_NOTES does **not** preserve a sword-specific correction dossier, rival `COUNTERPART`, or alternative `PROTOFORM`. The live row and the published trace both treat `*swérdą -> sweord` as an ordinary OE breaking outcome before `r + consonant`, with no need to split `PROTO` from `PROTOFORM` and no need to retarget the OE noun away from `sweord` [Germanic/data/germanic-aligned-final.tsv:1198-1198; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5077-5087; @ClarkHall1960, s.v. "sweord"].

What DEV_NOTES does preserve is later West-Saxon variant background. The short handbook-summary block on initial-labial effects says `weo → wo → wu` and gives `late WS weorpan → wurpan, sweord → swurd` as examples [Germanic/docs/DEV_NOTES.md:214-219; @Bulbring1902, §§265-268]. The longer Kaluza quotation keeps the same point in source language: `"Ae. e, eo, das durch Brechung oder u-Umlaut aus urg. e entstanden war, wird durch vorhergehendes w zu o, u verdunkelt: sword, swurd neben sweord Schwert ..."` [Germanic/docs/DEV_NOTES.md:33419-33424; @Kaluza1906, p. 178 §57n]. For row 2239 this material is useful only if it is labeled carefully: `swurd` and `sword` are later variant comparators, not the live `COUNTERPART`, not rival `PROTOFORM` values, and not evidence that the regular OE target should be rewritten.

DEV_NOTES also preserves the project's present policy judgment on that late rounding, even though the note occurs inside the much larger `swester/swustor` dossier. When the project considers adding a late `swe- -> swu-/swo-` rule, it warns that the phenomenon is not a general sound law and would have to be lexically restricted to a few forms, explicitly including `sweord` [Germanic/docs/DEV_NOTES.md:33636-33653]. The later recommendation section repeats the same implementation caution: adding such a rule to `germanic.txt` would be hard to constrain to the right lexemes (`swester`, `weorld`, `sweord`) without over-generating [Germanic/docs/DEV_NOTES.md:33727-33730]. For row 2239 the practical conclusion is straightforward: keep the regular row `*swérdą -> sweord` as current, and treat `swurd/sword` only as later West-Saxon variant background rather than as a transducer target [@Bulbring1902, §§265-268; @Kaluza1906, p. 178 §57n].

The extra row-local infrastructure aligns with that conservative reading. The published OE trace shows exactly the regular path `*swérdą -> *swéordą -> sweord`, and the comparative audit in `mismatch_dossier_mizdo.md` uses `sweord` as one of the control cases proving that breaking applies regularly in `*-rd-` environments where it should [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5077-5087; Germanic/docs/analysis/mismatch_dossier_mizdo.md:529-535]. That supporting material does not create a new row policy, but it confirms that the surviving DEV_NOTES fragments are best read as variant-history background around an otherwise regular row.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-214-219

- Source heading: `Related: effects of initial labials on vowels (Bülbring §§260-274)`
- Source line or section hint: `lines 214-219`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `late_ws_rounding`; `w_influence`; `variant_background`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This is the shortest surviving DEV_NOTES statement that directly names the row's later variant terrain: `weo → wo → wu (§§265-268): late WS weorpan → wurpan, sweord → swurd` [Germanic/docs/DEV_NOTES.md:218-218]. It is useful because it cleanly separates the late West-Saxon variant from the live row target. For row 2239 it should be cited only as background on later `swurd`, not as authority to replace `sweord` [@Bulbring1902, §§265-268].

### DEV_NOTES:line-33419-33438

- Source heading: `Kaluza: labial darkening`
- Source line or section hint: `lines 33419-33438`
- Fragment type: `source_preserving_variant_background`
- Status: `diagnostic_only`
- Issue tags: `direct_quotation`; `late_ws_variant`; `darkening_after_w`; `shared_handbook_material`
- Recommended next use: `quote_if_variant_history_is_needed`
- Shared with row IDs:

This fragment is worth preserving because it carries the source quotation rather than only a paraphrase. DEV_NOTES cites Kaluza's formulation: `"Ae. e, eo, das durch Brechung oder u-Umlaut aus urg. e entstanden war, wird durch vorhergehendes w zu o, u verdunkelt: sword, swurd neben sweord Schwert ..."` [Germanic/docs/DEV_NOTES.md:33421-33424]. The surrounding prose then glosses this as a late form-set and explicitly lists `sword, swurd` as late-West-Saxon variants of `sweord` [Germanic/docs/DEV_NOTES.md:33432-33438; @Kaluza1906, p. 178 §57n]. For row 2239 the fragment is diagnostic and source-preserving, but it still does not justify changing the live row away from `sweord`.

### DEV_NOTES:line-33636-33653

- Source heading: `Option B disadvantages / Verdict`
- Source line or section hint: `lines 33636-33653`
- Fragment type: `current_project_policy_context`
- Status: `current`
- Issue tags: `no_general_rounding_rule`; `lexical_restriction`; `sweord_as_comparator`; `implementation_policy`
- Recommended next use: `cite_if_row_policy_needs_defense`
- Shared with row IDs: `2192`

This fragment matters because it records the project's current decision about whether late rounding like `sweord -> swurd` belongs in the transducer. DEV_NOTES says the putative rule would have to be lexically restricted, applying only to forms such as `swester, weorld, sweord`, and therefore would be a lexical exception rather than a general sound law [Germanic/docs/DEV_NOTES.md:33641-33643]. The verdict is explicit: `Not recommended` for inclusion in `germanic.txt` [Germanic/docs/DEV_NOTES.md:33650-33653]. For row 2239 this is the clearest surviving policy anchor: the live target should stay `sweord`, while later `swurd/sword` remains variant material outside the ordinary cascade.

## Superseded or diagnostic material

- No securely attachable DEV_NOTES fragment preserves a superseded row-local `PROTO`, `PROTOFORM`, or `COUNTERPART` for `sword / sweord`. The row's surviving DEV_NOTES history is mostly not about lexical replacement at all; it is about later West-Saxon variant background and about a separate `swester/swustor` policy debate that happens to cite `sweord` as a comparator [Germanic/docs/DEV_NOTES.md:33419-33438; Germanic/docs/DEV_NOTES.md:33636-33653].
- The non-live forms here are `swurd` and `sword`. They should remain visible only as labeled late variants or handbook comparators, not as current row targets [Germanic/docs/DEV_NOTES.md:218-218; Germanic/docs/DEV_NOTES.md:33421-33424; @Bulbring1902, §§265-268; @Kaluza1906, p. 178 §57n].
- The `swester` recommendation lines that mention `sweord` are useful project-policy evidence, but they are still shared material rather than a dedicated sword note. Later writers should not overread them as if DEV_NOTES had carried out an independent lexeme-level reanalysis of row 2239 [Germanic/docs/DEV_NOTES.md:33636-33653].

## Open questions for later work

- If `index.tsv` is updated later, decide whether row 2239 should receive any entry at all or whether the surviving material is too shared and variant-oriented to justify indexing. The strongest candidate fragment is `DEV_NOTES:line-33636-33653`, but even that fragment is shared policy context rather than a sword dossier.
- If a later full report wants a variant paragraph, keep the distinction explicit: regular row target `sweord` versus later West-Saxon variants `swurd/sword`, with the latter cited from Bülbring/Kaluza and kept outside the ordinary FST target path [@Bulbring1902, §§265-268; @Kaluza1906, p. 178 §57n].
- If a shared dossier on late `weo -> wo/wu` rounding after initial `w` is ever created, row 2239 should probably link there instead of trying to manufacture a sword-specific DEV_NOTES controversy that the surviving record does not actually contain.

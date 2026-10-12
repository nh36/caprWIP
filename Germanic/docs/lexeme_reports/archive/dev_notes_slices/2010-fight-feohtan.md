---
row_id: 2010
concept: fight
counterpart: feohtan
proto: *féxtaną
protoform: *féxtaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2010 fight / feohtan

## Current row state

- The live OE row is currently an exact regular match: `CONCEPT = fight`, `COUNTERPART = feohtan`, `PROTO = *féxtaną`, `PROTOFORM = *féxtaną`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:310-310].
- `PROTO` and `PROTOFORM` are identical in the live TSV, so this row is **not** presently being handled by a substitute OE-facing paradigm cell, an analogical rescue input, or a corrected alternate reconstruction. The comparative label and the derivational input are both written `*féxtaną` in current project state [Germanic/data/germanic-aligned-final.tsv:310-310].
- The published derivation trace is already exact and gives the current project chronology explicitly: `PROTO: *féxtaną`, `EXPECTED: feohtan`, `OUTPUTS: feohtan`, with OE-side steps `OE Breaking: *féoxtaną`, `OE Heavy Syllable Nasal Apocope: *féoxtan`, `OE Secondary Nasalization: *féoxtąn`, `OE Weak Tail Reduction: *féoxtan`, and orthographic `Old English Orthography: *féohtan`, `Outcome: feohtan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1259-1279].
- `oe_known_problems.tsv` has no row-specific entry for row `2010`, for `fight`, or for `*féxtaną`; the current file lists unrelated exception buckets only [Germanic/data/oe_known_problems.tsv:1-8].
- `coverage_audit.md` classifies row `2010` as a regular row with no note and no pre-existing report requirement (`Requirement basis = none`), so this slice is replacement working documentation rather than continuation of an earlier required-report chain [Germanic/docs/lexeme_reports/coverage_audit.md:236-236].
- No row-2010 packet, research memo, or manifest entry was found in the present lexeme-report materials. `report_manifest.tsv` currently contains only pilot entries for other rows, and the search pass for `2010`, `fight`, `feohtan`, and `*féxtaną` found no row-specific packet or memo to inherit a different filename stem from [Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].

## Development-note summary

No dedicated row-2010 DEV_NOTES dossier currently survives. What survives is still useful, but it is mostly **shared control-case material** plus later audit prose, not a bespoke `feohtan` memo. The strongest current row-explicit fragment is the later `*x`-loss audit, which lists `2010 *féxtaną -> feohtan` among the preserved `*xt` rows [Germanic/docs/DEV_NOTES.md:39278-39284]. The main supporting source audit is Campbell's quoted statement that in Primitive OE the only inherited internal `x` + voiceless-consonant cluster was `xt`, and that this cluster remained, with examples including `"feohtan fight ... miht might, niht night"` [Germanic/docs/DEV_NOTES.md:39045-39056].

That means the safest current interpretation is narrow but solid. `PROTO = PROTOFORM = *féxtaną` is the live derivational input, and the current cascade reaches exact `feohtan` without special repair machinery [Germanic/data/germanic-aligned-final.tsv:310-310; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1259-1279]. The row should therefore be described as a regular preserved-`*xt` witness, not as an unresolved deletion problem and not as a row whose OE target depends on an alternate paradigm cell.

The main conditioning distinction that later writers must keep explicit is **`*xt` preservation vs. preconsonantal `*xsC` loss**. DEV_NOTES' broad research dossier says the classic loss rule is narrowly about `*xs` followed by another consonant, citing examples such as `wæstm` and `sesta`; it is not a blanket rule deleting `x` before any consonant cluster [Germanic/docs/DEV_NOTES.md:39023-39044]. `feohtan` belongs on the other side of that boundary. In the current project record it is one of the lexemes used to show that inherited `*xt` remains and should stay out of the `*xs+C` deletion bucket [Germanic/docs/DEV_NOTES.md:39045-39056,39278-39284].

Later DEV_NOTES material mentions the row only as a collateral-risk check. During the `ten / tēon` contraction repair, the audit explicitly searched the `*[eé]x` cohort and recorded that `*féxtaną`, like `*séxs`, `*wéxtiz`, and `*knéxtaz`, has `*x + C`, not `*x + V`, so the new contraction clauses should not touch it [Germanic/docs/DEV_NOTES.md:42450-42455,42499-42500,42633-42638]. That is useful project history because it confirms that subsequent rule work was checked against row 2010. It is **not** a row-specific philological explanation of `fight / feohtan` in the same sense as a dedicated lexeme dossier would be.

The replacement note should therefore remain conservative. Current project evidence supports row 2010 as a stable regular exact-match row and preserves one row-explicit DEV_NOTES anchor plus one strong quoted handbook anchor. But it does **not** preserve a rich row-local mismatch narrative, an alternate `PROTOFORM`, or a separate attestation-status discussion beyond the fact that the selected OE target is the live exact output `feohtan` [Germanic/data/germanic-aligned-final.tsv:310-310; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1259-1279; Germanic/docs/DEV_NOTES.md:39045-39056,39278-39284].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-39278-39284

- Source label line: `DEV_NOTES:line-39278-39284`
- Source heading: `Corpus rows that depend on the current loss rule`
- Source line or section hint: `lines 39278-39284`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `xt_cluster`; `control_case`; `preconsonantal_x_loss`; `preserved_ht`
- Recommended next use: `cite_if_explaining_why_row_stays_regular`
- Shared with row IDs: `2086`, `2102`, `2125`, `2140`, `2291`

This is the clearest surviving row-explicit DEV_NOTES attachment. Under the `*xt` subgroup, DEV_NOTES lists `2010 *féxtaną → feohtan` beside `*knéxtaz → cniht`, `*léuxtijaną → līehtan`, `*máxtiz → miht`, `*náxti → niht`, and `*wéxtiz → wiht` [Germanic/docs/DEV_NOTES.md:39278-39284]. The force of the fragment comes from the sentence immediately above and below the list: the surrounding audit contrasts `*xs` rows that do **not** need the loss rule with `*xt` rows preserved per Campbell §464, so `feohtan` is being used as one of the current control witnesses for the project's preserved-`*xt` behavior, not as a suspected failure case [Germanic/docs/DEV_NOTES.md:39260-39284].

For row 2010, this fragment is more valuable than a bare search hit because it records current project policy in row-numbered form. It shows that the row is not merely tolerated by the present grammar; it is part of the evidence set used to verify that the loss rule has not been overgeneralized into the `*xt` environment. If later reporting needs one short DEV_NOTES citation explaining why the row remains regular, this is the best surviving anchor [Germanic/docs/DEV_NOTES.md:39260-39284].

### DEV_NOTES:line-39045-39056

- Source label line: `DEV_NOTES:line-39045-39056`
- Source heading: `Campbell §464` quoted inside the `*x`-loss research dossier
- Source line or section hint: `lines 39045-39056`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `campbell`; `xt_preservation`; `quoted_source`; `shared_rule_authority`
- Recommended next use: `cite_as_shared_rule_authority`
- Shared with row IDs: `2086`, `2102`, `2125`, `2140`, `2291`

This fragment does not open as a dedicated `fight` note, but it preserves the strongest quoted source authority now attached to the row. DEV_NOTES copies Campbell's wording: `"x remained finally in OE (written h) … Internally, since xs > ks (§ 416), the only group in which x was followed by a voiceless consonant in Prim. OE was xt, and this group remained, e.g. feohtan fight, gefeoht … miht might, niht night …"` [Germanic/docs/DEV_NOTES.md:39049-39056]. Because `feohtan` appears inside the quotation itself, this is stronger than merely inferring row 2010 from a general `xt` rule.

For this slice, the quotation does two jobs. First, it preserves direct source language that DEV_NOTES itself considered worth copying, so later reports do not need to reduce the row to a vague statement like "Campbell allows `-ht-` here." Second, it explains why `feohtan` belongs in the retained-`xt` cohort even though later discussions elsewhere in DEV_NOTES are mainly about `x` loss. The row should therefore reuse this fragment whenever it needs a concise philological rationale for why inherited `*xt` survives to OE `ht` here [Germanic/docs/DEV_NOTES.md:39045-39056].

### DEV_NOTES:line-39023-39044

- Source label line: `DEV_NOTES:line-39023-39044`
- Source heading: `§17.40 research dossier — *x preconsonantal loss vs. j-gemination`
- Source line or section hint: `lines 39023-39044`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `xs_plus_c`; `rule_scope`; `negative_delimitation`; `shared_background`
- Recommended next use: `cite_as_shared_background_only`
- Shared with row IDs: `2194`, `2242`

This fragment matters because it defines the deletion rule narrowly enough to keep row 2010 out of the wrong bucket. DEV_NOTES says the handbook consensus is **not** "any `*x` before any CC"; rather, the canonical change is `*xs → s / _ C`, with examples like `wæstm`, `sesta`, `þisl`, and `néosan` [Germanic/docs/DEV_NOTES.md:39027-39044]. That means the research dossier itself distinguishes the classic `*xs+C` loss environment from other `x` + consonant sequences.

For `*féxtaną -> feohtan`, the value of this fragment is therefore negative and structural. It does not discuss `fight` directly, but it explains why later users should not treat any generic `x-loss` discussion in DEV_NOTES as if it automatically threatened row 2010. `feohtan` belongs to the `*xt` preservation set, not to the `*xs+C` loss set; this fragment is the best shared explanation of that boundary inside DEV_NOTES itself [Germanic/docs/DEV_NOTES.md:39023-39056,39278-39284].

### DEV_NOTES:line-42450-42455, line-42499-42500, and line-42633-42638

- Source label line: `DEV_NOTES:line-42450-42455 / line-42499-42500 / line-42633-42638`
- Source heading: `Risk audit` / `Implementation checklist` / `Lexicon audit`
- Source line or section hint: `lines 42450-42455; 42499-42500; 42633-42638`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current_but_diagnostic`
- Issue tags: `contraction_guardrail`; `collateral_check`; `x_plus_c`; `unaffected_row`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2086`, `2194`, `2242`, `2291`

These later notes come from the `ten / tēon` contraction repair, not from a `fight` investigation, so they should not be overstated. They are still worth preserving because they name row 2010's environment in current form. DEV_NOTES says the risk audit searched `*[eé]x` words with back-vowel continuations and found that only `*téxun` has `*x` followed by a non-apocopating back vowel; `*féxtaną` is explicitly grouped with `*séxs`, `*wéxtiz`, and `*knéxtaz` as a case where `*x` is followed by a consonant [Germanic/docs/DEV_NOTES.md:42450-42455]. The later lexicon audit repeats the same conclusion in even more compressed form: `*séxs, *féxtaną, *wéxtiz, *knéxtaz all have *x + C, not *x + V, and so are unaffected` [Germanic/docs/DEV_NOTES.md:42635-42638].

The checklist line makes the project-history point explicit: after adding the new contraction clauses, the repo should `verify no regression on *féxu/*féxtaną/*sláxaną (which already work)` [Germanic/docs/DEV_NOTES.md:42499-42500]. For row 2010, that is useful evidence that `feohtan` was already considered stable and was being protected from collateral damage. But it remains diagnostic implementation history, not central philological proof that `*féxtaną` should yield `feohtan` in the first place [Germanic/docs/DEV_NOTES.md:42450-42500,42633-42638].

## Superseded or diagnostic material

- No dedicated row-2010 packet, research memo, or row-local DEV_NOTES dossier was found during this pass. The absence of such materials is part of the current evidence state, not an omission in this slice: row 2010 presently survives mainly as a regular exact-match control case plus shared `*xt` notes [Germanic/docs/lexeme_reports/coverage_audit.md:236-236; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14; Germanic/docs/DEV_NOTES.md:39045-39056,39278-39284].
- The later contraction-risk material is easy to misuse. It does mention `*féxtaną`, but only to say the row is unaffected while repairing `*téxun -> tēon`; it should therefore be cited as collateral-check history, not as a substitute for the older Campbell-based `*xt` authority [Germanic/docs/DEV_NOTES.md:42450-42500,42633-42638].
- More generally, later users should not collapse all DEV_NOTES `x`-cluster discussion into one rule. The research dossier itself distinguishes `*xs+C` loss from retained `*xt`, and row 2010 belongs to the retained side [Germanic/docs/DEV_NOTES.md:39023-39056,39278-39284].

## Open questions for later work

- If a fuller final lexeme report is ever written, decide whether to add external lexicographic confirmation for the selected OE target `feohtan`; the current slice is intentionally conservative and relies only on live row state, trace state, and DEV_NOTES-preserved source material [Germanic/data/germanic-aligned-final.tsv:310-310; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1259-1279; Germanic/docs/DEV_NOTES.md:39045-39056].
- If central indexing is expanded later, decide whether a shared control fragment such as `DEV_NOTES:line-39278-39284` is strong enough to index for row 2010. It is row-explicit and current, but it is still a verification list rather than a rich row-specific dossier [Germanic/docs/DEV_NOTES.md:39278-39284].
- If later rule work revisits `*x` environments, keep row 2010 in the regression set and continue to distinguish `*x + C` from `*x + V` and `*xs + C` environments. Current DEV_NOTES history shows that `feohtan` has already served exactly that guardrail role during prior contraction work [Germanic/docs/DEV_NOTES.md:39023-39056,42450-42500,42633-42638].

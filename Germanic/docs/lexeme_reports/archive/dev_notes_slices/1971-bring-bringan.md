---
row_id: 1971
concept: bring
counterpart: bringan
proto: *brínganą
protoform: *brínganą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/dossier-ibreve-cleanup-2026.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1971 bring / bringan

## Current row state

- CONCEPT: `bring`
- COUNTERPART: `bringan`
- PROTO: `*brínganą`
- PROTOFORM: `*brínganą`
- DERIVATION_CLASS: `regular`
- Live TSV row: the current Old English row keeps `PROTO = *brínganą`, `PROTOFORM = *brínganą`, `COUNTERPART = bringan`, and `DERIVATION_CLASS = regular`; the source column contains only inherited-etymology placeholders, not a row-local note [Germanic/data/germanic-aligned-final.tsv:155-155].
- Existing report infrastructure: `coverage_audit.md` still lists row 1971 as `none`, with no packet, no research memo, and no previously attached DEV_NOTES fragment [Germanic/docs/lexeme_reports/coverage_audit.md:212-212].
- Current implementation trace: the published OE derivation snapshot already returns the live target with no special replacement step — `PROTO: *brínganą`, `EXPECTED: bringan`, `OUTPUTS: bringan`; the OE-side stages shown are heavy-syllable nasal apocope, secondary nasalization, and weak-tail reduction [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:591-610].

## Development-note summary

DEV_NOTES support for row 1971 is real but mostly **implementation-facing**, not a lexeme-specific source dossier. No standalone philological note for `bringan` was located in `Germanic/docs/DEV_NOTES.md`; instead, the row appears in three materially relevant ways: first as an older OE weak-tail diagnostic (`brengana` in the `-ana` bucket), then as a negative control in the OE `r`-metathesis discussion, and finally as a current sentinel in the `*ĭ` / `*ng` cleanup work [Germanic/docs/DEV_NOTES.md:2422-2427,2481-2485,5024-5055,38257-38303,38371-38386].

The oldest directly relevant DEV_NOTES material is diagnostic and now superseded. In the consolidated OE TODOs the note says, verbatim, “**Weak-tail cleanup (`-ana` → `-an`)**” is still needed so outputs like `bacana/gennana/brecana/**brengana**/brūcana` converge on attested `-an` forms, and the ending diagnostics repeat `brengana` as one of the sample bad outputs [Germanic/docs/DEV_NOTES.md:2427-2427,2485-2485]. That material matters because it preserves the earlier failure mode for this row: the problem was not uncertainty about whether OE should be `bringan`, but a broad implementation bug that left infinitives stranded with `-ana` and an unwanted `e` in this item [Germanic/docs/DEV_NOTES.md:2422-2427,2481-2485].

A separate shared discussion in DEV_NOTES is also directly relevant because it states that the OE `r`-metathesis machinery must **not** touch this verb. In the metathesis regression table the note explicitly lists “`*bringanan` → `*bringan` ... ✓ (no metathesis),” and the outstanding-issues paragraph immediately warns that extending the `*brunna → burna` rule to wider `rVn` environments “risks overapplication to forms like `*bringan`” [Germanic/docs/DEV_NOTES.md:5024-5055]. For row 1971, that is substantive guidance rather than incidental mention: DEV_NOTES is using `bringan` as evidence that the grammar must block analogically tempting `r`-metathesis outputs such as `*brengan` here [Germanic/docs/DEV_NOTES.md:5026-5055].

The most current DEV_NOTES authority comes from the 2026 closure of the `*ĭ` cleanup and the follow-up sentinel test set. The closure note says the rule now lowers unstressed `*ĭ` to `*e` but then restores `*e → *i` before `*ng`, with the explicit rationale that this is “**Phonetic blocking, not morpho-lexical: `*ng` is the diagnostic for `*-ing-/*-ung-` derivational suffixes at this stage**” [Germanic/docs/DEV_NOTES.md:38264-38272]. The regression table under that explanation includes `*brínganą → bringan` as “✓ no change,” and the later sentinel table makes the row's role even plainer by glossing it as “**`*brengan` blocking, suffix-an protection**” [Germanic/docs/DEV_NOTES.md:38292-38303,38371-38386]. In current project history, then, row 1971 is best understood as a **regression-control lexeme**: the live target `bringan` is stable, and the important DEV_NOTES substance is about preventing repairs elsewhere from reintroducing `brengana` or `*brengan` [Germanic/docs/DEV_NOTES.md:38257-38303,38371-38386].

Because the live DEV_NOTES material is this implementation-heavy, the slice should be conservative about claims it does **not** have source support for. There is no current DEV_NOTES passage here comparable to the row-specific source audits written for some other lexemes; the evidence on hand is enough to support the existing row and its current derivation, but not enough to justify a larger philological narrative beyond “regular inherited infinitive, presently used as a guardrail against OE regression” [Germanic/docs/lexeme_reports/coverage_audit.md:212-212; Germanic/docs/DEV_NOTES.md:38257-38303,38371-38386].

## Relevant DEV_NOTES fragments

### DEV_NOTES: `PGmc→OE TODOs` and `Ending diagnostics` (lines 2422-2427, 2481-2485)

- Source heading: `PGmc→OE TODOs (consolidated)` plus `Ending diagnostics (old_english.bin)`
- Source line or section hint: `lines 2422-2427 and 2481-2485`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `weak_tail_cleanup`; `-ana_bucket`; `old_mismatch_state`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs: `1967`, `1943`, `1972`

This is the earliest materially relevant DEV_NOTES support for row 1971, and it should be preserved as diagnostic history. DEV_NOTES says “**Weak-tail cleanup (`-ana` → `-an`)**” is needed so outputs like `bacana/gennana/brecana/**brengana**/brūcana` “converge on attested `-an`,” and the ending diagnostics repeat `brengana` in the sample bad-output list [Germanic/docs/DEV_NOTES.md:2427-2427,2485-2485]. For this row the point is narrow but important: the project once treated `bringan` as part of a broad OE infinitive-ending failure bucket, not as a disputed lexeme target.

### DEV_NOTES: `What the FST does NOT model` and `Outstanding issues` (lines 5024-5055)

- Source heading: `While correctly not applying to` plus `Outstanding issues`
- Source line or section hint: `lines 5024-5055`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `r_metathesis`; `negative_control`; `overapplication_guardrail`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This shared metathesis fragment is current and directly relevant. DEV_NOTES gives the explicit negative-control line “`*bringanan` → `*bringan` ... **✓ (no metathesis)**” and then warns that broadening the `*brunna → burna` rule “**risks overapplication to forms like `*bringan`**” [Germanic/docs/DEV_NOTES.md:5026-5055]. For row 1971 that material should be carried forward almost verbatim, because it is the clearest live project statement that the OE grammar must not create a metathesized `brengan`-type output here.

### DEV_NOTES: `§17.35.10 Closure (2026-04-27)` (lines 38257-38303)

- Source heading: `§17.35.10 Closure (2026-04-27)`
- Source line or section hint: `lines 38257-38303`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `ibreve_cleanup`; `ng_restoration`; `regression_probe`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2181`, `2057`, `1943`

This is the main current implementation fragment. DEV_NOTES rewrites unstressed `*ĭ` lowering as a two-stage composition and states the governing claim in exactly the wording worth preserving here: “**Phonetic blocking, not morpho-lexical: `*ng` is the diagnostic for `*-ing-/*-ung-` derivational suffixes at this stage**” [Germanic/docs/DEV_NOTES.md:38268-38272]. The same closure then records `*brínganą → bringan` as “✓ no change” in the post-rebuild regression table [Germanic/docs/DEV_NOTES.md:38292-38303]. For row 1971, this is current authority that the `i` of `bringan` is being actively protected against the lowering logic added for other lexemes.

### DEV_NOTES: `§17.36 *ĭ (i-breve) cleanup — incremental dismantling` (lines 38371-38386)

- Source heading: `Sentinel test set (must remain stable through every step)`
- Source line or section hint: `lines 38371-38386`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `sentinel_verification`; `brengan_blocking`; `suffix_an_protection`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2181`, `2057`, `1943`

This later sentinel table is the most explicit statement of row 1971's current function in DEV_NOTES. It keeps the probe `*brínganą → bringan` in the required stability set and annotates it as “**`*brengan` blocking, suffix-an protection**” [Germanic/docs/DEV_NOTES.md:38371-38386]. That wording should be preserved in the replacement note because it spells out both regression risks at once: the row is guarding against unintended medial lowering before `ng` **and** against reintroduction of the old weak-tail infinitive problem.

## Superseded or diagnostic material

- The early OE TODO / ending-diagnostics material is superseded as a description of the row's present state. It documents an older failure mode (`brengana`) rather than current behavior; the live derivation snapshot and the later sentinel tables show that row 1971 now surfaces correctly as `bringan` [Germanic/docs/DEV_NOTES.md:2422-2427,2481-2485,38292-38303,38371-38386; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:591-610].
- No matching packet or research memo exists for row 1971 at present. `coverage_audit.md` still marks the row as `none`, so this slice is replacing absent infrastructure rather than condensing a larger row dossier [Germanic/docs/lexeme_reports/coverage_audit.md:212-212].
- DEV_NOTES does **not** provide a row-local literature audit for `bringan`; its support is almost entirely about implementation behavior and regression boundaries. That absence should be reported neutrally: it means the row has not needed a special philological memo so far, not that DEV_NOTES found the lexical equation doubtful [Germanic/docs/lexeme_reports/coverage_audit.md:212-212; Germanic/docs/DEV_NOTES.md:5024-5055,38257-38303].

## Open questions for later work

- If row 1971 is ever proposed for `index.tsv`, decide whether implementation/regression material alone is enough to justify indexing, or whether the row should remain effectively no-index until a more lexeme-specific source discussion exists.
- If later OE cleanup revisits weak-tail reduction or the `*ĭ`/`*ng` restoration architecture, keep `*brínganą → bringan` in the sentinel set; DEV_NOTES explicitly uses this row to block regressions toward `brengana` and `*brengan` [Germanic/docs/DEV_NOTES.md:2427-2427,38268-38272,38371-38386].
- If a future packet or memo is created, it should check whether repo reference files offer any worthwhile lexeme-local source discussion for OE `bringan`; current DEV_NOTES material does not attempt that, so later writers should not pretend such a source audit already exists.

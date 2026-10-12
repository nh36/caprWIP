---
row_id: 2200
concept: sorrow
counterpart: sorg
proto: *súrgō
protoform: *súrgō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2200 sorrow / sorg

## Current row state

- CONCEPT: `sorrow` [Germanic/data/germanic-aligned-final.tsv:1047-1047]
- COUNTERPART: `sorg` [Germanic/data/germanic-aligned-final.tsv:1047-1047]
- PROTO: `*súrgō` [Germanic/data/germanic-aligned-final.tsv:1047-1047]
- PROTOFORM: `*súrgō` [Germanic/data/germanic-aligned-final.tsv:1047-1047]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:1047-1047]
- This row still needs the conceptual PROTO / PROTOFORM / COUNTERPART distinction even though the first two cells happen to coincide. Here `PROTO` and `PROTOFORM` are both `*súrgō`, but `COUNTERPART` is the OE target `sorg`; the row is not about silently replacing the OE form with the handbook example `sorge` [Germanic/data/germanic-aligned-final.tsv:1047-1047].
- There is no row-local entry in `oe_known_problems.tsv`, and coverage infrastructure still lists the row as undocumented: `| 2200 | sorrow | sorg | regular | no | - | - | - | none |` [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:360-360].
- The current published derivation trace already matches the live row with no exception or analogy flag: `Proto Input: *súrgō`, `NWGmc U Lowering: *sórgō`, `NWGmc Final Long O Raising: *sórgu`, `OE High Vowel Apocope: *sórg`, outcome `sorg` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4426-4445].
- Independent source material agrees that the lexeme itself belongs under PGmc `*surgō-` and that OE has `sorg/sorh`, even if DEV_NOTES never developed a dedicated row memo: Kroonen gives `*surgō- f. 'grief, sorrow, worry' … OE sorg, sorh` [@Kroonen2013, p. 493; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:25336-25337], Ringe-Taylor list `PGmce *surgo … > … OE sorg` [@RingeTaylor2014, p. 27; docs/references/ringe_taylor_linguistic_history_vol2.txt:2347-2347], and Campbell lists both `sorg sorrow` and orthographic `sorh` [@Campbell1959, §§446, 588; docs/references/campbell_old_english_grammar.txt:11624-11624,15202-15204].

## Detailed development-note summary

Row `2200` has usable DEV_NOTES support, but it is thin and mostly shared rather than row-specific. The surviving material falls into two distinct layers that should not be conflated.

The first layer is handbook-oriented and uses this lexeme as an example for ō-stem morphology, not as a dedicated dossier on row `2200`. DEV_NOTES twice preserves Ringe-Taylor's quotation: `"ō-stem acc. sg., gen. sg. -e < -ā < *-ā < PWGmc *-a < PGmc acc. sg. *-ō, gen. sg. *-ōz, e.g. in sorge 'trouble, of trouble' < sorge < *sorge < PWGmc *sorga < PGmc acc. sg. *surgō …"` [@RingeTaylor2014, pp. 299-300; Germanic/docs/DEV_NOTES.md:22709-22713,23497-23500]. That quotation is still worth carrying forward because it preserves the lexeme identity, the lowered West Germanic/OE root vowel (`surg-` > `sorg-`), and the fact that the literature itself uses this noun as a standard example. But it is not a direct statement of current row policy, because the quotation is about inflected `sorge` and about the acc./gen.sg. ō-stem ending, whereas the live OE row targets bare `sorg`.

Campbell's and Brunner's companion comments in the same DEV_NOTES blocks make that limitation even clearer. Campbell says the gen.sg. is exceptional because "the phonological development would be -a," and DEV_NOTES summarizes the consensus as: the ending survives to produce `-e`, but the exact route involves analogical pressure or at least a special ō-stem history [@Campbell1959, §586; Germanic/docs/DEV_NOTES.md:22715-22732,23502-23512]. For row `2200`, that means the `sorge` material is best treated as philological background and as a warning not to collapse inflected-form evidence into the row's distinct `COUNTERPART`. It supports the lexeme and the lowered root vowel, but it does not by itself explain why the live row is encoded as `*súrgō → sorg`.

The second layer is the genuinely current one for the row: the late chronology audit around the `*núsō / *skúflō / *súrgō` regression cluster. DEV_NOTES names row `2200` explicitly as one of the three `root *u + word-final suffix *-ō` forms that broke when `NWGmcFinalLongORaising` was moved ahead of `NWGmcULowering` [Germanic/docs/DEV_NOTES.md:24257-24265]. The note then states the mechanism plainly: if raising fires first, the original non-high `*-ō` disappears too early, so root `*u` no longer lowers; with the correct order, u-lowering sees `*-ō`, yielding `*sórgō`, then final long `ō` raises to `*sórgu`, and later OE apocope gives `sorg` [Germanic/docs/DEV_NOTES.md:24275-24308,24445-24449; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4435-4445]. For row `2200`, this is the real current project decision: the row is `regular` because the live cascade now derives `sorg` by ordinary sound change once the rule order is correct.

That shared chronology material also supersedes any temptation to reuse the older Case 3 `sorge` notes as though they directly governed the row. The live trace does not go through a final OE `-e`; it goes through `*sórgu > sorg`. So the working note for row `2200` has to keep two claims separate: (1) handbook material on `sorge` is still useful evidence for the lexeme and for the lowered root-vowel history [@RingeTaylor2014, pp. 299-300], and (2) the row's present OE output `sorg` is controlled by the later implementation audit that locked in `NWGmcULowering` before final-`ō` raising [Germanic/docs/DEV_NOTES.md:24275-24308,24446-24449,39799-39804].

The practical bottom line is therefore conservative. There is enough material to maintain a replacement working note: the row is live, regular, and supported by current trace evidence; Kroonen, Ringe-Taylor, and Campbell all support the lexeme `sorg/sorh` under `*surgō-` [@Kroonen2013, p. 493; @RingeTaylor2014, p. 27; @Campbell1959, §§446, 588]. But the DEV_NOTES support is still mostly shared chronology plus handbook exempla, not a row-local philological argument distinguishing citation-form `sorg` from inflected `sorge`. That is enough for a slice file, but weak for indexing.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-22709-22732-and-23497-23512

- Source heading: `Case 3 — *rástōz → ræst (expected ræste)` / `Case 3 implementation: PGmcFinalOZShortening outputs {*æ} directly (Option γ)`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `diagnostic_only_for_row`
- Issue tags: `lexeme_identity`; `ō_stem_morphology`; `inflected_form_vs_counterpart`; `source_background`
- Recommended next use: `use_with_caution_in_final_report`
- Shared with row IDs:

This fragment preserves the best direct quotation involving the lexeme in DEV_NOTES: `"… e.g. in sorge 'trouble, of trouble' < sorge < *sorge < PWGmc *sorga < PGmc acc. sg. *surgō, gen. sg. *surgoz …"` [@RingeTaylor2014, pp. 299-300; Germanic/docs/DEV_NOTES.md:22709-22713,23497-23500]. It is worth keeping because it shows that the same noun is explicitly used by Ringe-Taylor as an ō-stem example and because it preserves the lowered `sorg-` vocalism. For row `2200`, however, it is only diagnostic background. The fragment is about `sorge` and about the `-e` outcome of acc./gen.sg. ō-stems, while the live row's `COUNTERPART` is `sorg`; Campbell's accompanying note that the gen.sg. is not a straightforward phonological continuation reinforces that this cannot simply be reused as row-local output authority [@Campbell1959, §586; Germanic/docs/DEV_NOTES.md:22715-22732,23502-23512].

### DEV_NOTES:line-24257-24308-and-24445-24449

- Source heading: `Regression cluster` / `Root-cause: U-lowering has been bled` / `Probe outcome`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `chronology`; `u_lowering`; `final_ō_raising`; `shared_regression_cluster`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2143,2185`

This is the controlling current DEV_NOTES fragment for row `2200`. DEV_NOTES first lists `*súrgō → sorg` among the three rows that newly regressed together when the pipeline order was wrong [Germanic/docs/DEV_NOTES.md:24257-24265]. It then explains the failure mechanism in general terms: if final long `ō` raises first, the original non-high trigger disappears and root `*u` stays unlowered; with the correct order, u-lowering applies first and the row is restored [Germanic/docs/DEV_NOTES.md:24275-24308]. The later probe summary makes the row-level result explicit: ``*núsō → nosu`, `*skúflō → sċofl`, `*súrgō → sorg` … fixed by the reorder (root-*u lowered again)` [Germanic/docs/DEV_NOTES.md:24445-24449]. For working-note purposes, this fragment—not the older `sorge` morphology block—is the direct authority for the live `regular` analysis.

### DEV_NOTES:line-39799-39804

- Source heading: `Q4 finding — lautgesetz status (cell-switch, not wontfix)`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `regression_guard`; `chronology_lock`; `shared_control_row`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `2143,2185`

This later audit shows that row `2200` is no longer just one solved noun among many; it has become one of the data points constraining later rule work. DEV_NOTES says explicitly that reordering `NWGmcFinalLongORaising` before `NWGmcULowering` would regress rows `2143 (*núsō → nosu)`, `2200 (*súrgō → sorg)`, and `2185 (*skúflō → sċofl*)` [Germanic/docs/DEV_NOTES.md:39799-39804]. For this row, the fragment is not primary philology, but it matters as project chronology: `sorg` is now part of the evidence blocking a bad cascade reorder.

## Superseded or diagnostic material

- The main diagnostic trap is the temptation to treat DEV_NOTES' repeated `sorge` quotation as though it directly described the live row. It does not. Those notes discuss acc./gen.sg. ō-stem morphology and preserve the lexeme as an example, but row `2200` currently targets `sorg` and traces `*súrgō > *sórgō > *sórgu > sorg` [Germanic/docs/DEV_NOTES.md:22709-22732,23951-23978; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4435-4445].
- The detailed `*surgōz > *sorgǣ > *sorgę > sorge` chain in the long Case 3 plan is therefore diagnostic only for this row. It is useful if later work needs to discuss the noun's inflected ō-stem forms, but it should not be normalized into a statement that the row's live `COUNTERPART` ought to be `sorge` [@RingeTaylor2014, pp. 298-300; Germanic/docs/DEV_NOTES.md:23951-23978].
- Any account that lets `NWGmcFinalLongORaising` bleed `NWGmcULowering` is superseded for row `2200`. Later DEV_NOTES work explicitly uses `*súrgō → sorg` as evidence against that order, and the published trace now reflects the corrected chronology [Germanic/docs/DEV_NOTES.md:24275-24308,24445-24449,39799-39804; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4435-4445].

## Open questions for later work

- If row `2200` is ever prepared for indexing, add one explicit sentence distinguishing citation-form `sorg` from the handbook example `sorge`; at present the slice can document the contrast, but DEV_NOTES does not yet provide a row-local explanation of it.
- A future final lexeme report should probably cite Kroonen, Ringe-Taylor, and Campbell directly for the lexeme identity `*surgō- / sorg / sorh` [@Kroonen2013, p. 493; @RingeTaylor2014, p. 27; @Campbell1959, §§446, 588], while relegating the `sorge` material to an inflected-form background note [@RingeTaylor2014, pp. 299-300].
- If more row-specific documentation is ever desired, the obvious next step is not new rule work but a short philological note explaining why the dataset's `COUNTERPART` uses the bare form `sorg` even though some handbook discussions foreground `sorge`.

---
row_id: 2219
concept: stock
counterpart: stocc
proto: *stúkkaz
protoform: *stúkkaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2219 stock / stocc

## Current row state

- The live OE row is `2219`, with `CONCEPT stock`, `COUNTERPART stocc`, `PROTO *stúkkaz`, `PROTOFORM *stúkkaz`, and `DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:1122-1122].
- The row's `NOTE` field is blank, and the `HISTORY` field preserves only duplicated provenance strings — `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)` — rather than a project-authored lexical or phonological argument [Germanic/data/germanic-aligned-final.tsv:1122-1122].
- `oe_known_problems.tsv` has no entry for row `2219`, for `stocc`, or for `*stúkkaz`, so the project is not currently treating this item as an open OE exception bucket [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure currently records no attached packet, research memo, or indexed fragment for this row: `| 2219 | stock | stocc | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:371-371].
- The published OE derivation-class trace already matches the live row cleanly: `PROTO: *stúkkaz`, `EXPECTED: stocc`, `OUTPUTS: stocc`, with the staged path `*stúkkaz > *stókkaz > *stókka > *stókk > stocc` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4706-4725].

## Detailed development-note summary

No attachable lexeme-specific DEV_NOTES paragraph currently survives for `stock / stocc`. Searches for `stocc`, `*stúkkaz`, and `stock` in `Germanic/docs/DEV_NOTES.md` do not produce a row-local etymological note, lexical audit, or implementation note for row `2219`; the only hit worth recording is a false friend on `stocktake`, not the noun `stock` [Germanic/docs/DEV_NOTES.md:21840-21846]. This slice therefore has to function as a replacement working note built from the live row state, the existing trace/report infrastructure, and handbook lexical support rather than as a tidy extraction from a surviving DEV_NOTES dossier.

The row remains straightforward so long as the labels are kept distinct. `PROTO` and `PROTOFORM` both remain `*stúkkaz`, i.e. the comparative head/input form used for this OE row, while `COUNTERPART` is the Old English target `stocc` [Germanic/data/germanic-aligned-final.tsv:1122-1122]. Because the live row has no substantive note and no `oe_known_problems.tsv` entry, there is currently no project-side signal that the row depends on borrowing, analogical repair, or an exception-only derivation [Germanic/data/oe_known_problems.tsv:1-8]. The working project judgment is still the simple one stated in the live row and confirmed by the trace output: this is a regular inherited noun whose current pipeline already lands on `stocc` [Germanic/data/germanic-aligned-final.tsv:1122-1122; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4706-4725].

Handbook lexical support is coherent, but it should be kept separate from missing DEV_NOTES support. Kroonen gives `*stukka- m.` with `OE stocc m. 'stick, log, trunk'` and derives the noun from the strong verb `*stekan-`, adding that `the zero-grade *u ... arose secondarily` [@Kroonen2013, p. 487]. Orel likewise lists `*stukkaz sb.m.` with `OE stocc 'stock, trunk, log'` and remarks, `With an irregularity in the inlaut geminate` [@Orel2003, p. 383]. Those source remarks matter because they confirm that the comparative family behind the row is real and that OE `stocc` belongs to it, but they are not themselves row-specific project decisions from `DEV_NOTES.md`.

The clearest current project-side explanation is therefore the derivation trace rather than DEV_NOTES prose. In the published trace, `*stúkkaz` first shows Northwest Germanic u-lowering to `*stókkaz`, then final `-z` deletion to `*stókka`, then loss of final bare `-a` to `*stókk`, with orthographic `stocc` as the surface outcome [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4713-4725]. That is broadly compatible with Campbell's statement that Germanic `u` became `o` before mid and low vowels, albeit with lexical exceptions elsewhere in Old English [@Campbell1959, §115]. For replacement-working-note purposes, the conservative conclusion is: keep `PROTO *stúkkaz`; keep `PROTOFORM *stúkkaz`; keep `COUNTERPART stocc`; and treat the absence of a row-local DEV_NOTES discussion as a documentation gap, not as evidence that the row is presently misderived.

## Relevant DEV_NOTES fragments with line-based refs

No attachable row-specific DEV_NOTES fragment was found for `stock` / `stocc`. The only search hit worth preserving is a false friend that should **not** be attached to this row.

### DEV_NOTES:line-21840-21846

- Source heading: `Plan Y-minimal` / accent-convention discussion
- Source line or section hint: `lines 21840-21846`
- Fragment type: `diagnostic_only_false_friend`
- Status: `diagnostic_only`
- Issue tags: `false_friend_search_hit`; `stocktake_not_stock`; `not_lexeme_specific`
- Recommended next use: `exclude_from_oe_indexing`
- Shared with row IDs:

This fragment says `accent-convention stocktake proposal ("4 accents is overkill")` and then discusses the phonological roles of `ā`, `á`, `a`, and `ă` [Germanic/docs/DEV_NOTES.md:21843-21846]. The word `stocktake` is only an accidental string overlap. It has nothing to do with row `2219`, with `*stúkkaz`, or with OE `stocc`, and it should not be indexed to this lexeme.

## Superseded or diagnostic material

- The duplicated Wiktionary provenance in the live row history is diagnostic only. It explains where the row was imported from, but it does **not** function as a project-authored defense of the OE outcome or the comparative reconstruction [Germanic/data/germanic-aligned-final.tsv:1122-1122].
- The current coverage state (`none` for packet, memo, and indexed slice coverage) should be read as a documentation gap, not as evidence of derivational trouble. The trace report already shows a clean regular output for the row [Germanic/docs/lexeme_reports/coverage_audit.md:371-371; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4706-4725].
- Kroonen's note that the noun is derived from `*stekan-` and Orel's remark about an inlaut geminate irregularity are useful philological background, but no surviving DEV_NOTES passage currently states how much of that background the project intends to foreground in a final row report [@Kroonen2013, p. 487; @Orel2003, p. 383]. Later report writers should therefore not pretend that this interpretive layer has already been settled inside project notes.
- No packet or research-memo stem exists to reuse for row `2219`, which is why this slice uses the canonical row-based filename `2219-stock-stocc.md` rather than inheriting an existing report stem [Germanic/docs/lexeme_reports/coverage_audit.md:371-371].

## Open questions for later work

- If row `2219` is ever to become indexable, the missing ingredient is a genuinely row-specific memo or DEV_NOTES paragraph that ties the lexical evidence for `*stúkkaz` / `stocc` to the project's current derivational analysis. At present the support is real but mostly external or infrastructural, so a no-index stance is safer.
- If a later final lexeme report is written, decide whether Kroonen's derivation from `*stekan-` and Orel's warning about geminate irregularity should appear in the main argument or be kept as background philological notes [@Kroonen2013, p. 487; @Orel2003, p. 383].
- If later report prose cites the sound-law path, keep the row labels explicit: comparative/project input `PROTO`/`PROTOFORM *stúkkaz` versus OE target `COUNTERPART stocc`; do not let the absence of a DEV_NOTES dossier blur the distinction between the comparative form and the OE outcome [Germanic/data/germanic-aligned-final.tsv:1122-1122].

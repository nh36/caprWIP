---
row_id: 2215
concept: steal
counterpart: stelan
proto: *stélaną
protoform: *stélaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2215 steal / stelan

## Current row state

- Live `Germanic/data/germanic-aligned-final.tsv` line `1106` gives row `2215` as `CONCEPT steal`, `COUNTERPART stelan`, `PROTO *stélaną`, `PROTOFORM *stélaną`, and `DERIVATION_CLASS regular`; the row carries no row-local explanatory NOTE beyond duplicated Wiktionary-source provenance in the history field [Germanic/data/germanic-aligned-final.tsv:1106-1106].
- For this row, `PROTO` and `PROTOFORM` are currently the same quantity-marked form `*stélaną`, but they still do different jobs: `PROTO` is the comparative headword, while `PROTOFORM` is the OE-facing derivational input consumed by the transducer. `COUNTERPART` is the infinitive `stelan`, not a finite form and not a prefixed derivative [Germanic/data/germanic-aligned-final.tsv:1106-1106].
- `Germanic/data/oe_known_problems.tsv` currently has no row-local entry for `2215`, `steal`, `stelan`, or `*stélaną`, so the row is not being tracked as an OE exception or unresolved bug bucket [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still treats the row as uncovered regular material with no packet, memo, or report linkage: `| 2215 | steal | stelan | regular | no | - | - | - | none |`. That means no reusable packet or research-memo stem exists, so the canonical row-based slice filename is the right choice here [Germanic/docs/lexeme_reports/coverage_audit.md:370-370].
- The published OE derivation trace is an exact match: `PROTO: *stélaną`, `EXPECTED: stelan`, `OUTPUTS: stelan`. The trace shows only routine developments — `OE Heavy Syllable Nasal Apocope`, `OE Secondary Nasalization`, and `OE Weak Tail Reduction` — and ends in surface `stelan` with no exception-handling branch [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4666-4685].

## Detailed development-note summary

Direct DEV_NOTES support for row `2215` is effectively absent in the current file. No surviving DEV_NOTES passage was recovered in this pass that discusses `stelan` as a problem row, proposes a different OE target, distinguishes a different `PROTOFORM` from `PROTO`, or records a row-specific repair. The replacement working note therefore needs to preserve that absence explicitly rather than inventing a historical argument that is no longer there.

What does survive is a stable live-row state plus an exact trace match. The live TSV already classifies the row as `regular`, and the published derivation report independently confirms that the current pipeline derives `stelan` directly from `*stélaną` without detours, exception hooks, or late clean-up patches beyond the ordinary weak-tail stages [Germanic/data/germanic-aligned-final.tsv:1106-1106; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4666-4685]. For working purposes, that is the main durable point: nothing in the current infrastructure suggests that `stelan` is a mismatch row.

The note should also preserve the narrowness of that conclusion. This slice does **not** show that DEV_NOTES once solved a complicated `steal` problem; instead, it shows that no such row-local DEV_NOTES dossier currently survives. The present row is therefore stable enough to remain `regular`, but thin as DEV_NOTES-slicing evidence. Later report work should treat this as an absence-of-problem file, not as a hidden controversy file.

The filename decision is part of that same story. Because coverage audit still shows `none` for packet, research memo, and report linkage, there was no existing stem to reuse for row `2215`; the canonical row-based filename is therefore the conservative choice [Germanic/docs/lexeme_reports/coverage_audit.md:370-370].

## Relevant DEV_NOTES fragments with line-based refs

No row-local `DEV_NOTES:line-...` fragment was recoverable for `steal / stelan` in the current `Germanic/docs/DEV_NOTES.md` during this pass. There is therefore no attached fragment to cite, index, or summarize as current row policy.

That absence is itself the important preservation point for this slice: later work should not assume that an uncovered regular row necessarily has a hidden DEV_NOTES section waiting to be reattached. For row `2215`, the surviving support currently comes from the live TSV row, the coverage audit, and the exact derivation trace rather than from any recoverable DEV_NOTES passage [Germanic/data/germanic-aligned-final.tsv:1106-1106; Germanic/docs/lexeme_reports/coverage_audit.md:370-370; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4666-4685].

## Superseded or diagnostic material

- No superseded row-local target survives in DEV_NOTES for this lexeme. There is no preserved proposal that row `2215` should target anything other than `stelan`, and no surviving note that separates live `PROTO` from live `PROTOFORM`.
- No diagnostic bug history was recovered for this row either. The published trace already lands on `stelan`, and `oe_known_problems.tsv` does not treat `*stélaną` as an exception bucket or open defect [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4666-4685; Germanic/data/oe_known_problems.tsv:1-8].
- Because DEV_NOTES support is absent rather than superseded, the main risk for later work is overinterpreting the row's regular status as if it reflected a preserved lexical argument in DEV_NOTES. At present, the row is regular because nothing in the live materials contradicts it, not because this pass recovered a substantial `steal` note dossier.

## Open questions for later work

- If row `2215` ever becomes indexable from DEV_NOTES infrastructure, it will probably require a genuine row-local packet, memo, or later literature note; the current slice mainly records that no such DEV_NOTES fragment is presently recoverable.
- If a later lexeme report wants a fuller philological discussion, the next useful addition would be direct comparative and dictionary citation work for `*stélaną / stelan`, not another attempt to force nonexistent DEV_NOTES prose into row-local evidence.
- Unless new source material appears, this row should remain documented as a regular uncovered item whose main present support is exact derivational fit rather than explicit DEV_NOTES commentary.

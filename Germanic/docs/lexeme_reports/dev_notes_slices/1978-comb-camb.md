---
row_id: 1978
concept: comb
counterpart: camb
proto: *kámbaz
protoform: *kámbaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1978 comb / camb

## Current row state

- CONCEPT: `comb`
- COUNTERPART: `camb`
- PROTO: `*kámbaz`
- PROTOFORM: `*kámbaz`
- DERIVATION_CLASS: `regular`
- Live TSV row: the Old English row currently keeps `COUNTERPART = camb`, `PROTO = *kámbaz`, and `DERIVATION_CLASS = regular`; its history/source field contains only inherited-etymology placeholders rather than a row-local explanatory note [Germanic/data/germanic-aligned-final.tsv:183-183].
- Repo lexical baseline: `old_english_wiktionary.tsv` independently aligns `comb` with OE `camb` as an inherited item, which matches the live row's conservative setup [Germanic/data/old_english_wiktionary.tsv:44-44].
- Existing row infrastructure: `coverage_audit.md` records row 1978 as having no packet, no research memo, no attached DEV_NOTES fragment, and no other linked lexeme-report infrastructure to reuse [Germanic/docs/lexeme_reports/coverage_audit.md:217-217].
- Current implementation trace: the published derivation snapshot already returns the live target without repair — `*kámbaz` > `*kámba` (PGmc final `-z` deletion) > `*kámb` (final bare `-a` loss) > `camb` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:733-752].

## Development-note summary

DEV_NOTES support for row 1978 is effectively absent in the strong lexeme-specific sense, and that absence should be treated as a real finding rather than as an invitation to invent missing project history. The repo's own coverage audit marks the row as `none` for packet/memo/attached-fragment infrastructure, and the live row itself shows no sign that `comb / camb` was ever managed as an exception, repair target, or source-dispute case [Germanic/docs/lexeme_reports/coverage_audit.md:217-217; Germanic/data/germanic-aligned-final.tsv:183-183].

The practical consequence is that the replacement note has to stay conservative. Nothing in the current project evidence requires separating comparative `PROTO` from row-level `PROTOFORM`; both remain `*kámbaz`. Nothing in the current project evidence requires replacing the OE target with a dialectal substitute, reconstructed West-Saxon proxy, or analogical repair form; the target remains `camb`. And nothing in the current project evidence suggests that the row needs an `oe_known_problems.tsv` style exception bucket. What the repo does preserve is a straightforward success state: the cascade already derives `camb` from `*kámbaz` through ordinary end-of-word cleanup, with no row-local workaround documented anywhere in the lexeme-report infrastructure [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:733-752; Germanic/docs/lexeme_reports/coverage_audit.md:217-217].

That thin record matters for later reporting. This slice should not overstate the case by pretending DEV_NOTES contains a hidden philological dossier on `comb / camb`; nor should it imply that the row is undocumented in the negative sense of being unresolved. The current state is simpler: `camb` behaves like a regular inherited OE continuation already accepted by the live row, mirrored in the small repo lexical baseline, and not singled out in DEV_NOTES for special discussion [Germanic/data/germanic-aligned-final.tsv:183-183; Germanic/data/old_english_wiktionary.tsv:44-44; Germanic/docs/lexeme_reports/coverage_audit.md:217-217].

## Relevant DEV_NOTES fragments

No materially relevant lexeme-specific DEV_NOTES fragment has been identified for `comb / camb`, and the repo's own audit row correspondingly lists no attached fragment for row 1978 [Germanic/docs/lexeme_reports/coverage_audit.md:217-217].

No clearly reusable shared DEV_NOTES discussion has been located that bears on this row more specifically than the generic mechanics already visible in the derivation trace. For present purposes, the evidentiary core is therefore the live row plus the successful trace, not a preserved DEV_NOTES argument about target choice or source interpretation [Germanic/data/germanic-aligned-final.tsv:183-183; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:733-752].

## Superseded or diagnostic material

- No superseded row-specific DEV_NOTES repair history is presently preserved for this lexeme. That is itself diagnostic: unlike rows with protoform swaps or rule-order debates, row 1978 currently survives in the repo as a regular-success item rather than as a remembered problem case [Germanic/docs/lexeme_reports/coverage_audit.md:217-217; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:733-752].
- The derivation trace is diagnostic support, not DEV_NOTES. Its value is implementation-facing: it shows that the live cascade reaches `camb` directly from `*kámbaz`, so later writers should avoid retrofitting a source-history narrative that the project never actually recorded [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:733-752].
- The inherited-equation line in `old_english_wiktionary.tsv` is likewise baseline support rather than a substitute for a DEV_NOTES dossier. It is enough to confirm that the row's lexical pairing is conservative, but it does not supply additional project-internal argumentation beyond that [Germanic/data/old_english_wiktionary.tsv:44-44].

## Open questions for later work

- Decide whether row 1978 is worth indexing at all. On the present evidence, it looks more like a useful no-drama replacement slice than an index-worthy exception note, because the repo preserves no row-local DEV_NOTES argument beyond regular success [Germanic/docs/lexeme_reports/coverage_audit.md:217-217; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:733-752].
- If a future source-audit pass wants stronger lexicographic support than `old_english_wiktionary.tsv`, add exact repository citations from Bosworth-Toller, Clark Hall, or another in-repo reference file; the present slice should not imply that DEV_NOTES already performed that fuller audit [Germanic/data/old_english_wiktionary.tsv:44-44].
- If later DEV_NOTES consolidation creates a generic note on simple noun continuations with only final `-z` deletion and final bare-`-a` loss at issue, row 1978 could be attached there as a low-priority regular example rather than as an exception-driven case [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:746-752].

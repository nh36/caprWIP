---
row_id: 2223
concept: storm
counterpart: storm
proto: *stúrmaz
protoform: *stúrmaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2223 storm / storm

## Current row state

- The live OE row is `2223\tstorm\tPROTO *stúrmaz\tCOUNTERPART storm\tDERIVATION_CLASS regular`, and the table shows `PROTOFORM = *stúrmaz`, `COUNTERPART = storm`, plus only a duplicated provenance string in `HISTORY`: `Source: Wiktionary etymology (template:der) | Source: Wiktionary etymology (template:der)` [Germanic/data/germanic-aligned-final.tsv:1137-1137].
- `old_english_wiktionary.tsv` agrees on the OE target form and records the same imported provenance style: `storm\tstorm\tder\ttemplate:der\tstorm` [Germanic/data/old_english_wiktionary.tsv:283-283].
- `oe_known_problems.tsv` has no entry for row `2223`, for `storm`, or for `*stúrmaz`, so the row is not currently tracked as an OE exception, analogical repair, or known mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- The published OE derivation trace is a clean exact match: `PROTO: *stúrmaz`, `EXPECTED: storm`, `OUTPUTS: storm`, with the regular path `*stúrmaz > *stórmaz > *stórma > *stórm > storm` through Northwest Germanic `u`-lowering, final `-z` deletion, and final bare `-a` loss before surface orthography [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4786-4805].
- No reusable packet or research-memo stem was found for this row during this pass, so the canonical row-based filename `2223-storm-storm.md` is the appropriate replacement working note.

## Detailed development-note summary

No attachable storm-specific DEV_NOTES dossier presently survives in `Germanic/docs/DEV_NOTES.md`. Direct search for `storm`, `*stúrmaz`, and related lemma spellings did not produce a row-local project note, correction history, or implementation memo that can honestly be attached as a line-based fragment. This slice therefore has to stand in as a conservative replacement working note built from the live row, the current OE trace, and standard lexical references rather than from a dedicated DEV_NOTES argument.

The row itself is uncomplicated, and that simplicity needs to remain explicit. `PROTO` and `PROTOFORM` are both the comparative/input-side form `*stúrmaz`; `COUNTERPART` is the OE target `storm`; and `DERIVATION_CLASS` remains `regular` [Germanic/data/germanic-aligned-final.tsv:1137-1137]. Because the current trace already outputs `storm` without any exception logic, there is no positive evidence here for an analogical workaround, a rival OE form, or a hidden need to rewrite the row labels. The most useful project fact is simply that the regular cascade already works.

The derivational pathway is straightforward. In the published trace, the proto input `*stúrmaz` undergoes Northwest Germanic `u`-lowering to `*stórmaz`, then final `-z` deletion to `*stórma`, then final bare `-a` loss to `*stórm`, after which the surface output is `storm` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4793-4805]. For this row, that means the live project state already treats OE `storm` as an ordinary reflex of the comparative set, not as a lexeme that still needs custom chronology or morphology work.

Comparative handbooks agree with that ordinary reading, though they use their own lemma formatting rather than the project's accented row input. Kroonen gives `*sturma- m. 'storm'` with `ON stormr`, `OE storm`, `OS storm`, `Du. storm`, and `OHG sturm` [@Kroonen2013, p. 488]. Orel likewise gives `*sturmaz sb.m.` with `ON stormr id., OE storm id., OS storm id., OHG sturm id.` [@Orel2003, p. 384]. Clark Hall's OE dictionary simply lists `storm m. tempest, 'storm'` [@ClarkHall1960, s.v. "storm"]. Those references support the live row well, but they are external lexical confirmation, not surviving project-history prose.

One small thing that later work may need to keep separate is provenance metadata versus philological judgment. The row's duplicated `template:der` history string and the matching `old_english_wiktionary.tsv` `der` label are source-import traces, not by themselves an argument that OE `storm` is synchronically a special derivation inside this project [Germanic/data/germanic-aligned-final.tsv:1137-1137; Germanic/data/old_english_wiktionary.tsv:283-283]. The comparative dictionaries and the live OE trace both point instead to a stable inherited cognate set with a regular OE outcome [@Kroonen2013, p. 488; @Orel2003, p. 384].

The safest working conclusion is therefore narrow and conservative. Row `2223` is presently a regular, stable OE row with good comparative support and a successful trace, but the DEV_NOTES support is effectively absent rather than rich. That makes this slice useful as a replacement note, yet still a likely **no-index** case until genuinely row-local DEV_NOTES material, a packet, or a research memo exists.

## Relevant DEV_NOTES fragments with line-based refs

No attachable row-specific DEV_NOTES fragment was found for `storm` / `*stúrmaz`. Direct string search in `Germanic/docs/DEV_NOTES.md` did not locate a lexeme-specific note that can be cited with an honest `DEV_NOTES:line-...` reference, so there is currently no line-based fragment to attach for row `2223`.

## Superseded or diagnostic material

- No superseded storm-specific DEV_NOTES proposal currently survives. The real problem for this row is missing row-local note history, not a surviving abandoned analysis.
- The duplicated `template:der` provenance in the live TSV row and in `old_english_wiktionary.tsv` is diagnostic source bookkeeping only; it is not a substitute for a project-authored lexical argument [Germanic/data/germanic-aligned-final.tsv:1137-1137; Germanic/data/old_english_wiktionary.tsv:283-283].
- The successful OE derivation trace is important evidence that the row is stable, but it is still infrastructure output rather than DEV_NOTES prose [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4786-4805].
- `coverage_audit.md` previously listed the row as uncovered, which is useful only as workflow diagnostics, not as authority for the analysis: `| 2223 | storm | storm | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:375-375].

## Open questions for later work

- If row `2223` is ever to become indexable, the missing ingredient is a genuinely attachable DEV_NOTES fragment or dedicated row memo, not more proof that the current FST already outputs `storm`.
- If a later lexeme report cites handbook material, it should keep the label distinction explicit: handbook-style `*sturma-` or `*sturmaz` are comparative lemma formats, while the live row's `PROTO` and `PROTOFORM` remain the project's accented input `*stúrmaz` [@Kroonen2013, p. 488; @Orel2003, p. 384].
- A later cleanup pass may want to check whether the duplicated `template:der` provenance can be normalized or better explained, but nothing in the current row evidence requires changing `COUNTERPART storm` or `DERIVATION_CLASS regular`.

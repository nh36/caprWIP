---
row_id: 2222
concept: stork
counterpart: storc
proto: *stúrkaz
protoform: *stúrkaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2222 stork / storc

## Current row state

- The live OE row is `2222`, `CONCEPT stork`, `COUNTERPART storc`, `PROTO *stúrkaz`, `PROTOFORM *stúrkaz`, `DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:1133-1133].
- The row has no row-local OE note beyond duplicated provenance strings: `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)` [Germanic/data/germanic-aligned-final.tsv:1133-1133].
- `old_english_wiktionary.tsv` agrees on the OE form and inheritance status: `stork	storc	inh	template:inh	stork` [Germanic/data/old_english_wiktionary.tsv:282-282].
- `oe_known_problems.tsv` has no row-local entry for row `2222`, for `storc`, or for `*stúrkaz`; the row is not currently managed as an OE exception or unresolved bug bucket [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still treats the row as undocumented rather than disputed: `| 2222 | stork | storc | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:374-374].

## Detailed development-note summary

No attachable row-specific DEV_NOTES dossier currently survives for this item. Direct search of `Germanic/docs/DEV_NOTES.md` for `stork`, `storc`, and `*stúrkaz` did not locate a lexeme-specific paragraph, chronology note, or implementation fragment that can be cleanly tied to row `2222`. This slice therefore has to function as a replacement working note built from the live TSV row plus supporting lexical and trace evidence, not as an extraction from a pre-existing DEV_NOTES section.

The first thing to keep explicit is the row-label split. Here `PROTO` and `PROTOFORM` happen to coincide as `*stúrkaz`, but they still belong to the comparative/input side of the row; `COUNTERPART` is the OE target `storc` [Germanic/data/germanic-aligned-final.tsv:1133-1133]. Nothing in surviving project notes suggests a competing OE counterpart, a different protoform, or an analogy-driven rescue. The row is currently a regular masculine noun with identical `PROTO` and `PROTOFORM`, not a case where `COUNTERPART` should be silently replaced by a handbook citation form from another language.

The current derivational infrastructure also supports the row as fully regular. The published OE derivation trace gives `PROTO: *stúrkaz`, `EXPECTED: storc`, `OUTPUTS: storc`, and the stepwise path `*stúrkaz > *stórkaz > *stórka > *stórk > storc` through NWGmc `u`-lowering, final `-z` deletion, final bare `-a` loss, and OE orthographic surface output [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4766-4785]. That matters because the row currently does not need exception handling: the project already derives the target form by ordinary rule order.

External etymological support is coherent even though DEV_NOTES is silent. Orel's entry reads: `*sturkaz sb.m.: ON storkr 'stork', OE storc id., MLG stork id., OHG storah id.` and adds the semantic gloss that “The original meaning must have been 'stiff bird', 'bird standing without moving'” [@Orel2003, p. 384; docs/references/orel_handbook_germanic_etymology.vision.txt:42638-42645]. Kluge-Seebold gives the same family from the German side: `Aus g. *sturka- m. "Storch", auch in anord. storkr, ae. storc` and then explains the usual semantic proposal from `starr, Sterke` and the bird's stiff, stilted gait [@KlugeSeebold2011, s.v. "Storch"; docs/references/kluge_seebold_etymologisches_woerterbuch.txt:89082-89093]. Those sources do not create a row-specific OE philological note, but they do confirm that the live row's comparative alignment `*stúrkaz ~ storc` is not ad hoc.

Because the surviving evidence bundle is strong on lexical identity but thin on project history, the conservative project conclusion is narrow. Keep `PROTO *stúrkaz`; keep `PROTOFORM *stúrkaz`; keep `COUNTERPART storc`; keep `DERIVATION_CLASS regular`; and treat the row as a documented regular output whose main missing piece is not phonological repair but a lexeme-specific DEV_NOTES memo. That makes the slice useful as working infrastructure, but it also means the row is probably still better left no-index unless later work adds attachable DEV_NOTES material or a dedicated packet/memo.

## Relevant DEV_NOTES fragments with line-based refs

No attachable row-specific DEV_NOTES fragment was found for `stork` / `storc` / `*stúrkaz`. Direct string search in `Germanic/docs/DEV_NOTES.md` returned no lexeme-specific hits, so there is presently no honest line-based fragment ref to attach for row `2222`.

## Superseded or diagnostic material

- The duplicated Wiktionary provenance in the live TSV row is source bookkeeping only. It is useful for provenance, but it is not a project-authored argument about phonology, morphology, or lexical choice [Germanic/data/germanic-aligned-final.tsv:1133-1133].
- `coverage_audit.md` is diagnostic infrastructure, not authority for the row analysis. Its value here is simply to show that the row was still uncovered before this slice was created [Germanic/docs/lexeme_reports/coverage_audit.md:374-374].
- No packet or research memo stem exists to reuse for this row, which is why this slice uses the canonical row-based filename `2222-stork-storc.md`.

## Open questions for later work

- If row `2222` is ever to become indexable, the missing ingredient is a genuinely attachable DEV_NOTES fragment or a dedicated row memo, not more proof that the current trace outputs `storc`.
- A later final lexeme report could cite Orel and Kluge-Seebold directly for the comparative family and semantics, but should still keep the row labels explicit: comparative `PROTO/PROTOFORM *stúrkaz` versus OE `COUNTERPART storc` [@Orel2003, p. 384; @KlugeSeebold2011, s.v. "Storch"].
- If later philological work wants stronger OE-side support than the current inheritance line, the obvious next step is an OE dictionary citation or corpus note specific to `storc`, since the present slice relies mainly on the live TSV row, the derivation trace, and cross-Germanic etymological dictionaries.

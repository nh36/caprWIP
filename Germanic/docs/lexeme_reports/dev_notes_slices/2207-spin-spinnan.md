---
row_id: 2207
concept: spin
counterpart: spinnan
proto: *spínnaną
protoform: *spínnaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2207 spin / spinnan

## Current row state

- The live OE row reads `2207	spin	spinnan	*spínnaną	*spínnaną	regular`; it carries duplicated Wiktionary inheritance provenance and no row-local explanatory note beyond that source string [Germanic/data/germanic-aligned-final.tsv:1074-1074].
- For this row, `PROTO` and `PROTOFORM` are the same inherited verbal form `*spínnaną`. They are not a substitute paradigm cell, not a later OE-stage repair form, and not a neighboring lexeme borrowed for convenience. The OE `COUNTERPART` is the infinitive `spinnan` [Germanic/data/germanic-aligned-final.tsv:1074-1074].
- `old_english_wiktionary.tsv` independently maps English `spin` to OE `spinnan`, so the repo's lexical-source layer agrees with the live row's current target [Germanic/data/old_english_wiktionary.tsv:267-267].
- `oe_known_problems.tsv` currently lists unrelated exceptions only, so row `2207` is not being tracked as a live OE exception bucket or known mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- `coverage_audit.md` likewise treats row `2207` as ordinary uncovered regular material with no packet, memo, or report linkage yet attached: `| 2207 | spin | spinnan | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:363-363].
- The current derivation trace is an exact regular match: `PROTO: *spínnaną`, `EXPECTED: spinnan`, `OUTPUTS: spinnan`, with only routine OE-side steps `OE Heavy Syllable Nasal Apocope`, `OE Secondary Nasalization`, and `OE Weak Tail Reduction` before surface `spinnan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4526-4545].

## Detailed development-note summary

Direct DEV_NOTES support for row `2207` is extremely thin, and that absence is itself the main thing this slice needs to preserve. No surviving DEV_NOTES passage currently argues that OE `spinnan` is problematic, mismatched, or in need of a row-local repair. The live TSV row, the exact-match derivation trace, and the basic lexicographic comparanda all point in the same direction: this is a straightforward regular verb row, not a hidden exception dossier [Germanic/data/germanic-aligned-final.tsv:1074-1074; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4526-4545].

The comparative and OE reference works support the live row without needing any special project workaround. Kroonen reconstructs Proto-Germanic `*spinnan-` and lists OE `spinnan` among the reflexes [@Kroonen2013, p. 467]. Clark Hall has `spinnan³ to 'spin,'` as the ordinary OE verb entry [@ClarkHall1960]. Campbell likewise includes `spinnan spin` in his discussion of OE written geminates, treating it as an ordinary verb form rather than as a problematic or analogically displaced target [@Campbell1959, §52]. For present row policy, that means the clean distinction remains: `PROTO = *spínnaną`, `PROTOFORM = *spínnaną`, and `COUNTERPART = spinnan`.

What DEV_NOTES does preserve under nearby `spin-` searches is material for the separate row `2208` `spindle / spinl`, not for the verb `spin / spinnan`. The note quotes Clark Hall on the noun: `"spinel" f., gs. spinle 'spindle,' A, Cp.`, then explicitly discusses the syncopated variant `spinl` [Germanic/docs/DEV_NOTES.md:40295-40305]. Later in the same thread it states even more clearly: `Step 1 ... retargeted TSV row 2208 from spindle to spinl` [Germanic/docs/DEV_NOTES.md:42073-42080]. That material is valuable here only as a boundary marker. It shows that current DEV_NOTES `spin-` hits are about the neighboring spindle row's apocope and syncopation history, so they should not be imported into row `2207` as if they documented a verbal problem.

The replacement working conclusion is therefore conservative and simple. Row `2207` presently has no surviving DEV_NOTES fragment that needs to be indexed as current row-local authority. The row remains regular because all live evidence agrees with `*spínnaną → spinnan`, while the only nearby DEV_NOTES material belongs to row `2208` and is merely diagnostic for avoiding false attachment. This is exactly the kind of slice that should preserve a stable no-index note rather than overstate the evidential base.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-40295-40305

- Source heading: `Clark Hall spindle note`
- Source line or section hint: `lines 40295-40305`
- Status: `diagnostic_only`
- Issue tags: `neighboring_lexeme`; `spindle_not_spin`; `false_attachment_guard`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2208`

This fragment is not row-`2207` evidence in the positive sense; it is useful because it makes the neighboring lexeme explicit. DEV_NOTES quotes Clark Hall on OE `spinel` and adds the cross-reference `spinl, spinil = spinel` [Germanic/docs/DEV_NOTES.md:40297-40305]. For row `2207`, the value of the fragment is diagnostic only: it warns that a plain-text search for `spin` in DEV_NOTES currently lands on spindle material, not on the verb `spinnan`.

### DEV_NOTES:line-42073-42080

- Source heading: `§17.45.4 recap`
- Source line or section hint: `lines 42073-42080`
- Status: `diagnostic_only`
- Issue tags: `row_boundary`; `neighboring_lexeme`; `row_2208_only`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2208`

This later recap is the clearest explicit row-boundary marker. It says: `Step 1 ... retargeted TSV row 2208 from spindle to spinl`, and continues with the `spinnlu → spinlu` chronology for that noun row [Germanic/docs/DEV_NOTES.md:42077-42080]. For row `2207`, this fragment should be preserved only so later report work does not mistake a nearby `spin-` DEV_NOTES thread for evidence about `spinnan`.

## Superseded or diagnostic material

- The main diagnostic trap is lexical bleed from row `2208`. Forms such as `spinel`, `spinl`, `*spinilō`, `*spinnilō`, and `spinlu` belong to the spindle note, not to row `2207` `spin / spinnan` [Germanic/docs/DEV_NOTES.md:40297-40305,42077-42080].
- No superseded row-local OE target survives in DEV_NOTES for this verb. There is no preserved evidence that the row once targeted something other than `spinnan`, and no surviving note proposes a different `PROTOFORM` for the row.
- The strongest current support is therefore the ordinary alignment of sources, not a rescue note: `*spinnan-` in Kroonen, OE `spinnan` in Clark Hall, `spinnan spin` in Campbell, and an exact live derivation trace all point the same way [@Kroonen2013, p. 467; @ClarkHall1960; @Campbell1959, §52; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4526-4545].

## Open questions for later work

- If later report work wants this row to become indexable, it will probably need a genuine row-local packet, memo, or literature note; the current DEV_NOTES evidence is mostly negative and boundary-setting rather than substantive.
- If packet/research-memo infrastructure is expanded later, re-check whether an older `spin / spinnan` note exists under a non-obvious filename stem; no reusable stem was found during this pass, so the canonical row-based filename was used here.
- If source-provenance cleanup is undertaken later, row `2207` could replace duplicated Wiktionary source strings with denser local references, but nothing in the current evidence suggests any lexical retargeting or derivational-class change.

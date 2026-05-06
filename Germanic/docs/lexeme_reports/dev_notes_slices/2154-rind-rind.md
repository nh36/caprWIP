---
row_id: 2154
concept: rind
counterpart: rind
proto: *ríndō
protoform: *ríndō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2154 rind / rind

## Current row state

- CONCEPT: `rind` [Germanic/data/germanic-aligned-final.tsv:869-869]
- COUNTERPART: `rind` [Germanic/data/germanic-aligned-final.tsv:869-869]
- PROTO: `*ríndō` [Germanic/data/germanic-aligned-final.tsv:869-869]
- PROTOFORM: `*ríndō` [Germanic/data/germanic-aligned-final.tsv:869-869]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:869-869]
- The live row keeps `PROTO` and `PROTOFORM` identical. For this lexeme there is no separate paradigm-cell workaround, alternate OE-directed input, or row-local repair note in the TSV itself; the row is simply `*ríndō` targeting OE `rind` [Germanic/data/germanic-aligned-final.tsv:869-869].
- `old_english_wiktionary.tsv` also maps English `rind` to OE `rind`, so the row target is the ordinary OE lemma `rind`, not a reconstructed substitute or compound-only stand-in [Germanic/data/old_english_wiktionary.tsv:215-215].
- `oe_known_problems.tsv` currently has no entry for row `2154`, for `rind`, or for proto `*ríndō`; the file lists other exceptions and wontfix items only, so this row is not presently tracked as an open OE problem [Germanic/data/oe_known_problems.tsv:1-8].
- Current coverage infrastructure likewise shows no packet, memo, or dossier linked to this row: the coverage audit lists row `2154` as `regular`, with all report-link fields empty and issue status `none` [Germanic/docs/lexeme_reports/coverage_audit.md:327-327].
- The current published derivation trace is straightforward and regular: `PROTO: *ríndō`, then `NWGmc Final Long O Raising: *ríndu`, then `OE High Vowel Apocope: *rínd`, ending with `Outcome: rind` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3650-3669].

## Development-note summary

No dedicated rind-specific derivational dossier survives in `Germanic/docs/DEV_NOTES.md`. The only securely attachable DEV_NOTES passage that names this lexeme directly is a one-line orthography-policy note inside the older “Old English staging / TSV overhaul” section: “Open question: should the TSV adopt PGmc **ǭ** (e.g., *rindǭ*) instead of the current **ō**-only convention? For now we normalized to **ō** to keep the dataset consistent; revisit if we decide to shift the entire PGmc orthography” [Germanic/docs/DEV_NOTES.md:2386-2388]. That is the entire current DEV_NOTES payload for row `2154`: not a mismatch diagnosis, not an OE-target dispute, and not a request to reclassify the row, but a note about how the project writes this type of Proto-Germanic final long vowel.

For the live row, that orthography note matters in a narrow but concrete way. The row currently preserves `PROTO = PROTOFORM = *ríndō`, while the OE target is `rind` [Germanic/data/germanic-aligned-final.tsv:869-869]. DEV_NOTES uses unaccented example spelling `*rindǭ`, but the sentence is explicitly about the dataset's **`ō`-only convention**, not about replacing this row's lexical analysis or choosing a new OE comparator [Germanic/docs/DEV_NOTES.md:2388-2388]. In other words, the note does not tell reviewers to rewrite the row now; it tells them why a row of this shape may still appear in TSV-style data with final `-ō` rather than `-ǭ`.

That distinction is important because row `2154` otherwise looks entirely stable. The current derivation trace reaches `rind` with no special intervention: `*ríndō > *ríndu > *rínd > rind` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3657-3669]. There is no `oe_known_problems.tsv` entry, no attached packet or memo, and no DEV_NOTES fragment proposing an analogical repair, alternate paradigm cell, or literature-driven exception label [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:327-327]. Replacement working notes for this row should therefore preserve a very limited but explicit conclusion: the row is currently regular, and the only DEV_NOTES material worth carrying forward is the statement that project orthography currently normalizes possible `ǭ`-type spellings to `ō`.

Because the DEV_NOTES mention is so thin, the row-level distinction between `PROTO`, `PROTOFORM`, and OE target must be kept explicit in the slice itself rather than inferred from a nonexistent dossier. At present `PROTO` and `PROTOFORM` are both `*ríndō`; the OE target is `rind`; and DEV_NOTES' `*rindǭ` example is best treated as a possible future orthographic restatement of the same comparative layer, not as a separate current row input [Germanic/data/germanic-aligned-final.tsv:869-869; Germanic/docs/DEV_NOTES.md:2388-2388].

## Relevant DEV_NOTES fragments

No securely attachable dedicated **derivational** DEV_NOTES fragment survives for row `2154`. The only current fragment worth indexing is the orthography-convention line below.

### DEV_NOTES:line-2388

- Source heading: `Old English staging / TSV overhaul (PGmc → OE layer)`
- Source line or section hint: `line 2388`
- fragment_type: `lexeme_specific`
- current_status: `current`
- Issue tags: `proto_orthography`; `ǭ_notation`; `protoform_vs_proto`; `row_policy`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

DEV_NOTES states: “Open question: should the TSV adopt PGmc **ǭ** (e.g., *rindǭ*) instead of the current **ō**-only convention? For now we normalized to **ō** to keep the dataset consistent; revisit if we decide to shift the entire PGmc orthography” [Germanic/docs/DEV_NOTES.md:2388-2388]. For row `2154`, this is the only DEV_NOTES sentence that names the lexeme directly, so its scope has to be described precisely. What it establishes is a current project-writing convention: rows of this type remain written with final `-ō` in the dataset unless and until the entire PGmc orthography is migrated.

The fragment does **not** establish any special OE problem for `rind`. It does not argue that the live row should stop targeting OE `rind`, does not supply a different derivational input, and does not discuss any mismatch in the current cascade [Germanic/data/germanic-aligned-final.tsv:869-869; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3650-3669]. Its practical use is narrower: when a reviewer asks why the row is still written `*ríndō` instead of some `ǭ` spelling, this line is the project authority saying that `ō`-normalization is deliberate and still current.

## Superseded or diagnostic material

- The surrounding DEV_NOTES section is itself marked as an older, completed staging block, so row `2154` should not inherit an obsolete workflow task from that heading. What remains live for this row is only the convention statement at line 2388 about `ō`-normalization [Germanic/docs/DEV_NOTES.md:2386-2388].
- DEV_NOTES' example spelling `*rindǭ` is diagnostic for orthography policy only. It should not silently overwrite the live row's `PROTO`/`PROTOFORM` spelling `*ríndō`, because the DEV_NOTES line does not discuss the row's accent notation, does not announce a committed row rewrite, and does not distinguish a new `PROTOFORM` from a new `PROTO` [Germanic/data/germanic-aligned-final.tsv:869-869; Germanic/docs/DEV_NOTES.md:2388-2388].
- The absence of any row-local problem entry or linked report is itself part of the current state. There is no surviving DEV_NOTES mismatch note to mine beyond the orthography line, so later reviewers should not assume that a hidden rind exception dossier exists elsewhere in the current repo [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:327-327].

## Open questions for later work

- If the project ever shifts from the current `ō`-only convention to explicit PGmc `ǭ`, determine exactly how row `2154` should be restated and whether that change affects only the final-vowel symbol or also the current accent-marking layer (`*ríndō` vs. a possible `*ríndǭ`/`*rindǭ`) [Germanic/docs/DEV_NOTES.md:2388-2388; Germanic/data/germanic-aligned-final.tsv:869-869].
- If `Germanic/docs/lexeme_reports/dev_notes_slices/index.tsv` is updated later, one index row anchored to `DEV_NOTES:line-2388` is probably sufficient; there is no second securely attachable current DEV_NOTES fragment for `rind`.
- If later literature work produces a packet or memo for this lexeme, keep the current row-policy statement narrow: `PROTO = PROTOFORM = *ríndō`, OE target `rind`, regular derivation `*ríndō > *ríndu > *rínd > rind`, and DEV_NOTES relevance limited to the orthography-convention note [Germanic/data/germanic-aligned-final.tsv:869-869; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3650-3669].

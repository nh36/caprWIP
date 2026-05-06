---
row_id: 2038
concept: gang
counterpart: gang
proto: *gángaz
protoform: *gángaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2038-gang-gang.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2038-gang-gang.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2038 gang / gang

## Current row state

- CONCEPT: `gang`
- COUNTERPART: `gang`
- PROTO: `*gángaz`
- PROTOFORM: `*gángaz`
- DERIVATION_CLASS: `regular`
- Live TSV note: `PGmc *gangaz is a-stem noun > OE gang; cf. Dutch gang, German Gang` [Germanic/data/germanic-aligned-final.tsv:419].
- Packet status is clean and regular: `EXPECTED: gang`, `OUTPUTS: gang`, with the derivation reduced to ordinary `PGmc Final Z Deletion` followed by `PWGmc Final Bare A Loss` [Germanic/docs/lexeme_reports/packets/2038-gang-gang.md:17-42].
- `oe_known_problems.tsv`: no row-specific entry was found for `2038`, `*gángaz`, or `gang`, which matches the row's present regular status [Germanic/docs/lexeme_reports/packets/2038-gang-gang.md:44-46; Germanic/docs/lexeme_reports/research_memos/2038-gang-gang.md:50-52].
- `report_manifest.tsv`: no manifest entry is currently attached for this lexeme [Germanic/docs/lexeme_reports/packets/2038-gang-gang.md:11-13].
- The research memo identifies the real working issue as evidence hygiene rather than phonological repair: keep the inherited noun `gang` separate from the verb `gangan` and from stale verbal diagnostics elsewhere in the repo [Germanic/docs/lexeme_reports/research_memos/2038-gang-gang.md:13-31, 83-91].

## Development-note summary

No securely attachable **row-specific** DEV_NOTES authority survives for row 2038. The packet records no DEV_NOTES hits at all, and the memo's direct repo review concludes that the only relevant-looking DEV_NOTES material is actually about the verb **gangan** and past **géong**, not about the noun row `*gángaz -> gang` [Germanic/docs/lexeme_reports/packets/2038-gang-gang.md:48-60; Germanic/docs/lexeme_reports/research_memos/2038-gang-gang.md:50-58].

What *does* survive as current row policy is straightforward and should be stated explicitly so that this slice can replace a return trip through the packet and memo. The live row is a regular inherited noun derivation: comparative/project input `*gángaz`, OE target `gang`, and no need for analogical rescue, paradigm-cell substitution, or exception handling [Germanic/data/germanic-aligned-final.tsv:419; Germanic/docs/lexeme_reports/packets/2038-gang-gang.md:17-42]. The memo is right to separate three levels that could otherwise be conflated: comparative noun headword `*gangaz`, stress-marked project input `*gángaz`, and OE noun target `gang` [Germanic/docs/lexeme_reports/research_memos/2038-gang-gang.md:60-70]. None of those levels requires revision in the present workflow.

The replacement-note value of this slice therefore lies in preserving a **negative** but important conclusion: DEV_NOTES should not be mined for noun authority here. The one checked DEV_NOTES passage discusses Campbell's glide-vowel evidence from the verbal family, quoting Northumbrian `geong` and `geonga` as forms related to past `géong`; DEV_NOTES then glosses that material under the verb `*gangan* 'to go'` [DEV_NOTES:line-11443-11450]. That may be useful for the verb lexeme family, but it is not authority for row 2038's noun citation form `gang`.

The other durable workflow point is lexeme disambiguation. The packet's only local lexical-table hit maps English **gang** to OE **gangan**, which the memo explicitly rejects as misleading for this noun row [Germanic/docs/lexeme_reports/packets/2038-gang-gang.md:66-76; Germanic/docs/lexeme_reports/research_memos/2038-gang-gang.md:29-31, 83-91]. Later report writing should therefore keep the part of speech overt: row 2038 is the noun **gang**, not the verb **gangan**, and the absence of a row-local DEV_NOTES dossier does not signal a missing repair. It signals that the row is already regular and that the main risk is false-positive evidence capture.

## Relevant DEV_NOTES fragments

No securely attachable **current** row-specific DEV_NOTES fragment survives. The reviewed range below is kept only so later packet or index work has an explicit record of the checked false positive.

### DEV_NOTES:line-11443-11450

- Source heading: `Campbell quotation on geong/geonga from the verb gangan`
- Source line or section hint: `lines 11443-11450`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `verb_noun_confusion`; `false_positive`; `lexeme_disambiguation`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This range preserves Campbell's quotation, “Other North. forms with glides are **geong way, geonga go** (both with í transferred from past **géong**)”, and DEV_NOTES immediately explains the point in terms of the verb `*gangan* 'to go'` [DEV_NOTES:line-11443-11450]. Even though `geong` 'way' is semantically adjacent to the noun family, the passage is part of a glide-vowel argument about the verbal complex and not about the noun citation form `gang`. For row 2038 it should remain a checked false positive, not attached lexical authority.

## Superseded or diagnostic material

There is no surviving row-specific superseded analysis of the usual kinds seen elsewhere in these slices: no abandoned `PROTOFORM`, no target correction, no derivation-class rewrite, and no paradigm probe that later got reversed. The row is regular now and appears to have been regular all along in the live noun analysis [Germanic/data/germanic-aligned-final.tsv:419; Germanic/docs/lexeme_reports/packets/2038-gang-gang.md:17-42].

The diagnostic material is instead evidence-control noise. First, DEV_NOTES contains only the verbal-family false positive at `DEV_NOTES:line-11443-11450`. Second, the packet's local lexical-table hit points to `gangan`, not to noun `gang`, and should not be reused as OE noun attestation [Germanic/docs/lexeme_reports/packets/2038-gang-gang.md:66-76; Germanic/docs/lexeme_reports/research_memos/2038-gang-gang.md:29-31, 72-80, 83-91]. If later index cleanup trims reviewed-only false positives, preserve at minimum the explicit statement that row 2038 has **no securely attachable row-specific DEV_NOTES authority** rather than implying that a richer hidden dossier was omitted.

## Open questions for later work

- If a final lexeme report is drafted, make the part of speech explicit as **noun** `gang` so that packet or lexical-table noise cannot slide back toward the unrelated verb `gangan`.
- If later report prose wants direct OE attestation beyond the live TSV and packet trace, cite the memo's lexicographic authorities directly rather than reusing the packet's misleading `gangan` table hit [Germanic/docs/lexeme_reports/research_memos/2038-gang-gang.md:50-58, 72-80].
- If future packet or index cleanup suppresses reviewed-only false positives, keep at least the reviewed DEV_NOTES line hint `DEV_NOTES:line-11443-11450` and the statement that it was rejected as non-row authority.

---
row_id: 2118
concept: malt
counterpart: mealt
proto: *máltaz
protoform: *máltaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current_shared_only
needs_literature_agent: no
---

# DEV_NOTES material — 2118 malt / mealt

## Current row state

- The live OE row is straightforward and currently stable: `CONCEPT = malt`, `COUNTERPART = mealt`, `PROTO = *máltaz`, `PROTOFORM = *máltaz`, `DERIVATION_CLASS = regular`, with only duplicated imported provenance in the history field and no row-local explanatory note in the TSV itself [Germanic/data/germanic-aligned-final.tsv:729-729].
- `PROTO` and `PROTOFORM` currently coincide, and no surviving row-specific project note argues for splitting them, swapping in a paradigm-cell proxy, or reclassifying the row away from `regular` [Germanic/data/germanic-aligned-final.tsv:729-729].
- The row is not presently carried as an OE exception. `oe_known_problems.tsv` lists only unrelated `u`-lowering and analogy cases, with no entry for row `2118`, `malt`, `mealt`, or `*máltaz` [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage/report infrastructure is still absent for this row. `coverage_audit.md` lists `| 2118 | malt | mealt | regular | no | - | - | - | none |`, `report_manifest.tsv` has no report entry for row 2118, and `research_memo_index.tsv` jumps from row 2114 to row 2120 with no `2118` packet or memo assignment [Germanic/docs/lexeme_reports/coverage_audit.md:305-305; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14; Germanic/docs/lexeme_reports/research_memo_index.tsv:56-64].
- The current derivation/debug state is a clean exact match. The published OE trace gives `PROTO: *máltaz`, `EXPECTED: mealt`, `OUTPUTS: mealt`, with the staged path `*máltaz > *málta > *mált > *mælt > *mealt`, i.e. final `-z` deletion, final bare `-a` loss, Anglo-Frisian brightening, and OE breaking [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3104-3123].
- The shared A-restoration research inventory independently repeats the same classification line, `| 2118 | *máltaz | mealt | breaking |`, which is useful as confirmation of current project treatment but is still only shared analysis scaffolding, not a dedicated lexeme memo [Germanic/docs/analysis/arestoration_r_l_research.md:737-737].

## Development-note summary

No row-specific `malt / mealt` DEV_NOTES block currently survives. That absence needs to be stated plainly. The only securely attachable DEV_NOTES material for row 2118 is shared-background material about OE breaking chronology, a later cross-row inventory that names `*máltaz -> mealt` directly, and a subsequent side-effect audit saying breaking rows were unaffected by A-restoration work [Germanic/docs/DEV_NOTES.md:2575-2579; Germanic/docs/DEV_NOTES.md:30604-30634; Germanic/docs/DEV_NOTES.md:36625-36629].

That means the replacement note has to be conservative. The row is presently best understood not through a lost row dossier but through the combination of (a) live TSV state, (b) current successful derivation trace, and (c) shared DEV_NOTES statements that classify `mealt` as an ordinary OE breaking outcome in the `*a + lC` environment [Germanic/data/germanic-aligned-final.tsv:729-729; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3104-3123; Germanic/docs/DEV_NOTES.md:30604-30634].

The core derivational reading is stable and should be kept explicit: comparative/input-side `PROTO` and OE-facing `PROTOFORM` are both still `*máltaz`; the target OE form is `mealt`; and the current cascade reaches that target by the regular sequence `*máltaz > *málta > *mált > *mælt > *mealt` [Germanic/data/germanic-aligned-final.tsv:729-729; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3113-3123]. Nothing in the surviving DEV_NOTES material suggests an analogical workaround, a rival OE target, or a need to reinterpret the row as anything other than a regular breaking item.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2575-2579

- Source heading: `OE breaking reorder + diagnostics (2025-12-22)`
- Source line or section hint: `lines 2575-2579`
- Fragment type: `shared_background_rule_statement`
- Status: `current`
- Issue tags: `oe_breaking`; `chronology`; `shared_background_only`; `rule_order`
- Recommended next use: `cite_as_shared_rule_background`
- Shared with row IDs: `1975,2002,2008,2025,2077,2118,2166,2289,2297`

This is shared-background-only, but it is the clearest surviving DEV_NOTES statement of the breaking rule that row 2118 depends on. DEV_NOTES says: “**Breaking now precedes GH-marking and W-glide** so the conditioning consonants are still visible when OE breaking applies,” and adds that the “**Sandbox breaking rules [are] aligned to OE** (`*a/*æ → *ea`, `*e → *eo`, `*i → *ie` in `rC/lC/h/w` contexts)” [Germanic/docs/DEV_NOTES.md:2575-2579]. For `*máltaz -> mealt`, that shared rule statement supplies the surviving project rationale for the final vocalic step: once the row has reached brightened `*mælt`, the `lC` context licenses ordinary OE breaking to `*mealt`.

This fragment should not be overstated. It does not mention `malt` by name and it is not a row dossier. Its value is methodological and chronological: it records which version of OE breaking the project means when later materials classify row 2118 as a breaking form [Germanic/docs/DEV_NOTES.md:2575-2579]. For this row, the substance worth carrying forward is therefore the rule statement itself, not any claim of lexeme-specific debate.

### DEV_NOTES:line-30604-30634

- Source heading: `Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail`
- Source line or section hint: `lines 30604-30634, especially 30625`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `breaking`; `regular_row`; `shared_inventory`; `a_plus_lc`; `row_classification`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1975,2008,2025,2077,2166,2167,2204,2271`

This is the main securely attachable DEV_NOTES fragment for row 2118 because it names the row directly. Inside a broader audit of OE rows with proto `*aCl/*aCr` shapes, DEV_NOTES gives the table entry `| 2118 | *máltaz | mealt | breaking |` [Germanic/docs/DEV_NOTES.md:30609-30634]. The immediate context matters: the section is asking whether an A-restoration fix for another row would have side effects on related shapes, and `mealt` appears there not as a problem case but as one of the ordinary controls [Germanic/docs/DEV_NOTES.md:30601-30604,30625-30625].

For row 2118, this fragment is row-specific in naming but still shared in function. It tells later work two concrete things and little more: first, the project classifies `mealt` as a regular breaking outcome; second, row 2118 is outside the special A-restoration problem that motivated the audit [Germanic/docs/DEV_NOTES.md:30604-30634]. This is current support, but it is classificatory rather than discursive. Later writeups should preserve the exact classification without pretending that DEV_NOTES preserves a richer `malt` monograph than it actually does.

### DEV_NOTES:line-36625-36629

- Source heading: `side-effect audit after the A-restoration cleanup`
- Source line or section hint: `lines 36625-36629`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `breaking`; `a_restoration`; `stability_after_fix`; `shared_background_only`
- Recommended next use: `cite_for_stability_claim`
- Shared with row IDs: `1975,2008,2025,2077,2118,2166,2167,2204,2271`

This fragment is shared-background-only but important for current stability. DEV_NOTES says: “**For breaking-conditioned rows (`*xármaz, *márkō, *kálbaz, *fállaną` etc., 21 rows total), A-restoration is bled by breaking; unaffected.**” [Germanic/docs/DEV_NOTES.md:36628-36629]. Row 2118 is not named again there, but the earlier inventory had already placed `*máltaz -> mealt` in that same breaking-conditioned class [Germanic/docs/DEV_NOTES.md:30625-30625].

The practical use of this fragment is narrow and should stay narrow. It is not evidence for choosing `mealt` in the first place; it is evidence that later A-restoration work was explicitly understood not to disturb rows of the `mealt` type [Germanic/docs/DEV_NOTES.md:36625-36629]. For replacement-note purposes, that makes it a current stability statement rather than a philological source argument.

## Superseded or diagnostic material

No row-specific superseded `malt / mealt` DEV_NOTES block survives. The honest diagnostic fact is not that there was a rich earlier debate now obsolete, but that row 2118 seems never to have accumulated one. The surviving record is shared-background classification plus current successful tracing, not abandoned lexeme-specific theories [Germanic/docs/DEV_NOTES.md:2575-2579; Germanic/docs/DEV_NOTES.md:30604-30634].

`coverage_audit.md` is diagnostic only here. Its line `| 2118 | malt | mealt | regular | no | - | - | - | none |` is useful because it explains why this slice has to do replacement work at all, but it is not authority for the historical analysis [Germanic/docs/lexeme_reports/coverage_audit.md:305-305]. Likewise, the repeated inventory line in `arestoration_r_l_research.md` and the clean published trace are important for workflow and current-state validation, but they are not themselves DEV_NOTES prose and should not be cited as though they preserve a missing row memorandum [Germanic/docs/analysis/arestoration_r_l_research.md:737-737; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3104-3123].

One further caution: because the surviving DEV_NOTES evidence is almost entirely shared-background-only, later writers should not import argument from nearby `sealt`, `sealf`, `healdan`, or other `*a + lC` rows as though it were automatically row-2118-specific. Those rows belong to the same broad breaking class, but the only direct row-2118 DEV_NOTES hit is still the inventory line `| 2118 | *máltaz | mealt | breaking |` [Germanic/docs/DEV_NOTES.md:30625-30625].

## Open questions for later work

- If a fuller lexeme report is ever needed, the missing ingredient is a genuinely row-specific packet or memo. `report_manifest.tsv` and `research_memo_index.tsv` currently have no 2118 entry, so this slice is necessarily standing in for absent infrastructure as well as absent row-local DEV_NOTES prose [Germanic/docs/lexeme_reports/report_manifest.tsv:1-14; Germanic/docs/lexeme_reports/research_memo_index.tsv:56-64].
- If later report writing wants explicit handbook support for `mealt`, it will need to add that from the literature directly; the surviving DEV_NOTES material for this row is enough to prove project classification and stability, but thin on embedded primary-source quotation.
- If `dev_notes_slices/index.tsv` is updated in a later pass, the safest anchors for row 2118 are the shared breaking-rule statement (`2575-2579`), the direct inventory hit (`30604-30634`, especially 30625), and the later A-restoration stability audit (`36625-36629`), with their differing evidentiary statuses kept explicit.

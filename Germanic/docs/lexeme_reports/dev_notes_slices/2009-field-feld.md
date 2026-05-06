---
row_id: 2009
concept: field
counterpart: feld
proto: *félθuz
protoform: *félθuz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2009-field-feld.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2009-field-feld.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2009 field / feld

## Current row state

- CONCEPT: `field`
- COUNTERPART: `feld`
- PROTO: `*félθuz`
- PROTOFORM: `*félθuz`
- DERIVATION_CLASS: `regular`
- Live TSV note: `R/T §5.1.3 p.171: *felθu-/*feldu- may reflect Verner's alternation or regular PWGmc *lθ→*ld; either gives OE feld.`
- `oe_known_problems.tsv`: no entry for `*félθuz` or `feld`, which matches the row's present status as a solved regular derivation rather than a live exception file.
- `report_manifest.tsv`: no manifest entry for row 2009.
- Packet and research-memo review agree on the basic current claim: the live row is stable as `*félθuz -> feld`, and the reason the row still needs a note is explanatory rather than corrective. The issue is how to describe medial `-ld-`, not how to repair the row.

## Development-note summary

Row 2009 does have securely attachable DEV_NOTES authority, but it is narrow and should be kept narrow. The controlling current discussion is the early Verner/`*lþ > ld` note at `DEV_NOTES:line-1334-1356`. That passage preserves the exact handbook ambiguity that the live TSV note still mirrors: Ringe-Taylor treat `feld` as one of the cases where `*felþu- ~ *feldu-` could reflect inherited `*þ ~ *d` alternation, but they also allow the ordinary West Germanic `*lþ > ld` development. DEV_NOTES then makes the project decision explicit rather than leaving the row in theoretical suspense: “EITHER explanation yields the correct OE outcome,” and where the regular sound change already gives the correct result, “we use it (gold, feld, fealdan, etc.)” [DEV_NOTES:line-1338-1355; @RingeTaylor2014, §5.1.3, p. 171]. For normal workflow, that means the row stays `regular`, keeps `PROTO = PROTOFORM = *félθuz`, and does **not** wait on a future global Verner's Law implementation.

The slice also needs to preserve a second point that is easy to lose if one only reads the current TSV row: `feld` reappears in DEV_NOTES later not because the etymological analysis changed, but because regression work briefly broke an already-acceptable row. An older PGmc→OE TODO list still named `felþu` among outputs showing that final high-vowel apocope had not yet been generalized far enough, so the system was once failing before both final-vowel cleanup and the now-stable `-ld-` handling were in place [DEV_NOTES:line-2422-2430]. A much later probe table shows the newer, narrower failure mode: `*félθuz` was then producing `feldo` rather than `feld`, i.e. the row had advanced past the old `felþu` stage but still retained a stray final vowel after the consonant history had otherwise converged on `-ld-` [DEV_NOTES:line-24451-24459]. Those later mentions are important project chronology, but they do **not** authorize any change to `PROTOFORM`; they only explain why a regular row continued to surface in debugging notes.

Taken together, the replacement working note for row 2009 should preserve three distinct levels. First, the live philological/modeling position is conservative and current: `feld` is an attested OE target, and the project is content to derive it directly from `*félθuz` with the existing `PWGmcLThVoicing` treatment while leaving the underlying historical ambiguity in the NOTE field [DEV_NOTES:line-1334-1356]. Second, the older `felþu` and later `feldo` stages are not competing reconstructions; they are superseded regression snapshots showing how the row behaved before high-vowel apocope and final cleanup were stabilized [DEV_NOTES:line-2422-2430; DEV_NOTES:line-24451-24459]. Third, no stronger row-specific DEV_NOTES dossier survives beyond those points: the packet's other `field` hits are generic uses of the English word *field* or unrelated prose, not additional authority for row 2009. Later report prose should therefore stay explicit about what is current, what is merely diagnostic history, and what was rejected as search noise.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1334-1356

- Source heading: `Ambiguous examples (rule OR Verner's Law)` plus `Scope of Verner's Law in the project`
- Source line or section hint: `lines 1334-1356`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `lth_voicing`; `verners_law`; `regular_derivation`; `protoform_stable`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2043, 2136`

This is the main current fragment for row 2009 and should carry most of the report-facing load. It records the exact ambiguity the row note still needs: Ringe-Taylor cite `*felþu- ~ *feldu-` as an example where OE `feld` can be read either through inherited `*þ ~ *d` alternation or through the ordinary West Germanic `*lþ > ld` development [@RingeTaylor2014, §5.1.3, p. 171]. DEV_NOTES immediately states the project's operational conclusion: “EITHER explanation yields the correct OE outcome,” and the project therefore keeps `feld` with the cases where the regular sound change is enough — “gold, feld, fealdan, etc.” — while rows that **require** a separate Verner solution remain mismatches instead [DEV_NOTES:line-1340-1356]. For this row, that means the ambiguity belongs in explanatory prose, not in row metadata changes.

### DEV_NOTES:line-2422-2430

- Source heading: `PGmc→OE TODOs (consolidated)`
- Source line or section hint: `lines 2422-2430`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `high_vowel_apocope`; `old_output`; `debugging_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This fragment is worth retaining only because it captures the oldest row-specific failure state that DEV_NOTES still names directly. The TODO list says high-vowel apocope needs expanding and gives `felþu` as one of the observed `-u` outputs that should disappear once final `*i/*u` deletion is properly conditioned [DEV_NOTES:line-2426-2430]. For row 2009, that is diagnostic archaeology rather than present evidence: it shows the row once failed before final cleanup was mature, but it does not support any alternative protoform, target, or derivation class.

### DEV_NOTES:line-24451-24459

- Source heading: `probe outcome table showing new *CVCuz regressions`
- Source line or section hint: `lines 24451-24459`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `final_vowel_regression`; `apocope_cleanup`; `debugging_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This later probe table records the last named regression stage for the row: `*félθuz` was producing `feldo` instead of `feld` [DEV_NOTES:line-24453-24459]. That matters because it shows a different kind of failure from the older `felþu` note. By this point the consonant history had already converged on `-ld-`, so the remaining problem was the stray final vowel, not the `*lþ ~ *ld` question. For later working notes, this fragment should be used only to explain project chronology: row 2009 re-entered DEV_NOTES during regression cleanup, not because the project reopened its basic etymological analysis.

## Superseded or diagnostic material

The superseded material for row 2009 is unusually clean. There is no abandoned paradigm-cell rescue, no later switch in `PROTOFORM`, and no live argument that `feld` should be reclassified as a mismatch. The non-current material is almost entirely regression archaeology: first `felþu` in the early high-vowel-apocope TODO, then `feldo` in a later probe table. Both are useful to keep because they show the row passed through more than one failure mode on the way to the present regular output, but neither has any authority over the current row metadata.

The other packet hits should stay rejected. The packet's many matches on the ordinary English word *field* are search collisions, not lexical evidence for row 2009. If later packet or index cleanup trims reviewed-only noise, preserve at minimum the explicit distinction that row 2009 has a **real** current DEV_NOTES fragment at `line-1334-1356`, plus two row-specific diagnostic fragments, and not a larger hidden dossier beyond that.

## Open questions for later work

- Decide whether the final lexeme report should quote the DEV_NOTES sentence “EITHER explanation yields the correct OE outcome” directly, since it neatly captures why the row stays regular despite the historical ambiguity.
- If later report prose wants extra philological texture, it may add the memo's dictionary and Campbell background on attested `feld` and early `-felth` spellings, but that would be supplementary support rather than a change to row policy.
- If central index work records diagnostic history, keep the chronology explicit: old `felþu` stage, later `feldo` stage, current `feld` stage.

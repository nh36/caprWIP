---
row_id: 2110
concept: loath
counterpart: lāþ
proto: '*láiθaz'
protoform: '*láiθaz'
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2110 loath / lāþ

## Current row state

- Live OE row `2110` currently reads `CONCEPT = loath`, `COUNTERPART = lāþ`, `PROTOFORM = *láiθaz`, `PROTO = *láiθaz`, `DERIVATION_CLASS = regular`, with history note `Source: Wiktionary etymology (template:inh) | TSV: ð→þ (allographic convention)` [Germanic/data/germanic-aligned-final.tsv:698-698].
- `PROTO` and `PROTOFORM` are identical in the live row, so no substitute paradigm-cell input, no later-stage proxy form, and no repair protoform is currently being stored for this lexeme; the attested/target OE form is simply `lāþ` [Germanic/data/germanic-aligned-final.tsv:698-698].
- `coverage_audit.md` still treats the row as documentation-light regular material rather than as an already-dossiered exception: `| 2110 | loath | lāþ | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:298-298].
- `report_manifest.tsv` still contains only the pilot/report rows and has no entry for `2110`, so there is no pre-existing packet/report registration to inherit for this slice [Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- No row-specific `oe_known_problems.tsv` entry survives for `2110`, `lāþ`, or `*láiθaz`; in current repo state the row is not being tracked as an OE exception bucket.
- The published OE derivation trace is an exact match and is very short: `*láiθaz` → `*lāθaz` (`PWGmc Ai Monophthongization`) → `*lāθa` (`PGmc Final Z Deletion`) → `*lāθ` (`PWGmc Final Bare A Loss`) → orthographic `*lāþ` → `lāþ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2963-2983].

## Development-note summary

No row-local DEV_NOTES dossier for `lāþ` survives in the live file. The only direct row hit in `DEV_NOTES.md` is a diagnostic table entry marking row `2110` as `irrelevant`, and that label is narrow: it means `*láiθaz > lāþ` is irrelevant to the specific `*aCl/*aCr` + back-vowel-tail A-restoration problem being audited in the `nafola` dossier, not that the lexeme itself lacks a regular derivation or should be ignored [Germanic/docs/DEV_NOTES.md:30599-30627].

Accordingly, the usable DEV_NOTES support for this row is **shared-background-only**, not lexeme-specific. The surviving material says that stressed West Germanic `*ai` regularly monophthongizes to `*ā`, and one shared worked example explicitly adds that final `*-az` does not create an umlaut environment and is then lost regularly [Germanic/docs/DEV_NOTES.md:6423-6428,13945-13953]. That shared rule-set is exactly what the current row needs: `PROTO = PROTOFORM = *láiθaz`, while `COUNTERPART = lāþ` is the attested/target OE reflex after regular monophthongization and final-tail loss, with the TSV's `ð→þ` note making only an orthographic-allographic normalization point rather than positing a different phonological output [Germanic/data/germanic-aligned-final.tsv:698-698; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2963-2983].

The conservative replacement note therefore has to preserve two negative facts. First, there is **no surviving row-specific DEV_NOTES block** to quote for `lāþ`. Second, there is likewise no current evidence in repo state that the row needs a special exception story, alternate protoform, or repaired target. Everything currently visible points the other way: row `2110` is a straightforward exact-match regular row whose philological support is mostly generic rather than row-dedicated [Germanic/docs/lexeme_reports/coverage_audit.md:298-298; Germanic/docs/DEV_NOTES.md:30599-30627; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2963-2983].

## Relevant DEV_NOTES fragments

### DEV_NOTES:30599-30627

- Source heading: `§17.19.4 Other potentially affected words`
- Source line hint: `lines 30599-30627`
- Fragment type: `diagnostic_row_mention`
- Status: `current_but_diagnostic_only`
- Issue tags: `a_restoration_scope`; `negative_result`; `row_seen_in_dev_notes`
- Recommended next use: `quote_only_when_explaining_why_no_row_local_dossier_survives`
- Shared-with rows if relevant: `table rows surveyed against the *náblô / nafola aCl-tail bug family`

This is the only direct DEV_NOTES hit for row `2110`, and it needs to be handled carefully. The fragment comes from a scan of OE rows that might be affected by the `*nablô > nafola` problem, specifically rows with proto `*aCl-*` or `*aCr-*` before a back-vowel tail. In that inventory the row appears simply as ``| 2110 | *láiθaz | lāþ | irrelevant |`` [Germanic/docs/DEV_NOTES.md:30604-30627]. The important point is diagnostic scope: `irrelevant` here means “not part of this A-restoration cluster-tail problem set,” not “unsupported lexeme” or “discard this row.” For later work, the table should be used only to explain why no `nafola`-style repair discussion applies to `lāþ`.

### DEV_NOTES:13945-13953

- Source heading: `Per user feedback, the stressed vs. unstressed *ai monophthongization should be treated as TWO SEPARATE CHANGES at different chronological stages`
- Source line hint: `lines 13945-13953`
- Fragment type: `shared_background_sound_law`
- Status: `current`
- Issue tags: `stressed_ai_to_a`; `shared_background_only`; `regular_reflex`
- Recommended next use: `cite_when_defending_regular *láiθaz > lāþ`
- Shared-with rows if relevant: `all OE rows whose live derivation depends on stressed WGmc *ai > *ā`

This fragment is not about `lāþ` by name, but it preserves the cleanest current project statement of the sound law this row actually uses. DEV_NOTES says: “**PWGmc `*ai → *ā` (stressed): Traditional West Germanic monophthongization. Already in place in PWGmc for stressed syllables. Example: PGmc `*hailaz` → PWGmc `*hālaz` → OE `hāl`**” [Germanic/docs/DEV_NOTES.md:13949-13953]. Row `2110` has the same relevant structure: stressed `*ai` in the root, no competing proxy `PROTOFORM`, and an OE target with long `ā`. The support is therefore shared-background-only, but it is genuinely probative for `*láiθaz > lāþ`.

### DEV_NOTES:6423-6428

- Source heading: `For an a-stem *flaiskaz`
- Source line hint: `lines 6423-6428`
- Fragment type: `shared_worked_example`
- Status: `current`
- Issue tags: `final_-az`; `no_umlaut_trigger`; `shared_background_only`
- Recommended next use: `cite_if_final *-az behavior needs to be spelled out`
- Shared-with rows if relevant: `rows with stressed *ai plus final *-az where the question is regular monophthongization and tail loss rather than special repair`

This is a worked comparator rather than row-local evidence, but it is unusually close to the row's phonological shape. DEV_NOTES states for `*flaiskaz`: “**`*ai` monophthongizes to `ā` (no umlaut trigger from `*-az`) ... Final `*-az` lost**” [Germanic/docs/DEV_NOTES.md:6423-6428]. Row `2110` is not the same lexeme and should not inherit the comparator's entire morphological discussion, but the useful shared substance carries over directly: final `*-az` is not being treated here as an umlaut trigger that would dislodge the long-`ā` outcome, and regular end-of-word simplification then removes the tail. The live trace's `*láiθaz > *lāθaz > *lāθa > *lāþ` is exactly the short row-specific realization of that same background pattern [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2970-2983].

## Superseded or diagnostic material

- No superseded row-specific DEV_NOTES block was located for `2110 loath / lāþ`. The slice should say that plainly so later users do not infer a lost lexeme dossier from the mere existence of this replacement file.
- The DEV_NOTES table label `irrelevant` is diagnostic, not substantive. It only excludes row `2110` from the `*náblô`-type A-restoration bug family [Germanic/docs/DEV_NOTES.md:30599-30627].
- The published derivation trace is diagnostic implementation support rather than DEV_NOTES prose, but for this row it is highly informative because it shows that the live cascade already derives `lāþ` exactly from the live stored input without workaround or alternate `PROTOFORM` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2963-2983].
- `coverage_audit.md` and the absence of a `report_manifest.tsv` row are also diagnostic only. They describe current documentation infrastructure state (`none`, no manifest entry); they do not constitute philological argument in themselves [Germanic/docs/lexeme_reports/coverage_audit.md:298-298; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].

## Open questions for later work

- If row `2110` is ever promoted into indexed report infrastructure, decide whether shared stressed-`*ai > *ā` material plus the exact-match trace is enough, or whether the row should remain unindexed until genuinely lexeme-specific DEV_NOTES prose exists.
- If later literature pass work touches this lexeme family, add a compact dictionary/reference citation for OE `lāþ`/`lāð` specifically, so the TSV's current `ð→þ` allographic normalization note is backed by a local lexicographic citation rather than standing alone [Germanic/data/germanic-aligned-final.tsv:698-698].
- If future shared-note consolidation creates a reusable dossier for stressed `*ai` + final `*-az` reflexes in OE, row `2110` would be a straightforward attach point alongside comparator examples such as `*hailaz > hāl` [Germanic/docs/DEV_NOTES.md:13949-13953].

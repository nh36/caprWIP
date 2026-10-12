---
row_id: 2067
concept: heath
counterpart: hǣþ
proto: *xáiθiz
protoform: *xáiθiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: ""
linked_research_memo_file: ""
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_full_trace_report.txt
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2067 heath / hǣþ

## Current row state

- The live OE row reads `CONCEPT = heath`, `COUNTERPART = hǣþ`, `PROTO = *xáiθiz`, `PROTOFORM = *xáiθiz`, `DERIVATION_CLASS = regular`, with no row-local NOTE beyond duplicated Wiktionary inheritance sourcing [Germanic/data/germanic-aligned-final.tsv:532-532].
- For this row, **PROTO** and **PROTOFORM** are identical in the live TSV. The attested/target OE form is `hǣþ`. Older DEV_NOTES and older trace snapshots write the proto input without the acute as `*xaiθiz`; on present evidence that is only a house-notation difference, not a different stage-form or a different row policy [Germanic/data/germanic-aligned-final.tsv:532-532; Germanic/docs/DEV_NOTES.md:2608-2612; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:6493-6546].
- `oe_known_problems.tsv` has no surviving entry for row `2067`, for `heath`, for `hǣþ`, or for `*xáiθiz/*xaiθiz`, so the row is not currently being tracked as an unresolved OE exception, wontfix, or analogue-only case [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage/report infrastructure is still empty for this row. `coverage_audit.md` lists `2067 | heath | hǣþ | regular | no | - | - | - | none`, and `report_manifest.tsv` has no row-2067 manifest entry among its current pilot rows [Germanic/docs/lexeme_reports/coverage_audit.md:274-274; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The current published derivation trace is an exact match: `PROTO: *xáiθiz`, `EXPECTED: hǣþ`, `OUTPUTS: hǣþ`, with the compact stage chain `PWGmc Ai Monophthongization: *xāθiz`, `PGmc Final Z Deletion: *xāθi`, `OE I Umlaut: *xǣθi`, `OE High Vowel Apocope: *xǣθ`, `Old English Orthography: h*ǣþ`, `Outcome: hǣþ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2242-2262].
- The full trace gives the same derivation in rule-by-rule detail and shows that nothing exotic is being invoked for this row: the crucial live changes are `PWGmcAiMonophthongization`, `PGmcFinalZDeletion`, `OEIUmlaut`, `OEHighVowelApocope`, and the orthography/surface cleanup that converts starred `*hǣþ` to `hǣþ` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:14735-14849].
- Repo-local OE lexeme support agrees with the row target: `old_english_wiktionary.tsv` also has `heath    hǣþ` [Germanic/data/old_english_wiktionary.tsv:131-131].

## Development-note summary

No dedicated `heath / hǣþ` dossier survives in `DEV_NOTES.md`. That needs to be said plainly. The only securely attachable DEV_NOTES material naming this lexeme is a short 2026-01-01 implementation note: `Added {*ǣ} -> ǣ to OldEnglishRemoveStars so OE surface accepts long fronted a (e.g., *dailiz → dǣl, *xaiθiz → hǣþ)` [Germanic/docs/DEV_NOTES.md:2608-2612].

That surviving note is **row-specific but narrow**. It does not argue that `hǣþ` is exceptional, analogical, or philologically doubtful. It records a surface-layer repair: the grammar was already reaching starred OE `*ǣ`, but the output-cleanup layer needed to accept and print that vowel so rows like `*xaiθiz/*xáiθiz` could surface as `hǣþ` instead of stalling or printing a starred form [Germanic/docs/DEV_NOTES.md:2608-2612; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:14846-14849].

Everything else useful for this row is therefore either **shared-background-only** or **diagnostic**. Shared background: DEV_NOTES later re-checks that stressed `*ai` developments still work, but it does so with other control forms, not with `heath` itself [Germanic/docs/DEV_NOTES.md:14036-14043]. Diagnostic/current-state support: the live published trace and full trace both show that row 2067 is now a regular exact match with no special rescue mechanism [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2242-2262; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:14735-14849]. The conservative replacement note for this row should therefore preserve one explicit row-local DEV_NOTES sentence, then build outward from current trace state rather than pretending a richer heath-specific DEV_NOTES argument exists.

## Relevant DEV_NOTES fragments

### DEV_NOTES:no-row-local-dossier

- Source heading: no dedicated `heath / hǣþ` section survives
- Source line hint: direct attachable hits are limited to `2608-2612`; later shared stressed-`*ai` verification at `14036-14043`
- fragment type: `negative_result_with_thin_positive_support`
- status: `current`
- issue tags: `thin_support`; `no_row_local_dossier`; `shared_background_only`; `surface_fix_not_etymology`
- recommended next use: `state_conservatively_if_row_is_summarized_elsewhere`
- shared-with rows if relevant: `1986 deal / dǣl` for the same 2026-01-01 surface-fix note

Direct review of `DEV_NOTES.md` does **not** uncover a standalone `heath` block comparable to rows that preserve a mismatch narrative or a source-backed argument about rule ordering. The usable row-local evidence is confined to the short `ǣ`-surface implementation note, and the only later DEV_NOTES material that can be brought in at all is class-level stressed-`*ai` verification that names other lexemes, not this one [Germanic/docs/DEV_NOTES.md:2608-2612,14036-14043]. For later work that distinction matters: claims about `heath / hǣþ` itself should rest on the one explicit sentence plus the live traces, while broader claims about the robustness of the stressed-`*ai` pathway should be labelled shared-background-only rather than row-specific authority.

### DEV_NOTES:line-2608-2612

- Source heading: `OE ai cleanup + ǣ surface fix (2026-01-01)`
- Source line hint: `lines 2608-2612`
- fragment type: `lexeme_specific_but_narrow_implementation_fix`
- status: `current`
- issue tags: `oe_surface`; `remove_stars`; `long_fronted_a`; `explicit_row_example`; `proto_spelling_variant`
- recommended next use: `cite_when_explaining_how_starred_*ǣ_reaches_printed_hǣþ`
- shared-with rows if relevant: `1986 deal / dǣl`

This is the controlling surviving DEV_NOTES fragment for row 2067 because it names the lexeme directly. DEV_NOTES records two linked points: `Removed OldEnglishAiMonophthongization (never fires because WG monophthongization already rewrites *ai → *ā)` and `Added {*ǣ} -> ǣ to OldEnglishRemoveStars so OE surface accepts long fronted a (e.g., *dailiz → dǣl, *xaiθiz → hǣþ)` [Germanic/docs/DEV_NOTES.md:2608-2612]. The substantive preservation target is narrow but important. For this row, DEV_NOTES is not re-deriving `hǣþ` from a new protoform, not changing the derivation class, and not proposing an analogue-based workaround. It is saying that once the regular chain has produced starred OE `*xǣθ` / orthographic `*hǣþ`, the output-cleanup layer must know how to print `ǣ`.

The same fragment also constrains how to interpret the spelling difference between older DEV_NOTES `*xaiθiz` and the live TSV/trace `*xáiθiz`. The note's real chronological distinction is `*ai -> *ā -> *ǣ`, not accented versus unaccented `ai`; the acute in the live row is current project notation, while the January note still used the older plain-`ai` spelling [Germanic/docs/DEV_NOTES.md:2608-2612; Germanic/data/germanic-aligned-final.tsv:532-532; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2243-2262]. For this row, therefore, the fragment is **row-specific** for the surface bottleneck, but only that.

### DEV_NOTES:line-14036-14043

- Source heading: `Test results` within the 2026-04-06 implementation note
- Source line hint: `lines 14036-14043`
- fragment type: `shared_background_only_verification`
- status: `current`
- issue tags: `stressed_ai`; `regression_check`; `shared_background_only`; `not_row_specific`
- recommended next use: `use_only_as_class_level_support`
- shared-with rows if relevant: `1986 deal / dǣl`; stressed-`*ai` control rows generally

This fragment does not mention `heath`, so it should not be inflated into row-local authority. Its value is narrower: DEV_NOTES later records `Stressed *ai forms still work: *bainą → bān, *dailiz → dǣl` after an unrelated change set [Germanic/docs/DEV_NOTES.md:14036-14043]. For row 2067, that is **shared-background-only** evidence that the same general `*ai` machinery remained stable later in the project. It helps explain why the live trace for `*xáiθiz` can be read with confidence as part of a still-working regular pathway, but because `hǣþ` is not one of the named probes here, the fragment should be cited only as class-level corroboration, never as a surviving heath-specific DEV_NOTES argument [Germanic/docs/DEV_NOTES.md:14036-14043; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2242-2262].

## Superseded or diagnostic material

- Older full-trace snapshots from 2026-02-07 and 2026-03-11 already produced `OUTPUTS: hǣþ` from unaccented `PROTO: *xaiθiz`, with the same essential regular path `*xaiθiz > *xāθi > *xǣθi > *xǣθ > hǣþ` [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-02-07_post_root_noun_fix.txt:2307-2352; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:6493-6546]. This is useful **diagnostic** history showing outcome stability across grammar revisions, but it is superseded as a statement of current notation and current rule inventory; the live row now stores accented `*xáiθiz`, and the modern full trace has more granular rule naming [Germanic/data/germanic-aligned-final.tsv:532-532; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:14735-14849].
- The absence of row 2067 from `oe_known_problems.tsv`, from current mismatch reports, and from the manifest is likewise **diagnostic**, not argumentative. It shows that the row is not a live trouble case and not yet part of the pilot report infrastructure, but it does not add independent philological substance beyond current-success status [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:274-274; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The live derivation traces themselves are **diagnostic/current-state support**, not DEV_NOTES fragments. They should be used to document what the grammar now does — especially the regular sequence `PWGmcAiMonophthongization > PGmcFinalZDeletion > OEIUmlaut > OEHighVowelApocope > surface hǣþ` — but not mistaken for evidence that a longer row-specific DEV_NOTES memo once existed [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2242-2262; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:14749-14849].

## Open questions for later work

- If `dev_notes_slices/index.tsv` is revisited later, decide whether row 2067 should remain a no-index slice unless more than a narrow surface-fix mention survives. On present evidence the documentation is real but thin.
- If a later packet or memo is created, keep three layers explicit near the top: live TSV `PROTO = PROTOFORM = *xáiθiz`; older DEV_NOTES/older-trace spelling `*xaiθiz` as a notation variant; and attested OE target `hǣþ` [Germanic/data/germanic-aligned-final.tsv:532-532; Germanic/docs/DEV_NOTES.md:2608-2612; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:6493-6546].
- If later reporting wants to generalize beyond the single 2026-01-01 note, attach row 2067 to a shared stressed-`*ai` / OE-`ǣ` background discussion rather than inventing a heath-specific controversy that the surviving record does not support [Germanic/docs/DEV_NOTES.md:2608-2612,14036-14043].

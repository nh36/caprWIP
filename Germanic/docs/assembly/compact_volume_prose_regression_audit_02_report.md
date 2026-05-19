# Compact volume prose-regression audit 02 report

## Summary

- generated broad citations remain at zero: **yes**
- citations restored in this pass: **0**
- structural/style issues found: **12**
- structural/style issues fixed: **10**
- issues left for human review: **2**
- outputs regenerated: **yes**

This pass stayed out of ordinary locator work. It focused on the generated
reader-facing volume, removed the remaining structural/project-facing wording
from generated summaries and tables, cleared the last generated `->` rows, and
left the still-dormant upstream-only source vocabulary for a later hygiene
pass.

## Citation and scan taxonomy checkpoint

| Bucket | Broad citations |
| --- | ---: |
| generated compact Markdown | 0 |
| regular book prose | 0 |
| non-regular model entries | 0 |
| regular model-entry-only sources | 315 |
| upstream-only total | 315 |

- `citation_locator_remaining_master.tsv`: **header only**
- manifest state: **synchronized with the regenerated compact Markdown**

The key taxonomy point is that the compact regular volume is currently built
from `book_prose/regular_all_01/*.book.md`, not from the regular
`*.model.md` body prose. In `build_full_lexical_volume.py`, regular entries are
rewritten from `.book.md` whenever `LEXICAL_REGULAR_BOOK_PROSE_DIR` is set,
while non-regular entries still read from `.model.md`. That is why the current
generated compact volume can have **0** generated broad citations even though
the regular-model-only source layer still has **315** broad citations.

The audit-10 figure of **314 upstream-only broad citations** was a different
queue: it referred to the then-active upstream non-regular/model-entry cleanup
state. Audit 02 splits the scan by source bucket and shows that the non-regular
queue is now **0**, while the remaining **315** belong to regular `.model.md`
files that sit behind the compact regular book-prose overlay. Those citations
do not affect the current generated compact regular volume unless the assembly
path changes back to regular model-entry prose.

## Structural vocabulary search

The search covered generated compact Markdown and TeX first, then upstream
regular book prose and model-entry sources. In the generated compact Markdown,
all targeted structural/project-facing phrases reached zero after the rebuild.

| Phrase | Before | After |
| --- | ---: | ---: |
| `selected input` | 182 | 0 |
| `selected target` | 51 | 0 |
| `selected form` | 19 | 0 |
| `selected cell` | 11 | 0 |
| `comparison cell` | 2 | 0 |
| `documented trace` | 8 | 0 |
| `trace output` | 67 | 0 |
| `compact-trace output` | 46 | 0 |
| `manual comparison` | 3 | 0 |
| `current cascade` | 2 | 0 |

Remaining upstream-only source hits were deliberately left untouched when they
did not feed the current generated compact volume:

| Source layer | Remaining notable hits |
| --- | --- |
| regular `.book.md` | `selected input` 33; `selected target` 5; `selected form` 9 |
| `.model.md` source corpus | `selected input` 257; `selected target` 41; `selected form` 12; `documented output` 143; `trace output` 64; `compact-trace output` 41; `->` 145 |

Those remaining hits are now an upstream source-hygiene problem rather than a
generated compact-volume problem.

## Table and summary language

Systematic generated labels were changed in the assembly path:

1. derivation summaries now say `form followed here` / `Old English form here`
   instead of `selected input` / `selected target`;
2. trace labels now use `Regular outcome:` and `Old English form:` rather than
   `Transducer outcome:` and `Selected target:`;
3. generated comparison tables now use `regular output` and `paradigm
   comparison` instead of `compact-trace output` and `manual comparison`.

Targeted source tables were also cleaned in the sampled non-regular entries
`needle / nǣdl`, `span / spanne`, `loam / lām`, `find / fundene`, `rust / rust`,
`wolf / wulf`, `wool / wull`, and `knob / cnobba`.

Labels deliberately left unchanged:

- `Proto input` remains useful as a direct description of the trace table;
- `Derivation trace` remains acceptable as reader-facing technical prose;
- upstream-only source metadata tables were not bulk-rewritten in this pass.

## Arrow and formatting cleanup

- generated Markdown `->` occurrences found before cleanup: **7**
- generated Markdown `->` occurrences after cleanup: **0**
- generated Markdown `→` occurrences after cleanup: **0**
- generated TeX `->` occurrences after cleanup: **0**
- generated TeX `ḯ` occurrences after cleanup: **0**
- bad `*x~*y` spacing after cleanup: **0**
- raw Markdown bold `**` in generated TeX: **0**

All seven generated `->` strings were in negative-control or unexplained rows
for `rust / rust`, `wolf / wulf`, `wool / wull`, and `knob / cnobba`. They were
all converted to reader-facing `>` notation or recast as regular-output labels.
Regular sound-change / derivational notation now uses `>`, not `->` or `→`.

Two raw underscores remain in generated TeX, but both are harmless:

1. `known_unmodelled` appears as an escaped derivation-class label, not leaked
   raw Markdown;
2. one underscore occurs inside a bibliography URL.

## High-risk entry review

| Entry | Finding |
| --- | --- |
| `ban / bannes` | Audit-10 removal remains safe; the conservative genitive vs nominative background still reads naturally and stays adequately cited. |
| `shove / sċēaf` | Audit-10 removal remains safe; the singular preterite comparator is clear and no source-backed class-history citation had to be restored. |
| `birth / byrd` | Regular book prose now reads naturally in generated form; no project/internal wording remains in the generated entry. |
| `needle / nǣdl` | The alternant comparison now reads as book prose rather than selection metadata; support remains adequate. |
| `fright / fyrhte` | The late-analogy preterite comparison still reads naturally and remains adequately supported after audit-01 cleanup. |
| `span / spanne` | The conservative dative-singular comparison is preserved, but the table and prose now avoid “selected ... cell” wording. |
| `warp / weorpan` | The regular entry remains clean and reader-facing; no structural/project vocabulary appears in the generated prose. |
| `fast / festan` | The early-analogy summary is now concise and book-facing; no generated metadata wording remains. |
| `find / fundene` | The oblique participle remains the controlling comparator, but “comparison cell” phrasing has been removed. |
| `meed / meorde` | The oblique comparison remains clear and adequately cited; the generated wording no longer reads like internal selection logic. |
| `have / hæfeþ` | The late-analogy 3sg comparison remains clear in generated form and does not show project/internal vocabulary. |
| `rust / rust` | The exception note now uses `>` and reader-facing regular-output language; the unresolved analysis is unchanged. |
| `still / stillan` | The generated entry no longer says “selected target”; the verb/adjective distinction still reads naturally. |
| `loam / lām` | The class-comparison prose is clearer and less database-like while preserving the early class-shift analysis. |
| `think / þenċan` | The regular entry continues to read naturally and remains adequately supported. |
| `wolf / wulf` | The negative-control discussion now reads as philological prose rather than project explanation; the unresolved exception is unchanged. |
| `wool / wull` | The lexical-exception table is cleaner and uses reader-facing `>` notation. |
| `knob / cnobba` | The prose is cleaner and clearer about the reconstructed comparator, but the comparator-policy choice remains review-sensitive. |

## Files changed

| File(s) | Why |
| --- | --- |
| `Germanic/docs/assembly/build_full_lexical_volume.py` | systematic cleanup of generated derivation summaries, outcome labels, and repeated table wording |
| `Germanic/docs/assembly/section_introductions_draft.md` | removed the last `current cascade` front-matter phrasing |
| `Germanic/docs/lexeme_reports/model_entries/2011-find-fundene.model.md` and paired `.source_ledger.md`, `.reviewer_checklist.md`, `.model_implementation_report.md` | removed remaining comparison-cell wording and recorded the audit-02 note |
| `Germanic/docs/lexeme_reports/model_entries/2087-knob-cnobba.model.md` and paired sidecars | softened reconstructed-comparator wording, cleaned table language, and recorded the audit-02 note |
| `Germanic/docs/lexeme_reports/model_entries/2109-loam-lām.model.md` and paired sidecars | softened class-comparison wording and recorded the audit-02 note |
| `Germanic/docs/lexeme_reports/model_entries/2136-needle-nǣdl.model.md` and paired sidecars | softened alternant/table wording and recorded the audit-02 note |
| `Germanic/docs/lexeme_reports/model_entries/2162-rust-rust.model.md` and paired sidecars | replaced reader-facing `->` rows with `>` and cleaned exception-table wording |
| `Germanic/docs/lexeme_reports/model_entries/2203-span-spanne.model.md` and paired sidecars | softened dative-singular comparison wording and recorded the audit-02 note |
| `Germanic/docs/lexeme_reports/model_entries/2298-wolf-wulf.model.md` and paired sidecars | removed the last explicit project phrasing, replaced reader-facing `->`, and recorded the audit-02 note |
| `Germanic/docs/lexeme_reports/model_entries/2300-wool-wull.model.md` and paired sidecars | replaced row labels / `->` notation and recorded the audit-02 note |
| `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.md` | regenerated compact Markdown after source/build cleanup |
| `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.tex` | regenerated TeX from the rebuilt compact Markdown |
| `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.pdf` | regenerated PDF from the rebuilt compact Markdown |
| `Germanic/docs/assembly/compact_volume_prose_regression_audit_02_inventory.tsv` | recorded issue inventory for this pass |
| `Germanic/docs/assembly/compact_volume_prose_regression_audit_02_report.md` | recorded findings, counts, and recommendation for this pass |

## Remaining issues

1. Upstream source layers still contain structural vocabulary (`selected input`,
   `selected target`, `documented output`, source-level `->`) in regular
   `.book.md` prose and `.model.md` metadata tables that no longer feed the
   current generated compact volume directly.
2. `knob / cnobba` remains review-sensitive for comparator policy even after the
   prose cleanup; the open question is editorial/analytical, not stylistic.

## Recommendation

**D. Move to rendered PDF/layout review.**

The generated compact volume is now clean on the structural-vocabulary target:
generated broad citations remain at zero, the generated Markdown no longer
carries the targeted project/internal phrases, and the last generated `->` rows
are gone. The next highest-value pass is therefore a rendered PDF/layout review
rather than another generated-prose cleanup pass.

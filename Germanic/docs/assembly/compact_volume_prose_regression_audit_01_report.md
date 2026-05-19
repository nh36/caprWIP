# Compact volume prose-regression audit 01 report

## Summary

- generated broad citations remain at zero: **yes**
- citations restored in this pass: **0**
- prose/style issues found: **9**
- prose/style issues fixed: **7**
- issues left for human review: **2**
- outputs regenerated: **yes**

This pass stayed out of ordinary locator work. The only citation-facing change
was a syntax normalization in `span / spannan` that kept existing locators
attached to the correct source item; no locator was invented and no removed
citation had to be restored.

## Citation checkpoint

- generated compact Markdown broad citation count: **0**
- regular book-prose broad citation count: **0**
- non-regular model-entry broad citation count: **0**
- upstream-only broad citation count: **0**
- `citation_locator_remaining_master.tsv`: **header only**
- manifest state: **synchronized with generated Markdown**

The robust Pandoc-based re-scan did **not** reproduce the audit-10 snapshot of
`314` non-regular / upstream-only broad citations. Instead, the current scan
found those queues at **0** and found **315** broad citations in regular
`.model.md` source files that sit behind the compact regular book-prose layer.
Those regular model-entry broad citations were not reopened in this pass.

## Audit-10 removal review

### ban / bannes

- citation removal was safe: **yes**
- prose remained adequately cited: **yes**
- citation restoration needed: **no**
- style outcome: **improved in this pass**

The Campbell removal in audit 10 did not strip out a necessary source-backed
rule claim. The entry still rests on localized noun evidence from
`BosworthToller1898, 303`, while the nominative/genitive contrast is now stated
in more natural prose without phrases such as “reviewed material” or
“citation-form comparison cell.”

### shove / sċēaf

- citation removal was safe: **yes**
- prose remained adequately cited: **yes**
- citation restoration needed: **no**
- style outcome: **improved in this pass**

The removed `RingeTaylor2014` citation did not need to come back once the entry
stopped making a source-backed class-history claim. Localized support from
`Kroonen2013, 444`, `BrightCassidyRingler1971, 347`, and `Sweet1953, 29`
remains sufficient, and the singular-preterite comparison now reads as lexical
prose rather than as an internal note about the “selected input.”

## Style-regression search

The phrase scan over the rebuilt compact Markdown, regular book prose, and
model-entry prose found the sharpest reader-facing regressions in:

1. compact front matter that still spoke about broad citations, audit state, and
   technical integration;
2. `ban / bannes`, `shove / sċēaf`, `fright / fyrhte`, `find / fundene`, and
   `meed / meorde`;
3. one regular book-prose citation span whose section-locator syntax was being
   split by Pandoc.

Fixed in this pass:

- front-matter audit/process language removed upstream;
- `ban / bannes` and `shove / sċēaf` recast into more natural body prose;
- `fright / fyrhte`, `find / fundene`, and `meed / meorde` stripped of explicit
  project-facing phrasing;
- `span / spannan` locator syntax normalized so the generated broad count stayed
  at zero.

Still widespread after the targeted fixes:

| Phrase | Remaining count |
| --- | ---: |
| `selected input` | 480 |
| `selected target` | 103 |
| `selected form` | 40 |
| `selected cell` | 22 |
| `documented output` | 144 |
| `trace output` | 138 |
| `documented trace` | 16 |
| `manual comparison` | 6 |

These remaining hits are concentrated in generated derivation summaries,
metadata tables, and comparison tables rather than in the narrowed set of body
paragraphs fixed here.

## Formatting-regression search

- `ḯ` in rebuilt Markdown/TeX: **0**
- raw Unicode arrows `→`: **0**
- bad `*x~*y` tilde spacing: **0**
- raw Markdown bold `**` in rebuilt TeX: **0**
- code-font leakage in sampled prose: **not reproduced**; sampled forms render
  as italics in TeX

Notes:

1. The raw backticks counted in rebuilt TeX are typographic quotation marks from
   prose and bibliography output, not leaked Markdown code spans.
2. Seven `->` strings remain in generated Markdown comparison tables for
   unexplained/unmodelled negative-control rows. They were recorded for follow-up
   rather than widened into a second formatting edit wave during this pass.

## Sampled-entry review

| Entry | Finding |
| --- | --- |
| `ban / bannes` | Reads more naturally after the edit; Bosworth-Toller still supports the noun claim; no citation restoration needed. |
| `shove / sċēaf` | Reads more naturally after the edit; the singular preterite remains adequately supported; no internal “chosen here” wording remains in body prose. |
| `birth / byrd` | Natural regular-book prose; support still adequate; no project/internal terminology noted in body prose. |
| `needle / nǣdl` | Body prose reads naturally; support remains adequate; metadata still carries structural “selected input” language. |
| `fright / fyrhte` | Body prose improved; citations remain adequate; earlier project-facing wording removed. |
| `span / spanne` | Reads acceptably; support remains adequate; some table phrasing is still formulaic but not severe enough for this pass. |
| `warp / weorpan` | Natural concise prose; support remains adequate; no notable internal terminology in the body paragraph reviewed. |
| `fast / festan` | Reads naturally; class split and citation support remain clear; no immediate prose change needed. |
| `find / fundene` | Improved by removing project-facing wording; attested `fundene` remains clearly supported. |
| `meed / meorde` | Improved by recasting the project/source-backed transition; citations remain adequate while the broader `mēd` debate stays open. |
| `have / hæfeþ` | Reads naturally; paradigm-cell distinction and support remain clear. |
| `rust / rust` | Prose remains readable and adequately supported; comparison table still uses `->` in negative-control rows. |
| `still / stillan` | Natural body prose in the sampled generated paragraph; support remains adequate. |
| `loam / lām` | Natural body prose; support remains adequate; no project/internal wording noted. |

## Files changed

- `Germanic/docs/assembly/section_introductions_draft.md` — removed
  placeholder “selected input/target” framing from the section introductions.
- `Germanic/docs/assembly/build_full_lexical_volume.py` — rewrote compact
  front-matter prose to remove citation-audit/process language and broadened the
  breeches build assertion so the regular book-prose build passes.
- `Germanic/docs/assembly/book_prose/regular_all_01/2202-span-spannan.book.md`
  — normalized the Brunner multi-section locator syntax so Pandoc no longer
  splits it into generated broad citations.
- `Germanic/docs/lexeme_reports/model_entries/1936-ban-bannes.model.md` —
  softened post-citation meta phrasing while preserving the nominative/genitive
  analysis.
- `Germanic/docs/lexeme_reports/model_entries/1936-ban-bannes.source_ledger.md`,
  `Germanic/docs/lexeme_reports/model_entries/1936-ban-bannes.reviewer_checklist.md`,
  `Germanic/docs/lexeme_reports/model_entries/1936-ban-bannes.model_implementation_report.md`
  — added the required prose-regression audit note.
- `Germanic/docs/lexeme_reports/model_entries/2184-shove-sċēaf.model.md` —
  recast the present-system vs singular-preterite distinction into more natural
  prose.
- `Germanic/docs/lexeme_reports/model_entries/2184-shove-sċēaf.source_ledger.md`,
  `Germanic/docs/lexeme_reports/model_entries/2184-shove-sċēaf.reviewer_checklist.md`,
  `Germanic/docs/lexeme_reports/model_entries/2184-shove-sċēaf.model_implementation_report.md`
  — added the required prose-regression audit note.
- `Germanic/docs/lexeme_reports/model_entries/2034-fright-fyrhte.model.md` —
  removed explicit project-facing phrasing from the body prose.
- `Germanic/docs/lexeme_reports/model_entries/2034-fright-fyrhte.source_ledger.md`,
  `Germanic/docs/lexeme_reports/model_entries/2034-fright-fyrhte.reviewer_checklist.md`,
  `Germanic/docs/lexeme_reports/model_entries/2034-fright-fyrhte.model_implementation_report.md`
  — added the required prose-regression audit note.
- `Germanic/docs/lexeme_reports/model_entries/2011-find-fundene.model.md` —
  recast the comparison paragraph into reader-facing prose.
- `Germanic/docs/lexeme_reports/model_entries/2011-find-fundene.source_ledger.md`,
  `Germanic/docs/lexeme_reports/model_entries/2011-find-fundene.reviewer_checklist.md`,
  `Germanic/docs/lexeme_reports/model_entries/2011-find-fundene.model_implementation_report.md`
  — added the required prose-regression audit note.
- `Germanic/docs/lexeme_reports/model_entries/2124-meed-meorde.model.md` —
  removed explicit project/source-backed phrasing from the transition into the
  broader `mēd` problem.
- `Germanic/docs/lexeme_reports/model_entries/2124-meed-meorde.source_ledger.md`,
  `Germanic/docs/lexeme_reports/model_entries/2124-meed-meorde.reviewer_checklist.md`,
  `Germanic/docs/lexeme_reports/model_entries/2124-meed-meorde.model_implementation_report.md`
  — added the required prose-regression audit note.

Regenerated outputs:

- `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.md`
- `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.tex`
- `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.pdf`

## Remaining issues

1. Structural metadata and table vocabulary (`selected input`, `documented
   output`, `trace output`, and related phrasing) remains widespread across the
   compact corpus and now looks like the main blocker to fully monograph-style
   prose.
2. Seven `->` strings remain in generated Markdown comparison tables for
   unexplained/unmodelled rows.
3. The robust scan now places the remaining broad-citation source queue in
   regular `.model.md` files (315 items), not in generated output or non-regular
   model entries. That queue was not reopened here.

## Recommendation

**B. Do a second prose-regression pass.**

Generated broad citations are back to zero and the audit-10 removals are now
explicitly reviewed, but the remaining structural metadata/table vocabulary is
still too visible for a finished monograph voice.

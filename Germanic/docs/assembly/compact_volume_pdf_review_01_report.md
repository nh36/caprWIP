# Compact volume PDF review 01 report

## Summary

- **PDF inspected:** yes
- **Issues found:** 4
- **Issues fixed:** 2
- **Issues left for later review:** 2
- **Markdown/TeX/PDF regenerated:** yes

This pass treated the compact lexical volume as a rendered book rather than as a locator queue. The main fixes were presentation-facing: the front matter now reads less like an internal assembly scaffold, and `knob / cnobba` no longer carries stray bold or project-facing wording in the running prose.

## Rendered-output checks

The rendered PDF was sampled across the front matter and the major entry classes:

- front matter: page 1
- regular outcomes: pages 2 and 5
- attested variants: page 27
- early analogy: pages 31-32
- late analogy: pages 67-68 and 79
- reconstructed Old English: pages 97-98
- known unmodelled: page 100
- unexplained unmodelled: page 106
- references: pages 109-110

Checks completed:

- No raw Markdown leakage was found in the regenerated output.
- No `ḯ`, `PNWGmce`, raw `--type`, unspaced `~`, `→`, `p.`/`pp.` citation locators, malformed citation spans, or empty citation brackets were found in the regenerated Markdown/TeX sweep.
- The regenerated PDF still carries live link annotations (`970` total: `965` internal GoTo links and `5` URI links).
- The bibliography is present, readable, and starts cleanly on page 109.
- The references header and first bibliography page break are clean.

One non-fatal render-log artifact remains: the Docker-backed Pandoc run still emits the already-familiar `pandoc: Ticker: poll failed` noise, but this pass did not surface any corresponding PDF defect.

## Trace-table review

Representative trace tables were inspected in the rendered PDF on pages 27, 31-32, 67-68, 79, 98, 100, and 106.

Results:

- column headings remain correct and non-redundant
- `Earlier Germanic changes` / `Old English changes` remain visually clear
- stage subheaders such as `West Germanic` and `Northwest Germanic` are legible
- no sampled table spilled outside its border
- no sampled form/output alignment problem required a layout change
- the previously addressed dense-label spacing issues remain under control

No systematic table-layout fix was needed in this pass.

## Entry-prose review

Entry-opening prose was reviewed in a structured sample extracted from the regenerated volume:

- `20` regular entries
- `10` early analogy entries
- `10` late analogy entries
- `10` entries combined from reconstructed Old English, known unmodelled, and unexplained unmodelled sections

Findings:

- the regular and analogy samples now read consistently as lexical prose rather than as row dumps
- no broad pattern of citation-splitting damage or atomized prose was found in the sampled openings
- the clearest remaining project-facing wording was isolated to `knob / cnobba`, and was fixed in this pass
- the front matter still openly labels the volume as `Alpha 01`, but its wording is now substantially more reader-facing than before

## Human-review subset

### meed / meorde

The page reads clearly enough as prose, and the forms are presented cleanly in print. The unresolved problem is analytical, not typographic: a later human-review pass still needs to decide how the entry should balance the attested oblique target `meorde` against the broader competing `mēd` tradition.

### knob / cnobba

The rendered entry is now cleaner after the prose cleanup. It still needs a human decision, however, on whether the reconstructed comparator `cnobba` should remain the chosen OE-stage target or whether attested `cnoppa` should replace it as the preferred comparator.

## Remaining broad-citation check

Locator work was not reopened in this pass.

The regenerated Markdown was rechecked against `citation_locator_remaining_master.tsv`, and the broad-citation manifest still matches the assembled Markdown exactly:

- manifest rows: `161`
- broad citation occurrences in generated Markdown: `161`
- pairwise manifest/Markdown match: `true`

The remaining broad citations looked reasonable in the sampled rendered prose. No new unsupported or obviously missing broad citations were introduced by this PDF-review pass.

## Files changed

- `Germanic/docs/assembly/build_full_lexical_volume.py` — front-matter wording and derivation-class list made more reader-facing
- `Germanic/docs/lexeme_reports/model_entries/2087-knob-cnobba.model.md` — removed stray bold on ordinary prose and replaced project-facing wording
- `Germanic/docs/lexeme_reports/model_entries/2087-knob-cnobba.source_ledger.md` — added required PDF review 01 note
- `Germanic/docs/lexeme_reports/model_entries/2087-knob-cnobba.reviewer_checklist.md` — added required PDF review 01 note
- `Germanic/docs/lexeme_reports/model_entries/2087-knob-cnobba.model_implementation_report.md` — added required PDF review 01 note
- `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.md` — regenerated
- `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.tex` — regenerated
- `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.pdf` — regenerated
- `Germanic/docs/assembly/compact_volume_pdf_review_01_inventory.tsv` — new issue inventory
- `Germanic/docs/assembly/compact_volume_pdf_review_01_report.md` — this report

## Remaining issues

- `meed / meorde` — **human review**: decide whether the current oblique-cell framing should remain the reader-facing comparator, or whether the entry should be reframed around the wider `mēd` problem.
- `knob / cnobba` — **human review**: decide whether reconstructed `cnobba` or attested `cnoppa` is the right comparator policy for the entry.
- Docker render log noise — **no action for now**: the current `pandoc: Ticker: poll failed` output did not correspond to a visible render defect in this pass.

No remaining issue from this pass appears to require source preparation, locator work, or table-layout work.

## Recommendation

**C. Do a human-review pass on meed / knob.**

The PDF now reads cleanly enough for ordinary human reading, and the remaining problems surfaced in this pass are narrowly concentrated in the two already-flagged human-review entries rather than in the rendering or book layout.

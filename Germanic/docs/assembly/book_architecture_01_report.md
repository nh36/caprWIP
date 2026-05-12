# Book architecture 01 report

## Summary

- Book architecture drafted: **yes**
- Class-based manifests created: **yes**
- Total model entries found: **147**
- Counts by canonical class:
  - `regular`: **70**
  - `early_analogy`: **35**
  - `late_analogy`: **28**
  - `unexplained_unmodelled`: **5**
- Entries with non-canonical derivation classes: **9**
- Incomplete metadata problems found: **0**
- Filename row-ID parse problems found: **0**
- Full assembly attempted: **no**

All 147 current `.model.md` entries were scanned through the manifest builder,
and all 147 achieved a confident compact-trace match under the current assembly
matching logic.

## Architecture

The proposed lexical volume structure is:

1. front matter / introduction
2. data and sources
3. transducer and derivation method
4. derivation classes
5. four main catalogue parts:
   - Regular derivations
   - Early analogy and pre-Old-English input selection
   - Late analogy and paradigm-cell selection
   - Unexplained or deliberately unmodelled exceptions
6. appendices for citation caveats, machine-readable manifest notes, known
   exceptions, and the later sound-change volume/report boundary

The design keeps the lexical volume word-centered while explicitly reserving the
later sound-change volume or report for rule chronology and system-level
discussion.

## Manifest generation

Model entries were discovered by scanning:

- `Germanic/docs/lexeme_reports/model_entries/*.model.md`

The helper script:

- `Germanic/docs/assembly/build_class_manifests.py`

parses the top metadata fields:

- `PROTO`
- `PROTOFORM`
- `COUNTERPART`
- `DERIVATION_CLASS`

It then:

1. extracts row IDs from filenames
2. assigns entries to class buckets
3. orders entries by class and then numeric row ID
4. checks for missing metadata and filename-parse issues
5. checks trace-match confidence against the compact derivation-trace report

Created files:

- `manifest_regular.tsv`
- `manifest_early_analogy.tsv`
- `manifest_late_analogy.tsv`
- `manifest_unexplained.tsv`
- `manifest_all_by_class.tsv`
- `manifest_summary.md`

The live scan found no incomplete metadata, no filename row-ID parse defects,
and no non-confident trace matches.

## Section-introduction scaffolding

Created:

- `section_introductions_draft.md`

This file contains concise, intentionally mechanical placeholder prose for:

- the catalogue as a whole
- regular derivations
- early analogy
- late analogy
- unexplained exceptions
- the later sound-change volume/report boundary

It is **scaffolding**, not final prose. The intended use is to supply stable
section openings in the first full lexical assembly alpha, then revise those
paragraphs later without touching the per-entry assembly logic.

## Full assembly design

Created:

- `full_assembly_design.md`

This note specifies the future full-assembly workflow:

- use class manifests as ordered inputs
- keep the class order fixed
- place entries under part headings rather than directly under the document
  title
- preserve the generated derivation summary and boxed derivation trace
- use `docs/refs.bib`, `--citeproc`, and `link-citations: true`
- preserve the Docker-backed PDF route
- include section-introduction scaffolding
- exclude support-package files from the assembled body
- keep the later sound-change volume or report separate

No full 147-entry Markdown, TeX, or PDF assembly was run in this pass.

## Problems or review points

The main review issue is the presence of **9 entries with non-canonical
derivation-class labels**:

- `attested_variant`: rows `1983`, `2242`, `2254`, `2273`
- `known_unmodelled`: rows `2013`, `2240`
- `reconstructed_oe`: rows `2087`, `2151`, `2227`

These should not be silently discarded. For the first full lexical assembly
alpha they should either be mapped explicitly into one of the four main parts or
held out in an editorial review bucket.

Additional review points:

- `1959 bottom / botm` remains the reviewed-but-unchanged separator case from
  assembly pilot 08.
- No new separator, citation, or trace-layout regressions were introduced in
  this design pass.
- Because all 147 current model entries have confident trace matches, trace
  matching does not currently block full assembly.

## Recommendation

**Decision: A. Architecture and manifests are ready; proceed to full lexical assembly alpha by class.**

The one caveat is explicit rather than blocking: the nine entries with
non-canonical class labels should be kept visible as a review bucket instead of
being silently forced into the four-part architecture.

## Scope confirmation

- No original model-entry prose was edited.
- No TSV source data, FST files, `report_manifest.tsv`, compact trace files,
  packets, dev-note slices, research memos, bibliography files,
  OCR/reference files, or citation-locator reports were edited.
- Changes were limited to new assembly-side design/manifests files, the assembly
  README, and the helper script used to generate the class manifests.
- No full-corpus PDF was generated.

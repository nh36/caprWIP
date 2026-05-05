# Research memo — 2284 whale / hwæl

## Starting point

- ID: 2284
- CONCEPT: whale
- COUNTERPART: hwæl
- PROTO: *wálaz
- PROTOFORM: *xwálaz
- DERIVATION_CLASS: early_analogy
- NOTE: Kroonen *hwalaz with initial *hw-; OE hwæl.

The live row already separates a cognate-set headword (`PROTO = *wálaz`) from the actual OE modelling input (`PROTOFORM = *xwálaz`). The memo question is not whether the current cascade reaches `hwæl`—it does—but whether the row note and the evidential framing accurately explain why the project uses `*xwálaz` and what that choice means relative to comparative sources.

## Packet evidence assessment

**Authoritative/current:**
- The live TSV row is current and shows the key project distinction: `PROTO = *wálaz`, `PROTOFORM = *xwálaz`, `COUNTERPART = hwæl`, `DERIVATION_CLASS = early_analogy`.
- The packet’s compact derivation trace is current for the project input form: `*xwálaz -> hwæl` in the present FST.
- `analysis/arestoration_r_l_research.md` is current and genuinely useful here: it treats `hwæl` as a closed monosyllable with `æ`, and it separately cites plural `hwalas` as the contrasting open-syllable form.
- `coverage_audit.md` is current workflow evidence that this row requires a lexeme report and has no pilot/full report yet.

**Useful background:**
- `old_english_wiktionary.tsv` is a light confirmation that the repo treats `hwæl` as the ordinary OE headword.
- The packet’s row-history note (`*walăz -> *xwalăz`) is useful chronology for the project fix, though not lexical authority by itself.

**Stale or superseded:**
- The pre-fix backup row with `PROTOFORM = *walăz` and no explanatory note is important project history, but not the current lexical analysis.
- Debug-snapshot occurrences of `# whale / PROTO: *xwálaz / OUTPUTS: hwæl` are current implementation checks, not independent philological authority.

**Irrelevant or misleading:**
- The packet note is misleading as written: the repo’s Kroonen OCR file gives `*hwali-`, not `*hwalaz`; the a-stem form `*xwalaz` is instead supported in-repo by Orel. So the packet is right that the row needs initial `hw-/xw-`, but wrong to attribute that exact form to Kroonen.
- The packet’s “possibly stale” line from the a-restoration analysis is diagnostic for rule coverage, not an argument about etymological stem class on its own.

## Additional repo research

Beyond the packet, I checked:
- `Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06` for the earlier project state (`*walăz`, no note, no `early_analogy` label).
- `Germanic/data/old_english_wiktionary.tsv` for the repo’s lexical headword support.
- `Germanic/data/oe_known_problems.tsv`, which has no entry for this lexeme.
- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md`, which cites Ringe & Taylor on `hwalas` as an exclusion from second fronting.
- `Germanic/docs/lexeme_reports/coverage_audit.md` and the debug snapshots, which confirm report scope but no existing manual report.
- `Germanic/tools/oe_paradigm_probe.py`, which has no built-in probe spec for whale / `hwæl`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`, `orel_handbook_germanic_etymology.vision.txt`, `clark_hall_concise_anglo_saxon_dictionary.vision.txt`, `bosworth_toller_anglo_saxon_dictionary.vision.txt`, and `bright_anglo_saxon_reader.txt` for the comparative etymology and OE lexical/paradigmatic evidence.

I found no dedicated dossier, no DEV_NOTES discussion for this row, and no pilot report already written for this lexeme.

## Reconstruction and early-stage forms

This row needs the full three-way distinction kept explicit:

1. **Cognate-set proto / aligned headword:** `*wálaz` in TSV `PROTO`. This is the project’s cross-row cognate-set label, not the strongest lexeme-specific authority for OE by itself.
2. **Project input form for OE derivation:** `*xwálaz` in TSV `PROTOFORM`. This is the form the FST actually consumes to derive `hwæl`.
3. **OE target form represented by the row:** attested citation-form `hwæl`.

The comparative sources in the repo are not uniform. Orel explicitly gives `*xwalaz` (with some mixed `*xwaliz` evidence), while Kroonen’s OCR entry is `*hwali-`, not `*hwalaz`. That means the current note collapses two different issues: inherited initial `hw-/xw-` and stem-class choice. The live `PROTOFORM = *xwálaz` is still defensible as the project’s OE input, but it aligns more closely with Orel’s a-stem framing and with the OE plural evidence than with a literal Kroonen citation.

## Old English philology

`hwæl` is an attested OE lexeme/headword, not a project reconstruction. `old_english_wiktionary.tsv`, Clark Hall (`hwal ... m. 'whale'`), and Bosworth-Toller (`hwal ...`, with plural `hwalas`) all support that basic point.

The most useful philological contrast is singular `hwæl` versus plural `hwalas`. The a-restoration analysis and Ringe & Taylor both treat `hwalas` as preserving `a` in the open-syllable plural environment, while singular `hwæl` belongs with closed monosyllables that keep `æ`. That supports reading the row as the OE citation form, not as a claim that every paradigm cell had the same vowel outcome. I found no repo-local basis for stronger manuscript or dialect claims beyond ordinary OE attestation.

## Project problem and solution

The project problem had two layers:

1. **A now-fixed modelling error:** the older row state used `*walăz`, which could not transparently explain OE initial `hw-`.
2. **A still-murky explanatory note:** the live note now points in the right direction about initial `hw-`, but it attributes `*hwalaz` to Kroonen even though the repo’s Kroonen file actually gives `*hwali-`.

The current row is best understood as a resolved project-input choice. The row represents attested OE `hwæl`; the cascade needs `*xwálaz` to model that outcome; and `early_analogy` remains a reasonable label because the project is not merely copying a unanimous comparative protoform, but choosing an early English/Germanic input shape that fits the OE evidence, especially alongside plural `hwalas`.

## Paradigm probe

A paradigm probe is **not required** for this memo.

The row’s core issue is not competition among OE paradigm cells but the distinction between cognate-set proto, project input form, and attested OE target. If a future editor wants an optional supporting probe, the most useful cells would be the citation-form singular input (`*xwálaz`) and a representative plural input such as `*xwálōz` to illustrate the `hwæl` / `hwalas` split, but that is supplementary rather than missing required evidence.

## Recommended final report

Recommend a short final report stating that row 2284 represents attested OE `hwæl`, while the project deliberately distinguishes cognate-set `PROTO = *wálaz` from derivational `PROTOFORM = *xwálaz`. It should note that in-repo comparative sources diverge (`*xwalaz` in Orel, `*hwali-` in Kroonen), and that the project’s a-stem-like input is justified by the OE evidence (`hwæl` beside plural `hwalas`). It should explicitly avoid repeating the current inaccurate claim that Kroonen gives `*hwalaz`.

## Data-change recommendations

- **TSV `PROTO`: No change recommended.** `*wálaz` can remain as the cognate-set/alignment headword so long as the final report and note make clear that it is not identical with the OE modelling input.
- **TSV `PROTOFORM`: No change recommended.** `*xwálaz` is still the right project input for deriving `hwæl`.
- **TSV `COUNTERPART`: No change recommended.** `hwæl` is the correct OE target/headword.
- **TSV `DERIVATION_CLASS`: No change recommended.** `early_analogy` is still a defensible label for this early input/stem-shape choice.
- **TSV `NOTE`: Change recommended.** It should stop saying “Kroonen *hwalaz”; instead it should say that repo-local comparative sources diverge (Orel `*xwalaz`, Kroonen `*hwali-`) and that the project uses `*xwálaz` as the OE modelling input because the English evidence points to `hwæl` with plural `hwalas`.
- **`oe_known_problems.tsv`: No change recommended.** This is not an outstanding unmodelled exception.
- **`DEV_NOTES` / dossier text: No change required.** There is no dedicated DEV_NOTES entry or dossier for this lexeme that currently needs correction; the cleanup belongs in the TSV note/final report framing rather than in a separate ledger file.

# Research memo — 1934 bake / bacan

## Starting point
- ID: 1934.
- CONCEPT: bake.
- COUNTERPART: `bacan`.
- PROTO: `*bákaną`.
- PROTOFORM: `*bákaną`.
- DERIVATION_CLASS: `regular`.
- NOTE: “Proto encoding: -aną (full vowel) for A-restoration; R/T §6.3.1.”

## Packet evidence assessment
- **Authoritative/current:** the aligned TSV row; the packet’s compact current derivation (`*bákaną > bacan`); the current trace reports showing `EXPECTED: bacan`, `OUTPUTS: bacan`; and live `old_english.bin` probing (`bákaną -> bacan`).
- **Useful background:** the packet’s `DEV_NOTES` references on the earlier `bacen`/`bacana` failures and `Germanic/docs/analysis/arestoration_r_l_research.md`, because they show why `bacan` is the expected A-restoration outcome before single `k`.
- **Stale or superseded:** the March 2026 proposal to rewrite the OE infinitive rows to `-ăną`, plus older snapshots where `*bakaną` gave `bacen` or `*bakăną` gave `bacana`. Those are debugging history, not current row evidence.
- **Irrelevant or misleading:** English-sandbox mentions of Modern English `bake`, generic table-of-contents hits, and any note that treats debugging probe spellings (`*bakăną`, `*bakaną`) as if they were the current canonical row input.

## Additional repo research
Checked beyond the packet:
- `Germanic/docs/DEV_NOTES.md` at the 2026-03-13 `bacen` analysis (`9183-9224`), the same day’s `-ăną` recommendation (`9388-9514`), and the later A-restoration/breve reassessment (`21738-21940`).
- `Germanic/docs/analysis/arestoration_r_l_research.md` (`§157–159` quotations, especially Campbell §158 with `bacan` as a textbook A-restoration example).
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md`.
- `Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv` (checked; no row-specific entry).
- Live probe of `old_english.bin`.

## Reconstruction and early-stage forms
The row’s current project input is `*bákaną`, not an attested OE form. In current repo chronology that input yields Anglo-Frisian brightening `*bækaną`, then A-restoration back to `*bakaną`, then OE `bacan`. The important distinction is between:
- the reconstructed project input `*bákaną`;
- intermediate reconstructed OE-stage forms such as `*bækaną` / `*bakaną`;
- the attested OE infinitive `bacan`.

Older engineering variants such as `*bakăną` or unaccented `*bakaną` are useful only as probes of the grammar’s conditioning. They should not be promoted to the row’s preferred philological reconstruction now that the later `DEV_NOTES` section explicitly defends plain-suffix `a` for this Class VI infinitive class.

## Old English philology
`bacan` is the OE infinitive/citation form supported locally by `old_english_wiktionary.tsv` and by Campbell’s canonical A-restoration examples. The philological point is straightforward: this is an infinitive in `-an`, not a participle in `-en`, and not an oblique nominal cell. Earlier project discussion of `bacen` reflects a modelling problem in unstressed-vowel handling, not an alternative lexical target.

The repo evidence is therefore strongest for a conservative claim: OE `bacan` is attested, and the project row is correctly about that citation form.

## Project problem and solution
The real project problem was not lexical uncertainty about `bacan`, but conflicting internal encodings of the infinitival suffix during A-restoration/fronting work. March 2026 notes temporarily argued for rewriting these rows to `-ăną`; the later April 2026 notes reverse course and state that the current TSV keeps plain `a` in Class VI infinitives exactly because those rows need to trigger `OEARestoration`.

For row 1934, the solution is therefore to treat the current TSV/trace state as authoritative: the row represents OE `bacan`, and earlier `bacen` / `-ăną` discussions belong in project-history context only.

## Paradigm probe
No dedicated paradigm probe is required if the eventual report stays row-specific. If a final report wants to explain why infinitive `bacan` differs from participial `-en` outcomes, the only useful probe would be a contrast between an infinitive input and a participial input; otherwise a probe would add engineering detail without changing the lexical recommendation.

## Recommended final report
Recommend a short lexeme report stating that row 1934 targets the attested OE infinitive `bacan`, derived in the current project from `*bákaną` with expected A-restoration, and that older `bacen` / `-ăną` discussions are superseded debugging history rather than current lexical evidence.

## Data-change recommendations
- TSV `PROTO`: no change.
- TSV `PROTOFORM`: no change.
- TSV `COUNTERPART`: no change.
- TSV `DERIVATION_CLASS`: no change.
- TSV `NOTE`: no required change; optional clarification could cite the later `DEV_NOTES` section explaining why plain suffix `a` is retained for these Class VI infinitives.
- `oe_known_problems.tsv`: no change.
- `DEV_NOTES` / dossier text: `DEV_NOTES` should ideally mark the 2026-03-13 `-ăną` recommendation as superseded by the later 2026-04-21 analysis; no dossier change identified.

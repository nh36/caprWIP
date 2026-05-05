# Research memo — 2266 wade / wadan

## Starting point
- **ID:** 2266
- **CONCEPT:** wade
- **COUNTERPART:** `wadan`
- **PROTO:** `*wádaną`
- **PROTOFORM:** `*wádaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `Proto encoding: -aną (full vowel) for A-restoration; R/T §6.3.1`

This is a note-bearing regular OE row, so it still needs a concise final lexeme report even though the current derivation already lands on the expected infinitive.

## Packet evidence assessment
- **Authoritative/current:** the live TSV row; the packet’s compact derivation (`*wádaną > *wædaną > *wadaną > wadan`); the current debug-trace snapshot in `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md`; and the lexical-table confirmation in `Germanic/data/old_english_wiktionary.tsv`.
- **Useful background:** the packet’s A-restoration references in `Germanic/docs/analysis/arestoration_r_l_research.md`, `Germanic/docs/analysis/notable_findings.md`, and the relevant `DEV_NOTES.md` sections, because they explain why class-VI infinitives like `wadan` are supposed to show restored `a`.
- **Stale or superseded:** the March 2026 proposal that these OE infinitives should be rewritten to `-ăną`, along with older mismatch snapshots such as `*wadăną -> wædan`. Those are debugging history, not the current lexical decision.
- **Irrelevant or misleading:** generic table-of-contents hits for A-restoration, and any project note that treats probe spellings like `*wadăną` or erroneous `wæden` as if they were current row data rather than failed intermediate hypotheses.

## Additional repo research
Checked beyond the packet:
- `Germanic/docs/DEV_NOTES.md` at the A-restoration fix (`1649-1705`), the March 2026 `-ăną` proposal (`9288-9520`), and the later reassessment in §17.10.11 (`21729-21755`).
- `Germanic/docs/analysis/arestoration_r_l_research.md`.
- `Germanic/docs/analysis/notable_findings.md`.
- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md`.
- `Germanic/docs/germanic_notes/weak_tail_vowels_and_a_restoration.md`.
- `Germanic/docs/germanic_notes/oe_a_restoration_debug.md`.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md` and `Germanic/docs/debug_snapshots/oe_mismatch_report_2026-02-07_post_root_noun_fix.txt`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv` (checked; no row-specific entry).
- `Germanic/docs/lexeme_reports/pilot/` (no pilot report for this lexeme).

Main result of that broader check: the repo’s current evidence consistently treats `wadan` as an ordinary class-VI infinitive with A-restoration, while the `-ăną` idea survives only in superseded debugging chronology.

## Reconstruction and early-stage forms
For this row, the cognate-set proto and the project input form are currently the same: `PROTO = PROTOFORM = *wádaną`. That reconstructed input is not itself an attested OE form; it is the project’s derivational source.

The early OE staging reflected in the current trace is straightforward: Anglo-Frisian Brightening gives `*wædaną`, A-restoration returns `*wadaną`, and later reduction/apocope yields OE `wadan`. The target form is therefore the attested OE infinitive `wadan`, not the reconstructed intermediate stages.

The important negative point is that `*wadăną` belongs to an older engineering proposal, not to the current lexical reconstruction for row 2266. It should be treated as stale project history unless a future FST redesign explicitly reopens that encoding choice.

## Old English philology
`wadan` is an attested OE citation infinitive, not a reconstructed pseudo-form. Repo-local support is modest but sufficient: `old_english_wiktionary.tsv` gives `wade -> wadan`, and `arestoration_r_l_research.md` quotes Luick listing `wadan` among textbook open-syllable A-restoration examples.

Philologically, this row is about the infinitive/citation form, not about other paradigm cells. Earlier project outputs such as `wæden` reflect modelling failures in suffix/fronting handling, not a rival lexical target. The repo-local evidence does not require any dialect-specific or manuscript-specific qualification for the normalized counterpart `wadan`.

## Project problem and solution
The project problem was not uncertainty about whether OE had `wadan`; it was uncertainty about how the infinitival suffix should be encoded so that the OE pipeline produced `wadan` rather than fronted forms like `wæden`.

The chronology matters. March 2026 notes argued that reduced `*ă` should trigger A-restoration and that rows like this should move to `*wadăną`. Later `DEV_NOTES` analysis (§17.10.11) rejects that migration for the current system and states that the Class-VI infinitives keep plain-suffix `a` precisely because these rows rely on that vowel to trigger `OEARestoration`. On the current repo evidence, row 2266 is therefore already modelling the intended object correctly: the attested infinitive `wadan` from project input `*wádaną`.

## Paradigm probe
A dedicated paradigm probe is **not required** for this memo. The row’s target form is already settled by the current TSV, current trace, and handbook-style A-restoration evidence; the issue was implementation history, not an unresolved paradigm-cell choice.

If the supervisor later wants a small explanatory probe anyway, the only worthwhile cells would be the infinitive, present 2sg, present 3sg, and past participle, to show how citation-form `wadan` coexists with fronted/non-citation cells. That would be explanatory only, not a prerequisite for the final report.

## Recommended final report
Recommend a short final lexeme report saying that row 2266 targets the attested OE infinitive `wadan`, that the current project input `*wádaną` is intentionally retained because this class-VI infinitive needs the full-vowel `-aną` environment for the current A-restoration analysis, and that earlier `*wadăną` / `wæden` discussion is superseded debugging history.

## Data-change recommendations
- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no required change. Optional clarification could mention the later `DEV_NOTES` section that explicitly retains plain-suffix `a` for these class-VI infinitives.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** `DEV_NOTES` cleanup is recommended. The March 2026 `-ăną` recommendation should ideally be marked more explicitly as superseded by the later §17.10.11 analysis so repo search results do not over-weight stale guidance. No separate dossier-text change is identified.

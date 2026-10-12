---
row_id: 1972
concept: brook
counterpart: brūcan
proto: *brūkaną
protoform: *brūkaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1972 brook / brūcan

## Current row state

- The live OE row reads `1972 | brook | brūcan | *brūkaną | *brūkaną | regular`. The row still carries duplicated Wiktionary-etymology provenance in the trailing metadata field, but no row-local explanatory note of its own [Germanic/data/germanic-aligned-final.tsv:159-159].
- `coverage_audit.md` still marks the row as uncovered and shows no attached packet, research memo, or indexed fragment infrastructure: `| 1972 | brook | brūcan | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:213-213].
- `oe_known_problems.tsv` has no entry for row `1972`, `brook`, `brūcan`, or `*brūkaną`; the active ledger is presently about other OE exception buckets only [Germanic/data/oe_known_problems.tsv:1-8].
- The published OE derivation traces are exact matches. The compact trace gives `PROTO: *brūkaną`, `EXPECTED: brūcan`, `OUTPUTS: brūcan`, and the full trace repeats the same match for the live row [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:611-614; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:4179-4182].
- A directly related dossier exists, but it is class-level rather than row-local: the later `bugan-scufan` paradigm-cell review names `*brūcan*` among the other Class-II `*ū`-stem verbs that are not yet represented in strong-verb cells, which helps explain why no packet or memo for row `1972` exists yet [Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:530-537].

## Development-note summary

Surviving DEV_NOTES support for row `1972` is real but thin and mostly shared. No section of `Germanic/docs/DEV_NOTES.md` is a bespoke `brook / brūcan` dossier. The row appears in two materially relevant places only: first as one item in the old OE infinitive-ending bug bucket (`brūcana` instead of `brūcan`), and later as one of the handbook examples in the class-wide note on strong verbs with analogical present-system `*ū` instead of expected `*ēo` [Germanic/docs/DEV_NOTES.md:2422-2485,14354-14404].

The older diagnostic material is straightforwardly superseded, but it should not be discarded. DEV_NOTES explicitly set the engineering task as: “Weak-tail cleanup (`-ana` → `-an`): reshape or drop weak-tail `ă/ą` endings in verbs so outputs like `bacana/gennana/brecana/brengana/brūcana` converge on attested `-an`” [Germanic/docs/DEV_NOTES.md:2427-2427]. The matching evaluator snapshot then repeated `brūcana` in the sample list of bad `-ana` outputs whose targets should be bare infinitival `-an` [Germanic/docs/DEV_NOTES.md:2481-2485]. For row `1972`, that fragment preserves project history rather than a live philological controversy: the expected OE target was already `brūcan`, and the problem was unfinished weak-tail handling shared with other infinitives.

The later class-II strong-verb note is more substantive, though still indirect. DEV_NOTES opens a research section on verbs where the FST was producing `ēo` but attested OE shows `ū`, then quotes Ringe & Taylor: “A considerable group of verbs have `*ū` instead of `*ēo` in the present system … Examples are `*brūcan` 'use', `būgan` 'bend', `*lūcan` 'lock', `*strūdan` 'rob', `*sūcan` 'suck'” [Germanic/docs/DEV_NOTES.md:14354-14376]. DEV_NOTES then preserves Ringe & Taylor's conclusion that “most or all of the verbs with `*ū` must be innovative (either entirely new lexemes or remodellings of older verbs with `*eu`)” and immediately adds Campbell's matching list with `*brūcan` again included [Germanic/docs/DEV_NOTES.md:14391-14404]. For the present row, this matters in a bounded way: it is in-repo evidence that `brūcan` belongs to the recognized NWGmc/OE analogical `*ū` group, but the note was written to diagnose other rows and does **not** itself order a change to row `1972`, split `PROTO` from `PROTOFORM`, or create a row-local exception policy.

The conservative row-level reading is therefore limited but usable. DEV_NOTES does support the live row state `*brūkaną → brūcan`, but only through shared material: an old diagnostic showing that `brūcan` was already the intended infinitive target, and a later literature summary showing that `brūcan` is a standard example of the analogical `*ū` class rather than an isolated spelling accident [Germanic/data/germanic-aligned-final.tsv:159-159; Germanic/docs/DEV_NOTES.md:2427-2427,2481-2485,14372-14404].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2422-2485

- Source heading: `PGmc→OE TODOs (consolidated)` / `OE evaluator snapshot (old_english.bin)` / `Ending diagnostics (old_english.bin)`
- Source line or section hint: `lines 2422-2485`
- Fragment type: `shared_diagnostic_bucket_with_row_explicit_hit`
- Status: `diagnostic_only`
- Issue tags: `weak_tail_cleanup`; `infinitive_-an`; `historical_mismatch`; `oe_evaluator`
- Recommended next use: `preserve_as_old_mismatch_history_not_current_policy`
- Shared with row IDs: `1934`; `1943`; `1967`; `1971`

This is the earliest surviving DEV_NOTES material that names the lexeme directly. DEV_NOTES states the cleanup target in so many words: “reshape or drop weak-tail `ă/ą` endings in verbs so outputs like `... brūcana` converge on attested `-an`” [Germanic/docs/DEV_NOTES.md:2427-2427]. The same diagnostic block then repeats `brūcana` in the bad-output sample list: “Sample `-ana` outputs where target is `-an`: `... brūcana` (brook)” [Germanic/docs/DEV_NOTES.md:2481-2485]. For row `1972`, this should be cited only as labelled chronology. It shows that `brūcan` was already the intended OE infinitive while the stack was still overproducing weak tails.

### DEV_NOTES:line-14354-14404

- Source heading: `Class II Strong Verbs with *ū instead of *ēo: Analogical Leveling (2026-04-06)`
- Source line or section hint: `lines 14354-14404`
- Fragment type: `shared_literature_summary_with_row_explicit_hit`
- Status: `current_background`
- Issue tags: `analogical_ū`; `class_II_strong_verbs`; `shared_source_quote`; `not_row_specific_fix`
- Recommended next use: `cite_as_class_level_support_only`
- Shared with row IDs: `1962`; `2184`

This is the only surviving DEV_NOTES fragment that preserves substantive literature reasoning directly naming `brūcan`. DEV_NOTES first frames the class-wide problem as mismatches where the FST produced `ēo` but attested OE has `ū` [Germanic/docs/DEV_NOTES.md:14356-14366]. It then quotes Ringe & Taylor's list of verbs with innovative present-system `*ū`, including “`*brūcan` 'use'” [Germanic/docs/DEV_NOTES.md:14372-14376], and preserves the follow-up conclusion that these verbs are largely innovative or remodeled forms rather than ordinary continuations of the expected `*eu` pattern [Germanic/docs/DEV_NOTES.md:14391-14396]. Campbell is then quoted as confirming the same list, again naming `*brūcan` [Germanic/docs/DEV_NOTES.md:14398-14404]. For row `1972`, the important limitation is part of the substance: `brūcan` is present here as a class member and handbook example, not as the target of a row-specific repair. The fragment supports the long `ū` of the live row, but it should not be promoted into evidence for any extra metadata surgery that DEV_NOTES never actually proposed.

## Superseded or diagnostic material

- The `brūcana` mismatch is superseded as current row policy. It records an older stage where OE infinitives still surfaced with unreduced weak tails, not a surviving alternative target or a reason to mistrust `brūcan` [Germanic/docs/DEV_NOTES.md:2427-2427,2481-2485].
- The analogical-`*ū` discussion is **not** superseded, but for row `1972` it remains diagnostic/background rather than a dedicated implementation note. DEV_NOTES used `brūcan` as one member of a recognized class while actively solving other lexemes, so later writeups should cite it conservatively as class support, not as a hidden row-specific retargeting order [Germanic/docs/DEV_NOTES.md:14354-14404].
- The dossier note that other Class-II `*ū`-stem verbs, including `*brūcan*`, are not yet represented in strong-verb cells is also diagnostic only. It explains the absence of a row-local paradigm-cell review, but it does not itself change the infinitive row now under discussion [Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:530-537].

## Open questions for later work

- If a fuller lexeme report is written later, add direct lexical-source support for the OE verb itself; the surviving DEV_NOTES material explains the old mismatch and the class-level analogical `*ū` background, but it is still thin as a standalone monograph on `brook / brūcan`.
- If future work adds non-infinitive cells for this lexeme, reuse the class-II `*ū`-stem policy discussion deliberately rather than by analogy alone. The current dossier explicitly says those other verbs, including `*brūcan*`, have not yet had the same cell-level review given to `būgan` and `sċūfan` [Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:530-537].
- This slice is probably better treated as no-index material unless a later packet or memo adds a genuinely row-specific argument. The current evidence is useful and should be preserved, but most of it is shared class history rather than a dedicated `1972` dossier.

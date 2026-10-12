---
row_id: 2304
concept: wring
counterpart: wringan
proto: *wrínganą
protoform: *wrínganą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: null
linked_research_memo_file: null
linked_dossier_or_analysis_files: []
current_status: conservative_shared_background_only
needs_literature_agent: no
---

# DEV_NOTES material — 2304 wring / wringan

## Current row state

- The live OE row is plain and currently problem-free: `row_id 2304`, `CONCEPT = wring`, `COUNTERPART = wringan`, `PROTO = *wrínganą`, `PROTOFORM = *wrínganą`, `DERIVATION_CLASS = regular`. The row carries source attributions but no row-local NOTE text and no derivation-class override beyond `regular` [Germanic/data/germanic-aligned-final.tsv:1450-1453].
- `PROTO` and `PROTOFORM` are presently identical. That matters because nothing in the live data suggests that the OE target is being reached through an alternate oblique cell, an analogical surrogate, or a reconstructed OE-only preform; the same comparative input `*wrínganą` is also the cascade input for the OE derivation [Germanic/data/germanic-aligned-final.tsv:1452-1452].
- The published derivation snapshot is an exact match with no repair logic exposed: `PROTO: *wrínganą`, `EXPECTED: wringan`, `OUTPUTS: wringan`, with OE-side stages only `OE Heavy Syllable Nasal Apocope: *wríngan`, `OE Secondary Nasalization: *wríngąn`, and `OE Weak Tail Reduction: *wríngan`, finishing at `Outcome: wringan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6085-6104].
- The full trace confirms how inert the row is under the present cascade. All potentially relevant shared-problem rules visible around other `*ng` and unstressed-vowel items stay `[no-change]` here, including `OEMedUnstressedILowering`, `OEIUmlaut`, `OEVelarPalatalization`, `OEBackMutation`, `OERMetathesis`, and `OldEnglishOrthography`; only the ordinary infinitive steps named above actually fire [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:34757-34871].
- `oe_known_problems.tsv` contains no entry for `*wrínganą`, `wringan`, or row `2304`, so the row is not currently managed as an exception, wontfix, or analogue-driven mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- `coverage_audit.md` also keeps row `2304` in the ordinary “regular rows with empty NOTE and no report required” bucket: `| 2304 | wring | wringan | regular | no | - | - | - | none |`. This slice therefore replaces no rich pre-existing row packet; it is a conservative row-local note built mainly from current exact-match state plus the nearest surviving shared DEV_NOTES background [Germanic/docs/lexeme_reports/coverage_audit.md:419-421].

## Development-note summary

No row-specific `DEV_NOTES.md` block for `wring / wringan / *wrínganą` survives in the current live notes. The row is absent from the reviewed `DEV_NOTES` lexical discussions, so there is no dedicated wringan dossier to condense here. What does survive is thinner and must be classified carefully: (i) the row’s own exact-match live trace, which is row-specific and current; (ii) shared 2026 notes about unstressed-front-vowel lowering and `*_ng` restoration, which are **background only** or **diagnostic by parallel**, not direct evidence about row 2304 itself [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6085-6104; Germanic/docs/DEV_NOTES.md:6636-6657,38257-38303,38371-38386].

The main practical conclusion is simple: row 2304 currently needs no special phonological rescue. The full trace shows that the usual trouble spots from nearby DEV_NOTES debates do not engage this item: there is no medial unstressed-`*i` lowering event, no `*_ng` restoration event, no palatalization dispute, and no metathesis issue; the form simply passes through ordinary OE infinitive shaping to `wringan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:34812-34821,34827-34831,34847-34852,34858-34871].

The closest surviving shared DEV_NOTES material is the 2026 `*ĭ` cleanup. That material does **not** name `wringan`; it names `bringan` and suffixal `-ing-` forms as sentinels while explaining when unstressed `*i` should lower to `e` and when `i` should be restored before retained velar `*ng` [Germanic/docs/DEV_NOTES.md:38264-38272,38292-38303,38371-38386]. For row 2304, that material is useful only as a boundary marker: it explains why later reviewers might be tempted to inspect a `*wrínganą` form for `*ng`-related behavior, but the current row trace shows that none of that shared repair machinery is actually invoked here [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:34784-34799,34847-34852].

The shared handbook digest on unstressed front-vowel merger is likewise background only. DEV_NOTES preserves Hogg’s statement that “by about 700 all unstressed front vowels had become /e/,” with the exception that `[i] was preserved in derivational suffixes such as -ig, -ing, -isc” [Germanic/docs/DEV_NOTES.md:6636-6645]. That is important background for the 2026 `*_ng` repair, but it should not be overread into row 2304: `wringan` is not presented anywhere in DEV_NOTES as an `-ing`-suffix noun/adjective problem, and the current derivation trace shows no unstressed front-vowel lowering pressure on the row in the first place [Germanic/docs/DEV_NOTES.md:6647-6657; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:34847-34850].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-38257-38303

- Source heading: `§17.35.10 Closure (2026-04-27)`
- Source line hint: `lines 38257-38303`
- Fragment type: `shared_background_only_with_diagnostic_parallel`
- Status: `current`
- Issue tags: `unstressed_i_lowering`; `ng_restoration`; `bringan_parallel`; `do_not_overread`
- Recommended next use: `cite only if explaining which shared 2026 repair area row 2304 does not enter`
- Shared-with rows if relevant: `1971`, `2057`, `2181`, `2228`

This is the nearest current DEV_NOTES material, but it is not row-specific. The closure rewrites `OEMedUnstressedILowering` as a composition and preserves the key wording: “Restore *e → *i before the *ng cluster ... Phonetic blocking, not morpho-lexical: *ng is the diagnostic for *-ing-/*-ung- derivational suffixes at this stage” [Germanic/docs/DEV_NOTES.md:38264-38272]. Its regression table then lists `*brínganą → bringan` as `✓ no change`, beside the repaired `*-ing-*` nouns and other controls [Germanic/docs/DEV_NOTES.md:38292-38303].

For row 2304 this fragment is **shared-background-only** and **diagnostic by analogy**. It identifies the rule family that a superficially similar `*...ng...` form might trigger, but the published trace for `*wrínganą` shows that row 2304 does not actually pass through the relevant lowering/restoration sequence: both the Northwest Germanic and Old English preconditions remain `[no-change]` until the ordinary infinitive-end steps fire [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:34784-34799,34847-34852]. Use this fragment only to explain the nearby shared repair landscape, not as if DEV_NOTES had written a `wringan` note.

### DEV_NOTES:line-38371-38386

- Source heading: `§17.36 *ĭ (i-breve) cleanup — incremental dismantling`
- Source line hint: `lines 38371-38386`
- Fragment type: `diagnostic_shared_regression_parallel`
- Status: `current`
- Issue tags: `sentinel_table`; `brengan_blocking`; `suffix_an_protection`; `parallel_only`
- Recommended next use: `cite only if a later rule refactor needs a verb-in-ng-aną comparator`
- Shared-with rows if relevant: `1943`, `1971`, `2057`, `2181`, `2228`

This sentinel table is even more clearly diagnostic rather than row-specific. DEV_NOTES keeps `*brínganą → bringan` in the must-stay-stable set with the note “`*brengan` blocking, suffix-an protection” [Germanic/docs/DEV_NOTES.md:38371-38386]. The usefulness for row 2304 is narrow: it shows that the project already treats at least one strong verb in `*-nganą` as a regression sentinel when refactoring unstressed-`*i` behavior. But the table still names `bringan`, not `wringan`, and the row-2304 trace gives no sign that an analogous repair is needed or firing now [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:34847-34852].

If a later phonology pass broadens or rewrites the `*ĭ` logic again, row 2304 could reasonably be added to the same kind of sentinel set because its current trace is entirely stable. At present, though, this fragment remains **diagnostic material only**, not support for any row-specific intervention.

### DEV_NOTES:line-6636-6657

- Source heading: `OE hierfest 'harvest' — Unstressed Front Vowel Merger`
- Source line hint: `lines 6636-6657`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `unstressed_front_vowel_merger`; `derivational_suffix_i`; `background_not_row_specific`
- Recommended next use: `cite only to define the shared vowel-lowering background behind the 2026 cleanup`
- Shared-with rows if relevant: `2057`, `2181`, `2228`

This is the best preserved handbook quotation behind the 2026 repair family, but it is still only shared background for row 2304. DEV_NOTES quotes Hogg: “by about 700 all unstressed front vowels had become /e/. The only exception is that [i] was preserved in derivational suffixes such as -ig, -ing, -isc, e.g. ... cyning” [Germanic/docs/DEV_NOTES.md:6636-6645]. Campbell and Ringe–Taylor are then quoted for the ordinary merger of unstressed `æ/e/i` to `e`, again with suffixal survivals handled as special cases [Germanic/docs/DEV_NOTES.md:6647-6657].

For `wringan`, this fragment should be used conservatively. It explains the general historical background of the `*ĭ` cleanup, but the row’s own trace shows no unstressed front vowel under active treatment, and nothing in current DEV_NOTES treats `wringan` as a derivational `-ing-` preservation case [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:34847-34850]. Its status here is therefore **shared-background-only**, not lexical support.

## Superseded or diagnostic material

- No explicit `wringan` block survives in current `DEV_NOTES.md`, so later writers should not silently substitute the `bringan` sentinel passages as if they were row-2304 evidence. Those passages are the nearest parallels, but they remain parallels [Germanic/docs/DEV_NOTES.md:38292-38303,38371-38386].
- The shared `*_ng` / unstressed-`*i` material is diagnostic only for this row. The full trace shows `OEMedUnstressedILowering [no-change]` and `OEMedUnstressedILowering1 [no-change]`, so the 2026 repair family is not part of the row’s live derivation path at present [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:34847-34848].
- There is no current exception-management signal to preserve here: `oe_known_problems.tsv` has no `*wrínganą` entry, and `coverage_audit.md` classifies the row as ordinary `regular | no | ... | none` rather than as a note-bearing or report-required item [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:421-421].
- Because the row currently reaches `wringan` exactly from `*wrínganą`, any future note that turns this lexeme into a problem case would need fresh evidence rather than appeal to a lost DEV_NOTES block. The surviving material documents regularity plus nearby shared rule history, not a suppressed controversy.

## Open questions for later work

- If a fuller philological packet is ever wanted for row 2304, it will need fresh lexicographic/literature gathering; this slice cannot recover a non-existent row-specific DEV_NOTES block.
- If future refactors touch `*_ng` behavior, unstressed-`*i` lowering, or strong-verb `*-aną` handling, row 2304 is a good candidate for an added sentinel probe because the current full trace shows it should remain inert except for ordinary nasal apocope, secondary nasalization, and weak-tail reduction [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:34820-34821,34847-34852].
- If `index.tsv` is revisited later, row 2304 should probably remain unindexed unless a genuinely row-specific evidence block is created; the present slice is intentionally conservative and built mostly from shared-background-only material plus current row state.

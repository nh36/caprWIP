---
row_id: 1989
concept: dew
counterpart: dēaw
proto: *dáwwō
protoform: *dáwwō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/lexeme_reports/coverage_audit.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1989 dew / dēaw

## Current row state

- The live OE row is `1989`, with `CONCEPT = dew`, `COUNTERPART = dēaw`, `PROTO = *dáwwō`, `PROTOFORM = *dáwwō`, and `DERIVATION_CLASS = regular`; the row has duplicated Wiktionary inheritance sourcing and no live exception note in the TSV [Germanic/data/germanic-aligned-final.tsv:227-227].
- Coverage tracking still records row `1989 | dew | dēaw | regular | no | - | - | - | none`, so there is no packet, research memo, dossier, or full report stem currently linked for this lexeme [Germanic/docs/lexeme_reports/coverage_audit.md:223-223].
- The current published derivation trace is an exact match: `PROTO: *dáwwō`, `EXPECTED: dēaw`, `OUTPUTS: dēaw`; the OE side now runs through `OE WW Simplification: *dáwu`, `OE Aw Long Diphthong: *dḗawu`, and `OE High Vowel Apocope: *dḗaw`, surfacing as `Outcome: dēaw` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:896-914].
- `oe_known_problems.tsv` does not list this row or protoform. That is consistent with the present row state: whatever earlier debugging existed in DEV_NOTES is not being carried as a current OE known-problem entry [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

DEV_NOTES support for row 1989 is real but relatively thin, and it is almost entirely rule-diagnostic rather than philological. The notes do not preserve a long standalone lexeme essay for `dew / dēaw`; instead they preserve the row as one of the project’s recurring `*ww` / `*aw` control cases. The earliest directly relevant surviving note is a February 2026 mismatch audit under `Breaking gaps`, where `*dawwō (dew)` is said to have passed Anglo-Frisian brightening to `*æw`, but then stalled because `EnglishBreakingA` had no `w` context, yielding `dawō` instead of expected `dēaw` [Germanic/docs/DEV_NOTES.md:1715-1717]. That is the clearest statement of the original problem as DEV_NOTES understood it: the issue was not doubt about the target `dēaw`, but missing breaking behavior in the `a/æ + w` environment.

A later repair note records the row among the immediate beneficiaries of a pipeline intervention placed after `OEEwLongDiphthong` and before Anglo-Frisian brightening. There DEV_NOTES says `*dawwō → dēaw (was dawu) — dew` under `Fixes (3 new matches)` [Germanic/docs/DEV_NOTES.md:3639-3645]. For replacement-note purposes, that fragment matters because it preserves both the claimed solution and a second older bad-output signature (`dawu`). The exact pre-fix surface differs from the February note’s `dawō`, so the safe conclusion is only that row 1989 went through more than one debugging snapshot before stabilizing, not that DEV_NOTES preserves a single perfectly consistent failed derivation state [Germanic/docs/DEV_NOTES.md:1717-1717; Germanic/docs/DEV_NOTES.md:3642-3645].

The most useful current-state DEV_NOTES material is the shared `*ww` discussion later in the file. DEV_NOTES gives `*dawwō` as a textbook example of the development `PWGmc *dauwō > OE dēaw`, then immediately remarks that the existing FST already handles `*ww` inputs correctly: `Testing *kewwăną → ċēowan ✓, *dawwō → dēaw ✓, *xawwăną → hēawan ✓` [Germanic/docs/DEV_NOTES.md:16272-16275; Germanic/docs/DEV_NOTES.md:16308-16324]. That section also adds a methodological caution that the present implementation may reach the correct result by a mechanism somewhat different from Ringe–Taylor’s two-step account, so later prose should distinguish verified outcome from overconfident claims about the exact internal path [Germanic/docs/DEV_NOTES.md:16313-16317].

Finally, the later `*aw+j` risk audit uses row 1989 as a safe non-target control. In the affected-forms table, row 1989 appears as `1989 *dáwwō            dēaw           dēaw            ✓ no *j present`, and the regression table classifies `Other *Vw` items like `*dáwwō, *láugō` as `NONE` risk because there is no following `*j` [Germanic/docs/DEV_NOTES.md:26619-26628; Germanic/docs/DEV_NOTES.md:26678-26685]. So the present replacement note should treat row 1989 as a solved regular row whose documentary value lies mainly in shared OE breaking / `*ww` rule history.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1715-1717

- Source line or section hint: `lines 1715-1717`
- Fragment type: `rule_not_firing_diagnosis`
- Status: `diagnostic_only`
- Issue tags: `breaking_gap`; `a_or_æ_plus_w`; `former_output_dawō`
- Recommended next use: `cite_if_explaining_why_the_row_once_failed`
- Shared with row IDs: `1968`

This is the earliest explicit row-specific DEV_NOTES material now visible. DEV_NOTES says: `**Breaking gaps**: *brustz (breast) shows no u-breaking; output brust vs expected brēost. *dawwō (dew) passes A-F brightening (*æw) but EnglishBreakingA lacks a w context; output dawō vs expected dēaw` [Germanic/docs/DEV_NOTES.md:1715-1717]. The important substance is the diagnosis, not just the mismatch: the project thought the row had already reached the brightened `*æw` stage and was then failing because the breaking rule did not recognize `w` as a trigger context.

### DEV_NOTES:line-3639-3645

- Source line or section hint: `lines 3639-3645`
- Fragment type: `repair_note`
- Status: `current_for_history`
- Issue tags: `pipeline_placement`; `new_match`; `former_output_dawu`
- Recommended next use: `cite_if_describing_the_specific_fix_window`
- Shared with row IDs: `2227`; `2074`

This is the clearest “fixed now” DEV_NOTES fragment. After specifying pipeline placement, DEV_NOTES lists three new matches and includes the exact line `*dawwō → dēaw (was dawu) — dew` [Germanic/docs/DEV_NOTES.md:3639-3645]. The fragment should be preserved because it ties row 1989 to a concrete repair pass and shows that the row belonged to the same intervention that also improved `straw` and `hew`. It is still partly diagnostic only, because the older failing form here (`dawu`) does not perfectly match the separate February diagnostic (`dawō`).

### DEV_NOTES:line-16272-16324

- Source line or section hint: `lines 16272-16324`
- Fragment type: `shared_rule_discussion_and_verification`
- Status: `current`
- Issue tags: `ww_handling`; `pwgmc_dauwō`; `verified_exact_match`
- Recommended next use: `cite_if_documenting_the_current_solved_state`
- Shared with row IDs: `1976`; `2061`; `2074`

This is the strongest shared current-state material for the row. DEV_NOTES first gives `*dawwō` as an example in the chain `*dawwō 'dew' > PWGmc *dauwō > OE dēaw` [Germanic/docs/DEV_NOTES.md:16272-16275]. It then states: `Note: The existing FST already handles *ww inputs correctly via *ww → ēo. Testing *kewwăną → ċēowan ✓, *dawwō → dēaw ✓, *xawwăną → hēawan ✓` and repeats row 1989 in the list of existing TSV `*ww` entries [Germanic/docs/DEV_NOTES.md:16308-16324]. The same passage also warns that the implementation may be reaching the right answer by “a different mechanism than R/T's two-step analysis,” which should be retained as a caution against overspecifying the internal derivation beyond the verified output [Germanic/docs/DEV_NOTES.md:16313-16317].

### DEV_NOTES:line-26619-26685

- Source line or section hint: `lines 26619-26685`
- Fragment type: `regression_scope_note`
- Status: `current`
- Issue tags: `safe_control`; `no_j_present`; `other_Vw`
- Recommended next use: `cite_if_explaining_why_later_aw_plus_j_work_should_not_touch_this_row`
- Shared with row IDs: `1976`; `2061`; `2074`; `2116`; `2227`

This later note matters because it defines row 1989’s role in subsequent OE work. The affected-forms table lists `1989 *dáwwō            dēaw           dēaw            ✓ no *j present`, and the regression table explicitly classifies `Other *Vw       *dáwwō, *láugō — no *j present             NONE` [Germanic/docs/DEV_NOTES.md:26619-26628; Germanic/docs/DEV_NOTES.md:26678-26685]. For later work, this is the fragment that most clearly marks `dew / dēaw` as a solved control case that should stay outside narrow `*aw+j` interventions.

## Superseded or diagnostic material

- The older failed outputs `dawō` and `dawu` are both superseded. They are worth preserving only as debugging history showing that row 1989 passed through more than one pre-fix failure signature before the current exact-match state was reached [Germanic/docs/DEV_NOTES.md:1717-1717; Germanic/docs/DEV_NOTES.md:3643-3643].
- The February `Breaking gaps` note is diagnostic, not a live row recommendation. It preserves the project’s then-current claim that `EnglishBreakingA` lacked a `w` context after A-F brightening to `*æw`, but it does not compete with the present row state or with the later successful trace [Germanic/docs/DEV_NOTES.md:1715-1717; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:896-914].
- No surviving DEV_NOTES passage argues for a `PROTO`/`PROTOFORM` split, a non-regular derivation class, or a different OE target. The later notes uniformly treat `*dáwwō → dēaw` as a regular solved row and use it as a control in broader rule work [Germanic/data/germanic-aligned-final.tsv:227-227; Germanic/docs/DEV_NOTES.md:16321-16324; Germanic/docs/DEV_NOTES.md:26624-26624].

## Open questions for later work

- If a future full report wants a more precise bug chronology, inspect the archived traces behind the February and later repair notes to determine why one DEV_NOTES snapshot reports `dawō` while another reports `dawu` [Germanic/docs/DEV_NOTES.md:1717-1717; Germanic/docs/DEV_NOTES.md:3643-3643].
- If later prose wants to say more than “regular solved row,” it may need a fresh literature pass, because the surviving DEV_NOTES material for row 1989 is mostly shared rule-debugging and contains little lexeme-specific philological discussion beyond the PWGmc `*dauwō > dēaw` example [Germanic/docs/DEV_NOTES.md:16272-16275; Germanic/docs/DEV_NOTES.md:16308-16324].
- For indexing purposes, this slice probably remains a `no-index` candidate unless the project decides to index short shared rule-history controls. The material is useful and explicit, but thin, heavily shared, and primarily diagnostic rather than a rich row-specific dispute dossier [Germanic/docs/lexeme_reports/coverage_audit.md:223-223; Germanic/docs/DEV_NOTES.md:1715-1717; Germanic/docs/DEV_NOTES.md:26619-26685].

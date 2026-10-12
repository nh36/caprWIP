---
row_id: 1976
concept: chew
counterpart: ċēowan
proto: *kéwwaną
protoform: *kéwwaną
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

# DEV_NOTES material — 1976 chew / ċēowan

## Current row state

- The live OE row is `1976`, with `CONCEPT = chew`, `COUNTERPART = ċēowan`, `PROTO = *kéwwaną`, `PROTOFORM = *kéwwaną`, and `DERIVATION_CLASS = regular`; the row carries only duplicated Wiktionary inheritance sourcing and no live exception note [Germanic/data/germanic-aligned-final.tsv:175-175].
- The row is not currently listed in `oe_known_problems.tsv`; that file only tracks a small set of unrelated OE exceptions and known non-fixes, so row 1976 is not being treated as a live OE problem at present [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still records row `1976 | chew | ċēowan | regular | no | - | - | - | none`, so there is no pre-existing packet, research memo, dossier, or full report stem for this lexeme beyond general analysis files [Germanic/docs/lexeme_reports/coverage_audit.md:215-215].
- The current published derivation trace is an exact match: `PROTO: *kéwwaną`, `EXPECTED: ċēowan`, `OUTPUTS: ċēowan`, with OE-side steps `OE WW Simplification: *kéwaną`, `OE Ew Long Diphthong: *kēowaną`, `OE Heavy Syllable Nasal Apocope: *kēowan`, `OE Secondary Nasalization: *kēowąn`, `OE Velar Palatalization: *ʧēowąn`, and surface `Outcome: ċēowan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:672-692].

## Development-note summary

DEV_NOTES preserves a clear before/after history for this row even though the lexeme does not have a long standalone essay. In the January 2026 OE mismatch audits, row 1976 was still being used as a live failure in the “long-vowel missing” bucket: the report listed `*kewwăną → ċeowwan (expected ċēowan)` and pointed readers to a dedicated trace file for that bucket [Germanic/docs/DEV_NOTES.md:2622-2624]. The problem was not uncertainty about the target lexeme. DEV_NOTES consistently treats `ċēowan` as the intended OE outcome; the issue was that the derivation was underproducing the long diphthong and still surfacing an overconservative `-ww-` style result.

The most explicit repair note comes immediately afterward in the January 2026 follow-up list. DEV_NOTES states: `*kewwăną → ċēowan`: `OldEnglishEwLongDiphthong` only sees single `{*w}`; extend the rule to promote `{eww}` to `{ēow}` so duplicated glides still trigger the long diphthong tier [Germanic/docs/DEV_NOTES.md:1769-1773]. For replacement-note purposes, that sentence preserves the substantive project diagnosis: the troublesome environment was specifically `*eww`, and the missing behavior was promotion to the long OE diphthong tier rather than any rethinking of the row's protoform or counterpart.

Later DEV_NOTES material shows that this issue moved from active bug to solved control case. A subsequent verification note says, `Note: The existing FST already handles *ww inputs correctly via *ww → ēo. Testing *kewwăną → ċēowan ✓, *dawwō → dēaw ✓, *xawwăną → hēawan ✓` [Germanic/docs/DEV_NOTES.md:16308-16313]. That same section then lists row 1976 among the existing `*ww` entries already handled correctly [Germanic/docs/DEV_NOTES.md:16319-16325]. The important replacement-note point is chronological: early January notes preserve the bug signature and proposed remedy; later notes preserve the fact that the grammar now treats `*kewwăną` as a successful inherited `*ww` case.

A still later `*aw+j` risk audit reinforces that solved status by using row 1976 as a non-problem control. In the table of potentially affected forms, row 1976 appears as `*kéwwaną          ċēowan         ċēowan          ✓ no *j present`, and the regression-risk summary classifies `*kéwwaną, *xáwwaną` under `Class VII       ... NONE` because there is no following `*j` to trigger the new rule under discussion [Germanic/docs/DEV_NOTES.md:26619-26624; Germanic/docs/DEV_NOTES.md:26678-26685]. That matters for this slice because it shows how the row functions in current project reasoning: not as a disputed philological item, but as evidence that ordinary OE handling of `*eww` Class VII verbs should stay untouched while nearby `*aw+j` repairs are made.

Taken together, the current state is straightforward. The live row keeps `PROTO = PROTOFORM = *kéwwaną`, the live target remains `ċēowan`, and the active trace now derives it regularly [Germanic/data/germanic-aligned-final.tsv:175-175; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:672-692]. The value of the DEV_NOTES material is therefore mostly project-historical and rule-diagnostic: it records that row 1976 was once a long-diphthong failure, that DEV_NOTES explicitly framed the missing behavior as duplicated-glide handling in the `*eww` environment, and that later notes treat the row as verified and safe from unrelated `*aw+j` interventions [Germanic/docs/DEV_NOTES.md:1769-1773; Germanic/docs/DEV_NOTES.md:16308-16325; Germanic/docs/DEV_NOTES.md:26619-26624].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2622-2624

- Source heading: `Closeness scan` / `Long-vowel missing probe narrowed`
- Source line or section hint: `lines 2622-2624`
- Fragment type: `diagnostic_bucket`
- Status: `diagnostic_only`
- Issue tags: `long_vowel_missing`; `former_output_ċeowwan`; `oe_mismatch_audit`
- Recommended next use: `cite_if_describing_early_bug_state`
- Shared with row IDs: `2033`; `2074`; `2155`; `2204`; `2281`

This is the earliest directly row-specific surviving DEV_NOTES fragment for the OE issue. It says the long-vowel-missing list currently includes ``*kewwăną → ċeowwan (expected ċēowan)`` [Germanic/docs/DEV_NOTES.md:2622-2624]. The fragment is worth preserving because it captures the exact bad output shape that the later repair discussion is trying to eliminate. It should, however, be treated as diagnostic history only: it documents a no-longer-current failure state, not a competing OE target.

### DEV_NOTES:line-1769-1773

- Source heading: `Next actionable targets (carryover)` / `2026-01-10 tracing follow-up`
- Source line or section hint: `lines 1769-1773`
- Fragment type: `rule_diagnosis`
- Status: `current_for_history`
- Issue tags: `oldenglishewlongdiphthong`; `duplicated_glide`; `repair_plan`; `eww_to_ēow`
- Recommended next use: `cite_when_explaining_why_row_once_failed`
- Shared with row IDs: `2033`; `2204`

This is the controlling DEV_NOTES fragment for the original repair logic. DEV_NOTES says: ``*kewwăną → ċēowan`: `OldEnglishEwLongDiphthong` only sees single `{*w}`; extend the rule to promote `{eww}` to `{ēow}` so duplicated glides still trigger the long diphthong tier`` [Germanic/docs/DEV_NOTES.md:1770-1770]. The key substance is not merely that the row was fixed, but how the fix was understood at the time: the project was diagnosing a duplicated-glide blind spot in the OE long-diphthong machinery. Use this fragment when explaining why row 1976 belonged in the long-vowel-missing bucket in the first place.

### DEV_NOTES:line-16308-16325

- Source heading: `Rule 2: PWGmc Geminate *ww Simplification` / `Verification of Existing *ww Handling`
- Source line or section hint: `lines 16308-16325`
- Fragment type: `verification_probe`
- Status: `current`
- Issue tags: `ww_handling`; `exact_match`; `control_case`; `verification`
- Recommended next use: `cite_if_documenting_current_solved_state`
- Shared with row IDs: `1989`; `2061`; `2074`

This is the strongest current-state DEV_NOTES material for the row. DEV_NOTES explicitly says, `Note: The existing FST already handles *ww inputs correctly via *ww → ēo. Testing *kewwăną → ċēowan ✓, *dawwō → dēaw ✓, *xawwăną → hēawan ✓` and then repeats row 1976 in the list of `Existing TSV entries with *ww` [Germanic/docs/DEV_NOTES.md:16310-16312; Germanic/docs/DEV_NOTES.md:16321-16324]. The note also adds a useful caution: the system may be reaching the right result through “a different mechanism than R/T's two-step analysis,” so later writers should not overstate the exact implementation internals beyond the verified fact that `*kewwăną` now derives correctly [Germanic/docs/DEV_NOTES.md:16316-16317].

### DEV_NOTES:line-26619-26685

- Source heading: `Affected forms in our TSV` / `Regression risk assessment`
- Source line or section hint: `lines 26619-26685`
- Fragment type: `regression_scope_note`
- Status: `current`
- Issue tags: `no_j_present`; `safe_control`; `aw_plus_j_scope`; `class_vii`
- Recommended next use: `cite_if_explaining_why_new_awj_rules_should_not_touch_this_row`
- Shared with row IDs: `1989`; `2061`; `2074`; `2227`

This fragment matters because it shows row 1976 being used as a safety check rather than as a target for repair. In the affected-forms table, the row is listed as ``1976 *kéwwaną          ċēowan         ċēowan          ✓ no *j present`` [Germanic/docs/DEV_NOTES.md:26619-26624]. The regression table then states that the `Class VII` cases `*kéwwaną, *xáwwaną` have `NONE` risk because there is no `*j` after the glide cluster [Germanic/docs/DEV_NOTES.md:26678-26685]. For later work, this is the fragment that most clearly protects the row from being swept back into unrelated `*aw+j` or `*j`-strengthening interventions.

## Superseded or diagnostic material

- The older output `ċeowwan` is superseded project history only. It is useful because it preserves the exact failure signature that put the row into the long-vowel-missing bucket, but it should never be presented as a viable OE alternative to `ċēowan` [Germanic/docs/DEV_NOTES.md:2622-2624].
- The January 2026 repair note is likewise partly diagnostic. Its statement that `OldEnglishEwLongDiphthong` “only sees single `{*w}`” records the problem as understood in that debugging session, but later DEV_NOTES material reframes the state of the grammar by saying that existing `*ww` inputs are already handled correctly and that the mechanism may differ from the initially sketched two-step account [Germanic/docs/DEV_NOTES.md:1770-1770; Germanic/docs/DEV_NOTES.md:16316-16317].
- No surviving DEV_NOTES passage argues for a `PROTO`/`PROTOFORM` split, a non-regular derivation class, or a different OE target. All later evidence instead points toward a solved regular row whose main documentary value is as a control case for `*ww` handling [Germanic/data/germanic-aligned-final.tsv:175-175; Germanic/docs/DEV_NOTES.md:16321-16324; Germanic/docs/DEV_NOTES.md:26623-26624].

## Open questions for later work

- If a future full lexeme report wants to narrate the repair more precisely, it may be worth checking the archived trace named in the long-vowel-missing bucket (`docs/debug_snapshots/oe_long_vowel_missing_traces_2026-01-02d.txt`) to see exactly where the pre-fix derivation still retained `-ww-` before the long-diphthong step [Germanic/docs/DEV_NOTES.md:2622-2624].
- If later OE rule work revisits `*ww` handling, cite the January diagnosis and the later verification together rather than choosing only one. The pair preserves both the bug signature and the current verified outcome, while also warning that the implementation pathway may not map neatly onto the first diagnostic gloss [Germanic/docs/DEV_NOTES.md:1770-1770; Germanic/docs/DEV_NOTES.md:16310-16317].
- For indexing purposes, this slice probably remains a `no-index` candidate unless the project decides to index short shared rule-fix notes. The surviving material is useful but thin, and most of it is shared rule-debugging rather than a rich row-specific philological dispute [Germanic/docs/lexeme_reports/coverage_audit.md:215-215; Germanic/docs/DEV_NOTES.md:1769-1773; Germanic/docs/DEV_NOTES.md:26619-26624].

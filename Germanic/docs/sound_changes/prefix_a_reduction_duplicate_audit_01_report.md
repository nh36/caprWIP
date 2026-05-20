# Prefix A Reduction duplicate audit 01 report

## Summary

- `OEPrefixAReduction` **was** applied twice in the live Old English cascade before this audit: once early in `EnglishProtoToOE` and once late after `OEPrefixIReduction`.
- The early and late applications used the **same rule definition**: `define OEPrefixAReduction [ {*a} -> {*ĕ} || .#. {*g} _ [EnglishStarConsonant | EnglishPalatalConsonant] EnglishStarVocalic ];`
- The late application changed **0** corpus forms in the current Old English lexical corpus (`380` rows). The early application changed **1** form (`believe / *galáubijaną`).
- Removing the late application changed **0** final corpus outputs. The current cascade and the no-late variant both yielded `373` matches and `7` mismatches against the expected Old English targets, with `0` changed rows, `0` newly failing rows, and `0` newly passing rows.
- Decision: **A. Late invocation is redundant and has been removed.**

## Source confirmation

- Shared rule definition in `Germanic/fsts/germanic.txt`:
  - `define OEPrefixAReduction [ {*a} -> {*ĕ} || .#. {*g} _ [EnglishStarConsonant | EnglishPalatalConsonant] EnglishStarVocalic ];`
- Early call in `Germanic/fsts/germanic.txt`:
  - inside `define EnglishProtoToOE (...)`
  - after `OEAwLongDiphthong`
  - before `OEInterStressRaising`
- Former late call in `Germanic/fsts/germanic.txt`:
  - inside `define EnglishProtoToOE (...)`
  - after `OEPrefixIReduction`
  - before `OEWeakTailReduction`
- Early sandbox checkpoint in `Germanic/fsts/old_english_sandbox.txt`:
  - `define SOEPrefixAReductionEarly SOEAwLongDiphthong`
  - `.o. OEPrefixAReduction;`
- Former late sandbox checkpoint in `Germanic/fsts/old_english_sandbox.txt`:
  - `define SOEPrefixAReductionLate SOEPrefixIReduction`
  - `.o. OEPrefixAReduction;`
- Current inventory treatment before removal:
  - `SC035` = `OE Prefix A Reduction Early`, active canonical historical entry.
  - `SC077` = `OE Prefix A Reduction Late`, previously classified as `duplicate_application`, `include_in_volume = no`, `is_reader_facing = no`, `canonical_change_id = SC035`.

## Late-stage effect test

The direct sandbox comparison used the built bins immediately before and after the late stage:

- before late stage: `backend/old_english_sandbox_after_oe_prefix_i_reduction.bin`
- after late stage: `backend/old_english_sandbox_after_oe_prefix_a_reduction_late.bin`

Results:

- total lexical items checked: **380**
- rows changed by late stage: **0**
- rows changed by early stage: **1**
- only early-stage change observed: `believe / *galáubijaną`, where the early stage converts `*galēabijaną` to `*gĕlēabijaną` and the late stage leaves the form unchanged

Detailed row-level output is recorded in:

- `Germanic/docs/sound_changes/order_tests/summaries/prefix_a_reduction_late_effect.tsv`

## No-late variant test

A temporary variant of both `germanic.txt` and `old_english_sandbox.txt` was compiled with the late `OEPrefixAReduction` invocation removed while preserving the early invocation.

Corpus-level comparison against the expected Old English targets:

- current cascade: **373** matches, **7** mismatches
- no-late variant: **373** matches, **7** mismatches
- rows whose final output changed: **0**
- newly failing rows: **0**
- newly passing rows: **0**

Detailed row-level output is recorded in:

- `Germanic/docs/sound_changes/order_tests/summaries/prefix_a_reduction_no_late_variant.tsv`

## Decision

**A. Late invocation is redundant and has been removed.**

The corpus-level evidence is clean in both directions:

1. the late stage is identity on the current corpus;
2. removing it changes no final outputs;
3. the early invocation still performs the only prefix-a-reduction work seen in the corpus.

Because the late application proved computationally redundant, it has been removed from the main FST and sandbox, and the sound-change inventory now keeps only `SC035` as the reader-facing prefix-a-reduction entry.

## Files changed

- `Germanic/fsts/germanic.txt` — removed the late `OEPrefixAReduction` composition from the live OE cascade and the mirrored helper chain.
- `Germanic/fsts/old_english.bin` — rebuilt after removing the redundant late prefix-a-reduction invocation.
- `Germanic/fsts/old_english_sandbox.txt` — removed the late sandbox checkpoint and rewired `OEWeakTailReduction` to follow `OEPrefixIReduction` directly.
- `Germanic/tools/oe_full_trace_report.py` — removed the obsolete `OEPrefixAReductionLate` stage from the tracked sandbox stage list.
- `backend/old_english.bin` — rebuilt backend-side OE bin used by the trace/mismatch tooling.
- `Germanic/docs/debug_snapshots/oe_full_trace_report.txt` — regenerated after the sandbox stage list changed.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt` — regenerated after the sandbox stage list changed.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md` — regenerated compact trace snapshot after the derivation-class trace update.
- `Germanic/docs/sound_changes/order_tests/summaries/prefix_a_reduction_late_effect.tsv` — added the direct before/after late-stage comparison.
- `Germanic/docs/sound_changes/order_tests/summaries/prefix_a_reduction_no_late_variant.tsv` — added the temporary no-late variant comparison.
- `Germanic/docs/sound_changes/sound_change_inventory.tsv` — removed `SC077` and updated `SC035` to note that duplicate audit 01 removed the redundant late application.
- `Germanic/docs/sound_changes/sound_change_aliases.tsv` — removed alias rows for the deleted active sandbox stage `SC077`.
- `Germanic/docs/sound_changes/sound_change_book_entry_plan.tsv` — kept a single reader-facing prefix-a-reduction entry (`SC035`) and updated its note to reflect duplicate audit 01.
- `Germanic/docs/sound_changes/prefix_a_reduction_duplicate_audit_01_report.md` — added this report.

## Follow-up

No further book-entry split is needed for prefix a-reduction. The sound-change volume should keep **one** reader-facing entry (`SC035` / `OE Prefix A Reduction`).

The remaining follow-up is routine synchronization:

1. keep the regenerated trace snapshots aligned with the updated sandbox stage list;
2. leave `sound_change_inventory_audit_02_report.md` as historical context and treat this duplicate-audit report as the superseding computational decision record for prefix a-reduction.

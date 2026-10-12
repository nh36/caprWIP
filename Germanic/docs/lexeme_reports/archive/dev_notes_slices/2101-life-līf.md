---
row_id: 2101
concept: life
counterpart: līf
proto: *lī́bą
protoform: *lḯbą
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

# DEV_NOTES material — 2101 life / līf

## Current row state

- Live TSV row `2101` currently targets OE `līf` and is marked `regular`. The row-level OE-facing derivational field uses `*lḯbą`, while the shared concept-level protoform field at the right edge remains `*lī́bą`; adjacent Dutch, English, and German cognate rows still show plain `*lībą`, so the OE row's `ḯ` is a project-internal encoding choice, not a different lexeme [Germanic/data/germanic-aligned-final.tsv:660-663].
- `old_english_wiktionary.tsv` independently maps English `life` to OE `līf`, so the target itself is not a replacement lemma or a paradigm-cell workaround [Germanic/data/old_english_wiktionary.tsv:163-163].
- `oe_known_problems.tsv` does not show this lexeme among the currently tracked OE exception buckets visible in the file header and active entries, so row 2101 is not presently being handled as a known-problem row [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still treats the row as uncovered routine material rather than as a packet/memo case: `2101 | life | līf | regular | no | - | - | - | none` [Germanic/docs/lexeme_reports/coverage_audit.md:293-293].
- The best current derivational snapshot is the published OE trace, which gives `PROTO: *lḯbą`, `EXPECTED: līf`, `OUTPUTS: līf`; the trace shows no Proto-West-Germanic or Northwest-Germanic innovation here and only the OE-side steps `OE Heavy Syllable Nasal Apocope: *lḯb` and `PGmc B Allophony: *lḯβ` before `Outcome: līf` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2822-2841].

## Development-note summary

No dedicated row-2101 DEV_NOTES block survives. The live row is regular, and the only securely attachable DEV_NOTES material is shared stressed-long-`ī` implementation history plus one general warning that names `*lībą` as a form that would have passed an older context restriction only “by accident” [Germanic/docs/DEV_NOTES.md:41908-41917]. Accordingly, this slice has to be conservative: current support is mostly **shared-background-only** rather than row-local philological argument, and the row-specific substance comes mainly from the live TSV plus the current published derivation trace [Germanic/data/germanic-aligned-final.tsv:660-663; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2822-2841].

What does survive is still useful. DEV_NOTES explains why the OE row now carries `*lḯbą` instead of older combining-acute `*lī́bą`: the project introduced a dedicated symbol for stressed long `*ī`, because combining-acute input was unreliable under `apply down`, and `ḯ` was adopted as the machine-safe single-codepoint notation [Germanic/docs/DEV_NOTES.md:41923-41939]. DEV_NOTES is explicit that “The diaeresis is purely notational. Semantically `*ḯ` = stressed long *ī,” and that the surface mapping `{*ḯ} -> ī` is correct because OE orthography does not distinguish the stressed-root tier from ordinary long `ī` [Germanic/docs/DEV_NOTES.md:41938-41957]. For row 2101, that is the main surviving project reason to preserve the distinction `PROTO *lī́bą` versus OE-facing `PROTOFORM *lḯbą` versus attested/target OE `līf`.

The other usable DEV_NOTES attachment is migration history. Row 2101 is named directly in Batch 1 of the stressed-long-`ī` TSV migration (`1998, 2047, 2101 | drīfan, grīpan, līf`), and the same section says those rows were rebuilt, probed, mismatch-checked, and committed, while branch-wide totals held steady through the migration phases [Germanic/docs/DEV_NOTES.md:42006-42027,42031-42051]. That is not row-specific philology, but it is current project evidence that `līf` was intentionally migrated into the `*ḯ` cohort and remained stable afterward.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-41908-41917

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — A. Why a tier and not a context restriction`
- Source line hint: `lines 41908-41917`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `stressed_long_i`; `in_stem_n_loss`; `row_named_as_example`; `shared_background_only`
- Recommended next use: `cite_if_explaining_why_2101_was_not_left_on_plain_*ī`
- Shared with rows: `1998`; `2047`; `2103`; `2105`; `2106`; `2153`; `2182`; `2188`; `2197`; `2257`; `2285`; `2286`; `2290`; `2296`

This is the one place where DEV_NOTES names the lexeme directly before the migration table. The fragment is **shared-background-only**, not a row-local etymology note, but it matters because it records why the old fix was rejected. DEV_NOTES says the relevant loss is stress-conditioned, not syllable-count-conditioned, and then adds the row-relevant warning: “Words like `*tīdiz` or `*lībą` happen to satisfy the V+C+ context by accident of having an inflectional ending; the principle is unrelated” [Germanic/docs/DEV_NOTES.md:41908-41917]. For row 2101, the practical force is narrow but real: older success of `*lībą` under a crude context restriction was not the linguistic justification for the row, so later writers should not treat the `life / līf` row as independent evidence for that abandoned conditioning rule.

### DEV_NOTES:line-41923-41957

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — B. Notation / C. Pipeline plumbing`
- Source line hint: `lines 41923-41957`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `notation_policy`; `proto_vs_protoform`; `surface_mapping`; `shared_background_only`
- Recommended next use: `cite_if_explaining_*lī́bą_vs_*lḯbą_vs_līf`
- Shared with rows: `1998`; `2047`; `2103`; `2105`; `2106`; `2153`; `2182`; `2188`; `2197`; `2257`; `2285`; `2286`; `2290`; `2296`

This is the controlling surviving fragment for the row's notation layers. DEV_NOTES records the failed and accepted encodings in direct sequence: combining-acute `ī́` “compiles, prints correctly via `print upper-words`, but `apply down ī́ → ???`,” whereas single-codepoint `ḯ` “works” and was therefore “**Adopted**” [Germanic/docs/DEV_NOTES.md:41925-41936]. The fragment then gives the sentence that should be preserved verbatim for row 2101: “The diaeresis is purely notational. Semantically `*ḯ` = stressed long *ī” [Germanic/docs/DEV_NOTES.md:41938-41939]. It immediately adds the OE-side consequence: `{*ḯ} -> ī` at surface level, because OE spelling does not mark the stressed-root/internal-tier distinction [Germanic/docs/DEV_NOTES.md:41948-41957]. For this row, support is again **shared-background-only**, but it is the main evidence explaining why live TSV `*lḯbą` and shared proto `*lī́bą` are compatible rather than contradictory.

### DEV_NOTES:line-42006-42027

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — E. TSV migration (Phase 4)`
- Source line hint: `lines 42006-42027`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `row_explicit`; `migration_history`; `stressed_long_i`; `shared_background_with_row_name`
- Recommended next use: `cite_if_documenting_current_row_history`
- Shared with rows: `1998`; `2047`

This fragment is the strongest surviving **row-explicit** DEV_NOTES attachment, even though it is still implementation history rather than a dedicated lexical analysis. DEV_NOTES inventories the OE rows with long `*ī`, says that fifteen stressed-root cases were migrated to `*ḯ`, and then names Batch 1 as `1998, 2047, 2101 | drīfan, grīpan, līf` [Germanic/docs/DEV_NOTES.md:42010-42022]. The row-specific substance is limited but useful: row 2101 was not left behind accidentally; it was part of the deliberately migrated stressed-long-`ī` cohort. Use this as **row-specific support for current encoding/history**, not as independent evidence for the noun's philology.

### DEV_NOTES:line-42031-42051

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — F. Verification`
- Source line hint: `lines 42031-42051`
- Fragment type: `diagnostic_project_history_for_lexeme`
- Status: `current`
- Issue tags: `verification`; `migration_regression_check`; `diagnostic`; `shared_background_only`
- Recommended next use: `use_as_supporting_history_only`
- Shared with rows: `all migrated *ḯ rows`

This verification block is **diagnostic**, not row-local. It does not name `līf` individually, but it is the shared evidence showing that the stressed-long-`ī` work was regression-checked: representative probes behaved as intended, and the mismatch totals stayed at `13` through Phase 4 batches 1–5 [Germanic/docs/DEV_NOTES.md:42031-42051]. For row 2101, the fragment should only be used to support the claim that the migration cohort remained stable; the actual row-level success claim still comes from the published derivation trace `PROTO: *lḯbą ... OUTPUTS: līf` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2822-2841].

## Superseded or diagnostic material

- No row-specific DEV_NOTES block survives for `life / līf`; generic concept-name hits elsewhere in DEV_NOTES are not automatically relevant. In particular, the later probe plan mentioning `*feorh* ('life' — back-umlauted but no final -u in attested form)` is about a different OE lexeme altogether and should not be imported into row 2101's note just because the English gloss is the same [Germanic/docs/DEV_NOTES.md:29210-29220].
- Current sandbox/export snapshots are useful only as **diagnostic history**. `old_english_sandbox_results_current.json` still shows pre-migration `proto: "*lībą"` with a bundle of outputs (`līf`, `līfu`, `līfuz`, `līfiz`), and the stage-by-stage export also keeps pre-migration `*lībą`, flags `first_failing_stage: "ProtoRhoticFronting"`, yet continues through to surface `lība` [Germanic/tmp/old_english_sandbox_results_current.json:1613-1622; Germanic/tmp/old_english_sandbox_results_with_stages.json:24293-24437]. Those files illuminate workflow history, but they are superseded by the published trace and live TSV row, which already use `*lḯbą` and end cleanly at `līf` [Germanic/data/germanic-aligned-final.tsv:662-662; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2822-2841].
- The older combining-acute spelling `*lī́bą` remains relevant, but only as shared comparative/proto notation and older project encoding. DEV_NOTES explicitly says the project moved away from combining-acute input because `apply down` handling was unreliable, not because the lexical analysis changed [Germanic/docs/DEV_NOTES.md:41925-41939]. Treat `*lī́bą` as preserved comparative/shared-background material, not as evidence that live row 2101 should be reverted off `*lḯbą`.

## Open questions for later work

- If a packet or memo is ever created for row 2101, decide whether its metadata should spell out more explicitly the three-way distinction between shared proto notation `*lī́bą`, live OE-facing input `*lḯbą`, and attested/target OE `līf`; that is the only substantial interpretive trap left by the surviving materials.
- Refresh or retire the stale sandbox/export snapshots if they are still meant to be consulted during slicing work, because row 2101 currently appears there under pre-migration `*lībą` with contradictory diagnostic metadata even though the published trace already gives the stable current result `*lḯbą -> līf` [Germanic/tmp/old_english_sandbox_results_current.json:1613-1622; Germanic/tmp/old_english_sandbox_results_with_stages.json:24293-24437; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2822-2841].
- If `dev_notes_slices` indexing is revisited later, decide whether row 2101 should remain a no-index regular slice. On present evidence, the row is well supported operationally but lacks a surviving lexeme-specific DEV_NOTES argument block of the kind that usually justifies stronger indexing [Germanic/docs/lexeme_reports/coverage_audit.md:293-293; Germanic/docs/DEV_NOTES.md:41908-42051].

---
row_id: 2146
concept: ox
counterpart: oxa
proto: *úxsô
protoform: *úxsô
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2146 ox / oxa

## Current row state

- CONCEPT: `ox` [Germanic/data/germanic-aligned-final.tsv:839]
- COUNTERPART: `oxa` [Germanic/data/germanic-aligned-final.tsv:839]
- PROTO: `*úxsô` [Germanic/data/germanic-aligned-final.tsv:839]
- PROTOFORM: `*úxsô` [Germanic/data/germanic-aligned-final.tsv:839]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:839]
- The live row currently keeps `PROTO` and `PROTOFORM` identical. That matters because the row does **not** preserve any separate paradigm-cell workaround or alternative OE-directed input; the same `*úxsô` is both the comparative label and the derivational input for the OE target `oxa` [Germanic/data/germanic-aligned-final.tsv:839].
- `oe_known_problems.tsv` currently has no row-local entry for `2146`, `*úxsô`, `*uxsô`, `ox`, or `oxa`; this row is not being tracked there as an unresolved exception or wontfix item [Germanic/data/oe_known_problems.tsv:1-8].
- Current published trace material agrees with the live TSV and shows that the row now passes cleanly: `PROTO: *úxsô`, `EXPECTED: oxa`, `OUTPUTS: oxa`, with explicit intermediate stages `NWGmc U Lowering: *óxsô`, `OE Unstressed Long Vowel Shortening: *óxsa`, `OE Xs Merge: *óXSa`, and surface `Outcome: oxa` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3528-3546].
- Coverage infrastructure currently shows no attached packet, memo, dossier, or other lexeme-report scaffold for this row beyond the slice being created here; the coverage audit lists row `2146` as `regular` with all linked-report fields empty (`-`) and issue status `none` [Germanic/docs/lexeme_reports/coverage_audit.md:321-321].
- Current DEV_NOTES authority status: no dedicated row-specific ox/oxa dossier survives. The securely relevant DEV_NOTES material consists of (i) a shared u-lowering bug cluster that explicitly names `*uxsô → uxa (expected oxa)` and (ii) a later `*xs` audit that explicitly lists row `2146 *úxsô → oxa` among forms where `*xs` is preserved rather than deleted [Germanic/docs/DEV_NOTES.md:2967-2973,39260-39276].

## Development-note summary

The current row is a regular row that now works, but the surviving DEV_NOTES material is still important because it preserves **which parts of the derivation were once at risk and which were never supposed to be exceptional**. The live TSV gives `PROTO = PROTOFORM = *úxsô` and OE target `oxa`, and the current published derivation trace confirms that the pipeline now reaches `oxa` without mismatch: first NWGmc u-lowering gives `*óxsô`, then OE unstressed long-vowel shortening gives `*óxsa`, then `OE Xs Merge` yields the orthographic `x` sequence seen in `oxa` [Germanic/data/germanic-aligned-final.tsv:839; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3528-3546]. In other words, the row's present state is not an unresolved exception and not a row that needs a special analogical input.

The first securely relevant DEV_NOTES fragment shows why the row once mattered. In the shared “Remaining root-level issues” section, DEV_NOTES explicitly lists `*uxsô → uxa (expected oxa)` under `A. u-lowering (u → o before back vowel)` and states that `NWGmcULowering should lower *u → *o before non-high vowels in a following syllable`, but certain forms with `*ô` suffixes were incorrectly retaining `u` [Germanic/docs/DEV_NOTES.md:2967-2973]. That note is crucial because it says the older bad output `uxa` was a **model bug**, not a philologically licensed OE exception. DEV_NOTES immediately contrasts this cluster with genuinely documented u-retention exceptions such as `bucc`, `fugol`, and `wulf`, and says that for forms like `buga/boga`, `fula/fola`, and by the same logic `uxa/oxa`, the lowered-vowel form is the one that should be expected [Germanic/docs/DEV_NOTES.md:2971-2973]. For row `2146`, this is the decisive row-policy point: `oxa` belongs with regular u-lowering, not with the wontfix exception set.

The second securely relevant DEV_NOTES fragment shows that the consonant side of the row should not be over-corrected while fixing the vowel side. Much later, in the audit of preconsonantal `*x` loss, DEV_NOTES groups row `2146 *úxsô → oxa` with the medial `*xs` rows and states that these forms are “mostly preserved as `x` orthographically, no loss” [Germanic/docs/DEV_NOTES.md:39260-39276]. It then says explicitly that these rows “do not require the loss rule” and that, per Campbell §416, `*xs` survives as `x (= ks)` when no further consonant follows; therefore the loss rule “should not fire here” [Germanic/docs/DEV_NOTES.md:39273-39276]. For this row that warning is concrete: the correct repair path is to ensure `*u > *o` before the following non-high vowel, **not** to delete the `x` cluster. The current trace matches exactly that interpretation, since it shows vowel lowering plus `Xs` merger, not `x` loss [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3540-3546].

Taken together, the surviving DEV_NOTES material supports a precise replacement working note even without a dedicated packet or memo. `PROTO` and `PROTOFORM` remain the same (`*úxsô`), the OE target remains `oxa`, the historically wrong state to remember is `uxa`, and the row's two governing phenomenon-level facts are: (1) it belongs to the regular `u > o` before non-high back-vowel environment, and (2) its medial `*xs` should survive into OE orthographic `x`, not be deleted by the separate preconsonantal `*x`-loss rule [Germanic/data/germanic-aligned-final.tsv:839; Germanic/docs/DEV_NOTES.md:2967-2973,39260-39276; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3528-3546].

## Relevant DEV_NOTES fragments

No securely attachable **dedicated current row-specific** DEV_NOTES dossier survives for row `2146`. The fragments below are nevertheless strong enough to replace casual consultation of `DEV_NOTES.md`, because both name the row's form directly and each fixes a different piece of the derivation.

### DEV_NOTES:line-2967-2973

- Source heading: `A. u-lowering (u → o before back vowel)`
- Source line or section hint: `lines 2967-2973`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `u_lowering`; `u_o_alternation`; `regular_not_exception`; `historical_bug_state`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the key DEV_NOTES fragment for the row because it names the exact bad and good outcomes: `*uxsô → uxa (expected oxa)` [Germanic/docs/DEV_NOTES.md:2969-2969]. DEV_NOTES then explains the mechanism in general terms but with direct consequences for this lexeme: `NWGmcULowering` should lower `*u → *o` before a following non-high vowel, yet these `*ô`-suffix forms were retaining `u` incorrectly [Germanic/docs/DEV_NOTES.md:2971-2971]. For row `2146`, that means the crucial contrast is not between two acceptable lexical variants; it is between a bug output (`uxa`) and the regular target (`oxa`).

The note is especially valuable because it prevents the row from being misclassified as a documented u-retention exception. DEV_NOTES immediately says that some u-retentions such as `bucc`, `fugol`, and `wulf` are real documented exceptions, but that forms like `buga/boga` and `fula/fola` are different because the lowered-vowel form is the expected one and the `u`-form is an FST error [Germanic/docs/DEV_NOTES.md:2973-2973]. The same diagnostic applies here. Later report prose should therefore treat `oxa` as the regular OE outcome of the row's `*úxsô` input, and preserve `uxa` only as the historical bad state recorded in DEV_NOTES.

### DEV_NOTES:line-39260-39276

- Source heading: `6. Corpus rows that depend on the current loss rule`
- Source line or section hint: `lines 39260-39276`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `xs_cluster`; `x_loss_guard`; `orthographic_x`; `regular_row`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2017,2031,2194,2275,2276`

This late audit is the best current DEV_NOTES safeguard against a different kind of over-repair. DEV_NOTES explicitly lists row `2146` under the medial `*xs` rows: `*úxsô → oxa` [Germanic/docs/DEV_NOTES.md:39265-39269]. It then says these rows are “mostly preserved as `x` orthographically, no loss” and that they “do not require the loss rule” [Germanic/docs/DEV_NOTES.md:39265-39276]. For this lexeme, that is not background trivia: it tells later editors that the row's `x` is the expected continuation of `*xs`, not something that should disappear during cleanup of `*x`-loss behaviour.

This fragment also dovetails neatly with the current published trace. The trace does not show any `x` deletion. Instead it shows `NWGmc U Lowering: *óxsô`, then `OE Unstressed Long Vowel Shortening: *óxsa`, then `OE Xs Merge: *óXSa`, ending at `oxa` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3540-3546]. That alignment matters because row `2146` has two moving parts in DEV_NOTES history: the vowel had once been wrong (`uxa`), but the `xs` cluster belongs to the preserved set. This fragment is therefore best cited alongside the u-lowering fragment so the row's repair history is not flattened into a one-dimensional “just make it oxa” statement.

## Superseded or diagnostic material

The only important superseded row history preserved in DEV_NOTES is the older mismatch state `*uxsô → uxa (expected oxa)` [Germanic/docs/DEV_NOTES.md:2969-2973]. That material remains worth keeping because it identifies the exact former failure mode and explicitly classifies it as a regular-rule bug rather than as an accepted OE exception. It should **not** be cited as if the row were still unresolved; the live TSV marks the row `regular`, and the current trace now outputs `oxa` correctly [Germanic/data/germanic-aligned-final.tsv:839; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3528-3546].

Just as important is what does **not** survive. There is no stale alternate protoform, no paradigm-cell retargeting proposal, and no `oe_known_problems.tsv` entry attached to this lexeme [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:321-321]. The main diagnostic risk is instead that a future sweep through `DEV_NOTES.md` could overgeneralize from the separate preconsonantal `*x`-loss discussion and accidentally treat `*úxsô` as a candidate for `x` deletion. The late `*xs` audit explicitly says not to do that [Germanic/docs/DEV_NOTES.md:39265-39276].

## Open questions for later work

- If a packet or memo is eventually created for this lexeme, keep the row-level story very narrow and explicit: `*úxsô` is both `PROTO` and `PROTOFORM`, `oxa` is the OE target, `uxa` is only the historical bad output, and the current trace already supplies the working derivation `*úxsô > *óxsô > *óxsa > oxa` [Germanic/data/germanic-aligned-final.tsv:839; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3528-3546].
- If later rule work revisits NWGmc u-lowering buckets, keep row `2146` with the genuine `vowel_quality__u_o_alternation`/regular-lowering material rather than with the accepted lexical u-retention exceptions such as `wulf`, `fugol`, or `wull` [Germanic/docs/DEV_NOTES.md:2967-2973,24579-24612].
- If later rule work revisits `NWGmcPreconsonantalXLoss`, re-check that row `2146` stays in the preserved `*xs` set and still reaches orthographic `x`; the current DEV_NOTES audit treats that as the correct behaviour, not as an unresolved edge case [Germanic/docs/DEV_NOTES.md:39260-39276].

---
row_id: 2190
concept: sing
counterpart: singan
proto: *síngwaną
protoform: *síngwaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2190 sing / singan

## Current row state

- The live OE row reads `CONCEPT = sing`, `COUNTERPART = singan`, `PROTO = *síngwaną`, `PROTOFORM = *síngwaną`, `DERIVATION_CLASS = regular`; the row currently has no OE `NOTE`, and its only listed source strings are duplicated `Wiktionary etymology (template:inh)` provenance rather than a row-specific project note [Germanic/data/germanic-aligned-final.tsv:1007-1007].
- `PROTO` and `PROTOFORM` are identical in the TSV, so the live row is not currently using a substitute stage-form, a paradigm-cell retarget, or an OE-facing proxy input. The stored derivational input is `*síngwaną`; the attested OE target is the infinitive `singan` [Germanic/data/germanic-aligned-final.tsv:1007-1007].
- `oe_known_problems.tsv` has no surviving entry for `*síngwaną`, `singan`, or row `2190`, so the lexeme is not being tracked as a live OE exception or known breakage case [Germanic/data/oe_known_problems.tsv:1-8].
- `coverage_audit.md` likewise treats row `2190` as a regular row with empty note and no required report coverage: `| 2190 | sing | singan | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:352-352].
- The current published derivation traces are exact matches. The compact report gives `PROTO: *síngwaną`, `EXPECTED: singan`, `OUTPUTS: singan`, with the active OE-side steps `OE Heavy Syllable Nasal Apocope`, `OE Secondary Nasalization`, `OE Post Velar W Loss`, and `OE Weak Tail Reduction` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4225-4244]. The full trace shows the same sequence in expanded form: `*síngwaną > *síngwan > *síngwąn > *síngąn > *síngan > singan` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28772-28885].
- Local reference files support the lexical identification without introducing a rival OE target. Ringe–Taylor give `PGmc *sing“ang ‘to sing’ ... > PWGmc *singwan ... > OE singan`; Kroonen lists `*singwan-` with `OE singan`; Clark Hall gives `singan³ ... to 'sing,' celebrate in song`; and Bright's strong-verb paradigm table lists `singan ... sang ... sungon ... sungen` [docs/references/ringe_taylor_linguistic_history_vol2.txt:12434-12435; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22648-22657; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:36529-36533; docs/references/bright_anglo_saxon_reader.txt:2449-2449].

## Development-note summary

This row does have genuinely attachable DEV_NOTES material, but it is narrower than a long corrective dossier like `fare / faran` or `sunder / sundrian`. The useful current authority is the March 2026 `*gw`-cluster note at `DEV_NOTES:line-3098-3110`. That material is enough to explain the live row and the current exact-match derivation, because it does two things explicitly: first, it says that `sing` really did inherit a labiovelar cluster (`"This genuinely had a PGmc labiovelar *g^w ..."`); second, it states the OE-side simplification rule in reusable form (`"Then per R/T §6.4.2, *w was lost after non-initial velars: *singwan → singan"`) [Germanic/docs/DEV_NOTES.md:3098-3098].

The row therefore needs a clear three-layer distinction. The live project input is `PROTO = PROTOFORM = *síngwaną`, written in the current stress-marking convention used by the TSV and the live trace [Germanic/data/germanic-aligned-final.tsv:1007-1007; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28772-28779]. DEV_NOTES writes the same lexeme once as `*singwăną`, which is best read as an older/internal diagnostic spelling of the same project-level form rather than as a different row policy: the note drops the acute on stressed `í` and marks the final short `a` with a breve, but it is still discussing the same inherited `singw-` verb that yields OE `singan` [Germanic/docs/DEV_NOTES.md:3089-3098]. Ringe–Taylor's `PGmc *sing... > PWGmc *singwan > OE singan` and Kroonen's dictionary headword `*singwan-` are then comparative/stage notations, not replacement TSV inputs [docs/references/ringe_taylor_linguistic_history_vol2.txt:12434-12435; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22648-22657]. Nothing in the surviving material suggests a split between `PROTO` and `PROTOFORM`, or any need to alter the attested OE target.

The live derivational behavior is regular and should be spelled out rather than merely labelled "matches." In the full trace, final `-ą` first loses its segmental nasal in `OEHeavySyllableNasalApocope`, then the remaining nasalization is represented in `OESecondaryNasalization`, so the word reaches `*síngwąn`; `OEPostVelarWLoss` then removes `w` after the non-initial velar, giving `*síngąn`; `OEWeakTailReduction` yields `*síngan`; orthographic cleanup produces `singan` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28834-28840,28865-28885]. That trace matters because DEV_NOTES' prose is not merely speculative literature summary: the exact rule named there is the rule now actively delivering the row's correct OE output in the published pipeline [Germanic/docs/DEV_NOTES.md:3098-3110; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4238-4244].

The most important negative point is that no evidence survives for a rival OE target. Unlike rows where DEV_NOTES preserves a wrong older counterpart, a paradigm-cell workaround, or an analogy-vs-sound-law dispute, row `2190` currently shows no such instability. The only stale material is the old mismatch snapshot where the system had not yet applied post-velar `w` loss and was outputting `singwan` instead of expected `singan` [Germanic/docs/DEV_NOTES.md:3086-3089]. That is useful project chronology, but it is not evidence against the current row. The current philological and implementation picture is unified: comparative sources point to inherited `*singwan-`, DEV_NOTES says `*singwan → singan`, and the live trace now returns exactly `singan` [Germanic/docs/DEV_NOTES.md:3098-3110; docs/references/ringe_taylor_linguistic_history_vol2.txt:12434-12435; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22653-22657; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28772-28885].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3086-3089

- Source heading: `The problem`
- Source line or section hint: `lines 3086-3089`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `old_mismatch_snapshot`; `pre_rule_fix`; `w_loss_missing`; `project_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2234`

This fragment preserves the only clearly stale row-local state that still matters: the project once listed `*singwăną → singwan (expected singan): cons_mismatch__w_vs_n` among unresolved `*gw`-cluster items [Germanic/docs/DEV_NOTES.md:3086-3089]. That line should be carried forward only as diagnostic history. It shows what the pre-fix failure looked like and why `sing` was grouped with other `*gw` cases, but it does not preserve an alternate lexical policy, alternate OE target, or alternate protoform. The row's present target was already `singan`; the problem was that the grammar had not yet implemented the rule that removes `w` after non-initial velars.

### DEV_NOTES:line-3098-3098

- Source heading: `Research`
- Source line or section hint: `line 3098`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `labiovelar_cluster`; `comparative_support`; `post_velar_w_loss`; `regular_derivation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling lexeme-specific DEV_NOTES statement. It says, in one compact line, that `sing` is not a false-positive `*gw` case but a genuine inherited labiovelar case: `"This genuinely had a PGmc labiovelar *g^w (Kroonen p.437, *singwan-; R/T p.215, *sing^wanan). After PWGmc labiovelar resolution (R/T §3.1.3), the cluster became *ngw. Then per R/T §6.4.2, *w was lost after non-initial velars: *singwan → singan."` [Germanic/docs/DEV_NOTES.md:3098-3098]. Later report prose can rely on this fragment directly because it already bundles the comparative reconstruction, the relevant stage distinction (`*g^w` > `*ngw`), and the OE-facing rule that yields the attested target. It is also current in the strongest possible practical sense: the same `w`-loss claim is now visibly borne out by the live trace's `OEPostVelarWLoss` step [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28834-28840].

### DEV_NOTES:line-3102-3110

- Source heading: `Analysis of *gw developments`
- Source line or section hint: `lines 3102-3110`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `rule_generalization`; `allophony`; `post_velar_w_loss`; `shared_sound_change_context`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `2234`

This shared follow-up explains why `sing` behaves differently from the neighboring `snow` and `swallow` cases in the same cluster. DEV_NOTES states that Ringe–Taylor §6.4.2 covers `"Loss of *w after non-initial velars"` and then distinguishes the outcomes by the allophony of `*g`: `"After nasal (*ngw): *g = stop [g], so *w is lost → *ng (singan, stincan)"`, while post-vocalic and post-liquid environments lose `g` instead [Germanic/docs/DEV_NOTES.md:3102-3110]. For row `2190`, this is background rather than row policy, but it is valuable background because it prevents later writers from flattening all `*gw` histories into one rule. `singan` is not another `snow`-type deletion of `g`; it is specifically the nasal-cluster subtype where `w` is lost and `ng` remains.

## Superseded or diagnostic material

The superseded material for this row is narrow and purely diagnostic. DEV_NOTES does **not** preserve an older claim that OE should be something other than `singan`; it preserves only the earlier engineering state where the cascade stalled at `singwan` before `OEPostVelarWLoss` was in place [Germanic/docs/DEV_NOTES.md:3086-3089]. The live trace now shows that rule firing exactly where DEV_NOTES predicted it would, so the stale state should be treated as implementation history rather than as a live lexical problem [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28834-28840].

The notation differences likewise should not be promoted into fake disagreement. `*síngwaną` in the TSV and trace, `*singwăną` in DEV_NOTES, `*singwan-` in Kroonen, and `*singwan` in Ringe–Taylor are different notation/stage presentations of the same lexeme, not evidence for competing row policies [Germanic/data/germanic-aligned-final.tsv:1007-1007; Germanic/docs/DEV_NOTES.md:3089-3098; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22648-22657; docs/references/ringe_taylor_linguistic_history_vol2.txt:12434-12435]. The only form here that is an attested OE row target is `singan`.

## Open questions for later work

- If `index.tsv` is updated later, the safest indexable core is the current lexeme-specific line `DEV_NOTES:line-3098-3098`; decide whether the broader `*gw`-analysis lines `3102-3110` should also be indexed as shared background or left only in the slice.
- If a later full report wants a short paradigm note, Bright's strong-verb table gives a compact attested series `singan / sang / sungon / sungen`, which could help keep the target identified explicitly as the infinitive rather than as an underspecified lemma string [docs/references/bright_anglo_saxon_reader.txt:2449-2449].
- If later cleanup normalizes source provenance for rows with empty notes, row `2190` would benefit from replacing duplicated Wiktionary source strings with a denser local-reference citation set, but no row correction is currently implied by that bookkeeping issue [Germanic/data/germanic-aligned-final.tsv:1007-1007].

# Working state: inherited-*r* adverb investigation

**Authority:** research-only work on `update`, based on `c92cbd9d541785986998ab2ab99a416f87da4f68`. The released SC015 rule, 387 selections, registries, baselines and book remain protected. No production adoption or corpus admission is authorized.

## Established

- Original dictionary scans corrected the earlier pagination and OCR errors. Kroonen PDF sheets 265/303/574 are printed pp. 225/263/534; Orel sheets 211/237/455 are pp. 172/198/416. Kroonen p. 225 prints unmarked OFris *hir*; Orel p. 172 prints *hīr* and *xē₂r*. These are dictionary citation forms, not independently inspected manuscript readings.
- The corrected 22-row, 13-column `WITNESSES.tsv` distinguishes attested OE targets, manuscript/editorial status, comparative citations, reconstructions, and experimental inputs. Gothic <ƕar, þar> and the conflicting Old Frisian dictionary spellings do not resolve the relevant quantity.
- Hill (2017:148) explicitly leaves both orders open: *hir > hīr > hẹ̄r* and *hir > hẹr > hẹ̄r*. The short-*i* antecedent is a morphological reconstruction, not a dictionary citation form; neither sequence is established by the attested OE output alone.
- The isolated driver completed all 21 recipes against 387 selected rows and 34 supplementary probes through 107 wrapper events in Foma `0.10.0alpha`. The receipt includes event traces, firings, outputs, rejections, ambiguities, and protected-file checks.
- Baseline: 387 unique selected outputs, 379 exact matches, and the same eight mismatches documented in `PROVENANCE.md`. Nineteen recipes preserve every selected final; two delayed technical-marker variants introduce only an additional row-2326 (*you*) mismatch.
- With Hill's short antecedent, the simple lengthening-before-short-*i*-lowering model gives *hīr*, while lowering-before-lengthening gives *hēr*. A separate long-*ī* lowering also yields *hēr*, so the experiment does not distinguish Hill's two stated orders if that extra rule is allowed. The *where/there* probes yield *hwǣr/þǣr* but do not constrain the *i* chronology.
- `XRLen` has no firings in the 387 selected rows; its effects are assessed through supplementary probes. No candidate changes any production file or selected output except the two named representation-stress cases.
- All 4,108 files in the original protected start manifest were rehashed: zero changed or missing. The completed receipt also reports `protected_unchanged=true`.

## Rejected or qualified interpretations

- Do not say Hill demonstrates that lowering must precede lengthening; his section 4 presents the opposite order as a live possibility.
- Do not conflate vowel quality with quantity: OE hē is long; OFris hīr is reported as likely long but unlowered, while unmarked <hir> spellings alone do not prove shortness; OE meord has e, not retained i.
- Do not infer history from the SC024 serialization. If newly lengthened e is encoded as `ḗ`, a computational collision with inherited ē₁ is a representation control, not a historical ordering result.
- Do not call *hēr* a direct witness to a short Proto-Germanic input. Hill's *hir* is a reconstruction; no canonical corpus input is justified by this experiment.
- The added long-*ī* lowering is a sensitivity recipe, not an adopted or independently established sound law. Its rule, domain, and chronology require separate evidence.
- Late placement cannot distinguish inherited from post-rhotacism *r* and overapplies to weak-final controls; successful adverb outputs alone cannot support a generalized late inherited-*r* rule.
- The rejected `xíar` probe is a wrapper limitation, not evidence against Kroonen's reported *hiar* account.
- The earlier `sc015-a-ablaut-investigation` receipts are pinned to a different source and remain historical; do not rerun or repin them.

## Completed assessment

- The source-verified witness distinctions, full-cascade results, intermediate divergences, representation failures, and conditional corpus consequence are adjudicated in `REPORT.md`.
- Recommendation: retain the protected baseline. Lowering-before-lengthening is the economical conditional analysis for Hill's short antecedent, but evidence does not choose it over Hill's long-*ī*-lowering alternative. Do not implement a rule or add a canonical row from this investigation alone.

## Current validation

- Full-cascade receipt status: complete; receipt hash and source pins are in `PROVENANCE.md`.
- Protected start manifest: 4,108 files rehashed, zero changed or missing.
- Remaining release steps: rerun the focused research tests after the final report edits, run `git diff --check`, inspect staged paths, and commit/push research artifacts only. Exclude the unrelated `Germanic/fsts/tmp_probe.foma`, Node OOM report, caches, and scratch directories.

# SC053 — postvelar labial loss and singleton medial labiovelars

## Identity

- **SC id:** SC053, existing postvelar labial loss.
- **Executable identifier:** `OEPostVelarWLoss`.
- **Date / branch / base:** 2026-11-28, `integration/sc083-lexical-medial-labiovelars`, `20a6bbbb3d8fb173ec6bbb930198e6c29da2661c`; package 2.

## Question

Was the labial of a West Germanic intervocalic dorsal–labial sequence lost before the dorsal, and does the evidence justify extending the existing SC053 operation to both singleton and geminate dorsals? A securely inherited medial singleton retaining *hw* in the same environment, or a proposed application to voiced, geminate or final controls, would defeat the narrow executable candidate.

## Current state (before any edits)

SC053 represents the loss of *w* after *ng* and executes after SC052, without a fricative branch. SC045 already implements palatal articulation for the fricative, SC085 removes a singleton between vowels under its own prosodic conditioning, and SC086 handles selected hiatuses afterward. The accepted compatibility corpus had 396 active entries, none selected to exhibit the new fricative environment. The original SC053 runner-boundary results are negative observations on that earlier domain, not an account of the broader historical process.

## Diagnosis

The pre-brightening exploratory rule and the later post-palatalization candidate distinguish the labial from the dorsal. In compatibility at the later slot, the independently established inputs of ‘see’ and ‘lend’ reach `*s*éo*x*w*ą*n` and `*l*īo*x*w*ą*n`: both lose only `*w`. The whole comparative prefixed filter infinitive reaches `*ᶠ*b*i*s*īo*x*w*ą*n` and loses only `*w`, with the prefix and foot marker preserved. This comparative infinitive is not the attested participle in *Christ* C 1086. A river accusative trajectory reaches `*ea*x*w*ǣ` and loses only the labial. The river direct form with syllabic *u* is not this positive input. The ‘near’ superlative has a source-backed history but the full PWGmc probe is rejected; it is not counted as a whole-word test.

The frozen local panel isolates the geminate: \emph{*sihhwā} retains both dorsals if the labial is separately removed, and SC085 does not delete the result. Initial ‘white’ and ‘turn’, the preconsonantal sequence in the ‘wheel’ structural control, a word-edge *hw* probe, the independently labiovelar-free ‘thrive’ and ‘arrange’ and the voiced filter alternant remain unchanged under the labial rule. The final dorsal of the securely attested filter command is also untouched. These are local or full retention witnesses as individually labelled, not interchangeable historical cells.

The replay preserves exact component traces and endpoints for the two protected populations (394 historical and 396 then-active rows) in each order and each candidate. Early composed networks agree with staged evaluation on those inputs and the seven diagnostic inputs; the restricted later exports agree on their nine whole-word diagnostics. In all three cascades, the later singleton and joint candidates agree on ‘see’ (*seohwan* → *seoan*), simplex ‘lend’ (*līohwan* → *līoan*), projected prefixed ‘filter’ (*besīohwan* → *besīoan*) and actual selected filter imperative (*sīoh* unchanged). The ‘near’ stage-local branch drops the labial before the retained vowel; its rejected full form is not evidence against that application. The earlier assembled runner receipts failed only in the reporting driver (`zip(strict=...)` on the container Python); the subsequent evaluation reused the compiled networks without recompilation.

## Literature

Ringe and Taylor (2014:48–50) distinguish Proto-Germanic unit labiovelars, their West Germanic resolution into sequences and the gemination of some dorsals by the following glide. Their §6.4.2 (214–215) groups the later English losses after noninitial dorsal consonants, including ‘sing’, ‘see’, ‘lend’, the river accusative and the ‘near’ stem. The hard geminate of *þicce* is evidence for retention of the labial during stop palatalization in that independent etymology. It is not a second geminate **fricative** witness. The broken-vowel histories and the one derived *seohhe* family are at pp.178–179, with separate accounting for the vulnerable singleton and the surviving geminate at pp.314–317. Campbell (1959:186–187 §§461, 464–465) independently distinguishes medial singleton dorsal loss from retention finally, in geminates and before a stressed vowel after an unstressed one. Seebold (1970:327–328, 387–390) documents the ablaut and voiced alternants. The published sources do not contain the executable clause or license a general contraction.

## Historical analysis

The English loss follows the inherited contrast between a labialized dorsal and its voiced alternant and the resolution of the voiceless unit into a sequence. Preserve the broader comparative observation of loss after noninitial dorsals, but add only the well-evidenced singleton intervocalic fricative fragment. The existing *ngw* environment is retained. The candidate permits both executable allophones of the voiceless fricative and has no lexical, morphological or stress exception. Initial and final position and adjacency to another consonant are outside this fragment; the latter does not assert universal historical preservation of every nonintervocalic labial. Final loss of rounding earlier in West Germanic, word-edge survival of the dorsal itself, and the behavior of voiced grades are distinct. Analogy is positively supported for the levelled dorsal in the ‘lend’ participle and the partly remodelled West Saxon strong paradigms (Ringe and Taylor 2014:344–345), not as an explanation of ordinary labial loss.

Order after SC052 is supported for the broader historical operation by the hard-geminate stop witness of Ringe and Taylor 2014:214; applying that source-led placement to the singleton fricative is a modelling choice compatible with the attested forms, not an independent relative date from those infinitives. Order before SC085 follows the independently reconstructed delabialized singleton dorsal in the ‘see’, ‘lend’ and ‘filter’ histories; the distinct conditions permit its later loss. Breaking before delabialization is possible in the implementation because it sees the dorsal already; the comparison with the exploratory slot does not establish a date for either from identical endpoints.

## Verdict

Registry-verdict: SC053=REFORMULATE

**Reformulate the existing postvelar law to implement its independently supported singleton fricative fragment.** Keep the existing stage position and its *ngw* reduction. Do not assign a second identifier: the literature groups the singleton history with the process already named SC053, and the one derived fricative geminate does not establish another independently dated sound change. Defer extending the executable fricative environment to geminates; preserve the positive local observation and historical geminate retention. Do not change SC045, SC052, SC085 or SC086.

## Propagation (only after verdict)

The source-owned definition is:

```foma
define OEPostVelarWLoss Ctx([
    {*w} -> 0 || {*n} {*g} _,
                EnglishStarVocalic [{*x}|{*ç}] _ EnglishStarVocalic
]);
```

There is a single replacement with two environments, not two replacement clauses sharing contexts. Foma `test equivalent` confirms that this definition denotes the same unbounded relation as the composed incumbent and singleton probe.

Authorize the separately researched simplex ‘see’ infinitive and the endingless ‘filter’ imperative through the exact two-row lexical expansion. Neither changes any pre-existing target, input or output. The former provides an active new positive; the latter is a final-dorsal nonapplication with a residual vowel mismatch. The same test follows this distinction in each model and retains ‘sing’ for the incumbent clause. The preceding ‘call’ expansion is protected separately. The numbered SC053 chapter, canonical corpus, source ledgers, lexical dossiers and both model projections are the publication owners.

The canonical compatibility result grows from 396 to 397 after ‘call’ and 399 after these two admissions, retaining 388 matches throughout. The mismatch counts are eight, nine and eleven respectively, with no rejected or ambiguous outputs. The two-row transition reproduces every one of the 397 before records and both original-380 protections. SC053's compatibility census changes from ‘sing’ alone to ‘sing’ and ‘see’; SC085 adds ‘see’ to its four earlier firings. SC083 still fires on the same eight weak-verb cells.

The [integrated expansion approval](../cascade_baseline/approved_sc053_sc083_integrated_expansion.json) checks the net three-row delta against the accepted 396-row Git base at finalization. It does not replace the sequential SC083 and SC053 approvals, their actual adoption receipts, or the two before snapshots.

The registry-to-reader crosswalk contains 88 active historical sound changes, of which 86 have individual published treatments in the 101-item numbered reader sequence. SC002 (PGmc *gm* simplification) and SC088 (OE epenthetic vowel) are publication omissions, not technical stages or justified exclusions; addressing them is outside this increment. Nonhistorical stages and spelling operations included elsewhere in that sequence do not inflate the historical coverage count.

The lexical class manifest now contains 187 articles, seven more than the baseline, including the three admissions and the existing infinitives of ‘bore’, ‘handle’, ‘lick’ and ‘make’. The remaining required-but-unassembled articles are ‘march’ (2120), ‘wound’ (2327), ‘sow’ (2328) and ‘betray’ (2329); the SC083 follow-up removes ‘handle’ (2055) from that list. See the [editorial population projection](../../lexeme_reports/pgmc_integration/population_summary.md) for the canonical live accounting.

Validation cost: `test_adoption_capture_is_bound_to_active_source_and_preserves_historical_controls` consumes the existing three-arm capture and the exact 396-row before reference. It checks full prior derivations and the extended rule's singleton and retention behavior; it adds no compiler call, variant, network, or runtime fixture. Active capture regeneration processes three additional row inputs per arm in the existing batched comparisons. Historical replay fixtures are unchanged.

## Residue

- ‘See’ and the projected infinitives retain uncontracted nuclei in the model; the final-vowel discrepancy in the filter imperative does not require either medial delabialization or dorsal deletion.
- Keep the explicitly prefixed ‘lend’ cells outside scoring pending an independently defensible full entry and compatible prefix admission. ‘Strainer’ has a reconstructed stage-local geminate, but lacks a currently accepted fully justified direct-cell submission. Publish neither as an active admission.
- Resolve the unusual *biseon* participle independently. Do not read it as an attested prefixed infinitive or impute the voiced grade of *āsiwen* to it.
- Retain the distinct stressed front-vowel issue for ‘call’ for later adjudication. This does not start SC086 or the early labial/nucleus packages.

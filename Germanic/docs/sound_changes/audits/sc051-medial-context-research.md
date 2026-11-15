# SC051: required medial context before testing the flask alternatives

## Identity

- **SC id:** SC051; bounded component research, not a completed
  adjudication of the whole palatalization complex.
- **Executable identifier:** `OESkPalatalization`; the name supplies
  neither historical stage nor phonetic dating.
- **Date / branch / base commit:** 14 November 2026,
  `research/flask-inherited-paradigm`; verified PR10 reference
  `77f314bf85035c23706b6b09b3a1855aa23c0620`. PR9 had merged into
  `update` as `85d3edc9b17e9eb9ca51831d5a1faf1df79faaeb`.
  The reference tree is identical to certified candidate `2805d98a`.
  The research merge is `ced7a6a36071aee2b52bb78e5ed829c978340b64`;
  its FST differs only by the already published restoration comment.

## Question

- **Hypothesis or suspected problem (falsifiable):** optional following
  context in the preceding-front-vowel clause wrongly palatalizes medial
  sk before back vowels. Requiring a following consonant or boundary
  should repair that failure without losing palatalization before
  non-high front vowels. Only then should following-clause timing and
  flask root retention/retraction be compared.
- **What evidence would confirm it; what would refute it:** paired
  fisċes/fiscas, disċes/discas, wasċe/wascan and þersċe/þerscan
  controls, initial/final controls and every selected raw input.
  A failed independent positive or unexplained corpus delta blocks
  recommendation; a better flask score alone does not establish a law.

## Current state (before any edits)

- **Existing historical characterization:** the registry describes
  SC051 as active, Old English, English-specific, confidence A,
  unadjudicated, with mixed chronology. That metadata is retained.
- **Existing executable behavior:** five serial clauses cover initial
  sk, a preceding front vowel, a following front vowel and adjacent j.
  The preceding-front clause ends in
  `EnglishStarFrontVowel _ (EnglishStarConsonant | .#.)`.
  Foma parentheses make that context optional. The following-vowel
  clause remains at the late SC051 position after final ā-fronting.
- **Selected-input assumptions:** all394 selected inputs use their
  current raw entry and context metadata. Row2016 remains
  `*fláskōn`, comparator flasce; row2141 remains `*márōn`, mære.
  The formation label supplies no evidence about flask's root vowel.
- **Existing verdicts/dossiers consulted:** SC051 component packet §11,
  its chronology card and reader; the final-nasal candidate, first
  flask research audit, SC046 restoration and clay/fringe records.

## Diagnosis

- **Complete firing census:** fresh canonical `SC051 --evidence`
  changes20/394 selected rows. The complete IDs/forms for identity
  and every variant are in
  [live_firings.tsv](sc051-medial-context-evidence/live_firings.tsv).
  They comprise fish, flask, flesh, shaft, shame, shear, sheath,
  sheep, shield, shilling, shine, shoulder, shove, shovel, show,
  shower, thrash, the two additional show cells and dart.
  Nineteen have the expected generalized-outcome environment;
  thrash is the following-back-vowel overgeneration exposed here.
  Initial applications do not individually date initial generalization.
  The archived380 snapshot is protected, not falsely reported as a
  newly executed historical replay.
- **Principal witness traces:** the complete raw corpus outputs and
  decisive histories are in
  [corpus_outputs.tsv](sc051-medial-context-evidence/corpus_outputs.tsv)
  and [stage_traces.tsv](sc051-medial-context-evidence/stage_traces.tsv).
  Every selected input traverses every named relation, beginning at
  the normal raw tokenizer; all intermediate outputs are singletons.
  Identity equals a fresh application of the canonical whole-cascade
  bin. Variant outputs are serial executions of compiled relations,
  not newly compiled whole-root bins.

| Variant | Matches /394 | Changed finals relative to PR10 |
|---|---|---|
| identity |385| none |
| required context alone |384|2253 þresċan → þrescan |
| guard + earlier following-vowel clause |384|2016 flæsċe → flæsce;2253 as above |
| guard + retention, original timing |384|2016 flæsċe → flasċe;2253 as above |
| guard + retraction, original timing |384|2016 flæsċe → flasċe;2253 as above |
| guard + earlier clause + retention |385|2016 flæsċe → flasce;2253 as above |
| guard + earlier clause + retraction |385|2016 flæsċe → flasce;2253 as above |

The guard alone changes exactly one final. The selected comparator for
row2253 explicitly contains dotted ċ; the new hard-cluster result
therefore counts as a new mismatch, not a silent normalization success.
Its live input before SC051 is `*θ*r*é*s*k*ą*n`: the back nasal vowel
must block the preceding-front clause. Campbell's hard-cluster
þerscan/þerxan supplies an independent phonological comparison; it
does not authorize silently replacing the corpus's selected metathesis
variant or its editorial consonant marking.

Relative to guard alone, moving only the following-vowel clause removes
flask's palatalization but leaves its root front: flæsce. Retaining or
retracting a with original timing instead gives flasċe. Combining the
two independent hypotheses gives flasce. Exact orders, including the
position of retraction after the early following-vowel clause in that
variant, are frozen in [orders.json](sc051-medial-context-evidence/orders.json).
The following-vowel clause sees back ā in either root experiment, so
that detail makes no difference to its application here.

All six guarded variants pass14/14 independent atomic consonant
controls. Identity passes11/14, failing fiscas, discas and the
structural þrescan environment. The controls include fixas as normalized
ks: SC051 preserves that cluster; it does not derive late sk-to-ks
metathesis. The paired wasċe and þersċe positives retain their
non-high-front trigger. Initial-front/initial-back and final-front/
final-back controls retain the existing generalized-outcome behavior.
These are explicitly normalized stage-entry consonant probes, not
complete authenticated Proto-Germanic inputs. Artificial suffix replays
and their later vowel changes are recorded separately and are not
substituted for the atomic consonant results.

Every other final is unchanged: mære, tunge, toe, wash and rest
remain intact. Every shared checkpoint in toe, tongue, nightmare and
the documented clay trace is identical to identity. Clay still retains
the fricative, loses it to create hiatus and contracts to þō; fringe
still has exact `*w*l*ō*x*u*m → *w*l*ō*u*m` at h-loss.

- **Witness role classification:** fisċes/disċes/wasċe/þersċe =
  positive conditioning controls; fiscas/discas/wascan/þerscan and
  the structural thrash environment = following-back negative controls;
  fish/flesh = selected medial/final applications; initial examples =
  generalized-outcome controls; flask = independent root/consonant
  experimental comparison, not a chronology proof; toe/clay/fringe =
  protected downstream sequence controls.

## Literature

- **Existing CAPR dossiers checked:** the SC051 packet and the first
  flask research/source ledger, with the sources preserved there.
- **Sources checked, with page numbers:** original Campbell1959
  pp177–178, §§440–441, and Ringe–Taylor2014 p204 were inspected.
  Campbell explicitly contrasts palatal medial sc before front
  vowels with retained sk, later often ks, before back vowels;
  wasċe/þersċe and fiscas/fixas/discas are not invented controls.
  Ringe–Taylor distinguish medial/final conditions, later initial
  generalization and subsequent sibilant realization.
  Wright1908 pp37–38 §57, Versloot pp122–124, Campbell p61 §158 and
  Luick pp152–153 §161 retain the qualifications established in the
  first flask audit.
- **Source-supported historical phenomenon:** following back vowels
  block medial palatalization; front-vowel positives include e.
  Written sc is ambiguous, whereas the contextual x spellings supply
  additional evidence for a hard/metathesized cluster. Neither dating
  [ʃ] from the marker nor moving every clause to one early event follows.
- **CAPR modelling decisions:** square brackets express required
  context in the proposed narrow syntax repair. The skā#-only
  retention/retraction and moving just the following-vowel clause
  before final ā-fronting remain independent experimental hypotheses.

## Historical analysis

- **Historical stage:** retain Old English; no new earlier node assigned.
- **Historical scope:** retain English-specific, without treating
  present executable positions as dates.
- **Regular phonological conditioning:** medial sk is protected before
  a back vowel; the proposed repair requires a consonant or boundary
  after sk when only a preceding front vowel licenses palatalization.
  No morphological-class or lexical-membership condition is introduced.
- **Counterexamples and falsification:** the first study's discas
  failure is now repaired, not carried forward as an objection to the
  guarded variants. The new row2253 delta must be disclosed.
  Earlier whole-rule movement harms wascan, broader st retraction
  harms ræste, and a high-front-only following trigger loses wasċe/
  þersċe. Those earlier negative results are preserved.
- **Positive evidence for analogy:** restored inflected stems provide
  possible donors, and Campbell/Luick explicitly propose root
  levelling. This is not proof against regular retention. The narrow
  skā# environment and its particular relative date still lack an
  independent discriminating witness; fixing the consonant context
  removes one blocker, not that evidential gap.
- **Relationship between phenomenon and proxy:** the required-context
  repair corrects an independently demonstrable medial overgeneration.
  The other four clauses still represent a composite generalized
  outcome, not a newly adjudicated single early phonetic event.
- **Chronology evidence:** no new historical edge. SC046/SC051 wash
  and SC051/SC056 initial evidence retain their qualified existing
  roles. The timing trial is model-local, not an
  `independently_demonstrated` chronology. SC073–SC085 remains
  `technical_computational` / `boundary_observation`; Corpus thoae
  remains conditional on the value of ae. Written h's exact phonetics
  remain open. Independent SC085 loss feeding SC086 contraction stands.

## Verdict

- **Verdict:** recommend RESTRICT only the preceding-front-vowel
  context for a separate production patch; DEFER the timing/root
  package and any new lexical cell/transponent. RETAIN production
  and protected baselines in this research publication.
- **Machine-readable line:** n/a: this is a bounded recommendation,
  not a new whole-SC registry adjudication. SC051 stays unadjudicated.
- **Justification:** the proposed one-line production diff is
  `(EnglishStarConsonant | .#.)` to
  `[EnglishStarConsonant | .#.]` in the preceding-front clause only.
  Independent controls support it; its single, fully explained corpus
  delta is scientifically acceptable, despite the lower literal score.
  A production adoption must explicitly review row2253's target/
  baseline consequence rather than conceal it. The two regular flask
  packages now pass the consonant controls, but fit alone still does
  not establish their narrow root condition or relative date.
  Prefer the regular account if evidence and economy tie; here the
  required independent conditioning/date evidence has not yet supplied
  that tie. Keep flasce as comparator and disclose the unresolved
  derivational mismatch instead of adopting a transponent.

## Propagation (only after verdict)

- **Affected files/registries:** this audit/evidence, SC051 reader and
  card qualifications, flask entry/ledger and subsequent Chapter3
  paradigm discussion. No production FST, order, selected TSV,
  chronology registry or baseline changes.
- **Regression tests added/updated:** no production behavior is adopted.
  The sealed driver asserts all selected singleton intermediates,
  reference whole-cascade equality, clay and fringe. Paired consonant
  controls and all394 raw outputs are published for every trial.
- **Baseline/fingerprint effect:** none on this branch. Current385/394
  and nine mismatches remain the protected production observation.
  The proposed guard-only change would give384/394, with only2253
  changing; the combined flask variants would exchange that match
  for2016, giving385/394. No rejection or ambiguity occurs.

## Residue

- **Unresolved uncertainty / deferred questions / author decisions:**
  review row2253 separately with its lexical/metathesis evidence before
  production migration; find an independent witness for the narrow
  flask environment/date; keep late sk-to-ks metathesis distinct.
  The next paradigm experiment is the attested genitive plural,
  with inherited masculine guma rather than originally neuter nama.
  SC044 and SC067 then SC080 remain queued.
- **Execution provenance:** [execution.json](sc051-medial-context-evidence/execution.json)
  records exact source/driver/recipe/log digests and the successful
  v2 snapshot. The preserved v1 monolithic seven-root compile timed
  out at the existing600-second limit and supplies no scientific
  result. It was not relabelled as a pass.

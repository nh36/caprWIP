# Flask: inherited cells and regular nominative alternatives

Follow-up, 14 November 2026: the
[guarded SC051 comparison](sc051-medial-context-research.md) repairs
the discas control and discloses the additional thrash delta.
The subsequent [genitive-plural investigation](flask-genitive-plural-research.md)
tests flascena/flaxena with inherited guma and exposes a quantity-carrier
syncope sensitivity. The original measurements below remain dated
observations, not silently updated scores or current unresolved controls.

## Identity

- **SC id:** cross-rule research on SC023, SC046, SC048, SC051, SC069
  and SC070; not a replacement adjudication of any one of them.
- **Executable identifier:** `PNWGmcNStemNLoss`, `OEARestoration`,
  `OESecondaryNasalization`, `OESkPalatalization`, `OEEarlyOShortening`,
  `OEUnstressedFrontingEarly`. Names do not establish historical stages.
- **Date / branch / base commit:** 13–14 November 2026;
  `research/flask-inherited-paradigm`;
  exact PR10 reference `2805d98ae5ecf7df33c65dc0caf7d9df2ed22077`.
  This candidate includes the corrected lexical integration baseline, with Model B's early
  final nasal-vowel merger retained, not archived pre-fronting inputs.

## Question

- **Hypothesis or suspected problem (falsifiable):** an independently
  inherited oblique/plural may provide an uninterrupted regular route
  to attested back-root *flascan*. Alternatively, a narrowly conditioned
  regular nominative may explain *flasce* without root analogy.
- **What evidence would confirm it; what would refute it:** require a
  contextual token, a justified complete input, the actual named-stage
  history, successful independent class controls, and a complete
  current-corpus delta. An isolated match after supplying a desired
  intermediate is insufficient. Shared-environment failures, a missing
  raw-entry route or independently unsupported conditioning block
  adoption even when the final matches.

## Current state (before any edits)

- **Existing historical characterization:** SC023's governing
  adjudication characterizes general old final-n loss as
  “(pre-)Proto-Germanic, not Northwest Germanic”; the citation-form
  implementation is only a proxy. SC046's restoration discussion treats
  the back vowel as a trigger, and the flask entry follows Campbell's
  and Luick's oblique-to-nominative levelling analysis. SC051 distinguishes
  medial front-vowel conditioning from the other cluster clauses.
  Registry stages and verdicts are unchanged by this research.
- **Existing executable behavior:** SC023 rewrites
  `{*ō} {*n} -> {*ǭ} || _ .#.` after early i-apocope and z-loss.
  The candidate merger removes final nasal bimoric rounding before
  ordinary fronting. The following-vowel medial clause in SC051 is
  `{*s} {*k} -> {*ʃ} || (EnglishStarConsonant | .#.) _ EnglishStarFrontVowel`;
  it currently runs after final ā-fronting. Foma parentheses here are
  optional context, not obligatory grouping. No production rule is
  changed in this branch.
- **Selected-input assumptions:** protect row2016's comparative
  `PROTO *flaskō`, selected `PROTOFORM *fláskōn`, comparator `flasce`
  and `early_analogy` formation label. That label concerns the
  comparative headword/weak-input relationship; it proves nothing
  about the history of the root vowel.
- **Existing verdicts/dossiers consulted:** SC023 adjudication and its
  secondary-n/dōn evidence; SC046 restoration and the March restoration
  memo; SC051 palatalization packet; the April flask memo, mature entry
  and source ledger; the final-vowel candidate and clay/fringe audits.
  SC023's authoritative `REFORMULATE/RETAIN` verdict is not reopened.

## Diagnosis

- **Complete firing census:** [live_firings.tsv](flask-inherited-paradigm-evidence/live_firings.tsv)
  records every changed selected row at the affected/diagnostic stages
  in every variant, not only flask. In the current394 reference, SC023
  changes17 rows, SC04620, SC04889 and SC05120; SC069 changes none.
  The SC023 rows are its ordinary citation-proxy domain, not new
  evidence for morphological conditioning. Secondary n in the newly
  reconstructed plural is outside the old-n-loss domain; its loss is
  an artifact of exposing a new input to the proxy. The other censuses
  are phonological applications within the selected inputs; their
  presence does not independently prove their historical ordering.
  The archived380 corpus was not separately re-executed in these
  experiments: its immutable fixtures remain protected, and this
  report does not relabel the394 run as a fresh historical380 replay.
- **Principal witness traces:** exact star-tokenized before/after
  states are in [stage_traces.tsv](flask-inherited-paradigm-evidence/stage_traces.tsv).
  The following readable forms suppress token separators only.

| Route | Decisive history | Result |
|---|---|---|
| Current selected nominative | *fláskōn → *fláskǭ → *fláskā → *flæskā → *flæskǣ; restoration has no back-vowel trigger; late sk palatalizes | flæsċe |
| Retain root a only before skā# | ordinary fronting variant gives *flaskā; following-front-vowel clause sees back ā; later ā → ǣ, but that clause is no longer present late | flasce |
| Front, then retract before skā# | *flæskā → *flaskā before following-vowel clause and final ā-fronting | flasce |
| Inherited nom.pl./gen.sg., after tokenizer | *fláskōniz → *fláskōnz → *fláskōn; current SC023 consumes secondary n, reproducing the citation route | flæsċe |
| Same, old n-loss before early i-apocope | secondary n survives; *flæskōn → *flaskōn at restoration; shortening occurs too late for nasalization | flascen |
| Same, also earlier shortening | restoration *flæskōn → *flaskōn; then *flaskan → *flaskąn; short nasal vowel does not front | flascan |
| Same, instead earlier general polysyllabic ōn-unrounding | *fláskōn → *fláskān; restoration and subsequent shortening/nasalization preserve back root and ending | flascan |

The explicit post-SC023 entry is before `EAFNasalSpirantLengthening`,
not an invented “just before restoration” shortcut. It still receives
ordinary fronting and all intervening stages. On the unchanged cascade
it gives *flæskōn → *flaskōn → flascen*. Earlier shortening is tested
after restoration/heavy nasal apocope and before secondary nasalization.
It is a general experiment, not a sound law conditioned on “weak plural”.

The inherited nominative plural was the first noncorpus raw probe.
`fláskōniz` is rejected by `EnglishProtoInput`, as are the complete
accusative-singular, dative-singular and dative-plural hypotheses.
Their separately labelled diagnostics enter before
`PGmcGmSimplification`, after tokenization; a diagnostic success must
not be called a successful normal-entry derivation.

| Complete reconstructed cell | Current post-tokenization output | Independent control / limit |
|---|---|---|
| nom.pl. and gen.sg. *fláskōniz | flæsċe | Early-n-loss alone gives flascen/tungen/ascen; either ending experiment gives flascan/tungan/ascan |
| acc.sg. *fláskōnų | flasconu | Earlier-shortening experiment gives flascn, not the desired attested oblique |
| dat.sg. *fláskōni | flæsċe | Earlier-shortening diagnostic gives flascan; still no raw-entry route |
| dat.pl. *fláskōmaz | flascem | Tongue gives tungem, not attested tungum; secure flask dat.pl. not found |

The class probes include tongue, ash and the separately labelled name
hypotheses. Name is originally neuter in Ringe's reconstruction, not
an inherited masculine control by fiat. `dōn` preserves its secondary
n in both general plural experiments. No inherited accusative-plural
`*fláskōnunz` run is claimed: the newly verified accusative-plural tokens
establish that cell's attestation, not an unexecuted derivation.

- **Witness role classification:** flask nominative = live fronting/
  palatalization application; inherited flask/tongue/ash plural =
  diagnostic feeding witness for restoration and ending chronology,
  with current secondary-n loss an out-of-domain proxy artifact;
  dōn = counterfeeding-negative; wash and rest = negative controls
  against overly broad movement/retraction; wasċe/þersċe = positive
  non-high-front conditioning controls; discas = retained-cluster
  negative currently failed by the preceding-front clause.

### Complete raw-input comparison

All394 selected inputs start at `EnglishProtoInput`. The two compiled
root matrices verify full-composition equality with every row's
stage-by-stage execution. The later shortening and precise-high trials
compose the same frozen stage relations including that tokenizer;
they are not falsely described as newly compiled whole-root FSTs.
Every accepted row has one usable output; no variant introduces a
rejection or ambiguity.

| Variant | Matches /394 | Exact changed finals relative to reference |
|---|---|---|
| identity |385| none |
| retain a + following-vowel-only early clause |386|2016 flæsċe → flasce |
| front then retract + same split |386|2016 flæsċe → flasce |
| move entire sk rule early (negative) |385|2016 resolves;2272 wascan → wæsċan |
| extend retraction to st (negative) |385|2016 resolves;2152 ræste → raste |
| restrict both medial trigger classes to high front vowels (negative) |385|2016 resolves;2253 þresċan → þrescan |
| restrict only following-vowel trigger to high front vowels |386|2016 resolves, but structural wasċe/þersċe controls fail |
| old n-loss before early i-apocope |385| none |
| same + early polysyllabic ōn-unrounding |385| none |
| same + shortening before secondary nasalization |385| none |

[corpus_outputs.tsv](flask-inherited-paradigm-evidence/corpus_outputs.tsv)
lists every output and comparator, including all unresolved mismatches.
Both promising nominative variants leave the other393 finals identical,
including mære. This independently reproduces386/394 from raw inputs,
not the earlier archived pre-fronting replay.

Structural `*waske`, `*θerske`, `*diskes`, `*diskas` are labelled stage
probes, not certified complete PGmc verb/noun inputs. Retain/retract
give wasċe, þersċe and disċes, but also disċes for discas. The actual
atomic consonant failure is `*diskas → *diʃas` at the late
preceding-front clause; the artificial complete discas probe additionally
fronts its ending later. These are distinct observations. The precise
following-high-only trial preserves disċes but gives wasce/þersce;
the stronger both-context restriction must not be substituted for it.
Raw verb guesses `wāskō/ô` and `þérskō/ô` do not establish the cited
first-singular histories.

Toe and clay have identical intermediate histories in retain/retract
and reference. Toe has *tāxǭ → *tāxā → *tāxǣ → *tāçǣ* and later
*tāçe → *tāe → *tā → tā*. Clay enters before
`PGmcNasalLossBeforeX` and passes through
*θōxā → *θōxǣ → *θōçǣ → *θōçe → *θōe → *θō → þō*.
Thus live clay already contains palatal [ç], confirming why its
regression tests the sequence rather than requiring [x].
Every variant preserves fringe's exact `*w*l*ō*x*u*m → *w*l*ō*u*m`
at `OEHLoss`.

## Literature

- **Existing CAPR dossiers checked:** those listed under Current state,
  including the SC073–SC085 technical-boundary and independent
  SC085–SC086 feeding discussions. No chronology-card interpretation
  is promoted from output fit.
- **Sources checked, with page numbers:** original pages and identities
  are itemized in the updated
  [flask source ledger](../../lexeme_reports/model_entries/2016-flask-flasce.source_ledger.md).
  They include Hecht66,141–142; Goodwin64; Wright–Wülcker97,109,123,240,411;
  Ringe312–313; Ringe–Taylor117–118,163–164,192;
  Fulk88–90,171–172; Hogg64–65,93–95,298–299;
  Campbell61,177–178; Luick152–153; Wright and Wright37–38;
  Versloot122–124. Wright1908 is the authenticated first edition,
  not the excluded/misattributed Wright1925 holding.
- **Source-supported historical phenomenon:** weak paradigms and their
  cross-language ending contrasts, contextual flascan/flaxan and
  flascena/flaxena, the sources' levelling analysis, retention/restoration
  alternatives, and medial palatalization before non-high front vowels.
  [attestations.tsv](flask-inherited-paradigm-evidence/attestations.tsv)
  distinguishes each manuscript/recension and grammatical construction.
  Hecht's genitives are plural, not singular; Guthlac and the Colloquy
  supply contextual accusative plurals. The col.411 italic Latin
  Flasce is excluded. No secure genitive singular or dative plural
  was established.
- **CAPR modelling decisions:** root-accent placement in the test forms,
  explicit star tokenization after raw rejection, the skā#-only condition,
  splitting the five-clause rule, and the exact positions of the two
  experimental ending repairs are hypotheses, not quotations from a
  source. The raw acute-to-plain-a retention rewrite matches the
  incumbent fronting representation; it asserts no new deaccenting law.

DOE Corpus access failed (including a separate20-second timed request);
this is not an exhaustive DOE negative search. Public dictionary and
compound searches supplied no secure dat.pl./gen.sg. The Mark14:13
wæterflaxan quotation is explicitly secondary compound corroboration,
not a newly verified bare-noun manuscript token. Manuscript copying
dates do not date the phonological processes.

## Historical analysis

- **Historical stage:** old final-n loss precedes the secondary
  apocope-created n historically. The northern ending developments and
  root fronting/restoration must be reconstructed independently;
  neither the PNWGmc prefix nor an executable slot assigns their stage.
- **Historical scope:** compare the common inherited paradigm with
  northern OE/OF redistribution versus OS/OHG contrasts. The comparative
  evidence constrains the reconstruction, but no non-OE production
  pipeline is researched or changed.
- **Regular phonological conditioning:** following back vowels,
  nasal closure, quantity, independently reconstructed stress, and
  consonantal/front-vowel contexts; never “because feminine” or
  “because flask”. Wright and Wright's broader sk/st/consonant account
  and Versloot's restricted-fronting model do not independently justify
  the experimental skā# restriction.

| Rival / cells | Input and expected result | Analogical step | Distinguishing evidence |
|---|---|---|---|
| Ringe–Taylor raising alternative | inherited oblique/plural *-ōn → *-ūn; relic accusatives foldu/eorðu/galgu retain u | masculine -an spreads into feminine | Earlier unreplaced nasal endings and independently datable redistribution |
| Their earlier masculine replacement alternative | same raising; masculine *-ini replaced by *-ani earlier | subsequent cross-class generalization | Early masculine genitive/dative forms separating ini/ani histories |
| Their regular northern -an alternative | inherited *-ōn → -an | feminine ending spreads to other genders | Secure pre-levelling feminine forms plus general phonological quantity/nasal chronology |
| Fulk/Hogg raising-oriented accounts | accusatives from forms such as *tungōnu; dat.pl. *tungōm → tungum | -an distribution not a direct reading of every inherited cell | Northern u relics and dat.pl. forms constrain raising; no flascum token yet |
| Campbell/Luick root levelling | front-root nominative, restored back-root flascan/ascan | oblique/plural root generalized to nominative | Evidence that excludes a general regular retention/retraction account |
| Regular nominative retention or early retraction | *fláskōn, early final merger, skā# condition and following-vowel-only earlier clause → flasce | none for root vowel | Independent skā# witness/order; wascan/ræste and non-high-front controls must also work |

- **Counterexamples and falsification:** moving all sk clauses harms
  wascan; adding st harms ræste; high-only following conditioning
  loses wasċe/þersċe despite passing the selected corpus. Disc-as
  retention remains a preceding-front-clause problem in all relevant
  proposals. The earlier-shortening plural success fails the acc.sg.
  and does not repair dat.pl. tungum. A second matched flask form
  cannot erase these disagreements.
- **Positive evidence for analogy:** Campbell and Luick explicitly
  analyze root levelling, and an oblique donor is available; this is
  an argued account, not independently decisive proof. The April
  formation label adds no evidence. If an independently supported
  regular account is equally economical and fits equally well, prefer
  it. The present narrow implementation lacks that independent support;
  output superiority alone cannot supply it.
- **Relationship between historical phenomenon and executable proxy:**
  SC023 is narrower than general old-n loss but overapplies when a
  secondary-n input is newly admitted at the current late slot.
  Moving the proxy earlier tests the distinction, not a discovery that
  inherited plural n historically disappeared. The surviving ending
  problem is separate from successful root restoration.
- **Chronology evidence:** old-n loss before secondary n is
  `independently_demonstrated` by the historical secondary-n/dōn argument,
  not by this new flask output alone; the executable test corroborates
  the predicted contrast. Earlier shortening before nasalization and
  the proposed sk split are model-local experimental orders, neither
  new `stage_entailed` nor `independently_demonstrated` edges. SC073–SC085
  stays `technical_computational` / `boundary_observation`; Corpus
  thoae supports loss before merger only if ae represents distinct
  unstressed æ. Written h marks a written distinction with its phonetics
  open. Independently supported SC085 loss feeding SC086 contraction
  remains separate.

## Verdict

- **Verdict:** DEFER adoption of either general repair or nominative
  variant; RETAIN production, row2016 and protected baselines.
- **Machine-readable line:** n/a: this is a cross-rule research decision,
  not a new registry adjudication. SC023's existing
  `Registry-verdict: SC023=REFORMULATE/RETAIN` remains authoritative.
- **Justification:** the inherited nominative plural is genuinely
  promising: two general diagnostic ending histories yield flascan,
  tungan and ascan without root analogy and leave the394 selected
  outputs unchanged. Both nominative variants independently reproduce
  the386 score from raw inputs, but their narrow condition/order lacks
  an independent witness and does not settle the discas control.
  Raw admission, the full inherited ending paradigm and independent
  chronology remain blockers. No historically justified transponent
  is selected.

## Propagation (only after verdict)

- **Affected files/registries:** mature flask entry and ledger; Chapter3
  immediately after early apocope; SC023/046/048/051/069/070 cross-references;
  dated qualifications to the April flask and March restoration memos;
  inaccurate live restoration comment; bibliography; this audit and
  frozen evidence. Existing discussion of earlier literature is
  preserved. No registry, rule semantics, rule order or lexical
  selection changes.
- **Regression tests added/updated:** none in production: no new behavior
  is adopted. Reproducible research drivers retain positive/negative
  controls, single-output checks, all394 comparison and class controls.
  Existing clay/fringe and lexical publication regressions cover the
  retained production behavior.
- **Baseline/fingerprint effect:** expected none. Reference394:
 385 matches, nine mismatches; row2016 remains flæsċe versus flasce.
  The proposed lexical alternative, explicitly NOT adopted, is
  `PROTOFORM *fláskōniz`, `COUNTERPART flascan` (nominative plural),
  with comparative PROTO/headword preserved. It requires raw admission
  and a source-supported ending history first; it is not permission
  to refreeze the baseline.

## Residue

- **Unresolved uncertainty / deferred questions / author decisions
  required:** obtain DOE access and secure dat.pl./gen.sg./early dialect
  evidence; discriminate the northern ending histories with the full
  paradigm, not only flascan; establish an independent narrow sk
  environment/order or abandon that restriction; handle the existing
  discas preceding-front failure separately. No production adoption is
  recommended on the present evidence. SC044 and SC067 → SC080 stay
  queued.
- **Execution provenance:** sealed experiment identities, timestamps,
  source/driver/log digests and authentic successful command statuses
  are in [executions.json](flask-inherited-paradigm-evidence/executions.json).
  Initial empty-batch and front-control setup failures are not counted
  as successes. Two scientific runs sealed successfully before their
  host terminal-print code tried a relocated staging log and exited1;
  their successful Foma receipts and outputs are preserved unchanged.
  Exported reproduction drivers move that terminal read before sealing;
  the scientific worker/recipes are unchanged. See the evidence README
  for exact replay commands and the distinction between scientific
  assay results and later publication certification.

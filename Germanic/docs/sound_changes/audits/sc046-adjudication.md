# SC046 adjudication: Old English a-restoration

## Identity

- SC id: SC046.
- Executable identifier: `OEARestoration`.
- Date / branch / base: 2026-11-16--17; `research/sc046-a-restoration`;
  current `update` at start was
  `aea30b033f911d7417f8e38f87b02c9b35cbcda9`.
- Scientific reference: that unchanged SC044-certified executable source
  (`germanic.txt` SHA-256
  `74d13549dfce23dca7690d2b095ee0bbf6b550faf5816241c823343035de7c5b`).
  No SC044 work is reopened.

## Question

Can the cited evidence require fronting followed by retraction rather
than blocked fronting, and does it license the executable target,
trigger and consonant classes across dialects? A specifically falsifiable
implementation question is whether unstressed compound linkers are
incorrectly retracted and whether restricting the target preserves their
regular histories through syncope. A universal no-geminate restriction
must survive independent *crabba/racca* positives, not merely improve
the corpus's *tæppa*.

The preregistration is
`literature_dossiers/sc046-a-restoration/04-source-assessment.md`;
immutable trial plans retain its predictions, including the prediction
refuted by the initial three-slot order experiment.

## Current state (before any edits)

The registry characterized the phenomenon as Old English, `oe`,
`english_specific`, confidence A, unadjudicated. These labels did not
establish a single synchronous chronology for every Old English dialect.
The executable receives fronted vowels after breaking and fricative
palatalization, before SC047 final nasal-vowel apocope and SC048 coda
nasalization.

Its target is any plain `*æ` accepted by `FootCtx`, not just a stressed
vowel. Its right environment is a singleton, geminate, arbitrary *sC*
or *fC*, followed by `EnglishStarBackVowel`, trimoric `*ô`, or `*ǭ`,
minus the separately encoded weak-tail class. The opening FST comment
correctly cites stressed targets, but the later “FULL (stressed)”
trigger comment conflates target stress with following-vowel status.
Those are separate historical questions.

The selected *bake/wade* inputs encode full *-aną*, *bast* a nasal
final tail, *flascan* the inherited weak feminine nominative plural
`*fláskōniz`, and *mære* the weak feminine nominative
`*márōn`, whose ending has changed before restoration. These are
selected histories, not recoveries of endings from their desired outputs.
*Tæppa*'s older corpus annotation asserts analogy; the source review
does not independently demonstrate that assertion.

Consulted existing records: the post-brightening book dossier and
SC046 chronology card, SC041 bleeding adjudication, SC042/SC069 ending
decisions, the Fulk1998, Seiler2019 and distinct Versloot source cards.
Original experiments, selected cells, protected baselines and scientific
FST bytes are preserved.

## Diagnosis

### Complete firing census

`adjudicate.py SC046 --prepare` and `SC046 --evidence` were executed.
The latter rebuilt production/cumulative bins, checked their freshness
and proved 394-row production/sandbox equivalence. There are 21 live
firings. Twenty concepts belong to the protected legacy380 inventory;
*earthly* is the additional firing. This is classification of current
selected inputs, not a replay of archived legacy cells.

| Rows / lexemes | Environment and classification |
|---|---|
| 1934 *bake*, 2003 *fare*, 2046 *grave*, 2059 *haw*, 2060 *hawk*, 2088 *lade*, 2117 *make*, 2132 *nave*, 2133 *navel*, 2165 *sake*, 2205 *spare*, 2266 *wade*, 2268 *wake*, 2309 *make* imperative, 2310 *make* 3sg | Fifteen stressed-root singleton applications: in the ordinary handbook restoration domain under the adopted input histories. The *hawk* match does not explain the separate Épinal *hebuc* spelling. |
| 2016 *flask*, 2272 *wash* | Two *sk* applications: source-supported cluster type; *flask*'s selected ending is essential. |
| 2090 *lap* | Geminate *pp*, positive *lappa* history, while *læppa* is a documented comparison; the complete prehistoric distribution remains qualified. |
| 2240 *tap* | Geminate *pp*, unresolved negative: produces *tappa*, not selected *tæppa*. No newly demonstrated analogy licenses dismissing it. |
| 2148 *rainbow*, 2336 *earthly* | Two unstressed linker applications: out of the stressed-target domain of the proposed history. Not historical restoration witnesses. |

Thus 18 firings are ordinary positives under the adopted histories,
one is an unresolved geminate counterexample, and two are
out-of-domain target applications. There are no live *fC* firings
proving that entire class and no *Cr/Cl* firing population proving a
general extension. Absence of such firings is not historical evidence
against those environments.

### Witness traces and interventions

The exact machine records preserve every row and output set, the actual
finite compiler appendix, source/helper hashes and measured process
costs. Named raw-input stages and endpoints come from manifest-validated
cumulative/production bins, not recompiled prefixes.

| Witness | Immediately before and after current SC046 | Role |
|---|---|---|
| *bake* | `*b*æ*k*a*n*ą` → `*b*a*k*a*n*ą` | Positive oral-trigger application. |
| *bast* | `*b*æ*s*t*ą` unchanged | Nasal weak-tail negative, despite *sC*. |
| *day/craft* | `*d*æ*g`, `*k*r*æ*f*t` unchanged | SC041 has removed their triggers; reuse its independently recorded bleeding comparison, not another corpus displacement sweep. |
| *flascan* | `*f*l*æ*s*k*ō*n` → `*f*l*a*s*k*ō*n` | Protected oral *ōn* positive. |
| *mære* | `*m*æ*r*ǣ` unchanged | No back trigger survives in this selected nominative. |
| *tæppa* | `*t*æ*p*p*ô` → `*t*a*p*p*ô` | Unresolved geminate negative. |

The no-geminate alternative corrects *tappa* to *tæppa* but changes
*lappa* to *læppa*. It also leaves `*kræbbô` and `*rækkô` front,
contrary to source-backed *crabba/racca*. These two added strings are
declared pre-SC046 schemata, not certified new corpus cells or
attestations. Ringe--Taylor p.192 and independently Orel s.vv.
`*krabbōn`, `*rakkōn II` back the geminate/weak-stem positives.
The 394-row score remains 386 only by trading one match for another.

The stressed-target alternative retracts only first-root plain *æ*
(respecting the current foot representation) and explicitly
secondary-stressed *ǽ*. It leaves the two linker vowels front.
On the declared secondary schema `*g*e*b*ǽ*k*ō`, it produces
`*g*e*b*à*k*ō`; this is a prosodic component control, not a claimed
attested lexeme.

*Earthly* then converges through ordinary nonhigh syncope:
`*éo*r*θ*æ*k*ù*n*d*ǣ` → `*éo*r*θ*k*ù*n*d*ǣ` →
*eorþcunde*. Its present back-linker intermediate is therefore
unnecessary to the endpoint, not evidence that the linker was stressed.

*Rainbow* does not converge. The unretracted linker survives to
`*r*é*ʝ*n*ea*b*o*g*ô` at nonhigh syncope, and the endpoint is
*reġneafoga*, not *reġnboga*. This exposes a downstream interaction,
not a reason to reinterpret the linker as stressed.

The initial ordering prediction was refuted when the outer slots alone
were exchanged with SC047 in the middle:
46/47/48 gives `*bakąn`, `*wadąn`, but 48/47/46 gives
`*bakan`, `*wadan`, with endpoints *bacen, waden*. SC048 has run
before SC047 exposes its word-final coda; SC046 still sees an oral
trigger and retracts the root. This is an ending-protection failure,
not by itself a root-vowel order proof.

The preregistered follow-up fixes SC047 before both competing operations,
at the shared independently staged `*bækan`, `*wædan` checkpoint.
47/46/48 gives `*bakąn`, `*wadąn`, while 47/48/46 gives
`*bækąn`, `*wædąn`; the latter remainder yields *bæcan, wædan*.
This isolates the root-vowel dependency once SC047's exposure is held
constant. It establishes how this trigger implementation behaves, not
an independently sourced universal order for restoration and
nasalization.

The second follow-up comparison locates rainbow's divergence exactly.
Before SC059 `OEBackMutation`, the candidate gives
`*r*é*ʝ*n*æ*b*o*g*ô`; immediately after it gives
`*r*é*ʝ*n*ea*b*o*g*ô`. The current back-mutation operation therefore
diphthongizes the unstressed linker before the labial plus back vowel.
SC114 nonhigh syncope deletes plain *a/æ/e*, not *ea*, and the
surviving vowel also changes the environment of subsequent
b-allophony. *Earthly* lacks that labial context and loses its plain
*æ* normally. No change to SC059, syncope, the selected compounds,
or their stress is smuggled into this SC046 proposal.

## Literature

The four new SC046 source records separate the Dresher intake,
Versloot's actual 2021 critique, glossary collation, and source
assessment. They are the detailed literature/witness tables for this
memorandum; their explicit gaps are part of the decision.

- Dresher (1985), printed 205--217 and 229--244 first, then 218--228
  and 245--252: restoration loss can expose front underlying vowels
  in Mercian while independent consonantal retraction preserves
  *hwalas/ald*. The decisive argument uses distributions of
  *a/æ/ea*, nonalternating *habuc/gabul/sadol*, and differing
  chronology of back mutation in Épinal and Corpus. It is an
  ordered-grammar/representation account, not direct attestation of
  every early fronted vowel.
- Campbell §§157--159, Hogg §§5.35--38 and Ringe--Taylor §6.3.1,
  pp.189--196 support the working southern restoration account,
  but differ in breadth, exceptions and use of levelling. Hogg
  permits blocked fronting before Anglian dark *l*. Following-vowel
  history, not its late spelling, supplies the trigger.
- *Slēan* supports earlier fronting if its diphthong is from
  breaking; the extension to *dagum* is then a phonetic-regularity
  inference. Versloot2021Review:93--95 offers *x*-loss plus
  contraction as an alternative source of the diphthong. That
  alternative still fronts *slæhan* and does not prove blocked
  fronting in *dagum*.
- Hogg's Northumbrian *slāa* allows restoration before breaking;
  Fulk1998:150--151 makes that inference conditional. It does not
  override southern chronology. Analogy competes where there is
  positive paradigmatic evidence, not merely resemblance.
- The *spadan/hebuc/fristmearc* collation preserves exact Épinal,
  Erfurt and Corpus spellings, independently sourced stem/ending
  evidence, manuscript image hashes and both predictions. *Spadan*
  is nondiscriminating; both simplified accounts miss *hebuc*;
  *fristmearc* discriminates breaking/smoothing packages, not
  restoration alone. Independent Ringe2017:312--313 n-stem suffixes
  give *spad-aniz* versus *spad-anunz*, but Ringe--Taylor153--154,
  376 n.10 positively identifies remodelling in the comparable
  nominative/accusative syncretism. A unique complete unlevelled
  prehistoric cell is therefore not asserted. The *markō-* comparison
  independently distinguishes nominative *-ō* and accusative *-ǭ*.
- Barrack157:56--57 concerns a short stressed target;
  Barrack162:57 a different long-vowel development. His latter rule
  cannot resolve the short-vowel consonant restrictions.
- Seiler's shared-*EE transmission analysis qualifies glossary
  agreement. Versloot's 2026 study concerns early Anglian, expressly
  not West Saxon; its quantitative choices and lexical-diffusion
  interpretation are not adopted as exceptionless CAPR laws.
- Lass and Anderson1975:66--69 remains deferred, not represented
  as consulted evidence.

## Historical analysis

- Historical stage: preliterary Old English under the adopted
  southern reconstruction, not inferred from the executable name.
- Scope: English-specific phenomenon with dialectally differing
  environments/ordering, not proved pan-English synchronous retraction.
  Retain the registered stage/scope axes without using confidence to
  derive a dialect or chronology.
- Regular conditioning: stressed short front low vowel before a
  historically back following vowel across a singleton; qualified
  geminate and *sk/st* evidence; much weaker *fC* and limited
  consonant-plus-liquid evidence. Root stress is independent of
  following-vowel stress, quality and nasal history.
- Counterexamples: *tæppa* and other fronted geminates remain
  substantive. Removing all geminates contradicts positives;
  restricting just *pp* is not independently established by Hogg.
  Épinal *hebuc* also remains unexplained by both simplified accounts.
- Analogy: positive redistribution is discussed by the handbooks in
  strong-verb and nominal/adjectival paradigms. No positive
  word-specific analogy has been newly established for *tæppa*.
  Do not repeat its inherited annotation as a proven explanation.
- Proxy: current SC046 both overgenerates onto two unstressed linkers
  and underrepresents explicit secondary stress. A source-led
  stressed-target correction is therefore worth review, but its
  standalone rainbow regression prevents adoption as a complete fix.
- Chronology: SC041 bleeding remains independently demonstrated in
  its owning adjudication. Brightening feeding restoration is a
  dependency of the adopted account, not an independent experiment
  distinguishing it from blocked fronting. The local SC046/SC048
  constraint depends on trigger representation and exposure by SC047;
  do not retain its old claim of independent historical proof.
  Breaking/restoration ordering in *slēan* is source-conditional and
  dialect-scoped; no universal new edge is introduced.

## Verdict

DEFER the executable revision; preserve the working southern restoration
account and record the source-critical and computational limits.

Registry-verdict: SC046=DEFER

A generic geminate ban is falsified by independent positives. The
stressed-target restriction is source-led but not independently
production-ready because it exposes rainbow's downstream diphthong/
syncope interaction. Current matches do not establish that the broad
target is historical, nor can a match score choose restoration over
blocked fronting in nondiscriminating forms. No FST/cell/baseline
adoption is authorized by this verdict.

## Propagation (only after verdict)

Authoritative targets: SC046 registry verdict and human note,
this memorandum, SC046 reader and dated chronology-card qualification,
focused regressions, and the post-brightening dossier. Source holdings/cards and
immutable experiment records are evidence, not a new validation system.

The proposed stressed-target FST diff is reviewable but unapplied.
All production FST bytes, order, selected corpus inputs/targets,
contexts and protected baselines remain unchanged. Current reference
is 386/394, with the same eight mismatches. Candidate comparisons
explicitly record every rejection and ambiguity; neither has any.

Validation completion and costs are recorded in the accompanying
source-bound evidence; no unfinished run is represented as certification.

### Regression execution and cost-review entry

The new runtime owner is
`Germanic/tests/test_sc046_adjudication.py::test_current_production_restoration_positives_and_scoped_residue`.
It reads two cumulative snapshots and the production endpoint for eleven
selected rows: three batched lookups, no compiler call, no definition
preparation, no new corpus sweep or rebuild, and no concurrency change.
It preserves oral/nasal and selected-ending controls while explicitly
protecting the known compound/geminate residue against silent changes.
The existing SC041 controls own its seven-row bleeding intervention;
the strict suite retains the existing all-corpus production owner.

The other two new nodes in that module authenticate the immutable
source-bound trials and their complete row deltas, fixed-apocope
intervention, independent geminate positives and compound checkpoints.
They do not claim fresh counterfactual execution in portable validation.
No commit-pinned historical replay is added to the routine lane.

The actual scientific work, separate from recurring regression cost,
was one initial ten-network compilation (two rule restrictions and
the initial order intervention), 300.260 s in Foma, 300.723 s worker
end-to-end, peak 2,790,788 KiB; and one six-network follow-up compilation,
438.400 s in Foma, 438.968 s worker end-to-end, peak 2,790,396 KiB.
Both were isolated full-source standalone executions, with no extant
shared session image, and each used one Foma process. Peak memory is
the actual Linux Foma child's `wait4.ru_maxrss`, not host Python
memory. Common-definition work is included, not hidden as setup.
The five-minute versus seven-minute totals are not a controlled
performance comparison. These one-off costs are justified by the
two distinct falsifiable scientific questions; neither is introduced
as a new recurring compiler job.

Canonical evidence regeneration was required by the adjudication
workflow and took 8m33s, including its forced production/stage rebuild.
That diagnostic receipt truthfully records concurrent bibliography/
source-card edits and a generated provenance update; it is not reused
as an exact-final-source certification. Both immutable isolated-trial
execution receipts record `source_changed=false`. Subsequent final
validation must identify the settled documentary candidate separately.

## Residue

The next scientific issue is to reconcile stressed-target restoration
with the exposed back-mutation/syncope history of *rainbow*, without
inventing a lexical exception or changing a selected input for fit.
The geminate and early-Anglian alternatives need independent
conditioning/ending evidence; *tæppa* cannot be disposed of by
unsupported analogy. *Hebuc*'s distinct spellings and the full
prehistoric case endings in the deciding set remain qualified.
Lass and Anderson1975:66--69 is deferred. No SC044 revision, broad
chronology rewrite, Foma optimization or new corpus admission is begun.

# Flask late-final-n: adoption assessment and full-corpus comparison

## Identity

2026-11-14, `research/flask-inherited-paradigm`; production reference
`1bad32cd15dfdc10c154c3e90fcfe9afd0e42eb4`.
Research concerning input coverage, SC023 `PNWGmcNStemNLoss`,
SC069 `OEEarlyOShortening`, SC071 `OELateOShortening` and SC100
`OEFinalUnstressedOLowering`. SC051 is unchanged throughout.

Recommendation: do not yet adopt the exact variant or switch selection.
The computational condition passes: no collateral changes, and the
separate plural selection gains one match. The historical condition does
not yet pass. Hill's now-consulted argument supplies substantive support
for the competing raised-ending history, not merely an unexamined
traditional assumption. This remains unresolved between 1B and 2;
neither an established 1A nor demonstrated analogy in every cell.

## Question

Does the exact archived `late_final_n` variant support selecting the
secure nominative plural *flascan* from full `*fláskōniz`? Separate
admission, protection of secondary n and survival of ō until late
shortening. A defensible synthesis of published analyses is sufficient
in principle; no requirement that one author print the complete CAPR
derivation is imposed.

Confirmation requires both a safe corpus delta and a positive historical
case for that synthesis. Early raised reflexes of the same northern
non-u cases, independently shown not to be remodelled, would refute
categorical retention of their ō.

## Current state (before any edits)

Production selects `*fláskōn : flasce`, output `flæsċe`.
The [previous cell audit](flask-attested-cells-late-ending.md) documents
experimental normal-entry *flascan* in nominative plural and dative
singular, but no 394-row run. It distinguishes inherited accusative
`*-ōnunz` from nominative replacement and records the existing failures.
Its source and pipeline bytes remain the production reference here.

The exact candidate retains the archived gateway, including `ōnunz`,
not just `ōniz/ōni`; moves old final-n loss before early i-apocope;
and replaces only the early-shortening relation with:

```foma
define FLEarly Ctx([
    {*ō} -> {*a} ||
    EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _
    [{*m} | {*n} ContextSegments]
]);
```

Thus unstressed ō before final n escapes early shortening; pre-m and
nonfinal pre-n environments do not. No new late rule, root-retention
rule or SC051 modification is composed. The archived unused
`FPUnround` definition is not part of any tested order.

## Diagnosis

### Preregistered predictions and execution

The pre-execution version of this note is sealed in experiment
`flask-late-n-1bad32cd-v1`. It predicted no unchanged-vocabulary delta,
then only row 2016 changing under a separate selection. Those are now
measurements, not substituted predictions.

Three complete 394-row runs start at the ordinary gateway from normalized
raw inputs, retaining the existing context metadata, including the one
noncitation-context row. They propagate all branches through all 113
relations; no singleton assumption conceals intermediate ambiguity.
The second candidate run changes only Flask's selected input and
comparator, preserving its comparative PROTO and the other 393 records.

| Run | Gateway accepted | Final outputs | Matches | Ambiguous rows, gateway / intermediate / final |
|---|---:|---:|---:|---|
| Production, original vocabulary | 394 | 394 | 385 | 0 / 0 / 0 |
| Exact candidate, identical vocabulary | 394 | 394 | 385 | 0 / 0 / 0 |
| Exact candidate, only Flask selection changed | 394 | 394 | 386 | 0 / 0 / 0 |

With identical vocabulary there are no admission changes, new
ambiguities, changed outputs or changed match statuses. At the aligned
early-shortening checkpoint all 394 before/after pairs also agree.
There is consequently no unexpected row requiring a first-divergence
trace or gateway-only/protected-n corpus decomposition; neither
conditional corpus run was executed.

The complete row-by-row output delta in the separate selection is:

| ID | Input before → after | Comparator before → after | Output before → after | Match |
|---|---|---|---|---|
| 2016 | `*fláskōn` → `*fláskōniz` | *flasce* → *flascan* | `flæsċe` → `flascan` | no → yes |

All other 393 outputs, admissions, cardinalities and match statuses are
identical. There are no collateral changes to explain. The eight remaining
mismatches are 1973 *bucc* (`bocc`), 2013 *fȳre* (`fȳr`), 2030
*fugol* (`fogol`), 2162 *rust* (`rost`), 2224 *strēaw* (`strēa`),
2240 *tæppa* (`tappa`), 2298 *wulf* (`wolf`) and 2300 *wull* (`woll`).
None is new.

### Census and evidential weight

Old n-loss changes the same 17 selected citation forms in both
unchanged-vocabulary runs: 1933, 1999, 2016, 2065, 2105, 2106,
2139, 2141, 2188, 2231, 2234, 2259, 2262, 2271, 2279, 2287, 2288.
With Flask changed to the plural it changes the remaining 16, not
2016. These are citation-normalization applications, not evidence that
the loss was historically productive in West Germanic.

Neither production early shortening nor `FLEarly` changes any of the
original 394 rows. Therefore the successful unchanged-vocabulary
comparison is a nonregression result, not independent positive validation
of the new final-n exception. The new plural supplies an exemption
witness. No additional frozen-subset or strict-suite census was run.

### Fresh independent controls

All 15 previous raw controls were run afresh through production and the
candidate; the latter's gateway preserves their segments, stress and
quantities exactly. All 15 candidate finals equal their frozen
`1bad32cd` results. Production admits four and rejects eleven at its
gateway; a rejection is not a wrong phonological output.

| Control input | Fresh candidate output | Assessment |
|---|---|---|
| `*fláskōniz` | `flascan` | Secure nom.pl., Hecht C p.141 l.27; full normal entry |
| `*fláskōni` | `flascan` | Secure dat.sg., Hecht C/H p.142 l.3; full normal entry |
| `*túngōniz` | `tungan` | Parallel class result; inherited versus remodelled ending still disputed |
| `*túngōn` | `tunge` | Ordinary nom.sg. preserved |
| `*dōną` | `dōn` | Secondary n and stressed vowel preserved |
| `*búrōθi` | `boraþ` | Independent late mechanism, not independent final-n retention |
| `*fláskōn` | `flæsċe` | Singular mismatch remains |
| `*fláskōnų`, `*fláskōnunz` | `flasconu`, `flasconun` | Existing inherited accusative failures, not new failures |
| `*túngōnų`, `*túngōnunz` | `tungunu`, `tungunun` | Existing accusative failures, unchanged |
| `*fláskōmaz`, `*túngōmaz` | `flascem`, `tungem` | Existing pre-m problem; Flask dat.pl. unattested, attested *tungum* not derived |
| `*fúldōnų`, `*érθōnų` | `foldonu`, `eorþonu` | Conditional full inputs still fail to derive northern accusatives |

The genitive-plural quantity problem was not retested or silently solved;
the expansion does not establish admission of every possible weak ending.
Control records have no supplied comparator; their recorded `match`
flags are not historical success judgments. The test here is their
unchanged outputs and explicitly assessed attested cells.

### Decisive traces and witness roles

Normal nominative-plural admission gives `fláskōniz` with every segment
and quantity intact. Old n-loss leaves its nonfinal n alone; i-apocope
gives `fláskōnz`, z-loss `fláskōn`. The dative converges at `fláskōn`
after loss of i. Both then follow:

| Relation | Before → after |
|---|---|
| `EAFBrightening` | `fláskōn → flæskōn` |
| `OEARestoration` | `flæskōn → flaskōn` |
| `OESkPalatalization` | `flaskōn → flaskōn` |
| `OEMedLongShort` | `flaskōn → flaskōn` |
| `FLEarly`, early unstressed fronting | `flaskōn → flaskōn` |
| `OELateOShortening` | `flaskōn → flaskon` |
| `OEFinalUnstressedOLowering` | `flaskon → flaskan` |
| Final rendering | `flascan` |

Restoration is a live root-vowel application; the retained back vowel
feeds it. The secondary nasal is a counterfeeding-negative witness for
old n-loss, and the old nominative a positive loss/escape control.
The final-n condition is an exemption, not an application of an invented
replacement rule. *Boraþ* supports the late mechanism outside this ending.
The previous protected-n `flascen` control is reused, not rerun here;
it implements early shortening/fronting, not the literature's competing
ō-to-ū raising history.

SC051 sees a back root and following back vowel, retaining hard sk,
written sc. Plain sc is compatible, not decisive phonetic proof.
The attested *flaxan* parallels supply hard/metathesized-cluster evidence;
literal x is not derived by this experiment. Root-vowel regularity,
the ending and metathesis must not be conflated.

## Literature

### Three changes, assessed separately

| Change | Supported | Inference / experimental limit |
|---|---|---|
| Input coverage | Ringe 2017, pp.312–313, §4.3.4(ii), supplies the inherited weak-feminine endings. Gateway expansion preserves the assembled Flask and tongue inputs exactly. | Applying the generic ending to the source-supported Flask stem is analyst assembly, not an author-printed whole form. Admission says nothing about the ending's subsequent history. |
| Old final-n loss before new-n exposure | Ringe 2017, pp.101–103, dates the old loss before Proto-Germanic; Ringe–Taylor 2014, pp.55–58, treats subsequent high-vowel erosion. The SC023 dossier already distinguishes this from secondary n in *dōn*. | Moving the executable citation-normalizer earlier expresses that distinction and preserves the nominative. Its identifier is not a date; it is not a new West Germanic n-loss law. |
| Late shortening of surviving `ōn#` | Ringe–Taylor p.164 scenario (3) explicitly allows regular northern `ōn → an`. Campbell pp.147–148 §355, Hogg pp.227–228 §§6.27–6.28 and Stausland Johnsen pp.28–30 establish a late-shortening mechanism. | Exempting this particular secondary-n ending from earlier developments, so that its vowel still is ō at that mechanism, remains the synthesis under test. The generic mechanism does not settle that premise. |

Campbell §355(4) includes syllables made final by ending loss. His final
paragraph explains why late shortened ō gives a too late to front.
Hogg §6.27(3) includes long vowels before final consonants; §6.28n2
places shortening later than i-umlaut. These are genuine reasons the
proposed route is possible, not evidence restricted to open syllables.
They do not single out inherited weak `*-ōni/-ōniz` as retained-ō cases.

Hogg pp.64–65 §3.34 instead derives raised feminine accusatives before
following u and explains ordinary *tungan* by paradigm influence.
Fulk pp.88–90 §§5.5–5.6 and p.172 §7.33 distinguish before-u raising
from later raising before tautosyllabic n, including the non-u cases.
Fulk treats feminine conformity to the masculine as the common account
but points to Ringe–Taylor's alternatives. Those alternatives are real:
the latter's pp.163–164 scenarios (1) and (2) use masculine redistribution,
whereas (3) allows the feminine phonological ending to spread instead.
Neither direction is a demonstrated complete solution.

### Hill 2010: newly consulted primary argument

Eugen Hill, “A case study in grammaticalized inflectional morphology:
origin and development of the Germanic weak preterite,” *Diachronica*
27(3), 411–458, DOI `10.1075/dia.27.3.02hil`, pp.432–443, especially:

- Pp.433–435, tables (19)–(20): raising includes dat.sg. and nom.pl.,
  not just inherited accusatives. Hill uses a PGmc *ān* notation,
  yielding early NWGmc ō before consonants; CAPR's Ringe-based PGmc
  input notation is not silently replaced by his.
- P.436, §4.2: lexicalized “friend,” including OE *frēond* and
  OFr *friōnd/friūnd*, supplies evidence outside weak-feminine endings.
- Pp.436–437, §4.3: Hill explicitly addresses OE/OFr *tungan/tunga*.
  Their shared endings need not prove absence of raising: genitive
  and dative plurals independently show masculine/feminine convergence
  in his account. His pre-m interpretation differs from Hogg's; it is
  not a new resolution of CAPR's *tungum* failure.
- P.437 n.8: comparative/superlative u/o supplies possible indirect
  Anglo-Frisian raising evidence, not a securely dated weak-noun cell.
- Pp.439–441, §4.4: restricting raising to a following u leaves
  the non-u OHG cases unexplained; an added high-i condition
  requires further restrictions to exclude the dative plural.
- Pp.441–443, §§4.5–4.6: fifth-century Runic *igijon/agilamudon*
  and the contrasting North Germanic “friend” history argue against
  a shared Northwest Germanic raising event. Hill concludes in favour
  of common West Germanic tautosyllabic-n raising and a separate,
  later North Germanic development.

The Runic dates therefore constrain the North Germanic/shared-protolanguage
claim, not directly the date of raising in the ancestors of OE/OFr.
They do not establish that the Anglo-Frisian branch escaped it.
Conversely Hill's comparative reconstruction is not a directly dated
northern nominative/dative attestation. His “friend” argument is relevant
but not identical to final `ōn#`; Ringe–Taylor p.62 cautions against
generalization from its exceptional contracted trimoric vowel. The
quantity and context difference must be reconciled, not erased.

This makes raising-plus-redistribution a supported competing history,
not an extra analogy invoked only to rescue a failed CAPR run.
It also prevents treating the exact final-n exemption as the automatic
default of the already implemented late mechanism.

The supplied PDF was checked directly, printed pp.432–443 = sheets22–33.
Its SHA256 is
`b9dba868bba0b48a243a52b5da73014322fd69e01c1faac98c6b3f86e06ce7b2`.
The local holding is `docs/references/hill_2010_germanic_weak_preterite.pdf`.
Boutkan 1995, *The Germanic “Auslautgesetze”*, pp.289–290 was unavailable
in this pass and has not been read directly. Hill p.435 and pp.436, 442
report relevant arguments and cite pp.288–290; those are explicitly
indirect evidence, not a substitute consultation of Boutkan.

### What the relics and the late mechanism distinguish

*Ēastron/-un*: Fulk p.172 §7.33 calls these plural; Campbell
p.250 §619(1b) reports -on in inflected singular cases and nom./acc.pl.,
beside strong plural variants. Ringe–Taylor pp.62, 164 calls its
profusion of oblique forms difficult to evaluate. Rounded reflexes
are potentially decisive in the non-u singular obliques or nominative
plural, not merely because the word sometimes ends in u. Without
identifying a token's inherited cell and excluding redistribution
they do not prove that `*-ōni` or `*-ōniz` raised in northern West
Germanic. If an unremodelled
nominative plural in -un were established, it would be a direct
problem for this candidate; no such new attestation claim is made here.

*Foldu/eorðu*: the early Northumbrian accusatives (Cædmon's Hymn 9;
Leiden Riddle 11; Ringe–Taylor p.62) have inherited following-u
environments. They support raising there, not necessarily before n
exposed by loss of i. Their small number and exclusively accusative
distribution are suggestive rather than a securely categorical
restriction; Ringe–Taylor explicitly cautions about the sample.
The proposed ō-exemption does not undo earlier ū. CAPR's unchanged
full-input failures do not decide their historical account.

Stausland Johnsen, “Vowel reduction in verbs in King Alfred's
*Pastoral Care*” (2015), pp.28–31: after shortening, medial o raises
while final-syllable o lowers to a, with syllable count already reduced
by short-vowel loss. P.36 §7 explicitly leaves other morphological
classes and non-West-Saxon dialects to further demonstration.
Extending a phonetically/prosodically stated process to a noun is a
reasonable regular-phonology hypothesis, not forbidden grammatical
conditioning. It nevertheless needs the noun's ō to survive the
earlier raising discussed by Hill. The verb corpus does not test that.

## Historical analysis

The late route is a reasonable synthesis of the published northern
scenario and general shortening, but its crucial survival premise has
less independent support than the mechanism itself. Hill supplies
positive cross-paradigm and comparative grounds for the competing
raising account, while ordinary feminine -an and parallel *tungan*
fit both histories. Genitive/dative-plural convergence gives positive
evidence for some redistribution, but does not demonstrate it in the
two particular Flask cells.

On balance, raising plus redistribution currently has firmer independent
support than this exact retained-ō synthesis. This is not a demonstrated
evidential-and-economic tie to be broken against CAPR's preference for
regular phonology: preserving ō here overrides an independently argued
earlier development, and no independent unremodelled northern non-u
cell has yet been supplied to warrant that override. Nor is the regular
route disproved. Ringe–Taylor's northern alternative and the distinction
between following-u and newly final-n environments keep it viable.
Simply counting the fewest operations in the Flask trace would not
compare the accounts' wider morphological commitments.

| Chronology statement | Classification and warrant |
|---|---|
| Old final-n loss precedes apocope exposing a new n | `stage_entailed`: pre-PGmc loss versus later high-vowel erosion; original/secondary distinction, not a prefix-based stage inference |
| Generic late long-vowel shortening follows short-vowel loss | `independently_demonstrated`: *byrst/byrsti* argument, Stausland Johnsen pp.29–30; Hogg §6.28n2; not proof about this noun ending |
| Secondary `ōn#` survives earlier changes to reach that mechanism | Experimental hypothesis; no new independently demonstrated chronology edge |

The corpus safety result supports implementation feasibility, not
selection of a historical account. No chronology graph, historical
stage inventory or sound-law authority is changed by this experiment.

## Verdict

DEFER production adoption of the exact `late_final_n` variant and
retain *flasce* as selected comparator. No 1A is established. The
normal-entry *flascan* nominative and dative demonstrate a viable
computational 1B candidate, but not a historically adjudicated 1B.
The evidence also does not establish 2, because neither root levelling
in the singular nor ending redistribution elsewhere proves analogy
in every attested cell.

Registry-verdict: n/a; bounded research assessment, with all existing
SOURCE registry verdicts retained.

A deciding observation would be a securely cell-identified early
OE/OFr reflex of `*-ōni/-ōniz`, independently insulated from
masculine/feminine redistribution: retained-ō/-an evidence before that
convergence would favour the regular route; raised -un would oppose it.
Alternatively, independently dating tautosyllabic-n raising before or
after the Anglo-Frisian separation could decide the geographic premise.
Rounded spelling alone, the three following-u accusatives, or another
successful Flask implementation does not supply that observation.

## Propagation (only after verdict)

Only this research note, reproducible evidence and the Flask source
ledger change. Production rules, selected TSV, classification, reader
chapters, baselines and registries remain untouched. No publication
build or strict suite was run: implementation and selection remain
unsettled, whereas the mandatory 394-row comparison is complete.

The independently defensible gateway expansion and old/new-n distinction
are not silently adopted as a partial production patch in this pass.
An eventual adoption of the exact bundle would additionally require
the disputed early-shortening restriction, the nominative-plural input
and comparator migration, and canonical certification.

### Evidence and reproduction

[Experiment driver](flask-late-final-n-evidence/experiment.py),
[recorded matrices](flask-late-final-n-evidence/observed.json),
[all 394 rows](flask-late-final-n-evidence/corpus.tsv), and
[changed-row and control traces](flask-late-final-n-evidence/decisive_traces.tsv).

Production FST SHA256:
`21f86e76dd3d7f3f76633fabd679d3fab2d40548a5b8dc84596c6760d11b52d6`;
pipeline:
`742068d0091372e72865c235b4289c430f30fab83e2d1b4a6edb040a7570fcd6`;
exact recipe:
`91c1e6c199ab21578c9085736bf7c9378d04dacbf7a603d824700c8e7ec8bbeb`.

The 115 isolated component binaries were compiled at 15:27:28–15:32:00
UTC in `flask-cells-a829dfcb-v1`, not freshly compiled here.
All their hashes were verified before reuse. New execution was
16:18:07–16:18:12 UTC, exit 0: three full corpus runs plus two 15-control
runs, 1,212 normal-entry derivations. The source-bound snapshot pins
source, pipeline, vocabulary, context metadata, recipe, driver and
previous evidence; the receipt seals all results.

From the reference-compatible tree, for an independent fresh compile:

```sh
python3 Germanic/docs/sound_changes/audits/flask-late-final-n-evidence/experiment.py \
  --snapshot-id flask-late-n-independent-v1
```

The measured run instead reused the verified prior manifest:

```sh
python3 Germanic/docs/sound_changes/audits/flask-late-final-n-evidence/experiment.py \
  --reuse-components .capr-work/experiments/flask-cells-a829dfcb-v1/results/isolated-compile-f8c728bb7bbc4948a851ad2e520b618e.stdout.log
```

Choose a new snapshot ID on repetition; completed snapshots cannot be
overwritten. Full 113-relation histories for every row, including unchanged
rows, remain sealed locally in that experiment's `results/all_traces.json`,
SHA256 `a6cfa7b01abeddcf0820a08255fb1aad5bc757a404c50dfaf12803dea992c1d7`.

## Residue

Direct consultation of Boutkan pp.289–290 remains outstanding. The
remaining scientific issue is the northern non-u ending history, not
admission, ambiguity, corpus nonregression, root restoration or a newly
failed accusative/dative control. Existing metathesis and pre-m problems
remain separate. No negative attestation search or implementation failure
has been promoted into proof that every Flask cell requires analogy.

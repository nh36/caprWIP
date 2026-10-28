# Rainbow and earthly: secondary-stress adjudication

## Identity

- SC ids: SC017, SC036–SC038, SC040; isolated research, no registry action.
- Executables: `PNWGmcULowering`, `OECompoundLinkingSyncope`,
  `OEStripSecondaryStress`, `OEInterStressRaising`,
  `OEMedUnstressedULowering`. Names do not establish historical stages.
- Date / branch / base: 2026-10-27–28, this research receipt on
  `research/compound-secondary-stress`,
  `3cb109c981c8868bf383172e2be06cdc88c00fb0`.

## Question

Hypothesis: early lowering in subordinate-stressed *-bùgô*, combined
with independently computed OE quantity-sensitive prominence, permits
one inherited-grave deletion while preserving *weorold*, *reġnboga*
and an inherited inflected *-cund-* cell.

Confirmation requires source-backed conditioning and morphology, complete
ending development, appropriate positive/negative controls, and no new
selected-output ambiguity or unexplained regression. Counterevidence
includes an independently attested phonological counterexample in the
proposed domain, failure of the complete cell, or stress assigned only
because a particular suffix needs its vowel saved.

## Current state (before any edits)

The registry characterizes SC017 as “Northwest Germanic,” scope
`pan_pnwgmc`; SC036 as “OE weak medial vocalism,” with the compact
inherited world input adopted and soul explicitly provisional; SC038
is a `technical_marker`, not an independently dated sound change.
SC040's notes state “root u and following m preserve u.” These
authorities are retained, not revised by this research.

`results.json.gz` records the exact source text/hashes, input grammar,
109-stage order and identity traces. Relevant positions are SC017 at
20, linking syncope at 45, inherited-grave deletion at 46, weak raising
at 47, and late medial lowering at 89. Early lowering has only
word-initial plain/acute branches. `FootCtx` protects a pretonic
syllable; it does not calculate the required medial feet.

The selected inputs remain `*wír-àldiz`, `*régna-bùgô` and
`*sáiwalō`; their outputs are *weorold*, *reġnboga*, *sāwol*.
The compact world junction is pre-encoded, not newly derived.
Earthly has no new selected corpus row. Existing SC036 adjudication,
world migration closeout/frozen experiments, lexical-witness gate
adjudication and input-gate tests were consulted without modification.

Verified baseline: 389 accepted, 381 matches, eight mismatches
`1973, 2013, 2030, 2162, 2224, 2240, 2298, 2300`. No rejected
or ambiguous selected outputs. Evaluator hash
`d6e8b90551e4bb57d8d161a8f2334c29620533a487a0e64f8857f500380d5e45`;
active380 hash
`9fb5d393e2f91ad077115593034099851c2d067f5dfefec5859f516a93783597`.

## Diagnosis

### Complete firing census and witness roles

Every selected firing/nonfiring and final delta is in each model's
`transitions` and `final_deltas`; immutable380 comparisons use the
frozen original inputs, not merely the current selected subset.
Production early lowering has 39 selected firings. The secondary branch
adds exactly rainbow (2148), giving 40; the early-checkpoint grave-*u*
census contains no other selected entry. The 39 inherited firings are
retained baseline applications, not 39 newly adjudicated historical
positives: existing mismatches and the old nasal proxy remain explicit.
The added rainbow firing is in the proposed subordinate-root domain;
there is no new out-of-domain selected firing.
Production linking syncope fires only on rainbow; inherited-grave
deletion on rainbow, thousand and world; weak raising on world and soul.
Late lowering has 11 selected firings in production and ten in the joint
model: rainbow no longer needs it. Every other selected late firing is
preserved.

| Witness | Role and decisive result |
|---|---|
| rainbow | New early live application; grave preserved to feed linking syncope; late lowering becomes a nonapplication |
| independent bow | Existing early live application; final *boga* remains unchanged |
| earthly genitive | Early nasal-blocked negative; linking-syncope application; later computed medial prominence blocks lowering |
| world | Weak-raising/back-mutation feeding witness; initial LH blocks an independent secondary foot |
| soul | Protected provisional proxy; still *sāwol*, no new historical claim |
| *-un / -um* | Attested dental/labial comparison; no general dental-nasal exemption |
| hawk/head | Attested negatives to overbroad early unstressed lowering |
| Buga | Actual unexplained name retention, not a synthetic blocker or silently successful control |

The immutable380 original inputs likewise have a full firing census in
`transitions[].immutable380_states`: each input is stored in
`immutable_legacy380`, and the preceding state is the previous transition.
The stable identity mapping is `active_legacy380`; the historical TSV
has no `row_id`, so its physical positions are not invented as identities.

The overbroad diagnostic introduces two mismatches: hawk (2060)
*hafoc → hafac*, head (2063) *hēafod → hēafad*. It prematurely
lowers their weak vowel, making it available to intervening vowel changes;
the complete responsible traces are in `final_deltas`. Its other extra
early firings, navel and widow, reconverge. These are not exceptions
added to repair the experiment.

### Principal traces

Rainbow, joint model:
`*régna-bùgô → *régna-bògô → *régnbògô → *régnbogô`
before the later palatal/ending/orthographic developments to *reġnboga*.
The inherited nonhigh ending is present when early lowering acts.
SC099 does not re-raise this *o*, and SC040 does not supply it.
In this exact serialization trimoric *ô* is separately recognized in
the early nonhigh inventory, not in every later vocalic context.
That technical nonfiring is recorded; it is not proof of a new historical
chronology edge.

Earthly genitive:
`*érθa-kùnðas → *érθa-kùndas → *érθkùndas → *érθkundas
→ *érθkundæs → *éorθkundæs → *éorθkundes → eorþcundes`.
Early lowering is blocked by the first post-vocalic nasal.
SC037 consumes the inherited grave, then SC038 removes it once.
The later analysis syllabifies *eorþ.cun.des* as H H H: initial
heavy foot, eligible nonfinal heavy head, final destressing. The computed
medial head protects *u* at SC040. The final-*a* alternative
`*-kùnðasa` independently loses bare final *a* and reaches the same
complete genitive; the neuter *-es* alternative also succeeds.
Plain `*-kunðas` fails linking syncope and gives *eorþocundes*,
so later footing is not secretly replacing earlier accent information.

World retains the complete approved sequence:
`*wír-àldiz → *wír-àldz → *wér-àldz → *wér-àld
→ *werald → *weruld → *weoruld → weorold`.
The machine trace preserves the precise acute/star representation omitted
from the later readable abbreviations. Initial LH, including inflected
*weruldes*, does not acquire an independent medial head. The earlier
compound junction remains outside this selected regular span.

### Displacement controls

| SC038 placement | Early rainbow lowering off | Early rainbow lowering on |
|---|---|---|
| before linking syncope | rainbow *reġnofuga* | rainbow *reġnefoga* |
| production, before weak raising | no selected change | no selected change |
| after weak raising, before late lowering | world *wereald* | world *wereald* |
| after late lowering | world *weorald*, rainbow *reġnbuga* | world *weorald* only |

These are annotation/dependency diagnostics, not dates. Early lowering
removes rainbow's dependence on late lowering, but does not permit
erasing the earlier grave before linking syncope or retaining world's
grave through weak raising.

## Literature

Existing dossiers: approved world/SC036 research, the early vocalic
SC017 dossier/adoption, medial-lowering discussions, and the lexical
witness gate record. The supplied revised essay proposes the questions,
not their authority.

Direct source checks and page-level arguments are in `literature.md`:
Campbell 1959: 34–35, 43; Hogg 1992/2011: 49–50, 54–55,
239–241; Fulk 2018: 56–57, 209–211; Ringe–Taylor 2014:
22–23, 27–29; Kroonen 2013: 82; Orel 2003: 85; Colman 2011:
95–98; McCully–Hogg 1990: 323–333, especially the revised
formulation at 330–333; Hogg 1996: 3–12; Goering 2023: 79–84;
Minkova–Zhou 2023: 86–90; Ciszek-Kiliszewska 2015: 489–490.
Russom/Bredehoft were abstract-only, and Fulk's meter monograph
was accessed only through Hogg's discussion. No direct full-text reading
of those unavailable works is claimed.

Sources establish early assimilation in *boga*, nasal/*j*
restrictions, legitimate genitive endings, inflection-sensitive subordinate
prominence, quantity-sensitive initial/medial footing, and the special
initial-LH issue. They do not directly print the complete proposed
rainbow/earthly histories. The subordinate-root extension, precise
single-domain executable projection and its historical application at
late lowering are explicitly CAPR inferences.

## Historical analysis

Historical stage/scope: early lowering belongs to the source-backed
Northwest Germanic account; the later stress grammar and lowering are
OE. No stage is inferred from an identifier. No new absolute date or
general historical reaccentuation is asserted.

The early experimental branch is exactly:

```foma
define RSyllEarly Ctx([
    {*ù} -> {*ò} || _
        [EnglishStarConsonantNoJ - EnglishStarNasal]
        EnglishStarConsonantNoJ* EnglishStarNonHighVowel
]);
```

It preserves stress, excludes nasal as the first intervening consonant,
excludes *j* throughout, and requires a following nonhigh vowel.
It is not a rule for every unstressed *u*. The compound-explicit
control additionally requires a preceding primary nucleus in the accepted
compound domain; no lexical identity or adjective flag conditions it.
The exact old nasal restriction remains narrower than all the scholarly
formulations: a synthetic later-position nasal exposes that inherited
limitation rather than fixing it silently.

Late prominence is computed by compulsory nucleus marking and
maximal listed onset assignment. Initial H(+L) or L+syllable fills the
first foot; subsequent nonfinal heavy nuclei can be heads, final nuclei
cannot. Only eligible short plain vowels receive computed graves.
*Æþelingas* versus *cyningas*, *weruld(es)* versus *eorþcundes*,
and inflected versus uninflected *synfull* test the independent quantity
claim. A single-onset sensitivity model tests the onset assumptions.
Pretonic material is recognized by the existing phonological marker,
not a prefix list.

B2 separately encodes and decodes that classification around unchanged
SC040; B3 composes the same procedure with lowering and immediately
decodes it. B2/B3 and the joint model agree on complete selected outputs.
The encoding/decoding is technical representation, not a second dated
loss of inherited secondary stress. This is a bounded single-domain
projection, not the full cyclic McCully–Hogg grammar or Goering's
qualified final-overheavy exceptions.

### Six explanations compared

| Model | Evidence and complete-cascade outcome | Assessment |
|---|---|---|
| 1. Production/B0–B1 | Both selected words correct; rainbow's *o* late; grave earthly genitive *eorþcondes* | Existing contradiction remains |
| 2. A alone | General early branch, comparative *boga* support; rainbow early *o*, earthly still *eorþcondes* | Rainbow correction supported |
| 3. B2/B3 alone | Source-motivated quantity/inflection contrast; complete *eorþcundes*; rainbow *o* still late | Genitive rescue, not early rainbow account |
| 4. Joint | Both source-supported inferences; *weorold*, early-*o reġnboga*, complete *eorþcundes* | Best bounded explanation; no added morphology, transponent or dated stress loss |
| 5. Segmental B4 | Labial restriction supported; dental *-un > -on* refutes a blanket nasal block | No independently supported extra segmental law; not encoded |
| 6. Analogy B5 | Inflected *u* could supply uninflected stem; independent *boga* could influence compound | Possible later levelling, not demonstrated or encoded; not required for the selected genitive |

### Counterexamples, gaps and falsification

The result is a regular derivation of a legitimate reconstructed genitive,
not proof that the whole earthly paradigm is regular. Masculine accusative
retains *u* but gives *eorþcundene*, not predicted *eorþcundne*.
The feminine genitive gives *eorþcundere*, not attested
*eorþcundre*. Neuter nominative–accusative gives *eorþcundan*;
feminine accusative gives *eorþcunde*, but cannot change the neuter
agreement of *eád* in the actual Genesis passage. Uninflected
*eorþcond/godcond* and *synfoll* also show that ordinary final
destressing does not explain every attested retained suffix vowel.
These failures are not hidden by reporting only the stem.

Only two earthly dictionary loci were recovered from the reported six
tokens. Neither genitive *eorþcundes* nor accusative *eorþcundne*
was recovered; related *eardcundes* is not equated with earthly.
The genitive is a possible accidental gap, not an attestation.
*Buga* retention is not derived by feeding the same string as *boga*;
no name-specific phonology has been invented.

All serious models preserve each of the 389 selected outputs and the
eight named mismatches, the active380 fingerprints and all immutable380
original-input outputs. This is compatibility, not exhaustive proof of
the historical law. Transparent compounds, final-overheavy formations,
unrecovered tokens and the old early nasal proxy require separate review.
Minkova–Zhou's metrical cautions remain relevant to the inference
from literary pattern to speech prosody.

The main added sound operations `REarly`, `REarlyComp`, `RFoot`
and `RLate` pass both whole-relation checks in `functionality.json.gz`.
Every tested cascade stage has at most one distinct forward output.
The inherited parser and private extension nevertheless have a real
global segmentation defect: `biu → *b*i*u | *b*iu`.
It does not affect the tested populations or cells and was not repaired
in this assignment. Internal `RSyll`, `RSyllOne`, and sensitivity
`RFootOne` have conflicting Foma property diagnostics (functionality
false, extracted ambiguous domain empty); neither diagnostic is omitted.
This is not licence to call multiple historical outputs “variation.”
No blanket universal functionality claim is made for those internal
networks or for the inherited parser.

### Chronology evidence

| Relation | Classification | Evidence/limit |
|---|---|---|
| Early assimilation before loss/raising of its nonhigh trigger | `independently_demonstrated` in comparative literature | Fulk's *scolu* argument; not a new proof from rainbow's final spelling |
| Northwest Germanic assimilation before OE late lowering | `stage_entailed` | Source-assigned historical domains, not identifier prefixes |
| Early *bùgô > bògô* before the compound's ending changes | Model-local feeding realization | Full trace supplies the still-present trigger; compound extension is an inference |
| SC037 → SC038 → SC036 | Model-local annotation/feeding order | Existing rainbow and world displacement controls; not universally dated syncope/deaccentuation |
| Computed OE prominence at late lowering | Historical modelling inference | Hogg/McCully–Hogg quantity and inflection; no independently dated reaccentuation event |
| Initial weak raising → back mutation → late lowering | Retained approved world account | No alteration or new chronology promotion |

## Verdict

Research assessment: READY FOR ADOPTION REVIEW for the bounded joint
analysis and the strong genitive cell, not authorization for production
adoption or a claim that all OE secondary stress has been implemented.
The ten requested conditions are met for that cell: comparative early
lowering, general conditioning, established inherited morphology,
complete ending, independent prosodic contrast, one inherited-grave
deletion, surviving world history, unchanged selected corpus, agreement
between traces and argument, and explicit empirical limitations.

Controlled production verdict: DEFER implementation / RETAIN current
production. Machine-readable registry line: n/a, because this is
research-only and the canonical registry has deliberately not changed.
No new `Registry-verdict` record is asserted.

The combined account removes the proposed historical contradiction for
the bounded three-word test without retaining inherited grave stress
until late lowering. Generality and the successful inherited genitive
make it preferable to arbitrary accent relocation or a dental-nasal
exception. Adoption review must retain the explicit limits of the
single-domain projection, the parser defect and formal-helper diagnostic
disagreement; this is not unconditional approval of a universal grammar.
Scientific sign-off: Copilot, on the evidence and scope recorded here.

## Propagation (only after verdict)

Affected production files/registries: none. Future authorized adoption
would extend the existing early operation with the subordinate branch,
incorporate general OE prominence into the late-lowering operation,
and extend the legitimate-cell input grammar where necessary. It would
update the associated source-led reader/dossier/registry commentary
through the adjudication interface, without changing selected world,
rainbow, soul, chronology or frozen receipts. It would not admit earthly
as an attested genitive without new documentary evidence.

Focused research tests cover complete cells, paired early/late controls,
weight/inflection contrasts, grave lifetime, ordering negatives,
overbroad regressions, composed/component equivalence, both protected
populations and source/runtime preservation. All additions are confined
to this research directory. No production assertions were weakened.
Expected baseline/fingerprint effect: none; none was refrozen.

Closeout checks compared all 3,448 initially tracked research-worktree
files with their captured hashes: no differences. An earlier check also
found all 20 originally dirty files unchanged. At final closeout, 16 still
matched and four SC087/Barrack files had been externally modified in
the original worktree; they were not overwritten, reverted or staged
here (details in `environment.md`). The accepted matrix and formal
assay each additionally preserve complete 3,330-file canonical before/after
hash maps. Those final maps protect the independent backend reference
clone; the earlier successful shared-runtime assay protected 3,302 files.
Concurrent external rebuilds were rejected, not represented as
byte-stable intervals.
The 15 focused receipt tests
pass; no production/publication tests or rebuilds were substituted for
the requested isolated experiment.

## Residue

Separate authorization is required before implementation. Review the
bounded metrical projection against full cyclic domains, source access
gaps and final-overheavy exceptions; resolve the inherited parser
segmentation defect and annotation-helper diagnostic discrepancies;
recover the remaining earthly tokens if possible. Accusative and
feminine-genitive endings, uninflected suffix retention, onomastic
*Buga*, the complete early nasal restriction, and the provisional soul
history remain separate problems. No broad corpus expansion, second
stress-loss event, morphology-conditioned law or hidden analogy is
proposed as their substitute.

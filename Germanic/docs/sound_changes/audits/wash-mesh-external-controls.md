# Wash and mesh as external controls for Flask

## Identity

SC043 (root fronting), SC046 (restoration); fixed SC051. Bounded research on
2026-11-14; `research/flask-inherited-paradigm`, reference
`e7a9bed5c22b000131bf21252d2af7bda873c313`. No production adjudication.

## Question

Do independently established infinitive and neuter plural cells distinguish
Wright and Wright's retention from subsequent restoration or levelling?
Back-root agreement already supplied by ordinary restoration cannot do so.

## Current state (before any edits)

The reference derives the selected wash input `*wáskaną`; Flask remains
`*fláskōn` against *flasce*. SC043 fronts stressed `*á` before a nonnasal
consonant; SC046 can restore `*æ` across *sC* before a back vowel. The
existing narrow experiments retain `*a`, or retract `*æ`, only before
`*skā#`. Neither changes SC051 or its timing. These are executable
conditions, not historical stages inferred from identifier prefixes.

### Predictions frozen before execution

All root-vowel comparisons keep the production SC051 relation and position.
The broader scratch condition is evaluated at ordinary root fronting, before
the final-*ā* helper: one consonant, the existing geminate class (no *hh*),
*sk*, or *st*, immediately followed by a back vowel. It implements the
relevant open/closed environments of Wright and Wright §57, not a general
recovery mechanism for every lost historical vowel.

| Cell/input | Baseline prediction | Narrow prediction | Broader prediction |
|---|---|---|---|
| Flask/ashes weak nominatives, `*fláskōn`, `*áskōn` | Front root; final `*ā > *ǣ` prevents restoration | Root *a*, retained or retracted | Root *a* retained before still-back `*ā` |
| Wash infinitive `*wáskaną` | Fronting, then restoration across *sk* before the first ending *a* | Same as baseline: no `*skā#` | Retention before *sk+a*; same final root |
| Neuter acc. pl. `*máskō` | `*-ō > *-u`; fronting, then restoration; later heavy-syllable apocope | Same as baseline: *u*, not `*ā` | Retention before *sk+u*; same final root |
| Conditional neuter/wa-stem acc. pl. `*máskwō` | Check whether *w* survives; *skw* is not SC046's *sC* | Does not match `*skā#` | Literal *sk* condition does not skip an extra *w* |
| Conditional early-glide-loss diagnostic for that plural | Delete *w* after final raising, as independently described by Ringe–Taylor p.16; should converge on `*masku` | Same | Same |
| Neuter dat. pl. `*máskamaz` | `*-amaz > *-umaz`; restoration should already supply *a* | Same | Retention; no independent root-vowel success |
| Selected rest `*rástōz`, negative *st* control | Front-root *ræste* | Same | Back-root *raste*: a counterexample to this unqualified extension |

The back vowels relevant here have not disappeared before root fronting:
infinitival *a* remains internal; inherited plural *ō* becomes back *u*;
dative *a* becomes back *u* before *m*. The nominative's secondary final
*ā* fronts only after the root-fronting checkpoint. No historical-vowel
memory or unseen triggering *i* is supplied. For a different cell whose
only back vowel had already disappeared, this scratch condition would
need a separately justified earlier consultation point.
The predicted dative *a > u* did not execute; the results below retain
this failed prediction rather than silently substituting a later input.

## Diagnosis

One isolated backend compilation (117 components), 13:58:23–14:03:02 UTC;
focused runs 14:03:02–14:03:07 UTC, on the exact reference source. Across
four variants and eight probes, 24 normal entries complete and eight
normal entries reject; all 32 separately labelled post-tokenization
diagnostics complete uniquely. For accepted raw entries their finals
agree with the diagnostics. No corpus-wide census or comparison was run.

| Input/cell | Baseline final | Narrow retention / retraction | Broader retention | Decisive root history |
|---|---|---|---|---|
| `*fláskōn`, weak nom. sg. | *flæsċe* | *flasċe* / *flasċe* | *flasċe* | Baseline `*fláskā > *flæskā > *flæskǣ`; narrow/broad retention `*flaskā`, retraction `*flæskā > *flaskā`; all keep late SC051 |
| `*áskōn`, weak nom. sg. | *æsċe* | *asċe* / *asċe* | *asċe* | Same vowel/ending sequence without *fl-* |
| `*wáskaną`, infinitive | *wascan* | *wascan* / *wascan* | *wascan* | Baseline/narrow `*wæskaną > *waskaną` at restoration; broad retains *a* before *sk+a* |
| Conditional `*máskō`, neut. acc. pl. | *masc* | *masc* / *masc* | *masc* | `*másku > *mæsku > *masku` versus direct retention of *a*; later final *u* loss |
| Conditional `*máskwō`, neut./wa acc. pl. | Reject; diagnostic *mæsċw* | Same | Same | `*máskwu > *mæskwu`; neither literal *sk+V* retention nor *sC+V* restoration skips the extra *w* |
| Same, with sourced early *w*-loss setup | Reject; diagnostic *masc* | Same | Same | After raising, `*máskwu > *másku` at `WMGlideLoss`; then converges on the unlabialized plural |
| `*máskamaz`, neut. dat. pl. | *mascem*, not *maxum* | Same | Same | Early *a > u* misses; baseline/narrow `*mæskam > *maskam` restores the root; later ending *a > æ > e* |
| `*rástōz`, rest control | *ræste* | *ræste* / *ræste* | *raste* | Broader retention protects *a* before *st+ā*; the narrow condition does not |

Both `*máskwō` rows reject at the first relation, `EnglishProtoInput`,
with normalized raw input `máskwō` and no output path. Their reported
positive results enter immediately after that relation as
`*m*á*s*k*w*ō`; they are not successful raw-input derivations. This
locates the admission failure without attributing it, untested, to
either phonotactics or the relation's ambiguity filter. The glide-loss
setup inserts only `*w > 0 / C _ u#` after final-*ō* raising, before root
fronting, identically across all four root treatments.

The dative failure is also real: `PNWGmcAToUBeforeM` runs while
`*-amaz` still contains its final *a*; its current final-*m(i)(z)*
context does not admit that *a*. Final *z* and *a* subsequently disappear,
leaving *-am*, whose vowel fronts and merges to *e*. Thus its root *a*
is compatible with ordinary restoration, but this run does not derive
attested *maxum*. No ending repair or substituted input is adopted.

The fixed SC051 leaves hard *sk* in *wascan* and *masc*, but no run
performs *sk > ks*: it does not derive the actual *cs/x* spellings.
Conversely, Flask/ashes remain palatal in the root-*a* experiments
because final *ā > ǣ* still feeds the following-vowel clause. Root-vowel
agreement therefore cannot decide the consonant history.

## Literature

| Witness/source | Cell and evidential limit |
|---|---|
| Miller 1891, *Bede*, IV.XXXII, p.378.17–19 (PDF sheet 178) | Image-verified *in sæ wæscan 7 feormian*: uninflected infinitive governed by *wolde*, coordinated with *feormian*. Not an i-bearing finite cell. |
| [Bosworth–Toller, *wæscan*](https://bosworthtoller.com/34455), Bede IV.31, S.610.11 | Dictionary quotes *wacsan (wæscan, MS. T.)* in this sentence. The back variant is dictionary-transmitted here, not independently verified against the earlier edition; Miller's numbering differs. No manuscript date/dialect is inferred from the siglum. |
| Wright–Wülcker 1884, I, printed 93, fisherman's answer | *wyrpe max mine on ea*, Latin *pono retia mea in amne*: *max* is accusative plural, object of *wyrpe*; *retia mea* and *mine* confirm number. |
| Wright–Wülcker 1884, I, printed 92, hunter's answer | *on þam maxum*, Latin *in retibus*: locative dative plural. Not a weak feminine oblique. |
| [Bosworth–Toller, *masc*](https://bosworthtoller.com/22424), header *masc, max, es; n.* | OE neuter, genitive *-es*, supporting strong a-stem treatment, not an inherited feminine nominative in *-ōn*. |
| Kroonen 2013, pp.356–357, *maska-* | Distinguishes *maska-* and feminine *maskō(n)-*; OE *masc/max* is explicitly neuter. The *maskwan-* comparison on p.357 is not a complete reconstruction of this OE plural cell. |
| Orel 2003, p.262, *maskwō(n)* | Comparative headword explicitly m./f.; OE reflex explicitly neuter. An inherited route to the OE neuter is therefore conditional, not supplied by that headword alone. |
| Ringe 2017, p.300 | Neuter a-stem nom./acc. plural *-ō*, dative plural *-amaz*. These endings, not a feminine nominative or neuter singular *-ą*, determine the mesh probes. |
| Kroonen 2013, p.575; Orel 2003, p.450 | Strong *waskan-* / *waskanan*, both citing front-root OE *wæscan*. Orel p.450 is PDF sheet 489, not printed p.489. |
| Ringe–Taylor 2014, pp.16–17, 79, 127, 233 | Final *ō > ū > u*, early postconsonantal *w*-loss before unstressed *u*, *a > u / _m*; infinitive's inherited accusative *-ą*; *waskan*; distinct finite *wæsċeþ*. Wash p.127 is PDF sheet 142: the old ledger's 142 must not be used as a printed-page citation. |
| Wright and Wright 1908, §57, pp.37–38; Campbell 1959, §§158–159, p.61 | Published retention includes *sc/st* and geminates except *hh* before an originally back next-syllable vowel; examples include *wascan* and *masc/max*. Campbell allows restoration and later analogical removal; neither citation demonstrates the cause of Bede's front infinitive. |

Wash's full comparative input is the selected strong infinitive
`*wáskaną`, not `*wáskijaną`: its ending starts with *a*. The infinitive
can therefore undergo restoration, but not root i-umlaut conditioned by
its own ending. A front-vowel finite form is a possible analogical donor,
not proof that this transfer occurred. No distributional or dialectal
explanation of Bede's *wæscan* has been established in this short pass.

For mesh, the OE neuter classification does not establish PGmc gender.
`*máskō` conditionally projects an unlabialized neuter a-stem backwards;
`*máskwō` additionally assumes a neuter/wa-stem reclassification of
the labialized comparative material. Orel's m./f. *maskwō(n)* alone
licenses neither that transfer nor its date. The separately labelled
early-glide-loss diagnostic tests the subsequent, independently sourced
phonological bridge, not an attested intermediate or a selected input.
Written *x/cs* bears on the cluster separately from the root vowel;
plain *sc* does not settle palatality.

## Historical analysis

Scope: early English root-vowel history, not a chronology claim derived
from network names. Witness roles: wash and mesh are compatibility
controls where restoration already works; *wæscan* is a counterexample
requiring explanation; rest checks the proposed broader *st* condition.
No new chronology edge is asserted. Levelling remains a hypothesis, not
an inference from spelling variation alone; a regular account takes
priority only where it actually ties on evidence and economy.

## Verdict

DEFER production adoption; no registry verdict is changed.

Wash is compatible with both restoration and retention, not an
independent success for broader retention. Its securely contextual
*wæscan* infinitive remains unexplained by all four runs. Its inherited
ending has no triggering *i*: invoking finite *wæsċeþ* would require
an independently supported analogical transfer. Wright and Wright
themselves admit front/back doublets, so this rejects an unqualified
categorical implementation, not every possible formulation of their
published discussion.

Mesh is likewise nondiscriminating on the supported conditional routes:
the unlabialized neuter plural already restores *a*; the labialized
plural converges on it after independently sourced early glide loss.
Retaining that glide exposes an admission/implementation problem,
not evidence for the broader root condition. No supported reconstruction
of this accusative plural gives broader retention a unique success.
Using a feminine *-ōn* instead would change the attested cell, not solve
its history. The dative's ending failure cannot be counted as a match.

Recommendation for Flask: these controls leave the choice open.
They do not supply the missing independent evidence for narrow
`*skā#` retention, and this broader implementation additionally fails
the selected *ræste* control. The provisional regular-account preference
from the ashes pass is not a license to promote a condition without
establishing the evidential/economic tie. Keep *flasce* as comparator
and leave the production mismatch unresolved.

## Propagation (only after verdict)

Research note and reproducible evidence only. Production rules, selected
vocabulary, Flask target and protected baselines remain unchanged.
No full suite or publication rebuild.

Reproduce the isolated compile and all focused probes from the repository root:

```sh
python3 Germanic/docs/sound_changes/audits/wash-mesh-external-controls-evidence/experiment.py
```

Snapshot ID `wash-mesh-root-only-e7a9bed5` is immutable. On a rerun in
the same workspace choose a fresh ID in the driver; never overwrite
the sealed result. The adjacent `observed.json` preserves changed
relations, named checkpoints, raw rejections and all component hashes;
the sealed local snapshot retains full histories, receipts and the
pre-execution predictions document identified by its recorded SHA-256.

## Residue

Earlier-edition back-infinitive verification, the distribution of Bede's
front infinitive, and the comparative-to-neuter morphological bridge
remain distinct evidential questions.

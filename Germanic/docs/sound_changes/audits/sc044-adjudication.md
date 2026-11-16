# SC044: vowel-specific breaking and witness-specific chronology

## Identity

- SC id: SC044; executable identifier: `OEBreaking`.
- Branch: `research/sc044-breaking-adjudication`.
- Control: `54b15a2d3a764d5ac92c9ce0c1ecaf398aed878f`, the integrated
  mære/Flask state. Investigation begun 15 November 2026.
- This is the SC044 assignment only. No subsequent adjudication is begun.

## Question

The falsifiable hypothesis is that the selected short-front-vowel core is
sound, but unused back-a/quantity, lateral and stress clauses overgenerate,
and whole-rule displacement has been mistaken for a uniform historical
chronology. Independent witnesses can refute the proposed restrictions;
unchanged selected outputs alone cannot establish their historical truth.
The alternative late Anglian account must be allowed a genuinely different
prediction for mutation-created e, rather than merely another route to ea.

## Current state (before any edits)

The registry characterizes SC044 as `oe / english_specific`, confidence A,
`unadjudicated`, with a `reciprocal_or_near_reciprocal` chronology.
The executable composes A, E and I components under `FootCtx`, immediately
after stressed SC043 and its separately retained long-final support, and
before the voiceless SC045 component.

The original A component includes back a/á, front æ and a special direct
long outcome before x plus a weak tail. E includes general lx/lk/lg but not
lw. I already distinguishes an initial unmarked nucleus, explicit primary
í and preserved subordinate ì from plain weak medial i. There is no
long-front-vowel breaking component.

The selected inputs, comparators and input contexts are frozen. Flask is
nominative plural, with dative singular an independent external control;
mære retains its adopted final-nasal history. SC051, root fronting,
restoration, corpus admission and all approved migration chains are
controls, not variables in this adjudication.

The routed reader, chronology card and 042–048 dossier were read first.
The settled SC043 and SC045 memos are consulted at their last substantive
source commit `671edc53a247ab3fc5916c6d87dd39aecddde09d`; their 387-row
measurements are not relabelled as current. The older B/P packet belongs
to `67a18cfb`, before the current component and lexical changes.

## Diagnosis

The canonical `SC044 --evidence` rebuild reproduces all 394 production and
sandbox outputs: 386 matches, eight established mismatches, no rejections
or final ambiguities. A separately compiled pinned control agrees with
the frozen baseline in every record, not just its aggregate digest.

There are 50 selected firing rows: 29 A applications, all short æ, and
21 E applications, all short stressed é. Forty-nine are members of the
protected legacy-380 population resolved through the approved migration
chains; row 2336, earthly, is the additional E application. The three
learn rows already have é on entry. They are not I witnesses. No selected
firing tests E before l, I breaking, or back-a direct lengthening.
The complete stable-ID input/output/context census and 394-row comparison
are published with the independent experiment records.

The ordinary slay route is:

```
SC043       *s*l*á*x*a*n*ą   -> *s*l*æ*x*a*n*ą
SC044       *s*l*æ*x*a*n*ą   -> *s*l*ea*x*a*n*ą
h-loss      *s*l*ea*x*a*n    -> *s*l*ea*a*n
contraction *s*l*ea*a*n      -> *s*l*ēa*n
surface                              slēan
```

Breaking itself is short. The quantity question at contraction is not
answered by assigning a long diphthong at SC044.

The control's back-a clause produces both short and long outputs even
before bare x. For example, `*s*l*a*x` yields both `*s*l*ea*x` and
`*s*l*ēa*x`; `*s*l*á*x*a*n*ą` likewise has short and long alternatives.
Optional parentheses admit the empty nonweak continuation. Moreover,
a right context matching x can match the beginning of x plus a longer
tail; a context-language acceptance test alone does not establish
disjoint replacement environments. Both language recognition and actual
rewriting are therefore recorded.

The direct-long helper originated in
`740427ca8b40a53399d9e6539d7c2a31adc55b58`, then under
`server/fsts/germanic.txt`; `6449d01b` added its stressed counterpart.
The surrounding notes concern output/quantity workarounds, including
slay, rather than a cited short-a-to-long-breaking intermediate.
This provenance explains the code but is not historical warrant.

The independently constructed controls are labelled in `witnesses.tsv`.
They distinguish attested comparisons with reconstructed histories from
isolated stage-entry diagnostics. In particular, a rejected ordinary
input cannot be presented as a successful complete historical derivation.

The first candidate preserved all 394 records but failed the weak-E and
weak-long controls. Merely putting an initial-nucleus context beside
unrestricted marked-vowel replacements in the same parallel expression
did not enforce the intended distinction. The confirmatory packet places
the domains in separate compositions, as the existing I component does.
Its required weak A/E/I, weak selk, weak long-vowel, rj and following-i/j
negatives all pass, together with the marked-primary and subordinate-I
positives. This failed candidate remains in the archive; corpus parity
was not used to waive its failures.

The earlier displacement initially stopped at the production baseline
validator's correct rejection of transient cardinality drift. The
confirmatory research worker observes the counterfactual output sets
directly against pinned control records instead; it does not change,
refreeze or disable any production baseline protection.

The first full strict run then found two existing conditional-compound
regressions: seleweard became selewerd, and its subordinate root failed
to break in an isolated control. Acknowledging erased secondary stress
as a limitation was insufficient. The final candidate retains à/è until
their consumers and carries short fronted secondary à as precomposed ǽ.
A first carry trial exposed world wereald: its à missed the existing LH
a-to-u reduction. Letting that same weight condition read the annotated
a variant restores weorold without changing the environment. The final
independent trial preserves all 394 records, all prior weak negatives,
and all three conditional seleweard routes. No old expected output is
relaxed. The obsolete plain-æ stage diagnostic is updated to the actual
post-fronting secondary carrier, with its expected broken result unchanged.

A later strict replay identified two further compatibility assertions,
not selected-row changes. The frozen bounded-domain packet already admits
synthetic raw à as *à at the native gateway, but its old complete cascade
rejects it. The retained annotation now survives SC038 and final-a
deletion, fronts to ǽ and decodes to æ. Its first divergence is SC038
(*a versus *à). This is an explicitly disclosed noncorpus full-cascade
acceptance change, not an attested word or a new gateway admission; an
isolated secondary accent is not supplied as a defensible reconstruction.
The current regression checks both the unchanged parser result and the
new regular symbolic result rather than narrowing the sound law solely
to recover an accidental rejection of this synthetic string.

The live world migration replay also injected an old MWeakA hypothesis
whose plain-a target assumed the former SC038 decoding. Without notation
transport its two combined variants now give wereald, exactly the failed
carry experiment's diagnosis. The current replay therefore records and
applies only the explicit a-to-[a|à] target transport, leaving its LH
environment and the historical MIGRATION_DEFINITIONS constant unchanged.
Both literal grave-stage probes now reduce under the same condition;
the other 28 component controls and every selected final remain protected.
Historical packets, their negative grave probes and earlier counts are
not rewritten. The runtime regression compares production with the
transported component and retains every six-model corpus/legacy check.

## Literature

Checked sources and relevant locators:

- Campbell §§139–154, 157 and 234: vowel-specific environments, southern
  covered-l, the palatal-ll exclusion, restricted E laterals, short versus
  inherited long breaking, and contraction.
- Hogg, *Grammar*, pp.81–88, §§5.15–25, and pp.217–218, §§6.7–8:
  fronting/retraction alternatives, lx/lw and the disputed obliques,
  short-i positives, subordinate stress and genuinely weak negatives.
- Ringe–Taylor §§6.2–6.3, especially pp.177–178, 181–182, 184–190:
  slay, mihs and linhtaz, rj, liquid distinctions, pre-w breaking,
  and the conventional fronting/breaking/restoration account.
- Fulk 2018 pp.73–75, §4.13, including the contraction qualification
  in note 5.
- Hogg 1979 pp.90–92: feoh, the effective velar trigger and the distinction
  between phonetic palatal colouring and effective palatalization.
- Fulk 1998 pp.145–146: why the h argument does not date all k/g
  articulation; palatal ll and dialect-specific evidence.
- Versloot, online 2025, print 2026, §§3.3, 5.4–5.5 and 7:
  low-vowel alternatives and the late Anglian rC proposal.
- Pheifer p.22, no.402, and no.656 with p.103 commentary: manuscript
  readings and the qualified geormantlab etymology.

Pheifer's no.402 page image was inspected: Épinal has feormat, Erfurt
caeormad; the apparatus includes the Corpus feormat parallel. These are
not interchangeable diplomatic readings. Hogg p.86 and Fulk 1998 p.146
were also checked as page images rather than relying on font-damaged
text extraction. Hogg's sentence about exceptional selC mentions f while
also listing āseolcan; it must not be silently converted into a general
lk law. Campbell's narrower comparison and the independent melcan
negative are retained.

## Historical analysis

### Clause conclusions

| Clause | Historical assessment |
|---|---|
| Short æ before x and rC | Retain in the conventional stressed domain; slay independently fixes short quantity at breaking. Exclude rj. |
| Short æ before covered l | Retain the southern development, not an unrestricted all-dialect claim. Exclude the palatal ll of hell/sellan; earlier gemination retains a visible j in the actual representation. |
| Back a/á, especially direct long before x plus a weak tail | Remove from the conventional production component. There is no selected firing, and the historical account supplies front æ; the short-to-long shortcut and its overlapping contexts have no independent source warrant. A rival low-a analysis is tested separately, not smuggled in through this fallback. |
| E before lx | Retain: seolh/eolh are independent positives. |
| General E before lk | Restrict: āseolcan does not license meolcan for melcan. A narrowly preceding-s-conditioned proxy must be distinguished from proof of the ultimate historical mechanism. |
| General E before lg | No independent positive found. The old general clause is unwarranted by the checked evidence. |
| E before lw | Hogg and Ringe–Taylor provide a positive case for direct breaking in ġeolwe/meolwes. Back mutation of the nominatives plus transfer is an explicit competing analysis; surface diphthongs alone do not decide. |
| E before lf | Keep WS self/delfan distinct from non-WS seolf. No pan-OE lf rule follows. |
| I before x/rC and conditioned w | Retain the short-i phenomenon, with meox/Peohtas rather than learn as the positive evidence. The Anglian following-i/j restrictions are not identical to the WS domain. |
| I before lx | Hogg's single filhiþ history warrants the narrow lx extension. An independent positive confirms short í→ío there; ordinary weak i remains protected. It is not a general lC rule. |
| Weak medial vowels | Breaking is not an ordinary unstressed development. fulwiht/nawiht and no-w diagnostics distinguish stress from accompanying w-retraction. Initial plain vowels can remain stressed after accent consumption; preserved ì supplies a subordinate-stress diagnostic. |
| Noninitial plain A/E | Do not conflate genuine weak nuclei with subordinate roots. Retain low/front secondary annotation through fronting and breaking, while the existing weight-conditioned reduction still applies to the annotated a variant. The conditional seleweard positive and selected world negative enforce both requirements. |
| Short E before w | Retain cneowe and the following-i/j exclusion. Neither cnēo nor restored cnēow proves lengthening of the selected short dative. |
| Inherited long front vowels before x | Separate, source-supported long breaking: ǣ→ēa, ē→ēo and ī→īo. This is not a defence of short a→long ēa. The selected light verb is not the weight adjective. |

CAPR's phonological conditions are not lexical lists, grammatical classes
or probabilistic sound laws. Regular phonology has explanatory priority;
the existence of a published levelling account is reported without
treating mere possibility as positive proof of analogy. Hogg's argument
from the distribution of ġeolu is stronger evidence for direct lw breaking
than a naked statement that transfer could have occurred. The rival
account remains a real historical alternative.

The existing later `OEBackMutation` already produces diphthongs for both
tested lw obliques. Early lw breaking therefore is a source-motivated
placement, not a change required to fit those final strings. The full
nonselected controls independently improve milk meolcan→melcan, hell
hiell→hell and sell siellan→sellan. Slay stays slēan, both inherited
Flask routes stay flascan, and mære stays mære.

### Chronology and witness roles

The conventional stressed low-vowel part of SC043 feeds short æ-breaking.
It is this contribution, not SC107's unstressed member or SC108's
final-quantity support, that slay implicates. Moving the original bundle
early activates its back-a fallback; the separate front-only displacement
isolates the missing feeder from that artifact.

Fee and fight are bleeding/displacement negatives for SC045: short é
becomes éo while x remains x. Breaking thereby removes the front-vowel
context that would otherwise change x to ç; it does not destroy its own
velar trigger or feed a live SC045 application in those forms. Flax and
knight test the analogous low/e-vowel environments. Laugh is separate:
the second x of xxj really changes at SC045 because it stands next to j.
It is not another example of fee's nonapplication.

These are independently supported conventional precedence arguments,
not two independent reciprocal dates for entire executable bundles.
Hogg's feoh argument concerns effective h-palatalization. Fulk's objection
prevents promoting it into a date for every k/g articulation or into proof
that English and Frisian breaking were one inherited event.
The registry must reconcile both records of each reciprocal relation.
Older displacement counts remain dated observations, not current reruns.

| Executed comparison against 54b15a2d | Changed output sets | Ambiguous rows | Matches |
|---|---:|---:|---:|
| Original SC044 before SC043 | 29 | 29 | 385 |
| Front-only SC044 before SC043 | 26 | 0 | 360 |
| Original SC044 after SC045 | 12 | 0 | 374 |
| Final repaired candidate, unchanged order | 0 | 0 | 386 |

The first moved stage is inserted between SC107 and stressed SC043.
For slay it changes á to éa or ḗa before fronting can supply æ; h-loss
then leaves éaa or ḗaa, neither handled by the actual contraction
mapping. With that fallback removed, early breaking does nothing to á,
later fronting supplies æ, h-loss gives æa and final slæan remains.
Calf, swallow and yarn regain the same finals despite their different
intermediate histories in the front-only experiment.

The twelve later-displacement changes are flax fleax→flæhs; fee
feoh→feh; fight feohtan→fehtan; knight cniht→cneht; might miht→meht;
night niht→neht; slay slēan→slæan; six six→sehs; ten tēon→teon;
wax verb weaxan→wæhsan; wax noun weax→wæhs; laugh hliehhan→hlehhan.
In live laugh `*xlæxxjan- -> *xleaxxjan- -> *xleaxçjan-`;
reversal instead gives `*xlæççjan-` before breaking. No independent
early-SC045 run is claimed for the registry's reverse representation.

#### Front-only brightening displacement

The following is the complete word-by-word `front-before043` intervention,
not the ambiguous 29-row whole-rule trial. It moves fallback-free breaking
before stressed SC043 on the pinned `54b15a2d` control. These are archived
observations from `observed.json`, not new runs on the secondary-stress repair.
All 26 changed output sets are singleton; matches fall from 386 to 360.

| Concept | Selected input | Control | Displaced |
|---|---|---|---|
| belly | *bálgiz | bielġ | belġ |
| beard | *bárdaz | beard | bærd |
| flax | *fláxsą | fleax | flæhs |
| fall | *fállaną | feallan | fallan |
| fold | *fálθaną | fealdan | fældan |
| fern | *fárnaz | fearn | færn |
| gall | *gállô | ġealla | galla |
| malt | *máltaz | mealt | mælt |
| march | *márkō | mearc | mærc |
| might | *máxtiz | miht | meht |
| night | *náxti | niht | neht |
| slay | *sláxaną | slēan | slæan |
| spar | *spárrô | spearra | sparra |
| salve | *sálbō | sealf | sælf |
| salt | *sáltą | sealt | sælt |
| wield | *wáldaną | wealdan | wældan |
| wold | *wálθuz | weald | wæld |
| warp | *wárpą | wearp | wærp |
| wart | *wártōn | wearte | wærte |
| wax (verb) | *wáxsaną | weaxan | wæhsan |
| wax (noun) | *wáxsą | weax | wæhs |
| laugh | *xláxjaną | hliehhan | hlehhan |
| hold | *xáldaną | healdan | hældan |
| hall | *xállō | heall | hall |
| harvest | *xárbistuz | hierfest | herfest |
| harm | *xármaz | hearm | hærm |

#### Breaking after fricative palatalization

This is the separate complete `after045` intervention: original breaking
moved after voiceless fricative palatalization, on the same pinned control.
All twelve changed output sets are singleton; matches fall to 374.

| Concept | Selected input | Control | Displaced |
|---|---|---|---|
| flax | *fláxsą | fleax | flæhs |
| fee | *féx | feoh | feh |
| fight | *féxtaną | feohtan | fehtan |
| knight | *knéxtaz | cniht | cneht |
| might | *máxtiz | miht | meht |
| night | *náxti | niht | neht |
| slay | *sláxaną | slēan | slæan |
| six | *séxs | six | sehs |
| ten | *téxun | tēon | teon |
| wax (verb) | *wáxsaną | weaxan | wæhsan |
| wax (noun) | *wáxsą | weax | wæhs |
| laugh | *xláxjaną | hliehhan | hlehhan |

#### West Saxon vowel-order follow-up

The falsifiable question was whether the actual SC044/SC055 vowel
operations commute on the selected West Saxon inputs when consonants and
the surviving mutation trigger are held fixed. This follow-up retains
the existing verdict, order, corpus and production source: FST SHA-256
`74d13549dfce23dca7690d2b095ee0bbf6b550faf5816241c823343035de7c5b`.
The original complete census and its 50 phonological versus 51 mechanical
SC044 applications remain the before-state; no new census population or
chronology edge is adopted.

`west_saxon.py` uses manifest-validated production endpoints and cumulative
snapshots reached from the actual raw inputs. Both rows enter the finite
counterfactual immediately before `OEBreaking`, at the live
`EAFBrighteningLongFinal` output. Source, plan, worker, corpus and helper
hashes are pinned in the separate immutable experiment snapshot.

| Checkpoint | bielġ 'belly, bag', row 1945 | hliehhan 'laugh', row 2092 |
|---|---|---|
| Selected raw input | `bálgiz` | `xláxjaną` |
| After stressed brightening / common entry | `*b*æ*l*g*i` | `*x*l*æ*x*x*j*a*n*ą` |
| Live after SC044 | `*b*ea*l*g*i` | `*x*l*ea*x*x*j*a*n*ą` |
| Live after SC045 | `*b*ea*l*g*i` | `*x*l*ea*x*ç*j*a*n*ą` |
| Live after SC055 | `*b*ie*l*ʝ*i` | `*x*l*ie*x*ç*j*ą*n` |
| Live normal endpoint | `bielġ` | `hliehhan` |
| Local SC044 then SC055, no intervening rules | `*b*ie*l*g*i` | `*x*l*ie*x*x*j*a*n*ą` |
| Local SC055 alone | `*b*e*l*g*i` | `*x*l*e*x*x*j*a*n*ą` |
| Local SC055 then SC044, no intervening rules | `*b*e*l*g*i` | `*x*l*eo*x*x*j*a*n*ą` |

The local pairs have identical consonants and the same surviving i/j.
The early mutation gives e in both rows; revised e-breaking does not
break before lg, but does give eo before the still-velar fricative in
laugh. Thus the local reverse prediction is e for belly, not e for every
environment. Both rows distinguish the local operations from the live
West Saxon ie path. The current consonantal realization is not silently
substituted into one side of that controlled pair.

Two full live remainders distinguish vowel order from a consonantal
displacement effect. Write B for SC044, U for SC055, M for the unchanged
intervening sequence and T for the entire unchanged suffix after SC055.
The current order is B·M·U·T. The finite variants are U·B·M·T
(`mutation_early`) and M·U·B·T (`breaking_late`); each consumes the exact
two common-entry forms, not raw PGmc input.

| Full variant / checkpoint | Belly | Laugh |
|---|---|---|
| U·B·M·T after B | `*b*e*l*g*i` | `*x*l*eo*x*x*j*a*n*ą` |
| U·B·M·T after fricative palatalization | `*b*e*l*g*i` | `*x*l*eo*x*ç*j*a*n*ą` |
| U·B·M·T final | `belġ` | `hleohhan` |
| M·U·B·T after fricative palatalization, before U/B | `*b*æ*l*g*i` | `*x*l*æ*ç*ç*j*a*n*ą` |
| M·U·B·T after B | `*b*e*l*ʝ*i` | `*x*l*e*ç*ç*j*ą*n` |
| M·U·B·T final | `belġ` | `hlehhan` |

No rule restores ie in either reversed remainder. In particular the
recorded before/after `OEWsPalatalUmlaut` states are identical: its ht/hp/hs
environments are not the laugh cluster. Belly's two reversed experiments
converge on belġ; laugh's do not, because moving whole breaking past
SC045 also changes x·x·j to ç·ç·j, rather than the live x·ç·j.
The local breaking-first vowels agree with the live ie results despite
deliberately omitting intervening consonantal changes. Agreement of those
vowels is not identity of the complete intermediate strings.

Ringe and Taylor §6.6.3, pp.240–244, distinguish the West Saxon ie
outcomes of broken ea from non-West-Saxon outcomes. Their p.243 balgiz
example directly supports the covered-lateral vowel path; their p.240
laugh derivation already marks a palatalized geminate in the West
Germanic reconstruction. The PDF notation was checked visually. CAPR
instead retains xx through breaking and explicitly changes the
j-adjacent fricative afterwards. The experiments support these two
selected West Saxon vowel histories under the current formalization,
not the identity of those consonantal reconstructions or a global
reordering of every breaking/mutation component. Wierman and iermþ
remain literature examples, not unexecuted extra experimental witnesses.

The 16 November 2026 registry closeout records one independently
demonstrated, witness-scoped feeding relation, SC044 -> SC055. Bielġ
(row 1945) is the clearest witness: breaking supplies ea for mutation to
ie, whereas mutation first leaves e before lg and ends in belġ.
Hliehhan (row 2092) corroborates the vowel relation with hleohhan under
mutation-first; hlehhan belongs to the separate whole-breaking
displacement past fricative palatalization. This retains the adopted
rules and order; it asserts neither a reciprocal edge nor a universal
date outside these West Saxon vowel histories. The positive live
derivations, not merely a changed harness endpoint, establish feeding.

The source-bound comparison, capture receipts and final strict evidence
are preserved in the existing
[GitHub review bundle](https://github.com/nh36/caprWIP/releases/tag/sc044/west-saxon-612ffcae),
archive SHA-256
`f247041e8f6b1eceff62a6e1e0dfd7d457baa8772fd9d64d5631cb9ce7f8920e`.
The duplicate West Saxon ZIP is no longer tracked; `west_saxon.py` and
inspectable `west-saxon-observed.json` remain in Git. The live regression
runs from source, not that bundle. The original `experiments.zip` remains
byte identical (SHA-256
`64cdb3963efdc5d7612df52cda4611359c1a28ba6997dbcca8db192f4ec3b157`).
Its writer now verifies every required snapshot's inputs and completed
result hashes before replacing the archive or checksum. Temporary-directory
regressions remove either historical snapshot or corrupt a result and
require both published files to remain byte-identical; verified failed
trials are still included. This fixes the archive-review failure path
without regenerating the historical evidence.

The new live regression is
`test_sc044_adjudication.py::test_west_saxon_vowel_order_with_live_remainder`.
It compiles fourteen finite two-input networks in one call through the
matching isolated session image, with no private image preparation or
full-root/corpus variant. The first owning run measured 4.155 s in the
actual Foma child and 1,229,204 KiB peak RSS (`wait4`, Linux), 4.893 s
worker time and 5.97 s pytest call time. Shared fresh definitions took
452.490 s; the paired integrated selection, including both affected
SC037 owners and every SC044 control, passed 30 tests in 469.36 s.
These are measurements of that invocation, not a new global timing claim.

### A discriminating early Anglian test

The finite comparison explicitly gives the two histories different
predictions. With *farmjan- and mutation-created short e accepted, the
conventional early-breaking history gives æ→ea→e; a limited post-mutation
rm-breaking history gives æ→e→eo. The actual observed finite relations
produce these distinct outputs. Épinal feormat therefore favours the late
account under that reconstruction. It is not corpus parity masquerading
as discrimination, and not a result against the rival.

The Old English form is third-person singular present feormat 'fosters'
or 'nourishes', as Pheifer §70, p.lxxxii, explicitly parses it. No.402,
p.22, and its apparatus give Latin fouit in Épinal and Erfurt, against
fouet in Corpus. The Latin tense variants do not turn the Old English
form into a past tense. Lloyd and Lühr 2007, III, cols.492–493,
s.v. formôn (online article 45160, directly consulted), consider deriving
the verbs from original-e North-West-Germanic *ferma(n)- while expressly
retaining etymological difficulties. On that alternative either Anglian
order can yield eo; the farmjan-based contrast is not reconstruction-free
chronology evidence. This is a source alternative, not a new executable
trial or an unqualified adoption of a complete protoform.

Original-front *germ- can yield eo in both orders. Pheifer's qualification
of geormantlab's etymology and t remains important: the complete preform
is not independently certain merely because the rm comparison is useful.
The low-vowel gard~geard comparison tests whether back a or front æ was
supplied; it does not by itself identify mutation-created e. A sufficiently
limited late rm rule leaves uuerci and smeruui unbroken, unlike an
unrestricted extension of conventional e-before-rC breaking. The initial
finite teru probe had already vocalized w and was non-discriminating;
the confirmatory *terwu probe keeps consonantal w and yields eo under
the conventional relation but e under the bounded late relation.
Which was historically present at breaking is a separate premise, not
something recoverable from the spelling teru alone.
Published levelling from smeru is a genuine competing explanation of
smeruui, so that word is not an unqualified chronological disproof.

The finite experiment is not a complete Anglian cascade. It does not
establish a single environment from one convenient word, import
Versloot's lexical-diffusion/statistical machinery as a CAPR sound law,
or replace the WS account globally. Independent establishment of the
farmjan reconstruction, the vowel identity immediately before breaking,
and a wider regular Anglian rm distribution would decide how far the
late account should be extended. Later, differently conditioned Frisian
breaking supplies comparative plausibility, not a shared inherited date.

For the lateral negative, unbroken melcan rules out obligatory breaking
in that environment, not every reported broken variant. Wright and
Wright 1908 §84, p.46, list meolcan and Anglian melcan without a manuscript
locator. The original 1908 text was checked; the listing does not by
itself verify an attestation or the distribution of a particular token.
No independent manuscript claim is made here. The two weorold passages
now carry à to SC036's existing light-initial rewrite, and the laugh
article distinguishes the handbook's palatalized geminate reconstruction
from CAPR's explicit post-breaking j-adjacent rewrite.

## Verdict

REFORMULATE/RESTRICT the executable conditioning and historical claims;
RETAIN the supported short core, production order, stage/scope and core
confidence. Add the independently supported narrow I/lx and long-x
coverage. Do not adopt a global late-breaking reordering.

Registry-verdict: SC044=REFORMULATE/RESTRICT

The independent positives and negatives justify the vowel-specific
repair, not mere selected-corpus parity. The final candidate passes the
stress controls which refuted its predecessor, and improves the three
normal-entry lateral comparisons without changing any selected record.
The conventional chronology remains defensible for its actual witnesses,
while feormat gives positive conditional evidence for the rival Anglian
account. The proposed low-vowel history of that rival is not rejected by
removing an unsupported direct-phonemic-length shortcut.

## Propagation (only after verdict)

The exact SOURCE proposal comprises the production FST, SC044 registry
and inventory notes, both records of the two reciprocal relations,
SC043–045 reader passages, the current chronology card, 042–048 dossier,
live status, this memo and focused source-bound regressions. Original
pilot files, prior memos and frozen comparisons are not rewritten.
The unused weak-tail quantity helpers are removed rather than left
available for accidental recomposition. The directly dependent technical
annotation decoder and the existing weight rule read the carried variant;
this does not reopen their historical adjudications or add a new sound law.
SC043 fronts secondary à to short ǽ; SC044 breaks it where warranted and
decodes surviving low/front labels. The secondary è of selected thousand
therefore contributes annotation cleanup, not another historical breaking
witness. Keep that distinction from the 50 phonological control firings.

All 394 normalized inputs, contexts, comparators, output sets, match
statuses and multiplicities are identical to the frozen control:
394 accepted, 386 matches, the same eight mismatches, no rejections or
ambiguities. Output digest
`1bef3798e864ce1277511f9d9f6bf5c461dcbfa4608173849f4b467225e89727`
and protected legacy digest
`145b92fe89d055e8a14e900cc0755ac3f4f1219b5ba815e10d111a057a016624`
are unchanged. There is no baseline migration or lexical selection.

Reproducible evidence is in `sc044-breaking-evidence/`: `firing-census.tsv`
contains every stable ID and immediate input/output/context;
`corpus-comparison.tsv` contains every selected comparison; `observed.json`
contains the individual controls and all displacement deltas.
`experiments.zip` preserves both the partial main trial, including its
failure receipt, and the successful confirmatory snapshot with its exact
sources, recipes, probes, full outputs and authentic command receipts.
It contains no source-library PDFs.

Commands from the repository root:

```sh
python3 Germanic/tools/adjudicate.py SC044 --prepare
python3 Germanic/tools/adjudicate.py SC044 --evidence
python3 Germanic/docs/sound_changes/audits/sc044-breaking-evidence/experiment.py
# Supply that run's freshly prepared definition-image path:
python3 Germanic/docs/sound_changes/audits/sc044-breaking-evidence/repair.py --image /tmp/capr-sc044-image-38ba5a61/defined.bin
python3 Germanic/docs/sound_changes/audits/sc044-breaking-evidence/stress_carry.py
python3 Germanic/docs/sound_changes/audits/sc044-breaking-evidence/report.py .capr-work/experiments/sc044-breaking-3c1302e0 .capr-work/experiments/sc044-stress-repair-b407dd03 .capr-work/experiments/sc044-secondary-carry-dab50d5a
python3 Germanic/tools/adjudicate.py SC044 --finalize
python3 Germanic/tools/adjudicate.py --refresh
python3 Germanic/tools/adjudicate.py --status
INDEX_VERBORUM_STRICT=1 ASSEMBLY_KEEP_DEBUG_TEX=1 bash Germanic/docs/assembly/build_capr_book_draft_docker.sh
python3 Germanic/tools/run_portable_checks.py
cd Germanic/tests
python3 -m pytest -q --ignore=test_evidence_interface.py
python3 -m pytest -q test_evidence_interface.py
```

The first experimental runner intentionally retains its failed candidate
and protected-counterfactual stop; its process exit is not a scientific
success claim. The confirmatory runner records raw counterfactual sets
without asking production protection to approve them. A fresh replay
uses the newly printed snapshot IDs and validated image path, not these
machine-local operational names. Final certification is separate from
the scientific verdict and must use the unchanged final SOURCE state.

## Residue

The late Anglian interpretation is a substantive alternative, especially
for feormat, not disproved by keeping the conventional WS production
order. The lw analysis, precise scope of exceptional selk, the conditional compound reconstruction, and dialect-specific later developments
are separately qualified above. A raw long-ē probe without the model's stressed ē1
annotation is not a certified PGmc-to-WS nēah derivation; inherited-long
quantity is independently tested at explicit stage entry. Correcting that
annotation yields nēahw, exposing an additional w-loss question rather
than a complete scored nēah history. The weight adjective yields līoht,
an early spelling; no new later io/eo-merger claim follows. Meox breaks
correctly at SC044 but the current later palatal-umlaut rule still gives
mix; that nonselected downstream issue is disclosed, not fixed by
distorting SC044 or admitting a new scored row. The seal raw input still
rejects at the normal gateway, so seolh is specifically a source-backed
stage-entry positive, not a claimed new end-to-end admission.

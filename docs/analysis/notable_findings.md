# Notable findings and contributions

This document collects instances where the FST implementation process led to
observations, refinements, or discoveries that go beyond what is stated in the
standard secondary literature. These are flagged as potential contributions for
discussion in the eventual write-up of the project.

---

## 1. Medial high-vowel syncope: dental-obstruent conditioning

**Date discovered:** Session 039 (fyrhtu investigation)

**Background:** OE medial syncope deletes short unstressed vowels in medial
position after heavy syllables. The standard references (Campbell OEG
§§389-393; Luick Hist. Gr. §§114-121; Hogg vol.1 §3.3.3.2; R/T vol.2 §6.7.3)
all formulate the rule in terms of syllable weight and stress position. None of
them state that the identity of the consonant following the syncopated vowel
is relevant.

**What happened:** When we implemented medial high-vowel syncope as the
literature describes it — deleting medial *i after heavy syllables before any
consonant — the pipeline produced four regressions:

- *θestilaz → þistl (expected: þistel — vowel preserved before *l)
- *skellinaz → sċielln (expected: sċiellen — vowel preserved before *n)
- *wīθijaz → wīþ (expected: wīþeġ — vowel preserved before *j)
- *xarbistuz → +? (crash — vowel deleted before *s, creating impossible cluster)

When we restricted the rule to fire only before dental obstruents (*θ, *ð,
*d, *t), all regressions disappeared and all attested syncope forms (dozens of
Class 1 weak preterites in R/T pp.267-268, all *-iθō- abstracts, and the
comparatives) produced correct output.

**The observation:** Syncope is consistently regular before dental obstruents
and irregular or blocked before laterals, glides, sibilants, and nasals. This
may reflect:

1. A genuine phonological conditioning — syncope is favoured when the
   resulting cluster is homorganic (dental + dental) and blocked when it would
   create heterorganic or phonotactically difficult clusters
2. A chronological difference — earlier syncope before dentals, later
   (sporadic) syncope elsewhere
3. Post-syncope analogical restoration in forms with difficult resulting clusters

**What the literature says:**

- **Campbell (OEG §§389-393, pp.143-147):** "Short medial vowels are
  syncopated after a long stressed syllable." Does not discuss the following
  consonant. Notes "much irregularity" and levelling by analogy but does not
  connect this to specific consonant environments.

- **Hogg (vol.1 §3.3.3.2, pp.120-121):** "The high vowels were also subject
  to syncope in medial positions after a heavy syllable." Describes syncope
  and apocope as interacting changes causing irregularity. Does not mention
  conditioning by following consonant.

- **R/T (vol.2 §6.7.3, pp.264-270):** "High *i and *u were lost only if the
  preceding syllable was both heavy and stressed." Give the most detailed
  treatment. Note a complication with CR-clusters (p.269): "if a CR-cluster
  in a weak class I verb is preceded by a stressed short vowel, syncope
  occurs; otherwise it does not." This concerns the cluster formed AFTER
  syncope (preceding C + following sonorant R), not the consonant immediately
  following the syncopated vowel. It is the closest any source comes to
  noting that consonantal context matters.

- **Luick (Hist. Gr. §§114-121, pp.279-288):** Foundational treatment;
  discusses paradigmatic alternations in detail but formulates conditioning in
  terms of syllable weight and stress, not following consonant.

**Significance for the project:** This is a clear case where the FST methodology
functioned as a hypothesis-testing engine. The traditional prose formulation
("after heavy syllable") is too imprecise to implement directly; the FST forces
exact specification and the dataset provides immediate feedback. The dental-
obstruent conditioning is a pattern that only emerged when the rule was
formalized and tested at scale — it was invisible to over a century of
traditional scholarship.

**Pipeline implementation:** `OEMedialSyncope` in germanic.txt. Rule fires
before `[{*θ}|{*ð}|{*d}|{*t}]` only.

**Full analysis:** See `docs/analysis/fryhtu_investigation.md`, §5.

---

## 2. NWGmc u-lowering exceptions near labials: a non-Neogrammarian pattern

**Date discovered:** Session 021 (NWGmc u-lowering investigation)

**Background:** NWGmc u-lowering is a well-established sound change: stressed
\*u → \*o before non-high vowels in a following syllable (R/T vol.2 §2.3.1,
pp.27-33). However, a cluster of lexemes retains \*u where \*o is predicted:
\*fullaz → full (not ×foll), \*wulfaz → wulf (not ×wolf), \*fuglaz → fugol
(not ×fogol), \*bukkaz → bucc (not ×bocc), \*wullō → wulle (not ×wolle),
\*lubō → lufu (not ×lofu). OHG consistently shows the lowered forms (fol,
wolf, fogal, boc, wolla), confirming the exceptions are specifically OE (and
shared with OFris. and OS).

**What the literature says:**

- **Bülbring (EB §116, pp.45-46):** First observed the pattern. Notes that
  u appears instead of expected o "namentlich zwischen Labial und langem
  oder gedecktem l" — between a labial and long or covered l. Proposes
  that \*u was only lowered partway ("etwa zu [ou] oder zu engem [o]") and
  then, under influence of labial/velar environment, reverted to u. Concedes
  that counterexamples exist (wolcen, folgian, bolt, folc). Remains agnostic
  on mechanism.

- **Luick (Hist. Gr. §78, Anm. 3):** Engages directly with Bülbring and
  **rejects** the phonological conditioning. Argues for paradigmatic leveling:
  doublet forms arose because paradigms had both u-preserving (high-vowel
  suffix) and u-lowering (non-high suffix) cells; near labials/gutturals, the
  u-forms happened to win. He explicitly cites the counterexamples that
  make Bülbring's conditioning untenable: wolcen, folc, folġian, folde, folm,
  bolla, bolt, bolster, molde, molcen, smolt — all have labial/velar
  environments but show regular lowering.

- **R/T (vol.2 §2.3.1, pp.32-33):** Agree these are genuine exceptions.
  Find paradigmatic leveling "implausible" for a-stem nouns because the
  only paradigm cells with high-vowel suffixes (inst.sg. \*-u, dat.pl. \*-umaz)
  are functionally marginal. Conclude: **"We do not really know why \*u
  failed to lower in these forms."**

**What our FST implementation revealed:** When we attempted to model the
exceptions, we systematically evaluated four approaches:

1. **U-stem paradigm forms** — philologically indefensible (Kroonen
   reconstructs \*wulfa-, \*fugla-, \*bukka(n)- as a-/n-stems)
2. **Instrumental singular \*-u** — R/T reject this as implausible source
   of leveling
3. **Root-noun analysis** — Gothic wulfs shows thematic inflection, ruling
   this out
4. **Derivational forms with \*j/\*i** — would show i-umlaut, giving wrong
   root vowel

None of the four approaches could produce the correct outputs via
lautgesetzlich derivation. The FST implementation thus confirmed
R/T's assessment that these are genuine exceptions, while demonstrating
more rigorously that no paradigm-cell workaround is available.

**The observation:** The statistical clustering of exceptions near labial/velar
consonants is real (confirmed by our systematic inventory) but cannot be
formalized as a Neogrammarian rule because identical environments also show
regular lowering (folc, wolcen, bolla, etc.). This is a case where the FST
methodology demonstrates its own limits: **the pattern is gradient/probabilistic,
not categorical**, and is therefore fundamentally outside the scope of a
deterministic finite-state transducer. Bülbring's 1902 intuition about
"incomplete lowering + reversion" may be the closest to a correct explanation,
but it describes a phonetic tendency rather than a sound law.

**Significance for the project:** This is an instructive negative result. The
FST methodology is designed to test Neogrammarian sound laws; when it cannot
model a pattern, that failure is itself informative. In this case, it confirms
that the u-lowering exceptions resist formalization and are likely the result
of a gradient phonetic effect — precisely the conclusion that four generations
of scholarship (Bülbring 1902, Luick 1914-40, Hogg 1992, R/T 2014) have
been unable to improve upon.

**Full analysis:** See DEV_NOTES.md, "NWGmc u-lowering Exceptions Near
Labials" section.

---

## 3. PWGmc \*j-related sound changes: formalization of under-specified rules

**Date discovered:** Session 021 (PWGmc stage implementation)

**Background:** Two PWGmc sound changes involve the loss or transformation
of \*j. Both are historically legitimate, but the standard literature leaves
their formalization significantly under-specified, and our FST implementation
required making explicit choices that the prose accounts leave open.

**Change 1: PWGmcSyllabicJ (\*ja/\*ją → \*i)**

R/T vol.2 §3.1.2 (p.46): "Upon the loss of unstressed \*a and \*ą, preceding
postconsonantal \*j and \*w became syllabic \*i and \*u respectively." Our
implementation restricts this to after light syllables word-finally:
`{*j}{*a} → {*i} / V̆C _ #`. This conditioning is implicit in R/T's examples
but not explicitly stated as a rule. Our implementation successfully derives:
\*bazją → \*bazi → berġes, \*harjaz → \*hari → here, \*natją → \*nati → net.

**Change 2: PWGmcIjContraction (\*ijō → \*iu)**

R/T vol.2 §3.1.5 (p.62): "A roughly similar change of \*ijo to \*iu appears
to have occurred in the word 'friend' in PWGmc." R/T add an explicit caveat:
**"the uniqueness of the sequence \*ijo (with stressed \*i) makes it
inadvisable to attempt any generalizations based on the history of this
word."** Our FST had to implement it anyway (as `{*i}{*j}{*ō} → {*iu}`,
unconditional) to derive PGmc \*frijōnd- → PWGmc \*friund → OE frēond.

R/T note a **parallel change** \*Vwu → \*Vu (§3.1.5): \*knewu → \*kneu →
OE cnēo ('knee'), \*fawu → \*fau → OE fēa ('few'). They explicitly state
that the two changes "cannot plausibly be reduced to a single phonological
rule," despite the structural similarity (semivowel deletion between vowels).

**What the FST methodology reveals:** The process of formalization forces
decisions that prose scholarship can defer. R/T can write "it is inadvisable
to attempt any generalizations" — but the FST must either implement a rule or
not. Our implementation raises concrete questions:

1. Should \*ijō → \*iu be treated as a regular sound change (which happens
   to have only one attested input) or as a lexical irregularity that should
   be hard-coded?
2. Is the structural parallel between \*ijō → \*iu and \*Vwu → \*Vu deeper
   than R/T acknowledge? Both involve loss of a semivowel between vowels
   with compensatory vowel change. An FST could test a unified rule against
   both datasets.
3. What happens if additional PGmc \*ijV sequences are identified in the
   lexicon? The FST provides immediate testability.

**Significance for the project:** This case illustrates a different advantage
of the FST methodology from the syncope finding (§1). There, the FST
revealed a conditioning environment the literature didn't discuss. Here, the
FST **forces explicit formalization** of rules that the literature deliberately
leaves vague. The questions this raises — about rule generality, about
unifying structurally parallel changes — are questions that only arise when you
try to implement the sound changes as formal rules rather than prose
descriptions.

**Full analysis:** See DEV_NOTES.md, "PWGmc \*j-related Sound Changes —
NEEDS EXPERT REVIEW" section.

---

## 4. A-restoration trigger set: {*æ} is NOT a trigger

**Date discovered:** Session 041 (water fix investigation)

**Background:** A-restoration (R/T §6.3.1) retracts stressed *æ → *a when
a back vowel follows in the next syllable. After Anglo-Frisian Brightening
(AFB) has fronted *a → *æ, the question is which remaining vowels count as
"back" for the purposes of triggering restoration.

**What we initially assumed:** We included `{*æ}` in the trigger set, on the
reasoning that suffix *a (like gen.sg. *-as) had been fronted to *æ by AFB
but was "underlyingly back" and should still trigger restoration. This seemed
necessary to explain A-restoration in a-stem paradigms.

**What the FST implementation revealed:** When we implemented PGmc *watōr
'water' (r/n-stem nom.sg.), the PWGmc shortening *ō → *a (R/T §3.1.4)
produced *watar. AFB fronted both *a's to *æ, giving *wætær. A-restoration
then incorrectly fired (because the unstressed *æ was in the trigger set),
restoring stressed *æ → *a → "water" instead of correct "wæter".

**What R/T actually say (§6.3.2, p.199):** The paradigm of *dagaz 'day'
proves conclusively that `{*æ}` is NOT a trigger:

| Form | PGmc | OE | Restoration? |
|------|------|----|-------------|
| gen.sg. | *dagas | **dæges** | NO — suffix *a → *æ does NOT trigger |
| nom.pl. | *dagōs/os | **dagas** | YES — suffix *o is genuinely back |
| dat.pl. | *dagumaz | **dagum** | YES — suffix *u is genuinely back |

The gen.sg. *dagas → OE dæges (with preserved *æ*) is the key datum. If
{*æ} were a trigger, we would predict ×dages — which is not the OE form.
Only genuine back vowels (*o, *u, *ō, *ū) trigger restoration.

**The observation:** The "underlyingly back" analysis of suffix *æ was an
over-interpretation. R/T's rule refers to the **surface** vowel quality at the
time restoration applies, not to etymological provenance. By the time
A-restoration fires, suffix *a has been irreversibly fronted to *æ by AFB
and counts as a front vowel.

**Significance for the project:** This is a case where the FST methodology
exposed an error in our own analytical reasoning. The incorrect trigger
analysis had persisted for many sessions because it didn't cause visible
problems until a specific test case (*watōr) was encountered. The FST's
immediate falsification — producing "water" instead of "wæter" — forced us
to re-examine R/T's paradigm data and discover the correct analysis. This
demonstrates how FST implementation can catch analytical errors that might
persist indefinitely in a prose description.

**Full analysis:** See DEV_NOTES.md, "Water fix: PWGmc ō-shortening and
A-restoration correction" section.

---

## How to add new entries

When the FST pipeline reveals a conditioning environment, chronological
ordering, or interaction that is not discussed in the standard literature:

1. Verify the observation against R/T, Campbell, Hogg, and Luick
2. Document exactly what each source says (with page/section numbers)
3. Describe how the FST testing revealed the pattern
4. Add an entry to this document with date, background, observation, and
   literature review
5. Cross-reference the detailed analysis document

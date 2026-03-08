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

**Cross-referencing with additional sources (March 2026):**

The following sources were consulted to see whether they shed further light on
the dental-obstruent conditioning of medial syncope that our FST revealed.

- **Fulk (2018), §5.6 (pp.92–94):** Fulk's treatment is the most detailed
  comparative account now available and provides important indirect
  confirmation of our finding. He distinguishes two phases of medial vowel
  loss. In the first, high vowels (*i, *u) in medial open syllables after
  heavy syllables are lost — this is the standard "weight-based" formulation.
  In the second, a later prehistoric change, *i is lost after light syllables
  specifically "when the consonant following the vowel was l or r" (p.93:
  "micles 'large' < *mikilæs and betra 'better' < *batizô"). He then adds
  explicitly: "Loss of i (and u) before consonants other than l, r is less
  regular" (p.93), citing eg(e)sa, ef(e)sian, heolstor. And: "Syncope is
  constant in a few such words, e.g. eln, hwelc, twelf. It is generally
  absent when it would create a syllable coda with a disfavored sonority
  sequence, e.g. wæter 'water', bydel (PDE beadle)."

  This is highly significant. Fulk is the first comparatist to state
  explicitly (a) that l/r form a privileged class of following consonants for
  light-stem syncope, and (b) that syncope is blocked when it would create
  "a disfavored sonority sequence." This is a sonority-based constraint on
  syncope — exactly the type of conditioning our FST's dental-obstruent
  restriction captures, albeit from a different angle. Our finding that
  syncope after heavy syllables fires reliably before dental obstruents but
  not before other consonants is the mirror image of Fulk's observation
  about light syllables: in both cases, the phonotactic wellformedness of
  the resulting cluster determines whether syncope applies. Fulk does not
  make this connection to heavy-stem syncope explicitly, but his formulation
  for light stems strongly supports the principle that consonantal
  environment matters — contrary to the standard "weight-only" account.

- **Kaluza (1900–01), §72 (pp.124–126):** Kaluza's treatment is the oldest
  in our reference set and is formulated in purely weight-based terms. His
  rule (d): "Kurze Mittelvokale vor einfacher Konsonanz werden nach langer,
  vor l auch nach kurzer Stammsilbe ausgestossen" (short medial vowels
  before a single consonant are deleted after a long root syllable, and
  before l also after a short root syllable). This singles out *l* as a
  special following consonant for light-stem syncope — consistent with
  Fulk's later, more refined formulation. But Kaluza says nothing about the
  following consonant after heavy syllables. His examples for heavy-stem
  syncope (engles, dēofles, hālges, hīrde, dǣlde) all happen to have
  dental or lateral following consonants, which is consistent with our
  finding but is not noted by Kaluza as a conditioning factor.

- **Orel (2003):** Not relevant to this finding (etymological dictionary,
  does not discuss synchronic OE phonology).

- **Kluge/Seebold (2002):** Not relevant (German etymological dictionary).

**Assessment:** Fulk (2018) provides the strongest independent support for
our finding. His explicit recognition of sonority-based constraints on
syncope (for light stems) validates the principle that our FST discovered
independently (for heavy stems). The key new observation from cross-
referencing is that the two patterns — Fulk's "l/r privilege" for light
stems and our "dental-obstruent restriction" for heavy stems — are likely
two manifestations of a single underlying principle: **syncope is sensitive
to the phonotactic wellformedness of the resulting consonant cluster**. This
connection has not been drawn in the literature.

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

**Cross-referencing with additional sources (March 2026):**

- **Fulk (2018), §4.3 (pp.56–58):** Fulk gives the most detailed
  comparative treatment of u-lowering now available. He confirms the
  standard conditioning: "when u stood before a mid or low vowel in the
  next syllable...it was lowered to o" and that "lowering is prevented
  before a tautosyllabic nasal consonant" as well as "when j preceded the
  non-high vowel conditioning the change: cf. OE cnyssan 'knock', trymman
  'strengthen' (not †cnessan, †tremman) < *knusjanan, *trumjanan."

  Crucially, Fulk adds a **chronological argument** in footnote 1 (p.58),
  citing Ringe: this lowering occurred "before the loss of WGmc. *-az,
  since it is common in a-stem nouns but not root-stems (Ringe & Taylor
  2014: 27–34, at 29)." This chronological precision — u-lowering preceded
  *-az loss — is important for our pipeline ordering and suggests that the
  conditioning vowel was still present in the suffix at the time of
  lowering. However, Fulk says nothing about the labial/velar exceptions
  that are the subject of our finding. His examples (*skulō > scolu,
  *stulanaz > stolen, *ʒulþan > gold) are all regular cases.

  Also noteworthy is Fulk's observation that "heterosyllabic nasal" may
  also block lowering (OE fruma, guma, cuman retain u), "though OS and OHG
  show instances of o beside u." This adds another blocking environment
  not always mentioned in the standard accounts.

- **Orel (2003):** Orel's dictionary does not discuss the phonological
  conditioning of u-lowering. His entries for *fullaz (p.124) and *wulfaz
  (p.462) give the expected forms in each daughter language without
  commenting on why OE retains u. The dictionary format naturally precludes
  such discussion.

- **Kluge/Seebold (2002):** As a German etymological dictionary, this work
  consistently shows the lowered OHG forms (fol, wolf, fogal) that contrast
  with the OE retentions. This confirms the OE-specificity of the exceptions,
  since OHG lowered u regularly in precisely the environments where OE did
  not. Kluge/Seebold do not discuss the phenomenon as such.

- **Kaluza (1900–01):** Kaluza's treatment of stressed vowels (§§56–57) does
  not discuss u-lowering exceptions near labials. His account of *u > *o is
  integrated into the general vowel correspondences rather than being treated
  as a separate sound change with conditioning factors.

**Assessment:** Fulk's chronological argument (u-lowering before *-az loss)
and his additional blocking environment (heterosyllabic nasals) refine the
picture but do not resolve the labial/velar puzzle. The fact that the most
comprehensive modern comparative grammar (Fulk 2018) does not even mention
the labial exceptions — while R/T (2014) discuss them at length and
explicitly give up on explaining them — confirms our conclusion that these
exceptions remain genuinely unexplained. Our finding stands: the pattern
is real but resists Neogrammarian formalization.

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

**Cross-referencing with additional sources (March 2026):**

- **Fulk (2018), §5.8 (Sievers' law, pp.97–100) and §6.11 (WGmc consonant
  gemination, pp.98, 112–113):** Fulk provides the most thorough modern
  comparative treatment of the interaction between *j, syllable weight, and
  gemination. Several points are directly relevant to our finding:

  (a) On Sievers' law, Fulk confirms that "only i/j (and not u/w) attests
  to alternations" in Germanic and notes that "evidence for it is not found
  in all the environments in which it might be expected." This validates our
  observation that the rules governing *j-loss are under-specified.

  (b) On WGmc gemination, Fulk shows that it "occurs in OE ja- and jō-stems
  like fæstenn 'evening' < *fastunjaz and hæftenn 'captivity' < *xaftunjō,
  but not byrele 'cup-bearer' < *burilijaz or acc. sg. gydene 'goddess' <
  *ʒuðinijōn" (p.98), following Barrack (1998). This confirms that the
  heavy/light distinction governs gemination distribution, not just *j-loss.

  (c) Most importantly for our finding 3, Fulk notes explicitly that R/T's
  caveat about *ijō → *iu ("the uniqueness of the sequence *ijo...makes it
  inadvisable to attempt any generalizations") is connected to a broader
  problem: "the distinction between *-ij- and *-j- was eliminated in favor
  of the latter, certainly not in Proto-WGmc. itself" (p.99). This confirms
  that the merger of the two j-allomorphs was a gradual, dialect-specific
  process — exactly the situation that makes FST formalization difficult.

- **Kaluza (1900–01):** Kaluza's treatment of consonants does not discuss
  the *j-alternation in terms that connect to our formalization problem.
  His account of gemination (§§76–77) is descriptive rather than historical.

- **Orel (2003), Kluge/Seebold (2002):** Etymological dictionaries; do not
  discuss the phonological rules governing *j-behavior.

**Assessment:** Fulk (2018) substantially enriches the picture for this
finding. His account confirms that the formalization challenges we
encountered are genuine: the *j-alternation in Germanic is governed by
interacting factors (syllable weight, morphological class, dialect-specific
timing of the *ij/*j merger) that the standard prose accounts leave
deliberately vague. Fulk's explicit statement that the *ij/*j distinction
was eliminated "not in Proto-WGmc. itself" implies that any single-stage
FST rule will necessarily be an approximation. This is exactly what our
implementation experience showed.

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

**Cross-referencing with additional sources (March 2026):**

- **Fulk (2018), §4.12 (pp.72–74) and §4.13 (pp.74–76):** Fulk's treatment
  is particularly valuable for this finding because he uses different
  terminology from R/T but describes the same phenomenon, allowing us to
  confirm our analysis from a different scholarly tradition.

  Fulk does not use R/T's term "A-restoration." Instead he describes the
  process as part of the interaction between Anglo-Frisian Brightening
  (AFB) and subsequent retraction. His key passage (§4.13, p.76): "Before
  w, [æ] was retracted to [a], as in WS ge-sawen 'seen' and pret. pl.
  sāwon 'saw'. In open syllables it was also retracted before a back vowel
  in the following syllable, hence nom. pl. dagas 'days' (sg. dæg) and
  dat. pl. māgum 'kinsman' (nom. sg. mǣg), though ǣ is often found for ā."

  This passage confirms three things: (a) retraction/restoration occurs
  "before a back vowel in the following syllable" — the trigger must be a
  back vowel, not any vowel; (b) the gen.sg. dæges (not ×dages) is
  implicit in Fulk's paradigm (sg. dæg vs. pl. dagas), confirming that the
  fronted suffix vowel *æ does NOT trigger restoration; (c) Fulk adds the
  important caveat "though ǣ is often found for ā," suggesting that even
  in environments where restoration should apply, the fronted variant
  sometimes persists — a complication our pipeline does not currently model.

- **Kaluza (1900–01), §57 (pp.98–99):** Kaluza's account is the most
  explicit early formulation of the A-restoration condition and directly
  supports our finding. His rule (a): "Urg. a = ae. a in offener Silbe vor
  dunklem Vokal der folgenden Silbe" (PGmc *a = OE a in open syllable
  before a dark vowel in the following syllable). The key phrase is "vor
  dunklem Vokal" — before a DARK vowel. Kaluza's examples (dagas, fatu,
  gladu, faran, grafan) all have back suffixal vowels. He explicitly gives
  the gen.sg. as cræftas with æ (Anm. 1: "Zu cræft 'Kraft' lautet der
  Plural cræftas, cræfta, cræftum, weil hier geschlossene Silbe vorliegt")
  — but this concerns closed syllables, not the trigger question.

  Most importantly, Kaluza's rule (b) adds: "Urg. a bleibt auch
  unverändert, wenn der dunkle Vokal der folgenden Silbe durch
  Vokaldissimilation...in einen hellen übergegangen ist" (PGmc *a also
  remains unchanged when the dark vowel of the following syllable has
  become a light one through vowel dissimilation). This is the converse of
  our finding: Kaluza says that even when the surface suffixal vowel has
  been fronted (by dissimilation), the ORIGINAL back quality of the
  conditioning vowel still determines the outcome. His examples: hafela
  (*hafulā-), gaderian (*gadurōjan), macian (*macōjan). This appears to
  contradict our finding that {*æ} is not a trigger — but Kaluza is
  describing a different situation: these are cases where the suffixal
  vowel was *originally* back (ō, u) and was later fronted by
  dissimilation, NOT cases where AFB fronted an original *a. The distinction
  is between dissimilated dark > light (Kaluza's case, where restoration
  persists) and AFB-fronted *a > *æ (our case, where it does not). This
  is actually a further refinement: restoration is determined by the
  underlying quality at the time it applies, and AFB-fronted *æ counts
  as front, while dissimilated ō > e does not undo a prior restoration.

- **Orel (2003), Kluge/Seebold (2002):** Not relevant (etymological
  dictionaries; do not discuss OE-specific phonological conditioning).

**Assessment:** Both Fulk and Kaluza independently confirm the core of our
finding: A-restoration requires a genuinely back vowel in the following
syllable. Kaluza's additional observation about vowel dissimilation adds
an important nuance — restoration is determined by the vowel quality at
the time the rule applies, and different sources of fronting (AFB vs.
dissimilation) have different effects. Fulk's note that "ǣ is often found
for ā" even in restoration environments suggests that the process may
have been less categorical than our FST currently models. Both points
deserve further investigation.

---

## 5. The stefn/stemn problem: transponent versus reconstruction

**Date discovered:** Session 046 (stefn/stemn investigation)

**Background:** The word for 'voice' in Old English appears as stebn (earliest,
Corpus Glossary c.800), stefn (standard early OE, all dialects), and stemn
(late West Saxon only). The TSV originally had PGmc \*stamnăz — an ad hoc
a-stem masculine with root \*a that no source reconstructs. The pipeline
produced "stamn" with no mechanism to front the root vowel.

**What the FST implementation forced us to confront:** When we tried to fix
the mismatch, we discovered that the literature presents fundamentally
different Proto-Germanic reconstructions for this word:

- **R/T (2014, p.330):** \*stebnō (ō-stem f., e-grade, \*-bn- cluster)
- **Kroonen (2013, p.480):** \*stimnō- (heading; i-grade, \*-mn- cluster),
  but discusses \*stamnjo- (o-grade jō-stem with j-umlaut) as the "usual"
  derivation of OE stemn in the older literature
- The daughter languages split three ways on the medial cluster: \*-bn-
  (Gothic stibna, OE stebn/stefn), \*-mn- (OS stemna, OE stemn), \*-mm-
  (OHG stimma, OFri. stemme)

No single PGmc reconstruction straightforwardly accounts for all daughter
forms. The disagreement concerns root vocalism (e vs. i vs. o-grade), medial
consonantism (\*-bn- vs. \*-mn- vs. \*-mm-), and stem class (ō-stem vs.
jō-stem vs. thematized n-stem).

**The observation:** Implementing a historical transducer forces a distinction
that traditional comparative reconstruction can leave blurred:

**(a) What must be assumed locally for one daughter language** — a pre-OE
transponent that yields the correct output through regular sound changes.
For OE, this is \*stebn- (with root \*e and cluster \*-bn-), yielding stefn.

**(b) What is genuinely reconstructable for Proto-Germanic** — a single
ancestral form that feeds all daughter-language transducers and yields
correct output in each case.

These are not the same thing. The pre-OE transponent is well determined by
the OE evidence alone (the early attestation stebn, the chronological chain
stebn → stefn → stemn, the ME continuation stevne with -v- from -f-). But
the PGmc reconstruction requires weighing Gothic, OHG, OS, and OFri.
evidence — and the daughter languages disagree.

**Why this matters methodologically:** In traditional comparative
reconstruction, one can write "\*stebnō (or \*stimnō-)" and leave the
ambiguity unresolved. An FST pipeline cannot do this: it must have a single
input form that produces a single output. This forces the implementer to
choose — and in choosing, to make explicit exactly what is being claimed and
what is being deferred.

Our solution — using a pre-OE transponent rather than claiming to have
solved the PGmc reconstruction — is itself a methodological contribution.
It shows that FST-based historical phonology can proceed productively even
when the deeper reconstruction is disputed, by clearly separating the
daughter-language-internal derivation from the cross-branch reconstruction.

**Evidence that stemn is secondary (not primary):**
1. Earliest OE attestation is stebn (CorpGl c.800), not stemn
2. All OE dialects have stefn; only late WS has stemn (Bülbring §485)
3. Bülbring dates fn → mn to "Alfreds Zeit" (§62 Anm. 3)
4. ME stevne (with -v- < -f-) continues the fn-type, not the mn-type
   (Luick §347)
5. Parallel efn → emn 'even' (< \*ebnaz) shows the same chain (R/T p.330)

**Significance for the project:** This is perhaps the most important
methodological finding of the project so far. The previous findings (§§1–4)
showed how the FST revealed conditioning environments (§1), confirmed
non-Neogrammarian patterns (§2), forced formalization of vague rules (§3),
and caught analytical errors (§4). This finding goes further: it demonstrates
that the FST methodology requires — and rewards — a principled separation
between **local transponent** and **cross-branch reconstruction**. This
distinction, while implicit in good comparative practice, is rarely made
explicit in the literature because traditional methods do not force it.

**Future plan:** When OHG and Gothic transducers are built, this word will
serve as a cross-branch test case. If a single PGmc form can feed all
daughter transducers and yield the correct output in each, that form has
stronger support than any reconstruction based on comparative argument alone.
This item is flagged as a potential publishable finding.

**Full analysis:** See DEV_NOTES.md, "The stefn/stemn problem" dossier
(§§A–G).

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

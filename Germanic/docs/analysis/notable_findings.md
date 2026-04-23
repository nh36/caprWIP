# Notable findings and contributions

This document collects instances where the FST implementation process led to
observations, refinements, or discoveries that go beyond what is stated in the
standard secondary literature. These are flagged as potential contributions for
discussion in the eventual write-up of the project.

## Table of Contents

1. [Medial high-vowel syncope: dental-obstruent conditioning](#1-medial-high-vowel-syncope-dental-obstruent-conditioning)
2. [NWGmc u-lowering exceptions near labials: a non-Neogrammarian pattern](#2-nwgmc-u-lowering-exceptions-near-labials-a-non-neogrammarian-pattern)
3. [PWGmc \*j-related sound changes: formalization of under-specified rules](#3-pwgmc-j-related-sound-changes-formalization-of-under-specified-rules)
4. [A-restoration trigger set: {*æ} is NOT a trigger](#4-a-restoration-trigger-set-æ-is-not-a-trigger)
5. [The stefn/stemn problem: transponent versus reconstruction](#5-the-stefnstemn-problem-transponent-versus-reconstruction)
6. [PGmc stem-class disambiguation via OE phonology: \*kraft- and \*stab-](#6-pgmc-stem-class-disambiguation-via-oe-phonology-kraft--and-stab-)
7. [NWGmc \*i > \*e lowering: consonant-conditioned blocking and rule ordering](#7-nwgmc-i--e-lowering-consonant-conditioned-blocking-and-rule-ordering)
8. [PGmc \*þistilaz 'thistle': unresolved \*e/\*i reconstruction problem](#8-pgmc-þistilaz-thistle-unresolved-ei-reconstruction-problem)
9. [OE wīþiġ 'withy': ja-stem vs. -ig suffix problem](#9-oe-wīþiġ-withy-ja-stem-vs--ig-suffix-problem)

---

## 1. Medial high-vowel syncope: dental-obstruent conditioning

**Date discovered:** Session 039 (fyrhtu investigation)

**Background:** OE medial syncope deletes short unstressed vowels in medial
position after heavy syllables. The standard references (Campbell OEG
§§389-393; Luick Hist. Gr. §306; Hogg vol.1 §3.3.3.2; R/T vol.2 §6.7.3)
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

- **Campbell (OEG §§351, 388-393):** Campbell separates prehistoric and
  historical syncope. §351 gives the prehistoric rule: "i and u are also
  lost in open medial syllables after a long stressed syllable. This applies
  to original short vowels only, as i and u had not yet been shortened in
  this position." §388 restricts loss after short syllables: "Medial
  unaccented vowels are very freely dropped after short syllables, when the
  loss causes a group consisting of consonant + l or r to arise." §389
  extends sporadic loss to other clusters, but notes forms "mostly appear
  beside forms with preserved middle vowels." §392 on long-stem historical
  syncope: "After long accented syllables, all fully unaccented vowels had
  been lost in open medial syllables in prehistoric OE." The key footnote
  to §388 (fn.2) explicitly cross-references §351 and §341, separating the
  earlier syncope of i/u in open syllables from the later sporadic losses.
  Campbell does not discuss the identity of the following consonant as a
  conditioning factor.

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

- **Luick (Hist. Gr. §306, pp.283-285):** Foundational treatment;
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

The scholarly treatments of medial syncope differ in how much attention
they give to the consonantal environment of the syncopated vowel. The
older scholarship (Kaluza, Luick) formulates the rule almost entirely in
terms of syllable weight and stress, while the newer literature (Fulk, R/T)
increasingly acknowledges that the consonant following the syncopated
vowel plays a role — though none of them states this as directly as our
FST implementation forced us to do.

**Kaluza (1900–01), §72d (p.124):** The oldest treatment in our reference
set. His formulation is: "Kurze Mittelvokale vor einfacher Konsonanz werden
nach langer, vor l auch nach kurzer Stammsilbe ausgestossen" ('short medial
vowels before a single consonant are deleted after a long root syllable, and
before l also after a short root syllable'). For heavy stems, Kaluza's rule
is purely weight-based: the following consonant is not mentioned as
conditioning. But for light stems, he singles out *l* as a special
environment: syncope before *l* after short stems (e.g. *micles*, *yfles*),
but not before other consonants (§72e: "Kurze Mittelvokale vor einfacher
Konsonanz (ausser l) bleiben nach kurzer erster Silbe erhalten: wæteres,
æceres..."). The fact that Kaluza already treats the following consonant as
relevant for light stems — but not for heavy — raises an obvious question:
is heavy-stem syncope really insensitive to the following consonant, or
did Kaluza simply not notice the pattern? His own heavy-stem examples
(engles, dēofles, hālges, hīrde, dǣlde) all have *l* or *d* following
the syncopated vowel, which is consistent with our dental/lateral
restriction but happens not to include any counterexamples.

**Luick (1914–40), §306 (pp.283–285):** Luick's formulation is also
weight-based: "sie fielen nach langer Tonsilbe aus und blieben nach
kurzer erhalten" ('they fell after a long stressed syllable and were
preserved after a short one'). Like Kaluza, he restricts light-stem
syncope by following consonant: his Anm. 1 gives byrela, staðoles as
forms where syncope does NOT apply after a short syllable (before
sonorants other than *l*). His Anm. 2 makes the crucial observation that
syncope applies "nur für offene Mittelsilben" ('only in open medial
syllables') — i.e. it is blocked when the post-vocalic consonant is itself
followed by another consonant closing the syllable: "daher noch in
historischer Zeit costinga, -unga plur. 'Versuchungen', āresta 'erste',
mennisce 'menschlich'." But he then qualifies this: when the consonant
cluster "zur Folgesilbe gezogen werden kann" ('can be drawn to the
following syllable'), like *st*, syncope applies anyway: "hīehsta 'höchste',
nīehsta, wiersta, lǣsta." This is a phonotactic constraint — it depends on
whether the resulting cluster is syllabifiable — which is closely related to
our observation that syncope fires reliably before dental obstruents.

**R/T (2014), §6.7.3 (pp.264–270):** R/T provide the most extensive
exemplification. Their main rule: "high *i and *u were lost only if the
preceding syllable was both heavy and stressed." They then note a
significant complication with CR-clusters (p.269): "if a CR-cluster in a
weak class I verb is preceded by a stressed short vowel, syncope occurs;
otherwise it does not." Their data (p.268–269): syncope occurs in
*þrysmde* 'choked', *wyrsmde* 'festered', *nemde* 'named' (before
nasal), and in *eglde* 'afflicted', *siglde* 'sailed' (before *l* after *g*),
but NOT in *bytledon* 'built', *symblede* 'feasted', *wrixledon*
'exchanged' (before *l* after obstruent), and never before *r*:
*āfréfredon* 'consoled', *timbrede* 'built'. R/T call this constraint
"admittedly odd: we might have expected all heavy syllables to behave
similarly." This is the closest any source comes to noting that consonantal
context affects syncope after heavy syllables.

The differences between the scholars can be tabulated:

| Scholar | Heavy-stem rule | Light-stem rule | Following C noted? |
|---------|----------------|-----------------|-------------------|
| Kaluza (1900) | after long syllable | before *l* only | for light stems only |
| Luick (1914) | after long syllable, open syllable | similar to Kaluza | phonotactic constraint on clusters (Anm. 2) |
| Campbell (1962) | after heavy syllable (open syllable, §351); sporadic elsewhere (§§389-393) | before l/r only (§388) | consonant+l/r for light stems (§388); not discussed for heavy |
| Hogg (1992) | after heavy syllable | — | not discussed |
| R/T (2014) | after heavy + stressed | CR-cluster complication | for preterites only (CR-clusters) |
| Fulk (2018) | after heavy syllable | before *l* or *r* | sonority constraint |

**Fulk (2018), §5.6 (pp.92–94):** Fulk's treatment synthesises the earlier
accounts but goes further. For light stems, he extends Kaluza's l-only
rule to include *r*: "already at a prehistoric date there was loss of i in
such an environment when the consonant following the vowel was l or r,
as in gen. sg. masc. micles 'large' < *mikilæs and betra 'better' <
*batizô" (p.93). He then adds: "Loss of i (and u) before consonants
other than l, r is less regular, e.g. eg(e)sa 'fear', ef(e)sian 'shear',
heolstor 'darkness'." And the key sentence: "It is generally absent when
it would create a syllable coda with a disfavored sonority sequence, e.g.
wæter 'water', bydel (PDE beadle)."

This is a genuinely new formulation. Where Kaluza and Luick described
the constraint descriptively (before *l*, in open syllables), Fulk states
the underlying principle: syncope is constrained by the **sonority** of the
resulting cluster. A cluster like *-dl-* (bydel → ×bydl) violates sonority
sequencing (stop before lateral); a cluster like *-cl-* (micles) or *-tr-*
(betra) does not. Wæter is a light-stem case where the following consonant
is *t*, not *l* or *r*, so Kaluza's and Fulk's light-stem restriction
predicts non-syncope directly.

**Implications for our implementation:** Our FST restricts syncope to fire
before dental obstruents `[{*θ}|{*ð}|{*d}|{*t}]`. This works empirically,
but the sources suggest two alternative analyses:

1. **Luick's "open syllable" analysis:** Syncope applies only in open medial
   syllables. This would predict syncope before single consonants that can
   form a well-formed onset with what follows, i.e. precisely the clusters
   that obey sonority sequencing. Our dental-obstruent restriction might be
   a subset of this.

2. **Fulk's "sonority" analysis:** Syncope is blocked when the resulting
   coda would have a disfavored sonority profile. This is a more general
   version of our restriction.

Both analyses predict our observed pattern but also predict cases where
our rule is too restrictive (blocking syncope before, say, *s* in *hīehsta*)
or not restrictive enough. A more principled FST implementation might
test Fulk's sonority constraint directly, but the current dental-obstruent
restriction is a good first approximation and has no known regressions.

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
of a gradient phonetic effect — precisely the conclusion that successive
generations of scholarship (Bülbring 1902, Luick 1914–40, R/T 2014) have
been unable to improve upon.

**Full analysis:** See DEV_NOTES.md, "NWGmc u-lowering Exceptions Near
Labials" section.

**Cross-referencing with additional sources (March 2026):**

The basic lowering rule is uncontroversial: PGmc *u > *o before a non-high
vowel in the following syllable. What is at issue is how to explain the
residual cases where *u survives — specifically *fullaz, *wulfaz, *fuglaz —
and whether any Neogrammarian conditioning can capture them.

**Bülbring (1902), §116** provides the only explicit phonological
conditioning ever proposed. He observes that *u is retained "namentlich
zwischen Labial und langem oder gedecktem l" ('especially between a
labial and long or covered l'): full, wulle, wulf, fugol, bucca, murcnian,
murnan. But he concedes that the regular outcome is o in the same
consonantal environments: "Meist steht jedoch der Hauptregel gemäß o:
wolcen, folc, folʒian, folde, folm, bolla, bolt, bolster, molde, molcen,
smolt." His solution is that the lowering was incomplete — a half-way
realisation to "[ou] oder zu engem [o]" — which under influence of
surrounding labials and velars reverted to u. This amounts to a phonetic
plausibility argument, not a rule: there is no formalisable distinction
between *fullaz (retained) and *fulkam (lowered to OE folc), since both have a labial
onset and velar/lateral continuation.

**Luick (1914–40), §78 Anm. 3** directly rejects Bülbring. His reasoning
is worth quoting in full: "Ein Lautwandel aber, der o 'zwischen Labial und
langem oder gedecktem l' zu u werden ließ...ist schwerlich anzunehmen, da
auch bei dieser Konsonantengruppierung gewöhnlich o gilt: wolcen 'Wolke',
folc 'Volk', folʒian 'folgen', folde 'Erde', folm 'Handfläche', bolla
'Schale', bolt 'Pfeil', bolster 'Polster', molde 'Erde', molcen 'geronnene
Milch', smolt 'heiter'." Luick's counterexamples are devastating: they show
that the supposedly conditioning environment (labial + covered l) produces
regular lowering in the majority of cases. His alternative is paradigmatic
levelling: in most inflectional types, high and mid vowels alternated in
the endings, and "die konsonantische Umgebung mag insofern von Belang
gewesen sein, als, wenn Doppelformen entstanden, bei den Wörtern mit l
und Labial oder Guttural die u-Formen nicht selten den Vorzug erhielten"
('the consonantal environment may have been relevant insofar as, when
doublets arose, in words with l and labial or guttural the u-forms not
infrequently won out'). This reframes the problem as lexical selection
among analogical variants, not as a sound law.

**R/T (2014), §2.3.1 (pp.27–34)** engage the problem at greatest length.
They carefully separate genuinely unexplained retentions from forms that
can be explained by paradigmatic levelling. For instance, OE lufian 'love'
could owe its u to nom.sg. lufu with *-ō > *-u; OE wulle 'wool' could have
levelled from *wullō; OE spurnan 'kick' from 3sg. *spurniþi where *u was
not before a low vowel. "But when all such examples are excluded we are
left with a few inherited words in which *u was not lowered in northern
WGmc, usually in the neighborhood of a labial fricative or *w and *l"
(p.33): *fullaz, *wulfaz, *fuglaz, *tulga-. Yet counterexamples in
identical environments — *fulmō > OE folm, *fulkam > OE folc, *fulgijan- >
OE folgian — make a sound law impossible. R/T conclude: "We do not really
know why *u failed to lower in these forms" (p.34). This is an explicit
concession that no Neogrammarian account is available.

**Fulk (2018), §4.3 (pp.56–58)** gives the most systematic comparative
treatment. He confirms the standard blocking environments — tautosyllabic
nasals ("OE pp. wunden 'wound' < *wundanaz"), heterosyllabic nasals ("OE
fruma 'beginning', guma 'man', cuman 'come', though OS and OHG show
instances of o beside u"), and preceding *j ("OE cnyssan 'knock', trymman
'strengthen' (not †cnessan, †tremman) < *knusjanan, *trumjanan"). He also
provides a chronological anchor in fn.1, citing R/T: lowering occurred
"before the loss of WGmc. *-az, since it is common in a-stem nouns but
not root-stems." But Fulk says nothing about the labial/velar exceptions.
The silence is itself informative: the most comprehensive modern comparative
grammar treats these cases as beneath notice or beyond explanation.

**Campbell (1962), §§115–118** treats the same change as part of the PGmc
vowel system: "u > o before mid and low vowels. In OE forms this change
occurs with considerable regularity, e.g. dohtor daughter, god god, gold
gold, geoc yoke, and passive participles of strong verbs of Classes II,
III, and IV, e.g. coren, boren, holpen." But he immediately notes the
exceptions: "There are, however, many exceptions in OE, which have
preserved u, very often where other West Gmc. languages, especially OHG,
have o, e.g. full full, fugol bird, bucca buck, wulf wolf, ufan from above,
OHG foll, fogal, boch, wolf, obana." Campbell then adds a detail others
miss: "Even within OE itself, there is variation in some words, e.g.
cnocian knock, spora spur, spornan spurn, beside cnucian, spura, spurnan."
§116 provides the nasal blocking: before nasal + consonant, "u is retained,
and e > i irrespective of what vowel follows." §117 extends this to single
*m* (niman, cuman, guma, sumor) and §118 notes a similar tendency before
single *n* (þunor, wunað, hunig). Campbell's OHG comparison — "OHG foll,
fogal, boch, wolf, obana" vs. OE full, fugol, bucca, wulf, ufan — is the
most direct statement in any of our sources that OE is exceptional here
while OHG shows regular lowering.

**The OHG contrast is instructive.** OHG consistently has the lowered
outcome in precisely the environments where OE retains *u: OHG fol, wolf,
fogal vs. OE full, wulf, fugol. The Kluge/Seebold entries for these words
show the OHG forms without comment. Campbell (§115) provides this comparison
directly. If Bülbring's labial conditioning were correct, it should apply
equally in OHG, which shares the consonantal environment. It does not,
which further undermines any universal phonetic explanation. Luick (Anm. 1)
notes this explicitly: "während das Althochdeutsche durchweg o bietet:
wolf, vogal, voll."

**Implications for the FST:** The sources agree on the basic rule but
diverge sharply on the residual exceptions:

| Scholar | Position on exceptions |
|---------|----------------------|
| Bülbring (1902) | Labial/velar environment blocks full lowering (phonological) |
| Campbell (1962) | Lists exceptions, notes OHG contrast; no explanation offered |
| Luick (1914) | Paradigmatic levelling; consonantal environment selects among doublets |
| R/T (2014) | Genuinely unexplained; "we do not really know" |
| Fulk (2018) | Not discussed |

For our pipeline, the exceptions cannot be captured by a general rule.
Following R/T's honest assessment, we treat the basic lowering as a
regular sound law and handle the handful of exceptions by marking them as
documented irregularities in the TSV. A Bülbring-style labial-blocking
rule would produce more regressions than fixes, since forms like *folkam,
*fulmō, *fulgijan- all show regular lowering in identical environments.

### Expert consultation (Stefan Schuhmacher, Vienna, 2026-03-20)

We consulted Prof. Stefan Schuhmacher (University of Vienna) on the u-lowering
exceptions. His response provides important terminological and empirical
clarifications:

**On terminology:** Schuhmacher prefers "Lowering of high vowels" or "Lowering
of \*u" over the traditional "a-Umlaut" (German *a-Umlaut*).

**On the scope of the rule:** "To begin with, it must be mentioned that such
lowering **affects only stressed vowels**... I do not see that the lowering
affects unstressed vowels such as the middle vowel in the word for 'widow'."
This confirms our implementation, which restricts u-lowering to stressed
syllables.

**On the labial environment exceptions:** "In these words the erstwhile *u is
preceded by bilabial /w/ and /b/ or by labiodental /f/. I have always been
inclined to think that the preceding /w/, /b/, /f/ blocked the lowering but
as far as I remember, **there are lots of counterexamples**." This aligns with
Luick's position. Schuhmacher adds: "Others have wondered whether there were
places in the paradigm of these words where lowering did not occur, such as
the instrumental singular (e.g., \*wulfu) or the dative plural (e.g., \*wulfum)
but this strikes me as not very attractive." He notes no solution exists.

**On the OHG contrast:** "I must mention that Franconian/Alemannic/Bavarian
here **consistently have /o/**, i.e. 'Old High German' fol, wolf, fogal, boc."
This confirms Campbell's observation that OE is exceptional here while
continental WGmc shows regular lowering.

**On bucc specifically:** "There may be additional complications such as the
possibility that *bucc* originally may have been a u-stem word, in which case
the vowel of Old English *bucc* would be what we expect." This is a potential
explanation for one exception that we had not fully considered.

**Follow-up research on bucc stem-class (2026-03-20):** We checked Kroonen
(EDPG, p.82) and Kluge-Seebold (s.v. "Bock") on this question:

- **Kroonen** reconstructs \*bukka(n)- as an **n-stem** (not u-stem): "Most of
  the evidence points to a thematic form \*bukka-, but in view of the gemination
  of the final consonant it seems likely that the word was originally inflected
  as an **n-stem**, viz. \*bukō, gen. \*bukkaz." The gemination (\*-kk-) reflects
  the n-stem genitive \*-n-os > \*-az with Kluge's Law ("spontaneous gemination").
  He derives it from PIE \*bhug-ōn, gen. \*bhug-n-ós.

- **Kluge-Seebold** notes: "ae. bucca (n-Stamm, neben bucc 'Rehbock')" — i.e., OE
  had **both** an n-stem (bucca) and an a-stem (bucc), confirming the word's
  complex inflectional history.

**Assessment:** Kroonen's reconstruction is n-stem, not u-stem. However,
Schuhmacher's suggestion could still be valid if there was an earlier u-stem
stage (\*buku-?) before the n-stem formation, or if some dialects preserved a
u-stem variant. The word's IE cognates (Av. būza-, Arm. bowc) show no n-stem
suffix, so the n-stem formation is Germanic. Whether a u-stem variant existed
alongside the n-stem would require more investigation. For now, we note:
1. The n-stem reconstruction explains the gemination via Kluge's Law
2. Schuhmacher's u-stem hypothesis remains unverified but not disproven
3. Either stem-class might explain retention of \*u if the paradigm lacked
   lowering-triggering vowels in certain forms

**On the character of the exceptions:** "It does hurt our Neogrammarian pride
that what looks like a full-blown sound law (and not just a 'tendency') seems
to have some exceptions." This candidly acknowledges the problem.

**On \*i-lowering (parallel change):** "As for the expected parallel lowering
of \*i > e, this is really no more than a 'tendency' (my apologies for the
vague term). That is, *nest* and *wer* 'man' are the usual suspects but no one
has been able to mention a substantial number of other candidates for such
lowering. **Such lowering simply seems not to happen across the board.**
Unpleasant as it is, this is the way it is."

**Summary from Schuhmacher:**
- "\*u is lowered in most of the cases where we would expect it but does not always take place, for whatever reason."
- "\*i is not usually lowered but there are at least *nest* and *wer* where it did happen."
- "As far as I can see, **lowering is only found in stressed vowels** so there is no need to bother about the development of words like \*furxtiθō. \*u is not lowered here (because an \*i follows, which itself is not lowered), and later the \*u is fronted to y precisely because of the \*i."

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

The rules governing *j in the transition from PGmc to PWGmc interact with
at least three distinct phenomena: Sievers' law (the *ij/*j alternation
conditioned by syllable weight), WGmc consonant gemination (*Cj > *CC),
and the loss of *j after unstressed vowels. The sources treat these as
separate problems, but for the FST they converge in a single module that
must handle all *j-bearing forms.

**R/T (2014), §3.1.2 (pp.44–48):** R/T provide the foundational ordering.
Upon loss of word-final *-a and *-ă, "preceding postconsonantal *j and *w
became syllabic *i and *u respectively, and preceding *ij > *ī." Their
examples: *harjaz > PWGmc *hari (> OE here), *hirdijaz > PWGmc *hirdi
(> OE hierde), *arbija > PWGmc *arbi (> OE ierfe). The ordering is
crucial: "that this change preceded the WGmc gemination *Cj > *CC is
demonstrated by facts of two kinds": (a) some OE i-stems develop ja-stem
byforms, e.g. *matiz 'food' > PWGmc *mati, reanalysed as *matja-, whence
OE mettas pl. with -tt- < *-tj-, alongside sg. mete without gemination;
(b) relic OHG spellings like beti 'bed' < PWGmc *badi < PGmc *badja show
the ungeminated stage preserved. This means the pipeline must apply
*j-vocalisation BEFORE gemination, which is what we do.

For the *ijō → *iu change (PGmc *frijōnd- → PWGmc *friund → OE frēond),
R/T are explicit about their uncertainty (§3.1.5, p.62): "the uniqueness
of the sequence *ijō (with stressed *i) makes it inadvisable to attempt any
generalizations based on the history of this word." They note a parallel
change *Vwu → *Vu (*knewu → *kneu → OE cnēo), but insist the two
"cannot plausibly be reduced to a single phonological rule."

**Fulk (2018), §5.8 (pp.97–100):** Fulk's treatment of Sievers' law
provides the theoretical context that R/T's ordered-rules account leaves
implicit. On the alternation itself: "In Gmc. only i/j (and not u/w)
attests to alternations of this type, and evidence for it is not found in
all the environments in which it might be expected." The examples are
instructive: Go. ja-stem gen.sg. harjis 'army' (light stem: *j retained)
vs. hairdeis 'herdsman' (heavy stem: *ij > *i), but jō-stems show no
alternation at all ("there is no inflectional difference between, e.g.,
bandi 'band' and mawi 'maiden'"), and even ja-stems have exceptions:
"gen.sg. arbjis 'heritage' for expected *arbeis."

On WGmc gemination, Fulk gives the distributional data that matters for
our pipeline: gemination "occurs in OE ja- and jō-stems like fæstenn
'evening' < *fastunjaz...but not byrele 'cup-bearer' < *burilijaz or
acc.sg. gydene 'goddess' < *ʒuðinijōn" (p.98, citing Barrack 1998). This
is Sievers' law applied to gemination: after a heavy initial syllable in a
disyllable, *-ij- (not *-j-) appears, and *-ij- does not geminate.

The key sentence for our finding 3 is Fulk's chronological note (p.99):
"the distinction between *-ij- and *-j- was eliminated in favor of the
latter, certainly not in Proto-WGmc. itself, given NSGmc. changes to weak
verbs (Ringe & Taylor 2014: 156–7)." This means that at the stage our
pipeline operates — PWGmc to pre-OE — the *ij/*j alternation had not yet
been fully resolved. Any single-stage FST rule for *j-loss is therefore
an approximation of what was in reality a gradual dialect-specific process.

**Campbell (1962), §§407–408:** Campbell gives the OE-internal data on
gemination with direct quotation. §407: "W. Gmc. consonant doubling is
particularly strongly developed before j, every consonant except r being
affected after short syllables." His examples: "many weak verbs of Class I,
as sellan give, fremman do, þennan stretch, clyppan embrace, settan set,
cnyssan knock, wecċan awake; nouns and adjs. of the ja-, jō-, and jan-/jōn-
declensions, as cynn race (cf. Goth. g.s. kunjis), sibb relationship, wrecċa
exile." On the r-exception: "But r was not doubled, whether original or from
z (§404), and -rj- remained in OE, e.g. nerian save, herias armies (Goth.
nasjan, harjēs)." On voicing consequences: "When doubled, v and ʒ became
the corresponding stops, bb and gg (written in OE cg), e.g. OE hebban raise,
licgan lie < *ɣaƀjan, *liʒjan." §408 extends doubling to liquids: "There
was clearly already in West. Gmc. extensive doubling of consonants before l
and r after short vowels, for there is evidence in all the languages, e.g.
OS appul apple, OHG snottar wise, OE æppel, snottor." Campbell's footnote
to §407 challenges the standard account of n-gemination, citing Krahe and
Martinet against the view that "double consonants in weak nouns such as OE
docga, sugga, crabba...are due to West Gmc. gemination before n."

**Implications for the FST:** The pipeline currently handles *j through a
sequence of ordered rules: (1) *-ja-/*-ją- > *-i-/*-u- after loss of final
vowels; (2) *Cj > *CC (gemination) in remaining environments; (3) the
*ijō > *iu special case. The sources confirm that this ordering is
correct: vocalisation feeds reanalysis which feeds gemination (R/T's
explicit argument). But the *ij/*j alternation, which Fulk shows was not
yet resolved in PWGmc, means our pipeline is forced to pick one allomorph
per form. For most forms this works (the OE outcome discriminates), but
for forms where both *-j- and *-ij- would yield the same OE result, the
choice is underdetermined — precisely the situation R/T warn about.

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

All sources agree that the trigger must be a back vowel, though they
formulate this differently. The real interest lies in the boundary cases:
what counts as "back" when various sound changes have intervened between
the original vowel and the stage at which restoration applies?

**R/T (2014), §6.3.1 (pp.204–208):** R/T provide the most extensive
exemplification. Their account establishes the rule by demonstration
rather than formulaic statement, listing over fifty Class II weak verbs
(*karōną > carian, *labōną > laþian, *wakōjan > wacian, *hatōjan >
hatian, *baþōną > baþian) where the back suffix vowel *ō/*a triggered
restoration. Then nominals with *-u- or *-ō-suffixes: *nakwadaz > nacod,
*nabulō > nafola, *habukaz > hafoc, *sadulaz > sadol. Then n-stems
whose oblique endings contained *-a-/*-ō-: *askōn- > ascan, *maþō >
maþa, *draka > draca. The crucial negative evidence is the hagatussi
passage (p.208): "the unstressed *æ of the second syllable must have
remained front, since otherwise we would not expect the stressed vowel to
have remained front and the intervening *g to have been palatalized."
This proves that unstressed *æ (from AFB) did NOT trigger restoration.

§6.3.2 (p.199) gives the paradigm that clinches the argument. R/T set out
the development of *dagaz step by step:

| | nom.sg. | gen.sg. | dat.sg. | nom.pl. | dat.pl. |
|---|---|---|---|---|---|
| PGmc | *dagaz | *dagas | *dagē | *dagōs | *dagumaz |
| post-AFB | *dægæz | *dægæs | *dæge | *dægōs | *dægumæz |
| post-restoration | dæg | **dæges** | dæge | **dagas** | **dagum** |

Gen.sg. dæges retains *æ because the suffix vowel was also *æ (from AFB
of *-as > *-æs). Nom.pl. dagas has restored *a because the suffix was *-ōs
(> -os), a genuine back vowel. This paradigmatic split is the strongest
evidence that AFB-fronted *æ does not trigger, while original back vowels
do.

**Fulk (2018), §4.13 (p.76):** Fulk calls the process "retraction" rather
than "restoration." His key formulation: "In open syllables it was also
retracted before a back vowel in the following syllable, hence nom. pl.
dagas 'days' (sg. dæg) and dat. pl. māgum 'kinsman' (nom. sg. mǣg),
though ǣ is often found for ā." "Before a back vowel" confirms the same
trigger set as R/T. The parenthetical "(sg. dæg)" implicitly confirms
that the gen.sg. dæges does not undergo retraction. Fulk's caveat "though
ǣ is often found for ā" introduces an additional complication: even where
restoration should apply, some forms show the unretracted variant, perhaps
by analogical spread from forms without back suffixal vowels. Our
pipeline does not model this variation — it applies restoration
categorically.

**Hogg (1992), §3.3.3.1 (pp.104–105):** Hogg's account is the most
theoretically oriented. He describes restoration as a "final adjustment
to the low vowel system": "/æ/, and to a lesser extent /æ:/, were
retracted to /a, a:/ when a back vowel was present in the following
syllable." He then draws out the systemic consequence: "The effect of
the change would be to harmonise low vowels to a following vowel, so
that any low vowel followed by a back vowel would be back itself, and all
other low vowels (except nasalised ones) would be front." The noun fæt
'vessel' with plural fatu is his paradigm case. Hogg alone raises the
phonemic question: did restoration eliminate the /æ/~/a/ contrast
entirely, reducing it to allophony? He argues not, because "largely
because of later morphologically motivated changes, affecting alternations
of the type fæt ~ fatu, we do find in Old English minimal pairs such as
fare 'journey' dat.sg.masc. vs. fare 'journey' dat.sg.fem." But he
concedes "the case for therefore assuming a phonemic contrast between /æ/
and /a/ is not unassailable."

**Kaluza (1900–01), §57 (pp.98–99):** Kaluza's formulation is the most
direct: "Urg. a = ae. a in offener Silbe vor dunklem Vokal der folgenden
Silbe" ('PGmc *a = OE a in open syllable before a dark vowel of the
following syllable'). His examples (dagas, fatu, gladu, faran, grafan)
all have back suffixal vowels. But Kaluza adds a critical observation in
rule (b): "Urg. a bleibt auch unverändert, wenn der dunkle Vokal der
folgenden Silbe durch Vokaldissimilation...in einen hellen übergegangen
ist" ('PGmc *a also remains unchanged when the dark vowel of the
following syllable has become a light one through vowel dissimilation').
His examples: hafela (*hafulā-), gaderian (*gadurōjan), macian
(*makōjan). Here the suffix vowel was originally back (*u, *ō) and was
later fronted by dissimilation — but restoration had already applied, so
the result stands. This is chronologically distinct from the AFB case: AFB
fronting of *a → *æ happens BEFORE restoration (so restoration sees *æ
and does not fire), while dissimilation of *ō > *e happens AFTER
restoration (so restoration has already fired and the later fronting is
irrelevant).

**Luick (1914–40), §161 (pp.152–153):** Luick's formulation is: "Urengl. æ
wurde gemeinenglisch vor einem dunklen Folgevokal zu a, ohne daß der
dazwischen stehende Konsonant von Belang gewesen wäre" ('Pre-OE æ
became a before a dark following vowel, without the intervening consonant
being relevant'). He then distinguishes four positional environments:
(1) "am deutlichsten in offener Silbe" ('most clearly in open syllable'):
hara, faran, nacod, macian, dagas, fatu; (2) before long consonants;
(3) before s+C and f+C; (4) "nur in wenigen Resten" ('only in a few
relics') before obstruent + liquid: appla, accras. His open-syllable
examples match Kaluza's and R/T's.

**Campbell (1962), §§157–160:** Campbell provides the most detailed
positional analysis of A-restoration. §157 opens: "One of the most obvious
peculiarities of the OE phonological system is that æ and a interchange,
the former standing in closed syllables, and in open syllables when a front
vowel (e, in early texts sometimes written i or æ) follows, the latter in
open syllables when a back vowel (a, o, u) follows." His paradigm case is
*dæg*: "dæg, dæges, dæge, dagas, daga, dagum." §157 establishes the logic
of restoration (as opposed to fronting-avoidance): "This interchange is
clearly due to the restoration of a before a back vowel, for breaking can
hardly be regarded otherwise than as a change affecting front vowels, and
from this it follows that OE slēan is developed from *slæxan. Now it is
hardly conceivable that when Prim. Gmc. *slaxan- was at the stage *slexan,
Prim. Gmc. *draʒan- would not be at the stage *dræʒan; from which it
follows that OE dragan has restored a in its first syllable by later change."
§158 gives positional data: "The restoration of a is common before all single
consonants and geminates," then: "a is commonly restored also before groups
consisting of f or s followed by another consonant, e.g. wascan wash, asce
ash...Before other groups, a is not restored except for a few instances
before consonant plus liquid: W-S appla, apla apples, watrode he watered,
Angl. (Rit., Ru.) accras, acras fields, beside æplas, ǣcras, weterode, and
always sægdon, hæfdon, fædras, næġlas, &c." Campbell thus agrees with Luick
on the gradient application before clusters, but adds a telling observation:
"Yet it need not be doubted that a was originally widely restored before
groups, and that it was subsequently removed by the analogy of forms in which
a front vowel followed. This is reflected by some doublets, e.g. gæfel, gafol
tribute, hæġel, hagol hail, fægen, fagen glad." §159 adds: "The restoration
of a was frequently due to a back vowel which subsequently became a front
vowel or was lost, e.g. gaderian gather, staþelian found (cf. geador, staþol),
and weak verbs in -i- (< -ōi-), laþian, macian, hnappian, &c." This is the
same chronological point as Kaluza's — restoration preceded dissimilation.
§160 gives the morphological categories: a-nouns (dæg/dagas), adjectives
(which "generally level a into all open syllables"), ō-nouns (rare: sacu,
inflected sæce or (anal.) sace), and Class VI strong verbs (which "have in
W-S a strong tendency to extend the a of the inf. and pres. indic. pl. to
forms where -e follows").

**Where the scholars disagree:**

The sources are unanimous that the trigger must be a back vowel. They
disagree on three subsidiary points:

1. **Categoricity:** Fulk's "though ǣ is often found for ā" suggests
   restoration was not fully regular. R/T's extensive paradigmatic data
   implies it was. Hogg raises the phonemic question without resolving it.
   For our FST, we treat restoration as exceptionless (which matches the
   standard paradigms) but acknowledge that dialectal and analogical
   variation exists.

2. **Chronological ordering with dissimilation:** Kaluza alone makes the
   ordering explicit: restoration precedes vowel dissimilation, so forms
   like hafela retain their restored *a even after the suffix is fronted.
   R/T show this implicitly through their paradigm data but do not state
   the ordering as a principle. For our FST, this means restoration must
   be ordered before any dissimilation rules (which we do not yet model).

3. **Scope of "back vowel":** R/T include only *o, *u, *ō, *ū. Fulk
   says "back vowel" without specifying. Kaluza says "dunklem Vokal"
   ('dark vowel'), which in 1900 usage covers *a, *o, *u and their long
   counterparts — but his examples all have *o or *u, never *a. The
   question of whether *a counts as a trigger is moot for our finding
   (since AFB has already fronted *a → *æ by the time restoration
   applies), but it could matter for forms with protected *a (e.g. after
   nasals).

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

---

## 6. PGmc stem-class disambiguation via OE phonology: \*kraft- and \*stab-

**Date discovered:** Session (2026-03-09g)

**Background:** Two TSV entries (cræft, stæf) had PGmc proto-forms ending in
\*-iz (i-stem nominative singular), which our pipeline processed with i-umlaut
to yield \*creft and \*stefe. But the attested OE forms are **cræft** and
**stæf** — with æ, not e — indicating that i-umlaut did not apply.

**What the FST implementation revealed:** The discrepancy forced us to survey
the etymological literature, which revealed that **modern PGmc dictionaries
disagree on the stem class** of these lexemes:

| Lexeme | Kroonen (2013) | Orel (2003) | Kluge-Seebold (25th) |
|--------|----------------|-------------|----------------------|
| \*kraft- | \*kraftu- (tu-stem) | \*kraftiz ~ \*kraftuz | \*krafti- (i-stem) |
| \*stab- | \*staba- (a-stem) | \*stabiz ~ \*stabaz | \*stabi-/a- |

This is not a case of one dictionary being "wrong" — the comparative evidence
is genuinely ambiguous, and different scholars weight the daughter-language
reflexes differently.

**The observation:** The OE phonological evidence disambiguates the input
form for English, regardless of what the "true" PGmc reconstruction is:

1. **i-stem \*-iz** → triggers i-umlaut (æ → e) → predicts OE \*creft, \*stefe
2. **u-stem \*-uz** → triggers a-restoration (æ → a before back vowel) → predicts OE \*craft
3. **a-stem \*-ăz** → no trigger (suffix vowel is front after AFB, not high) → predicts OE **cræft**, **stæf** ✅

The a-stem analysis is the only one that correctly predicts the attested OE
forms. The key insight is that after Anglo-Frisian Brightening fronts the
suffix vowel (\*ă → \*æ), this front vowel does not trigger a-restoration
(which requires a back vowel) and does not trigger i-umlaut (which requires
high \*i or \*j).

**Evidence from the daughter languages:**

The disagreement among etymological dictionaries reflects genuine ambiguity
in the comparative record:

- **ON krafptr** has u-umlaut (a → ǫ), suggesting the stem vowel was followed
  by \*u when u-umlaut applied → supports u-stem
- **OHG kraft** (fem., no umlaut) is compatible with a-stem, i-stem, or u-stem
- **Gothic** lacks both words, removing the most conservative witness
- **OE cræft, stæf** with æ (not e) are incompatible with i-stem; compatible
  with a-stem or u-stem (if \*u was lost before a-restoration)

Kluge-Seebold explicitly notes for \*kraft-: "Spuren von u-Flexion (anord.
krǫptr m.) weisen wohl auf einen parallelen maskulinen u-Stamm" — acknowledging
that both i-stem and u-stem morphology are attested for this word.

**What the sources say:**

- **Kroonen (2013), p.307:** Reconstructs \*kraftu- as a "tu-stem" (a subtype
  of u-stem), citing ON krafptr, OE craft, OHG kraft. Notes it is "possibly
  related to \*krabēn-".
- **Kroonen (2013), p.469:** Reconstructs \*staba- as an a-stem, citing Gothic
  stabeis pl., ON stafr, OE stæf. The form is given as \*staba-, not \*stabi-.
- **Orel (2003), p.220:** Lists "\*kraftiz ~ \*kraftuz" with both alternatives.
  Notes "OE cræft 'power, might, art, skill'".
- **Orel (2003), p.378:** Lists "\*stabiz ~ \*stabaz" with both alternatives.
  Notes "OE stæf 'staff, stick, character'".
- **Kluge-Seebold (25th), s.v. Kraft:** "Aus g. \*krafti- f. 'Macht, Kraft'...
  Spuren von u-Flexion (anord. krǫptr m.) weisen wohl auf einen parallelen
  maskulinen u-Stamm."
- **Kluge-Seebold (25th), s.v. Stab:** "Aus g. \*stabi-/a- m. 'Stab'" —
  explicitly marking uncertainty between i-stem and a-stem.
- **Campbell (1959), §133:** Lists "cræft skill" as an example of OE æ from
  PGmc \*a. §160 shows "cræftas powers" in the plural.
- **Luick (1914–40), p.176:** Lists "stæf 'Stab', cræft 'Kraft'" as examples
  of retained æ.
- **Fulk (2018), §4.7 n.12:** Cites MHG paradigmatic alternation "kraft beside
  krefte", showing umlaut variation within the MHG paradigm.

**Significance for the project:** This case demonstrates a powerful application
of the FST methodology: **using daughter-language phonology to adjudicate
between competing PGmc reconstructions**. When etymological dictionaries
disagree on the proto-form, the FST allows us to test each hypothesis against
the attested outcome. Only the form that produces correct output through
regular sound changes is viable as the input for that daughter language.

This is similar to the stefn/stemn case (§5), but with a different payoff.
In that case, the disagreement concerned a single word with a disputed
consonant cluster. Here, the disagreement concerns the **nominal stem class**
— a morphological category with systematic phonological consequences (i-umlaut,
a-restoration, vowel harmony). The FST approach can potentially disambiguate
stem classes across the lexicon, not just for individual words.

**Methodological note:** Our resolution — using a-stem \*-ăz forms — does not
claim to have solved the PGmc reconstruction. It claims only that for the
pre-OE input, the form must have lacked both an i-umlaut trigger and a back
vowel for a-restoration. This could reflect:
- An original a-stem inherited into pre-OE
- A u-stem with early loss of \*u before a-restoration applied
- An i-stem with early loss of \*i before i-umlaut applied

The OE evidence cannot distinguish these scenarios. But the FST requires us to
make this explicit, rather than blurring the distinction with a notation like
"\*krafti-/u-" that leaves the phonological prediction undefined.

**Full analysis:** See DEV_NOTES.md, "PGmc stem-class disagreements: \*kraft-
and \*stab-".


---

## 7. NWGmc *i > *e lowering: consonant-conditioned blocking and rule ordering

**Date discovered:** 2025-03-09

**Background:** NWGmc \*i lowered to \*e before non-high vowels in the following
syllable, parallel to the well-established \*u > \*o lowering (a-umlaut).
However, the \*i lowering is notoriously sporadic — Campbell (OEG §114) notes
that "in OE this change is shown **only by** the common Gmc. words *nest* and
*wer*... and by *spec* bacon beside *spic*." This contrasts sharply with
u-lowering, which is nearly regular. The sporadic character has led scholars
to either dismiss i-lowering as "not a real sound change" (Lloyd 1966) or to
treat it as pre-PGmc (Hogg 1992).

**The problem:** Our FST needed to model \*nistą → OE *nest* (with \*i > \*e),
while correctly preserving \*i in forms like \*fiskăz → *fisċ*, \*likkōjăną →
*liccian*, \*librō → *lifer*. An unconditional i-lowering rule caused 9
regressions.

**What we discovered:**

1. **Consonant conditioning via place features:** Following Howell & Salmons
   (1997), we conditioned i-lowering to apply only when ALL intervening
   consonants are coronals. Velars and labials block the change via place
   feature sharing (dorsals and labials share place features with high back
   vowels and resist harmony processes). This explains:
   - \*nest (coronal cluster \*-st-): lowering ✓
   - \*fisċ (velar \*-sk-): blocking ✓
   - \*liccian (velar geminate \*-kk-): blocking ✓
   - \*lifer (labial \*-br-): blocking ✓

2. **Rule ordering matters (potentially novel):** When testing \*widuwōn
   →widow, we discovered a feeding interaction:
   - If u-lowering runs first: \*widuwōn → \*widowōn, then i-lowering sees
     \*i_d_o_ (coronal + non-high) → lowering applies → \**wedowe* (incorrect)
   - If i-lowering runs first: \*widuwōn, i-lowering sees \*i_d_u_ (coronal +
     HIGH vowel) → lowering blocked → \*widuwōn → u-lowering → \*widowōn (correct
     for the first syllable)

   By ordering i-lowering **before** u-lowering, the rule correctly sees the
   original high \*u which prevents the lowering context from being satisfied.

**What the literature says:**

- **Lloyd (1966):** Argues that "the so-called a-umlaut of i in Proto-Germanic
  did not exist" and that sporadic \*e forms result from "systemic analogy"
  due to the partial overlap of /i/ and /e/ phonemes after the IE \*e > Gmc
  \*i split. Lloyd notes that Class I strong verb past participles (OHG
  *giritan*) retain \*i, which would be unexplainable if lowering were regular.

- **Cercignani (1980):** Explains the scarcity of i-lowering as "merger
  avoidance": "the assimilation exerted by \*[-a] on \*/i/—being less powerful
  than that exerted by \*[-i] on \*/e/—was resisted, with varying results,
  **in order to avoid a merger of \*/i/ with \*/e/**." Notes that consonantal
  environment affected outcomes in Old Icelandic (retention after \*k, \*g).

- **Howell & Salmons (1997):** Developed a general theory of umlaut blocking
  based on place feature sharing: "the more place features the target shares
  with intervening consonants, the more likely umlaut failure becomes." Their
  hierarchy: dorsals (most blocking) > labials > coronals (most transparent).

- **Stiles (2012):** Uses \*nest < \*nistaz as an example of a-umlaut
  phonologization, noting that Older Runic forms show the change with
  conditioning factors still intact.

**The novel contribution:**

Our analysis yielded two potentially novel findings:

1. **Onset-velar blocking in OE (extension of Cercignani 1980):** Cercignani
   notes that in Old Icelandic, \*i was retained "after \*/k/ and \*/g/" (citing
   Noreen and Gutenbrunner). However, he explicitly states this "was by no
   means true of at least certain types of Old High German" (OHG shows skif/skef,
   ginen/genen doublets). Our OE data suggests that onset velars also blocked
   i-lowering in Old English:
   - \*xlidą → OE *hlid* (not \**hled*) — onset \*x blocks
   - \*furxtiθō → OE *fyrhtu* (not \**forhteþu*) — earlier \*x blocks
   
   If correct, this makes OE pattern with OIc. (onset blocking) rather than OHG
   (no onset blocking). This is phonologically coherent: OE and OIc. share
   northern/Ingvaeonic features. This extension is NOT explicitly stated in the
   literature and represents a potentially novel observation.

2. **Rule ordering (i-lowering before u-lowering):** None of the sources
   consulted discuss the ordering of i-lowering relative to u-lowering. Our
   finding shows:
   - i-lowering and u-lowering are in a **counter-feeding** relationship
   - i-lowering must apply **before** u-lowering to produce correct outputs
   - This ordering is required because u-lowering creates new \*o vowels that
     would otherwise feed i-lowering in unintended environments

   If this ordering constraint is not documented in the literature, it represents
   a methodological contribution from the FST implementation.

**Implementation:** The rule is implemented in `server/fsts/germanic.txt` with:
- `EnglishStarCoronal`: coronals transparent to lowering
- `EnglishStarVelarOrLabial`: velars and labials that block lowering
- `EnglishStarNonVelar`: used for onset-velar blocking
- `NWGmcILowering`: applies only when (a) no velar in onset, (b) only coronals
  in coda
- Pipeline ordering: `NWGmcILowering` before `NWGmcULowering`

**Results (2026-03-09):** Implementing onset-velar blocking yielded +2 matches
(297 → 299), fixing *lid* (\*xlidą → hlid) and *fright* (\*furxtiθō → fyrhtu)
without regressions. This confirms the onset-velar blocking hypothesis.

**Full analysis:** See DEV_NOTES.md, "PGmc \*i > WGmc \*e Lowering: The Case
of nest".

### Expert consultation (Stefan Schuhmacher, Vienna, 2026-03-20)

We consulted Prof. Stefan Schuhmacher on i-lowering. His response clarifies
the status of the change and questions our use of Cercignani:

**On i-lowering as a "tendency":** "As for the expected parallel lowering of
\*i > e, this is really no more than a 'tendency' (my apologies for the vague
term). That is, *nest* and *wer* 'man' are the usual suspects but **no one has
been able to mention a substantial number of other candidates** for such
lowering. Such lowering simply seems not to happen across the board.
Unpleasant as it is, this is the way it is."

**On Cercignani (1980):** Schuhmacher's assessment of the article we cited is
blunt: "I have also looked at Cercignani's article... To put it nicely, that
article is **unhelpful. I can make neither head nor tail of it.**" He questions
our interpretation: "Does he actually say that 'in Old Icelandic, onset velars
(\*/k/, /g/) blocked the lowering of \*i'??? And if so, how does he explain the
lack of lowering of \*i in words other than 'nest' and 'man'? I don't
understand where that idea came from, and whether it is an idea of Cercignani's
or a (possibly wrong) conclusion of yours."

**On chronology:** "Now since the very 'sporadic' lowering of \*i certainly is
not a sound law, it is **impossible to find any chronological relationship**
with the almost exceptionless lowering of \*u."

**Implications for our implementation:** Our onset-velar blocking rule produced
correct empirical results (+2 matches, no regressions), but we should:
1. Re-examine the Cercignani attribution to ensure it accurately represents his claims
2. Consider whether our rule is an independent observation rather than a citation of Cercignani
3. Be cautious about treating sporadic i-lowering as a formalizable sound law

**Re-examination of Cercignani attribution (2026-03-20):**

In response to Schuhmacher's question, we re-read Cercignani 1980, p. 289–292.
Cercignani does explicitly state (lines 289–291):

> "In Old Icelandic, PGmc. \*/i/ was apparently retained after \*/k/ and \*/g/;
> but this was by no means true of at least certain types of Old High German."

So yes, Cercignani **does** attribute onset-velar blocking to Old Icelandic—citing
Noreen §60 and Gutenbrunner §26.1.2. But he explicitly denies this pattern for OHG,
which shows doublets (skif/skef, ginen/genen).

**Crucial clarification:** Cercignani says nothing about Old English. Our extension
of onset-velar blocking to OE is **our own hypothesis**, supported by OE data
(hlid, fyrhtu) but not stated anywhere in Cercignani. The phrasing "extension of
Cercignani 1980" in our earlier notes was correct but potentially misleading—it
should be understood as "we extend a pattern Cercignani observed for OIc. to OE"
rather than "Cercignani claims this for OE."

Whether Schuhmacher's puzzlement concerns Cercignani's claim for OIc. (which is
explicit in the text) or our extension to OE (which he correctly identifies as
our own inference) is unclear. In either case, our documentation now explicitly
separates:
- What Cercignani says (OIc. onset-velar blocking, citing Noreen and Gutenbrunner)
- What we hypothesize (that OE patterns with OIc., not OHG)

The rule ordering (i-lowering before u-lowering) remains necessary for correct
outputs, regardless of how i-lowering is characterized theoretically.

---

## 8. PGmc \*þistilaz 'thistle': unresolved \*e/\*i reconstruction problem

**Date discovered:** 2026-03-18

**The puzzle:**

All Germanic daughter languages attest 'thistle' with root vowel \*i:

| Language | Form | Root vowel |
|----------|------|------------|
| OE | þistel | i |
| ON | þistill | i |
| OHG | distil(a) | i |
| OS | thistil | i |
| Dutch | distel | i |
| German | Distel | i |

Yet major etymological dictionaries disagree on the Proto-Germanic reconstruction:

- **Orel (2003):** Reconstructs \*þe(x)stilaz with root **\*e**
- **Kluge-Seebold (25th ed.):** Reconstructs \*þistila- with root **\*i**

**The phonological problem:**

If Orel's \*þe(x)stilaz with \*e is correct, we need to explain how \*e became \*i in **all** daughter languages. The standard accounts invoke:

1. **PGmc raising** (Campbell §112, Luick §§71-76): \*e > \*i before \*i in following syllable
2. **OE i-umlaut**: \*e > \*i before \*-il- suffix (Fulk §5.5)

But there are problems:

- **ON þistill** shows \*i yet lacks an i-umlaut environment (ON preserves \*-ill, doesn't trigger umlaut)
- If PGmc raising applied "with practically perfect regularity" (Campbell), why does Orel still reconstruct \*e?
- The "raising" solution assumes PIE \*-elo- > PGmc \*-ila-, but Cercignani (1979), following Krahe-Meid, argues some \*-il- words may have **original PIE \*-ilo-**

**Competing IE etymologies:**

The root itself is disputed:

| Etymology | IE Root | Proposed by |
|-----------|---------|-------------|
| "weave/fashion" | \*tek̂s- | Orel (via \*þexsanan, Lat. textilis) |
| "prick" | \*(s)teig- | Kluge-Seebold, Pokorny |

If from \*tek̂s-, root \*e is expected. If from \*(s)teig-, the normal outcome would be PGmc \*ī (from IE \*ei), not short \*i — requiring special pleading.

**The unresolved question:**

**We do not understand how scholars who reconstruct \*e in the root vowel (Orel) explain the phonology.** If the reconstruction is \*þe(x)stilaz:

1. Why do ALL daughter languages show \*i, including ON which lacks the umlaut trigger?
2. Was PGmc raising applied? If so, why isn't the surface form \*þistilaz given as the reconstruction?
3. If raising was pre-PGmc, what is the evidence for underlying \*e?
4. Did Orel intend \*þe(x)stilaz as a deep/underlying form, with surface \*þistilaz?

No source consulted explains this discrepancy.

**Sources consulted:**

- Orel (2003), *Handbook of Germanic Etymology*, p. 419
- Kluge-Seebold (25th ed.), s.v. "Distel"
- Campbell, *OEG*, §§111-112
- Luick, *Historische Grammatik*, §§71-76
- Fulk (2018), *Comparative Grammar*, §§4.4, 5.5
- Cercignani (1979), "Proto-Germanic */i/ and */e/ Revisited," JEGP 78:72-82

**Sources needed (not in local collection):**

- de Vries, *Altnordisches etymologisches Wörterbuch* (ANEW) — s.v. þistill
- Pokorny IEW — full entries for \*tek̂s- and \*(s)teig-
- EWA Band II — s.v. distil
- Holthausen, *Altenglisches etymologisches Wörterbuch* — s.v. þistel

**FST status:**

```
$ echo 'θestilăz' | flookup -i old_english.bin
θestilăz    þestel  ✗

$ echo 'θistilăz' | flookup -i old_english.bin
θistilăz    þistel  ✓
```

The FST correctly handles \*θistilăz → þistel. **TSV updated 2026-03-18:** Changed PROTOFORM to \*θistilăz (adopting Kluge-Seebold). The scholarly question about Orel's \*e reconstruction remains open.

**Full analysis:** See DEV_NOTES.md, "OE þistel 'thistle': I-Umlaut Not Preserved (2026-03-18)".


---

## 9. OE wīþiġ 'withy': ja-stem vs. -ig suffix problem

**Date discovered:** 2026-03-20

**The puzzle:**

OE `wīþiġ` 'withy, willow' (TSV row 2296) is reconstructed as a ja-stem:

| Source | Reconstruction | Notes |
|--------|----------------|-------|
| Wiktionary | \*wīþijaz | Standard ja-stem masculine |
| Kluge-Seebold | \*wīþja/ō | ja/jō-stem (masc/fem variants) |

Yet the attested OE form `wīþig` preserves the `-ig` suffix, which should NOT survive from a heavy monosyllabic ja-stem.

**The phonological problem (per Adamczyk 2001):**

According to Adamczyk (2001), "Old English reflexes of Sievers' Law," heavy monosyllabic ja-stems yield OE `-e` in the nom.sg., NOT `-ig`:

| Proto-form | OE form | Gloss |
|------------|---------|-------|
| \*andijaz | **ende** | 'end' |
| \*witijam | **wite** | 'punishment' |
| \*linþijaz | **līðe** | 'gentle' |

The derivation: \*-ijaz → \*-ij (z-loss) → \*-ii (j-vocalization) → \*-ī (contraction) → **-e** (unstressed reduction)

Therefore, \*wīþijaz should yield OE \*wīþe or simply \*wīþ — NOT wīþig.

**FST behavior:**

```
$ echo 'wīθijăz' | flookup -i old_english.bin
wīθijăz    wīþ
```

The FST produces `wīþ`, which is phonologically correct per Adamczyk's analysis:
1. SieversLawSyncope deletes \*i before \*j after consonant: \*θ\*i\*j → \*θ\*j
2. OEJLossAfterHeavy deletes \*j after heavy syllable: \*wī\*θ\*j → \*wī\*θ

**Where does OE -ig come from?**

Campbell §376 reveals that OE `-ig` has TWO distinct sources:

1. **From ja-stem \*-ijaz** (via Sievers' Law alternation) — yields `-e` after heavy stems
2. **From \*-ag-/\*-ig-** (adjective-forming suffix) — raises to `-ig` before palatal g

If `wīþig` has the second suffix (\*-igaz or \*-agaz), the `-ig` would be expected. But **no etymological source reconstructs** \*wīþigaz or \*wīþagaz.

**Possible explanations (none confirmed):**

1. **Different suffix:** The word was formed with \*-igaz (productive adjective suffix), not ja-stem \*-ijaz
2. **Analogical restoration:** The highly productive OE `-ig` suffix was restored after regular phonological loss
3. **Late formation:** Post-PGmc derivative \*wīþ- + OE `-ig`
4. **K-S's speculative \*wīþw- stem:** Based on non-Gmc cognates (Gk ἰτέα, OPruss witwan, Skt vetasá-)

**The unresolved question:**

**No authoritative source provides a proto-form that yields OE `wīþig` through regular sound change.** The FST's output `wīþ` is phonologically correct for any ja-stem reconstruction. The attested form requires either:
- An undocumented proto-form (\*wīþigaz?)
- Analogy to the productive `-ig` suffix class
- A late derivation post-dating the ja-stem phonology

**Sources consulted:**

- Campbell (OEG) §576 (ja-nouns), §376 (-ig suffix)
- Kluge-Seebold (25th ed.) s.v. "Weide 1"
- Kroonen (2013) — no entry for this lexeme
- R/T vol.2 p.70 (ja-stem overview)
- Bülbring §327
- Adamczyk (2001) "Old English reflexes of Sievers' Law," Studia Anglica Posnaniensia
- Erdmann (1972) "Suffixal j in Germanic," Language 48
- Pierce (1999, 2003, 2006) — Sievers' Law studies

**Sources needed (not in local collection):**

- de Vries ANEW s.v. víðir
- Holthausen AEW s.v. wīþig
- OED "withy" (full etymology)
- Any specialist study of OE -ig adjectives

**TSV status:** Marked as Known Exception (FST correct but no proto yields attested form).

**Full analysis:** See DEV_NOTES.md, "OE wīþiġ 'withy': ja-stem Adjective vs Sievers' Law Syncope (2026-03-19)".

**Full analysis:** See DEV_NOTES.md, "OE þistel 'thistle': I-Umlaut Not Preserved (2026-03-18)".

---

### Resolution (DEV_NOTES §17.10.35, 2026-04-23)

**The puzzle is solved.** "Possible explanation 1" above (suffix
`*-igaz`/`*-agaz` rather than ja-stem `*-ijaz`) turns out to be
correct, and the etymological source is **Campbell §275(7) and §376
itself** — already cited in the original section but its implications
for *wīþiġ* not followed through. Campbell explicitly groups *wiðig*
with *hunig*, *bodig*, *hālig* as derivatives in OE `-ig` < Prim. OE
`-æg` < PGmc `*-ag-` (short *a). The structurally exact PGmc parent
is `*wīþagą` (neut. *-agą), morphologically parallel to `*xúnagą` →
`hunig` (TSV row 2079, which works in the FST without modification).

**End-to-end FST verification:**

```
$ echo wīθagą | flookup -i old_english.bin
wīθagą  wīþiġ
```

Exact match to the attested OE target. The lautgesetzlich chain is:

  *wīθ-agą → (a-umlaut leaves long *ī untouched: only *u/*i affected)
   → *wīþ-agą → (unstr. *a > *e) → *wīþ-egą →
   (Campbell §376 *e > *i / _g) → *wīþ-igą → (apocope of nasal
   vowel; palatalization of *g before *i) → wīþ-iġ ✓

**Why this is a "really useful" finding for the project**:

The Wiktionary `*wīþijaz` and Kluge-Seebold `*wīþja-/ō-` reconstructions
that were the starting point of the puzzle are **morphologically
inconsistent with the OE form they themselves cite**. A heavy-stem
masc. ja-stem in PGmc regularly yields OE `-e` or `-Ø` (cf. *ende*,
*hierde*, *here*, *wite*, *līðe* — exactly the parallels this
section's table at the top lists). The FST output `wīþ` from
`*wīþijaz` is the *correct* lautgesetzlich heavy-ja-stem outcome.
Both reference works (and Wiktionary which follows Kluge) silently
elide this inconsistency: they give a cognate-set headword that fits
the Continental cognates (OHG *wīda* fem. ō-stem, ON *víðir* m.
ja-stem) and tack the OE form on without checking whether the Old
English suffix `-ig` is morphologically derivable from the
reconstructed stem.

**The FST surfaced this elision automatically.** Running the
reconstructed PROTOFORM through the compiled grammar produced a
philologically defensible output (`wīþ`, the regular ja-stem outcome)
that did not match the attested OE form — exposing that the
Wiktionary/Kluge reconstruction cannot derive *wīþiġ* without invoking
analogy. Switching to Campbell's `*-ag-` derivational analysis (which
Campbell himself explicitly classifies *wiðig* under) yields the
attested form by regular sound change end-to-end. This is a clean
example of the FST functioning as a Neogrammarian audit tool: it
mechanically separates "this reconstruction yields the attested form
by regular sound change" from "this reconstruction is asserted to be
the source of the attested form, but cannot derive it without
analogy."

**Updated TSV status (2026-04-23)**: PROTOFORM changed from
`*wīθijaz` to `*wīθagą`; row matches under the Campbell §275(7)/§376
suffix etymology. Sections of the standard etymological literature
(Wiktionary headword, Kluge-Seebold s.v. Weide¹) that retain the
`*-ja-` reconstruction for the OE form should be regarded as
inheriting an unverified analogy.

# Research memorandum — cycle 9 (correction of cycle 8)

Branch `research/hay-article`. This memorandum identifies the
source-critical errors of cycle 8, their consequences, and the corrected
historical argument. It supersedes `RESEARCH_MEMO_CYCLE8.md` wherever the
two conflict. All page references were re-verified against the held
full-text sources during this cycle.

## 1. The central error

Cycle 8 claimed that loss of non-initial \*w before unstressed \*i "has
no support in the historical grammars" and recommended withdrawing the
frozen production definition `OEWLossBeforeI`. **This was wrong.** The
claim was formed from Campbell §405 and Hogg §3.19 (w-loss before
\*u/\*ō) and Hogg §§3.17, 7.72 (word-final w-loss) without reading the
section of Ringe & Taylor that treats the change directly:

- **Ringe & Taylor 2014: 257–61 (§6.7.1 "Early changes of front vowels
  and loss of \*w before \*i")**: "After the syncope of \*i in \*-CijV-
  (see 5.1.3) but before the regular syncope of short vowels (see below),
  non-word-initial \*w was regularly lost before fully unstressed \*i"
  (p. 258). The change is dated **after i-umlaut** (clinched by the
  ō-stem transfer of 'ewe', p. 260) and **before general syncope**
  (w-loss bleeds syncope: *gierede*, *gerede*, p. 260).
- **Campbell 1959: §406** ("OE forms often show loss of w before i,
  although w is often analogically restored"), **§237.1.b** (contraction
  after this loss, with the explicit staging "\*kaui- > \*kei- > \*kē-"),
  **pp. 327–8** (the gierwan-class weak verbs), **p. 100** (nī-
  compounds, ēde, strēn, cēð, strēd).
- **Hogg 1992: §5.133** (persistence of the resulting hiatus in the early
  Mercian glossaries: *streide*, and metrically at Beo 2436).

The frozen `OEWLossBeforeI` (`Germanic/fsts/germanic.txt` at SC047 commit
`113101ac`, line 3132: `{*w} -> 0 || EnglishStarVocalic
EnglishStarConsonant* _ [{*i}|{*ī}]`) encodes precisely this change with
precisely these citations; the consonant-skipping environment covers the
gierwan-class (\*gærwiþi > gierþ/gereþ). The cycle-8 recommendation to
eliminate it is **withdrawn**. (Refinement remains possible — the frozen
cascade does not model the subsequent contraction — but the change's
historical basis is secure.)

The simplified cycle-8 experimental rule (`w -> 0 || _ i`, no preceding
vowel requirement, applied without the subsequent contraction) was not an
exact reproduction of the frozen definition and must not be cited as
evidence about it.

## 2. The two purported counterexamples

- ***eowu* 'ewe'.** Not a counterexample. R&T 2014: 259–60 explain its
  retained w by **transfer into the ō-stems before w-loss** (i-stem
  endings began with high front vowels; the ō-stem endings did not), and
  they use exactly this fact to date w-loss after i-umlaut. Cycle 8
  inverted an exception-handling argument into a refutation of the rule
  it supports. The derivative *ēde* 'flock' (< \*awidī, R&T p. 259) shows
  the regular treatment — medial w lost, hiatus contracted to long ē —
  while WS *eowede* is remodelled on *eowu*.
- ***cleweþa* 'itch'.** Not a control. R&T 2014: 260–1 explicitly flag it
  as "an isolated form in which \*w did not drop", attributing it to
  lexical analogy with *clāwan* 'to scratch' or to competition between
  parallel suffix forms. The cycle-8 objection that "no other grammatical
  cell could restore its w" overlooked lexical and derivational analogy —
  the very mechanisms R&T invoke. The regular prediction is \*\*clēþa;
  the attested form is the documented exception.
- ***crāwan* : *crǣwþ*.** Cycle 8 cited this as w-retention before the
  umlaut vowel. Backwards: R&T p. 260 cite the **w-less** 3sg relics
  *gecnēþ* (early WS) and *crēd* (Ru²) as the phonological outcomes;
  *crǣwþ*-type forms have w restored by levelling (Campbell §406: "by
  phonological development beside analogical gecnǣwð ... crǣwþ").

## 3. The positive evidence, classified

Strongest independent controls (vowel quantity/shape not established by
the reconstruction under test):

| Form | Preform | Status |
| --- | --- | --- |
| *sǣ* 'sea' | \*sāwi < \*saiwiz | regular; ambiguous between apocope and contraction (R&T p. 318) |
| *ǣ* 'law' | \*āwi < \*aiwi | regular; same ambiguity |
| ***glī* 'merrymaking'** | \*gliwi | **regular; long vowel provable only by contraction (R&T p. 318); light neuter ja-stem — the closest structural control for 'hay'** |
| *nī-* 'new-' (nīcenned) | \*niwi- | regular; contraction (Campbell p. 100) |
| ***ēde* 'flock'** | \*awidī | **regular; contraction; medial \*awi exactly parallel to 'hay'** |
| *streide/strēdun/strēd* | \*strawidē | regular; ⟨ei⟩ spelling (EpGl/CorpGl) and Beo 2436 scansion show persisting hiatus |
| *gecēd/gecēde* (Ps(A)) | \*gakawiþi/-idē | regular; Campbell §237.1.b gives the staging \*kaui- > \*kei- > \*kē- |
| *pyle* 'pillow' | Lat. pulvinus → \*pylwi | regular; postconsonantal, no hiatus; loanword, fully independent |
| *gierede/gerede* | \*garwidē | regular; bleeds syncope (chronology anchor) |
| *gecnēþ*, *crēd*, *bilēde*, *ǣtīede*, *strēn* | various | regular relics beside analogical restorations |

Affected by analogy: *eowu* (morphological transfer before w-loss),
*cleweþa* (lexical exception), all w-restored verb forms (*crǣwþ*,
*gecnǣwð*, *ǣtīewde*, inflected *gierwan*-forms with w), *glīg*
(re-formation, Campbell §411), WS *eowede*.

The examples with **final \*-wi after a short vowel** are the critical
class for 'hay': *gliwi* > *glī* is the only exact structural parallel
(light ja-stem, short vowel + wi#), and its long vowel "can only" be the
product of contraction (R&T p. 318).

## 4. The corrected derivation of the direct cell (early apocope)

\*hawją > \*hawi (= Goth. *hawi*; cf. OHG *hewi*, "the inherited
nom.-acc. sg.", R&T pp. 53, 173) > AFB \*hæwi (R&T 5.1.2 p. 148) >
i-umlaut \*hewi (R&T 6.6.2; Campbell §579(4) "\*hewi ... would be the
undisturbed development") > **w-loss** \*he.i (R&T 6.7.1, post-umlaut,
pre-syncope) > **contraction** \*hē (R&T 6.9.3 p. 318; long by
contraction, as in *glī*, *ēde*, *gecēd*; the hiatus stage could persist
for some generations — ⟨ei⟩ spellings of the *streide* type).

The cycle-8 reconstruction \*\*hewe is **withdrawn**: the mete-class
treatment of final \*-i presupposes a preceding consonant; w-loss removes
the consonant and feeds contraction instead.

Consequences:

1. **Anglian *hēġ* may continue the inherited direct cell with only the
   analogical restoration of final -ġ from the protected cells** — the
   exact operation attested in *glī* → *glīg* (Campbell §§411, 579(4):
   the attested nom.-acc. sg. forms stand "under influence of the other
   cases"; R&T p. 259 "glī, glīg-"). This is a far smaller analogical
   operation than whole-stem levelling, and Campbell's own framework
   (§§406 + 237.1.b + 579(4)) implies it.
2. **West Saxon is different.** Regular \*hē would remain WS *hē*; the
   attested WS vocalism (*hīeġ*, *hīġ*, *hȳġ* presupposing īe/ī) matches
   the oblique stem (\*hauj- > \*hēaj- > īeġ-). Under early apocope the
   WS direct cell therefore requires stem replacement or import from the
   oblique cases (R&T's ">—" at pp. 173, 246), unless WS *hīeġ* reflects
   the geminate (late-apocope) route. The necessity and scope of analogy
   are **dialect-differentiated**.
3. Under late apocope both WS *hīeġ* and Angl. *hēġ* are regular with no
   analogy (geminate route); Dahl's ungeminated variant yields the
   vocalism regularly but restores final -ġ analogically **by his own
   statement** — it is not analogy-free.
4. The possible histories are therefore: (i) regular survival + -ġ
   restoration (Anglian, early apocope); (ii) whole-stem replacement
   (WS, early apocope); (iii) fully regular (both dialects, late
   apocope); (iv) regular vocalism + -ġ restoration (Dahl, late
   apocope). Different dialects may even instantiate different routes.

## 5. 'Glee' as the key precedent

PWGmc \*gliwi (direct), \*gliwwja- (protected; PNWGmc \*gliwją, ON
*glý*). Direct cell: \*gliwi > \*glii > *glī* regular (R&T pp. 259, 318);
attested *glī*, *glīo-mann*/*glī-mann*. Re-formations: *glīg* with -g
restored from the inflected cases (Campbell §411); *glīow*/*glēo(w)*
re-formed on the protected cells, where "final -ġ should drop (§400)" but
-w- "is usually replaced from the inflected cases" (Campbell §579(4) and
n. 1). 'Glee' therefore supplies a complete precedent for an inherited
ungeminated direct stem that underwent w-loss and later limited
paradigmatic restoration — precisely the Anglian *hēġ* scenario — and for
coexisting re-formed variants. Note the asymmetry with 'hay': beside
*glī*/*glīg* the protected-cell type *glēo(w)* survives, whereas 'hay'
shows no \*hēo(w)-type forms; but 'hue' (*hīew*/*hīw*, no †*hīeg*) shows
the protected type winning in the same class, so both outcomes of the
competition are attested.

## 6. Corrected wider conclusions (superseding cycle 8)

1. **\*\*hewe is withdrawn** as the regular early-apocope outcome; the
   regular outcome is \*hē (via \*he.i).
2. **Model A's \*hei is not historically impossible**: it is the
   documented pre-contraction hiatus stage (Campbell §237.1.b *kei-*;
   spelling ⟨ei⟩, Cp. *streide*). The frozen cascade stops before
   contraction; that is a refinement question, not an error of history.
3. **Whole-stem levelling is not obligatory in every dialect** under
   early apocope: Anglian needs only -ġ restoration; WS needs the larger
   operation (or the geminate route).
4. **Quantity**: every surviving derivation gives the word a long vowel
   in the attested period — the early-apocope route now by contraction
   (\*hē), the geminate and Dahl routes as before (īe/ē). The
   pre-contraction stage had a short first vowel in hiatus; on the
   *streide* evidence such a stage could persist into the earliest
   written period, so quantity claims about the very earliest ⟨hei-⟩
   items (S 1196, if 'hay' at all) must be hedged; the 9th–11th-century
   attestations are long on all accounts.
5. **'Hay' does not weigh like 'bed'.** *bedd*-type geminate direct
   cells are regular only under late apocope and need levelling under
   early apocope; 'hay''s early-apocope cost is the cheap, precedented
   -ġ restoration (Anglian) plus the WS vocalism. The cycle-8 claim that
   'hay' joined *nett/bedd/cynn* with equal weight is withdrawn.
6. **The mene/hay "minimal pair" is withdrawn.** Under early apocope
   *mene* is regular AND Anglian *hēġ* is near-regular; the pair is not
   symmetric and the slogan "exactly one member requires analogy under
   either chronology" is false as stated.
7. **Gothic vs OHG.** Gothic *hawi* is outside West Germanic: it cannot
   be an outcome (anomalous or otherwise) of West Germanic gemination
   and is neutral on the apocope chronology; it attests only the PGmc
   shape. Only OHG *hewi* bears on the WGmc chronology, and its force
   depends on whether it is inherited (R&T) or remodelled — which is the
   question at issue.
8. **Dahl.** On his own representational assumptions (diphthongal parse
   of \*-awj-) his vocalism is regular and his final -ġ analogical; the
   cycle-8 conclusion that described his route as analogy-free is
   corrected. His route presupposes that the direct cell had the
   diphthongal nucleus, i.e. his own parse, not the consonantal parse;
   calling it "a late-apocope variant" presupposed the consonantal
   analysis and is withdrawn as a statement about his framework.
9. **No specifically Kentish paradigmatic history** may be claimed from
   charter compounds (S 1196 *heiweg*) whose lexical identification is
   unresolved.

## 7. Formal verification (cycle 9)

`experiments/direct_cell.foma`, 14/14 PASS
(`bash Germanic/articles/hay/experiments/run_direct_cell.sh`):

- `wloss_contract.bin`: hewi→hē; glī, pyle, ēde, mete, mene controls;
  'ewe' modelled with explicit pre-w-loss ō-stem transfer (ewu→ewu);
  'itch' regular prediction clēþa recorded as R&T's exception.
- `hiatus_stage.bin`: hewi→hei; gliwi→glii (the ⟨ei⟩/⟨ii⟩ stage).
- `g_restore.bin`: hē→hēġ, glī→glīġ (analogical operation, separated).
- `late_b2.bin`: hauj→hīeġ, auju→īeġ (unchanged).

Production cascades, frozen SC047 models and benchmark scores untouched.

## 8. What the article should now say

The question "did 'hay' require analogy under early nasal apocope?" has a
differentiated answer: **some analogy, but less than the conventional
whole-stem levelling account recognizes, and not the same amount in every
dialect.** Anglian *hēġ* is derivable from the inherited direct cell by
regular change plus the glīg-precedented restoration of -ġ; West Saxon
*hīeġ* requires the oblique vocalism; under late apocope no analogy is
needed anywhere (except Dahl's -ġ on his variant). The word's
contribution to the chronology debate is correspondingly modest and
asymmetric: it imposes a real but small analogical cost on early apocope
(concentrated in WS), not the bedd-sized cost cycle 8 claimed, and the
open questions remain the apocope chronology itself, the status of OHG
*hewi*, and the unresolved manuscript identifications.
